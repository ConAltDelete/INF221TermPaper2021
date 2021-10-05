LaTex: ./tex/main.tex
	xelatex -aux-directory=./aux_files/ -enable-installer -job-name=termpaper $?

bibUpdate: ./tex/main.tex ./tex/main.bib
	bibtex -job-name=termpaper ./tex/main
	for round in 1 2 ; do \
		xelatex -aux-directory=./aux_files/ -enable-installer -job-name=termpaper $< ; \
	done

clean:
	rm ./aux_files/*
