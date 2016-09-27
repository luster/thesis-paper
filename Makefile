all:
	#xelatex -shell-escape paper.tex
	#bibtex paper
	#xelatex -shell-escape paper.tex
	#xelatex -shell-escape paper.tex
	xelatex  paper.tex
	bibtex paper
	xelatex  paper.tex
	xelatex  paper.tex
