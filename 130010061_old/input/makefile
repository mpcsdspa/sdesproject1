FILES := report.pdf
AUXFILES := $(FILES:.pdf=.aux)
LOGFILES := $(FILES:.pdf=.log)
BBLFILES := $(FILES:.pdf=.bbl)
BLGFILES := $(FILES:.pdf=.blg)
OUTFILES := $(FILES:.pdf=.out)
PICS := $(wildcard *.png)
PICSDEL := $(filter-out vanderpol.png,$(PICS))
PYC := $(wildcard *.pyc)

main :
	python vanderpol.py
	make pdf

pdf : $(FILES:.pdf=.tex)
	make report.pdf

%.pdf: %.tex
	pdflatex $<
	bibtex `echo $< |cut -d "." -f1`.aux
	pdflatex $<
	pdflatex $<

.PHONY: clean clean-all
clean-all:
	$(RM) $(AUXFILES) $(FILES) $(OUTFILES) $(LOGFILES) $(BBLFILES) $(BLGFILES) $(OTHERS) $(PICSDEL) $(PYC) $(PICS)

clean:
	$(RM) $(AUXFILES) $(LOGFILES) $(BBLFILES) $(OUTFILES) $(BLGFILES) $(OTHERS) $(PICSDEL) $(PYC)
