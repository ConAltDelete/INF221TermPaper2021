TERM PAPER
==========

The file structure used in this repository is:

```
.\
+--aux_files       (auxilary files for LaTex)
|
+--tex             (Source files for LaTex, and bibtex)
|  +---pic         (pictures used for illustrations)
|  \---main.tex    (Source code for LaTex)
|
+--code            (Code used for illustration)
|  +--results      (results from testing, data, and pictures)
|
+--Lib             (python folder)
|
+--Scripts         (enviroment folder)
|
+--task            (folder for mandetory taskes)
|
\--TermPaper_2021  (The task given to us, pluss template)
Makefile           (Makefile to automate LaTex and illustation generation)
README
term_notes.md
termpaper.pdf      (Finale version of our paper)
```

Deeper notes of folders and its relation with others:
-----------------------------------------------------

### CODE:

In the "**Code**" folder is containing primarily files with their own implementation of algorithms. The files has the file format of "\<algorithm + _ + limit/quirk\>.py". The file `test.py` generates several csv files containing data on the algorithms regarding average performance, the minimum, and maximum time.

The python code used uses python 3.9 to use the `type hint`-feature for somewhat clearer code.

### TASK:

"TASK" folder is to be ignored regarding the term paper as it only contains mandatory tasks not related to the paper.

### TERMPAPER_2021

This folder contains the description of the purpose of the paper.

Requirements
------------

- Python 3.9 [^2]
- make or gmake [^1]
- xelatex

LOG:
----

20211007:

	<Mats>: Updated README.md, and read though the term_paper description.
		The formulation of the structure of the workflow is important but expect it to fall fairly quickly without knowning how, and why. I guess it's nature.
20211008:

	<Mats>: Updated README.md
		Added an title page, because I wanted it. Going to attempt to work on one of the algorithms tomorrow; Warning to those with a heart condision, PEP8 will be violated in this attempt.
		I have created the "test.py" where we can test an function and gets its average time. I just need to make the pipe-script to pipe every algoritm in the folder to get a table of time for each.
20211009:

	<Mats>: Updated README.md, and made better progressbar. Still need to perform a test for my `test.py` to se if everything is working, as of now everything is hypothetical. And I need to add an makefile argument for just updating data. But first testing... later...
20211012:
	
	<Mats>: Added a whole lot of stuff, like error handeling, quicksort, fixed a bug regarding testing. However We still need to figure out quicksort as when given a sorted list it will loop len(list) as its default parition is way off.
20211014:

	<Mats>: Made the bibliografhy work and figured out how to section off the paper. Just need to create a script (Thinking to do it in R) to convert `csv` files to diagrams and analasys. Other than that, I think we are well on our way to finish first draft.
[^1]: One can run the commands in sequence manually if this is not an option.
[^2]: You can now an venv.
