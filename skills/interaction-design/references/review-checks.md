# Interaction review checks

Check the actual artifact against its product sources, decisions and evidence. Skip checks outside the assigned scope; a routine visual tweak needs no product review. A change is consequential if it changes navigation, who can see or do something, or a screen's primary action.

## Authority

- Can a reader find the source and standing of each consequential requirement and presentation decision?
- Is any open default or unknown provenance hidden?
- Has an agent's suggestion, a repeated spec, a working prototype or reviewer agreement been treated as human acceptance?
- Can one person still hold several roles?
- Is every role, permission and scope distinction backed by the domain?
- Does any interaction change business meaning or add behaviour that belongs to Product?

## Coverage

- Does every journey and requirement reach an interaction or a named non-UI owner, including failures, restrictions, unfinished work and handoffs between roles?
- Does every consequential destination, tab, summary and control group trace to a purpose? For example, does a history requirement justify a new Activity page?
- Is each missing behaviour marked as left out of this mock, left out of the product, or built but unverified?
- Does the structure help people choose and finish actions, without repeated prose making up for unclear structure? Keep the labels people need for errors, restrictions and decisions.

## Fidelity, only if a reviewed visual reference exists

- Is the result compared with the reviewed revision at the same viewport, state and content?
- Are explicit and accepted placement, size, shape, colour, spacing and state treatments kept? Check the rendering; CSS values alone don't prove layout.
- Do responsive and accessibility adaptations stay inside the constraints? Return a conflict instead of dropping an instruction.
- Is each difference a supported change, a defect or unverified? Similar screenshots don't prove behaviour, and working behaviour doesn't prove fidelity.
- Are fidelity differences kept apart from concerns about the reference itself?

## Alternatives and handoff

- Did unsettled alternatives get a fair comparison on shared constraints, with tradeoffs and disagreement kept rather than votes counted?
- Can the technical owner find the contract, requirements, decisions, states and open constraints without reading a mock as the full spec?
- Can the verifier derive actions and expected results without reading the implementation?
- Is prototype evidence claimed only for what was exercised?
- Does each requirement and decision have one home, with proposed, superseded and archived records findable?

Return one line per finding:

```
<blocking | risk | improvement> — <artifact ref> — <issue> — <defect | concern | question>
```

Blocking must be fixed before handoff. A risk is consequential and its owner decides. An improvement is optional.

After fixes, check the revised combined artifact. A review of an earlier candidate doesn't carry over.
