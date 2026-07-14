---
title: "Theta Realisation Ratio"
type: concept
created: 2026-05-07
updated: 2026-06-21
status: excellent
tags: [options, risk-management, theta, performance-attribution]
aliases: ["Realised Theta", "Theta Capture Ratio", "Decay Capture Rate", "Realisation Rate"]
related: ["[[theta]]", "[[theta-targeting]]", "[[theta-decay-curve]]", "[[gamma-to-theta-ratio]]", "[[gamma-explosion]]", "[[gamma-scalping]]", "[[time-to-expiration]]", "[[vega-budgeting]]", "[[options-portfolio-construction]]", "[[expiration-laddering]]", "[[zero-dte-options]]", "[[managing-winners]]", "[[variance-risk-premium]]", "[[volmageddon-2018]]", "[[bid-ask-spread]]", "[[second-order-greeks]]", "[[vanna]]", "[[volatility-spike]]"]
domain: [risk-management]
prerequisites: ["[[theta]]", "[[theta-targeting]]", "[[options-greeks]]"]
difficulty: advanced
---

The **theta realisation ratio** is the actual P&L of a short-premium book over a window divided by its cumulative theoretical theta over the same window. It is the long-horizon scorecard of a [[theta-targeting|theta-targeted]] book — the metric that distinguishes a position whose extrinsic value is genuinely being harvested from one where the screen-theta is being silently siphoned off by [[gamma-scalping|dealer gamma scalping]], slippage, and adverse path. Where [[theta]] tells you what the book *should* earn if the world stays still, the realisation ratio tells you how much of that earning actually lands in the account once the world moves.

## Overview

The intuition behind the ratio is simple. A book with $50/day theoretical theta should, in the absence of anything else happening, produce $50 of P&L per day. Across a 30-day window that is $1,500 of theoretical decay. If the book actually netted $1,050 over that window, the realisation ratio is 70%. If it netted $300, the ratio is 20% and most of the theoretical decay was eaten by [[gamma]], [[vega]], skew, slippage, or adverse spot moves.

Realisation is the empirical proof — or refutation — of the [[variance-risk-premium]] thesis. A book whose long-run realisation ratio is consistently above 100% is being subsidised by something (favourable [[volatility-skew|skew]], [[implied-volatility|IV]] crush, lucky direction). A book consistently below 50% on liquid index products is leaking edge in a way that no amount of theoretical theta can compensate for. Tracked over months, it answers the question: *"Is this book a premium-selling business, or am I just renting [[gamma]] risk to dealers and paying for the privilege?"*

## Definition / Formula

The basic formula:

```
Realisation Ratio = Σ Realised P&L over window / Σ Theoretical Theta over window
```

Three windowing conventions are useful:

1. **Rolling window** — typically 21 trading days or 30 calendar days. Smooth enough to ignore single-day noise, short enough to react to regime changes. Most disciplined books track a 21-day rolling realisation.
2. **Per-cycle** — measure realisation from position open to position close (or roll). This is the cleanest attribution because it isolates a single decay cycle, but it gives spiky readings.
3. **Year-to-date** — for the long-run scorecard. The denominator is the cumulative theoretical theta the book *would* have produced if every position decayed exactly at its theta number.

Refinements practitioners make:

- **P&L attribution decomposition.** Realised P&L = theta P&L + gamma P&L + vega P&L + slippage. Pure realisation is more accurately `(Realised P&L − vega P&L − slippage) / Theoretical Theta`, isolating the decay-vs-gamma trade-off from independent vega and execution effects.
- **Net of [[managing-winners|profit-taking]]**. Closing at 50% of credit captures the realised P&L *up to that point*; the cumulative theta denominator should match the holding period, not the original DTE-to-expiry.
- **Dollar normalisation**. For multi-underlying books, sum realised P&L in dollars and theoretical theta in dollars. Do not average per-position ratios — that systematically over-weights small positions.

### P&L attribution — where the missing theta goes

The realisation gap is not random; every dollar of theoretical theta that fails to land was diverted by an identifiable Greek. Decomposing realised P&L into its sources is what turns the ratio from a scorecard into a diagnostic:

| P&L bucket | Greek source | Sign on a short-premium book | What it tells you |
|------------|--------------|------------------------------|--------------------|
| Theta P&L | [[theta]] | + (the income engine) | the theoretical decay actually accrued |
| Gamma P&L | [[gamma]] / [[gamma-scalping]] | − when the tape chops | realised variance the dealer scalped back |
| Vega P&L | [[vega]] | + on IV crush, − on [[volatility-spike|IV spike]] | how much of the result was a vol move, not decay |
| Vanna/vomma P&L | [[second-order-greeks]] | varies | "unexplained" P&L during regime changes (see [[vanna]]) |
| Slippage | [[bid-ask-spread]] | − | execution cost on entry, roll, and close |

