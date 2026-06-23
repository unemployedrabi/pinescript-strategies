#!/usr/bin/env python3
"""Lightweight static checks for Pine Script files.

This is intentionally minimal: TradingView does not publish a standalone Pine
compiler, so we can only run cheap, structural sanity checks. It verifies that
every ``.pine`` file under ``src/``:

  * declares an indicator/strategy/study,
  * has balanced (), [] and {} brackets,
  * ends with a trailing newline,
  * contains no literal tab characters (the repo uses spaces).

Exit code is non-zero if any file fails, so it works as a CI gate.
"""
from __future__ import annotations

import sys
from pathlib import Path

SRC = Path(__file__).resolve().parent.parent / "src"
PAIRS = {")": "(", "]": "[", "}": "{"}
OPENERS = set(PAIRS.values())


def check_brackets(text: str) -> str | None:
    """Return an error string if brackets are unbalanced, else None.

    Bracket characters inside string literals and // comments are ignored.
    """
    stack: list[str] = []
    in_string: str | None = None
    in_comment = False
    prev = ""
    for ch in text:
        if in_comment:
            if ch == "\n":
                in_comment = False
            prev = ch
            continue
        if in_string:
            if ch == in_string and prev != "\\":
                in_string = None
            prev = ch
            continue
        if ch in ("'", '"'):
            in_string = ch
        elif ch == "/" and prev == "/":
            in_comment = True
        elif ch in OPENERS:
            stack.append(ch)
        elif ch in PAIRS:
            if not stack or stack[-1] != PAIRS[ch]:
                return f"unbalanced '{ch}'"
            stack.pop()
        prev = ch
    if stack:
        return f"unclosed '{stack[-1]}'"
    return None


def check_file(path: Path) -> list[str]:
    errors: list[str] = []
    raw = path.read_bytes()
    text = raw.decode("utf-8", errors="replace")

    if "indicator(" not in text and "strategy(" not in text and "study(" not in text:
        errors.append("no indicator()/strategy()/study() declaration found")

    if "//@version=" not in text and "study(" not in text:
        errors.append("missing //@version= directive")

    if not raw.endswith(b"\n"):
        errors.append("file does not end with a newline")

    if "\t" in text:
        errors.append("contains tab characters (use spaces)")

    bracket_err = check_brackets(text)
    if bracket_err:
        errors.append(bracket_err)

    return errors


def main() -> int:
    files = sorted(SRC.rglob("*.pine"))
    if not files:
        print("No .pine files found under src/", file=sys.stderr)
        return 1

    failed = 0
    for path in files:
        rel = path.relative_to(SRC.parent)
        errors = check_file(path)
        if errors:
            failed += 1
            print(f"FAIL  {rel}")
            for err in errors:
                print(f"        - {err}")
        else:
            print(f"ok    {rel}")

    print(f"\n{len(files) - failed}/{len(files)} files passed.")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
