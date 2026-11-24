---
name: prune-tests
description: Remove or rewrite tests that guard no intended behavior, and prove nothing still needed lost its coverage. Use when explicitly asked to prune or clean up a test suite, or when Refactoring assigns test pruning.
argument-hint: "[optional path]"
user-invocable: false
---

# Prune tests

Before starting, read the [execution contract](../pilot/references/execution.md) and the [approved-principle index](../principles/INDEX.md), unless already in context.

Prune within the caller's scope or the supplied path; with neither, ask for the scope before editing. [Verification clarity](../maintainability/references/local-code.md) defines a needed test. This skill owns the decision for each test, the edits and the proof.

## Classify each test

Name the behavior each test guards, then:

- **Keep** it when it fails on that behavior's regression and only then.
- **Rewrite** it against what callers see when it covers relied-on behavior but asserts private state, call order or values derived from the code's own logic.
- **Delete** it when no code change can fail it, when it repeats another test through the same entry point, or when it asserts removed code stays gone.

Keep an absence test a current contract requires, such as a removed endpoint returning 404; rewrite it against public behavior instead of a file check. Tests of one rule at different entry points, such as unit and API, are not duplicates. Keep type-guarantee tests at runtime boundaries such as parsed input or untyped callers. Prune only passing tests: classify a failing test as a defect or a stale expectation first, and report a defect to the caller instead of deleting the test.

## Prune and prove

1. Run the scoped tests and record the result with each test's guarded behavior.
2. Invoke the [`implement`](../implement/SKILL.md) skill to make the edits, or make them within the assigned scope. Remove production code used only by deleted tests.
3. Rerun the remaining tests. For each deletion, name the test that still guards its behavior, or why that behavior is not intended. Where cheap, introduce the regression the deleted test claimed to catch, confirm a remaining test fails, then revert it.
4. Record [signal effects](../pilot/references/execution.md#signal-effects): the coverage removed and any regression no longer detected.

## Return

Return deletions, rewrites and kept exceptions with reasons, the before and after runs, the regression checks and their limits, and any production code removed. The caller owns independent verification and delivery; when invoked directly, obtain it under [independent implementation verification](../pilot/references/verification-contract.md#independent-implementation-verification).

## Example

```diff
--- a/pricing.test.ts
+++ b/pricing.test.ts
@@ rewritten: the expected value repeated the code's logic @@
 test("applies the discount", () => {
-  const price = 100;
-  expect(applyDiscount(price, 0.2)).toBe(price - price * 0.2);
+  expect(applyDiscount(100, 0.2)).toBe(80);
 });
--- a/cart.test.ts
+++ b/cart.test.ts
@@ rewritten against what callers see: it asserted private state @@
 test("adds an item to the cart", () => {
   const cart = new Cart();
   cart.add(book);
-  expect(cart._items.length).toBe(1);
+  expect(cart.total()).toBe(book.price);
 });
@@ deleted: checkout.test.ts already guards the same total through the same entry point @@
-test("total includes tax", () => {
-  expect(cartTotal([book], { tax: 0.1 })).toBe(11);
-});
--- a/export.test.ts
+++ b/export.test.ts
@@ deleted: no current contract requires the old file to stay absent @@
-test("legacy exporter is gone", () => {
-  expect(existsSync("src/export/legacy.ts")).toBe(false);
-});
--- a/session.test.ts
+++ b/session.test.ts
@@ deleted, with the production code that only existed for it @@
-test("clears the cache", () => {
-  _resetCacheForTests();
-  expect(_getCacheSize()).toBe(0);
-});
--- a/session.ts
+++ b/session.ts
@@ @@
-export function _resetCacheForTests() { cache.clear(); }
-export function _getCacheSize() { return cache.size; }
```
