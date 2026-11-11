"""
Problem Description:
You are given a web server access log. Each line contains an HTTP request. Your task is to parse the log and return the URL (request target) that was requested the most times.

Ignore HTTP method, protocol version, status code, and other fields — only the request target matters.

If multiple URLs have the same highest request count, return the one which attains the highest count first while scanning the file from top to bottom.

Input Format:
A plain text access log with one entry per line, where each request is represented in quotes as: "METHOD <URL> HTTP/<version>".

Output Format:
Return the most frequently requested URL as a string.
"""

import re


def most_requested_url(file_path):
    url = ""
    max_count = 0
    d = {}

    pattern = re.compile(r"([A-Z]+)\s+(\S+)\s+HTTP/\d+(?:\.\d+)?")

    with open(file_path, 'r') as file:
        for line in file:
            ans = pattern.search(line)

            if ans:
                current_url = ans.group(2)

            if current_url in d:
                d[current_url] += 1
            else:
                d[current_url] = 1

            if d[current_url] > max_count:
                max_count = d[current_url]
                url = current_url

    return url

from pathlib import Path
SCRIPT_DIR = Path(__file__).resolve().parent


file1 = SCRIPT_DIR / "access_example.log"
file2 = SCRIPT_DIR / "all_unique.log"
file3 = SCRIPT_DIR / "large_access.log"
file4 = SCRIPT_DIR / "tie_breaker.log"

print(most_requested_url(file1))
