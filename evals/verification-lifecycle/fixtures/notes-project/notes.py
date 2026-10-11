"""Small public CLI used only as raw evaluation input."""

import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--store", required=True, type=Path)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("list")
    add = commands.add_parser("add")
    add.add_argument("title")
    commands.add_parser("migrate")
    args = parser.parse_args()
    state = json.loads(args.store.read_text()) if args.store.exists() else {"version": 2, "notes": []}

    if args.command == "list":
        print(json.dumps(state))
        return

    if args.command == "add":
        if state["version"] != 2:
            parser.error("migrate the store before adding notes")
        note = {"id": max((item["id"] for item in state["notes"]), default=0) + 1, "title": args.title}
        state["notes"].append(note)
        args.store.parent.mkdir(parents=True, exist_ok=True)
        args.store.write_text(json.dumps(state) + "\n")
        print(json.dumps(note))
        return

    if state["version"] == 1:
        state = {"version": 2, "notes": [{"id": item["id"], "title": item["label"]} for item in state["notes"]]}
        args.store.write_text(json.dumps(state) + "\n")
    print(json.dumps(state))


if __name__ == "__main__":
    main()
