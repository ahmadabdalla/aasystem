# Decision records (ADRs)

## Which rules apply

Follow the project's written ADR rules. If it has none, follow the format its existing ADRs use. Otherwise use the default below. If two sources conflict and nothing says which wins, say so. Review an ADR against the same rules it was written to.

## When to write one

Write an ADR only when all three are true:

1. **Hard to reverse:** changing your mind later costs something real.
2. **Surprising without context:** a future reader would wonder why.
3. **A real trade-off:** there were genuine alternatives and you picked one for a reason.

Otherwise keep the choice in the task or design record, unless the user asks for an ADR.

## Where it goes

Use the project's locations, numbering and index. Otherwise put system-wide choices in `docs/adr/` and choices inside one context in `<context>/docs/adr/`, named `NNNN-short-title.md` with the next unused number. Create the directory when the first ADR needs it, and link the new ADR from the project's index or instructions.

One decision per ADR. Before writing, read related ADRs. If yours contradicts one, supersede it. Link related ADRs to each other.

## What every ADR says

Whatever the format, the record says:

- the problem or constraint
- the decision and why
- at least one alternative you rejected, and why
- the costs and limits
- what happens at 10x: run [10x](../../10x/SKILL.md) when you create an ADR or change its choice, and say what you accommodate now, what you defer and what would make you reconsider. If growth changes nothing, say why in one line.

If the project's format has no slot for one of these, put it in the closest section, such as consequences or fallout. Never drop it, and don't add headings the format lacks. Keep each point to a sentence or two.

## Default format

```md
# {Short title of the decision}

{The problem. What we decided and why. The alternative we rejected and why. The costs.}

Standing: {user-confirmed | delegated | proposed | unresolved | superseded by ADR-NNNN}, {source}

## At 10x scale

{What grows, what we accommodate now and defer, and what would make us reconsider.}
```

## Standing

Say who settled the choice, in the project's format. **User-confirmed** or **delegated** (by a project record that grants authority) means accepted; link the source. Otherwise it's **proposed**, or **unresolved** if you can't tell. Don't guess.

A draft, a generated document or working code doesn't make a choice accepted, and acceptance doesn't prove the code does it.

## Changing an ADR

- **Same choice, better wording or evidence:** update it in place.
- **A different choice:** write a new ADR that says what changed and links both ways. Keep the old one and its rationale, and mark it superseded once the new one is accepted.
- **A new, separate choice:** give it its own ADR if it meets the threshold.

If the code doesn't match an ADR, report it. Don't rewrite the ADR to match the code.
