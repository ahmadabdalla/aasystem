---
name: why
description: Reconstruct why an existing design or behavior took its current shape. Use for rationale, historical constraints, regressions, and thresholds; use how for current mechanics.
user-invocable: false
---

# Why

Before starting, read the [execution contract](../pilot/references/execution.md) and the [approved-principle index](../principles/INDEX.md), unless already in context.

1. **Name the target.** Say in one line which file, symbol, value or decision you're explaining, such as "Why is the retry limit 3? `src/queue.ts:42`." If you don't know how it works today, call the Skill tool with "how" ([how](../how/SKILL.md)) to trace it first. If the user offers a reason, treat it as a guess to check.
2. **Find the origin.** Run `git log --follow` (or `git log -L` for a line) to find the commit that introduced the target, across renames. A recent edit that touches the line is rarely the reason. Done when you have the introducing commit, or you've said where the trail ends.
3. **Read the records.** Read the project's ADRs for this area, and the reviews, issues and incidents the history points to. An accepted record from the time can state the reason. A proposal or a later write-up is weaker. If a record was superseded, read what replaced it. For a defensive check or an odd number, look for the incident behind it.
4. **Account for every source.** Go through source control, the issue tracker, design docs, team discussions, infrastructure, error records and product data. Mark each one: found something, searched and found nothing, can't access, or can't answer this question (say why). Before marking a source as can't access, try the tools you have. A source you can't access is a gap, not proof there was no reason.
5. **Check the constraints.** For each constraint the records give, check whether it still holds today, and cite what shows it. If the recorded reason no longer matches the code, say so.
6. **Label each claim.** Cite each claim and check the source says what you claim.
   - **Direct:** a record from the time states the reason.
   - **Supported:** several independent clues agree.
   - **Inferred:** a plausible reading, with your reasoning.
   - **Speculative:** weak evidence, or rivals just as likely.
   - **Unknown:** the sources you searched can't answer it.

   Today's code shows what it does, not why.
7. **Answer.** Give a short timeline, every claim with its bold label and citation, any conflicting records or rival explanations, which constraints still hold, and the source list from step 4.

If the sources are too many for one context, split them under the [delegation rule](../pilot/references/delegation.md). Give each worker the same target, question and labels. Check their citations yourself.

If a change follows, list what to preserve, change, avoid and treat as risk, each with its evidence or uncertainty. Hand that to the [`solution`](../solution/SKILL.md) or [`architect`](../architect/SKILL.md) skill.
