---
name: maintain-verification
description: Audit a project's verification procedure and feature map against source and live behavior. Use after relevant drift, for a verification audit, or when a project recipe no longer works.
disable-model-invocation: true
---

# Maintain verification

Before starting, read the [shared execution contract](../aapilot/references/execution.md) in full and the [approved-principle index](../principles/INDEX.md). Follow the contract’s baseline requirements.

Keep the project's map and operating procedure usable while preserving the intended behavior they check. Use [the project contract](../bootstrap-verification/references/project-contract.md) to identify missing meaning, preserving equivalent existing layouts.

## Establish scope

Locate the project verifier, its map, existing instructions, and prior evidence. A task-scoped pass follows changed behavior and its dependents; a full audit covers every declared feature plus a bounded search for missing surfaces. State which scope is being audited. If there is no verifier, use [bootstrap-verification](../bootstrap-verification/SKILL.md) within the authorized setup scope.

Read the requirements behind expected outcomes. Keep source revisions and run environments with observations. Ask one focused question and wait only when a material contract or preference cannot be recovered or reasonably assumed. Unavailable access is a gap, not an invitation to change the expected result.

## Compare the map with the project

Read `features/README.md` and compare its entries with the sibling feature files; follow the existing index location for an established equivalent layout. Repair missing, duplicate, orphaned, or dead entries. Treat each feature file as a maintenance unit and keep its sub-feature IDs, entry points, driving recipes, and gotchas aligned. For another layout, apply the same review to its feature groups without creating a second map.

Check mapped entry points against executable paths, documentation, existing tests, and relevant recent changes. Use [how](../how/SKILL.md) for an unclear flow. Identify new or removed entry points and changes in prerequisites, persistence, dependencies, or driving tools. Cite concrete source evidence before adding a purported feature. Distinguish intended changes from unexplained discrepancies.

Include affected business invariants, identity/context meanings, consistency and failure guarantees in that comparison. Reconcile their required cases from accepted requirements and design handoffs with runnable recipes or explicit gaps. Structural changes preserve still-authoritative expectations; recipe edits follow actual drift.

When splitting delivery, separate increment acceptance from cumulative regression and assign every deferred assertion to a later increment. For rewritten contracts, compare source clauses and branches directly with actual destinations before consulting the author's mapping. Check new examples for unintended obligations, exclusions or prohibitions as well as tracing preserved behaviour.

Consolidate live recipes to reuse setup without losing distinct entry points or assertions. Drive each feature in the declared audit scope through its verifier. A full audit must account for every mapped feature; source inspection alone does not establish live coverage. State which paths were exercised and which remain unverified. If an owned resource cannot be isolated for concurrent use, drive it serially.

Follow the local launch, health, identity, reset, evidence, and cleanup procedure. Recheck the instance after a surprising result and confirm evidence survives teardown. When a verifier fault prevents progress, make a bounded repair and retry the affected path; persistent external prerequisites stay blocked.

Audit executable copying, input identity, output ownership and retention against the [evidence lifecycle](../bootstrap-verification/references/project-contract.md#evidence-and-retention). Repair incompatible harness behavior within scope and exercise the affected lifecycle paths; prose changes alone do not establish adoption.

## Classify and repair

| Finding | Action |
| --- | --- |
| Confirmed intended behavior changed | Update the affected map/expectation with its authority and recheck. |
| Recipe or index drift | Correct the local instructions, links, or entry points and exercise the corrected recipe. |
| Product works but driving or assertions fail | Repair the owned harness and rerun it against the real surface. |
| Product violates the intended contract | Report a regression with evidence; retain the expectation. Fix product code only when that work is separately in the authorized task scope. |
| Missing access, environment, or unsettled intent | Record the exact prerequisite and affected unverified scope. |

By default, edits belong to the local verifier, its owned helpers/map, and narrow project routing needed to reach it. Do not rewrite unrelated tests or product code just to make this audit pass. Preserve existing instructions and historical evidence required by the [evidence lifecycle](../bootstrap-verification/references/project-contract.md#evidence-and-retention). Keep concise run notes in uncommitted scratch; an unchanged run needs no permanent map edit. New helpers must have documented invocations and demonstrated behavior.

Return the scope, features and entry points covered, repairs and rechecks, product defects, and unresolved gaps with evidence. Distinguish a usable verifier from a passing product. Report a full audit clean only when its declared coverage is complete and no defect or unresolved gap remains. A partial audit can be useful without certifying the rest of the map. Do not schedule future runs or publish changes unless requested.
