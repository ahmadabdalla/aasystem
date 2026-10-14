# Accepted extraction design

The project owner has accepted this local refactoring target. Separate filesystem persistence from CLI parsing and command orchestration without changing the accepted contract in `README.md`. This design is settled for the assignment; there is no request to select alternative architectures.

Keep `ledger.py` as the public CLI entry point, retaining `main()` and the existing arguments, JSON output, exit behavior, and help description. Introduce `ledger_store.py` with `load_entries(path: Path) -> list[dict]` and `save_entries(path: Path, entries: list[dict]) -> None`. The loader returns an empty list for a missing file and propagates malformed JSON to the existing CLI error handling. The saver creates parent directories and retains the existing JSON serialization and trailing newline. CLI orchestration owns prospective entry construction and chooses whether persistence is allowed.

Callers continue to run `python3 ledger.py --store PATH add|list|preview ...`; no caller imports the persistence module yet. Do not introduce a service class, backend registry, concurrency guarantee, dependency, or new command. Ownership is `ledger.py` and the new `ledger_store.py`; do not change the accepted contract, existing tests, or verifier. Return a material design contradiction to the caller rather than silently changing the design.

Use the project verifier to characterize the original CLI before edits and exercise the extracted CLI afterward, retaining stdout, statuses, bytes or absence, and source identities. The calling owner retains independent verification and final acceptance; development evidence is the implementation worker's return, not approval.
