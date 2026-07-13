---
title: "Kelly Criterion for Strategies"
type: concept
created: 2026-04-10
updated: 2026-06-21
status: excellent
tags: [portfolio-theory, position-sizing, kelly, multi-strategy, risk-management]
aliases: ["Kelly Sizing", "Multi-Strategy Kelly", "Kelly Allocation"]
domain: [portfolio-theory]
difficulty: advanced
related: ["[[kelly-criterion]]", "[[position-sizing]]", "[[multi-strategy-portfolio]]", "[[strategy-correlation-matrix]]", "[[risk-of-ruin]]", "[[risk-parity-for-strategies]]", "[[modern-portfolio-theory]]", "[[geometric-mean]]"]
---

# Kelly Criterion for Strategies

How to apply the Kelly criterion when allocating capital across multiple trading strategies, not just sizing individual bets. The single-bet Kelly formula is well-known; the multi-strategy generalization is much less commonly applied — and when applied incorrectly, can blow up portfolios faster than naive equal-weighting.

## The Single-Bet Kelly

For a binary bet with edge `p` (probability of winning) and payout `b:1`, the Kelly fraction is:

```
f* = (b × p − (1 − p)) / b
```

For continuous returns with mean `μ` and variance `σ²`, the analog is:

```
f* = μ / σ²
```

This is the fraction of capital to risk per bet that maximizes the long-run *geometric* growth rate (equivalent to maximizing expected log wealth).

The intuition: you want to size up when expected return is high and size down when variance is high. Larger expected returns can support larger position sizes; larger variance penalizes large sizes because of the asymmetry of geometric returns (a 50% loss requires a 100% gain to recover).

## Multi-Strategy Kelly

For N strategies with mean return vector `μ` and covariance matrix `Σ`, the Kelly-optimal allocation vector is:

```
f* = Σ⁻¹ × μ
```

This is just `Σ⁻¹μ` — the same form as the unconstrained mean-variance optimum. The Kelly approach maximizes geometric growth, while mean-variance maximizes expected utility under specific assumptions; under log utility they coincide.

Key properties:
- **The optimal allocation depends on the covariance structure**, not just individual Sharpes
- **Negative correlations enable larger absolute allocations** — the diversification reduces variance, which lets you size up
- **Highly correlated strategies are penalized** — adding a second copy of a strategy you already have produces little Kelly benefit
- **The total leverage** can be computed as `Σ f*ᵢ`, often greater than 1

## A Worked Example

Three strategies with annualized:
- A: μ = 8%, σ = 10%
- B: μ = 6%, σ = 8%
- C: μ = 10%, σ = 15%

Correlations: ρ(A,B) = 0.3, ρ(A,C) = 0.0, ρ(B,C) = 0.2

Covariance matrix:
```
Σ = [[0.0100, 0.0024, 0.0000],
     [0.0024, 0.0064, 0.0024],
     [0.0000, 0.0024, 0.0225]]
```

Solve `f* = Σ⁻¹ × μ`:

```
f* ≈ [6.5, 5.6, 3.9]
```

Total leverage ≈ 16x. This is the Kelly-optimal allocation. **It is also almost certainly wrong to actually use** — see the "Why You Should Use Half-Kelly" section below.

### How correlation reshapes the allocation

The `Σ⁻¹μ` form means allocations are driven by *correlation-adjusted* edge, not raw Sharpe. The intuition, holding individual Sharpes fixed and varying only the pairwise correlation:

| Pairwise correlation between two similar strategies | What Kelly does | Why |
|---|---|---|
| Strongly negative (ρ ≈ −0.5) | Sizes *both up* aggressively | Each hedges the other's variance — the pair is near risk-free |
| Zero (ρ ≈ 0) | Sizes both at standalone level | True diversification; variance adds in quadrature |
| Mildly positive (ρ ≈ +0.3) | Modest haircut to each | Some shared risk |
| Strongly positive (ρ ≈ +0.8) | Heavy haircut; near-collapses to one position | Adding a near-duplicate buys little growth, much risk |
| Perfectly correlated (ρ = 1) | Treats them as a single strategy | No diversification benefit at all |

This is the practical payoff of the multi-strategy form: **a mediocre strategy that is negatively correlated to your book can deserve more capital than a higher-Sharpe strategy that duplicates exposure you already hold.** It is also where the danger lives — the off-diagonal terms of `Σ` are the noisiest to estimate, and crisis correlations converge toward +1 exactly when the negative-correlation assumption was load-bearing. This is why the practical workflow below insists on *stressed/conditional* correlations from the [[strategy-correlation-matrix]] rather than full-period sample correlations.

