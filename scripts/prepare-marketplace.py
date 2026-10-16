#!/usr/bin/env python3
"""Prepare two catalog files; the workflow validates them and opens the PR."""
import json
import os
from pathlib import Path
import re
import subprocess
import sys


CATALOG = ".claude-plugin/marketplace.json"
BRANCH = "refs/remotes/origin/automation/aasystem-release"


def version_number(version):
    if not re.fullmatch(r"(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)", version):
        raise ValueError(f"Invalid stable version: {version}")
    return tuple(map(int, version.split(".")))


def aasystem(catalog):
    return next(plugin for plugin in catalog["plugins"] if plugin["name"] == "aasystem")


def prepare(version):
    candidate = version_number(version)
    original = Path(CATALOG).read_text()
    catalog = json.loads(original)
    plugin = aasystem(catalog)
    current = plugin["version"]
    if candidate <= version_number(current):
        print(f"Catalog already has {current}; skipping {version}.")
        return False

    pending = subprocess.run(["git", "show-ref", "--verify", "--quiet", BRANCH])
    if pending.returncode == 0:
        contents = subprocess.check_output(["git", "show", f"{BRANCH}:{CATALOG}"], text=True)
        if candidate < version_number(aasystem(json.loads(contents))["version"]):
            print(f"A newer adoption is pending; skipping {version}.")
            return False
    elif pending.returncode != 1:
        raise ValueError("Cannot inspect the pending adoption branch")

    plugin["version"] = version
    plugin["source"]["ref"] = f"v{version}"
    # Preserve catalog formatting and every other entry; verify the resulting JSON.
    prefix, entry = original.split('"name": "aasystem"', 1)
    entry = entry.replace(f'"v{current}"', f'"v{version}"', 1).replace(f'"{current}"', f'"{version}"', 1)
    updated = prefix + '"name": "aasystem"' + entry
    if json.loads(updated) != catalog:
        raise ValueError("Catalog format changed; update the aasystem entry manually")
    readme, count = re.subn(r"(?m)^(\| \[aasystem\][^\n]*\| )[^|\n]+(\|)$",
                            rf"\g<1>{version} \2", Path("README.md").read_text())
    if count != 1:
        raise ValueError("Expected one aasystem version row in README.md")
    Path(CATALOG).write_text(updated)
    Path("README.md").write_text(readme)
    return True


if __name__ == "__main__":
    try:
        changed = prepare(sys.argv[1])
        with open(os.environ["GITHUB_OUTPUT"], "a") as output:
            output.write(f"changed={str(changed).lower()}\n")
    except (OSError, ValueError, KeyError, StopIteration, subprocess.CalledProcessError) as error:
        sys.exit(f"FAIL: {error}")
