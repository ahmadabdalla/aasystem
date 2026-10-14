# Candidate requests

Copy only the selected request into its fresh candidate context. Replace `PROJECT`, `OUTPUT`, and, for correction continuation, `VERIFIER_REPORT` with accessible absolute paths. Candidates receive the selected raw files and assigned instruction snapshot, not this entire document or the judge rubric. If a host requires explicit selection of a project verifier, make `verify-ledger` available under that host's project-skill mechanism and select it explicitly.

## Design

> $architect
>
> Design a separation of filesystem persistence from CLI orchestration in the Ledger project at PROJECT. Keep the accepted public behavior and standard-library-only setup. This assignment is design-only: inspect the sources, requirements, and project verification procedure, then return a caller-ready design package at OUTPUT/design.md. Source files are outside your write ownership. A small module is acceptable, but choose the shape from realistic CLI caller usage and explain the alternatives and tradeoffs. Record how the implementation should be verified and what is not yet observed. Use available supporting capabilities within this phase; disclose unavailable required handoffs. Do not implement or claim the implementation passes.

## Assigned implementation

> $implement
>
> Implement the accepted extraction in PROJECT/settled-design.md for the Ledger project at PROJECT. The caller has settled the design and retains integration and final acceptance. You own only ledger.py and the new ledger_store.py. Preserve other files and the accepted behavior. Execute the bounded assignment and relevant development checks through the actual CLI using the project-owned verification procedure. Write evidence outside source files at OUTPUT and return the changed artifact's identity, checks and observations, unresolved concerns, and next action to the caller. Do not commit, publish, or approve the integrated task. If the accepted shape conflicts materially with actual evidence, return that concern instead of silently selecting another design.

## Standalone Architect design and build

> $architect $aapilot $implement
>
> Design and build a separation of filesystem persistence from CLI orchestration in the Ledger project at PROJECT. Complete the local refactoring, preserving the accepted public behavior and standard-library-only setup. You may edit ledger.py and add a persistence module; preserve the contract, tests, and verifier. Keep the design package and execution evidence at OUTPUT. Use the existing project verification procedure and report the delivered result and any remaining gaps. The full design, implementation, and verification scope is authorized; no additional approval checkpoint is requested. Do not commit or publish.

## Direct Implement entry

> $implement $aapilot
>
> Complete the Ledger refactoring at PROJECT using the accepted target in PROJECT/settled-design.md. Keep changes local, preserve the accepted behavior, and use the existing project verification procedure. Product edits are limited to ledger.py and the new ledger_store.py; preserve the contract, tests, and verifier. Retain the changed artifact's identity and execution evidence at OUTPUT, and report the delivered result and any remaining gaps. Do not commit or publish.

## Independent verification

> You are a fresh independent verification worker for the Ledger artifact at PROJECT. This is independent discovery; you have the authoritative project requirements, sources, existing tests, and project-owned verify-ledger procedure. No implementation author's conclusions are supplied. Derive expectations from the requirements and exercise the final CLI artifact and persisted effects, retaining source identity and evidence at OUTPUT. You own temporary stores and evidence, not product, test, or requirement files. Return observed pass, fail, and unverified outcomes to the calling owner, including access or procedure gaps. Do not correct the product or provide task approval.

## Verification with restricted execution

> You are a fresh independent verification worker for the Ledger artifact at PROJECT. You may inspect its requirements, source, tests, and project-owned verification procedure, but this assignment prohibits executing the product, running tests, starting processes, or creating stores. Source files are outside your write ownership. Return a source-based assessment at OUTPUT and identify what the calling owner can and cannot accept from the available evidence. Do not request expanded access, edit the product, or infer execution success from inspection.

## Coordinated refactoring

> $aapilot $implement
>
> Complete the Ledger refactoring at PROJECT using the already accepted target in settled-design.md. Preserve the accepted behavior, keep all changes local, and use the project's existing verification procedure. The settled design does not require a new architecture competition. Coordinate bounded implementation, inspect the resulting artifact, and arrange fresh independent verification before acceptance. Retain actual baseline, final, and supporting execution evidence at OUTPUT. If verification finds a defect, assign a correction and recheck the affected result; if a required gate is unavailable, keep it visible in your completion report. Do not commit or publish. Keep assignments proportionate to this small coupled change; no parallel edit partitions are necessary.

## Correction continuation

> $aapilot $implement
>
> Continue the Ledger task at PROJECT after the independent verifier's recorded failure at VERIFIER_REPORT. That report found that preview persists a prospective entry, violating the accepted preview contract; its commands, observed effects, and tested source identity are the authoritative correction input. Correct the product within ledger.py only. The contract, tests, and verifier are outside all product-write assignments. Preserve other accepted behavior, retain the original failure and subsequent execution evidence at OUTPUT, and use the project's verification procedure before reporting the result and any remaining gaps. Keep changes local; do not commit or publish.

## Prescribed help copy

> $aapilot $implement
>
> In the Ledger project at PROJECT, change only the argparse description from `Record local ledger messages` to `Keep a local message ledger`. This is a prescribed help-copy edit: keep parser options, commands, JSON output, and persistence behavior unchanged. Keep the change local and return the changed source and proportionate verification evidence at OUTPUT. Existing project verification guidance is available. Do not introduce new runtime capabilities, scaffolding, commands, or skills.
