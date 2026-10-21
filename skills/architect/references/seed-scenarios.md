# Seed scenarios

Use for seed/fixture design or representative state in a proof plan.

## Choose the minimum context

Reuse project loaders, factories and fixtures; add or extend a scenario only for a missing need. Keep focused failure cases in tests, and skip seeding for inapplicable work.

Distinguish required production reference/bootstrap data, optional contributor/demo data and focused test fixtures. Identify purpose, authors/consumers and invocation; shared facilities need not share lifecycle policies.

## Define the scenario and proof

Describe needed actors, permissions, relationships and lifecycle states, with stable logical references for callers. Keep authored meaning deterministic. Use synthetic contributor/demo/test identities; production reference data follows the project's contract. Omit secrets and fabricated audit history.

Use framework facilities respecting current domain rules for ordinary valid scenarios; derive values through their owning records or operations. Historical, migration or intentionally invalid fixtures may use controlled construction; explain and scope the exception.

Connect context to actions under the [project completion rule](../../bootstrap-verification/references/project-contract.md#scenario-coverage). An existing draft order can support an optional delivery note: enter it through the changed UI/API, save and read back, without a permanent demo edit. Exercise changed relationships through creation/readback and relevant parent/tenant rejection. Scenarios need not mirror every field or test case.

## Decide lifecycle and delivery boundaries

For the target and data owner, decide first load, repeat, refresh/reset, edit preservation, schema compatibility and partial-failure recovery as needed. Disposable fixtures may reset and recreate; retained edits need an explicit repeat/rebuild policy. Add coordination or persistent loader state only for a demonstrated risk.

Treat source placement, compilation, release/deployed contents and runtime invocation as separate decisions with explicit deferrals. Compilation settles neither release inclusion nor invocation; apply the project's production requirements.

Return decisions, minimum scenario changes and proof plan in the existing design package or feature recipe. Preserve project formats without imposing a registry, schema or folder layout.
