---
title: "Time to Expiration (DTE)"
type: concept
created: 2026-05-07
updated: 2026-06-11
status: good
tags: [options, indicators, derivatives, theta, gamma]
aliases: ["DTE", "Days to Expiration", "Days to Expiry", "Time to Expiry", "T", "Tau"]
related: ["[[theta]]", "[[gamma]]", "[[vega]]", "[[implied-volatility]]", "[[theta-targeting]]", "[[theta-decay-curve]]", "[[gamma-explosion]]", "[[vega-budgeting]]", "[[options-portfolio-construction]]", "[[expiration-laddering]]", "[[zero-dte-options]]", "[[black-scholes-model]]", "[[managing-winners]]"]
domain: [indicators, risk-management]
prerequisites: ["[[options-greeks]]", "[[black-scholes-model]]"]
difficulty: intermediate
---

**Time to expiration (DTE)** is the number of days remaining until an [[options|option]] contract expires, and it is the single most important non-price input to every [[options-greeks|Greek]] in the [[black-scholes-model|Black-Scholes]] family. DTE is the variable that turns an option from a near-pure [[vega]] play (months out) into a near-pure [[gamma]] / [[theta]] play (hours out), and the entire engineering of a short-premium book — strike selection, [[expiration-laddering|laddering]], adjustment cadence — is structured around the DTE axis. Where [[vega-budgeting]] caps how much volatility risk the book carries and [[theta-targeting]] sets how much decay it harvests, DTE is the lever that controls *how* both numbers are produced.

## Overview

DTE has three closely related but distinct definitions used in practice:

1. **Calendar-day DTE** — raw number of calendar days until expiration. Dominant convention on most retail platforms ([[thinkorswim]], tastytrade, [[interactive-brokers|IBKR]]). A 45-DTE option opened on a Tuesday expires on a Thursday roughly six and a half weeks later.
2. **Trading-day DTE** — number of *trading sessions* remaining. Equals calendar DTE minus weekends and US market holidays. A "45 calendar-DTE" option is closer to **31 trading days** out.
3. **Year fraction (t or τ)** — DTE expressed as a fraction of the year, used inside pricing models. Convention varies: `t = DTE/365` (calendar-year basis) or `t = DTE/252` (business-year basis). [[orats|ORATS]], CBOE's VIX methodology, and most quant libraries default to a calendar-year basis with a small weekend "decay tax" baked in.

The choice matters. Black-Scholes uses a continuous time variable, but the market does not decay continuously over weekends — exchanges are closed. Different brokers, models, and analytics platforms make different compromises about weekend and holiday decay, which is why two screens may show meaningfully different theta numbers for the same option. See [[theta-decay-curve]] for the canonical shape and [[weekend-effect]] for the empirical evidence.

DTE differs from **maturity** in fixed income. A bond's "time to maturity" is purely calendar (semi-annual coupon dates aside), and the cash flows are deterministic. An option's DTE is the time remaining for a *probabilistic* payoff to crystallise, and the relationship between DTE and value is highly non-linear because the payoff is a max() function. A bond's price-vs-time curve is smooth; an option's value-vs-time curve has a kink at the strike at t=0 and steep curvature near it as t shrinks.

## Definition / Formula

For pricing purposes, define the time variable:

```
t  =  DTE / Y       where Y = 365 (calendar) or 252 (trading)
```

The Black-Scholes Greeks each have a characteristic dependence on `t`:

| Greek | Approximate scaling for ATM option | Behaviour as t → 0 |
|---|---|---|
| Delta (call) | `≈ 0.5 + small drift term` | Snaps to {0, 1} depending on moneyness |
| Gamma | `1 / (S σ √(2π t))` — i.e. **∝ 1/√t** | Diverges to infinity at the strike |
| Vega | `S √(t / 2π)` — i.e. **∝ √t** | Goes to zero |
| Theta (per calendar day) | `−S σ / (2 √(2π t)) · (1/Y)` | Diverges (large negative) |

Two consequences fall out of these scaling laws and are at the heart of every DTE-based risk decision:

