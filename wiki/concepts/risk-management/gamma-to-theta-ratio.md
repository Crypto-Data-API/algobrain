---
title: "Gamma-to-Theta Ratio"
type: concept
created: 2026-05-07
updated: 2026-06-21
status: excellent
tags: [options, risk-management, gamma, theta]
aliases: ["G/T Ratio", "Gamma/Theta", "Path Risk Ratio"]
related: ["[[gamma]]", "[[theta]]", "[[theta-targeting]]", "[[vega-budgeting]]", "[[theta-decay-curve]]", "[[gamma-explosion]]", "[[time-to-expiration]]", "[[theta-realisation-ratio]]", "[[options-portfolio-construction]]", "[[expiration-laddering]]", "[[zero-dte-options]]", "[[gamma-scalping]]", "[[managing-winners]]", "[[short-strangle]]", "[[iron-condor]]", "[[variance-risk-premium]]", "[[volmageddon-2018]]"]
domain: [risk-management]
prerequisites: ["[[gamma]]", "[[theta]]", "[[theta-targeting]]"]
difficulty: advanced
---

The **gamma-to-theta ratio (G/T)** is the absolute value of a portfolio's net [[gamma]] divided by the absolute value of its net [[theta]]. It is the **path-risk** sister metric to the [[theta-targeting|theta-to-vega ratio (T/V)]]: where T/V measures how much vega risk the book carries per dollar of decay, G/T measures how much *spot-path* risk it carries per dollar of decay. A G/T ratio above 1.0 means a typical one-day move in the underlying erases more than one day of decay — the book is path-dominated, not decay-dominated, and short-premium positioning at that level requires explicit gamma sizing rather than implicit theta sizing.

## Overview

The conceptual setup mirrors [[vega-budgeting]] and T/V. A short-premium book bears three primary risks: vega (volatility moves against the position), gamma (spot moves and re-prices delta against the position), and direction (the move was monotone). T/V engineers the first risk against the income objective; G/T engineers the second.

For a book carrying $52/day theta and $0.10/$ portfolio gamma (i.e., a 1-point SPX move costs $10 in delta P&L on top of whatever the gamma curvature implies), a 0.5% SPX move (≈ 25 SPX points at S=5,000) produces a gamma P&L of roughly `0.5 × $0.10 × 25² = $31`. Compared to one day's $52 theta, the gamma cost is 60% — the book is decay-dominated for a typical session.

Now imagine the same theta target run with 7-DTE rather than 45-DTE structures. Per-contract theta is roughly 3.5x higher (since theta scales as 1/√t and √(45/7) ≈ 2.5, with additional convexity from gamma feedback) but per-contract gamma is 7-10x higher. The position count drops to roughly one third, so the book-level gamma is 2-3x higher even with fewer contracts. Same theta, much more gamma, much higher G/T.

The metric is most useful as a **regime indicator**: in a stable regime, watching G/T trend lets you see when the book is migrating toward the front of the [[theta-decay-curve|decay curve]] regardless of whether the trader notices the migration consciously.

## The Income-vs-Convexity Tradeoff

At its core, G/T quantifies a single tradeoff that every option position embodies: **theta is the income you are paid; gamma is the convexity risk you are paid to bear.** The two are mechanically inseparable in any single option — Black-Scholes pins them together through the relation that, for an at-the-money option, the dollar theta you collect is approximately the dollar gamma cost you would incur at the break-even daily move (this is the "gamma rent" framing in Natenberg). You cannot collect theta without being short gamma; you cannot be long gamma (own convexity) without paying theta. G/T simply makes the *exchange rate* between the two explicit.

| Position posture | Theta sign | Gamma sign | G/T reading | Who wins |
|---|---|---|---|---|
| Short premium (sell options) | + (collect) | − (short convexity) | The relevant path-risk metric | Seller wins on quiet days; loses on big moves |
| Long premium (buy options) | − (pay) | + (own convexity) | Mirror image — paying for path exposure | Buyer wins on big moves; bleeds on quiet days |
| Delta-hedged short gamma | + | − | High G/T = frequent re-hedge losses | [[gamma-scalping]] on the other side captures the move |

A short-premium book is, definitionally, **selling convexity to collect income**. The G/T ratio answers: *how much convexity am I short per dollar of income?* When that ratio rises (front-cycle migration, [[zero-dte-options|0DTE]] concentration, a vol shock), the book is being paid less and less income per unit of the convexity it has sold — the worst possible exchange rate, and exactly the configuration that detonates in events like [[volmageddon-2018]]. The disciplined response is to lengthen DTE, buy back convexity, or cut size — never to "add theta," which only adds matching gamma. See [[variance-risk-premium]] for why the seller is compensated on average despite this.

## Definition / Formula

The basic formula:

```
G/T = |Net Portfolio Gamma| / |Net Portfolio Theta|
```

