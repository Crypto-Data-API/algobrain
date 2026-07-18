---
title: "Holiday Effect"
type: concept
created: 2026-04-11
updated: 2026-06-11
status: good
tags: [anomalies, mean-reversion]
aliases: ["Pre-Holiday Effect", "Holiday Return Premium", "Holiday Effect"]
domain: [anomalies]
prerequisites: ["[[anomalies-overview]]", "[[calendar-effects-anomalies]]"]
difficulty: beginner
related: ["[[anomalies-overview]]", "[[calendar-effects-anomalies]]", "[[turn-of-month-effect]]"]
---

# Holiday Effect

The trading day immediately preceding a US market holiday has historically earned returns roughly 5x the normal daily average. Pre-holiday returns were strongly positive and statistically distinct from ordinary days in Ariel's (1990) sample, making the holiday effect one of the larger calendar anomalies. Unlike the [[weekend-effect]], it has held up better out-of-sample.

## What

Define a "pre-holiday" day as the trading day immediately before a market closure (Thanksgiving, Christmas, New Year, July 4, Labor Day, Memorial Day, MLK, President's Day, Good Friday). Compute the average return on these days and compare to average returns on all other days. In Ariel's 1963-1982 US sample, pre-holiday days averaged ~37 bps — roughly 14x the non-pre-holiday average.

## Original Paper

Ariel, R. (1990) "High Stock Returns Before Holidays: Existence and Evidence on Possible Causes" — *Journal of Finance*. Precursor: Fields (1934) in early data.

## Mechanism

- **Reluctance to be short over closed markets** — traders close short positions before extended closures to avoid gap risk, producing buying pressure
- **Optimism effect** — retail and institutional investors may exhibit holiday-related positive sentiment
- **Low volume, thin liquidity** — on the day before a holiday, order flow is dominated by residual buying pressure

The short-covering story is the strongest candidate because the effect is concentrated in the afternoon session of pre-holiday days, consistent with systematic position adjustments.

## Edge Category

**Structural** (short-covering flows) + **behavioral** (optimism).

## Replication Status

Replicated in most US samples through the 2000s and in many international markets. The magnitude has shrunk but the sign is consistent.

## Decay History

Moderate decay. Vergin & McGinnis (1999) showed the effect compressed after publication. Modern estimates put the pre-holiday premium at 10-15 bps rather than 30-40, but the sign has been consistent and it hasn't flipped or disappeared.

## Current Viability

Marginally tradeable as an overlay. The per-trade magnitude is too small for dedicated round-trip trading after costs. Useful as:

- A tilt: go slightly long-biased the day before holidays in an equity portfolio you already hold
- A feature in multi-factor intraday models
- An explanation for otherwise-puzzling calendar returns

## Related Strategies

- [[turn-of-month-effect]] — similar flow-driven mechanism
- [[calendar-effects-anomalies]] — broader family

## Sources

- Ariel (1990) "High Stock Returns Before Holidays" — *Journal of Finance*
- Lakonishok & Smidt (1988) "Are Seasonal Anomalies Real? A Ninety-Year Perspective"
- Vergin & McGinnis (1999) on post-publication decay

## Related

- [[anomalies-overview]]
- [[calendar-effects-anomalies]]
- [[turn-of-month-effect]]