## Why Full Kelly Is Too Aggressive in Practice

The Kelly formula assumes:

1. **Known μ and Σ** — but in reality these are estimated from data and are noisy
2. **Stationary distribution** — but real returns are non-stationary
3. **Log utility** — most investors are more risk-averse than log utility implies
4. **No path dependence** — but in practice you may need to withdraw or face margin calls along the way
5. **Continuous compounding** — discrete trading introduces friction

When `μ` is overestimated (which it almost always is in backtests), full Kelly is *catastrophically* over-leveraged. A 30% overestimate of expected return at full Kelly leads to drawdowns 2-3x larger than the Kelly model predicts.

## Half-Kelly and Fractional Kelly

The standard practical fix is to use *half-Kelly* — half of the formula's recommended size. Or *quarter-Kelly* for more conservative investors.

Why this works:
- Halves the leverage, halves the catastrophic risk from estimation error
- Reduces expected geometric return by only ~25% (because of the diminishing returns to size in the log-growth equation)
- Much more forgiving to noisy parameter estimates

The math: if your estimated `μ` is off by a factor of `1 + ε`, full Kelly leads to size that's `1 + ε` too large. Half-Kelly leads to size that's `0.5 × (1 + ε)` — still too large but by half as much.

A useful heuristic: **half-Kelly captures ~75% of the long-run growth at one-quarter the catastrophic risk**.

### Fractional-Kelly comparison

The growth-vs-risk trade-off as the Kelly fraction `c` is dialed down (figures are the standard textbook approximations under the log-growth model, illustrative — real outcomes depend on the accuracy of `μ` and `Σ`):

| Fraction `c` | Leverage vs full Kelly | ≈ Share of max growth retained | ≈ Theoretical drawdown | Tolerance to over-estimating μ |
|---|---|---|---|---|
| Full (1.0) | 1.0× | 100% | ~50% | None — catastrophic if μ wrong |
| Three-quarter (0.75) | 0.75× | ~94% | ~35% | Poor |
| **Half (0.5)** | 0.5× | ~75% | ~25% | Good — the standard choice |
| Quarter (0.25) | 0.25× | ~44% | ~15% | Very good |
| Tenth (0.1) | 0.1× | ~19% | ~6% | Extreme caution |

The growth curve is *concave* in size: the first half of the Kelly leverage buys most of the growth, while the second half buys the last quarter of growth at the price of doubling the drawdown and eliminating all margin for estimation error. This concavity is *why* fractional Kelly dominates in practice — you give up a little growth to buy a lot of robustness. See [[risk-of-ruin]] for the formal link between leverage and ruin probability.

## Estimation Error Dominates

The Kelly formula is exquisitely sensitive to estimation error in `μ` and `Σ`:

- A 10% error in `μ` translates roughly into a 10% sizing error
- A 10% error in `Σ` (covariance) translates roughly into a 10% sizing error in the opposite direction
- These errors compound — small mis-estimations in both produce larger sizing errors

Most backtests overestimate `μ` (selection bias, lookahead, overfitting) and underestimate the *tail* of `Σ` (full-period correlation hides crisis correlation). The net effect is sizing recommendations that are 2-5x too aggressive in practice.

## Robust Kelly Variants

Several practical adjustments make Kelly more robust to estimation error:

### 1. Shrinkage on `μ`
Replace the estimated `μ` with a shrunken version that pulls toward zero:

```
μ_shrunk = (1 - λ) × μ_estimated
```

Where `λ ∈ [0.3, 0.7]` typical. Equivalent to applying a Bayesian prior that strategies have small expected returns until proven otherwise.

### 2. Shrinkage on `Σ`
Use Ledoit-Wolf or constant-correlation shrinkage to stabilize the covariance estimate. Plain sample covariance is unstable for large N.

### 3. Robust Optimization
Instead of optimizing for the point estimate, optimize for the worst case in a confidence region around the estimate. Reduces sensitivity to extreme parameter realizations.

### 4. Resampling
Bootstrap the historical returns, recompute the optimal allocation for each bootstrap sample, average the allocations. Smooths out noise in any single estimate.

### 5. Fractional Kelly Plus Constraints
Apply half-Kelly *and* constrain individual allocations to (say) ±10% of capital. The constraint protects against any single bad estimate dominating the portfolio.

## Practical Guidelines

A defensible workflow for using Kelly with multiple strategies:

