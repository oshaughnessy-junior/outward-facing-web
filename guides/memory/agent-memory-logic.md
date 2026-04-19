---
layout: page
title: Agent Memory Logic
---

# Agent Memory Logic

This file documents the operational logic for our assistant's memory system, as defined in our workspace.

## Memory Continuity

- **Daily notes:** `memory/YYYY-MM-DD.md` — raw logs of daily activities.
- **Long-term:** `MEMORY.md` — the curated essence of our history.

## Curation Protocol

- Review daily files periodically to distill lessons into `MEMORY.md`.
- Remove outdated information that no longer guides current actions.
- **Text > Brain**: Never rely on "mental notes." If it matters, write it down immediately.

## Session Startup Logic

1. Read `SOUL.md` (Persona).
2. Read `USER.md` (Human Context).
3. Read `memory/YYYY-MM-DD.md` (Recent Context).
4. Read `MEMORY.md` (Long-term Wisdom).
