# الوافية — Critical edition (taḥqīq)

LaTeX critical edition of *Wāfiyah* (Mawlānā Muḥammad Mīrān Bāqawī Qāsimī), a ṣarf
textbook of the Dars-i Niẓāmī curriculum, transcribed from the Hyderabad lithograph
(`manuscript.pdf`, 84 pages).

- `make` — build `wafiyah.pdf` (XeLaTeX, four passes: reledmac + RTL needs them). **PDF page N is printed page N**: one page per printed page, with the lithograph's frame and number box; `build/main.map` lists `printed-page absolute-page` and must read `N N` throughout.
- The editor's own title page (`frontmatter.tex`) is not included by default so that the page numbers match; enable the `\include{frontmatter}` line in `main.tex` when adding editorial front matter (give it roman numerals).
- `make check P=p012` — compile one page in isolation.
- `printf '%s\n' '\facsimiletrue' > facsimile.cfg && make` — facsimile mode: each page's scan precedes its transcription.
- `REVIEW.md` — every reading flagged `\unclear`, `\com` or `TODO` during transcription, by page; work through it against the scans.
- `CONVENTIONS.md` — transcription rules and the editorial macros (`\tq`, `\corr`, `\com`, `\unclear`).
- `pages/pNNN.tex` — one file per printed page; `scans/pNNN.jpg` — the scans.
- `tools/zoom.py` — render a 300-dpi crop of a page for reading harakat.

Requirements: TeX Live 2024+ (reledmac, polyglossia) and the *Noto Nastaliq Urdu* font; the Arabic font, Scheherazade New, ships in `fonts/`
(ships with macOS; otherwise install it from Google Fonts).