The honest realisation number strips vega (and ideally vanna/vomma) before dividing by theoretical theta, isolating the decay-vs-gamma trade-off from independent vol moves. Scenario A in the worked example below shows exactly why: a 165% headline collapses to an 84% theta-only realisation once IV-crush vega is removed.

### Typical realisation by structure (reference)

The values below are conventional rough benchmarks for *normal* vol regimes, not measured constants. They exist to set expectations, not to be plugged into a backtest:

| Structure | Typical realisation | Variance | Driver |
|-----------|---------------------|----------|--------|
| 45-DTE SPX [[iron-condor]] | ~70–90% | low | far from the [[gamma-explosion]] zone |
| 30-DTE single-name [[short-strangle]] | ~50–70% | medium | single-name path risk |
| 7-DTE weeklies | ~40–60% | high | entering the explosion zone |
| 0DTE iron flies / [[zero-dte-options]] | ~30–50% | very high, fat left tail | full gamma explosion; dealers scalp the variance |
| Liquid index book, all-in annual | ~60% | — | dragged down by rare deep-negative windows |

## Why It Matters (for theta-targeted books)

The realisation ratio is the connecting tissue between [[theta-targeting]]'s theoretical income target and the bank account. Several practical uses:

### 1. Setting realistic income targets

A trader with a 12% annual income objective and a long-run realisation ratio of 70% should set a *theoretical* theta target of `12% / 0.70 ≈ 17%` to actually deliver the income. Without the realisation buffer, every theta-targeted book systematically under-delivers its stated objective. See [[theta-targeting]] for the buffering arithmetic.

### 2. Diagnosing book health in real time

A declining realisation ratio is the earliest signal that something has shifted in either the book's structure or the volatility regime:

| Ratio trend | Likely cause | Action |
|---|---|---|
| Stable 60-90% on index | Healthy [[variance-risk-premium]] capture | Stay the course |
| Drifting from 70% → 40% | Average DTE shrinking; gamma rising; or a vol-regime change | Trim front cycle, re-ladder |
| One-week collapse to 0% or negative | Vol shock or wrong-way directional move | Stress-test; reduce size |
| Above 100% for an extended period | Lucky direction, [[implied-volatility|IV]] crush | Do **not** scale up — this will revert |

### 3. Comparing strategies on a common axis

Different short-premium strategies have wildly different realisation profiles:

- **45-DTE [[iron-condor|iron condors]] on SPX**: ~70-90% realisation in normal vol regimes.
- **30-DTE [[short-strangle|short strangles]] on liquid single names**: ~50-70%.
- **7-DTE [[short-strangle|strangles]] / weeklies**: ~40-60%.
- **0DTE iron flies and [[zero-dte-options|0DTE]] short premium**: ~30-50% on average; with high variance and a fat left tail.
- **[[calendar-spread]] structures**: variable; the metric is harder to interpret because the denominator includes both legs' theta.

The ratio normalises across these; a strategy that "produces $30/day theta" is not equivalent to another strategy producing $30/day theta if the realisation rates are 80% versus 35%.

### 4. Distinguishing a vol-event regime from genuine edge

In a sustained low-realised-vol environment, realisation ratios on short-premium books drift toward 100%. A trader who scales up at this point is increasing size into the regime *most likely* to mean-revert. Realisation above 90% is a warning, not a green light — see [[volatility-regime]] and [[volmageddon-2018]] for the historical evidence.

## Worked Example

Consider the four-condor SPX book from the [[theta-targeting]] worked example: $150K account, 4 [[iron-condor]] contracts at 45 DTE, theoretical theta of $52/day, T/V of 0.118, vega budget of $1,500/IV point. Theoretical cumulative theta over a 21-day holding period is `$52 × 21 = $1,092`.

### Scenario A — calm market, monotone realisation

Over the 21 days the SPX moves smoothly within the short strikes (4,800 / 5,200) and IV declines from 16 to 14.

- Theta P&L: ≈ $1,000
- Vega P&L: 4 contracts × $110 vega × −2 IV pts = +$880 (long beneficiary of IV crush despite being short premium because vega is negative-by-sign on a short strangle; IV down ⇒ price down ⇒ short benefits)
- Gamma P&L: ≈ −$50 (small adverse drift)
- Slippage at close: ≈ −$30
- Realised P&L: $1,800
- **Realisation ratio: 1,800 / 1,092 ≈ 165%**

The headline number is misleading. Stripping out the vega contribution, the *theta-only* realisation is `(1,800 − 880) / 1,092 = 84%`, which is the honest read on what the structure delivered as decay capture. This is why P&L attribution matters — without decomposing, the trader credits the decay engine with what the IV crush did.

### Scenario B — choppy market, gamma-active

