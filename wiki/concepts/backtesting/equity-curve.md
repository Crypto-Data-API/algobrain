---
title: "Equity Curve"
type: concept
created: 2026-04-13
updated: 2026-06-22
status: excellent
tags: [backtesting, portfolio-theory, risk-management]
aliases: ["Equity Curve Trading", "Account Curve", "P&L Curve"]
domain: [backtesting, risk-management]
prerequisites: ["[[backtesting-overview]]"]
difficulty: beginner
related: ["[[sharpe-ratio]]", "[[backtesting-overview]]", "[[backtesting]]", "[[risk-management-overview]]", "[[drawdown]]", "[[walk-forward-analysis]]", "[[overfitting]]", "[[overfitting-detection]]", "[[maximum-drawdown]]", "[[moving-average]]", "[[underwater-plot]]", "[[when-to-retire-a-strategy]]"]
---

# Equity Curve

An equity curve is a plot of a trading account's or strategy's value over time. It is the primary visual tool for judging strategy performance: a smooth, upward-sloping curve indicates consistent returns, while large [[drawdown|drawdowns]] and high volatility signal risk. The shape of the curve — not just its endpoint — is what distinguishes a robust edge from a fragile one.

## How It Is Constructed

The equity curve is the running cumulative value of an account as each trade's profit and loss is applied. For a sequence of per-period returns rₜ:

```
Compounded (geometric):   Eₜ = E₀ × Π (1 + rₜ)
Additive (fixed-size):    Eₜ = E₀ + Σ (P&Lₜ)
```

- **Compounded** curves reinvest gains, so position size scales with equity; they look exponential and are best read on a **log scale**, where a constant compound rate plots as a straight line.
- **Additive** curves assume a fixed bet size each trade; they show the raw edge without the distortion of compounding and are often preferred for *evaluating* a signal in isolation.

Two derived plots are inseparable from the equity curve:

- **[[drawdown|Drawdown]] series** — at each point, `(Eₜ − running peak) / running peak`. Always ≤ 0.
- **[[underwater-plot|Underwater plot]]** — the drawdown series charted over time, making the *depth and duration* of every losing stretch visually obvious.

## What to Read From a Curve

Total return (where the curve ends) is the least informative thing about it. The diagnostic features are in the path:

- **Slope** — the average rate of return. A steeper slope is better, all else equal.
- **Smoothness** — how tightly returns cluster around the slope. Smoothness is the visual proxy for the [[sharpe-ratio]]: a high-Sharpe strategy produces a curve that hugs a straight line on a log scale; a low-Sharpe strategy zig-zags violently around the same trend.
- **Maximum drawdown depth** — the deepest peak-to-trough decline (see [[maximum-drawdown]]). A 20% drawdown and a 50% drawdown can reach the same endpoint, but the second is far harder to hold through and may breach risk limits or trigger redemptions before recovery.
- **Drawdown duration / time-to-recovery** — how long it takes to reclaim a prior high-water mark. A strategy with a 20% drawdown that recovers in two months has a very different risk profile from one with the same depth that takes eighteen months. Long underwater periods are where discretionary traders and allocators abandon a system at the worst time.
- **Slope consistency / regime concentration** — whether gains are spread evenly or concentrated in a few favourable windows. A curve that earns nearly all its value in one regime (e.g. the 2020–2021 bull market) and flatlines otherwise is likely capturing a single beta exposure rather than a durable edge.

### Reading two curves with the same endpoint

Two strategies can finish at the same +60% and be completely different propositions:

| Feature | Strategy A | Strategy B |
|---------|-----------|-----------|
| Total return | +60% | +60% |
| Max [[drawdown]] | −12% | −38% |
| Longest underwater period | 3 months | 19 months |
| Annualized volatility | 9% | 26% |
| [[sharpe-ratio]] (approx) | ~1.4 | ~0.5 |
| Curve shape | Smooth, near-linear on log scale | Jagged, big air-pockets |

Strategy A is deployable at meaningful size; Strategy B will likely breach a risk limit, exhaust a trader's conviction, or trigger LP redemptions during its 38% / 19-month hole long before the recovery arrives — even though the *endpoint is identical*. This is the central lesson of equity-curve analysis: the path dominates the destination.

## In-Sample vs Out-of-Sample

The single most important test for distinguishing genuine edge from curve-fitting is comparing equity curves across [[backtesting|in-sample]], out-of-sample, and [[walk-forward-analysis|walk-forward]] periods. A real edge produces a curve whose slope and smoothness degrade only *gracefully* out of sample. A curve that is beautiful in-sample and then goes flat or negative the moment it crosses into unseen data is the classic signature of [[overfitting]] (see [[overfitting-detection]]) — the parameters were fit to the noise of the training window, not to a repeatable mechanism.

