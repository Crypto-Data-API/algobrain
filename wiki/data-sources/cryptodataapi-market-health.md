---
title: "CryptoDataAPI — Market Health"
type: source
created: 2026-07-13
updated: 2026-07-13
status: good
tags: [data-provider, crypto, api, market-health, market-breadth, composite-score]
aliases: ["CDA Market Health", "CryptoDataAPI Market Health", "cryptodataapi altcoin breadth", "cryptodataapi dual score"]
source_type: data
source_url: "https://cryptodataapi.com/api/docs"
source_author: "CryptoDataAPI"
confidence: high
related: ["[[cryptodataapi]]", "[[cryptodataapi-regimes]]", "[[cryptodataapi-sentiment]]", "[[cryptodataapi-on-chain]]", "[[cryptodataapi-indicators]]", "[[market-breadth]]", "[[market-regime]]", "[[btc-dominance]]", "[[bitcoin-dominance-rotation]]"]
---

The Market Health category of [[cryptodataapi]] serves a dual-score system (0-100) built from 11 components, condensing the whole market's condition into two headline numbers plus a sentiment label. It also includes an altcoin-breadth endpoint — the percentage of coins above a configurable moving average — making it the wiki's primary API source for [[market-breadth]] readings.

## Endpoints

| Method | Path | Returns | Key Params | Tier |
|--------|------|---------|------------|------|
| GET | /api/v1/market-health | Full dual-score + 11 components | — | — |
| GET | /api/v1/market-health/summary | Scores + sentiment only | markdown format available | — |
| GET | /api/v1/market-health/components | All 11 component details | — | — |
| GET | /api/v1/market-health/component/{name} | Single component (historical composition available) | name | — |
| GET | /api/v1/market-health/history | Historical scores | days 1-730 | — |
| GET | /api/v1/market-health/altcoin-breadth | % coins above MA + detail | MA period 5-365d (default 200) | — |
| POST | /api/v1/market-health/refresh | Force recalculation | — | Pro+ |

Tier "—" means the docs list no tier restriction for that endpoint.

## Live Data

`/market-health`, `/market-health/summary`, `/market-health/components`, and `/market-health/component/{name}` all return the **current** dual-score state — the full breakdown, a trimmed scores-plus-sentiment view (with a markdown format for reports), or individual components. `/market-health/altcoin-breadth` reads current breadth against a chosen MA period (5-365 days, default 200). Pro+ keys can `POST /market-health/refresh` to force a recalculation.

## Historical Data

`/market-health/history` returns up to 730 days of historical scores — enough for two years of regime backtesting. `/market-health/component/{name}` also exposes historical composition for a single component, letting you decompose past score moves.

## Trading Applications

- **Breadth-based regime detection** — altcoin breadth above/below key thresholds is a direct [[market-breadth]] input for classifying the current [[market-regime]]
- **Alt-season confirmation** — broadening participation (rising % of coins above the 200D MA) alongside falling [[btc-dominance]] is the classic [[bitcoin-dominance-rotation]] setup for rotating from BTC into alts
- **Risk throttle** — headline health scores act as a portfolio-level exposure dial: scale gross exposure up in healthy regimes, cut it as scores deteriorate
- **Divergence warnings** — price making highs while health components roll over flags narrow, fragile rallies before they break
- **Backtestable regime filter** — 730 days of score history allows testing "only trade longs when health > X" style gates alongside [[cryptodataapi-regimes]] labels

## Example

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-health/altcoin-breadth?period=200"
```

## Related

- [[cryptodataapi]] — hub page with auth, tiers, and the full category map
- [[cryptodataapi-regimes]] — discrete regime labels that complement the continuous health scores
- [[cryptodataapi-sentiment]] — Fear & Greed and stablecoin flows feeding the sentiment picture
- [[cryptodataapi-on-chain]] — On-Chain Health composite as an independent 0-100 score
- [[cryptodataapi-indicators]] — per-asset technical state to pair with market-wide health
- [[market-breadth]], [[market-regime]], [[btc-dominance]], [[bitcoin-dominance-rotation]]

## Sources

- https://cryptodataapi.com/api/docs (fetched 2026-07-13)
