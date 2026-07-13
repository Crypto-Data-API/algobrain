---
title: "NinjaTrader"
type: concept
created: 2026-04-22
updated: 2026-06-12
status: good
tags: [trading-platforms, futures, backtesting, technology]
aliases: ["NinjaTrader 8", "NT8"]
domain: [trading-platforms]
related: ["[[sierra-chart]]", "[[atas-platform]]", "[[order-flow]]", "[[futures]]", "[[backtesting]]", "[[cme-group]]", "[[tradingview]]"]
---

NinjaTrader is a widely used trading platform for [[futures]] and forex markets, offering charting, analysis, strategy development, [[backtesting]], and direct brokerage services. It serves as both a front-end trading platform and, since 2019, a [[futures]] brokerage (NinjaTrader Brokerage).

## Overview

NinjaTrader is popular among retail futures traders for its combination of free charting capabilities, extensive third-party add-on ecosystem, and integrated brokerage. The platform connects to data feeds from Kinetick (NinjaTrader's own data service), CQG, Rithmic, and Interactive Brokers, and routes orders to the [[cme-group|CME]], ICE, EUREX, and other futures exchanges.

The software runs on Windows and has gone through several major versions, with NinjaTrader 8 being the current production release.

## Core Features

### Charting and Analysis

- **Advanced charting** — multiple chart types including candlestick, bar, line, point-and-figure, Renko, and range bars
- **200+ built-in indicators** — including standard [[technical-analysis]] indicators (moving averages, [[rsi]], [[macd]], Bollinger Bands) and volume-based tools
- **Chart Trader** — interactive order entry directly from charts with drag-and-drop stop/target management
- **Market Analyzer** — real-time scanning and filtering across multiple instruments

### Depth of Market (DOM)

NinjaTrader includes a native SuperDOM (Depth of Market) ladder for order book visualization and one-click trading. Features include:

- Real-time bid/ask depth display
- Volume profile overlay on the DOM
- One-click order placement at specific price levels
- Dynamic position and P&L display

### Strategy Development

NinjaTrader provides **NinjaScript**, a C#-based programming language for building custom indicators and automated strategies:

- Full access to price, volume, and order data
- Event-driven architecture for strategy logic
- Integrated strategy [[backtesting]] with historical data
- Strategy optimization with parameter sweeps
- Market replay for walk-forward testing

### Order Flow Add-Ons

While NinjaTrader's native order flow tools are basic compared to [[sierra-chart]], a large third-party ecosystem fills the gap:

- **OrderFlow+** — popular add-on for [[footprint-chart|footprint charts]], [[volume-imbalance|volume imbalance]] detection, and cluster analysis
- **Footprint charts** — available through multiple third-party packages
- **Volumetric bars** — added in later NT8 updates as a native feature
- **Custom DOM columns** — third-party tools for advanced order book analysis

## NinjaTrader Brokerage

Since 2019, NinjaTrader operates as a futures brokerage, offering:

- Competitive commission rates (as low as $0.09/contract on micros)
- Free platform access for brokerage customers
- Margin rates often lower than competitors for day trading
- Direct [[cme-group|CME]], ICE, and EUREX access

This vertical integration (platform + brokerage) distinguishes NinjaTrader from pure software platforms like [[sierra-chart]].

## Pricing Model

- **Free** — charting, analysis, and strategy backtesting (with delayed data)
- **Lease** — monthly/quarterly subscription for live trading features
- **Lifetime** — one-time purchase for permanent live trading access
- **Free with brokerage** — platform access included with NinjaTrader Brokerage accounts

## Related

- [[sierra-chart]] — competing professional futures platform with deeper order flow tools
- [[atas-platform]] — competing platform focused on order flow analysis
- [[futures]] — the primary market NinjaTrader serves
- [[backtesting]] — strategy testing capabilities built into NinjaTrader
- [[order-flow]] — analysis discipline supported via add-ons
- [[cme-group]] — primary exchange for NinjaTrader users
- [[tradingview]] — alternative charting platform (web-based, broader market coverage)

## Sources

*No raw sources ingested yet. This page is based on NinjaTrader's publicly documented features and capabilities.*
