LaTex: ./tex/main.tex
	xelatex -aux-directory=./aux_files/ -enable-installer -job-name=termpaper $?

./aux_files/termpaper.aux: ./tex/main.tex
	make LaTe
	./aux_files/termpaper.aux: ./tex/main.tex
	make LaTex

bibUpdate: ./tex/main.tex ./tex/INF221.bib ./aux_files/termpaper.aux
	bibtex -job-name=termpaper ./aux_files/termpaper
	for round in 1 2 ; do \
		xelatex -aux-directory=./aux_files/ -enable-installer -job-name=termpaper $< ; \
	done
data: .\code\variabler.py .\code\test.py
	python .\code\test.py

termpaper.pdf: .\tex\main.tex
	xelatex -aux-directory=./aux_files/ -enable-installer -job-name=termpaper $? 

clean:
	rm ./aux_files/*
