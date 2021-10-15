LaTex: ./tex/main.tex
	xelatex --include-directory=./data/ --aux-directory=./aux_files/ --enable-installer --job-name=termpaper $?

./aux_files/termpaper.aux: ./tex/main.tex
	gmake LaTex

bibUpdate: ./tex/main.tex ./tex/INF221.bib ./aux_files/termpaper.aux
	biber ./aux_files/termpaper
	gmake LaTex
	gmake LaTex

data: .\code\python\variabler.py .\code\python\test.py
	python .\code\python\test.py

termpaper.pdf: .\tex\main.tex .\data\
	xelatex --include-directory=./data/ --aux-directory=./aux_files/ -enable-installer -job-name=termpaper $? 

./data/*.csv: ./code/python/test.py
	gmake data

clean:
	del .\aux_files /s /q
