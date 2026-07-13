---
title: "Expected Shortfall"
type: concept
created: 2026-04-15
updated: 2026-06-21
status: excellent
tags: [risk-management, volatility, options, portfolio-theory]
aliases: ["CVaR", "Conditional Value at Risk", "ES", "Expected Shortfall", "Average Value at Risk", "AVaR", "Tail Conditional Expectation"]
related: ["[[var]]", "[[options-stress-testing]]", "[[options-portfolio-construction]]", "[[vega-budgeting]]", "[[theta-targeting]]", "[[options-income]]", "[[short-strangle]]", "[[iron-condor]]", "[[volmageddon]]", "[[vix-august-2024-spike]]", "[[long-vol-vs-short-vol]]", "[[fat-tails]]", "[[risk-management-overview]]"]
domain: [risk-management, portfolio-theory]
prerequisites: ["[[var]]", "[[probability-distributions]]"]
difficulty: advanced
---

**Expected Shortfall (ES)** — also called **Conditional Value-at-Risk (CVaR)**, **Average Value-at-Risk (AVaR)**, or **Tail Conditional Expectation (TCE)** — is the average loss conditional on the loss exceeding a [[var|Value-at-Risk]] threshold. Where VaR answers *"what is the loss I will not exceed with confidence α?"*, expected shortfall answers the harder and more useful question *"if I do exceed the VaR threshold, how bad is it on average?"*. ES is the regulatory standard for trading-book risk under [[frtb|FRTB]] (Fundamental Review of the Trading Book, 2019+) and the natural risk metric for any book — particularly an [[options-income|options income]] book — whose left tail is much fatter than its right.

## Overview

VaR was the dominant trading-book risk number for two decades after J.P. Morgan's 1994 *RiskMetrics* publication, but it has two well-known defects:

1. **It says nothing about the size of losses beyond the threshold.** A 99% one-day VaR of $1M means there is a 1% chance of losing *more than* $1M — but whether "more" is $1.1M or $50M is not in the number.
2. **It is not [[coherent-risk-measure|coherent]].** Specifically, VaR is not subadditive — combining two portfolios can produce a VaR larger than the sum of the two individual VaRs, which is the wrong sign for a sane risk metric. (Diversification should reduce risk, not increase it.) This was proved formally by [[artzner-delbaen-eber-heath|Artzner, Delbaen, Eber, and Heath]] in their 1999 paper *Coherent Measures of Risk* (*Mathematical Finance*, 9(3): 203-228).

Expected shortfall fixes both problems. It captures the average severity of tail events (so it sees the difference between a thin-tailed and fat-tailed distribution at the same VaR), and it is provably coherent under the standard definition (subadditive, monotone, positively homogeneous, translation-invariant). For any book whose loss distribution has appreciable fat tails — short-vol, short-gamma, credit, leveraged carry — ES is a strictly better risk number than VaR.

## Definition / Formula

For a loss random variable $L$ (positive numbers represent losses) and a confidence level $\alpha$ (typically 0.95, 0.975, or 0.99):

$$
\text{VaR}_\alpha(L) = \inf\{ \ell : P(L \le \ell) \ge \alpha \}
$$

$$
\text{ES}_\alpha(L) = \mathbb{E}[\, L \mid L \ge \text{VaR}_\alpha(L) \,]
$$

In words: ES is the expected value of the loss, conditional on the loss being in the worst $(1 - \alpha)$ tail. Equivalently, for a continuous distribution:

$$
\text{ES}_\alpha(L) = \frac{1}{1-\alpha}\int_\alpha^1 \text{VaR}_u(L)\,du
$$

This integral form makes ES the *average* of all VaRs deeper than $\alpha$ — which is why "Average VaR" is one of its names. ES is always at least as large as VaR at the same confidence, and strictly larger whenever the tail has any mass.

### Numerical relationships

Under a normal distribution $L \sim \mathcal{N}(\mu, \sigma^2)$:

$$
\text{ES}_\alpha = \mu + \sigma \cdot \frac{\phi(\Phi^{-1}(\alpha))}{1 - \alpha}
$$

