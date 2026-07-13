---
title: "ATAS Platform"
type: concept
created: 2026-04-22
updated: 2026-06-12
status: good
tags: [trading-platforms, order-flow, market-microstructure]
aliases: ["ATAS", "Advanced Time And Sales", "ATAS OrderFlow Trading"]
domain: [market-microstructure, trading-platforms]
related: ["[[order-flow]]", "[[footprint-chart]]", "[[volume-profile]]", "[[absorption]]", "[[volume-imbalance]]", "[[sierra-chart]]", "[[ninjatrader]]", "[[cme-group]]"]
---

ATAS (Advanced Time And Sales) is a trading and analysis platform specializing in [[order-flow]] visualization, particularly [[footprint-chart|footprint/cluster charts]]. ATAS pioneered accessible cluster chart analysis for non-institutional traders and remains one of the most focused order flow platforms available.

## Overview

ATAS was designed from the ground up for [[order-flow]] analysis, unlike platforms such as [[ninjatrader|NinjaTrader]] or TradingView that added order flow features to existing charting platforms. This focus makes it the preferred tool for traders whose primary methodology revolves around reading volume at price, detecting [[absorption]], identifying [[volume-imbalance|volume imbalances]], and analyzing the time and sales tape.

The platform connects to [[futures]] exchanges (via CQG, Rithmic, and other data providers), [[crypto]] exchanges (Binance, Bybit, OKX), and equity markets. This cross-asset connectivity is useful for traders who apply order flow methodology across multiple markets.

## Core Features

### Cluster Charts (Footprint)

ATAS's signature feature is its cluster chart implementation, which displays detailed volume information at every price level within each bar:

- **Bid/Ask volume** — shows exactly how many contracts traded at the bid vs. ask at each tick
- **Delta visualization** — color-coded display of net buying vs. selling aggression
- **[[volume-imbalance|Imbalance]] detection** — automatic highlighting of diagonal imbalances (where buy-to-sell or sell-to-buy ratios exceed configurable thresholds like 3:1)
- **Cumulative delta** — running total of aggressive buying minus aggressive selling
- **Multiple cluster modes** — volume, delta, bid x ask, trades count, time-based clusters

### Smart Tape

The Smart Tape feature filters and categorizes time-and-sales data to highlight significant transactions:

- Large trade detection (configurable thresholds)
- Iceberg order detection (repeated fills at the same price suggesting hidden liquidity)
- Trade clustering (grouping rapid fills that likely represent a single institutional order)
- Color-coded tape by trade size and aggression

### DOM Analysis

- Real-time depth of market display with historical volume overlay
- Order pulling/spoofing detection (orders that appear and disappear rapidly)
- Cumulative depth visualization showing total resting liquidity at each price level

### Volume Analysis Tools

- **[[volume-profile]]** — session, composite, and custom profiles with value area and POC
- **Volume histogram** — horizontal volume display alongside price charts
- **[[absorption]] indicators** — built-in tools to detect passive orders absorbing aggressive flow
- **Unfinished auction** detection — identifying price levels where the auction process did not complete (potential revisit targets)

## Crypto Integration

ATAS was among the first professional order flow platforms to offer direct [[crypto]] exchange connectivity:

- Real-time cluster charts for Bitcoin, Ethereum, and altcoin perpetual futures
- Funding rate and open interest overlays
- Cross-exchange comparison (useful for detecting exchange-specific [[liquidity]] dynamics)

## Comparison with Alternatives

| Feature | ATAS | [[sierra-chart\|Sierra Chart]] | [[ninjatrader\|NinjaTrader]] |
|---|---|---|---|
| Cluster/footprint charts | Native, primary focus | Advanced (Numbers Bars) | Via add-ons |
| Crypto exchange support | Native (multiple exchanges) | Limited | None |
| Custom programming | Limited scripting | C/C++ (ACSIL) | C# (NinjaScript) |
| Smart tape | Native | Basic | Via add-ons |
| Learning curve | Moderate | Steep | Moderate |
| Pricing | Subscription | Subscription | Free/Lease/Lifetime |

## Related

- [[order-flow]] — the analytical methodology ATAS is designed for
- [[footprint-chart]] — ATAS's primary visualization tool
- [[volume-imbalance]] — key signal visible on ATAS cluster charts
- [[absorption]] — order flow pattern ATAS can detect
- [[volume-profile]] — auction-based analysis tool native to ATAS
- [[sierra-chart]] — competing professional order flow platform
- [[ninjatrader]] — competing futures trading platform
- [[cme-group]] — primary futures exchange for ATAS users

## Sources

*No raw sources ingested yet. This page is based on ATAS platform's publicly documented features and capabilities.*
