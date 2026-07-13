---
title: "News & Events"
type: index
created: 2026-04-06
updated: 2026-06-12
status: good
tags: [news, index]
---

# News & Events

Verified, market-moving news stories and events with documented impact.

This section documents specific news events that moved markets, with verified facts, price impact data, and analysis of why the event mattered. Unlike ephemeral news feeds, these pages are designed to be lasting references -- explaining the context, the market reaction, and the lessons for traders.

Events are tagged by impact level (high, medium, low) and the markets affected. The most consequential recent events include the [[2024-01-10-bitcoin-spot-etf-approval|Bitcoin spot ETF approval]], the [[2025-04-02-liberation-day-tariffs|Liberation Day tariff shock]], and the [[2026-market-regime-overview|2026 market regime overview]] that contextualizes current conditions.

For DeFi security incidents specifically, see [[defi-hacks-and-exploits]] — the master timeline covering $8B+ in exploits from 2016 to present.

## Start Here

- [[2024-01-10-bitcoin-spot-etf-approval]] -- The SEC finally approves spot Bitcoin ETFs
- [[2025-04-02-liberation-day-tariffs]] -- Sweeping tariff announcement shocks global markets
- [[2026-market-regime-overview]] -- Current market regime context and key themes

## Forward-Looking Watchlists

These pages are *living watchlists* rather than event records — intentionally speculative, updated quarterly, and explicitly not predictions. Verify current state before trading.

- [[2026-exploit-target-watchlist]] -- crypto protocols ranked by AI-era exploit risk (TVL × code novelty × audit gap); now tracks AI-discovered cryptographic bugs after the [[2026-06-05-zcash-orchard-counterfeiting-bug|ZEC Orchard disclosure]]
- [[2026-fork-watchlist]] -- scheduled, debated, and rumored chain-split / contentious-fork events for 2026

## AI-in-Finance Events (2026)

- [[2026-claude-opus-4-7-finance-benchmark]] -- the milestone where a frontier LLM first led finance-specific benchmarks (since superseded by Opus 4.8 / [[claude|Fable 5]])
- [[2026-chatgpt-mainstream-adoption]] -- ChatGPT crosses from early-adopter to mainstream (over-35 cohort, gender balance), reshaping retail information flows
- [[2026-uniswap-v4-launch]] -- hooks system + lowest-cost AMM, with implications for on-chain arbitrage economics

## All News Events

```dataview
TABLE event_date, impact, markets_affected, verified
FROM "wiki/news"
WHERE type = "news"
SORT event_date DESC
```

## By Impact Level

### High Impact
```dataview
LIST
FROM "wiki/news"
WHERE impact = "high"
SORT event_date DESC
```
