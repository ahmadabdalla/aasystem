# Evaluation

Before starting any agent, read [delegation](../references/delegation.md) and its [review rules](../references/delegation.md#reviews).

1. **Frame.** Write 3-6 observable criteria for the changed behaviour. Use a realistic task and a boundary case. To claim an improvement, run the old version on the same request, model and fixture.
2. **Prepare.** Give each candidate its own directory, the request a user would type, and one instruction version. Show no candidate the criteria, expected answers or another candidate's output. If anything it sees says eval, test, judge, rubric or variant, rename it. If the request names the skill, you're testing explicit use, not discovery.
3. **Run.** Start fresh candidates; save each prompt, instruction version, output and transcript.
4. **Check the runs.** Before grading, read the end of each transcript. If a run hit a usage limit or stopped early, rerun it; that is not a regression. If the host emits several final results, as `claude -p` does with subagents, grade the longest.
5. **Judge.** Give one independent judge the rubric and every output labelled A, B and so on, with no variant or model names in outputs or paths. Score all variants together on one scale. Run the output's tests. Grade routing and handoffs from the files each candidate opened and the commands it ran, not from what it says it did. If there's no transcript, mark routing unverified.
6. **Reconcile.** Read every output and settle disagreements from the artifacts. Call each failure an instruction defect, a host limit or a fixture fault. Keep failed runs; say why you reran any.
7. **Recommend.** Adopt, fix or investigate further, within what you ran. Record the evidence location and limits in the change record. After a fix, rerun the affected cases.

Keep run evidence outside the repo, per [project evidence conventions](../../bootstrap-verification/references/project-contract.md#evidence-and-retention). Keep a permanent regression case only when you will reuse it, with a request, a check and the failure it catches.
