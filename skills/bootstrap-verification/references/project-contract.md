# Project verification contract

Use this when adopting or generating a project verifier. New feature maps use the layout below. Preserve an established equivalent layout and avoid parallel sources of truth; it must still carry the required meaning. These are artifact instructions, not mandatory reply headings.

## Operating procedure

The project skill needs a discriminating name and description in YAML frontmatter and concrete instructions for:

- **Scope and launch:** Supported surfaces, prerequisites, exact commands, fixture setup, and the signal that each instance is ready. Use a fresh invocation for short-lived commands; keep server lifecycle explicit.
- **Health and identity:** Confirm the intended instance, current build or source revision, owned port/data location, and required access. Without a Git revision, record a reproducible fingerprint of relevant source and checks. Stop or reset when identity cannot be established.
- **Drive and observe:** Operate the public surface through existing tools or documented helpers. Record actions and resulting state, including persistence or other consequential effects. A simulated dependency only supports a claim about that simulation.
- **Reset and cleanup:** Restore a known fixture state and release owned resources, including after failure. State where evidence survives. Do not stop unrelated processes or remove unrelated data.
- **Completion:** Select recipes by affected behavior, entry points, and dependencies; derive expected results from the contract and apply [scenario coverage](#scenario-coverage) where relevant. Report pass, fail, and unverified outcomes separately. Include an explicit mismatch when checks ran against a different artifact.

Generated instructions use real project paths and commands, with no unfinished placeholders or references to the author's machine. Existing external tooling prerequisites are named and checked. New helper invocations are documented and actually executed.

## Scenario coverage

For scenario-dependent work, map changed semantics and fields, including optional ones, to starting context, real feature actions, contract-derived expectations and relevant persistence, constraint and isolation observations in affected recipes. Seed checks and old test passes cannot replace missing feature proof. Keep scenario references, evidence and gaps in existing project records. Read [Seed scenarios](../../architect/references/seed-scenarios.md) when setup or lifecycle needs design; skip seeding where inapplicable.

Inspect suite selectors, skip conditions and actual local/CI commands. Distinguish a usable procedure, an observed local pass, configured automation and an enforced merge check; prose alone supplies no enforcement.

## Discovery and feature map

Start with a broad survey, then deepen selected paths. Record inspection boundaries and reasons for prioritization; do not label the map exhaustive without evidence. For a new map, use:

```text
verify-<project>/
├── SKILL.md
└── features/
    ├── README.md
    └── <feature>.md
```

`features/README.md` is the single index. Link each feature file and summarize its entry points, recipe coverage, and gaps. Include shared preconditions and driving conventions, or link to their owner in the local verifier. Link durable source references; keep ordinary dated results with the task's review evidence, not in a permanent run history. A documented recipe is not proof of a current pass. The verifier links back to this index and directs readers to the relevant feature files.

Each feature file starts with an H1 and a short description of the actor, intended outcome, and authority for that expectation. Include scheduled or external callers where relevant. Link the requirement, published contract, or recorded user decision; label observed behavior without an independent authority as characterization.

Use agreed project vocabulary and link relevant current ADRs as decision authority. Keep proposed choices conditional and implementation evidence separate from decision acceptance.

For UI scope, link the relevant project interaction model and its requirement coverage. Keep the product's feature/story/journey map with its product owner; this operational feature map describes how to reach and exercise behavior. A deliberate omission from a mock is not removal from the product contract: retain its later proof path or explicit coverage gap. Use the interaction review to question unsupported UI scope; observing a working control does not authorize its existence.

Then use these four H2 sections in order:

| Section | What it must establish |
| --- | --- |
| `Sub-features` | Short stable IDs for observable behaviors, including consequential failure, retry, access, concurrency, or recovery cases. |
| `How to get to it (user POV)` | Every known UI path, command, route, export, or trigger, including alternate entry points. |
| `Driving it with <harness>` | Replace the harness name with the actual tool. Start with `Preconditions:` covering data, access, services, versions, and isolation. Pair each action in the selected scope with exact commands or interactions, independent expected results, and relevant persisted or external effects. Identify any entry points or sub-features without recipes. |
| `Gotchas` | Traps that can invalidate a run, unmet prerequisites, unresolved expectations, and remaining coverage gaps. Refer to shared reset and cleanup instructions where needed. |

See [the authoring example](feature-map-example/README.md) for this shape. Populate generated maps with the project's real contracts and commands; the example is not an application or an additional runtime dependency. All generated links must resolve within the project or its actual dependencies, without the portable toolbox.

Discovery findings identify concrete source locations, dependencies, existing checks, contradictions, and areas left uninspected. Keep reusable findings with the procedure or its existing sources, temporary tracing with task evidence, and feature recipes focused on user-observable behavior. Reconcile new, changed, or removed feature files and entry points with the index as work proceeds. An unchanged ordinary run requires no map edit. A check through one entry point does not prove the others.

## Evidence and retention

Keep maintained instructions, recipes and helpers separate from run output. Prefer a unique OS temporary directory allocated through the runtime's native API, without hard-coded machine paths. One invocation owns the run root and passes it to child checks; keep isolated fixtures and evidence in separate subdirectories. Reuse established project facilities when their ownership and lifecycle satisfy this contract. Name necessary exceptions, such as tool-managed caches or external databases; do not relocate or clean shared resources merely to fit this layout. Reject existing output paths or allocate new ones.

Use the existing checkout or task worktree under the [local execution contract](../../aapilot/references/verification-contract.md#local-execution). Fingerprint complete required inputs, including dirty/new source, checks and ignored configuration; a commit alone is insufficient. Share identity for common inputs without omitting fixture-specific inputs. Do not archive source by default. Extra execution copies need a concrete check requirement, selected inputs, expected storage and owned disposal. Neither copies nor worktrees are security sandboxes. Generated commands work without the plugin.

Reuse harness output instead of duplicating reports. Record the feature/entry point, action, expected result and authority, observation, environment, tested identity and rerun procedure in the existing result owner. Capture only evidence needed for the claim or investigation; avoid whole-workspace inventory and secret contents. Publish/commit proof only for an identified future reader within authority. Durable conclusions must remain understandable without temporary files.

Release owned processes and disposable fixtures on success, failure and graceful cancellation. A pass does not end pending review: retain necessary evidence through review, or investigation/explicit handoff for unresolved failures. Preserve baseline failures and pending changes. Name retained resources, their owner, reason and retirement event in the existing task/review record. Move only necessary proof to an authorized review, CI or project evidence destination when it must survive temporary storage. OS housekeeping is a fallback, not guaranteed cleanup or retention. Abrupt interruption may prevent teardown; report incomplete checks and assess leftovers before reuse or retirement.

Before completion and before disposing of referenced output, run a deterministic project-local check of selected maintained instructions, recipes, configuration and durable local result files for disposable-path references, whether targets still exist or not. Reuse an equivalent check or copy [the reference checker](../assets/check-temporary-references.py) into project tooling. Supply known run/output roots disjoint from selected durable files; its CLI help defines recognized literal paths, relative references and failure codes. Report inspection scope and gaps: lexical matching cannot find computed references or unselected files, and literal examples can also match. Missing/unreadable inputs are incomplete inspection, not a pass. Repair references by retaining necessary proof and linking its durable location, or recording unavailability and limiting the claim. A summary cannot replace required original evidence. Generate runnable scope and repair instructions; execute the check without the plugin.

After retention obligations end, retire only resources whose exact ownership, boundary and lack of active writers are established. Never sweep by prefix or age, follow deletion outside the owned boundary, or remove credentials, shared caches, retained databases or ambiguous resources. Preserve unresolved required evidence; report uncertain ownership instead of claiming cleanup. Inspect owners and inbound links before migrating tracked runs; preserve proof, repair references and review removal. This contract authorizes no bulk deletion.

For temporary output deliberately kept inside Git, ignore its location and reuse a check rejecting indexed files beneath it, including files tracked before the ignore rule. Otherwise copy [the Git guard](../assets/check-verification-output.sh), configure its repository-relative path and execute it. Use an equivalent project runtime if POSIX shell is unavailable. Report offending paths without automatic deletion/untracking; integrate existing checks only within scope.

Match observations to the strength of the claim. Byte-preservation checks compare raw bytes or their hashes and file existence; decoded text can normalize line endings, and parsed values establish only semantic equality. Equal final content alone does not prove that no write occurred. If absence of writes is the contract, observe the relevant write effects as well.

## Readiness

Report both dimensions:

- **Procedure readiness per surface:** usable for named checks; partial with exact gaps; or blocked with a missing prerequisite. Name the sampled path when several features share a procedure.
- **Behavior results:** pass, fail, or unverified for the exercised scope. Planned features and unexercised paths cannot inherit a pass.

A successful sample establishes that procedure's usability. It does not establish other features, alternate paths, integrations, operating conditions, or product-wide quality. A failing behavior can be valid evidence from a working verifier.
