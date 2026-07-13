---
title: "Marc Chaikin"
type: entity
created: 2026-04-20
updated: 2026-06-21
status: excellent
tags: [person, technical-analysis, indicators, data-provider, volume]
entity_type: person
aliases: ["Chaikin", "Marc Chaikin"]
website: "https://chaikinanalytics.com"
related: ["[[chaikin-money-flow]]", "[[chaikin-oscillator]]", "[[accumulation-distribution]]", "[[volume]]", "[[on-balance-volume]]", "[[joseph-granville]]", "[[larry-williams]]", "[[money-flow]]", "[[macd]]"]
---

# Marc Chaikin

Marc Chaikin (b. c. 1943) is an American stock analyst with a 50+ year Wall Street career, creator of a family of volume-based indicators — the **[[accumulation-distribution|Accumulation/Distribution Line]]**, **[[chaikin-oscillator|Chaikin Oscillator]]**, **[[chaikin-money-flow|Chaikin Money Flow]]**, and **Chaikin Volatility** — and founder of **Chaikin Analytics**, whose 20-factor "Power Gauge" rating is a widely used retail quantamental stock-screening tool. His central insight — that *where a price closes within its bar's range, weighted by [[volume]], reveals hidden institutional accumulation or distribution* — turned [[money-flow|money-flow analysis]] into a standard layer of [[technical-analysis-overview|technical analysis]]. His indicators ship as defaults on essentially every modern charting platform.

## Key Facts

| | |
|---|---|
| **Name** | Marc Chaikin |
| **Born** | c. 1943, United States |
| **Known for** | [[chaikin-money-flow\|Chaikin Money Flow]], [[chaikin-oscillator\|Chaikin Oscillator]], [[accumulation-distribution\|Accumulation/Distribution Line]], Chaikin Volatility |
| **Career start** | 1966 (stockbroker) |
| **Major roles** | SVP, Drexel Burnham Lambert; founder of Bomar Securities; head of Instinet Research quant group |
| **Firm founded** | Chaikin Stock Research (2008) → Chaikin Analytics (2011) |
| **Flagship product** | Power Gauge — 20-factor "quantamental" stock rating |
| **Acquired by** | MarketWise (Stansberry/MarketWise parent), 2021 |
| **Lineage** | Refined [[joseph-granville\|Granville]]'s [[on-balance-volume\|OBV]] and [[larry-williams\|Williams]]' accumulation work |
| **Domain** | stocks, [[indicators]], [[volume]]-based [[money-flow]] analysis |

## Career

- **1966**: Began as a stockbroker; rose to senior vice president at Drexel Burnham Lambert, where he developed his volume-flow work for institutional clients.
- **Bomar Securities**: Founded and ran Bomar Securities LP, an early quantitative shop whose database covered 3,000+ stocks with multi-year price histories — sold to **Instinet** (a Reuters subsidiary) in the early 1990s.
- **Instinet**: Founded and managed Instinet Research's five-person quantitative equity research department and spearheaded the front end of Instinet's Research and Analytics workstation — one of the first real-time analytics platforms for institutional investors.
- **2008/2011**: Founded Chaikin Stock Research (2008), rebranded **Chaikin Analytics** in 2011.
- **2017**: Nasdaq launched co-branded Chaikin Power indexes based on the Power Gauge methodology.
- **2021**: Chaikin Analytics was acquired by MarketWise (the Stansberry Research parent), through which his *Power Gauge Report* newsletter is distributed. Chaikin, in his early 80s as of 2026, remains the firm's public face.

## Indicators

| Indicator | What it measures |
|---|---|
| **[[accumulation-distribution\|Accumulation/Distribution Line]]** (1970s–80s) | Cumulative volume weighted by where price closes within its daily range — refining [[joseph-granville]]'s [[on-balance-volume\|OBV]] and [[larry-williams]]'s earlier accumulation work |
| **[[chaikin-oscillator\|Chaikin Oscillator]]** | [[macd\|MACD]]-style difference of 3- and 10-period EMAs of the A/D Line — momentum of money flow |
| **[[chaikin-money-flow]]** | 20/21-period sum of A/D volume divided by total volume; oscillates around zero to flag institutional accumulation vs. distribution |
| **Chaikin Volatility** | Rate of change of the high-low range EMA |

### Mechanics: how the family is built

The whole Chaikin family stacks on one building block, the **Money Flow Multiplier**, which scores where the close sits inside the bar's range:

