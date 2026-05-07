# LLM Wiki

A pattern for building personal or engineering knowledge bases using LLMs.

This file is intentionally abstract. It describes the pattern, not a single required implementation.

## The Core Idea

Many document workflows use retrieval at query time only:

- upload a set of files
- retrieve relevant chunks when a question is asked
- synthesize an answer

That works, but the knowledge is rediscovered again and again.

The `LLM Wiki` pattern is different. Instead of answering only from raw sources every time, the LLM incrementally builds and maintains a persistent markdown wiki between the user and the raw materials.

The wiki becomes a compounding artifact:

- entity pages are updated
- concept pages are refined
- summaries stay current
- contradictions are flagged
- links are maintained over time

## Why It Matters

The maintenance burden is what usually kills a knowledge base. Cross-links, summaries, synthesis, and consistency checks are all tedious for humans and cheap for an LLM.

The user focuses on:

- source curation
- asking the right questions
- validating important conclusions

The LLM focuses on:

- summarizing
- cross-linking
- updating pages
- keeping the structure coherent

## Typical Architecture

Three layers are usually enough:

1. `Raw sources`
   Immutable inputs such as PDFs, source snapshots, meeting notes, images, and exports.
2. `Wiki`
   Maintained markdown pages that capture durable knowledge.
3. `Schema`
   A control document such as `AGENTS.md` that tells the LLM how the wiki is organized and how to operate on it.

In this vault, those ideas map roughly to:

- `raw/`
- `wiki/`
- `AGENTS.md`

with `references/`, `templates/`, and `scripts/` added as support layers.

## Standard Operations

### Ingest

1. Read a new source from `raw/normalized/` when available.
2. Identify durable concepts, entities, project facts, business policy, and open questions.
3. Create or update pages in `wiki/`.
4. Update `index.md` for important pages.
5. Append a meaningful entry to `log.md`.

### Query

1. Read `index.md`.
2. Open the relevant wiki pages first.
3. Fall back to `raw/normalized/` or `raw/originals/` only when the wiki is incomplete.
4. If the answer has long-term value, file it back into the wiki.

### Lint

Periodically check for:

- orphan pages
- stale summaries
- duplicate pages
- contradictions
- missing cross-links
- pages that have grown too broad and should be split

## Index And Log

Two files are especially important:

- `index.md`
  Content-oriented navigation for both humans and LLMs.
- `log.md`
  Chronological record of meaningful changes.

Together they help the LLM know both:

- what exists
- what changed recently

## What Makes A Good LLM Wiki Page

A good page is:

- focused on one responsibility
- durable across sessions
- linked to nearby pages
- explicit about uncertainty
- not written like disposable chat output

## Engineering-Specific Adaptation

For engineering work, it is useful to separate:

- `entities/`
  What the thing is.
- `concepts/`
  How it works technically.
- `projects/`
  How it is implemented in the codebase or configuration.
- `business/`
  Why the project uses it this way and what policy must hold.
- `decisions/`
  Why one approach was chosen over alternatives.

This separation keeps raw chip behavior, code behavior, and project policy from being mixed together.

## Practical Note

This pattern is flexible. A vault can stay small and simple, or it can grow into a large maintained engineering wiki. The exact folder names, page types, and tooling can be adapted over time as the domain becomes clearer.

## Short Chinese Summary

`LLM Wiki` 的核心不是“临时检索”，而是“持续沉淀”。

- 原始资料放在 `raw/`
- 长期知识沉淀在 `wiki/`
- 维护规则写在 `AGENTS.md`

人负责：

- 提供资料
- 提问
- 判断关键结论

LLM 负责：

- 总结
- 建链接
- 更新知识页
- 维护结构一致性

对于工程知识库，最好把：

- 技术原理
- 代码实现
- 业务规则
- 设计决策

分层管理，而不是混在同一页里。

