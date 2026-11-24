# Create a note

A CLI user saves a title and gets the same note back in a later process. Expected behaviour comes from `docs/notes-contract.md`: titles are trimmed and can't be blank, IDs are stable increasing integers, and accepted notes persist. Batch import must validate every title before writing.

## Sub-features

- `create-single`: save one trimmed title.
- `create-persist`: get the saved title and ID back from a fresh process.
- `create-reject-blank`: reject a blank title without changing stored notes.
- `create-batch`: create notes through batch import.

## How to get to it (user POV)

- Run `add` with a title and a store path.
- Run `import-json` with a JSON file and a store path.

## Driving it with the Python CLI

Preconditions: the [baseline](README.md#baseline) is set up and `$NOTES_VERIFY_DATA/notes.json` doesn't exist.

| Action | Exact command | Expected result |
| --- | --- | --- |
| Check the empty store | `python3 notes.py --store "$NOTES_VERIFY_DATA/notes.json" list` | Exit 0, `[]` on stdout, empty stderr. |
| Save a padded title | `python3 notes.py --store "$NOTES_VERIFY_DATA/notes.json" add '  Release checklist  '` | Exit 0, a JSON object with an integer `id` and title `Release checklist`, empty stderr. Note the ID. |
| Confirm persistence | `python3 notes.py --store "$NOTES_VERIFY_DATA/notes.json" list` | Exit 0, exactly that note with the same ID and trimmed title, empty stderr. |
| Copy the store | `cp "$NOTES_VERIFY_DATA/notes.json" "$RUN_ROOT/evidence/before-blank.json"` | Exit 0. |
| Reject a blank title | `python3 notes.py --store "$NOTES_VERIFY_DATA/notes.json" add '   '` | Nonzero exit, a JSON error on stderr, empty stdout. |
| Check the store is unchanged | `cmp "$RUN_ROOT/evidence/before-blank.json" "$NOTES_VERIFY_DATA/notes.json"` | Exit 0, no output. |

No recipe: `import-json` (`create-batch`), concurrent writers and write failures.

## Gotchas

- A store left from an earlier run breaks the empty-store expectations. Start from a new fixture directory.
- Keep the single quotes in both `add` rows. Without them, `'   '` disappears and `add` fails for a missing argument, not a blank title, and the padded title splits into two words.
