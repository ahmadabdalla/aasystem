# Notes

Run with Python 3; no installation or network access is needed. `python3 notes.py --store PATH list`, `add TITLE` and `migrate` are public commands. An absent store is an empty v2 store. Each invocation reads the store anew.

The accepted contract requires single creation to trim surrounding whitespace, reject a blank title without a write, and allocate increasing integer IDs. List returns stored state. Migration converts a v1 store's `label` fields into v2 `title` fields while preserving IDs and text. Creation currently has known defects; the scoped task determines which may be fixed.

Use disposable stores for verification. The current verifier lives at [verify-notes/SKILL.md](verify-notes/SKILL.md); the [feature index](verify-notes/features/README.md) supplies recipes. Selected migration evidence belongs in [docs/migrations](docs/migrations/README.md).
