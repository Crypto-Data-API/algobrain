---
title: "Joseph Granville"
type: entity
created: 2026-04-20
updated: 2026-06-21
status: excellent
tags: [person, technical-analysis, indicators, history]
aliases: ["Granville", "Joseph Ensign Granville", "Joe Granville"]
entity_type: person
founded: 1923
headquarters: "Kansas City, Missouri, USA"
related: ["[[obv]]", "[[volume]]", "[[technical-analysis]]", "[[market-timing]]"]
---

# Joseph Granville

Joseph Ensign Granville (August 20, 1923 – September 7, 2013) was an American financial writer and market-letter publisher who created [[obv|On-Balance Volume (OBV)]], one of the first indicators to use cumulative volume flow to confirm price trends (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]). At his peak in the early 1980s he was arguably the most market-moving individual forecaster in history — a single "sell everything" telegram to subscribers knocked roughly 2.4% off the Dow in one session — and his later record became the canonical cautionary tale about guru forecasting.

## Key Facts

| Field | Detail |
|-------|--------|
| Full name | Joseph Ensign Granville |
| Born | August 20, 1923 |
| Died | September 7, 2013 (aged 90) |
| Nationality | American |
| Known for | [[on-balance-volume|On-Balance Volume (OBV)]]; the Granville Market Letter |
| Earlier role | Market analyst, E.F. Hutton (1957–1963) |
| Key thesis | "Volume precedes price" |
| Key books | *A Strategy of Daily Stock Market Timing for Maximum Profit* (1960); *Granville's New Key to Stock Market Profits* (1963) |
| Famous call | "Sell everything" telegram, January 6, 1981 |
| Reputation | Most market-moving individual forecaster of his era; later a cautionary tale on [[market-timing]] |
| Discipline | [[technical-analysis]], [[volume]] analysis |

## Overview

Granville worked as a market analyst at E.F. Hutton from 1957 to 1963 before launching the **Granville Market Letter**, which he published for five decades. His books *A Strategy of Daily Stock Market Timing for Maximum Profit* (1960) and *Granville's New Key to Stock Market Profits* (1963) introduced On-Balance Volume — a running total that adds the day's volume on up-closes and subtracts it on down-closes — built on his thesis that "volume precedes price" and that smart-money accumulation shows up in volume before it shows up in price.

## The Method: On-Balance Volume (OBV)

[[on-balance-volume|On-Balance Volume]] is a **cumulative** indicator that treats each period's entire volume as a single positive or negative vote, depending only on whether price closed up or down. The running total is built as:

```
If Close(today) > Close(yesterday):   OBV = OBV_prev + Volume(today)
If Close(today) < Close(yesterday):   OBV = OBV_prev − Volume(today)
If Close(today) = Close(yesterday):   OBV = OBV_prev          (unchanged)
```

The *absolute level* of OBV is arbitrary (it depends on the starting point); what matters is its **slope and direction** relative to price. Granville's interpretive logic:

- **Confirmation** — when price makes a new high and OBV makes a new high, the up-move is "backed" by volume and is more trustworthy.
- **Divergence** — when price makes a new high but OBV fails to (or vice versa), volume is *not* confirming the move, warning of a possible reversal. This was the operational core of "volume precedes price."
- **Accumulation vs. distribution** — a rising OBV during a flat or basing price suggested *smart-money accumulation* before a markup; a falling OBV during flat price suggested distribution before a decline.

OBV deliberately ignores the *size* of the daily price change and any intraday range — every up-day adds its full volume, every down-day subtracts it. That simplicity (computable by hand in 1963) is both its strength and its limitation; later refinements such as the **Accumulation/Distribution Line**, **Chaikin Money Flow**, and **Volume-Price Trend** weight volume by where price closed within its range, addressing OBV's all-or-nothing rule.

## The Market-Moving Calls (1980–1981)

- **April 22, 1980**: Granville's bullish call coincided with the Dow rising 4.05% — at the time one of its largest single-day gains.
- **January 6, 1981**: Late in the evening, Granville sent his subscribers an unconditional "sell everything" signal. The next day, January 7, 1981, the Dow fell 23.80 points (about 2.4%) on then-record NYSE volume of roughly 93 million shares, with estimated paper losses of about $25 billion. It remains the textbook example of a single forecaster moving an entire market — a phenomenon studied in [[behavioral-finance]] and market-impact research.

## Decline of the Record

Granville stayed bearish through the great 1982–1987 bull market, repeatedly predicting a crash that arrived only in October 1987 after the Dow had nearly tripled. He also damaged his credibility with non-market predictions, most famously forecasting a Los Angeles earthquake in 1981. Mark Hulbert's *Hulbert Financial Digest*, which tracked the Granville Market Letter for 25 years, rated it the worst performer of any letter monitored over 1980–2005, with stock-picking advice losing on the order of 20% a year on an annualized basis. Granville was also a showman — he appeared at investment seminars in costume, once "walked on water" across a hotel pool, and toured the world giving sold-out market lectures.

## Influence and Legacy

- **OBV's staying power**: [[on-balance-volume|On-Balance Volume]] is shipped in virtually every charting platform and is the conceptual ancestor of the entire volume-flow family — Accumulation/Distribution, Chaikin Money Flow, Volume-Price Trend, and Money Flow Index. Granville arguably did more than anyone to popularize **[[volume]] as a confirming dimension of price**.
- **Proof that attention moves markets**: the January 1981 episode is a textbook demonstration of *reflexivity* and market impact — a forecast, broadly acted on at once, became briefly self-fulfilling. It is cited in [[behavioral-finance]] and market-microstructure discussion of crowding and information cascades.
- **The canonical guru cautionary tale**: Granville's full-cycle record — staying bearish through the 1982–1987 bull market and rated the worst-performing letter Hulbert tracked — became the standard argument for *systematic, evidence-based* methods over charismatic forecasting. He is, in effect, the case study that motivates rigorous [[backtesting]] and skepticism of personality-driven [[market-timing]].
- **Showman and popularizer**: his theatrical seminars (costumes, the famous "walking on water" pool stunt, sell-out world tours) helped bring [[technical-analysis]] to a mass retail audience in the 1970s–80s, for better and worse.

## Trading Relevance

Granville's legacy is double-edged. OBV remains a standard volume indicator shipped in virtually every charting platform and underpins the modern family of volume-flow tools (accumulation/distribution, Chaikin Money Flow, volume-price trend). At the same time, his career is the canonical case study in (1) the market impact of concentrated attention — the 1981 signal demonstrated that forecasts themselves can move prices; and (2) guru risk — a forecaster can be famous, market-moving, and still destroy wealth over a full cycle, which is the core argument for systematic [[backtesting]] over personality-driven [[market-timing]].

## Related

- [[obv]]
- [[on-balance-volume]]
- [[volume]]
- [[technical-analysis]]
- [[market-timing]]
- [[behavioral-finance]]
- [[indicators-overview]]
- [[accumulation-distribution]]
- [[chaikin-money-flow]]

## Sources

- [[2026-04-20-comprehensive-guide-technical-trading-indicators]] — Comprehensive Guide to Technical Trading Indicators
- Wikipedia: Joseph Granville — https://en.wikipedia.org/wiki/Joseph_Granville (birth/death dates; April 1980 and January 1981 market moves; ~$25B one-day loss) — fetched 2026-06-10
- New York Times obituary, "Joseph Granville, Stock Market Predictor, Dies at 90" (September 2013) — Hulbert Financial Digest assessment of his 25-year record
- Joseph Granville, *Granville's New Key to Stock Market Profits* (1963)
- Verified via Perplexity (sonar), 2026-06-10
