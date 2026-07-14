---
title: "Narrative Log"
type: index
created: 2026-05-08
updated: 2026-05-08
status: good
tags: [narratives, log, ledger]
aliases: ["narrative-log"]
---

# Narrative log

Append-only ledger of every narrative the bot has tracked. Newest first.
Updated by:

- `src/wiki/narrative_log.py::append_event` (called by `NarrativeReader.write`
  and the `/narrative` slash command);
- the bot's daily review pipeline (logs P&L attribution when a narrative
  closes out).

This page is the **historical record**: which narratives were called, on what
date, why, what trades they spawned, what played out, what didn't.

## Ledger

| Date | Slug | Status change | Side | Tickers | Signals | P&L | Notes |
|---|---|---|---|---|---|---|---|
| 2026-05-10 | mstr-bitcoin-treasury-premium-unwind-short | created (proposed) | pair | MSTR, IBIT | 0 | — | Successor leg to bitcoin-blowoff-long; short MSTR mNAV / long IBIT — captures premium decay, not BTC direction; GBTC playbook |
| 2026-05-09 | bitcoin-late-cycle-blowoff-crypto-equities-long | created (proposed) | long | MSTR, COIN | 0 | — | 13mo post-halving; Q3-Q4 2026 cycle blow-off window; QQQ put hedge |

## Conventions

- One row per status change, not per narrative. A narrative that goes
  proposed → active → played-out gets three rows.
- `Tickers` shows `tickers_primary` only (secondary/hedge omitted for brevity).
- `Signals` is a count at the time of the row. Final P&L lives only on
  played-out / invalidated rows.
- Stale narratives (>180 days `proposed` with no activation) are auto-marked
  `invalidated: stale` by the daily review.

## Pattern detection

The motivation for a single ledger page (rather than a row per narrative file)
is to make patterns greppable:

- "Every workforce-cut narrative I've called this year — how many played out?"
- "All narratives where the catalyst window expired without action — what was
  the common reason?"
- "Played-out narratives by sector — which sector themes have been most
  productive?"

Use `wiki_search` against this page for retrospective analysis.
