# Skill authoring

1. Name the behaviour the change must produce. If it captures a judgment or correction, run [Reflect](../../reflect/SKILL.md) to choose where it lives and what evidence backs it.
2. Trace the task from the entry skill through every file it reaches. If a rule must always apply, put it in a file the agent always reads. Agents skip "read this" links.
3. Edit the file that owns the rule. Write "If X, do Y." Link to a shared rule instead of copying it. Keep routing in the entry skill, and keep what the next skill needs at each handoff. Cut any line the model already follows. Add a line only when a run showed the failure without it.
4. Split a skill only when a caller needs part of it alone. Put a long procedure that applies only sometimes in a linked reference.
5. Keep the required metadata and the existing invocation settings. New portable skills set `disable-model-invocation: true` and ship `agents/openai.yaml` with `policy.allow_implicit_invocation: false`. Generated project verifiers keep their own discovery policy.
6. Validate. Parse the frontmatter, check names and every changed link, and run the shipped helpers. If a strict validator rejects a deliberate host extension, report it as an extension, not malformed metadata. Check on each real host that the skill is found, runs when named, and calls its supporting skills.
7. If the change touches routing, ownership, handoffs or proof, run [Evaluation](eval.md). If it only changes wording, report it as structurally reviewed only.
8. Report the changed lines, what they should change, what you checked and what you couldn't. If you're asked to open a PR, follow [Opening a PR](opening-a-pr.md).
