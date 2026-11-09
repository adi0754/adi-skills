# Host adaptation

Use this guide when a skill names a Cursor tool, model, or invocation. Apply the current user's instructions and the host's actual tool schemas first. Never invent a model identifier or agent type.

## Paths

`<adi-skills>` is the directory that contains this repository's `skills/` and `references/` directories. In Claude Code, use `${CLAUDE_PLUGIN_ROOT}` when the host provides it. For a standalone skills.sh installation, locate the shared `references/` directory beside `skills/` in the installed package.

A reference link from `skills/<name>/SKILL.md` to `../../references/<file>` resolves inside this package. Read that file directly. A reference link to `../<other-skill>/SKILL.md` resolves to another selected skill in the same package.

## Tools

| Original name | Claude Code | Codex |
| --- | --- | --- |
| `Task` subagent | `Agent` | The available collaboration or subagent tool |
| `subagent_type: generalPurpose` | `subagent_type: "general-purpose"` | The available general-purpose agent |
| `readonly: true` | A read-only agent type, or an explicit read-only brief | An explicit read-only brief |
| Open a todolist | `TodoWrite` when available | The available plan or task-list mechanism |
| `AskQuestion` | `AskUserQuestion` when available | The available user-input mechanism |

If subagents or a named tool are unavailable, perform the investigation in the main session and disclose the limitation. Do not bypass a user or project rule that prohibits delegation.

## Models

Use a model available in the current host. In Cursor, an optional `pstack-models.mdc` role line can select a model. In other hosts, omit unavailable Cursor model identifiers and choose from the host's actual tool schema. Preserve the requested role, such as explorer, candidate, judge, or synthesizer. Disclose substitutions that change the workflow's independence or evidence quality.

## Invocation

In Claude Code, invoke a plugin skill as `/adi-skills:<skill-name>`. To follow another skill or workflow as part of the current task, read its `SKILL.md` or Markdown reference directly. Do not require a missing skill from the upstream pstack plugin.

Cursor-specific automations, cloud agents, and editor-only tools are optional. Use a host-supported equivalent or report the skipped check. Do not stop unrelated work because one optional integration is unavailable.
