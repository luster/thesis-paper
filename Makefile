all:
	xelatex paper.tex
	bibtex paper
	xelatex paper.tex
	xelatex paper.tex
