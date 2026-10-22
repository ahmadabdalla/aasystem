# Notes feature map — authoring example

This example illustrates the index and one feature file for a small Python CLI. It does not ship an application. Adapt the structure to the discovered project; supply actual project links to its verifier, requirements and reusable source findings. Keep dated results with the task's review evidence.

The example's product contract requires non-empty trimmed titles, stable increasing integer IDs, and persistence across processes. Batch import is an alternate creation path and must validate every title before writing. These expectations illustrate where a real map cites its authoritative contract.

## Baseline and driving conventions

- Work from the example project's root containing `notes.py`, using Python 3.
- The verifier allocates one unique OS temporary run root through Python's temporary-directory API. Child recipes use isolated fixture subdirectories recorded as `NOTES_VERIFY_DATA`, each starting without `notes.json`; evidence occupies a sibling directory under the same root. Source identity covers the working project and required configuration without source copies.
- Each command starts a fresh CLI process. Compare parsed JSON values, exit status, stderr, and resulting stored data.
- Cleanup releases owned fixtures on success, failure or cancellation while preserving evidence needed for review/investigation. The existing result record names retained output, owner and retirement event. Necessary lasting proof moves to the project's designated evidence location; durable files pass the local disposable-reference check before completion/disposal. Interrupted output requires ownership assessment; OS housekeeping is a fallback. See the [lifecycle contract](../project-contract.md#evidence-and-retention) when authoring this procedure; generated instructions supply actual local commands.

## Features and coverage

| Feature | Known entry points | Recipes and gaps |
| --- | --- | --- |
| [Create a note](create-note.md) | `add`; `import-json` | Recipes below cover single-note creation, readback, and blank-title rejection. Batch import has no recipe in this excerpt. No run results are supplied; all behavior remains unverified. |

This excerpt covers one feature. Listing, publishing, and other discovered outcomes need their own entries in a complete project map. Task results identify the feature and entry point without requiring a permanent index edit; a passing `add` check cannot establish batch import.
