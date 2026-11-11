"""
Problem Description
You are given the path to a text file.
Each line in the file may contain letters, symbols, whitespace, and digits (0-9).

Your task is to find and return the line that contains the maximum number of digit characters.

A digit is any character from '0' to '9'.
If multiple lines contain the same maximum number of digits, return the first such line.
Ignore all non-digit characters while counting digits.
"""
def max_digit_line(file_path):

    # Code here
    pass



from pathlib import Path
SCRIPT_DIR = Path(__file__).resolve().parent

file1 = SCRIPT_DIR /"file1_basic.txt"
file2 = SCRIPT_DIR /"file2_tie_case.txt"
file3 = SCRIPT_DIR /"file4_empty_lines.txt"
file4 = SCRIPT_DIR /"file5_large_line.txt"
file5 = SCRIPT_DIR /"file6_large_content.txt"
file6 = SCRIPT_DIR /"file7_large_content_2.txt"

print(max_digit_line(file1))