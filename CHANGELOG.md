# Changelog

## [Unreleased]

## [0.10.0]

- Add System in Motion, a direct skill for walking through one product journey in synchronized Experience and Architecture views. It builds an offline HTML walkthrough and an editable model grounded in project sources. Start with `$aasystem:system-in-motion` in Codex or `/aasystem:system-in-motion` in Claude Code.
- Give Pilot and System in Motion dedicated sections in the README, highlight the core skills, and consolidate CLI installation instructions.
- Add an Interrogate assessment for operational and security detection gaps. Design, implementation, and verification carry the relevant checks across change routes.
- Add merge-risk guidance to Interrogate for PR readiness and consequential recovery or failure-detection concerns.

## [0.9.1]

- Add Explain Visually, invoked directly or through Pilot's explanation route, to present a change, design or finding as an inline plain-text diagram in `before-after`, `flow` or `layers` mode. Pilot keeps one explanation route: Investigation grounds the facts and presents requested diagrams through Explain Visually, which draws only established evidence.
- How no longer adds diagrams unasked; a standalone How question presents a requested diagram through Explain Visually.

## [0.9.0]

- Replace vague conditions that decide what a worker or later step receives with concrete cases, so hosts that read conditions loosely still pass the right inputs. Pilot links Engineering Verification directly where it assigns acceptance proof, and the owner reads it before briefing the verifier. Boundary criteria now apply to new or changed callable parameters.
- Name concrete triggers for requirement and invariant coverage in Architect, Product and OpenSpec verification plans; settled-design retrieval in Implement; Architect handoff from prototypes; independent interaction-model review; scenario coverage; effect inspection; and adversarial review in Figure It Out and PR preparation. Routes, ownership and invocation policies are unchanged.

## [0.8.1]

- Engineering Verification now asks the owner to give the verifier the absolute path of each applicable criteria file, so a fresh verifier can load the Maintainability criteria from any working directory.

## [0.8.0]

