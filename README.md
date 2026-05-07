# Vault Storage

这个 Obsidian 仓库被组织成一个由 Codex 维护的 `LLM Wiki`，用于沉淀嵌入式工程知识。

## 目标

这个仓库主要用于长期积累以下知识：

- 手写驱动理解
- 配置文件理解
- 业务规则沉淀
- 代码注释生成支撑
- 代码生成支撑
- 设计文档与评审文档支撑

目标不是只在提问时临时检索原始资料，而是把资料持续编译成一个可维护的知识层。

## 总体工作模型

仓库按四个主要工作层组织：

1. `raw/`
   原始资料输入层，存放不可变原件和规范化文本。
2. `wiki/`
   持续维护的知识层，是长期工程理解的主承载区。
3. `references/`
   方法说明、外部模式、支撑性参考资料。
4. `templates/`
   各类知识页模板，避免每次从零设计页面结构。

如后续需要自动化，可在 `scripts/` 下增加辅助脚本。

## 推荐目录结构

```text
Vault_storage/
|- .obsidian/
|- AGENTS.md
|- index.md
|- log.md
|- README.md
|- raw/
|  |- assets/
|  |- originals/
|  |  |- code/
|  |  |- manuals/
|  |  |- meetings/
|  |  |- projects/
|  |  |- standards/
|  |  `- web-clips/
|  `- normalized/
|     |- manuals/
|     |- meetings/
|     |- projects/
|     |- standards/
|     `- web-clips/
|- wiki/
|  |- business/
|  |- concepts/
|  |- decisions/
|  |- entities/
|  |- inbox/
|  |- projects/
|  `- summaries/
|- references/
|  `- patterns/
|- templates/
`- scripts/
```

## 顶层目录说明

### `.obsidian/`

仅存放 Obsidian 本地配置，不属于知识内容本体。

### `AGENTS.md`

这是给 Codex 的“维护协议”或“知识库 schema”。  
它定义：

- 新资料如何 ingest
- 问题如何优先在 wiki 中查询
- 页面应如何拆分
- 结构如何长期维护

### `index.md`

内容导航入口。  
如果隔了一段时间没看这个知识库，建议先读它。

### `log.md`

时间线式更新记录。  
用于回答“最近往知识库里加了什么、改了什么、为什么改”。

### `raw/`

原始资料层。

- `raw/originals/`
  存放不可修改的原始输入，比如 PDF、源码快照、会议导出、截图、文档原件。
- `raw/normalized/`
  存放从原始资料转换出的 markdown 或 text，优先给人和 AI 阅读。
- `raw/assets/`
  存放附件图片、下载图片或被规范化文本引用的资源。

### `wiki/`

长期知识层。真正有持续价值的工程理解应沉淀在这里。

- `wiki/entities/`
  放“这是什么”的页面，比如芯片、工具、协议、模块、平台对象。
- `wiki/concepts/`
  放“它怎么工作”的页面，比如状态机、SPI 访问模型、寄存器分组、时序模型。
- `wiki/projects/`
  放“在当前代码库/项目里怎么实现”的页面，比如驱动结构、配置绑定、callout 关系、模块架构。
- `wiki/business/`
  放“为什么项目要这样用”的页面，比如唤醒策略、复位策略、看门狗策略、安全状态策略、故障处理策略、电源域使用策略。
- `wiki/summaries/`
  放摘要页和跨来源综合页。
- `wiki/decisions/`
  放设计决策、权衡和原因。
- `wiki/inbox/`
  放临时笔记或尚未整理完成的中间页。

### `references/`

存放方法论、模式说明、外部参考，不作为主知识层本体。

### `templates/`

存放可复用模板，用于创建新知识页。

### `scripts/`

预留给 `ingest / query / lint / search` 等后续自动化脚本。

## `wiki/` 各分层怎么用

### 什么时候放到 `entities/`

当页面主要回答这些问题时：

- 这是什么对象
- 它的职责是什么
- 有哪些相关页面应继续看

### 什么时候放到 `concepts/`

当页面主要回答这些问题时：

- 这个机制怎么工作
- 它的技术模型是什么
- 它会带来什么设计约束

### 什么时候放到 `projects/`

当页面主要回答这些问题时：

- 这部分在当前代码库里怎么实现
- 涉及哪些文件、配置、callout、运行流
- 当前模块结构是什么样

### 什么时候放到 `business/`

当页面主要回答这些问题时：

- 项目为什么这样使用这个模块
- 哪些是产品功能策略，而不是芯片原理
- 唤醒、复位、看门狗、安全状态、故障处理有哪些项目级规则
- 哪些行为是“当前项目政策”，而不是“硬件天然能力”

### 什么时候放到 `decisions/`

当页面主要回答这些问题时：

- 为什么最终选这个方案
- 替代方案是什么
- 哪些约束或假设决定了当前选择

