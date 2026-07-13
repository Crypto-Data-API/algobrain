---
title: "Jigsaw Trading"
type: entity
created: 2026-04-10
updated: 2026-06-10
status: good
tags: [order-flow, trading-tools, market-microstructure, day-trading]
entity_type: company
website: "https://www.jigsawtrading.com"
aliases: ["Jigsaw", "Jigsaw Trading"]
related: ["[[order-flow]]", "[[footprint-charts]]", "[[order-book]]", "[[bookmap]]", "[[tape-reading]]"]
---

# Jigsaw Trading

**Jigsaw Trading** is an [[order-flow]] trading platform and education provider specializing in reconstructed tape, advanced [[depth-of-market]] (DOM) tools, and structured training for reading live order flow. Founded by Peter Davies, Jigsaw focuses on giving traders the ability to read institutional intent from the raw transaction data — a modern evolution of [[tape-reading]] that dates back to Jesse Livermore and Richard Wyckoff.

## Platform: Jigsaw Daytradr

The core product is **Jigsaw Daytradr**, a standalone order flow analysis and trade execution platform. It can also run as a plugin within NinjaTrader. Key tools include:

### Summary Tape

The Summary Tape condenses the raw time and sales feed into a readable format by aggregating trades at each price level over configurable intervals. Instead of watching thousands of individual prints scroll past, traders see net buying vs selling pressure at each price, updated in real time. This makes it practical to identify when aggressive buyers or sellers are dominating at a specific level.

### Reconstructed Tape

Jigsaw's signature innovation. The Reconstructed Tape groups individual trade prints back into the likely original orders that generated them. When a large institution sends a 500-lot order that gets filled across dozens of small prints, the reconstructed tape shows it as a single large order rather than noise. This reconstruction reveals the footprint of institutional activity that is invisible on a standard time and sales window.

### Auction Vista

Auction Vista provides a visual representation of order flow over time, showing cumulative buying and selling at each price level as colored bars. It serves a similar purpose to [[footprint-charts]] but with Jigsaw's own visual approach, designed to highlight [[absorption]], exhaustion, and initiative activity at key price levels.

### DOM (Depth of Market)

Jigsaw's enhanced DOM displays current bid/ask depth alongside historical order placement and pulling activity. Traders can see not just what is on the book now, but how the book has changed — orders that were placed and then pulled (potential spoofing) vs orders that remained firm as price approached (genuine institutional interest).

## How It Differs from Bookmap

While [[bookmap|Bookmap]] excels at visual heatmap representation of the full order book over time, Jigsaw focuses on the **transaction data** — what actually traded, in what size, and how to reconstruct the original orders behind the prints. Bookmap answers "where is liquidity resting?" while Jigsaw answers "who is actually buying and selling, and how aggressively?" The two platforms are complementary, and many professional [[order-flow]] traders use both.

## Educational Resources

Jigsaw is known for its structured education program, which is unusual for a trading software company. The platform includes:

- **Order Flow Trading Course** — a multi-module program covering DOM reading, tape reading, and order flow interpretation
- **Live Trading Room** — sessions where traders analyze markets in real time using Jigsaw's tools
- **Trading Combine** — a simulated evaluation program where traders must demonstrate profitability before receiving a funded account referral

This educational emphasis reflects Jigsaw's philosophy that order flow tools without proper training are useless — the data is meaningless without the skill to interpret it in context.

## Supported Markets

Jigsaw connects to [[futures]] markets via CQG and Rithmic data feeds, covering the [[cme|CME]], CBOT, NYMEX, COMEX, ICE, and Eurex. The platform is primarily designed for futures traders, particularly those trading ES (E-mini S&P 500), NQ (E-mini NASDAQ), CL (crude oil), and Treasury futures.

## Trading Relevance

Jigsaw is referenced in the [[smart-money-orderflow-combo|Smart Money + Order Flow Combo]] strategy as a key tool for reconstructed tape analysis. When a trader identifies an [[order-blocks|order block]] or [[fair-value-gaps|fair value gap]] using [[smart-money-concepts]], Jigsaw's reconstructed tape can confirm whether large institutional orders are actually being executed at that level — providing the execution-level confirmation that turns a structural hypothesis into a high-probability trade.

## See Also

- [[bookmap]] — Heatmap-based order flow visualization platform
- [[sierra-chart]] — Professional charting with footprint chart capabilities
- [[order-flow]] — The broader concept of analyzing transaction data
- [[tape-reading]] — Historical practice that Jigsaw modernizes
- [[footprint-charts]] — Related volume-at-price visualization

## Sources

- [Jigsaw Trading official site](https://www.jigsawtrading.com) — product documentation for Daytradr, Summary/Reconstructed Tape, Auction Vista, and supported data feeds (CQG, Rithmic)
- Page content reviewed against vendor documentation, 2026-06-10. Jigsaw is a private company; no public financials.
