<p align="center">
  <img src="./assets/adi-mark.svg" width="88" alt="ADI Skills logo" />
</p>

<h1 align="center">ADI Skills</h1>

<p align="center">Understand first. Prove the result.</p>
<p align="center">先理解，再验证。ADI 精选的 Agent Skills。</p>

<p align="center">
  <img src="https://img.shields.io/badge/skills-26-5B5CE2" alt="26 skills" />
  <img src="https://img.shields.io/badge/install-skills.sh%20%7C%20Claude%20%7C%20Codex-181818" alt="Install with skills.sh, Claude, or Codex" />
  <a href="./LICENSE"><img src="https://img.shields.io/badge/license-MIT-2E7D32" alt="MIT license" /></a>
</p>

A curated collection for code investigation, design, verification, and technical communication. ADI selects each skill and keeps the installation simple.

ADI 精选的代码调研、方案设计、行为验证和技术沟通技能。按需挑选，或一次安装整套。

## Installation / 安装

Pick one method per agent. Plugins include all 26 skills. Use skills.sh to choose individual skills and their dependencies.

每个客户端选择一种安装方式。插件包含全部 26 个技能；按需挑选时使用 skills.sh，并同时安装相关依赖。

### skills.sh / 全局安装

Install the complete collection for Codex:

为 Codex 全局安装全部技能：

```bash
npx skills add adi0754/adi-skills -g --agent codex --skill '*'
```

For Claude Code, replace `codex` with `claude-code`. To select skills, replace `'*'` with their names.

为 Claude Code 安装时将 `codex` 改为 `claude-code`。按需安装时将 `'*'` 换成技能名称。

```bash
npx skills add adi0754/adi-skills -g --agent codex --skill how why teach
```

skills.sh stores Codex skills in `~/.agents/skills/` and Claude Code skills in `~/.claude/skills/`. Review the installation plan before confirming it, especially when a skill with the same name exists. Update with `npx skills update -g`.

Codex 的全局目录为 `~/.agents/skills/`，Claude Code 为 `~/.claude/skills/`。确认安装前先检查同名技能，更新时执行 `npx skills update -g`。

### Claude Code plugin / Claude 插件

```bash
claude plugin install adi-skills --marketplace adi0754/adi-skills --scope user
```

In `/plugin`, open **Marketplaces**, select `adi-skills`, and choose **Enable auto-update**. Claude Code refreshes it when a session starts. Restart or run `/reload-plugins` after an update.

在 `/plugin` 的 **Marketplaces** 中选择 `adi-skills`，再开启 **Enable auto-update**。Claude Code 会在会话启动后刷新插件，更新后重启或执行 `/reload-plugins`。

Invoke a skill as `/adi-skills:<skill-name>`, for example `/adi-skills:how`.

使用 `/adi-skills:<skill-name>` 调用技能，例如 `/adi-skills:how`。

### Codex plugin / Codex 插件

```bash
codex plugin marketplace add adi0754/adi-skills
codex plugin add adi-skills@adi-skills
```

Codex updates plugins at startup. Restart Codex, then start a new task.

Codex 会在启动时更新插件。安装后重启 Codex，再新建任务。

## Choose a skill / 选择技能

### Workflows / 工作流程

| skill / 技能 | use it when / 使用它 |
| --- | --- |
| [`architect`](./skills/architect/SKILL.md) | 在编码前比较多个设计，确定类型、接口和模块边界。 |
| [`arena`](./skills/arena/SKILL.md) | 需要多个独立候选方案，并按明确标准择优和合并。 |
| [`blast-radius`](./skills/blast-radius/SKILL.md) | 需要确认一个小改动会不会破坏其他调用方或业务流程。 |
| [`how`](./skills/how/SKILL.md) | 需要弄清现有系统如何工作、调用链怎样运行、代码属于哪一层。 |
| [`why`](./skills/why/SKILL.md) | 需要追查某个设计、阈值或历史决策为什么形成。 |
| [`teach`](./skills/teach/SKILL.md) | 需要真正理解一个改动或子系统，包括现状、原理和历史原因。 |

### Architecture and design / 架构与设计

| skill / 技能 | use it when / 使用它 |
| --- | --- |
| [`principle-foundational-thinking`](./skills/principle-foundational-thinking/SKILL.md) | 编写逻辑前需要确定数据结构、核心类型和共享状态。 |
| [`principle-model-the-domain`](./skills/principle-model-the-domain/SKILL.md) | 状态逻辑散落在条件分支中，需要模型直接表达业务规则。 |
| [`principle-exhaust-the-design-space`](./skills/principle-exhaust-the-design-space/SKILL.md) | 面对没有现成先例的交互或架构，需要比较不同整体方案。 |

### Verification and debugging / 验证与排障

