#!/bin/sh -l

set -e

# Get the absolute path to the generate_readme.py script
generate_readme_script_path="/generate_readme.py"

# Get the full paths for the input and output files
input_file="$GITHUB_WORKSPACE/$1"
output_file="$GITHUB_WORKSPACE/$2"

# Execute the generate_readme.py script with the provided arguments
python $generate_readme_script_path $input_file $output_file
