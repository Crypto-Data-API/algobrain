---
title: "Fibonacci Retracement"
type: concept
created: 2026-04-07
updated: 2026-07-19
status: good
tags: [technical-analysis, indicators]
aliases: ["Fibonacci Levels", "Fib Retracement", "Fibonacci", "Fibonacci Retracements", "Fib Retracements", "Fib Levels"]
related: ["[[support-and-resistance]]", "[[chart-patterns]]", "[[trend-following]]", "[[elliott-wave]]", "[[harmonic-patterns]]", "[[fibonacci-trading]]"]
domain: [technical-analysis]
difficulty: intermediate
---

Fibonacci retracement is a [[technical-analysis]] tool that identifies potential [[support-and-resistance]] levels by drawing horizontal lines at key Fibonacci ratios -- 23.6%, 38.2%, 50%, 61.8%, and 78.6% -- between a swing high and swing low. The premise is that after a significant price move, the market tends to retrace a predictable portion of that move before continuing in the original direction. The 61.8% level (the "golden ratio") is considered the most significant.

## Overview

The Fibonacci sequence (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...) produces ratios that appear throughout nature, architecture, and -- proponents argue -- financial markets. The key ratios used in trading are derived from relationships between numbers in the sequence:

- **61.8%** -- any number divided by the next number converges to 0.618 (the golden ratio, phi). The most important Fibonacci level.
- **38.2%** -- any number divided by the number two places ahead (e.g., 34/89). The second most important level.
- **23.6%** -- any number divided by the number three places ahead (e.g., 21/89). Indicates shallow retracement in strong trends.
- **50%** -- not a true Fibonacci ratio but included due to Dow Theory and the observed tendency of markets to retrace half a move.
- **78.6%** -- the square root of 0.618. A deep retracement level; if price reaches this level, the original move is significantly eroded.

Fibonacci retracement is used across all markets -- stocks, [[forex]], [[crypto]], [[commodities]], [[futures]] -- and all timeframes. Its widespread adoption by traders contributes to its effectiveness as a self-fulfilling prophecy: because many traders place orders at Fibonacci levels, price often does react at these levels.

## How It Works

### Drawing Fibonacci Retracements

1. Identify a significant completed swing -- a clear move from a swing low to a swing high (for uptrends) or swing high to swing low (for downtrends)
2. Apply the Fibonacci tool from the start of the swing to the end
3. The tool automatically plots horizontal lines at the key ratios
4. These levels represent potential support (in uptrend pullbacks) or resistance (in downtrend rallies)

**In an uptrend**: draw from swing low to swing high. The Fibonacci levels below the current price act as potential support during a pullback. The 38.2% and 61.8% levels are the most watched.

**In a downtrend**: draw from swing high to swing low. The Fibonacci levels above the current price act as potential resistance during a bounce.

### Interpreting the Levels

| Retracement Level | Interpretation |
|-------------------|---------------|
| 23.6% | Shallow pullback. Strong trend likely to resume quickly. Common in momentum-driven moves. |
| 38.2% | Moderate pullback. Trend is healthy. Popular entry level for aggressive traders. |
| 50.0% | Half-retracement. Significant psychological level. Often coincides with other S/R. |
| 61.8% | Deep pullback at the golden ratio. The "last line of defense" for trend continuation. Most significant Fibonacci level. |
| 78.6% | Very deep retracement. If price reaches here, the original trend is questionable. Sometimes the final support before a full reversal. |

### Confluence with Other Tools

Fibonacci retracements are most effective when they align with other technical evidence:

- **Fibonacci level at a prior [[support-and-resistance]] level** -- doubles the significance
- **Fibonacci level aligning with a [[moving-averages|moving average]]** (e.g., the 61.8% retracement coincides with the 200-SMA) -- strong confluence
- **Fibonacci level at a trendline** -- triple confluence
- **Fibonacci level with a [[candlestick-patterns|candlestick rejection pattern]]** -- provides entry timing