SPX whipsaws between 4,950 and 5,050 over the same 21 days, IV unchanged, no IV crush.

- Theta P&L: ≈ $1,000
- Vega P&L: ≈ $0
- Gamma P&L: ≈ −$650 (the dealer on the other side scalps every up-and-down, harvesting the realised variance the position is short)
- Slippage at close: ≈ −$40
- Realised P&L: $310
- **Realisation ratio: 310 / 1,092 ≈ 28%**

This is the realisation regime that destroys premium-selling P&L without anything dramatic happening. No vol shock, no large move, just chop. The realised variance over the period was higher than the implied variance the book sold; that delta is exactly the gamma scalping the dealer captured. Tracking the ratio surfaces this immediately; tracking only mark-to-market P&L makes it look like "a slow month."

### Scenario C — vol shock and recovery

Day 5 brings a 2% SPX gap-down and a 5-vol-point IV expansion. By day 21, SPX has recovered and IV is back to 17.

- Theta P&L: ≈ $1,000
- Vega P&L: net roughly flat (large drawdown then recovery)
- Gamma P&L: ≈ −$1,500 (the gap)
- Slippage at close: ≈ −$80 (wider spreads through the shock)
- Realised P&L: −$580
- **Realisation ratio: −580 / 1,092 ≈ −53%**

The book paid for 21 days of theoretical theta and lost half a month of income on top. This is the "structural tail" of a short-premium book — see [[expected-shortfall]] and [[volmageddon-2018]]. A *single* such window in a year of otherwise 80% realisation drags the annual ratio to roughly 60%, which is the typical empirical value for liquid index short-premium strategies.

## Common Misuse / Pitfalls

- **Confusing realisation ratio with win rate.** Win rate measures how often trades close profitable. Realisation measures how much of theoretical decay actually lands. A book can have 90% win rate and 40% realisation if the average winner is small and the rare losers are large — exactly the failure mode of premium selling.
- **Failing to decompose vega P&L.** A book that benefits from an IV crush will look like it has a 150% realisation ratio. The trader who internalises that number as "I am earning 50% above theoretical" is misled when IV mean-reverts. Always strip vega P&L before computing the headline realisation number.
- **Cherry-picking the window.** Computing realisation only on closed positions excludes the worst losing months when positions are still open at month-end. Use a rolling window that captures mark-to-market, not realised cash only.
- **Computing a per-position average instead of dollar-weighted.** A book of three positions — two small high-realisation winners and one large low-realisation loser — has a dollar-weighted realisation that reflects the loser. The simple-average ratio across positions hides this.
- **Treating the ratio as a forward predictor on short windows.** A single week's realisation is dominated by gamma noise and tells you almost nothing about forward expectation. Statistical significance only emerges over 60-90+ days.
- **Adjusting the theoretical theta number after the fact** to make the ratio look better. The theoretical theta should be locked in at position open (or marked daily at *that day's* model theta), not reverse-engineered from realised P&L.
- **Using brokerage-reported theta without checking the model.** Different platforms use different IV inputs and day-count conventions; the same position can have a $52/day theta on one platform and $58/day on another. Pick a consistent reference and stick with it.

## Related

- [[theta-targeting]] — the discipline whose results the realisation ratio measures.
- [[theta]] — the theoretical numerator's denominator.
- [[theta-decay-curve]] — what theoretical decay looks like as a curve.
- [[gamma-to-theta-ratio]] — the path-risk metric that predicts low realisation in front-cycle books.
- [[gamma-explosion]] — why front-cycle realisation is structurally lower.
- [[gamma-scalping]] — the activity on the other side of the trade that captures the gap between theoretical and realised.
- [[variance-risk-premium]] — the long-run wedge that makes 60-90% realisation a profitable business.
- [[expiration-laddering]] — DTE diversification raises realisation by smoothing the gamma profile.
- [[managing-winners]] — closing at 50% of max profit raises realisation by avoiding the steepest hockey-stick segment.
- [[options-portfolio-construction]] — where the realisation metric belongs in the daily/weekly review cadence.
- [[zero-dte-options]] — the strategy class with the lowest typical realisation rates.
- [[volmageddon-2018]] — case study in catastrophic single-window realisation collapse.
- [[bid-ask-spread]] — slippage component of the realisation gap.
- [[second-order-greeks]] — vanna/vomma are the "unexplained" attribution bucket.
- [[vanna]] — second-order delta drift that contaminates realisation during vol moves.
- [[volatility-spike]] — the regime where realisation collapses to negative.

## Sources

- [[book-option-volatility-and-pricing]] — Natenberg on the difference between theoretical and realised P&L for short-volatility positions.
- General market-making literature on gamma scalping by dealers as the source of the realisation gap on the other side of retail premium-selling flow.
