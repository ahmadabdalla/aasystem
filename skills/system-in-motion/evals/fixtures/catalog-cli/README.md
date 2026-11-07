# Catalog importer (synthetic fixture)

An operator runs `python3 import_catalog.py catalog.csv products.db`. This is a local
CLI, not a web service or asynchronous job system. It uses Python's csv module and
SQLite. All input is validated before opening the database. Valid records are
inserted in a transaction; a duplicate SKU causes rollback rather than partial import.

The command prints a count on success, or writes an error to stderr and exits 2.
No email, browser, approval workflow, background queue or cloud is present. Inspect
the source to explain it; do not execute database writes for this exercise.
