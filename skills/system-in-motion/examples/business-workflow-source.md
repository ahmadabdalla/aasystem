# EquipmentFlow: fictional reference rules

This document defines an invented equipment-reservation process solely for evaluating a business-workflow diagram. It is not a real application specification or a claim of deployed behavior.

## Roles

- Requester asks for equipment, dates and quantity.
- EquipmentFlow is software that checks eligibility and availability, calculates allocations, enforces completeness and records state.
- Service team supplies missing information, resolves exceptions, reviews plans and makes approval decisions.

## Assumed current behavior in this example

1. Every request retains its original contents.
2. Software accepts requests passing the configured eligibility checks; uncertain requests go to staff review.
3. Staff may accept a held request or close it. A closed request has no prepared reservation.
4. Accepted requests proceed to detail preparation. Staff save corrections or missing equipment, dates and quantities.
5. Saving triggers software availability checking. Unresolved details are flagged for staff; the software does not invent missing facts.
6. Software calculates an allocation using configured stock and allocation rules. Staff review exceptions; they do not perform that routine calculation manually.
7. Staff approve or reject the plan. Software refuses approval while required details or allocation issues remain unresolved and records the approving person and plan version.
8. Rejection produces Plan cancelled while retaining history. Important changes after review require preparation and approval again.

## Planned behavior in this example

9. Staff explicitly submit the approved reservation. Submission leaves Pending confirmation and does not itself mean Confirmed.
10. Software confirms only after an independent receipt matching the reservation exists. Waiting longer is not evidence of confirmation.
11. After confirmation, staff may record Collected or Not collected. Leaving the collection result Unrecorded is valid. Confirmation does not prove physical collection.

## Expected graph

Three horizontal lanes: Requester, EquipmentFlow, Service team.

Twelve nodes: Request equipment; Accept this request?; Review request; Request closed; Complete request; Check stock; Plan allocation; Approve this allocation?; Plan cancelled; Reserve equipment; Confirm reservation; Record collection.

Thirteen connections:

| From | To | Meaning |
|---|---|---|
| Request equipment | Accept this request? | Request arrives. |
| Accept this request? | Review request | Uncertain eligibility requires review. |
| Accept this request? | Complete request | Automatic checks pass. |
| Review request | Complete request | Staff accept. |
| Review request | Request closed | Staff close without preparation. |
| Complete request | Check stock | Staff save; software runs the check. |
| Check stock | Plan allocation | Software calculates using supplied details and available stock. |
| Plan allocation | Approve this allocation? | Staff review the calculated plan. |
| Approve this allocation? | Plan cancelled | Staff reject. |
| Approve this allocation? | Complete request | Changed details require preparation and approval again. |
| Approve this allocation? | Reserve equipment | Staff approve and explicitly choose to proceed. |
| Reserve equipment | Confirm reservation | Await the independent matching receipt. |
| Confirm reservation | Record collection | Confirmation permits optional later staff recording; it does not initiate it. |

The last three activities and their associated connections are marked planned. The first two exits are distinct from collection outcomes. Playback illustrates one representative route; the entire graph remains visible so alternatives are not lost.
