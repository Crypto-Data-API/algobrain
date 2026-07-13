---
title: "George Lane"
type: entity
created: 2026-04-20
updated: 2026-06-21
status: excellent
tags: [person, technical-analysis, indicators, history]
entity_type: person
aliases: ["Lane", "George C. Lane"]
related: ["[[stochastic]]", "[[stochastic-oscillator]]", "[[rsi]]", "[[macd]]", "[[divergence]]", "[[momentum]]", "[[mean-reversion]]", "[[j-welles-wilder]]"]
---

# George Lane

George C. Lane (1921 – July 7, 2004) was an American securities trader, educator, and technical analyst who popularised the [[stochastic-oscillator|Stochastic Oscillator]] (%K, %D) in the 1950s–1970s. The indicator compares the closing price to the recent price range to flag momentum exhaustion, and remains one of the most widely used oscillators for identifying overbought/oversold conditions (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]).

## Key Facts

| Field | Detail |
|-------|--------|
| Full name | George C. Lane |
| Born | 1921 |
| Died | July 7, 2004 (aged 83) |
| Nationality | American |
| Early firm | E.F. Hutton & Co. (early 1950s) |
| Career hub | Chicago futures community |
| Known for | Popularising the **[[stochastic-oscillator\|Stochastic Oscillator]]** (%K / %D) |
| Education company | President, **Investment Educators Inc.** (Watseka, Illinois) |
| Signature teaching | *"Momentum changes direction before price"* |
| Primary signal | [[divergence\|Divergence]] between oscillator and price |

## Who He Was and His Era

Lane's career in the markets spanned more than 50 years, beginning at **E.F. Hutton & Co.** in the early 1950s before he moved into the Chicago futures community — the world capital of commodity and index-futures trading. He worked in the era when [[technical-analysis]] was transitioning from hand-drawn chart reading into the systematic, formula-based oscillators that now dominate trading screens, the same generation that produced J. Welles Wilder's [[rsi|RSI]] and Donald Lambert's [[cci|CCI]].

He served as president of **Investment Educators Inc.** (Watseka, Illinois), teaching basic and advanced technical analysis to retail and professional traders, and ran seminars worldwide for decades. More than the inventor, Lane became the **lifelong evangelist** for stochastics — the reason his name is attached to it ("Lane's stochastics") in every charting package. He died on **July 7, 2004**, aged 83.

## What He Is Known For: The Stochastic Oscillator

Lane was part of a group of Chicago futures traders who developed the stochastic oscillator in the late 1950s, and he became the figure who refined, taught, and championed it for the rest of his life. The indicator is built on a single observation: **in an uptrend, closes tend to cluster near the top of each period's range; in a downtrend, near the bottom.** When that relationship breaks down, momentum is fading.

### The %K / %D Formula

Over a chosen lookback period (default **14**):

- **%K = 100 × (Close − Lowest Low) / (Highest High − Lowest Low)**

  where Lowest Low and Highest High are taken over the lookback period. %K therefore expresses *where the latest close sits within the recent high-low range*, scaled 0–100.

- **%D = a 3-period moving average of %K** — the smoothed "signal" line.

Standard readings: **above 80 = overbought, below 20 = oversold**. The "fast" stochastic plots raw %K and its 3-period %D; the "slow" stochastic smooths %K once more before computing %D, reducing whipsaw; the "full" stochastic exposes both smoothing parameters for tuning.

### Lane's Real Emphasis: Divergence, Not the 80/20 Lines

Critically, Lane himself emphasised **[[divergence]]** between the oscillator and price as the *primary* signal — not the overbought/oversold levels that most retail traders fixate on. A **bearish divergence** (price makes a higher high while %K makes a lower high) warns of an exhausting uptrend; a **bullish divergence** (price lower low, %K higher low) warns of an exhausting downtrend. His most-quoted teaching — ***"Momentum changes direction before price"*** — is the rationale for trading these %K/%D divergences rather than waiting for price confirmation.

## How Traders Use It

- Stochastics remain a **default oscillator in every charting platform** (TradingView, MetaTrader, Bloomberg) and a standard component of [[mean-reversion]] entry filters in equities, FX, and crypto.
- The **%K crossing %D** inside an extreme zone (e.g. a bullish cross below 20) is a common timing trigger.
- **Divergence-first** signals follow Lane's own methodology and are treated as leading rather than lagging.

## Influence and Legacy

Lane's divergence-first methodology anticipated the modern use of momentum non-confirmation as a **leading** signal — the same logic later applied to [[rsi|RSI]] and [[macd|MACD]] divergences. The fast/slow/full stochastic variants and the popular **StochRSI** hybrid (which applies the stochastic formula to RSI values rather than to price) all descend from his %K/%D framework. Through decades of seminars and his association with Investment Educators Inc., Lane probably taught the mechanics of stochastics to more working traders than any other single figure, cementing it as one of the three or four oscillators every charting platform ships by default.

## Related

- [[stochastic-oscillator]] / [[stochastic]] — the indicator Lane popularised
- [[rsi]] — companion momentum oscillator (Wilder)
- [[macd]] — companion divergence tool (Appel)
- [[divergence]] — Lane's primary signal
- [[momentum]] — the concept underlying his core teaching
- [[mean-reversion]] — the dominant modern application
- [[j-welles-wilder]] — contemporary indicator pioneer

## Sources

- [[2026-04-20-comprehensive-guide-technical-trading-indicators]] — Comprehensive Guide to Technical Trading Indicators (compiled research, 29 references)
- Wikipedia: https://en.wikipedia.org/wiki/George_Lane_(technical_analyst)
- CMT Association, "Origins of the Stochastic Oscillator": https://www.mta.org/kb/origins-of-the-stochastic-oscillator-article/
- Lane, G. C. (1984). "Lane's Stochastics." *Technical Analysis of Stocks & Commodities*, 2(3).
- Verified via web search, 2026-06-10.
