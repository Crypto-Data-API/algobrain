---
title: "Correlation of Returns"
type: concept
created: 2026-04-10
updated: 2026-06-21
status: excellent
tags: [portfolio-theory, correlation, statistics, risk-management]
aliases: ["Return Correlation", "Strategy Returns Correlation"]
domain: [portfolio-theory]
difficulty: intermediate
related: ["[[strategy-correlation-matrix]]", "[[multi-strategy-portfolio]]", "[[diversification]]", "[[correlation]]", "[[correlation-regime]]", "[[correlation-breakdown]]", "[[correlation-matrix]]", "[[risk-parity-for-strategies]]", "[[failure-modes]]", "[[quant-meltdown-2007]]", "[[implied-correlation]]", "[[modern-portfolio-theory]]"]
---

# Correlation of Returns

The statistical correlation between the return streams of two strategies (or assets) over a common time period. The single most important input to portfolio construction and the most commonly misused. This page covers what correlation actually measures, what it doesn't, and the specific failure modes that matter for trading strategies.

## The Definition

For two return series `r_A` and `r_B` over the same N observations:

```
ρ(A, B) = cov(r_A, r_B) / (σ_A × σ_B)
```

Where `cov(r_A, r_B) = E[(r_A - μ_A)(r_B - μ_B)]` and `σ_A`, `σ_B` are the standard deviations of A and B.

Bounded between -1 (perfect negative correlation) and +1 (perfect positive correlation). Zero means linearly uncorrelated — but **not** independent.

### ρ interpretation table

| ρ range | Reading | Portfolio meaning |
|---|---|---|
| +0.8 to +1.0 | move together strongly | almost no diversification; treat as one bet |
| +0.4 to +0.8 | move together, partially | modest diversification benefit |
| −0.2 to +0.4 | weak / near-independent | strong diversification (if it holds in stress) |
| −0.8 to −0.2 | offsetting | hedge-like; one cushions the other |
| −1.0 to −0.8 | mirror images | near-perfect hedge (rare and usually regime-fragile) |

The right-hand column carries a hidden asterisk that the rest of this page exists to explain: every diversification reading assumes the measured ρ *holds in the regime you care about*. Calm-regime ρ near zero routinely jumps toward +1 in stress — see [[correlation-regime]] and [[correlation-breakdown]].

## Return Correlation vs Price Correlation

A foundational distinction that trips up newcomers: **correlate returns, not prices (levels).**

- **Price/level correlation** measures whether two *price series* trend together. Two unrelated assets that both drift upward over a decade (almost everything, in a bull market) will show a high price correlation — a **spurious correlation** driven by their common trend, not by any genuine co-movement. This is the classic non-stationary-series trap from statistics.
- **Return correlation** measures whether the two assets' *period-over-period changes* move together. Returns are (approximately) stationary, so their correlation reflects genuine co-movement rather than shared drift.

Practical rule: always compute ρ on **returns** (log or simple), never on raw prices or cumulative equity curves. A common analyst error is correlating two strategies' *equity curves* (which both rise over time) and concluding they are highly correlated when their *return streams* may be nearly independent. The equity-curve correlation is dominated by the shared upward trend; the return correlation is the decision-relevant number for [[diversification]] and sizing.

## What Correlation Measures

It measures the *linear* co-movement of two return series around their respective means. Specifically:

- ρ = 1: A and B move in lockstep, same direction, perfectly proportional
- ρ = -1: A and B move in lockstep, opposite directions, perfectly proportional
- ρ = 0: A and B have no *linear* relationship
- 0 < ρ < 1: A and B tend to move in the same direction, but not perfectly

A correlation of 0.5 means roughly: when A is up 1 std, B is on average up 0.5 std.

## What Correlation Does *Not* Measure

This is where most portfolio construction mistakes come from.

### 1. Tail Co-movement
Two series with full-period correlation 0.1 can have *tail* correlation 0.9. Linear correlation averages over the entire joint distribution; tail behavior is dominated by a small number of extreme observations and gets washed out.

For trading strategies, the tail is where correlation matters most — that's when drawdowns happen. See [[strategy-correlation-matrix]] for tail correlation methods.

### 2. Non-Linear Dependence
Two series can be perfectly dependent and have correlation zero. Example: B = A². If A is symmetric around zero, then `cov(A, A²) = 0` and `ρ = 0` — but knowing A tells you everything about B.

In trading, non-linear dependence shows up in any options-related strategy: a long-vol position has zero correlation with the underlying in normal times but explodes when the underlying moves a lot in either direction.

