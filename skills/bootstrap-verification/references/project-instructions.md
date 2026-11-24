# Connect verification to normal project work

Reuse the project's existing instruction routing where it works. Otherwise add the smallest entry that does the job to the established instruction file, following directory ownership in larger repositories. Keep toolbox skills out of the project.

Replace `VERIFIER_PATH` and `MAP_PATH` with real relative paths before installing.

> For changes affecting product behaviour, read [the project verifier](VERIFIER_PATH) and its [feature map](MAP_PATH). Before implementing, pick checks for the changed behaviour, its other entry points and affected dependencies, taking expected results from the request or contract, not the code. Run them on the final change and report pass, fail and unverified separately. If intended behaviour or the procedure changes, update the affected recipes. If a check can't run, report what's missing; an unrelated pass doesn't close the gap.

Link the real tests and scripts that enforce the contract.

If the project has a glossary or ADRs, keep or add a short pointer to read the relevant ones before changing that area. Don't create empty records.

For user-facing work, also point to the product purpose, journey map and interaction records that exist, and say when each is needed:

- outcomes and their authority, before changing behaviour
- interaction decisions, before changing navigation, workflow or what users can see

In the verifier, link requirements; don't copy business rules.

Finally, read the installed entry and follow its links from the project. Then test it: give a fresh-context agent a change request that doesn't mention verification, and check that it finds and follows the verifier.
