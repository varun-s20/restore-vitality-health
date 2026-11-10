"""Restore Vitality Health: the drawn media system (upgrade pass 8b). Imported by tools/build.py.

Concept 1, the gold seam: cream line figures on plum, mended by gold seams, the way kintsugi mends a bowl.
Everything is inline SVG drawn from the client's data, so it is sharp at any size and never upscaled.
- step_art(slug): the five How it works scenes (spec 7: five custom gold line drawings on plum).
- product_art(p): a treatment's media, drawn in the step scenes' language (pass 8c). The format sets the figure
  (tablet, liposome, cream, patch, injection drop, nasal mist), an object with body mended by one gold seam; under
  the horizon, one week of ticks shows the dosing rhythm (gold on dose days) and gold beads count the active
  ingredients; a soft round of tint names the program (gold Men's, terracotta Women's, sage Shared; ruling 8).
- program_art(cat, ...): a program's formats composed as one group, for category banners and the quiz band.
Strokes use vector-effect: non-scaling-stroke, so a line is the same weight on a card and on a 900px tile.
Variation comes from a seed per slug (crc32), so the output never changes between runs.
"""
import math
import random
import zlib

from markupsafe import Markup

TINT = {'mens': 'gold', 'womens': 'terracotta', 'shared': 'sage'}


def _f(v):
    return ('%.1f' % v).rstrip('0').rstrip('.')


def _pts(points):
    return ' '.join('%s %s' % (_f(x), _f(y)) for x, y in points)


def _seam_points(rng, a, b, steps=7, amp=5.0):
    """A mended crack from a to b: straight on average, with small seeded kinks, like the logo's veins."""
    (x1, y1), (x2, y2) = a, b
    dx, dy = x2 - x1, y2 - y1
    ln = math.hypot(dx, dy) or 1
    nx, ny = -dy / ln, dx / ln
    out = [a]
    for i in range(1, steps):
        t = i / steps + rng.uniform(-.03, .03)
        k = rng.uniform(-amp, amp)
        out.append((x1 + dx * t + nx * k, y1 + dy * t + ny * k))
    out.append(b)
    return out


