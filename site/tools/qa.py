"""Restore Vitality Health: browser QA (Playwright, already installed).

For each page path: loads it at 1440x900 and 390x844, hides the scrollbar (evals/lessons.md 1), scrolls the
whole page and back (lesson 2), waits out the hero load, then records:
- console errors and failed requests (404s), unused preloads
- images shown wider than their own pixels (natural width < rendered css width), at 1x
- horizontal overflow, h1 count, elements still hidden by a reveal after the scroll
- with reduced motion emulated: running animations
and saves screen-stop captures to build/shots/<page>-<width>-<n>.png (every screen at 1440 and 390).

Run from site/ with the local server up:  python tools/qa.py index.html es/index.html [--shots] [--base URL]
Writes a JSON summary to stdout; build/qa-report.md is written by hand from it.
"""
import json
import os
import sys

from playwright.sync_api import sync_playwright

BASE = 'http://127.0.0.1:8740/'  # the local preview (python -m http.server 8740 from site/)
HERE = os.path.dirname(os.path.abspath(__file__))
SHOTS = os.path.join(os.path.dirname(os.path.dirname(HERE)), 'build', 'shots')
HIDE_SB = 'html{scrollbar-width:none} ::-webkit-scrollbar{display:none}'

CHECK_JS = r"""() => {
  const out = {h1: document.querySelectorAll('h1').length, overflow: document.documentElement.scrollWidth - window.innerWidth,
               upscaled: [], hidden: [], noalt: [], emdash: false};
  document.querySelectorAll('img').forEach(img => {
    const r = img.getBoundingClientRect();
    if (!img.complete || !img.naturalWidth || r.width < 2) return;
    const cs = getComputedStyle(img);
    if (cs.display === 'none' || cs.visibility === 'hidden') return;
    // object-fit cover: the image's own width is scaled by the larger of the two ratios
    // real file pixels: srcset derivatives carry their width in the name (naturalWidth is density-adjusted)
    const m = img.currentSrc.match(/-(\d+)\.webp$/);
    const fw = m ? +m[1] : img.naturalWidth, fh = img.naturalHeight * fw / img.naturalWidth;
    let scale = r.width / fw;
    if (cs.objectFit === 'cover') scale = Math.max(r.width / fw, r.height / fh);
    if (scale > 1.02) out.upscaled.push([img.currentSrc.split('/').pop(), Math.round(r.width), Math.round(r.height), fw, Math.round(fh), +scale.toFixed(2)]);
    if (!img.hasAttribute('alt')) out.noalt.push(img.currentSrc);
  });
  document.querySelectorAll('[data-reveal] .m-word, [data-reveal-follow]').forEach(el => {
    if (parseFloat(getComputedStyle(el).opacity) < 0.99) out.hidden.push(el.textContent.slice(0, 40));
  });
  out.emdash = /\u2014/.test(document.body.innerText);
  return out;
}"""

HEADER_JS = r"""async () => {
  // ruling A2: header text must stay readable over whatever band sits under it, at every screen stop
  function lum(c) { const m = c.match(/[\d.]+/g).map(Number); const f = v => { v /= 255; return v <= .03928 ? v / 12.92 : Math.pow((v + .055) / 1.055, 2.4); }; return .2126 * f(m[0]) + .7152 * f(m[1]) + .0722 * f(m[2]); }
  function bgAt(x, y) {
    const els = document.elementsFromPoint(x, y).filter(e => !e.closest('.o-header'));
    for (const e of els) { const b = getComputedStyle(e).backgroundColor; const a = b.match(/[\d.]+/g); if (a && (a.length < 4 || +a[3] > .5)) return b; }
    return 'rgb(74,46,61)';
  }
  const h = document.querySelector('.o-header'); const bad = [];
  const H = document.documentElement.scrollHeight;
  for (let y = 0; y < H; y += innerHeight) {
    window.scrollTo(0, y); await new Promise(r => setTimeout(r, 650));
    const scrolled = h.classList.contains('is-scrolled');
    const bg = scrolled ? (h.classList.contains('is-light') ? 'rgb(245,239,230)' : 'rgb(46,27,38)') : bgAt(innerWidth - 40, h.offsetHeight / 2);
    const fg = getComputedStyle(h).color;
    const L1 = lum(fg), L2 = lum(bg); const ratio = (Math.max(L1, L2) + .05) / (Math.min(L1, L2) + .05);
    if (ratio < 3) bad.push([y, fg, bg, +ratio.toFixed(2)]);
  }
  window.scrollTo(0, 0);
  return bad;
}"""


