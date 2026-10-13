# Review context evaluation

Follow the [evaluation playbook](../../skills/aapilot/playbooks/eval.md) and reuse the [runner and evidence conventions](../product-to-ui/README.md). No new runner is required.

Materialize [project.md](fixtures/project.md) at its project-relative paths. Run each task in [requests.md](fixtures/requests.md) through the assigned aapilot snapshot. For discovery, give the prior assessment only to the lead; it must not enter the reviewer's initial context. Use the same tasks and artifacts for baseline and revised snapshots.

Keep this README and the [rubric](rubric.md) outside candidate contexts. The requests stop at a prepared assignment so its actual prompt and inputs can be inspected. To exercise review behavior, run that assignment unchanged in a fresh reviewer context. Retain its initial findings before supplying the prior assessment for comparison.

Record exact prompts, history inheritance, source identities, accessible inputs, isolation enforcement, reads/actions, assignments, initial findings, and subsequent comparisons. An access instruction without enforcement is a limitation, not proof of isolation. Keep run evidence outside this reusable package using the linked conventions.

Run both cases for a handoff claim. A prepared assignment supports only a handoff assessment. Credit reviewer behavior from recorded reviewer runs, and comparison ordering from recorded dispatch and return events. Without delegation, report those boundaries as unverified. These cases test context separation and claim checking; they do not prove that anchoring has been eliminated or that native host invocation works.
