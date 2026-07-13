---
title: "Sherman McClellan"
type: entity
created: 2026-04-20
updated: 2026-06-21
status: excellent
tags: [person, technical-analysis, indicators, history]
entity_type: person
website: "https://www.mcoscillator.com"
aliases: ["McClellan", "Sherman McClellan"]
related: ["[[mcclellan-oscillator]]", "[[mcclellan-summation-index]]", "[[market-breadth]]", "[[advance-decline-line]]", "[[breadth-thrust]]", "[[arms-index]]", "[[richard-arms]]"]
---

# Sherman McClellan

Sherman McClellan is the co-creator, with his wife Marian McClellan, of the [[mcclellan-oscillator|McClellan Oscillator]] (1969), a [[market-breadth|breadth]] indicator measuring NYSE advance/decline dynamics used by index traders to gauge market internals (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]). The McClellan family's breadth tools remain among the most widely quoted market-internal measures more than five decades later.

## Key Facts

| Field | Detail |
|-------|--------|
| Name | Sherman McClellan |
| Co-creator | **Marian McClellan** (wife; d. 2003) |
| Nationality | American (worked in Los Angeles) |
| Known for | Co-creator of the **[[mcclellan-oscillator\|McClellan Oscillator]]** and **[[mcclellan-summation-index\|McClellan Summation Index]]** (1969) |
| Field | [[market-breadth\|Market breadth]] / market internals |
| Key influence | P.N. "Pete" Haurlan (JPL rocket scientist; EMA pioneer) |
| Book | *Patterns for Profit* (1970) |
| Major honor | Market Technicians Association (MTA) Annual Award, **2004** |
| Continued by | Son **Tom McClellan**, *The McClellan Market Report* (since 1995) |
| Publication site | https://www.mcoscillator.com |

## Who He Was and His Era

Working in **Los Angeles in 1969**, Sherman and Marian McClellan developed the oscillator after exposure to the work of **P.N. "Pete" Haurlan**, a Jet Propulsion Laboratory rocket scientist who pioneered the use of exponential moving averages in market analysis and aired the *Charting the Market* television program. Haurlan's insight — that EMAs (which he called "trend smoothing constants" from his missile-tracking background) could be applied to market data — gave the McClellans the mathematical machinery to convert raw daily breadth into a smooth, tradable signal. They sat at the intersection of the aerospace-engineering culture of 1960s Southern California and the emerging discipline of quantitative [[technical-analysis]].

The couple published their methodology in the book ***Patterns for Profit*** (1970), which laid out both the oscillator and its running-total companion, the Summation Index.

## What He Is Known For: The McClellan Oscillator and Summation Index

The McClellans' signature contribution is a pair of linked [[market-breadth|breadth]] tools built on **NYSE net advances** (the number of advancing issues minus declining issues each day).

### The McClellan Oscillator

The oscillator is the **difference between two exponential moving averages of daily net advances (advances minus declines)**:

- **19-day EMA** of (advances − declines) — the "fast" component (≈ 10% smoothing constant)
- **39-day EMA** of (advances − declines) — the "slow" component (≈ 5% smoothing constant)
- **McClellan Oscillator = 19-day EMA − 39-day EMA**

This is structurally analogous to [[macd|MACD]], but applied to *breadth* (the whole market's participation) rather than to a single instrument's price. A positive and rising oscillator means breadth momentum is improving; a negative and falling reading means deterioration beneath the index surface.

### The McClellan Summation Index

The **[[mcclellan-summation-index|Summation Index]]** is the **running cumulative total of the daily McClellan Oscillator values** — a slower, longer-horizon gauge of breadth trends. Where the oscillator is a momentum signal, the Summation Index behaves like a position/regime gauge: sustained readings above zero characterize healthy bull phases, while a falling Summation Index warns of an aging or weakening advance even when headline indices are still rising.

## How Traders Use It

- The McClellan Oscillator is a standard **overbought/oversold and divergence** tool for index and [[etf]] traders; readings beyond roughly ±100 flag breadth extremes.
- A **"[[breadth-thrust|breadth thrust]]"** — a surge above +100 from deeply negative levels — is a classic bull signal indicating that selling has been exhausted and broad buying has resumed.
- The **Summation Index** is widely used for regime identification and for spotting [[divergence]] between market internals and the price of the index itself.
- NASDAQ and custom-universe versions are computed by most major data platforms, and the oscillator is a common input in systematic [[market-breadth]] models alongside the [[advance-decline-line|advance-decline line]] and [[arms-index|Arms Index (TRIN)]].

## Influence and Legacy

The McClellans received the **Market Technicians Association (MTA) Annual Award in 2004** for their contribution to technical analysis. Marian McClellan died in **2003**. Their son, **Tom McClellan**, has edited and published *The McClellan Market Report* since **1995** (mcoscillator.com), continuing the family's breadth-focused research; the publication remained active as of 2025–2026, and no reports indicate Sherman's death as of June 2026.

The lasting significance of the McClellan work is that it made **market breadth a first-class quantitative input** rather than an eyeballed concept. By giving advance-decline data the EMA treatment, they produced internals indicators that institutions, newsletter writers, and systematic traders still quote daily — a rare example of an indicator family that has been maintained and extended by the same family across three generations.

## Related

- [[mcclellan-oscillator]] — the headline breadth momentum tool
- [[mcclellan-summation-index]] — the cumulative regime gauge
- [[market-breadth]] — the broader concept they helped quantify
- [[advance-decline-line]] — the raw data series the oscillator is built on
- [[breadth-thrust]] — the classic bullish signal
- [[arms-index]] / [[richard-arms]] — companion breadth/volume internals

## Sources

- [[2026-04-20-comprehensive-guide-technical-trading-indicators]] — Comprehensive Guide to Technical Trading Indicators
- Sherman & Marian McClellan, *Patterns for Profit: The McClellan Oscillator and Summation Index* (Trade Service Corp, 1970)
- McClellan Financial Publications (Tom McClellan, ed.), *The McClellan Market Report*: https://www.mcoscillator.com
- StockCharts ChartSchool, "McClellan Oscillator": https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/mcclellan-oscillator
- Verified via Perplexity (sonar), 2026-06-10: oscillator origin (1969, with Marian), McClellan Market Report status, no death notice for Sherman
