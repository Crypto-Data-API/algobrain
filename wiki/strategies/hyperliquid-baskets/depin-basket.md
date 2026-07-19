---
title: "DePIN Basket (Hyperliquid Basket)"
type: strategy
created: 2026-07-19
updated: 2026-07-19
status: good
tags: [crypto, perpetual-futures, hyperliquid, algorithmic, quantitative, momentum, altcoins, market-regime]
aliases: ["DePIN Sector Basket", "Decentralised Physical Infrastructure Basket", "Physical Infrastructure Crypto Basket"]
related: ["[[hyperliquid-baskets-overview]]", "[[momentum-rotation]]", "[[cross-sectional-relative-value]]", "[[narrative-position-vol-targeting]]", "[[alt-season-momentum-gate]]", "[[crypto-beta-rotation]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[funding-rate]]", "[[open-interest]]", "[[hyperliquid-liquidation-engine]]", "[[when-to-retire-a-strategy]]", "[[atr-position-sizing]]"]
strategy_type: quantitative
timeframe: swing
markets: [crypto]
complexity: intermediate
backtest_status: untested
edge_source: [behavioral, informational]
edge_mechanism: "DePIN tokens share a real-world adoption narrative (decentralised networks replacing traditional infrastructure) that creates correlated narrative cycles; within-sector dispersion tracks actual network metrics (active nodes, data transferred, compute hours sold), creating cross-sectional edges between adoption-leaders and laggards."
data_required: [ohlcv-daily, ohlcv-1h, funding-rates, open-interest, bitcoin-dominance-data]
min_capital_usd: 10000
capacity_usd: 20000000
crowding_risk: medium
expected_sharpe: 0.7
expected_max_drawdown: 0.42
breakeven_cost_bps: 35
kill_criteria: |
  - basket drawdown > 42% from peak on a rolling 6-month basis
  - rolling 6-month Sharpe < 0 on minimum 10 completed trades
  - DePIN sector narrative absent from top-10 crypto narratives for > 60 days
---

# DePIN Basket (Hyperliquid Basket)

A sector basket of Decentralised Physical Infrastructure Network tokens with active Hyperliquid perpetuals. DePIN covers wireless, compute, storage, energy, and mobility networks built on blockchain token incentives. The basket provides exposure to the "real-world adoption" crypto narrative — distinct from pure DeFi or pure AI plays.

> **Not investment advice.** All performance figures are illustrative estimates. *Part of the [[hyperliquid-baskets-overview|Hyperliquid basket library]].*

## Edge Source

**Behavioral + informational** (see [[edge-taxonomy]]). DePIN tokens react to real-world adoption milestones (node count milestones, enterprise partnerships, data throughput records) that are observable before fully priced, and co-move on shared "decentralised infrastructure" narrative cycles.

## Constituents

| Token | Ticker | Rationale |
|-------|--------|-----------|
| Helium | HNT | Decentralised wireless network; established DePIN anchor |
| Render | RNDR | Decentralised GPU rendering; largest DePIN by market cap |
| Akash Network | AKT | Decentralised cloud compute marketplace |
| io.net | IO | GPU compute for AI inference; fastest-growing DePIN |
| Hivemapper | HONEY | Decentralised mapping network |
| GEODNET | GEOD | Decentralised GPS correction network |
| Filecoin | FIL | Decentralised storage; established DePIN infrastructure |

**Constituent count:** 7. Minimum $2M daily HL perp volume (DePIN tokens can be thinner than DeFi majors).

## Selection Rule

Constituents must: (1) operate a real physical-world infrastructure network (wireless, compute, storage, energy, mobility, sensing) with verifiable nodes; (2) have a token that provides genuine network utility (not just governance); (3) have ≥ $2M daily HL perp volume.

## Weighting Scheme

**Equal-weight**. RNDR and FIL are significantly larger than other constituents — consider vol-weighting to reduce their dominance and increase exposure to smaller-cap DePIN narratives.

## Rebalance Cadence

Weekly. DePIN is a fast-evolving sector; monthly eligibility reviews may add newly listed HL DePIN perps.

## Regime Character

Performs in narrative-driven "real-world adoption" cycles and alt-seasons. Less sensitive to pure DeFi or BTC macro than other baskets. Often outperforms during AI hype cycles (compute DePIN) and connectivity infrastructure news. Weakest in pure bear markets with no risk appetite for speculative infrastructure tokens.

## Strategies That Deploy This Basket

- [[momentum-rotation]] — long DePIN when the sector ranks top momentum quintile
- [[cross-sectional-relative-value]] — long DePIN leaders vs. short DePIN laggards
- [[narrative-position-vol-targeting]] — DePIN as a distinct narrative position
- [[alt-season-momentum-gate]] — DePIN included in alt-season rotation universe

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/candles?coin=RNDR&interval=1h&limit=168` — per constituent
- `GET /api/v1/derivatives/funding-rates?coin=RNDR`
- `GET /api/v1/derivatives/open-interest?coin=RNDR`

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/candles?coin=FIL&interval=1d&limit=90"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-hyperliquid]].

## Related

[[hyperliquid-baskets-overview]] · [[momentum-rotation]] · [[cross-sectional-relative-value]] · [[narrative-position-vol-targeting]] · [[alt-season-momentum-gate]] · [[ai-tokens-basket]] · [[edge-taxonomy]] · [[failure-modes]] · [[atr-position-sizing]]
