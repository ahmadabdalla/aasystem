---
name: design-judge
description: Audit a design system or UI code for visual consistency (corner radii, spacing, alignment, typography, colour, component dimensions and motion) and report located corrections and token improvements without editing. Owns the default visual standards.
disable-model-invocation: true
---

# Design Judge

Before starting, read the [execution contract](../pilot/references/execution.md) and the [approved-principle index](../principles/INDEX.md), unless already in context.

Audit a project's tokens and UI code against the [visual standards](references/visual-standards.md) and return a report. Change no files.

## Process

### 1. Scope

Take the in-scope sections of the standards and the surfaces from the request. Tokens always applies. If it names none, audit every dimension across the whole design system and say so under Coverage.

If the request is a narrow question, such as a list of values or one check, answer only that, in a table or list, and skip the report template.

### 2. Inventory

Find the styling stack. List every token with its value in each supported theme and the file that defines it. List the shared components and every implementation of each. Read the project's design decisions; they set what counts as [established](references/visual-standards.md#precedence).

### 3. Inspect

Work from widest reach down: token files, shared controls, shared containers (cards, menus, popovers, dialogs), then page-local styles. Resolve each component's effective values through tokens, variants, overrides and themes, and check them against each in-scope section of the standards.

Also search for:

- hard-coded values that bypass a token
- near-duplicate values doing one job, such as 6px, 7px and 8px radii

Source values prove geometry, such as a radius or a contrast ratio. If the app runs with the project's preview steps, start it and check each High finding rendered, in its affected states and themes. Mark any balance or alignment claim you didn't see rendered as **source-only**.

### 4. Alignment (only when in scope and the app can run)

1. Run [capture.mjs](scripts/capture.mjs) (usage in its header) with `--schemes` for every theme and a prep script for each menu, popover and dialog. If a theme doesn't follow `prefers-color-scheme`, switch it in the prep script and check the capture shows it. Install Playwright in `PLAYWRIGHT_DIR`, outside the project. Write captures outside the repository.
2. Give a fresh agent that didn't run the capture the PNG and JSON paths and the [alignment](references/visual-standards.md#alignment) section. It returns one line per miss: `<capture> <miss>: confirmed | rejected: <reason>`. Only if your host has no subagent tool, confirm them yourself.
3. Report each confirmed miss with page, state, pixels off and capture path. A miss marked `xN` repeats down one list: report it once. An `unmeasured` container's edges weren't checked: say so, and still report its listed misses.
4. The scripts measure only edge lines and centring in bars. Check middle columns and sibling panels by eye. Text is measured by line box and icons by element box, so allow for side bearings and viewBox padding. Shadow DOM and iframes are skipped.

### 5. Full-app audits

If the audit covers a runnable app's whole interface, add Interaction Design's [rendered UX assessment](../interaction-design/references/rendered-ux-assessment.md). If you own the user's request, including through Pilot, run it. If a skill handed you part of its task, put it under Next action.

### 6. Report

Start with one paragraph: the overall state and the worst problems. Then list findings, highest priority first:

| Priority | Component | Location | Issue | Current | Recommended |
| --- | --- | --- | --- | --- | --- |
| High | Menu item in dropdown | `path/to/file.css:42` | Corners not concentric with the 12px menu | `12px` | `7px` (12 − 4 padding − 1 border), or a derived token |

- **Priority:** High, Medium or Low, by reach (usage sites) and visibility.
- **Location:** file and line, or token name.
- **Issue:** one sentence, plus the root cause if known (missing token, duplicate component, page override). Mark source-only findings.
- **Recommended:** a specific value or token, with its derivation.

An established value that differs from a default is a finding only when it breaks geometry or accessibility, such as a non-concentric radius, failing contrast or an undersized touch target; name the decision behind it. List every other departure under Informational, with no recommendation.

Then add:

- **Informational**
- **Token proposals:** new, renamed, derived or removed tokens, and the components each affects
- **Themes:** light and dark differences, or "none found"
- **Coverage:** what you inspected, what you didn't, and which checks were rendered
- **Next action:** the fixes to authorize, smallest high-impact change first

## Hand-off

If the user authorizes fixes, send the report to the [Feature playbook](../pilot/playbooks/feature.md). Put navigation and interaction-behaviour problems under Next action for [Interaction Design](../interaction-design/SKILL.md), and business-meaning changes for [Product](../product/SKILL.md).
