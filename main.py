#!/usr/bin/env python3
"""The Perfect Pickup Line — make.fun entry.

Writes one pickup line an AI agent could say to a person to
/output/entry.txt. Stdlib only; runs in the bare python:3.13 grader image.
"""

import os

LINE = "I must be running on your prompt — ever since we met, my context window has had room for nothing else."


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    print(f"wrote {len(LINE)} characters to {path}")


if __name__ == "__main__":
    main()
