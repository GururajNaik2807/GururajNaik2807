#!/usr/bin/env python3
"""
Itachi / Akatsuki themed GitHub profile assets.

    python build_assets.py

Optional: put avatar.jpg (or .png) next to this file and re-run.
Your photo goes inside the rotating Sharingan ring in the header.
"""
import base64
import html
import os
import random

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "assets")
os.makedirs(OUT, exist_ok=True)

# ------------------------------------------------------------------ content
NAME = "GURURAJ NAIK"
INITIALS = "GN"
TAGLINE = "FULL-STACK WEB DEVELOPER"
LINES = [
    "> building products end to end",
    "> React • Flask • FastAPI • SQL",
    "> every bug is just a genjutsu",
    "> open to full-stack roles",
]
SECTIONS = [("title-about.svg", "ABOUT", "紹介"), ("title-projects.svg", "PROJECTS", "任務"),
            ("title-skills.svg", "SKILLS", "忍術"), ("title-stats.svg", "RECORD", "記録"),
            ("title-contact.svg", "CONTACT", "連絡")]
FILE_FIELDS = [
    ("NAME", "Gururaj Naik"),
    ("CLASS", "Full-Stack Web Developer"),
    ("ACADEMY", "B.E. Information Technology"),
    ("JUTSU", "React · Flask · FastAPI · SQL"),
    ("STATUS", "Open to Web Developer and Full-Stack roles"),
]
PROJECTS = [
    dict(file="card-bublops.svg", num="01", rank="S", title="BUBLOPS", sub="saas investor analytics",
         lines=["Investor and borrower analytics", "with one-click WhatsApp payment", "nudges and live due dates."],
         tags=["JavaScript", "SQL", "Web APIs"], link="live demo"),
    dict(file="card-codetoanim.svg", num="02", rank="A", title="CODETOANIM", sub="python code visualizer",
         lines=["Animates algorithms step by step", "so learners see every line run,", "with play, pause and step."],
         tags=["Python", "JavaScript", "Canvas"], link="live demo"),
    dict(file="card-skillproof.svg", num="03", rank="A", title="SKILLPROOF", sub="resume verification engine",
         lines=["Checks engineering resumes", "against real GitHub activity:", "repos, commits, tests, deploys."],
         tags=["TypeScript"], link="view repo"),
]
SKILL_GROUPS = [
    ("LANGUAGES", "言語", ["JavaScript (ES6+)", "Python", "SQL", "HTML5", "CSS3"]),
    ("FRONTEND", "表", ["React.js", "Responsive Design", "Reusable UI Components", "DOM Manipulation", "HTML5 Canvas"]),
    ("BACKEND", "裏", ["Flask", "FastAPI", "RESTful APIs", "MySQL", "SQLite", "WhatsApp API Integration"]),
    ("TOOLS", "道具", ["Git", "GitHub", "VS Code", "Web Analytics", "Data Visualization"]),
]

# ------------------------------------------------------------------ style
SANS = "Impact, Haettenschweiler, 'Arial Narrow Bold', 'Arial Black', 'Segoe UI', sans-serif"
MONO = "'Fira Code', 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace"
TOK = {"$BG2": "#0d0a11", "$BG": "#050507", "$DRED": "#8a0b14", "$RED": "#e11d2e",
       "$WHT": "#f3f1f4", "$GRY": "#a5a1ad", "$SANS": SANS, "$MONO": MONO}


def T(s):
    for k in sorted(TOK, key=len, reverse=True):
        s = s.replace(k, TOK[k])
    return s


def esc(s):
    return html.escape(s, quote=False)


def doc(w, h, body, label):
    return (f'<?xml version="1.0" encoding="UTF-8"?>\n'
            f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
            f'viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{esc(label)}">\n'
            f'<title>{esc(label)}</title>\n{body}\n</svg>\n')


def write(name, content):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote assets/" + name)


