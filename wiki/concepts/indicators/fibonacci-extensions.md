---
title: "Fibonacci Extensions"
type: concept
created: 2026-04-15
updated: 2026-07-19
status: good
tags: [indicators, technical-analysis]
aliases: ["Fibonacci Extensions", "Fib Extensions", "Fibonacci Projections", "Fibonacci Targets"]
related: ["[[fibonacci-retracement]]", "[[technical-analysis]]", "[[support-and-resistance]]", "[[trend-following]]", "[[elliott-wave]]", "[[harmonic-patterns]]", "[[chart-patterns]]", "[[price-action]]"]
domain: [indicators]
prerequisites: ["[[fibonacci-retracement]]"]
difficulty: intermediate
---

Fibonacci extensions are a [[technical-analysis|technical analysis]] tool that projects potential price targets *beyond* the end of a completed move, using ratios derived from the Fibonacci sequence (most commonly 127.2%, 161.8%, 200%, and 261.8%). Where [[fibonacci-retracement|Fibonacci retracements]] identify where a pullback might find [[support-and-resistance|support or resistance]] *within* a move, extensions answer the opposite question: once the trend resumes, how far might it run? Traders use them to set profit targets and identify exhaustion zones.

## Overview

Both retracements and extensions come from the same set of ratios in the Fibonacci sequence (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55...), but they are applied to different parts of a swing structure. A retracement measures a counter-trend pullback as a fraction of the prior impulse (always less than 100% of it). An extension measures the next impulse leg as a multiple of the prior one — typically more than 100% — projecting a target above the prior high (uptrend) or below the prior low (downtrend).

The key extension ratios are:

| Level | Derivation | Typical use |
|---|---|---|
| **100%** | The new leg equals the prior swing (a "measured move" / AB=CD) | First conservative target |
| **127.2%** | Square root of 1.618 (√φ) | Common first extension target |
| **161.8%** | The golden ratio (φ); any Fibonacci number divided by the previous one | The single most-watched extension target |
| **200%** | Double the prior swing | Strong-trend target |
| **261.8%** | φ² (1.618²) | Extended target for powerful, accelerating trends |

161.8% is the most significant extension level because it is the golden ratio itself — the inverse relationship to the 61.8% retracement. In an [[elliott-wave]] framework, a third wave commonly extends to 161.8% of the first wave, which is one reason this level is so closely watched.

## How to Draw Fibonacci Extensions

Extensions require three reference points (a swing leg plus its retracement), unlike retracements which need only two:

1. **Point A** — the start of the prior impulse (e.g., a swing low in an uptrend).
2. **Point B** — the end of that impulse (the swing high).
3. **Point C** — the end of the retracement / pullback (the higher low from which the next leg launches).

The tool then projects the extension levels of the A→B distance, measured from point C. For example, if a stock rallies from $100 (A) to $150 (B), pulls back to $130 (C), and then breaks above $150, the extensions from C are:

- 100% extension = $130 + ($150−$100) = **$180**
- 127.2% extension = $130 + (0.50 × 1.272 × 100) ... more directly: $130 + ($50 × 1.272) = **$193.60**
- 161.8% extension = $130 + ($50 × 1.618) = **$210.90**
- 200% extension = $130 + ($50 × 2.00) = **$230**

(Software conventions vary — some tools project the A→B range from C, others project from B. The 127.2%/161.8%/261.8% targets are the same idea regardless.)

## Trading Applications

### Profit targets
The dominant use of extensions is to set realistic, pre-planned exit prices. A trend trader who enters long on a [[fibonacci-retracement]] pullback (e.g., at the 61.8% retracement of A→B) can scale out at the 127.2% and 161.8% extensions of the next leg, giving a defined risk/reward plan before the trade is placed.

### Confluence
As with retracements, an extension level carries far more weight when it lines up with other evidence — a prior [[support-and-resistance]] zone, a round number, a [[volume-profile]] node, or a measured move from a [[chart-patterns|chart pattern]]. A 161.8% extension that coincides with a major resistance shelf is a high-conviction target zone.

### Elliott Wave and harmonic patterns
[[elliott-wave]] theory uses extensions to project impulse-wave targets (wave 3 ≈ 161.8% of wave 1; wave 5 often equals wave 1 or extends to 61.8% of waves 1–3). [[harmonic-patterns]] (Gartley, Butterfly, Crab) are defined by precise combinations of retracement and extension ratios — the Crab pattern, for instance, hinges on a 161.8% extension of the initial leg.

## Limitations

- **Subjectivity** — like retracements, extensions depend on which swing points (A, B, C) the trader selects; different choices yield different targets.
- **Targets, not guarantees** — price frequently stalls *near* but not *at* an extension level, or blows through it entirely in a strong trend. Extensions define zones to watch, not precise reversal prices.
- **Best as an exit tool** — extensions help plan where to take profit; they are weak as standalone entry signals and should be combined with [[price-action]] confirmation and other [[technical-analysis]] tools.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=BTCUSDT` — current price versus projected targets

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=500` — OHLCV for detecting the A-B-C swing structure
- `GET /api/v1/backtesting/klines` — deep kline archive

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=500"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-data]].

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can work with this tool directly:

- **Compute** — detect swing points A/B/C in `GET /api/v1/market-data/klines` output (pivot logic with a fixed lookback), then project C + (B−A) × {1.0, 1.272, 1.618, 2.0, 2.618}
- **Confluence** — score targets higher when they land near prior highs/lows from the same kline series — the confluence requirement this page stresses, made mechanical
- **Backtest** — `GET /api/v1/backtesting/klines` (Binance spot 1h/4h/1d back to 2017-08) lets you measure how often price stalls within a tolerance band of each ratio versus random levels — the honest test of whether extensions beat chance
- **Tip** — fix the pivot definition (e.g. fractal depth) in code; subjective swing selection is the tool's main weakness, and a consistent agent removes it

## Related

- [[fibonacci-retracement]] — the companion tool for pullback support/resistance (extensions and retracements are used together)
- [[support-and-resistance]] — extension levels act as projected resistance/support
- [[elliott-wave]] — uses extension ratios to project impulse targets
- [[harmonic-patterns]] — chart patterns defined by retracement and extension ratios
- [[trend-following]] — extensions set profit targets for trend trades
- [[chart-patterns]] — measured-move targets overlap with the 100% extension

## Sources

- [[book-technical-analysis-of-the-financial-markets]] — Murphy's coverage of Fibonacci projections and price targets in technical analysis
- Frost, A.J. & Prechter, R. (2005). *Elliott Wave Principle: Key to Market Behavior* — the canonical treatment of Fibonacci extension relationships between impulse waves
