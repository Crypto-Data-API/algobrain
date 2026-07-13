---
title: "Stress Test"
type: concept
created: 2026-05-07
updated: 2026-06-20
status: excellent
tags: [risk-management, options, portfolio-theory, backtesting, volatility]
aliases: ["Stress Testing", "Portfolio Stress Test", "Adverse Scenario Test"]
related: ["[[expected-shortfall]]", "[[value-at-risk]]", "[[options-portfolio-construction]]", "[[theta-targeting]]", "[[the-theta-trap]]", "[[vega-budgeting]]", "[[itpm-framework]]", "[[itpm-trading-philosophy]]", "[[volmageddon]]", "[[vix-august-2024-spike]]", "[[covid-crash]]", "[[reverse-stress-test]]", "[[monte-carlo-simulation]]", "[[volatility-of-volatility]]", "[[options-greeks]]", "[[skew]]", "[[volatility-term-structure]]"]
domain: [risk-management]
prerequisites: ["[[options-greeks]]", "[[implied-volatility]]"]
difficulty: intermediate
---

A stress test re-prices a portfolio under a defined adverse scenario — a spot shock, a volatility shock, a combined shock, or a historical replay — and reports the resulting P&L against the book's risk budget. Stress testing complements [[value-at-risk|VaR]] (which gives a single percentile of the loss distribution) and [[expected-shortfall]] (which gives the average loss in the tail) by answering the operationally different question *"if this specific thing happens, what do I lose?"*. For an [[options-portfolio-construction|options book]] with material non-linear exposure to spot, volatility, skew, and time, stress testing is the only risk discipline that captures second-order effects accurately, and it is the standard pre-commitment tool used inside the [[itpm-framework|ITPM framework]] to size positions before they are entered.

## Overview

The basic claim of stress testing is that a portfolio's risk is not a single number. The full risk profile is a *surface* over the variables the book is exposed to — for an options book, primarily spot, [[implied-volatility|IV]] (with skew and term-structure dimensions), time, and rates. A stress test samples that surface at chosen points and reports the P&L at each. The value of the test depends on whether the chosen points are realistic and severe — too soft and the test gives false comfort, too contrived and the trader ignores it.

Three orthogonal use-cases:

