#!/usr/bin/env python3
"""Package checks only; real host installation and invocation are separate."""
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote

import yaml


ROOT = Path(__file__).resolve().parents[1]
SYSTEM_MAP = Path("docs/design/skill-system.md")


def check(condition, message):
    if not condition:
        raise ValueError(message)


def read(path):
    return Path(path).read_text(encoding="utf-8")


def parse_yaml(source, path):
    try:
        return yaml.safe_load(source)
    except yaml.YAMLError as error:
        raise ValueError(f"Invalid YAML in {path}: {error}") from error


def validate_skill(path):
    frontmatter = re.match(r"\A---\s*\n(.*?)\n---\s*\n", read(path), re.DOTALL)
    check(frontmatter, f"Missing metadata: {path}")
    metadata = parse_yaml(frontmatter[1], path)
    check(isinstance(metadata, dict), f"Metadata must be a mapping: {path}")
    check(metadata.get("name") == Path(path).parent.name, f"Skill name differs from directory: {path}")
    description = metadata.get("description")
    check(isinstance(description, str) and description.strip(), f"Missing description: {path}")
    check(metadata.get("disable-model-invocation") is True, f"Explicit invocation policy missing: {path}")
    adapter_path = Path(path).parent / "agents/openai.yaml"
    adapter = parse_yaml(read(adapter_path), adapter_path)
    policy = adapter.get("policy") if isinstance(adapter, dict) else None
    check(isinstance(policy, dict) and policy.get("allow_implicit_invocation") is False,
          f"Adapter invocation policy differs: {path}")


def validate_local_links(documents):
    # Only these two documented authoring placeholders are exempt from path checks.
    placeholders = {
        "skills/bootstrap-verification/references/project-instructions.md": {"VERIFIER_PATH", "MAP_PATH"},
    }
    links = 0
    for path in documents:
        source = re.sub(r"```.*?```", "", read(path), flags=re.DOTALL)
        for target in re.findall(r'\]\(([^\s)]+)(?:\s+"[^"\n]*")?\)', source):
            if re.match(r"[a-z][a-z0-9+.-]*:", target, re.IGNORECASE) or target.startswith("#"):
                continue
            target = unquote(target.split("#", 1)[0].removeprefix("<").removesuffix(">"))
            if target in placeholders.get(path.as_posix(), set()):
                continue
            check((path.parent / target).exists(), f"Missing link target in {path}: {target}")
            links += 1
    return links


def validate():
    os.chdir(ROOT)
    portable = json.loads(read("plugin.json"))
    claude = json.loads(read(".claude-plugin/plugin.json"))
    check(portable["name"] == "aasystem", "Installation identity must remain aasystem")
    version = portable["version"]
    check(isinstance(version, str) and re.fullmatch(r"(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)", version),
          "Use a stable X.Y.Z version")
    for key in ("name", "version"):
        check(portable[key] == claude[key], f"Manifest {key} values differ")

    required = (
        "README.md", SYSTEM_MAP, "docs/ops/codex.md", "docs/ops/releasing.md", "LICENSE", "PSTACK_LICENSE.txt",
        "MATT_POCOCK_LICENSE.txt", "skills/principles/INDEX.md", "skills/aapilot/SKILL.md",
        "skills/aapilot/agents/openai.yaml",
    )
    for path in required:
        check(Path(path).is_file(), f"Missing export file: {path}")
    check(not Path("skills/aasystem").exists(), "Former entry point must not remain")

    skills = sorted(path.as_posix() for path in Path("skills").glob("*/SKILL.md"))
    check(skills, "Skill tree is empty")
    for path in skills:
        validate_skill(path)

    # The system inventory links every portable skill, catching incomplete exports.
    inventory = {
        (SYSTEM_MAP.parent / target).resolve().relative_to(ROOT).as_posix()
        for target in re.findall(r"\]\(((?:\.\./)*skills/[^)]+/SKILL\.md)\)", read(SYSTEM_MAP))
    }
    check(sorted(inventory) == skills, "System inventory and portable skill tree differ")

    documents = (
        sorted(Path("skills").glob("**/*.md"))
        + sorted(Path("docs").glob("**/*.md"))
        + list(map(Path, ("README.md", "AGENTS.md", "CHANGELOG.md")))
    )
    links = validate_local_links(documents)

    notes = re.split(rf"^## \[{re.escape(version)}\]\s*$", read("CHANGELOG.md"), maxsplit=1, flags=re.MULTILINE)
    check(len(notes) == 2 and re.split(r"^## \[", notes[1], maxsplit=1, flags=re.MULTILINE)[0].strip(),
          "Missing versioned release notes")
    guard = "skills/bootstrap-verification/assets/check-verification-output.sh"
    check(subprocess.run(["sh", "-n", guard]).returncode == 0, "Shipped helper syntax failed")
    check(subprocess.run(["sh", guard]).returncode == 0, "Verification output guard failed")
    print(f"PASS: aasystem {version}; {len(skills)} skills and adapters; {links} local link paths; release notes.")
    print("Host installation, invocation, workflow evaluations and link anchors are separate checks.")


if __name__ == "__main__":
    try:
        validate()
    except (OSError, ValueError, KeyError, TypeError, yaml.YAMLError) as error:
        sys.exit(f"FAIL: {error}")
