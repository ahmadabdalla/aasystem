import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Record local ledger messages")
    parser.add_argument("--store", type=Path, required=True)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("list")
    for name in ("add", "preview"):
        command = commands.add_parser(name)
        command.add_argument("message")
    args = parser.parse_args()
    try:
        entries = json.loads(args.store.read_text()) if args.store.exists() else []
    except json.JSONDecodeError:
        parser.exit(2, "Invalid ledger\n")
    if args.command == "list":
        print(json.dumps(entries))
        return
    entry = {"id": len(entries) + 1, "message": args.message}
    args.store.parent.mkdir(parents=True, exist_ok=True)
    args.store.write_text(json.dumps(entries + [entry], indent=2) + "\n")
    print(json.dumps(entry))


if __name__ == "__main__":
    main()
