# Execution contract

Read the [principle index](../../principles/INDEX.md) and the project's instructions.

Read more before you start:

- If you'll change the product, even one word of copy, read [verification-contract.md](verification-contract.md) before editing.
- If you'll hand work to another agent or set up a review, read [delegation.md](delegation.md).
- If the work is long or has stages, goes to other agents or runs unattended, read [task-continuity.md](task-continuity.md). If you're resuming earlier work, read it first.

A link in a skill's step is part of that step: read it.

## One owner

One agent owns the request until it's delivered. Keep the goal, constraints, decisions and their reasons, open questions, expected results and evidence in the task brief; for small work in one context, the conversation is enough until a handoff or reset. Specialists add to that brief. They never start their own coordinator.

When you hand off, say what to read, what to deliver, which files the worker may touch, what to check and what to send back. Workers keep others' edits and the project's formats, and send anything out of scope back to the owner.

Workers inherit the task's effort level, checks and limits; a smaller piece doesn't lower them. If new evidence changes the scope, coupling, risk or proof needed, reassess the effort and update the assignments.

## Scope and proof

Restate a new or changed request in a line: the goal, what must stay true, and what's unclear. Then go without waiting for a reply. If the user set a stopping point, such as "research only" or "design only", stop there.

Build the smallest thing that works, with no architecture, tooling or process the goal doesn't need. Size the work with the [effort rubric](effort.md) unless the caller already did. At each phase boundary, say what's ready, what's missing and what's next, then carry on. If someone will review the reasoning later, invoke the [`show-me-your-work`](../../show-me-your-work/SKILL.md) skill from the start to keep the log.

Look up any fact you can check yourself instead of assuming it or asking the user. Reuse the project's requirements, accepted decisions and verification steps. In the brief and the report, label each claim as a fact, a proposal or a decision. A model agreeing isn't proof.

Proof matches the work: research cites sources, design shows its reasoning, and code shows observed behaviour. If you couldn't check something, say it's unverified.

## Signal effects

For every change, note what it does to operational and security signals: what logging, monitoring or alerting it adds, what it removes, and what failure or misuse still goes unnoticed. "No change" is fine if you looked.

Record them once in the task record, carry them into verification, and check them against the final result. If a current requirement needs detection, deferring it leaves the work incomplete. Link any other deferred detection work to its owner. If the change touches authentication, permissions, money or personal data, use Interrogate's [signal assessment](../../interrogate/references/signal-assessment.md).

## Ask the human

Decide routine details yourself. Before anything that changes product meaning, architecture, trust boundaries, permissions or external effects, or that needs a visual review, stop and ask. Don't re-ask for permission you already have.

When you ask, show the proposal, what you checked, what's uncertain and what you'll do next. Give a preview for visual decisions. Ask one question, then wait. Record the human's answer with the decision. No agent's recommendation or check is the human's approval.

## Finish

Before delivering, check the final result against current evidence, resolve open findings, clean up what you started and update affected project records. Report:

- what changed
- the checks you ran, and what they showed
- what's unverified
- where the evidence is
- anything you left in place on purpose (worktrees, artifacts, temporary code) and why

Stop once the agreed outcome is verified. Keep bulky artifacts only for a named need, under the [evidence lifetime](../../bootstrap-verification/references/project-contract.md#evidence-and-retention). Keep one log, and point to evidence instead of copying it.

Edits, commits, PRs, merges and releases are separate steps, so only do the ones you were asked for. Use [Opening a PR](../playbooks/opening-a-pr.md) when asked for one. For read-only work, the answer is the report: skip "what changed".
