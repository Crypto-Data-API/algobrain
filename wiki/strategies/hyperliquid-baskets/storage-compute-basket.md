---
title: "Storage / Compute Basket (Hyperliquid Basket)"
type: strategy
created: 2026-07-19
updated: 2026-07-19
status: good
tags: [crypto, perpetual-futures, hyperliquid, algorithmic, quantitative, momentum, altcoins, market-regime]
aliases: ["Decentralised Storage Basket", "Compute Infrastructure Basket", "Storage Token Basket", "Cloud Compute Crypto Basket"]
related: ["[[hyperliquid-baskets-overview]]", "[[depin-basket]]", "[[ai-tokens-basket]]", "[[momentum-rotation]]", "[[cross-sectional-relative-value]]", "[[narrative-position-vol-targeting]]", "[[alt-season-momentum-gate]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[funding-rate]]", "[[open-interest]]", "[[hyperliquid-liquidation-engine]]", "[[when-to-retire-a-strategy]]", "[[atr-position-sizing]]"]
strategy_type: quantitative
timeframe: swing
markets: [crypto]
complexity: intermediate
backtest_status: untested
edge_source: [behavioral, informational]
edge_mechanism: "Storage and compute tokens benefit from AI demand for decentralised infrastructure, co-moving on shared GPU-compute and data-storage narratives; within-sector dispersion tracks which protocol is gaining storage/compute utilisation, creating cross-sectional harvest as AI workloads grow unevenly across decentralised networks."
data_required: [ohlcv-daily, ohlcv-1h, funding-rates, open-interest, bitcoin-dominance-data]
min_capital_usd: 8000
capacity_usd: 20000000
crowding_risk: medium
expected_sharpe: 0.7
expected_max_drawdown: 0.42
breakeven_cost_bps: 35
kill_criteria: |
  - basket drawdown > 42% from peak on a rolling 6-month basis
  - rolling 6-month Sharpe < 0 on minimum 10 completed trades
  - AI-demand narrative collapses (no AI model launches for > 6 months)
---

# Storage / Compute Basket (Hyperliquid Basket)

A sector basket of decentralised storage and compute tokens with active Hyperliquid perpetuals. These tokens are infrastructure layers for decentralised data storage (Filecoin, Arweave, Storj) and decentralised compute (Render, Akash, io.net) — overlapping with the DePIN and AI narratives but forming a distinct infrastructure cluster.

> **Not investment advice.** All performance figures are illustrative estimates. *Part of the [[hyperliquid-baskets-overview|Hyperliquid basket library]].*

## Edge Source

**Behavioral + informational** (see [[edge-taxonomy]]). Storage and compute tokens react to AI-demand narratives (GPU shortage news, large model training announcements) and to on-chain utilisation metrics (storage filled, compute hours sold) that are observable before fully priced.

## Constituents

| Token | Ticker | Rationale |
|-------|--------|-----------|
| Filecoin | FIL | Largest decentralised storage; established ecosystem |
| Arweave | AR | Permanent storage; distinct data-permanence narrative |
| Render | RNDR | Decentralised GPU rendering; AI compute narrative |
| Akash Network | AKT | Decentralised cloud compute marketplace |
| io.net | IO | GPU compute for AI inference; fastest-growing |
| Storj | STORJ | Distributed cloud storage; enterprise focus |

**Constituent count:** 6. Minimum $2M daily HL perp volume.

## Selection Rule

Constituents must: (1) provide decentralised storage OR compute infrastructure with verifiable network utilisation; (2) have active paying users (not just testnet); (3) ≥ $2M daily HL perp volume.

## Weighting Scheme

**Equal-weight**. FIL is larger; RNDR and RNDR-equivalents are currently high-momentum AI plays. Consider vol-weighting to balance the AI-compute (high-volatility) vs. storage (lower-volatility) split.

## Rebalance Cadence

Weekly. AI-demand events trigger out-of-cycle rebalances (e.g., major GPU shortage announcement, large model training capacity milestone).

## Regime Character

Highly correlated with AI narrative momentum and with tech-sector sentiment (Nasdaq correlation during AI hype cycles). RNDR and AKT move most with AI narratives; FIL and AR move more independently on storage-specific events. The basket as a whole is an AI-adjacent infrastructure play.

## Strategies That Deploy This Basket

- [[momentum-rotation]] — long storage/compute when sector ranks top momentum quintile
- [[cross-sectional-relative-value]] — long compute tokens vs. short storage tokens during AI-demand cycles
- [[depin-basket]] — overlapping constituents; storage/compute basket is the more specific cut
- [[ai-tokens-basket]] — overlapping compute tokens (RNDR, AKT, IO)
- [[narrative-position-vol-targeting]] — decentralised infrastructure narrative position

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/candles?coin=FIL&interval=1h&limit=168` — per constituent
- `GET /api/v1/derivatives/funding-rates?coin=RNDR`
- `GET /api/v1/derivatives/open-interest?coin=FIL`

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/candles?coin=FIL&interval=1d&limit=90"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-hyperliquid]].

## Related

[[hyperliquid-baskets-overview]] · [[depin-basket]] · [[ai-tokens-basket]] · [[momentum-rotation]] · [[cross-sectional-relative-value]] · [[narrative-position-vol-targeting]] · [[edge-taxonomy]] · [[failure-modes]] · [[atr-position-sizing]]
