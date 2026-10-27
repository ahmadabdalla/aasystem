---
name: how
description: Trace how an existing subsystem behaves and where responsibilities live. Use for runtime flow, code walkthroughs, ownership, and placement questions; use why for historical rationale.
disable-model-invocation: true
---

# How

Before starting, read the [shared execution contract](../pilot/references/execution.md) in full and the [approved-principle index](../principles/INDEX.md). Follow the contract’s baseline requirements.

Assess the scope, explore the system, reconcile findings, and explain the behavior. Build a working model from the actual code and configuration.

State the target and any consequential scope assumption. Investigate and explain a narrow question directly. For broad systems, use bounded explorers for distinct flows or boundaries when separate coverage or context separation provides a concrete benefit under the shared delegation rule. Synthesize in the current context unless a separate explainer provides a concrete benefit. Require source locations, flow, responsibilities and gaps. Use actual configured models and read-only access where it retains the tools needed. Reconcile conflicting findings against the source; disclose independence limits when claiming independent corroboration.

Trace from the trigger or public entry point through calls, data transformations, state changes, and externally visible effects. Follow both sides of important boundaries. Inspect callers, configuration, representative tests, and failure or concurrency behavior where relevant. Read the implementation rather than guessing from names. Use a focused [probe](../probe/SKILL.md) when an unresolved runtime claim matters; a read-only explanation does not require executing every path.

Explain the core flow, key concepts, responsibility map, and non-obvious constraints at the level needed for the user's decision. Cite exact files, symbols, and lines for material claims. Distinguish behavior traced in code from behavior actually exercised. If a connection cannot be traced, identify that gap. Use a small diagram when it clarifies interactions. Return the explanation to the calling workflow for integration, or present it directly for a standalone question; preserve the explainer's evidence and uncertainty when editing it.

Use [why](../why/SKILL.md) to investigate motivation. Current mechanics alone cannot establish historical intent.
