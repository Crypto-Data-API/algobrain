---
title: "Scenario Analysis"
type: concept
created: 2026-05-07
updated: 2026-06-21
status: excellent
tags: [risk-management, options, portfolio-theory, derivatives, volatility]
aliases: ["Scenario Analysis", "What-If Analysis", "Scenario Pricing"]
related: ["[[stress-test]]", "[[historical-stress-test]]", "[[reverse-stress-test]]", "[[value-at-risk]]", "[[expected-shortfall]]", "[[options-risk-budgeting]]", "[[options-portfolio-construction]]", "[[portfolio-greeks-aggregation]]", "[[monte-carlo-simulation]]", "[[options-greeks]]", "[[implied-volatility]]", "[[volatility-skew]]", "[[volatility-term-structure]]", "[[black-scholes-model]]", "[[vega-budgeting]]", "[[theta-targeting]]"]
domain: [risk-management]
prerequisites: ["[[options-greeks]]", "[[implied-volatility]]"]
difficulty: intermediate
---

Scenario analysis is the practice of re-pricing a portfolio under a defined set of *what-if* moves — spot shocks, IV shifts, time decay, rate moves, or any combination — and reporting the P&L at each cell of the resulting grid. The output is a **scenario surface**: a multi-dimensional table of book P&L as a function of the input variables. It is the broader operational tool of which [[stress-test|stress testing]] (focused on tail and adverse scenarios) is one specialised application; the same machinery is also used for routine *event planning* ("what happens if the Fed delivers 50bp instead of 25bp?"), [[options-portfolio-construction|position sizing]], and [[options-risk-budgeting|risk-budget]] verification.

## Overview

Scenario analysis answers a different question from [[value-at-risk|VaR]] or [[expected-shortfall|ES]]. VaR collapses the loss distribution to a single percentile; ES collapses the tail to a single average; scenario analysis preserves the full *if-this-then-that* mapping that a trader needs to make pre-commitment decisions. A book might have an acceptable VaR and a tolerable ES while still having one specific scenario — say, "FOMC delivers a hawkish surprise *and* the dollar rallies 1%" — that produces an unacceptable loss. VaR and ES will hide that cell; the scenario grid surfaces it.

The technique has three stable use-cases, each with a different emphasis:

1. **Pre-trade planning.** Before adding a candidate position, re-run the book under a fixed grid (e.g., spot ±5/±10/±20%, IV ±5/±10/±20 points) and verify the candidate does not push any cell outside the [[options-risk-budgeting|risk budget]]. The adverse cells are the [[stress-test|stress test]]; the benign cells are the *upside* scenario showing what the book makes if the thesis plays out.
2. **Event hedging.** Before a known catalyst (CPI release, FOMC, earnings, election), enumerate plausible event outcomes — base case, hawkish, dovish, tail — and price the book under each. The grid tells the trader which outcomes leave them comfortable and which require pre-positioning.
3. **Continuous monitoring.** Run the same grid daily on the live book. Drift in the worst cell, even with no new positions, is a signal that the Greeks have moved and the book has implicitly re-budgeted itself.

The technique is universal across asset classes — fixed-income desks scenario-test rate moves, FX desks test dollar-index moves, options desks test spot × IV grids — but it is most powerful for [[options-portfolio-construction|options books]] because the non-linear payoff means linear approximations (delta × move) are wrong by exactly the amount that matters.

## Definition / Mechanics

### What a scenario is

A *scenario* is a deterministic, joint specification of new values for the variables the portfolio is exposed to. For an options book, the canonical variables are:

- **Spot** — price of each underlying (or a shock to a benchmark with beta-weighted propagation).
- **Implied volatility** — surface-wide shift, with optional skew and term-structure components.
- **Time** — horizon over which the scenario plays out (instantaneous, 1 day, 5 days).
- **Rates** — risk-free curve shift; relevant for long-dated and rate-sensitive options.
- **Dividends / borrow** — for single-name books; rarely material for index books.
- **Correlations** — for multi-asset books; the most under-stressed dimension.

A *scenario grid* (or *scenario surface*) is the Cartesian product of values along two or three of these axes. The most useful 2-D grid for an equity-options book is **spot × IV**, with rows being percentage spot moves and columns being IV-point shifts. Each cell of the grid is the book's P&L re-priced under that joint shock.

### What scenario analysis is *not*

It is helpful to anchor the definition by contrast:

| Tool | What it produces | Inputs |
|---|---|---|
| **Scenario analysis** | A grid of P&L over chosen joint shocks. Deterministic. | Operator-chosen shocks; pricing model. |
| **[[stress-test]]** | A subset of scenarios chosen to be adverse / extreme. | Same as scenario analysis, restricted to tail. |
| **[[reverse-stress-test]]** | The smallest shock that produces a chosen unacceptable loss. | A loss limit; sweep over the grid. |
| **[[value-at-risk\|VaR]]** | A single percentile of the loss distribution. | Distribution assumption; covariance. |
| **[[expected-shortfall\|ES]]** | The average loss in the tail beyond VaR. | Distribution; tail percentile. |
| **[[monte-carlo-simulation]]** | A simulated distribution of outcomes. | Stochastic process; many random draws. |
| **[[backtesting]]** | Historical track record of an executed strategy. | Real or simulated past trades. |

Scenario analysis is the most *transparent* of these — every cell of the grid is auditable and explainable to a risk committee or to oneself the morning after a loss. Its weakness is that scenarios are *chosen* rather than sampled, so the framework gives no information about the *probability* of the bad cells. Combine with VaR/ES for that.

### Greeks repricing under each cell

For an options book, each scenario cell requires more than multiplying by current Greeks. The book must be *re-priced*: every option re-quoted at the new (spot, IV, time, rates) inputs using the [[black-scholes-model|pricing model]]. This is essential because Greeks themselves change with the inputs:

- A short put with delta -10 at current spot has delta -25 at -5% spot.
- Vega scales with the level of IV — `vol-of-vol` matters in vol-up scenarios.
- Theta accelerates near expiry — the same horizon is a different fraction of remaining time on each position.

A scenario tool that holds Greeks constant ("delta × move + vega × IV-shift + theta × dt") is doing a Taylor approximation; it is wrong precisely in the cells where the answer matters.

## Methodology / How To Apply

### Step 1 — Choose the axes

A standard equity-options grid has two axes:

- **Spot axis**: -20%, -10%, -5%, 0%, +5%, +10%, +20% (or finer). Beta-weighted across underlyings if the book is multi-name.
- **IV axis**: -10, -5, 0, +5, +10, +20, +50 IV points. Applied as a parallel shift to the surface, with optional skew/term overlays.

Less often, a third axis is added:

- **Time** (instantaneous vs +1 day vs +5 days) — important when theta is large relative to gamma (short-premium books).
- **Skew** — applied as a shift to the 25Δ-put-minus-call differential. Worth a separate dimension on books with material wing exposure.

Three axes mean the grid is `7 × 7 × 3 = 147` cells. Most desks reduce this by running the spot × IV grid at one or two horizons rather than three.

### Step 2 — Choose scenario realism

The grid range should bracket *plausible* moves, calibrated to the book's holding period. For a daily-rebalanced book, the spot range should bracket ±2σ moves; for a weekly book, ±2σ over a week (which is wider). A guideline:

- Daily horizon: spot ±2-3% mild, ±5% moderate, ±10% severe.
- Weekly horizon: spot ±5% mild, ±10% moderate, ±20% severe.
- Monthly horizon: spot ±10% mild, ±20% moderate, ±40% severe.

The IV axis should similarly scale: 5 points is a normal day's range, 20 points is a moderate event, 50 points is a tail. Combining "+50 IV with -10% spot" is the canonical short-vol stress (see [[stress-test]]).

#### Catalyst-specific axis recipes

For *event hedging* the generic spot × IV grid is replaced with axes calibrated to the specific catalyst. The discipline is the same — re-price the book under each cell — but the ranges are tuned to how the catalyst actually moves the surface. The figures below are illustrative starting points, not forecasts.

| Catalyst | Spot axis (illustrative) | IV axis (illustrative) | Special dimension |
|---|---|---|---|
| [[fomc\|FOMC]] decision | ±0.5% / ±1.5% / ±3% | front-month IV −5 / 0 / +5 | Rate-curve shift; the *dots* surprise |
| CPI / payrolls | ±0.5% / ±1.5% / ±2.5% | −3 / 0 / +8 | Often a sharp IV crush after the print |
| Single-name earnings | ±implied move ×{0.5, 1, 1.5, 2} | front-week IV −40 / −20 / 0 | The [[earnings-iv-crush\|IV crush]] dominates; see [[earnings-volatility-trading]] and [[implied-earnings-move]] |
| Election / referendum | ±2% / ±5% / ±10% | −10 / 0 / +20 | Multi-day path; overnight gap risk |
| Geopolitical / oil shock | ±3% / ±7% / ±15% | 0 / +15 / +40 | Cross-asset (oil, USD, gold) |
| Index rebalance / OPEX | ±0.5% / ±1.5% | −5 / 0 / +5 | [[pin-risk\|Pinning]] and dealer-gamma flow |