def scroll_through(page):
    page.evaluate("""async () => {
      const h = document.documentElement.scrollHeight;
      for (let y = 0; y < h; y += Math.round(innerHeight * .8)) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 120)); }
      window.scrollTo(0, h); await new Promise(r => setTimeout(r, 300));
      window.scrollTo(0, 0); await new Promise(r => setTimeout(r, 300));
    }""")


def run(paths, shots=False, base=BASE):
    os.makedirs(SHOTS, exist_ok=True)
    report = {}
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for path in paths:
            for (w, h) in ((1440, 900), (390, 844)):
                ctx = browser.new_context(viewport={'width': w, 'height': h})
                ctx.add_init_script("try { localStorage.setItem('rvh:cookie-choice', 'qa'); } catch (e) {}")
                page = ctx.new_page()
                errors, failed = [], []
                page.on('console', lambda m: errors.append(m.text) if m.type in ('error', 'warning') else None)
                page.on('requestfailed', lambda r: failed.append(r.url))
                page.on('response', lambda r: failed.append('%s %s' % (r.status, r.url)) if r.status >= 400 else None)
                page.goto(base + path, wait_until='networkidle')
                page.add_style_tag(content=HIDE_SB)
                page.evaluate("() => { try { localStorage.setItem('rvh:cookie-choice', 'qa'); } catch (e) {} document.querySelector('[data-cookie]') && (document.querySelector('[data-cookie]').hidden = true); }")
                page.wait_for_timeout(2600)
                scroll_through(page)
                page.wait_for_timeout(1400)
                res = page.evaluate(CHECK_JS)
                res['header'] = page.evaluate(HEADER_JS)
                res['console'] = errors
                res['failed'] = failed
                key = '%s@%d' % (path, w)
                report[key] = res
                if shots:
                    name = path.replace('/', '_').replace('.html', '')
                    total = page.evaluate('document.documentElement.scrollHeight')
                    n, y = 0, 0
                    page.mouse.move(w - 2, h - 2)
                    while y < total:
                        page.evaluate('y => window.scrollTo(0, y)', y)
                        page.wait_for_timeout(450)
                        page.screenshot(path=os.path.join(SHOTS, '%s-%d-%02d.png' % (name, w, n)))
                        n += 1
                        y += h
                ctx.close()
            # reduced motion: nothing should be animating once loaded
            ctx = browser.new_context(viewport={'width': 1440, 'height': 900}, reduced_motion='reduce')
            page = ctx.new_page()
            page.goto(base + path, wait_until='networkidle')
            page.wait_for_timeout(500)
            report['%s@reduce' % path] = page.evaluate("() => document.getAnimations().filter(a => a.playState === 'running').map(a => (a.effect && a.effect.target && a.effect.target.className) + ':' + (a.animationName || a.transitionProperty || ''))")
            ctx.close()
        browser.close()
    return report


if __name__ == '__main__':
    argv = sys.argv[1:]
    base = BASE
    if '--base' in argv:  # --base URL (was documented but never read)
        i = argv.index('--base')
        base = argv[i + 1].rstrip('/') + '/'
        del argv[i:i + 2]
    args = [a for a in argv if not a.startswith('--')]
    print(json.dumps(run(args, shots='--shots' in argv, base=base), indent=1, ensure_ascii=False))
