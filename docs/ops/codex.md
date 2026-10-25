# Codex usage

See the [README](../../README.md#codex-cli) for installation.

## Invoke a skill

Start with `$aasystem:aapilot`, or select a focused skill such as `$aasystem:product` or `$aasystem:how`. Direct skill installations omit the plugin prefix. Keep the complete [export tree](../design/skill-system.md#export-boundary), including references, adapters and license notices.

Aapilot may work directly or delegate through actual host tools. Required independent implementation verification still needs a fresh noneditor, except for the [narrow presentation exception](../../skills/aapilot/references/execution.md#owner-presentation-eligibility). Missing tool/access prerequisites remain explicit gaps.

## Local work and verification

Use the current checkout or one task worktree and follow the [verification contract](../../skills/aapilot/references/verification-contract.md). The optional read-only [identity helper](../../skills/aapilot/scripts/input_identity.py) needs Python 3.10+ and Git; reuse adequate project facilities instead when available.

Project verifier commands must remain usable without the plugin.

Ordinary invocation does not provide tool interception, a process sandbox, host-enforced approval, scheduling or recovery after chat closure. Actual discovery and supporting-skill composition need host observation; files on disk alone do not establish them. Read [How Aapilot works](../design/verification-contract.md) for the operating model.

## Durable orchestration hooks

The optional [local Codex adapter](../../skills/aapilot/assets/codex/README.md) adds
context restoration and recorded completion checks to `$aasystem:aapilot <outcome>`.
It requires separate configuration and trust; installing skills does not activate it.

Start with the guide's [setup](../../skills/aapilot/assets/codex/README.md#one-time-setup),
then follow its [coordinator protocol](../../skills/aapilot/assets/codex/README.md#coordinator-protocol)
and [handoff/resume steps](../../skills/aapilot/assets/codex/README.md#handoff-and-resume).
Checked handoff preserves intent/proof in an existing task file before retiring
owned scratch. Active state and pending review proof remain until safe retirement;
there is no background or session-close collector.

Hooks check recorded obligations, not semantic fulfillment, reviewer independence
or authenticated approval. Verify actual callbacks in your host and read the
[failure limits](../../skills/aapilot/assets/codex/README.md#stop-behavior-and-limits).
Hosted orchestration and other harnesses may lack these callbacks; use the
[portable continuity procedure](../../skills/aapilot/references/task-continuity.md)
and disclose instruction-driven operation there.

## Invocation policy

Every portable skill includes `agents/openai.yaml` with:

```yaml
policy:
  allow_implicit_invocation: false
```

Select skills explicitly. Preserve each adapter's policy and dependency settings with its frontmatter; generated project verifiers retain their own invocation policy. See the [official invocation policy](https://learn.chatgpt.com/docs/build-skills#optional-metadata) and [system map](../design/skill-system.md).
