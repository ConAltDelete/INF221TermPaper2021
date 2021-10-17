termpaper.pdf: .\code\python\%.py ./tex/%.bib ./tex/%.tex

LaTex: ./tex/main.tex
	xelatex --include-directory=./data/ --aux-directory=./aux_files/ --enable-installer --job-name=termpaper $?

./aux_files/termpaper.aux: ./tex/main.tex
	gmake LaTex

bibUpdate: ./tex/main.tex ./tex/INF221.bib ./aux_files/termpaper.aux
	biber ./aux_files/termpaper
	gmake LaTex
	gmake LaTex

./tex/%.bib:
	gmake bibUpdate

./tex/%.tex:
	gmake LaTex

data: .\code\python\variabler.py .\code\python\test.py
	python .\code\python\test.py

pic: .\code\R\csv2plot.R
	.\langs\R-4.1.1\bin\Rscript.exe $?

./code/python/%.py:
	gmake data

clean:
	del .\aux_files /s /q
	del .\data /s /q