where $\phi$ and $\Phi$ are the standard normal pdf and cdf. Quick reference (zero-mean, unit-variance):

| α     | VaR (z) | ES (z) | ES / VaR ratio |
|-------|---------|--------|----------------|
| 0.95  | 1.645   | 2.063  | 1.25           |
| 0.975 | 1.960   | 2.338  | 1.19           |
| 0.99  | 2.326   | 2.665  | 1.15           |
| 0.995 | 2.576   | 2.892  | 1.12           |

For *normal* distributions the ratio is modest (15-25%). For fat-tailed distributions (Student-t with low degrees of freedom, or empirical equity returns post-2008), the ratio is far larger — often 1.4x to 2.5x at the 97.5% level, and unbounded for distributions whose tails decay slower than $1/\ell^2$. The gap between ES and VaR is itself a measure of how fat-tailed the distribution is.

### ES at 97.5% ≈ VaR at 99% — the FRTB calibration trick

A practically important coincidence drove the FRTB calibration choice. Under a normal distribution, ES at 97.5% (2.338σ) is almost exactly equal to VaR at 99% (2.326σ). This let the Basel Committee swap the metric *without* changing the headline confidence intuition that desks were used to — but the swap is not neutral for fat-tailed books. Under a Student-t with low ν, ES(97.5%) is materially larger than VaR(99%), so the metric switch silently increased the capital charge on exactly the books (short-vol, exotic-correlation) that most needed it.

| Distribution | VaR(99%) | ES(97.5%) | ES(97.5%) − VaR(99%) |
|---|---|---|---|
| Normal | 2.326σ | 2.338σ | ≈ 0 (by design) |
| Student-t (ν=5) | ~2.61σ | ~3.00σ | meaningfully positive |
| Student-t (ν=3) | ~2.62σ | ~3.18σ | large |
| Empirical equity (post-2008 daily) | varies | typically 1.3-1.8× the Gaussian | large |

## Comparison with Other Risk Measures

| Measure | What it answers | Coherent? | Tail-aware? | Notes |
|---|---|---|---|---|
| **Variance / [[volatility|σ]]** | Average dispersion | n/a (symmetric) | No | Penalises upside as much as downside; useless for asymmetric books |
| **[[var\|VaR]]** | Threshold not exceeded with prob α | No (not subadditive) | No (ignores beyond threshold) | Two-decade incumbent; still widely reported |
| **Expected Shortfall / CVaR** | Average loss beyond VaR | **Yes** | **Yes** | FRTB standard; convex objective in optimisation |
| **[[maximum-drawdown\|Max drawdown]]** | Worst peak-to-trough | No | Path-dependent | Backward-looking realised metric, not a forward distributional one |
| **[[semi-deviation\|Semi-deviation]]** | Downside-only dispersion | n/a | Partial | Used in [[sortino-ratio]]; ignores how fat the tail is |
| **Spectral / distortion measures** | Weighted average of quantiles | Yes (with decreasing weights) | Yes | ES is the special case of a spectral measure with a flat tail weight |
| **Entropic VaR (EVaR)** | Chernoff-bound upper proxy | Yes | Yes | Tighter than ES, harder to estimate; emerging in quant work |

ES is the simplest coherent, tail-aware measure that is also a *convex* function of portfolio weights — the property that makes [[mean-cvar-optimization|mean-CVaR optimisation]] a linear program (Rockafellar-Uryasev 2000), unlike VaR minimisation which is non-convex and NP-hard in general.

## Why ES Is Coherent and VaR Is Not

A risk measure $\rho(\cdot)$ is **coherent** (Artzner et al. 1999) if it satisfies:

1. **Monotonicity** — if $L_1 \le L_2$ a.s., then $\rho(L_1) \le \rho(L_2)$. More loss = more risk.
2. **Translation invariance** — adding a riskless cash position $c$ shifts the risk by exactly $c$: $\rho(L + c) = \rho(L) + c$.
3. **Positive homogeneity** — scaling the position scales the risk: $\rho(\lambda L) = \lambda \rho(L)$ for $\lambda \ge 0$.
4. **Subadditivity** — $\rho(L_1 + L_2) \le \rho(L_1) + \rho(L_2)$. Diversification cannot increase risk.

