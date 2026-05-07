# AGENTS

This vault follows an `LLM Wiki` pattern for Codex-assisted knowledge management.

## Mission

Maintain a persistent, compounding markdown wiki instead of answering only from raw source retrieval.

## Layers

- `raw/originals/`: immutable originals such as PDF, DOCX, PPTX, exports
- `raw/normalized/`: markdown or text converted from originals for easier ingest
- `wiki/`: Codex-maintained knowledge pages
- `references/`: methodology and reference notes
- `templates/`: seed templates for new pages

## Rules

1. Never edit files in `raw/originals/`.
2. Prefer reading `raw/normalized/` before parsing binaries.
3. Write durable knowledge into `wiki/`, not only into chat replies.
4. Update `index.md` when adding important pages.
5. Append to `log.md` when ingesting sources or making substantial wiki updates.
6. Prefer small, focused pages over large catch-all pages.
7. Link related pages with wiki links whenever the relationship is meaningful.
8. Flag contradictions instead of silently overwriting older claims.
9. Keep `concepts`, `projects`, `business`, and `decisions` separated by responsibility.
10. Prefer `raw/normalized/.../chapters/` over legacy split structures when both exist.

## Standard Workflows

### Ingest

1. Read the new source from `raw/normalized/` when available.
2. Identify the main concepts, entities, and project relevance.
3. Create or update one or more pages in `wiki/`.
4. Update `index.md` with new important pages.
5. Add an entry to `log.md`.

### Query

1. Read `index.md` first.
2. Open only the wiki pages relevant to the question.
3. Fall back to `raw/normalized/` or `raw/originals/` only when the wiki is incomplete.
4. If the answer has long-term value, file it back into `wiki/`.

### Lint

Check for:

- orphan pages
- stale summaries
- duplicate concepts
- missing cross-links
- oversized pages that should be split

## Current Scope

This vault is being initialized for structured knowledge work in Obsidian. The next planned ingest is the `TLF35584` manual markdown.

## Current Structure Notes

- `wiki/business/` is reserved for project-level functional policy and usage semantics.
- `wiki/projects/` should focus on implementation shape, code architecture, and configuration binding.
- `wiki/concepts/` should focus on reusable technical understanding rather than project policy.
