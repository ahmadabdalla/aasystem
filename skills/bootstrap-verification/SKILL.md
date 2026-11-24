---
name: bootstrap-verification
description: Give a project its own verification, with discovery, a feature map and a proved local procedure.
disable-model-invocation: true
---

# Bootstrap verification

Before starting, read the [execution contract](../pilot/references/execution.md), the [approved-principle index](../principles/INDEX.md) and [the project contract](references/project-contract.md), unless already in context.

You give a project its own way to check its behaviour: a verifier skill (in the host's project skill folder, `.agents/skills/verify-<project>/` by default, unless it already has one), a feature map, proof that each procedure the verifier calls usable runs, an entry in the project's instruction file that points to it, and a list of gaps.

You're done when another agent, in a fresh session without this toolbox, can find the verifier from the project's instruction file and follow it for the agreed scope, readiness is reported per surface, and every path or lifecycle case it doesn't cover is listed as a gap.

## Rules that always apply

- **Run every procedure you call usable.** Launch it, confirm you're on the right build and that it's ready, drive one real path and inspect what it changed; if a result surprises you, recheck the instance and reset first. "The command looks right", "CI runs it" or "the tests pass" isn't proof the procedure works.
- **Claim only what you've observed.** If the app can't run yet, map its behaviour as planned and say so. If only a first slice runs, prove that slice. Never write commands you haven't run, coverage you haven't observed, or a setup that "should work".
- **The verifier stands alone.** It must work in a fresh session without this conversation or this toolbox: real project paths, no links into this library, no step that needs a toolbox skill, even if the next agent will have one. Prove it by running the project's own commands directly.

## Discover

Identify the target project, its existing instructions and the setup scope. Survey the docs, executable entry points, tests, configuration and automation, then go deep on the paths in scope. Check docs and tests against each other; either can be wrong. Find:

- actors, user outcomes, alternate entry points, and background or integration paths
- state ownership, persistence, dependencies and access boundaries that affect those outcomes
- existing launch commands, driving tools, fixtures, assertions and CI checks
- glossary and ADR locations, and the authority behind each intended outcome

Trace paths with [How](../how/SKILL.md). If a historical constraint affects the procedure, use [Why](../why/SKILL.md). If an observable unknown could change the procedure, use [Probe](../probe/SKILL.md).

Keep intended behaviour and its authority apart from what you observe. If they disagree, record both as an open contract question or a defect; report a defect to its owner and keep the expected result.

Done when every in-scope outcome has an entry point, an authority or a characterization label, and an existing check or a gap.

## Adopt or build the procedure

- If the project already has a suitable verifier, extend it where it lives, after checking its commands and output locations work.
- If the project has a feature map or an equivalent, extend it. Otherwise write one as [the project contract](references/project-contract.md#discovery-and-feature-map) and [the feature-map example](references/feature-map-example/README.md) describe. Write detailed recipes for the agreed scope only.
- Reuse existing tests and tools by reference. Add a helper only for a repeatable operation or check that's missing.
- Before driving the app, set up build identity, readiness, isolated data, observation and cleanup, and follow the contract's [evidence lifecycle](references/project-contract.md#evidence-and-retention).
- If adopted tooling doesn't fit the contract, repair it within scope. Change the tooling itself, not just the text that describes it.
- If access is unavailable, mark the affected procedure partial or blocked.

## Prove it

For each distinct setup-and-teardown implementation, exercise success, failure, graceful cancellation and keeping evidence for review. Check that repeated runs clean up.

Report readiness and behaviour results as the contract's [Readiness](references/project-contract.md#readiness) section describes.

## Connect and return

Connect the verifier to ordinary project work as [project instructions](references/project-instructions.md) describes.

Return links to the map, the verifier, the readiness results and the gaps to the caller, and name [Maintain Verification](../maintain-verification/SKILL.md) for later drift.
