---
title: Order Flow
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags: [order-flow, market-microstructure, liquidity]
aliases: ["Order Flow", "tape", "time and sales"]
domain: [market-microstructure]
prerequisites: ["[[order-book]]", "[[bid-ask-spread]]"]
difficulty: intermediate
related:
  - "[[order-book]]"
  - "[[order-flow-analysis]]"
  - "[[price-discovery]]"
  - "[[volume]]"
  - "[[market-maker]]"
  - "[[liquidity]]"
  - "[[order-flow-imbalance]]"
  - "[[book-trading-and-exchanges]]"
  - "[[book-flash-boys]]"
---

Order flow is the stream of buy and sell orders entering the market. Where the [[order-book]] shows *resting* orders (intentions), order flow is about *executions* (actions) — who is aggressively buying or selling, at what size, and against which side of the book. It is the rawest, most granular view of market activity and the substrate from which prices are formed.

## Overview

By analyzing who is aggressively buying or selling — and at what size — traders can identify institutional activity, shifting momentum, and potential turning points before they appear on price charts. Order flow is the engine of [[price-discovery]]: price moves when aggressive orders consume resting liquidity faster than it can be replenished. The broader discipline of studying this stream is covered in [[order-flow-analysis]]; this page defines the underlying phenomenon and its core vocabulary.

## How It Works

- **Aggressive vs passive orders**: Market orders (aggressive, "takers") cross the spread and consume resting liquidity. Limit orders (passive, "makers") add liquidity to the book. An imbalance of aggressive orders on one side signals directional conviction.
- **Tape reading**: Watching the time-and-sales feed (the "tape") to observe individual trades — their size, price, and whether they hit the bid (seller-initiated) or lift the ask (buyer-initiated).
- **Delta**: The difference between volume traded at the ask (buying pressure) and volume traded at the bid (selling pressure) over a period. Positive delta = net buying; negative delta = net selling. The running total is **cumulative delta**, and its divergence from price is a classic signal.
- **Footprint charts**: Visual representations (see [[footprint-charts]]) that show traded volume split by bid/ask within each price bar, exposing imbalances and exhaustion.

## Key Concepts

- **Toxic flow**: Order flow from informed traders that consistently moves the market against [[market-maker|market makers]] (Source: [[book-trading-and-exchanges]]). Market makers respond by widening spreads or pulling quotes when they detect toxic flow — the [[adverse-selection]] problem, quantified by metrics like [[vpin|VPIN]] and [[order-flow-imbalance|OFI]].
- **Absorption**: When large resting orders absorb aggressive selling (or buying) without price moving — indicates strong passive demand/supply at that level and is one of the highest-conviction signals.
- **Exhaustion**: When aggressive buying pushes price up but volume delta starts declining, suggesting the move is running out of fuel.

## Trading Relevance

Order flow analysis provides the most granular view of market activity available (Source: [[book-flash-boys]]). It is particularly valuable at key [[support-and-resistance]] levels, where you can observe whether resting orders are being defended or consumed. It is most actionable in centralized, transparent markets (futures, some crypto venues) and least reliable in fragmented equity markets where flow scatters across dozens of venues and dark pools. While more complex than chart-based analysis, order flow reveals the "why" behind price movements in real time.

## Sources

- [[book-trading-and-exchanges]] — the definitive academic text on order flow, covering informed vs. uninformed flow, toxic flow, adverse selection, and how order flow drives price discovery
- [[book-flash-boys]] — narrative account of how high-frequency traders exploit order flow advantages and the structural issues in modern market plumbing
- Larry Harris, *Trading and Exchanges* (Oxford University Press, 2003) — chapters on order-driven markets and the economics of liquidity supply.

## Related

- [[order-book]] — the static counterpart to dynamic order flow
- [[order-flow-analysis]] — the methodology and tooling for trading order flow
- [[order-flow-imbalance]] — a formal quantitative measure of net order pressure
- [[price-discovery]] — order flow drives price discovery
- [[volume]] — order flow disaggregates volume into buy/sell components
- [[market-maker]] — reacts to and is affected by order flow
- [[smart-money-orderflow-combo]] — combining order flow with smart money concepts for trade signals
- [[stop-hunting-and-liquidity-sweeps]] — how large players exploit order flow concentrations
