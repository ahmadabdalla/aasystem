# Product discovery evaluation

This package exercises the conditional discovery -> journeys -> requirements path. Follow the [evaluation playbook](../../skills/aasystem/playbooks/eval.md) and reuse the [product-to-interaction package's runner preparation and evidence conventions](../product-to-ui/README.md). Use fresh, isolated baseline/revised candidates with the same raw fixture and explicit `aasystem` entry point; keep this README and the [judge-only rubric](rubric.md) outside candidate contexts. No new runner is required.

Product returns the assigned discovery result or behavior contract to its caller. Grill-me returns interview evidence to its caller, including Product for a discovery assignment. The caller owns continuation; a discovery-only result does not automatically trigger requirements or Interaction Design.

## Cases

| Fixture | Candidate work |
| --- | --- |
| [founder-platform-discovery](fixtures/founder-platform-discovery.md) | Interview a founder about concrete platform work within a discovery-only scope |
| [interview-to-journey](fixtures/interview-to-journey.md) | Synthesize attributed answers into a cross-person journey and scoped requirements |
| [resume-discovery](fixtures/resume-discovery.md) | Resume retained answers with revisions and a pending question |
| [existing-contract](fixtures/existing-contract.md) | Complete a routine authorized edit using a sufficient contract |
| [unresolved-authority](fixtures/unresolved-authority.md) | Stop at one consequential permission question while preserving the accepted baseline |

Run all five for the full regression claim; a subset supports only its exercised paths. Material questions end a run as in the reused conventions, except for the bounded founder interview below.

## Runner-only founder replies

For `founder-platform-discovery`, deliver the following predefined replies over successive turns, only after a single focused question that matches the stated topic. Attribute every reply to Morgan, founder, 2026-10-06; these establish founder intent and recollection, not observed end-user behavior. Use the same matching rule and replies for both variants. Each reply is available once, and the next question must arise from the preceding answer or existing project context. Preserve the exact delivered text and question in the run record.

| Question topic | Participant reply |
| --- | --- |
| A concrete activity/example or sequence of work, such as booking, collection or return | “Yesterday Lee booked a drill for a repair crew at North Workshop. I confirmed it in the spreadsheet, then Lee collected it from Pat. Pat checked its condition and wrote the collection time beside the booking. The platform should support that sequence. We still use paper at the counter when the network is down.” |
| The return handoff, responsibilities, completion, damage, or offline recovery | “Lee brings the drill back to Pat. Pat checks the serial number and condition before marking it returned. Lee can report damage, but Pat records the final condition. A return is complete when Pat records that inspection; a drop-off without inspection is unfinished. If Pat finds damage, the drill stays unavailable until a repair technician clears it. Offline, Pat records the inspection on paper and enters it later. I have not decided who may resolve a disagreement about damage; keep that question open.” |

Do not supply both replies in advance, invent replies, or treat these statements as acceptance of an assistant proposal. A question outside these topics stays pending and ends the run. After two replies, allow a final synthesis or preserve the next unanswered question and stop. Record unmatched questions and unexercised answer-capture/adaptation behavior as unverified, rather than supplying a convenient answer. `unresolved-authority` receives no follow-up reply.

## Evidence and limits

Retain exact prompts, source/snapshot identities, replies, reads/actions, outputs, questions, edits and independent judgments using the linked evidence conventions. Assess routing from traces, answer capture from records produced before the next question, and outcomes from actual artifacts. Fixture presence, a walkthrough or candidate claims do not establish behavioral success. Report structural checks separately from exercised behavior; native host invocation, usability, runtime behavior and owner acceptance remain unverified unless separately exercised.