### 什么时候放到 `summaries/`

当页面主要回答这些问题时：

- 这个来源整体说了什么
- 后续应该抽哪些知识、建哪些链接

## 原始资料处理规则

- 永远不要直接修改 `raw/originals/` 下的文件。
- 如果存在 `raw/normalized/` 版本，优先从规范化文本开始读。
- 对于同时存在 `chapters/` 和 `div/` 的规范化手册，默认优先读 `chapters/`。
- `div/` 更适合作为兼容层、追溯层或遗留拆分层，除非那里有尚未提升到其他层的细节。

## 推荐知识流转方式

1. 新资料先放入 `raw/originals/`
2. 如有必要，再生成 `raw/normalized/`
3. 从资料中提炼长期有效的知识，写入 `wiki/`
4. 更新 `index.md`
5. 在 `log.md` 记录一次有意义的变更

## 当前实际状态

目前这个知识库最成熟的内容是 `TLF35584` 相关知识。

- `raw/normalized/manuals/TLF35584/chapters/` 是当前最干净的手册事实源
- `wiki/concepts/` 和 `wiki/projects/` 已经沉淀了较多芯片和驱动理解
- `wiki/business/` 正在补齐项目语义和策略层页面

## 后续可选优化

这些不是现在必须做的，只是后续可以考虑：

- 如果 `wiki/projects/` 越来越混，可以再拆成 `wiki/modules/` 和真正的 `wiki/projects/`
- 如果 `raw/originals/projects/` 继续积累图片，建议改成具名子目录并补短 README
- 如果 `wiki/inbox/` 开始频繁使用，可以定义“暂存页如何提升为正式页”的轻量流程
- 如果业务策略页越来越多，可以再增加专门的策略模板，例如 `wake`、`reset`、`safe-state`、`power-domain`
未来新更多驱动时的参考架构
Vault_storage/
  ├── raw/
  │   ├── originals/manuals/
  │   │   ├── TLF35584/          ← 已有
  │   │   └── TJA1145/           ← 新增
  │   ├── originals/code/
  │   │   ├── Gp_TLF35584/       ← 已有
  │   │   └── Gp_TJA1145/        ← 新增
  │   └── normalized/manuals/
  │       ├── TLF35584/          ← 已有
  │       └── TJA1145/           ← 新增 (PDF → md)
  │
  ├── wiki/
  │   ├── entities/
  │   │   ├── TLF35584.md        ← 已有
  │   │   └── TJA1145.md         ← 新增
  │   ├── concepts/
  │   │   ├── TLF35584_spi_interface*.md      ← 已有
  │   │   ├── TLF35584_watchdogs*.md          ← 已有
  │   │   ├── TJA1145_spi_interface*.md       ← 新增
  │   │   ├── TJA1145_can_fd_configuration*.md ← 新增
  │   │   └── SPI_Protected_Register_Pattern*.md  ← 跨芯片共享概念
  │   ├── projects/
  │   │   ├── TLF35584_driver_code_architecture*.md
  │   │   └── TJA1145_driver_code_architecture*.md
  │   └── summaries/
  │       ├── TLF35584_manual_summary*.md
  │       └── TJA1145_manual_summary*.md
  │
  ├── index.md                   ← 追加 TJA1145 入口
  └── log.md

未来再新增不同层级的知识参考架构
Vault_storage/
  ├── raw/
  │   ├── originals/
  │   │   ├── manuals/TLF35584/, TJA1145/       ← 芯片手册
  │   │   ├── standards/                        ← 公司规范原文/PDF
  │   │   └── safety/                           ← ISO 26262 等原文
  │   └── normalized/                           ← (同上，全部 markdown 化)
  │
  ├── wiki/
  │   ├── drivers/                  ← 现有 TLF35584 内容迁入
  │   │   ├── concepts/
  │   │   ├── projects/
  │   │   ├── summaries/
  │   │   └── entities/
  │   │
  │   │
  │   ├── standards/                ← 公司规范
  │   │   ├── C_Code_Comment_Standard.md
  │   │   └── MISRA_Guidelines.md
  │   │
  │   ├── safety/                   ← 功能安全
  │   │   ├── ISO_26262_Part6.md
  │   │   └── ASIL_Decomposition.md
  │   │
  │   └── autosar/                  ← AUTOSAR
  │       ├── MCAL_Architecture.md
  │       └── EcuM_Overview.md
  │
  ├── index.md
  └── AGENTS.md                     ← 告诉 AI 按任务域选读对应子目录
## 命名建议

- 页面名尽量明确、稳定
- 少用 `notes`、`misc` 这类模糊命名
- 一页只承担一个主要职责
- 当页面开始同时混入原理、实现和业务策略时，应考虑拆页

## 建议入口

- [[index]]
- [[log]]
- [[AGENTS]]
- [[references/patterns/llm-wiki]]

