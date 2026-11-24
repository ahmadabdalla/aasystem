# Feature

You own the acceptance criteria; specialists give you the design.

If the change is a presentation edit that [qualifies](../references/verification-contract.md#owner-presentation-eligibility), do it as that section says and skip these steps. If it stops qualifying, before or after the edit, come back to them.

1. **Ground the change.**
   - If behaviour, business rules or acceptance scenarios that matter are missing or unsettled, or this is a new app, use [Product](../../product/SKILL.md).
   - If you'll touch existing systems, read them with [How](../../how/SKILL.md) first.
   - If the approach is unsettled, use [Solution](../../solution/SKILL.md).

   Done when the behaviour, rules and acceptance scenarios are settled or listed as open.

2. **Design.** If design is missing or unsettled:
   - If the user asked to refine a prototype first, or how it looks is still open, use [UI Refinement](../../ui-refinement/SKILL.md) for design and review only. Come back here with what it settled.
   - If not, use [Interaction Design](../../interaction-design/SKILL.md) for the interactions that change.
   - If the change meets the [Architect design trigger](../../architect/SKILL.md#design-trigger), give Architect the interaction decisions, open choices and anything the design leaves out.
   - If design alternatives would change the result, compare them with [Arena](../../arena/SKILL.md).
   - If the design is contested, run [Interrogate](../../interrogate/SKILL.md) and act on the findings that hold up.

   Send changed business meaning back to Product, and changed interaction choices back to their owner. Done when you have a settled design and a verification plan. If proof depends on state, the plan uses [Seed scenarios](../../architect/references/seed-scenarios.md) for the starting data and the changes the proof needs.

3. **Plan the work.** If the work has several parts, note the blockers, independent workstreams and shared state, then pick the smallest safe split, using [Swarm](../../swarm/SKILL.md) for independent slices.

4. **Build.**
   - Build with [Implement](../../implement/SKILL.md).
   - If an unresolved integration assumption could break the design, build the smallest kept slice that tests it first, before anything depends on it. Name the assumption, entry point, input, expected output and side effects in the verification plan, and run it through the real components, not stubs. If it fails or is inconclusive, stop the dependent work and take the contradiction to Architect.
   - If the build exposes a design error, go back to design.
   - If you change something shared, update everything that uses it.

5. **Verify.** Get [independent verification](../references/verification-contract.md#independent-implementation-verification) of the final combined change, covering the affected user paths and side effects. If there's a reviewed visual reference, compare the rendered result using the [interaction review checks](../../interaction-design/references/review-checks.md).

6. **Deliver.** If you split the work, report how.
