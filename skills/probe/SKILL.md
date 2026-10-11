---
name: probe
description: Resolve a consequential assumption with research, observation, or a small experiment before making a decision. Use when reality can answer an unknown; use project verification to check a finished implementation.
disable-model-invocation: true
---

# Probe

Before starting, read the [shared execution contract](../aapilot/references/execution.md) in full and the [approved-principle index](../principles/INDEX.md). Follow the contract’s baseline requirements.

Resolve a consequential unknown with evidence proportionate to the claim.

1. State one falsifiable question, the decision it affects, and the assumptions in the method. Establish what observation would support or refute the claim before running it. If the question is a preference, identify the human decision rather than disguising it as an experiment.
2. Choose the cheapest credible source or experiment. For a capability claim, inspect current primary documentation and its conditions. For actual runtime, permission, throughput, or persistence behavior, use a representative environment. A simulation or mock establishes only what its model represents. In an advisory research task, report the evidence and limitations without expanding into implementation.
3. Run within the existing authorization and cost bounds. Isolate throwaway work when needed. Record inputs, versions, environment, method, and observed results. For comparisons, use comparable conditions and enough repetitions to distinguish noise when variability matters. Check that the observation measured the claimed thing.
4. Return supported, refuted, or inconclusive, with evidence, confidence and limits, and the implication for the decision. Keep documented capability, observed behavior, and inference distinct. Stop when further work would not change the choice; otherwise name the next discriminating observation.

A probe's success is a useful answer, including a negative one. Do not promote a scratch prototype into the implementation or claim that one successful observation proves all operating conditions.