- Breaking entry-point rename: `aapilot` is now `pilot`, under `skills/pilot/`. Use `$aasystem:pilot` in Codex, `$pilot` for direct skill installs, or `/aasystem:pilot` in Claude Code. The plugin remains `aasystem`; no old-name alias is shipped.
- Update shared references, system graph, package validation and optional Codex hooks together. Existing hook users must regenerate and trust configuration pointing to the new helper path, preserving their existing state directory. Version-2 task records and captured requests are unchanged. See the [migration steps](docs/ops/releasing.md#upgrade-from-aapilot-to-pilot).

## [0.7.1]

- Bound acceptance verification with a cumulative time allowance across diagnosis, repairs, rechecks and handoffs. Reassess recurring failures before retrying and report incomplete work when the allowance is exhausted.
- Classify correction failures and reuse earlier proof only when the affected inputs and outcomes remain valid. Preserve independent rechecks and integration coverage for shared production changes.
- Keep engineering coverage and discoverability review within the assigned change, and reuse current brief and rule inputs across stages. These are instruction-level controls; host-enforced budgets and delivery-time improvements are not established.

## [0.7.0]

- Keep Aapilot's original intent, scope assessment, decisions and acceptance requirements retrievable across increments, specialist handoffs and context recovery. Reuse the existing rubric and routes for research, product, UX, architecture and implementation rather than require a fixed agent chain.
- Add an opt-in local Codex adapter for temporary intent bindings, context restoration and mechanical completion checks. A checked handoff to an existing local task record retires owned scratch; explicit resume keeps intent identity across sessions. Hooks require explicit configuration and trust; portable invocation and other hosts retain their existing behavior. Recorded checks do not authenticate approval or prove semantic correctness.

## [0.6.1]

- Add the “Be ready to deliver and prove” principle to Implement's opening procedure. Establish delivery prerequisites and a runnable verification path before dependent work, and record material gaps in the existing task brief.
- Update the principle index, skill inventory, README, and system graph for the readiness check.

## [0.6.0]

- Add seed-scenario design and verification coverage guidance, including data purpose, lifecycle, delivery boundaries, and checks through real feature actions.
- Add compact engineering guidance for dependency boundaries, refactoring moves, and business-state consistency through the existing Maintainability, Implement, and Architect skills.
- Carry business-state guarantees and required failure, concurrency, replay, and recovery cases from design into implementation and independent verification. Update project verification recipes when coverage is missing or stale.
- Document the engineering guidance's conceptual sources and how existing skills use it.
- Clarify the README's usage examples, working agreements, and verification expectations. Shorten the system graph guide to explain its controls and relationships.
- Prefer one owned OS temporary run root for project verification. Require Bootstrap and Maintain to inspect adopted executable harnesses and verify cleanup, evidence retention and safe retirement.
- Ask independent Grill Me questions together and confirm shared understanding before implementation. Record agreed terms and qualifying decisions when authorized. Load the selected interview procedure on demand; product discovery keeps its own procedure.
- Add an S/M/L effort rubric with brief discovery, consequence-driven scrutiny and inherited execution conditions. Apply it to standalone owners while preserving required procedures, verification and human checkpoints.

## [0.5.1]

- Add independent rendered UX assessment through Interaction Design, using separate visual and interaction assessors with evidence-backed findings and explicit coverage gaps.
- Require the smallest retained integration slice to exercise unresolved assumptions before dependent feature work expands; keep final independent verification.
- Add a shared `10x` skill for design growth scenarios, constraints, tradeoffs, proof needs and reconsideration triggers. Reuse it in Solution, Architect, Interaction Design and ADR creation, with required checks carried into engineering verification.
- End default ADRs with an `At 10x scale` section while preserving established project formats. Update skill navigation and the system graph for the new assessment routes.

## [0.5.0]

- Simplify delivery around shared understanding, bounded specialist work, independent verification and human review. Reuse the checkout or one task worktree across correction rounds.
- Retire the work-receipts state machine, full-copy archives and managed execution runtime. Keep tested-input identity with an optional read-only streaming fingerprint check.
- Breaking tooling change: existing project verifiers using the retired CLI/runtime need explicit maintenance. Historical evidence and project files are not automatically migrated or deleted.

## [0.4.0]

- Distinguish lead acceptance requests from required independent proof, with domain criteria and specialist procedures assigned to a verifier separate from assessed-work producers.
- Define a portable host acceptance contract and distinguish owner-held local receipts from host-owned authoritative acceptance; no host integration or enforcement is shipped.
- Bound authorized active-session autonomy with explicit authority, proof, clock/budget checks and whole-process human stops.
- Select additional workers and Arena comparisons for concrete task needs; allow bounded implementer corrections while keeping independent review fresh.
- Assess scope and stage-appropriate proof before advancing a requested outcome, and allow the current owner to apply supporting procedures directly while preserving independent production verification and human checkpoints.
- Retain owner development returns without invented native dispatches; exclude the root owner from independent production proof.

## [0.3.1]

- Require a bounded engineering assessment alongside executable checks in the existing independent verification receipt and report, with material findings reconciled before acceptance.
- Clarify test independence and generated-source ownership in shared engineering assessment criteria.
- Enforce the manually prepared release PR contract and automate reviewed marketplace adoption after successful publication.
- Use Python release tooling with pinned development dependencies and reorganize maintainer documentation under `docs/`.

## [0.3.0]

- Make the shared verification contract and receipts standard for retained production changes through existing entry skills, with one root owner and run.
- Allow exact prescribed, low-impact presentation edits to use current owner checks without a worker; label that proof separately from independent production verification.
- Retain common native-dispatch, current-proof and human decision/visual checkpoints, including stopping for an actual human answer before resumption.
- Ship the Python 3.10+ standard-library receipt runtime under `skills/`. State schemas 1 and 2 remain historical read-only records; start a new schema-3 run without automatic approval or proof migration.
- Keep actual human viewing/resumption and other-host support unverified until exercised; local package and CLI checks do not establish them.

## [0.2.1]

- Define delegation capability checks, execution assignments and result acceptance; plan and verify closing work before completion.
- Separate independent discovery reviews from audits of supplied claims, including reviewer context and isolation limits.
- Clarify Architect routing for interface, state ownership and responsibility changes, glossary and decision-record creation, and Swarm comparison criteria.
- Specify ADR convention precedence and required default content, using the same rules for authors and reviewers.

## [0.2.0]

- Publish a versioned release automatically when a release PR merges to `main`, after checking the exact merged commit.
