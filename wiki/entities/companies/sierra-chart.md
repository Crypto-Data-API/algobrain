---
title: "Sierra Chart"
type: entity
created: 2026-04-10
updated: 2026-06-10
status: good
tags: [order-flow, trading-tools, technical-analysis, futures]
entity_type: company
founded: 1996
website: "https://www.sierrachart.com"
aliases: ["Sierra Chart", "Sierra-Chart", "SierraChart", "Sierra Charts"]
related: ["[[footprint-charts]]", "[[order-flow]]", "[[volume-profile]]", "[[bookmap]]", "[[quantower]]", "[[futures]]"]
---

**Sierra Chart** is a professional-grade charting and trading platform known for its exceptional reliability, low-latency data handling, and deep [[order-flow]] analysis capabilities. It has been in continuous development since 1996, making it one of the longest-running trading platforms still actively maintained. Sierra Chart is the tool of choice for many professional [[futures]] traders, prop desks, and quantitative developers who require precise, fast, and highly customizable market analysis. (Note: Sierra Chart is a privately held software vendor, not a listed company — there is no ticker; traders engage with it as a tool, not an investment.)

## Overview

Unlike platforms that prioritize visual polish, Sierra Chart prioritizes **performance and accuracy**. Its interface is utilitarian — reminiscent of early 2000s Windows software — but its engine processes market data with minimal latency and high fidelity. The platform supports real-time and historical charting, direct order execution, and a full suite of [[technical-analysis]] and [[order-flow]] tools. It connects natively to major data feeds and exchanges, handling tick-by-tick data for the most liquid instruments without bottlenecks.

## Key Features

### Footprint Charts and Order Flow

Sierra Chart provides comprehensive [[footprint-charts]] (called "Numbers Bars" in Sierra's terminology) that display bid/ask volume, [[delta]], and imbalance ratios at every price level within each bar. Traders can configure these to show:

- **Bid x Ask volume** at each price level
- **Delta per bar** and cumulative delta across sessions
- **Imbalance highlighting** where buying or selling aggression exceeds a configurable threshold
- **Diagonal imbalance stacking** that reveals institutional absorption patterns

These footprint capabilities make Sierra Chart a core tool for [[order-flow]] traders who need granular volume data beyond what standard candlestick charts provide.

### Volume Profile

Sierra Chart's [[volume-profile]] implementation is highly regarded. Traders can display volume profiles on any timeframe — session, composite, or custom range — with point of control (POC), value area high (VAH), and value area low (VAL) automatically calculated. The developing profile updates in real time, showing how the auction is unfolding within the current session.

### Market Depth and DOM

The platform includes a functional [[depth-of-market]] (DOM) trading ladder with historical depth recording, allowing traders to replay how the order book evolved at key price levels. While less visually intuitive than [[bookmap|Bookmap's]] heatmap, Sierra Chart's DOM data is precise and can be integrated into custom studies.

### ACSIL Custom Study Development

Sierra Chart's **Advanced Custom Study Interface and Language (ACSIL)** allows traders and developers to write custom indicators, strategies, and automated trading systems in C++. This provides near-native execution speed and access to the full range of market data (tick data, order book snapshots, position data). ACSIL is significantly more powerful than scripting languages found in retail platforms, but the learning curve is steep — it is effectively C++ programming against Sierra Chart's API.

## Pricing

Sierra Chart uses a service-based pricing model. The base platform starts at $26/month (Service Package 3), which includes charting, basic studies, and trading. Higher tiers ($36-$56/month) add real-time market depth data, ACSIL, and advanced order flow tools. Data feeds (CQG, Rithmic, Denali Exchange) are separate subscriptions. Compared to competitors, Sierra Chart is among the most cost-effective professional platforms available.

## Supported Markets

The platform connects to all major [[futures]] exchanges ([[cme|CME]], CBOT, NYMEX, COMEX, ICE, Eurex) via CQG, Rithmic, and Sierra Chart's own Denali Exchange data feed. Equities and [[forex]] data is available through select providers. Crypto support is limited compared to [[bookmap]] or [[quantower]], though some data feed providers offer crypto instruments.

## Trading Relevance

Sierra Chart is referenced in the [[smart-money-orderflow-combo|Smart Money + Order Flow Combo]] strategy as a primary platform for [[footprint-charts]] analysis. Professional futures scalpers on the [[cme|CME]] frequently use Sierra Chart's Numbers Bars to identify [[absorption]], [[delta-divergence]], and imbalance patterns at [[smart-money-concepts|SMC]] zones. Its combination of low latency, precise data handling, and deep customization makes it the platform of choice for traders who treat order flow analysis as their primary edge.

## See Also

- [[bookmap]] — Heatmap-based order flow visualization
- [[jigsaw]] — Reconstructed tape and DOM analysis platform
- [[quantower]] — Multi-asset platform with modern interface
- [[footprint-charts]] — Volume-at-price visualization that Sierra Chart excels at
- [[volume-profile]] — Auction theory tool with strong Sierra Chart implementation
- [[order-flow]] — The broader analytical approach these tools support
