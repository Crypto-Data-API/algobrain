---
title: "Exocharts"
type: entity
created: 2026-06-19
updated: 2026-06-19
status: draft
tags: [order-flow, trading-tools, market-microstructure, data-provider, crypto, futures]
entity_type: company
website: "https://exocharts.com"
aliases: ["Exocharts", "Exo Charts", "ExoCharts"]
related: ["[[order-flow]]", "[[footprint-chart]]", "[[sierra-chart]]", "[[volume-profile]]", "[[market-profile]]", "[[value-area]]", "[[point-of-control]]"]
---

**Exocharts** is an order-flow and volume-analysis charting platform that combines [[footprint-chart|footprint (cluster) charts]], depth-of-market (DOM), [[volume-profile|volume profiles]], [[composite-profile|composite profiles]], and [[market-profile|TPO (time-price opportunity)]] tooling in a single workflow. It is widely used in the futures and crypto-derivatives communities by traders who want to cross-compare volume and TPO distributions alongside [[order-flow]] detail (Source: [[2026-04-22-gap-finder-volume-profile-indicator-as-a-trading-st]]).

## Overview

Exocharts occupies the same niche as [[sierra-chart|Sierra Chart]], Bookmap, and Quantower — specialised, order-flow-centric platforms rather than generic charting tools. Its distinguishing characteristic is the tight integration of three analytic lenses on one chart (Source: [[2026-04-22-gap-finder-volume-profile-indicator-as-a-trading-st]]):

1. **Volume profiles** — horizontal volume-by-price histograms showing the [[point-of-control|POC]], [[value-area]], and high/low-volume nodes, with both session and composite modes.
2. **Footprint / cluster charts** — intra-bar breakdowns of volume, delta, and trades at each price level (see [[footprint-chart]]).
3. **TPO / market profile** — the time-based distribution that complements the volume view (see [[market-profile]]).

Because a trader can overlay or toggle between these on the same instrument, Exocharts is positioned as a tool for reconciling *where* volume transacted (volume profile), *how* it transacted inside each bar (footprint), and *over how much time* (TPO).

## Markets and Use

Exocharts has become a go-to platform in the **crypto derivatives** community, where it provides order-flow views on perpetual-futures venues, and it is also used by **futures** traders for CME-style instruments (Source: [[2026-04-22-gap-finder-volume-profile-indicator-as-a-trading-st]]). Its documentation frames volume profiles in the standard auction-market language: profiles reveal which prices the market is willing to **accept** and which it **rejects**, helping traders anticipate behaviour when price revisits those ranges.

This makes Exocharts a natural bridge between volume-profile theory and the crypto-perps context, where much of the speculative volume now lives and where order-flow analytics (footprints, DOM, cumulative volume delta) are increasingly accessible to retail traders.

## Comparison to Peers

| Platform | Emphasis | Typical user |
|----------|----------|--------------|
| **Exocharts** | Footprint + volume profile + TPO + DOM, crypto & futures | Crypto-derivatives and futures order-flow traders |
| bookmap | Order-book heatmap + liquidity + CVD | Scalpers reading resting liquidity |
| [[sierra-chart]] | Low-latency execution + Volume by Price study | Professional futures traders |
| quantower | Multi-asset charting + cluster charts + volume-analysis toolbar | Multi-asset discretionary traders |

## Related

- [[order-flow]] — the analytic discipline Exocharts serves
- [[footprint-chart]] — Exocharts' cluster-chart view
- [[volume-profile]] / [[composite-profile]] — the profile tooling it provides
- [[market-profile]] — its TPO view
- [[sierra-chart]], quantower, bookmap — peer order-flow platforms
- [[value-area]] / [[point-of-control]] — profile features it renders

## Sources

- [[2026-04-22-gap-finder-volume-profile-indicator-as-a-trading-st]] — gap-finder Perplexity deep research (2026-06-19)
- Reference video: https://www.youtube.com/watch?v=YmygDgtoxO8
- General market knowledge
