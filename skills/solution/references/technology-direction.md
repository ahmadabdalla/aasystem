# Technology direction

## Find the gaps that matter

Check the brief against these:

- **Commitments:** existing technologies, team experience, provider accounts, ownership, and technical or contractual controls. Organisation size alone isn't a requirement.
- **Workload:** where user interactions, server requests, scheduled work and long-running jobs run, and the duration, concurrency, latency and scaling that affect the choice.
- **Data and access:** persistent records, files, data ownership and access boundaries. Give each workload its own identity, and confirm it's permitted to use each endpoint, not just able to reach it.
- **Operations:** budget, acceptable downtime and data loss, who owns recovery, deployment and rollback, and how you'd notice the worst silent failure.
- **Compatibility:** whether the parts fit together, including runtime limits, regions, tiers, identity integration and total recurring cost.

## Compare the whole approach

Check whether one choice changes another's assumptions: hosting can limit background work, identity can limit data access, and recovery needs can change storage and cost.

Add the chosen technologies, each runtime role with where it runs and its key dependencies, and the evidence limits to the decision record. For a provider, data-format or runtime commitment, name how data, contracts and operations would move off it. A replacement interface alone isn't an exit.
