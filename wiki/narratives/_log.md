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
| 2026-05-10 | ai-search-disruption-googl-short | created (proposed) | short | GOOGL | 0 | — | AI Overviews ad-inventory compression + Apple Safari search risk + DOJ remedy phase; long MSFT/QQQ as paired hedge |
| 2026-05-10 | glp1-megatrend-pharma-long-staples-short | created (proposed) | long | LLY, NVO | 0 | — | Healthcare basket gap-fill; long LLY/NVO + paired short KO/MDLZ/DVA on demand-destruction read-across |
| 2026-05-10 | fiscal-dominance-long-bond-supply-short | created (proposed) | short | TLT | 0 | — | Counter-leg to bls-stealth-recession (long TLT); $2T deficits + term-premium normalization + IEF long as steepener |
| 2026-05-10 | boj-normalization-yen-banks-long | created (proposed) | long | FXY, MUFG, SMFG | 0 | — | Missing global macro hedge — long yen + JP megabank NIM expansion + QQQ put kicker on carry-unwind tail |
| 2026-05-09 | office-reit-distress-cre-refi-wall-short | created (proposed) | short | SLG, BXP, VNO | 0 | — | $1.5T CRE refi wall + AI-displaced seat demand; XLRE long hedge |
| 2026-05-09 | volatility-dispersion-single-vs-index-long | created (proposed) | long | NVDA, MSFT, META | 0 | — | Long single-name vol vs short index vol; pure ITPM dispersion play; 90d earnings cycle |
| 2026-05-09 | nuclear-renaissance-small-cap-long | created (proposed) | long | OKLO, SMR, BWXT | 0 | — | Hyperscaler nuclear PPAs + NRC milestones; pure-play small-cap; URA/CCJ secondary |
| 2026-05-09 | skilled-trades-wage-boom-services-long | created (proposed) | long | PWR, MTZ, FIX | 0 | — | Inverse of [[ai-layoff-trap]]; labor-services layer of AI-capex buildout |
| 2026-05-09 | gold-safe-haven-real-rates-rollover-long | created (proposed) | long | GLD | 0 | — | Real rates rollover + central-bank de-dollarization; UUP small hedge; GDX/NEM secondary |
| 2026-05-09 | european-banks-ecb-behind-curve-short | created (proposed) | short | EUFN | 0 | — | Kreil's worked example from [[itpm-framework]]; ECB hiking into a slowdown; XLF/UUP hedge |
| 2026-05-09 | bitcoin-late-cycle-blowoff-crypto-equities-long | created (proposed) | long | MSTR, COIN | 0 | — | 13mo post-halving; Q3-Q4 2026 cycle blow-off window; QQQ put hedge |
| 2026-05-09 | bls-stealth-recession-long-bonds-short-cyclicals | created (proposed) | long | TLT | 0 | — | 900K BLS revision is informational edge; long duration / short cyclicals (KRE/XLF/XLY) |
| 2026-05-09 | tariff-persistence-domestic-manufacturers-long | created (proposed) | long | NUE, MLM, VMC | 0 | — | Post-Liberation-Day reimposition; long US-domestic, short global supply chain (NKE/F/FXI) |
| 2026-05-09 | stagflation-tail-hedge-long-vol-overlay | created (proposed) | long | SPY, VIX | 0 | — | Canonical [[itpm-framework]] long-vol overlay; ~1.5% NAV/yr; defensive sleeve underneath all other narratives |
| 2026-05-09 | iran-war-persistence-energy-defense-long | created (proposed) | long | XLE, ITA | 0 | — | Two months post [[2026-03-iran-conflict-oil-spike]]; bet on persistence over fade; XLY/SPY hedged |
| 2026-05-09 | show-me-regime-ai-saas-short | created (proposed) | short | WCLD | 0 | — | Basket-level expression of integrated thesis chain (Klarna → SaaSpocalypse → Cloudflare → COGS creep); QQQ hedged |
| 2026-05-09 | ai-layoff-trap-capex-beneficiaries | created (proposed) | long | VRT, CEG, ETN, NRG | 0 | — | Inverse leg of [[ai-layoff-trap]] — long picks-and-shovels capex beneficiaries |
| 2026-05-08 | cloudflare-ai-mix-shift-trap | created (proposed) | short | FSLY, AKAM | 0 | — | NET -24% selloff read-through; AI-infra mix-shift short basket |
| 2026-05-08 | crm-workforce-cut-ai-margin | created (proposed) | long | CRM, NOW, WDAY | 0 | — | Worked example narrative |

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
