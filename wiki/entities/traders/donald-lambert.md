---
title: "Donald Lambert"
type: entity
created: 2026-04-20
updated: 2026-06-21
status: excellent
tags: [person, technical-analysis, indicators, commodities, history]
entity_type: person
aliases: ["Lambert", "Donald R. Lambert"]
related: ["[[cci]]", "[[commodity-channel-index]]", "[[chester-keltner]]", "[[rsi]]", "[[stochastic-oscillator]]", "[[mean-reversion]]", "[[momentum]]", "[[divergence]]"]
---

Donald R. Lambert was an American mathematician and technical analyst who created the [[cci|Commodity Channel Index (CCI)]], one of the most widely used oscillators in technical analysis. He introduced the indicator in the October 1980 issue of *Commodities* magazine (now *Futures*) in the article "Commodity Channel Index: Tool for Trading Cyclic Trends" (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]; StockCharts ChartSchool).

## Key Facts

| Field | Detail |
|-------|--------|
| Full name | Donald R. Lambert |
| Nationality | American |
| Profession | Mathematician / technical analyst |
| Known for | Inventor of the **[[cci\|Commodity Channel Index (CCI)]]** |
| Seminal publication | "Commodity Channel Index: Tool for Trading Cyclic Trends," *Commodities* magazine, **October 1980** |
| Listed location (1980 reprint) | Cedar Falls, Iowa, USA |
| Original market focus | Commodity / futures cyclical trends |
| Indicator family | Standardized-deviation oscillator (statistical z-score analogue) |
| Default lookback | 20 periods (Lambert: choose < 1/3 of the cycle length) |
| Scaling constant | 0.015 (chosen so ~70–80% of values fall in ±100) |

## Who He Was and His Era

Lambert was active during the explosion of systematic [[technical-analysis]] in the late 1970s and early 1980s — the same window that produced J. Welles Wilder's [[rsi|RSI]] and Average True Range (both 1978) and the broad popularization of George Lane's [[stochastic-oscillator]]. He is consistently described in the technical-analysis literature as a **mathematician** rather than a professional floor trader, which shows in the design of his indicator: the CCI is built on a clean statistical foundation rather than chart-pattern intuition.

Little else is publicly documented about Lambert's biography. The reprint of his original article lists his address at the time as **Cedar Falls, Iowa**, and his legacy rests almost entirely on the single 1980 article — an unusually high impact-to-output ratio in the indicator canon. He belongs to the small group of authors (alongside [[chester-keltner|Chester Keltner]] and Wilder) whose names became permanently attached to a tool that outlived their public profile.

## What He Is Known For: The Commodity Channel Index

Lambert designed the CCI to identify **cyclical turning points** in commodity markets. Conceptually it is a "standard score" from statistics: it measures how far the current typical price has deviated from its own moving average, scaled so the result is comparable across instruments and timeframes.

### The CCI Formula

The CCI is computed in four steps over a chosen lookback period *N*:

1. **Typical Price (TP)** = (High + Low + Close) / 3
2. **SMA of TP** = the *N*-period simple moving average of the Typical Price
3. **Mean Absolute Deviation (MAD)** = the average of |TP − SMA(TP)| over the *N* periods
4. **CCI** = (TP − SMA(TP)) / (**0.015** × MAD)

The constant **0.015** is the key design choice. Lambert selected it deliberately so that roughly **70–80% of CCI readings fall between −100 and +100**, making readings beyond those bounds statistically notable. Because the divisor is mean absolute deviation (not standard deviation), the CCI is a *robust* z-score variant — less sensitive to outliers than a textbook standardized score.

Lambert's original use was explicitly **cyclical**. He emphasized that the CCI does **not** determine cycle lengths itself; the trader must select the lookback period to match the seasonal or cyclical contract being traded, suggesting a lookback of **less than one-third of the cycle length** so the indicator turns in time to catch the cyclical reversal.

## How Traders Use It Today

Though built for commodities, the CCI is now applied across all asset classes — equities, FX, and crypto:

- **Overbought/oversold** — readings beyond +100 / −100 (or +200 / −200 for stricter signals) flag stretched prices, a [[mean-reversion]] application Lambert did not originally emphasize.
- **Trend confirmation** — sustained CCI above +100 is used as a [[momentum]]/trend filter, the closer analogue to Lambert's cyclical-turn intent: a move from below −100 up through zero, or a thrust above +100, is read as a new trend beginning.
- **Zero-line crossings** — crossing above/below zero is used as a simpler trend-bias trigger.
- **[[divergence]]** — CCI/price divergences are a standard reversal-warning technique, paralleling [[rsi|RSI]] and [[stochastic-oscillator|stochastic]] usage.
- It is available by default on essentially every charting platform, making it one of the most-deployed legacy indicators alongside RSI and [[macd|MACD]].

## Influence and Legacy

The CCI sits in the small canon of unbounded, deviation-based oscillators and is frequently taught alongside [[chester-keltner|Keltner Channels]] (which also use a deviation-from-average band) and Bollinger Bands as statistical envelopes around price. Its survival on every modern platform — TradingView, MetaTrader, Bloomberg, ThinkorSwim — more than four decades after a single magazine article is a testament to the durability of a simple, well-grounded statistical idea. Lambert is the archetype of the "one great indicator" author: a mathematician whose lone published method became permanent infrastructure for [[technical-analysis|technical traders]].

## Related

- [[cci]] / [[commodity-channel-index]] — the indicator Lambert created
- [[chester-keltner]] — fellow commodity-indicator pioneer (deviation-band channels)
- [[rsi]] — contemporaneous oscillator (Wilder, 1978)
- [[stochastic-oscillator]] — comparable overbought/oversold tool
- [[mean-reversion]] — the dominant modern use of CCI
- [[momentum]] — the trend-confirmation use closer to Lambert's intent
- [[divergence]] — CCI/price non-confirmation as a reversal signal

## Sources

- Donald R. Lambert, "Commodity Channel Index: Tool for Trading Cyclic Trends," *Commodities* magazine, October 1980 (reprinted in *Technical Analysis of Stocks & Commodities* V.1:5, pp. 120–122) — https://store.traders.com/-v01-c05-comm-pdf.html
- StockCharts ChartSchool, "Commodity Channel Index (CCI)" — https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/commodity-channel-index-cci
- Wikipedia, "Commodity channel index" — https://en.wikipedia.org/wiki/Commodity_channel_index
- (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]) — Comprehensive Guide to Technical Trading Indicators (compiled research, 29 references)
- Verified via Perplexity + web search, 2026-06-10 (historical figure; biographical record is sparse — noted in text)
