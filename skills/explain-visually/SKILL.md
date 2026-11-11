---
name: explain-visually
description: Explain how something works, who owns what, or what changed with a plain-text diagram. Match the layout to the question and write plainly.
disable-model-invocation: true
---

# Explain visually

Read the [shared execution contract](../pilot/references/execution.md) in full and the [principle index](../principles/INDEX.md). Follow the baseline requirements.

If the request and conversation give no subject, ask “What would you like me to explain visually?” and wait for the answer. Do not invent a topic or example, or investigate without a subject. Use existing context when the subject is clear; missing audience or layout alone need not block work.

Answer the reader's question with compact diagrams inline in fenced `text` blocks. Use the requested number; otherwise start with one and add more only to avoid crowding or answer another requested question. No rendering tool is needed. Save a file only when asked, using the project's format.

## Use known facts

Use the conversation, code, designs, and check results. [Investigation](../pilot/playbooks/investigation.md) handles missing facts: for a direct request, investigate important gaps before drawing; for an assigned task, return gaps to the caller. Follow [scope and proof](../pilot/references/execution.md#scope-and-proof), including for labels and arrows. Label hypothetical examples as hypothetical.

## Choose the layout

Use the requested mode, or choose by the question:

- **How does it work? — `flow`:** show one request, action, or example in step order.
- **Who owns what, or how do parts relate? — `layers`:** group parts and show their relationships. Do not imply a sequence where none exists.
- **What changed? — `before-after`:** align the same parts and example across two states. Label unimplemented behavior **PROPOSED**.

Do not invent a before-state. For alternatives, align both and label them by name. If a requested before-and-after has no before, show the current or proposed state and say why. Stack comparisons if columns would wrap. Keep diagrams within 80–100 columns where possible, never over 120; shorter is fine. Shorten labels and put source details below the diagram.

Use boxes for useful groups or boundaries, and arrows for direction, access, or relationships. Use Unicode or ASCII as the terminal supports; honor requests for ASCII. Pair `✓` / `✗` with words such as “allowed” / “denied.”

## Write plainly

- Use concrete, consistent names and short sentences suited to the reader. Explain needed unfamiliar terms on first use.
- Keep one idea per box. Label arrows with actions or relationships, such as “sends query” or “owns invoices,” rather than “handles” or “integrates.”
- Carry one example through a process. Include commands only when known and useful; do not run them to fill the diagram.
- Skip preambles, filler, repeated summaries, and forced pattern names. Add sections, impact, user actions, or checks only if they answer the question. Do not force a change report or security story.
- Follow the diagram and any sources with one or two sentences explaining the point, without repeating every label.

## Show sources and limits

For important claims about a real system, use keys such as `[1]` and list the file/line, design, or conversation source below the diagram. One key can cover several claims. For a general concept or hypothetical, state the assumptions; do not invent sources or results. Keep the caller's sources and limits.

Include check results and gaps when they matter to the answer. Distinguish expected results from observed passes. Put important limits beside the affected behavior, even without a separate proof section. Never show secret values, even partly; show only their type and location, marked “hidden” or “redacted” where needed.

Before returning, check the answer, labels, sources, alignment, and width. Remove jargon, decoration, and repeated prose. Give the explanation and its limits to the caller, or directly to the user for a standalone request.
