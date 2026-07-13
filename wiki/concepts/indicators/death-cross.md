---
title: "Death Cross"
type: concept
created: 2026-04-15
updated: 2026-06-21
status: excellent
tags: [indicators, technical-analysis, trend-following]
aliases: ["Death Cross"]
domain: [technical-analysis]
prerequisites: ["[[moving-averages]]"]
difficulty: beginner
related: ["[[golden-cross]]", "[[moving-averages]]", "[[trend-following]]", "[[support-resistance]]", "[[200-day-moving-average]]", "[[volume]]"]
---

A **death cross** occurs when a shorter-term [[moving-averages|moving average]] — most commonly the 50-day simple moving average — crosses *below* a longer-term moving average, typically the [[200-day-moving-average|200-day SMA]], signalling a potential shift from a bullish to a bearish trend. It is the mirror image of the [[golden-cross]], which marks the shorter average crossing above the longer one and is read as bullish. The death cross is one of the most widely cited signals in [[technical-analysis]], precisely because it is simple, mechanical, and visible on any chart.

## How It Works

The signal triggers on the crossover itself:

```
Death Cross: SMA(50) crosses below SMA(200)
Golden Cross: SMA(50) crosses above SMA(200)
```

The 50-day average reflects the intermediate-term trend; the 200-day reflects the long-term, "is-this-a-bull-or-bear-market" trend. When the intermediate trend turns down hard enough to drag the 50-day beneath the 200-day, it is read as the short-term weakness having metastasised into a genuine long-term regime change.

Because both averages are derived from past prices, the death cross is a **lagging** indicator. The 50-day average only falls beneath the 200-day after weeks of declining prices, so by the time the cross prints, a substantial portion of the down move has usually already happened. Its value is less in timing a top than in *confirming* that a meaningful trend change has occurred rather than a temporary pullback. Some practitioners use [[exponential-moving-average|exponential moving averages]] for a faster (but noisier) version of the signal, or alternative pairs (e.g. 20/50, 100/200) for faster or slower timeframes.

### Variations of the crossover

| Pair (short / long) | Speed | Typical use |
|---------------------|-------|-------------|
| 50 / 200 SMA | Slow, canonical | The "classic" death cross watched by media and institutions |
| 50 / 200 EMA | Slightly faster | Reacts sooner; more whipsaws |
| 20 / 50 | Fast | Swing trading, intermediate trend shifts |
| 100 / 200 | Slowest | Position trading, filtering out most noise |

## Worked Example

Imagine a stock that rallied through the year, peaked, and rolled over:

- 200-day SMA sits at **$100** and has just begun to flatten.
- 50-day SMA, which had been well above it at $115, has been falling for weeks as price declined.
- On the crossover day the 50-day prints **$99.80**, dipping just below the 200-day at **$100.10**.

That crossover is the death cross. Note what it does *not* tell you: the actual high might have been $130 two months earlier, so the signal arrives roughly 25% below the top. A trader using it as a regime filter would now treat the stock as "below a flattening/falling 200-day" and reduce long exposure — not sell the absolute peak (which the signal structurally cannot catch).

## Lag, Whipsaws, and False Signals

The death cross's reliability is regime-dependent:

- **In trending markets it can be a useful confirmation.** When a real bear market is underway, the cross confirms the regime and keeps a trend follower out of further downside. The cost is that the entry is late.
- **In choppy, range-bound markets it whipsaws.** When price oscillates sideways, the 50- and 200-day averages cross back and forth repeatedly, producing death crosses that quickly reverse into golden crosses and vice versa. Each round trip is a losing trade for anyone shorting the cross mechanically.
- **It is a coincident-to-lagging confirmation, not a forecast.** Because it requires weeks of prior decline, it can fire *near* a bottom just as much as near further downside — the worst case being a death cross that prints right before a sharp recovery.

Historically the signal has had a mixed record: it has at times preceded major bear markets, and at other times it has fired late in a selloff just before a rebound. The honest summary is that the death cross is better understood as a *description of a trend that has already turned* than as a predictive timing tool.

## How Traders Use This

Traders rarely treat the death cross as a standalone short trigger. Common refinements:

- **Confirm the slope, not just the cross.** Require the 200-day average to itself be turning down (a falling long-term trend) rather than merely being pierced by a dipping 50-day in an otherwise rising market.
- **Demand [[volume]] confirmation.** Expanding [[volume]] on the crossover suggests real distribution rather than a thin, holiday-week drift.
- **Combine with structure.** Pair the cross with a break of [[support-resistance|support]] or a lower-high/lower-low sequence ([[dow-theory]]) for confluence.
- **Use it as a regime filter, not an entry.** Many systematic traders simply reduce long exposure, tighten stops, or switch to [[defensive-sectors|defensive]] positioning while price trades below a falling 200-day average — and re-risk when a [[golden-cross]] reverses it.
- **Mind reflexivity.** Because the cross is so widely reported for the [[sp500|S&P 500]] and major large-caps, it carries a degree of self-fulfilling influence as institutions de-risk around the headline.

## Common Pitfalls

- **Selling the bottom.** The biggest risk is shorting (or panic-selling) a death cross that fires after the decline is largely over, only to be stopped out by a V-shaped recovery.
- **Mechanical use in ranges.** Trading every cross in a sideways market guarantees a string of whipsaw losses.
- **Ignoring the underlying.** A death cross on a high-[[beta]], thin-volume small-cap is far noisier than one on a broad index.
- **Treating it as precise.** It is a coarse trend gauge, not an entry signal; pairing it with [[risk-management|risk management]] and a stop is essential.

## Sources

- Murphy, John J. *Technical Analysis of the Financial Markets.* New York Institute of Finance, 1999.
- Fidelity Investments, "Golden cross and death cross" (technical indicators reference).
- Investopedia, "Death Cross" definition and historical examples.

## Related

- [[golden-cross]] — the bullish inverse signal
- [[moving-averages]] — the underlying construction
- [[200-day-moving-average]] — the long-term average most often used
- [[trend-following]] — the broader style the signal serves
