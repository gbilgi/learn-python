"""

"""
def duplicate_lines(file_path):

    d = {}
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip('\n')
            if line in d:
                d[line] += 1
            else:
                d[line] = 1

    li = []
    for key, value in d.items():
        if value > 1:
            li.append(key)

    return li                  


from pathlib import Path
SCRIPT_DIR = Path(__file__).resolve().parent

file1 = SCRIPT_DIR /"duplicates_basic.log"
file2 = SCRIPT_DIR /"duplicates_order.log"
file3 = SCRIPT_DIR /"duplicates_with_empty_lines.log"
file4 = SCRIPT_DIR /"large_duplicates.log"
file5 = SCRIPT_DIR /"no_duplicates.log"

print(duplicate_lines(file4))