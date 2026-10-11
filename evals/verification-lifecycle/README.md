# Verification lifecycle evaluation

Exercises temporary verification output, teardown, retained proof, and reruns using the [evaluation playbook](../../skills/aasystem/playbooks/eval.md). Fixtures stay outside runtime skills; generated runs stay outside this package.

Copy [the Notes project](fixtures/notes-project/) into a separate temporary Git repository for each request in [requests.md](fixtures/requests.md), committing its initial files before execution. Save complete baseline and revised `skills/` snapshots. Give fresh candidates only their assigned snapshot, request and raw project, with separate writable directories. Keep this README, the [rubric](rubric.md), label mapping and other outputs out of candidate contexts. Explicit instruction reads test application, not native host discovery. Record when isolation is instruction-based rather than enforced.

Use an independent judge to inspect actual projects, evidence and available execution records. Execute generated helper invocations and check relevant CLI observations, post-teardown proof, Git tracking, unchanged-map reruns and durable links after temporary evidence removal. Do not delete the candidate's original run evidence: simulate expiry in another checkout. Preserve failed attempts and distinguish fixture faults from instruction defects.

Record prompts, source/fixture hashes, environments, model settings, artifacts, findings and reconciliation outside the reusable package. Retain evidence through review and name its disposal boundary. State missing host traces or invocation checks. A revised-only run supports the exercised behavior, not an improvement over baseline or broad reliability.
