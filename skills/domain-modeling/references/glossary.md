# Project glossary

Use the existing glossary and context boundaries. Without an established format, give each term a short definition and clarify relationships or confusing synonyms only when needed.

Default to a root `GLOSSARY.md`. When established contexts use different meanings, keep definitions in each context's `GLOSSARY.md`. Reuse the project's navigation; if several glossaries need a new entry point, add a small root `GLOSSARY-MAP.md` linking their contexts and locations.

Record domain concepts specific to this project. Keep implementation plans, unresolved hypotheses, and decision rationale in their owning records. Check proposed definitions against concrete examples and distinguish intended meaning from current implementation where they disagree.

For example:

```markdown
**Customer:** The organisation that owns a subscription. A customer may have several users.

**User:** A person with access to a customer's subscription.
```

Add or revise a term when its meaning is established. If a changed definition affects existing contracts, return those affected behaviors to the caller for design and verification. A terminology edit alone does not migrate the code or prove those contracts.
