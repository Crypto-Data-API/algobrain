---
title: "Iceberg Orders"
type: concept
created: 2026-04-10
updated: 2026-06-11
status: good
tags: [market-microstructure, order-types, liquidity, slippage]
aliases: ["iceberg order", "Iceberg Orders", "iceberg-detection", "hidden order", "reserve order"]
domain: [market-microstructure]
prerequisites: ["[[order-book]]", "[[order-types]]"]
difficulty: advanced
related: ["[[order-flow]]", "[[order-book]]", "[[absorption]]", "[[market-maker]]", "[[footprint-charts]]", "[[order-blocks]]", "[[market-impact]]"]
---

**Iceberg orders** (also called hidden orders or reserve orders) are large orders that are split into smaller visible portions, called "clips," to conceal the true order size from the market. Only a fraction of the total order is displayed on the [[order-book]] at any time; as each visible clip is filled, the next one automatically appears. They are a primary tool for institutional execution and one of the key signals in [[order-flow]] analysis.

## Overview

Institutional traders routinely need to buy or sell thousands of contracts or hundreds of thousands of shares. Displaying the full size on the order book would cause other participants to front-run the order -- buying ahead of a large buy order to sell back at a higher price, or selling ahead of a large sell order. This market impact problem (see [[market-impact]]) is the fundamental reason iceberg orders exist.

An iceberg order works by dividing a large parent order (e.g., 5,000 contracts) into small displayed clips (e.g., 50 contracts). The exchange or the trader's execution algorithm shows only 50 contracts on the book. When those 50 fill, the next 50 appear at the same price. This continues until the entire 5,000-contract order is filled. To casual observers watching the [[order-book]], it looks like a series of small, unrelated orders -- not a single massive position being built.

## How Exchanges Handle Icebergs

Most major exchanges ([[cme]], NYSE, NASDAQ, and major [[crypto]] exchanges like Binance) offer native iceberg order types. The trader specifies:

- **Total quantity**: The full order size (hidden from the market)
- **Display quantity**: The visible clip size shown on the book
- **Price**: The limit price for all clips
- **Variance** (optional): Some platforms allow randomizing the clip size (e.g., between 40-60 contracts instead of exactly 50) to make detection harder

Exchange-native icebergs have a disadvantage: they lose time priority after each clip fills. The new clip enters the queue behind other orders at the same price. Sophisticated firms use their own algorithms to manage clip timing and sizing, sometimes varying the price slightly between clips to avoid detection.

## How Order Flow Tools Detect Icebergs

Despite the intent to hide, iceberg orders leave telltale footprints that modern order flow tools can identify:

1. **Repeated fills at the same price**: The most basic detection method. If the same bid or ask price is hit 20, 50, or 100 times with similar-sized fills, it strongly suggests an iceberg. Normal limit orders fill once and are gone.
2. **Replenishing depth**: On a depth-of-market (DOM) display or bookmap heatmap, you can see a level that keeps "refilling" after being consumed. The resting quantity at a price drops to zero, then immediately reappears.
3. **Volume vs. visible size mismatch**: A price level shows only 50 contracts on the book, but 2,000 contracts trade there in a short time. The volume far exceeds what was ever visible. [[footprint-charts]] make this mismatch obvious.
4. **Algorithmic detection**: Tools like Jigsaw Trading and Bookmap have built-in iceberg detection algorithms that flag suspected hidden orders in real time. They analyze fill patterns, timing between replenishments, and clip sizes to assign confidence scores.

## Trading Significance

Iceberg detection is valuable because it reveals where institutions are placing large orders that they do not want the market to see. These levels often act as strong [[support-and-resistance]] because the institution will continue to defend the price until their full order is filled.

When an iceberg is detected at a level that aligns with a higher-timeframe [[order-blocks|order block]] or [[fair-value-gaps|fair value gap]], it provides strong confirmation that the level is institutionally defended. In the [[smart-money-orderflow-combo]] framework, iceberg activity at an SMC zone is a high-conviction entry signal -- it means the structural analysis and the real-time flow data agree.

However, iceberg detection is not infallible. Sophisticated algorithms vary clip sizes, timing, and even price levels to evade detection. Not every cluster of fills at the same price is an iceberg -- it could be multiple independent traders with similar ideas. Context matters: icebergs are most significant when they appear at structurally important levels during [[high-volume-sessions]].

## Related

- [[order-flow]] -- icebergs are a key component of order flow analysis
- [[order-book]] -- icebergs manipulate what the order book displays
- [[absorption]] -- iceberg orders are the mechanism behind many absorption patterns
- [[market-maker]] -- market makers use icebergs routinely for inventory management
- [[market-impact]] -- icebergs exist to minimize market impact of large orders
- [[footprint-charts]] -- the primary tool for spotting volume-vs-visible-size mismatches

## Sources

*No raw sources ingested yet. This page is based on general market microstructure knowledge and will be updated as source material is added.*
