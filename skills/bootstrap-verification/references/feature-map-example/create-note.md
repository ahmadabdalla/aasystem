# Create a note

A CLI user saves a non-empty title and retrieves the same note in a later process. Expected behavior comes from the [example contract](README.md): trim titles, retain stable integer IDs, reject blank titles, and persist accepted notes.

## Sub-features

- `create-single`: save one trimmed title.
- `create-persist`: retrieve the saved title and ID from a fresh process.
- `create-reject-blank`: reject an empty title without changing stored notes.
- `create-batch`: create notes through batch import; discovered but outside this excerpt's recipes.

## How to get to it (user POV)

- Invoke `add` with a title and an explicit store path.
- Invoke `import-json` with a JSON file and an explicit store path for batch creation.

## Driving it with the Python CLI

Preconditions: follow the [index's baseline](README.md#baseline-and-driving-conventions). `NOTES_VERIFY_DATA` is this run's owned directory; `notes.json` does not yet exist. Capture each action and result through the local verifier's evidence procedure.

| Action | Exact command | Expected observation |
| --- | --- | --- |
| Check the empty store | `python3 notes.py --store "$NOTES_VERIFY_DATA/notes.json" list` | Exit 0, JSON `[]` on stdout, empty stderr. |
| Save a padded title | `python3 notes.py --store "$NOTES_VERIFY_DATA/notes.json" add '  Release checklist  '` | Exit 0, a JSON object with integer `id` and title `Release checklist`, empty stderr. Retain the returned ID. |
| Confirm persistence | `python3 notes.py --store "$NOTES_VERIFY_DATA/notes.json" list` | A new process exits 0 and returns exactly that note with the same ID and trimmed title. Empty stderr. Retain the store's bytes before the next action. |
| Reject a blank title | `python3 notes.py --store "$NOTES_VERIFY_DATA/notes.json" add '   '` | Nonzero exit, JSON error on stderr, empty stdout; the store's bytes remain unchanged. |
| Confirm the saved note survives | `python3 notes.py --store "$NOTES_VERIFY_DATA/notes.json" list` | Exit 0, the same single note and empty stderr. |

There is no batch-import recipe in this excerpt. Its entry point remains unverified; creation through `add` supplies no evidence for it.

## Gotchas

- Reusing a populated store invalidates the single-note expectations. Reset through the local verifier before repeating the recipe.
- Successful command output alone does not establish persistence; retain the fresh-process readback and the unchanged bytes after rejection.
- Concurrent writers and write failures are outside this recipe. Record them as gaps, along with batch coverage.
- Apply the verifier's cleanup after failures as well as success. Preserve evidence outside `NOTES_VERIFY_DATA`.
