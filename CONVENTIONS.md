# Wafiyah — transcription & editing conventions

Critical edition (taḥqīq) of *Wāfiyah* by Mawlānā Muḥammad Mīrān Bāqawī Qāsimī
(Sabīl al-Falāḥ, Hyderabad, lithograph dated 8 Shawwāl 1396 / 3 Oct 1976).
Source: `manuscript.pdf` (84 scanned pages). Page scans: `scans/pNNN.jpg`.
Printed page number == edition page number == file number (the front matter comes first).

## Layout

| path | purpose |
|---|---|
| `main.tex` | document; inputs every page file in order |
| `preamble.tex` | fonts, polyglossia/bidi, reledmac apparatus, editorial macros (do not edit while transcribing) |
| `frontmatter.tex` | edition title page and key to the editorial signs (numbered أ، ب) |
| `pages/pNNN.tex` | one file per printed page, `NNN` zero-padded (p004 … p084) |
| `scans/pNNN.jpg` | the scan of that page (170 dpi) |
| `facsimile.cfg` | optional: contains `\facsimiletrue` to put each scan before its transcription |
| `Makefile` | `make` builds `wafiyah.pdf`; `make check P=p012` compiles one page alone |

Engine: XeLaTeX. Arabic in Scheherazade New (SIL, OFL; in `fonts/`), Urdu and the title in Noto Nastaliq Urdu.

## Page file skeleton

```latex
% p.12 — الباب الخامس في أوزان الثلاثي المجرد
\mspage{12}
\bab{الباب الخامس في أوزان الثلاثي المجرد}
\pstart
الثلاثي المجرد فعل يكون ماضيه على ثلاثة أحرف … وهي ستة أبواب
\pend
\begin{sarf}{|c|c|c|c|c|}
\thead{} & \thead{ماضي} & \thead{مضارع} & \thead{أمر} & \thead{نهي}\\\hline
(1) & فَعَلَ & يَفْعَلُ & اِفْعَلْ & لَا تَفْعَلْ\\
\end{sarf}
```

Rules:

1. **Every page file starts with `\mspage{N}`** (N = printed page number). It resets
   reledmac line numbering so apparatus notes cite *page + line*.
2. **All text must sit inside `\pstart … \pend`** (reledmac). `\bab`, `\subbab` and the
   `sarf` environment already do this; free prose needs explicit `\pstart`/`\pend`.
   Never nest them.
3. **Chapters**: `\bab{الباب الثالث في المنفيات}` at the top of the page where the chapter begins.
   It prints no heading: the chapter is named in the header strip (top right) of its pages.
   Mid-page headings (e.g. `اسم آلة`, `قانون`, `تمرين` as a block title): `\subbab{…}`.