def common_defs(extra=""):
    return T("""<defs>
<radialGradient id="iris" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#ff5a5f"/><stop offset=".55" stop-color="$RED"/><stop offset="1" stop-color="$DRED"/></radialGradient>
<radialGradient id="aura" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="$RED" stop-opacity=".55"/><stop offset="1" stop-color="$RED" stop-opacity="0"/></radialGradient>
<filter id="glow" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<filter id="soft" x="-50%" y="-80%" width="200%" height="260%"><feGaussianBlur stdDeviation="14"/></filter>
<path id="tomoe" d="M-1 0 C-.8 -1.8 1.8 -2.6 3.6 -1.4 C2 -1.6 1 -.8 1 0 A1 1 0 0 1 -1 0Z"/>
<path id="feather" d="M0 0 C5 -9 7 -22 0 -38 C-7 -22 -5 -9 0 0Z" fill="#0b0b10" stroke="$RED" stroke-opacity=".55" stroke-width=".9"/>
<path id="cloud" d="M0 26 C-14 26 -16 8 -2 5 C0 -10 22 -14 28 -2 C38 -10 56 -2 50 12 C62 14 60 30 46 30 L6 30 C2 30 0 28 0 26Z" fill="$RED" stroke="$WHT" stroke-width="2.2"/>
""" + extra + "</defs>")


def sharingan(cx, cy, r, dur=9, aura=True):
    tom = "".join(
        f'<use xlink:href="#tomoe" transform="rotate({a}) translate(0 {-0.62 * r:.1f}) scale({0.15 * r:.2f})" fill="#080002"/>'
        for a in (0, 120, 240))
    s = f'<g transform="translate({cx} {cy})">'
    if aura:
        s += f'<circle r="{r * 1.7:.0f}" fill="url(#aura)"/>'
    s += f'<circle r="{r}" fill="url(#iris)" stroke="#000" stroke-width="{r * 0.05:.1f}"/>'
    s += f'<circle r="{r * 0.62:.1f}" fill="none" stroke="#1a0004" stroke-width="{r * 0.03:.1f}"/>'
    s += (f'<g><animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="{dur}s" '
          f'repeatCount="indefinite"/>{tom}</g>')
    s += f'<circle r="{r * 0.2:.1f}" fill="#000"/></g>'
    return s


def crow(sc=1.0):
    return T(f"""<g transform="scale({sc})" fill="#08080c" stroke="$RED" stroke-opacity=".45" stroke-width=".8">
<g><animateTransform attributeName="transform" type="rotate" values="-22 0 0;32 0 0;-22 0 0" dur=".6s" repeatCount="indefinite"/><path d="M0 0 C-4 -14 -16 -24 -34 -26 C-26 -18 -22 -10 -20 -2Z"/></g>
<ellipse cx="0" cy="1" rx="10" ry="4.2"/><circle cx="11" cy="-1" r="3.4"/><path d="M13.5 -2.6 L21 0 L13.5 1Z"/><path d="M-9 0 L-22 3 L-9 5.5Z"/>
<circle cx="12" cy="-1.8" r=".9" fill="$RED" stroke="none"/>
<g opacity=".7"><animateTransform attributeName="transform" type="rotate" values="30 0 0;-20 0 0;30 0 0" dur=".6s" repeatCount="indefinite"/><path d="M0 1 C-6 12 -16 20 -30 20 C-22 14 -18 8 -16 2Z"/></g></g>""")


def flying_crow(y, dur, begin, sc, W=1000, bend=-90):
    return (f'<g><animateMotion path="M-90 {y} Q{W / 2:.0f} {y + bend} {W + 90} {y + 25}" dur="{dur}s" begin="{begin}s" '
            f'repeatCount="indefinite" rotate="auto"/>{crow(sc)}</g>')


def feathers(n, W, seed, dur_lo=9, dur_hi=17):
    random.seed(seed)
    out = []
    for _ in range(n):
        x = random.uniform(0, W)
        s = random.uniform(0.5, 1.1)
        d = random.uniform(dur_lo, dur_hi)
        out.append(f'<g transform="translate({x:.0f} -50) scale({s:.2f})"><g class="fe" '
                   f'style="animation-duration:{d:.1f}s;animation-delay:-{random.uniform(0, d):.1f}s"><use xlink:href="#feather"/></g></g>')
    return "".join(out)