where gamma is typically expressed in **dollars of delta change per 1% move in the underlying** (or equivalently `∂²C / ∂S² × S² / 100` for a percent-based gamma) and theta in **dollars per calendar day**.

A useful equivalent reading: G/T tells you the percentage spot move that produces a P&L hit equal to one day of theta. Specifically, for a short-gamma book with portfolio gamma `Γ$` (dollars of delta gained per 1% spot move, sign convention: positive number even for short-gamma books) and theta `Θ$` (positive number for the dollar magnitude):

```
Break-even daily move (%)  ≈  √(2 · Θ$ / Γ$)
                          =  √(2 / G/T) × 100
```

So a G/T of 1.0 implies a break-even daily move of √2 ≈ 1.4% — any move larger than that erases the day's decay. A G/T of 0.25 implies a break-even of 2.8%, which is the comfortable regime. A G/T of 4.0 implies a break-even of 0.7% — small moves dominate decay, and the book is structurally a gamma trade with theta as a small offset.

### Variants and refinements

- **Per-position G/T**, computed before sizing, predicts the structural path risk of a candidate trade independent of how many contracts are deployed.
- **DTE-bucketed G/T** is more informative than aggregate G/T for laddered books. A 0-7 DTE bucket might run G/T of 5+ while a 45-DTE bucket runs G/T of 0.3; aggregate G/T can hide an unhealthy front-cycle concentration.
- **Beta-weighted G/T** for multi-underlying books — both gamma and theta are first beta-weighted to a common reference (typically SPY) and then ratio'd.
- **Realised G/T over a window** — the actual gamma P&L drawn over the window divided by realised theta. The forward-looking screen-G/T is the *expected* version of this; the realised version is what the [[theta-realisation-ratio]] captures.

## Why It Matters (for theta-targeted books)

G/T is the second leg of the engineering tripod that supports [[theta-targeting]]:

1. **Theta target** — what the book is engineered to earn (the objective).
2. **T/V** — how much vega risk is taken per unit of decay (the volatility constraint).
3. **G/T** — how much path risk is taken per unit of decay (the spot-move constraint).

A book can satisfy any two of these and fail catastrophically on the third. The classic failure mode is hitting the theta target by loading front-cycle premium — T/V looks fine because front-cycle positions are gamma-dominated and not particularly vega-heavy, but G/T quietly drifts above 1 and any normal-range daily move erases multiple days of theoretical decay.

### Practical thresholds

Empirical bands for short-premium books on liquid index products:

| G/T regime | Interpretation | Typical structures |
|---|---|---|
| < 0.10 | Very calm; back-month dominated | 60-90 DTE [[iron-condor|iron condors]], [[calendar-spread|calendars]] |
| 0.10 - 0.30 | Healthy 30-45 DTE book | Standard [[theta-targeting]] cadence |
| 0.30 - 0.60 | Front-cycle present; manageable | 14-30 DTE focus, [[managing-winners|profit-take]] discipline applies |
| 0.60 - 1.0 | Path-risk approaching parity with decay | Last week of front cycle |
| 1.0 - 3.0 | Path-dominated | 0-7 DTE, [[gamma-explosion|gamma-explosion]] regime |
| > 3.0 | Extreme | [[zero-dte-options|0DTE]] short premium |

A typical hard rule: **reject any new position that would lift book G/T above 0.50**, and **trim mechanically when book G/T crosses 0.75**. The thresholds are not magic; they are the values at which a 1.5-σ daily move in the underlying produces a P&L hit larger than several days of theta.

### How G/T evolves with DTE

The same position drifts upward in G/T as time decays:

- A 45-DTE [[iron-condor]] with G/T ≈ 0.25 at entry.
- The same position at 21 DTE: G/T ≈ 0.55.
- At 14 DTE: G/T ≈ 0.85.
- At 7 DTE: G/T ≈ 1.4.
- At 1 DTE: G/T ≈ 4+.

This is the mechanical reason for the [[managing-winners|"manage at 21 DTE"]] heuristic. The trader is exiting before G/T crosses parity, not because of theta diminishing returns — there is plenty of theta left to capture — but because the gamma side of the ledger has grown to dominate.

## Worked Example

Take the four-condor SPX book from the [[theta-targeting]] worked example. SPX at 5,000, VIX at 16, short 16-delta strikes at ~4,800 / ~5,200, 50-point wings, 4 contracts. At entry (45 DTE):

- Theta: $52/day
- Gamma at the short strikes: roughly $0.10/$ per contract (positive sign, i.e., the book gains $10 of delta per 1% spot move toward the strike on the side of the move). With 4 contracts and roughly equal exposure on both sides of the body, the position behaves like net short ~$0.32/$ at the short strike.
- Net portfolio gamma (dollar terms, |Γ$| per 1% spot move): ≈ $16
- **G/T = 16 / 52 ≈ 0.31**

