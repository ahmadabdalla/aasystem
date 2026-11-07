---
name: system-in-motion
description: Build a source-grounded animated walkthrough of a software project, connecting business purpose, user experience, backstage work and technology. Invoke this skill directly to get synchronized Experience and Architecture views.
disable-model-invocation: true
---

# System in Motion

Turn a bounded project journey into a standalone offline HTML explanation.
Experience and Architecture share one scene clock, showing the actor's experience,
backstage work and the technology responsible. This is a simulation, not a live app.

Target normal laptop browsers: check 1280×800 and 1440×900 CSS viewports at normal
zoom unless the user supplies different laptop dimensions. Phone/tablet layouts
are outside scope. Keep production systems untouched; do not install dependencies,
run application writes, publish, commit or deploy as part of explaining a project.

## Invocation

Start only when the user directly selects or invokes this skill. Use
`$aasystem:system-in-motion` in Codex or `/aasystem:system-in-motion` in Claude Code.
Standalone installations omit the plugin prefix. Leave invocation to the user
even when they request the walkthrough through Pilot or another coordinator.

## Ground and prepare

Read [grounding](references/grounding.md) to select and evidence the journey,
reuse settled answers and proceed with disclosed safe defaults. Reserve a bounded
`$aasystem:grill-me` handoff for unresolved consequential choices. Read
[verification](references/verification.md) early to establish agent/browser access:
the executor must launch a separate noneditor UI verifier before delivery.
Self-review and automated checks do not replace that gate; missing capability
leaves a draft with independent verification incomplete.

Resolve `<skill>` to this installed directory. Create a unique working directory
using the host's temporary-directory facility, such as Python's
`tempfile.mkdtemp(prefix="system-in-motion-")`; do not hard-code `/tmp`.

Resolve `<output>` to that directory. Put generated references, candidate files,
screenshots, review evidence and helper scripts there. Give subagents the same
run directory and bounded write ownership.

Announce the working location and intended delivery location before building.
Default delivery to a unique folder under `~/system-in-motion/`, outside the
repository, unless the user chooses another location. Do not add repository
folders, ignore rules or configuration as a side effect.

Build the synthetic reference in the working directory, then open both views
before authoring:

```sh
python3 <skill>/scripts/build.py <skill>/examples/service-request.json --output <output>/reference.html
```

The [fictional source](examples/reference-project.md) grounds this reference only.
Preserve the [presentation contract](references/presentation.md), while adapting
content, theme and topology to the project. The reference demonstrates composition;
it does not certify its wiring or supply facts about another system.

## Author and build

Read the [model contract](references/model-contract.md) while authoring the shared
JSON model. Follow [diagram readability](references/diagram-readability.md) before
placing nodes or routing edges. Use the project's real interaction surface and
causal/observation boundaries; do not invent a dashboard for an API or CLI.

```sh
python3 <skill>/scripts/build.py MODEL.json --validate-only
python3 <skill>/scripts/build.py MODEL.json --output <output>/walkthrough.html
```

The builder uses Python's standard library; the HTML needs no server or network.
When the supplied renderer cannot communicate the journey clearly, copy
`assets/viewer.html` into the output workspace and adapt it using `--template
CUSTOM.html`. Preserve the model, presentation and shared-clock contracts. Correct
the output's layout/template, not the installed skill, during ordinary execution.

## Verify and deliver

Self-check the actual export, then launch the UI verifier and resolve material
findings under [verification](references/verification.md). The optional helper uses
an already installed Playwright:

```sh
node <skill>/scripts/check-browser.cjs OUTPUT.html --screenshots SCREENSHOT_DIR
```

Deliver the HTML, editable model and any custom template needed to rebuild it.
Follow [delivery and cleanup](references/verification.md#delivery-and-cleanup)
to preserve the finished package and offer removal of temporary working files.
Name the journey, evidence/uncertainty, reviewer, checked states, corrections and
remaining gaps. Local builds and agent review do not establish host discovery,
production health or human acceptance. Other design/browser skills are optional;
this package requires no proprietary plugin.
