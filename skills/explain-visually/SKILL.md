---
name: explain-visually
description: Present a change, design, or finding as an inline plain-text diagram, usually a before-and-after comparison. Use for terminal-readable explanations of established evidence; Investigation grounds missing facts.
disable-model-invocation: true
---

# Explain visually

Before starting, read the [shared execution contract](../pilot/references/execution.md) in full and the [approved-principle index](../principles/INDEX.md). Follow the contract’s baseline requirements.

Own the visual presentation: help someone outside the session understand what changed, why it matters, what remains familiar, and how we know. Produce the diagram inline in a fenced `text` block, followed by its source keys and then a one- or two-sentence takeaway naming the pattern to recognize. No image, browser, or external rendering tool is needed. Save an artifact only when requested, preserving project-owned formats.

## Use established evidence

Identify the subject, intended reader, and evidence already established in the conversation, code, design, and check results. [Investigation](../pilot/playbooks/investigation.md) owns grounding. When invoked directly and a material fact is missing, establish it there, then return here to present the findings; when another workflow is the caller, return the gap to it. Apply the execution contract’s [scope and proof](../pilot/references/execution.md#scope-and-proof) distinctions to every claim, including labels and arrows.

## Choose the layout

Use the mode the user requests:

- **`before-after`** (default): side-by-side **BEFORE | AFTER** when evidence establishes two meaningful states. Label an unimplemented state **PROPOSED**, not as an observed after-state. Keep the same components and scenarios aligned across columns so the difference is visible.
- **`flow`:** a single-column request or data path.
- **`layers`:** a single-column sketch of who owns what.

Without a requested mode, fall back to `flow` or `layers` when there is no meaningful before. If a requested `before-after` has no meaningful before, show the after or proposed state alone and say why. If columns would wrap, stack the before and after sections. Aim for 80–100 display columns and stay within 120; shorten labels or move source details below the diagram instead of compressing text into unreadable boxes.

Use boxes for components and arrows for direction or access. Unicode box drawing (`┌─┐`, `│`, `└─┘`) and section breaks (`═══╪═══`) are useful when supported; use ASCII (`+`, `-`, `|`, `->`) when requested or needed by the terminal. Pair `✓` / `✗` with words such as “allowed” / “denied,” so their meaning is explicit.

## Show the difference

Use these sections in this order. Include the first three when they explain the subject; always include Proof:

1. **Structure or access:** show each relevant component, responsibility, and boundary; put what it can reach or do inside its box.
2. **Impact:** follow one concrete request, failure, or misuse scenario through the structure and show its outcome in each state. Include commands only when established and useful; never run them to produce a result. Do not force a security narrative onto another kind of change.
3. **Experience:** show the system user’s day-to-day actions, marking established unchanged steps “(same),” plus any one-time action.
4. **Proof:** name the checks and their actual results, including the before result when available. Mark absent before results, checks not run, and inference explicitly. An expected result is not an observed pass.

Keep residual limits beside the affected after/proposed behavior. Do not hide them in the takeaway. Never include secret values, even partially; show only their locations and kinds. If a hidden value matters, label it “hidden” or “redacted” without reproducing its contents.

Use compact source keys such as `[1]` beside claims, with resolvable file/line, design, or session-observation pointers immediately below the diagram. A shared key may cover several claims from one source. Keep references outside the columns when they would break alignment.

Before returning, trace each material claim to its source, check column alignment and width, and remove decoration or repeated prose that obscures the comparison. Return the explanation and evidence limits to the caller, or deliver them directly for a standalone invocation.
