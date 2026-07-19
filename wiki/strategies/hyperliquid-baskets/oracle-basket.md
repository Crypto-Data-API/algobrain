---
title: "Oracle Basket (Hyperliquid Basket)"
type: strategy
created: 2026-07-19
updated: 2026-07-19
status: good
tags: [crypto, perpetual-futures, hyperliquid, algorithmic, quantitative, momentum, altcoins, market-regime]
aliases: ["Oracle Token Basket", "Price Feed Protocol Basket", "Oracle Network Basket"]
related: ["[[hyperliquid-baskets-overview]]", "[[momentum-rotation]]", "[[cross-sectional-relative-value]]", "[[narrative-position-vol-targeting]]", "[[alt-season-momentum-gate]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[funding-rate]]", "[[open-interest]]", "[[hyperliquid-liquidation-engine]]", "[[when-to-retire-a-strategy]]", "[[atr-position-sizing]]"]
strategy_type: quantitative
timeframe: swing
markets: [crypto]
complexity: intermediate
backtest_status: untested
edge_source: [behavioral, structural]
edge_mechanism: "Oracle tokens share a critical infrastructure narrative — they power DeFi, RWA, and AI applications — that makes them co-move with broad DeFi activity cycles; within-sector dispersion tracks which oracle provider is winning market share (data feed counts, integrations), creating cross-sectional harvest between the dominant provider and challengers."
data_required: [ohlcv-daily, ohlcv-1h, funding-rates, open-interest, bitcoin-dominance-data]
min_capital_usd: 8000
capacity_usd: 20000000
crowding_risk: low
expected_sharpe: 0.7
expected_max_drawdown: 0.38
breakeven_cost_bps: 30
kill_criteria: |
  - basket drawdown > 38% from peak on a rolling 6-month basis
  - rolling 6-month Sharpe < 0 on minimum 10 completed trades
---

# Oracle Basket (Hyperliquid Basket)

A sector basket of blockchain oracle protocol tokens with active Hyperliquid perpetuals. Oracle networks provide price feeds and external data to smart contracts — they are critical infrastructure for DeFi, RWA, and AI-agent applications. The sector is less speculative than meme or gaming baskets and benefits from "picks and shovels" narratives during any DeFi expansion.

> **Not investment advice.** All performance figures are illustrative estimates. *Part of the [[hyperliquid-baskets-overview|Hyperliquid basket library]].*

## Edge Source

**Behavioral + structural** (see [[edge-taxonomy]]). Oracle tokens have structural support from genuine on-chain demand for data feeds (every DeFi protocol requires them). Behavioral momentum arises from oracle-narrative cycles tied to DeFi expansion, AI-agent data demand, and real-world data tokenisation.

## Constituents

| Token | Ticker | Rationale |
|-------|--------|-----------|
| Chainlink | LINK | Dominant oracle network; most integrations |
| Pyth Network | PYTH | High-frequency financial data; Solana native |
| API3 | API3 | First-party oracle model; dAPI narrative |
| Band Protocol | BAND | Cross-chain oracle; Cosmos ecosystem |
| UMA Protocol | UMA | Optimistic oracle for complex data types |

**Constituent count:** 5. Minimum $2M daily HL perp volume.

## Selection Rule

Constituents must: (1) operate an oracle network providing external data to smart contracts; (2) have verifiable on-chain integrations (number of data feeds, protocols using the oracle); (3) ≥ $2M daily HL perp volume.

## Weighting Scheme

**Equal-weight**. LINK is dramatically larger than other constituents; equal-weight provides meaningful exposure to challenger oracles (PYTH, API3) where narrative moves are larger.

## Rebalance Cadence

Weekly. Out-of-cycle rebalance on major oracle integration announcements (new protocol adoption, cross-chain expansion).

## Regime Character

Correlated with broad DeFi activity. Performs when DeFi TVL is growing and when new data-hungry applications (AI agents, RWA) expand oracle demand. LINK is the most defensive oracle token (deepest institutional integration); PYTH and API3 are higher-beta challengers. Weakest in bear markets when DeFi activity collapses and oracle demand falls.

## Strategies That Deploy This Basket

- [[momentum-rotation]] — long oracles when sector ranks top momentum quintile
- [[cross-sectional-relative-value]] — long challenger oracle winners vs. short LINK in periods of challenger-narrative dominance
- [[narrative-position-vol-targeting]] — oracle infrastructure as a "picks and shovels" narrative position

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/candles?coin=LINK&interval=1h&limit=168` — per constituent
- `GET /api/v1/derivatives/funding-rates?coin=LINK`
- `GET /api/v1/derivatives/open-interest?coin=LINK`

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/candles?coin=LINK&interval=1d&limit=90"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-hyperliquid]].

## Related

[[hyperliquid-baskets-overview]] · [[momentum-rotation]] · [[cross-sectional-relative-value]] · [[narrative-position-vol-targeting]] · [[alt-season-momentum-gate]] · [[defi-bluechip-basket]] · [[edge-taxonomy]] · [[failure-modes]] · [[atr-position-sizing]]