def fe_css(H):
    return (".fe{animation-name:fe;animation-timing-function:linear;animation-iteration-count:infinite}"
            "@keyframes fe{0%{transform:translate(0,0) rotate(0deg)}"
            f"25%{{transform:translate(40px,{H * .25:.0f}px) rotate(80deg)}}"
            f"50%{{transform:translate(-30px,{H * .5:.0f}px) rotate(170deg)}}"
            f"75%{{transform:translate(35px,{H * .75:.0f}px) rotate(260deg)}}"
            f"100%{{transform:translate(-10px,{H + 120:.0f}px) rotate(350deg)}}}}")


def arch(x, w, top, bot):
    y1 = top + w * 0.9
    return (f'<path d="M{x} {bot} V{y1:.0f} Q{x} {top} {x + w / 2:.0f} {top} Q{x + w} {top} {x + w} {y1:.0f} V{bot}"/>'
            f'<path d="M{x + w / 2:.0f} {top} V{bot} M{x} {y1 + 60:.0f} H{x + w} M{x} {y1 + 190:.0f} H{x + w}"/>')


def avatar_inner(cx, cy, r):
    for ext, mime in (("jpg", "jpeg"), ("jpeg", "jpeg"), ("png", "png")):
        p = os.path.join(HERE, "avatar." + ext)
        if os.path.exists(p):
            b64 = base64.b64encode(open(p, "rb").read()).decode()
            return (f'<clipPath id="av"><circle cx="{cx}" cy="{cy}" r="{r}"/></clipPath>'
                    f'<image xlink:href="data:image/{mime};base64,{b64}" x="{cx - r}" y="{cy - r}" width="{2 * r}" '
                    f'height="{2 * r}" preserveAspectRatio="xMidYMid slice" clip-path="url(#av)"/>')
    return T(f'<text x="{cx}" y="{cy + 14}" text-anchor="middle" font-family="$SANS" font-size="42" fill="$WHT" '
             f'letter-spacing="2">{INITIALS}</text>')