The earnings row is the clearest example of why a catalyst-specific grid matters: a generic "+IV" stress is exactly backwards for an earnings event, where the dominant move is a *collapse* in front-week IV. A book that screens clean on a generic vol-up grid can still be badly exposed to the post-earnings vol-down move.

### Step 3 — Build or use the tool

Several tools expose scenario analysis directly:

- **[[thinkorswim]] Analyze tab** — supports custom slices of the surface; built-in spot/IV slider; beta-weights to SPX. Standard retail tool.
- **[[interactive-brokers|IBKR]] Risk Navigator** — full Greeks repricing across the book under custom scenarios; supports historical-event replay.
- **OptionNet Explorer** — granular what-if for a defined book, including time-forward scenarios over several days.
- **[[orats]]** — historical surfaces for replay; can run scenarios using surfaces from prior dates.
- **Custom Python** — for sophisticated books, the standard stack is QuantLib (pricing engine), pandas (grid), and a fitted vol-surface (e.g., SVI, SABR) so the scenarios can shift skew/term-structure realistically. py_vollib is the lightweight alternative for fast Greeks repricing.
- **Bloomberg OVME / OVRA** — institutional desks; full-surface scenarios with derivatives modelling.

A homemade tool is fine for individual books; the discipline matters more than the platform. The minimum requirement is that scenarios *re-price* (not Taylor-approximate) and that the grid output is comparable across days.

### Step 4 — Read the grid

A useful daily report visualises the grid as a heat-map: green for positive cells, red for negative, intensity scaling with magnitude. The trader looks for:

- **The single worst cell.** Compare to the [[options-risk-budgeting|tail-risk budget]]. If the worst cell is wider than the budget, cut size before next session.
- **The shape of the surface.** A book that is positive in the centre and negative in all corners is short-volatility; a book that is positive in the corners and negative in the centre is long-volatility. Compare to the trader's stated thesis — mismatches reveal unintended exposure.
- **Asymmetry.** A book that loses more in the down-spot/IV-up corner than in the up-spot/IV-down corner has skew and vanna exposure even if delta is flat. Verify this is intentional.
- **Time decay shape.** Compare today's grid to yesterday's — the difference is the *theta plus drift* of the book. If the worst cell got worse without an explicit position change, the position has decayed in a way that requires action.

#### Diagnosing the book from the grid's shape

The geometry of the heat-map is itself a read on the book's hidden exposures. Use this as a quick diagnostic — a mismatch between the shape and the trader's stated thesis is the most common way scenario analysis surfaces *unintended* risk.

| Grid shape | What it reveals | Dominant Greeks |
|---|---|---|
| Green centre, red corners | Short volatility | Short [[vega]], short [[gamma]] |
| Red centre, green corners | Long volatility | Long [[vega]], long [[gamma]] |
| Tilted (worse in down-spot/IV-up corner) | Short the put wing / negative [[volatility-skew\|skew]] exposure | Vanna, skew |
| Diagonal stripe | Strong directional ([[delta]]) tilt | Net delta dominates |
| Symmetric bowl, deepens with IV | Pure short-vega, skew-neutral | Vega without skew |
| One catastrophic corner | A single uncapped tail (e.g., naked [[short-strangle]]) | Short gamma in the tail |

## Worked Example

**Book**: $250k SPX-only options book.

- Net delta: +120 (beta-weighted)
- Net gamma: -150
- Net vega: -$800/IV pt
- Net theta: +$95/day
- Drawdown limit: -15% NAV = -$37,500.

**Grid**: spot ×{-20, -10, -5, 0, +5, +10}%; IV ×{-10, 0, +10, +20, +50} points; horizon = 1 day.

| Spot \ IV | -10 | 0 | +10 | +20 | +50 |
|---|---:|---:|---:|---:|---:|
| -20% | +$3,200 | -$28,000 | -$58,500 | -$83,400 | **-$152,000** |
| -10% | +$1,400 | -$10,500 | -$23,400 | -$31,500 | -$48,600 |
| -5% | +$650 | -$3,800 | -$11,200 | -$15,800 | -$28,500 |
| 0% | +$8,300 | +$95 | -$7,800 | -$15,500 | -$38,500 |
| +5% | +$3,200 | -$2,100 | -$10,400 | -$17,800 | -$40,200 |
| +10% | -$8,500 | -$14,500 | -$22,800 | -$30,000 | -$52,300 |

**Reading the grid**:

- *Centre cell* (0%, 0): +$95 = today's theta. Check.
- *Best cell* (0%, -10): +$8,300. The book makes money in a calm vol crush — confirms it is short-vol.
- *Worst cell* (-20%, +50): -$152,000 = -61% of NAV. Dramatically outside the -15% drawdown limit.
- *Worst cell within plausible range* (-10%, +20): -$31,500 = -12.6%. Inside the limit but close.
- *Asymmetry*: the (-10%, +50) and (+10%, +50) cells are -$48k and -$52k respectively — roughly symmetric, which says the book has limited skew bias. If those numbers were -$48k and -$15k, the book would be heavily short the put wing.

