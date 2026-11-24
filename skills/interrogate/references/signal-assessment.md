# Signal assessment

List how the work in scope could fail or be misused, and check whether anyone would notice. For an existing system, trace the detection it has. For a design, assess what it proposes. For a change, compare before and after.

Fill in one block per scenario:

```text
Scenario: <trigger> → <consequence>
Signal: <what is emitted> → <where it lands>
Consumer: <who or what acts on it, or none>
Evidence: <observed | traced | documented | inferred | unverified>, under <conditions tested>
Gap: <what still goes unnoticed>
Fix: <smallest change or check>
```

Blocking an action, recording it and notifying someone are three separate claims; check each. If a signal changes, trace everything that consumes it. Say what you inspected.
