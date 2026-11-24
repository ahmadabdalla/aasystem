# Skill system

This file records the library's structure, who owns what, where each skill came from, and what we changed on purpose. Maintenance rules live in [`AGENTS.md`](../../AGENTS.md) and Codex settings in [`docs/ops/codex.md`](../ops/codex.md).

- **Operating design:** [How Pilot works](verification-contract.md)
- **Visual map:** [Ahmad Abdalla's Pilot System Graph](../../visualizations/skill-library/index.html)

## System flow

`pilot -> playbook -> supporting skills -> project evidence`

1. [`pilot`](../../skills/pilot/SKILL.md) coordinates the task and decides when it's done.
2. A playbook sets the sequence.
3. Supporting skills return bounded results to their caller.
4. The caller updates the project's records.
5. Project verification supplies what was observed.

Pilot and its supporting skills use the [execution contract](../../skills/pilot/references/execution.md), the [principle index](../../skills/principles/INDEX.md), the project's instructions and the task brief. [System in Motion](../../skills/system-in-motion/SKILL.md) is a separate direct entry point with its own source, presentation and verification contracts.

## Ownership boundaries

Each skill's role is in the [inventory](#skill-inventory). These parts aren't skills:

- **Task continuity reference:** the durable brief, increments, recovery and task-wide reconciliation.
- **Optional Codex adapter:** local state per session and directory, restored context and recorded completion checks. It doesn't choose the route or judge the result.
- **Playbooks:** the sequence for each kind of task; Feature owns authorized production delivery.
- **Project verifier:** the project's own procedure and checks.
- **Independent verification agent:** a worker separate from everyone who produced the work. It assesses with Maintainability's criteria, runs the project's checks, and returns findings and observations separately.
- **Caller:** phase changes and updates to project records.

Supporting skills don't gain production scope from an assignment. Project records must stay usable without this library.

## Project-owned records

Projects own their verification procedures, feature maps, glossaries, and product, design and software decisions. New feature maps live in the project verifier as `features/README.md` plus linked feature files, unless an equivalent layout exists. OpenSpec projects follow the [integration reference](../../skills/pilot/references/openspec.md).

## Skill inventory

Each row names the skill’s role, source, and local adaptation.

| Skill | Role | Source | Local adaptation |
| --- | --- | --- | --- |
| [`pilot`](../../skills/pilot/SKILL.md) | Coordinate and finish tasks | pstack [`poteto-mode`](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/SKILL.md) | Uses host tools; needs no custom agent setup |
| [`system-in-motion`](../../skills/system-in-motion/SKILL.md) | Flagship walkthrough of a source-grounded product journey | First-party skill developed in isolation | Direct entry routes technical or business-workflow requests to two synchronized views; shared validated model, playback, offline HTML and independent UI review |
| [`product`](../../skills/product/SKILL.md) | Define journeys and behavior | First-party split; [OpenSpec](https://github.com/Fission-AI/OpenSpec/blob/main/docs/concepts.md) | Owns discovery synthesis and separates facts, proposals, and agreements |
| [`solution`](../../skills/solution/SKILL.md) | Choose the overall approach | pstack [`investigation`](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/investigation.md); [selected engineering inputs](#selected-engineering-inputs) | Compares viable existing and simpler approaches, exposes consequential assumptions, and records demonstrated reversal costs and reconsideration conditions |
| [`architect`](../../skills/architect/SKILL.md) | Shape implementation boundaries | pstack [`architect`](https://github.com/cursor/plugins/blob/main/pstack/skills/architect/SKILL.md); [selected engineering inputs](#selected-engineering-inputs) | Applies Maintainability criteria and justifies added structure against present callers, invariants, and change burden; returns a design package and proof plan while the caller retains implementation and acceptance |
| [`10x`](../../skills/10x/SKILL.md) | Assess decisions under plausible growth | First-party; user-requested | Returns scenarios, first constraints, accommodate/defer tradeoffs, proof needs and reconsideration triggers to domain callers |
| [`implement`](../../skills/implement/SKILL.md) | Execute bounded edits and development checks | First-party extraction from the library’s implementation workflows and [execution contract](../../skills/pilot/references/execution.md); [selected engineering inputs](#selected-engineering-inputs) | Applies relevant Maintainability criteria and conditional refactoring moves within settled scope, returns edits and development evidence, and returns design contradictions to the caller; final acceptance remains with the owner |
| [`maintainability`](../../skills/maintainability/SKILL.md) | Assess reader effort, local change, and ease of verification | pstack [`Minimize Reader Load`](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-minimize-reader-load/SKILL.md) and [`Architect red flags`](https://github.com/cursor/plugins/blob/main/pstack/skills/architect/references/design-red-flags.md); Matt Pocock [`codebase-design`](https://github.com/mattpocock/skills/blob/main/skills/engineering/codebase-design/SKILL.md) and [`code-review`](https://github.com/mattpocock/skills/blob/main/skills/engineering/code-review/SKILL.md); [selected engineering inputs](#selected-engineering-inputs) | Owns reusable criteria in [`SKILL.md`](../../skills/maintainability/SKILL.md), [`local code`](../../skills/maintainability/references/local-code.md), and [`boundaries`](../../skills/maintainability/references/boundaries.md), consumed directly by design, implementation, and independent verification |
| [`interaction-design`](../../skills/interaction-design/SKILL.md) | Design consequential interactions | pstack [`Experience First`](https://github.com/cursor/plugins/blob/9f451cf875ad1239912762f67741e8e5ba6ac0f1/pstack/skills/principle-experience-first/SKILL.md), [`Exhaust the Design Space`](https://github.com/cursor/plugins/blob/9f451cf875ad1239912762f67741e8e5ba6ac0f1/pstack/skills/principle-exhaust-the-design-space/SKILL.md), Matt Pocock [`wayfinder`](https://github.com/mattpocock/skills/blob/6fd947921b935b7e1e69293a200400f0fdd5c15f/skills/engineering/wayfinder/SKILL.md) | Keeps product meaning and implementation architecture with their owners |
| [`ui-refinement`](../../skills/ui-refinement/SKILL.md) | Refine a rendered experience | First-party founder requirement | Returns a reviewed reference; the caller retains delivery |
| [`design-judge`](../../skills/design-judge/SKILL.md) | Audit visual consistency and own default visual standards | First-party; user-stated corner-radius audit and UI/UX standards; alignment method adapted from the [`gridlines`](https://github.com/pritamux/gridlines) skill | Owns the default [visual standards](../../skills/design-judge/references/visual-standards.md) and a report-only audit; project tokens take precedence |
| [`prototype`](../../skills/prototype/SKILL.md) | Build an inspectable experiment | Matt Pocock [`prototype`](https://github.com/mattpocock/skills/blob/6fd947921b935b7e1e69293a200400f0fdd5c15f/skills/engineering/prototype/SKILL.md) | Uses isolated artifacts; excludes automatic production promotion |
| [`how`](../../skills/how/SKILL.md) | Trace current behavior | pstack [`how`](https://github.com/cursor/plugins/blob/main/pstack/skills/how/SKILL.md) | Names each untraced step as a gap |
| [`why`](../../skills/why/SKILL.md) | Reconstruct prior rationale | pstack [`why`](https://github.com/cursor/plugins/blob/main/pstack/skills/why/SKILL.md) | Checks several evidence sources and reports access gaps |
| [`explain-visually`](../../skills/explain-visually/SKILL.md) | Explain flows, responsibilities, and changes with plain-text diagrams | First-party; [issue 62](https://github.com/ahmadabdalla/aasystem/issues/62) and agreed user scope | Matches layout to the question, writes plainly, and keeps sources and limits; Investigation finds missing facts |
| [`probe`](../../skills/probe/SKILL.md) | Test an important assumption | pstack [`prototype`](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/prototype.md) | Separates empirical questions from artifact prototyping |
| [`arena`](../../skills/arena/SKILL.md) | Compare competing options | pstack [`arena`](https://github.com/cursor/plugins/blob/main/pstack/skills/arena/SKILL.md) | Uses an independent judge when available |
| [`interrogate`](../../skills/interrogate/SKILL.md) | Find consequential weaknesses and assess PR merge risk | pstack [`interrogate`](https://github.com/cursor/plugins/blob/main/pstack/skills/interrogate/SKILL.md); Warp [`merge-risk`](https://github.com/warpdotdev/common-skills/blob/8792394ff1b655e0af451b8fabb68ef0cfcbd208/.agents/skills/merge-risk/SKILL.md) | Challenges framing, selects review inputs through the shared context rule, and owns the conditional [merge-risk criteria](../../skills/interrogate/references/merge-risk.md) |
| [`grill-me`](../../skills/grill-me/SKILL.md) | Interview in decision rounds or conduct product discovery | Matt Pocock [`grilling`](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/productivity/grilling/SKILL.md) and [`grill-with-docs`](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/grill-with-docs/SKILL.md) | Keeps question rounds in its entry and discovery in one reference; reuses Domain Modeling for scoped inline capture; Product retains discovery synthesis |
| [`domain-modeling`](../../skills/domain-modeling/SKILL.md) | Define terms and record decisions | Matt Pocock [`domain-modeling`](https://github.com/mattpocock/skills/blob/b0618bc436ad893b3c5e84e55fba86586d34a404/skills/engineering/domain-modeling/SKILL.md) | Adds ownership, evidence, layout, and supersession rules |
| [`tdd`](../../skills/tdd/SKILL.md) | Prove a regression before a fix | pstack [`tdd`](https://github.com/cursor/plugins/blob/main/pstack/skills/tdd/SKILL.md) | Adds practical test limits and repeats the original check |
| [`prune-tests`](../../skills/prune-tests/SKILL.md) | Remove tests that guard no behavior | User-supplied standalone skill; source to be confirmed | Keeps contract-required absences and tests at different entry points, prunes only passing tests, and proves coverage for each deletion |
| [`swarm`](../../skills/swarm/SKILL.md) | Coordinate parallel work | pstack [`swarm`](https://github.com/cursor/plugins/blob/main/pstack/skills/swarm/SKILL.md) | Uses available models; missing results remain unfinished |
| [`figure-it-out`](../../skills/figure-it-out/SKILL.md) | Create a task-specific workflow | pstack [`figure-it-out`](https://github.com/cursor/plugins/blob/main/pstack/skills/figure-it-out/SKILL.md) | Preserves plan-only requests and adds explicit checks |
| [`show-me-your-work`](../../skills/show-me-your-work/SKILL.md) | Keep a decision log | pstack [`show-me-your-work`](https://github.com/cursor/plugins/blob/main/pstack/skills/show-me-your-work/SKILL.md) | Saves locally and reports missing review material |
| [`reflect`](../../skills/reflect/SKILL.md) | Turn session findings into edits | pstack [`reflect`](https://github.com/cursor/plugins/blob/df581122cde17e6e27686b5a448bde23e4ad4318/pstack/skills/reflect/SKILL.md) | Adapts transcript access, reviewers, approval, and host tools |
| [`bootstrap-verification`](../../skills/bootstrap-verification/SKILL.md) | Create project verification | pstack [`create-verification-skill`](https://github.com/cursor/plugins/blob/main/pstack/skills/create-verification-skill/SKILL.md) | Writes project-owned checks and a feature map |
| [`maintain-verification`](../../skills/maintain-verification/SKILL.md) | Maintain project verification | pstack [`maintain-verification-skill`](https://github.com/cursor/plugins/blob/main/pstack/skills/maintain-verification-skill/SKILL.md) | Separates product defects from verifier drift |
| [`principle-preserve-decision-context`](../../skills/principle-preserve-decision-context/SKILL.md) | Preserve decision inputs | User-approved judgment | Removes repetition only when the next decision stays informed |
| [`principle-deliver-and-prove`](../../skills/principle-deliver-and-prove/SKILL.md) | Establish implementation readiness | User-stated and approved judgment | Applies two delivery/proof questions at Implement's entry, reusing project verification and the existing task brief |
| [`principle-ui-meaning-through-structure`](../../skills/principle-ui-meaning-through-structure/SKILL.md) | Express UI meaning through structure | User-approved judgment | Retains text needed for safety, limits, or decisions |

## Orchestrator playbooks

The pilot skill selects one of these sequences:

| Playbook | Purpose |
| --- | --- |
| [`investigation`](../../skills/pilot/playbooks/investigation.md) | Answer a question with evidence |
| [`bug-fix`](../../skills/pilot/playbooks/bug-fix.md) | Reproduce, diagnose, fix, and recheck |
| [`feature`](../../skills/pilot/playbooks/feature.md) | Design, build, and verify a feature |
| [`refactoring`](../../skills/pilot/playbooks/refactoring.md) | Change structure without changing behavior |
| [`prototype`](../../skills/pilot/playbooks/prototype.md) | Coordinate a bounded experiment |
| [`authoring-a-skill`](../../skills/pilot/playbooks/authoring-a-skill.md) | Create or update a skill |
| [`eval`](../../skills/pilot/playbooks/eval.md) | Run fresh candidates against separate criteria |
| [`opening-a-pr`](../../skills/pilot/playbooks/opening-a-pr.md) | Prepare, publish, and confirm a pull request |

The playbooks follow [pstack’s playbook set](https://github.com/cursor/plugins/tree/main/pstack/skills/poteto-mode/playbooks).

## Deliberate system adaptations

Each section records a decision and its source. The linked file owns the rule.

### Entry-point rename

The entry skill is `pilot`, in `skills/pilot/` with its playbooks, contracts, scripts and optional adapter. Only the name and path changed: routes, ownership, proof, invocation policies and the `aasystem` plugin identity are the same. There's no `aapilot` alias. The Codex adapter answers to `$aasystem:pilot` and `$pilot`, and its version 2 state format is unchanged. The [upgrade procedure](../ops/releasing.md#upgrade-from-aapilot-to-pilot) owns migration.

### Coordination

The first-party [effort rubric](../../skills/pilot/references/effort.md) owns S, M and L sizing. The [execution contract](../../skills/pilot/references/execution.md) is short because every skill reads it. Rules only some tasks need live in files it links: [Delegation](../../skills/pilot/references/delegation.md) for handoffs, invocation restrictions and review context; the [verification contract](../../skills/pilot/references/verification-contract.md) for behaviour changes, with [local execution](../../skills/pilot/references/local-execution.md) for worktrees, copies, cleanup and input fingerprints; and [task continuity](../../skills/pilot/references/task-continuity.md#bounded-autonomy) for unattended work. Agents read whole files, so a separate file, not a section pointer, keeps those rules out of tasks that don't need them.

The [skill authoring playbook](../../skills/pilot/playbooks/authoring-a-skill.md) owns how specific an instruction must be, deduplication, and when to split a skill or add a reference. Specialists keep only scope reminders they act on.

### Grilling and documentation

Pilot and direct requests use the same [Grill Me entry](../../skills/grill-me/SKILL.md), which owns the question rounds. [Product-discovery interviews](../../skills/grill-me/references/discovery-interview.md) load their own reference and return attributed evidence to Product. Grill Me records settled terms and decisions through Domain Modeling; "with docs" uses the same path.

### Design, implementation and verification

- [Architect](../../skills/architect/SKILL.md) designs only. A design-and-build request needs a playbook to own the build.
- [Implement](../../skills/implement/SKILL.md) is shared by Feature, Bug Fix, Refactoring and Figure It Out. The caller supplies the design, file ownership and checks.
- The [verification contract](../../skills/pilot/references/verification-contract.md) owns when a separate verifier runs and the narrow [owner-presentation exception](../../skills/pilot/references/verification-contract.md#owner-presentation-eligibility). [Engineering Verification](../../skills/pilot/references/engineering-verification.md) is that verifier's brief. The verifier is an agent role, not another skill or review pool.
- The optional [input_identity.py](../../skills/pilot/scripts/input_identity.py) fingerprints and compares inputs read-only (Python 3.10+ and Git) when the project has nothing suitable. It creates no copies.
- Architect's [seed scenario reference](../../skills/architect/references/seed-scenarios.md) is conditional, read by Feature when proof depends on state, so seed data needs no separate skill.

None of these mechanisms authenticates who acted or controls every host tool.

### Signal effects

The [execution contract](../../skills/pilot/references/execution.md#signal-effects) owns the signal account for a change. Interrogate's [signal assessment](../../skills/interrogate/references/signal-assessment.md) traces detection, and How traces current signal paths. Neither adds a skill. Source: [issue 66](https://github.com/ahmadabdalla/aasystem/issues/66).

### Merge-risk review

Interrogate's [Merge risk](../../skills/interrogate/references/merge-risk.md) reference keeps the instructional body of Warp's [`merge-risk`](https://github.com/warpdotdev/common-skills/blob/8792394ff1b655e0af451b8fabb68ef0cfcbd208/.agents/skills/merge-risk/SKILL.md) verbatim at commit `8792394ff1b655e0af451b8fabb68ef0cfcbd208`, with only the frontmatter removed and a heading added. Upstream credits Matt Pocock's PR skill. The Matt Pocock notice and the [Warp MIT notice](../../WARP_LICENSE.txt), copyright Denver Technologies, Inc., travel with the export. The earlier local rewrite and its scoring definitions are gone.

Interrogate reads it for PR merge-readiness, or when recovery or failure detection could change a review verdict. [Opening a PR](../../skills/pilot/playbooks/opening-a-pr.md) carries the result into the reviewer brief. A low or medium rating doesn't close missing checks or authorize a merge.

### Growth assessment

[10x](../../skills/10x/SKILL.md) is one reusable assessment. Solution, Architect and Interaction Design apply it before settling a consequential design, and Pilot routes standalone requests to it. Deferred targets don't become release requirements.

### Maintainability

[Maintainability](../../skills/maintainability/SKILL.md) owns the criteria that used to live in Architect: its `SKILL.md`, [local code](../../skills/maintainability/references/local-code.md) and [boundaries](../../skills/maintainability/references/boundaries.md). Architect, Implement and the verifier read them directly, without invoking Maintainability. A full assessment runs only when its findings could change a design, refactoring or review verdict, or when Pilot routes an explicit request. The [module design review](../../skills/maintainability/references/module-design-review.md) adapts the user's proposal.

Two conditional references follow the same pattern: Implement reads [Refactoring moves](../../skills/implement/references/refactoring-moves.md) for structural edits, and Architect reads [Business state](../../skills/architect/references/business-state.md) when identity, state ownership, invariants or cross-context coordination change. Each of the three references stays under 80 lines. The [design package](../../skills/architect/references/design-package.md) carries guarantees and required cases to the verifier, so one verifier covers these concerns.

### Test pruning

[Prune Tests](../../skills/prune-tests/SKILL.md) owns test cleanup. Maintainability's [verification clarity](../../skills/maintainability/references/local-code.md) defines a needed test. Pilot routes "which tests are useless?" to Maintainability and "prune them" to Refactoring. Implement, Maintain Verification and the verifier never prune tests nobody asked to prune.

### Selected engineering inputs

The user supplied local Clean Code and Pragmatic Programmer references as conceptual inputs. The Clean Code skill's metadata names author `wondelai`, version `1.4.0` and license `MIT`. The Pragmatic Programmer file declares no license, and none is asserted here. Neither is an export dependency.

These pinned sources informed bounded first-party references, not copied text:

- Wondel.ai [`refactoring-patterns`](https://github.com/wondelai/skills/blob/c172996495bed0fcd26896a9416b2093fd7073f0/refactoring-patterns/SKILL.md): Implement's refactoring moves.
- Wondel.ai [`clean-architecture`](https://github.com/wondelai/skills/blob/c172996495bed0fcd26896a9416b2093fd7073f0/clean-architecture/SKILL.md), [`software-design-philosophy`](https://github.com/wondelai/skills/blob/c172996495bed0fcd26896a9416b2093fd7073f0/software-design-philosophy/SKILL.md) and Matt Pocock [`codebase-design`](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/codebase-design/SKILL.md): Maintainability's boundary criteria.
- Wondel.ai [`domain-driven-design`](https://github.com/wondelai/skills/blob/c172996495bed0fcd26896a9416b2093fd7073f0/domain-driven-design/SKILL.md): Architect's business-state reference.
- Wondel.ai [`pragmatic-programmer`](https://github.com/wondelai/skills/blob/c172996495bed0fcd26896a9416b2093fd7073f0/pragmatic-programmer/SKILL.md): an identified upstream for the craftsmanship concepts, separate from the local file.

Not adopted: fixed scores, size quotas, blanket extraction or error-handling policies, fixed architecture shapes and adapter-count thresholds. Test deletion comes only through Prune Tests.

### UI review

[Independent rendered UX assessment](../../skills/interaction-design/references/rendered-ux-assessment.md) sits under Interaction Design, for [issue 33](https://github.com/ahmadabdalla/aasystem/issues/33), using the two-domain model the user agreed. Two fresh assessors who didn't build the interface work in parallel: one on [visual composition](../../skills/interaction-design/references/visual-assessment.md), one on [interaction and continuity](../../skills/interaction-design/references/interaction-assessment.md). Keeping the rubric with Interaction Design avoids another skill. [UI Refinement](../../skills/ui-refinement/SKILL.md) can use it within a slice. It isn't a visual-parity claim or required for every UI edit.

### Design standards

[Design Judge](../../skills/design-judge/SKILL.md) is first-party, built from the user's corner-radius audit requirements and UI/UX standards. Its [visual standards](../../skills/design-judge/references/visual-standards.md) are defaults; a project's tokens and decisions take [precedence](../../skills/design-judge/references/visual-standards.md#precedence). The audit reports and stops; fixes go through Feature.

The alignment rules and measurement approach adapt the MIT-licensed [`gridlines`](https://github.com/pritamux/gridlines) skill without copying its code or text; it draws on Karri Saarinen's Linear sidebar redraw and Apple's HIG. The [measurement scripts](../../skills/design-judge/scripts/capture.mjs) are a separate implementation; one vote per table or list, card and list-row edges, single ownership of nested items and right-to-left mirroring are local extensions, not from gridlines. They need Playwright and Chromium, which the library doesn't bundle. [`tests/test_design_judge_capture.py`](../../tests/test_design_judge_capture.py) checks the [fixtures](../../tests/fixtures/design-judge/) at 1440px and 390px when Playwright resolves; CI skips it.

Evaluation: a corner-radius audit of a synthetic fixture found every planted conflict without editing files. Reviewers then probed the scripts with 54 adversarial containers and a local build of a real application at both widths; the misses and false positives they found are fixed and pinned in the fixtures. Known limits: middle columns, stacked bottom tab bars and single-row bars get no edge check; two disagreeing rows derive no line unless one sits on the padding edge; overlay scroll arrows can set an arguable trailing line; table text inset from its heading is reported by design; the app's dark theme wasn't rendered. Discovery, consumer uptake, routing of ambiguous requests, an agent-run rendered audit, and shadow DOM or iframes are unevaluated.

### Decision records

The [ADR convention](../../skills/domain-modeling/references/adr.md) keeps Matt Pocock's rules: a record needs reversal cost, surprising rationale and a real tradeoff; rationale stays short; records are created lazily and numbered in sequence. Local additions: project layouts, one decision per record, cross-links, explicit supersession, project rules before a framework default, and a closing `At 10x scale` section. Poteto supplies workflow ideas, not the ADR taxonomy. The default content adapts pstack's [rationale template](https://github.com/cursor/plugins/blob/1dcc2bacde73ddd284803b7af28164d0436198fc/pstack/skills/architect/references/rationale-template.md). Accepted decisions constrain work but don't prove the result.

### Verification evidence

The [project verification contract](../../skills/bootstrap-verification/references/project-contract.md#evidence-and-retention) owns evidence lifetime: durable recipes, temporary review evidence and proof kept for a named reader. The [Git guard](../../skills/bootstrap-verification/assets/check-verification-output.sh) rejects disposable output staged inside a checkout. Sources: pstack [`create-verification-skill`](https://github.com/cursor/plugins/blob/df581122cde17e6e27686b5a448bde23e4ad4318/pstack/skills/create-verification-skill/SKILL.md), [`maintain-verification-skill`](https://github.com/cursor/plugins/blob/df581122cde17e6e27686b5a448bde23e4ad4318/pstack/skills/maintain-verification-skill/SKILL.md), [`Prove It Works`](https://github.com/cursor/plugins/blob/df581122cde17e6e27686b5a448bde23e4ad4318/pstack/skills/principle-prove-it-works/SKILL.md), [`Show Me Your Work`](https://github.com/cursor/plugins/blob/df581122cde17e6e27686b5a448bde23e4ad4318/pstack/skills/show-me-your-work/SKILL.md) and [`Encode Lessons in Structure`](https://github.com/cursor/plugins/blob/df581122cde17e6e27686b5a448bde23e4ad4318/pstack/skills/principle-encode-lessons-in-structure/SKILL.md).

## Supporting sources

- **Technology discovery:** [`tech-interviewer`](https://github.com/ahmadabdalla/tech-interviewer)
- **Context control:** pstack [`Guard the Context Window`](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-guard-the-context-window/SKILL.md)
- **Worker baseline:** pstack [`poteto-agent`](https://github.com/cursor/plugins/blob/main/pstack/agents/poteto-agent.md)
- **Learning:** pstack [`Automate me`](https://github.com/cursor/plugins/blob/main/pstack/skills/automate-me/SKILL.md)
- **Feature maps:** pstack [`feature-map example`](https://github.com/cursor/plugins/blob/main/pstack/skills/create-verification-skill/references/feature-map-example/README.md)
- **Specification workflow:** OpenSpec [`CLI`](https://github.com/Fission-AI/OpenSpec/blob/main/docs/cli.md) and [`workflows`](https://github.com/Fission-AI/OpenSpec/blob/main/docs/workflows.md)

## Evaluation

### Durable orchestration

- Delivery-judgment rules in the execution contract and Engineering Verification address [issue 51](https://github.com/ahmadabdalla/aasystem/issues/51).
- The [verification working loop](../../skills/pilot/references/verification-contract.md#working-loop) sets acceptance scope, correction classes and when to stop churning, informed by [UpNow issue 16](https://github.com/ahmadabdalla/UpNow/issues/16). These are instructions, not host-enforced budgets or measured speedups.
- [Task continuity](../../skills/pilot/references/task-continuity.md) addresses [issue 49](https://github.com/ahmadabdalla/aasystem/issues/49), extended by the user's agreed requirements for context recovery, scope-aware specialist work and optional local Codex enforcement. It adds no skill. Following [Preserve decision context](../../skills/principle-preserve-decision-context/SKILL.md), a shorter handoff must still carry what the next owner needs.

The optional [Codex adapter](../../skills/pilot/assets/codex/README.md) uses the official [hooks protocol](https://learn.chatgpt.com/docs/hooks): hooks restore a coordinator-owned record and check its obligations at stop, while the coordinator still picks procedures and judges results. It adds no SDK controller, manifest hook registration, tool interception or managed runtime. The [harness adapter boundary](../../skills/pilot/assets/README.md) owns the rules for adding integrations and their [data lifecycle](../../skills/pilot/assets/README.md#consumer-data-lifecycle). Those rules came from a consumer audit of version 1, which kept every prompt and session indefinitely and left stale locks; version 2 binds sessions only until a checked handoff to an existing task file.

Separating state by session and directory lets independent tasks run at once; revision checks stop stale coordinator writes. Several writers, distributed execution and authenticated approval are out of scope. Evidence hashes catch changed files; source-artifact identity stays with the verification contract. Tests and evaluations cover only what they exercised.

Across this file: package validation checks links, metadata and adapters only. None of these structures, and no risk verdict, proves host discovery, cross-host composition, production readiness, participant usability or a comparative improvement; those need observed evaluation.

The [evaluation playbook](../../skills/pilot/playbooks/eval.md) adapts [pstack's Eval](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/eval.md): realistic tasks, blinded candidates and judging, transcript reading and lead reconciliation. The library ships no evaluation runner or standing fixtures.

## Export boundary

Export these files together:

- [`plugin.json`](../../plugin.json)
- [`.claude-plugin/plugin.json`](../../.claude-plugin/plugin.json)
- [`skills/`](../../skills/)
- [`LICENSE`](../../LICENSE)
- [`PSTACK_LICENSE.txt`](../../PSTACK_LICENSE.txt)
- [`MATT_POCOCK_LICENSE.txt`](../../MATT_POCOCK_LICENSE.txt)
- [`WARP_LICENSE.txt`](../../WARP_LICENSE.txt)
- [`docs/design/skill-system.md`](skill-system.md)
- [`README.md`](../../README.md)
- [`docs/ops/codex.md`](../ops/codex.md)

Both manifests package the same skill tree as `aasystem`. The root manifest owns the identity, version and OpenAI presentation metadata; the [release validator](../../scripts/validate-release.py) checks the Claude manifest matches. The Codex hook helper and guide travel inside `skills/pilot/`, and neither manifest registers them: opting in is separate from installing.

The [release process](../ops/releasing.md) adapts Azure Cost Calculator's tag, release and changelog helpers. Merging a reviewed, manually versioned release PR into `main` validates and publishes that exact commit, with safe retries, then opens a separate marketplace adoption PR.
