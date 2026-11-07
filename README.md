# Ahmad's Pilot System

Skills and playbooks for AI coding agents to explore ideas, understand a product, build changes, and check that they work. Use them in Codex CLI, Claude Code, or GitHub Copilot CLI.

Use [Pilot](#pilot) to coordinate work from an idea through verification. Open [System in Motion](#system-in-motion) directly to see how one product journey unfolds.

[Install the plugin](#install-the-plugin) · [Choose a skill](#flagship-skills)

## Why I created this

People share skills, prompts, and workflows, often alongside the efficiencies they get from using them. What stood out to me is that these systems encode a person's experience: their thought process, judgments, and decisions. What feels natural to the author can be difficult for someone else to follow. Copying the system doesn't automatically transfer that experience or produce the same efficiencies.

Sharing gives others a way to study those behaviors and practices, understand why someone works that way, and use what fits to build their own system. Whether they publish that system or keep it private is their choice. I've benefited from that openness, including [Lauren Tan's pstack](https://github.com/cursor/plugins/tree/main/pstack) and [Matt Pocock's skills](https://github.com/mattpocock/skills), whose work helped shape this library.

I find it hard to articulate ideas to AI, especially around user experience and product design. I like the agent to replay what it understood so we can reach a shared understanding. A diagram, visual design, prototype, or working product gives me something to inspect and makes vague requirements and hidden assumptions easier to spot.

Once we've agreed on what to make, I want the agent to design it, build it, and verify it. That shared understanding lets me delegate the work. Trust comes from verification: I want to see the result, what was checked, and what still needs attention.

I'm sharing this so others can understand how I work and adapt what fits, as I've learned from others. I judge the system by what it helps me deliver: products customers love and pay for, work that supports a business, or something I enjoy building.

## Pilot

[Pilot](skills/pilot/SKILL.md) is where I start. I tell it what I want to work out or change. It chooses the skills for the job and checks the result.

### How I use it

Sometimes I have an idea I haven't settled on. Other times I need to understand an existing product or build a change.

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

I tell Pilot where to stop. Sometimes a recommendation or a sketch is enough. For bigger jobs, Pilot keeps a [task brief](skills/pilot/references/task-continuity.md) so I don't have to explain the same decisions after a handoff.

## System in Motion

[System in Motion](skills/system-in-motion/SKILL.md) follows one product journey in two synchronized views. **Experience** shows what a person sees and does. **Architecture** shows the work and technology behind each moment.

Say a customer submits a request and a worker saves the result in the background. The walkthrough shows when the request is accepted, when the result is saved, and when the customer can actually see it. Product, design, and engineering can inspect those moments together and trace them to the source. The result is a standalone offline HTML file in the target repository root by default. Editing files stay in temporary storage unless you request a permanent package.

Start this skill directly with `$aasystem:system-in-motion` in Codex or `/aasystem:system-in-motion` in Claude Code. Give it one journey to explain, such as “Show how a request moves from submission to a result the customer can see.” A project subdirectory scopes the source inspection. Specify an output path if you want the HTML somewhere else.

## Contracts define the working rules

This is where my thinking about trust and verification started to develop, helped by people in the community sharing their experiences. Building trust in what agents do is hard, especially when several agents work together. I wanted to explore whether a shared contract could make their communication with each other, and with me, more reliable.

Language models can respond differently to the same request. My thinking is that an agent harness, the software running the agent, can use deterministic code to check what the model proposes and control when work proceeds. This library uses shared contracts, project checks and input-identity comparisons to support verification. These do not intercept tool calls or guarantee that an agent followed the instructions.

## How I check the work

If the agent needs a decision from me, I want to see the options and answer before it keeps going. For a visual design, I want a preview I can react to. When it builds a feature or fixes a bug, I want a second agent to review the work and run the project checks. [How Pilot works](docs/design/verification-contract.md)

When the agent says it's finished, I look for three things.

- What it made or changed
- What was checked and what happened
- What failed, wasn't checked, or still needs my attention

For the notes app, I want to see what happens when I search for a known note, apply a filter, or get no results. A passing build leaves those questions open. If I asked for research or design, I look for the sources, the reasoning, and the decisions still open.

## Install the plugin

Add the marketplace once, then install `aasystem`. This example uses Codex CLI.

```bash
codex plugin marketplace add ahmadabdalla/plugins
codex plugin add aasystem@ahmadabdalla-plugins
```

For Claude Code or GitHub Copilot CLI, replace `codex` with `claude` or `copilot` and use `plugin install` in place of `plugin add` on the second line.

Start Pilot with `$aasystem:pilot` in Codex or `/aasystem:pilot` in Claude Code. In Copilot CLI, find Pilot under `/skills`.

Marketplace installs use published releases. If you already added the marketplace, refresh it before installing. [Marketplace commands](https://github.com/ahmadabdalla/plugins#marketplace-commands) · [Upgrade guide](docs/ops/releasing.md#upgrade-an-installed-plugin) · [Migration from aapilot](docs/ops/releasing.md#upgrade-from-aapilot-to-pilot)

## Flagship skills

| I want to… | Skill |
| --- | --- |
| Work through an idea or a change and check the result | [Pilot](#pilot) |
| Watch what a customer sees and what happens behind the scenes | [System in Motion](#system-in-motion) |
| Work out who the product is for and what it should do | [Product](skills/product/SKILL.md) |
| Design how people use an interface and refine it with feedback | UX · [Interaction Design](skills/interaction-design/SKILL.md) and [UI Refinement](skills/ui-refinement/SKILL.md) |
| Decide how code, interfaces, and data should fit together | [Architect](skills/architect/SKILL.md) |

Browse the [full skill catalog](docs/design/skill-system.md#skill-inventory).

## Project guides

- See how the skills fit together in the [system graph](visualizations/skill-library/index.html).
- Set up optional hooks and find Codex-specific commands in the [Codex guide](docs/ops/codex.md).
- Start with the [maintenance rules](AGENTS.md) if you're changing the library. The [release guide](docs/ops/releasing.md) covers checks and publication, and the [export inventory](docs/design/skill-system.md#export-boundary) lists what to copy.
- See what's changed in the [changelog](CHANGELOG.md).

## License and attribution

Original contributions are licensed under the [MIT License](LICENSE), copyright Ahmad Abdalla.

The library draws on Lauren Tan's [pstack](https://github.com/cursor/plugins/tree/main/pstack) ([MIT notice](PSTACK_LICENSE.txt)) and [Matt Pocock's skills](https://github.com/mattpocock/skills) ([MIT notice](MATT_POCOCK_LICENSE.txt)), and adapts [Warp's common-skills](https://github.com/warpdotdev/common-skills) ([MIT notice](WARP_LICENSE.txt)) for Interrogate's merge-risk guidance.

The [source and adaptation inventory](docs/design/skill-system.md#skill-inventory) identifies the upstream sources and local changes for each skill.