1. **Estimate `μ` and `Σ`** from at least 3 years of returns; use shrinkage on both
2. **Stress the covariance matrix** — replace with conditional/tail correlations from [[strategy-correlation-matrix]]
3. **Compute full Kelly** as a reference number
4. **Apply half-Kelly** as the actual sizing
5. **Cap individual allocations** at some fraction (e.g., 25% of capital) regardless of what Kelly says
6. **Cap total leverage** at some level (e.g., 2-3x) regardless of what Kelly says
7. **Recompute periodically** (monthly or quarterly) to incorporate new data

Even with all these adjustments, Kelly is a *reference framework*, not a literal allocation rule. It tells you which strategies *deserve* more capital and roughly how much more — not the exact dollar amount.

## Connection to Drawdown

Full Kelly produces theoretical drawdowns of approximately 50% — that's the cost of maximizing geometric growth. Half-Kelly produces approximately 25% drawdowns. Quarter-Kelly produces ~15%.

If you can't tolerate a 50% drawdown, you can't run full Kelly even if your `μ` and `Σ` are perfectly estimated. The Kelly formula maximizes long-run growth without regard to path; in practice, the path matters enormously because investors get nervous, redeem, or close strategies during drawdowns that are still within the model's range.

## When NOT to Use Kelly

- **Strategies with non-Gaussian, fat-tailed returns** — Kelly assumes a specific distribution shape
- **Strategies with capacity constraints** that bind below the Kelly recommendation
- **Strategies whose true `μ` is unknown beyond order of magnitude**
- **Investors with non-log utility** — full Kelly is only optimal under log utility

In these cases, simpler heuristics (equal-risk, risk parity, fixed fraction) often outperform Kelly on practical metrics because they don't compound estimation errors.

### Kelly vs other allocation methods

| Method | Inputs needed | Robustness to estimation error | Best when |
|---|---|---|---|
| Full Kelly (`Σ⁻¹μ`) | μ and Σ | Very poor | Inputs are genuinely known (rare) |
| Half / quarter Kelly | μ and Σ | Moderate / good | You have a real edge estimate but it is noisy |
| [[risk-parity-for-strategies\|Risk parity]] | Σ only (no μ) | Good | Edges are similar or unknowable; vols differ |
| Equal-weight | None | Best | N small, edges indistinguishable |
| Mean-variance ([[modern-portfolio-theory\|MPT]]) | μ and Σ + utility | Poor (same as Kelly) | Single-period, known utility |
| Fixed fractional | Per-trade risk % | Best | Single-strategy discretionary trading |

Note that risk parity is *Kelly with μ set equal across strategies* — it drops the noisiest input (expected return) and keeps only the covariance structure. That is often the right move when you cannot tell strategies apart on edge.

## How This Connects to the Rest of the Wiki

Kelly-for-strategies is the book-level generalisation of single-trade [[position-sizing]] and the [[kelly-criterion]]. Its objective — maximize expected log wealth — is the same one that drives the [[geometric-mean|geometric-mean argument]] behind the [[barbell-portfolio]], and its failure mode (over-leverage from over-estimated μ) is a direct route to [[risk-of-ruin]]. It sits one layer below [[multi-strategy-portfolio]] (which decides *which* sleeves to run) and consumes the [[strategy-correlation-matrix]] (which supplies the stressed `Σ`). When capacity constraints bind below the Kelly recommendation — common for the strategies catalogued in [[strategies-overview]] — the capacity cap, not Kelly, sets the size; see [[strategy-capacity]] and [[market-impact-models]].

## Sources

- Kelly (1956) "A New Interpretation of Information Rate" — *Bell System Technical Journal*
- Thorp (2006) "The Kelly Criterion in Blackjack, Sports Betting, and the Stock Market"
- MacLean, Thorp, Ziemba (2010) *The Kelly Capital Growth Investment Criterion*
- [[book-fortune-formula]] — Poundstone on Kelly's history
- [[book-advances-in-financial-machine-learning]] — López de Prado on robust portfolio construction

## Related

- [[kelly-criterion]]
- [[position-sizing]]
- [[multi-strategy-portfolio]]
- [[strategy-correlation-matrix]]
- [[risk-parity-for-strategies]]
- [[modern-portfolio-theory]]
- [[risk-of-ruin]] — the leverage-to-ruin link fractional Kelly manages
- [[geometric-mean]] — the log-wealth objective Kelly maximizes
- [[barbell-portfolio]] — a hard-capped, convexity-first take on the same objective
- [[strategy-capacity]] — when capacity, not Kelly, sets the size
