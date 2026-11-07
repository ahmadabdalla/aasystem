"""Synthetic local catalog importer."""

import csv
import sqlite3
import sys


def import_catalog(input_file, database):
    with open(input_file, newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != ["sku", "name"]:
            raise ValueError("Expected headers: sku,name")
        rows = list(reader)
    if any(not row["sku"].strip() or not row["name"].strip() for row in rows):
        raise ValueError("Every row needs a sku and name")
    with sqlite3.connect(database) as connection:
        connection.execute("CREATE TABLE IF NOT EXISTS products (sku TEXT PRIMARY KEY, name TEXT NOT NULL)")
        connection.executemany("INSERT INTO products (sku,name) VALUES (?,?)", [(row["sku"], row["name"]) for row in rows])
    return len(rows)


if __name__ == "__main__":
    try:
        count = import_catalog(sys.argv[1], sys.argv[2])
        print(f"Imported {count} products")
    except (ValueError, sqlite3.Error, OSError, IndexError) as error:
        print(f"Import failed: {error}", file=sys.stderr)
        sys.exit(2)
