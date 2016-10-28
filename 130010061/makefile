main :   
	mkdir output
	cd input && python vanderpol.py
	mv input/*.png output/
	jupyter nbconvert --execute --to html input/130010061.ipynb
	mkdir output/html_file
	mkdir output/animations
	mv input/130010061.html output/html_file
	mv input/*.mp4 output/animations
	make report

report: 
	cp input/Ref.bib  ./output
	cp input/report.tex  ./output
	cd output && pdflatex report.tex
	cd output && bibtex report.aux
	cd output && pdflatex report.tex
	cd output && pdflatex report.tex
	mkdir output/images
	cd output && mv *.png ./images  


.PHONY: clean tests

clean:	 
	rm -rf output
	rm -rf input/__pycache__
