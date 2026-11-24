---
name: figure-it-out
description: Design and execute a verifiable task-specific workflow when no bundled playbook fits or a change spans coupled phases. Use for bounded migrations and unfamiliar multi-part work; preserve plan-only requests and explicit checkpoints.
user-invocable: false
---

# Figure it out

Before starting, read the [execution contract](../pilot/references/execution.md) and the [approved-principle index](../principles/INDEX.md), unless already in context.

1. **Write "done when".** One line you can check on the real result, such as "every caller reads the new format and the suite passes". For a research or value question, done is a sourced answer with open claims named; don't invent a test for a judgement. If you can't write one you could prove within the request, stop and say what's missing.
2. **Split the job into phases.** For each phase, write its input, its output, the check that proves it and what it waits on. Put the baseline first: build any missing checks and record the current behaviour they'll compare against. Put the riskiest unknown next. Name anything this environment lacks, such as a credential or an outside service. Build and test everything you can without it; stop only at the step that needs it.
   - If an experiment can answer an unknown, call the Skill tool with "probe" ([probe](../probe/SKILL.md)).
   - If the shape is unsettled and costly to get wrong, call the Skill tool with "architect" ([architect](../architect/SKILL.md)).
   - If phases are independent and ready, call the Skill tool with "swarm" ([swarm](../swarm/SKILL.md)).
   - If approaches compete and nothing has settled the choice, call the Skill tool with "arena" ([arena](../arena/SKILL.md)).
3. **Show the plan.** If the user asked for a plan only, return it and stop, with no edits. If they named another checkpoint, stop there. If a phase needs a decision only the user can make, ask before that phase. Otherwise carry on.
4. **Run each phase.** Call the Skill tool with "show-me-your-work" ([show-me-your-work](../show-me-your-work/SKILL.md)) to keep a decision log. Call the Skill tool with "implement" ([implement](../implement/SKILL.md)) to make production edits. Run the phase's check and read the result yourself, not a report about it. Mark it verified, failed or inconclusive; inconclusive isn't a pass. Start a phase only after the phases it waits on are verified.
   - If an experiment fails, revert your own edits and log why the plan changed.
   - If a check passes too easily, say what it actually observes and why that can't fail. If the check is wrong, fix it as its own change; never weaken the requirement to make it pass.
   - If you can't meet a gate, stop the phases that depend on it and keep what's proven. Say what's needed to continue and who can provide it.
5. **Check the whole.** Run the "done when" check on the integrated result. Get [independent verification](../pilot/references/verification-contract.md#independent-implementation-verification) for production code you keep.

Reply with each phase's verdict and evidence, where the plan changed and why, the decision-log path and what's still open.
