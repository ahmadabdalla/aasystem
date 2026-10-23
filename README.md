# Ahmad's Pilot System

Skills and playbooks for AI coding agents to explore ideas, understand a product, build changes, and check that they work. Use them in Codex CLI, Claude Code, or GitHub Copilot CLI.

Each skill contains instructions for a particular job. Aapilot may apply those instructions in its own context or assign bounded work to another agent; required independent verification remains separate. [Aapilot](skills/aapilot/SKILL.md) is the starting skill: describe what you want, and it chooses the steps and supporting skills. There are playbooks for bug fixes, features, and other engineering tasks.

## Why I created this

People share skills, prompts, and workflows, often alongside the efficiencies they get from using them. What stood out to me is that these systems encode a person's experience: their thought process, judgments, and decisions. What feels natural to the author can be difficult for someone else to follow. Copying the system doesn't automatically transfer that experience or produce the same efficiencies.

Sharing gives others a way to study those behaviors and practices, understand why someone works that way, and use what fits to build their own system. Whether they publish that system or keep it private is their choice. I've benefited from that openness, including [Lauren Tan's pstack](https://github.com/cursor/plugins/tree/main/pstack) and [Matt Pocock's skills](https://github.com/mattpocock/skills), whose work helped shape this library.

I find it hard to articulate ideas to AI, especially around user experience and product design. I like the agent to replay what it understood so we can reach a shared understanding. A diagram, visual design, prototype, or working product gives me something to inspect and makes vague requirements and hidden assumptions easier to spot.

Once we've agreed on what to make, I want the agent to design it, build it, and verify it. That shared understanding lets me delegate the work. Trust comes from verification: I want to see the result, what was checked, and what still needs attention.

I'm sharing this so others can learn from my practices and adapt them, as I've learned from others. I judge the system by what it helps me deliver: products customers love and pay for, work that supports a business, or something I enjoy building.

## From idea to verified delivery

The starting point determines what the agent needs to do. An open idea needs exploration, an existing product may need investigation, and an agreed change can move into design and delivery.

```text
              What to change and what to preserve
                              |
                           Aapilot
                              |
       Ideation <-> Discovery -> Delivery -> Verification
          ^             ^                        |
          |             +------------------------+
          +--------------------------------------+
```

> For example, in a notes app:
>
> Ideation might compare adding search with improving navigation. Choosing search still leaves decisions about what should match and how filters should work. Discovery makes those choices explicit, and a visual or prototype can show the proposed experience before implementation. Once the behavior is agreed and built, verification tries actual searches, including empty results and searches with filters applied.

You can stop at research or design. A recommendation should explain its sources and tradeoffs; a design should explain how the proposed parts fit together and how to check them.

## Start here

[Install the plugin](#install-the-plugin), then start `aapilot` in your agent:

| Host | Entry point |
| --- | --- |
| Codex CLI | `$aasystem:aapilot` |
| Claude Code | `/aasystem:aapilot` |
| GitHub Copilot CLI | Run `/skills` to find the installed skills |

The request tells the agent how much work you want to delegate. Say what you want, what must stay unchanged, and where to stop. For example:

**Explore an idea**

> I want to help small teams track unfinished work. Compare possible approaches and identify what we need to learn before choosing one. Stop at a recommendation.

**Understand a product**

> Find out how people create, share, and find notes today. Propose how search should work, with examples of expected results. Mark which requirements still need my agreement.

**Deliver a change**

> Add search to the notes list. Follow the existing design, preserve current filters, and verify the result. Open a PR for review.

Use a [focused skill](#choose-a-focused-skill) directly when you want help with one job.

Aapilot briefly inspects the ask and uses the [effort rubric](skills/aapilot/references/effort.md) to choose S, M or L execution conditions. Consequence is assessed separately: a small permission fix can still need strong security checks. The assessment travels with downstream work; size does not waive required verification or human decisions.

## Contracts define the working rules

This is where my thinking about trust and verification started to develop, helped by people in the community sharing their experiences. Building trust in what agents do is hard, especially when several agents work together. I wanted to explore whether a shared contract could make their communication with each other, and with me, more reliable.

Language models can respond differently to the same request. My thinking is that an agent harness, the software running the agent, can use deterministic code to check what the model proposes and control when work proceeds. This library uses shared contracts, project checks and input-identity comparisons to support verification. These do not intercept tool calls or guarantee that an agent followed the instructions.

The [execution contract](skills/aapilot/references/execution.md) defines what each assignment must include: what was agreed, what may change, who edits which files, and what needs to be checked. It also defines when the agent must stop for your answer. The lead agent checks the contributions against your request and owns acceptance requests; required independent proof comes from a separate verifier.

```text
You                       Lead agent                   Other agents
 |                             |                             |
 +-- Request and permissions ->|                             |
 |                             +-- Task, files, checks ----->|
 |                             |<-- Work and check results --+
 |<-- Decision to make --------+                             |
 +-- Your answer ------------->|                             |
 |                             |                             |
 |<-- Result and evidence -----+                             |
```

An assignment can uncover a decision that changes what you agreed to build. If that decision needs your input, the contract requires the lead agent to show the options and relevant work, ask, and wait. When visual review is required, it must give you a preview to inspect before continuing. Getting agents to do this consistently is challenging, and I'm trying different ideas to make it more reliable.

The agent making a change runs checks while it works. For a feature or bug fix, the [verification contract](skills/aapilot/references/verification-contract.md) also requires another agent to review the changes and run the affected project checks. This gives the result a separate assessment against the agreed requirements. There is a [limited exception for appearance edits](skills/aapilot/references/execution.md#owner-presentation-eligibility).

> For example, an exact label change that preserves meaning and behavior may qualify for checks by the same agent that made the edit. The full eligibility rules still apply.

## Evidence connects the request to the result

When the agent says a change is complete, I want to see the result, what was checked, and what still needs attention. Reuse the project's task, PR or evidence format to connect agreed expectations to the tested work and actual observations. Research and design provide their sources and reasoning.

```text
Your request -> Shared understanding -> Design / build / research
                         ^                       |
                         |              Independent assessment
                         |                       |
                         +---- Decisions / corrections
                                                 |
                                      Result for your review
```

For a feature or bug fix, a separate verifier reviews the combined change and runs the affected project checks. The owner reconciles findings and obtains current checks after corrections. Missing or failing required checks leave the work incomplete. The [limited presentation exception](skills/aapilot/references/execution.md#owner-presentation-eligibility) stays explicitly owner-checked.

Local work uses the current checkout or one task worktree when separation is useful. Implementer and verifier take turns, and input identity checks detect stale results without archiving the repository each round. Required configuration and external inputs still need deliberate inclusion. A worktree containing pending review changes is a deliverable, not disposable scratch.

Keep useful findings and evidence through review; clean up owned processes and disposable outputs. Retain bulky artifacts only for a specific need. The final report distinguishes observed success, failure and unverified scope. Read [How Aapilot works](docs/design/verification-contract.md) for the workflow and limitations.

## Install the plugin

Install `aasystem` from the [ahmadabdalla/plugins](https://github.com/ahmadabdalla/plugins) marketplace in Codex CLI, Claude Code, or GitHub Copilot CLI.

Add the marketplace once in each coding tool. If you already added it, [refresh it](https://github.com/ahmadabdalla/plugins#marketplace-commands) before installing aasystem.

### Codex CLI

```bash
codex plugin marketplace add ahmadabdalla/plugins
codex plugin add aasystem@ahmadabdalla-plugins
```

Use `$aasystem:aapilot` to coordinate a task, or `$aasystem:product` for product discovery.

### Claude Code

```bash
claude plugin marketplace add ahmadabdalla/plugins
claude plugin install aasystem@ahmadabdalla-plugins
```

Use `/aasystem:aapilot` to coordinate a task, or `/aasystem:product` for product discovery.

### GitHub Copilot CLI

```bash
copilot plugin marketplace add ahmadabdalla/plugins
copilot plugin install aasystem@ahmadabdalla-plugins
```

Run `/skills` in Copilot to check that aasystem's skills are available.

Marketplace installations use published releases. The `main` branch may include unreleased changes; see [release notes](https://github.com/ahmadabdalla/aasystem/releases) for what has shipped. See the [upgrade guide](docs/ops/releasing.md#upgrade-an-installed-plugin) for existing installations.

## Choose a focused skill

If you already know which part of the work needs attention, you can ask for that skill directly:

| Need | Entry point |
| --- | --- |
| Work through a plan in question rounds and record agreed terms and decisions | [`grill-me`](skills/grill-me/SKILL.md) |
| Compare ways to solve a problem | [`solution`](skills/solution/SKILL.md) |
| Assess a design under plausible growth | [`10x`](skills/10x/SKILL.md) |
| Run a check to find out whether an assumption holds | [`probe`](skills/probe/SKILL.md) |
| Build a throwaway experiment | [`prototype`](skills/prototype/SKILL.md) |
| Find out how something works today | [`how`](skills/how/SKILL.md) |
| Find out why an earlier decision was made | [`why`](skills/why/SKILL.md) |
| Define who a product serves and how it should work | [`product`](skills/product/SKILL.md) |
| Clarify terms or record a decision | [`domain-modeling`](skills/domain-modeling/SKILL.md) |
| Design navigation, screens, and interactions | [`interaction-design`](skills/interaction-design/SKILL.md) |
| Independently assess an existing rendered interface | [`interaction-design`](skills/interaction-design/SKILL.md#select-the-assignment) — two parallel domain assessors |
| Improve a working interface through visual review | [`ui-refinement`](skills/ui-refinement/SKILL.md) |
| Plan how code, interfaces, and data fit together | [`architect`](skills/architect/SKILL.md) |
| Make assigned edits from an agreed plan | [`implement`](skills/implement/SKILL.md) |
| Find weaknesses in a plan, design, or implementation | [`interrogate`](skills/interrogate/SKILL.md) |
| Review how hard code is to read and change | [`maintainability`](skills/maintainability/SKILL.md) |
| Create instructions and checks for verifying your project | [`bootstrap-verification`](skills/bootstrap-verification/SKILL.md) |
| Check and update your project's verification instructions | [`maintain-verification`](skills/maintain-verification/SKILL.md) |

Browse [`skills/`](skills/) for all available skills.

Ask aapilot to "grill me about this plan" or "grill me with docs about this plan." Both ask independent questions together and use your answers to choose the next round. Agreed terms and qualifying decisions are recorded when edits are authorized; read-only work returns proposed notes. Confirm shared understanding before implementation. Product discovery uses its own interview procedure.

For example, ask aapilot or Interaction Design to independently assess a rendered records page, including long names, finding older records and narrow layouts. The [rendered UX assessment](skills/interaction-design/references/rendered-ux-assessment.md) uses separate visual-composition and interaction/continuity assessors, each with its own instructions and rubric. It returns reconciled findings, exercised coverage and gaps to the task owner.

## Explore the system

Read more about how the system works:

- [How Aapilot works](docs/design/verification-contract.md): who does the work, how decisions are made, and what must be checked
- [System graph](visualizations/skill-library/index.html): see which skills call each other
- [System structure and sources](docs/design/skill-system.md): skill responsibilities, origins, and local changes
- [Codex usage](docs/ops/codex.md): how to start skills in Codex and configure them
- [Version history](CHANGELOG.md): releases and changes to skill names and commands

## Change the library

A change to one skill can affect the skills that call it. Start with the [maintenance rules](AGENTS.md) and follow the [skill authoring playbook](skills/aapilot/playbooks/authoring-a-skill.md) to check those relationships. The [evaluation playbook](skills/aapilot/playbooks/eval.md) describes how to try instruction changes on realistic tasks and inspect the results.

For development, follow the [maintainer setup](docs/ops/releasing.md#maintainer-setup) to install Python dependencies and run the package checks.

## Export the library

Skills call other skills and load shared references, so keep the [export contents](docs/design/skill-system.md#export-boundary) together. Include both plugin manifests, all skills, and the license notices.

Coding tools differ in how they discover and call skills. See the [release guide](docs/ops/releasing.md) for package checks, publication, and upgrades.

## License and attribution

Original contributions are licensed under the [MIT License](LICENSE), copyright Ahmad Abdalla.

This system is inspired by and adapts [pstack](https://github.com/cursor/plugins/tree/main/pstack) by Lauren Tan and [Matt Pocock's skills](https://github.com/mattpocock/skills). Their original MIT notices are preserved in [PSTACK_LICENSE.txt](PSTACK_LICENSE.txt) and [MATT_POCOCK_LICENSE.txt](MATT_POCOCK_LICENSE.txt).

The [source and adaptation inventory](docs/design/skill-system.md#skill-inventory) identifies the upstream sources and local changes for each skill.