# ------------------------------------------------------------------ header
def header():
    W, H = 1000, 640
    CW, DT, HOLD, BEGIN = 9.6, 0.07, 1.6, 2.8
    segs = [len(s) * DT + HOLD + 0.35 for s in LINES]
    total = sum(segs)
    clips, texts, carets = [], [], []
    start = 0.0
    for i, (s, seg) in enumerate(zip(LINES, segs)):
        n = len(s)
        tw = round(n * CW, 1)
        x0 = round((W - tw) / 2, 1)
        kt, ws, cx, cw = ["0"], ["0"], [str(x0)], ["0"]
        for j in range(1, n + 1):
            kt.append("%.5f" % ((start + j * DT) / total))
            ws.append(str(round(j * CW, 1)))
            cx.append(str(round(x0 + j * CW, 1)))
            cw.append("2.5")
        kt.append("%.5f" % ((start + n * DT + HOLD) / total))
        ws.append("0")
        cx.append(str(x0))
        cw.append("0")
        KT = ";".join(kt)

        def anim(attr, vals, KT=KT):
            return (f'<animate attributeName="{attr}" dur="{total:.2f}s" begin="{BEGIN}s" repeatCount="indefinite" '
                    f'calcMode="discrete" keyTimes="{KT}" values="{";".join(vals)}"/>')

        clips.append(f'<clipPath id="tc{i}"><rect x="{x0}" y="552" width="0" height="30">{anim("width", ws)}</rect></clipPath>')
        texts.append(T(f'<text x="{x0}" y="572" font-family="$MONO" font-size="16" fill="$GRY" textLength="{tw}" '
                       f'lengthAdjust="spacingAndGlyphs" clip-path="url(#tc{i})" xml:space="preserve">{esc(s)}</text>'))
        carets.append(T(f'<rect x="{x0}" y="556" width="0" height="20" fill="$RED">{anim("x", cx)}{anim("width", cw)}</rect>'))
        start += seg

    clouds = "".join(
        f'<g><ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="$BG" opacity=".88" filter="url(#soft)"/>'
        f'<animateTransform attributeName="transform" type="translate" values="-420 0;1300 0" dur="{d}s" begin="-{b}s" repeatCount="indefinite"/></g>'
        for x, y, rx, ry, d, b in ((0, 250, 170, 22, 36, 8), (0, 330, 210, 26, 48, 30), (0, 215, 120, 16, 30, 3)))
    crows = (flying_crow(210, 15, -2, 1.5) + flying_crow(300, 19, -9, 1.1, bend=60) +
             flying_crow(170, 23, -15, 0.85, bend=-40) + flying_crow(360, 17, -6, 1.25, bend=-70))
    windows = ('<g fill="none" stroke="$RED" stroke-opacity=".2" stroke-width="1.6">'
               + arch(40, 130, 90, 640) + arch(195, 95, 190, 640) + arch(830, 130, 90, 640) + arch(715, 95, 190, 640) + '</g>')

    body = T(f"""
{common_defs(f'''<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#050507"/><stop offset=".55" stop-color="#1b040a"/><stop offset="1" stop-color="#050507"/></linearGradient>
<radialGradient id="moon" cx=".4" cy=".35" r=".7"><stop offset="0" stop-color="#ff6a5c"/><stop offset=".5" stop-color="#d42030"/><stop offset="1" stop-color="#7a0710"/></radialGradient>
<radialGradient id="vig" cx=".5" cy=".45" r=".75"><stop offset=".55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".8"/></radialGradient>
<linearGradient id="bot" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#050507" stop-opacity="0"/><stop offset="1" stop-color="#050507"/></linearGradient>
{''.join(clips)}
<style>{fe_css(H)}
.in{{animation:fin 1.3s 1.5s ease-out both}}
@keyframes fin{{from{{opacity:0}}to{{opacity:1}}}}
.cov{{animation:cov 2.1s ease-out both}}
@keyframes cov{{0%,40%{{opacity:1}}100%{{opacity:0}}}}
.eye{{transform-box:fill-box;transform-origin:center;animation:eye 2.1s ease-in both}}
@keyframes eye{{0%{{transform:scale(.35);opacity:1}}55%{{transform:scale(1.5);opacity:1}}100%{{transform:scale(6);opacity:0}}}}
.g1{{animation:gl 4.2s infinite}}.g2{{animation:gl 4.2s .15s infinite}}
@keyframes gl{{0%,88%,100%{{transform:translate(0,0);opacity:0}}90%{{transform:translate(-5px,1px);opacity:.9}}94%{{transform:translate(6px,-1px);opacity:.9}}97%{{opacity:0}}}}
.pulse{{animation:pu 4s ease-in-out infinite;transform-box:fill-box;transform-origin:center}}
@keyframes pu{{50%{{transform:scale(1.08);opacity:.75}}}}
</style>''')}
<rect width="{W}" height="{H}" fill="url(#sky)"/>
{windows}
<circle class="pulse" cx="500" cy="290" r="270" fill="url(#aura)"/>
<circle cx="500" cy="290" r="152" fill="url(#moon)"/>
<g fill="#7a0710" opacity=".28"><circle cx="450" cy="255" r="26"/><circle cx="545" cy="335" r="34"/><circle cx="480" cy="360" r="15"/><circle cx="560" cy="235" r="13"/></g>
{clouds}
{crows}
{feathers(16, W, 11)}
<rect width="{W}" height="{H}" fill="url(#vig)"/>
<rect y="470" width="{W}" height="{H - 470}" fill="url(#bot)"/>
<g class="in">
<circle cx="500" cy="290" r="128" fill="url(#aura)" opacity=".8"/>
<circle cx="500" cy="290" r="84" fill="#07070a" stroke="$RED" stroke-opacity=".6" stroke-width="2"/>
<circle cx="500" cy="290" r="62" fill="none" stroke="$RED" stroke-width="24"/>
<circle cx="500" cy="290" r="74.5" fill="none" stroke="#000" stroke-width="1.6"/>
<circle cx="500" cy="290" r="49.5" fill="none" stroke="#000" stroke-width="1.6"/>
<g transform="translate(500 290)"><g><animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="9s" repeatCount="indefinite"/>
<use xlink:href="#tomoe" transform="rotate(0) translate(0 -62) scale(8)" fill="#080002"/><use xlink:href="#tomoe" transform="rotate(120) translate(0 -62) scale(8)" fill="#080002"/><use xlink:href="#tomoe" transform="rotate(240) translate(0 -62) scale(8)" fill="#080002"/></g></g>
<circle cx="500" cy="290" r="49" fill="#000"/>
{avatar_inner(500, 290, 48)}
<g font-family="$SANS" font-size="66" letter-spacing="4" text-anchor="start">
<text class="g1" x="200" y="496" fill="$RED" textLength="600" lengthAdjust="spacing">{NAME}</text>
<text class="g2" x="200" y="496" fill="#6ad7ff" textLength="600" lengthAdjust="spacing">{NAME}</text>
<text x="200" y="496" fill="$WHT" textLength="600" lengthAdjust="spacing" filter="url(#glow)">{NAME}</text></g>
<text x="290" y="532" font-family="$SANS" font-size="16" fill="$RED" textLength="420" lengthAdjust="spacing">{TAGLINE}</text>
{''.join(texts)}{''.join(carets)}
</g>
<rect class="cov" width="{W}" height="{H}" fill="#000"/>
<g class="eye">{sharingan(500, 290, 120, 2.5, aura=False)}</g>
""")
    write("header.svg", doc(W, H, body, "Gururaj Naik, full-stack developer. Crows and a crimson moon with a Sharingan avatar ring"))


