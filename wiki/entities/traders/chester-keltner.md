---
title: "Chester Keltner"
type: entity
created: 2026-04-20
updated: 2026-06-21
status: excellent
tags: [person, technical-analysis, indicators, commodities, history]
entity_type: person
aliases: ["Keltner", "Chester W. Keltner"]
related: ["[[keltner-channels]]", "[[bollinger-bands]]", "[[atr]]", "[[moving-averages]]", "[[linda-raschke]]"]
---

Chester W. Keltner (1909–1998) was an American grain trader and commodity market analyst, best known for the volatility envelope indicator that bears his name: [[keltner-channels|Keltner Channels]]. He introduced the concept in his 1960 book *How To Make Money in Commodities*, where he called it the "ten-day moving average trading rule" and made no claim to originality for the idea (Source: Wikipedia, "Keltner channel"; [[2026-04-20-comprehensive-guide-technical-trading-indicators]]).

## Key Facts

| Field | Detail |
|-------|--------|
| Full name | Chester W. Keltner |
| Born / Died | 1909 – 1998 |
| Nationality | American |
| Profession | Grain trader / commodity market analyst |
| Based | Kansas City, Missouri (statistical/advisory service founded 1939) |
| Known for | [[keltner-channels|Keltner Channels]] (volatility envelope) |
| Original name | "Ten-day moving average trading rule" |
| Key book | *How To Make Money in Commodities* (1960) |
| Original inputs | 10-day SMA of *typical price* ± 10-day SMA of the high–low range |
| Modern inputs | EMA ± multiple of [[average-true-range|ATR]] (Raschke revision) |
| Modernized by | [[linda-raschke|Linda Bradford Raschke]] (1980s) |

## Overview

Keltner built his career as a grain market analyst. He moved to Kansas City in 1939, where he founded a commodity-market statistical and advisory service, publishing market letters and statistical research for commodity traders; some references also describe him as a Chicago grain trader. His lasting contribution came from a single chapter of *How To Make Money in Commodities* (1960).

## The Method: Keltner Channels

### Original construction (Keltner, 1960)

Keltner's "ten-day moving average trading rule" built a band around a moving average of *typical price*, with band width driven by the recent trading range:

```
Typical Price (TP) = (High + Low + Close) / 3
Centerline         = SMA(TP, 10)                 # 10-day simple moving average of typical price
Range              = High − Low                  # the day's trading range
Band offset        = SMA(Range, 10)              # 10-day SMA of the daily high–low range
Upper Band         = Centerline + Band offset
Lower Band         = Centerline − Band offset
```

**Trading rule**: a *close above the upper band* was a buy (the trend is strengthening); a *close below the lower band* was a sell. Crucially, this is a **trend-following breakout** system — closes *outside* the channel are signals to go *with* the move — not a mean-reversion system that fades the extremes. Because everything reduces to a few moving averages of price and range, the rule could be computed by hand each evening, a hallmark of pre-computer technical analysis.

### Modern construction (Raschke / ATR version, 1980s)

In the 1980s, trader [[linda-raschke|Linda Bradford Raschke]] popularized a revised formulation that is what virtually every charting platform now labels "Keltner Channels":

```
Centerline  = EMA(Close, n)                      # typically n = 20 (exponential MA)
Upper Band  = EMA + (m × ATR(p))                 # typically m = 2, p = 10 (or 20)
Lower Band  = EMA − (m × ATR(p))
```

Two substitutions modernized the indicator: an **exponential moving average** replaced the simple one (more responsive to recent price), and the [[average-true-range|Average True Range (ATR)]] replaced the raw high–low range. ATR is itself an average of the **true range** — `max(High−Low, |High−PrevClose|, |Low−PrevClose|)` — so it accounts for overnight gaps that the simple high-minus-low range ignores, making the channel a cleaner volatility measure (Source: StockCharts ChartSchool).

## Trading Relevance

Keltner Channels remain a staple volatility envelope across all asset classes:

- **Trend identification**: sustained closes outside the channel signal strong trends (Keltner's original breakout use)
- **Squeeze setups**: the popular "TTM Squeeze" compares [[bollinger-bands|Bollinger Bands]] to Keltner Channels — Bollinger Bands contracting inside the Keltner Channel signals a volatility compression that often precedes a breakout
- **ATR-based channels** are smoother and less reactive to single-bar shocks than standard-deviation-based Bollinger Bands, making them preferred by some trend followers (see [[bollinger-bands-vs-keltner-channels]])

Keltner's work predates computerized technical analysis; his rule was simple enough to be computed daily by hand, an early example of a fully mechanical, rule-based trading system.

## Influence and Legacy

- **A founding volatility-envelope indicator**: alongside [[bollinger-bands|Bollinger Bands]] and the older percentage-envelope ideas, Keltner Channels are one of the canonical ways to wrap price in an adaptive band. Where [[john-bollinger|Bollinger]]'s bands key off [[standard-deviation|standard deviation]], Keltner's key off the trading range / [[average-true-range|ATR]] — the two are complementary, and comparing them is a standard exercise (see [[bollinger-bands-vs-keltner-channels]]).
- **Half of the "Squeeze"**: the widely used **TTM Squeeze** indicator is defined by the relationship between the two — when [[bollinger-bands|Bollinger Bands]] contract *inside* the Keltner Channel, the standard-deviation measure has fallen below the ATR measure, flagging extreme volatility compression that often precedes a breakout. Keltner's channel is therefore embedded in one of the most popular modern setups.
- **Modest creator, durable idea**: Keltner himself claimed no originality and treated the rule as one tool among many; yet because Raschke's ATR revision generalized it cleanly across asset classes, the indicator long outlived its commodity-grain origins and now appears on equities, futures, [[forex]], and crypto charts.
- **Early mechanical system**: by stating explicit, hand-computable entry/exit rules, Keltner contributed to the lineage of *systematic, rule-based* trading that later flourished with computers and [[backtesting]].

## Related

- [[keltner-channels]] — the indicator he originated
- [[bollinger-bands]] — the standard-deviation-based alternative
- [[john-bollinger]] — creator of the SD-based bands
- [[bollinger-bands-vs-keltner-channels]] — direct comparison
- [[average-true-range]] — used in the modern formulation
- [[atr]] — Average True Range
- [[standard-deviation]] — the basis of the Bollinger alternative
- [[moving-averages]] — the channel centerline
- [[linda-raschke]] — modernized the indicator in the 1980s
- [[technical-analysis]]
- [[volatility]]

## Sources

- Chester W. Keltner, *How To Make Money in Commodities* (The Keltner Statistical Service, 1960)
- Wikipedia, "Keltner channel" — https://en.wikipedia.org/wiki/Keltner_channel (confirms 1909–1998 dates, 1960 book, "ten-day moving average trading rule," Raschke revision)
- StockCharts ChartSchool, "Keltner Channels" — https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-overlays/keltner-channels
- (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]])
- Verified via Perplexity + web search, 2026-06-10
