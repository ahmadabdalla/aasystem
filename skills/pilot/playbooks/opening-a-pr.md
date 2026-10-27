# Opening a PR

Use when the user or established task instructions authorize PR delivery. Opening a PR does not authorize monitoring, merging, or deployment.

1. **Check the delivery context.** Read repository instructions, branch state, target branch, changed files, and existing PRs. Use the project's supported worktree and forge tools. Preserve unrelated work and shared history. Reuse the task's PR instead of creating a duplicate.
2. **Review the complete change.** Inspect the diff and retained evidence. Remove unsupported experimental edits, accidental artifacts, and unnecessary prose. Use [interrogate](../../interrogate/SKILL.md) for contested or consequential changes. Address supported findings within scope and rerun affected verification. Material unverified claims must be visible to the reviewer.
3. **Prepare the change history.** Follow repository commit conventions and keep meaningful units ordered with their proof. For bug fixes, preserve failing-before and passing-after evidence. Rewrite only owned history when authorized; do not reset or force-push shared work to manufacture a tidy sequence.
4. **Write the reviewer brief.** Give the reason, behavior changed, scope, important tradeoffs, affected consumers, verification results, and unresolved gaps. Link detailed artifacts rather than pasting the full investigation. Use repository title conventions and its required PR template. Choose readiness from the actual review state and project rules.
5. **Publish and verify.** Use the host's supported PR tool or the repository's established forge CLI. Verify the PR's URL, base, head, and actual status. Attach it to the task when the host supports or requires that. Report the link and evidence limits; start no ongoing monitor or merge action without its own authorization.

If PR delivery cannot complete, retain the reviewed local artifact and name the exact missing prerequisite. Do not claim that publication or CI succeeded from a local check.
