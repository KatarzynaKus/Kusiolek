#!/bin/bash
ANKIETA="ankieta/"
PROJECTDIR="$PWD/$ANKIETA"
export PROJECTDIR=$PROJECTDIR
sdaps sdaps_files setup_tex ankieta/questionnaire.tex
