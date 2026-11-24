# Opening a PR

Opening a PR doesn't mean you may watch CI, merge or deploy. Each needs its own ask.

1. **Read the ground rules.** Read the project's instructions, contributing guide and PR template. Check the branch, its base, the changed and untracked files, and whether this task already has a PR. If it does, update that PR instead of opening another. Leave work that isn't part of this change alone.
2. **Review the whole diff.** Remove debug output, scratch files, failed experiments and prose nobody needs. If the change touches a public interface, stored data or permissions, someone disputed the approach, or you can't say how a bad merge would be caught or undone, invoke the [`interrogate`](../../interrogate/SKILL.md) skill. Fix the findings that hold up. If nobody independent has checked the final diff, your cleanup included, go back to the [working loop](../references/verification-contract.md#working-loop) for a fresh recheck.
3. **Tidy the commits.** Follow the project's commit convention. For a bug fix, commit the failing test before the fix, so the history shows it red then green. Reword or squash only commits nobody else has; never force-push shared work.
4. **Write the brief.** Fill the project's PR template. If there isn't one, cover why, what changed, what you verified and what you couldn't. Add Interrogate's merge-risk call if you ran it. Link long evidence instead of pasting it. If review isn't finished, or the project asks for drafts, open it as a draft.
5. **Push and open it.** Push the branch and open the PR with the host's PR tool or the project's forge CLI. Read it back: URL, base, head and draft state. If the host can link the PR to the task, link it. Report the link.

If you can't open the PR, keep the reviewed branch, give the brief in your reply and name exactly what's missing, such as "no GitHub remote". Never claim a PR exists, or that CI passed, from a local check.
