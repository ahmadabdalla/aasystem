# How Aapilot works

Aapilot carries a requested outcome from product ideation through design, engineering delivery and verification, stopping at the requested boundary. The human supplies the outcome and authority. One owner keeps the work coherent, brings in domain experts when needed, checks evidence and decides whether the authorized task is complete.

This guide explains that operating model. The [Aapilot entry skill](../../skills/aapilot/SKILL.md) selects routes; the [execution contract](../../skills/aapilot/references/execution.md) owns authority, delegation and completion; [engineering verification](../../skills/aapilot/references/engineering-verification.md) owns the combined independent assessment and executable-check assignment; the [verification contract](../../skills/aapilot/references/verification-contract.md) owns receipts and their detailed protocol.

## One owner, proportional work

The owner carries a retrievable brief: the request, its authority, scope, settled decisions, expected results, evidence obligations and remaining questions. Supporting specialists contribute to that same task. They do not create another coordinator or production run.

The **verification contract** is the shared agreement about what must be shown before completion. A **run** is one owner's bounded task record, including its authority and budget. Its **receipt** connects the request, artifacts, observed checks, limits and acceptance so the result can be inspected.

```text
Human: outcome + authority + required checkpoints
                           |
                  One existing task owner
                           |
             Select route and proof obligation
             /              |                \
     Read / design   Prescribed low-impact   Other retained
     scoped evidence presentation edit      production work
             |              |                |
     Answer / design Owner edits + checks   Owner or specialists
     within scope    zero workers allowed   + separate verifier
             |              |                |
             |              +--------+-------+
             |                       |
             |          One common production receipt
             |                       |
             +----------+------------+
                        |
               Owner inspects result
                        |
              Result + evidence + limits
```

Read-only and design-only work keeps its scoped evidence obligations without production receipts or implementation ceremony. A plan-only request ends with the plan. Retained production changes use the common verification contract through existing entry skills; no special activation phrase is needed.

