---
title: "Narratives Index"
type: index
created: 2026-05-08
updated: 2026-05-08
status: good
tags: [narratives, theses, itpm]
---

# Narratives

A **narrative** is a thematic position — a story-level thesis that parents one
or more individual trades. The convention follows
[[itpm-framework]] Stage 2 (*"These themes are the parents of all individual
stock positions"*).

This is the canon of every narrative the bot has acted on, with provenance,
status, and downstream signals.

## Active narratives

See `_log.md` for the chronological ledger.

Each narrative file lives at `wiki/narratives/<slug>.md` and follows the schema
in `_schema.md`. A narrative can be created:

- by hand in the wiki (preferred for high-conviction theses);
- by the `/narrative` Claude Code slash command (assists drafting);
- by the bot's daily macro pipeline (auto-generated `macro-tilt-YYYY-MM-DD`
  narratives from Stage 1-3 output).

## Lifecycle

```
proposed → active → played-out
                  ↘ invalidated
```

- **proposed** — drafted, not yet acted on.
- **active** — at least one signal has been generated under this narrative.
- **played-out** — thesis materialised; positions closed. Logged in `_log.md`
  with realised P&L attribution.
- **invalidated** — thesis disproved or catalyst missed. Logged with reason.

## See also

- [[narratives-schema|Narrative frontmatter schema]]
- [[narrative-log|Narrative chronological log]]
- [[itpm-framework]] §"Worked Example" — thematic positions
- [[itpm-trade-construction-playbook]] §"Stage 2: Geographic and Asset Class"
