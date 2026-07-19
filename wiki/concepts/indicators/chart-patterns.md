---
title: "Chart Patterns"
type: concept
created: 2026-04-07
updated: 2026-07-19
status: good
tags: [technical-analysis, indicators]
aliases: ["Chart Pattern Recognition", "ascending-triangle", "Ascending Triangle"]
related: ["[[price-action]]", "[[support-and-resistance]]", "[[candlestick-patterns]]", "[[head-and-shoulders]]", "[[flags-and-pennants]]", "[[cup-and-handle]]", "[[volume-analysis]]", "[[breakout-strategies]]"]
domain: [technical-analysis]
difficulty: intermediate
---

Chart patterns are recognizable geometric formations that appear in price charts, created by the collective behavior of market participants. These patterns encode phases of accumulation, distribution, consolidation, and breakout, and are used to forecast the probable direction and magnitude of the next price move. Chart pattern analysis is a core discipline within [[technical-analysis]] and [[price-action]] trading.

## Overview

The study of chart patterns dates back to the early 20th century, with Charles Dow's work on market structure and Richard Schabacker's 1932 systematization. The definitive reference is Edwards and Magee's *Technical Analysis of Stock Trends* (1948), later expanded upon in [[book-technical-analysis-of-the-financial-markets]] by John Murphy.

Patterns are broadly categorized as:

- **Reversal patterns** -- signal that the prevailing trend is likely to change direction
- **Continuation patterns** -- signal that the current trend will resume after a pause
- **Bilateral patterns** -- can resolve in either direction (e.g., symmetric triangles)

The reliability of any pattern depends on context: the preceding trend, [[volume-analysis|volume]] behavior during formation, the timeframe, and proximity to major [[support-and-resistance]] levels.

## How It Works

### Reversal Patterns

**Head and Shoulders**: Three peaks with the middle (head) highest and two lower peaks (shoulders) on either side. The neckline connecting the troughs is the key level. A break below the neckline confirms the reversal. Measured move target equals the distance from head to neckline. See [[head-and-shoulders]].

**Inverse Head and Shoulders**: Mirror image of the above, appearing at market bottoms. Break above the neckline signals bullish reversal.

**Double Top / Double Bottom**: Two peaks (or troughs) at approximately the same price level, with a pullback between them. Confirms when price breaks the intervening pullback level. Signals exhaustion of the trend.

**Triple Top / Triple Bottom**: Three tests of the same level that fail to break through, followed by reversal. Stronger signal than double patterns due to repeated failure.

**Rounding Bottom (Saucer)**: Gradual, U-shaped transition from downtrend to uptrend. Indicates a slow shift in sentiment from bearish to bullish. Often seen on longer timeframes.

### Continuation Patterns

**Flags and Pennants**: Short, compact consolidations that slope against the prevailing trend. [[flags-and-pennants|Flags]] are parallelogram-shaped; pennants are small symmetrical triangles. Both resolve in the trend direction. Measured move equals the length of the prior impulse (the "flagpole"). Among the most reliable short-term patterns.

**Cup and Handle**: Rounded bottom (cup) followed by a small downward drift (handle), then breakout. Identified by william-o-neil as a powerful continuation setup. See [[cup-and-handle]].

**Ascending / Descending Triangle**: A flat boundary on one side (resistance for ascending, support for descending) with a converging trendline on the other. Ascending triangles are bullish; descending are bearish. Breakout direction matches the flat boundary side.

**Rectangles (Trading Ranges)**: Horizontal consolidation between parallel support and resistance. Neutral until a breakout occurs in either direction.

### Bilateral Patterns

**Symmetric Triangle**: Converging trendlines with lower highs and higher lows. Can break in either direction. Volume typically contracts during formation and expands on breakout.

**Wedges**: Rising wedges (bearish) and falling wedges (bullish). Resemble triangles but both boundaries slope in the same direction. Rising wedges in uptrends are continuation patterns for the bearish move; falling wedges in downtrends are bullish.

### Volume Confirmation

Volume behavior is critical for validating chart patterns:
- Volume should decline during pattern formation (consolidation)
- Volume should surge on the breakout candle
- A breakout on low volume is suspect and more likely to fail
- See [[volume-analysis]] for detailed treatment

### Measured Move Targets

Most patterns provide a price target based on the pattern's dimensions:
- **Head and shoulders**: distance from head to neckline, projected from breakout point
- **Flags/pennants**: length of the flagpole, projected from breakout
- **Triangles/rectangles**: width of the pattern at its widest point, projected from breakout
- **Cup and handle**: depth of the cup, projected from the handle's breakout level

These targets are guidelines, not guarantees. Many traders use them for initial profit targets and then trail stops for additional gains.

## Trading Applications

### Pattern Trading Process
1. Identify the prevailing [[trend]] and context
2. Recognize the forming pattern and classify it (reversal, continuation, bilateral)
3. Wait for the breakout -- do not anticipate
4. Confirm with [[volume-analysis|volume]] and ideally a close beyond the breakout level
5. Enter on the breakout or on a retest of the broken level
6. Set stop-loss just inside the pattern boundary
7. Target the measured move or the next significant [[support-and-resistance]] level

### Common Pitfalls
- **Seeing patterns that are not there** (apophenia / confirmation bias)
- **Trading patterns in isolation** without considering trend, volume, and support/resistance context
- **Ignoring failed patterns** -- a failed [[head-and-shoulders]] breakout, for example, often produces a powerful move in the opposite direction
- **Over-reliance on pattern targets** -- markets are not obligated to reach measured move levels

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-data/ticker/24hr?symbol=BTCUSDT` — 24h ticker stats
- `GET /api/v1/market-data/short-term-price` — short-term momentum metrics

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=4h&limit=1000` — OHLCV bars for pattern scans
- `GET /api/v1/market-data/volume-history?days=90` — daily volume + buy ratio for breakout confirmation
- `GET /api/v1/backtesting/klines` — deep kline archive

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=4h&limit=1000"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-data]].

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can work with these patterns directly:

- **Fetch** — `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=4h&limit=1000` supplies the swing highs/lows that pattern-recognition code (pivot detection, trendline fitting) runs on
- **Confirm** — validate breakouts against `GET /api/v1/market-data/volume-history`: the volume-contraction-then-surge signature this page requires
- **Backtest** — `GET /api/v1/backtesting/klines` (Binance spot 1h/4h/1d back to 2017-08) is deep enough to measure pattern completion rates and measured-move accuracy across full cycles
- **Tip** — codify each pattern as explicit pivot-geometry rules before backtesting; eyeballed patterns cannot be validated, and loose definitions data-mine themselves into false edges (see the pitfalls above)

## Related

- [[price-action]] -- broader framework within which chart patterns are a component
- [[candlestick-patterns]] -- individual bar patterns vs. multi-bar chart formations
- [[head-and-shoulders]] -- classic reversal pattern
- [[cup-and-handle]] -- powerful continuation pattern
- [[flags-and-pennants]] -- short-term continuation patterns
- [[support-and-resistance]] -- levels that define pattern boundaries
- [[volume-analysis]] -- essential confirmation tool for breakouts
- [[breakout-strategies]] -- trading strategies built around pattern breakouts

## Sources

- [[book-technical-analysis-of-the-financial-markets]] -- comprehensive reference for all major chart patterns
