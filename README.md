<p align="center">
  <img src="./assets/adi-mark.svg" width="88" alt="ADI Skills logo" />
</p>

<h1 align="center">ADI Skills</h1>

<p align="center">Understand first. Prove the result.</p>
<p align="center">先理解，再验证。ADI 维护的个人 Agent Skills 集合。</p>

<p align="center">
  <img src="https://img.shields.io/badge/skills-24-5B5CE2" alt="24 skills" />
  <img src="https://img.shields.io/badge/install-skills.sh%20%7C%20Claude%20%7C%20Codex-181818" alt="Install with skills.sh, Claude, or Codex" />
  <a href="./LICENSE"><img src="https://img.shields.io/badge/license-MIT-2E7D32" alt="MIT license" /></a>
</p>

Use these skills to investigate existing code, compare designs, control change scope, verify behavior, and explain technical work. The collection includes 22 selected pstack skills and their `arena` and `unslop` dependencies.

这些技能覆盖代码调研、方案设计、影响面检查、行为验证和技术讲解。集合包含 22 个精选 pstack 技能，以及它们依赖的 `arena` 和 `unslop`。

## Install / 安装

Choose one installation method. Plugin installation includes all 24 skills. Use skills.sh to select individual skills.

选择一种安装方式。插件一次安装全部 24 个技能；需要按需选择时使用 skills.sh。

### skills.sh

List the available skills without installing them:

只列出技能，不执行安装：

```bash
npx skills add adi0754/adi-skills --list
```

Install the complete collection for Codex. skills.sh stores these skills in `~/.agents/skills/` (`~\.agents\skills` on Windows):

为 Codex 全局安装全部技能，目录为 `~/.agents/skills/`（Windows 为 `~\.agents\skills`）：

```bash
npx skills add adi0754/adi-skills -g --agent codex --skill '*'
```

Install selected skills for Codex:

为 Codex 按需安装技能：

```bash
npx skills add adi0754/adi-skills -g --agent codex --skill how why teach
```

Install the complete collection for Claude Code. skills.sh stores these skills in `~/.claude/skills/` (`~\.claude\skills` on Windows):

为 Claude Code 全局安装全部技能，目录为 `~/.claude/skills/`（Windows 为 `~\.claude\skills`）：

```bash
npx skills add adi0754/adi-skills -g --agent claude-code --skill '*'
```

Install selected skills for Claude Code:

为 Claude Code 按需安装技能：

```bash
npx skills add adi0754/adi-skills -g --agent claude-code --skill how why teach
```

Review the installation plan before confirming it. skills.sh can replace a skill with the same name. Restart the client or start a new session after installation, then check the discovered skills before invoking one.

先检查安装计划再确认。skills.sh 可能替换同名技能。安装后重启客户端或开始新会话，再检查技能是否已被发现。

### Claude Code plugin / Claude 插件

```bash
claude plugin install adi-skills --marketplace adi0754/adi-skills --scope user
```

Invoke a skill as `/adi-skills:<skill-name>`, for example `/adi-skills:how`.

使用 `/adi-skills:<skill-name>` 调用技能，例如 `/adi-skills:how`。

### Codex plugin / Codex 插件

```bash
codex plugin marketplace add adi0754/adi-skills
codex plugin add adi-skills@adi-skills
```

