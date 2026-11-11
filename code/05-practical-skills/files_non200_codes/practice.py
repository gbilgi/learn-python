"""
Problem Description
You are given the path to a log file.
Each line in the file may contain an HTTP status code such as 200, 404, 500, etc.

Your task is to find and return all log lines that contain a non-200 HTTP status code.

Only the first 3-digit number in each line is considered the status code.
Ignore lines that do not contain any 3-digit number.
HTTP status codes are always 3-digit integers.

Input Format
Log File Contains multiple lines.Each line may or may not contain an HTTP status code.

Output Format
Return a list of strings, where each string is a log line whose first status code is not 200.
If no lines match, return an empty list.
"""

import re

def find_non_200_status_codes(file_path):

    # Code here
    pass
                       

from pathlib import Path
SCRIPT_DIR = Path(__file__).resolve().parent


file1 = SCRIPT_DIR / "app_debug.log"
file2 = SCRIPT_DIR / "app_logs.log"
file3 = SCRIPT_DIR / "complex.log"

print(find_non_200_status_codes(file3))