VaR satisfies the first three but **not subadditivity**. The classic counterexample: two independent zero-coupon defaultable bonds, each with 0.7% default probability. Each has a 99% VaR of zero (the chance of default is below the 1% threshold). A portfolio of both has a 99% VaR equal to the loss-given-default of one bond — *more* than zero plus zero. Combining the portfolios produced a worse risk number than holding them apart, which means a VaR-minimising trader would split a book into two desks to artificially lower the total. This is the regulatory disaster mode FRTB explicitly addressed.

ES is provably subadditive (and therefore coherent) for all distributions where the conditional expectation is well-defined. The proof uses the integral representation: an average over a tail region preserves subadditivity in a way that a single quantile does not.

In practice, this matters for any book that is a mixture of tail-binary positions: short-premium options ([[short-strangle]], [[iron-condor]]), short credit, [[short-vol-strategies|short-vol]], or any structure whose loss distribution has a discontinuity at a strike or barrier. VaR can hide concentrated tail risk; ES cannot.

## Computing Expected Shortfall

Three approaches are standard, in order of computational cost and accuracy.

### 1. Historical (empirical) ES

Take the worst $\lceil (1-\alpha) N \rceil$ losses from a window of $N$ historical P&L observations, average them.

```
sorted_losses = sorted(P&L_history, reverse=True)   # losses positive, gains negative
k = ceil((1 - alpha) * N)
ES_alpha = mean(sorted_losses[0:k])
```

- **Pros** — model-free, captures empirical fat tails by construction, no distributional assumption.
- **Cons** — at α = 0.99 with one year of daily data ($N=252$), only ~3 observations enter the tail. Estimate is extremely noisy. Standard practice is to use 4-10 years of data, or supplement with a [[bootstrap-resampling|bootstrap]].

### 2. Parametric ES

Assume a parametric distribution (most commonly Student-t for fat tails, or a [[generalized-pareto-distribution|generalised Pareto]] in [[extreme-value-theory|EVT]]) fitted to historical returns, then evaluate the closed-form ES.

For Student-t with $\nu$ degrees of freedom:

$$
\text{ES}_\alpha = \mu + \sigma \cdot \frac{f_\nu(t_\nu^{-1}(\alpha))}{1 - \alpha} \cdot \frac{\nu + (t_\nu^{-1}(\alpha))^2}{\nu - 1}
$$

- **Pros** — much smaller estimation variance, smooth in α, extrapolates beyond observed data.
- **Cons** — answer is only as good as the distribution. A Gaussian VaR/ES on a fat-tailed book systematically *under-states* tail risk.

### 3. Monte Carlo ES

Simulate $M$ scenarios under a model that captures the relevant risk factors (delta, gamma, vega, vanna, volga; correlations across underlyings; jump processes for crashes), revalue the book under each, take the worst tail.

- **Pros** — handles full-book non-linearity, supports stress-conditioned scenarios, integrates with [[options-stress-testing]].
- **Cons** — computationally heavy, requires enough scenarios to populate the tail (typically $M \ge 10{,}000$ for stable α = 0.99 ES), and is only as good as the underlying model — particularly the jump and correlation assumptions.

For an [[options-portfolio-construction|options book]], Monte Carlo with explicit jump-diffusion (or filtered historical simulation that conditions on volatility regime) is the only approach that captures the [[gamma-explosion|gamma]] and [[volga|volga]] convexity that detonates short-premium books in stress.

## ES for Options Books

Options books have two structural features that make ES the appropriate risk measure:

1. **Asymmetric tails.** Short-premium positions ([[short-strangle]], [[iron-condor]], [[cash-secured-puts]], [[covered-calls]] in stress) have bounded right-tail (the credit collected) and a fat, often unbounded left-tail. The mean-variance summary that VaR implicitly assumes is meaningless for these distributions.
2. **Convexity.** Linear vega understates loss in a [[vega-budgeting|vega shock]] because of [[volga]] (vega-of-vega); linear delta understates loss in a spot shock because of [[gamma]]. ES computed via Monte Carlo with full revaluation captures these second-order effects; VaR at a fixed confidence level often does not.

