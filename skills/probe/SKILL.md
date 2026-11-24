---
name: probe
description: Resolve a consequential assumption with research, observation, or a small experiment before making a decision. Use when reality can answer an unknown; use project verification to check a finished implementation.
user-invocable: false
---

# Probe

Before starting, read the [execution contract](../pilot/references/execution.md) and the [approved-principle index](../principles/INDEX.md), unless already in context.

A probe answers **one question** that blocks a decision. A "no" is a useful answer.

1. **Write the question.** One line that could prove false, and the decision it changes, such as "Does the webhook retry after a 500? If yes, we drop our retry queue." Write what you'd see if yes and if no. If part of the question is a preference, name that decision and who owns it, and probe only the facts.
2. **Pick the cheapest source that can answer it.**
   - **What a tool says it supports:** read its current official docs and their conditions.
   - **What it actually does** (runtime, permissions, speed, persistence): run it somewhere like the real environment. A mock or an existing test shows only the path it runs, so check that it runs the real one.
3. **Run it.** If the run would touch production, shared data or a paid service, ask first. Keep throwaway work in a scratch directory or worktree. Record inputs, versions, environment, method and what you saw. If you compare options, run each under the same conditions. If results vary, repeat and report the spread. Check that you measured what the question asks.
4. **Return the answer.** Say **supported**, **refuted** or **inconclusive**, with evidence, confidence, limits and what it means for the decision. Label each claim as documented, observed or inferred. Stop when more work wouldn't change the decision. If the answer is inconclusive, name the next observation that would settle it.

One run proves only the conditions it ran under. Leave scratch code in scratch; whoever asked decides what to build.
