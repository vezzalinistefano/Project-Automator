#!/bin/bash
#
# $1 -> folder name
# $2 -> project name
function creator() {
    python ~/Documents/Projects/Project-Automator/prjCreator.py $1 $2
    cd $1
}