This is why practitioners plot the in-sample and out-of-sample segments on the same chart with a vertical marker at the split: the eye catches a regime break at the boundary faster than any single summary statistic.

## Equity Curve Trading (the meta-strategy)

Equity curve trading is a meta-strategy in which the trader monitors the equity curve of an *existing* strategy and switches the strategy off when its own performance degrades. The most common rule applies a [[moving-average]] to the equity curve itself: when the curve falls below its own N-period moving average, the strategy is paused; it resumes only when the curve climbs back above.

- **The case for it** — it can cut drawdowns during regime changes when a strategy's edge has temporarily disappeared, since a deteriorating curve is sometimes an early warning that the market has shifted.
- **The case against it** — it adds parameters (the MA length, the lookback) that are themselves prone to [[overfitting]], and switching off can cause the trader to miss the sharp recovery trades that often follow a drawdown, materially reducing long-run returns. Empirical results are mixed and strategy-dependent.

The deeper principle holds regardless: no strategy works in every market condition, so having predefined rules for *when to stop trading* is as important as the entry and exit rules. See [[when-to-retire-a-strategy]] for the related question of permanent retirement versus a temporary equity-curve pause.

## Common Pitfalls and Risks

- **Worshipping the endpoint.** The single most common error: ranking strategies by total return and ignoring the [[drawdown]] path. The endpoint is the *least* informative feature of a curve.
- **Survivorship in the curve itself.** A curve assembled only from the trades a discretionary trader *chose to log*, or a portfolio that quietly dropped its losers, flatters the record. The curve is only honest if it includes every signal the rules generated.
- **No [[transaction-costs|cost]] overlay.** A pristine backtest curve drawn before commissions, [[slippage]], spreads, and financing routinely inverts into a losing curve once realistic costs are applied — especially for high-turnover strategies.
- **Compounding illusion.** Plotting a compounded curve on a *linear* axis makes recent performance look explosive and early performance look flat, hiding a deteriorating Sharpe. Use a log scale to judge consistency.
- **Suspicious smoothness.** A curve with almost no drawdown and a near-perfect 45° line is a red flag, not a triumph — it usually means look-ahead bias, an unmodeled cost, a hidden short-volatility exposure (which pays steadily then blows up), or outright [[overfitting]].
- **Short sample / few trades.** A beautiful curve built from 20 trades carries almost no statistical weight; the path could be luck. Curve quality must be read alongside the number of independent trades.
- **Equity-curve filtering adds fragility.** As above, the meta-strategy's own parameters overfit and it can lock you out of recoveries.

## How Traders and Allocators Use It

The equity curve is the artefact every allocator, risk manager, and prop desk evaluates first. Two strategies with identical annual returns are not interchangeable: the one with the shallower, shorter drawdowns is the one that survives a real account, because position sizing, margin, and human (or LP) tolerance are all governed by the worst stretch of the curve, not the average. In practice:

- **Allocators** size capital to a strategy from its [[maximum-drawdown]] and underwater duration, not its mean return — a 38% historical drawdown caps how much can be risked.
- **Risk managers** set kill/de-risk thresholds (see [[when-to-retire-a-strategy]]) directly off the live curve diverging from its backtested envelope.
- **System developers** overlay in-sample vs out-of-sample segments with a split marker to catch [[overfitting]] at a glance, and require the live curve to track the [[walk-forward-analysis|walk-forward]] curve within tolerance before scaling up.

Reading curves well — and being skeptical of suspiciously smooth ones — is a core defence against deploying overfit systems.

## Related

- [[drawdown]] -- the per-point decline from peak derived from the curve
- [[underwater-plot]] -- the drawdown series charted over time
- [[maximum-drawdown]] -- the deepest peak-to-trough point on the curve
- [[sharpe-ratio]] -- smoothness of the curve is its visual proxy
- [[walk-forward-analysis]] -- the out-of-sample stitching used to validate the curve
- [[backtesting]] / [[backtesting-overview]] -- where backtested curves are produced
- [[overfitting]] / [[overfitting-detection]] -- the failure a too-smooth curve signals
- [[when-to-retire-a-strategy]] -- acting on a deteriorating live curve
- [[risk-management-overview]] -- sizing and limits governed by the worst stretch
- [[moving-average]] -- the filter used in equity-curve trading

## Sources

- Pardo, R. (2008). *The Evaluation and Optimization of Trading Strategies*. Wiley. (Equity-curve analysis, drawdown, and walk-forward evaluation.)
- Tomasini, E. & Jaekle, U. (2009). *Trading Systems: A New Approach to System Development and Portfolio Optimisation*. (Equity-curve filtering as a meta-strategy.)
- Investopedia — "Equity Curve": https://www.investopedia.com/terms/e/equity-curve.asp
