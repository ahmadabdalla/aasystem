# Verify the export

Source fidelity, structural validity, playback and visual readability are distinct
claims. A build cannot establish a true story, and geometry checks cannot establish
human understanding.

## Required independent UI verifier

For every ordinary delivery, including revisions, the executor launches at least
one UI verifier separate from all candidate authors. Check agent/browser access
early. Use a fresh context without producer conclusions when supported; disclose
isolation limits. No particular plugin or model is required. Missing delegation
or rendered-browser access leaves a draft with independent UI verification incomplete.

After self-checks, pause edits. Give the verifier:

- Original request, accepted constraints, source locators and exact HTML/model/custom
  template paths, identified by hashes or equivalent snapshot; laptop sizes from SKILL.md.
- This reference, [presentation](presentation.md) and
  [diagram readability](diagram-readability.md), to read and apply.
- Browser access, read-only candidate/source ownership, an evidence destination and
  practical review/correction bound. Withhold prior verdicts, producer pass claims
  and preferred fixes from the initial review.

The verifier opens the actual export and performs the checks below. Return tested
identity, actual viewport/theme/motion/playback states, findings with scene/edge
locations and visual evidence, prose findings with suggested replacements, and unverified scope. Distinguish material failures
from taste. Screenshots alone do not prove playback; code alone does not prove UI.

Preserve original findings. The executor corrects material failures in the owning
model/template, rebuilds, and requests rechecks of affected states and the connected
map. The same reviewer may do a labeled confirmation audit with prior findings.
Identify final files again; do not edit while reviewed or deliver a stale export.
Within the work bound, resolve material findings or report the remaining gap.
The executor retains delivery responsibility; an agent verdict is not human acceptance.

If a confirmation audit finds any new or unresolved material defect, require a
second fresh noneditor reviewer before delivery. The reviewer classifies findings
against the checks below; the executor cannot waive escalation or unilaterally
downgrade a finding. Give the new reviewer the affected scope and current candidate
under the independent handoff above, withholding prior verdicts until their initial
findings return; then reconcile findings and confirm corrections on the final
artifact. Unresolved disagreement or unavailable required review leaves a delivery
gap. Keep the existing work bound.

## Source and model

Run builder validation. Trace important claims to their locators: initiator, state
change, actor observation, responsibility and technology. Preserve planned/inferred/
unknown distinctions. Compare consecutive scenes for each actor, not just selected
screenshots: every newly visible fact needs a response/read/push. Otherwise retain
the last observed state and show backstage facts in a labeled explanation scene.
An API/CLI retains its real surface. Rebuild and inspect after model changes.

## Actual playback and controls

Open the exported HTML locally. The optional `scripts/check-browser.cjs` uses an
installed Playwright; otherwise use an available browser tool/native browser.
It installs nothing and does not replace judgment. If no browser can open the
export, runtime and visual verification remain incomplete.

Exercise early, middle and final scenes plus a meaningful async/decision boundary.
Observe automatic transitions and explicit selection. Pause/resume, Back/Next and
switch views during playback; scene, progress, captions, components, wires and
experience must stay synchronized. Paused time cannot advance or jump on a view
change. Confirm completion and replay/reset. Test seeking if the output offers it.

At the SKILL.md laptop sizes, check supported themes, reduced motion, keyboard
focus/navigation and legible controls/text/uncertainty. Reduced motion may suppress
travel but must retain current scene, direction and meaning. Mobile/tablet is outside scope.

## Visual and causal review

Apply all [diagram trace checks](diagram-readability.md#inspect-and-revise-the-export)
in their stated order at both laptop sizes and all supported themes. That reference
owns route, caption, direction, dependency and affected-route rechecks.

Check the [default palette](presentation.md#default-palette) when no user/project
palette applies: inspect both views on white, including paused active and inactive
paths, captions and badges. Verify a dark system preference does not silently switch
the fallback to dark. Inspect a screenshot at its intended slide placement size;
flag text or wires that disappear when reduced. Do not claim PowerPoint export was
tested unless it was actually exercised.

Apply [plain process language](presentation.md#plain-process-language) to all rendered
copy, including controls and uncertainty notes. Return each actionable finding with
its location, original wording, simpler replacement and meaning to preserve. Use
the shared correction loop, confirming meaning, fit and reading time. Report a prose
review outcome even when no changes are needed; this is not AI-authorship detection.

Review scene boundaries against [story guidance](presentation.md#one-story-one-clock):
flag padding or transport-only fragmentation without prescribing a scene count.

Compare the export with the built reference using
[presentation anchors](presentation.md#compare-the-exported-result) at matching
width/theme/stable scene states. Functional playback does not establish visual parity.

The helper's geometry and playback checks do not replace this review or close an
observed readability failure. For custom templates, verify nonzero selector coverage
of actual node and relationship captions under the diagram reference's measurement rules.

## Delivery and cleanup

After verification, copy the finished package to the announced delivery folder:

- Standalone walkthrough HTML.
- Editable model.
- Custom template and any other local files required to rebuild.
- Concise report linking the deliverables and source evidence, with uncertainty,
  tested identity, reviewer and isolation limits, actual checked states, material
  findings/corrections and remaining gaps. Distinguish automated checks from visual
  observations; do not infer general reliability, host discovery, production health
  or human acceptance.

Use a new destination; do not overwrite existing files. Confirm the delivered
HTML opens, matches the reviewed artifact, and the retained sources can rebuild
it. Do not change reviewed content during packaging. Working-directory paths must
not be required to open or rebuild the delivered result.

Show the delivery location and offer cleanup through the host's question tool.
If unavailable, ask in the conversation:

"The walkthrough is ready at [location]. What would you like to keep?"

- Editable package — recommended: keep the finished package and remove temporary
  working files.
- Everything: keep the finished package and preserve the working files and
  detailed evidence in a clearly named supporting folder at the delivery location.
  Verify the copies, then remove the run-owned temporary originals; include this
  removal in the offered choice. Preserve unresolved evidence as required below.
- HTML only: keep the standalone HTML and concise report; remove separate editing
  sources and temporary working files. Explain that those sources will no longer
  be available for straightforward revision.

Identify the exact folders and file categories affected before requesting the
choice. No answer means no deletion; disclose that files left in temporary storage
may be removed by the host.

Cleanup requires the user's choice or an applicable earlier explicit instruction.
Remove only files owned by this run. Never delete the installed skill, project
files, unrelated temporary files or evidence for unresolved findings.

If detailed evidence is discarded, preserve the report and record that removal
was at the user's request. Moving evidence to verified durable copies is not discarding it.

Verify the retained deliverables after cleanup and report their final location.

Package maintainers use [evaluation](../evals/maintainer.md) and `tests/test_build.py`;
ordinary explanation requests do not need the maintenance rubric.
