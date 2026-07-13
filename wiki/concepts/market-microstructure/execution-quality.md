---
title: "Execution Quality"
type: concept
created: 2026-04-15
updated: 2026-06-11
status: good
tags: [market-microstructure, execution, slippage, algorithmic]
aliases: ["Execution Quality", "execution-quality", "fill quality", "TCA", "transaction cost analysis"]
domain: [market-microstructure]
prerequisites: ["[[transaction-costs]]", "[[bid-ask-spread]]", "[[slippage]]"]
difficulty: intermediate
related: ["[[best-execution]]", "[[transaction-costs]]", "[[implementation-shortfall]]", "[[slippage]]", "[[market-impact]]", "[[vwap]]", "[[twap]]", "[[smart-order-routing]]", "[[payment-for-order-flow]]", "[[reg-nms]]", "[[dark-pools]]"]
---

**Execution quality** is the measure of how well an order was actually filled relative to a chosen benchmark price, capturing the realized cost of converting a trading decision into a position. Where [[best-execution]] is the *obligation* to seek favourable terms and [[transaction-costs]] are the *components* of cost, execution quality is the *ex-post measurement* — the scorecard that tells a desk whether its routing, timing, and algorithms are actually saving or leaking money.

## Overview

Two traders can submit the identical order and receive very different fills depending on venue, timing, order type, and market conditions. Execution quality quantifies that difference. The analysis is formalized as **Transaction Cost Analysis (TCA)** — the systematic comparison of realized fill prices against reference benchmarks, decomposed into the sources of slippage so a desk can attribute cost to spread, [[market-impact|market impact]], timing, and routing decisions.

Good execution is not simply "the lowest price." It is the best *combination* of price, speed, fill probability, and information leakage appropriate to the order. A marginally better price is worthless if the order does not fill, and a fast fill is expensive if it telegraphs intent and moves the market against the remaining size.

## How It Works

### Benchmarks

Execution quality is always measured *against something*. The common benchmarks:

- **Arrival price (decision price)** — the mid-quote at the moment the order was released. The difference between arrival price and the average fill is [[implementation-shortfall]], the most rigorous benchmark because it captures every cost including delay and unfilled quantity.
- **[[vwap|VWAP]]** — the volume-weighted average price over the order's lifetime. Beating VWAP means the desk traded better than the average market participant during that window. Easy to compute, but gameable (a trader can match VWAP by simply tracking volume) and blind to the cost of *deciding when to start*.
- **[[twap|TWAP]]** — time-weighted average price; a simpler schedule benchmark.
- **NBBO / quoted spread** — for retail and marketable orders, fills are compared to the [[reg-nms|National Best Bid and Offer]]. A fill *inside* the NBBO is **price improvement**; a fill outside it is a trade-through concern.
- **Close price** — relevant for index funds and end-of-day rebalancers benchmarked to the closing auction.

### The slippage decomposition

Implementation shortfall is decomposed into attributable buckets:

1. **Spread cost** — paying the [[bid-ask-spread]] to cross.
2. **Delay (timing) cost** — price drift between the decision and the first fill.
3. **[[market-impact|Market impact]]** — the order's own pressure on price, split into temporary (liquidity consumption) and permanent ([[adverse-selection|information leakage]]) components.
4. **Opportunity cost** — the cost of the unfilled portion when the order is cancelled or the limit is never reached.

Attributing cost to these buckets tells a desk *what to fix*: high impact suggests slowing the schedule or using [[dark-pools]]; high delay cost suggests trading more aggressively at the start; high opportunity cost suggests limits set too passively.

### Regulatory disclosure

In the US, execution quality is partly public. **SEC Rule 605** requires market centers to publish standardized statistics on speed, fill rates, effective spread, and price improvement; **Rule 606** requires brokers to disclose where they route orders and any [[payment-for-order-flow|payment for order flow]] received. These reports let clients compare brokers' realized fill quality rather than relying on marketing claims.

## Trading Relevance

- **Strategy viability.** For high-turnover or short-horizon strategies, execution quality is frequently the line between a backtested edge and a live loss. A naive backtest assuming mid-price fills silently assumes *perfect* execution quality; TCA reveals the real number. See [[transaction-costs]] and [[backtesting]].
- **Algo and venue selection.** Buy-side desks run TCA to choose between [[vwap]], [[twap]], implementation-shortfall, and liquidity-seeking algos, and to tune [[smart-order-routing]] across lit venues and [[dark-pools]].
- **Broker accountability.** Comparing realized [[slippage]] and Rule 606 routing across brokers exposes real differences in fill quality and is the practical enforcement mechanism behind the [[best-execution]] duty.
- **Retail price improvement.** Retail traders rarely route their own orders, so the price-improvement statistics on marketable orders (driven by wholesalers and PFOF arrangements) *are* their execution quality — making Rule 605/606 disclosures the most useful retail-facing measure.

## Sources

- SEC Rule 605 (market-center execution-quality statistics) and Rule 606 (order-routing disclosure) — official SEC rulebook
- FINRA Rule 5310 — "Best Execution and Interpositioning" ([[best-execution]])
- Larry Harris, *Trading and Exchanges: Market Microstructure for Practitioners* — execution measurement and venue selection ([[book-trading-and-exchanges]])
- Robert Kissell, *The Science of Algorithmic Trading and Portfolio Management* — Transaction Cost Analysis and implementation-shortfall decomposition
- Andre Perold (1988), "The Implementation Shortfall: Paper Versus Reality," *Journal of Portfolio Management*

## Related

- [[best-execution]] — the regulatory/fiduciary duty that execution quality measures compliance with
- [[transaction-costs]] — the cost components TCA decomposes
- [[implementation-shortfall]] — the arrival-price benchmark and gold-standard metric
- [[slippage]] — the realized gap between expected and actual fill
- [[market-impact]] — the largest cost component for institutional orders
- [[vwap]] / [[twap]] — schedule benchmarks and the algos built around them
- [[smart-order-routing]] — the technology optimizing where fills happen
- [[payment-for-order-flow]] — the routing arrangement Rule 606 exposes
