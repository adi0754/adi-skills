# Upstream provenance

The 26 skills in `skills/` come from [Cursor's pstack](https://github.com/cursor/plugins/tree/main/pstack).

- Source commit: [`c742dd61706fbacc1b95f1a20b7b988cf096ce6c`](https://github.com/cursor/plugins/commit/c742dd61706fbacc1b95f1a20b7b988cf096ce6c)
- Source date: 2026-10-27
- Upstream license: [MIT](./LICENSE)
- Collection maintained by: [ADI](https://github.com/adi0754)

ADI selected the skills, adapted host-specific instructions and dependency paths, and added the installation manifests, documentation, and validation. The original MIT license and copyright notice remain in this repository.

The root `skills/` directory contains the 24 selected skills plus `arena` and `unslop`, which are required by selected skills. Host-specific instructions and missing optional dependencies are adapted locally.

`create-formal-verification-skill` uses the included `statechart` skill rather than the unselected `maintain-formal-verification-skill` skill. `statechart/scripts/run.ts` additionally accepts Windows CRLF output when reading TLC logs. The upstream process-management and test code remains unchanged.