Concretely, a typical short-strangle book might have a VaR(99%, 1-day) of -3% but an ES(99%, 1-day) of -8% — meaning the *average* of the bad-tail outcomes is more than twice the VaR. In a [[vix-august-2024-spike|VIX spike]] or [[volmageddon|vol detonation]], the realised loss can be 3-4x the VaR because the worst-case tail (which dominates the conditional expectation) is filled with margin-call cascades and forced unwinds.

A practical rule used by [[itpm-trading-philosophy|ITPM]]-aligned and similar discretionary practitioners: **size short-premium positions to ES, not to VaR**. Concretely:

- Set the per-trade and book-level loss budget against expected shortfall at 97.5% or 99%, not at 95% VaR.
- Re-estimate ES weekly, conditioned on the current [[volatility-regime-classification|vol regime]] (a low-VIX regime has different tail dynamics than a high-VIX regime).
- Stress-test by computing ES under explicit scenarios — the [[volmageddon|2018 vol detonation]], the March 2020 COVID crash, the [[vix-august-2024-spike|August 2024 yen-carry unwind]] — and use the worst as a sanity floor.
- If realised ES from a stress scenario exceeds the book's risk budget, the book is too big, regardless of how comfortable the VaR number looks.

## FRTB and the Regulatory Shift

The [[basel-committee|Basel Committee]]'s **Fundamental Review of the Trading Book (FRTB)**, finalised in January 2019 and phased in over the following years, replaced VaR with **Expected Shortfall at the 97.5% confidence level** as the regulatory capital metric for trading-book market risk. Reasons cited:

1. **Coherence.** The regulator wanted a metric that respects diversification and cannot be artificially lowered by splitting a book.
2. **Tail sensitivity.** Post-2008, regulators concluded that VaR systematically understated the tail risk that actually wiped out trading desks (Bear Stearns, Lehman, monoline insurers).
3. **Scaling consistency.** ES at 97.5% is approximately equal to VaR at 99% under the normal distribution but *strictly larger* under fat-tailed distributions — meaning fat-tailed books face higher capital charges, which is the desired incentive.

FRTB also moved to **liquidity-horizon-adjusted ES** — different risk factors (equity vol, single-name credit, exotic correlations) have different unwind horizons, and ES is computed over each factor's appropriate liquidity horizon (10-120 days) rather than a uniform 10-day VaR. This is the core innovation that makes the regulatory metric vaguely realistic for a book that holds illiquid exotic options positions.

For a retail or proprietary trader, the FRTB framework is overkill, but the principle — *measure tail loss, not threshold loss; assume liquidation is slow and adverse; use a coherent metric* — applies at any scale. Anyone running a serious [[options-income|options-income]] book benefits from running the same calculations.

## ES in Portfolio Optimisation (Mean-CVaR)

The single most useful property of ES for portfolio construction is that, unlike VaR, it is a **convex** function of portfolio weights. Rockafellar and Uryasev (2000) showed that minimising CVaR can be cast as a linear program by introducing an auxiliary VaR-threshold variable and a set of scenario slack variables. This means:

- **Mean-CVaR optimisation** is the tail-aware analogue of [[markowitz|mean-variance]] optimisation. Replace variance in the objective with ES, and the efficient frontier becomes a *tail-risk* frontier — maximise return per unit of average tail loss rather than per unit of dispersion.
- Because the program is convex, it has a unique global optimum and solves quickly even for thousands of scenarios — whereas VaR minimisation is non-convex (the VaR surface is riddled with local minima) and intractable at scale.
- It naturally consumes scenario sets — the same Monte Carlo or filtered-historical scenarios used to *measure* ES can be fed directly into the *optimiser*, keeping measurement and allocation consistent.

For an [[options-portfolio-construction|options book]], mean-CVaR with full revaluation is the rigorous way to balance [[theta-targeting|theta income]] against [[vega-budgeting|vega tail risk]] — it produces the position sizes that the qualitative "size to ES" rule approximates by hand.

## Backtesting Expected Shortfall

