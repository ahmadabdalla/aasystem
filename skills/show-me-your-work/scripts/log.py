#!/usr/bin/env python3
"""Append a single decision to a task-owned TSV log."""

import argparse
from datetime import datetime, timezone
from pathlib import Path


HEADER = "ts\tphase\tdecision\twhy\tevidence\tresult\n"


def cell(value):
    value = value.replace("\t", " ").replace("\r", " ").replace("\n", " ")
    if value.lstrip().startswith(("=", "+", "-", "@")):
        return "'" + value
    return value


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("logfile", "phase", "decision", "why", "evidence", "result"):
        parser.add_argument(name)
    args = parser.parse_args()
    path = Path(args.logfile)
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with path.open("a+", encoding="utf-8", newline="") as stream:
            stream.seek(0)
            first = stream.readline()
            if first and first != HEADER:
                parser.error("existing log has a different header; choose the correct log")
            if first:
                stream.seek(0, 2)
                end = stream.tell()
                stream.seek(max(0, end - 1))
                if stream.read() != "\n":
                    parser.error("existing log ends with an incomplete row; inspect it before appending")
            stream.seek(0, 2)
            if not first:
                stream.write(HEADER)
            stamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
            values = [stamp, args.phase, args.decision, args.why, args.evidence, args.result]
            stream.write("\t".join(cell(value) for value in values) + "\n")
    except OSError as exc:
        parser.exit(1, f"cannot append decision log: {exc}\n")


if __name__ == "__main__":
    main()
