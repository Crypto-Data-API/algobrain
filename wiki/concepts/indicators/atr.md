---
title: Average True Range (ATR)
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags: [atr, indicators, volatility]
aliases: [ATR, average-true-range]
domain: [indicators]
prerequisites: ["[[volatility]]"]
difficulty: intermediate
related:
  - "[[volatility]]"
  - "[[stop-loss]]"
  - "[[position-sizing]]"
  - "[[bollinger-bands]]"
  - "[[book-technical-analysis-of-the-financial-markets]]"
  - "[[j-welles-wilder]]"
  - "[[turtle-trading]]"
  - "[[donchian-channels]]"
  - "[[adx]]"
  - "[[rsi]]"
---

# ATR (Average True Range)

ATR is a [[volatility]] indicator that measures the average range of price movement over a specified number of periods, accounting for gaps.

## Overview

Developed by J. Welles Wilder (also the creator of [[rsi]]), ATR does not indicate direction -- only the degree of price movement (Source: [[book-technical-analysis-of-the-financial-markets]]). A high ATR means the asset is experiencing large price swings; a low ATR means it is trading quietly. ATR is one of the most practical indicators for setting [[stop-loss]] levels and calibrating [[position-sizing]].

## How It Works

- **True Range (TR)**: The greatest of: (1) current high minus current low, (2) absolute value of current high minus previous close, (3) absolute value of current low minus previous close. This captures gap moves that a simple high-low range would miss.
- **ATR**: The moving average (typically 14-period) of True Range values.
- **ATR is expressed in price units** (e.g., $2.50), not as a percentage, making it specific to the asset's price level.

## Key Applications

- **Stop-loss placement**: Set stops at a multiple of ATR from entry (e.g., 2x ATR). This adapts your stop to current volatility -- wider in volatile conditions, tighter in calm conditions.
- **Position sizing**: Divide your risk budget by ATR to normalize risk across different assets. If Asset A has an ATR of $5 and Asset B has an ATR of $50, you trade 10x more units of A to equalize volatility exposure.
- **Breakout confirmation**: ATR expansion confirms that a breakout has genuine momentum behind it, not just a low-volume spike.

## Trading Relevance

ATR solves a common problem: using fixed-dollar stops that are either too tight (stopped out by normal noise) or too wide (excessive risk). By anchoring stops and position sizes to ATR, your risk management automatically adjusts to market conditions. Many professional traders consider ATR-based position sizing the single most important risk management technique.

## The Turtle "N" Unit

ATR's most famous application beyond basic stop-loss placement is as the "N" unit in the [[turtle-trading|Turtle Trading]] system. Richard Dennis and Bill Eckhardt used ATR to normalise risk across their diversified futures portfolio: each "unit" risked a fixed fraction (~1%) of equity per 1N of ATR, then stacked up to 4 units per market. This approach — where ATR governs position sizing rather than leverage — produced effective gross leverage of 4×–10× capital while keeping per-trade risk consistent across markets with wildly different volatility profiles (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]).

[[j-welles-wilder|Wilder]] himself emphasised that ATR-based position sizing — not raw leverage — is what separates durable systems from blow-ups. The principle applies across all venues: futures (intrinsic 10–25× margin leverage), forex (30–500× retail leverage), and crypto perp-futures (20–125× leverage). In all cases, ATR-normalised sizing prevents the strategy from taking outsized risk in volatile conditions while being too conservative in calm ones (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]).

## Sources

- J. Welles Wilder Jr., *New Concepts in Technical Trading Systems* (Trend Research, 1978) — the original definition of True Range and the Average True Range.
- Curtis Faith, *Way of the Turtle* (McGraw-Hill, 2007) — first-hand account of the Turtle system's use of ATR as the "N" volatility unit for position sizing.
- John J. Murphy, *Technical Analysis of the Financial Markets* (NYIF, 1999) — covers True Range/ATR for stop placement and volatility measurement.
- [[book-technical-analysis-of-the-financial-markets]] -- Murphy covers Wilder's True Range and ATR concepts, including their application to stop-loss placement and volatility measurement
- [[2026-04-20-comprehensive-guide-technical-trading-indicators]] — Turtle "N" unit, Wilder's position sizing philosophy, cross-venue leverage context

## Related

- [[volatility]] -- ATR is a core volatility measure
- [[stop-loss]] -- ATR-based stops adapt to conditions
- [[position-sizing]] -- ATR normalizes risk across assets
- [[bollinger-bands]] -- complementary volatility tool
- [[j-welles-wilder]] -- ATR's creator, from the same 1978 book as [[rsi]] and [[adx]]
- [[turtle-trading]] -- ATR as the "N" unit for position sizing
- [[donchian-channels]] -- Donchian + ATR is the core Turtle system
