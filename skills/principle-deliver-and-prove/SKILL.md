---
name: principle-deliver-and-prove
description: Establish readiness to deliver an implementation and verify its expected behavior before editing. Use when beginning implementation or when new findings change what delivery or proof requires.
disable-model-invocation: true
---

# Be ready to deliver and prove

At the start of implementation, answer two questions:

1. **Do I have everything I need to deliver this?**
2. **Do I have everything I need to verify what I build and prove it?**

Ground the answers in the assigned scope, project instructions and observed evidence. Delivery needs clear expected behavior, relevant conventions, accessible inputs and usable dependencies. Proof needs a runnable verification path, its prerequisites and a way to compare observed outcomes with the agreed expectations. Establish that path before depending on it; finding test files alone does not show that it works.

Resolve gaps within authorized scope before the work that depends on them. Use the existing [project verification routes](../pilot/references/execution.md#verification-through-the-project); return material conflicts or unavailable prerequisites to the owner under the [decision authority rules](../pilot/references/execution.md#decision-authority). Revisit the questions when findings change either answer.

Prefer discovering delivery and proof gaps early to building on untested assumptions. Match the checks to the change: an exact presentation edit needs its relevant checks, while a behavior change needs evidence from the affected surface. Code checks support only the boundaries they exercise; identify any system validation still needed. A failing baseline can be useful proof of a reported bug. Record material gaps and intended checks in the existing task brief; these questions add no routine approval or separate report. Readiness establishes a way to obtain proof; completion still requires the actual results.
