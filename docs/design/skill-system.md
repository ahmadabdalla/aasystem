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
- **Interaction design:** navigation, interactions, information hierarchy, and coordination of assigned independent rendered UX assessments
- **UI refinement:** the bounded human review loop
- **Prototype:** the inspectable throwaway artifact
- **Solution:** the overall approach
- **Architect:** implementation shape, boundaries, rationale, and verification planning; design-only
- **10x:** shared growth assessment; domain callers retain decisions and carry required proof into delivery
- **Implement:** bounded edits against a supplied design or contract, development checks, and evidence return
- **Maintainability:** reusable criteria for reader effort, local change cost, and ease of verification; also returns bounded assessments to its caller
- **Feature playbook:** authorized production delivery
- **Project verifier:** the project-owned procedure and reusable checks
- **Independent verification agent:** a worker separate from every producer of assessed work, using the affected domains' criteria and specialist procedures; production engineering combines Maintainability assessment with project-verifier execution and returns distinct findings and observations
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
| [`10x`](../../skills/10x/SKILL.md) | Assess decisions under plausible growth | First-party; user-requested | Returns scenarios, first constraints, accommodate/defer tradeoffs, proof needs and reconsideration triggers to domain callers |
| [`implement`](../../skills/implement/SKILL.md) | Execute bounded edits and development checks | First-party extraction from the library’s implementation workflows and [execution contract](../../skills/aapilot/references/execution.md); [selected engineering inputs](#selected-engineering-inputs) | Applies relevant Maintainability criteria and conditional refactoring moves within settled scope, returns edits and development evidence, and returns design contradictions to the caller; final acceptance remains with the owner |
| [`maintainability`](../../skills/maintainability/SKILL.md) | Assess reader effort, local change, and ease of verification | pstack [`Minimize Reader Load`](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-minimize-reader-load/SKILL.md) and [`Architect red flags`](https://github.com/cursor/plugins/blob/main/pstack/skills/architect/references/design-red-flags.md); Matt Pocock [`codebase-design`](https://github.com/mattpocock/skills/blob/main/skills/engineering/codebase-design/SKILL.md) and [`code-review`](https://github.com/mattpocock/skills/blob/main/skills/engineering/code-review/SKILL.md); [selected engineering inputs](#selected-engineering-inputs) | Owns reusable criteria in [`SKILL.md`](../../skills/maintainability/SKILL.md), [`local code`](../../skills/maintainability/references/local-code.md), and [`boundaries`](../../skills/maintainability/references/boundaries.md), consumed directly by design, implementation, and independent verification |
| [`interaction-design`](../../skills/interaction-design/SKILL.md) | Design consequential interactions | pstack [`Experience First`](https://github.com/cursor/plugins/blob/9f451cf875ad1239912762f67741e8e5ba6ac0f1/pstack/skills/principle-experience-first/SKILL.md), [`Exhaust the Design Space`](https://github.com/cursor/plugins/blob/9f451cf875ad1239912762f67741e8e5ba6ac0f1/pstack/skills/principle-exhaust-the-design-space/SKILL.md), Matt Pocock [`wayfinder`](https://github.com/mattpocock/skills/blob/6fd947921b935b7e1e69293a200400f0fdd5c15f/skills/engineering/wayfinder/SKILL.md) | Keeps product meaning and implementation architecture with their owners |
| [`ui-refinement`](../../skills/ui-refinement/SKILL.md) | Refine a rendered experience | First-party founder requirement | Returns a reviewed reference; the caller retains delivery |
| [`prototype`](../../skills/prototype/SKILL.md) | Build an inspectable experiment | Matt Pocock [`prototype`](https://github.com/mattpocock/skills/blob/6fd947921b935b7e1e69293a200400f0fdd5c15f/skills/engineering/prototype/SKILL.md) | Uses isolated artifacts; excludes automatic production promotion |
| [`how`](../../skills/how/SKILL.md) | Trace current behavior | pstack [`how`](https://github.com/cursor/plugins/blob/main/pstack/skills/how/SKILL.md) | Reports unavailable exploration paths |
| [`why`](../../skills/why/SKILL.md) | Reconstruct prior rationale | pstack [`why`](https://github.com/cursor/plugins/blob/main/pstack/skills/why/SKILL.md) | Checks several evidence sources and reports access gaps |
| [`probe`](../../skills/probe/SKILL.md) | Test an important assumption | pstack [`prototype`](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/prototype.md) | Separates empirical questions from artifact prototyping |
| [`arena`](../../skills/arena/SKILL.md) | Compare competing options | pstack [`arena`](https://github.com/cursor/plugins/blob/main/pstack/skills/arena/SKILL.md) | Uses an independent judge when available |
| [`interrogate`](../../skills/interrogate/SKILL.md) | Find consequential weaknesses | pstack [`interrogate`](https://github.com/cursor/plugins/blob/main/pstack/skills/interrogate/SKILL.md) | Also challenges framing and selects review inputs through the shared context rule |
| [`grill-me`](../../skills/grill-me/SKILL.md) | Interview in decision rounds or conduct product discovery | Matt Pocock [`grilling`](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/productivity/grilling/SKILL.md) and [`grill-with-docs`](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/grill-with-docs/SKILL.md) | Loads one interview reference; reuses Domain Modeling for scoped inline capture; Product retains discovery synthesis |
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

The first-party, user-requested [effort rubric](../../skills/aapilot/references/effort.md) owns S/M/L profiles and consequence-driven scrutiny. The [execution contract](../../skills/aapilot/references/execution.md#scope-and-proof) owns application by task owners and standalone specialists, with [inheritance and reassessment](../../skills/aapilot/references/execution.md#ownership-and-handoffs) across assignments.

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

### Grilling and documentation

Aapilot and direct requests use the same [Grill Me entry](../../skills/grill-me/SKILL.md). The [grilling reference](../../skills/grill-me/references/grilling.md) owns the decision tree, question rounds, fact finding, recommendations and final confirmation. The execution contract supplies scope and authority. Pending facts block only dependent questions; each round waits for the user's answers.

Load Domain Modeling when terms or consequential decisions emerge. Record them as they settle, following its glossary and ADR formats, recording thresholds and edit scope. "With docs" uses this same path. Requirements stay in their brief; read-only work returns proposed text. [Product-discovery interviews](../../skills/grill-me/references/discovery-interview.md) keep their one-question procedure and return attributed evidence to Product for synthesis.

Load the selected interview reference and reuse shared instructions already in context. New contexts read the baseline. Skill count and invocation policies stay unchanged. Package checks alone do not establish host discovery or composition.

### Standard verification contract

The [verification contract](../../skills/aapilot/references/verification-contract.md) connects agreed expectations to the tested artifact, independent observations, findings and delivery. Reuse project records. Research and design retain scoped sources and rationale.

The [execution contract](../../skills/aapilot/references/execution.md#owner-presentation-eligibility) owns the narrow owner-presentation exception. Feature and direct Implement expose it without extra coordinator or worker; it cannot waive independent review required by the user or project. Other retained implementation requires separate verification and applicable human checkpoints.

Local implementation and verification reuse the checkout or one task worktree. The optional [input_identity.py](../../skills/aapilot/scripts/input_identity.py) provides a Python 3.10+/Git read-only fingerprint and comparison when project facilities are insufficient. It streams selected inputs and creates no source copies. Project checks supply behavioural observations; owner/verifier judgment supplies semantic scope and acceptance. None of these mechanisms authenticates actors or controls all host tools.

### Design, implementation, and independent verification

[`architect`](../../skills/architect/SKILL.md) owns design only: caller usage, interfaces, data shapes, ownership, rationale, and proof planning. A direct design-and-build request needs a coordinating playbook to retain implementation and completion scope. Implementation evidence that contradicts the design returns through the caller for design revision.

[`implement`](../../skills/implement/SKILL.md) is shared bounded execution support for Feature, Bug Fix, Refactoring, and Figure It Out. Each caller supplies its settled design or contract, file ownership, constraints, and assigned checks; Implement returns edits and development evidence into that caller’s run. A direct eligible owner-presentation request can stay with Implement through acceptance.

The [execution contract](../../skills/aapilot/references/execution.md#independent-implementation-verification) owns dispatch of a separate verification worker and [owner-presentation eligibility](../../skills/aapilot/references/execution.md#owner-presentation-eligibility). The first-party [engineering-verification reference](../../skills/aapilot/references/engineering-verification.md) defines that worker's combined assignment: bounded scope and structure assessment using Maintainability criteria, plus affected project-verifier checks. Its result distinguishes qualitative findings from executable observations. The verifier is an existing agent role, not another portable skill or review pool. The caller retains integration, material-finding dispositions, current proof, and explicit semantic acceptance. Interrogate supplies adversarial review when warranted; its findings do not establish runtime behavior.

[Feature](../../skills/aapilot/playbooks/feature.md) orders retained implementation around unresolved integration assumptions, recording the first slice's expected and observed results before dependent expansion. Final independent verification remains required.

Architect's first-party [seed scenario reference](../../skills/architect/references/seed-scenarios.md) owns data purpose, minimal context, lifecycle and source/build/release/invocation decisions. Feature reads it when proof depends on state. The [project verification contract](../../skills/bootstrap-verification/references/project-contract.md#scenario-coverage) owns completion and automation criteria through existing Bootstrap/Maintain routes. Decisions and proof stay in current assignments and project records. A conditional reference avoids a separate skill and repeated lifecycle guidance.

### Growth assessment

[`10x`](../../skills/10x/SKILL.md) owns one reusable assessment method. Solution, Architect and Interaction Design apply it before settling consequential designs, reusing current findings and extending only newly exposed constraints. Aapilot also routes standalone growth-assessment requests to it. Direct application and bounded independent assignments use the same contract; invocation creates no new coordinator or mandatory worker.

The assessment states a baseline and growth scenario, first constraint, present/deferred tradeoff, proof need and reconsideration trigger. Assumptions, proposed targets and observed capacity remain distinct. Existing design handoffs carry required checks to [engineering verification](../../skills/aapilot/references/engineering-verification.md); deferred targets do not become release requirements. ADR formatting remains owned by [Domain Modeling](../../skills/domain-modeling/references/adr.md).

### Maintainability

[`maintainability`](../../skills/maintainability/SKILL.md) is a conditional supporting assessment for Architect, Refactoring, and Interrogate when its findings can change a design, structural improvement, or review verdict.

The reusable assessment criteria formerly held by Architect now live with Maintainability in its [`SKILL.md`](../../skills/maintainability/SKILL.md), [local-code reference](../../skills/maintainability/references/local-code.md), and [boundaries reference](../../skills/maintainability/references/boundaries.md). Architect, Implement, and the independent verifier consume the relevant criteria directly; reading them does not require a separate Maintainability invocation. The conditional deeper assessment remains available when its findings could change a decision. Architect retains implementation design and Refactoring retains equivalence proof.

The boundaries reference also supplies dependency-design questions: caller obligations, knowledge ownership, dependency direction, justified adapters, and preserved failure meaning. Architect applies these during comparison; Implement and the verifier use the same criteria against the actual artifact.

Implement conditionally reads [Refactoring moves](../../skills/implement/references/refactoring-moves.md) for assigned structural improvements. Architect conditionally reads [Business state and consistency](../../skills/architect/references/business-state.md) when identity, state ownership, invariants, or cross-context coordination change. Both return into existing design, implementation, and verification handoffs; Domain Modeling retains terminology and records. No new skill, verifier, or external installation is introduced. This PoC keeps each of these three references at no more than 80 physical lines, including headings and blanks.

The [design package](../../skills/architect/references/design-package.md) carries applicable guarantees and required cases into implementation and independent verification. [Engineering Verification](../../skills/aapilot/references/engineering-verification.md) applies local-code criteria to production edits and boundary criteria when relevant, derives checks from the authorised contract and actual artifact as well as that handoff, and keeps qualitative findings separate from executable proof. It reads the business-state procedure only when interpreting or checking coverage requires it. Recipe gaps return through [Maintain Verification](../../skills/maintain-verification/SKILL.md) within the existing scope; unchanged recipes need no edit. One verifier can cover these concerns without another review pool or blanket source reading.

### Selected engineering inputs

The user supplied local Clean Code and Pragmatic Programmer references as conceptual inputs. The local Clean Code skill's metadata identifies author `wondelai`, version `1.4.0`, and license `MIT`. The supplied Pragmatic Programmer file has no license declaration; no additional provenance or license is asserted here. These local inputs are not export dependencies.

The library authors its own bounded adaptations rather than copying those manuals: names and flow that expose intent, meaningful failure contracts, preserved rationale, duplication judged as shared knowledge, explicit invariants, test independence, generated-source ownership, and evidence about coupling and reversal cost. Solution owns approach and commitment comparisons. Maintainability owns the criteria consumed by Architect for design, Implement for assigned edits, and the existing verifier for independent assessment. The [engineering-verification reference](../../skills/aapilot/references/engineering-verification.md) is a first-party procedure for that gate. Fixed cleanliness scores, size quotas, blanket extraction or error-handling policies, speculative abstractions, and unrelated cleanup are not adopted.

The compact-reference PoC uses these additional conceptual inputs, pinned for review:

- Wondel.ai [`refactoring-patterns`](https://github.com/wondelai/skills/blob/c172996495bed0fcd26896a9416b2093fd7073f0/refactoring-patterns/SKILL.md): transformation choices and compatibility hazards inform Implement's first-party refactoring reference.
- Wondel.ai [`clean-architecture`](https://github.com/wondelai/skills/blob/c172996495bed0fcd26896a9416b2093fd7073f0/clean-architecture/SKILL.md), [`software-design-philosophy`](https://github.com/wondelai/skills/blob/c172996495bed0fcd26896a9416b2093fd7073f0/software-design-philosophy/SKILL.md), and Matt Pocock [`codebase-design`](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/codebase-design/SKILL.md): dependency ownership, caller burden, and useful abstraction inform the existing boundary criteria.
- Wondel.ai [`domain-driven-design`](https://github.com/wondelai/skills/blob/c172996495bed0fcd26896a9416b2093fd7073f0/domain-driven-design/SKILL.md): identity, business contexts, and invariant ownership inform Architect's first-party business-state reference. Events, consistency mechanisms, and deployment splits remain decisions derived from the project's accepted rules.
- Wondel.ai [`pragmatic-programmer`](https://github.com/wondelai/skills/blob/c172996495bed0fcd26896a9416b2093fd7073f0/pragmatic-programmer/SKILL.md) provides an identified upstream counterpart for the selected craftsmanship concepts. This is separate from the locally supplied file of undeclared provenance; neither is a runtime dependency.

Selected behavior remains owned and verifiable through the following existing paths. This is a maintainer coverage map, not an additional runtime checklist or a claim to reproduce the full upstream manuals.

| Engineering input | Behavior retained and owning instructions | Verification connection |
| --- | --- | --- |
| Clean Code | [Local-code criteria](../../skills/maintainability/references/local-code.md): intent, focused responsibilities, visible effects, meaningful failures, rationale, and independent test expectations. [Refactoring moves](../../skills/implement/references/refactoring-moves.md): preserve ordering, compatibility, and effects during structural edits. | The same independent verifier assesses relevant changed code; [Refactoring](../../skills/aapilot/playbooks/refactoring.md) retains baseline/equivalence proof. |
| Pragmatic Programmer | Local-code criteria distinguish shared knowledge from coincidental similarity; [boundary criteria](../../skills/maintainability/references/boundaries.md) retain change locality, generated-source ownership, invariants, and concrete reversal cost. [Solution](../../skills/solution/SKILL.md) owns commitments and exit conditions; [Feature](../../skills/aapilot/playbooks/feature.md) owns the first retained integration slice, while [Prototype](../../skills/aapilot/playbooks/prototype.md) owns throwaway experiments. | Check contract-derived outcomes and real integration at the affected surface; accepted rationale and a substitute's pass do not prove production behavior. |
| DDD | [Business-state design](../../skills/architect/references/business-state.md) covers identity/value meaning, context translations, invariant ownership, consistency, competing writers, and recovery. [Domain Modeling](../../skills/domain-modeling/SKILL.md) owns terminology and justified records. | Applicable guarantees and cases travel in the design package; the verifier checks the actual enforcement and affected outcomes, and Maintain Verification reconciles recipe drift. |

These are selected conceptual inputs, not vendored upstream skill bodies or runtime dependencies. Upstream scores, fixed architecture shapes, adapter-count thresholds, and unconditional test deletion are not adopted. The PoC establishes inspectable content and caller wiring; comparative behavioral improvement and cross-host composition require separate evaluation.

### UI review

[Independent rendered UX assessment](../../skills/interaction-design/references/rendered-ux-assessment.md) is a first-party reference under Interaction Design, added for [issue 33](https://github.com/ahmadabdalla/aasystem/issues/33) using the user-agreed two-domain model. It adds no portable skill. Aapilot routes the assessment to Interaction Design; UI Refinement can use it within an assigned refinement slice. Routine design and model reviews retain their existing flow.

The reference owns setup and reconciliation for exactly two fresh nonproducer assessors working in parallel. [Visual composition](../../skills/interaction-design/references/visual-assessment.md) owns the static composition rubric; [Interaction and continuity](../../skills/interaction-design/references/interaction-assessment.md) owns the exercised interaction rubric. Each receives its own instructions, common grounded constraints and explicit domain boundaries, with separate sessions and isolated mutable fixtures. Initial reports remain separate until returned. The caller retains delivery, material decisions and existing human/production-verification gates. Missing required independence or access leaves the affected assessment incomplete.

This shape keeps the rubric with the existing design owner while making assessment separately reachable. It follows the preserve-decision-context principle by carrying accepted constraints and evidence limits into each domain assignment rather than inheriting producer discussion. Explicit routes and domain references are authored behavior; comparative improvement, participant usability and cross-host execution require observed evidence and are not established by this structure alone.

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
- Keep the core rationale short, using one to three sentences where sufficient
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
- A final `At 10x scale` section in the framework default, with equivalent content placed within established project formats

Poteto supplies workflow ideas, not the ADR taxonomy.

The default content and shared author/reviewer contract adapt pstack's [architecture rationale template](https://github.com/cursor/plugins/blob/1dcc2bacde73ddd284803b7af28164d0436198fc/pstack/skills/architect/references/rationale-template.md). ADR convention selection is a local addition; the default requires decision meaning and the compact scale section above.

Accepted decisions constrain work but do not prove the result.

Runtime guidance excludes evaluation-only examples.

### Verification evidence

The [project verification contract](../../skills/bootstrap-verification/references/project-contract.md#evidence-and-retention) owns evidence lifetime.

It separates:

- Durable verification recipes
- Temporary review evidence
- Deliberately retained proof

Local additions include:

- Suitable project facilities with explicit ownership and lifecycle
- Native OS temporary allocation and one owned output root per invocation
- Retention through review or investigation
- Explicit disposal and migration rules
- Source identity for the exercised artifact
- A Git guard for temporary verification output
- Durable proof only for a named future reader

The [Git guard](../../skills/bootstrap-verification/assets/check-verification-output.sh) rejects indexed disposable output when runs live inside a checkout. Bootstrap checks adopted executable harnesses; Maintain reconciles drift. The project contract owns evidence retention and retirement.

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
