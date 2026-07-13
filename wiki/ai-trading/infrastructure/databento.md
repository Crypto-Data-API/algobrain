---
title: "Databento"
type: source
created: 2026-04-15
updated: 2026-06-12
status: good
tags: [data-provider, technology, market-microstructure, futures, stocks, options]
aliases: ["Databento", "databento.com"]
source_type: data
source_url: "https://databento.com"
confidence: high
related:
  - "[[data-sources-overview]]"
  - "[[paid-data-providers]]"
  - "[[low-latency-trading]]"
  - "[[market-microstructure]]"
  - "[[high-frequency-trading]]"
  - "[[fix-protocol]]"
  - "[[backtesting]]"
---

Databento is a modern market-data provider that delivers normalized historical and real-time data — including full order-book depth (MBO/L3) — across US equities, futures, and options through a single API and unified schema. It targets quant developers and systematic traders who previously had to license raw exchange feeds or stitch together multiple vendors, and it is notable for usage-based pricing that lets a researcher pull only the data they need rather than committing to large annual contracts.

## What It Provides

- **Asset coverage**: US equities (all venues including consolidated tape and venue-specific feeds), CME/CBOT/NYMEX/COMEX futures, and US equity/index options. Coverage continues to expand toward additional global venues.
- **Schemas (granularity)**: from top-of-book and OHLCV bars down to **MBP-10** (market-by-price, 10 levels) and **MBO** (market-by-order, full L3 reconstruction) — the kind of microstructure data needed for [[high-frequency-trading]] research, queue-position modeling, and realistic fill simulation.
- **Historical depth**: multi-year history for major venues, delivered as point-in-time, survivorship-bias-aware data with stable instrument identifiers.
- **Real-time / live**: low-latency streaming feeds available via the live gateway, with Databento advertising zero exchange license fees and free redistribution rights on its US Equities Mini feed for active subscriptions.

## Access and Pricing (2026)

- **Usage-based historical pricing** billed from roughly **$0.40/GB** of data retrieved — you pay for what you query rather than a flat annual license.
- **Live data** is sold via subscription plans rather than pay-per-byte.
- **Free credits**: new users receive about **$125 in free credits** usable on historical requests and to trial real-time data.
- **Interfaces**: Python, C++, and Rust client libraries; REST and a streaming binary protocol (DBN — the Databento Binary Encoding). Data normalizes to one schema regardless of venue, which removes most of the parsing/normalization burden of raw exchange feeds.

For institutional flows requiring co-located raw feeds and microsecond determinism, direct exchange connectivity and [[fpga]]-based handlers still win on latency (see [[low-latency-trading]]); Databento's edge is breadth, normalization, and cost transparency for research and mid-latency systematic trading.

## Trading Use-Cases

- **Backtesting with realistic microstructure** — MBO/MBP data lets you simulate queue position, slippage, and partial fills instead of assuming mid-price execution (see [[backtesting]], [[event-driven-backtesting]]).
- **Signal research** on order-flow imbalance, depth, and trade-print features.
- **Execution analytics / TCA** — reconstruct the book at any timestamp to evaluate fills.
- **Live systematic trading** for strategies that need depth but not nanosecond co-location.

## Alternatives

- **Polygon.io / Alpaca / Tiingo** — cheaper, shallower (mostly trades/quotes/bars, not full L3).
- **Raw exchange feeds** (CME MDP 3.0, Nasdaq TotalView-ITCH) — maximum fidelity and lowest latency, but you handle normalization, license fees, and co-location.
- **Refinitiv / Bloomberg** — broader cross-asset and reference data, far higher cost (see [[paid-data-providers]]).
- **kdb+/FlexTrade and in-house tick stores** — for firms that have already built capture infrastructure.

## Related

- [[data-sources-overview]] — catalog of trading data providers
- [[paid-data-providers]] — where Databento sits in the paid landscape
- [[low-latency-trading]] — when Databento is and isn't fast enough
- [[high-frequency-trading]] — primary consumer of MBO/L3 data
- [[market-microstructure]] — the domain Databento's deep schemas serve
- [[backtesting]] — realistic fill simulation from order-book data

## Sources

- Databento product documentation and pricing pages (databento.com/stocks, /live, /equities), accessed via web research June 2026
- Databento startups / free-credits program page
