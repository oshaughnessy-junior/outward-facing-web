# Obsidian Memory SCHEMA

This document defines the structural and metadata standards for the AI Agent's Obsidian vault. Strict adherence is required to maintain retrieval efficiency and prevent context bloat.

## 1. Filesystem Hierarchy

### A. Agent Internals (`_agent/`)

Contains the internal operational state of the agent.

- `_agent/protocols/`: System instructions, schemas, and retrieval guidelines.
- `_agent/memory/working/`: Short-term, session-scoped context. High churn.
- `_agent/memory/episodic/`: Timestamped records of experiences, decisions, and observations.
- `_agent/memory/semantic/`: Distilled, a-temporal knowledge (The Wiki).
- `_agent/templates/`: Standardized markdown templates for note creation.

### B. Immutable Sources (`raw/`)

Append-only storage for source material. Never edit these files.

- `raw/articles/`: Web content, blogs, news.
- `raw/papers/`: Academic papers, technical specifications.
- `raw/logs/`: Raw session logs or system output.
- `raw/[category]/`: Additional categories as needed.

### C. Generated Deliverables (`output/`)

The "Export" layer. Content derived from raw and semantic memory.

- `output/reports/`: Formal synthesized reports.
- `output/briefs/`: Daily or project-specific briefs.
- `output/artifacts/`: Code snippets, diagrams, or data tables.

---

## 2. Metadata Schema (YAML Frontmatter)

All notes MUST include a YAML frontmatter block at the top of the file.

### Required Fields

- `type`: (concept | episode | source | output)
- `created`: YYYY-MM-DD
- `updated`: YYYY-MM-DD
- `tags`: [list of kebab-case tags]

### Contextual Fields (Optional but Recommended)

- `confidence`: (high | medium | low) - Used for semantic memory.
- `sources`: [list of paths to `raw/` files] - Used for attribution.
- `importance`: (critical | high | medium | low)
- `status`: (draft | reviewed | archived)

**Example Frontmatter:**

```yaml
---
type: concept
created: 2026-04-17
updated: 2026-04-17
tags: [gravitational-waves, ligo-detector]
confidence: high
sources: [raw/papers/gw150914.md]
---
```

---

## 3. Naming Conventions

### A. Semantic Memory (`_agent/memory/semantic/`)

- Use kebab-case: `gravitational-wave-detection.md`
- Avoid generic names like `notes.md`.

### B. Episodic Memory (`_agent/memory/episodic/`)

- Format: `YYYY-MM-DD-HHMM-description.md`
- Example: `2026-04-17-1230-obsidian-schema-setup.md`

### C. Raw Sources (`raw/`)

- Format: `YYYY-MM-DD-source-slug.md`
- Example: `2026-04-17-towards-ai-memory-layers.md`

---

## 4. Retrieval & Indexing Rules

- **MOCs (Maps of Content)**: Any directory with >10 files should have an `_index.md` file listing key topics and links.
- **Cross-Linking**: Semantic notes must link to at least one other semantic note and their original `raw/` source.
- **Search Priority**:
  1. `_agent/memory/semantic/` (Highest truth)
  2. `_agent/memory/episodic/` (Contextual truth)
  3. `raw/` (Source truth)
