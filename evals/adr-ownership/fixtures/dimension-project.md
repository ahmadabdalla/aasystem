# Enquiry project

## User request

Use domain-modeling to preserve the consequential enquiry decisions from the review. Update the existing local documents and index. Do not implement code or contact anyone. Keep existing decisions and their sources discoverable; the review is all the decision authority available.

## Project files

### AGENTS.md

```markdown
Decision index: docs/decisions.md. ADRs live in docs/product/adr,
docs/design/adr and docs/software/adr. Number independently within each directory.
There are no established business contexts within this single-site project.
Read relevant decisions through the index before changing a feature.
```

### docs/decisions.md

```markdown
# Decisions
- [Enquiry service](product/adr/0002-managed-enquiries.md)
- [Site navigation](design/adr/0004-navigation.md)
- [Hosting](software/adr/0007-hosting.md)
```

### docs/product/adr/0002-managed-enquiries.md

```markdown
# Use Web3Forms for enquiry delivery
Site-wide product decision, confirmed by Jules in [review](../enquiry-review.md).
Use the managed service rather than operate mail delivery because the small
team cannot support a mail service during the annual campaign. Provider
dependency is accepted; delivery beyond the current volume needs reconsideration.
```

### docs/product/enquiry-review.md

```markdown
# Enquiry review
Jules, product owner, 2026-10-08:
"Service selection remains as recorded in product ADR 0002. Enquiries require
name, reply email and message; we must preserve the draft when delivery fails."
Jules confirmed the team's new inline feedback/recovery design instead of a
replacement result page. The form stays visible, retains input on failure and
offers retry; success replaces the form with confirmation. This changes the
site's shared interaction pattern and reversing it entails redesigning all
enquiry entry points. The team chose continuity over a simpler result page.
Jules delegated technical submission architecture to the delivery team.
The team's agreed architecture is one server adapter for all enquiry entry
points, instead of direct browser submission. This keeps provider configuration
behind one boundary and gives one place to reconcile uncertain delivery before
retrying. It adds deployment/operating work; replacing it after launch changes
all integrations. No implementation has been built or exercised yet.
```

### docs/design/adr/0004-navigation.md

```markdown
# Keep one site navigation
Confirmed site-wide design decision. Reuse one navigation across the campaign
pages rather than distinct menus because the enquiry journey crosses them.
```

### docs/software/adr/0007-hosting.md

```markdown
# Keep the existing deployment target
Delegated site-wide software decision. Retain the current host through this
campaign rather than migrate infrastructure; migration cost exceeds the benefit.
```
