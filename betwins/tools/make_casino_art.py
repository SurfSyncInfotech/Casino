"""Generates the casino artwork (SVG) used by the templates.

Run from the project root:   python tools/make_casino_art.py
Output:                      apps/static/images/casino/*.svg
"""
import math
import os

OUT = os.path.join(os.path.dirname(__file__), "..", "apps", "static", "images", "casino")
os.makedirs(OUT, exist_ok=True)

GOLD = "#ffba23"
CYAN = "#9cecfe"

# --------------------------------------------------------------------------
# shared definitions
# --------------------------------------------------------------------------
DEFS = f"""
<linearGradient id="gGold" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff3b8"/><stop offset=".45" stop-color="{GOLD}"/><stop offset="1" stop-color="#a8650a"/></linearGradient>
<linearGradient id="gRuby" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ff7a85"/><stop offset=".5" stop-color="#d11a3a"/><stop offset="1" stop-color="#6a0b1e"/></linearGradient>
<linearGradient id="gSapphire" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#8fbaff"/><stop offset=".5" stop-color="#2563d8"/><stop offset="1" stop-color="#0c2a6e"/></linearGradient>
<linearGradient id="gEmerald" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#8ff5c0"/><stop offset=".5" stop-color="#14a366"/><stop offset="1" stop-color="#075238"/></linearGradient>
<linearGradient id="gOnyx" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#5b5f6c"/><stop offset=".5" stop-color="#2a2c34"/><stop offset="1" stop-color="#0d0e12"/></linearGradient>
<linearGradient id="gCyan" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#e3fbff"/><stop offset=".5" stop-color="{CYAN}"/><stop offset="1" stop-color="#3c9db8"/></linearGradient>
<linearGradient id="gCard" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#dfe3ee"/></linearGradient>
<linearGradient id="gWood" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#8a4b1c"/><stop offset=".5" stop-color="#4e2610"/><stop offset="1" stop-color="#2b1208"/></linearGradient>
<radialGradient id="gGlow" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="{CYAN}" stop-opacity=".45"/><stop offset=".6" stop-color="{CYAN}" stop-opacity=".08"/><stop offset="1" stop-color="{CYAN}" stop-opacity="0"/></radialGradient>
<radialGradient id="gGlowGold" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="{GOLD}" stop-opacity=".5"/><stop offset=".6" stop-color="{GOLD}" stop-opacity=".1"/><stop offset="1" stop-color="{GOLD}" stop-opacity="0"/></radialGradient>
<radialGradient id="gFelt" cx=".5" cy=".4" r=".8"><stop offset="0" stop-color="#1f7a55"/><stop offset="1" stop-color="#0a3523"/></radialGradient>
<filter id="fShadow" x="-30%" y="-30%" width="160%" height="170%"><feDropShadow dx="0" dy="10" stdDeviation="9" flood-color="#000" flood-opacity=".45"/></filter>
<filter id="fSoft" x="-30%" y="-30%" width="160%" height="170%"><feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#000" flood-opacity=".4"/></filter>
"""

SUITS = {
    "heart": ("M50 90 C18 63 6 47 6 30 C6 16 17 7 30 7 C39 7 46 12 50 20 C54 12 61 7 70 7 C83 7 94 16 94 30 C94 47 82 63 50 90Z", "#d11a3a"),
    "diamond": ("M50 4 L90 50 L50 96 L10 50 Z", "#d11a3a"),
    "spade": ("M50 5 C50 5 8 38 8 62 C8 76 20 85 33 85 C40 85 46 81 49 76 C48 87 44 93 35 97 L65 97 C56 93 52 87 51 76 C54 81 60 85 67 85 C80 85 92 76 92 62 C92 38 50 5 50 5Z", "#16171c"),
    "club": ("M50 4 A21 21 0 1 1 50 46 A21 21 0 1 1 50 4 Z M27 38 A21 21 0 1 1 27 80 A21 21 0 1 1 27 38 Z M73 38 A21 21 0 1 1 73 80 A21 21 0 1 1 73 38 Z M46 60 C46 78 43 90 33 97 L67 97 C57 90 54 78 54 60 Z", "#16171c"),
}


def svg(w, h, body, vb=None):
    vb = vb or f"0 0 {w} {h}"
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="{vb}">'
            f"<defs>{DEFS}</defs>{body}</svg>")


def save(name, content):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as fh:
        fh.write(content)


# --------------------------------------------------------------------------
# primitives
# --------------------------------------------------------------------------
def suit(kind, x, y, size, color=None):
    d, c = SUITS[kind]
    s = size / 100.0
    return f'<path d="{d}" fill="{color or c}" transform="translate({x - size/2:.1f} {y - size/2:.1f}) scale({s:.3f})"/>'


def sparkle(x, y, r, color="#fff", op=1):
    d = f"M{x} {y-r} Q{x} {y} {x+r} {y} Q{x} {y} {x} {y+r} Q{x} {y} {x-r} {y} Q{x} {y} {x} {y-r}Z"
    return f'<path d="{d}" fill="{color}" opacity="{op}"/>'


