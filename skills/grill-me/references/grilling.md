# Grilling

Map the decisions as a **design tree**: each answer can unlock more questions. Keep settled, open and deferred choices in the existing brief; conversation can suffice. Propose routine defaults within delegated authority. Keep unrelated branches outside the interview.

Work in **rounds**. The **frontier** is every open decision whose prerequisites are settled. Ask them together. Questions that depend on unanswered questions wait for a later round.

## Find the facts

Inspect relevant code, terminology, decisions and primary sources. Finding facts is your job; choices needing judgment belong to the user. Separate observations, assumptions and preferences.

Use tools and fact-finding workers under the [delegation rules](../../pilot/references/execution.md#delegation). Pending facts block only dependent questions. If a needed fact is inaccessible, state the gap and ask for the minimum missing input.

## Ask and update

Number each question and give a recommendation with its main tradeoff. Word it so "yes" accepts the recommendation. Use the evidence and state uncertainty.

```text
Q1. <Question whose prerequisites are settled>
Recommendation: <Answer and main tradeoff>

Q2. <Another independent question>
Recommendation: <Answer and main tradeoff>
```

Then stop and wait for answers before further investigation or action. Update the brief with the user's answers, reasons and constraints. Keep unanswered or ambiguous choices open. Surface contradictions with earlier answers or evidence. Reopen settled choices only when new evidence warrants it. Recompute the frontier for the next round.

## Finish the interview

Finish when the frontier is empty and all decisions needed for this scope are resolved. Unresolved prerequisites leave a gap; deferred consequential choices make the affected result conditional.

Summarize choices, reasons, assumptions, deferred questions and observable success criteria. Ask the user to confirm shared understanding, then stop and wait before implementation. Reuse explicit confirmation already covering that agreement. Return the brief to the caller.