| skill / 技能 | use it when / 使用它 |
| --- | --- |
| [`statechart`](./skills/statechart/SKILL.md) | 需要穷举状态转换中的规则违例，并把最短异常路径画成状态图。 |
| [`create-formal-verification-skill`](./skills/create-formal-verification-skill/SKILL.md) | 需要为高风险、普通测试难覆盖的逻辑建立可重复运行的形式化验证。 |
| [`principle-prove-it-works`](./skills/principle-prove-it-works/SKILL.md) | 宣布完成前，需要检查真实运行结果和最终产物。 |
| [`principle-sequence-verifiable-units`](./skills/principle-sequence-verifiable-units/SKILL.md) | 多步骤需求需要拆成可独立验证的小批次。 |
| [`principle-test-behavior-not-implementation`](./skills/principle-test-behavior-not-implementation/SKILL.md) | 需要测试用户可观察的行为，而不是绑定私有实现。 |
| [`principle-fix-root-causes`](./skills/principle-fix-root-causes/SKILL.md) | 排查故障时需要定位最早出错的位置，而不是继续加表面兜底。 |
| [`principle-attack-the-premise`](./skills/principle-attack-the-premise/SKILL.md) | 多次修复基于同一假设却反复失败，需要直接验证假设。 |
| [`principle-explain-the-number`](./skills/principle-explain-the-number/SKILL.md) | 报告性能、延迟、吞吐或评测数据前，需要确认测量可信。 |

### Implementation and code quality / 实现与代码质量

| skill / 技能 | use it when / 使用它 |
| --- | --- |
| [`principle-laziness-protocol`](./skills/principle-laziness-protocol/SKILL.md) | 需要控制改动范围，避免为了假想需求增加抽象和兼容层。 |
| [`principle-minimize-reader-load`](./skills/principle-minimize-reader-load/SKILL.md) | 代码跳转过多、隐式状态太多，已经难以理解或审查。 |
| [`principle-subtract-before-you-add`](./skills/principle-subtract-before-you-add/SKILL.md) | 新增或重构前，需要先清理死代码和多余约束。 |
| [`principle-build-the-lever`](./skills/principle-build-the-lever/SKILL.md) | 重复、复杂或需复核的工作值得写成可重跑的脚本或检查。 |

### Replies and documentation / 回复与文档

| skill / 技能 | use it when / 使用它 |
| --- | --- |
| [`bro`](./skills/bro/SKILL.md) | 需要把上一条技术回答改成直白、无术语的大白话。 |
| [`in-your-own-words`](./skills/in-your-own-words/SKILL.md) | 开始任务前，需要 AI 复述目标和问题以暴露理解偏差。 |
| [`ketchup`](./skills/ketchup/SKILL.md) | 离开一段时间后，需要知道发生了什么，以及哪些决定仍在等你。 |
| [`technical-writing`](./skills/technical-writing/SKILL.md) | 编写或审查 README、技术方案、RFC、提交说明等文档。 |
| [`unslop`](./skills/unslop/SKILL.md) | 需要去掉文档里的 AI 腔、套话和模糊表达。 |

[English skill reference](./docs/SKILLS.md)

## Dependencies and compatibility / 依赖与兼容性

`create-formal-verification-skill` uses `statechart` to read TLA+ results. `architect` needs `how`, `why`, and `arena`. `teach` needs `how`, `why`, and `unslop`. `technical-writing` needs `unslop`. Plugins include all dependencies. Install them explicitly when selecting individual skills.

`create-formal-verification-skill` 使用 `statechart` 解读 TLA+ 结果；`architect` 依赖 `how`、`why`、`arena`；`teach` 依赖 `how`、`why`、`unslop`；`technical-writing` 依赖 `unslop`。插件已包含依赖，按需安装时请一并选择。

`statechart` needs a compatible TypeScript runtime and TLC. It downloads TLC and Java with `mise` on first use, or accepts `TLA2TOOLS` and `JAVA` from the local environment. `mise` is not bundled.

Some skills use subagents, MCP servers, or other host tools. The [host adaptation guide](./docs/harness/host-adaptation.md) explains how to use available tools without assuming a Cursor-specific environment. Missing tools can limit parallel investigation or external evidence collection.

`statechart` 需要兼容的 TypeScript 运行时和 TLC。首次使用默认通过 `mise` 下载 TLC 与 Java，也可使用本机 `TLA2TOOLS`、`JAVA` 环境变量；`mise` 不随插件打包。

部分技能使用子代理、MCP 或其他客户端工具。[客户端适配说明](./docs/harness/host-adaptation.md) 说明了对应关系。客户端缺少相关工具时，并行调查和外部资料收集会受到限制。

## Maintain this collection / 维护这个仓库

Add each new skill under `skills/<skill-name>/SKILL.md`. See [the contribution guide](./CONTRIBUTING.md) for naming, dependency, validation, and release steps.

在 `skills/<skill-name>/SKILL.md` 中添加新技能。命名、依赖、验证和发布步骤见[贡献指南](./CONTRIBUTING.md)。

## Source and license / 来源与许可

The selected skills come from [Cursor's pstack](https://github.com/cursor/plugins/tree/main/pstack). ADI selected and adapted them for this collection. See [upstream provenance](./upstream/SOURCE.md) for the source commit and local adaptations.

本集合由 ADI 从 [Cursor pstack](https://github.com/cursor/plugins/tree/main/pstack) 精选并适配。源提交及本地调整见[上游来源说明](./upstream/SOURCE.md)。

The upstream MIT license and copyright notice are preserved in [LICENSE](./LICENSE).

[LICENSE](./LICENSE) 保留了上游 MIT 许可证及版权声明。
