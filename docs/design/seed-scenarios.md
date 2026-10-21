# Seed scenario guidance design

Integration for [issue 39](https://github.com/ahmadabdalla/aasystem/issues/39), approved for implementation in the task conversation. The starting point was revision `7b84af7add05903e8de57375435a4864ae71d46c`.

## Decision and ownership

Keep scenario design with Architect and feature completion with project verification. Use the existing task assignments and project records to connect them.

| Owner | Maintained guidance |
| --- | --- |
| Architect | [Seed scenarios](../../skills/architect/references/seed-scenarios.md): purpose, minimal context, valid construction, lifecycle and separate source/build/release/invocation choices. |
| Feature | [Ground the change](../../skills/aapilot/playbooks/feature.md): conditionally identify adequate starting context or a needed scenario change. |
| Project verification | [Scenario coverage](../../skills/bootstrap-verification/references/project-contract.md#scenario-coverage): changed semantics, real feature actions, observations and automation distinctions. Bootstrap and Maintain Verification already consume this contract. |
| Existing delivery assignments | [Implement](../../skills/implement/SKILL.md) receives approved data changes and feature exercises; [independent verification](../../skills/aapilot/references/engineering-verification.md) assesses the combined artifact and executes affected project checks. |

Four portable files change: the new reference, Architect, Feature, and the project verification contract. The [system record](skill-system.md#design-implementation-and-independent-verification) and [graph](../../visualizations/skill-library/README.md) describe these responsibilities without a new skill or agent node. Invocation metadata is unchanged.

## Why this shape

Putting lifecycle guidance inline in several skills would make unrelated work load it and create multiple places to maintain one rule. A separate seed skill would add discovery and handoff obligations without a demonstrated independent responsibility. One conditional reference is the smallest useful home for these design decisions.

The [preserve-decision-context principle](../../skills/principle-preserve-decision-context/SKILL.md) shapes the handoff: link owned rules, but carry the actual project-specific scenario decisions and proof requirements in the existing assignment. A reference alone cannot replace those inputs. Generated project procedures contain their own real commands and expectations and remain runnable without this library.

Existing data can support a feature action without a permanent fixture change. A disposable fixture can keep its simple reset policy; retained contributor edits need an explicit repeat/rebuild policy. Project production reference data follows its real contract. This increment introduces no loader, registry, fixed schema or folder layout, automatic field-coverage detection, or CI machinery.

For hypothetical tenfold growth in scenarios or projects, the expected first maintenance pressure is repeated lifecycle policy and inventory drift. Keep inventories and commands project-owned and link shared setup. Reconsider central machinery only if observed callers cannot resolve scenarios or maintain recipes. This reasoning establishes no measured capacity.

## Evaluation boundary

Follow the [evaluation procedure](../../skills/aapilot/playbooks/eval.md) with equivalent bounded requests under the starting and changed instruction versions. Use contrasting synthetic projects: disposable SQLite fixtures and retained JSON contributor data. Judge routing usability, minimum appropriate machinery, valid scenario meaning, changed-feature proof, and honest evidence/automation reporting from actual artifacts and actions.

Exercise optional-field write/readback despite old passes; derived values and relationship rejection; adequate existing context and stateless work; edit preservation and disposable reset; separate compile/release decisions; omitted or skipped automation; and controlled legacy/invalid construction. Supplied-record decisions prove only that boundary; generated helpers and feature claims require executable checks. No improvement claim follows from fixture presence or self-reported compliance.

The PR records actual comparisons, independent review, package checks and remaining limits. Temporary inputs, original outputs and failed attempts remain outside maintained source through review under the existing evidence lifetime. Instruction drafts have moved to their owning files so this record retains rationale rather than a second copy of the rules.
