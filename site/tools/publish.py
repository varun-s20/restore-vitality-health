"""Restore Vitality Health: copy the public website into ../dist for deploying.

Run from site/ after build.py:  python tools/publish.py
dist/ gets only what visitors load: the built pages (EN and es/), assets/, robots.txt and sitemap.xml.
The page sources (src/), data/ and tools/ stay out of it. dist/ is rebuilt from scratch each run.
"""
import glob
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(HERE)
DIST = os.path.join(os.path.dirname(SITE), 'dist')

if os.path.isdir(DIST):
    shutil.rmtree(DIST)
os.makedirs(DIST)
for f in glob.glob(os.path.join(SITE, '*.html')) + [os.path.join(SITE, n) for n in ('robots.txt', 'sitemap.xml')]:
    shutil.copy2(f, DIST)
shutil.copytree(os.path.join(SITE, 'es'), os.path.join(DIST, 'es'))
shutil.copytree(os.path.join(SITE, 'assets'), os.path.join(DIST, 'assets'))
pages = len(glob.glob(os.path.join(DIST, '*.html'))) + len(glob.glob(os.path.join(DIST, 'es', '*.html')))
print('dist ready: %d pages in %s' % (pages, DIST))
