# Project verification contract

What a project verifier, its feature map and its evidence must contain. If the project already has an equivalent layout, keep it and make it carry the same meaning.

## Operating procedure

The verifier is a project skill whose name and description set it apart from the project's other skills. It says:

- **Launch:** surfaces, prerequisites, exact commands, fixtures and the signal that each instance is ready.
- **Identity:** how to confirm the right instance and build. Fingerprint every input the run uses, including uncommitted files and config; a commit alone isn't enough. If identity can't be established, reset and check again, then stop.
- **Drive and observe:** operate the public surface and record each action and the state it left. A simulated dependency proves only the simulation. If "nothing was written" is the claim, observe the writes.
- **Cleanup:** restore the fixture state, release what the run owns, and say where evidence survives.
- **Completion:** choose recipes by what changed, take expected results from the contract, and report pass, fail and unverified separately.

Everything you generate must work without this toolbox: real project paths and commands, no placeholders, no links back here. Run every helper you add.

## Scenario coverage

If a change adds fields or states, each affected recipe starts from a state that uses them, drives the real feature, and checks what was stored. A seed check or an old passing test isn't feature proof. If setup needs design, read [Seed scenarios](../../architect/references/seed-scenarios.md).

Keep apart a usable procedure, an observed local pass, configured CI and an enforced merge check. Text in a file enforces nothing.

## Discovery and feature map

Record what you inspected. Don't call the map exhaustive without evidence. A new map uses:

```text
verify-<project>/
├── SKILL.md
└── features/
    ├── README.md
    └── <feature>.md
```

`features/README.md` is the only index: one line per feature with its entry points, coverage and gaps. Each feature file opens with the actor, the intended outcome and its authority. If an expectation comes only from observed behaviour, label it characterization. Then four sections, in order:

| Section | Contents |
| --- | --- |
| `Sub-features` | Stable IDs for observable behaviours, including failure and recovery cases that matter. |
| `How to get to it (user POV)` | Every UI path, command, route or trigger. |
| `Driving it with <harness>` | `Preconditions:`, then each action with its exact command and an expected result from the contract, not the code. List entry points with no recipe. |
| `Gotchas` | Traps that can invalidate a run, and unresolved expectations. |

[The authoring example](feature-map-example/README.md) shows this shape. Keep dated results out of the map; a run that changes nothing needs no map edit.

## Evidence and retention

- Each run owns one unique OS temp directory, allocated through the runtime, with fixtures and evidence in subdirectories. Never write into an output path that already exists.
- Record each check's feature, action, expected result and authority, observation, tested identity and rerun command in the harness output.
- Release owned processes and fixtures on success, failure and cancellation. Keep evidence until review ends; OS temp cleanup isn't teardown. Before you finish, move any evidence a review or record needs to the project's evidence location.
- Delete only what the run owns. Never sweep by prefix or age, stop unrelated processes, or remove anything ambiguous; report what you left.
- If output must sit inside a Git checkout, ignore it and add a check that rejects tracked files there. Reuse the project's check, or copy [the Git guard](../assets/check-verification-output.sh). Report offending paths; don't delete them.

## Readiness

Report two things:

- **Procedure readiness, per surface:** usable, partial with the exact gaps, or blocked by a named prerequisite.
- **Behaviour results:** pass, fail or unverified for what you ran. Anything you didn't run can't inherit a pass. A failing result can be valid evidence from a working verifier.
