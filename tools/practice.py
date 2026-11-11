#!/usr/bin/env python3
"""Helper for the practice-problems section.

  python tools/practice.py init                    create folders and the topic pages
  python tools/practice.py new 3 "Sum of digits"   add a problem to topic 3
  python tools/practice.py list                    show topics and problem counts
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CODE = ROOT / "code" / "05-practical-skills"
DOCS = ROOT / "docs" / "05-practical-skills" / "practice"
FENCE = "`" * 3

TOPICS = [
    ("01-data-types", "Data Types"),
    ("02-operators-and-control-statements", "Operators and Control Statements"),
    ("03-iteration", "Iteration: Loops & Iteration Analysis"),
    ("04-lab-iteration", "Lab Session on Iteration"),
    ("05-functions", "Functions"),
    ("06-1d-list", "1D List"),
    ("07-2d-list", "2D List"),
    ("08-lab-list", "Lab Session on List"),
    ("09-tuples-and-strings", "Tuples & Strings"),
    ("10-sets-and-dictionaries", "Sets and Dictionaries"),
    ("11-file-and-exception-handling", "File & Exception Handling"),
    ("12-interview-problems", "Interview Problems"),
]


def slugify(text):
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")


def count_problems(slug):
    return len(list((CODE / slug).glob("[0-9][0-9]_*.py")))


def init():
    DOCS.mkdir(parents=True, exist_ok=True)
    for i, (slug, title) in enumerate(TOPICS, 1):
        folder = CODE / slug
        folder.mkdir(parents=True, exist_ok=True)
        if not any(folder.iterdir()):
            (folder / ".gitkeep").touch()
        page = DOCS / f"{slug}.md"
        if not page.exists():
            page.write_text(
                f"# {i:02d} - {title}\n\n"
                f"Practice problems for **{title}**. Each problem has the statement, "
                f"the expected output, and a working solution. The solution is included "
                f"straight from `code/05-practical-skills/{slug}/`, so the code shown "
                f"here is the code that was run.\n\n"
            )
    index = DOCS / "index.md"
    if not index.exists():
        rows = "\n".join(
            f"| [{i:02d} - {t}]({s}.md) | |" for i, (s, t) in enumerate(TOPICS, 1)
        )
        index.write_text(
            "# Practice Problems\n\n"
            "Problems with the statement, expected output, and working code, "
            "grouped by topic.\n\n"
            "| Topic | Notes |\n|---|---|\n" + rows + "\n"
        )
    print("init done: folders and pages are in place")


def new(number, title):
    if not 1 <= number <= len(TOPICS):
        sys.exit(f"Topic number must be between 1 and {len(TOPICS)}")
    init()
    slug, topic_title = TOPICS[number - 1]
    folder = CODE / slug
    nums = [int(p.name[:2]) for p in folder.glob("[0-9][0-9]_*.py")]
    no = max(nums, default=0) + 1
    filename = f"{no:02d}_{slugify(title)}.py"
    path = folder / filename
    if path.exists():
        sys.exit(f"{path} already exists")

    path.write_text(
        f"# Problem: {title}\n"
        f"# Topic:   {number:02d} - {topic_title}\n\n\n"
        "def main():\n    pass\n\n\n"
        'if __name__ == "__main__":\n    main()\n'
    )
    (folder / ".gitkeep").unlink(missing_ok=True)

    snippet = f"code/05-practical-skills/{slug}/{filename}"
    section = (
        f"\n## Problem {no:02d}: {title}\n\n"
        "**Difficulty:** Easy | **Tags:** \n\n"
        "### Problem statement\n"
        "Describe the task in your own words, with any constraints.\n\n"
        "### Sample input\n"
        f"{FENCE}text\n(none)\n{FENCE}\n\n"
        "### Expected output\n"
        f"{FENCE}text\n(paste the real output here)\n{FENCE}\n\n"
        "### Solution\n"
        f'{FENCE}python title="{filename}"\n--8<-- "{snippet}"\n{FENCE}\n\n'
        "### Approach and notes\n"
        "- Idea:\n- Time / space complexity:\n- Gotchas:\n"
    )
    with open(DOCS / f"{slug}.md", "a") as f:
        f.write(section)
    print(f"created {path.relative_to(ROOT)}")
    print(f"added section to {(DOCS / f'{slug}.md').relative_to(ROOT)}")


def list_topics():
    for i, (slug, title) in enumerate(TOPICS, 1):
        print(f"{i:2d}  {title:<42} {count_problems(slug)} problem(s)")


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[:1] == ["init"]:
        init()
    elif args[:1] == ["list"]:
        list_topics()
    elif len(args) == 3 and args[0] == "new" and args[1].isdigit():
        new(int(args[1]), args[2])
    else:
        print(__doc__)
