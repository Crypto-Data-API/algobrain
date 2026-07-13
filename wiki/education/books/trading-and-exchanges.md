---
title: "Trading and Exchanges — Larry Harris (2003)"
type: concept
created: 2026-04-07
updated: 2026-06-21
status: excellent
tags: [education, book, market-microstructure, liquidity]
aliases: ["Trading and Exchanges", "Harris Market Microstructure"]
related:
  - "[[market-microstructure]]"
  - "[[order-flow-scalping]]"
  - "[[market-making-strategy]]"
  - "[[implementation-shortfall]]"
  - "[[order-types]]"
  - "[[liquidity]]"
  - "[[flash-boys]]"
---

**Trading and Exchanges: Market Microstructure for Practitioners** by Larry Harris (2003) is the definitive practitioner-oriented textbook on how markets actually work. Harris, a finance professor at USC and a former chief economist of the SEC, covers the full machinery of [[market-microstructure]]: who trades and why, order types and their strategic implications, the economics of market making, informed vs. uninformed flow, transaction costs (explicit and implicit), market-quality measurement, and the regulation of trading. At roughly 640 pages it is comprehensive — and deliberately about the *machinery* all strategies operate within, not about strategies themselves.

## Key Facts

| Field | Detail |
|-------|--------|
| **Author** | Lawrence E. ("Larry") Harris — USC Marshall; ex-SEC Chief Economist (2002–2004) |
| **Published** | 2003 (Oxford University Press) |
| **Subtitle** | *Market Microstructure for Practitioners* |
| **Length** | ~640 pages |
| **Math level** | Low — conceptual and institutional, almost no calculus required |
| **Audience** | Practitioners, regulators, exchange designers, quants, MBA/finance students |
| **Status** | Standard reference text in market microstructure courses |
| **Scope** | Trader taxonomy, order types, liquidity, costs, market structure, regulation |

## Core Thesis

Trading is a negotiation between parties with different information, motives, and time horizons, mediated by an institutional structure (exchanges, brokers, dealers, rules) that determines who profits. Understanding *who is on the other side of your trade* — and what the structure costs you — is prerequisite to trading well. Liquidity, price discovery, and transaction costs are the central organizing concepts, and they frequently trade off against one another.

## Chapter / Section Themes

- **The structure of markets.** Trading sessions, order-driven vs. quote-driven (dealer) markets, brokers, dealers, and exchanges.
- **The benefits of trading.** Why utilitarian, informed, and profit-motivated traders participate; the social value of liquidity and price discovery.
- **The traders.** A taxonomy — informed traders, dealers/market makers, uninformed (liquidity/utilitarian) traders, parasitic traders (front-runners, manipulators) vs. beneficial ones.
- **Orders and order properties.** Market, limit, stop, and contingent orders; the strategic trade-off between execution certainty and price.
- **Bid/ask spreads.** The three-component theory of the spread.
- **Liquidity and transaction costs.** The "iceberg" of costs beneath visible commissions; market impact and timing risk.
- **Informed trading and market efficiency.** Adverse selection, price discovery, and the informativeness of order flow.
- **Origins of liquidity and volatility.** What makes markets deep, resilient, and tight — or not.
- **Evaluating and regulating markets.** Market-quality dimensions and how rules (tick size, transparency, access) shape outcomes.

## Key Concepts / Takeaways

| Concept | Takeaway |
|---------|----------|
| **Informed vs. uninformed traders** | Market makers profit from uninformed flow and lose to informed flow; know which you are. |
| **Order types as strategy** | Limit orders supply liquidity, earn the spread, and bear adverse selection; market orders pay the spread for certainty (see [[order-types]]). |
| **Three-component spread** | The bid–ask spread compensates for order-processing, inventory-holding, and adverse-selection costs. |
| **Iceberg of transaction costs** | Commissions are visible but often dwarfed by spread, market impact, delay, and opportunity costs. |
| **Market impact** | Function of order size, urgency, and information content; large orders move price against you. |
| **Liquidity dimensions** | Depth, breadth, tightness (spread), resilience, and immediacy — distinct facets of [[liquidity]]. |
| **Market quality** | Liquidity, price-discovery efficiency, volatility, and cost — dimensions that often trade off. |
| **Regulation shapes structure** | Tick sizes, order-handling rules, transparency, and access rules determine who profits. |
| **Parasitic vs. beneficial traders** | Some strategies (front-running, manipulation) extract value without adding it; others provide real services. |

## Criticisms / Limitations

- **Dated in specifics.** Written in 2003 — it predates Reg NMS (2007), the explosion of [[high-frequency-trading]], maker-taker proliferation, and modern dark-pool-trading. The principles endure; the institutional details have moved on (see [[flash-boys]] for the post-2007 world).
- **Not a strategy book.** It explains the arena, not how to win in it; readers wanting alpha must look elsewhere.
- **Length and density.** ~640 pages; best used as a reference rather than a cover-to-cover read.
- **U.S./equity bias.** Examples skew toward U.S. equities; crypto, FX, and modern electronic venues are not covered.
- **Light on quantitative models.** The deliberately low-math approach means readers seeking formal microstructure models (Kyle, Glosten-Milgrom, Almgren-Chriss) must supplement it.

## Who Should Read This

Anyone building execution algorithms or market-making systems. Quants who need to understand why their strategies face the transaction costs they do. Regulators and exchange designers. Traders who want to understand the game they are playing at a structural level. Academic but readable — no advanced math required. Pairs naturally with [[flash-boys]] for the narrative version of the modern landscape.

## How It Applies to AI Trading

Understanding [[market-microstructure]] is not optional for anyone building trading algorithms. This book explains why [[order-flow-scalping]] can work (informed order flow is partially detectable), how [[market-making-strategy]] profits and manages risk (the spread compensates for adverse selection), why [[implementation-shortfall]] matters (the gap between decision price and execution price is where alpha leaks), and what determines the real cost of any strategy. Every assumption in your [[backtesting|backtest]] about fills, slippage, and market impact should be grounded in the microstructure principles Harris explains — otherwise your simulated P&L is fiction.

## Rating

**9/10** — The microstructure bible. Dense and academic in places, but indispensable. Not a cover-to-cover read for most — use it as a reference when you need deep understanding of a specific market-mechanics topic. Pairs with [[flash-boys]] for the narrative version.

## Related

- [[market-microstructure]] — The field this book defines for practitioners
- [[order-types]] — Strategic implications of limit, market, stop, and contingent orders
- [[order-flow-scalping]] — Detecting and trading on informed order flow
- [[market-making-strategy]] — The economics of providing liquidity
- [[implementation-shortfall]] — Measuring and minimizing execution costs
- [[liquidity]] — Depth, tightness, resilience, and immediacy
- [[flash-boys]] — Accessible narrative covering the modern, post-Reg-NMS structure

## Sources

General market knowledge; no specific wiki source ingested yet.