Traders who use Fibonacci without confluence tend to find it unreliable. The tool works best as a filter layered on top of other analysis.

### Fibonacci Extensions

Beyond retracement, Fibonacci ratios are used for **price extensions** (projecting targets beyond the original move):
- **100%** -- the move equals the original swing in length
- **127.2%** -- common extension target
- **161.8%** -- the most important extension level (inverse of 61.8%)
- **200%** -- double the original move
- **261.8%** -- extended target for powerful trends

Extensions help set profit targets when trading breakouts from [[chart-patterns]] or continuation setups.

## Trading Applications

### Pullback Entry Strategy
1. Identify a strong trending move (a clear impulse leg)
2. Draw Fibonacci retracement from swing low to swing high (uptrend)
3. Wait for price to pull back to the 38.2% or 61.8% level
4. Look for confirming price action (bullish [[candlestick-patterns|candlestick pattern]], [[volume-analysis|volume]] increase)
5. Enter long with a stop below the next Fibonacci level (e.g., enter at 38.2%, stop below 50%)
6. Target the prior swing high, then Fibonacci extension levels (127.2%, 161.8%)

### Fibonacci Clusters
When multiple Fibonacci retracements from different swings converge at the same price zone, it creates a "Fibonacci cluster" -- a highly significant support or resistance area. Drawing retracements from multiple timeframes and swing points can identify these clusters.

### Connection to Elliott Wave
[[elliott-wave]] theory incorporates Fibonacci ratios extensively:
- Wave 2 typically retraces 50-61.8% of Wave 1
- Wave 3 often extends to 161.8% of Wave 1
- Wave 4 typically retraces 38.2% of Wave 3
- Wave 5 often equals Wave 1 or extends to 61.8% of Waves 1-3

### Connection to Harmonic Patterns
[[harmonic-patterns]] (Gartley, Butterfly, Bat, Crab) are defined entirely by specific Fibonacci ratios between their legs. These patterns formalize the idea that market swings relate to each other through Fibonacci proportions.

### Limitations
- **Subjectivity in swing selection** -- different traders may identify different swing highs and lows, producing different Fibonacci levels. This is the tool's greatest weakness.
- **No predictive power in isolation** -- Fibonacci levels are best used as a framework for identifying zones, not as precise predictive levels
- **Self-fulfilling prophecy** -- some of the tool's effectiveness comes from widespread use rather than mathematical inevitability
- **Cherry-picking** -- with five retracement levels, price will often react at one of them by chance, creating an illusion of reliability. Always require confluence.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=BTCUSDT` — current price versus retracement levels

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=500` — OHLCV for swing detection and level placement
- `GET /api/v1/backtesting/klines` — deep kline archive

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=500"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-data]].

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can work with this tool directly:

- **Compute** — detect the impulse swing (low to high) in `GET /api/v1/market-data/klines` output and lay the 23.6/38.2/50/61.8/78.6% levels across it
- **Confluence** — cross-reference each level against moving averages computed from the same series and prior S/R pivots; only confluence-backed levels earn entries, per this page's guidance
- **Backtest** — `GET /api/v1/backtesting/klines` (Binance spot 1h/4h/1d back to 2017-08) supports bounce-rate studies per level — control against random levels, since five lines will catch *something* by chance
- **Tip** — codify swing selection (pivot lookback, minimum swing %) so backtest and live agree; subjective swing choice is the tool's greatest weakness

## Related

- [[support-and-resistance]] -- the broader concept that Fibonacci levels represent
- [[elliott-wave]] -- wave theory that uses Fibonacci ratios extensively
- [[harmonic-patterns]] -- chart patterns defined by Fibonacci relationships
- [[fibonacci-trading]] -- trading strategies built around Fibonacci tools
- [[chart-patterns]] -- structural patterns that benefit from Fibonacci target measurement
- [[trend-following]] -- Fibonacci pullback entries are a trend-following technique

## Sources

- [[book-technical-analysis-of-the-financial-markets]] -- comprehensive coverage of Fibonacci tools and their application in technical analysis
