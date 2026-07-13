---
title: "Risk Parity for Strategies"
type: concept
created: 2026-04-10
updated: 2026-06-21
status: excellent
tags: [portfolio-theory, risk-parity, multi-strategy, position-sizing]
aliases: ["Strategy Risk Parity", "Equal Risk Contribution"]
domain: [portfolio-theory]
difficulty: intermediate
related: ["[[risk-parity]]", "[[multi-strategy-portfolio]]", "[[strategy-correlation-matrix]]", "[[kelly-for-strategies]]"]
---

# Risk Parity for Strategies

A multi-strategy allocation method that sizes each strategy so it contributes an equal amount of *risk* to the portfolio. Distinct from equal-dollar allocation (which gives more risk weight to volatile strategies) and from Kelly/Markowitz (which depend heavily on noisy expected return estimates). Risk parity is the most robust simple allocation framework for multi-strategy portfolios.

## The Idea

Equal-dollar allocation across two strategies — one with 5% vol and one with 30% vol — gives the high-vol strategy 6x the risk weight even though both have the same dollar weight. The portfolio's behavior is dominated by the volatile strategy.

Risk parity inverts this: allocate *less* dollars to volatile strategies and *more* dollars to calm strategies, so each contributes the same amount of variance to the portfolio. The result is a portfolio that doesn't concentrate risk in whichever strategy happens to have the largest σ.

## The Simple Form

For two strategies, the risk-parity weights are inversely proportional to their volatilities:

```
w_A = (1 / σ_A) / (1/σ_A + 1/σ_B)
w_B = (1 / σ_B) / (1/σ_A + 1/σ_B)
```

For three or more strategies, simple inverse-vol weighting gives an approximate risk parity, though it ignores correlations.

## The Full Form (with correlations)

The exact risk-parity solution — also called the **Equal Risk Contribution (ERC)** portfolio — requires that each strategy contribute equally to the portfolio's total variance, *taking correlations into account*. The marginal contribution of strategy i to portfolio variance is:

```
MCR_i = (Σ × w)_i × w_i / σ_p
```

Where `Σ` is the covariance matrix, `w` is the weight vector, and `σ_p = sqrt(wᵀ Σ w)` is the portfolio volatility.

The risk parity condition is `MCR_i = MCR_j` for all i, j. Equivalently, the *total* risk contribution `RC_i = w_i × (Σw)_i / σ_p` is equal across strategies, and the contributions sum to `σ_p` (Euler's theorem for the homogeneous-degree-one volatility function). This is a non-linear optimization problem solved iteratively (Newton's method or convex programming).

### Three weighting regimes compared

The three common "risk-balancing" weight schemes differ only in how much of the covariance structure they use:

| Scheme | Inputs used | Formula (long-only) | Correlations? | When it equals ERC |
|---|---|---|---|---|
| **Inverse-variance** | diagonal of `Σ` only | `w_i ∝ 1/σ_i²` | No | Only if all ρ equal |
| **Inverse-volatility** | diagonal of `Σ` only | `w_i ∝ 1/σ_i` | No | When all pairwise ρ are equal |
| **Equal Risk Contribution (ERC)** | full `Σ` | solve `RC_i = RC_j` | Yes | Always (definition) |

Inverse-vol is the workhorse approximation: it is closed-form, monotone in σ, and coincides with true ERC whenever correlations are uniform. ERC only diverges materially from inverse-vol when the correlation structure is *heterogeneous* — e.g. two highly correlated trend sleeves plus one uncorrelated carry sleeve. See [[strategy-correlation-matrix]] for estimating the `Σ` that drives the difference.

### ERC solver (Newton / cyclical-coordinate sketch)

