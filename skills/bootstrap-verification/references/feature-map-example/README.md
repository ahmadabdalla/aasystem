# Notes feature map — authoring example

This example illustrates the index and one feature file for a small Python CLI. It does not ship an application. Adapt the structure to the discovered project; supply actual project links to its verifier, requirements and reusable source findings. Keep dated results with the task's review evidence.

The example's product contract requires non-empty trimmed titles, stable increasing integer IDs, and persistence across processes. Batch import is an alternate creation path and must validate every title before writing. These expectations illustrate where a real map cites its authoritative contract.

## Baseline and driving conventions

- Work from the example project's root containing `notes.py`, using Python 3.
- The local verifier checks source identity and creates an owned temporary directory, recorded as `NOTES_VERIFY_DATA`. Each recipe starts with an absent `notes.json` inside that directory.
- Each command starts a fresh CLI process. Compare parsed JSON values, exit status, stderr, and resulting stored data.
- The verifier captures actions, observations, environment, and source identity in a unique ignored `.verification/runs/` directory outside the temporary data. Its cleanup removes only owned temporary data and confirms that evidence survives. Its local retention procedure keeps evidence through review, or investigation for an unresolved failure, and names who disposes of it afterward.

## Features and coverage

| Feature | Known entry points | Recipes and gaps |
| --- | --- | --- |
| [Create a note](create-note.md) | `add`; `import-json` | Recipes below cover single-note creation, readback, and blank-title rejection. Batch import has no recipe in this excerpt. No run results are supplied; all behavior remains unverified. |

This excerpt covers one feature. Listing, publishing, and other discovered outcomes need their own entries in a complete project map. Task results identify the feature and entry point without requiring a permanent index edit; a passing `add` check cannot establish batch import.
