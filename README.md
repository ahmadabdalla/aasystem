# Ahmad Abdalla's Pilot System

A portable skill library for AI coding agents to plan, build, review, and verify engineering work. Use Aapilot for a complete task or a specialist for focused work.

Inspired by [pstack](https://github.com/cursor/plugins/tree/main/pstack) by Lauren Tan and [Matt Pocock's skills](https://github.com/mattpocock/skills).

## Install the plugin

Install `aasystem` from the [ahmadabdalla/plugins](https://github.com/ahmadabdalla/plugins) marketplace in Codex CLI, Claude Code, or GitHub Copilot CLI.

Add the marketplace once in each host. If already configured, [refresh it](https://github.com/ahmadabdalla/plugins#marketplace-commands) before installing aasystem.

### Codex CLI

```bash
codex plugin marketplace add ahmadabdalla/plugins
codex plugin add aasystem@ahmadabdalla-plugins
```

Invoke `$aasystem:aapilot` for an end-to-end task, or `$aasystem:product` for product discovery.

### Claude Code

```bash
claude plugin marketplace add ahmadabdalla/plugins
claude plugin install aasystem@ahmadabdalla-plugins
```

Invoke `/aasystem:aapilot` for an end-to-end task, or `/aasystem:product` for product discovery.

### GitHub Copilot CLI

```bash
copilot plugin marketplace add ahmadabdalla/plugins
copilot plugin install aasystem@ahmadabdalla-plugins
```

Run `/skills` in Copilot to check that aasystem's skills are available.

## Start here

Invoke [`aapilot`](skills/aapilot/SKILL.md) using your host's syntax above. Describe the outcome you want and any constraints:

> Add search to the notes list. Follow the existing design, preserve current filters, and verify the result. Open a PR for review.

Aapilot selects the appropriate playbook and specialists and coordinates checks within your requested scope. It pauses for unresolved consequential choices and required visual review. Verification scales with the change. [How Aapilot works](docs/design/verification-contract.md) explains the process and its limits.

## Choose a focused skill

Use a specialist directly when you already know the work you need:

| Need | Entry point |
| --- | --- |
| Define product behavior | [`product`](skills/product/SKILL.md) |
| Choose an overall approach | [`solution`](skills/solution/SKILL.md) |
| Design implementation boundaries | [`architect`](skills/architect/SKILL.md) |
| Make bounded edits against a settled design or contract | [`implement`](skills/implement/SKILL.md) |
| Design interactions | [`interaction-design`](skills/interaction-design/SKILL.md) |
| Refine a rendered experience | [`ui-refinement`](skills/ui-refinement/SKILL.md) |
| Build a throwaway experiment | [`prototype`](skills/prototype/SKILL.md) |
| Trace current behavior | [`how`](skills/how/SKILL.md) |
| Reconstruct prior rationale | [`why`](skills/why/SKILL.md) |
| Test an assumption | [`probe`](skills/probe/SKILL.md) |
| Challenge existing work | [`interrogate`](skills/interrogate/SKILL.md) |
| Assess readability and ease of change | [`maintainability`](skills/maintainability/SKILL.md) |
| Explore choices through an interview | [`grill-me`](skills/grill-me/SKILL.md) |
| Clarify terms or record a decision | [`domain-modeling`](skills/domain-modeling/SKILL.md) |

Architect is design-only. Implement makes bounded edits and returns the changed artifact with development-check evidence. See [How Aapilot works](docs/design/verification-contract.md) for delivery ownership and verification requirements.

Browse [`skills/`](skills/) for all available skills.

## Explore the system

- [System graph](visualizations/skill-library/index.html): explore routes and handoffs
- [System structure and sources](SKILL_SYSTEM.md): ownership, adaptations, and upstream references
- [Codex usage](CODEX.md): invocation settings and limits
- [Version history](CHANGELOG.md): releases and invocation migration

## Change the library

Start with the [maintenance rules](AGENTS.md) and follow the [skill authoring playbook](skills/aapilot/playbooks/authoring-a-skill.md). The [evaluation playbook](skills/aapilot/playbooks/eval.md) covers experiments for assessing instruction changes.

## Export the library

Keep the [export contents](SKILL_SYSTEM.md#export-boundary) together, including both plugin manifests, all skills, and the license notices.

Host-specific invocation support varies. See the [release guide](RELEASING.md) for validation, publication, and existing-user upgrades.

## License and attribution

Original contributions are licensed under the [MIT License](LICENSE), copyright Ahmad Abdalla. This system adapts upstream work from Lauren Tan's pstack and Matt Pocock's skills. Their original MIT notices are preserved in [PSTACK_LICENSE.txt](PSTACK_LICENSE.txt) and [MATT_POCOCK_LICENSE.txt](MATT_POCOCK_LICENSE.txt).

The [source and adaptation inventory](SKILL_SYSTEM.md#skill-inventory) identifies the upstream sources and local changes for each skill.
