---
title: "Geometric Mean Return"
type: concept
created: 2026-05-07
updated: 2026-06-21
status: excellent
tags: [portfolio-theory, statistics, risk-management, performance]
aliases: ["Geometric Mean", "Compound Annual Growth Rate", "CAGR", "Geometric Return"]
domain: [portfolio-theory, statistics]
difficulty: beginner
prerequisites: ["[[compounding]]"]
related: ["[[compounding]]", "[[kelly-criterion]]", "[[ergodicity]]", "[[ergodicity-economics]]", "[[ole-peters]]", "[[sharpe-ratio-pitfalls]]", "[[gaussian-assumption]]", "[[negative-skew]]", "[[fat-tails]]", "[[long-vol-vs-short-vol]]", "[[volmageddon]]"]
---

The geometric mean return is the constant per-period growth rate that, applied repeatedly, produces the same terminal wealth as the actual sequence of returns. It is the **only mean** that correctly describes how an investor's wealth compounds; the arithmetic mean systematically over-states the growth rate that any single investor experiences. The gap between the two -- approximately `0.5 * σ²` for moderate volatility -- is called **variance drag** or **volatility tax** and is the foundational reason that leverage on a positive-arithmetic-return strategy can still produce ruin.

## Overview

If wealth evolves as `W_t = W_0 * Π (1 + r_i)`, then by definition the **geometric mean return** `g` is the value such that:

```
(1 + g)^T = Π_{i=1}^T (1 + r_i)
```

Equivalently, the geometric mean is the **arithmetic mean of log-returns**:

```
g = exp((1/T) * Σ ln(1 + r_i)) - 1
```

For long-horizon practical use, the **annualized geometric return** is what is reported as "CAGR" (compound annual growth rate) in fund factsheets:

```
CAGR = (W_T / W_0)^(1/years) - 1
```

The arithmetic mean, by contrast, simply averages the per-period returns:

```
arithmetic_mean = (1/T) * Σ r_i
```

For any non-trivial volatility, the arithmetic mean **strictly exceeds** the geometric mean. Equality holds only when all returns are identical.

## The AM ≥ GM Inequality

The relationship between arithmetic and geometric means is not an empirical regularity — it is a **mathematical theorem**. For any set of non-negative numbers `x_1, …, x_n` (here, gross returns `1 + r_i`):

```
(1/n) Σ x_i  ≥  (Π x_i)^(1/n)
arithmetic mean  ≥  geometric mean
```

with equality if and only if all `x_i` are equal. The proof follows from Jensen's inequality applied to the concave logarithm function: `E[ln X] ≤ ln E[X]`. Because `ln` is strictly concave, the gap is strictly positive whenever there is any dispersion in returns. This is why a trader can **never** experience the arithmetic mean as a compounded growth rate over more than one period — the math forbids it.

The size of the gap is governed by the dispersion (variance) of returns. The richer the variance, the wider the wedge:

| Return dispersion | AM − GM gap (≈ `0.5 σ²`) | Practical reading |
|---|---|---|
| Zero (constant return) | 0 | AM = GM exactly |
| Low (σ = 10%) | ~0.50% | Negligible drag |
| Moderate (σ = 20%) | ~2.0% | Meaningful over decades |
| High (σ = 40%) | ~8.0% | Severe — most "alpha" can be drag |
| Extreme (σ = 80%) | ~32% | Strategy can have positive AM and negative GM |

The last row is the danger zone for leveraged, short-vol, and crypto strategies: a positive arithmetic edge that compounds to ruin. See [[volatility-drag]] and [[kelly-criterion]].

## Why It Matters

A trader compounding capital cares about terminal wealth. Terminal wealth is determined by the geometric mean. The arithmetic mean is the right number for a one-period decision over independent identically-distributed gambles, **but no real investor faces that situation** -- real investors compound across periods, and the geometric mean is the relevant quantity (see [[ergodicity]] and [[ergodicity-economics]]).

Three concrete consequences:

1. **Volatility eats compounding.** Two strategies with the same arithmetic mean but different volatilities have different terminal wealths -- the lower-vol strategy compounds more.
2. **Drawdowns are punished asymmetrically.** A 50% drawdown requires a 100% gain to break even. This asymmetry is the geometric-mean dynamic at work.
3. **Leverage has a finite optimum.** Beyond a certain point, additional leverage raises arithmetic return but lowers geometric return. See [[kelly-criterion]].

## Formula and the Variance Drag Approximation

For log-normally distributed returns with arithmetic mean μ and standard deviation σ (per period):

```
g ≈ μ - 0.5 * σ^2
```

This is the **variance drag** identity. Each percentage point of volatility-squared shaves off half a percent of geometric return. The exact relationship for log-normal returns:

```
g = exp(μ_log) - 1
   ≈ μ - 0.5 * σ^2
```

