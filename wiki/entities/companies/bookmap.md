---
title: "Bookmap"
type: entity
created: 2026-04-10
updated: 2026-06-10
status: good
tags: [order-flow, trading-tools, market-microstructure, data-provider]
entity_type: company
website: "https://bookmap.com"
aliases: ["Bookmap"]
related: ["[[order-flow]]", "[[order-book]]", "[[footprint-charts]]", "[[iceberg-orders]]", "[[sierra-chart]]", "[[jigsaw]]"]
---

# Bookmap

**Bookmap** is an advanced order flow visualization platform that renders real-time and historical [[order-book]] data as a continuous heatmap. Unlike traditional [[depth-of-market]] (DOM) ladders that show a static snapshot, Bookmap plots limit order density over time, making it possible to see where large orders are placed, pulled, or absorbed as price moves through them. The platform is widely used by professional [[futures]] scalpers, crypto day traders, and institutional desks that rely on [[order-flow]] analysis for execution timing.

## Key Features

### Heatmap Visualization

Bookmap's signature feature is the liquidity heatmap — a color-coded display of resting limit orders across all price levels over time. Dense liquidity appears as bright bands (typically yellow/orange/red), while thin areas appear dark. This visual approach reveals patterns invisible on a standard DOM: spoofing behavior, large walls being built and pulled, and genuine institutional resting orders that hold firm as price approaches.

### Volume Dots and Trades

Every executed trade is plotted as a circle on the heatmap, sized proportionally to the trade volume. This makes it immediately obvious when large aggressive orders hit the book — a cluster of large dots at a specific price level signals institutional activity. Traders use these volume dots to confirm [[absorption]] patterns and identify [[iceberg-orders]] being filled in clips.

### Iceberg Detection

Bookmap includes built-in [[iceberg-detection]] algorithms that flag hidden orders. When repeated fills occur at the same price level beyond the visible resting quantity, the platform highlights these as probable icebergs. This is critical for [[smart-money-concepts]] traders who need to confirm that institutional participants are genuinely defending a level, not just placing and canceling orders.

### Multibook and Correlation

The Multibook feature aggregates order book data across multiple exchanges (particularly useful in [[crypto]] markets where liquidity is fragmented across [[binance]], [[coinbase]], and other venues). This composite view shows true market depth rather than single-exchange depth, reducing the risk of being misled by exchange-specific spoofing.

## Supported Markets

Bookmap connects to major [[futures]] exchanges including the [[cme|CME]], ICE, and Eurex via supported data feeds (CQG, Rithmic, dxFeed). For [[crypto]], it supports [[binance]], Coinbase, Bybit, OKX, and other major exchanges with direct API connections. Equities coverage is available through select data providers, though the platform is primarily used for futures and crypto.

## Pricing

Bookmap operates on a subscription model with tiered pricing. A free Digital tier provides delayed data and basic heatmap functionality. The Global tier ($39/month as of early 2026) adds real-time data, volume dots, and basic indicators. The Global Plus tier ($69/month) includes advanced features like iceberg detection and Multibook. Crypto-specific plans are also available.

## Trading Relevance

Bookmap is a core tool in the [[smart-money-concepts]] + [[order-flow]] combination strategy described in [[smart-money-orderflow-combo|Smart Money + Order Flow Combo]]. Traders use it to visually confirm institutional activity at [[order-blocks]], [[fair-value-gaps]], and other SMC zones. The heatmap reveals whether large passive orders are genuinely absorbing aggressive flow at a level, providing the real-time evidence that separates high-probability entries from hopeful limit orders.

## Company Status

Bookmap is a **private company** (no ticker; traders get no equity exposure — it is a tool vendor, not a tradable name). The platform originated from the proprietary visualization tools of trading firm VeloxPro and was commercialized as a retail/professional product in the mid-2010s. As of June 2026 it remains independently operated on a subscription model, with an active education arm (Bookmap blog, webinars, "Bookmap University") used heavily in order-flow trading communities.

## See Also

- [[jigsaw]] — Alternative order flow platform focused on reconstructed tape
- [[sierra-chart]] — Professional charting platform with footprint chart capabilities
- [[quantower]] — Multi-asset platform with order flow and DOM tools
- [[order-flow]] — The broader concept of analyzing transaction data
- [[footprint-charts]] — Volume-at-price visualization used alongside heatmaps
- [[iceberg-orders]] — Hidden orders that Bookmap is designed to detect

## Sources

- https://bookmap.com — official site (features, pricing tiers, supported connections)
- https://bookmap.com/blog — platform documentation and education hub
