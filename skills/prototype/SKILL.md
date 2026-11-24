---
name: prototype
description: Build and exercise a throwaway prototype that answers one question, either a state model a domain expert can click through, or UI rendered inside the real app. Use probe for research and other experiments.
disable-model-invocation: true
---

# Prototype

Before starting, read the [execution contract](../pilot/references/execution.md) and the [approved-principle index](../principles/INDEX.md), unless already in context.

A prototype is **throwaway code that answers a question**. Your caller owns the decision. If a human invoked you directly, follow the [Prototype playbook](../pilot/playbooks/prototype.md) as your caller. You build the artifact, exercise it and return what you saw. If the question isn't about business state or UI, use [Probe](../probe/SKILL.md) instead.

## Pick a branch

- **"Does this logic or state model feel right?"** Follow [logic-prototype.md](references/logic-prototype.md): one HTML file a domain expert can click through.
- **"What should this look like?"** Follow [ui-prototype.md](references/ui-prototype.md): one candidate or several variants, rendered inside the real app.

If the brief doesn't say which, pick one and state why at the top of the prototype. If an unknown would change what you build and you can't infer it, ask one question and wait. If you can't reach the human, return the question to your caller.

## Rules for both

1. **Isolate it.** If it mounts in the app, build it in a separate worktree. Otherwise, build it in a scratch directory outside the repository. Name it so a reader can see it's a prototype.
2. **Make it trivial to run.** One command or file launches it, and one action resets it.
3. **No live side effects.** Keep state in memory and stub every mutation. If persistence is the question, create a new scratch store named as a prototype, and let reset wipe only that.
4. **Skip the polish.** No test suite, and no error handling beyond what keeps it runnable.
5. **Keep to the brief.** If the prototype needs a business rule, scope or interaction choice the brief doesn't give, show it as a labelled proposal and return it.

## Observe and return

Exercise it yourself before handing it over: launch it the way the recipient will and run each scenario from reset. If the demo can't express the rule, fix the demo before you judge the idea. A screenshot shows layout; it doesn't prove an interaction you didn't drive.

Return:

- the question and the alternatives
- the artifact path, its revision if it's in a worktree, and launch and reset steps
- what you did, expected and saw, with evidence paths
- human feedback, with who gave it, or "no human feedback yet". An agent's review, yours included, is an assessment, not acceptance
- the decision, or the open choice and who decides it
- what the prototype can't show: production reliability, permission enforcement, persistence and integration
- through the caller: business-meaning changes for [Product](../product/SKILL.md), interaction choices for the interaction owner, feasibility questions for [Architect](../architect/SKILL.md)

Leave the artifact where it is. Copy it into production, commit, publish, update a tracker or delete it only when the caller asks.
