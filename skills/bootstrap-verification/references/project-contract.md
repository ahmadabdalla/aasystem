# Project verification contract

Use this when adopting or generating a project verifier. New feature maps use the layout below. Preserve an established equivalent layout and avoid parallel sources of truth; it must still carry the required meaning. These are artifact instructions, not mandatory reply headings.

## Operating procedure

The project skill needs a discriminating name and description in YAML frontmatter and concrete instructions for:

- **Scope and launch:** Supported surfaces, prerequisites, exact commands, fixture setup, and the signal that each instance is ready. Use a fresh invocation for short-lived commands; keep server lifecycle explicit.
- **Health and identity:** Confirm the intended instance, current build or source revision, owned port/data location, and required access. Without a Git revision, record a reproducible fingerprint of relevant source and checks. Stop or reset when identity cannot be established.
- **Drive and observe:** Operate the public surface through existing tools or documented helpers. Record actions and resulting state, including persistence or other consequential effects. A simulated dependency only supports a claim about that simulation.
- **Reset and cleanup:** Restore a known fixture state and release owned resources, including after failure. State where evidence survives. Do not stop unrelated processes or remove unrelated data.
- **Completion:** Select recipes by affected behavior, entry points, and dependencies; derive expected results from the contract. Report pass, fail, and unverified outcomes separately. Include an explicit mismatch when checks ran against a different artifact.

Generated instructions use real project paths and commands, with no unfinished placeholders or references to the author's machine. Existing external tooling prerequisites are named and checked. New helper invocations are documented and actually executed.

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

Keep maintained instructions, feature recipes and necessary helpers separate from run output. Use the project's existing scratch or artifact location. Otherwise use unique run directories under ignored `.verification/runs/`, outside the reusable verifier. Helpers must reject an existing output path or choose a new one. Preserve baseline failures and earlier evidence needed for the current review or investigation.

For temporary output inside a Git checkout, ignore the run location and provide a project-owned check that fails when Git's index contains files beneath it, including files tracked before the ignore rule. Bound detection to designated temporary-output paths; deliberately retained proof belongs in the project's durable evidence destination, with its purpose in the owning review or record. Report offending paths without deleting or untracking files automatically.

Reuse an equivalent repository check. Otherwise copy [the Git guard](../assets/check-verification-output.sh) into project-owned tooling and set `temporary_runs` to the project's repository-relative run directory. It uses Git and a POSIX shell; use the project's existing runtime for an equivalent check if that shell is unavailable. Document and execute the local invocation before delivery; integrate with existing checks only within scope.

Each result identifies feature and entry point, action/command, expected result and its authority, actual observation, relevant environment, tested artifact identity, and evidence location. Keep enough to rerun the check without this conversation.

Identify the build or source actually exercised. A Git revision alone is insufficient when relevant changes are uncommitted; use the project's existing identity check or fingerprint the relevant inputs. When recording repository status or diffs, scope them to those inputs.

Capture output needed to establish the claim. Collect additional diagnostics for a specific investigation, without default whole-workspace inventory. Reuse existing harness output instead of creating another report.

Cleanup releases owned processes and fixture state, including after failure. It does not dispose of evidence. Confirm proof remains accessible after teardown. Ordinary evidence stays available through the task's review; unresolved failures through investigation or an explicit handoff that transfers access and retention responsibility. At delivery, report the evidence location and retention boundary. After that boundary, the task owner may dispose of the run's temporary output.

Publish or commit selected evidence only when an identified future reader needs an auditable trail. Use an existing review, CI or project evidence location. Durable records explain the conclusion, scope, limitations and rerun procedure without depending on temporary files. Before disposal, resolve durable references by retaining necessary proof or explicitly recording its unavailability; a summary is not a substitute where the retained claim requires the original evidence.

For existing tracked runs, inspect their owners and inbound links before proposing migration. Preserve required proof, repair references and review the migration before removal. An ignore rule does not untrack existing files; this lifecycle does not authorize bulk deletion.

Match observations to the strength of the claim. Byte-preservation checks compare raw bytes or their hashes and file existence; decoded text can normalize line endings, and parsed values establish only semantic equality. Equal final content alone does not prove that no write occurred. If absence of writes is the contract, observe the relevant write effects as well.

## Readiness

Report both dimensions:

- **Procedure readiness per surface:** usable for named checks; partial with exact gaps; or blocked with a missing prerequisite. Name the sampled path when several features share a procedure.
- **Behavior results:** pass, fail, or unverified for the exercised scope. Planned features and unexercised paths cannot inherit a pass.

A successful sample establishes that procedure's usability. It does not establish other features, alternate paths, integrations, operating conditions, or product-wide quality. A failing behavior can be valid evidence from a working verifier.
