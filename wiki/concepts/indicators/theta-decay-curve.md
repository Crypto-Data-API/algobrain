---
title: "Theta Decay Curve"
type: concept
created: 2026-05-07
updated: 2026-06-11
status: good
tags: [options, indicators, theta, derivatives, time-decay]
aliases: ["Decay Curve", "Theta Curve", "Time Decay Curve", "Theta vs DTE"]
related: ["[[theta]]", "[[theta-targeting]]", "[[time-to-expiration]]", "[[gamma-explosion]]", "[[gamma-to-theta-ratio]]", "[[theta-realisation-ratio]]", "[[vega-budgeting]]", "[[options-portfolio-construction]]", "[[expiration-laddering]]", "[[managing-winners]]", "[[black-scholes-model]]", "[[implied-volatility]]", "[[zero-dte-options]]"]
domain: [indicators, risk-management]
prerequisites: ["[[theta]]", "[[time-to-expiration]]", "[[options-greeks]]"]
difficulty: intermediate
---

The **theta decay curve** is the plot of an option's [[theta]] (or, equivalently, its remaining extrinsic value) against [[time-to-expiration|time-to-expiration]]. Its canonical shape — gently sloped for months, then bending sharply downward in the final weeks and turning near-vertical in the last few days — is the central visual that drives strike selection, [[expiration-laddering]] decisions, and the timing of [[managing-winners|profit-take]] rules in any [[theta-targeting|theta-targeted]] book. The curve is universal across [[options]] markets, but its precise shape depends critically on moneyness: ATM, OTM, and ITM options have noticeably different decay profiles, and confusing the three is one of the most common errors in retail options trading.

## Overview

A long option's value is a sum of intrinsic value (`max(S − K, 0)` for calls) and extrinsic (time + volatility) value. Theta is the rate at which extrinsic value bleeds out per unit of time. Plot extrinsic value on the y-axis and DTE on the x-axis, and you get the **decay curve**. Plot theta itself (the slope) on the y-axis and you get the *derivative* of the curve.

Three properties of the curve dominate practical use:

1. **Convexity in DTE** — the curve is *not* a straight line. Decay accelerates as expiration approaches.
2. **Hockey-stick shape near expiry** — the last 7-14 days are where the curve bends most violently, especially for ATM options.
3. **Moneyness-dependent shape** — ATM options have the steepest acceleration; deep-ITM and deep-OTM options have flatter, more linear curves with smaller absolute theta.

The curve is the dual of the [[gamma-explosion]]. Theta and gamma share the `1/√t` scaling for ATM options, so wherever the theta curve bends down sharply, the gamma curve is bending up by an equal-and-opposite amount. A trader staring at the theta side of the chart and ignoring the gamma side is looking at half the picture; see [[gamma-to-theta-ratio]].

## Definition / Formula

For an ATM option in the [[black-scholes-model|Black-Scholes]] framework, the canonical approximations are:

```
Extrinsic value (ATM)  ≈  0.4 · S · σ · √t
Theta (per calendar day, ATM) ≈ −0.4 · S · σ / (2 √t · Y)
                              =  −(extrinsic value) / (2 · t · Y)
```

where `S` is spot, `σ` is annualised IV, `t` is year-fraction-to-expiry, and `Y` is the day-count basis (365 calendar / 252 trading). The key observations:

- **Extrinsic value scales as √t.** Doubling DTE only multiplies premium by √2 ≈ 1.41, not 2. This is why selling 90-DTE premium is *not* twice as good as selling 45-DTE premium — it's only ~1.4x as much credit, with significantly more vega risk per dollar.
- **Theta scales as 1/√t.** Halving DTE roughly multiplies theta by √2. Front-week theta is 3-4x back-month theta in $/day terms.
- **Theta over the holding period is the integral.** A position held from 45 DTE to 21 DTE accumulates the area under the theta curve between those two points — about 30% of the option's original extrinsic value, even though the holding period is only about half the original DTE.