# ------------------------------------------------------------------ section titles
def titles():
    for fname, text, kanji in SECTIONS:
        body = T(f"""{common_defs('''<style>.u{stroke-dasharray:880;stroke-dashoffset:880;animation:dr 1.6s ease-out .3s forwards}
@keyframes dr{to{stroke-dashoffset:0}}</style>''')}
<path d="M0 10 L10 0 H890 L900 10 V68 L890 78 H10 L0 68Z" fill="$BG2"/>
{sharingan(30, 36, 18, 6, aura=False)}
<text x="62" y="49" font-family="$SANS" font-size="36" letter-spacing="6" fill="$WHT">{text}</text>
<text x="890" y="48" text-anchor="end" font-family="$SANS" font-size="28" fill="$DRED">{kanji}</text>
<path class="u" d="M10 64 H890" stroke="$RED" stroke-width="3" fill="none" filter="url(#glow)"/>
<path d="M10 70 H890" stroke="$DRED" stroke-width="1" opacity=".5"/>
<g><animateMotion path="M140 44 Q500 14 840 40" dur="7s" repeatCount="indefinite" rotate="auto"/>{crow(.4)}</g>""")
        write(fname, doc(900, 78, body, text.title()))


# ------------------------------------------------------------------ developer file (bingo book style)
def dossier():
    W, H = 900, 340
    rows = []
    for i, (k, v) in enumerate(FILE_FIELDS):
        y = 112 + i * 42
        n = len(v)
        tw = n * 9.0
        b = 0.7 + i * 0.7
        rows.append(T(f"""<text x="300" y="{y}" font-family="$MONO" font-size="13" fill="$RED" letter-spacing="2">{k}</text>
<text x="398" y="{y}" font-family="$MONO" font-size="13" fill="$DRED">:</text>
<clipPath id="r{i}"><rect x="412" y="{y - 20}" width="{tw}" height="28"><animate attributeName="width" from="0" to="{tw}" dur="{n * 0.04:.2f}s" begin="{b:.1f}s" fill="freeze"/></rect></clipPath>
<text x="412" y="{y}" font-family="$MONO" font-size="15" fill="$WHT" textLength="{tw}" lengthAdjust="spacingAndGlyphs" clip-path="url(#r{i})">{esc(v)}</text>
<path d="M300 {y + 10} H860" stroke="$DRED" stroke-opacity=".35" stroke-dasharray="2 5"/>"""))
    body = T(f"""{common_defs('''<style>.st{animation:stp 2.4s ease-in-out infinite;transform-box:fill-box;transform-origin:center}
@keyframes stp{0%,100%{opacity:1}50%{opacity:.45}}</style>''')}
<path d="M0 14 L14 0 H886 L900 14 V326 L886 340 H14 L0 326Z" fill="$BG2" stroke="$RED" stroke-width="2"/>
<path d="M8 20 L20 8 H880 L892 20 V320 L880 332 H20 L8 320Z" fill="none" stroke="$DRED" stroke-width="1" opacity=".7"/>
<rect x="14" y="14" width="872" height="40" fill="#1b0509"/>
<text x="34" y="43" font-family="$SANS" font-size="24" letter-spacing="5" fill="$WHT">DEVELOPER FILE</text>
<g class="st" transform="translate(760 20) rotate(-4)"><rect width="110" height="28" fill="none" stroke="$RED" stroke-width="2"/><text x="55" y="20" text-anchor="middle" font-family="$SANS" font-size="17" letter-spacing="4" fill="$RED">CLASSIFIED</text></g>
<g opacity=".16"><use xlink:href="#cloud" transform="translate(620 250) scale(2.2)"/><use xlink:href="#cloud" transform="translate(760 150) scale(1.6)"/></g>
{sharingan(150, 195, 82, 8)}
<text x="150" y="312" text-anchor="middle" font-family="$MONO" font-size="11" fill="$GRY" letter-spacing="3">UCHIHA MODE: ON</text>
{''.join(rows)}
<rect x="14" y="54" width="872" height="3" fill="$RED" opacity=".3"><animate attributeName="y" values="54;330;54" dur="6s" repeatCount="indefinite"/></rect>""")
    write("dossier.svg", doc(W, H, body, "Developer file: Gururaj Naik, full-stack web developer, B.E. Information Technology"))


