---
name: show-me-your-work
description: Keep and audit an evidence-linked decision log for substantial, multi-phase, or unattended work. Use when someone will review the reasoning and outcomes later; omit routine action-by-action narration.
disable-model-invocation: true
---

# Show me your work

Before starting, read the [shared execution contract](../aapilot/references/execution.md) in full and the [approved-principle index](../principles/INDEX.md). Follow the contract’s baseline requirements.

Keep one canonical append-only decision log. Existing decision records, design packages, and proof artifacts retain their detail; this log points to them.

## Record decisions

Use a task-owned local `decisions.tsv` or another established audit location. Keep it uncommitted unless the task's delivery needs the trail. The columns are `ts`, `phase`, `decision`, `why`, `evidence`, and `result`. Evidence contains resolvable pointers, and results distinguish observation from inference or unfinished work.

Append a row with the bundled helper, requiring Python 3:

```sh
python3 scripts/log.py /absolute/task/decisions.tsv phase "Decision" "Reason" "Evidence path" "Observed result"
```

Resolve `scripts/log.py` relative to this skill. The helper creates the header, timestamps in UTC, and keeps cells on one line. One owner writes the log; workers return evidence to that owner. It does not verify that an evidence pointer proves a claim.

Record choices, accepted or refuted hypotheses, changed plans, completed verification gates, and blockers as they happen. Skip routine tool actions. Correct a wrong entry by adding a superseding row with its reason; preserve the original. The log must not contain secrets.

A new chat or replacement owner starts a new run. Before appending to an existing log, read its tail and add a `start` row identifying this run and the earlier time range it inherits. If another run appended since your last contribution, add a new `start` row before resuming. Use `start` only for run ownership, and never claim earlier observations as your own.

## Audit before delivery

Compare this run's rows with its accessible transcript or execution record and the actual artifacts. Check evidence pointers, outcomes, missing pivots, and superseded claims. Read only the authorized task's records. If no transcript is available, audit artifacts and disclose that limit. A helper's successful append proves formatting, not truthful logging.

Use an independent reviewer, preferably a different available model family, to inspect the log and permitted run evidence for unsupported claims, skipped verification, risky choices, and omissions. Self-review does not replace independence; disclose unavailable review or model diversity. The reviewer returns findings with row or artifact pointers, and the lead checks them.

Return the log path and an attention summary naming the reviewer setup, consequential findings, and evidence limits. An empty findings list is valid only for the scope actually reviewed.
