---
title: "Dukascopy"
type: entity
created: 2026-06-13
updated: 2026-06-13
status: good
tags: [forex, data-provider, backtesting]
entity_type: company
founded: 2004
headquarters: "Geneva, Switzerland"
website: "https://www.dukascopy.com"
aliases: ["Dukascopy", "Dukascopy Bank", "JForex"]
related: ["[[forex]]", "[[alpha-vantage]]", "[[backtesting-py]]", "[[transaction-cost-modeling]]", "[[ai-data-providers-overview]]"]
---

# Dukascopy

Dukascopy Bank SA is a Swiss bank and [[forex]]/CFD broker headquartered in Geneva. To most traders its biggest draw is not the brokerage but the data: Dukascopy publishes free, high-quality tick-level historical FX data through its Historical Data Export tool and the JForex platform, making it one of the most accessible sources of granular currency price history.

## Overview

Dukascopy is a regulated Swiss bank that operates as an ECN-style [[forex]] and CFD broker. Its flagship trading environment is the **JForex** platform, a Java-based desktop and API client widely used for automated trading and historical research. Order flow is routed through the **SWFX Swiss FX Marketplace**, Dukascopy's own ECN that aggregates liquidity from banks and other participants and quotes streaming bid/ask prices. Because Dukascopy is both a bank and a data publisher, it can expose its internal price feed to clients and the public in a way that most retail brokers do not.

## Historical Data Export

The standout feature for traders is free historical price data at very fine granularity:

- **Resolution**: from raw **tick** data up to aggregated bars (minute, hourly, daily, weekly, monthly).
- **Instruments**: FX majors, minors, and exotic crosses, plus commodities and indices offered as CFDs.
- **Both sides of the book**: separate **bid** and **ask** series, which makes spread reconstruction possible.
- **Format**: downloadable **CSV** (and other formats via JForex).

Two main access paths:

1. **Historical Data Feed** web tool — a browser-based exporter on the Dukascopy site; pick instrument, date range, and resolution, then download.
2. **JForex** — open *Tools → Historical Data Manager* inside the platform to pull and cache historical data locally, or access it programmatically through the JForex API.

## Why the Data Matters

Tick-level bid/ask data is what separates a realistic backtest from an optimistic one. With both sides of the spread captured at every tick, you can reconstruct the actual cost of crossing the market at any moment, enabling spread-aware backtests and proper [[transaction-cost-modeling]] instead of assuming a fixed or zero spread. Coverage spans majors, minors, and exotic crosses, and some pairs carry multi-decade depth, which supports longer-horizon and regime studies. This contrasts with API-first providers like [[alpha-vantage]], which are convenient for OHLCV pulls but do not offer the same tick-level bid/ask detail for FX.

## Caveats

- **Broker-specific feed**: this is Dukascopy's own price stream, not a consolidated tape. Quotes reflect SWFX liquidity and may differ from other venues.
- **Preprocessing required**: raw tick exports are large and need cleaning, timezone alignment, and aggregation before use.
- **Gaps and quirks**: feed-specific gaps, weekend handling, and occasional anomalies can appear and should be screened for.
- **Survivorship and feed considerations**: instrument availability changes over time, and a single broker's feed carries its own biases.

Treat the data as a strong primary source but **validate it** before relying on it for live decisions.

## Using It for Backtesting

Dukascopy data pairs well with Python backtesting frameworks such as [[backtesting-py]]. A typical workflow:

1. **Export** the desired instrument and date range to CSV via the Historical Data Feed or JForex.
2. **Clean and align** — parse timestamps, normalize timezones, handle gaps, and resample to the target bar size if not trading on ticks.
3. **Feed the backtester** with the cleaned series, applying realistic spread/commission costs derived from the bid/ask data so results reflect true execution costs.

## Relevance to Traders

- Strategy development and prototyping on real FX price action.
- Cost-aware [[backtesting]] using genuine bid/ask spreads.
- Correlation and [[volatility]] studies across currency pairs.
- Seasonal and intraday pattern analysis where tick resolution matters.

## Related

- [[forex]]
- [[alpha-vantage]]
- [[backtesting-py]]
- [[transaction-cost-modeling]]
- [[ai-data-providers-overview]]

## Sources

Compiled from Dukascopy public documentation (Source: gap-analysis research, raw/articles/2026-04-22-gap-finder-injest-forex-trading-strategies.md). Historical Data: https://www.dukascopy.com/swiss/english/marketwatch/historical/