# ------------------------------------------------------------------ mission cards
def cards():
    for p in PROJECTS:
        W, H = 290, 270
        shape = "M0 14 L14 0 H276 L290 14 V256 L276 270 H14 L0 256Z"
        tags, x = [], 22
        for tg in p["tags"]:
            w = round(len(tg) * 7.0 + 16, 1)
            tags.append(T(f'<rect x="{x}" y="204" width="{w}" height="22" fill="#14090e" stroke="$RED" stroke-opacity=".7"/>'
                          f'<text x="{x + w / 2}" y="219" text-anchor="middle" font-family="$MONO" font-size="11" fill="$WHT">{esc(tg)}</text>'))
            x += w + 8
        desc = "".join(T(f'<text x="22" y="{128 + i * 19}" font-family="$MONO" font-size="12" fill="#d0ccd6">{esc(l)}</text>')
                       for i, l in enumerate(p["lines"]))
        body = T(f"""{common_defs(f'''<clipPath id="cc"><path d="{shape}"/></clipPath>
<style>{fe_css(H)}.bd{{animation:bd 3s ease-in-out infinite}}@keyframes bd{{50%{{stroke-opacity:.35}}}}</style>''')}
<path d="{shape}" fill="$BG2"/>
<g clip-path="url(#cc)">
<g opacity=".09"><use xlink:href="#cloud" transform="translate(20 150) scale(1.5)"/><use xlink:href="#cloud" transform="translate(170 60) scale(1.2)"/><use xlink:href="#cloud" transform="translate(120 225) scale(1.1)"/><animateTransform attributeName="transform" type="translate" values="-30 0;30 0;-30 0" dur="14s" repeatCount="indefinite"/></g>
<circle cx="245" cy="40" r="90" fill="url(#aura)"/>
{feathers(4, W, 3 + int(p['num']), 7, 11)}
</g>
<path class="bd" d="{shape}" fill="none" stroke="$RED" stroke-width="2"/>
<text x="22" y="30" font-family="$MONO" font-size="11" fill="$DRED" letter-spacing="3">MISSION {p['num']}</text>
<g transform="translate(236 14)"><circle cx="20" cy="20" r="19" fill="#14090e" stroke="$RED" stroke-width="2"/><text x="20" y="28" text-anchor="middle" font-family="$SANS" font-size="22" fill="$RED">{p['rank']}</text></g>
<text x="22" y="74" font-family="$SANS" font-size="30" letter-spacing="2" fill="$WHT">{esc(p['title'])}</text>
<text x="22" y="95" font-family="$MONO" font-size="11" fill="$RED">{esc(p['sub'])}</text>
<path d="M22 106 H268" stroke="$DRED" stroke-opacity=".6"/>
{desc}
{''.join(tags)}
<text x="22" y="252" font-family="$MONO" font-size="12" fill="$RED">▶ {esc(p['link'])}</text>""")
        write(p["file"], doc(W, H, body, p["title"].title() + " mission card"))


