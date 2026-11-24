# Product discovery

1. **Ground.** Read the existing product records, specs, glossary, decisions and journeys. Agreed behaviour is the baseline: keep proposals apart from it, and report code that breaks it as a defect, not behaviour to keep.
2. **Interview**: call the Skill tool with "grill-me" ([grill-me](../../grill-me/SKILL.md)) and give it the scope, what you already know and where to stop. Call the Skill tool with "how" ([how](../../how/SKILL.md)) for how the current product works. Cover the areas the task needs, such as who uses it and what each may decide, who can access what, how work is organised, handoffs between people, manual work and the first release.
3. **Record** in the project's product folder, or the one the user picks, using the [interview record](../../grill-me/references/discovery-interview.md).
4. **Map each journey:** actor and what they may decide, trigger, outcome, prerequisites, steps, handoffs, how it ends, and what happens when it fails or stops halfway. Mark each part observed, intended, proposed or open, and link its sources. If the product is being replaced, say what each journey would lose and how people would do that work. Call the Skill tool with "domain-modeling" ([domain-modeling](../../domain-modeling/SKILL.md)) for terms.
5. **Requirements** only if the caller asked for them: follow [Product's steps](../SKILL.md#steps) and link each to the answer or decision behind it. Keep them in the one spec (the [OpenSpec convention](../../pilot/references/openspec.md) if the project uses it); discovery notes link to it.

Return the journeys, open questions and who acts next.
