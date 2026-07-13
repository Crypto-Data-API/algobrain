---
title: "January Effect"
type: concept
created: 2026-04-11
updated: 2026-07-01
status: excellent
tags: [anomalies, stocks, mean-reversion]
aliases: ["Turn-of-Year Effect", "January Small-Cap Premium", "January Effect"]
domain: [anomalies]
prerequisites: ["[[anomalies-overview]]", "[[size-anomaly]]"]
difficulty: beginner
related: ["[[anomalies-overview]]", "[[calendar-effects-anomalies]]", "[[size-anomaly]]"]
---

# January Effect

The January effect is the historical tendency for small-cap stocks to earn disproportionately high returns in January — specifically in the first 5-10 trading days — relative to other months. At its peak in the 1926-1980 sample, roughly half of the entire small-cap size premium was earned in January alone. It is one of the most-studied and most-decayed of the classical calendar anomalies.

## What

In the post-WWII US sample studied by Keim (1983), the equal-weighted return of the smallest-decile stocks in January averaged roughly 7% per month — compared to ~1% per month in the other eleven months combined. The effect was concentrated in the last trading day of December and the first five trading days of January.

## Original Paper

Keim, D. (1983) "Size-Related Anomalies and Stock Return Seasonality: Further Empirical Evidence" — *Journal of Financial Economics*. Earlier hints in Rozeff & Kinney (1976).

## Mechanism

Three complementary explanations:

- **Tax-loss selling** — US investors sell losers in December to realize capital losses, depressing the prices of already-beaten-down (often small-cap) names. They reinvest the cash in early January, lifting prices.
- **Window dressing** — institutional investors sell losers before year-end reporting so their holdings look respectable; they repurchase in January.
- **Portfolio rebalancing** — new-year rebalancing and bonus money being put to work concentrates buying flow in early January.

The tax-loss mechanism is the strongest candidate because the effect is weaker in non-US markets with different tax years, and stronger in stocks that have underperformed in the prior year.

## Edge Category

**Behavioral** and **structural** (tax-driven flows). See [[edge-taxonomy]].

## Replication Status

Replicated in pre-1990 data. Post-1990 the effect has shrunk substantially in US large-caps and is effectively gone in US mid-caps. It persists weakly in micro-caps and in some international markets with different tax regimes.

## Decay History

One of the best examples of anomaly decay after publication. Pre-Keim (1976-1981): ~7%+ in January. Post-1990: ~2%. Post-2000: statistically indistinguishable from zero in most subsamples, though still measurable in micro-caps.

## Current Viability

Not a standalone strategy. Potentially a weak overlay on small-cap or micro-cap exposure — tilt more into beaten-down names in late December, take profits in mid-January. The magnitude is too small to pay transaction costs as a standalone trade.

## Worked Example (hypothetical)

The numbers below are an illustration of the *tax-loss mechanism*, not a real backtest.

Imagine a small-cap stock that fell from $20 to $12 over the course of a year. In December:

- Investors holding it at a loss sell to "harvest" the capital loss before year-end — they can use the realised loss to offset gains elsewhere on their tax return.
- This tax-motivated selling pushes the price down further, say to $11, even though nothing about the business has changed.
- In early January the tax incentive is gone, the selling pressure lifts, and some of those investors **buy back** in. Price rebounds toward $12-13.

A trader trying to exploit this might tilt into a basket of beaten-down small-caps in late December and trim in mid-January. Note the catch: the entire round-trip might capture only a couple of percent, and small-caps carry wide [[bid-ask-spread|bid-ask spreads]] and real [[transaction-costs]] — which is exactly why the edge is hard to monetise net of costs today.

## Limitations and FAQ

- **Is the January effect still tradeable?** Largely no. As the [[#Decay History|decay history]] shows, the premium has compressed to near zero in liquid US stocks since publication. Markets adapt: once traders front-run the effect by buying in December, the abnormal return migrates earlier and shrinks.
- **Why does it survive at all in micro-caps?** Micro-caps are costly to short and hard to arbitrage, so the [[limits-to-arbitrage]] keep a faint residual effect alive where transaction costs exceed the premium.
- **Is it the same as the "Santa Claus rally"?** No. The Santa Claus rally refers to the last week of December plus the first two trading days of January for the broad market; the January effect is specifically a *small-cap* size phenomenon driven by tax-loss flows.
- **Does it work outside the US?** Weakly and inconsistently. Countries whose tax year does not end in December show different (or absent) seasonality, which is itself the strongest evidence for the tax-loss-selling explanation.
- **Survivorship and data-mining caveat:** with twelve months to choose from, some month will look special by chance. The January effect is more credible than most calendar anomalies because it has a clear economic mechanism, but its post-publication collapse is a textbook example of [[anomaly-decay]].

## Related Strategies

- [[size-anomaly]] — half of its historical premium was the January effect
- [[turn-of-month-effect]] — related calendar concentration
- [[calendar-effects-anomalies]] — broader overview
- [[tax-loss-harvesting]] — the flow that drives the effect

## Sources

- Rozeff & Kinney (1976) — precursor
- Keim (1983) — the canonical reference
- Reinganum (1983) — tax-loss-selling interpretation
- Easterday, Sen, Stephan (2009) — modern decay analysis

## Related

- [[anomalies-overview]]
- [[calendar-effects-anomalies]]
- [[size-anomaly]]
- [[turn-of-month-effect]]
