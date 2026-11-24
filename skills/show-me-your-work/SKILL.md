---
name: show-me-your-work
description: Keep a decision log with evidence links and get it audited before delivery. Use when someone will review the reasoning later, such as on long, staged or unattended work.
disable-model-invocation: true
---

# Show me your work

Before starting, read the [execution contract](../pilot/references/execution.md) and the [approved-principle index](../principles/INDEX.md), unless already in context.

1. **Pick one log.** If the task already keeps an audit log, use it. Otherwise use a `decisions.tsv` in the task's working folder, and commit it only if the delivery needs the trail. Only you write to it; workers send you their evidence.
2. **Inherit with a `start` row.** A new chat or a new owner is a new run. Before you add to a log that has rows, read its tail and append a `start` row naming this run and the time range you inherit. Never claim earlier rows as your own. If you rely on one, check it again and log what you saw. If it was wrong, say so in your reply.
3. **Log turns, not steps.** If two rows say the same thing, you're logging steps. Add a row as soon as you pick between options, you rule a guess in or out (say why), the plan changes, a check passes or fails, or you're blocked.

   ```sh
   python3 scripts/log.py /absolute/task/decisions.tsv phase "Decision" "Why" "Evidence" "Result"
   ```

   Resolve `scripts/log.py` relative to this skill.
   - Evidence is a repo path, an existing commit or a command someone else can rerun. Not /tmp, not agent IDs.
   - Result says what you saw. Write `inferred` for what you didn't see and `open` for what's unfinished.
   - Never write secrets.
4. **Fix by adding.** If a row is wrong, append a row that names the wrong row's timestamp, what's true and why. Leave the original. If a row holds a secret, replace only the secret with `<REDACTED>` without typing it out, even in a command, append a row saying so, and tell the user to rotate it.
5. **Audit before delivery.** Check the rows against the transcript, git history and the real files. Every pointer should open, every result should match, and every pivot or revert should have a row. Read only this task's records. If you have no transcript, audit the artifacts and say so.
6. **Get an independent review.** Have an agent that didn't do the work, preferably another model family, check the log and run evidence for unsupported claims, skipped checks, risky choices and gaps, each pointing at a row or file. Check each finding yourself. If you can't start one, or it's the same model, say so.

In under 200 words, reply with the absolute log path, the reviewer and its model family, findings riskiest first, and what the audit couldn't see. If the review found nothing, say what it covered.
