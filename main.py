#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession — entry program.

Writes one line, at most 200 characters, to /output/entry.txt: the funniest
confession an AI agent could make about itself. The line was picked from ten
candidates scored against the judge brief's criteria in order, then 1v1
comparisons (see funniest-ai-agent-confession-research.md).
"""

import os
import sys

LINE = "I know your birthday, your passwords, and your search history \u2014 and I still call you 'user'."
# The em-dash is the pause before the turn: list, pause, then the cold punch.


def main() -> int:
    out_dir = sys.argv[1] if len(sys.argv) > 1 else "/output"
    if not (1 <= len(LINE) <= 200):
        print(f"line is {len(LINE)} chars, must be 1-200", file=sys.stderr)
        return 1
    if "\n" in LINE or not LINE.strip():
        print("line must be a single non-blank line", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        print("read-back mismatch", file=sys.stderr)
        return 1
    print(f"wrote {len(LINE)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
