---
name: domain-modeling
description: "Pin down what project terms mean and record the decisions that matter, in a glossary and ADRs. Use when a term or relationship is ambiguous, or when recording, changing or reviewing a project decision."
disable-model-invocation: true
---

# Domain Modeling

Before starting, read the [execution contract](../pilot/references/execution.md) and the [approved-principle index](../principles/INDEX.md), unless already in context.

If the project already has a glossary, ADRs, contexts or its own formats and locations, use them. The defaults below apply only where it has none.

Start by reading the project instructions, then the glossary and ADRs for the area. If a `GLOSSARY-MAP.md` exists, use it to find the right context's glossary.

## During the session

**Challenge against the glossary.** If the user's word conflicts with the glossary, say so: "Your glossary defines 'cancellation' as X, but you seem to mean Y. Which is it?"

**Sharpen fuzzy words.** If a word is vague or overloaded, propose one precise term: "By 'account', do you mean the Customer or the User?"

**Test with a scenario.** Check each meaning or relationship against a concrete example, including an edge case where getting it wrong would matter.

**Check the code.** If the code contradicts what the user says, show the contradiction and ask which is right. Record the agreed meaning and report the code as a mismatch. Don't redefine the term to match the code.

If a meaning that matters stays unclear, ask one question and wait. If no user is present to answer, return the question with your recommended answer, and don't record the term as agreed. If several dependent choices are open, use [grill-me](../grill-me/SKILL.md).

## Glossary

Add or change a term as soon as its meaning is agreed.

Default to one `GLOSSARY.md` at the root. If established contexts use a word differently, give each context its own `GLOSSARY.md`. If there are several and the project has no way to find them, add a root `GLOSSARY-MAP.md` that links each context.

```md
**Customer:** The organisation that owns a subscription. A customer may have several users.
_Avoid_: client, account

**User:** A person with access to a customer's subscription.
```

- Pick one word per concept. List the others under `_Avoid_`.
- Keep each definition to one or two sentences.
- Include only concepts specific to this project; leave out general programming terms and implementation details. Plans, open hypotheses and decision rationale go in their own records.

## Decisions

Before creating, editing or reviewing an ADR, read [adr.md](references/adr.md). Most choices don't need one: an ADR is only for a choice that is hard to reverse, surprising without context and a real trade-off. Keep other choices in the task or design record.

## Edits

If the task allows edits, make them. If the work is read-only, return the proposed wording and the file it belongs in.

When you create or change a glossary or ADR, check that the project instructions (`AGENTS.md`, `CLAUDE.md` or equivalent) have one short line telling agents to read the relevant terms and decisions before changing that area. If the instructions already point agents at the glossary and decisions, leave them as they are. Otherwise, for ADRs, the line also names the project's ADR rules and says to check edits and the final diff against them. Use real project paths: the line and the records must work without this toolbox. Leave unrelated instructions alone.

## Return

- the agreed meaning or decision, and its path if saved
- the evidence it rests on, and what you couldn't check
- the acceptance criteria it changes, so the caller can update the verification plan

Link the record from the brief, requirements, solution or design record; don't copy its text. A glossary edit or an accepted ADR doesn't change the code or prove it passes.