Restart Codex after installation, then start a new task. The [official Codex plugin guide](https://developers.openai.com/plugins/build/plugins) explains local and remote marketplaces.

安装后重启 Codex，再新建任务。[Codex 插件官方文档](https://developers.openai.com/plugins/build/plugins) 说明了本地和远程 marketplace 的使用方式。

## Choose a skill / 选择技能

| skill / 技能 | use it when / 使用它 |
| --- | --- |
| [`architect`](./skills/architect/SKILL.md) | 在编码前比较多个设计，确定类型、接口和模块边界。 |
| [`arena`](./skills/arena/SKILL.md) | 需要多个独立候选方案，并按明确标准择优和合并。 |
| [`blast-radius`](./skills/blast-radius/SKILL.md) | 需要确认一个小改动会不会破坏其他调用方或业务流程。 |
| [`bro`](./skills/bro/SKILL.md) | 需要把上一条技术回答改成直白、无术语的大白话。 |
| [`how`](./skills/how/SKILL.md) | 需要弄清现有系统如何工作、调用链怎样运行、代码属于哪一层。 |
| [`in-your-own-words`](./skills/in-your-own-words/SKILL.md) | 开始任务前，需要 AI 复述目标和问题以暴露理解偏差。 |
| [`ketchup`](./skills/ketchup/SKILL.md) | 离开一段时间后，需要知道发生了什么，以及哪些决定仍在等你。 |
| [`teach`](./skills/teach/SKILL.md) | 需要真正理解一个改动或子系统，包括现状、原理和历史原因。 |
| [`technical-writing`](./skills/technical-writing/SKILL.md) | 编写或审查 README、技术方案、RFC、提交说明等文档。 |
| [`unslop`](./skills/unslop/SKILL.md) | 需要去掉文档里的 AI 腔、套话和模糊表达。 |
| [`why`](./skills/why/SKILL.md) | 需要追查某个设计、阈值或历史决策为什么形成。 |
| [`principle-attack-the-premise`](./skills/principle-attack-the-premise/SKILL.md) | 多次修复基于同一假设却反复失败，需要直接验证假设。 |
| [`principle-build-the-lever`](./skills/principle-build-the-lever/SKILL.md) | 重复、复杂或需复核的工作值得写成可重跑的脚本或检查。 |
| [`principle-exhaust-the-design-space`](./skills/principle-exhaust-the-design-space/SKILL.md) | 面对没有现成先例的交互或架构，需要比较不同整体方案。 |
| [`principle-explain-the-number`](./skills/principle-explain-the-number/SKILL.md) | 报告性能、延迟、吞吐或评测数据前，需要确认测量可信。 |
| [`principle-fix-root-causes`](./skills/principle-fix-root-causes/SKILL.md) | 排查故障时需要定位最早出错的位置，而不是继续加表面兜底。 |
| [`principle-foundational-thinking`](./skills/principle-foundational-thinking/SKILL.md) | 编写逻辑前需要确定数据结构、核心类型和共享状态。 |
| [`principle-laziness-protocol`](./skills/principle-laziness-protocol/SKILL.md) | 需要控制改动范围，避免为了假想需求增加抽象和兼容层。 |
| [`principle-minimize-reader-load`](./skills/principle-minimize-reader-load/SKILL.md) | 代码跳转过多、隐式状态太多，已经难以理解或审查。 |
| [`principle-model-the-domain`](./skills/principle-model-the-domain/SKILL.md) | 状态逻辑散落在条件分支中，需要模型直接表达业务规则。 |
| [`principle-prove-it-works`](./skills/principle-prove-it-works/SKILL.md) | 宣布完成前，需要检查真实运行结果和最终产物。 |
| [`principle-sequence-verifiable-units`](./skills/principle-sequence-verifiable-units/SKILL.md) | 多步骤需求需要拆成可独立验证的小批次。 |
| [`principle-subtract-before-you-add`](./skills/principle-subtract-before-you-add/SKILL.md) | 新增或重构前，需要先清理死代码和多余约束。 |
| [`principle-test-behavior-not-implementation`](./skills/principle-test-behavior-not-implementation/SKILL.md) | 需要测试用户可观察的行为，而不是绑定私有实现。 |

[English skill reference](./docs/SKILLS.md)

## Dependencies and compatibility / 依赖与兼容性

`architect` uses `how`, `why`, and `arena`. `teach` uses `how`, `why`, and `unslop`. `technical-writing` uses `unslop`. Install these dependencies when selecting individual skills.

按需安装时，请同时安装相关依赖。完整插件已经包含全部依赖。

Some skills use subagents, MCP servers, or other host tools. The [host adaptation guide](./docs/harness/host-adaptation.md) explains how to use available tools without assuming a Cursor-specific environment. Missing tools can limit parallel investigation or external evidence collection.

部分技能使用子代理、MCP 或其他客户端工具。[客户端适配说明](./docs/harness/host-adaptation.md) 说明了对应关系。客户端缺少相关工具时，并行调查和外部资料收集会受到限制。

## Maintain this collection / 维护这个仓库

Add each new skill under `skills/<skill-name>/SKILL.md`. See [the contribution guide](./CONTRIBUTING.md) for naming, dependency, validation, and release steps.

在 `skills/<skill-name>/SKILL.md` 中添加新技能。命名、依赖、验证和发布步骤见[贡献指南](./CONTRIBUTING.md)。

## Source and license / 来源与许可

The selected skills come from [Cursor's pstack](https://github.com/cursor/plugins/tree/main/pstack). ADI selected and adapted them for this collection. See [upstream provenance](./upstream/SOURCE.md) for the source commit and local adaptations.

本集合选自 [Cursor pstack](https://github.com/cursor/plugins/tree/main/pstack)，由 ADI 筛选和适配。源提交及本地调整见[上游来源说明](./upstream/SOURCE.md)。

The upstream MIT license and copyright notice are preserved in [LICENSE](./LICENSE).

[LICENSE](./LICENSE) 保留了上游 MIT 许可证及版权声明。
