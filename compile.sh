#!/bin/bash

pdflatex thesisTemplate #compile *.tex file
pdflatex thesisTemplate #compile *.tex file again for including images ref
bibtex thesisTemplate   #compile *.tex file again for including references
pdflatex thesisTemplate #compile *.tex file again for final version
pdflatex thesisTemplate #compile *.tex file again for final version
echo "Done"

