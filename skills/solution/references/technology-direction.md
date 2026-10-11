# Technology direction

Use this review within solution's existing research and comparison. Reuse the product contract, project evidence, and settled decisions. Examine only choices relevant to the assigned scope.

## Find consequential gaps

Use these prompts to inspect the brief. Ask the user only when a missing preference or constraint could change the recommendation.

- **Commitments:** Existing technologies, team experience, provider accounts, ownership, and explicit technical or contractual controls. Organization size alone does not establish a requirement.
- **Workload:** Where user interactions, server requests, scheduled work, and long-running jobs execute. Check duration, concurrency, latency, and scaling needs where they affect the choice.
- **Data and access:** Persistent records, files, data ownership, and access boundaries. Distinguish endpoint reachability from permission to use it, and human identity from workload identity.
- **Operations:** Budget, acceptable downtime and data loss, recovery ownership, deployment, and rollback. Identify how the most consequential silent failure would be detected.
- **Compatibility:** Whether the proposed components fit together. Check relevant runtime limits, regions, tiers, identity integration, and combined recurring cost.

## Compare the complete approach

Feed relevant findings into solution's existing alternatives. Check whether a choice changes the assumptions behind another: hosting can constrain background work; identity can constrain data access; recovery needs can change storage and cost.

Name the required runtime roles, where they run, and their important dependencies. Include components only when the requirements justify them. Research current capabilities and test consequential assumptions through solution's existing evidence process.

## Carry the decision forward

Keep the selected technologies, runtime arrangement, tradeoffs, and evidence limits in the existing solution record.

For each material unresolved choice, name who must resolve it, what must be established, and when it becomes blocking: before selection, implementation, release, or a stated future trigger. Record a credible fallback when available; otherwise keep the recommendation conditional.

Stop when the technical direction is justified and the remaining uncertainty has a clear next step. Leave routine library and code-shape choices to architect.
