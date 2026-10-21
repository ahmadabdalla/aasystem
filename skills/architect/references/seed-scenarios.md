# Seed scenarios

Use when designing seed/fixture data or when verification needs representative state. Keep the decisions and proof plan in the existing design package or feature recipe.

## Choose the minimum context

Inspect existing framework loaders, factories, fixtures and project requirements first. Reuse adequate context; add or extend a scenario only for a missing need. Keep focused failure cases in tests rather than expanding permanent demo data. Inapplicable work needs no seeding subsystem.

Distinguish required production reference/bootstrap data, optional contributor/demo data and focused test fixtures. State each scenario's purpose, authors/consumers and invocation. These purposes can share existing facilities without sharing every lifecycle policy.

## Define the scenario

Describe the actors, permissions, relationships and lifecycle state needed by the caller. Where callers need to locate seeded records, provide stable logical references rather than depending on generated database IDs. Keep authored meaning deterministic; use synthetic identities for contributor/demo/test data, omit secrets and do not invent audit history. Required production reference data follows the project's actual contract.

Use existing framework facilities that respect current domain rules for ordinary valid scenarios. Derive values from their authoritative records or operations rather than inserting fabricated results. Historical, migration and intentionally invalid fixtures may need separate controlled construction; document why and keep that exception scoped.

Connect starting context to the changed action and contract-derived expected observations under the [project completion rule](../../bootstrap-verification/references/project-contract.md#scenario-coverage). Existing context followed by a feature action can be sufficient; a scenario need not mirror every database field or test case.

For example, an existing account and draft order can support adding an optional delivery note: enter the note through the changed UI or API, save, and read it back. No permanent demo edit is required. Exercise a total through its underlying items and calculation, and relationship constraints through real creation and rejection paths rather than loader output alone.

## Decide lifecycle and delivery boundaries

Name the target and data owner, then settle first load, repeat, refresh/reset, edit preservation, schema compatibility and partial-failure recovery to the extent the scenario needs them. A disposable isolated fixture may use reset-and-recreate; retained contributor edits require a deliberate repeat/rebuild policy. Prefer existing framework mechanisms. Add coordination or persistent loader state only for a demonstrated risk.

Record source placement, compilation, release/deployed contents and runtime invocation as separate decisions, including explicit deferrals. Compiling with the app does not settle release inclusion or execution. Required production data and optional data may need different choices; apply project requirements rather than a blanket production prohibition or allowance.

Return these decisions, the minimum scenario changes and the proof plan in the existing design package. Link owned project instructions instead of introducing a separate scenario registry, prescribed schema or folder layout. The [execution contract](../../aapilot/references/execution.md) owns authority, resource isolation, evidence and independent verification.
