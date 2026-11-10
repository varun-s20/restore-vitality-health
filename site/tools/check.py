"""Restore Vitality Health: static check of the built site (no browser).

Fails on: broken internal links or assets, missing #anchors, zero or several h1s, duplicate titles or
descriptions, missing canonical, images without alt, srcset without sizes, inline style attributes, lorem,
em dashes or AI attribution in shipped files. Reports (does not fail on) bracketed copy placeholders, which
Varun asked to keep visible this round, and dashes inside the client's verbatim legal text.
Run from site/: python tools/check.py
"""
import glob
import os
import re
import sys
from collections import Counter

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEGAL = {'privacy.html', 'terms.html', 'medications-safety-information.html', 'telehealth-and-medical-info.html', 'do-not-sell.html'}


def main():
    os.chdir(SITE)
    pages = sorted(glob.glob('*.html') + glob.glob('es/*.html'))
    errors, notes = [], []
    titles, descs = Counter(), Counter()
    ids = {}
    for p in pages:
        html = open(p, encoding='utf-8').read()
        ids[os.path.normpath(p)] = set(re.findall(r'\sid="([^"]+)"', html))
    for p in pages:
        html = open(p, encoding='utf-8').read()
        base = os.path.dirname(p)
        name = os.path.basename(p)
        if len(re.findall(r'<h1[\s>]', html)) != 1:
            errors.append('%s: h1 count %d' % (p, len(re.findall(r'<h1[\s>]', html))))
        t = re.search(r'<title>(.*?)</title>', html)
        d = re.search(r'<meta name="description" content="(.*?)">', html)
        lang = 'es' if os.path.normpath(p).startswith('es' + os.sep) else 'en'
        # within one language: product names stay in English in both, by the copy deck's rule
        titles[(lang, t.group(1) if t else '')] += 1
        descs[(lang, d.group(1) if d else '')] += 1
        if 'rel="canonical"' not in html:
            errors.append('%s: no canonical' % p)
        for img in re.findall(r'<img\b[^>]*>', html):
            if ' alt=' not in img:
                errors.append('%s: img without alt %s' % (p, img[:80]))
            if 'srcset=' in img and 'sizes=' not in img:
                errors.append('%s: srcset without sizes' % p)
        if re.search(r'\sstyle="', html):
            errors.append('%s: inline style' % p)
        if re.search(r'lorem', html, re.I):
            errors.append('%s: lorem' % p)
        if re.search(r'generated with|claude|chatgpt|openai', html, re.I):
            errors.append('%s: AI attribution' % p)
        body = re.sub(r'<script.*?</script>', '', html, flags=re.S)
        if '\u2014' in body or '\u2013' in body:
            (notes if name in LEGAL else errors).append('%s: em or en dash%s' % (p, ' (client legal text, verbatim)' if name in LEGAL else ''))
        for ph in sorted(set(re.findall(r'\[[A-Z][^\]<]{2,60}\]', re.sub(r'<[^>]+>', ' ', body)))):
            notes.append('%s: placeholder %s' % (p, ph))
        for ref in re.findall(r'(?:href|src)="([^"]+)"', html) + [u.split(' ')[0] for s in re.findall(r'srcset="([^"]+)"', html) for u in s.split(', ')]:
            if re.match(r'(https?:|mailto:|tel:|#$)', ref):
                continue
            path, _, frag = ref.partition('#')
            target = os.path.normpath(os.path.join(base, path)) if path else p
            if path and not os.path.exists(target):
                errors.append('%s: missing %s' % (p, ref))
            elif frag and target.endswith('.html') and frag not in ids.get(os.path.normpath(target), set()):
                errors.append('%s: missing anchor %s' % (p, ref))
    for k, n in list(titles.items()) + list(descs.items()):
        if n > 1:
            errors.append('duplicate title or description (%d): %s' % (n, k[1][:80]))
    for f in ['assets/global.css', 'assets/global.js']:
        if '\u2014' in open(f, encoding='utf-8').read():
            errors.append('%s: em dash' % f)
    print('%d pages checked' % len(pages))
    print('ERRORS (%d)' % len(errors), *errors[:80], sep='\n  ')
    ph = Counter(re.sub(r'^.*?placeholder ', '', n) for n in notes if 'placeholder' in n)
    print('NOTES: placeholders kept visible (pages):', dict(ph))
    print('NOTES:', *[n for n in notes if 'placeholder' not in n], sep='\n  ')
    sys.exit(1 if errors else 0)


if __name__ == '__main__':
    main()