Break-even daily move: `√(2 × 52 / 16) = √6.5 ≈ 2.55%`. Any single-day SPX move below 2.5% leaves theta P&L ahead of gamma P&L. Comfortable.

### Roll the same book to 14 DTE.

Same 4 contracts, aged 31 days, no adjustments. SPX still 5,000.

- Theta has risen from $52/day to roughly $112/day (per-contract theta has roughly 2.2x'd as DTE went from 45 to 14).
- Gamma has risen from $16 to roughly $48 (per-contract gamma roughly 3x'd, consistent with the 1/√t scaling).
- **G/T = 48 / 112 ≈ 0.43**

Break-even: `√(2 × 112 / 48) = √4.67 ≈ 2.16%`. Still comfortable, but the margin has narrowed and the dollar magnitude of both has grown.

### Now 3 DTE.

- Theta ≈ $380/day.
- Gamma ≈ $260.
- **G/T ≈ 0.68**

Break-even ≈ 1.71%. SPX has averaged about 0.7% daily realised vol in the prior week; a 1.7% day is roughly 2.4σ. The expected path P&L over the next 3 sessions has the book breaking even on theta alone with about 30% probability of a path that erodes more than a session of decay.

### And 1 DTE.

- Theta ≈ $1,200/day (most of the remaining extrinsic, concentrated).
- Gamma ≈ $1,600.
- **G/T ≈ 1.33**

Break-even drops to 1.22%, well within a typical 1-day SPX range. The book is now more like a short-gamma trade with theta as a side payment than a decay-harvesting position. This is what triggers the [[gamma-explosion]] regime — see that page for the unbounded path-risk problem on 0-2 DTE.

The arc 0.31 → 0.43 → 0.68 → 1.33 over 44 days is the canonical ramp. A book that does **not** roll positions out of the front cycle will mechanically reach G/T > 1 every cycle, regardless of trader skill.

## Common Misuse / Pitfalls

- **Computing G/T at the wrong sign convention for gamma.** A short-premium book has *negative* gamma in the standard sign convention. The ratio uses absolute values; using signed gamma yields a negative number that is meaningless for the path-risk interpretation.
- **Mixing "per 1-point" gamma with "per 1-percent" gamma.** Brokers display both. The break-even-move arithmetic only works if gamma is in dollar-delta-per-percent units. Per-point units are useful for delta-hedging math but produce confusing G/T ratios.
- **Ignoring DTE bucketing.** An aggregate G/T of 0.4 sounds healthy but can mask a front-week sub-bucket at G/T 3 and a back-month sub-bucket at G/T 0.05 — different risks dressed up as a benign average.
- **Forgetting that gamma and theta are coupled.** The book cannot reduce G/T by simply "adding more theta" without adding gamma; the same DTE bucket adds both proportionally. To reduce G/T, the book must either lengthen DTE (add back-month exposure) or buy gamma (long options).
- **Using G/T without [[theta-realisation-ratio]] context.** A book with a healthy theoretical G/T of 0.3 can still leak P&L if the realised volatility is consistently above implied — that's a [[variance-risk-premium]] issue, not a G/T issue, and the two metrics together pinpoint which is which.
- **Treating the metric as point-in-time only.** G/T trend matters more than absolute level. A book whose G/T is rising week over week is migrating up the [[theta-decay-curve]] hockey stick and the trader is often unaware until a single bad day proves it.
- **Hedging gamma via more short premium.** Selling more options to "diversify" gamma adds gamma in the same direction; it does not reduce G/T. The only mechanical gamma-reduction levers are *closing* short premium, *buying* long options, or *moving DTE longer*.

## Related

- [[gamma]] — the numerator.
- [[theta]] — the denominator.
- [[theta-targeting]] — the parent discipline; G/T is one of its three engineering metrics.
- [[theta-decay-curve]] — what the denominator looks like as a function of DTE.
- [[gamma-explosion]] — what happens to G/T as DTE → 0.
- [[theta-realisation-ratio]] — the empirical companion metric.
- [[time-to-expiration]] — how G/T scales with t (it scales as 1/√t for ATM).
- [[expiration-laddering]] / [[managing-winners]] — DTE diversification and the close-before-G/T-crosses-1 discipline.
- [[options-portfolio-construction]] — where G/T sits in the daily Greeks check.
- [[gamma-scalping]] — the activity on the other side of a high-G/T short position.
- [[zero-dte-options]] — the regime where G/T > 3 is structural.
- [[variance-risk-premium]] — the long-run wedge that makes high-G/T positions profitable on average despite the path risk.
- [[volmageddon-2018]] — case study in what happens when G/T-blind books meet a vol shock.

## Sources

- [[book-option-volatility-and-pricing]] — Natenberg, on the relationship between gamma and theta as duals of the time-volatility surface; the "gamma rent" framing.
- Hull, *Options, Futures and Other Derivatives*, 10th ed., Chapter 19 — Black-Scholes derivation of gamma and theta and their `1/√t` joint scaling.