ES is harder to backtest than VaR because it is a conditional expectation, not a quantile, and a single realised tail loss does not directly "breach" or "not breach" an expectation. The standard tests:

| Test | Idea | Notes |
|---|---|---|
| **Acerbi-Szekely (2014)** | Three direct ES tests comparing realised tail losses to predicted ES, without requiring the underlying distribution | The de-facto standard since FRTB; Z-tests on the tail |
| **McNeil-Frey (2000)** | Test that VaR exceedance residuals (loss minus ES, on breach days) have zero mean | Conditional on a VaR breach; requires enough breaches to be powerful |
| **Elicitability critique (Gneiting 2011)** | ES is *not* elicitable on its own (no scoring function makes the true ES the unique minimiser), unlike VaR | Resolved by Fissler-Ziegel (2016): (VaR, ES) are **jointly** elicitable — backtest the pair, not ES alone |

The practical takeaway: never report an ES number without some validation. The most common operational failure (see Limitations #5) is to compute an elaborate Monte Carlo ES and never check whether realised tail losses are consistent with it. A simple Acerbi-Szekely Z-test on the last few years of breaches is the minimum diligence.

## Worked Example

A trader runs a $250{,}000 [[short-strangle]] book on SPX, sized to a vega budget of -$1{,}500/IV-point. Daily mark-to-market P&L over 10 years (~2{,}500 sessions) shows the following empirical distribution of one-day losses:

| Quantile | Empirical loss |
|----------|---------------|
| 50%      | -$70 (small daily theta gain, but flipped to loss on bad days) |
| 95%      | -$2{,}100 |
| 99%      | -$6{,}400 |
| 99.5%    | -$11{,}000 |
| 99.9%    | -$32{,}000 |

**VaR(99%) = $6{,}400.**

The 1% tail contains 25 daily P&L observations. Their average is **$14{,}800**. So **ES(99%) = $14{,}800** — more than 2.3x the VaR. The 25 observations include the [[volmageddon|February 2018 detonation]] (-$58{,}000), the COVID crash period (-$45{,}000 worst day), and the [[vix-august-2024-spike|August 2024]] event (-$28{,}000).

**Interpretation.** The trader's intuition based on VaR — "I lose more than $6{,}400 only 1% of the time, that's manageable" — is correct in frequency but wildly wrong in *severity*. When the trader does break the VaR threshold, the average loss is more than twice the threshold, and the worst loss in the dataset is nearly 10x. A book sized so that VaR represents 2.5% of capital is, in ES terms, sized so that the average bad day represents nearly 6% of capital — and the worst day in a decade represents 23% of capital.

The risk-budget conclusion: this book is too large by a factor of roughly 2 if the trader's true tolerance is "no more than 5% loss on a bad day." Sizing to ES rather than VaR produces a halved book, which is exactly the discipline that [[options-portfolio-construction|professional options portfolio construction]] enforces.

## Common Misuse / Limitations

1. **Estimation noise at high α.** ES at 99% with one year of daily data has a standard error often exceeding 30% of the point estimate. Anyone reporting "ES = $X" without a confidence band is presenting noise as signal. Use multi-year windows, bootstrap CIs, or parametric/EVT estimates.
2. **Distributional assumption smuggling.** A Gaussian-fitted ES on an obviously fat-tailed P&L distribution is no better than VaR — sometimes worse, because it carries the air of sophistication. ES inherits the model's tail. Use Student-t, EVT, or empirical methods.
3. **Static ES on a regime-conditional book.** Realised ES is not stationary. A short-premium book has very different ES in a 12-VIX regime than in a 22-VIX regime. Computing ES on a 10-year average ignores regime-dependence and produces a number that is too high in calm periods and too low in stressed ones. [[volatility-regime-classification|Regime-conditioned]] ES is the correct refinement.
4. **Ignoring liquidity.** A 1-day ES assumes the book can be unwound at mark in one day. In a real stress event, bid-ask blows out, dealers pull quotes, and the realised exit cost is much larger than the model assumes. FRTB's liquidity-horizon ES is the regulatory response; in practice, multiplying short-horizon ES by a realistic liquidity factor (1.5x for liquid index, 3-5x for illiquid single-name OTM) is a reasonable haircut.
5. **Backtesting difficulty.** Unlike VaR, ES is not directly testable via simple breach counts (because it's a conditional expectation, not a quantile). Backtesting requires more sophisticated tests — Acerbi-Szekely, McNeil-Frey — and many practitioners skip the backtest step and quietly assume the ES estimate is correct. This is the most common operational failure mode of ES in practice.
6. **Tail correlation creep.** ES on individual positions does not aggregate cleanly when correlations are themselves regime-dependent. Single-name and index ES computed in calm regimes both understate the joint ES in a panic, when correlations spike to ~1. The fix is to compute ES jointly under stressed correlations, not to sum individual ES.
7. **False precision.** Reporting ES to four significant figures invites confidence the number does not deserve. Treat ES as an order-of-magnitude tool: a book whose ES is "around $15K" vs "around $50K" is a meaningful difference; a book whose ES is "$15{,}231" is a fabricated precision.

## Related

- [[var]] — the threshold-loss measure ES extends and replaces.
- [[options-stress-testing]] — scenario-based companion methodology; ES summarises the tail of stress outputs.
- [[options-portfolio-construction]] — how to size a book against ES rather than against premium received.
- [[vega-budgeting]] — the strategic constraint; ES quantifies what a vega budget breach actually costs.
- [[theta-targeting]] — the income side; ES is the tail-risk side.
- [[options-income]] — the strategy class whose left-tail ES dominates its evaluation.
- [[short-strangle]] / [[iron-condor]] / [[covered-calls]] / [[cash-secured-puts]] — premium-selling structures with fat left-tails best measured by ES.
- [[volmageddon]] / [[vix-august-2024-spike]] — historical detonations that show the realised ES of unhedged short-vol books.
- [[long-vol-vs-short-vol]] — the Spitznagel-style critique of measuring short-vol risk by anything other than a tail metric.
- [[fat-tails]] / [[extreme-value-theory]] — the underlying distribution theory.
- [[coherent-risk-measure]] — the axiomatic framework ES satisfies and VaR does not.
- [[mean-cvar-optimization]] — the convex portfolio-optimisation method ES enables.
- [[markowitz]] / [[sortino-ratio]] — the variance- and semi-deviation-based measures ES improves on.
- [[maximum-drawdown]] — the realised path-dependent counterpart to forward ES.
- [[frtb]] — the regulatory shift to ES in 2019+.
- [[risk-management]] / [[risk-management-overview]]

## Sources

- Artzner, P., Delbaen, F., Eber, J.-M., and Heath, D. (1999). *Coherent Measures of Risk*. *Mathematical Finance*, 9(3): 203-228. The foundational paper introducing the coherent-risk-measure framework and proving that VaR is not subadditive.
- Acerbi, C., and Tasche, D. (2002). *On the Coherence of Expected Shortfall*. *Journal of Banking and Finance*, 26(7): 1487-1503. Establishes that ES is coherent under standard regularity conditions.
- Basel Committee on Banking Supervision (2019). *Minimum Capital Requirements for Market Risk* (FRTB). The regulatory text moving from VaR to ES at 97.5% with liquidity-horizon adjustments.
- McNeil, A. J., Frey, R., and Embrechts, P. (2015). *Quantitative Risk Management*. Princeton. Standard reference for ES estimation, EVT methods, and backtesting.
- Rockafellar, R. T., and Uryasev, S. (2000). *Optimization of Conditional Value-at-Risk*. *Journal of Risk*, 2: 21-41. Formalises CVaR as a convex objective for portfolio optimisation.
- Acerbi, C., and Szekely, B. (2014). *Backtesting Expected Shortfall*. *Risk* magazine. The three direct ES backtests adopted under FRTB.
- Gneiting, T. (2011). *Making and Evaluating Point Forecasts*. *JASA*. The elicitability result showing ES is not elicitable on its own.
- Fissler, T., and Ziegel, J. (2016). *Higher Order Elicitability and Osband's Principle*. *Annals of Statistics*. Establishes joint elicitability of (VaR, ES).
- [[book-option-volatility-and-pricing]] — Natenberg on tail risk in short-premium books.