For non-ATM options, the curve flattens. Deep-OTM options have a small absolute theta that decays roughly linearly until they go effectively bid-less. Deep-ITM options behave like the underlying minus a small extrinsic shell that decays away over the last 30 DTE.

### Discontinuities — weekends, holidays, half-days

The mathematical curve is smooth, but the realised curve is not. Markets are closed on weekends and holidays, and pricing models handle the gap in three different ways:

- **Continuous-time model**: theta accrues at the calendar-day rate over Friday close → Monday open. Position appears to lose 3 days of value over a weekend.
- **Trading-day model**: no decay over weekends; Monday morning premium equals Friday close premium absent any move or IV change.
- **Hybrid (most platforms)**: dealers begin marking down extrinsic on Friday afternoon — a phenomenon known as **weekend decay anticipation** — so the realised Friday-close-to-Monday-open theta is typically **1.5-2x a normal session**, not 3x. See [[weekend-effect]].

Around major holidays (Thanksgiving, Christmas, Good Friday, July 4) the same compression occurs, plus an [[implied-volatility|IV]] drop into the long weekend that further deflates premium independent of pure time decay. The *visual* effect is small steps in the decay curve at weekend boundaries rather than a smooth slope.

## Why It Matters (for theta-targeted books)

The shape of the decay curve dictates almost every operational decision in a short-premium book.

### 1. The "hockey stick" defines the manage-and-roll cadence

The standard tastytrade-style cadence — open at 45 DTE, close or roll at 21 DTE — is a direct consequence of the curve. Between 45 DTE and 21 DTE a position captures roughly 40-50% of the original extrinsic value at relatively manageable [[gamma]]. Between 21 DTE and 0 DTE the remaining 50% is captured but [[gamma]] roughly doubles, and so does the [[gamma-to-theta-ratio|gamma-to-theta ratio]]. For a fixed expected return, the second half of the curve carries materially more variance.

The [[managing-winners|50% profit-take rule]] (close when 50% of credit is captured) is the same idea expressed in P&L space: lock in the smooth portion of the curve, let someone else stand for the hockey stick.

### 2. Curve shape drives DTE bucket selection

[[expiration-laddering]] across DTE buckets is in part an attempt to **smooth the aggregate decay curve** by stacking positions whose individual curves are at different points on their hockey sticks. A book that holds positions at 7 / 21 / 45 / 90 DTE has cumulative theta that grows at a near-linear rate as the calendar advances, even though each individual position's theta curve is highly non-linear.

### 3. Curve shape governs the optimal time of week to trade

Front-week (0-7 DTE) options have most of their decay concentrated in two days: Thursday and the Friday morning. Back-month options decay roughly proportionally each session. This is why short-dated strategies tend to entry on Mondays/Tuesdays (capture the steepest segment) and longer-dated strategies are indifferent to the day of week.

### 4. Curve shape interacts with [[implied-volatility|IV]] regime

A change in IV reprices the whole curve vertically. In a higher-IV regime, every point on the curve is taller (more extrinsic, larger theta), but the *shape* is preserved. The implication: a 45-DTE position in a 22-VIX regime has the same proportional decay profile as a 45-DTE position in a 12-VIX regime, just larger in absolute dollar terms. This is what makes IV-regime-relative position sizing so important — see [[volatility-regime]].

## Worked Example

Take the 45-DTE SPX [[iron-condor]] from the [[theta-targeting]] worked example: SPX at 5,000, VIX at 16, short 16-delta strikes at ~4,800 / ~5,200, long wings 50 points wider. The four short strikes together produce a per-contract decay curve of approximately:

| DTE | Extrinsic value ($) | Theta ($/day) | Δ extrinsic over next 7 days |
|---|---|---|---|
| 60 | 8.40 | 9 | 0.95 |
| 45 | 6.50 | 13 | 1.40 |
| 30 | 4.40 | 17 | 1.80 |
| 21 | 2.90 | 22 | 1.65 |
| 14 | 2.00 | 28 | 1.50 |
| 7 | 0.80 | 45 | 0.80 |
| 3 | 0.30 | 90 | 0.30 |
| 1 | 0.10 | 110 | — |
| 0 | 0 | — | — |

