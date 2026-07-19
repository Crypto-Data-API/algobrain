---
title: "Payments Basket (Hyperliquid Basket)"
type: strategy
created: 2026-07-19
updated: 2026-07-19
status: good
tags: [crypto, perpetual-futures, hyperliquid, algorithmic, quantitative, momentum, altcoins, market-regime]
aliases: ["Crypto Payments Basket", "Payments Protocol Basket", "Remittance Crypto Basket", "Settlement Token Basket"]
related: ["[[hyperliquid-baskets-overview]]", "[[momentum-rotation]]", "[[cross-sectional-relative-value]]", "[[narrative-position-vol-targeting]]", "[[alt-season-momentum-gate]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[funding-rate]]", "[[open-interest]]", "[[hyperliquid-liquidation-engine]]", "[[when-to-retire-a-strategy]]", "[[atr-position-sizing]]"]
strategy_type: quantitative
timeframe: swing
markets: [crypto]
complexity: intermediate
backtest_status: untested
edge_source: [behavioral, informational]
edge_mechanism: "Payments tokens react to real-world adoption announcements (merchant partnerships, remittance corridor launches, CBDC integration news) and to regulatory environment shifts for cross-border payments; the sector co-moves on these shared catalysts while within-sector dispersion tracks which networks are winning payment volume."
data_required: [ohlcv-daily, ohlcv-1h, funding-rates, open-interest, bitcoin-dominance-data]
min_capital_usd: 8000
capacity_usd: 20000000
crowding_risk: low
expected_sharpe: 0.6
expected_max_drawdown: 0.40
breakeven_cost_bps: 32
kill_criteria: |
  - basket drawdown > 40% from peak on a rolling 6-month basis
  - rolling 6-month Sharpe < 0 on minimum 10 completed trades
---

# Payments Basket (Hyperliquid Basket)

A sector basket of crypto payments and settlement protocol tokens with active Hyperliquid perpetuals. Payments tokens target the use case of faster, cheaper cross-border payments, remittances, and merchant settlements — they carry real-world adoption narratives distinct from DeFi or speculative tokens.

> **Not investment advice.** All performance figures are illustrative estimates. *Part of the [[hyperliquid-baskets-overview|Hyperliquid basket library]].*

## Edge Source

**Behavioral + informational** (see [[edge-taxonomy]]). Payments tokens react to observable adoption announcements that create predictable short-term price momentum.

## Constituents

| Token | Ticker | Rationale |
|-------|--------|-----------|
| XRP | XRP | Largest payments token; Ripple; SEC legal resolution narrative |
| Stellar | XLM | Cross-border payments; IBM/Stellar partnerships |
| Nano | XNO | Feeless instant payments; environmental angle |
| Celo | CELO | Mobile-first payments; emerging markets |
| Request Network | REQ | Crypto invoicing and B2B payments |

**Constituent count:** 5. Minimum $2M daily HL perp volume; verify HL perp availability for all constituents.

## Selection Rule

Constituents must: (1) have a primary use case of payments, remittances, or financial settlement on-chain; (2) have an operational payment network (not just a theoretical whitepaper); (3) ≥ $2M daily HL perp volume.

## Weighting Scheme

**Equal-weight**. XRP is dramatically larger than other constituents; equal-weight provides meaningful exposure to smaller payments tokens.

## Rebalance Cadence

Weekly. Event-driven rebalance on major payments adoption news (e.g., Ripple SEC resolution, new financial institution partnerships).

## Regime Character

Performs in institutional/regulatory-positive crypto narratives. XRP is the most litigation-driven; tends to pump on SEC-related news. Other payments tokens are relatively immune to DeFi narratives. Weakest in pure speculative cycles where retail ignores utility tokens.

## Strategies That Deploy This Basket

- [[momentum-rotation]] — long payments when sector ranks top momentum quintile
- [[cross-sectional-relative-value]] — long XRP vs. alternatives during Ripple-specific catalysts
- [[narrative-position-vol-targeting]] — payments as an institutional-adoption narrative overlay

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/candles?coin=XRP&interval=1h&limit=168` — per constituent
- `GET /api/v1/derivatives/funding-rates?coin=XRP`
- `GET /api/v1/derivatives/open-interest?coin=XRP`

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/candles?coin=XRP&interval=1d&limit=90"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-hyperliquid]].

## Related

[[hyperliquid-baskets-overview]] · [[momentum-rotation]] · [[cross-sectional-relative-value]] · [[narrative-position-vol-targeting]] · [[edge-taxonomy]] · [[failure-modes]] · [[atr-position-sizing]]