- **Gamma × Theta is roughly invariant in t.** Multiplying `1/√t` by `1/√t` gives `1/t`, but in the dollar-PnL formulation theta and gamma combine such that an ATM short-premium position expects to break even when realised variance equals implied variance — independent of DTE in the idealised Black-Scholes world. See [[gamma-scalping]] and [[variance-risk-premium]].
- **The ratio Gamma / Theta scales as √t / t = 1/√t.** Front-week options have far more path risk per unit of decay than back-month options. This is the engine behind [[gamma-to-theta-ratio]] and the [[gamma-explosion]] near expiry.

For multi-leg structures, the *effective* DTE of the position is the DTE of the nearest expiry that is short. A [[calendar-spread]] short the 30-DTE and long the 90-DTE behaves like a 30-DTE structure for [[gamma]] and [[theta]] purposes and like a 60-DTE *spread* in vega — mixing DTE buckets is precisely the point of the structure.

## Why It Matters (for theta-targeted books)

DTE is the dominant axis on which a short-premium book is engineered, for three reasons:

### 1. DTE selects the trade-off between decay and path risk

The fundamental tension in premium selling is that the steepest part of the [[theta-decay-curve]] — the last 30 days, especially the last 10 — is also where [[gamma]] is most violent. A trader who only sells front-week premium maximises theoretical theta per dollar of capital but accepts a [[gamma-to-theta-ratio]] above 1 and a typical [[theta-realisation-ratio]] of 30-50% (versus 60-90% for 30-45 DTE on liquid index products). DTE selection is the choice of how aggressively to sit on that trade-off.

The canonical [[tastytrade]] / [[itpm-trading-philosophy|ITPM]] heuristic — *open at 45 DTE, manage at 21 DTE* — is a DTE-based discipline that puts the trade in the part of the curve where theta has begun its meaningful acceleration but gamma has not yet turned vertical.

### 2. DTE buckets are the unit of [[expiration-laddering|laddering]] and concentration limits

Most professional-grade portfolio rules are stated as DTE-bucket caps, not raw position counts:

- No single DTE bucket holds more than 30-40% of book theta.
- No two consecutive weekly expiries together hold more than 50% of book gamma.
- At least 25% of negative vega sits in 45+ DTE as a vega anchor (see [[vega-budgeting]]).

A book with 70% of theta in a single Friday is one CPI print away from a portfolio-level loss far larger than any single position's max loss. DTE buckets are the lens through which this concentration becomes visible.

### 3. DTE drives the realisation rate

Theoretical theta is what the model says the option *should* shed. Realised P&L is what actually shows up in the account. The ratio between them (see [[theta-realisation-ratio]]) is highly DTE-dependent:

- **0-2 DTE**: 30-50% on liquid index, lower on single names. Dealers actively scalp gamma against retail flow; pin and gap risk dominate.
- **7-21 DTE**: 50-70%. Manageable but still gamma-sensitive.
- **30-45 DTE**: 60-90%. The "sweet spot" where realisation reliably approaches theory.
- **60+ DTE**: 70-100%. Theta is small in absolute terms; whatever shows up shows up.

## Worked Example

Consider an SPX [[iron-condor]] structure consistent with [[theta-targeting]]'s 16-VIX, 45-DTE example. SPX at 5,000, IV at 16%, short 16-delta strikes at roughly 4,800 / 5,200, long wings 50 points wider. Per contract:

| DTE | Theta ($/day) | Gamma ($/$ × 100) | Vega ($/IV pt) | G/T ratio |
|---|---|---|---|---|
| 90 | 7 | 0.04 | 180 | 0.006 |
| 60 | 9 | 0.06 | 145 | 0.007 |
| **45** | **13** | **0.08** | **110** | **0.006** |
| 30 | 17 | 0.13 | 85 | 0.008 |
| 14 | 28 | 0.28 | 50 | 0.010 |
| 7 | 45 | 0.55 | 28 | 0.012 |
| 2 | 110 | 1.80 | 9 | 0.016 |
| 0.5 | 380 | 7.5 | 2 | 0.020 |