```
Money Flow Multiplier (MFM) = [(Close − Low) − (High − Close)] / (High − Low)
Money Flow Volume (MFV)     = MFM × Volume
```

The multiplier runs from +1 (close at the high — pure accumulation) to −1 (close at the low — pure distribution). From this:

- **[[accumulation-distribution|A/D Line]]** = running cumulative sum of Money Flow Volume. A rising A/D Line with rising price confirms the trend; a falling A/D Line under rising price is a bearish *divergence* (price up on weakening buying).
- **[[chaikin-oscillator|Chaikin Oscillator]]** = EMA(3) of A/D Line − EMA(10) of A/D Line. This applies the [[macd|MACD]] idea to money flow rather than to price, turning the slow-moving A/D Line into a faster zero-crossing momentum signal.
- **[[chaikin-money-flow|Chaikin Money Flow (CMF)]]** = Σ(Money Flow Volume, n) ÷ Σ(Volume, n), typically n = 20 or 21. Unlike the cumulative A/D Line, CMF is bounded and oscillates around zero: persistent readings above zero indicate accumulation, below zero distribution; the strength of the signal scales with how far it is from the zero line.
- **Chaikin Volatility** measures the rate of change of an EMA of the high−low range, flagging volatility expansion (often near tops) versus contraction.

Chaikin's important refinement over [[joseph-granville|Granville's]] [[on-balance-volume|OBV]] is that OBV assigns a *full* day's volume to the up/down direction based only on the close-to-close change, whereas Chaikin weights volume *continuously* by the intra-bar close location — a far more granular read on whether buyers or sellers controlled the session.

### Power Gauge
Chaikin Analytics' flagship: a **20-factor model** combining financials (value), earnings, technicals, and expert/sentiment factors into a bullish-to-bearish rating for 4,000+ US stocks and 1,700+ ETFs — an early example of packaged "quantamental" scoring for retail investors.

## Why Chaikin Matters to Traders

- His indicators formalized the idea that **where price closes within the bar's range, times volume,** reveals institutional buying/selling pressure that raw price can hide — the foundation of modern [[money-flow|money-flow analysis]].
- [[chaikin-money-flow|CMF]] and A/D-Line *divergences* against price are a standard confirmation filter in [[breakout]] and [[trend-following|trend]] systems: a [[breakout]] backed by a rising A/D Line is treated as higher-conviction than one on falling money flow.
- The Power Gauge illustrates the productization of multi-factor screening — useful as a benchmark for what a retail-grade [[factor-investing|factor]] model contains, blending value, growth, technical, and sentiment factors.

## Influence and Legacy

Chaikin sits in the direct lineage of [[volume]] analysts running from [[joseph-granville|Joseph Granville]] ([[on-balance-volume|OBV]], 1963) and [[larry-williams|Larry Williams]] through to himself, and his refinements are now the default money-flow tools on TradingView, MetaStock, Bloomberg, and most retail platforms. Where earlier pioneers built single indicators, Chaikin's second act — Bomar, Instinet's quant research desk, and finally Chaikin Analytics' Power Gauge — helped bring institutional-grade quantitative screening to individual investors decades before "quantamental" became a buzzword. The Nasdaq-listed Chaikin Power indexes (2017) extended his rating methodology into investable products.

## Related

- [[chaikin-money-flow]] — his most-used indicator
- [[chaikin-oscillator]] — the MACD-style momentum read of the A/D Line
- [[accumulation-distribution]] — the cumulative base indicator of the family
- [[on-balance-volume]], [[joseph-granville]] — the lineage CMF descends from
- [[money-flow]] — the analytical category his work defines
- [[volume]] — the raw input his indicators reinterpret
- [[macd]] — the construction the Chaikin Oscillator borrows
- [[larry-williams]] — parallel pioneer of accumulation/distribution concepts
- [[martin-pring]], [[john-bollinger]] — contemporary indicator creators

## Sources

- Chaikin Analytics, "Who We Are" — https://chaikinanalytics.com/whoweare
- Chaikin Analytics, "Chaikin Power Gauge" — https://chaikinanalytics.com/powergauge
- Meb Faber Research podcast #407, "Marc Chaikin — A Quantamental Approach to Investing" (April 2022) — https://mebfaber.com/2022/04/13/e407-marc-chaikin/
- CMT Association presenter profile — https://cmtassociation.org/presenter/marc-chaikin/
- [[2026-04-20-comprehensive-guide-technical-trading-indicators]] — Comprehensive Guide to Technical Trading Indicators (compiled research, 29 references)
- Web research verification, 2026-06-10
