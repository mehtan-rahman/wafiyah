LATEX = xelatex -interaction=nonstopmode -halt-on-error -output-directory=build
all: build/main.pdf
build/main.pdf: main.tex preamble.tex frontmatter.tex pages/*.tex
	mkdir -p build
	rm -f build/main.[0-9]*   # reledmac section files: stale ones can break the first pass
	$(LATEX) main.tex >/dev/null || (grep -A3 '^!' build/main.log; exit 1)
	for i in 2 3 4 5 6 7 8 9 10; do $(LATEX) main.tex >/dev/null; done   # reledmac refs + table auto-fill converge over passes
	cp build/main.pdf wafiyah.pdf
	@awk 'NR==1{o=$$2-$$1} $$2-$$1!=o{print "PAGE DRIFT: lithograph p."$$1" spilled onto an extra page"; bad=1} END{exit bad}' build/main.map && echo "OK  every lithograph page is on its own page"
# check one page in isolation:  make check P=p012
check:
	mkdir -p build
	printf '\\documentclass[10pt]{article}\\input{preamble}\\begin{document}\\input{pages/$(P)}\\finishnumbering\\end{document}\n' > build/check_$(P).tex
	cd build && TEXINPUTS=..: xelatex -interaction=nonstopmode -halt-on-error check_$(P).tex >/dev/null || (grep -B2 -A6 "^!" check_$(P).log; exit 1)
	cd build && TEXINPUTS=..: xelatex -interaction=nonstopmode -halt-on-error check_$(P).tex >/dev/null
	@echo "OK  build/check_$(P).pdf"
clean:
	rm -rf build
.PHONY: all check clean
