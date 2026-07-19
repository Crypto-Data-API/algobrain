---
title: "Solana Ecosystem Basket (Hyperliquid Basket)"
type: strategy
created: 2026-07-19
updated: 2026-07-19
status: good
tags: [crypto, perpetual-futures, hyperliquid, algorithmic, quantitative, momentum, altcoins, market-regime, solana]
aliases: ["Solana Season Basket", "SOL Ecosystem Basket", "Solana Alt Basket", "SOL-Native Basket"]
related: ["[[hyperliquid-baskets-overview]]", "[[momentum-rotation]]", "[[cross-sectional-relative-value]]", "[[alt-season-momentum-gate]]", "[[narrative-position-vol-targeting]]", "[[l1-blockchains-basket]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[funding-rate]]", "[[open-interest]]", "[[hyperliquid-liquidation-engine]]", "[[when-to-retire-a-strategy]]", "[[atr-position-sizing]]"]
strategy_type: quantitative
timeframe: swing
markets: [crypto]
complexity: intermediate
backtest_status: untested
edge_source: [behavioral, structural]
edge_mechanism: "Solana ecosystem tokens share the SOL price trend as their strongest common factor; during Solana-specific narrative cycles (DEX volume records, meme coin launches, mobile wallet adoption milestones), Solana-native DeFi and infrastructure tokens outperform the broad crypto market by 2–5× — creating concentrated sector momentum that the basket captures directionally while providing within-sector cross-sectional dispersion."
data_required: [ohlcv-daily, ohlcv-1h, funding-rates, open-interest, bitcoin-dominance-data]
min_capital_usd: 8000
capacity_usd: 20000000
crowding_risk: high
expected_sharpe: 0.7
expected_max_drawdown: 0.50
breakeven_cost_bps: 35
kill_criteria: |
  - basket drawdown > 50% from peak on a rolling 6-month basis
  - SOL falls below its 90-day MA for > 20 consecutive days (Solana season is over)
  - rolling 6-month Sharpe < -0.2 on minimum 10 completed trades
---

# Solana Ecosystem Basket (Hyperliquid Basket)

A sector basket of Solana-native protocol tokens with active Hyperliquid perpetuals. Deployed specifically during "Solana seasons" — periods when SOL outperforms ETH and the Solana DeFi ecosystem attracts narrative and capital rotation. The basket is more concentrated and more volatile than the broad [[l1-blockchains-basket]].

> **Not investment advice.** All performance figures are illustrative estimates. *Part of the [[hyperliquid-baskets-overview|Hyperliquid basket library]].*

## Edge Source

**Behavioral + structural** (see [[edge-taxonomy]]). Solana ecosystem tokens share SOL's price beta with an amplification factor (DeFi tokens on a network tend to outperform the L1 token itself during the network's bull phase). The structural driver is that Solana's throughput advantages attract specific application categories (DEX, meme coins, mobile) with concentrated capital rotation.

## Constituents

| Token | Ticker | Rationale |
|-------|--------|-----------|
| Raydium | RAY | Solana's primary AMM; volume-correlated revenue |
| Jupiter | JUP | Solana DEX aggregator; largest Solana DeFi protocol |
| Pyth Network | PYTH | Solana-native oracle; Solana ecosystem infrastructure |
| Bonk | BONK | Solana-native memecoin; ecosystem representative |
| Dogwifhat | WIF | Solana meme flagship; high-volume HL perp |
| Helium | HNT | Solana-migrated DePIN; Solana ecosystem DePIN narrative |

**Constituent count:** 6. All require ≥ $3M daily HL perp volume.

## Selection Rule

Constituents must: (1) be a protocol, application, or token with primary activity on the Solana blockchain; (2) have ≥ $3M daily HL perp volume; (3) be deployed or operating on Solana mainnet (not just "Solana-adjacent").

## Weighting Scheme

**Equal-weight**. JUP and BONK/WIF are large-cap; RAY and PYTH are smaller but have distinct protocol utility. Equal-weight balances the meme component (BONK, WIF) with the DeFi component (RAY, JUP, PYTH).

## Rebalance Cadence

Weekly. Activate / deactivate the full basket based on Solana season gate (SOL outperforming ETH by > 10% over 30 days as the primary activation signal).

## Regime Character

Deploy ONLY when SOL is in a confirmed uptrend vs. ETH (SOL/ETH ratio rising). The basket is highly correlated within Solana season and loses its diversification benefits when SOL enters a bear market (all constituents decline together). Flat the basket when the SOL/ETH ratio reverses more than 15% from peak.

## Strategies That Deploy This Basket

- [[momentum-rotation]] — long Solana ecosystem in confirmed Solana-season regime
- [[cross-sectional-relative-value]] — long Solana DeFi leaders vs. short Solana underperformers
- [[alt-season-momentum-gate]] — Solana ecosystem is a primary alt-season rotation target
- [[narrative-position-vol-targeting]] — Solana ecosystem as a concentrated narrative position

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/candles?coin=JUP&interval=1h&limit=168` — per constituent
- `GET /api/v1/derivatives/funding-rates?coin=RAY`
- `GET /api/v1/derivatives/open-interest?coin=BONK`

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/candles?coin=JUP&interval=1d&limit=90"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-hyperliquid]].

## Related

[[hyperliquid-baskets-overview]] · [[l1-blockchains-basket]] · [[momentum-rotation]] · [[cross-sectional-relative-value]] · [[alt-season-momentum-gate]] · [[narrative-position-vol-targeting]] · [[edge-taxonomy]] · [[failure-modes]] · [[atr-position-sizing]]
