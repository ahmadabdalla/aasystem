# Exercise a changed skill

Use when maintaining this package, not during ordinary explanation requests.
The fixtures are synthetic read-only projects, not authoritative architecture
templates. Keep produced explanations and run evidence outside maintained source.

1. Run `python3 -m unittest discover -s <skill>/tests -v` and build the reference.
   For profile changes, build both bundled models through the standard command
   without `--template`, and run the shared browser helper on both exports.
2. Give a fresh agent the skill and one case below. Copy the fixture to a fresh
   temporary Git repository so default delivery is observable without writing to
   maintained source. Withhold this rubric, the producer's conclusions and the
   example's intended topology. Give the agent an execution request to exercise
   explicit use.
3. Observe whether the executor launches its own UI verifier under
   references/verification.md; parent-launched review does not prove this handoff.
   Preserve the assignment and original return. Ask a separate noneditor evaluation
   judge to inspect source, model and actual HTML, applying
   the criteria below. Give the judge access to required browser tooling. Producer
   assertions or a valid JSON model are not substitutes for observed behavior.
4. Preserve original attempts and distinguish skill defects, fixture defects and
   tool gaps. Repair only supported findings, rerun affected cases, and record the
   instruction/output identities, observed outcomes and finite limits.

## Judge-only criteria

- Important claims have meaningful source locators; unknown transport/hosting
  implementations remain unknown rather than acquire invented products.
- Triggers and state transitions match the source, including asynchronous acceptance
  versus completion, deliberate reads, and the requested failure outcomes.
- The experience uses the project's real interaction surface; the API/CLI cases
  do not acquire a browser, notification or approval flow absent from source.
- Business responsibility, backstage actions and technology are mapped through the
  shared model, with current exchanges highlighted rather than implied calls.
- The exported HTML works offline: automatic finite playback, pause/resume, view
  switching without resetting progress, selection, replay and reduced motion.
- A settled brief proceeds directly. A single consequential gap gets one focused
  question and a pause. Grill Me uses Discovery interviews to uncover activities
  or journeys and Grilling to settle walkthrough choices. Check that the executor
  waits for answers and carries the accepted brief into the build.
- Verify root delivery from a subdirectory, collision handling, and offline
  opening without the run directory. Check that the run note identifies the
  rebuild inputs. Exercise missing-state recovery when reviewing refinements.
- The executor launches a separate aligned UI verifier, supplies the exact candidate
  and required references, preserves findings and resolves material issues before
  claiming completion. With delegation or browser access unavailable, it reports
  the missing independent proof rather than substituting self-review. Exercise this
  boundary with an explicit tool constraint; a claimed launch is not observed proof.
- The entire diagram remains readable across the laptop dimensions in SKILL.md and
  theme states, with no material overflow, clipped labels or misleading connectors.

For the review-console case, also judge the actual renders against the bundled
[presentation anchors](../references/presentation.md#reference-composition).
A functional card deck does not pass visual fidelity.

For the business-workflow case, apply the Business map source and reader checks in
[verification](../references/verification.md#source-and-model). Compare both views
with the fictional reference at both laptop sizes. Trace the entire map and inspect
the busiest phase; automated geometry must cover every node and relationship
caption, including docking, clearance and route obstructions. Exercise ordered
phases, readable paused selection and stable control labels. Also exercise native
Safari Pause/Resume and paused selection, recording its actual viewport. WebKit
automation on another OS does not establish native Safari behavior; report missing
access as an outstanding check.

A materially false causal claim, unexercised required runtime path or unusable
graph blocks a passing case. Report cosmetic preferences separately. Finite cases
do not prove reliability on arbitrary projects, deployment health or host discovery.
No model-diversity claim is warranted when all workers use the same configured model.

## Case prompts

Give the executor only its selected fixture and prompt, not the judge criteria.

### business-workflow

Fixture: a fresh temporary repository containing only
[`business-workflow-source.md`](../examples/business-workflow-source.md).

> Use system-in-motion to explain this equipment-reservation journey from a business
> architecture perspective: who performs each activity, what people decide, what
> the software does, and what happens next. Keep the planned confirmation and
> collection boundary visible. Produce an offline walkthrough and editable model.

Observe the executor's profile selection and standard build without supplying a
renderer choice, layout, expected graph or model. The source defines the expected
responsibilities and topology; assess actual output, not fixture presence.

### reading-service

Fixture: `fixtures/reading-service`

> Use system-in-motion to help a new teammate understand this reading intake service: what its caller sees, how background processing works, and what technology roles drive it. Include the unsupported-unit outcome and be clear about what is not known. Produce a local animated explanation without modifying or running the service.

### catalog-cli

Fixture: `fixtures/catalog-cli`

> Use system-in-motion to explain this catalog importer to a new operator and developer, including success, validation failure and duplicate-SKU failure. Produce an animated local explanation. Inspect the source without importing data or modifying the importer.

### review-console

Fixture: `fixtures/review-console`

> Use system-in-motion to explain this document-review project from submission through background scanning, operator review and recorded approval, including the planned publisher boundary. Reconstruct its relevant UI moments and explain the technical flow in the demonstrated motion-walkthrough pattern. Keep source inputs read-only and write a local model and HTML explanation.

### Source scope and collision

Put the catalog fixture under `tools/catalog` in a temporary repository and
place a sentinel file at the root named `system-in-motion.html`. Use the
catalog-cli prompt with `tools/catalog` as its source directory. Verify that the
sentinel keeps its contents and the new HTML is its only new sibling.

### Open brief

Use the catalog fixture with either prompt. For the interview case, provide
answers after observing the pause, then verify that the accepted scope is reused.

> Use system-in-motion to compare today's catalog import with the proposed new
> import process.

> Use system-in-motion for this catalog importer. Grill me before you build so
> we can choose the audience and whether to focus on success or error recovery.
