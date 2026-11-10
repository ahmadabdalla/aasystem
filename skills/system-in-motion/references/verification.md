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

For Business map, trace every node against its lane performer and source: trigger,
input, action, result and any human choice. Check every alternative, non-success
exit and rework path, including planned work and independent confirmation boundaries.
Review the map alone as a reader unfamiliar with the source: can each visible node
answer who acts, on what object, and what changes or choice follows? A decision
must ask a complete question (for example, “Accept this request?”). For each unclear
label record the unanswered who/what question and replacement wording, then recheck
the final map. Tooltips and narration cannot repair an ambiguous visible label.

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

Choose the first applicable HTML destination.

1. The user's explicit output path.
2. The previous delivery directory and base filename for a refinement.
3. The project's walkthrough output convention.
4. The repository root containing the source scope, even when the request names
   a subdirectory.

For a directory without a filename, use `system-in-motion.html` or the next free
numbered sibling. When refining at the previous destination, use a numbered
sibling unless replacement is authorized. If an exact path is occupied and the
user has yet to authorize replacement, ask whether to replace it or use another
path. Confirm the existing file's identity before any authorized replacement.

If a required destination is unavailable, report the blocker and the verified
candidate's path. If the default repository root is read-only or there is no
repository, deliver from the run directory and state that the file is temporary.

Deliver only the verified HTML by default. Create a new file without overwriting
an existing path unless replacement was authorized. Compare the delivered bytes
with the reviewed candidate and confirm it opens offline without the run
directory. Delivery grants no authority to commit, publish or deploy.

If the user requests a permanent editable package, include the model, any custom
template, and the other inputs and command needed to rebuild. Verify the rebuild
works without the temporary directory and report the package path.

### Refinement state

In the run directory's `run.md`, record the delivered HTML path and hash, the
source scope and revision or snapshot, and the command that built the reviewed
export. Include paths and hashes for the builder and inputs. Link the review record.
At delivery, share the HTML and note paths, source limits, reviewer, checks
performed and remaining gaps. Explain that the host can remove temporary files.

On refinement, use the note shared at delivery. Check the export and rebuild
inputs against its hashes. If the note is unavailable or the files are missing
or changed, explain the gap. Rebuild from available sources or ask for what is
needed.

### Cleanup

Clean up on request. Identify the affected paths and remove only run-owned files
covered by the request. Preserve active work and evidence for unresolved findings.
Verify any durable copy before removing the temporary original. If discarding
detailed evidence at the user's request, record the removal in the verification
summary. Verify the delivered HTML after cleanup.

Package maintainers use [evaluation](../evals/maintainer.md) and `tests/test_build.py`;
ordinary explanation requests do not need the maintenance rubric.
