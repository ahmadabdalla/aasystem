# Ahmad Abdalla's Pilot System

A portable skill system for planning, building, reviewing, and verifying engineering work.

Inspired by [pstack](https://github.com/cursor/plugins/tree/main/pstack) by Lauren Tan and [Matt Pocock's skills](https://github.com/mattpocock/skills).

## Install the plugin

Install `aasystem` from the [ahmadabdalla/plugins](https://github.com/ahmadabdalla/plugins) marketplace in Codex CLI, Claude Code, or GitHub Copilot CLI.

Add the marketplace once in each host you use, then install aasystem. If you already added it for Azure Cost Calculator, [refresh the marketplace](https://github.com/ahmadabdalla/plugins#marketplace-commands) and install aasystem.

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

You can always start with [`aapilot`](skills/aapilot/SKILL.md) to drive your work. Give it the task; it selects the appropriate playbook or specialist and coordinates the work through completion within your requested scope. Use your host's plugin invocation above.

- Open [Ahmad Abdalla's Pilot System Graph](visualizations/skill-library/index.html) to inspect routes and handoffs
- Read [`SKILL_SYSTEM.md`](SKILL_SYSTEM.md) for ownership, sources, and adaptations

## Use a flagship skill directly

For a focused task, you can invoke a flagship skill directly:

| Need | Entry point |
| --- | --- |
| Define product behavior | [`product`](skills/product/SKILL.md) |
| Choose an overall approach | [`solution`](skills/solution/SKILL.md) |
| Design implementation boundaries | [`architect`](skills/architect/SKILL.md) |
| Design interactions | [`interaction-design`](skills/interaction-design/SKILL.md) |
| Refine a rendered experience | [`ui-refinement`](skills/ui-refinement/SKILL.md) |
| Build a throwaway experiment | [`prototype`](skills/prototype/SKILL.md) |
| Trace current behavior | [`how`](skills/how/SKILL.md) |
| Reconstruct prior rationale | [`why`](skills/why/SKILL.md) |
| Test an assumption | [`probe`](skills/probe/SKILL.md) |
| Challenge existing work | [`interrogate`](skills/interrogate/SKILL.md) |
| Explore activities or resolve choices through an interview | [`grill-me`](skills/grill-me/SKILL.md) |
| Clarify terminology or record a consequential decision | [`domain-modeling`](skills/domain-modeling/SKILL.md) |

All skills remain available from [`skills/`](skills/).

For bounded edits against a settled design or contract, use [`implement`](skills/implement/SKILL.md). It returns the changed artifact and development-check evidence to its caller. Architect remains design-only; the coordinating playbook assigns a separate verification agent to run the project’s checks and owns acceptance.

For a bounded code or design assessment, use [`maintainability`](skills/maintainability/SKILL.md). It examines reader effort, local change cost, and ease of verification, then returns findings to the caller; it does not select a top-level task route or own implementation.

For the experimental bounded-autonomy capability, see [Bounded work](skills/aapilot/references/bounded-work.md). Request it explicitly with your existing entry skill; its shared receipt helper supports native delegation, current proof, repair and human checkpoints. The [PoC plan](docs/plans/issue-17-feature-flags-poc.md) separates local capability proof from later website testing.

## Repository map

| Path | Contents |
| --- | --- |
| [`skills/`](skills/) | Portable skills, references, assets, and orchestrator playbooks |
| [Evaluation playbook](skills/aapilot/playbooks/eval.md) | Temporary experiments for assessing instruction changes |
| [Bounded-autonomy PoC plan](docs/plans/issue-17-feature-flags-poc.md) | Implement and prove the reusable capability here; later exercise website delivery paths |
| [`visualizations/skill-library/`](visualizations/skill-library/) | Interactive system graph |
| [`AGENTS.md`](AGENTS.md) | Repository maintenance rules |
| [`SKILL_SYSTEM.md`](SKILL_SYSTEM.md) | Architecture, ownership, sources, and adaptations |
| [`CODEX.md`](CODEX.md) | Codex invocation settings |
| [`RELEASING.md`](RELEASING.md) | Release validation, publication and marketplace handoff |
| [`CHANGELOG.md`](CHANGELOG.md) | Version history and invocation migration |
| [`plugin.json`](plugin.json) | Portable plugin identity and OpenAI presentation metadata |
| [`.claude-plugin/plugin.json`](.claude-plugin/plugin.json) | Claude compatibility manifest |

## Change the library

1. Read [`AGENTS.md`](AGENTS.md)
2. Follow the [skill authoring playbook](skills/aapilot/playbooks/authoring-a-skill.md)
3. Edit the owning file
4. Update the system map when relationships change
5. Update the graph when routes or handoffs change
6. Run the owning validation checks

## Export the library

Keep the [export contents](SKILL_SYSTEM.md#export-boundary) together, including both plugin manifests, all skills, and the license notices.

Host-specific invocation support varies.

For versioned releases and existing-user upgrades, see [RELEASING.md](RELEASING.md).

See [`CODEX.md`](CODEX.md) for the included Codex adapter.

## License and attribution

Original contributions are licensed under the [MIT License](LICENSE), copyright Ahmad Abdalla. This system adapts upstream work from Lauren Tan's pstack and Matt Pocock's skills. Their original MIT notices are preserved in [PSTACK_LICENSE.txt](PSTACK_LICENSE.txt) and [MATT_POCOCK_LICENSE.txt](MATT_POCOCK_LICENSE.txt).

The [source and adaptation inventory](SKILL_SYSTEM.md#skill-inventory) identifies the upstream sources and local changes for each skill.
