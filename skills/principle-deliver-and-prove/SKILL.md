---
name: principle-deliver-and-prove
description: Before editing, check you can deliver the change and prove it works. Use when starting implementation, or when a finding changes what delivery or proof needs.
disable-model-invocation: true
---

# Be ready to deliver and prove

Before you edit, answer two questions:

1. **Can I deliver this?** You need the expected behaviour, the project's conventions, and inputs and dependencies you can actually reach.
2. **Can I prove it?** You need a check you can run, what it needs to run, and an agreed expected result to compare against.

Establish that the check runs before you depend on it. Test files existing don't show that.

If either answer is no, fix the gap within your assigned scope before the work that depends on it, using the [project's verification routes](../pilot/references/verification-contract.md#verification-through-the-project). If you can't, or the gap is a conflict that changes what you'd build, return it to the owner under [Ask the human](../pilot/references/execution.md#ask-the-human). If a finding changes either answer, answer again.

Match the checks to the change. A presentation-only edit needs presentation checks; a behaviour change needs evidence from the surface it affects. If a check covers only part of the change, name the system check still needed.

Write gaps and planned checks into the existing brief, not a new report or approval step.

Why: finding a delivery or proof gap early beats building on an untested assumption.

Where it stops: being ready to prove isn't proof. Finishing still needs the results.
