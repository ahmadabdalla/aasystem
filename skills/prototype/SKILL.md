---
name: prototype
description: Build and exercise an inspectable throwaway artifact to explore business state, refine specified presentation, or compare UI interactions. Use for concrete logic walkthroughs and contextual UI alternatives; use probe for research and other empirical unknowns.
disable-model-invocation: true
---

# Prototype

Before starting, read the [shared execution contract](../pilot/references/execution.md) in full and the [approved-principle index](../principles/INDEX.md). Follow the contract’s baseline requirements.

Own the inspectable artifact and its observations. The caller coordinates the larger task; the [prototype playbook](../pilot/playbooks/prototype.md) owns standalone experiments, and [probe](../probe/SKILL.md) owns the empirical method. Reuse the caller's question, decision criteria and grounding rather than reopening settled choices.

## Frame and build

Carry the source question, affected decision, authorized scope, requirements and their status, relevant domain terms, representative scenarios, and expected observations into the experiment. Distinguish a model's observable behavior from a preference requiring human judgment. When an unknown materially changes the experiment and cannot be inferred, ask one focused question and wait; otherwise state the assumption and proceed.

Read the reference matching the uncertainty:

- [Logic prototype](references/logic-prototype.md): let a domain expert drive actions and inspect business states, including awkward and forbidden transitions.
- [UI prototype](references/ui-prototype.md): render a specified candidate or compare consequential interaction structures in representative application context.

Use both only when they answer distinct necessary questions. Use [interaction-design](../interaction-design/SKILL.md) for the interaction model and its rationale; a prototype supplies evidence to that owner.

Build in an isolated scratch location or checkout, identified as a prototype, with a simple launch instruction. Keep mutations in memory or explicit stubs; persistence experiments use owned scratch storage. Preserve the context needed for a credible observation without silently enabling live side effects. Add only the scaffolding and checks needed to trust the answer.

## Observe and return

Exercise the actual artifact on its intended surface, including reset and the scenarios that discriminate the choices. Record expected and observed results, inputs, environment, revision or source identity, and evidence paths under the execution contract. Distinguish a broken demo from evidence against the proposed model. A screenshot can show layout; it cannot prove an unexercised interaction.

Return the question, alternatives, artifact path and launch/reset instructions, observations, human feedback with its source when available, decision or unresolved choice, and evidence limits. Agent reviews are assessments, not human acceptance. Return changed business semantics, interaction choices and technical feasibility findings through the caller, identifying [Product](../product/SKILL.md), the interaction owner or a design-only [Architect](../architect/SKILL.md) assignment as appropriate.

Keep the production boundary explicit: prototype behavior does not prove production reliability, authorization enforcement, persistence or integration. Hand selected findings to the current owner; production implementation needs its authorized workflow and verification. Retain evidence under the shared contract; do not automatically promote code, publish, commit, update external trackers, or discard artifacts.
