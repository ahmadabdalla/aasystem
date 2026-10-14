---
name: figure-it-out
description: Design and execute a verifiable task-specific workflow when no bundled playbook fits or a change spans coupled phases. Use for bounded migrations and unfamiliar multi-part work; preserve plan-only requests and explicit checkpoints.
disable-model-invocation: true
---

# Figure it out

Before starting, read the [shared execution contract](../aapilot/references/execution.md) in full and the [approved-principle index](../principles/INDEX.md). Follow the contract’s baseline requirements.

Produce the workflow before executing it. Scale rigor through concrete checks and artifacts, then retain the evidence for the owner's final judgment.

## Frame

Reuse the current brief, discovery, and [principle index](../principles/INDEX.md). Establish the intended outcome, scope, constraints, actual capabilities, and a checkable completion predicate. For research, the predicate can be a supported answer with unresolved claims identified; do not invent an implementation test for a value judgment.

Name any missing specialized procedure or external prerequisite. A custom workflow must explain its credible proof path and limits. Present the proposed phases and tradeoffs before substantial execution. A plan-only request ends with the plan; honor requested checkpoints and ask one question and wait if a material choice cannot reasonably be assumed.

## Design the phases

Divide the task into independently checkable units with explicit inputs, owners, artifacts, evidence gates, and dependencies. Put the riskiest unknowns and necessary baseline or harness work first. Use [probe](../probe/SKILL.md) for empirical uncertainty and [architect](../architect/SKILL.md) for an unresolved consequential shape; this workflow retains implementation.

Use [swarm](../swarm/SKILL.md) only for independent ready slices and [arena](../arena/SKILL.md) for unresolved alternatives. Reuse settled designs. Establish a stopping or reconsideration condition for repeated failed hypotheses and a practical bound for expensive experiments. New information can change the plan; record why.

## Execute and record

When execution is authorized, follow the phase list and use [show-me-your-work](../show-me-your-work/SKILL.md) from the first consequential decision. For each unit, state the expected effect, assign production edits and development checks to [Implement](../implement/SKILL.md), and inspect the returned artifact before retaining or revising it. Non-production units follow their assigned procedure. Verify each unit before dependent work starts. Revert only owned experimental changes whose hypothesis failed.

Use [independent verification](../aapilot/references/execution.md#independent-implementation-verification) for production implementation and separate adversarial review when warranted. If a check passes suspiciously easily, inspect its observation method. Fix a defective check as a separately explained change; never lower the product contract to make the result pass. Record verified, failed, and inconclusive results distinctly. If a required gate cannot be met, stop dependent work and return the established evidence and precise gap.

## Finish

Check the integrated result against the original completion predicate and the requested delivery boundary. Account for every phase, evidence gate, and deferred item. Report the workflow followed, significant changes of direction, decision-log path, proven outcomes, and remaining limitations. A completed checklist without artifact evidence does not establish completion.