Two patterns drop out:

- **Theta scales roughly as 1/√t** — going from 45 DTE to 14 DTE roughly doubles theta, exactly what `√(45/14) ≈ 1.79` predicts. The 0.5 DTE figure is 30x the 45 DTE figure because √(45/0.5) = 9.5 and the IC is being valued in its terminal regime.
- **Gamma scales the same way**, so the *ratio* G/T is roughly stable in t at the per-position level. The portfolio-level danger comes from **dollar magnitude**: a book sized to harvest the same theta target via 45-DTE versus 7-DTE positions has very different absolute gamma — far less *paper* gamma in the 45-DTE case, because the position count is smaller. See [[gamma-explosion]] for the regime where this breaks down.

A trader running the [[theta-targeting]] worked example ($50/day on $150K) at 45 DTE needs 4 condors. The same theta target executed at 7 DTE needs only ~1.1 contracts — but the per-contract gamma is 7x larger and the [[theta-realisation-ratio|realisation ratio]] is half. The book's theoretical theta hits target either way; the actual P&L distribution is wildly different.

## Common Misuse / Pitfalls

- **Confusing calendar DTE with trading DTE in pricing.** A "5-day" weekly option has 3-4 trading sessions but 5 calendar days of theta. Brokers default to calendar-day theta; backtests on closing prices implicitly use trading-day theta. The two diverge by 30%+ in the front week.
- **Treating DTE as the sole risk dimension.** A 45-DTE 0.05-delta put has tiny theta and massive [[expected-shortfall|tail risk]]; a 45-DTE 0.30-delta put has large theta and modest tail risk. DTE is a coordinate, not a strategy.
- **Forgetting that DTE shrinks in real time.** A "30-DTE" position on Monday is a 23-DTE position by next Monday and a 16-DTE position the Monday after. Books that roll mechanically on a fixed weekday creep toward shorter average DTE unless deliberately re-laddered.
- **Naive weekend annualisation.** Setting a $/day theta target on a calendar-day basis but reading theta off a trading-day model (or vice versa) introduces a systematic 30% error.
- **Ignoring earnings and FOMC dates inside the DTE window.** A 30-DTE single-name option spanning earnings is a binary-event trade dressed as a decay trade. The DTE number tells you nothing about the catalyst structure.
- **Using DTE alone to compare across underlyings.** A 30-DTE NVDA option and a 30-DTE XLU option have the same DTE but very different IV regimes, gamma profiles, and event exposure. DTE only normalises across options on the same underlying.

## Related

- [[theta-decay-curve]] — the canonical shape of theta versus DTE.
- [[gamma-explosion]] — what happens to gamma as DTE → 0.
- [[theta-targeting]] — how DTE buckets feed the daily theta target.
- [[vega-budgeting]] — DTE-bucketed vega caps.
- [[expiration-laddering]] — diversifying across DTE buckets.
- [[gamma-to-theta-ratio]] — the path-risk metric that scales with 1/√t.
- [[theta-realisation-ratio]] — how DTE drives the gap between theoretical and realised theta.
- [[zero-dte-options]] — the DTE = 0 limit case.
- [[options-portfolio-construction]] — DTE concentration rules at the book level.
- [[managing-winners]] — the 21-DTE close/roll discipline.
- [[black-scholes-model]] — where the t variable lives in the formula.
- [[implied-volatility]] — the second axis of the option surface.

## Sources

- [[book-option-volatility-and-pricing]] — Natenberg, Chapters 6 and 8: time decay, the role of t in the Black-Scholes framework, and the asymmetry between calendar and trading days.
- Hull, *Options, Futures and Other Derivatives*, 10th ed., Chapter 19 — Greeks as functions of t, including the 1/√t scaling for ATM gamma and the corresponding theta divergence.
- [[tastytrade]] research on the 45 DTE / 21 DTE cadence and the realisation profile across DTE buckets.
- [[orats]] historical data — empirical theta capture by DTE bucket on liquid index options.
