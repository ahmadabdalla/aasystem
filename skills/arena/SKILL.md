---
name: arena
description: Have separate agents attempt the same design or artifact, judge them, and combine the best into one checked result. Use when an early wrong shape would be costly to undo.
user-invocable: false
---

# Arena

Before starting, read the [execution contract](../pilot/references/execution.md) and the [approved-principle index](../principles/INDEX.md), unless already in context.

1. **Write one brief.** Include the question, the evidence and its limits, the required behaviour and the output format. If a workflow called you, use its brief and format. If a gap would make candidates answer different questions, settle it first.
2. **Set the criteria.** Before any candidate starts, write three to six criteria that would tell the options apart, such as "who owns retry state". Give them to the judge, not the candidates.
3. **Run the candidates.** Start at least two separate agents. Each gets the same brief, the raw files and its own output location. None sees another's work or the answer you'd pick. Each returns its artifact, why it chose that shape and what it rejected. If you can't start separate agents, write the alternatives yourself in turn and say they're one agent's work, not independent.
4. **Check the field.** If two design candidates share the same boundary, owner, data shape and interaction model, count them as one. If all candidates share a premise the evidence doesn't force, run one without it. If fewer than two distinct candidates finish, say there was no real comparison. Add a candidate only if it would offer a different shape.
5. **Judge.** Once every candidate has finished, give a separate judge, from another model family if you have one, the criteria and the candidates labelled A, B, C. Meanwhile, score every artifact yourself against the criteria. Where your scores and the judge's differ, settle it from the artifacts or by calling the Skill tool with "probe" ([probe](../probe/SKILL.md)), not a vote. If you can't start a judge, label the pick lead-only.
6. **Combine.** Pick one candidate as the base. Add the parts of others that fit it, noting where each came from, and say why you rejected the rest. If candidates solved different problems, fix the brief and rerun.
7. **Check the result.** The combined result is new, so no candidate's passing check carries over. For code, run the project's verification. For a recommendation, back each claim. For a design, check that usage, shape, constraints and verification plan agree.

Return one result in the caller's format, with a short record: the base, what you added and from where, what you rejected, both verdicts, any dropouts or limit on independence, and the evidence.
