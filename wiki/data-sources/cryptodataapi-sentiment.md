---
title: "CryptoDataAPI — Sentiment & Macro"
type: source
created: 2026-07-13
updated: 2026-07-13
status: good
tags: [data-provider, crypto, api, sentiment, fear-greed, stablecoins, macro]
aliases: ["CDA Sentiment", "CryptoDataAPI Sentiment", "cryptodataapi fear greed", "cryptodataapi macro"]
source_type: data
source_url: "https://cryptodataapi.com/api/docs"
source_author: "CryptoDataAPI"
confidence: high
related: ["[[cryptodataapi]]", "[[cryptodataapi-market-health]]", "[[cryptodataapi-market-intelligence]]", "[[cryptodataapi-on-chain]]", "[[fear-and-greed-index]]", "[[alternative-me]]", "[[stablecoin-supply]]", "[[sentiment-analysis]]", "[[sentiment-trading]]"]
---

The Sentiment & Macro category of [[cryptodataapi]] bundles the crowd-psychology and macro backdrop reads: the Fear & Greed index, a macro snapshot (EUR/USD, gold, yields), and stablecoin market-cap levels with 14d/90d flows. Stablecoin supply doubles as a "dry powder" gauge — capital parked on-chain waiting to rotate into risk.

## Endpoints

| Method | Path | Returns | Key Params | Tier |
|--------|------|---------|------------|------|
| GET | /api/v1/sentiment/fear-greed | Fear & Greed index | markdown format option | — |
| GET | /api/v1/sentiment/macro | EUR/USD, gold, yields | — | — |
| GET | /api/v1/sentiment/stablecoins | Stablecoin mcap + 14d/90d flows | — | — |
| GET | /api/v1/sentiment/stablecoins/remote-history | Daily stablecoin history | days 1-365 | — |
| GET | /api/v1/sentiment/stablecoins/history | Raw mcap timeseries | — | — |

Tier "—" means the docs list no tier restriction for that endpoint.

## Live Data

`/sentiment/fear-greed` returns the current index reading (with a markdown format option for direct LLM/report consumption), `/sentiment/macro` the present EUR/USD, gold, and yield levels, and `/sentiment/stablecoins` today's stablecoin market cap with 14d and 90d flow deltas already computed.

## Historical Data

`/sentiment/stablecoins/remote-history` serves up to 365 days of daily stablecoin history, and `/sentiment/stablecoins/history` the raw market-cap timeseries. For a Fear & Greed timeseries, the API exposes `/api/v1/market-intelligence/fear-greed-history` in the [[cryptodataapi-market-intelligence]] category.

## Trading Applications

- **Contrarian timing** — extreme readings on the [[fear-and-greed-index]] (the same index popularised by [[alternative-me]]) are classic fade signals in [[sentiment-trading]] systems
- **Dry-powder tracking** — rising [[stablecoin-supply]] with positive 14d/90d flows signals sidelined capital that can fuel the next leg up; falling supply warns of liquidity leaving crypto
- **Macro regime overlay** — yields and gold from `/sentiment/macro` provide the risk-on/risk-off backdrop that conditions how crypto [[sentiment-analysis]] signals should be weighted
- **Feature engineering** — the 365-day stablecoin history is long enough to z-score flows and build supply-change features for regime models
- **Composite inputs** — sentiment readings feed the dual-score system in [[cryptodataapi-market-health]] and pair with on-chain dry-powder signals in [[cryptodataapi-on-chain]]

## Example

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/sentiment/stablecoins/remote-history?days=90"
```

## Related

- [[cryptodataapi]] — hub page with auth, tiers, and the full category map
- [[cryptodataapi-market-health]] — composite health scores built partly from sentiment inputs
- [[cryptodataapi-market-intelligence]] — Fear & Greed history and stablecoin mcap timeseries
- [[cryptodataapi-on-chain]] — CEX stablecoin reserves and the dry-powder z-score signal
- [[fear-and-greed-index]], [[alternative-me]], [[stablecoin-supply]], [[sentiment-analysis]], [[sentiment-trading]]

## Sources

- https://cryptodataapi.com/api/docs (fetched 2026-07-13)
