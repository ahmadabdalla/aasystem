# Codex usage

See the [README](../../README.md#install-the-plugin) for installation.

## Invoke a skill

Start with `$aasystem:pilot`, or select a flagship skill such as `$aasystem:product` or `$aasystem:grill-me`. Direct skill installations omit the plugin prefix. Keep the complete [export tree](../design/skill-system.md#export-boundary), including references, adapters and license notices.

Start [System in Motion](../../skills/system-in-motion/SKILL.md) with the direct invocation `$aasystem:system-in-motion`.

Upgrading from `aapilot` requires new commands and helper paths; follow the
[rename migration](releasing.md#upgrade-from-aapilot-to-pilot), including existing
hook configuration and state handling.

Pilot may work directly or delegate through actual host tools. Required independent implementation verification still needs a fresh noneditor, except for the [narrow presentation exception](../../skills/pilot/references/verification-contract.md#owner-presentation-eligibility). Missing tool/access prerequisites remain explicit gaps.

## Local work and verification

Use the current checkout or one task worktree and follow the [verification contract](../../skills/pilot/references/verification-contract.md). The optional read-only [identity helper](../../skills/pilot/scripts/input_identity.py) needs Python 3.10+ and Git; reuse adequate project facilities instead when available.

Project verifier commands must remain usable without the plugin.

Ordinary invocation does not provide tool interception, a process sandbox, host-enforced approval, scheduling or recovery after chat closure. Actual discovery and supporting-skill composition need host observation; files on disk alone do not establish them. Read [How Pilot works](../design/verification-contract.md) for the operating model.

## Durable orchestration hooks

The optional [local Codex adapter](../../skills/pilot/assets/codex/README.md) keeps a
`$aasystem:pilot` task's record across sessions and blocks a stop until its checks pass.
Installing the skills doesn't enable it. Follow its
[setup](../../skills/pilot/assets/codex/README.md#one-time-setup),
[coordinator protocol](../../skills/pilot/assets/codex/README.md#coordinator-protocol),
[handoff and resume](../../skills/pilot/assets/codex/README.md#handoff-and-resume) and
[limits](../../skills/pilot/assets/codex/README.md#stop-behavior-and-limits).

If your host doesn't deliver these hooks, use the
[portable continuity procedure](../../skills/pilot/references/task-continuity.md)
and say the task runs on instructions alone.

## Invocation policy

Each portable skill ships `agents/openai.yaml` with a policy that matches its [tier](../design/skill-system.md#skill-inventory):

- **Flagship and Agent skills** set `allow_implicit_invocation: true`, so Codex can run them when another skill calls them.
- **User and Reference skills** set `allow_implicit_invocation: false`, so Codex runs them only when you name them.

Codex has no setting that hides a skill from users, so you can still name an Agent skill with `$aasystem:<skill>`. Preserve each adapter's policy and dependency settings with its frontmatter; generated project verifiers retain their own invocation policy. See the [official invocation policy](https://learn.chatgpt.com/docs/build-skills#optional-metadata) and the [authoring playbook](../../skills/pilot/playbooks/authoring-a-skill.md).
