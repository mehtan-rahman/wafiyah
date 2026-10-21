#!/usr/bin/env python3
"""Render a zoomed crop of a manuscript page for reading harakat.

usage: zoom.py PAGE [REGION] [DPI]
  PAGE   printed page number (1-84)
  REGION one of: full, top, bottom, left, right, tl, tr, bl, br,
         or four fractions x0,y0,x1,y1 of the page (e.g. 0.5,0,1,0.5 = top-left... see note)
  DPI    default 300
Output: build/zoom_pPAGE_REGION.png  (path printed)
Note: fractions are measured from the page's left/top edge.
"""
import sys, os, fitz
pdf = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'manuscript.pdf')
page = int(sys.argv[1]); region = sys.argv[2] if len(sys.argv) > 2 else 'full'
dpi = int(sys.argv[3]) if len(sys.argv) > 3 else 300
regions = {'full': (0,0,1,1), 'top': (0,0,1,.5), 'bottom': (0,.5,1,1), 'left': (0,0,.5,1), 'right': (.5,0,1,1),
           'tl': (0,0,.5,.5), 'tr': (.5,0,1,.5), 'bl': (0,.5,.5,1), 'br': (.5,.5,1,1)}
fr = regions.get(region) or tuple(float(v) for v in region.split(','))
d = fitz.open(pdf); p = d[page-1]; r = p.rect
clip = fitz.Rect(r.x0 + fr[0]*r.width, r.y0 + fr[1]*r.height, r.x0 + fr[2]*r.width, r.y0 + fr[3]*r.height)
out = os.path.join(os.path.dirname(pdf), 'build', f'zoom_p{page:03d}_{region.replace(",","_")}.png')
os.makedirs(os.path.dirname(out), exist_ok=True)
p.get_pixmap(dpi=dpi, clip=clip).save(out); print(out)
