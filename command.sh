#!/bin/bash
#
# $1 -> folder name
# $2 -> project name
function create() {
    python ~/<script path> $1 $2
    cd $1
    code .
}