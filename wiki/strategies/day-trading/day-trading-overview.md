---
title: "Day Trading"
type: overview
created: 2026-04-06
updated: 2026-06-10
status: good
tags: [day-trading, scalping, market-microstructure]
aliases: ["Intraday Trading"]
related: ["[[strategies-overview]]", "[[swing-trading-overview]]", "[[technical-analysis-overview]]", "[[edge-taxonomy]]", "[[regime-matrix]]", "[[bar-resolution-selection]]", "[[multiple-timeframe-analysis]]", "[[microstructure-noise-low-timeframe]]", "[[intrabar-fill-modeling]]", "[[scalping]]", "[[hyperliquid]]"]
---

# Day Trading

Day trading is the family of intraday strategies in which every position is opened and closed within a single trading session, eliminating overnight risk. It requires fast decision-making, tight risk controls, and a deep understanding of intraday market dynamics — opening drives, midday lulls, and closing auctions. Successful day traders typically specialize in one or two setups and execute them with high consistency.

## What Distinguishes This Family

- **Edge sources** (see [[edge-taxonomy]]): primarily *structural* (intraday liquidity provision, predictable institutional execution flows such as VWAP benchmarking) and *behavioral* (retail overreaction to opens, news, and round numbers). At the fastest end it shades into *latency* edge, which is effectively closed to non-institutional traders.
- **Typical timeframes**: seconds to hours; bar resolutions from tick/1m up to 15m. Holding past the close is, by definition, out of scope.
- **Capital and data requirements**: modest capital is workable in crypto and futures, but US equities impose the pattern-day-trader rule (USD 25,000 minimum). Data needs are heavier than slower styles — real-time Level 2 / order book, time & sales (tape), and low-latency execution matter; end-of-day OHLCV is insufficient.
- **Cost sensitivity**: with many small trades, commissions, spread, and slippage dominate. A setup that survives on 15m bars can be entirely consumed by costs on 1m bars — see [[microstructure-noise-low-timeframe]] and [[intrabar-fill-modeling]].
- **Who it suits**: traders who can be present (or fully automated) during the session, tolerate high decision frequency, and treat execution quality as a first-class problem. It does not suit anyone unable to watch positions in real time or unwilling to log and review every trade.

## Strategies in This Category

- [[scalping]] — High-frequency, small-profit trades capturing bid-ask spread and micro-momentum
- [[vwap-trading]] — Using the volume-weighted average price, the institutional execution benchmark, as a dynamic intraday support/resistance level for entries and exits
- [[order-flow-scalping]] — Reading the real-time tape and order book to front-run short-term supply/demand imbalances
- [[market-making-strategy]] — Quoting both sides of the book to earn the spread while managing inventory risk

## Start Here

- [[scalping]] — the purest expression of the intraday edge, and the best illustration of why costs decide everything
- [[vwap-trading]] — the most accessible setup, anchored to a benchmark institutions are forced to track
- [[order-flow-scalping]] — the discretionary skill ceiling of the category: tape reading

## Choosing a Timeframe (1m / 3m / 5m / 15m)

The bar resolution you trade on is a first-order decision, not a cosmetic one. Finer bars (1m) give more granular signals and tighter stops but lower signal-to-noise and far more room to curve-fit; coarser bars (15m) give steadier signals and fewer trades but each fill error costs proportionally more. The methodology pages:

- [[bar-resolution-selection]] — the 1m vs 3m vs 5m vs 15m trade-off, and how to pick
- [[multiple-timeframe-analysis]] — stack a higher timeframe for bias with a lower one for entry timing
- [[microstructure-noise-low-timeframe]] — why a 1m "edge" often drowns in bid-ask bounce
- [[intrabar-fill-modeling]] — what really happens inside a 1m/5m bar, and how fill assumptions inflate results

### Crypto Perps Note (24/7, No Session)

The "single session" framing above is an equities convention. On crypto perpetuals — [[hyperliquid|Hyperliquid]] and the CEX venues — there is **no session close**: markets run 24/7, so "intraday" means a self-imposed holding window rather than a closing bell. Two consequences for day-trading perps: (1) higher-timeframe context never resets, so [[multiple-timeframe-analysis|multi-timeframe]] bias carries continuously; (2) liquidity and the [[microstructure-noise-low-timeframe|noise floor]] vary sharply by hour and weekday (thin Asia-hours and weekend books widen effective spreads). Funding accrues every hour on Hyperliquid (vs 8h on most CEXs), so even a same-day perp position can pay or earn funding mid-hold — see [[hyperliquid-funding-rate-microstructure]]. Backtesting any of these setups on fine bars is governed by [[crypto-perp-backtesting-pitfalls|crypto-perp backtesting pitfalls]].

## All Pages in This Folder

```dataview
TABLE status, updated, tags
FROM "wiki/strategies/day-trading"
WHERE type != "index" AND type != "overview"
SORT updated DESC
```

## Key Topics to Cover

- Momentum day trading
- Gap trading
- Level 2 and tape reading
- Pattern day trader rules
- Risk management for day traders

## Related

- [[strategies-overview]] — parent catalog of all strategy categories
- [[swing-trading-overview]] — the next timeframe up: multi-day to multi-week holds
- [[technical-analysis-overview]] — most intraday setups are technical at their core
- [[quantitative-overview]] — systematic treatments of intraday anomalies (e.g. [[session-overlap-momentum]])
- [[edge-taxonomy]] — which of the five edge sources an intraday setup actually exploits
- [[regime-matrix]] — which day-trading setups work in which market regimes
- [[market-microstructure-overview|Market microstructure]] — the mechanics underneath every intraday fill
