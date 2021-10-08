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

In the "**Code**" folder is containing primarily files with their own implementation of algorithms. The files has the file format of "\<algorithm + _ + limit/quirk\>.py".

### TASK:

"TASK" folder is to be ignored regarding the term paper as it only contains mandatory tasks not related to the paper.

### TERMPAPER_2021

This folder contains the description of the purpose of the paper.


LOG:
----

20211007:

	<Mats>: Updated README.md, and read though the term_paper description.
		The formulation of the structure of the workflow is important but expect it to fall fairly quickly without knowning how, and why. I guess it's nature.
20211008:

	<Mats>: Updated README.md
		Added an title page, because I wanted it. Going to attempt to work on one of the algorithms tomorrow; Warning to those with a heart condision, PEP8 will be violated in this attempt.
		I have created the "test.py" where we can test an function and gets its average time. I just need to make the pipe-script to pipe every algoritm in the folder to get a table of time for each.
