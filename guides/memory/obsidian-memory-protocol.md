# Obsidian Memory Protocol

This protocol defines how AI agents must interact with the Obsidian memory vault to ensure persistence, accuracy, and context efficiency. All agents are required to follow these guidelines strictly.

## 1. Core Philosophy
The vault is not a folder of notes; it is a **Three-Layer Memory Architecture** designed to mirror human cognitive processes:
- **Working Memory** (`_agent/memory/working/`): Short-term, high-churn context for the current task.
- **Episodic Memory** (`_agent/memory/episodic/`): A chronological journal of experiences, decisions, and patterns.
- **Semantic Memory** (`_agent/memory/semantic/`): Distilled, a-temporal knowledge—the "truth" of the system.

## 2. Data Flow & The "Truth" Pipeline
Knowledge must flow through the following pipeline to prevent noise and ensure source attribution:
**Raw Sources** $\rightarrow$ **Semantic Synthesis** $\rightarrow$ **Deliverables**

1. **Ingestion**: Save all source material to `raw/[category]/` using the `raw-source` template. **Raw files are immutable.**
2. **Distillation**: During reflection cycles, synthesize information from `raw/` into `_agent/memory/semantic/`.
3. **Generation**: Create reports and briefs in `output/` based on the semantic layer.

## 3. The "Zoom-In" Retrieval Strategy
To prevent context bloat, agents MUST NOT read full directories or large files blindly. Follow these steps:

1. **Discover (Broad)**: Read the `_index.md` (Map of Content) of the target layer to find the relevant domain.
2. **Shortlist (Filtered)**: Use `obsidian-cli search-content "keyword"` to find candidate notes.
3. **Inspect (Precise)**: Use `obsidian-cli frontmatter <note>` to verify `type`, `confidence`, and `tags`.
4. **Execute (Deep)**: Use `obsidian-cli print <note>` or `read` only after verification.

## 4. Maintenance & Reflection Loop
The vault is a living system maintained via scheduled heartbeat cycles:
- **Session End**: Archive `working/` memory into `episodic/` records.
- **Daily Heartbeat**: Review recent `episodic/` logs $\rightarrow$ Update `semantic/` concepts $\rightarrow$ Prune outdated data.
- **Weekly Review**: Perform a deep audit of the `semantic/` layer to identify drift or contradictions.

## 5. Standards & Compliance
- **Schema**: Refer to `_agent/protocols/SCHEMA.md` for exact YAML frontmatter and naming conventions.
- **Linking**: Every semantic note must link to its original `raw/` source and at least one related semantic concept.
- **Metadata**: Never create a note without the required YAML frontmatter.

---
*Failure to follow this protocol leads to context fragmentation and memory drift. When in doubt, refer to the SCHEMA.md.*
