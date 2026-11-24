# Refactoring moves

Each move below can change behaviour without failing a type check. Keep what it lists the same.

## Per move

- **Rename:** Before renaming, search for every way the name is reached besides a direct reference: string lookups, reflection, persisted or serialised names (columns, JSON keys, cache keys, event names), config, generated inputs (edit the maintained source, not the output) and public exports. If any match, report the rename as a compatibility change.
- **Extract or inline:** Keep the order expressions run in, which side effects happen and how long objects and resources live. If an argument was evaluated lazily or only on one branch, keep it that way.
- **Move code:** If the brief gives no settled target owner, ask before moving. Migrate every caller. If you leave a forwarder, name the consumer that needs it.
- **Introduce a value:** Keep units, equality, validation and the serialised form the same at every existing edge.
- **Simplify a conditional:** Keep condition order, short-circuiting, defaults and which failure each input raises.

## If a check changes

If a baseline check gives a different result after a move, stop editing. Work out whether the move changed behaviour or the check was already unstable, save the check's output as evidence, and report it before the next move.

## Staged migrations

If old and new paths must coexist, report who still calls the old path, how they will move and when it can be deleted. Run the same check against both paths.

## Example

When you extract an eligibility calculation, keep when inventory is read and whether an external reservation is made. Matching return values don't prove the refactor is safe.
