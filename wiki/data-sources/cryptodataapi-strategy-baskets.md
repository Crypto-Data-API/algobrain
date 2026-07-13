---
title: "CryptoDataAPI — Trading Strategy Baskets"
type: source
created: 2026-07-13
updated: 2026-07-13
status: good
tags: [data-provider, crypto, api, strategy-baskets, portfolio, thematic, regime]
aliases: ["CryptoDataAPI Strategy Baskets", "CDA Strategy Baskets", "CryptoDataAPI Meta-Baskets", "Trading Strategy Baskets API"]
source_type: data
source_url: "https://cryptodataapi.com/api/docs"
confidence: high
related: ["[[cryptodataapi]]", "[[cryptodataapi-regimes]]", "[[cryptodataapi-coins]]", "[[cryptodataapi-hyperliquid]]", "[[trading-strategy-baskets]]", "[[hyperliquid-baskets-overview]]", "[[regime-strategy-playbook]]"]
---

CryptoDataAPI's Trading Strategy Baskets section is a single Pro+ endpoint that serves 50 pre-built meta-baskets organised into 6 thematic groups — curated asset groupings designed to be traded as units rather than assembled coin by coin. It is the API counterpart to this wiki's [[trading-strategy-baskets]] concept and the natural universe source for [[hyperliquid-baskets-overview]] implementations.

## Endpoints

| Method | Path | Returns | Key Params | Tier |
|--------|------|---------|------------|------|
| GET | /api/v1/trading-strategy-baskets | 50 meta-baskets across 6 thematic groups | — | Pro+ |

## Live Data

The single GET returns the current basket definitions: all 50 meta-baskets with their 6 thematic groupings, in one call. Because basket composition is curated server-side, re-fetching keeps your trading universe aligned with the provider's latest groupings without maintaining your own membership lists.

## Historical Data

There is no history endpoint for baskets — the endpoint always reflects the current definitions. To backtest basket strategies point-in-time, snapshot the response on your own schedule (or rely on the dated daily snapshots in [[cryptodataapi-backtesting]]) so that historical tests use the memberships that existed at the time, not today's.

## Trading Applications

- **Regime-to-basket routing** — pair basket definitions with the labels from [[cryptodataapi-regimes]] to implement the [[regime-strategy-playbook]]: rotate into the thematic groups that historically outperform in the current regime
- **Ready-made universes** — [[trading-strategy-baskets]] strategies get 50 curated universes without hand-maintaining sector lists as narratives shift
- **Hyperliquid basket trading** — intersect basket members with tradeable perps from [[cryptodataapi-hyperliquid]] to run [[hyperliquid-baskets-overview]] long/short structures
- **Relative-strength rotation** — rank the 6 thematic groups by aggregate momentum and rotate exposure toward the leaders
- **Pair and spread construction** — long the strongest basket against a short in the weakest within the same thematic group for market-neutral exposure

## Example

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/trading-strategy-baskets"
```

## Related

- [[cryptodataapi]] — provider hub (auth, tiers, category map)
- [[cryptodataapi-regimes]] — regime labels that decide which baskets to deploy
- [[cryptodataapi-coins]] — per-asset profiles and category groups behind basket members
- [[cryptodataapi-hyperliquid]] — perp market data for executing basket trades
- [[cryptodataapi-backtesting]] — point-in-time snapshots for basket backtests
- [[trading-strategy-baskets]], [[hyperliquid-baskets-overview]], [[regime-strategy-playbook]]

## Sources

- https://cryptodataapi.com/api/docs (fetched 2026-07-13)
