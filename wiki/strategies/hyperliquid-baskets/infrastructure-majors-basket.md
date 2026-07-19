---
title: "Infrastructure Majors Basket (Hyperliquid Basket)"
type: strategy
created: 2026-07-19
updated: 2026-07-19
status: good
tags: [crypto, perpetual-futures, hyperliquid, algorithmic, quantitative, momentum, altcoins, market-regime]
aliases: ["Crypto Infrastructure Basket", "Middleware Token Basket", "Protocol Infrastructure Basket"]
related: ["[[hyperliquid-baskets-overview]]", "[[momentum-rotation]]", "[[cross-sectional-relative-value]]", "[[crypto-beta-rotation]]", "[[defensive-majors]]", "[[narrative-position-vol-targeting]]", "[[alt-season-momentum-gate]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[funding-rate]]", "[[open-interest]]", "[[hyperliquid-liquidation-engine]]", "[[when-to-retire-a-strategy]]", "[[atr-position-sizing]]"]
strategy_type: quantitative
timeframe: swing
markets: [crypto]
complexity: intermediate
backtest_status: untested
edge_source: [structural, behavioral]
edge_mechanism: "Infrastructure tokens (oracles, data layers, identity protocols, sequencers) provide services to multiple blockchain ecosystems and are less tied to a single narrative cycle than sector tokens; they co-move with broad DeFi activity but exhibit lower narrative volatility, making them suitable as a 'quality alt' position in late-bear/early-bull regimes when narrative alts are too risky."
data_required: [ohlcv-daily, ohlcv-1h, funding-rates, open-interest, bitcoin-dominance-data]
min_capital_usd: 10000
capacity_usd: 40000000
crowding_risk: low
expected_sharpe: 0.7
expected_max_drawdown: 0.35
breakeven_cost_bps: 25
kill_criteria: |
  - basket drawdown > 35% from peak on a rolling 6-month basis
  - rolling 6-month Sharpe < 0 on minimum 10 completed trades
---

# Infrastructure Majors Basket (Hyperliquid Basket)

A basket of mid-to-large-cap crypto infrastructure tokens — oracles, data availability layers, identity, sequencers, and middleware — that serve multiple ecosystems and are less correlated with any single blockchain narrative. This is a "quality alt" basket suited for the late-bear / early-bull regime before sector-specific narratives emerge.

> **Not investment advice.** All performance figures are illustrative estimates. *Part of the [[hyperliquid-baskets-overview|Hyperliquid basket library]].*

## Edge Source

**Structural + behavioral** (see [[edge-taxonomy]]). Infrastructure tokens derive demand from actual protocol usage across ecosystems, giving them structural support beyond pure narrative. In early-bull regimes, they often lead because institutional capital prefers "picks and shovels" before committing to narrative-sector bets.

## Constituents

| Token | Ticker | Rationale |
|-------|--------|-----------|
| Chainlink | LINK | Dominant oracle; cross-ecosystem infrastructure |
| The Graph | GRT | Data indexing for DeFi and AI; cross-ecosystem |
| Celestia | TIA | Modular data availability layer; growing L2 demand |
| EigenLayer | EIGEN | Restaking middleware; Ethereum security layer |
| Ethereum Name Service | ENS | Identity/naming; highest Ethereum ecosystem lock-in |
| Pyth Network | PYTH | High-frequency oracles; cross-chain financial data |

**Constituent count:** 6. Minimum $3M daily HL perp volume.

## Selection Rule

Constituents must: (1) be a cross-ecosystem infrastructure protocol serving ≥ 2 blockchain networks; (2) have verifiable on-chain usage metrics (oracle queries, indexer queries, data blobs, etc.); (3) ≥ $3M daily HL perp volume.

## Weighting Scheme

**Equal-weight**. LINK is larger but also the most liquid; TIA and EIGEN are newer with higher growth potential. Equal-weight balances established infrastructure with newer infrastructure leaders.

## Rebalance Cadence

Weekly. Infrastructure tokens rotate more slowly than narrative tokens; monthly cadence is acceptable if transaction costs are a concern.

## Regime Character

Best in **early bull / late bear** as a quality alt position. Outperforms narrative-sector tokens in periods of macro uncertainty. Underperforms in peak speculative regimes where meme and gaming tokens capture retail attention. Cross-ecosystem diversification makes this basket less sensitive to single-ecosystem failures.

## Strategies That Deploy This Basket

- [[momentum-rotation]] — infrastructure alts as quality momentum position in early rotation
- [[crypto-beta-rotation]] — infrastructure basket as the "quality" component of an alt allocation
- [[cross-sectional-relative-value]] — cross-ecosystem infrastructure leaders vs. laggards
- [[defensive-majors]] — infrastructure basket as a quality add-on when pure BTC/ETH exposure is insufficient

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/candles?coin=LINK&interval=1h&limit=168` — per constituent
- `GET /api/v1/derivatives/funding-rates?coin=LINK`
- `GET /api/v1/derivatives/open-interest?coin=TIA`

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/candles?coin=TIA&interval=1d&limit=90"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-hyperliquid]].

## Related

[[hyperliquid-baskets-overview]] · [[oracle-basket]] · [[defensive-majors]] · [[momentum-rotation]] · [[cross-sectional-relative-value]] · [[crypto-beta-rotation]] · [[narrative-position-vol-targeting]] · [[edge-taxonomy]] · [[failure-modes]] · [[atr-position-sizing]]
