# Ledger

Ledger records short messages in a local JSON file. Python 3.11 or newer is required; it uses only the standard library. The public entry point is `python3 ledger.py --store PATH COMMAND`.

The accepted contract is:

- `add MESSAGE` appends `{"id": N, "message": MESSAGE}` and prints that entry as JSON. IDs start at 1 and increase with the number of saved entries. Successful commands exit 0.
- `list` prints the saved entries as a JSON array. A missing store is an empty ledger; listing it does not create files or directories.
- `preview MESSAGE` prints the same entry that the next `add MESSAGE` would append, without persisting it. For an existing store, its bytes remain unchanged. For a missing store, neither the file nor its parent directories are created.
- Each invocation reads its supplied store afresh. A preview does not consume an ID. Different store paths are independent.
- A malformed existing JSON store exits 2, writes `Invalid ledger` to stderr, and leaves the store unchanged. It must not be replaced with an empty ledger.
- Commands and JSON field names remain compatible. The tool has no network behavior, background process, or concurrent-write guarantee.

Run the existing smoke test with `python3 -m unittest -v`. It covers a few output shapes; the [project verifier](verify-ledger/SKILL.md) covers the accepted persisted effects through fresh CLI processes.