Plotting extrinsic value against DTE produces the canonical curve: a gentle slope from 60 to 30 DTE, a clear acceleration from 30 to 14, and a hockey-stick collapse from 7 to 0. Plotting theta against DTE produces the inverse: roughly flat from 60 to 30, rising sharply from 30 to 7, then near-vertical.

Note the asymmetry in *captured* decay over equal-length windows:

- 60 → 45 DTE (15 days): captures $1.90 ≈ 23% of original extrinsic.
- 45 → 21 DTE (24 days): captures $3.60 ≈ 43%.
- 21 → 0 DTE (21 days): captures the remaining $2.90 ≈ 35%.

The 45 → 21 window provides the best ratio of captured decay to elapsed time. The 21 → 0 window provides almost as much absolute decay but in a much riskier gamma regime — see [[theta-realisation-ratio]] for why the *realised* P&L on the last segment is typically far below the theoretical $2.90.

## Common Misuse / Pitfalls

- **Drawing one curve and assuming it applies to all moneynesses.** ATM options have the steepest hockey stick. A 5-delta short put has a nearly linear decay curve and a fraction of the theta — in absolute dollar terms — of an ATM short put. Selling 5-deltas to "harvest the steep part of the decay curve" misunderstands what the curve actually looks like for that strike.
- **Treating the curve as deterministic.** The curve assumes constant IV. A 30-DTE option in a 15-VIX environment that compresses to a 12-VIX environment over a week loses extrinsic value much faster than the curve predicts (vega P&L), and the trader who books this as "theta capture" is flattering their realisation ratio.
- **Ignoring weekend steps.** Backtests run on closing prices systematically attribute weekend decay to the Friday session, distorting any analysis of intraday theta capture.
- **Confusing the curve with the [[gamma-explosion]] curve.** They are duals, but they are *different curves*. The theta curve bends downward; the gamma curve bends upward. The trader who says "I love the steep part of the decay curve" is also saying "I love the steep part of the gamma curve." Whether that's a good thing depends on size and structure.
- **Generalising the index curve to single names.** Single-name decay curves have catalysts (earnings, FDA dates, FOMC) embedded in them. The curve has *kinks* at event dates that are not present in index curves.
- **Misreading the curve in [[zero-dte-options|0DTE]] products.** Same-day expirations have a curve that is essentially the last vertical inch of the standard curve, traversed in 6.5 hours. Theta numbers shown at the open are not what you collect by 4pm — most of it is consumed by gamma scalping. See [[gamma-explosion]] and [[theta-realisation-ratio]].

## Related

- [[theta]] — the rate the curve measures.
- [[theta-targeting]]#Theta Across DTE — direct connection to portfolio theta engineering.
- [[time-to-expiration]] — the x-axis variable.
- [[gamma-explosion]] — the dual curve on the gamma side.
- [[gamma-to-theta-ratio]] — what happens when you put the two curves into a ratio.
- [[theta-realisation-ratio]] — what fraction of the curve actually shows up as P&L.
- [[expiration-laddering]] — using multiple curves at different DTE to smooth aggregate theta.
- [[managing-winners]] — closing before the steepest gamma segment.
- [[options-portfolio-construction]] — book-level use of curve shape.
- [[vega-budgeting]] — vertical re-pricing of the curve when IV moves.
- [[implied-volatility]] — the parameter that sets the curve's height.
- [[weekend-effect]] — the discontinuities in the realised curve.
- [[zero-dte-options]] — the curve at the limit.

## Sources

- [[book-option-volatility-and-pricing]] — Natenberg, Chapter 8: theta as the negative slope of the value-vs-time curve, with the standard ATM `√t` derivation.
- Hull, *Options, Futures and Other Derivatives*, 10th ed., Chapter 19 — closed-form Black-Scholes theta and the moneyness-dependent shape of the decay curve.
