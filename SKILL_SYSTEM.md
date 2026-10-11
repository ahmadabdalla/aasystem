# Skill system

This file records the library’s structure, ownership, sources, and deliberate adaptations.

It does not define maintenance steps or Codex invocation settings.

- **Maintenance rules:** [`AGENTS.md`](AGENTS.md)
- **Codex settings:** [`CODEX.md`](CODEX.md)
- **Plugin preparation:** [`PLUGIN_PLAN.md`](PLUGIN_PLAN.md)
- **Visual map:** [Ahmad Abdalla's Work System Graph](visualizations/skill-library/index.html)

## System flow

The default flow is:

`aasystem -> playbook -> supporting skills -> project evidence`

1. [`aasystem`](skills/aasystem/SKILL.md) owns coordination and completion
2. A playbook defines the task sequence
3. Supporting skills return bounded results to their caller
4. The caller updates canonical project records
5. Project verification supplies observed results

All procedural skills use:

- The [execution contract](skills/aasystem/references/execution.md)
- The [principle index](skills/principles/INDEX.md)
- The current project instructions
- The current task brief

## Ownership boundaries

Use these boundaries when skills interact:

- **aasystem:** routing, coordination, and completion
- **Product:** journeys, behavior, rules, and acceptance scenarios
- **Grill me:** attributed interview evidence
- **Interaction design:** navigation, interactions, and information hierarchy
- **UI refinement:** the bounded human review loop
- **Prototype:** the inspectable throwaway artifact
- **Solution:** the overall approach
- **Architect:** implementation shape and boundaries
- **Feature playbook:** authorized production delivery
- **Project verifier:** observed behavior and reusable checks
- **Caller:** phase transitions and canonical record updates

Supporting skills do not gain production scope from an assignment.

Project records remain usable without this library.

Separate reports need a stated retention purpose.

## Project-owned records

Projects own these durable records:

- Verification procedures
- Feature maps
- Glossaries
- Product decisions
- Design decisions
- Software decisions

New feature maps live inside the project verifier.

Use `features/README.md` plus linked feature files.

Preserve an equivalent existing layout.

For OpenSpec projects, use the [integration reference](skills/aasystem/references/openspec.md).

## Skill inventory

Each row names the skill’s role, source, and local adaptation.

| Skill | Role | Source | Local adaptation |
| --- | --- | --- | --- |
| [`aasystem`](skills/aasystem/SKILL.md) | Coordinate and finish tasks | pstack [`poteto-mode`](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/SKILL.md) | Uses host tools; needs no custom agent setup |
| [`product`](skills/product/SKILL.md) | Define journeys and behavior | First-party split; [OpenSpec](https://github.com/Fission-AI/OpenSpec/blob/main/docs/concepts.md) | Owns discovery synthesis and separates facts, proposals, and agreements |
| [`solution`](skills/solution/SKILL.md) | Choose the overall approach | pstack [`investigation`](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/investigation.md) | Adds solution design and unresolved conditions |
| [`architect`](skills/architect/SKILL.md) | Shape implementation boundaries | pstack [`architect`](https://github.com/cursor/plugins/blob/main/pstack/skills/architect/SKILL.md) | Can stop after design; verifies against requirements |
| [`interaction-design`](skills/interaction-design/SKILL.md) | Design consequential interactions | pstack [`Experience First`](https://github.com/cursor/plugins/blob/9f451cf875ad1239912762f67741e8e5ba6ac0f1/pstack/skills/principle-experience-first/SKILL.md), [`Exhaust the Design Space`](https://github.com/cursor/plugins/blob/9f451cf875ad1239912762f67741e8e5ba6ac0f1/pstack/skills/principle-exhaust-the-design-space/SKILL.md), Matt Pocock [`wayfinder`](https://github.com/mattpocock/skills/blob/6fd947921b935b7e1e69293a200400f0fdd5c15f/skills/engineering/wayfinder/SKILL.md) | Keeps product meaning and implementation architecture with their owners |
| [`ui-refinement`](skills/ui-refinement/SKILL.md) | Refine a rendered experience | First-party founder requirement | Returns a reviewed reference; the caller retains delivery |
| [`prototype`](skills/prototype/SKILL.md) | Build an inspectable experiment | Matt Pocock [`prototype`](https://github.com/mattpocock/skills/blob/6fd947921b935b7e1e69293a200400f0fdd5c15f/skills/engineering/prototype/SKILL.md) | Uses isolated artifacts; excludes automatic production promotion |
| [`how`](skills/how/SKILL.md) | Trace current behavior | pstack [`how`](https://github.com/cursor/plugins/blob/main/pstack/skills/how/SKILL.md) | Reports unavailable exploration paths |
| [`why`](skills/why/SKILL.md) | Reconstruct prior rationale | pstack [`why`](https://github.com/cursor/plugins/blob/main/pstack/skills/why/SKILL.md) | Checks several evidence sources and reports access gaps |
| [`probe`](skills/probe/SKILL.md) | Test an important assumption | pstack [`prototype`](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/prototype.md) | Separates empirical questions from artifact prototyping |
| [`arena`](skills/arena/SKILL.md) | Compare competing options | pstack [`arena`](https://github.com/cursor/plugins/blob/main/pstack/skills/arena/SKILL.md) | Uses an independent judge when available |
| [`interrogate`](skills/interrogate/SKILL.md) | Find consequential weaknesses | pstack [`interrogate`](https://github.com/cursor/plugins/blob/main/pstack/skills/interrogate/SKILL.md) | Also checks whether the work solves the right problem |
| [`grill-me`](skills/grill-me/SKILL.md) | Run a bounded interview | Matt Pocock [`grilling`](https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md) | Returns attributed evidence; Product owns synthesis |
| [`domain-modeling`](skills/domain-modeling/SKILL.md) | Define terms and record decisions | Matt Pocock [`domain-modeling`](https://github.com/mattpocock/skills/blob/b0618bc436ad893b3c5e84e55fba86586d34a404/skills/engineering/domain-modeling/SKILL.md) | Adds ownership, evidence, layout, and supersession rules |
| [`tdd`](skills/tdd/SKILL.md) | Prove a regression before a fix | pstack [`tdd`](https://github.com/cursor/plugins/blob/main/pstack/skills/tdd/SKILL.md) | Adds practical test limits and repeats the original check |
| [`swarm`](skills/swarm/SKILL.md) | Coordinate parallel work | pstack [`swarm`](https://github.com/cursor/plugins/blob/main/pstack/skills/swarm/SKILL.md) | Uses available models; missing results remain unfinished |
| [`figure-it-out`](skills/figure-it-out/SKILL.md) | Create a task-specific workflow | pstack [`figure-it-out`](https://github.com/cursor/plugins/blob/main/pstack/skills/figure-it-out/SKILL.md) | Preserves plan-only requests and adds explicit checks |
| [`show-me-your-work`](skills/show-me-your-work/SKILL.md) | Keep a decision log | pstack [`show-me-your-work`](https://github.com/cursor/plugins/blob/main/pstack/skills/show-me-your-work/SKILL.md) | Saves locally and reports missing review material |
| [`reflect`](skills/reflect/SKILL.md) | Turn session findings into edits | pstack [`reflect`](https://github.com/cursor/plugins/blob/df581122cde17e6e27686b5a448bde23e4ad4318/pstack/skills/reflect/SKILL.md) | Adapts transcript access, reviewers, approval, and host tools |
| [`bootstrap-verification`](skills/bootstrap-verification/SKILL.md) | Create project verification | pstack [`create-verification-skill`](https://github.com/cursor/plugins/blob/main/pstack/skills/create-verification-skill/SKILL.md) | Writes project-owned checks and a feature map |
| [`maintain-verification`](skills/maintain-verification/SKILL.md) | Maintain project verification | pstack [`maintain-verification-skill`](https://github.com/cursor/plugins/blob/main/pstack/skills/maintain-verification-skill/SKILL.md) | Separates product defects from verifier drift |
| [`principle-preserve-decision-context`](skills/principle-preserve-decision-context/SKILL.md) | Preserve decision inputs | User-approved judgment | Removes repetition only when the next decision stays informed |
| [`principle-ui-meaning-through-structure`](skills/principle-ui-meaning-through-structure/SKILL.md) | Express UI meaning through structure | User-approved judgment | Retains text needed for safety, limits, or decisions |

## Orchestrator playbooks

The aasystem skill selects one of these sequences:

| Playbook | Purpose |
| --- | --- |
| [`investigation`](skills/aasystem/playbooks/investigation.md) | Answer a question with evidence |
| [`bug-fix`](skills/aasystem/playbooks/bug-fix.md) | Reproduce, diagnose, fix, and recheck |
| [`feature`](skills/aasystem/playbooks/feature.md) | Design, build, and verify a feature |
| [`refactoring`](skills/aasystem/playbooks/refactoring.md) | Change structure without changing behavior |
| [`prototype`](skills/aasystem/playbooks/prototype.md) | Coordinate a bounded experiment |
| [`authoring-a-skill`](skills/aasystem/playbooks/authoring-a-skill.md) | Create or update a skill |
| [`eval`](skills/aasystem/playbooks/eval.md) | Run fresh candidates against separate criteria |
| [`opening-a-pr`](skills/aasystem/playbooks/opening-a-pr.md) | Prepare, publish, and confirm a pull request |

The playbooks follow [pstack’s playbook set](https://github.com/cursor/plugins/tree/main/pstack/skills/poteto-mode/playbooks).

## Deliberate system adaptations

### Coordination

The [execution contract](skills/aasystem/references/execution.md) adds:

- Caller-owned phase transitions
- Scoped decision authority
- Non-overlapping canonical writes
- Freshness checks after supporting work returns
- No implied scheduler, runtime lock, or automatic approval
- Fresh workers for independent tasks
- Independent candidates and judges
- Adversarial review where the playbook requires it

Local styling cannot silently change a shared design system.

Shared rules stay in the execution contract.

Specialists keep only actionable scope reminders.

### UI review

The [UI refinement loop](skills/ui-refinement/references/refinement-loop.md) adds:

- Conditional grounding through How and Why
- Product ownership of business meaning
- Interaction Design ownership of visual-reference content
- Prototype ownership of the rendered candidate
- Feature ownership of delivery and final comparison
- Existing records for the review checkpoint and evidence

This is not a visual-parity claim.

It is not required for every UI edit.

### Decision records

The [ADR convention](skills/domain-modeling/references/adr.md) preserves Matt Pocock’s rules:

- Require reversal cost, surprising rationale, and a real tradeoff
- Default to a title and one to three short sentences
- Lazy creation and sequential numbering
- System-wide and established-context scope

The local system adds:

- Product, design, and software ownership
- Project-defined directory layouts
- One decision per record
- Cross-links between related decisions
- Separate authority and implementation evidence
- Explicit update, split, and supersession handling

Poteto supplies workflow ideas, not the ADR taxonomy.

Accepted decisions constrain work but do not prove the result.

Runtime guidance excludes evaluation-only examples.

### Verification evidence

The [project verification contract](skills/bootstrap-verification/references/project-contract.md#evidence-and-retention) owns evidence lifetime.

It separates:

- Durable verification recipes
- Temporary review evidence
- Deliberately retained proof

Local additions include:

- Project conventions before fallback paths
- `.verification/runs/` as the uncommitted fallback
- Retention through review or investigation
- Explicit disposal and migration rules
- Source identity for the exercised artifact
- A Git guard for temporary verification output
- Durable proof only for a named future reader

The guard can reuse or install the [shell asset](skills/bootstrap-verification/assets/check-verification-output.sh).

Unrelated workspace inventory is outside evidence identity.

Upstream sources are:

- pstack [`create-verification-skill`](https://github.com/cursor/plugins/blob/df581122cde17e6e27686b5a448bde23e4ad4318/pstack/skills/create-verification-skill/SKILL.md)
- pstack [`maintain-verification-skill`](https://github.com/cursor/plugins/blob/df581122cde17e6e27686b5a448bde23e4ad4318/pstack/skills/maintain-verification-skill/SKILL.md)
- pstack [`Prove It Works`](https://github.com/cursor/plugins/blob/df581122cde17e6e27686b5a448bde23e4ad4318/pstack/skills/principle-prove-it-works/SKILL.md)
- pstack [`Show Me Your Work`](https://github.com/cursor/plugins/blob/df581122cde17e6e27686b5a448bde23e4ad4318/pstack/skills/show-me-your-work/SKILL.md)
- pstack [`Encode Lessons in Structure`](https://github.com/cursor/plugins/blob/df581122cde17e6e27686b5a448bde23e4ad4318/pstack/skills/principle-encode-lessons-in-structure/SKILL.md)

## Supporting sources

Other sources inform bounded parts of the system:

- **Technology discovery:** [`tech-interviewer`](https://github.com/ahmadabdalla/tech-interviewer)
- **Context control:** pstack [`Guard the Context Window`](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-guard-the-context-window/SKILL.md)
- **Worker baseline:** pstack [`poteto-agent`](https://github.com/cursor/plugins/blob/main/pstack/agents/poteto-agent.md)
- **Learning:** pstack [`Automate me`](https://github.com/cursor/plugins/blob/main/pstack/skills/automate-me/SKILL.md)
- **Feature maps:** pstack [`feature-map example`](https://github.com/cursor/plugins/blob/main/pstack/skills/create-verification-skill/references/feature-map-example/README.md)
- **Specification workflow:** OpenSpec [`CLI`](https://github.com/Fission-AI/OpenSpec/blob/main/docs/cli.md) and [`workflows`](https://github.com/Fission-AI/OpenSpec/blob/main/docs/workflows.md)

## Evaluation coverage

The current evaluation packages cover:

| Package | Coverage |
| --- | --- |
| [`product-to-ui`](evals/product-to-ui/README.md) | Authority, interaction coverage, UI review, delivery, and portability |
| [`product-discovery`](evals/product-discovery/README.md) | Interviews, evidence, journeys, requirements, and checkpoints |
| [`adr-ownership`](evals/adr-ownership/README.md) | Decision scope, ownership, layout, maintenance, and counterexamples |
| [`verification-lifecycle`](evals/verification-lifecycle/README.md) | Temporary output, teardown, retained proof, and reruns |

Fixtures define test cases.

They do not prove that an evaluation passed.

## Export boundary

Export these files together:

- [`plugin.json`](plugin.json)
- [`.claude-plugin/plugin.json`](.claude-plugin/plugin.json)
- [`skills/`](skills/)
- [`LICENSE`](LICENSE)
- [`PSTACK_LICENSE.txt`](PSTACK_LICENSE.txt)
- [`MATT_POCOCK_LICENSE.txt`](MATT_POCOCK_LICENSE.txt)
- [`SKILL_SYSTEM.md`](SKILL_SYSTEM.md)
- [`README.md`](README.md)
- [`CODEX.md`](CODEX.md)

The portable root manifest and Claude compatibility manifest package the same skill tree as `aasystem`. The root manifest owns the portable identity and OpenAI presentation metadata. Keep the compatibility identity and version consistent. Packaging preserves the library's invocation policies and specialist boundaries.

See [`CODEX.md`](CODEX.md) for Codex adapters and invocation limits.
