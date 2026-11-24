# Business state and consistency

## Name the model

Pick one concrete operation, such as "reserve the last seat". Write down the facts that must hold for its result to be valid.

Say whether two things are equal by id or by contents. Add units, transitions and lifecycle only where this operation depends on them.

A table, class, context and service needn't line up. Folders don't prove a context.

If two contexts use one term differently, name both meanings and the translation between them. If a meaning is unsettled, invoke the [`domain-modeling`](../../domain-modeling/SKILL.md) skill. If a business rule is unsettled, return it to your caller.

## Place the invariant

1. Write the rule. List every writer, including jobs, imports and retries.
2. Pick the module or service that owns the state, and the operation in it that enforces the rule.
3. List the reads and writes that must succeed together.
4. Pick the mechanism that makes them succeed together, such as a transaction, lock, unique constraint or version check.
5. Say what happens on concurrent attempts, stale reads, duplicate requests and partial failure.
6. If the rule spans owners, name the agreed consistency guarantee and how a failed step recovers. Events are a choice, not a default. If nobody has agreed one, return it to your caller.

Keep state that changes independently apart, unless the rule needs it together. Add a factory, repository, event or rich object only if this operation needs one. Plain records and functions are fine.

## Carry the proof

For each rule, write the success, rejection, conflict and recovery cases. If competing writes or replays could break the rule, add them. Name any effect that survives a failure, and who sees or repairs it.

Put the owner, translations and consistency guarantee in the design package's shape, and these cases in its verification plan.

Example: two requests reserve the last item at once. Say which wins and what the other gets. A method named `reserve` doesn't answer this; name the atomic check-and-write. If payment is a separate step, keep the agreed pending and recovery states. Don't promise one transaction across both steps, and don't allow overselling.
