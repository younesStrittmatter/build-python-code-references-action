import os
import re
import sys

# Define the string pattern to be replaced
pattern = r'<!-- include:\s*(\S+)\s*-->'

# Define the path to the input file, relative to root
input_file_path = sys.argv[1]

# Define the path to the output file, relative to root
output_file_path = sys.argv[2]

# Get the path to the directory of the script file
script_dir_path = os.path.dirname(os.path.abspath(__file__))

# Get the path to the root directory
root_dir_path = os.path.abspath(os.path.join(script_dir_path, os.pardir))

# Get the absolute path to the input file
# input_file_abs_path = os.path.join(root_dir_path, input_file_path)

with open(input_file_path, 'r') as f:
    # Read the contents of the input file
    text = f.read()

    # Find all occurrences of the string pattern
    matches = re.findall(pattern, text)

    # Loop through each match and replace it with the contents of the included file
    for match in matches:
        included_file_path = os.path.join(root_dir_path, match)
        with open(included_file_path, 'r') as included_file:
            included_text = included_file.read()
        text = text.replace('<!-- include:{} -->'.format(match), included_text)

# Get the absolute path to the output file
output_file_abs_path = os.path.join(root_dir_path, output_file_path)

with open(output_file_path, 'w') as f:
    # Write the modified contents to the output file
    f.write(text)