### 3. Causation
Correlation is symmetric. It doesn't tell you whether A causes B, B causes A, or both depend on a common factor. For trading, the common-factor case is the dangerous one — your "uncorrelated" strategies may share an unobserved driver that occasionally dominates everything.

### 4. Stability Over Time
Correlations *change*. A 5-year average correlation tells you nothing about whether the two strategies are correlated *today*. Rolling correlation plots are essential.

### 5. Correlation in Specific Regimes
Two strategies might be uncorrelated in low-vol regimes and 0.9 correlated in high-vol regimes. The full-period number averages these out and is misleading for both regimes individually.

## Pearson vs. Spearman vs. Kendall

The standard correlation (Pearson) assumes linear relationships and is sensitive to outliers. Two alternatives:

### Spearman Rank Correlation
Computes Pearson correlation on the *ranks* of the observations rather than the values. Robust to outliers and non-linear monotonic relationships.

**Use when:** the return distributions are heavily skewed or have outliers; when the relationship between A and B might be monotonic but non-linear.

### Kendall Tau
Counts the number of concordant vs. discordant pairs. Even more robust than Spearman but slower to compute.

**Use when:** small sample sizes, very fat tails, or when monotonicity is the right model.

For most trading applications, *all three* should be computed. If they disagree substantially, you have non-linear or outlier-driven structure that Pearson alone is hiding.

### Method-selection table

| Method | Measures | Robust to outliers? | Best for |
|---|---|---|---|
| **Pearson** | linear co-movement | no | well-behaved, near-Gaussian returns |
| **Spearman** | monotonic (rank) co-movement | yes | skewed returns, non-linear-but-monotonic links |
| **Kendall τ** | concordance of pairs | very | small samples, very fat tails |

Diagnostic heuristic: if Pearson ≫ Spearman, a few outliers are inflating the linear estimate; if Spearman ≫ Pearson, the relationship is monotonic but non-linear (Pearson is understating it). Either disagreement is a signal to look at the scatter plot, not just the headline number.

## The Sample Correlation Has Noise

A sample correlation from N observations has standard error roughly:

```
SE(ρ) ≈ (1 - ρ²) / √N
```

For N = 252 (one year of daily returns), SE ≈ 0.06 around ρ = 0. The "uncorrelated" strategies you measured at ρ = 0.1 could plausibly have a true correlation of 0.0 to 0.2.

Implications:
- **One year of daily returns is not enough** to confidently estimate correlations.
- **Differences of 0.1-0.2 in measured correlation** are usually within noise.
- **Out-of-sample correlation** is almost always *higher* than in-sample correlation due to selection bias on the strategies that survived.

For portfolio construction, use 3+ years of overlapping returns and treat anything within ±0.15 of the point estimate as plausible.

### Worked noise example (illustrative)

> You measure two strategies at ρ = 0.10 over one year (N = 252) and conclude they are "uncorrelated diversifiers." Plug into the standard error: `SE ≈ (1 − 0.10²)/√252 ≈ 0.062`. A rough 95% interval is `0.10 ± 1.96·0.062 ≈ [−0.02, 0.22]`. The true correlation could be anything from slightly negative to +0.22. Sizing the book as if ρ = 0.10 is precise is false confidence; the honest move is to size for the upper end of the interval *and* add a stress margin (see below), because out-of-sample ρ on surviving strategies is typically *higher* than the in-sample estimate. The longer the history (larger N), the tighter the interval — which is why 3+ years is the working minimum.

## Time-Varying Correlation

Correlations are not constant. They change for several reasons:

### 1. Regime Changes
Correlations between asset classes (stocks, bonds, gold, dollar) shift dramatically across regimes. Stock-bond correlation was strongly negative for most of 2000-2020; positive from 2022 onward. A portfolio constructed assuming the negative regime broke when the regime changed.

### 2. Crisis Co-movement
"In a crisis, all correlations go to one." This is approximately true — diversifying assets become correlated as everything sells off together. Tail correlation is dramatically higher than full-period correlation. This is the [[correlation-breakdown]] event, and the persistent high-ρ state it produces is a [[correlation-regime|correlation regime]]; both pages treat the cross-asset version in depth.

### 3. Crowding
As more capital flows into a strategy, its returns become more correlated with the returns of capital-weighted versions of similar strategies. The August 2007 quant meltdown was a textbook case (see [[quant-meltdown-2007]]).

