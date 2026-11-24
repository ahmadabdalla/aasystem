---
name: explain-visually
description: Explain how something works, who owns what, or what changed with a plain-text diagram. Match the layout to the question and write plainly.
disable-model-invocation: true
---

# Explain Visually

Before starting, read the [execution contract](../pilot/references/execution.md) and the [approved-principle index](../principles/INDEX.md), unless already in context.

1. **Get the subject.** If the request and conversation name no subject, ask "What would you like me to explain visually?" and stop.
2. **Get the facts.** If the diagram needs a fact the conversation and code don't show, find it with [Investigation](../pilot/playbooks/investigation.md); if a workflow called you, return the gap to it instead. Draw what the code does. If a doc says otherwise, say so under the diagram.
3. **Pick the layout from the question.** If the user named a layout, use it.
   - "How does it work?" → **flow**: one real example, top to bottom, one step per line.
   - "Who owns what?" → **layers**: an indented tree of groups, the files in each, and what each owns or reads beside it.
   - "What changed?" → **before-after**: the after under the before, showing only the parts that change, in the same order. Label anything not built **PROPOSED** and cite where it's proposed. If there is no before, say so in one line and show only the after.
4. **Draw it small.** One diagram, up to 7 boxes and 80 columns. If it needs more, group parts into one box. Draw a second diagram only for a second question. Draw only the arrows the question asks about, and none that cross a line or a box. Name parts that everything uses, such as the store, in one line under the diagram. Label each arrow with a verb, such as "sends code". If a flow loops, write "(back to step 2)" instead of drawing the arrow.
5. **Keep it aligned.** Put each diagram in a `text` block. Use only keyboard characters: `+ - | > v`, letters and digits. Write "allowed" or "denied", not a tick or cross. Line up every column: each box's right edge, and the text beside each line of a tree.
6. **Cite under it.** Put keys like `[1]` in the diagram and list each `file:line` under it. Show a secret's name and where it lives, marked (hidden), never its value or any part of it.
7. **Say the point.** After the diagram, write one or two sentences on what the reader would miss. Add nothing else unless asked.
8. **Check it.** Read each diagram row by row: columns line up, no row passes 80 columns, no arrows cross, at most 7 boxes, every box and arrow has a source. Fix and recheck.

If a workflow called you, return the diagram and its limits to it. Otherwise give them to the user. Save to a file only if asked, in the project's format.
