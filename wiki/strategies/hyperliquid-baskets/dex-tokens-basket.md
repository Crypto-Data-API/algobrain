---
title: "DEX Tokens Basket (Hyperliquid Basket)"
type: strategy
created: 2026-07-19
updated: 2026-07-19
status: good
tags: [crypto, perpetual-futures, hyperliquid, algorithmic, quantitative, momentum, defi, altcoins, market-regime]
aliases: ["Decentralised Exchange Basket", "DEX Protocol Basket", "AMM Token Basket"]
related: ["[[hyperliquid-baskets-overview]]", "[[momentum-rotation]]", "[[cross-sectional-relative-value]]", "[[defi-bluechip-basket]]", "[[narrative-position-vol-targeting]]", "[[alt-season-momentum-gate]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[funding-rate]]", "[[open-interest]]", "[[hyperliquid-liquidation-engine]]", "[[when-to-retire-a-strategy]]", "[[atr-position-sizing]]"]
strategy_type: quantitative
timeframe: swing
markets: [crypto]
complexity: intermediate
backtest_status: untested
edge_source: [behavioral, structural]
edge_mechanism: "DEX tokens are directly tied to trading volume and fee revenue, which creates a structural relationship between on-chain activity cycles and token prices; within-sector dispersion tracks volume-share shifts between DEX protocols (AMM innovations, liquidity-mining changes, new chain launches), enabling cross-sectional harvest as market-share battles play out."
data_required: [ohlcv-daily, ohlcv-1h, funding-rates, open-interest, bitcoin-dominance-data]
min_capital_usd: 10000
capacity_usd: 30000000
crowding_risk: medium
expected_sharpe: 0.7
expected_max_drawdown: 0.40
breakeven_cost_bps: 30
kill_criteria: |
  - basket drawdown > 40% from peak on a rolling 6-month basis
  - rolling 6-month Sharpe < 0 on minimum 10 completed trades
  - on-chain DEX total volume falls > 60% from 90-day average (DeFi activity collapse)
---

# DEX Tokens Basket (Hyperliquid Basket)

A sector basket of decentralised exchange protocol tokens with active Hyperliquid perpetuals. DEX tokens (governance tokens of AMMs, perp DEXs, and aggregators) are directly linked to on-chain trading volume — a structurally trackable metric — making this basket more fundamental than pure narrative plays.

> **Not investment advice.** All performance figures are illustrative estimates. *Part of the [[hyperliquid-baskets-overview|Hyperliquid basket library]].*

## Edge Source

**Behavioral + structural** (see [[edge-taxonomy]]). DEX tokens have structural support from fee revenue (fee-switch protocols accrue value to token holders) and volume-driven narratives. Cross-sectional dispersion tracks genuine protocol-market-share competition.

## Constituents

| Token | Ticker | Rationale |
|-------|--------|-----------|
| Uniswap | UNI | Largest AMM by volume; fee-switch narrative |
| Curve | CRV | Stablecoin AMM leader; gauge-wars ecosystem |
| dYdX | DYDX | Perp DEX; direct Hyperliquid peer narrative |
| GMX | GMX | Perp DEX with real-yield; Arbitrum-native |
| Jupiter | JUP | Solana DEX aggregator; Solana-DeFi flag-bearer |
| Velodrome | VELO | Optimism AMM; ve(3,3) model |
| Raydium | RAY | Solana AMM; Solana ecosystem anchor |
| Aerodrome | AERO | Base-chain AMM; Coinbase ecosystem narrative |

**Constituent count:** 8. Minimum $2M daily HL perp volume.

## Selection Rule

Constituents must: (1) be the governance or utility token of a decentralised exchange (AMM, perp DEX, or aggregator); (2) have verifiable on-chain volume metrics; (3) ≥ $2M daily HL perp volume.

## Weighting Scheme

**Equal-weight**. UNI and CRV are larger-cap; equal-weight provides meaningful exposure to Solana and Base DEX tokens where narrative moves are currently faster.

## Rebalance Cadence

Weekly. Out-of-cycle rebalance on major DEX protocol upgrades (Uniswap v5, Curve v2) or new chain launches capturing significant volume share.

## Regime Character

Correlated with on-chain DeFi activity. Performs when trading volumes rise (bull markets, high volatility, new DeFi narratives). Within-sector: Solana DEXs (JUP, RAY) outperform during Solana season; perp DEXs (DYDX, GMX) outperform when perpetual trading volume rises (including HL); AMMs (UNI, CRV) are most defensive.

## Strategies That Deploy This Basket

- [[momentum-rotation]] — long DEX tokens when sector ranks top momentum quintile
- [[cross-sectional-relative-value]] — long volume-gaining DEXs vs. short volume-losing DEXs within the sector
- [[defi-bluechip-basket]] — DEX tokens overlap; this basket is the pure-DEX cut
- [[narrative-position-vol-targeting]] — DEX trading volume narrative position

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/candles?coin=UNI&interval=1h&limit=168` — per constituent
- `GET /api/v1/derivatives/funding-rates?coin=UNI`
- `GET /api/v1/derivatives/open-interest?coin=GMX`

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/candles?coin=UNI&interval=1d&limit=90"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-hyperliquid]].

## Related

[[hyperliquid-baskets-overview]] · [[momentum-rotation]] · [[cross-sectional-relative-value]] · [[defi-bluechip-basket]] · [[narrative-position-vol-targeting]] · [[edge-taxonomy]] · [[failure-modes]] · [[atr-position-sizing]]
