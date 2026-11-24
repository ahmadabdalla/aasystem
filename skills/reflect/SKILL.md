---
name: reflect
description: Review a session with three independent reviewers and turn the lessons the user approves into skill edits, principles or backlog items. Use when the user says reflect.
---

# Reflect

Before starting, read the [execution contract](../pilot/references/execution.md) and the [approved-principle index](../principles/INDEX.md), unless already in context.

Find lessons in this session that will still hold next month, and turn the ones the user approves into edits. If the session was trivial, say so and stop.

## 1. Find the transcript

Use this session's transcript file if the host exposes it, and check it's this session. Never read another project's or session's. If you can't find it, write a digest instead: what was asked, what went wrong, what the user corrected, and what the digest leaves out.

## 2. Run three reviewers

Start three reviewers in parallel, each in a fresh context. Send each the `<reviewer-prompt>` from [reviewer.md](references/reviewer.md), with `<TRANSCRIPT>` replaced by the path or digest and `<LENS>` by one lens block: judgment, tooling or divergent. If your host has no subagent tool, say the review can't be done independently, and stop.

## 3. Synthesize

Start a fourth agent with [synthesizer.md](references/synthesizer.md), filling in the transcript and all three reviewers' full output.

## 4. Ask the user

Show the lists as the synthesizer returned them. **Apply only the rows the user approves.** Saying "reflect" isn't approval.

## 5. Apply

Make each approved row with the [authoring playbook](../pilot/playbooks/authoring-a-skill.md). For a principle, follow [principle authoring](references/principle-authoring.md). File each approved Backlog row in the project's tracker.

## 6. Report

No preamble:

- Edited: `<path>`: what changed, one line each.
- Created: `<path>`: one line each.
- Backlog: `<issue link>`, or "not filed: <reason>".