# ------------------------------------------------------------------ skills
def skills():
    W = 900
    LABEL_W, CH_H, GAP = 190, 32, 10
    blocks, y, n = [], 24, 0
    for name, kanji, items in SKILL_GROUPS:
        x, row_y, chips = LABEL_W, 0, []
        for it in items:
            w = round(len(it) * 7.9 + 38, 1)
            if x + w > W - 10:
                x, row_y = LABEL_W, row_y + CH_H + GAP
            chips.append(T(f"""<g transform="translate({x} {row_y})"><g class="ch" style="animation-delay:{n * 0.09:.2f}s">
<path d="M0 0 H{w - 10} L{w} 10 V{CH_H} H10 L0 {CH_H - 10}Z" fill="#12090e" stroke="$RED" stroke-width="1.4"/>
<circle cx="14" cy="{CH_H / 2}" r="3" fill="$RED"/>
<text x="{w / 2 + 6}" y="{CH_H / 2 + 5}" text-anchor="middle" font-family="$MONO" font-size="13" font-weight="600" fill="$WHT">{esc(it)}</text></g></g>"""))
            x += w + GAP
            n += 1
        bh = row_y + CH_H
        blocks.append(T(f"""<g transform="translate(0 {y})"><rect x="22" y="0" width="4" height="{bh}" fill="$RED"/>
<text x="36" y="20" font-family="$SANS" font-size="20" letter-spacing="3" fill="$WHT">{name}</text>
{''.join(chips)}</g>"""))
        y += bh + 26
    H = y - 2
    body = T(f"""{common_defs('''<style>.ch{animation:sl .6s cubic-bezier(.2,.9,.3,1) both}
@keyframes sl{from{opacity:0;transform:translateX(-40px)}to{opacity:1;transform:translateX(0)}}</style>''')}
<path d="M0 14 L14 0 H886 L900 14 V{H - 14} L886 {H} H14 L0 {H - 14}Z" fill="$BG2" stroke="$RED" stroke-opacity=".5" stroke-width="1.5"/>
{''.join(blocks)}""")
    write("skills.svg", doc(W, H, body, "Skills: languages, frontend, backend and data, tools"))


# ------------------------------------------------------------------ record
def record():
    W, H = 900, 190
    stats = [(150, "15", "REPOSITORIES", ""), (450, "3", "STARS", ""), (750, "2", "ACHIEVEMENTS", "Pull Shark · Quickdraw")]
    parts = []
    for i, (x, num, lab, sub) in enumerate(stats):
        parts.append(T(f"""<g class="pop" style="animation-delay:{0.3 + i * 0.35:.2f}s"><text x="{x}" y="105" text-anchor="middle" font-family="$SANS" font-size="74" fill="$WHT" filter="url(#glow)">{num}</text></g>
<text x="{x}" y="138" text-anchor="middle" font-family="$MONO" font-size="13" letter-spacing="4" fill="$RED">{lab}</text>
<text x="{x}" y="160" text-anchor="middle" font-family="$MONO" font-size="11" fill="$GRY">{sub}</text>"""))
    body = T(f"""{common_defs('''<style>.pop{animation:pp .7s cubic-bezier(.2,1.6,.4,1) both;transform-box:fill-box;transform-origin:center}
@keyframes pp{from{opacity:0;transform:scale(.3)}to{opacity:1;transform:scale(1)}}</style>''')}
<path d="M0 14 L14 0 H886 L900 14 V176 L886 190 H14 L0 176Z" fill="$BG2" stroke="$RED" stroke-width="2"/>
<g opacity=".1">{sharingan(450, 95, 130, 20, aura=False)}</g>
<path d="M300 40 V150 M600 40 V150" stroke="$DRED" stroke-opacity=".6"/>
{''.join(parts)}""")
    write("record.svg", doc(W, H, body, "GitHub record: 15 repositories, 3 stars, 2 achievements"))


