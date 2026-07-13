---
title: "Technical Indicators"
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags: [indicators, technical-analysis]
aliases: ["Indicators", "Technical Indicators"]
domain: [indicators]
prerequisites: ["[[technical-analysis]]"]
difficulty: beginner
related: ["[[technical-analysis]]", "[[rsi]]", "[[macd]]", "[[moving-averages]]", "[[bollinger-bands]]", "[[atr]]", "[[vwap]]", "[[obv]]"]
---

Technical indicators are mathematical calculations derived from price, volume, or open-interest data that traders use to analyse market conditions, identify trends, and generate signals. They are the core quantitative tools of [[technical-analysis]] — transformations that compress raw price action into a smoother, comparable form.

## How They Work

Every indicator is a function of historical market data. Most fall on a spectrum between two properties:

- **Leading vs lagging** — *leading* indicators (oscillators, momentum) attempt to anticipate turns and tend to fire early but produce more false signals; *lagging* indicators ([[moving-averages]], MACD) confirm trends already underway and reduce false signals at the cost of timeliness.
- **Smoothing vs responsiveness** — longer lookbacks smooth noise but add lag; shorter lookbacks react faster but whipsaw.

No indicator adds information beyond what is in price and volume; they reorganise that information to make patterns easier to act on. This is why redundant indicators (e.g. three momentum oscillators) add little — they restate the same underlying signal.

## Categories

### Trend-Following Indicators

Identify and confirm trend direction. Best in trending markets; prone to whipsaw in ranges.

- **[[moving-averages]]** (SMA, EMA) — smoothed price over N periods. The [[200-day-moving-average|200-day MA]] is the key bull/bear dividing line.
- **[[macd]]** — convergence/divergence between two EMAs; signal-line crossovers generate entries.
- **[[adx]]** — measures trend *strength* (not direction). Above 25 = trending; below 20 = ranging.

### Oscillators

Measure overbought/oversold conditions, bounded in a range. Best in range-bound markets. (See [[oscillators]].)

- **[[rsi]]** — ranges 0–100; >70 overbought, <30 oversold. [[divergence]] vs price is a strong signal.
- **[[stochastic]]** — compares closing price to the recent high-low range.

### Volume Indicators

Confirm price moves with the volume behind them.

- **[[obv]]** (On-Balance Volume) — cumulative volume flow.
- **[[vwap]]** — volume-weighted average price; the key institutional execution benchmark.

### Volatility Indicators

Measure the magnitude of price fluctuation.

- **[[bollinger-bands]]** — envelopes at ±N standard deviations from a moving average; squeezes precede breakouts.
- **[[atr]]** (Average True Range) — average price range; used for [[stop-loss]] placement and [[position-sizing]].

## Trading Relevance

Indicators are decision aids, not systems. Effective use:

- Combine **complementary** indicator types (e.g. a trend filter + an oscillator for entry timing) rather than stacking redundant ones.
- Match the indicator to the **regime** — oscillators in ranges, trend tools in trends; misapplied, each generates the other's worst failure mode.
- Always pair signals with [[risk-management]] (defined stops, sizing). An indicator's edge is small and easily erased by poor execution.
- Beware **curve-fitting**: tuning lookback parameters to past data inflates [[backtesting]] results that do not survive out of sample.

See [[technical-analysis]] for the full framework.

## Sources

- John J. Murphy, *Technical Analysis of the Financial Markets* (1999) — the standard reference cataloguing indicator families.
- Martin Pring, *Technical Analysis Explained* — trend, momentum, and volume indicator mechanics.

## Related

- [[technical-analysis]] — the discipline these tools serve
- [[rsi]], [[macd]], [[moving-averages]], [[bollinger-bands]], [[atr]] — major individual indicators
- [[oscillators]] — the overbought/oversold indicator family
- [[divergence]] — a cross-indicator signal pattern
