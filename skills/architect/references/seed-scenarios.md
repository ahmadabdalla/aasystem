# Seed scenarios

## Reuse first

Use the existing loaders, factories and fixtures. Add a scenario only when none gives the state the proof needs.

Keep three kinds of data apart:

- **Reference data** production needs to run. Follow the project's rules.
- **Demo data** contributors load to try the app.
- **Test fixtures** for one test.

Keep edge and failure cases in test fixtures, not demo data.

## Describe the scenario

Name the actors, permissions, relationships and states the proof needs. Give each record a stable name the recipe can use, like `draft-order`, not a generated ID.

Create valid records through the app's own operations, so they obey domain rules. If a fixture must be invalid or historical, build it directly and note why.

Use made-up identities. Never seed secrets or fake audit history.

## Tie it to the proof

The seed sets the starting state; the recipe drives the feature. See [scenario coverage](../../bootstrap-verification/references/project-contract.md#scenario-coverage).

Example: to prove an optional delivery note, seed one draft order. The recipe adds the note through the changed UI or API, saves, and reads it back, without permanently editing demo data.

If a relationship changes, create and read back a linked record, and check that one from the wrong parent or tenant is rejected.

## Repeat runs

Say what a second load does, including after a schema change or a half-finished run. If fixtures are disposable, reset and recreate them. If people may edit seeded data, say whether a reload keeps or overwrites their edits. Add locking or loader state only for a shown risk.

Where the seed file lives doesn't decide whether it ships or when it runs. Decide both, or say they're deferred.

Put the scenario changes and proof plan in the existing design package or feature recipe, in the project's format.
