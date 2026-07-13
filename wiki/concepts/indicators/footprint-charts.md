---
title: "Footprint Charts"
type: concept
created: 2026-04-10
updated: 2026-06-11
status: good
tags: [market-microstructure, indicators, liquidity, technical-analysis]
aliases: ["Footprint Charts", "Footprint Chart", "Bid-Ask Chart", "Cluster Chart"]
domain: [market-microstructure, indicators]
difficulty: advanced
prerequisites: ["[[order-flow]]", "[[volume-profile]]"]
related: ["[[order-flow]]", "[[delta]]", "[[volume-profile]]", "[[absorption]]", "[[delta-divergence]]", "[[bookmap]]", "[[sierra-chart]]", "[[support-and-resistance]]", "[[order-blocks]]"]
---

**Footprint charts** (also called bid-ask charts or cluster charts) display the volume traded at each price level within each candle, broken down by trades executed at the bid versus trades executed at the ask. They provide a granular, inside-the-candle view of [[order-flow]] that standard candlestick charts cannot reveal, showing not just where price went but how buyers and sellers behaved at every tick along the way.

## Overview

A standard candlestick shows four data points: open, high, low, close. A footprint chart shows those same four points plus the complete volume distribution within the candle -- how many contracts or shares traded at each price, and whether those trades were initiated by aggressive buyers (hitting the ask) or aggressive sellers (hitting the bid). This transforms a single candle from a summary into a detailed narrative of the battle between buyers and sellers.

Footprint charts are used primarily in [[futures]] markets (ES, NQ, CL, GC) where centralized exchange data provides accurate trade-level information. They are also available for major [[forex]] pairs (via futures proxies) and some [[crypto]] exchanges, though fragmented crypto [[liquidity]] across venues makes the data less complete.

## Types of Footprint Charts

### Bid x Ask Footprint

The most common format. Each price level within the candle shows two numbers side by side: volume traded at the bid (left, typically red) and volume traded at the ask (right, typically green). This format makes it easy to spot imbalances -- where one side overwhelms the other at a specific price.

### Delta Footprint

Shows the net difference (ask volume minus bid volume) at each price level. Positive values (net buying) are green; negative values (net selling) are red. This is a more compact view that highlights which side was dominant at each price without showing the raw numbers.

### Volume Footprint

Shows total volume at each price level without the bid/ask breakdown. Less informative than the bid x ask format but useful for identifying high-activity levels that may act as [[support-and-resistance]]. Essentially a per-candle [[volume-profile]].

## Key Patterns

### Imbalances

An imbalance occurs when the ratio of ask volume to bid volume (or vice versa) at a single price level exceeds a threshold, typically 3:1 or higher. For example, if 500 contracts traded at the ask and only 100 at the bid at a particular price, that is a 5:1 buy imbalance. Imbalances reveal where one side overwhelmed the other and are often highlighted automatically by the charting software.

### Stacked Imbalances

Three or more consecutive price levels showing imbalances in the same direction. A column of stacked buy imbalances indicates strong, sustained aggressive buying across a price range -- institutional urgency. Stacked sell imbalances indicate the opposite. These often mark the origin of strong moves and can later function as [[order-blocks]] when price returns.

### Diagonal Imbalances

Imbalances that appear along the diagonal of the footprint (ask imbalance at one price matched with bid imbalance at the price below, creating a stepping pattern). These indicate aggressive momentum -- buyers lifting offers at progressively higher prices. Diagonal imbalances during [[high-volume-sessions]] are a sign of genuine directional conviction.

### Absorption Patterns

High volume at a single price level with minimal price displacement. The footprint shows large numbers on both bid and ask sides at the same price, but the candle body is small. This indicates [[absorption]] -- a large passive participant absorbing aggressive flow. See [[absorption]] for a detailed treatment.

### Exhaustion Prints

The footprint shows declining volume at the extreme of a move. For example, in a rally, the top few price ticks show progressively lower ask volume, suggesting buyers are losing conviction. When combined with [[delta-divergence]], exhaustion prints provide high-probability reversal signals.

## Platforms and Tools

Several platforms offer footprint chart functionality:

- **[[sierra-chart|Sierra Chart]]**: The most configurable and cost-effective option for footprint analysis. Popular among professional futures traders. Supports all footprint types with extensive customization.
- **[[quantower|Quantower]]**: Modern platform with clean footprint visualization. Supports futures, crypto, and forex. Competitive pricing.
- **[[bookmap|Bookmap]]**: Primarily a heatmap/depth visualization tool but includes footprint-style volume displays. Excels at showing order book depth alongside executed flow.
- **ATAS (Order Flow Trading)**: Dedicated order flow platform with advanced footprint features and pattern detection.
- **Exocharts**: Crypto-focused footprint tool with exchange-aggregated data.

Costs typically range from $50-200/month depending on the platform and data feed. Real-time exchange data fees (especially [[cme]] data) are an additional cost.

## Related

- [[order-flow]] -- footprint charts are the primary visualization of order flow
- [[delta]] -- footprint charts display delta at each price level
- [[volume-profile]] -- related concept showing volume distribution across a session or range
- [[delta-divergence]] -- a key signal read from footprint data
- [[absorption]] -- a pattern identified using footprint charts
- [[smart-money-orderflow-combo]] -- the strategy framework that relies on footprint chart confirmation

## Sources

- Jones, M. (2018). *Order Flow: Trading Setups* — practitioner reference on footprint imbalances, stacked imbalances, and absorption reading
- Sierra Chart documentation — *Numbers Bars (Footprint)* study reference, covering bid/ask, delta, and volume footprint configurations and imbalance highlighting
- CME Group educational materials on order-flow and volume-at-price analysis in futures markets
- *General order-flow trading knowledge*; to be supplemented as raw source material is ingested.
