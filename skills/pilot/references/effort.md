# Effort

Size the work S, M or L before you plan it. The size sets how much planning and coordination the work gets. It never skips a required procedure, check or human decision.

Look at the ask, the code it touches and the checks that already exist, just long enough to pick a size. Size by uncertainty and coupling, not file count. If missing evidence could change the size, call it provisional and resize when you know more. An unclear scope isn't automatically L.

| Size | When | Then |
| --- | --- | --- |
| S | One local change. You know what to build, how, and how to prove it. | Work directly, with no stages. Reuse the existing design and checks. Keep the plan to a few lines. |
| M | One outcome that crosses components, or needs design or dependency decisions. | Settle the interfaces and the proof before you build. Order the dependencies. Test risky integration assumptions early. |
| L | Several coupled outcomes, or open choices that need discovery before design or delivery. | Split into stages, each with an owner, a stop point and a result you can verify. Keep one plan across them. |

## Consequence

Consequence is separate from size. If the work could cause unauthorised access, a privacy leak, a financial error, data loss or an outage, name the invariant that must hold and the check that proves it. A small permission fix is still S and still needs strong security checks. If protecting the invariant turns up more work, resize.

## Record it

Write the size, a one-line reason and any consequence checks into the brief. Don't write a separate sizing report.