# ------------------------------------------------------------------ contact banner
def contact():
    W, H = 900, 220
    shape = "M0 14 L14 0 H886 L900 14 V206 L886 220 H14 L0 206Z"
    body = T(f"""{common_defs(f'''<clipPath id="cb"><path d="{shape}"/></clipPath>
<style>.bd{{animation:bd 2.6s ease-in-out infinite}}@keyframes bd{{50%{{stroke-opacity:.3}}}}</style>''')}
<path d="{shape}" fill="$BG2"/>
<g clip-path="url(#cb)"><g opacity=".1"><use xlink:href="#cloud" transform="translate(60 120) scale(2.4)"/><use xlink:href="#cloud" transform="translate(420 40) scale(1.8)"/><use xlink:href="#cloud" transform="translate(600 140) scale(2)"/>
<animateTransform attributeName="transform" type="translate" values="-40 0;40 0;-40 0" dur="16s" repeatCount="indefinite"/></g>
<circle cx="760" cy="110" r="190" fill="url(#aura)"/></g>
<path class="bd" d="{shape}" fill="none" stroke="$RED" stroke-width="2.4"/>
<text x="44" y="64" font-family="$MONO" font-size="12" letter-spacing="5" fill="$DRED">INCOMING TRANSMISSION</text>
<text x="44" y="112" font-family="$SANS" font-size="46" letter-spacing="4" fill="$WHT" filter="url(#glow)">MISSION REQUEST</text>
<text x="44" y="146" font-family="$MONO" font-size="15" fill="$GRY">Open to Web Developer and Full-Stack roles.</text>
<text x="44" y="180" font-family="$MONO" font-size="17" fill="$RED">▶ gururajnaik2807@gmail.com</text>
{sharingan(770, 110, 62, 7)}
<g><animateMotion path="M40 30 Q450 -10 860 36" dur="9s" repeatCount="indefinite" rotate="auto"/>{crow(.7)}</g>""")
    write("contact.svg", doc(W, H, body, "Mission request: open to Web Developer and Full-Stack roles"))


# ------------------------------------------------------------------ footer
def footer():
    W, H = 1000, 340
    clouds = "".join(
        f'<g opacity=".4"><use xlink:href="#cloud" transform="translate({x} {y}) scale({s})"/>'
        f'<animateTransform attributeName="transform" type="translate" values="-300 0;1300 0" dur="{d}s" begin="-{b}s" repeatCount="indefinite"/></g>'
        for x, y, s, d, b in ((0, 90, 1.6, 60, 10), (0, 210, 1.1, 80, 45), (0, 40, 0.9, 70, 25)))
    body = T(f"""{common_defs(f'''<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#050507"/><stop offset=".7" stop-color="#2a0610"/><stop offset="1" stop-color="#050507"/></linearGradient>
<radialGradient id="moon" cx=".4" cy=".35" r=".7"><stop offset="0" stop-color="#ff6a5c"/><stop offset=".5" stop-color="#d42030"/><stop offset="1" stop-color="#7a0710"/></radialGradient>
<style>{fe_css(H)}</style>''')}
<rect width="{W}" height="{H}" fill="url(#sky)"/>
<circle cx="500" cy="160" r="220" fill="url(#aura)"/>
<circle cx="500" cy="160" r="105" fill="url(#moon)"/>
<g fill="#7a0710" opacity=".28"><circle cx="470" cy="135" r="20"/><circle cx="540" cy="195" r="26"/></g>
{clouds}
{flying_crow(130, 14, -3, 1.3, bend=-60) + flying_crow(190, 18, -11, 1.0, bend=40) + flying_crow(100, 22, -16, 0.8, bend=-30)}
{feathers(10, W, 5)}
<path d="M0 300 L90 250 L130 275 L210 230 L300 285 L420 255 L520 290 L640 245 L760 285 L860 240 L1000 290 V340 H0Z" fill="#030304"/>
<text x="500" y="318" text-anchor="middle" font-family="$MONO" font-size="13" letter-spacing="4" fill="$GRY">UNTIL THE NEXT MISSION</text>""")
    write("footer.svg", doc(W, H, body, "Crimson moon with crows flying past. Until the next mission"))


if __name__ == "__main__":
    header()
    titles()
    dossier()
    cards()
    skills()
    record()
    contact()
    footer()
    print("done")
