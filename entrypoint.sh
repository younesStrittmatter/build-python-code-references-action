#!/bin/sh -l

set -e

cd $GITHUB_WORKSPACE

python generate_readme.py $1 $2