**Action**: the book passes most plausible cells but fails the deep-tail combined shock. The trader runs a [[reverse-stress-test]]: *what is the smallest cell that produces -15% NAV?* Sweep finds it at approximately spot -10%, IV +25, which has happened roughly 4-6 times in the trailing decade. Conclusion: cut net vega by ~30% before next session.

The same grid run for an [[fomc|FOMC]] event would replace the IV axis with a FOMC-specific shock (e.g., front-month IV +5 / +0 / -5 representing surprise-hawk / consensus / dovish) and the spot axis with a calibrated reaction range (e.g., ±0.5% / ±1.5% / ±3%). The same machinery, different ranges.

## Limitations / Common Pitfalls

1. **Choosing scenarios that confirm the thesis.** A trader long volatility who only stress-tests vol-up scenarios will see green grids and conclude the book is safe. The grid must include adverse-thesis cells.
2. **Holding Greeks constant in the grid.** The most common failure mode. A grid built by Taylor expansion `(δ + γ × ΔS + …)` is materially wrong in any cell with a large move — and the large-move cells are the ones the grid exists to catch. Always re-price.
3. **Ignoring liquidity in the cells.** A grid that says "loss in the worst cell is -$30k at theoretical mid" understates the realised loss because exit at theoretical mid is impossible in stress regimes. Apply a liquidity haircut (e.g., effective bid-ask 50% wider) to scenario cells beyond moderate magnitude. See [[liquidity-risk]].
4. **Using a parallel-IV shift on a skewed-position book.** A book heavy in put wings is most exposed to *skew* steepening, not parallel IV. The right grid for that book is spot × skew or spot × put-wing-IV, not spot × ATM-IV.
5. **Running the grid only at trade entry.** A book's Greeks drift; a grid clean at entry can degrade by day 10 as gamma builds or vega concentrates near a single expiry. Run the grid daily; treat any single-day worsening of the worst cell as a signal.
6. **Treating the grid as a probability statement.** Scenario analysis says nothing about the probability of any cell. The cell that loses $50k might be once-a-decade or once-a-year — the grid does not say. Combine with [[value-at-risk]], [[expected-shortfall]], or historical replay (see [[historical-stress-test]]) to attach probabilities.
7. **Single-asset grids on a multi-asset book.** Scenario analysis on the equity book that ignores the rate book and FX book misses correlations. For multi-asset books, the grid should include cross-asset shocks (e.g., spot down + dollar up + rates up).
8. **Static scenarios in a regime-shift world.** A scenario set calibrated in a 14-vol regime is wrong in a 35-vol regime — both the magnitude scale and the joint dynamics change. Recalibrate the grid quarterly or whenever realised vol crosses a regime boundary.

## Related

- [[stress-test]] — adverse-scenario subset of scenario analysis
- [[historical-stress-test]] — scenario analysis using historical event moves
- [[reverse-stress-test]] — the inverse formulation
- [[value-at-risk]] — distribution-based metric, complement to scenario analysis
- [[expected-shortfall]] — tail-conditional expectation, complement
- [[monte-carlo-simulation]] — stochastic alternative to deterministic scenarios
- [[options-risk-budgeting]] — the budget the scenario grid verifies
- [[options-portfolio-construction]] — the construction process the grid informs
- [[portfolio-greeks-aggregation]] — Greeks must be aggregated before scenarios are run
- [[options-greeks]] — variables being shocked
- [[implied-volatility]] — the most important scenario axis for options books
- [[volatility-skew]] — under-shocked dimension
- [[volatility-term-structure]] — under-shocked dimension
- [[black-scholes-model]] — repricing engine
- [[vega-budgeting]] — budget enforced by the IV axis of the grid
- [[theta-targeting]] — uses scenario grids in the sizing loop

## Sources

- [[itpm-trade-construction-playbook]] — practitioner workflow embedding scenario analysis
- [[options-portfolio-construction]] — book construction with scenario grids
- Hull, *Options, Futures, and Other Derivatives* — chapter on scenario analysis vs VaR
- Jorion, *Value at Risk* (3rd ed.) — VaR vs scenario analysis comparison
- Basel Committee on Banking Supervision, *Principles for sound stress testing practices and supervision* (2009) — institutional guidance on scenario design
- *FRTB (Fundamental Review of the Trading Book)* — Basel framework for ES-based market risk capital, complementary to scenario testing
- CME Group SPAN methodology — exchange-level scenario testing for margin
