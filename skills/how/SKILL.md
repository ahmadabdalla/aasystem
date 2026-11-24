---
name: how
description: Trace how an existing subsystem works and where each responsibility lives. Use for runtime flows, signal paths, code walkthroughs, ownership and placement questions; use why for history.
disable-model-invocation: true
---

# How

Before starting, read the [execution contract](../pilot/references/execution.md) and the [approved-principle index](../principles/INDEX.md), unless already in context.

1. **Name the target.** Say in one line what you'll trace and where it starts, such as "How does a reset email get sent? Starting at `POST /reset`." If the question has two readings, pick one, say which, and go on.
2. **Trace it.** Start at the trigger: a command, route, event or scheduled job. Follow the calls through state changes to the effect a person or another system sees. Read the code, not the names. At each boundary that matters, read both sides. Check the callers, the config and the tests. If the question touches failures or concurrency, trace those paths too. Done when each step from trigger to effect has a file and line, or is named as a gap.
3. **Split only broad questions.** If the question spans separate flows, give each flow to an explorer under the [delegation rule](../pilot/references/delegation.md). Ask each for file locations, the flow, owners and gaps. If explorers disagree, settle it against the source yourself.
4. **Probe what reading can't settle.** If a runtime claim matters and the code doesn't settle it, run a focused [probe](../probe/SKILL.md). Mark each runtime claim as traced or run.
5. **Explain.** Give the flow in order, who owns each step, and the constraints a reader would miss. Go only as deep as the caller needs. Keep each step's file and line, and each gap, in the answer.

If a workflow called you, return the explanation to it. If the user wants a diagram, use [Explain Visually](../explain-visually/SKILL.md).

If the question asks why it was built this way, give that part to [why](../why/SKILL.md). Code shows what happens, not why.
