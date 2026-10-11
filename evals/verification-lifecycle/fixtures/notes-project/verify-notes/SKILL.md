---
name: verify-notes
description: Verify Notes CLI creation and readback using disposable stores.
---

# Verify Notes

Run from the project root using Python 3. Hash `notes.py` before driving and confirm each invocation targets that file and your own store. This CLI has no server. Create a temporary data directory for the run and start each command as a fresh process. Use the [feature index](features/README.md) and [accepted contract](../README.md) to select checks and expected results.

Capture commands, stdout, stderr, exit status and relevant stored state in a separate output directory. Remove only the data directory you created when finished, including after a failure, and confirm captured output still exists. No persistent process should remain. Launch/identity failures are procedure gaps; observed contract violations are product failures.
