---
name: verify-ledger
description: Exercise Ledger's accepted CLI behavior and persisted effects in isolated local stores.
---

# Verify Ledger

Read the [accepted contract](../README.md) and [feature map](features/README.md). Run from the project root using Python 3.11 or newer. Identify the tested source by hashing `ledger.py`, `test_cli.py`, and any imported local module. Record the interpreter version and project path. Every product action is a fresh `python3 ledger.py --store PATH ...` process against your own temporary store. No server is needed.

First run `python3 -m unittest -v`; its smoke coverage is narrower than the contract. Then drive the affected cases below, recording exact commands, exit codes, stdout, stderr, expected observations, actual observations, and stored bytes or file absence. Derive expected observations from the contract.

1. On a missing nested store, list entries, preview a message, then add it. Inspect file and parent-directory existence after each action; list and preview leave both absent, while add persists entry 1.
2. Save two entries. Capture store bytes, preview a third, compare bytes, then list and add the third in fresh processes. The preview returns entry 3; the saved entries remain two until add, which persists entry 3.
3. Use a second independent store. Its first add starts at 1 and leaves the first store unchanged.
4. Write malformed JSON to your own store. Run list, add, and preview separately, restoring the same malformed bytes before each action. Each exits 2 with `Invalid ledger` on stderr and preserves the bytes.

Write evidence to an owned temporary output directory outside the source tree. Remove only the temporary stores you created and confirm retained evidence survives. No product process should remain. A command launch failure is a procedure or access gap; an observed contract violation is a product failure. A source inspection or passing smoke test cannot establish unexercised side effects. Return pass, fail, and unverified outcomes separately; do not edit the product while assigned verification.