where `μ_log` is the mean of log-returns. The `0.5 σ^2` correction follows from Itô's lemma applied to geometric Brownian motion and is the same drag that appears in the [[black-scholes]] PDE.

For higher-order accuracy under non-Gaussian returns, the cumulant expansion adds terms for skewness and kurtosis:

```
g ≈ μ - 0.5 * σ^2 + (skew/6) * σ^3 - (excess_kurt/24) * σ^4
```

[[Negative-skew]] strategies suffer additional drag beyond the variance term; positive-skew strategies receive a small boost. This is part of why naive Sharpe ratio reporting -- which doesn't capture higher-moment effects -- misallocates capital. See [[sharpe-ratio-pitfalls]].

### The volatility-drag decomposition

The `0.5 σ²` term is known by several names depending on context — **variance drag**, **volatility tax**, **volatility drain**, or simply the **Itô correction**. It is the same quantity in every domain:

| Domain | Where the `−0.5 σ²` term appears | Interpretation |
|---|---|---|
| Compounding (this page) | `g ≈ μ − 0.5 σ²` | Geometric vs arithmetic return gap |
| [[black-scholes]] PDE | Drift of log-price under GBM | Risk-neutral log-drift correction |
| [[kelly-criterion]] | `g(f) = f·μ − 0.5 f²σ²` | Growth rate as a function of leverage `f` |
| [[ergodicity]] | Time-average ≠ ensemble-average | The non-ergodicity of multiplicative growth |
| Leveraged ETFs | Daily-rebalanced decay | Why a 3× ETF lags 3× the index over time |

The unifying point: **wherever wealth compounds multiplicatively, volatility is a direct subtraction from the achievable growth rate**, not merely a measure of uncertainty around it. See [[volatility-drag]] for the dedicated treatment and [[long-vol-vs-short-vol]] for the strategic implications.

## Worked Example

### Two strategies, same arithmetic mean, different volatility

| | Strategy A (low vol) | Strategy B (high vol) |
|---|---|---|
| Arithmetic mean (annual) | 8% | 8% |
| Annual volatility | 10% | 25% |
| Variance drag (`0.5 σ²`) | 0.50% | 3.13% |
| Approx. geometric mean | 7.5% | 4.9% |
| Terminal wealth after 30 yrs | 8.75x | 4.21x |

The two strategies look identical on arithmetic mean. After 30 years, the low-vol strategy compounds to **2x more terminal wealth** than the high-vol strategy. This gap is pure volatility tax -- no skill difference whatsoever.

### Drawdown asymmetry

Suppose a strategy returns +20% in year 1 and -20% in year 2. Arithmetic mean: 0%. Geometric mean:

```
g = sqrt(1.20 * 0.80) - 1 = sqrt(0.96) - 1 ≈ -2.02%
```

Terminal wealth is below starting wealth despite a "zero average return". This is the drawdown asymmetry -- the gain to recover from a 20% loss is 25%, not 20%.

### The Kelly-criterion connection

Suppose you can bet on a positive-edge coin flip: 60% chance of doubling your stake, 40% chance of losing it. Optimal Kelly fraction is `f* = 2p - 1 = 0.20`. Compare three sizing choices:

| f | Arithmetic E[r] per round | Geometric (time-average) g |
|---|---|---|
| 0.10 | +6% | +5.97% |
| 0.20 (Kelly) | +12% | **+12.96%** (peak) |
| 0.40 | +24% | +1.93% |
| 0.60 | +36% | -16.5% (negative!) |
| 1.00 (full bet) | +60% | -infinity (ruin) |

At 60% Kelly fraction, the arithmetic expectation is enormous (+36% per round), but the geometric growth rate is negative -- the trader's wealth shrinks in time. The arithmetic mean is misleading; the geometric mean is what determines whether the trader survives. See [[kelly-criterion]] and [[ergodicity-economics]].

## Decision Table: Which Mean to Use

| Question being answered | Correct mean | Why |
|---|---|---|
| Expected value of a single, independent bet | Arithmetic | One-period EV is linear in probabilities |
| Long-run growth rate of compounded capital | **Geometric** | Terminal wealth is multiplicative |
| Position size that maximizes terminal wealth | **Geometric** (maximize log-growth) | This *is* [[kelly-criterion|Kelly]] |
| Headline "average annual return" in marketing | Arithmetic (often) | Higher number; flatters the manager |
| Honest "what did $1 become" statement | **Geometric** (CAGR) | The only number an investor actually realizes |
| Forward Monte Carlo of terminal wealth | Geometric drift in the generator | Avoids systematically over-stating outcomes |
| Equity risk premium for discounting | **Geometric** for multi-period | Arithmetic over-states forward wealth |
| Mean-variance optimizer input | Arithmetic (but adjust) | Optimizer uses AM; variance penalty *proxies* the GM correction |