```python
import numpy as np

def erc_weights(cov, tol=1e-10, max_iter=10000):
    """Equal Risk Contribution weights via cyclical coordinate descent.
    cov: (n,n) covariance matrix. Returns long-only weights summing to 1."""
    n = cov.shape[0]
    w = np.ones(n) / n                  # start at equal weight
    for _ in range(max_iter):
        sigma_p = np.sqrt(w @ cov @ w)
        mrc = cov @ w / sigma_p         # marginal risk contributions
        rc = w * mrc                    # total risk contributions
        target = sigma_p / n            # each should contribute 1/n of total risk
        # multiplicative update nudges each weight toward equal RC
        w = w * (target / rc)
        w = np.clip(w, 1e-12, None)
        w = w / w.sum()
        if np.max(np.abs(rc - target)) < tol:
            break
    return w
```

This converges quickly for well-conditioned `Σ`. For ill-conditioned or noisy `Σ` on small samples, prefer [[hierarchical-risk-parity|Hierarchical Risk Parity]] (below), which sidesteps matrix inversion entirely.

## Why Risk Parity Is Robust

The crucial property of risk parity: **it does not depend on expected return estimates**. Mean-variance optimization (and Kelly) require you to estimate `μ`, which is the noisiest parameter in finance. Risk parity only requires `Σ`, which is much more estimable.

This makes risk parity dramatically more stable in practice than mean-variance:
- It doesn't blow up when you mis-estimate expected returns
- It doesn't produce extreme allocations to a single strategy that happened to look great in backtest
- It naturally limits exposure to volatile strategies that might have crowded edges

The cost: risk parity is *inferior* to Kelly when expected returns are accurately known. Since expected returns are almost never accurately known in practice, the cost is usually small relative to the benefit.

## A Worked Example

Three strategies with the following annualized stats:

| Strategy | μ | σ | Notes |
|---|---|---|---|
| Trend | 8% | 12% | Slow trend-follower |
| Mean Reversion | 6% | 6% | Stat-arb basket |
| Carry | 10% | 18% | Crypto basis trade |

Correlations: ρ(Trend, MR) = -0.1, ρ(Trend, Carry) = 0.0, ρ(MR, Carry) = 0.4

### Equal-dollar weights
1/3 each. Portfolio vol ≈ 8.5%. Carry strategy contributes ~55% of total risk; mean reversion contributes ~10%. Highly concentrated in carry.

### Inverse-vol (simple risk parity)
```
w_Trend = (1/12) / (1/12 + 1/6 + 1/18) ≈ 0.286
w_MR    = (1/6)  / (1/12 + 1/6 + 1/18) ≈ 0.571
w_Carry = (1/18) / (1/12 + 1/6 + 1/18) ≈ 0.143
```
Portfolio vol ≈ 6.0%. Each strategy contributes roughly equal risk *ignoring correlations*.

### Full risk parity (with correlation matrix)
Solved iteratively. Weights ≈ [0.30, 0.55, 0.15]. Each strategy now contributes exactly equal risk *accounting for correlations*. Portfolio vol ≈ 5.9%.

### Half-Kelly
Solving the Kelly system and halving:
Weights ≈ [4.0, 6.5, 0.8] — total leverage ~11x. Carry is sized small because it's the riskiest, but the overall leverage is much higher than risk parity.

For the same risk budget, risk parity and half-Kelly land in similar places but risk parity is far more stable to changes in inputs.

## Using Stress Correlation

The risk parity solution depends on the covariance matrix `Σ`. As discussed in [[strategy-correlation-matrix]], full-period correlations dramatically understate stress-period correlations. A risk parity portfolio built on full-period covariance is *over-allocating* to strategies that look diversifying in normal times but become correlated in crises.

