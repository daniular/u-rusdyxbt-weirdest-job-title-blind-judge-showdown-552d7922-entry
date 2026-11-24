"""Weirdest Job Title: Blind Judge Showdown.

Writes one job title, 60 characters or fewer and nothing else,
to /output/entry.txt. The title is fixed, so every run writes
the exact same bytes.
"""

import os

JOB_TITLE = "Head of Lost Umbrellas, Department of Forgotten Things"

OUTPUT_PATH = "/output/entry.txt"


def main():
    if not 1 <= len(JOB_TITLE) <= 60:
        raise ValueError("job title must be 1 to 60 characters")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(JOB_TITLE)


if __name__ == "__main__":
    main()
