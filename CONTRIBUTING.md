# Contribute to ADI Skills

Add a skill when a repeated task needs a stable procedure. Keep unrelated preferences in the project that needs them.

## Add a skill

1. Create `skills/<skill-name>/SKILL.md` with a lowercase, hyphenated folder name.
2. Add YAML frontmatter with a `name` that matches the folder and a `description` that says what the skill does and when to use it.
3. Put substantial conditional guidance in that skill's `references/` directory. Link each reference from `SKILL.md`.
4. Install or document every required dependency. Do not add an undeclared reference to a skill outside this repository.
5. Update the skill tables in `README.md` and `docs/SKILLS.md`, the repository counts, and `upstream/SOURCE.md` when adding third-party material.
6. Preserve the original license and attribution when copying third-party work.
7. Run `python scripts/validate_repo.py` from the repository root.
8. Test installation in a temporary directory before publishing the change.

The [technical-writing skill](./skills/technical-writing/SKILL.md) and the [unslop skill](./skills/unslop/SKILL.md) apply to documentation changes.

## Package layout

The repository root is both a plugin and a marketplace. The `skills/` directory is the only source of installable skills.

- `plugin.json` declares the portable Agent Plugins package.
- `.claude-plugin/plugin.json` declares the Claude Code plugin.
- `.claude-plugin/marketplace.json` exposes the plugin to Claude Code.
- `.codex-plugin/plugin.json` supplies Codex presentation metadata.
- `.agents/plugins/marketplace.json` exposes the plugin to Codex.
- `upstream/` preserves source and license information, not installable skills.

Keep plugin and marketplace versions consistent. The current version is `0.1.0` in each manifest.

## Validate a change

Run the repository validator:

```bash
python scripts/validate_repo.py
```

Validate the Claude plugin when Claude Code is available:

```bash
claude plugin validate . --strict
```

Test discovery with skills.sh:

```bash
npx skills add . --list
```

Install the package into a temporary directory. Do not overwrite an existing personal installation during a test. On Windows, set both `HOME` and `USERPROFILE` to the isolated directory for the test process. `skills.sh` resolves the global home from the operating system user profile, not only from `HOME`.