The fix: build the risk parity solution using *stress-period covariance*. Estimate correlations from periods when VIX > 25, or use the worst-case 5% of historical 30-day correlation observations. The resulting allocation will be more conservative (smaller positions in strategies that appear diversifying but aren't, larger positions in genuine diversifiers like trend following).

## Risk Parity vs. Kelly

| Property | Risk Parity | Kelly |
|---|---|---|
| Requires `μ`? | No | Yes |
| Requires `Σ`? | Yes | Yes |
| Sensitive to `μ` errors? | No | Very |
| Maximizes growth rate? | No | Yes (under log utility) |
| Stable in practice? | Yes | No (full Kelly), somewhat (half-Kelly) |
| Captures expected return information? | No | Yes |

A defensible hybrid: use risk parity as the *base* allocation, and tilt toward Kelly only by a small amount (e.g., 25% Kelly tilt + 75% risk parity). This captures expected return information without becoming sensitive to its mis-estimation.

## Targeting a Volatility and the Role of Leverage

Risk parity sets *relative* weights; it does not by itself fix the portfolio's absolute volatility. A book of three low-vol mean-reversion sleeves can risk-parity to a 4% portfolio vol — too low to clear a return hurdle. The standard fix is to scale the whole (unit-sum) risk-parity weight vector by a leverage factor `L` to hit a target vol:

```
L = σ_target / σ_p(w_RP)
w_levered = L × w_RP
```

This is the mechanism behind classic "all-weather"/levered risk-parity products: bonds carry low vol, so the strategy levers the bond sleeve up to balance its risk contribution against equities. The trade-off is explicit in the table below.

| Lever | Effect on portfolio | Risk introduced |
|---|---|---|
| Raise `σ_target` (more leverage) | Higher expected return | Financing cost, margin calls, gap/tail risk the variance calc ignores |
| Lower `σ_target` (de-lever) | Smoother equity curve | May not clear return hurdle; cash drag |
| Cap per-strategy weight | Limits single-sleeve blow-up | Pushes book away from exact ERC |
| Cap total leverage | Bounds tail/funding risk | Caps achievable target vol |

A levered risk-parity book is only as safe as its volatility estimate. When realized vol or correlations spike together (the 2020 and 2022 risk-parity drawdowns are textbook examples), the leverage that balanced *normal-times* risk amplifies a *stress-times* loss. Couple leverage with the stress-covariance discipline below and with [[kelly-for-strategies|fractional-Kelly]] leverage caps.

## Rebalancing

Risk-parity weights drift as volatilities and correlations move. Rebalancing policy is a first-order decision, not an afterthought:

| Trigger | Description | Trade-off |
|---|---|---|
| **Calendar** | Recompute monthly/quarterly | Simple, predictable cost; can drift far between dates |
| **Threshold / no-trade band** | Rebalance only when a weight breaches ±X% of target | Lower turnover; needs band tuning |
| **Vol-trigger** | Rebalance when a sleeve's realized vol jumps | Responsive to regime change; can over-trade in noise |

Estimate `Σ` over a lookback long enough to be stable (often 6–24 months of returns or an EWMA half-life of ~60 days) but short enough to react. Rebalancing into a falling, rising-vol strategy is exactly the de-risking risk parity is meant to do, but it crystallizes turnover cost — overlay a no-trade band so you do not churn on noise.

## Hierarchical Risk Parity

López de Prado's improvement on standard risk parity. The procedure:

1. Compute the correlation matrix
2. Convert correlations to distances (high correlation → short distance)
3. Cluster the strategies hierarchically
4. Allocate within clusters first, then across clusters
5. Within each cluster, use simple inverse-vol; across clusters, recurse

The key benefit: hierarchical risk parity does not require *inverting* the covariance matrix. Inverting noisy covariance matrices is the source of most instability in standard mean-variance and Kelly. HRP avoids this entirely and is much more robust on small samples.

For most practical multi-strategy portfolios, HRP is the recommended default. It is more robust than Markowitz and more sophisticated than naive inverse-vol.

## Limitations

1. **Risk parity ignores expected returns.** A strategy with negative expected return gets the same risk allocation as a strategy with positive expected return, which is silly. Practical implementations exclude or down-weight clearly losing strategies.

2. **Risk parity equates volatility with risk.** Volatility is *one* measure of risk; for trading strategies it can be misleading (a long-vol strategy has high volatility but low downside risk in stress). Drawdown-based or CVaR-based versions address this.

3. **Risk parity can over-leverage to hit a target volatility.** If you risk-parity-allocate across low-vol strategies, the portfolio vol may be too low; some implementations apply leverage to reach a target. The leverage introduces tail risk that the risk parity calculation didn't account for.

4. **Risk parity is sensitive to the correlation matrix used.** Garbage in, garbage out. Always stress-test with the conditional/tail correlation matrix.

## Recommended Default

For most multi-strategy portfolios in this wiki's scope, the recommended default allocation method is:

**Hierarchical risk parity using stress-period correlations, with individual position caps at 25% of capital and overall leverage capped at 2x.**

This is robust to almost all common errors in strategy research while still capturing the diversification benefits of multi-strategy investing.

## Implementation Checklist

Before allocating real capital with a risk-parity scheme, walk this checklist:

- [ ] **Returns clean and aligned** — each strategy's return series is net of [[transaction-costs|costs]], same frequency, same calendar, gaps handled.
- [ ] **`Σ` estimated robustly** — adequate lookback, shrinkage or EWMA applied; condition number checked (an ill-conditioned matrix is a red flag for HRP).
- [ ] **Stress covariance computed** — build a second `Σ` from high-VIX / tail-correlation windows (see [[strategy-correlation-matrix]]).
- [ ] **Weights solved both ways** — inverse-vol *and* full ERC; large divergence flags heterogeneous correlations worth understanding.
- [ ] **Per-strategy and per-cluster caps applied** — e.g. 25% per sleeve.
- [ ] **Leverage decision explicit** — target vol chosen, financing cost modelled, total-leverage cap (e.g. 2x) set.
- [ ] **Losing strategies excluded** — risk parity does not look at `μ`; do not fund a sleeve with no edge (see [[edge-taxonomy]]).
- [ ] **Rebalancing rule chosen** — calendar/threshold/vol-trigger with a no-trade band.
- [ ] **Backtested with realized rebalancing cost**, not on a single static allocation.
- [ ] **Kill criteria defined** — what realized-vol or drawdown level forces a de-lever (see [[when-to-retire-a-strategy]]).

## Common Pitfalls

1. **Treating inverse-vol as ERC.** They only coincide under uniform correlations; on a correlated book inverse-vol over-allocates to the correlated cluster.
2. **Estimating `Σ` on too-short a window** — noisy covariance produces unstable weights and churn.
3. **Ignoring leverage's hidden tail risk** — the variance-balanced book is not loss-balanced when correlations spike.
4. **Full-period correlations** — they understate stress correlations and over-allocate to fake diversifiers.
5. **Funding zero/negative-edge sleeves** — risk parity will happily size a losing strategy.
6. **No rebalancing discipline** — drift quietly re-concentrates risk into whatever sleeve's vol fell.

## Sources

- Maillard, Roncalli, Teïletche (2010) "The Properties of Equally Weighted Risk Contribution Portfolios" — *Journal of Portfolio Management*
- Roncalli (2013) *Introduction to Risk Parity and Budgeting*
- López de Prado (2016) "Building Diversified Portfolios that Outperform Out of Sample" — *Journal of Portfolio Management* (hierarchical risk parity)
- [[risk-parity]] — basic concept page

## Related

- [[risk-parity]] — basic concept page
- [[hierarchical-risk-parity]] — López de Prado's cluster-based variant (recommended default)
- [[multi-strategy-portfolio]] — the portfolio risk parity allocates across
- [[strategy-correlation-matrix]] — source of `Σ`, including stress correlations
- [[kelly-for-strategies]] — the expected-return-aware alternative; hybridize with risk parity
- [[modern-portfolio-theory]] — mean-variance frame risk parity reacts against
- [[risk-budgeting]] — generalization where risk contributions are unequal by design
- [[position-sizing]] — sleeve-level sizing that feeds portfolio weights
- [[sharpe-ratio]] — the metric the levered target-vol book ultimately optimizes
- [[when-to-retire-a-strategy]] — kill-criteria framework referenced in the checklist
- [[edge-taxonomy]] — used to exclude no-edge sleeves before allocating
