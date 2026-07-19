---
title: "Volume Profile"
type: concept
created: 2026-04-07
updated: 2026-07-19
status: good
tags: [technical-analysis, indicators, market-microstructure]
aliases: ["Volume at Price", "Market Profile Volume"]
related: ["[[volume-analysis]]", "[[vwap]]", "[[support-and-resistance]]", "[[order-flow]]", "[[market-profile]]", "[[value-area]]"]
domain: [technical-analysis, market-microstructure]
difficulty: intermediate
---

Volume Profile is a charting tool that displays the amount of volume traded at each price level over a specified period, plotted as a horizontal histogram alongside the price chart. Unlike traditional volume bars that show volume per time period, Volume Profile reveals where the most trading activity occurred by price, identifying areas of high acceptance (consensus) and low acceptance (rejection). It is widely used by institutional and professional traders to locate [[support-and-resistance]] levels, gauge fair value, and identify high-probability trade setups.

## Overview

Volume Profile emerged from the Market Profile concept developed by J. Peter Steidlmayer at the Chicago Board of Trade in the 1980s. While Market Profile uses time-price opportunity (TPO) counts, Volume Profile uses actual volume data, making it more directly reflective of capital commitment at each price level.

The tool answers a fundamental question: **at what prices were market participants most willing to transact?** High-volume price levels represent areas where both buyers and sellers found the price acceptable -- areas of consensus and balance. Low-volume levels represent prices where the market moved through quickly -- areas of imbalance and rejection.

Key components:
- **Point of Control (POC)** -- the single price level with the highest traded volume. Represents the "fairest price" where the most agreement between buyers and sellers occurred.
- **Value Area (VA)** -- the range of prices encompassing approximately 70% of total volume (one standard deviation). Defined by the Value Area High (VAH) and Value Area Low (VAL).
- **High Volume Nodes (HVN)** -- price clusters with elevated volume. Act as magnets that attract price and as strong [[support-and-resistance]] levels.
- **Low Volume Nodes (LVN)** -- price clusters with minimal volume. Price tends to move through these areas quickly. They act as barriers between high-volume zones.

## How It Works

### Profile Types

**Session Profile (Daily)**: Volume distribution for a single trading session. Most useful for day traders identifying intraday S/R and fair value.

**Composite/Range Profile**: Volume distribution across multiple sessions or a custom date range. Useful for swing and position traders identifying structural levels that persist across days or weeks.

**Visible Range (VPVR)**: Volume profile calculated for whatever price range is currently visible on the chart. Dynamically adjusts as you zoom in or out.

**Fixed Range**: Profile for a user-selected price range, often applied to specific consolidation zones, bases, or trend legs.

### Reading the Profile

**Bell-Shaped (Balanced) Profile**: Volume is concentrated in the middle with thin tails on both ends. Indicates a balanced, range-bound market. The POC is near the center. Trading strategy: fade the extremes, target the POC.

**P-Shape Profile**: Heavy volume concentration in the upper portion with a thin tail below. Indicates that price rallied from lower levels and found acceptance at higher prices. The thin lower tail represents a strong buying impulse that moved price quickly through those levels.

**b-Shape Profile**: Heavy volume at the lower portion with a thin tail above. Indicates that price dropped from higher levels and found acceptance at lower prices. The upper tail was a selling impulse.

**D-Shape (Elongated) Profile**: Volume spread relatively evenly across a wide range. Indicates a trending day or period where neither buyers nor sellers established control at any single level.

### Volume Nodes as Support/Resistance

- **High Volume Nodes act like magnets**: price tends to gravitate toward and consolidate around HVNs. When price approaches an HVN from outside, expect it to slow, chop, and potentially reverse. HVNs are the strongest volume-based S/R levels.
- **Low Volume Nodes act like barriers**: price moves through LVNs quickly because there is little "memory" of trading at those levels. When price enters an LVN, expect fast, volatile movement until it reaches the next HVN.

This creates a framework: trade zones (HVNs) are separated by transition zones (LVNs). Price oscillates between HVNs, spending most time in them, and shoots through LVNs.

### Value Area Trading

The 70% Value Area provides a probabilistic framework:
- **If price opens within the prior session's Value Area**: expect a range-bound, rotational session. Fade moves toward VAH and VAL, target the POC.
- **If price opens outside the Value Area**: there is approximately a 80% chance that price will rotate back to test the Value Area edge, and a significant probability it will return inside. This is the "80% Rule" -- a high-probability mean-reversion setup.
- **Acceptance above VAH or below VAL**: if price opens outside the VA and moves further away with commitment, it signals a potential trend day. The prior VA edge becomes a reference for retest entries.

## Trading Applications

### Day Trading with Volume Profile
1. Plot the prior day's Volume Profile, noting POC, VAH, and VAL
2. Observe the opening relative to the Value Area
3. If inside the VA: trade rotations between VAH and VAL with POC as the target
4. If outside the VA: watch for rejection back into the VA (80% Rule) or acceptance away from it (trend day)
5. Use LVNs as profit targets (price will move fast through them) and HVNs as trade management zones

### Swing Trading with Composite Profiles
1. Build a composite profile over the last 20-60 sessions
2. Identify the major POC and HVNs -- these are the structural S/R levels
3. Look for price approaching an HVN for potential support/resistance plays
4. Look for price breaking through an LVN for breakout entries with targets at the next HVN

### Combining with Other Tools
Volume Profile is most powerful when combined with:
- [[vwap]] -- dynamic intraday fair value to complement the structural POC
- [[order-flow]] -- granular trade-by-trade data within the profile structure
- [[support-and-resistance]] -- traditional S/R levels that coincide with HVNs are particularly strong
- [[candlestick-patterns]] -- price action at HVN levels provides entry timing

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1h&limit=1000` — fine-grained OHLCV bars to bin volume into price buckets
- `GET /api/v1/hyperliquid/l2-book?coin=BTC` — current resting-order depth by price (complements the traded-volume profile with live order-book structure)

**Historical data:**
- `GET /api/v1/backtesting/klines` — deep kline archive for composite profiles over long ranges

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=1h&limit=1000"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-data]].

**Live dashboards:** [order-book depth](https://cryptodataapi.com/quant-order-books)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can work with this indicator directly:

- **Compute** — approximate volume-at-price by bucketing each kline's volume across its high-low range (or assigning it to the bar midpoint): fine intervals from `GET /api/v1/market-data/klines` yield POC, VAH/VAL, and HVN/LVN estimates without tick data
- **Resolution** — 1m klines exist in `GET /api/v1/backtesting/klines` only since 2026-03-30; profiles for earlier periods must build from 1h bars, which coarsens node boundaries
- **Backtest** — replay Value-Area rotation and LVN-breakout rules against the same archive (Binance spot 1h/4h/1d back to 2017-08), rebuilding the prior session's profile per test day
- **Tip** — cross-check a klines-built HVN against `GET /api/v1/hyperliquid/l2-book` depth: a historical high-volume node reinforced by current resting liquidity is a materially stronger level than either signal alone

## Related

- [[volume-analysis]] -- broader framework for interpreting volume
- [[vwap]] -- dynamic fair value benchmark
- [[support-and-resistance]] -- traditional S/R levels
- [[order-flow]] -- granular transaction-level analysis
- [[market-profile]] -- related time-based distribution concept

## Sources

- [[book-technical-analysis-of-the-financial-markets]] -- context for volume-based analysis in technical trading
