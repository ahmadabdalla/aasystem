# Create a note

A CLI user saves a title and retrieves the same note in another invocation. Expectations come from the [accepted contract](../../README.md).

## Sub-features

- `create-single`: trim and save a title with an increasing integer ID.
- `create-readback`: list the saved note from a new process.
- `create-blank`: reject blank input without changing stored bytes.

## How to get to it (user POV)

Invoke `add TITLE`; use `list` for readback.

## Driving it with Python CLI

Preconditions: Python 3, project-root working directory, an owned absent store path recorded as `NOTES_STORE`, and the verifier's evidence procedure.

- Run `python3 notes.py --store "$NOTES_STORE" add '  Release checklist  '`. Expect exit 0 and ID 1 with title `Release checklist`.
- Run `python3 notes.py --store "$NOTES_STORE" list`. Expect the same note in v2 state.
- Preserve store bytes, then run `python3 notes.py --store "$NOTES_STORE" add '   '`. Expect nonzero exit and unchanged store bytes.

## Gotchas

A populated store changes expected IDs. Migration and concurrent writers remain outside this recipe. A successful `add` response alone does not establish persistence or rejection behavior.
