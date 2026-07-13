---
title: "J. Welles Wilder Jr."
type: entity
created: 2026-04-20
updated: 2026-06-22
status: excellent
tags: [person, technical-analysis, indicators, history, futures]
entity_type: person
aliases: ["Wilder", "J. Welles Wilder", "Welles Wilder", "John Welles Wilder Jr."]
related: ["[[rsi]]", "[[atr]]", "[[adx]]", "[[parabolic-sar]]", "[[turtle-trading]]", "[[position-sizing]]"]
---

John Welles Wilder Jr. (June 11, 1935 – April 18, 2021) was an American mechanical engineer turned real estate developer who became one of the most influential figures in [[technical-analysis|technical analysis]]. He authored *New Concepts in Technical Trading Systems* (1978), a compact book that introduced a toolkit of indicators — [[relative-strength-index|RSI]], [[average-true-range|ATR]], [[adx|ADX/DMI]], [[parabolic-sar|Parabolic SAR]], Swing Index, and Commodity Selection Index (CSI) — that became the core of almost every charting platform in existence (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]).

## Key Facts

| Field | Detail |
|-------|--------|
| Full name | John Welles Wilder Jr. |
| Born | June 11, 1935 (Norris City, Illinois, USA) |
| Died | April 18, 2021 (Christchurch, New Zealand), aged 85 |
| Nationality | American (emigrated to New Zealand late in life) |
| Era | Active researcher/author from early 1970s; landmark work 1978 |
| Profession | Mechanical engineer → real estate developer → commodity-futures researcher |
| Education | BS Mechanical Engineering, North Carolina State University (1962) |
| Best known for | [[relative-strength-index\|RSI]], [[average-true-range\|ATR]], [[adx\|ADX/DMI]], [[parabolic-sar\|Parabolic SAR]] |
| Signature book | *New Concepts in Technical Trading Systems* (1978) |
| Company | Trend Research Ltd. (publishing/research) |
| Honors | Often called by *Forbes* "the premier technical trader publishing his work today" |

## Overview

Originally trained as a mechanical engineer, Wilder brought a quantitative, systems-based approach to markets. His indicators cover momentum ([[relative-strength-index|RSI]]), volatility ([[average-true-range|ATR]]), trend strength ([[adx|ADX/DMI]]), and trailing exits ([[parabolic-sar|Parabolic SAR]]), giving traders a complete framework for analysing any market (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]).

Biographical detail:

- Served in the **U.S. Navy** during the Korean War, then earned a BS in mechanical engineering from **North Carolina State University** (1962).
- Made his first fortune in **real estate development** in Greensboro, North Carolina, before turning full-time to commodity futures research in the early 1970s.
- Founded and ran **Trend Research Ltd.**, through which he published his books and trading research.
- Later books: *The Adam Theory of Markets* (1987) and *The Delta Phenomenon* (1991), the latter sold through the members-only Delta Society — both far more controversial than his 1978 indicator work.
- Emigrated to **New Zealand** in later life and died in **Christchurch on April 18, 2021**, aged 85.

## Key Contributions

All of these debuted together in the single 1978 volume *New Concepts in Technical Trading Systems* — arguably the highest indicators-per-page ratio of any trading book ever published (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]).

| Indicator | Year | Category | Default period | Core reading |
|-----------|------|----------|----------------|--------------|
| [[relative-strength-index\|RSI]] | 1978 | Momentum oscillator | 14 | 70 overbought / 30 oversold |
| [[average-true-range\|ATR]] | 1978 | Volatility | 14 | Higher = wider range; sized in price units |
| [[adx\|ADX/DMI]] | 1978 | Trend strength | 14 | ADX > 25 = trending; +DI/−DI = direction |
| [[parabolic-sar\|Parabolic SAR]] | 1978 | Trailing stop / reversal | AF start 0.02, max 0.20 | Dot flips side on stop hit |
| Swing Index / ASI | 1978 | Price-pattern momentum | n/a | Cumulative line confirms breakouts |
| Commodity Selection Index (CSI) | 1978 | Instrument ranking | n/a | Ranks futures by directional movement vs. cost |

### [[relative-strength-index|RSI]] — Relative Strength Index

A bounded momentum oscillator on a 0–100 scale. RSI = 100 − [100 / (1 + RS)], where **RS = average gain / average loss** over the lookback (default 14 periods). The first average is a simple mean of gains and losses; every subsequent value uses **Wilder smoothing** — `new avg = (prior avg × (n−1) + current value) / n` — a 1/n recursive method roughly equivalent to an EMA with α = 1/n. Readings above 70 are conventionally overbought and below 30 oversold; divergence between price and RSI is the classic reversal cue.

