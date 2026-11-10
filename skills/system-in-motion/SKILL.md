---
name: system-in-motion
description: Build a source-grounded animated walkthrough of one project journey. Invoke directly for synchronized Experience and Architecture views, or a business workflow with responsibility lanes.
disable-model-invocation: true
---

# System in Motion

Turn a bounded project journey into a standalone offline HTML explanation.
Experience shares one scene clock with Architecture or Business map, showing the
actor's experience and the work responsible. This is a simulation, not a live app.

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

Route a directly invoked request by its intended explanation, reusing any settled
journey and endpoint. State the chosen viewpoint; do not ask the user to choose a renderer.

| Request | Profile and opening view | Reference model |
| --- | --- | --- |
| User experience, software behavior, technology or runtime exchanges | Omit `presentation.profile` (technical); Experience opens, Architecture is the toggle | `examples/service-request.json` |
| Business workflow, process or responsibility: who acts, decides and hands work on | `presentation.profile: "business-workflow"`; Business map opens, Experience is the toggle | `examples/business-workflow.json` |

“Business architecture” alone does not expand a bounded journey into enterprise
capability or organization mapping. Use the business profile when the ask concerns
that journey's activities and responsibilities. Preserve software exchanges in the
technical profile and business progression in the business profile.

Read [grounding](references/grounding.md) to establish the source scope, choose
the journey and settle the brief under the shared decision rules. Read
[verification](references/verification.md) early to establish agent/browser access:
the executor must launch a separate noneditor UI verifier before delivery.
Self-review and automated checks do not replace that gate; missing capability
leaves a draft with independent verification incomplete.

Resolve `<skill>` to this installed directory and `<work>` to a unique run
directory from the host's temporary-directory facility, such as Python's
`tempfile.mkdtemp(prefix="system-in-motion-")`. Keep candidates, rebuild inputs
and review evidence there. Give subagents bounded write ownership in that directory.

Resolve and announce the [HTML destination](references/verification.md#delivery-and-cleanup)
before building. For a refinement, [check the previous run](references/verification.md#refinement-state) first.

Build the selected synthetic reference in the working directory, then open both views
before authoring:

```sh
python3 <skill>/scripts/build.py <skill>/examples/service-request.json --output <work>/reference.html
# For the business profile, use examples/business-workflow.json instead.
```

The [technical source](examples/reference-project.md) and
[business source](examples/business-workflow-source.md) ground their references only.
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
python3 <skill>/scripts/build.py MODEL.json --output <work>/walkthrough.html
```

The builder uses Python's standard library; the HTML needs no server or network.
The standard command selects the bundled renderer from the model's profile;
business requests need no custom template. Only when the supplied renderer cannot
communicate the journey clearly, copy
`assets/viewer.html` into the working directory and adapt it using `--template
CUSTOM.html`. Preserve the model, presentation and shared-clock contracts. Correct
the output's layout/template, not the installed skill, during ordinary execution.

## Verify and deliver

Self-check the actual export, then launch the UI verifier and resolve material
findings under [verification](references/verification.md). The optional helper uses
an already installed Playwright:

```sh
node <skill>/scripts/check-browser.cjs OUTPUT.html --screenshots SCREENSHOT_DIR
```

Deliver the verified standalone HTML. Follow
[delivery and cleanup](references/verification.md#delivery-and-cleanup) for
temporary refinement state, optional durable files and the delivery summary.
Other design/browser skills are optional; this package requires no proprietary
plugin.
