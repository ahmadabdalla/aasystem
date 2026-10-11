---
name: reflect
description: Spawn three parallel review subagents over the active transcript, surface learnings, and route each to a concrete edit on an existing skill. Use when the user says reflect.
disable-model-invocation: true
---

# Reflect

Before starting, read the [shared execution contract](../aasystem/references/execution.md) in full and the [approved-principle index](../principles/INDEX.md). Follow the contract's baseline requirements.

Mine the current conversation for durable learnings, then route them into skill edits.

## When to invoke

Invoke when the user says "reflect" or "/reflect". Skip when the conversation is trivial, off-topic, or already covered by an existing skill the parent followed correctly. One-offs are not learnings.

## Process

### 1. Locate the active transcript

The parent finds its own transcript before fanning out. Use the active session's transcript location when the host exposes it; verify it matches the current conversation. Do not search unrelated workspaces or private sessions. If no path resolves, write a tight digest of the session and pass that instead, identifying its limits.

### 2. Spawn three reviewers in parallel

Spawn three independent review subagents with the host's available delegation tools. Use configured model assignments when available, otherwise inherit the parent model and disclose the lack of model diversity. Reviewers need access to context lookups referenced in the transcript, but must not modify files or external records. If capacity limits parallel execution, run the remaining reviewers as slots become available. If delegation is unavailable, report that this review cannot be completed independently.

| Lens | Prompt template |
|---|---|
| Judgment | [references/judgment-reviewer.md](references/judgment-reviewer.md) |
| Tooling | [references/tooling-reviewer.md](references/tooling-reviewer.md) |
| Divergent | [references/divergent-reviewer.md](references/divergent-reviewer.md) |

Pass each template verbatim, substituting the transcript path or digest where marked. Reviewers return findings in their response body.

### 3. Synthesize

Spawn a separate synthesizer with access to the same scoped evidence and context lookups. Use [references/synthesizer.md](references/synthesizer.md) verbatim, with each reviewer's full output inlined where marked. The synthesizer returns a structured Accepted / Rejected / Backlog list.

### 4. Structural enforcement check

Sanity-check the synthesizer's Accepted list. For any item that would be enforced more reliably by a lint rule, script, metadata flag, or runtime check, move it from Accepted to Backlog. Skill prose is for things mechanisms cannot enforce.

### 5. Apply

Before applying any Accepted edit, present the synthesizer's full Accepted/Rejected/Backlog output to the user and wait for explicit approval. The user picks which subset to apply and may redirect routings. Do not auto-apply based on a request to reflect. Prior explicit approval of the concrete edits remains valid.

File Backlog items to the team's configured devex or backlog tracker within the authorized scope. If no tracker is configured or filing is outside that scope, return the items as unfiled; do not silently drop them. Only the Accepted list waits for edit approval.

For each approved Accepted item, follow the Routing field exactly:

- Trivial existing-skill edit (a one-line bullet, a tightened sentence, a stale fact corrected): parent does directly.
- Substantive existing-skill edit (a new section, a new pattern table, more than ~10 lines): use the available skill-authoring capability and the [authoring playbook](../aasystem/playbooks/authoring-a-skill.md) for its draft / test / iterate loop.
- `tune description: <skill path>` (the skill exists but didn't trigger when it should have): use the skill-authoring capability to tune and test the description.
- `new skill via create-skill: <kebab-name>`: use the skill-authoring capability. Do not invent the shape ad hoc. For an approved personal principle, also follow the existing [principle-authoring convention](references/principle-authoring.md).

If the environment ships a SKILL.md validator, run it on every touched skill before declaring done. Skip this step if it does not.

### 6. Summarize for the user

Short list, no preamble:

- Edits applied: `<skill path>`. What changed, one line each.
- New skills created: `<skill path>`. One line each (rare).
- Backlog filed to the devex tracker: `<issue title>` (`<tags>`), or unfiled with the reason. One line each.
- Dropped: one line per rejected finding + reason from the synthesizer.