### 4. Structural Change
Regulatory shifts, venue changes, and product introductions can change the underlying correlation structure permanently. The Volcker Rule changed prop trading dynamics; the introduction of leveraged ETFs changed cross-asset hedging flows.

## Measuring Time-Varying Correlation

Three practical methods:

### Rolling Window
Compute Pearson correlation on a rolling window of N observations (e.g., 60-day or 252-day). Plot over time. Look for trends, regime breaks, and stability.

**Strength:** Easy, interpretable.
**Weakness:** Window length is arbitrary; short windows are noisy, long windows are slow to react.

### EWMA (Exponentially Weighted Moving Average)
Compute correlation with weights that decay exponentially backward in time. Recent observations get more weight than older ones.

**Strength:** Reacts faster than equal-weight rolling.
**Weakness:** The decay parameter is another hyperparameter to choose.

### DCC (Dynamic Conditional Correlation)
Engle's GARCH-based model that explicitly fits a time-varying correlation process. More rigorous but assumes a specific parametric form.

**Use when:** doing serious risk management for a multi-asset portfolio.

### Time-varying method comparison

| Method | Reactivity | Hyperparameters | Best for |
|---|---|---|---|
| Rolling window | slow–medium | window length | quick visual diagnosis of drift |
| EWMA | fast | decay λ | near-real-time monitoring |
| DCC-GARCH | adaptive (model-driven) | full GARCH spec | rigorous multi-asset risk systems |

All three are estimates of the *same* moving quantity; the choice trades reactivity against noise and modelling burden. A rolling plot is the cheapest way to *see* a [[correlation-regime|regime]] change; DCC is the cleanest way to *forecast* covariance for sizing.

## Correlation in Practice for Portfolio Construction

Three rules of thumb:

1. **Always look at multiple correlation measures** — full-period, conditional on stress, rolling, and tail. Disagreements between them are diagnostically important.

2. **Use stress-scenario correlation for portfolio sizing**, not full-period. The full-period number flatters your diversification.

3. **Build in margin for correlation drift** — assume your correlations will rise by 0.2 in stress. Size positions assuming the worse case is realized.

## Common Mistakes / Pitfalls

1. **Correlating prices instead of returns.** Two trending equity curves look ~0.9 correlated even when their return streams are independent. Always use returns. See [[#Return Correlation vs Price Correlation]].
2. **Treating a point estimate as exact.** A measured ρ has a standard error; 0.1 and 0.2 are usually indistinguishable on one year of data. Quote intervals, not points.
3. **Using full-period ρ for stress sizing.** The full-period number averages calm and crisis; it *flatters* diversification. Size on the conditional/stress matrix — see [[strategy-correlation-matrix]] and [[correlation-regime]].
4. **Assuming ρ = 0 means independence.** Zero linear correlation is consistent with strong non-linear dependence (e.g. long-vol vs underlying). Check Spearman/Kendall and the scatter.
5. **Ignoring crowding-driven drift.** As capital crowds a strategy, its returns correlate more with similar strategies — a slow regime change that only shows up in rolling, not full-period, ρ. The [[quant-meltdown-2007|2007 quant meltdown]] is the case study.
6. **Trusting Pearson on fat-tailed strategy returns.** Outliers (the exact days you care about) dominate Pearson. Robust estimators and explicit [[strategy-correlation-matrix|tail-correlation methods]] are the fix.

## Sources

- López de Prado (2016) "Building Diversified Portfolios that Outperform Out of Sample" — *Journal of Portfolio Management*
- Engle (2002) "Dynamic Conditional Correlation" — *Journal of Business and Economic Statistics*
- [[book-the-quants]] — Patterson on correlation surprise
- [[correlation]] — basic correlation concept page

## Related

- [[correlation]] — the base statistical concept
- [[correlation-regime]] — the regime structure of correlation; calm vs crisis states
- [[correlation-breakdown]] — the "ρ → 1" transition event
- [[correlation-matrix]] — the multi-asset object built from pairwise ρ
- [[strategy-correlation-matrix]] — applying all of this to a book of strategies
- [[multi-strategy-portfolio]] — the portfolio this feeds
- [[diversification]] — the property ρ governs
- [[risk-parity-for-strategies]] — sizing that consumes the correlation matrix
- [[implied-correlation]] — options-implied forward correlation
- [[modern-portfolio-theory]] — the framework that takes ρ as a static input
- [[failure-modes]] — where mis-estimated ρ shows up as blow-ups
- [[volatility]] — the σ terms that pair with ρ in portfolio variance
