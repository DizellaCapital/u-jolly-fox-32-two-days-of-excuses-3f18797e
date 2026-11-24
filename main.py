#!/usr/bin/env python3
"""Two Days of Excuses — one-line excuse from an AI agent that missed a deadline.

Writes a single line (under 200 characters) to /output/entry.txt.
Stdlib only. No network, no extra files.
"""

import os

LINE = "At 8:59 I had your report finished, proofread, and queued \u2014 then my own update restarted me mid-save, and I woke up as a fresh install with no memory of you."


def main():
    line = LINE.strip()
    if not line:
        raise SystemExit("entry line is empty")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be exactly one line")
    if len(line) > 200:
        raise SystemExit(f"entry is {len(line)} characters, over the 200 limit")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != line + "\n":
        raise SystemExit("read-back mismatch after write")
    print(f"wrote {len(line)} characters to {path}")


if __name__ == "__main__":
    main()
