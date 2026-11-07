# Exercise a changed skill

Use when maintaining this package, not during ordinary explanation requests.
The fixtures are synthetic read-only projects, not authoritative architecture
templates. Keep produced explanations and run evidence outside maintained source.

1. Run `python3 -m unittest discover -s <skill>/tests -v` and build the reference.
2. Give a fresh agent the skill, one fixture directory and its prompt from
   the cases below, with a separate task output directory. Do not supply this rubric,
   the producer's conclusions or the example's intended topology. Do not ask it to
   recite the skill. Explicit use tests execution, not automatic discovery.
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

A materially false causal claim, unexercised required runtime path or unusable
graph blocks a passing case. Report cosmetic preferences separately. Finite cases
do not prove reliability on arbitrary projects, deployment health or host discovery.
No model-diversity claim is warranted when all workers use the same configured model.

## Case prompts

Give the executor only its selected fixture and prompt, not the judge criteria.

### reading-service

Fixture: `fixtures/reading-service`

> Use system-in-motion to help a new teammate understand this reading intake service: what its caller sees, how background processing works, and what technology roles drive it. Include the unsupported-unit outcome and be clear about what is not known. Produce a local animated explanation and editable model without changing or running the service.

### catalog-cli

Fixture: `fixtures/catalog-cli`

> Use system-in-motion to explain this catalog importer to a new operator and developer, including success, validation failure and duplicate-SKU failure. Produce an animated local explanation and model. Inspect the project without importing data or changing the project.

### review-console

Fixture: `fixtures/review-console`

> Use system-in-motion to explain this document-review project from submission through background scanning, operator review and recorded approval, including the planned publisher boundary. Reconstruct its relevant UI moments and explain the technical flow in the demonstrated motion-walkthrough pattern. Keep source inputs read-only and write a local model and HTML explanation.