1. **Pre-trade screening.** Before a candidate position is added, re-price the proposed book under a fixed scenario set. Reject if any scenario breaches the [[options-portfolio-construction#Risk Limits|written risk limits]].
2. **Daily monitoring.** Each morning, compute scenario P&Ls on the live book and compare to the limits. If any scenario has crept above its threshold, take action *before* the move happens.
3. **Reverse design.** Given a written maximum acceptable loss (e.g., -15% NAV), find the smallest move in spot/IV/skew that would produce it. This identifies the binding constraint and tells the trader exactly where the cliff is.

Stress testing differs from [[backtesting|backtesting]] in that it does not require historical data of the strategy itself — only a pricing model and a scenario set. It differs from [[monte-carlo-simulation|Monte Carlo simulation]] in that scenarios are *deterministic*, chosen by the operator, rather than sampled from a distribution. A complete risk discipline uses all three.

## Standard Scenario Set

A canonical scenario menu for an [[options-portfolio-construction|options book]] traded on US index and large-cap underlyings:

### Parallel spot shocks

Apply the same percentage move to every underlying simultaneously, holding IV constant.

| Scenario | Magnitude | Rationale |
|---|---|---|
| Mild down | -5% spot | Routine pullback; tests near-the-money [[gamma]] exposure |
| Moderate down | -10% spot | Typical correction (e.g., 2018 Q4, 2020 Sept); tests mid-range gamma and put-side wing exposure |
| Severe down | -20% spot | Crash scenario (e.g., 2020 Mar peak-to-trough first leg); tests far-OTM put exposure and wing utility |
| Mild up | +5% spot | Tests call-side gamma and any short-call positioning |
| Severe up | +10% / +20% spot | Squeeze scenario; tests upside short-call exposure (less common but historically real, e.g., 2008 VW squeeze, 2021 GME) |

### IV shocks

Apply a parallel shift to the IV surface, holding spot constant.

| Scenario | Magnitude | Rationale |
|---|---|---|
| Mild vol up | +3 IV points | Routine vol expansion; tests short-vega exposure |
| Moderate vol up | +10 IV points | Aug 2015, Dec 2018 magnitude; tests vega budget |
| Severe vol up | +20 IV points | Feb 2018 partial; tests max-vega scenarios |
| Tail vol up | +50 IV points | Mar 2020 / Aug 2024 magnitude; tests overlay sufficiency |
| Vol crush | -5 / -10 IV points | Tests long-vega exposure and overlay cost realisation |

### Combined shocks

Real crashes do not move one variable at a time. Combined shocks are the most operationally useful tests because they capture *correlated* moves.

| Scenario | Spot | IV | Skew | Rationale |
|---|---|---|---|---|
| Risk-off mild | -5% | +5 | +2 | Typical pullback with skew steepening |
| Risk-off moderate | -10% | +15 | +5 | Recession-fear move; covers most multi-day selloffs |
| Risk-off severe | -20% | +30 | +10 | Crash scenario |
| Tail | -10% / +50 IV | +50 | +15 | The combined extreme that catches short-premium books |
| Squeeze | +10% | +10 | -3 | Upside squeeze with call-skew expansion |

The "+50 IV with -10% spot" scenario is the **single most important pre-trade stress test for any short-vol book** — it represents the lower end of what the historical tail (Volmageddon, COVID, August 2024) actually delivered, and it is the move that reliably exposes books that are unhedged or oversized.

### Historical replay

Re-price the *current* book using the actual moves from past events. This is the most informative scenario set because it captures the joint distribution of spot, IV, skew, and term-structure that a stochastic-model scenario will miss.

| Date | Spot move | IV move | Notes |
|---|---|---|---|
| 2008-10-15 (GFC) | -9% | +30 IV | Liquidity collapse, skew inversion |
| 2010-05-06 (Flash Crash) | -9% intraday | +20 IV intraday | Microstructure event; intraday rebound |
| 2015-08-24 (China) | -3.9% | +28 IV | VIX 28 → 53 intraday |
| 2018-02-05 ([[volmageddon|Volmageddon]]) | -4.1% | +20 IV (VIX 17 → 37) | Short-vol-ETP-driven; Feb 6 closed worse |
| 2020-03-12 ([[covid-crash|COVID]]) | -9.5% | +21 IV | Liquidity event; followed by -12% on 2020-03-16 |
| 2020-03-16 (COVID peak) | -12% | +24 IV (VIX 57 → 82) | Largest single-session vol expansion of cycle |
| 2022-09-13 (CPI shock) | -4.3% | +5 IV | Macro-data shock; muted vol response |
| 2024-08-05 ([[vix-august-2024-spike|VIX Aug 24]]) | -3% | VIX 23 → 65 intraday | Yen-carry unwind; intraday; partial reversion |

A book that does not lose more than its written drawdown limit on any of these historical replays is at least *historically robust*. A book that breaches limits on multiple scenarios is unsafe at current size, regardless of how good the strategy looks in calm samples.

### Monte Carlo from realised covariance

A complementary technique: instead of fixed scenarios, sample joint moves of (spot, IV, skew, term-structure) from the realised covariance of the trailing 1-3 years and re-price the book over thousands of paths. Outputs:

- The full P&L distribution.
- Empirical [[expected-shortfall]] at chosen percentiles (e.g., 1% ES, 5% ES).
- Tail-tail conditional probabilities (e.g., probability of loss >X given loss already >Y).

Monte Carlo on realised covariance *underestimates* tail risk because it samples from a recent distribution that excludes the next regime shift. It should be used alongside historical replay and explicit stress scenarios, not in place of them. See [[monte-carlo-simulation]].

### Reverse stress tests

Where the standard test asks *"given this scenario, what is my loss?"*, the reverse test asks *"given this maximum loss, what scenario would cause it?"*. The procedure:

1. Set the maximum acceptable loss (e.g., -15% of NAV).
2. Sweep over scenarios — spot moves, vol moves, combined — and find the smallest one that produces the loss.
3. Compare that scenario to historical frequency: how often has a move that severe (or worse) happened?

If a -15% NAV loss requires only a -7% spot move with +12 IV, and that combined move has happened ~6 times in the trailing decade, the book is materially exposed. If it requires a -25% spot move with +60 IV (a once-per-decade event), the book is reasonably sized for the budget. Reverse stress is the most operationally useful test because it gives the trader the *exact location of the cliff*. See [[reverse-stress-test]].

## Application to Options Books

Options books require more sophisticated stress testing than linear (delta-1) books because:

### Greeks repricing

Greeks themselves change under stress. A short put that has delta -10, gamma 0.02, vega -50 at current spot will have *very different* Greeks at -10% spot. Naive stress testing that holds Greeks constant ("if delta is -10, a -10% move loses 10 × notional × 10% = …") materially understates the loss.

A correct stress test re-runs the [[black-scholes-model|pricing model]] under the new (spot, IV, skew, time) inputs and reports the actual P&L, which captures:

- Delta convexity (gamma)
- Vega convexity (volga / vol-of-vol)
- Skew dynamics (vanna)
- Time decay over the stress horizon

### Second-order effects

The Greeks that matter under stress are higher-order:

- **[[gamma]]** — convexity of P&L to spot. A -10% spot move on a short gamma book loses more than 10× delta × spot move because gamma compounds the directional loss. For a 30-DTE iron condor at 16-delta, a -10% move can deliver 5-10× the position's daily theta in gamma loss alone.
- **Vanna** — sensitivity of delta to vol. Short OTM puts develop *more* negative delta as IV rises, so a combined "spot down + vol up" move hurts more than the linear sum of the two effects.
- **Volga / Vol-of-vol** — convexity of P&L to IV. A book with non-linear vega exposure (calendar spreads, ratio structures) has materially different P&L profiles in vol shocks than a flat-vega book of the same nominal vega number.
- **Charm** — decay of delta over time. Important for stress horizons longer than 1 day.

Practitioners typically stress over a defined horizon (1 day, 5 days, 20 days) rather than instantaneously, to capture the interaction of theta with the other Greeks during the move.

### Skew and term-structure dimensions

A "+20 IV points" parallel shift is a useful first cut but materially understates real crashes, in which skew steepens dramatically (put IVs rise more than ATM, call IVs may rise less or fall) and term-structure inverts (front-month IV exceeds back-month). A short-put-heavy book is most exposed to skew steepening; a calendar-heavy book is most exposed to term-structure inversion. A complete stress menu therefore includes:

- Skew shocks: +5 / +10 / +15 skew points (25-delta-put IV minus 25-delta-call IV).
- Term-structure shocks: front-month +20 IV, back-month +5 IV (inverting the curve).
- Combined: spot down + IV up + skew up + term-structure invert.

The "tail" scenario in the table above bundles these for operational simplicity.

### Vol-of-vol

In the most extreme regimes — Feb 2018, Mar 2020, Aug 2024 — the *volatility of volatility* spikes alongside vol itself. A 50-IV-point shock is itself a sample from a distribution whose variance has expanded. Sophisticated stress testing accounts for this by stressing over *distributions* of IV moves rather than point estimates. See [[volatility-of-volatility]].

## Distinguishing from VaR and ES

Three related but distinct risk metrics:

| Metric | What it tells you | Limitations |
|---|---|---|
| [[value-at-risk\|VaR]] | "I will lose less than X with 95% confidence" — a single percentile of the loss distribution. | Does not say what happens in the 5% tail. Distribution-dependent — fat tails make Gaussian VaR useless. |
| [[expected-shortfall]] | "Conditional on a loss worse than VaR, my average loss is X" — the *mean* of the tail. | Still distribution-dependent. Hard to estimate without long history. Coherent risk measure, unlike VaR. |
| Stress test | "If exactly *this* happens, I lose X" — a deterministic scenario. | Only as good as the chosen scenarios. Says nothing about probabilities. |

The complete risk discipline uses all three:

- **VaR** for capital allocation conversations and reporting.
- **ES** for tail sizing — *given that I am in the bad regime, am I sized to survive it?*
- **Stress test** for operational pre-commitment — *here are the moves I am explicitly sized to survive, and here is what I would do if they happened.*

Stress testing's advantage over VaR/ES is that it is **transparent**: the trader can see exactly what scenario produces the reported loss, and can adjust the scenario if it does not match the regime they are worried about. Its disadvantage is that scenarios are *chosen*, so a trader can construct a stress menu that gives false comfort.

## Implementation

A practical implementation for an options book on a portfolio-margin account:

### Daily run

Each morning before the open:

1. Pull the current book's positions and Greeks from the broker.
2. Re-price under the standard scenario set (parallel spot, parallel IV, combined, historical replay).
3. Compute scenario P&Ls and compare to the written drawdown limits.
4. If any scenario breaches its limit, generate the rebalancing action *before* the open.

Tools that expose this directly:

- **[[thinkorswim]] Analyze tab** — supports custom scenario columns with simultaneous spot and IV shifts; beta-weighted across the book.
- **IBKR Risk Navigator** — full Greeks repricing under custom scenarios; supports historical-event replay.
- **[[optionnet-explorer]]** — granular what-if for a defined book; includes time-forward scenarios.
- **orats** — historical surfaces for replay; backtests through stress events.
- **Custom Python (QuantLib, py_vollib, OptionPriceHandler)** — for sophisticated books, a custom stress engine over fitted vol surfaces is standard.

### Pre-trade screen

Before adding any position:

1. Construct the *prospective* book (current book + candidate position).
2. Run the same standard scenario set.
3. Reject the candidate if it would push any scenario above its threshold.

This is the discipline that makes the [[itpm-framework]]'s "stage 6" sizing rigorous rather than discretionary.

### Worked example

*All figures in this example are illustrative and hypothetical — they are not real market data or a real book.*

A book with $250K NAV running an [[options-portfolio-construction|ITPM-style options portfolio]]:

- Current Greeks: delta +120 (beta-weighted to SPX), vega -800/IV pt, theta +$95/day, gamma -150.
- Drawdown limit: -15% NAV = -$37,500.

Scenario set:

| Scenario | Spot | IV | Stress P&L | % of NAV | Pass? |
|---|---|---|---|---|---|
| -5% / +5 IV | -5% | +5 | -$11,200 | -4.5% | OK |
| -10% / +10 IV | -10% | +10 | -$23,400 | -9.4% | OK |
| -10% / +20 IV | -10% | +20 | -$31,500 | -12.6% | OK (close) |
| -10% / +50 IV (tail) | -10% | +50 | -$48,600 | -19.4% | **FAIL** |
| 2018-02-05 replay | -4.1% | +20 | -$22,800 | -9.1% | OK |
| 2020-03-16 replay | -12% | +24 | -$36,200 | -14.5% | OK |
| 2024-08-05 replay | -3% | +42 | -$33,000 | -13.2% | OK |

The book passes most scenarios but **fails the tail combined shock**. The reverse-stress question: *what is the smallest move that breaches the -15% limit?* Sweep finds it at approximately spot -8% with IV +30, which is a roughly once-per-3-year historical event.

The action: *cut net vega in half before the next session*, primarily by closing back-month naked positions and replacing with closer-wing condors. Re-run scenarios after the adjustment; the tail scenario should now produce a loss inside the limit.

This is the daily loop ITPM-aligned practitioners run, and it is the only discipline that catches the [[the-theta-trap|theta trap]] before it springs.

## Building a Stress Menu: A Checklist

A defensible stress program is auditable. Each item below should be answerable "yes" before the menu is trusted:

- [ ] **Covers every non-linear axis the book actually carries** — spot, IV level, skew, term structure, rates, and time. A short-skew book that only stresses parallel IV is testing the wrong axis.
- [ ] **Reprices, never extrapolates** — every scenario re-runs the [[black-scholes-model|pricing model]] under the new inputs; Greeks are *outputs* of the stressed state, not held constant.
- [ ] **Includes historical replay** — the GFC, Flash Crash, Volmageddon, COVID, and Aug 2024 moves applied to the *current* book. These capture joint moves no parametric scenario will.
- [ ] **Includes the combined tail** — "-10% spot / +50 IV / skew up / term inverted" is the single most diagnostic test for a short-vol book.
- [ ] **Includes a reverse stress** — the smallest move that breaches the written drawdown limit, compared against its historical frequency.
- [ ] **Stresses over a horizon, not an instant** — 1-day, 5-day, and 20-day variants capture theta/charm interaction.
- [ ] **Applies a liquidity haircut** — widen effective spreads 1.5-3× and assume thinned depth in the severe scenarios.
- [ ] **Runs daily, not only at entry** — Greeks drift; a position safe on day 0 can breach by day 10.
- [ ] **Each breach maps to a pre-committed action** — the output is a rebalancing instruction, not a feeling.

## Severity Calibration

How severe is severe enough? Anchor each scenario class to its rough historical recurrence so the menu neither under- nor over-tests. *Recurrence bands below are coarse, illustrative orders-of-magnitude, not precise frequencies.*

| Scenario class | Illustrative recurrence | Purpose |
|---|---|---|
| Mild (-5% spot / +5 IV) | Several times a year | Tests near-the-money [[gamma]]; should be a shrug |
| Moderate (-10% spot / +15 IV) | Roughly annual | Tests the [[vega-budgeting\|vega budget]]; mild discomfort acceptable |
| Severe (-20% spot / +30 IV) | Every few years | Tests wing utility and tail hedges; should be survivable |
| Tail (-10% spot / +50 IV) | Once per several years | Tests overlay sufficiency; the binding pre-trade test |
| Replay (GFC / COVID) | Once per cycle or rarer | Regime-honest joint move; the integrity check |

The calibration principle: a book should be *uncomfortable but solvent* in the moderate-to-severe band and *solvent with hedges paying off* in the tail band. A book that fails the moderate scenario is oversized today, not in some distant future.

## Common Misapplications

1. **Stressing only the variables that look benign.** A book with concentrated short-skew exposure that only stress-tests parallel IV shifts will appear safe in every test. The stress menu must cover the actual non-linear axes.
2. **Holding Greeks constant in the stress.** Linear extrapolation from current Greeks materially understates loss in any scenario that moves through the gamma-rich part of the surface. Real stress requires repricing.
3. **Excluding historical replay because "this time is different."** Each tail event is dismissed as exceptional in hindsight; collectively they form the empirical distribution. Replay is the most regime-honest test available.
4. **Stress-testing only at trade-entry, never daily.** A book's Greeks drift; a position safe at entry can become unsafe by day 10 as gamma builds or vega concentrates. Daily stress is the operational discipline; pre-trade stress alone is not enough.
5. **Treating the stress numbers as worst-case.** They are *one* set of scenarios. Real outcomes can be worse — Mar 2020 had a multi-day sequence not captured by a single-day replay; Volmageddon had a Feb 6 tail beyond the Feb 5 number; Aug 2024 had intraday extremes not visible in close-to-close data. Stress numbers should be treated as a *floor* on the expected loss in the chosen scenario, not a ceiling.
6. **Ignoring liquidity in the stress.** In the stress regimes that matter, [[bid-ask-spread|bid-ask spreads]] expand 3-10×, market-makers widen size, and exiting a book at theoretical mid-price is impossible. Realistic stress applies a liquidity haircut (e.g., 50% wider effective spread) on top of theoretical pricing.

## Related

- [[expected-shortfall]] — the complementary distribution-based tail metric
- [[value-at-risk]] — the percentile-based metric stress testing complements
- [[options-portfolio-construction]] — the book-level discipline that consumes stress-test outputs
- [[theta-targeting]] — uses stress tests in the worked-example sizing loop
- [[the-theta-trap]] — the failure mode stress testing is most needed to detect
- [[vega-budgeting]] — the constraint stress tests verify
- [[itpm-framework]] — operational framework that embeds stress testing in stage 6
- [[itpm-trading-philosophy]] — the worldview that requires stress testing as discipline rather than option
- [[reverse-stress-test]] — the inverse formulation
- [[monte-carlo-simulation]] — the stochastic complement
- [[volatility-of-volatility]] — the higher-order risk dimension
- [[options-greeks]] — the variables being stressed
- [[skew]] — the most under-stressed dimension in retail tooling
- [[volatility-term-structure]] — the second under-stressed dimension
- [[volmageddon]] / [[covid-crash]] / [[vix-august-2024-spike]] — the canonical historical replays

## Sources

- [[options-portfolio-construction]] — ITPM-style book construction with explicit stress testing
- [[itpm-framework]] — operational embedding of stress tests in the construction sequence
- [[book-option-volatility-and-pricing]] — Natenberg on Greeks repricing under stress
- [[basel-iii]] — institutional framework for stress testing capital adequacy (regulatory parallel)
- [[ccar]] — Federal Reserve's Comprehensive Capital Analysis and Review, the canonical institutional stress-test programme
- *FRTB (Fundamental Review of the Trading Book)* — Basel framework for ES-based market risk capital, complement to stress testing
