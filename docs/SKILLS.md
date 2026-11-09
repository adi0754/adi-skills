# Skill reference

Use the name to select a skill during installation or invocation. Each link opens the skill's instructions.

### Workflows / 工作流程

| skill / 技能 | use it when / 使用它 |
| --- | --- |
| [`architect`](../skills/architect/SKILL.md) | Compare designs before implementation, then define types, interfaces, and module boundaries. |
| [`arena`](../skills/arena/SKILL.md) | Generate independent candidates, compare them against a rubric, and synthesize the result. |
| [`blast-radius`](../skills/blast-radius/SKILL.md) | Find what a change could break beyond its diff, and verify the key safety claim by running code. |
| [`how`](../skills/how/SKILL.md) | Explain how a subsystem works, how execution flows, and where responsibilities belong. |
| [`why`](../skills/why/SKILL.md) | Trace why a design, threshold, or historical decision exists using cited evidence. |
| [`teach`](../skills/teach/SKILL.md) | Understand a change or subsystem, including how it works and why it has its current shape. |

### Architecture and design / 架构与设计

| skill / 技能 | use it when / 使用它 |
| --- | --- |
| [`principle-foundational-thinking`](../skills/principle-foundational-thinking/SKILL.md) | Choose data structures, core types, and shared-state boundaries before writing logic. |
| [`principle-model-the-domain`](../skills/principle-model-the-domain/SKILL.md) | Encode domain rules in data structures instead of scattered conditionals. |
| [`principle-exhaust-the-design-space`](../skills/principle-exhaust-the-design-space/SKILL.md) | Compare two or three genuinely different designs when the codebase has no precedent. |

### Verification and debugging / 验证与排障

| skill / 技能 | use it when / 使用它 |
| --- | --- |
| [`principle-prove-it-works`](../skills/principle-prove-it-works/SKILL.md) | Verify the actual artifact and behavior before declaring work complete. |
| [`principle-sequence-verifiable-units`](../skills/principle-sequence-verifiable-units/SKILL.md) | Split multi-step work into small units that each end in a verifiable state. |
| [`principle-test-behavior-not-implementation`](../skills/principle-test-behavior-not-implementation/SKILL.md) | Test observable behavior instead of internal implementation details. |
| [`principle-fix-root-causes`](../skills/principle-fix-root-causes/SKILL.md) | Trace a defect to its origin instead of masking it with another guard. |
| [`principle-attack-the-premise`](../skills/principle-attack-the-premise/SKILL.md) | Test the shared premise after repeated fixes fail the same check. |
| [`principle-explain-the-number`](../skills/principle-explain-the-number/SKILL.md) | Check that a measured number represents the claimed work before reporting or acting on it. |

### Implementation and code quality / 实现与代码质量

| skill / 技能 | use it when / 使用它 |
| --- | --- |
| [`principle-laziness-protocol`](../skills/principle-laziness-protocol/SKILL.md) | Prefer the smallest change that solves the current problem. |
| [`principle-minimize-reader-load`](../skills/principle-minimize-reader-load/SKILL.md) | Reduce indirection and hidden state that make code hard to understand. |
| [`principle-subtract-before-you-add`](../skills/principle-subtract-before-you-add/SKILL.md) | Remove dead code and redundant rules before adding more logic. |
| [`principle-build-the-lever`](../skills/principle-build-the-lever/SKILL.md) | Turn repeated or reviewable work into a script or tool that another person can rerun. |

### Replies and documentation / 回复与文档

| skill / 技能 | use it when / 使用它 |
| --- | --- |
| [`bro`](../skills/bro/SKILL.md) | Restate the last answer in plain language without jargon. |
| [`in-your-own-words`](../skills/in-your-own-words/SKILL.md) | Have the agent restate your goal and the problem before work begins. |
| [`ketchup`](../skills/ketchup/SKILL.md) | Catch up on changes since your last message and every decision waiting for you. |
| [`technical-writing`](../skills/technical-writing/SKILL.md) | Write or review READMEs, design documents, RFCs, and commit messages. |
| [`unslop`](../skills/unslop/SKILL.md) | Remove AI writing patterns, filler, and vague language from documents. |