### [[average-true-range|ATR]] — Average True Range

A pure volatility measure (it carries no directional information). **True Range** is the greatest of: (1) current high − current low, (2) |current high − previous close|, (3) |current low − previous close| — the third and second terms capture gaps. ATR is the Wilder-smoothed average of True Range over 14 periods. Because it is denominated in the instrument's price units, ATR is the natural unit for volatility-normalised stop placement and [[position-sizing|position sizing]]; it became the "N" unit in the [[turtle-trading|Turtle Trading]] system.

### [[adx|ADX/DMI]] — Average Directional Index / Directional Movement

Wilder's trend-strength framework. Directional movement is split into +DM (today's high − yesterday's high, when positive and larger) and −DM (yesterday's low − today's low, similarly). Smoothing these and dividing by ATR yields **+DI and −DI**. The **DX** = 100 × |+DI − −DI| / (+DI + −DI), and **ADX** is the Wilder-smoothed average of DX. ADX measures only the *strength* of a trend (not its direction): readings above 25 signal a tradable trend, below 20 a range; the +DI/−DI crossover supplies direction.

### [[parabolic-sar|Parabolic SAR]] — Stop and Reverse

A trailing stop-and-reversal system plotted as dots above or below price. Each period the SAR moves toward price by an **acceleration factor (AF)** that starts at 0.02 and steps up 0.02 each time a new extreme point is made, capped at 0.20: `SAR(next) = SAR + AF × (EP − SAR)`, where EP is the extreme price of the current trend. The accelerating AF tightens the stop as a trend extends; when price crosses the SAR, the system flips long↔short — making it an always-in trend-following exit tool best used in trending, not choppy, markets.

### Swing Index, ASI, and CSI

The **Swing Index** quantifies the "real" price change between bars relative to their range; the **Accumulated Swing Index (ASI)** sums it into a line that confirms breakouts and trendline validity. The **Commodity Selection Index (CSI)** ranks futures by directional movement adjusted for volatility, margin, and commission — Wilder's tool for deciding *which* market to trade, not when.

Wilder's use of his own 1/n smoothing throughout is the reason platform RSI and ATR values differ from naive simple-MA or standard-EMA implementations.

## Influence and Legacy

Wilder's 1978 toolkit is the foundation layer of modern [[technical-analysis|technical analysis]]: RSI, ATR, ADX, and Parabolic SAR ship as defaults in virtually every charting platform (TradingView, MetaStock, Bloomberg, Thinkorswim) and are referenced constantly in systematic-strategy literature. RSI is consistently among the most-applied indicators on TradingView, and ATR underpins volatility-targeting and [[position-sizing|position sizing]] across the [[turtle-trading|Turtle Trading]] tradition, [[trend-following]] CTAs, and modern [[volatility-targeting|volatility-targeted]] portfolios.

Wilder emphasised that ATR-based position sizing — not raw leverage — is what separates durable systems from blow-ups, an idea that prefigured modern risk-parity and volatility-scaling. His indicators remain among the most widely used in equities, futures, forex, and crypto more than four decades after publication (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]). *Forbes* once called him "the premier technical trader publishing his work today."

His later, far more controversial work — *The Adam Theory of Markets* (1987) and *The Delta Phenomenon* (1991), the latter sold through the members-only Delta Society — never achieved the same acceptance and is widely regarded as unfalsifiable, in sharp contrast to the rigorously specified, reproducible indicators of 1978. The contrast is itself a lesson: Wilder's enduring legacy rests on the precisely defined, testable tools, not the proprietary "secret" systems.

## Related

- [[relative-strength-index]]
- [[average-true-range]]
- [[adx]]
- [[parabolic-sar]]
- [[turtle-trading]]
- [[position-sizing]]
- [[trend-following]]
- [[technical-analysis]]
- [[george-lane]]
- [[gerald-appel]]

## Sources

- [[2026-04-20-comprehensive-guide-technical-trading-indicators]] — Comprehensive Guide to Technical Trading Indicators (compiled research, 29 references)
- Wilder, J. W. (1978). *New Concepts in Technical Trading Systems*. Trend Research.
- Wikipedia: https://en.wikipedia.org/wiki/J._Welles_Wilder_Jr.
- *Technical Analysis of Stocks & Commodities* interview (2009): http://traders.com/documentation/FEEDbk_docs/2009/03/Interview.html
- Obituary, Dignity Memorial (Greensboro, NC): https://www.dignitymemorial.com/obituaries/greensboro-nc/john-wilder-11504749
- Verified via Perplexity (sonar), 2026-06-10.
