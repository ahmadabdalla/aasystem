# Skill system

This file records the library’s structure, ownership, sources, and deliberate adaptations.

It does not define maintenance steps or Codex invocation settings.

- **Maintenance rules:** [`AGENTS.md`](../../AGENTS.md)
- **Codex settings:** [`docs/ops/codex.md`](../ops/codex.md)
- **Operating design:** [How Aapilot works](verification-contract.md)
- **Visual map:** [Ahmad Abdalla's Pilot System Graph](../../visualizations/skill-library/index.html)

## System flow

The default flow is:

`aapilot -> playbook -> supporting skills -> project evidence`

1. [`aapilot`](../../skills/aapilot/SKILL.md) owns coordination and completion
2. A playbook defines the task sequence
3. Supporting skills return bounded results to their caller
4. The caller updates canonical project records
5. Project verification supplies observed results

All procedural skills use:

- The [execution contract](../../skills/aapilot/references/execution.md)
- The [principle index](../../skills/principles/INDEX.md)
- The current project instructions
- The current task brief

## Ownership boundaries

Use these boundaries when skills interact:

- **aapilot:** shared understanding, scope and proof assessment, routing, direct or delegated execution, and completion
- **Product:** journeys, behavior, rules, and acceptance scenarios
- **Grill me:** attributed interview evidence
- **Interaction design:** navigation, interactions, and information hierarchy
- **UI refinement:** the bounded human review loop
- **Prototype:** the inspectable throwaway artifact
- **Solution:** the overall approach
- **Architect:** implementation shape, boundaries, rationale, and verification planning; design-only
- **Implement:** bounded edits against a supplied design or contract, development checks, and evidence return
- **Maintainability:** reusable criteria for reader effort, local change cost, and ease of verification; also returns bounded assessments to its caller
- **Feature playbook:** authorized production delivery
- **Project verifier:** the project-owned procedure and reusable checks
- **Independent verification agent:** a separate worker that assesses the actual diff using Maintainability criteria and exercises the changed artifact through the project verifier; returns distinct findings and executable observations
- **Interrogate:** adversarial review findings; review does not replace executable verification
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

For OpenSpec projects, use the [integration reference](../../skills/aapilot/references/openspec.md).

## Skill inventory

Each row names the skill’s role, source, and local adaptation.

| Skill | Role | Source | Local adaptation |
| --- | --- | --- | --- |
| [`aapilot`](../../skills/aapilot/SKILL.md) | Coordinate and finish tasks | pstack [`poteto-mode`](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/SKILL.md) | Uses host tools; needs no custom agent setup |
| [`product`](../../skills/product/SKILL.md) | Define journeys and behavior | First-party split; [OpenSpec](https://github.com/Fission-AI/OpenSpec/blob/main/docs/concepts.md) | Owns discovery synthesis and separates facts, proposals, and agreements |
| [`solution`](../../skills/solution/SKILL.md) | Choose the overall approach | pstack [`investigation`](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/investigation.md); [selected engineering inputs](#selected-engineering-inputs) | Compares viable existing and simpler approaches, exposes consequential assumptions, and records demonstrated reversal costs and reconsideration conditions |
| [`architect`](../../skills/architect/SKILL.md) | Shape implementation boundaries | pstack [`architect`](https://github.com/cursor/plugins/blob/main/pstack/skills/architect/SKILL.md); [selected engineering inputs](#selected-engineering-inputs) | Applies Maintainability criteria and justifies added structure against present callers, invariants, and change burden; returns a design package and proof plan while the caller retains implementation and acceptance |
| [`implement`](../../skills/implement/SKILL.md) | Execute bounded edits and development checks | First-party extraction from the library’s implementation workflows and [execution contract](../../skills/aapilot/references/execution.md); [selected engineering inputs](#selected-engineering-inputs) | Applies relevant Maintainability criteria within settled scope, returns edits and development evidence, and returns design contradictions to the caller; final acceptance remains with the owner |
| [`maintainability`](../../skills/maintainability/SKILL.md) | Assess reader effort, local change, and ease of verification | pstack [`Minimize Reader Load`](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-minimize-reader-load/SKILL.md) and [`Architect red flags`](https://github.com/cursor/plugins/blob/main/pstack/skills/architect/references/design-red-flags.md); Matt Pocock [`codebase-design`](https://github.com/mattpocock/skills/blob/main/skills/engineering/codebase-design/SKILL.md) and [`code-review`](https://github.com/mattpocock/skills/blob/main/skills/engineering/code-review/SKILL.md); [selected engineering inputs](#selected-engineering-inputs) | Owns reusable criteria in [`SKILL.md`](../../skills/maintainability/SKILL.md), [`local code`](../../skills/maintainability/references/local-code.md), and [`boundaries`](../../skills/maintainability/references/boundaries.md), consumed directly by design, implementation, and independent verification |
| [`interaction-design`](../../skills/interaction-design/SKILL.md) | Design consequential interactions | pstack [`Experience First`](https://github.com/cursor/plugins/blob/9f451cf875ad1239912762f67741e8e5ba6ac0f1/pstack/skills/principle-experience-first/SKILL.md), [`Exhaust the Design Space`](https://github.com/cursor/plugins/blob/9f451cf875ad1239912762f67741e8e5ba6ac0f1/pstack/skills/principle-exhaust-the-design-space/SKILL.md), Matt Pocock [`wayfinder`](https://github.com/mattpocock/skills/blob/6fd947921b935b7e1e69293a200400f0fdd5c15f/skills/engineering/wayfinder/SKILL.md) | Keeps product meaning and implementation architecture with their owners |
| [`ui-refinement`](../../skills/ui-refinement/SKILL.md) | Refine a rendered experience | First-party founder requirement | Returns a reviewed reference; the caller retains delivery |
| [`prototype`](../../skills/prototype/SKILL.md) | Build an inspectable experiment | Matt Pocock [`prototype`](https://github.com/mattpocock/skills/blob/6fd947921b935b7e1e69293a200400f0fdd5c15f/skills/engineering/prototype/SKILL.md) | Uses isolated artifacts; excludes automatic production promotion |
| [`how`](../../skills/how/SKILL.md) | Trace current behavior | pstack [`how`](https://github.com/cursor/plugins/blob/main/pstack/skills/how/SKILL.md) | Reports unavailable exploration paths |
| [`why`](../../skills/why/SKILL.md) | Reconstruct prior rationale | pstack [`why`](https://github.com/cursor/plugins/blob/main/pstack/skills/why/SKILL.md) | Checks several evidence sources and reports access gaps |
| [`probe`](../../skills/probe/SKILL.md) | Test an important assumption | pstack [`prototype`](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/prototype.md) | Separates empirical questions from artifact prototyping |
| [`arena`](../../skills/arena/SKILL.md) | Compare competing options | pstack [`arena`](https://github.com/cursor/plugins/blob/main/pstack/skills/arena/SKILL.md) | Uses an independent judge when available |
| [`interrogate`](../../skills/interrogate/SKILL.md) | Find consequential weaknesses | pstack [`interrogate`](https://github.com/cursor/plugins/blob/main/pstack/skills/interrogate/SKILL.md) | Also challenges framing and selects review inputs through the shared context rule |
| [`grill-me`](../../skills/grill-me/SKILL.md) | Run a bounded interview | Matt Pocock [`grilling`](https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md) | Returns attributed evidence; Product owns synthesis |
| [`domain-modeling`](../../skills/domain-modeling/SKILL.md) | Define terms and record decisions | Matt Pocock [`domain-modeling`](https://github.com/mattpocock/skills/blob/b0618bc436ad893b3c5e84e55fba86586d34a404/skills/engineering/domain-modeling/SKILL.md) | Adds ownership, evidence, layout, and supersession rules |
| [`tdd`](../../skills/tdd/SKILL.md) | Prove a regression before a fix | pstack [`tdd`](https://github.com/cursor/plugins/blob/main/pstack/skills/tdd/SKILL.md) | Adds practical test limits and repeats the original check |
| [`swarm`](../../skills/swarm/SKILL.md) | Coordinate parallel work | pstack [`swarm`](https://github.com/cursor/plugins/blob/main/pstack/skills/swarm/SKILL.md) | Uses available models; missing results remain unfinished |
| [`figure-it-out`](../../skills/figure-it-out/SKILL.md) | Create a task-specific workflow | pstack [`figure-it-out`](https://github.com/cursor/plugins/blob/main/pstack/skills/figure-it-out/SKILL.md) | Preserves plan-only requests and adds explicit checks |
| [`show-me-your-work`](../../skills/show-me-your-work/SKILL.md) | Keep a decision log | pstack [`show-me-your-work`](https://github.com/cursor/plugins/blob/main/pstack/skills/show-me-your-work/SKILL.md) | Saves locally and reports missing review material |
| [`reflect`](../../skills/reflect/SKILL.md) | Turn session findings into edits | pstack [`reflect`](https://github.com/cursor/plugins/blob/df581122cde17e6e27686b5a448bde23e4ad4318/pstack/skills/reflect/SKILL.md) | Adapts transcript access, reviewers, approval, and host tools |
| [`bootstrap-verification`](../../skills/bootstrap-verification/SKILL.md) | Create project verification | pstack [`create-verification-skill`](https://github.com/cursor/plugins/blob/main/pstack/skills/create-verification-skill/SKILL.md) | Writes project-owned checks and a feature map |
| [`maintain-verification`](../../skills/maintain-verification/SKILL.md) | Maintain project verification | pstack [`maintain-verification-skill`](https://github.com/cursor/plugins/blob/main/pstack/skills/maintain-verification-skill/SKILL.md) | Separates product defects from verifier drift |
| [`principle-preserve-decision-context`](../../skills/principle-preserve-decision-context/SKILL.md) | Preserve decision inputs | User-approved judgment | Removes repetition only when the next decision stays informed |
| [`principle-ui-meaning-through-structure`](../../skills/principle-ui-meaning-through-structure/SKILL.md) | Express UI meaning through structure | User-approved judgment | Retains text needed for safety, limits, or decisions |

## Orchestrator playbooks

The aapilot skill selects one of these sequences:

| Playbook | Purpose |
| --- | --- |
| [`investigation`](../../skills/aapilot/playbooks/investigation.md) | Answer a question with evidence |
| [`bug-fix`](../../skills/aapilot/playbooks/bug-fix.md) | Reproduce, diagnose, fix, and recheck |
| [`feature`](../../skills/aapilot/playbooks/feature.md) | Design, build, and verify a feature |
| [`refactoring`](../../skills/aapilot/playbooks/refactoring.md) | Change structure without changing behavior |
| [`prototype`](../../skills/aapilot/playbooks/prototype.md) | Coordinate a bounded experiment |
| [`authoring-a-skill`](../../skills/aapilot/playbooks/authoring-a-skill.md) | Create or update a skill |
| [`eval`](../../skills/aapilot/playbooks/eval.md) | Run fresh candidates against separate criteria |
| [`opening-a-pr`](../../skills/aapilot/playbooks/opening-a-pr.md) | Prepare, publish, and confirm a pull request |

The playbooks follow [pstack’s playbook set](https://github.com/cursor/plugins/tree/main/pstack/skills/poteto-mode/playbooks).

## Deliberate system adaptations

### Coordination

The [execution contract](../../skills/aapilot/references/execution.md) adds:

- Caller-owned phase transitions
- Sourced requirements, delegated implementation proposals and actual human agreement under [decision authority](../../skills/aapilot/references/execution.md#decision-authority), which owns the inspectable human checkpoint handoff and stop/wait rule
- Non-overlapping canonical writes
- Freshness checks after supporting work returns
- No implied scheduler, runtime lock, or automatic approval
- Fresh workers for independent tasks
- Independent candidates and judges
- Review inputs distinguishing independent discovery from confirmation/evidence audits, including exposure through initial returned findings and preserved initial reports
- Adversarial review where the playbook requires it

Local styling cannot silently change a shared design system.

Shared rules stay in the execution contract. Its [delegation procedure](../../skills/aapilot/references/execution.md#delegation) owns capability checks, direct or delegated execution and result acceptance; its [completion rules](../../skills/aapilot/references/execution.md#completion) own planned closing assignments and final reconciliation.

Specialists keep only actionable scope reminders.

The [skill authoring playbook](../../skills/aapilot/playbooks/authoring-a-skill.md) owns instruction specificity, deduplication, and criteria for splitting skills or using references.

Worker selection follows a concrete parallelism, capability or context need. Comparison uses independent candidates when they can change an unresolved material choice; selected Arena comparisons retain isolation and separate judging. Bounded implementer continuity does not relax fresh independent verification.

The [Architect design trigger](../../skills/architect/SKILL.md#design-trigger) owns the boundary criterion linked by Bug Fix and Refactoring. [Swarm](../../skills/swarm/SKILL.md) declares comparison criteria before ranked races. [Domain Modeling](../../skills/domain-modeling/SKILL.md) distinguishes established glossary meanings from decision-record standing and authority.

### Standard verification contract

The first-party [verification-contract reference](../../skills/aapilot/references/verification-contract.md) owns the common receipt procedure for retained production changes through existing entry skills. One root owner retains request/authority, scope, source identity, nonempty claims, observations, evidence, limits and explicit acceptance. Specialists contribute to the same run within their existing scope. Read-only answers and design work keep scoped obligations without production ceremony.

The [execution contract](../../skills/aapilot/references/execution.md#owner-presentation-eligibility) owns the narrow owner-presentation eligibility rule, before/after checks and escalation. Feature exposes that short path before its six phases; direct Implement can own an eligible request without a coordinator wrapper or worker. Owner-presentation proof is distinct from independent proof and cannot waive independent engineering review required by the user, project, or task. Other retained production changes require separate verification and applicable human checkpoints.

[work_receipts.py](../../skills/aapilot/scripts/work_receipts.py) is the Python 3.10+ standard-library structural helper. The thin CLI delegates to private `_work_receipts` modules: `state.py` owns run mutation and locked commit orchestration; `evidence.py` owns input identity, report/proof inspection and protected snapshot effects; `gates.py` owns read-only eligibility, decision, native-attempt and review-interval checks; `__init__.py` marks the package. Keep that implementation closure and the complete export tree together. Repository tests and temporary evaluation artifacts are not runtime dependencies and remain outside the export.

The common mechanism retains current decision reviews, mandatory checkpoints, native attempt reservations/results when workers run, frozen initial independent findings, current artifact/proof identities, human pause/resume and uncertain-effect reconciliation. Each actual continuation uses the same nonrefundable root budget; generated owner-presentation metadata requires no fake native attempt. Existing owners retain semantic acceptance and canonical records. State/evidence remain outside the installed tree/cache. Diagnose missing Python/helper access or leave validation unmet.

Receipt validation neither authenticates people/native calls nor detects omitted semantic choices, undeclared exposure or direct native-tool bypass. It adds no coordinator, daemon, installer, portable skill or domain profile. Bounded autonomy applies to explicitly authorized work during a supported active session, using existing scope, authority, evidence and budget records. It retains whole-process human checkpoints. Package checks and local CLI proof do not establish scheduling, host discovery, session survival, automatic recovery or other-host support. [How Aapilot works](verification-contract.md) explains the current operating design, proof paths, and limits; the linked execution and verification contracts own the procedures.

### Design, implementation, and independent verification

[`architect`](../../skills/architect/SKILL.md) owns design only: caller usage, interfaces, data shapes, ownership, rationale, and proof planning. A direct design-and-build request needs a coordinating playbook to retain implementation and completion scope. Implementation evidence that contradicts the design returns through the caller for design revision.

[`implement`](../../skills/implement/SKILL.md) is shared bounded execution support for Feature, Bug Fix, Refactoring, and Figure It Out. Each caller supplies its settled design or contract, file ownership, constraints, and assigned checks; Implement returns edits and development evidence into that caller’s run. A direct eligible owner-presentation request can stay with Implement through acceptance.

The [execution contract](../../skills/aapilot/references/execution.md#independent-implementation-verification) owns dispatch of a separate verification worker and [owner-presentation eligibility](../../skills/aapilot/references/execution.md#owner-presentation-eligibility). The first-party [engineering-verification reference](../../skills/aapilot/references/engineering-verification.md) defines that worker's combined assignment: bounded scope and structure assessment using Maintainability criteria, plus affected project-verifier checks. These remain separate claims and evidence in one root run and verifier report. The verifier is an existing agent role, not another portable skill or review pool. The caller retains integration, material-finding dispositions, current proof, and explicit semantic acceptance. Interrogate supplies adversarial review when warranted; its findings do not establish runtime behavior.

### Maintainability

[`maintainability`](../../skills/maintainability/SKILL.md) is a conditional supporting assessment for Architect, Refactoring, and Interrogate when its findings can change a design, structural improvement, or review verdict.

The reusable assessment criteria formerly held by Architect now live with Maintainability in its [`SKILL.md`](../../skills/maintainability/SKILL.md), [local-code reference](../../skills/maintainability/references/local-code.md), and [boundaries reference](../../skills/maintainability/references/boundaries.md). Architect, Implement, and the independent verifier consume the relevant criteria directly; reading them does not require a separate Maintainability invocation. The conditional deeper assessment remains available when its findings could change a decision. Architect retains implementation design and Refactoring retains equivalence proof.

### Selected engineering inputs

The user supplied local Clean Code and Pragmatic Programmer references as conceptual inputs. The local Clean Code skill's metadata identifies author `wondelai`, version `1.4.0`, and license `MIT`. The supplied Pragmatic Programmer file has no license declaration; no additional provenance or license is asserted here. These local inputs are not export dependencies.

The library authors its own bounded adaptations rather than copying those manuals: names and flow that expose intent, meaningful failure contracts, preserved rationale, duplication judged as shared knowledge, explicit invariants, test independence, generated-source ownership, and evidence about coupling and reversal cost. Solution owns approach and commitment comparisons. Maintainability owns the criteria consumed by Architect for design, Implement for assigned edits, and the existing verifier for independent assessment. The [engineering-verification reference](../../skills/aapilot/references/engineering-verification.md) is a first-party procedure for that gate. Fixed cleanliness scores, size quotas, blanket extraction or error-handling policies, speculative abstractions, and unrelated cleanup are not adopted.

### UI review

The [UI refinement loop](../../skills/ui-refinement/references/refinement-loop.md) adds:

- Conditional grounding through How and Why
- Product ownership of business meaning
- Interaction Design ownership of visual-reference content
- Prototype ownership of the rendered candidate
- Bounded composition under the loop's [rendering assignment rules](../../skills/ui-refinement/references/refinement-loop.md#rendering-assignments), preserving role ownership and required independence
- Feature ownership of delivery and final comparison
- Existing records for the review checkpoint and evidence

This is not a visual-parity claim.

It is not required for every UI edit.

### Decision records

The [ADR convention](../../skills/domain-modeling/references/adr.md) preserves Matt Pocock’s rules:

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
- Project rules before existing scoped conventions (including older formats), then a framework default
- Required default content and review failures tied to the selected rules

Poteto supplies workflow ideas, not the ADR taxonomy.

The default content and shared author/reviewer contract adapt pstack's [architecture rationale template](https://github.com/cursor/plugins/blob/1dcc2bacde73ddd284803b7af28164d0436198fc/pstack/skills/architect/references/rationale-template.md). ADR convention selection is a local addition; the default requires decision meaning without mandatory headings.

Accepted decisions constrain work but do not prove the result.

Runtime guidance excludes evaluation-only examples.

### Verification evidence

The [project verification contract](../../skills/bootstrap-verification/references/project-contract.md#evidence-and-retention) owns evidence lifetime.

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

The guard can reuse or install the [shell asset](../../skills/bootstrap-verification/assets/check-verification-output.sh).

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

## Evaluation

The [evaluation playbook](../../skills/aapilot/playbooks/eval.md) adapts [pstack’s Eval](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/eval.md): realistic tasks, blinded candidates and judging, transcript inspection, and lead reconciliation. Local adaptations use the shared host and invocation rules and project evidence conventions; the playbook owns temporary experiments and the criterion for retaining reusable regression cases. The library does not ship an evaluation runner or a standing fixture collection.

## Export boundary

Export these files together:

- [`plugin.json`](../../plugin.json)
- [`.claude-plugin/plugin.json`](../../.claude-plugin/plugin.json)
- [`skills/`](../../skills/)
- [`LICENSE`](../../LICENSE)
- [`PSTACK_LICENSE.txt`](../../PSTACK_LICENSE.txt)
- [`MATT_POCOCK_LICENSE.txt`](../../MATT_POCOCK_LICENSE.txt)
- [`docs/design/skill-system.md`](skill-system.md)
- [`README.md`](../../README.md)
- [`docs/ops/codex.md`](../ops/codex.md)

The portable root manifest and Claude compatibility manifest package the same skill tree as `aasystem`. The root manifest owns the portable identity, version and OpenAI presentation metadata. The [release validator](../../scripts/validate-release.py) checks the compatibility identity and version mechanically. Packaging preserves the library's invocation policies and specialist boundaries.

The [release process](../ops/releasing.md) adapts Azure Cost Calculator's tag/release and changelog helpers. Merging a reviewed, manually versioned release PR into `main` triggers validation and publication of its exact merged commit, with safe retries. Successful publication prepares a separate reviewed marketplace adoption PR. Release automation does not change skill routes or handoffs.

See [`docs/ops/codex.md`](../ops/codex.md) for Codex adapters and invocation limits.
