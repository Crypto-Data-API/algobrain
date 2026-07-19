---
title: "L2 Rollups Basket (Hyperliquid Basket)"
type: strategy
created: 2026-07-19
updated: 2026-07-19
status: good
tags: [crypto, perpetual-futures, hyperliquid, algorithmic, momentum, quantitative, market-regime, altcoins]
aliases: ["L2 Basket", "Layer-2 Rollup Basket", "Rollup Sector Basket"]
related: ["[[hyperliquid-baskets-overview]]", "[[momentum-rotation]]", "[[cross-sectional-relative-value]]", "[[alt-season-momentum-gate]]", "[[crypto-beta-rotation]]", "[[narrative-position-vol-targeting]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[funding-rate]]", "[[open-interest]]", "[[perpetual-futures]]", "[[hyperliquid-liquidation-engine]]", "[[hyperliquid-funding-rate-microstructure]]", "[[when-to-retire-a-strategy]]", "[[atr-position-sizing]]"]
strategy_type: quantitative
timeframe: swing
markets: [crypto]
complexity: intermediate
backtest_status: untested
edge_source: [behavioral, structural]
edge_mechanism: "L2 rollup tokens co-move with Ethereum activity cycles and developer-adoption narratives; sector-relative momentum within L2s persists over 5–14 day windows as retail capital rotates between Optimistic and ZK-rollup narratives, creating harvestable dispersion for long-short or directional deployment against a confirmed alt-season gate."
data_required: [ohlcv-daily, ohlcv-1h, funding-rates, open-interest, bitcoin-dominance-data, altcoin-breadth]
min_capital_usd: 10000
capacity_usd: 30000000
crowding_risk: medium
expected_sharpe: 0.7
expected_max_drawdown: 0.40
breakeven_cost_bps: 30
kill_criteria: |
  - basket drawdown > 40% from peak on a rolling 6-month basis
  - rolling 6-month Sharpe < 0 on a minimum of 10 completed trades
  - Ethereum gas revenue collapses > 60% over 60 days (structural ETH headwind removes sector driver)
---

# L2 Rollups Basket (Hyperliquid Basket)

A sector basket of Layer-2 rollup perpetuals on [[hyperliquid|Hyperliquid]], providing concentrated exposure to the Ethereum scaling narrative. Can be deployed directionally (long the basket in confirmed alt-season / Ethereum bull regimes) or as the long-side of a sector-relative-value spread against a weak basket via [[cross-sectional-relative-value]].

> **Not investment advice.** All performance figures are illustrative estimates. *Part of the [[hyperliquid-baskets-overview|Hyperliquid basket library]].*

## Edge Source

**Behavioral + structural** (see [[edge-taxonomy]]). Retail capital rotates into L2 tokens as a high-beta Ethereum play during ETH outperformance periods; narrative rotation between Optimistic rollups and ZK rollups creates within-sector dispersion that cross-sectional strategies harvest.

## Constituents

| Token | Ticker | Rationale |
|-------|--------|-----------|
| Arbitrum | ARB | Largest optimistic rollup by TVL |
| Optimism | OP | Superchain leader; strong ecosystem narrative |
| Starknet | STRK | ZK-rollup leader; native account abstraction |
| Polygon | POL | Aggregated ZK network; strong institutional partnerships |
| zkSync | ZK | ZK-rollup; major airdrop and ecosystem recipient |
| Mantle | MNT | L2 with strong treasury; BitDAO lineage |
| Blast | BLAST | Yield-bearing L2; distinct yield narrative |

**Constituent count:** 7. Minimum 5 required; drop any constituent falling below $3M daily HL perp volume.

## Selection Rule

Constituents must: (1) have an active Hyperliquid perpetual with ≥ $3M daily volume; (2) be a production rollup or credible rollup with live mainnet; (3) be classified as an Ethereum Layer-2 scaling solution (not a standalone L1 or a sidechain without ZK/optimistic proof).

## Weighting Scheme

**Equal-weight** across active constituents. Rebalance trims and adds at each cadence to maintain equal notional.

## Rebalance Cadence

Weekly. Constituent eligibility reviewed monthly; replacements require ≥ 30 days of HL perp history before inclusion.

## Regime Character

Strongest in early-to-mid **Ethereum bull** and **confirmed alt-season** (BTC dominance falling, altcoin breadth rising). Weakest in BTC-dominance-rising regimes where capital concentrates in BTC and ETH underperforms majors. Gate with [[alt-season-momentum-gate]] before directional deployment.

## Strategies That Deploy This Basket

- [[momentum-rotation]] — long the basket when L2 sector ranks in the top momentum quintile
- [[alt-season-momentum-gate]] — ETH-alt season gating applies directly; L2s are the first-tier rotation target
- [[cross-sectional-relative-value]] — long L2s vs. short weak sector basket
- [[narrative-position-vol-targeting]] — L2 narrative position with vol-scaled sizing
- [[crypto-beta-rotation]] — L2s as high-beta ETH proxy; reduce in macro risk-off

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/candles?coin=ARB&interval=1h&limit=168` — 7d 1h klines per constituent
- `GET /api/v1/derivatives/funding-rates?coin=ARB` — funding for each leg
- `GET /api/v1/derivatives/open-interest?coin=ARB` — OI for each leg

**Historical:**
- `GET /api/v1/backtesting/klines` — full OHLCV archive for basket backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/candles?coin=ARB&interval=1d&limit=90"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-hyperliquid]].

## Related

[[hyperliquid-baskets-overview]] · [[momentum-rotation]] · [[cross-sectional-relative-value]] · [[alt-season-momentum-gate]] · [[crypto-beta-rotation]] · [[narrative-position-vol-targeting]] · [[edge-taxonomy]] · [[failure-modes]] · [[atr-position-sizing]] · [[hyperliquid-funding-rate-microstructure]]