The single operating rule: **arithmetic for one-period decisions, geometric for anything that compounds.** Almost all real trading compounds.

## The Gaussian-Assumption Trap

Many practitioner formulas implicitly use arithmetic returns where geometric returns belong:

- **CAPM and equity-risk-premium estimation** often quote arithmetic-mean equity premia. The geometric premium is roughly 1.5-2 percentage points lower. Models that use the arithmetic premium for forward projection over-state expected wealth.
- **Sharpe ratio** uses arithmetic mean returns. Two strategies with the same Sharpe can have different geometric returns, and the geometric is what compounds. See [[sharpe-ratio-pitfalls]].
- **Modern portfolio theory** uses arithmetic returns in mean-variance optimization. The optimizer rewards diversification partly because diversification reduces variance and therefore *raises geometric return* -- but the optimizer itself is computing the wrong objective.

The right operating principle: **arithmetic for one-period decisions, geometric for compounding decisions**. Almost all real trading is the second case.

## Common Misuse

- **Reporting CAGR alongside arithmetic stats without flagging which is which.** Some fund reports quote arithmetic mean returns ("average annual return of 12%") and CAGR ("growth of $1 to $X") side by side, and casual readers conflate them. The arithmetic mean is always higher.
- **Annualizing monthly returns by multiplying.** A monthly arithmetic mean of 1% does **not** annualize to 12%. The geometric annualization is `(1.01)^12 - 1 = 12.68%`. The two are close at low volatility but diverge with vol.
- **Using arithmetic returns in forward Monte Carlo.** A simulation that draws returns from `N(arithmetic_mean, σ)` and compounds them generates trajectories whose **median** is below the input mean -- because the simulation correctly compounds and the input mean was the wrong number to use. This produces apparently pessimistic terminal-wealth results that confuse practitioners.
- **Ignoring drawdown asymmetry in stop-loss design.** A 50% drawdown requires a 100% gain to recover. A risk-management rule that targets "maximum drawdown" but ignores the geometric reality of recovery is half a rule.
- **Mistaking volatility for risk.** Volatility is a contributor to variance drag, but [[fat-tails]] and [[negative-skew]] add additional drag that variance doesn't capture. The full picture requires higher moments.

## Practical Operating Rules

1. **Always report CAGR (geometric annualized return) alongside arithmetic mean.**
2. **Use log-returns for time-series modeling**, then exponentiate for terminal-wealth statements.
3. **Size positions to maximize log-growth** (fractional Kelly), not arithmetic expectation.
4. **Compute drawdown statistics on cumulative geometric paths**, not on arithmetic-return series.
5. **Apply the variance-drag heuristic**: for any strategy, `g ≈ μ - 0.5σ²`. If σ is large relative to μ, the strategy is closer to break-even than the headline number suggests.

## Related

- [[compounding]] -- the underlying multiplicative dynamic
- [[volatility-drag]] -- the `0.5 σ²` subtraction, treated in its own right
- [[kelly-criterion]] -- the position-sizing rule that maximizes geometric growth
- [[ergodicity]] -- why geometric mean (time-average) is the right statistic
- [[ergodicity-economics]] -- the broader research program
- [[ole-peters]] -- developer of ergodicity economics
- [[sharpe-ratio-pitfalls]] -- the metric that uses arithmetic returns
- [[gaussian-assumption]] -- the model under which the variance-drag identity is exact
- [[negative-skew]] -- adds further drag beyond variance
- [[fat-tails]] -- the kurtosis-driven tail that compounds losses
- [[long-vol-vs-short-vol]] -- the canonical case where naive arithmetic returns mislead
- [[volmageddon]] -- the realized event that destroys geometric returns

## Sources

- Bernoulli, Daniel (1738) "Specimen Theoriae Novae de Mensura Sortis" -- the foundational paper introducing logarithmic utility, equivalent in implication to maximizing geometric growth.
- Kelly, J. L. (1956) "A New Interpretation of Information Rate" -- *Bell System Technical Journal*. Derives the Kelly criterion as the bet fraction maximizing geometric growth rate.
- Latane, Henry (1959) "Criteria for Choice Among Risky Ventures" -- *Journal of Political Economy*. Explicit case for geometric-mean maximization in portfolio choice.
- Peters, Ole (2019) "The ergodicity problem in economics" -- *Nature Physics* 15, 1216-1221. Modern formal treatment.
- Spitznagel, Mark. *Safe Haven* (2021) -- argues that geometric returns (not arithmetic) are what matter for compounding portfolios, and that long-vol overlays improve geometric returns despite negative arithmetic expectation.
- Markowitz, Harry. *Portfolio Selection* (1959), Ch. 6 -- cautions on the difference between arithmetic and geometric portfolio statistics.