def card(cx, cy, w, h, rot, rank, kind, back=False):
    x, y = -w / 2, -h / 2
    col = SUITS[kind][1]
    parts = [f'<g transform="translate({cx} {cy}) rotate({rot})" filter="url(#fSoft)">']
    if back:
        parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{w*.08}" fill="url(#gRuby)" stroke="#fff" stroke-width="{w*.03}"/>')
        parts.append(f'<rect x="{x+w*.1}" y="{y+w*.1}" width="{w*.8}" height="{h-w*.2}" rx="{w*.05}" fill="none" stroke="{GOLD}" stroke-width="{w*.02}"/>')
        parts.append(suit("diamond", 0, 0, w * .45, GOLD))
    else:
        parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{w*.08}" fill="url(#gCard)" stroke="#c9cedc" stroke-width="1.5"/>')
        fs = w * .27
        parts.append(f'<text x="{x+w*.09}" y="{y+fs*1.05}" font-family="Georgia,\'Times New Roman\',serif" font-weight="bold" font-size="{fs:.1f}" fill="{col}">{rank}</text>')
        parts.append(suit(kind, x + w * .17, y + fs * 1.05 + w * .1, w * .17, col))
        parts.append(suit(kind, w * .06, h * .06, w * .46, col))
        parts.append(f'<g transform="rotate(180)"><text x="{x+w*.09}" y="{y+fs*1.05}" font-family="Georgia,\'Times New Roman\',serif" font-weight="bold" font-size="{fs:.1f}" fill="{col}">{rank}</text>'
                     f'{suit(kind, x + w * .17, y + fs * 1.05 + w * .1, w * .17, col)}</g>')
    parts.append("</g>")
    return "".join(parts)


def chip(cx, cy, r, grad="gRuby", label="", rot=0):
    edge = []
    for i in range(8):
        a = i * 45
        edge.append(f'<rect x="{-r*.13:.1f}" y="{-r:.1f}" width="{r*.26:.1f}" height="{r*.3:.1f}" rx="{r*.04:.1f}" fill="#fff" opacity=".95" transform="rotate({a})"/>')
    inner = r * .62
    txt = ""
    if label:
        txt = (f'<text x="0" y="{r*.14:.1f}" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-weight="bold" '
               f'font-size="{r*.42:.1f}" fill="#fff" stroke="rgba(0,0,0,.35)" stroke-width="{r*.02:.1f}">{label}</text>')
    return (f'<g transform="translate({cx} {cy}) rotate({rot})" filter="url(#fSoft)">'
            f'<circle r="{r}" fill="url(#{grad})"/>{"".join(edge)}'
            f'<circle r="{r*.74:.1f}" fill="url(#{grad})" stroke="rgba(255,255,255,.55)" stroke-width="{r*.03:.1f}"/>'
            f'<circle r="{inner:.1f}" fill="none" stroke="rgba(255,255,255,.7)" stroke-width="{r*.025:.1f}" stroke-dasharray="{r*.12:.1f} {r*.08:.1f}"/>'
            f'<path d="M{-r*.8:.1f} {-r*.25:.1f} A{r*.85:.1f} {r*.85:.1f} 0 0 1 {-r*.1:.1f} {-r*.82:.1f}" stroke="rgba(255,255,255,.55)" stroke-width="{r*.06:.1f}" fill="none" stroke-linecap="round"/>'
            f"{txt}</g>")


def chip_stack(cx, cy, r, n, grads, tilt=0.42):
    """Isometric-ish stack: n chips drawn bottom to top."""
    out = []
    th = r * .26
    for i in range(n):
        g = grads[i % len(grads)]
        y = cy - i * th
        out.append(f'<g filter="url(#fSoft)">'
                   f'<path d="M{cx-r} {y} v{th} a{r} {r*tilt} 0 0 0 {2*r} 0 v{-th}Z" fill="url(#{g})"/>'
                   f'<ellipse cx="{cx}" cy="{y}" rx="{r}" ry="{r*tilt}" fill="url(#{g})" stroke="rgba(255,255,255,.5)" stroke-width="1"/>'
                   f'<ellipse cx="{cx}" cy="{y}" rx="{r*.68}" ry="{r*tilt*.68}" fill="none" stroke="rgba(255,255,255,.85)" stroke-width="{r*.05}" stroke-dasharray="{r*.16} {r*.12}"/>'
                   f"</g>")
        # edge stripes
        for k in range(-3, 4):
            sx = cx + k * r * .28
            out.append(f'<rect x="{sx-r*.045:.1f}" y="{y + r*tilt*math.sqrt(max(0,1-(k*.28)**2)) - 1:.1f}" width="{r*.09:.1f}" height="{th*.8:.1f}" fill="#fff" opacity=".85"/>')
    return "".join(out)


def die(cx, cy, s, rot, pips=5, grad="gCard", pip="#16171c"):
    r = s * .18
    pos = {
        1: [(0, 0)],
        2: [(-1, -1), (1, 1)],
        3: [(-1, -1), (0, 0), (1, 1)],
        4: [(-1, -1), (1, -1), (-1, 1), (1, 1)],
        5: [(-1, -1), (1, -1), (0, 0), (-1, 1), (1, 1)],
        6: [(-1, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (1, 1)],
    }[pips]
    dots = "".join(f'<circle cx="{px*s*.27:.1f}" cy="{py*s*.27:.1f}" r="{s*.075:.1f}" fill="{pip}"/>' for px, py in pos)
    return (f'<g transform="translate({cx} {cy}) rotate({rot})" filter="url(#fShadow)">'
            f'<rect x="{-s/2}" y="{-s/2}" width="{s}" height="{s}" rx="{r}" fill="url(#{grad})" stroke="rgba(0,0,0,.15)" stroke-width="1.5"/>'
            f'<rect x="{-s/2+s*.05}" y="{-s/2+s*.05}" width="{s*.9}" height="{s*.9}" rx="{r*.8}" fill="none" stroke="rgba(255,255,255,.7)" stroke-width="2"/>'
            f"{dots}</g>")


def coin(cx, cy, r, sym="₹"):
    return (f'<g transform="translate({cx} {cy})" filter="url(#fSoft)">'
            f'<circle r="{r}" fill="url(#gGold)" stroke="#8a520a" stroke-width="{r*.05:.1f}"/>'
            f'<circle r="{r*.78:.1f}" fill="none" stroke="rgba(255,255,255,.7)" stroke-width="{r*.05:.1f}"/>'
            f'<text x="0" y="{r*.3:.1f}" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-weight="bold" font-size="{r*.95:.1f}" fill="#7a4608">{sym}</text>'
            f'<path d="M{-r*.7:.1f} {-r*.3:.1f} A{r*.75:.1f} {r*.75:.1f} 0 0 1 {-r*.1:.1f} {-r*.74:.1f}" stroke="rgba(255,255,255,.7)" stroke-width="{r*.07:.1f}" fill="none" stroke-linecap="round"/>'
            f"</g>")


def crown(cx, cy, w, grad="gGold"):
    h = w * .72
    x0, y0 = cx - w / 2, cy - h / 2
    pts = (f"M{x0} {y0+h} L{x0+w*.04} {y0+h*.2} L{x0+w*.27} {y0+h*.55} L{cx} {y0} L{x0+w*.73} {y0+h*.55} "
           f"L{x0+w*.96} {y0+h*.2} L{x0+w} {y0+h} Z")
    jewels = "".join(
        f'<circle cx="{jx:.1f}" cy="{jy:.1f}" r="{w*.045:.1f}" fill="{c}" stroke="#fff" stroke-width="1.2"/>'
        for jx, jy, c in [(x0 + w * .22, y0 + h * .82, "#d11a3a"), (cx, y0 + h * .78, "#2563d8"), (x0 + w * .78, y0 + h * .82, "#14a366")])
    tips = "".join(f'<circle cx="{tx:.1f}" cy="{ty:.1f}" r="{w*.04:.1f}" fill="#fff3b8"/>'
                   for tx, ty in [(x0 + w * .04, y0 + h * .2), (cx, y0), (x0 + w * .96, y0 + h * .2)])
    return (f'<g filter="url(#fSoft)"><path d="{pts}" fill="url(#{grad})" stroke="#8a520a" stroke-width="2" stroke-linejoin="round"/>'
            f'<rect x="{x0}" y="{y0+h*.86}" width="{w}" height="{h*.14}" rx="3" fill="#a8650a"/>{jewels}{tips}</g>')


EURO_ORDER = [0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23, 10, 5, 24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26]
REDS = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}


def polar(cx, cy, r, ang):
    a = math.radians(ang - 90)
    return cx + r * math.cos(a), cy + r * math.sin(a)


def sector(cx, cy, r1, r2, a0, a1):
    x0, y0 = polar(cx, cy, r2, a0)
    x1, y1 = polar(cx, cy, r2, a1)
    x2, y2 = polar(cx, cy, r1, a1)
    x3, y3 = polar(cx, cy, r1, a0)
    return f"M{x0:.2f} {y0:.2f} A{r2} {r2} 0 0 1 {x1:.2f} {y1:.2f} L{x2:.2f} {y2:.2f} A{r1} {r1} 0 0 0 {x3:.2f} {y3:.2f}Z"


def roulette(cx, cy, R, rot=0):
    out = [f'<g transform="translate({cx} {cy}) rotate({rot}) translate({-cx} {-cy})" filter="url(#fShadow)">']
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="url(#gWood)" stroke="#1a0b05" stroke-width="3"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{R*.97}" fill="none" stroke="url(#gGold)" stroke-width="{R*.025}"/>')
    n = len(EURO_ORDER)
    step = 360 / n
    r_out, r_in = R * .86, R * .62
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{R*.9}" fill="#120a06"/>')
    for i, num in enumerate(EURO_ORDER):
        a0, a1 = i * step, (i + 1) * step
        fill = "#0e9d62" if num == 0 else ("#c8102e" if num in REDS else "#17181d")
        out.append(f'<path d="{sector(cx, cy, r_in, r_out, a0, a1)}" fill="{fill}" stroke="url(#gGold)" stroke-width="1.2"/>')
        tx, ty = polar(cx, cy, (r_in + r_out) / 2 + R * .015, a0 + step / 2)
        out.append(f'<text x="{tx:.1f}" y="{ty:.1f}" text-anchor="middle" dominant-baseline="middle" font-family="Arial,Helvetica,sans-serif" '
                   f'font-weight="bold" font-size="{R*.062:.1f}" fill="#fff" transform="rotate({a0+step/2:.2f} {tx:.1f} {ty:.1f})">{num}</text>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{r_in}" fill="url(#gOnyx)" stroke="url(#gGold)" stroke-width="3"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{R*.5}" fill="url(#gWood)" stroke="url(#gGold)" stroke-width="2"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{R*.4}" fill="url(#gGold)" opacity=".92"/>')
    for k in range(4):
        out.append(f'<rect x="{cx-R*.03}" y="{cy-R*.4}" width="{R*.06}" height="{R*.8}" rx="{R*.02}" fill="url(#gGold)" stroke="#8a520a" stroke-width="1.5" transform="rotate({k*45} {cx} {cy})"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{R*.13}" fill="url(#gOnyx)" stroke="url(#gGold)" stroke-width="3"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{R*.055}" fill="url(#gGold)"/>')
    bx, by = polar(cx, cy, R * .74, 40)
    out.append(f'<circle cx="{bx:.1f}" cy="{by:.1f}" r="{R*.035}" fill="#fff" stroke="#bbb" stroke-width="1"/>')
    out.append("</g>")
    return "".join(out)


def glow(cx, cy, r, grad="gGlow"):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#{grad})"/>'


def fan(cx, cy, w, cards, spread=22, lift=0.0):
    out = []
    n = len(cards)
    for i, (rank, kind) in enumerate(cards):
        a = (i - (n - 1) / 2) * spread
        dx = math.sin(math.radians(a)) * w * 0.9
        dy = (1 - math.cos(math.radians(a))) * w * 0.9 - lift
        out.append(card(cx + dx, cy + dy, w, w * 1.4, a, rank, kind))
    return "".join(out)


# --------------------------------------------------------------------------
# images
# --------------------------------------------------------------------------
def make_logo():
    body = f"""
<g transform="translate(2 2)">
  <path d="M20 4 L36 12 L36 28 L20 40 L4 28 L4 12 Z" fill="url(#gGold)" stroke="#8a520a" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M20 9 L31 14.5 L31 26 L20 35 L9 26 L9 14.5 Z" fill="#1d1e24"/>
  <path d="M12 27 L13.5 17 L17 21.5 L20 14 L23 21.5 L26.5 17 L28 27 Z" fill="url(#gGold)"/>
  <circle cx="20" cy="14" r="1.6" fill="#fff3b8"/><circle cx="13.5" cy="17" r="1.3" fill="#fff3b8"/><circle cx="26.5" cy="17" r="1.3" fill="#fff3b8"/>
</g>
<text x="52" y="25" font-family="Georgia,'Times New Roman',serif" font-weight="bold" font-size="23" letter-spacing="1.5" fill="#ffffff">CASINO</text>
<text x="52" y="40" font-family="Arial,Helvetica,sans-serif" font-weight="bold" font-size="11.5" letter-spacing="7.2" fill="{GOLD}">ROYALE</text>
<path d="M150 21 h18" stroke="{GOLD}" stroke-width="1.2" opacity=".0"/>
"""
    save("logo.svg", svg(200, 46, body))
    save("favicon.svg", svg(64, 64, f"""
<rect width="64" height="64" rx="14" fill="#1d1e24"/>
<path d="M32 6 L54 17 L54 40 L32 58 L10 40 L10 17 Z" fill="url(#gGold)" stroke="#8a520a" stroke-width="2" stroke-linejoin="round"/>
<path d="M32 13 L47 20.5 L47 38 L32 50 L17 38 L17 20.5 Z" fill="#1d1e24"/>
<path d="M21 38 L23 25 L28 31 L32 21 L36 31 L41 25 L43 38 Z" fill="url(#gGold)"/>"""))
    # preloader mark (gold crown)
    save("crown.svg", svg(160, 120, crown(80, 60, 140)))


def make_hero():
    b = [glow(360, 380, 360), glow(250, 480, 220, "gGlowGold")]
    b.append(roulette(300, 410, 235, rot=-12))
    b.append(fan(500, 175, 130, [("A", "spade"), ("K", "heart"), ("Q", "diamond")], spread=24))
    b.append(chip_stack(110, 640, 62, 7, ["gRuby", "gOnyx", "gRuby"]))
    b.append(chip_stack(600, 660, 66, 9, ["gSapphire", "gGold", "gEmerald", "gSapphire"]))
    b.append(chip(535, 545, 58, "gGold", "₹", 14))
    b.append(chip(190, 125, 48, "gEmerald", "50", -10))
    b.append(die(95, 470, 96, -18, 5))
    b.append(die(640, 440, 74, 22, 6))
    b.append(coin(425, 690, 34))
    b.append(coin(40, 300, 26))
    b.append(crown(300, 62, 120))
    for x, y, r in [(70, 60, 16), (650, 90, 12), (610, 300, 18), (30, 560, 12), (470, 20, 10), (180, 660, 14)]:
        b.append(sparkle(x, y, r, "#fff"))
    save("hero-thumb.svg", svg(709, 719, "".join(b)))


def make_about():
    b = [glow(400, 300, 330), glow(560, 400, 200, "gGlowGold")]
    b.append(roulette(260, 330, 200, rot=8))
    b.append(fan(560, 215, 125, [("10", "club"), ("J", "diamond"), ("A", "heart")], spread=26))
    b.append(chip_stack(110, 560, 60, 8, ["gGold", "gRuby", "gGold"]))
    b.append(chip_stack(680, 530, 62, 6, ["gEmerald", "gOnyx"]))
    b.append(chip(470, 470, 58, "gSapphire", "100", 8))
    b.append(chip(395, 540, 44, "gRuby", "25", -6))
    b.append(die(620, 380, 82, 18, 3))
    b.append(die(330, 520, 62, -12, 6))
    b.append(coin(740, 290, 30))
    b.append(coin(50, 190, 24))
    for x, y, r in [(40, 60, 14), (740, 80, 16), (430, 40, 12), (200, 570, 10)]:
        b.append(sparkle(x, y, r))
    save("about-thumb.svg", svg(790, 598, "".join(b)))


def make_auth():
    b = [glow(380, 270, 300), glow(380, 340, 200, "gGlowGold")]
    b.append(fan(380, 250, 150, [("A", "spade"), ("K", "spade"), ("Q", "spade"), ("J", "spade"), ("10", "spade")], spread=20))
    b.append(chip_stack(140, 470, 66, 7, ["gRuby", "gOnyx", "gRuby"]))
    b.append(chip_stack(620, 480, 66, 9, ["gGold", "gSapphire", "gGold", "gEmerald"]))
    b.append(chip(380, 450, 62, "gGold", "₹", 10))
    b.append(die(260, 480, 70, -14, 4))
    b.append(die(500, 490, 62, 16, 5))
    b.append(coin(60, 200, 28))
    b.append(coin(700, 150, 26))
    b.append(crown(380, 40, 110))
    for x, y, r in [(70, 80, 14), (700, 300, 14), (330, 520, 10)]:
        b.append(sparkle(x, y, r))
    save("auth-thumb.svg", svg(761, 548, "".join(b)))


def make_banner_thumb():
    b = [glow(210, 170, 190)]
    b.append(fan(215, 140, 100, [("A", "heart"), ("K", "spade"), ("Q", "club")], spread=24))
    b.append(chip_stack(80, 285, 48, 6, ["gRuby", "gOnyx"]))
    b.append(chip_stack(340, 290, 46, 5, ["gGold", "gSapphire"]))
    b.append(die(260, 270, 56, 16, 5))
    b.append(sparkle(40, 60, 12))
    b.append(sparkle(380, 80, 14))
    save("banner-thumb.svg", svg(413, 325, "".join(b)))


def make_fantasy():
    b = [glow(182, 176, 170)]
    b.append(fan(182, 190, 112, [("A", "spade"), ("K", "heart"), ("Q", "diamond"), ("J", "club")], spread=20, lift=10))
    b.append(chip(70, 300, 44, "gGold", "₹", 8))
    b.append(chip(300, 296, 40, "gRuby", "50", -8))
    b.append(sparkle(320, 50, 14))
    b.append(sparkle(40, 80, 12))
    save("f-cards.svg", svg(365, 353, "".join(b)))
    b = [glow(120, 130, 120)]
    b.append(chip_stack(70, 205, 48, 6, ["gSapphire", "gOnyx"]))
    b.append(chip_stack(165, 215, 46, 4, ["gRuby", "gGold"]))
    b.append(chip(118, 100, 46, "gEmerald", "100", 10))
    b.append(sparkle(215, 40, 12))
    save("f-chips.svg", svg(241, 237, "".join(b)))
    b = [glow(120, 120, 120)]
    b.append(die(100, 110, 100, -14, 6))
    b.append(die(170, 160, 74, 20, 5))
    b.append(coin(60, 190, 28))
    b.append(sparkle(200, 50, 12))
    save("f-dice.svg", svg(241, 237, "".join(b)))


def make_decor():
    for i, (name, grad, lab) in enumerate([("chip-red", "gRuby", "5"), ("chip-blue", "gSapphire", "25"), ("chip-green", "gEmerald", "100"), ("chip-gold", "gGold", "₹")]):
        save(f"{name}.svg", svg(180, 180, chip(90, 90, 74, grad, lab, 12 * i)))
    save("dice.svg", svg(180, 180, die(90, 90, 110, -14, 5)))
    save("dice-b.svg", svg(180, 180, die(90, 90, 110, 18, 6)))
    save("coin.svg", svg(120, 120, coin(60, 60, 52)))
    save("premium.svg", svg(140, 140, crown(70, 70, 120)))
    save("cards-sm.svg", svg(300, 260, fan(150, 150, 100, [("A", "spade"), ("K", "heart")], spread=26)))
    save("wheel.svg", svg(320, 320, roulette(160, 160, 150)))
    b = [chip(90, 90, 80, "gSapphire", "", 0)]
    save("chip-plain.svg", svg(180, 180, "".join(b)))


def banner(name, title, sub, art, c1="#2b1658", c2="#0b1b3a", accent=GOLD):
    body = f"""
<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient>
<radialGradient id="spot" cx=".72" cy=".5" r=".55"><stop offset="0" stop-color="{accent}" stop-opacity=".35"/><stop offset="1" stop-color="{accent}" stop-opacity="0"/></radialGradient></defs>
<rect width="368" height="207" fill="url(#bg)"/><rect width="368" height="207" fill="url(#spot)"/>
<g opacity=".12" stroke="#fff"><path d="M0 40 H368 M0 90 H368 M0 140 H368 M0 190 H368"/></g>
<g>{art}</g>
<text x="20" y="88" font-family="Georgia,'Times New Roman',serif" font-weight="bold" font-size="27" fill="#fff" stroke="rgba(0,0,0,.45)" stroke-width=".8">{title[0]}</text>
<text x="20" y="118" font-family="Georgia,'Times New Roman',serif" font-weight="bold" font-size="27" fill="{accent}" stroke="rgba(0,0,0,.45)" stroke-width=".8">{title[1]}</text>
<text x="21" y="142" font-family="Arial,Helvetica,sans-serif" font-weight="bold" font-size="10.5" letter-spacing="2.4" fill="rgba(255,255,255,.78)">{sub}</text>
<rect x="21" y="150" width="46" height="3" rx="1.5" fill="{accent}"/>
"""
    # wrap with defs of the shared gradients too
    save(name, f'<svg xmlns="http://www.w3.org/2000/svg" width="368" height="207" viewBox="0 0 368 207"><defs>{DEFS}</defs>{body}</svg>')


def make_banners():
    s = 0.5
    banner("g-teen-patti.svg", ("TEEN", "PATTI"), "ROYAL 3 CARD CLASSIC",
           f'<g transform="translate(250 105)">{fan(0, 10, 78, [("A","spade"),("K","heart"),("Q","diamond")], spread=26)}</g>'
           + chip(330, 170, 22, "gGold", "₹", 10) + chip(215, 175, 18, "gRuby", "", 0), "#4a1230", "#150a22")
    banner("g-andar-bahar.svg", ("ANDAR", "BAHAR"), "THE DESI FAVOURITE",
           card(255, 100, 74, 104, -12, "A", "heart") + card(300, 105, 74, 104, 10, "K", "spade")
           + chip(332, 172, 22, "gEmerald", "50", 0) + sparkle(220, 40, 10), "#0e3d33", "#0a1624", "#7cf2c2")
    banner("g-blackjack.svg", ("BLACK", "JACK"), "21 · BEAT THE DEALER",
           card(250, 100, 76, 106, -10, "A", "spade") + card(298, 106, 76, 106, 12, "K", "diamond")
           + chip_stack(335, 188, 24, 4, ["gOnyx", "gRuby"]) + sparkle(215, 36, 10), "#14223f", "#07101f", "#9cecfe")
    banner("g-baccarat.svg", ("BACC", "ARAT"), "PUNTO BANCO PRESTIGE",
           card(250, 100, 76, 106, -12, "9", "heart") + card(298, 104, 76, 106, 10, "Q", "club")
           + chip(332, 172, 22, "gSapphire", "100", 0) + coin(212, 168, 16), "#3a1f5e", "#0c0a22", "#e4b8ff")
    banner("g-dragon-tiger.svg", ("DRAGON", "TIGER"), "ONE CARD · ONE WINNER",
           card(252, 100, 76, 106, -10, "K", "heart") + card(298, 104, 76, 106, 12, "Q", "spade")
           + f'<text x="252" y="170" text-anchor="middle" font-family="Georgia,serif" font-weight="bold" font-size="22" fill="{GOLD}">D</text>'
           + f'<text x="298" y="174" text-anchor="middle" font-family="Georgia,serif" font-weight="bold" font-size="22" fill="{CYAN}">T</text>', "#4b1111", "#190808", "#ff9b6b")
    banner("g-poker.svg", ("TEXAS", "HOLD'EM"), "NO-LIMIT · TOURNAMENT",
           card(240, 100, 70, 98, -14, "A", "spade") + card(285, 104, 70, 98, 6, "A", "heart")
           + chip_stack(335, 190, 24, 5, ["gRuby", "gOnyx", "gGold"]) + chip(205, 168, 18, "gGold", "", 0), "#10392a", "#07130e", "#7cf2c2")
    banner("g-sic-bo.svg", ("SIC", "BO"), "THE ANCIENT DICE GAME",
           die(255, 90, 66, -14, 4) + die(310, 118, 60, 18, 6) + die(240, 150, 52, 8, 5) + coin(335, 56, 17), "#3a2306", "#140c04")
    banner("g-keno.svg", ("ROYAL", "KENO"), "PICK · DRAW · WIN",
           "".join(chip(x, y, 20, g, str(n), r) for x, y, g, n, r in [(240, 80, "gRuby", "7", 0), (285, 104, "gSapphire", "21", 12), (330, 78, "gEmerald", "33", -8), (255, 142, "gGold", "9", 6), (305, 160, "gRuby", "40", -12)]),
           "#162c5a", "#0a1226", "#9cecfe")
    banner("g-andar-roulette.svg", ("LIVE", "ROULETTE"), "EUROPEAN · 37 POCKETS",
           roulette(290, 110, 78, 10), "#3a0d1a", "#12060a", "#ff8a8a")
    banner("g-lounge.svg", ("VIP", "LOUNGE"), "PRIVATE SALONS",
           crown(290, 70, 110) + chip_stack(255, 180, 28, 5, ["gGold", "gOnyx"]) + chip_stack(325, 182, 28, 4, ["gRuby", "gGold"]), "#352060", "#0d0a1f", GOLD)


def tile(name, label, grad_a, grad_b, art):
    body = f"""
<defs><linearGradient id="tb" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{grad_a}"/><stop offset="1" stop-color="{grad_b}"/></linearGradient></defs>
<g>
 <path d="M16 20 Q4 40 14 62 Q8 88 40 100 Q78 112 112 98 Q140 88 138 58 Q146 30 120 16 Q82 2 44 10 Q26 12 16 20Z" fill="url(#tb)"/>
 <circle cx="128" cy="18" r="8" fill="{grad_a}" opacity=".85"/><circle cx="14" cy="92" r="6" fill="{grad_b}" opacity=".85"/>
 <g transform="translate(0 -8)">{art}</g>
 <text x="72" y="88" text-anchor="middle" font-family="Arial Black,Arial,Helvetica,sans-serif" font-weight="900" font-size="11.5" letter-spacing=".5" fill="#fff" stroke="rgba(0,0,0,.4)" stroke-width=".6">{label}</text>
</g>"""
    save(name, f'<svg xmlns="http://www.w3.org/2000/svg" width="144" height="111" viewBox="0 0 144 111"><defs>{DEFS}</defs>{body}</svg>')


def make_tiles():
    tile("t-teen-patti.svg", "TEEN PATTI", "#e8315b", "#7d0f33", fan(72, 56, 34, [("A", "spade"), ("K", "heart"), ("Q", "diamond")], spread=26))
    tile("t-andar-bahar.svg", "ANDAR BAHAR", "#12b886", "#06543f", card(58, 50, 34, 48, -10, "A", "heart") + card(86, 52, 34, 48, 10, "K", "spade"))
    tile("t-roulette.svg", "ROULETTE", "#c8102e", "#4d0615", roulette(72, 46, 36, 0))
    tile("t-blackjack.svg", "BLACKJACK", "#2f6fe4", "#10285f", card(58, 50, 34, 48, -10, "A", "spade") + card(86, 52, 34, 48, 10, "J", "diamond"))
    tile("t-baccarat.svg", "BACCARAT", "#8b4be0", "#321466", card(58, 50, 34, 48, -10, "9", "heart") + card(86, 52, 34, 48, 10, "Q", "club"))
    tile("t-poker.svg", "POKER", "#18a574", "#07422d", card(60, 48, 32, 46, -12, "A", "spade") + card(84, 50, 32, 46, 8, "A", "heart") + chip(110, 60, 14, "gGold", "", 0))
    tile("t-dragon-tiger.svg", "DRAGON TIGER", "#ff7a2f", "#7a2306", card(58, 50, 34, 48, -10, "K", "heart") + card(86, 52, 34, 48, 10, "Q", "spade"))
    tile("t-slots.svg", "ROYAL SLOTS", "#f4b400", "#7a4a00",
         '<rect x="38" y="22" width="68" height="46" rx="8" fill="#16171c" stroke="#fff3b8" stroke-width="2.5"/>'
         + "".join(f'<rect x="{42+i*22}" y="27" width="20" height="36" rx="3" fill="#fff"/><text x="{52+i*22}" y="55" text-anchor="middle" font-family="Georgia,serif" font-weight="bold" font-size="26" fill="#d11a3a">7</text>' for i in range(3)))
    tile("t-sic-bo.svg", "SIC BO", "#a0522d", "#3c1d0d", die(56, 46, 30, -12, 4) + die(84, 50, 30, 14, 6))
    tile("t-keno.svg", "ROYAL KENO", "#2aa7d1", "#0b3a52",
         chip(52, 44, 15, "gRuby", "7") + chip(78, 36, 15, "gSapphire", "21") + chip(100, 54, 15, "gEmerald", "33") + chip(72, 62, 15, "gGold", "9"))
    tile("t-jackpot.svg", "JACKPOT", "#d946ef", "#4b0f66", crown(72, 40, 60) + coin(48, 58, 12) + coin(98, 58, 12))


def pay(name, text, c1, c2=None, size=15):
    t2 = f'<tspan fill="{c2}">{text[1]}</tspan>' if c2 else ""
    first = text[0]
    body = (f'<svg xmlns="http://www.w3.org/2000/svg" width="70" height="48" viewBox="0 0 70 48"><rect width="70" height="48" rx="7" fill="#fff"/>'
            f'<text x="35" y="29" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-weight="bold" font-size="{size}" fill="{c1}">{first}{t2}</text></svg>')
    save(name, body)


def make_payments():
    def badge(name, text, color, accent=None, size=15, sub=None):
        parts = text if isinstance(text, list) else [text]
        content = "".join(parts)
        extra = f'<text x="35" y="40" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="6.5" fill="#888">{sub}</text>' if sub else ""
        save(name, f'<svg xmlns="http://www.w3.org/2000/svg" width="70" height="48" viewBox="0 0 70 48"><rect width="70" height="48" rx="7" fill="#fff"/>'
                   f'<text x="35" y="{27 if sub else 30}" text-anchor="middle" font-family="Arial Black,Arial,Helvetica,sans-serif" font-weight="900" font-size="{size}" fill="{color}">{content}</text>{extra}</svg>')
    badge("upi.svg", '<tspan fill="#f58220">U</tspan><tspan fill="#0a8f3c">P</tspan><tspan fill="#f58220">I</tspan>', "#000", size=20, sub="UNIFIED PAYMENTS")
    badge("rupay.svg", '<tspan fill="#1a3a8f">Ru</tspan><tspan fill="#f58220">Pay</tspan>', "#000", size=15)
    badge("phonepe.svg", "PhonePe", "#5f259f", size=11.5)
    badge("paytm.svg", '<tspan fill="#002e6e">pay</tspan><tspan fill="#00baf2">tm</tspan>', "#000", size=15)
    badge("netbanking.svg", "NetBanking", "#0b3c6f", size=9.5)
    badge("imps.svg", "IMPS", "#c1272d", size=16, sub="INSTANT TRANSFER")


def make_sponsors():
    names = [("sp-aurum.svg", "AURUM", "GAMING"), ("sp-nexa.svg", "NEXA", "PLAY"), ("sp-zenith.svg", "ZENITH", "LIVE"),
             ("sp-sapphire.svg", "SAPPHIRE", "SOFT"), ("sp-vega.svg", "VEGA", "RNG LABS"), ("sp-orbit.svg", "ORBIT", "CERTIFIED"),
             ("sp-regal.svg", "REGAL", "STUDIOS")]
    for fn, a, b in names:
        w = 70 + 18 * len(a) + 11 * len(b)
        body = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="32" viewBox="0 0 {w} 32">'
                f'<path d="M14 2 L26 8 L26 20 L14 30 L2 20 L2 8 Z" fill="none" stroke="#cdd2de" stroke-width="2.2" stroke-linejoin="round"/>'
                f'<circle cx="14" cy="15" r="3.4" fill="{GOLD}"/>'
                f'<text x="36" y="22" font-family="Arial Black,Arial,Helvetica,sans-serif" font-weight="900" font-size="18" letter-spacing="1" fill="#e6e9f2">{a}'
                f'<tspan font-weight="400" font-family="Arial,Helvetica,sans-serif" font-size="12" letter-spacing="2" fill="#9aa1b4" dx="6">{b}</tspan></text></svg>')
        save(fn, body)



def cover(name, w, h, c1, c2, art, accent=GOLD):
    cx, cy = w / 2, h / 2
    body = (f'<defs><linearGradient id="cb" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient>'
            f'<radialGradient id="cs" cx=".5" cy=".5" r=".6"><stop offset="0" stop-color="{accent}" stop-opacity=".4"/><stop offset="1" stop-color="{accent}" stop-opacity="0"/></radialGradient></defs>'
            f'<rect width="{w}" height="{h}" fill="url(#cb)"/><rect width="{w}" height="{h}" fill="url(#cs)"/>'
            f'<g opacity=".08" stroke="#fff">' + "".join(f'<path d="M0 {y} H{w}"/>' for y in range(40, h, 56)) + '</g>'
            f'<g transform="translate({cx} {cy})">{art}</g>'
            + sparkle(w * .12, h * .15, 14) + sparkle(w * .88, h * .22, 12) + sparkle(w * .8, h * .85, 10))
    save(name, f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><defs>{DEFS}</defs>{body}</svg>')


def make_covers():
    arts = {
        "roulette": ("#3a0d1a", "#12060a", lambda k: roulette(0, 0, 150 * k, 8)),
        "blackjack": ("#14223f", "#07101f", lambda k: fan(0, 0, 110 * k, [("A", "spade"), ("J", "diamond")], spread=26) + chip_stack(-120 * k, 120 * k, 40 * k, 5, ["gOnyx", "gRuby"]) + chip(120 * k, 110 * k, 36 * k, "gGold", "", 8)),
        "baccarat": ("#3a1f5e", "#0c0a22", lambda k: fan(0, 0, 110 * k, [("9", "heart"), ("Q", "club"), ("K", "diamond")], spread=24) + chip(-120 * k, 125 * k, 38 * k, "gSapphire", "100", 0) + coin(125 * k, 120 * k, 28 * k)),
        "slots": ("#3a2306", "#140c04", lambda k: crown(0, -80 * k, 130 * k) + chip(-90 * k, 40 * k, 52 * k, "gRuby", "7", 0) + chip(0, 70 * k, 52 * k, "gGold", "7", 10) + chip(90 * k, 40 * k, 52 * k, "gEmerald", "7", -8)),
    }
    for key, (c1, c2, fn) in arts.items():
        cover(f"b-{key}-sq.svg", 416, 416, c1, c2, fn(1.0))
        cover(f"b-{key}-wide.svg", 636, 400, c1, c2, fn(1.05))

def make_misc():
    # simple generic avatar placeholders are reused from the template; nothing to do.
    pass


if __name__ == "__main__":
    make_logo()
    make_hero()
    make_about()
    make_auth()
    make_banner_thumb()
    make_fantasy()
    make_decor()
    make_banners()
    make_tiles()
    make_payments()
    make_sponsors()
    make_covers()
    print("written:", len(os.listdir(OUT)), "files to", os.path.abspath(OUT))
