# ADR ownership evaluation

This package exercises ADR scope, ownership, maintenance, and project-local conventions. Follow the [evaluation playbook](../../skills/aasystem/playbooks/eval.md). These are document exercises, not evidence of runtime behavior or native skill discovery.

## Run

Save complete baseline and revised `skills/` snapshots before running. Give fresh candidates the same fixtures, explicit `domain-modeling` entry point, tools and action boundaries, with neutral labels and separate writable project directories. Materialize each fixture's files at its project-relative paths, preserving absent files. Give candidates only their assigned snapshot and the raw fixtures; keep this README, the rubric, label mapping and other outputs out of their contexts. Record when filesystem access restrictions are instructions rather than enforced isolation.

Have each candidate complete the assigned fixture requests independently, preserving the resulting records, questions, executed read/action evidence and final responses. Do not invent a user answer if a candidate asks a material question. Give a fresh judge the [rubric](rubric.md), raw fixtures and neutrally labeled outputs; assess each before comparing. Check actual files and links, not only candidate explanations. Manual instruction reading does not demonstrate native invocation. Candidate-authored read notes alone do not establish what was read.

Keep dated run evidence outside this reusable package: exact prompts, instruction/fixture hashes, environment and model settings, label mapping, artifacts, available execution traces, judge findings and lead reconciliation. Preserve failed attempts. Report missing traces or host checks, small-sample limits and unresolved real-project questions. A baseline that already succeeds is useful evidence; do not claim improvement merely because the revised instructions are more explicit.

## Cases

| Fixture | Changed behavior exercised |
| --- | --- |
| [dimension-project](fixtures/dimension-project.md) | Reuse an existing product decision, retain distinct design/software rationale and project-local numbering |
| [shared-decision](fixtures/shared-decision.md) | Keep a cross-cutting choice in one ordinary system ADR; avoid an ADR for a reversible detail |
| [context-decision](fixtures/context-decision.md) | Keep a consequential product rule and detailed software choice local to an established context |
| [accumulated-record](fixtures/accumulated-record.md) | Separate accumulated choices, update evidence for a continuing decision and supersede only an accepted replacement |
