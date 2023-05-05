#!/bin/sh -l

set -e

cd /

python generate_readme.py $1 $2
