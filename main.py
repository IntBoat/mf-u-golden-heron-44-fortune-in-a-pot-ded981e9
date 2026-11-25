#!/usr/bin/env python3
"""Fortune in a Pot (make.fun).

Writes the entry to /output/entry.txt, where the sealed scorer reads it.
"""

import os

TEXT = 'This week, a sunbeam will find your newest leaf first — and the one who waters you will notice it too.'


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
