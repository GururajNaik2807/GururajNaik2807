#!/usr/bin/env python3
"""
Pulls live numbers from the GitHub API and writes assets/record.svg and assets/languages.svg.
No outside stats service needed.

    python build_assets.py     # first, if you changed anything else
    python update_stats.py     # then this (set GITHUB_TOKEN for a higher rate limit)
"""
import json
import os
import sys
import urllib.request
from collections import Counter

from build_assets import T, common_defs, doc, esc, sharingan, write

USER = "GururajNaik2807"
ACHIEVEMENTS = "Pull Shark · Quickdraw"


def api(path):
    headers = {"User-Agent": "profile-stats", "Accept": "application/vnd.github+json"}
    if os.environ.get("GITHUB_TOKEN"):
        headers["Authorization"] = "Bearer " + os.environ["GITHUB_TOKEN"]
    req = urllib.request.Request("https://api.github.com" + path, headers=headers)
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.load(r)


def record_svg(repos, stars, followers):
    W, H = 900, 205
    stats = [(150, repos, "REPOSITORIES"), (450, stars, "STARS EARNED"), (750, followers, "FOLLOWERS")]
    parts = []
    for i, (x, num, lab) in enumerate(stats):
        parts.append(T(f"""<g class="pop" style="animation-delay:{0.3 + i * 0.35:.2f}s"><text x="{x}" y="100" text-anchor="middle" font-family="$SANS" font-size="74" fill="$WHT" filter="url(#glow)">{num}</text></g>
<text x="{x}" y="134" text-anchor="middle" font-family="$MONO" font-size="13" letter-spacing="4" fill="$RED">{lab}</text>"""))
    body = T(f"""{common_defs('''<style>.pop{animation:pp .7s cubic-bezier(.2,1.6,.4,1) both;transform-box:fill-box;transform-origin:center}
@keyframes pp{from{opacity:0;transform:scale(.3)}to{opacity:1;transform:scale(1)}}</style>''')}
<path d="M0 14 L14 0 H886 L900 14 V191 L886 205 H14 L0 191Z" fill="$BG2" stroke="$RED" stroke-width="2"/>
<g opacity=".1">{sharingan(450, 100, 130, 20, aura=False)}</g>
<path d="M300 40 V150 M600 40 V150" stroke="$DRED" stroke-opacity=".6"/>
{''.join(parts)}
<text x="450" y="182" text-anchor="middle" font-family="$MONO" font-size="12" fill="$GRY">ACHIEVEMENTS · {esc(ACHIEVEMENTS)}</text>""")
    write("record.svg", doc(W, H, body, f"GitHub record: {repos} repositories, {stars} stars earned, {followers} followers"))


def languages_svg(counter):
    top = counter.most_common(6)
    total = sum(counter.values()) or 1
    W = 900
    H = 78 + max(len(top), 1) * 38 + 14
    rows = []
    for i, (lang, n) in enumerate(top):
        pct = n * 100 / total
        y = 82 + i * 38
        bw = max(8, round(pct / 100 * 500, 1))
        rows.append(T(f"""<text x="34" y="{y + 15}" font-family="$MONO" font-size="14" fill="$WHT">{esc(lang)}</text>
<rect x="190" y="{y}" width="500" height="20" fill="#14090e" stroke="$DRED" stroke-opacity=".6"/>
<rect x="190" y="{y}" width="{bw}" height="20" fill="$RED" opacity="{1 - i * 0.12:.2f}"><animate attributeName="width" from="0" to="{bw}" dur="1.1s" begin="{0.3 + i * 0.2:.1f}s" fill="freeze" calcMode="spline" keyTimes="0;1" keySplines=".2 .8 .3 1"/></rect>
<text x="720" y="{y + 15}" font-family="$MONO" font-size="14" fill="$RED">{pct:.0f}%</text>
<text x="780" y="{y + 15}" font-family="$MONO" font-size="12" fill="$GRY">{n} repo{'s' if n != 1 else ''}</text>"""))
    if not top:
        rows.append(T('<text x="34" y="100" font-family="$MONO" font-size="14" fill="$GRY">No language data yet.</text>'))
    body = T(f"""{common_defs()}
<path d="M0 14 L14 0 H886 L900 14 V{H - 14} L886 {H} H14 L0 {H - 14}Z" fill="$BG2" stroke="$RED" stroke-width="2"/>
<text x="34" y="46" font-family="$SANS" font-size="22" letter-spacing="4" fill="$WHT">TOP LANGUAGES</text>
<text x="330" y="45" font-family="$MONO" font-size="12" fill="$GRY">by repository</text>
<path d="M34 58 H866" stroke="$DRED" stroke-opacity=".6"/>
{''.join(rows)}""")
    write("languages.svg", doc(W, H, body, "Top languages by repository"))


def main():
    try:
        user = api(f"/users/{USER}")
        repos = api(f"/users/{USER}/repos?per_page=100&type=owner")
    except Exception as e:
        print("Could not reach the GitHub API:", e)
        print("Leaving the existing assets untouched.")
        sys.exit(0)
    own = [r for r in repos if not r["fork"]]
    stars = sum(r["stargazers_count"] for r in own)
    langs = Counter(r["language"] for r in own if r["language"])
    record_svg(user["public_repos"], stars, user["followers"])
    languages_svg(langs)
    print(f"repos={user['public_repos']} stars={stars} followers={user['followers']} languages={dict(langs)}")


if __name__ == "__main__":
    main()