The narrow [owner-presentation path](../../skills/aapilot/references/execution.md#owner-presentation-eligibility) covers an exact prescribed, low-impact presentation edit inside existing components. Meaning, behavior, data, contracts, permissions, dependencies and deployment must remain unchanged, with required decisions already settled. It cannot waive independent engineering assessment required by the user, project, or task. A short edit can still change business meaning: changing a billing term or consent statement needs the appropriate authority and proof.

The owner records eligibility before editing and checks the actual diff afterward. The receipt keeps specific claims, current artifact identity, actual source/diff observations, an available preview and unexercised limits. This is **owner-checked** proof. It does not establish independence. No worker assignment, verifier preflight or frozen findings packet is required for that path; the root can have zero native workers. Direct [Implement](../../skills/implement/SKILL.md) can own an eligible request through acceptance without an Aapilot wrapper.

Other retained production changes require a fresh verifier separate from every editor. That same worker assesses the actual diff and executes affected project checks. Development checks help the owner or an implementation worker find problems; they do not satisfy that independent gate.

| Example | Appropriate path |
| --- | --- |
| Change an existing label to exact supplied wording, preserving meaning and behavior | Owner-presentation checks, if the full eligibility rule holds |
| Change one word that alters a billing or consent commitment | Settle the consequential choice and use full production proof |
| Add new behavior | Owner or bounded specialists and independent proof, with human checkpoints where required |

## Domain experts contribute bounded results

The selected [playbook](skill-system.md#orchestrator-playbooks) supplies the sequence. Specialists supply expertise within that sequence:

| Responsibility | Owner |
| --- | --- |
| Product behavior, business rules and acceptance scenarios | [Product](../../skills/product/SKILL.md) |
| Overall approach while direction remains open | [Solution](../../skills/solution/SKILL.md) |
| Implementation boundaries, interfaces and proof planning | [Architect](../../skills/architect/SKILL.md), design-only |
| Navigation and interaction structure | [Interaction Design](../../skills/interaction-design/SKILL.md) |
| Inspectable rendered candidate and human review loop | [Prototype](../../skills/prototype/SKILL.md) and [UI Refinement](../../skills/ui-refinement/SKILL.md) |
| Bounded production edits and development checks | [Implement](../../skills/implement/SKILL.md) |
| Reusable criteria and conditional deeper assessment | [Maintainability](../../skills/maintainability/SKILL.md) |
| Bounded scope/structure assessment and executable acceptance observations | One separate verification worker using Maintainability criteria and the project verifier |
| Integration, canonical records and final acceptance | The current task owner |

An assignment names its inputs, deliverable, file ownership, authority, budget and checks. A specialist returns artifacts, observations and limits. New consequential choices or contradictions return to the owner. Accepted project decisions constrain the work; they do not prove that the implementation works. See the complete [ownership map](skill-system.md#ownership-boundaries).

Implement reads the relevant Maintainability criteria while making assigned edits. The independent verifier uses those same criteria for its assessment. This shares one criteria owner without adding a mandatory Maintainability worker or another specialist chain; a deeper specialist assessment remains conditional on its ability to change a decision.

## The owner and native workers do the work; the CLI records it

The owner applies procedures directly or uses the host's actual delegation tools for bounded assignments. Skill responsibilities remain distinct in either execution structure. The shipped [receipt CLI](../../skills/aapilot/scripts/work_receipts.py) records and checks the declared run. It does not launch workers or grant host permissions.

```text
                         ONE ROOT OWNER / RUN
                                  |
                  Brief + authority + decision review
                                  |
                  Owner execution, or reserve -> dispatch -> receipt
                                  |
                   Relevant domain / Implement procedure
                                  |
                  Returned artifact + development checks
                                  |
            +-> Fresh verifier: criteria + frozen inputs + recipes
            |                     |
            |    Original findings + executable evidence
            |           /                    \
            |   fail / unverified        current passing proof
            |          |                      |
            | Owner diagnoses gap      Owner inspects combined
            |          |               artifact + required gates
            | Fresh bounded repair             |
            |          |                 Explicit acceptance
            +----------+
```

The owner reserves an attempt before calling the native tool, checks current dispatch eligibility and records the actual request/result. Followups and retries consume the same root budget. A reserved allocation and an observed native call are different facts; an unknown call outcome requires reconciliation before retry.

For independent discovery, the verifier receives requirements, accepted constraints, original artifacts and runnable project recipes without prior conclusions. Its initial findings are preserved before lead assistance. Context exposure is tracked through that first return. A confirmation audit can examine supplied claims, but agreement in an audit does not establish independent discovery. The [review-context rule](../../skills/aapilot/references/execution.md#review-context) owns that distinction.

The verifier inspects the combined diff for authorized scope and concrete structural concerns, then exercises the identified artifact in a separate materialized workspace and inspects relevant effects. Its one report separates qualitative findings from executable pass, fail or unverified observations. It changes neither product code nor expectations. The owner reconciles each material finding through a correction or an explicit evidenced disposition, assigns bounded repairs, and obtains fresh affected assessment and executable proof for the current combined artifact before accepting it. [Engineering verification](../../skills/aapilot/references/engineering-verification.md) owns that procedure.

The CLI validates recorded transitions, declared scope subsets, budget, checkpoint bindings and input/evidence identities. Semantic eligibility, complete scope, real authority, worker isolation and truthful observations still require inspection. It cannot authenticate a human or native call, sandbox host tools, detect every omitted consequential choice or intercept direct tool use.

## Records explain decisions; evidence supports claims

The project owns its requirements, glossary, accepted decisions, feature map and verification recipes. Preserve its existing formats and locations. The receipt links those records and the actual domain artifact instead of imposing one universal document schema.

```text
PROJECT RECORDS                         RUN EVIDENCE
Request + authority --------------------> Root brief
Requirements + accepted decisions ------> Decision review / checkpoints
Domain artifact + verifier + environment -> Input snapshot + identity
Acceptance scenarios -------------------> Specific proof claims
Project verification recipes -----------> Observations + effects + limits
                                                 |
                                      Report + retained evidence
                                                 |
                                      Owner acceptance decision
```

A snapshot records copied inputs and hashes so a report identifies what was exercised. Relevant source, requirements, loaded procedures/helper, verifier/configuration and environment descriptor join that identity. The tested workspace is separate from the protected archive. Relevant dependencies must be included; copying unrelated repository contents does not improve a scoped claim.

Claims describe concrete expected results. Evidence records what was observed through the real UI, CLI, API or library entry point and its relevant side effects. A build, mock or worker summary cannot establish an unexercised boundary. Remote services and deployment instances need their own observations. Hashing an environment descriptor does not prove where a command ran.

The owner declares the required engineering-assessment claim alongside executable claims before editing. Its pass means a bounded review was performed with its scope, material findings and limits disclosed; it does not certify absolute maintainability or prove behavior. Missing, failing or unverified required claims block acceptance, and review completion cannot waive unresolved material findings. Finding dispositions remain part of the owner's acceptance rationale. Receipt validation checks recorded structure and identity; it cannot judge the substance of those dispositions.

The three distinctions below prevent arrival, proof and approval from collapsing into one label:

| Concept | Meaning |
| --- | --- |
| Returned | An artifact/report arrived. It may lack usable proof or contain failures. |
| Current proof | Declared claims have eligible evidence matching the current inputs. Owner-presentation proof remains owner-checked; independent proof has its separate obligations. |
| Accepted | The owner explicitly inspected the result and evidence, reconciled required decisions and resolved the applicable gates. |

The helper derives current proof status when asked; **verified is not a universal persisted lifecycle stage**. Empty claims establish no verification. Passing proof can still await a human checkpoint. Historical acceptance remains inspectable after proof becomes stale and cannot substitute for current integrated proof. The [report/status rules](../../skills/aapilot/references/verification-contract.md#events-and-reports) and [input identity rules](../../skills/aapilot/references/verification-contract.md#input-identity-and-limits) define the exact checks.

## A human checkpoint is an inspectable decision

Routine implementation details proceed within settled authority. An unresolved consequential product or architectural choice, required visual review or authority limit returns to the human. A checkpoint can arise at any stage. A model recommendation or declared assumption cannot supply human agreement.

```text
Owner identifies a decision / required review
                    |
Inspectable package: artifact stage + concrete artifact/evidence
checked/unverified limits + next authorized action + focused question/options
                    |
            HUMAN CHECKPOINT -> PAUSE WHOLE RUN
                    |
          Actual human answer matching that question
                    |
      Record answer/source -> resume within authority
                    |
        Current decision review + fresh current proof
                    |
              Owner may accept
```

The caller-visible handoff contains the essentials itself. A visual decision includes a usable preview or retained rendered views with access instructions and states cleanup ownership for an active preview; a nonvisual decision includes relevant evidence. The owner states the next authorized action, asks the focused question or offers concrete options, then stops the whole process and waits.

Resume records the actual answer and its source against the exact question/package. Matching receipt fields cannot authenticate a person or prove that they viewed the artifact. An ambiguous answer stays pending. Changed questions need a new package and answer. Resume retains consumed budget and invalidates prior proof until rechecked. The [decision-authority rule](../../skills/aapilot/references/execution.md#decision-authority) owns this human handoff.

## Changed inputs and broader effects reopen obligations

Proof is about an identified artifact, not just a commit label. Dirty edits, additions/deletions and changes to relevant requirements, procedures, helper, verifier, environment or retained evidence can stale it. The owner inspects the changed inputs and obtains current affected proof. A newer failed or stale report cannot be bypassed by selecting an older pass.

If an owner-presentation edit reveals broader effects, owner-presentation acceptance stops. The proof obligation can be strengthened to independent even when no dispatch budget remains; strengthening does not authorize more work. Execution continues only within existing authority, immutable resources, remaining budget and current gates. Otherwise the owner returns the limit and required decision to the human and waits.

Every native continuation draws from one nonrefundable root dispatch budget and deadline. Budget declarations do not measure tokens or cost. A pause, retry, repair or new run cannot silently restore consumed budget or expand authority. If changed immutable root identity requires a linked new run, preserve prior history, effects, checkpoints, uncertain effects, deadlines and consumed budget under the [escalation rule](../../skills/aapilot/references/execution.md#owner-presentation-eligibility).

An interruption records intended effects and the last known worker/process. The owner inspects and, when needed, stops actual owned work through native tools. Uncertain effects block unsafe overlapping work and acceptance until reconciled; cancelling an assignment does not erase its required obligations or effects. The receipt does not stop processes itself.

## Keep runtime and project evidence in their own places

The installed library ships portable skills, references, adapters, assets, the thin Python CLI and its private package. Keep the [complete export tree](skill-system.md#export-boundary) together. The helper needs Python 3.10+ and the standard library; repository tests and temporary evaluation artifacts are outside its runtime dependencies.

Run inputs, state, reports, snapshots and evidence belong in the target project's evidence location, outside installed skills/cache. Project verification procedures and feature maps remain durable project records. Temporary review evidence follows the project's retention policy; deliberately retained proof needs an identified future reader and purpose. The [project evidence contract](../../skills/bootstrap-verification/references/project-contract.md#evidence-and-retention) owns those lifetimes.

Missing Python/helper access must be diagnosed and repaired within authority or reported as an unmet validation obligation. Package checks establish package structure. Actual host discovery, supporting-skill composition, native execution, human viewing, remote behavior and session recovery each require their own observations. The owner reports completed, failed and unverified claims within the requested delivery boundary.
