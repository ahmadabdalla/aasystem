# Notes feature map

Read this index before driving Notes, then use the matching feature file as the recipe.

## Baseline

- Run from the project root containing `notes.py`, using Python 3.
- Give each run its own temp directory, with fixtures and evidence in subdirectories:

  ```sh
  export RUN_ROOT="$(python3 -c 'import tempfile; print(tempfile.mkdtemp())')"
  export NOTES_VERIFY_DATA="$RUN_ROOT/data"
  mkdir "$NOTES_VERIFY_DATA" "$RUN_ROOT/evidence"
  ```

- If your tool starts a new shell for each command, write the full paths in place of `$RUN_ROOT` and `$NOTES_VERIFY_DATA`.

- Each command starts a fresh CLI process. Compare parsed JSON, exit status, stderr and the stored file.

## Features

| Feature | Entry points | Covered | Gaps |
| --- | --- | --- | --- |
| [Create a note](create-note.md) | `add`, `import-json` | `create-single`, `create-persist`, `create-reject-blank` | `create-batch` (`import-json`) has no recipe. |
