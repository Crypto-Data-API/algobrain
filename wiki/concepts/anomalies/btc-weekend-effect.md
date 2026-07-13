---
title: "Bitcoin Weekend Effect"
type: concept
created: 2026-04-11
updated: 2026-06-11
status: good
tags: [anomalies, crypto, calendar-effects, seasonality]
aliases: ["Crypto Weekend Effect", "BTC Weekend Anomaly"]
domain: [anomalies]
difficulty: beginner
related: ["[[anomalies-overview]]", "[[weekend-effect]]", "[[calendar-effects-anomalies]]", "[[crypto-weekday-weekend-etf-era]]"]
---

# Bitcoin Weekend Effect

Bitcoin (and crypto more broadly) displays distinct day-of-week and weekend return patterns that differ from equity markets because crypto trades 24/7/365 with no formal weekend closure. The specific patterns have shifted over time — early samples (2013-2017) showed weak weekend positive bias, while later samples (2018-present) suggest weekend returns are approximately flat or slightly negative, with most directional activity concentrated during Asia-Europe overlap hours on weekdays.

> **Note:** post-2024, the weekend effect has evolved substantially with the launch of US spot Bitcoin ETFs. See [[crypto-weekday-weekend-etf-era]] for the modern treatment.

## What

Common measured patterns across samples:

- **Weekend liquidity thinness** — trading volumes on Saturdays and Sundays are typically 40-60% of weekday volumes. This thins out orderbooks and makes volatility more regime-dependent.
- **Weekend pump-and-dumps** — before institutional dominance, weekend liquidity vacuums were exploited for pump-and-dump schemes and short squeezes
- **Weekend vs. weekday mean returns** — small but inconsistent differences; the direction has varied across subsamples
- **"Friday night" effect** — heightened volatility in late Friday US hours as institutional market-makers reduce inventory going into the weekend

## Original Sources

Mostly practitioner research:

- Kaiko / Glassnode / Coin Metrics quarterly liquidity reports
- Hubrich, Aleph Research, Arthur Hayes' blog posts
- Academic coverage: Aharon & Qadan (2019) "Bitcoin and the Day-of-the-Week Effect" — *Finance Research Letters*

Academic consensus is thinner than for equity calendar effects because the sample is short and the market structure has changed rapidly.

## Mechanism

- **Institutional vs. retail mix** — weekends see disproportionate retail trading activity because institutions are off-market; this changes flow composition and volatility character
- **CME futures closure** — the CME bitcoin futures market closes Friday afternoon and opens Sunday evening, creating a "CME gap" that traders often point to as a source of predictable weekend price action
- **Liquidity provider risk aversion** — market-makers reduce inventory before the weekend to avoid being caught in gap-filling moves; this reduces depth and widens spreads
- **Asian trading session dominance** — weekend volumes skew more heavily to Asian retail than weekday volumes do

## Edge Category

**Structural / microstructure** — changes in liquidity composition produce predictable flow effects rather than a single information-based anomaly.

## Replication Status

Replication has been inconsistent across samples. Early-era findings have not cleanly held up in institutional-era data (post-2020). The *liquidity* patterns (thinner depth, wider spreads, different flow composition) are robust; the *directional* return patterns are noisier.

## Decay History

The weekend-pump-and-dump era largely ended with the 2022 FTX collapse and the subsequent withdrawal of small speculators. Modern crypto weekends are quieter and more mean-reverting than the 2017-2021 era.

## Current Viability

Mostly useful as:

- **A microstructure input** — widen market-making quotes on weekends to reflect thin liquidity
- **A tail-risk hedge** — avoid carrying large directional risk into weekends because liquidity cannot support unwind in a fast move
- **CME gap strategies** — trade the tendency for spot to "fill" CME gaps when the futures market reopens Sunday evening (mixed evidence, but frequently cited)

Not a standalone alpha source.

## Related Strategies

- [[weekend-effect]] — equity analog
- [[calendar-effects-anomalies]] — broader family
- CME gap-fill strategies (practitioner-level)

## Sources

- Aharon & Qadan (2019) "Bitcoin and the Day-of-the-Week Effect"
- Kaiko, Glassnode, Coin Metrics liquidity reports (industry-side)
- Caporale, Gil-Alana, Plastun (2019) "Is There a Day-of-the-Week Effect in Bitcoin?"

## Related

- [[anomalies-overview]]
- [[weekend-effect]]
- [[calendar-effects-anomalies]]
- [[crypto-momentum]]
