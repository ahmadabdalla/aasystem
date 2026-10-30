# Ahmad's Pilot System

Skills and playbooks for AI coding agents to explore ideas, understand a product, build changes, and check that they work. Use them in Codex CLI, Claude Code, or GitHub Copilot CLI.

Start with [Pilot](skills/pilot/SKILL.md): describe what you want, and it chooses the playbook and skills for the work. Each skill contains instructions for a particular job, such as product discovery, design, or implementation.

## Why I created this

People share skills, prompts, and workflows, often alongside the efficiencies they get from using them. What stood out to me is that these systems encode a person's experience: their thought process, judgments, and decisions. What feels natural to the author can be difficult for someone else to follow. Copying the system doesn't automatically transfer that experience or produce the same efficiencies.

Sharing gives others a way to study those behaviors and practices, understand why someone works that way, and use what fits to build their own system. Whether they publish that system or keep it private is their choice. I've benefited from that openness, including [Lauren Tan's pstack](https://github.com/cursor/plugins/tree/main/pstack) and [Matt Pocock's skills](https://github.com/mattpocock/skills), whose work helped shape this library.

I find it hard to articulate ideas to AI, especially around user experience and product design. I like the agent to replay what it understood so we can reach a shared understanding. A diagram, visual design, prototype, or working product gives me something to inspect and makes vague requirements and hidden assumptions easier to spot.

Once we've agreed on what to make, I want the agent to design it, build it, and verify it. That shared understanding lets me delegate the work. Trust comes from verification: I want to see the result, what was checked, and what still needs attention.

I'm sharing this so others can understand how I work and adapt what fits, as I've learned from others. I judge the system by what it helps me deliver: products customers love and pay for, work that supports a business, or something I enjoy building.

## How I use it

I start with what I want to work out or change. Sometimes that's an idea I haven't settled on. Sometimes it's an existing product I need to understand, or a change that's ready to build.

```text
                  Your idea or request
                           |
                        Pilot
                           |
    Explore -> Understand -> Design -> Build -> Verify
                  ^                              |
                  +---- Findings / corrections --+
```

For example, adding search to a notes app still leaves decisions about what should match and how filters should work. I want to agree on that behavior before building it. A visual or prototype can help me see what I'm asking for. Verification then tries actual searches, including empty results and searches with filters applied.

Tell the agent what you want, what must stay unchanged, and where to stop. Here are a few ways to start:

**Explore an idea**

> I want to help small teams track unfinished work. Compare possible approaches and identify what we need to learn before choosing one. Stop at a recommendation.

**Understand a product**

> Find out how people create, share, and find notes today. Propose how search should work, with examples of expected results. Mark which requirements still need my agreement.

**Deliver a change**

> Add search to the notes list. Follow the existing design, preserve current filters, and verify the result. Open a PR for review.

You can stop at research or design, ask for local changes, or ask for a PR. Use a [focused skill](#choose-a-focused-skill) directly when you want help with one job.

For substantial work, Pilot keeps one [task brief](skills/pilot/references/task-continuity.md),
selects the needed specialists, restores context after handoffs or compaction, and
checks the whole request before finishing. Describe the outcome; you need not repeat
the orchestration instructions.

Optional [local Codex hooks](docs/ops/codex.md#durable-orchestration-hooks) add
context restoration and recorded completion checks after separate setup/trust.
Checked handoff retires disposable adapter state while preserving the task record
and proof. Ordinary invocation remains instruction-driven.

## Contracts define the working rules

This is where my thinking about trust and verification started to develop, helped by people in the community sharing their experiences. Building trust in what agents do is hard, especially when several agents work together. I wanted to explore whether a shared contract could make their communication with each other, and with me, more reliable.

Language models can respond differently to the same request. My thinking is that an agent harness, the software running the agent, can use deterministic code to check what the model proposes and control when work proceeds. This library uses shared contracts, project checks and input-identity comparisons to support verification. These do not intercept tool calls or guarantee that an agent followed the instructions.

The [execution contract](skills/pilot/references/execution.md) sets out what we agreed to build, what each agent can change, and how the work will be checked. Pilot can follow a skill's instructions itself or assign work to another agent. It stays responsible for bringing the results together and checking them against the request.

If the work uncovers a decision that needs my input, I want the agent to show me the options and wait for my answer. When I need to review a visual design, I want a preview I can inspect before it continues. Getting agents to do this consistently is challenging, and I'm trying different ideas to make it more reliable.

## How I check the work

Implementation starts with [readiness to deliver and prove](skills/principle-deliver-and-prove/SKILL.md), a personal principle applied through Implement's opening procedure.

The agent making a change runs checks while it works. For a feature or bug fix, the [verification contract](skills/pilot/references/verification-contract.md) requires a separate agent to review the changes and run the affected project checks. There is a [limited exception for appearance edits](skills/pilot/references/execution.md#owner-presentation-eligibility).

When the agent says it's finished, I want to be able to inspect:

- What it made or changed
- What was checked and what happened
- What failed, wasn't checked, or still needs my attention

For the search example, a passing build wouldn't tell me whether search finds the right notes or preserves the filters. I want checks that exercise the behavior we agreed on. If those checks fail or haven't run, the work is still incomplete.

For research or design, I want the sources, reasoning, and unresolved questions. The agent should use the project's existing task or PR format so I can review the result where the work already lives.

These contracts are instructions for the agents. Project checks help verify the result, but the library doesn't intercept tool calls or guarantee that an agent followed the instructions. [How Pilot works](docs/design/verification-contract.md) explains the workflow, verification mechanics, and limitations.

## Install the plugin

Install `aasystem` from the [ahmadabdalla/plugins](https://github.com/ahmadabdalla/plugins) marketplace in Codex CLI, Claude Code, or GitHub Copilot CLI.

Add the marketplace once in each coding tool. If you already added it, [refresh it](https://github.com/ahmadabdalla/plugins#marketplace-commands) before installing aasystem.

### Codex CLI

```bash
codex plugin marketplace add ahmadabdalla/plugins
codex plugin add aasystem@ahmadabdalla-plugins
```

Use `$aasystem:pilot` to coordinate a task, or `$aasystem:product` for product discovery.

Existing `aapilot` users should follow the [Pilot migration steps](docs/ops/releasing.md#upgrade-from-aapilot-to-pilot)
for saved commands, direct installs and optional hooks.

### Claude Code

```bash
claude plugin marketplace add ahmadabdalla/plugins
claude plugin install aasystem@ahmadabdalla-plugins
```

Use `/aasystem:pilot` to coordinate a task, or `/aasystem:product` for product discovery.

### GitHub Copilot CLI

```bash
copilot plugin marketplace add ahmadabdalla/plugins
copilot plugin install aasystem@ahmadabdalla-plugins
```

Run `/skills` in Copilot to check that aasystem's skills are available.

Marketplace installations use published releases. The `main` branch may include unreleased changes; see [release notes](https://github.com/ahmadabdalla/aasystem/releases) for what has shipped. See the [upgrade guide](docs/ops/releasing.md#upgrade-an-installed-plugin) for existing installations.

## Start here

After installation, start Pilot in your agent:

| Host               | Entry point                                |
| ------------------ | ------------------------------------------ |
| Codex CLI          | `$aasystem:pilot`                        |
| Claude Code        | `/aasystem:pilot`                        |
| GitHub Copilot CLI | Run `/skills` to find the installed skills |

Describe the work in your own words, using the [examples above](#how-i-use-it) as a starting point.

## Choose a focused skill

If you already know which part of the work needs attention, you can ask for that skill directly:

| Need                                                      | Entry point                                                                      |
| --------------------------------------------------------- | -------------------------------------------------------------------------------- |
| Work through a plan by answering questions                | [`grill-me`](skills/grill-me/SKILL.md)                                           |
| Compare ways to solve a problem                           | [`solution`](skills/solution/SKILL.md)                                           |
| Assess a design under plausible growth                    | [`10x`](skills/10x/SKILL.md)                                                     |
| Run a check to find out whether an assumption holds       | [`probe`](skills/probe/SKILL.md)                                                 |
| Build a throwaway experiment                              | [`prototype`](skills/prototype/SKILL.md)                                         |
| Find out how something works today                        | [`how`](skills/how/SKILL.md)                                                     |
| Find out why an earlier decision was made                 | [`why`](skills/why/SKILL.md)                                                     |
| Define who a product serves and how it should work        | [`product`](skills/product/SKILL.md)                                             |
| Clarify terms or record a decision                        | [`domain-modeling`](skills/domain-modeling/SKILL.md)                             |
| Design navigation, screens, and interactions              | [`interaction-design`](skills/interaction-design/SKILL.md)                       |
| Independently assess an existing rendered interface       | [`interaction-design`](skills/interaction-design/SKILL.md#select-the-assignment) |
| Improve a working interface through visual review         | [`ui-refinement`](skills/ui-refinement/SKILL.md)                                 |
| Plan how code, interfaces, and data fit together          | [`architect`](skills/architect/SKILL.md)                                         |
| Make assigned edits from an agreed plan                   | [`implement`](skills/implement/SKILL.md)                                         |
| Find weaknesses in a plan, design, or implementation      | [`interrogate`](skills/interrogate/SKILL.md)                                     |
| Review how hard code is to read and change                | [`maintainability`](skills/maintainability/SKILL.md)                             |
| Review module design with behavior and change traces     | [`maintainability`](skills/maintainability/SKILL.md#select-the-assessment)       |
| Create instructions and checks for verifying your project | [`bootstrap-verification`](skills/bootstrap-verification/SKILL.md)               |
| Check and update your project's verification instructions | [`maintain-verification`](skills/maintain-verification/SKILL.md)                 |

Browse [`skills/`](skills/) for all available skills.

For example, ask Pilot to "grill me about this plan." It asks questions together, then uses your answers to choose the next round. The [Grill Me guide](skills/grill-me/references/grilling.md) explains how it records agreed terms and decisions.

You can also ask it to assess an existing interface. For a records page, that might include long names, finding older records, and narrow layouts. The [rendered UX assessment](skills/interaction-design/references/rendered-ux-assessment.md) uses two separate agents to check visual composition and interactions, then brings their findings together.

## Explore the system

Read more about how the system works:

- [How Pilot works](docs/design/verification-contract.md): who does the work, how decisions are made, and what must be checked
- [System graph](visualizations/skill-library/index.html): see which skills call each other
- [System structure and sources](docs/design/skill-system.md): skill responsibilities, origins, and local changes
- [Codex usage](docs/ops/codex.md): how to start skills in Codex and configure them
- [Version history](CHANGELOG.md): releases and changes to skill names and commands

## Change the library

A change to one skill can affect the skills that call it. Start with the [maintenance rules](AGENTS.md) and follow the [skill authoring playbook](skills/pilot/playbooks/authoring-a-skill.md) to check those relationships. The [evaluation playbook](skills/pilot/playbooks/eval.md) describes how to try instruction changes on realistic tasks and inspect the results.

For development, follow the [maintainer setup](docs/ops/releasing.md#maintainer-setup) to install Python dependencies and run the package checks.

## Export the library

Skills call other skills and load shared references, so keep the [export contents](docs/design/skill-system.md#export-boundary) together. Include both plugin manifests, all skills, and the license notices.

Coding tools differ in how they discover and call skills. See the [release guide](docs/ops/releasing.md) for package checks, publication, and upgrades.

## License and attribution

Original contributions are licensed under the [MIT License](LICENSE), copyright Ahmad Abdalla.

This system is inspired by and adapts [pstack](https://github.com/cursor/plugins/tree/main/pstack) by Lauren Tan and [Matt Pocock's skills](https://github.com/mattpocock/skills). Their original MIT notices are preserved in [PSTACK_LICENSE.txt](PSTACK_LICENSE.txt) and [MATT_POCOCK_LICENSE.txt](MATT_POCOCK_LICENSE.txt).

The [source and adaptation inventory](docs/design/skill-system.md#skill-inventory) identifies the upstream sources and local changes for each skill.