4. **One printed page = one PDF page.** The PDF page number is the printed page number and
   the lithograph's frame and number box are drawn automatically. A page must not overflow:
   reproduce the lithograph's arrangement with the layout environments below.
   - **Side-by-side tables** (most pages with several boxes): `\begin{tables} \begin{sarf}…\end{sarf} \begin{sarf}…\end{sarf} \end{tables}`,
     tables listed right-to-left. A prose block standing beside tables: `\sidetext{<width>}{<text>}` inside `tables`.
     The whole row is scaled to the text width/height if needed.
   - **Two-column pages** (pp. 63–83): `\begin{twocol} \begin{rightcol} … \end{rightcol} \begin{leftcol} … \end{leftcol} \end{twocol}`.
     Inside a column do **not** write `\pstart`/`\pend`; the column is one numbered block and items are
     separated by `\par`. `sarf` tables, `\subbab` and `\bab` work inside a column. A `\bab` heading
     that spans the page goes *before* `\begin{twocol}`. Nothing may follow `\end{twocol}` on that page.
     Line numbers of the right column carry ي in the apparatus. reledpar sets the two columns line
     by line, so when the columns hold tables of unequal height use `rightbox`/`leftbox` instead
     (each column then flows independently; its apparatus cites the column as one line).
   - **Stacked tables** that must share the page height: `\begin{stack} \begin{sarf}…\end{sarf}\\[6pt] \begin{sarf}…\end{sarf} \end{stack}` (p.19).
   - A single `sarf` table that is too wide/tall is scaled down automatically.
   - **Auto-fill**: like the lithograph, each page's tables fill the frame. All tables on a page share
     one type size (natural size at most, smaller only if they don't fit) and one row height; the
     space the page has left goes into taller rows (never shorter than 1.55× the line, so the vowel
     marks have room). This needs the Makefile's passes; a single `make check` shows the unfilled first
     pass. Two-column pages are not auto-filled.
   - A column number in a header, `\thead{(19) مثال واوي}`, is set beside the title as a small circled figure.
   - **If a page still overflows** (the page is 116×180 mm, close to the lithograph's own proportions):
     put `\tablereserve{N}` right after `\mspage` to keep N lines (default 5) free under a
     page-high table for a long apparatus, or `\densepage{9}` to set that page's prose at 9pt
     (used on prose-heavy pages: 2, 36, 69–71, 75–83). Both reset at the next `\mspage`.
5. **Tables**: `\begin{sarf}{<colspec>} … \end{sarf}`. Column spec and cells are written
   **right-to-left in the order they appear on the page** (bidi flips the table).
   Tables are drawn in booktabs style: vertical rules in the column spec are ignored,
   `\hline` becomes `\midrule` and `\cline{a-b}` becomes `\cmidrule`, so keep writing `|`, `\hline`, `\cline`
   where the lithograph has rules (they document the original grid).
   Column headers with `\thead{…}` (printed bold on a grey ground; use it for every header cell,
   including block titles in the middle of a column, and `\thead{}` for an empty header cell).
   A label the lithograph writes on two lines inside one cell: `\twoline{اسم ظرف}{زمان ومكان}`.
   Tables in a `tables` row are joined into one grid (shared top/bottom rules, thin rule between).
   Every row gets a light hairline beneath it automatically; on a page whose tables use
   `\multirow` put `\nohairlines` right after `\mspage` (the hairline would cut the merged cell).
   `\x` and `\ditto` print in grey so the real forms stand out.
   Body cells are aligned automatically: within each section of a column (the cells between two
   header rows) the forms share one starting (right) edge, so particles like لا / لم / ما line up,
   and that block is centred in the column (measured on one pass, applied on the next). A ditto/الخ
   after a form goes to the far edge; a lone ditto or `\x` stays centred; headers are centred.
   This applies to `c` and `r` columns alike (not to tables inside two-column pages). A `تمرين` header row inside the table is a normal row of
   `\thead{تمرين}` cells followed by `\hline`.
   Circled column numbers in headings (①②…) are written as `(5)` before the title:
   `\thead{(5) مضارع مجهول}`.
   Use `p{…}` columns or `\multirow` only where needed for prose cells (p.14, p.18).
   Where the lithograph layout is genuinely complex, prefer *content fidelity and
   reading order* over mimicking the grid, and leave a `%` comment describing the layout.
6. **Vocalisation**: transcribe the ḥarakāt **as printed**, including the sukūn the
   lithograph puts on letters of prolongation (فَعَلُوْا، يَفْعَلُوْنَ، تَفْعَلِيْنَ) and shadda/tanwīn.
   Do not "correct" vowels silently. Hamza: write it as printed (أ/إ/ا).
7. **Special cells**:
   - `\x` — the × the lithograph uses for a non-existent form
   - `\ditto` — the ditto mark (〃 / ״) meaning "same as the cell above / to the right"
   - `\ilkh` — الخ (etc.)
   - `\gap` — illegible or blank cell
8. **Uncertain readings** (smudged, cut off, ambiguous vowel): `\unclear{reading}`.
   It prints the reading with a † and files an apparatus note automatically.
   Use it generously; the muḥaqqiq will resolve them.
9. **Apparent misprints**: do **not** emend during transcription. Transcribe as printed
   and attach `\com{lemma}{كذا في الأصل، ولعل الصواب: …}` so the editor can decide.
   The editor's own tools later: `\corr{ms}{emended}` (emended text, ms reading in
   apparatus A) and `\tq{lemma}{note}` (variant/reading note in apparatus A).
10. **Urdu prose** (pp. 2, 84 and any Urdu glosses): wrap in `\begin{urduprose} … \end{urduprose}`
   with `\pstart`/`\pend` inside. Short Urdu words inside Arabic text: `\textUrdu{…}` is not
   defined; use `{\urdufont …}`.
11. **Digits**: type Western digits (`1`, `12`); the fonts render them as ١٢ / ۱۲.
12. **Comments**: first line `% p.NN — <chapter title>`. Flag anything doubtful with
    `% TODO:` next to the row.
13. **Check before you finish**: `make check P=pNNN` must print `OK` **and** the page must fit on one PDF page (check `build/check_pNNN.pdf` has 1 page).

## Apparatus series

- **A** (`\Afootnote`): readings of the lithograph, uncertain readings, emendations. Set in two
  columns (the notes are short). `\unclear` files «غير واضحة في الأصل».
- **B** (`\Bfootnote`): editor's commentary. Each note is its own paragraph, so long notes wrap.