def _seam(rng, a, b, cls='b-art__seam', steps=7, amp=5.0, branch=False):
    pts = _seam_points(rng, a, b, steps, amp)
    s = '<polyline class="%s" points="%s"/>' % (cls, _pts(pts))
    if branch:
        # one hairline vein leaving the seam about a third of the way along
        i = max(1, len(pts) // 3)
        x, y = pts[i]
        ang = math.atan2(b[1] - a[1], b[0] - a[0]) + rng.choice((-1, 1)) * rng.uniform(.6, .9)
        ln = rng.uniform(18, 30)
        end = (x + math.cos(ang) * ln, y + math.sin(ang) * ln)
        s += '<polyline class="b-art__vein" points="%s"/>' % _pts(_seam_points(rng, (x, y), end, 3, 2))
    return s


def _svg(view, body, cls, ratio='xMidYMid meet'):
    return Markup('<svg class="b-art %s" viewBox="%s" preserveAspectRatio="%s" aria-hidden="true" focusable="false">%s</svg>'
                  % (cls, view, ratio, body))


# ---------------------------------------------------------------- format figures
# Polish pass 8c (Studio Lead): the 8b figures were small diagrams in big tiles, with hairline program rings cropped by
# the tile edge as filler. They are now drawn in the step scenes' language: an object with body (a soft fill a step
# lighter than plum under the cream line), one kinked gold mend with a hairline vein, faint supporting marks, a shadow
# on a shared horizon. Each figure is drawn in its own frame, centred on 0, about 240 units across, and returns the
# y of its lowest point so every figure floats the same height above the horizon.
L, F, B = 'b-art__line', 'b-art__faint', 'b-art__body'


def _p(cls, d):
    return '<path class="%s" d="%s"/>' % (cls, d)


def _tablet(rng, seam):
    # a tablet seen at three quarters: top face, bevel, edge band
    rx, ry, t, e = 118, 56, -16, 28
    out = [_p(B, 'M%d %d V%d A%d %d 0 0 0 %d %d V%d A%d %d 0 0 0 %d %d Z' % (-rx, t, t + e, rx, ry, rx, t + e, t, rx, ry, -rx, t)),
           '<ellipse class="%s" cx="0" cy="%d" rx="%d" ry="%d"/>' % (L, t, rx, ry),
           '<ellipse class="%s" cx="0" cy="%d" rx="%d" ry="%d"/>' % (F, t, rx - 16, ry - 9),
           _p(L, 'M%d %d V%d A%d %d 0 0 0 %d %d V%d' % (-rx, t, t + e, rx, ry, rx, t + e, t)),
           _seam(rng, (-44, t - 52), (-6, t + 2), seam, 5, 3.2, branch=True),
           _seam(rng, (-6, t + 2), (26, t + e + ry - 2), seam, 4, 2.4)]
    return ''.join(out), t + e + ry


def _liposome(rng, seam):
    # a sphere of two layers: a bead on every head, a faint tail between the layers, a little cargo inside
    r = 112
    out = ['<circle class="%s" cx="0" cy="0" r="%d"/>' % (B, r)]
    for rr, n, c, br in ((r, 36, 'b-art__dot -bead', 3.6), (r * .8, 28, 'b-art__dot', 2.6)):
        for i in range(n):
            a = 2 * math.pi * (i + (.5 if rr < r else 0)) / n
            out.append('<circle class="%s" cx="%s" cy="%s" r="%s"/>' % (c, _f(math.cos(a) * rr), _f(math.sin(a) * rr), _f(br)))
    for i in range(36):
        a = 2 * math.pi * i / 36
        out.append('<line class="%s" x1="%s" y1="%s" x2="%s" y2="%s"/>' % (
            F, _f(math.cos(a) * (r - 6)), _f(math.sin(a) * (r - 6)), _f(math.cos(a) * (r - 13)), _f(math.sin(a) * (r - 13))))
    for _ in range(7):
        a, d = rng.uniform(0, 2 * math.pi), rng.uniform(10, 58)
        out.append('<circle class="b-art__dot -faint" cx="%s" cy="%s" r="2.2"/>' % (_f(math.cos(a) * d), _f(math.sin(a) * d)))
    # volume (critic 8c High 3: it still read as a ring diagram): an equator seen from above and a light on the
    # upper left, so it reads as a sphere sitting in the light; a vial is ruled out by the brief
    out.append('<ellipse class="%s" cx="0" cy="0" rx="%d" ry="%d"/>' % (F, r - 18, 30))
    out.append(_p(L + ' -soft', 'M-%d -%d A%d %d 0 0 1 -%d -%d' % (68, 40, r - 30, r - 30, 18, 76)))
    a0 = math.radians(rng.uniform(-150, -120))
    a1 = a0 + math.radians(rng.uniform(150, 165))
    out.append(_seam(rng, (math.cos(a0) * r, math.sin(a0) * r), (math.cos(a1) * r, math.sin(a1) * r), seam, 8, 3.4, branch=True))
    return ''.join(out), r + 4


def _cream(rng, seam):
    # a swatch of cream spread on the skin: full at the left, feathering out to the right, ridges from the stroke
    # (pass 8c: a peaked dollop was tried first and read as the wrong thing entirely)
    swatch = ('M-98 -40 C-40 -64 50 -58 106 -40 C118 -34 104 -26 114 -18 C122 -10 106 -6 116 6 '
              'C60 14 10 22 -36 40 C-80 58 -128 34 -122 -4 C-120 -22 -112 -34 -98 -40 Z')
    out = [_p(B, swatch), _p(L, swatch),
           _p(F, 'M-100 -14 C-50 -38 40 -36 106 -24'),
           _p(F, 'M-96 6 C-50 -12 40 -16 108 -4'),
           _p(F, 'M-80 28 C-40 10 20 4 70 8'),
           _p(F, 'M124 -30 L138 -32'), _p(F, 'M128 -12 L144 -11'), _p(F, 'M124 6 L136 9'),
           _seam(rng, (-20, -56), (-44, 44), seam, 6, 3.2, branch=True)]
    return ''.join(out), 52


def _patch(rng, seam):
    # a skin patch lying at an angle, its corner lifting, the release edge dashed inside
    s, c = 168, 22
    h = s / 2
    shape = ('M{a} {m} H{b} Q{h} {m} {h} {a} V{k} L{k} {h} H{a} Q{m} {h} {m} {b} V{a} Q{m} {m} {a} {m} Z'
             .format(a=_f(-h + c), b=_f(h - c), h=_f(h), m=_f(-h), k=_f(h - 44)))
    out = ['<g transform="rotate(-9)">', _p(B, shape), _p(L, shape),
           '<rect class="%s -dash" x="%s" y="%s" width="%s" height="%s" rx="12"/>' % (F, _f(-h + 18), _f(-h + 18), _f(s - 36), _f(s - 50)),
           _p(B, 'M%s %s L%s %s Q%s %s %s %s Z' % (_f(h), _f(h - 44), _f(h - 44), _f(h), _f(h - 10), _f(h - 6), _f(h), _f(h - 44))),
           _p(L, 'M%s %s Q%s %s %s %s L%s %s' % (_f(h - 44), _f(h), _f(h - 10), _f(h - 6), _f(h), _f(h - 44), _f(h - 44), _f(h))),
           _seam(rng, (-h + 8, -h + 34), (h - 30, h - 6), seam, 8, 3.2, branch=True), '</g>']
    return ''.join(out), h + 18


def _injection(rng, seam):
    # one measured drop above still water: a dose, drawn without the device
    drop = 'M0 -124 C0 -124 -70 -36 -70 10 A70 70 0 0 0 70 10 C70 -36 0 -124 0 -124 Z'
    out = [_p(B, drop), _p(L, drop),
           _p(F, 'M-48 6 C-48 -22 -26 -56 -14 -74'),
           _seam(rng, (-30, -76), (34, 70), seam, 7, 3.2, branch=True)]
    for k, cls in ((.5, L), (.84, F), (1.18, F)):
        out.append('<ellipse class="%s" cx="0" cy="112" rx="%s" ry="%s"/>' % (cls, _f(104 * k), _f(104 * k * .17)))
    return ''.join(out), 112  # the ripples lie on the horizon itself, so the drop needs no shadow


def _nasal(rng, seam):
    # a fine mist opening from one point, its plume held in a faint outline
    ox, oy = -96, 92
    plume = 'M%d %d C-60 30 -70 -60 0 -104 C60 -136 132 -84 118 -20 C108 30 40 54 %d %d Z' % (ox, oy, ox, oy)
    out = [_p(B + ' -mist', plume)]  # the plume has body but no outline: mist has no edge
    for j in range(5):
        a = -math.radians(52) + (j - 2) * .2
        for i in range(1, 11):
            d = 20 * i * (1 + i * .03)
            out.append('<circle class="b-art__dot%s" cx="%s" cy="%s" r="%s"/>' % (
                '' if i < 7 else ' -faint', _f(ox + math.cos(a) * d), _f(oy + math.sin(a) * d), _f(max(1.6, 3.4 - i * .18))))
    out.append('<circle class="%s" cx="%d" cy="%d" r="9"/>' % (L, ox, oy))
    a = -math.radians(52)
    out.append(_seam(rng, (ox + math.cos(a) * 30, oy + math.sin(a) * 30), (ox + math.cos(a) * 236, oy + math.sin(a) * 236), seam, 7, 3.2, branch=True))
    return ''.join(out), oy + 9


FIGS = {'tablet': _tablet, 'liposome': _liposome, 'cream': _cream, 'patch': _patch, 'injection': _injection, 'nasal': _nasal}


def _place(fmt, x, base, s, rng, seam='b-art__seam', tilt=0):
    """A figure at scale s, centred on x, its lowest point at base."""
    body, bottom = FIGS[fmt](rng, seam)
    y = base - bottom * s
    g = '<g transform="translate(%s %s) rotate(%s) scale(%s)">%s</g>' % (_f(x), _f(y), _f(tilt), _f(s), body)
    return g, y


def fmt_of(p):
    t = p['en']
    chip = t['chips'][0].lower()
    if chip == 'oral':
        return 'liposome' if ('vial' in t['card'] or 'liposomal' in p['slug']) else 'tablet'
    return {'cream': 'cream', 'patch': 'patch', 'injection': 'injection', 'nasal': 'nasal'}.get(chip, 'tablet')


def _week(p, x, y):
    """One week as seven ticks under the horizon, gold on the dose days. The 8b calendar (every day of the billing
    period) read as a halftone at 390; one week reads as a rhythm. Only drawn when the client's data gives a frequency
    ("take as needed" and Sermorelin's open question show none)."""
    chips = p['en']['chips']
    if len(chips) < 2:
        return ''
    days = {'daily': set(range(7)), 'weekly': {0}, 'twice weekly': {0, 3}}.get(chips[1].lower(), set())
    if not days:
        return ''
    return '<g class="b-art__week">%s</g>' % ''.join(
        '<line class="%s" x1="%s" y1="%s" x2="%s" y2="%s"/>' % (
            'b-art__tick' if d in days else F, _f(x + d * 13), _f(y), _f(x + d * 13), _f(y + 12)) for d in range(7))


def _actives(n, x, y):
    """n gold beads, right-aligned under the horizon: one per active ingredient."""
    return ''.join('<circle class="b-art__dose" cx="%s" cy="%s" r="3.6"/>' % (_f(x - k * 13), _f(y)) for k in range(n))


_IDS = [0]


def _tint(cat, cx, cy, r):
    """The program, read at a glance: a soft round of its tint behind the figures (gold Men's, terracotta Women's,
    sage Shared), fading to nothing well inside the tile. Ruling 8: quiet, a large shape only."""
    _IDS[0] += 1
    gid = 'rvh-tint-%d' % _IDS[0]
    return ('<defs><radialGradient id="%s"><stop class="b-art__tintStop" offset="0"/>'
            '<stop class="b-art__tintStop" offset=".55" stop-opacity=".55"/>'
            '<stop class="b-art__tintStop" offset="1" stop-opacity="0"/></radialGradient></defs>'
            '<circle class="b-art__tint" cx="%s" cy="%s" r="%s" fill="url(#%s)"/>' % (gid, _f(cx), _f(cy), _f(r), gid))


def _horizon(y, x1=-600, x2=1000):
    return '<line class="%s" x1="%d" y1="%s" x2="%d" y2="%s"/>' % (F, x1, _f(y), x2, _f(y))


def _shadow(x, y, rx):
    return '<ellipse class="b-art__shadow" cx="%s" cy="%s" rx="%s" ry="%s"/>' % (_f(x), _f(y), _f(rx), _f(rx * .09))


ORDER = {}  # slug: position within its category, set by tools/build.py, so neighbouring cards never share a composition

# Critic round 8b (High 2) asked that neighbours in a rail differ; 8c keeps that with four large compositions instead
# of a small icon in four places: the figure shifts, leans and trades sides with its tint. Fitted on the 400 x 500 card.
COMPS = [
    {'x': 200, 's': 1.0, 'tilt': 0, 'tint': (214, 250)},
    {'x': 192, 's': 1.06, 'tilt': -6, 'tint': (244, 226)},
    {'x': 210, 's': .98, 'tilt': 5, 'tint': (164, 238)},
    {'x': 200, 's': 1.02, 'tilt': -2, 'tint': (200, 290)},
]
HORIZON = 420


def product_art(p, cls='m-card__art'):
    rng = random.Random(zlib.crc32(p['slug'].encode()))
    # treatment pages take the first composition, drawn to fill their tile (slice); the varied ones are for rails
    comp = COMPS[0] if cls == 'o-product__art' else COMPS[ORDER.get(p['slug'], 0) % len(COMPS)]
    fmt = fmt_of(p)
    n = max(1, min(4, len(p['en'].get('ingredients', [])) or 1))
    seam = 'b-art__seam -fine' if p['program'] == 'micro' else 'b-art__seam'
    wet = fmt == 'injection'  # the drop's ripples lie on the horizon; everything else floats over its shadow
    fig, _ = _place(fmt, comp['x'], HORIZON - (0 if wet else 26), comp['s'], rng, seam, 0 if wet else comp['tilt'])
    body = [_tint(p['category'], comp['tint'][0], comp['tint'][1], 190), _horizon(HORIZON),
            '' if wet else _shadow(comp['x'], HORIZON, 108 * comp['s']), fig,
            _week(p, 44, HORIZON + 26), _actives(n, 356, HORIZON + 32)]
    # the treatment tile is about as wide as tall at 1440 (critic 8c High 2), so it gets a wider frame around the same
    # drawing; slice keeps a phone's 4:5 tile full, cropping only empty margin at the sides
    view = '-40 40 480 444' if cls == 'o-product__art' else '0 0 400 500'
    return _svg(view, ''.join(body), 'b-art -product -%s %s' % (TINT[p['category']], cls), 'xMidYMid slice')


# ---------------------------------------------------------------- program families
# Each program's formats composed as one group on one horizon, the way a still life is set: one figure in front,
# the others behind it, overlapping, under one round of the program's tint. (format, x, scale, tilt, lift), back to front.
FAMILY = {
    'mens': [('liposome', 244, .74, 0, 34), ('tablet', 150, .74, -4, 0)],
    'womens': [('patch', 124, .6, -6, 40), ('tablet', 296, .52, 3, 22), ('cream', 196, .66, 0, 0)],
    'shared': [('injection', 120, .54, 0, 30), ('liposome', 270, .5, 0, 74), ('tablet', 190, .52, -3, 0), ('nasal', 326, .4, 0, 0)],
}
GROUND = 316


def _group(cat, rng, horizon=True):
    out = [_tint(cat, 210, 200, 200)]
    if horizon:
        out.append(_horizon(GROUND))
    figs = FAMILY[cat]
    for f, x, s, tilt, lift in figs:
        if f != 'injection':
            out.append(_shadow(x, GROUND, 100 * s))
    for f, x, s, tilt, lift in figs:
        out.append(_place(f, x, GROUND - (lift if f == 'injection' else 22 + lift), s, rng, tilt=tilt)[0])
    return ''.join(out)


def program_art(cat, cls=''):
    rng = random.Random(zlib.crc32(cat.encode()))
    return _svg('0 0 400 400', _group(cat, rng), 'b-art -program -%s %s' % (TINT[cat], cls))


def quiz_art():
    """The quiz band's backdrop: the three programs side by side; each lights when its route row is pointed at."""
    gy = 170 + GROUND * .8
    body = ['<line class="%s" x1="0" y1="%s" x2="1440" y2="%s"/>' % (F, _f(gy), _f(gy))]
    for i, cat in enumerate(('mens', 'womens', 'shared')):
        rng = random.Random(zlib.crc32(cat.encode()))
        body.append('<g class="o-quizBand__fig -%s -%s" transform="translate(%d 170) scale(.8)">%s</g>'
                    % (cat, TINT[cat], 520 + i * 300, _group(cat, rng, horizon=False)))
    return _svg('0 0 1440 661', ''.join(body), 'b-art -quiz', 'xMaxYMid slice')


# ---------------------------------------------------------------- How it works scenes
# viewBox 256 x 377 (Neko's 397:584 card). Pass 8c (critic High 3): the line work is unchanged; each scene's main
# object gained the cards' body fill and a shadow on the horizon, so steps and cards read as one set. Every scene stands on one horizon at y 318, drawn past the edges so the
# five tiles share it. Gold is only where something is joined or decided.
_H = '<line class="b-art__faint" x1="-600" y1="318" x2="856" y2="318"/>'
STEPS = {
    # Consult: two voices overlapping, the seam where they meet, three intake lines
    'consult': (
        '<ellipse class="b-art__shadow" cx="128" cy="318" rx="72" ry="6.5"/>'
        '<circle class="b-art__body" cx="104" cy="176" r="62"/><circle class="b-art__body" cx="160" cy="204" r="46"/>'
        '<circle class="b-art__line" cx="104" cy="176" r="62"/>'
        '<circle class="b-art__line" cx="160" cy="204" r="46"/>'
        '<circle class="b-art__faint" cx="104" cy="176" r="74"/>'
        '<polyline class="b-art__seam" points="128 118 124 134 131 148 126 163 133 178 128 194 135 211 131 236"/>'
        '<polyline class="b-art__vein" points="126 163 114 170 108 184"/>'
        '<line class="b-art__faint" x1="44" y1="272" x2="132" y2="272"/>'
        '<line class="b-art__faint" x1="44" y1="286" x2="150" y2="286"/>'
        '<line class="b-art__faint" x1="44" y1="300" x2="104" y2="300"/>'),
    # Labs: one drop, cracked and mended, beside a measuring scale with a single reading in gold
    'labs': (
        '<ellipse class="b-art__shadow" cx="118" cy="318" rx="52" ry="5"/>'
        '<path class="b-art__body" d="M118 92 C118 92 64 168 64 206 A54 54 0 0 0 172 206 C172 168 118 92 118 92 Z"/>'
        '<path class="b-art__line" d="M118 92 C118 92 64 168 64 206 A54 54 0 0 0 172 206 C172 168 118 92 118 92 Z"/>'
        '<path class="b-art__faint" d="M118 116 C118 116 78 176 78 206 A40 40 0 0 0 158 206"/>'
        '<polyline class="b-art__seam" points="118 98 114 122 123 146 115 170 125 194 117 220 122 244 118 258"/>'
        '<polyline class="b-art__vein" points="123 146 137 154 141 168"/>'
        + ''.join('<line class="b-art__faint" x1="200" y1="%d" x2="%d" y2="%d"/>' % (y, 214 if (y - 134) % 32 == 0 else 207, y)
                  for y in range(134, 300, 8))
        + '<line class="b-art__seam" x1="192" y1="206" x2="218" y2="206"/>'),
    # Plan: a written page, folded at the corner, signed in gold
    'plan': (
        '<ellipse class="b-art__shadow" cx="128" cy="318" rx="62" ry="5.5"/>'
        '<g transform="rotate(-6 128 200)">'
        '<path class="b-art__body" d="M66 104 H160 L188 132 V276 H66 Z"/>'
        '<path class="b-art__line" d="M66 104 H160 L188 132 V276 H66 Z"/>'
        '<path class="b-art__faint" d="M160 104 V132 H188"/>'
        '<line class="b-art__faint" x1="84" y1="150" x2="170" y2="150"/>'
        '<line class="b-art__faint" x1="84" y1="166" x2="170" y2="166"/>'
        '<line class="b-art__faint" x1="84" y1="182" x2="160" y2="182"/>'
        '<line class="b-art__faint" x1="84" y1="198" x2="132" y2="198"/>'
        '<path class="b-art__seam" d="M84 246 C92 228 104 226 106 240 S118 254 128 236 S146 226 152 244 C156 252 164 250 172 240"/>'
        '</g>'),
    # Delivery: a parcel on a route that comes in from the previous tile, its tape in gold
    'delivery': (
        '<ellipse class="b-art__shadow" cx="128" cy="318" rx="64" ry="5.5"/>'
        '<path class="b-art__body" d="M128 150 L186 178 V244 L128 272 L70 244 V178 Z"/>'
        '<path class="b-art__line" d="M128 150 L186 178 L128 206 L70 178 Z"/>'
        '<path class="b-art__line" d="M70 178 V244 L128 272 L186 244 V178 M128 206 V272"/>'
        '<polyline class="b-art__seam" points="99 164 112 170 127 177 141 185 157 192"/>'
        '<polyline class="b-art__seam" points="157 192 158 208 156 224 158 240 157 258"/>'
        '<path class="b-art__faint -dash" d="M-40 304 C10 304 34 296 62 270"/>'
        '<path class="b-art__faint -dash" d="M194 268 C220 286 250 296 296 300"/>'),
    # Follow-up: a ring that renews, its one break mended in gold, four marks for the billing periods
    'follow-up': (
        '<ellipse class="b-art__shadow" cx="128" cy="318" rx="60" ry="5.5"/>'
        '<circle class="b-art__body" cx="128" cy="200" r="64"/>'
        '<path class="b-art__line" d="M168 150 A64 64 0 1 1 116 138"/>'
        '<path class="b-art__faint" d="M128 152 A48 48 0 1 1 82 192"/>'
        '<polyline class="b-art__seam" points="116 138 126 134 135 138 146 136 156 142 168 150"/>'
        '<polyline class="b-art__vein" points="135 138 138 126 146 120"/>'
        + ''.join('<line class="b-art__faint" x1="%s" y1="%s" x2="%s" y2="%s"/>' % (
            _f(128 + math.cos(a) * 74), _f(200 + math.sin(a) * 74), _f(128 + math.cos(a) * 84), _f(200 + math.sin(a) * 84))
            for a in (0, math.pi / 2, math.pi, 3 * math.pi / 2))),
}


def step_art(slug):
    return _svg('0 0 256 377', _H + STEPS[slug], 'b-art -step m-step__art')


# R2 media: real photos replace the drawn figures. The photo helpers ride on product_art, which build.py already
# registers, so templates reach them as product_art.photo and product_art.product_img. If tools/photos.py or its
# data is missing, the attributes stay unset and the templates fall back to the drawn figures.
try:
    import photos as _photos
    product_art.photo = _photos.photo
    product_art.product_img = _photos.product_img
except Exception:  # noqa: BLE001, photos not produced yet
    pass
