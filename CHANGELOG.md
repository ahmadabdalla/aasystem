# Changelog

## [0.2.0]

- Rename the main skill to `aapilot`: use `$aasystem:aapilot` in Codex or `/aasystem:aapilot` in Claude Code. The old `$aasystem:aasystem` and `/aasystem:aasystem` invocations have no alias.
- Use Ahmad Abdalla's Pilot System branding. The installation name remains `aasystem@ahmadabdalla-plugins`.
- Direct skill installations use `$aapilot`. Supporting skills and invocation policies stay the same.
- Add package checks and manual publication of versioned releases from the exact validated, merged commit.

Once the marketplace adopts `v0.2.0`, follow the [upgrade instructions](RELEASING.md#upgrade-an-installed-plugin) and start a fresh session. This also applies to the temporary `0.1.0` install that already exposes `aapilot`.

Release notes link the host check results and any gaps. Full workflow evaluation remains separate.
