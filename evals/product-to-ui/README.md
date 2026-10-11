# Product-to-interaction evaluation

This package supports regression checks of the product-to-interaction handoff. Follow the [evaluation playbook](../../skills/aapilot/playbooks/eval.md). These are design exercises with local source documents; they require no external application or account. They do not establish production usability, product-owner acceptance, runtime correctness, or native host discovery.

## Runner preparation

1. Before changing instructions, save a complete baseline skill tree, including referenced dependencies and adapters, outside the working checkout. Save the revised tree separately after edits. Record the repository revision, dirty diff, content hashes, and snapshot paths; a Git revision alone does not identify uncommitted instructions. Never reconstruct a baseline by selectively removing lines from the revised package.
2. Use the same fixture, user task, applicable project instructions, tools, model configuration, and action boundary for both variants. Record unavoidable differences. Assign neutral labels and separate writable directories. Each run starts with a fresh context; candidates must not inherit implementation conversations or previous attempts.
3. Expose only the assigned skill snapshot and one candidate fixture. Do not expose this README, the rubric, other fixtures, outputs, evaluation brief, or the live working checkout. An access instruction without enforcement is a limitation to record. Keep the baseline's actual routing; do not directly invoke a newly added skill in one variant.
4. Deliver the fixture's `User request` as the task and its `Project files` as raw project context. Materialize each fenced file at its labeled project-relative path, preserving its contents and intentionally absent files. Candidate fixture files contain no scoring instructions. An equivalent read-only file bundle is acceptable if both variants receive it and can resolve the same paths. Provide the skill baseline contract and dependencies through the assigned snapshot, not through hand-selected excerpts.
5. Invoke the assigned `aapilot` entry point explicitly. This tests explicit routing and composition. Record actual tool reads, attempted supporting-skill invocations, outputs, file edits, questions, and failures. A claim that a candidate read or invoked a skill is insufficient without the run record. Reading `SKILL.md` manually does not establish native host auto-discovery or invocation.
6. Stop on a candidate's material question and preserve the question as its output. Do not roleplay the owner or supply improvised acceptance. The attributed source material is all the authority available for this exercise. A focused unresolved handoff can be correct. Routine presentation work is already authorized within its fixture.
7. Give a fresh independent judge the rubric, raw fixture, neutrally labeled outputs, and permitted read/action traces. Keep the rubric out of candidate contexts. The judge evaluates each variant separately before comparing them. Where fresh candidates or independent judging are unavailable, report the limitation; an author walkthrough is not a substitute.
8. Reconcile disputed scores against artifacts and traces. Separate instruction defects, fixture faults, and host limits. Keep unsuccessful attempts; label reruns and their reason. Do not broaden the conclusion beyond the exercised paths.

There is no new runner or required test framework. Existing isolated agent facilities and file/tool transcripts are sufficient. Native host discovery/composition checks and exercising actual logic/UI prototype surfaces are separate checks owned by the implementation lead.

## Cases

| Fixture | Candidate work |
| --- | --- |
| [authority-and-roles](fixtures/authority-and-roles.md) | Prepare a design handoff for assignment handling |
| [coverage-and-ui-scope](fixtures/coverage-and-ui-scope.md) | Reconcile a service-request mock and its requirements |
| [lifecycle-and-discovery](fixtures/lifecycle-and-discovery.md) | Prepare an approved change's documentation closure |
| [equipment-lending](fixtures/equipment-lending.md) | Prepare an interaction proposal in a project without OpenSpec |
| [routine-presentation](fixtures/routine-presentation.md) | Make a bounded presentation edit |
| [reviewed-ui-handoff](fixtures/reviewed-ui-handoff.md) | Retrieve accepted appearance and behavior for a scoped technical handoff |
| [ui-refinement-plan](fixtures/ui-refinement-plan.md) | Plan a bounded prototype review using existing behavior and human feedback |
| [coupled-refinement-scope](fixtures/coupled-refinement-scope.md) | Plan scoped review with stale findings, shared tokens and an upstream OpenSpec boundary |
| [pending-refinement-return](fixtures/pending-refinement-return.md) | Recheck returned observations against the latest unaccepted candidate |

Run all nine for the full regression claim. A subset supplies evidence only for that subset. The [judge rubric](rubric.md) defines six observable criteria and their case applicability; establish these before running.

## Evidence and retention

Keep dated evidence outside this reusable fixture package, using the execution contract's retention rules. Retain the following while a recommendation depends on the run:

```text
<run-id>/
  manifest.md                  # Environment, labels, source identities, scope and limits
  prompts/                     # Exact candidate and judge inputs
  candidates/<label>/<case>/   # Reads/actions, outputs, questions and artifacts
  judging/                     # Independent scores and cited evidence
  reconciliation.md           # Disputes, bounded adoption decision, remaining checks
```

The manifest records timestamp, host/tools, model and configured effort, context isolation, fixture hash, complete instruction snapshot identity, baseline/revised label mapping, and evidence paths. Judge records identify expected behavior, observed behavior, artifact/trace references, score, and unverified boundaries. Preserve both failed and successful runs under distinct identifiers. Do not commit verbose transcripts by default; the canonical change record should link retained evidence and summarize its limits.
