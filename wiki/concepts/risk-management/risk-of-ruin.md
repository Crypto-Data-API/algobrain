---
title: "Risk of Ruin"
type: concept
created: 2026-04-15
updated: 2026-06-20
status: excellent
tags: [risk-management, position-sizing, kelly-criterion, drawdown, options]
aliases: ["Risk of Ruin", "RoR", "Probability of Ruin", "Gambler's Ruin"]
domain: [risk-management]
prerequisites: ["[[position-sizing]]", "[[expected-value]]", "[[volatility]]"]
difficulty: intermediate
related:
  - "[[position-sizing]]"
  - "[[options-position-sizing]]"
  - "[[options-concentration-risk]]"
  - "[[kelly-criterion]]"
  - "[[max-drawdown]]"
  - "[[maximum-drawdown]]"
  - "[[drawdown-management]]"
  - "[[expected-value]]"
  - "[[risk-management]]"
  - "[[ergodicity-economics]]"
  - "[[when-to-retire-a-strategy]]"
  - "[[kill-criteria]]"
  - "[[tail-risk]]"
  - "[[long-vol-vs-short-vol]]"
---

Risk of ruin (RoR) is the probability that a trading account is depleted to a level that ends the strategy — either by hitting zero, by breaching a margin/maintenance threshold, or by crossing a self-imposed kill level. It is the single number that answers the question "given this edge, this win rate, this payoff geometry, and this position sizing, what is the chance I run out of capital before the math has time to work?" Every other risk metric — Sharpe, Sortino, [[max-drawdown|max drawdown]], [[value-at-risk|VaR]] — is descriptive. Risk of ruin is *terminal*: a positive expectancy strategy with the wrong sizing has a ruin probability above zero, and across enough sample paths the trader is guaranteed to land on one of them. Survivability, not return, is the constraint.

## Definition

Risk of ruin is the probability that the running balance of an account hits a defined absorbing barrier (typically zero, sometimes a kill level set above zero) at any point during a trading horizon. Three quantities determine it:

- **Edge** — the expected value per unit of capital risked
- **Win rate** — the probability that a single trade is profitable
- **Payoff ratio** — the average win divided by the average loss
- **Position size** — the fraction of capital risked per trade
- **Number of trades** — the sample-path length

The same edge with too-large position sizing has a ruin probability orders of magnitude higher than the same edge with proper sizing. Sizing is the dominant lever.

## Quick Reference

| Concept | One-line takeaway |
|---|---|
| **Definition** | Probability the account hits an absorbing barrier (zero, kill level, or margin floor) before the edge compounds |
| **Dominant lever** | [[position-sizing\|Position size]] — far more than win rate or payoff ratio |
| **Core formula** | For finite bankroll vs unbounded counterparty with edge: RoR ≈ (q/p)^N |
| **Optimal-growth bound** | [[kelly-criterion\|Kelly fraction]] f* = (p·b − q)/b; above it, long-run growth turns negative |
| **Practitioner choice** | 0.25× to 0.5× [[kelly-criterion\|Kelly]] — drawdown reduction is super-linear, growth cost sub-linear |
| **Zero-edge warning** | An expectancy-zero strategy with positive variance has RoR → 100% over the long run ([[ergodicity-economics\|non-ergodicity]]) |
| **Options caveat** | Convex losses + [[tail-risk\|fat tails]] + correlated concentration make realized RoR 5-20× the model number |
| **Right framing** | RoR > 0 is not "might happen" — it is "over enough paths, guaranteed to land on a ruined one" |

## The Gambler's Ruin Formula

For a sequence of independent bets each with probability p of winning $b and probability q = 1 - p of losing $a, starting with bankroll N units against an opponent (or absorbing barrier) at distance N units, the classical result is:

```
If p == q:                  RoR = N / (N + M)
If p != q (general):        RoR = ((q/p)^N - (q/p)^(N+M)) / (1 - (q/p)^(N+M))
```

For the practically relevant case of a finite bankroll against an unbounded counterparty (M → ∞) with edge (p > q):

```
RoR = (q/p)^N
```

A trader risking 1 unit per trade with a 55% win rate (1:1 payoff) starting with 20 units has

```
RoR = (0.45/0.55)^20 ≈ 0.017 = 1.7%
```

Cut the bankroll to 5 units (or equivalently risk 4x as much per trade) and

```
RoR = (0.45/0.55)^5 ≈ 0.366 = 36.6%
```

Same edge, same win rate, very different survivability.

## Kelly Framework

The [[kelly-criterion|Kelly criterion]] gives the position size that *maximises long-run geometric growth* of the bankroll, which is also the smallest size at which the long-run growth rate is positive. The classic formula for a binary outcome:

```
Kelly fraction f* = (p × b - q) / b
                  = (p × (b + 1) - 1) / b
```

Where p = win probability, q = 1 - p, b = win/loss ratio.

Worked examples:

| Win Rate | Payoff (b) | Kelly Fraction f* | Half Kelly | Quarter Kelly |
|----------|-----------|-------------------|------------|----------------|
| 55% | 1.0 | 10% | 5% | 2.5% |
| 50% | 2.0 | 25% | 12.5% | 6.25% |
| 60% | 1.0 | 20% | 10% | 5% |
| 40% | 3.0 | 20% | 10% | 5% |
| 45% | 1.5 | 8.3% | 4.2% | 2.1% |

**Above Kelly**: long-run growth is *negative* despite positive expectancy — the bankroll has compounded too much variance and ruin probability accelerates.

**At Kelly**: maximum long-run growth, but with brutal drawdowns (50%+ peak-to-trough is routine at full Kelly).

**Below Kelly (fractional Kelly)**: lower growth rate, much lower drawdowns, much lower RoR. Most professional traders run between 0.25× and 0.5× Kelly. The drawdown reduction is super-linear, the growth-rate cost is sub-linear, and the *ruin* probability collapses.

The reason fractional Kelly is the practitioner's choice: full Kelly assumes you *know* p and b. In trading, p and b are estimated with error. Over-estimating either by 10-20% (common) leads to over-Kelly sizing, which leads to long-run capital decay. Half Kelly tolerates substantial estimation error before crossing the over-Kelly threshold.

## Practical Approximations for Trading

A widely used trading-specific approximation for RoR over a horizon of N trades, with risk fraction f per trade, win rate p, and average win/loss ratio R:

```
A = (1 - p × R + q) / (1 + p × R - q)        # if A < 1, edge exists

RoR ≈ A^(1/f)                                # over a long horizon
```

For p = 0.5, R = 1.5 (a typical "minimum acceptable" trading profile):

- Risk f = 1% per trade: A ≈ 0.6, RoR ≈ 0.6^100 ≈ 0% (essentially zero)
- Risk f = 5% per trade: RoR ≈ 0.6^20 ≈ 0.0036 = 0.36%
- Risk f = 10% per trade: RoR ≈ 0.6^10 ≈ 0.6% (still low but the *drawdown* path is brutal)
- Risk f = 25% per trade: RoR ≈ 0.6^4 ≈ 13%

For p = 0.4, R = 1.5 (positive expectancy: 0.4 × 1.5 - 0.6 = 0):

- Edge is exactly zero. Long-run RoR = 100% at any positive f. This is the "house edge" warning: an expectancy-zero strategy with positive variance is *guaranteed* to ruin in the long run because of the [[ergodicity-economics|non-ergodicity]] of multiplicative returns.

This is the crucial intuition. **Marginal-edge strategies have RoR very sensitive to position size; high-edge strategies have RoR insensitive to position size, but their drawdowns can still be career-ending.**

## Why Monte Carlo Beats the Closed Form

The closed-form formulas above assume fixed bet sizes, IID outcomes, and a stable win/loss distribution. Real trading violates all three: position sizes vary, P&L is autocorrelated (winning and losing *streaks*), and the loss distribution has fat left tails. For any real strategy, the practical way to estimate RoR is **simulation**:

1. Take the empirical distribution of per-trade returns (out-of-sample, not in-sample — see Common Mistakes).
2. Resample it thousands of times to build sample paths of the chosen length (e.g., 1,000 trades), applying the actual position-sizing rule.
3. Count the fraction of paths that touch the absorbing barrier (zero, or the kill level). That fraction *is* the RoR estimate.
4. Read off the **drawdown distribution** at the same time — the 95th-percentile max drawdown is usually more decision-relevant than the RoR number itself, because kill criteria fire at drawdown thresholds long before the formal ruin barrier.

**Block bootstrap** (resampling contiguous blocks of trades rather than single trades) preserves the autocorrelation of P&L and is the right method when losing streaks matter — which, for trend-following and short-premium books, they always do.

Two refinements that matter:

- **Fat-tail resampling.** If the empirical sample is short (most are), the worst observed loss understates the true left tail. Either fit a fat-tailed distribution to the tail or inject synthetic stress scenarios (the worst historical analogue) so the simulation does not "learn" a tail that is thinner than reality. See [[tail-risk]].
- **Time-to-ruin, not just probability-of-ruin.** RoR is monotonically increasing in horizon: a strategy with 1% RoR over 500 trades may have a far higher RoR over 5,000 trades. Report RoR *as a function of horizon*, and recognise that for any RoR > 0 the probability compounds toward certainty as the number of trades grows. The honest question is "how many trades before ruin becomes likely," not "is my RoR acceptable today."

## Worked Examples for Traders

### Example 1: Trend-Follower

A futures trend-follower runs at win rate 40%, average win $3.0, average loss $1.0 (payoff ratio 3.0). Edge per trade: 0.4 × 3.0 - 0.6 × 1.0 = 0.6 units. Kelly fraction: f* = (0.4 × 4 - 1) / 3 = 20%. At quarter Kelly (5% per trade) RoR over 1,000 trades is ~10⁻⁵ — practically zero. At full Kelly (20%) RoR is still low but expected drawdowns are ~50-60%.

### Example 2: Mean-Reversion Premium Seller

A short-premium options trader runs at win rate 80%, average win $0.20, average loss $1.50 (payoff ratio 0.13). Edge per trade: 0.8 × 0.20 - 0.2 × 1.50 = -0.14. **Negative expectancy**. RoR over a long horizon = 100% at any positive position size. The win rate flattered the trader; the asymmetry of payoffs killed them.

### Example 3: Defined-Risk Iron Condor Trader

Win rate 70%, average win $1.0, average loss $3.0 (payoff 0.33). Edge: 0.7 × 1 - 0.3 × 3 = -0.20. Negative expectancy again. The structure is *defined-risk* but that does not save the math — bounded losses do not produce a positive edge if the win-rate to payoff geometry is wrong. This is the [[options-concentration-risk|options-portfolio]] failure mode at small scale.

### Example 4: Marginal-Edge Discretionary

Win rate 53%, payoff 1.0. Edge: 0.06. Kelly: f* = (0.53 × 2 - 1) / 1 = 6%. At 1% per trade, RoR over 500 trades is essentially zero; at 5% per trade RoR is ~3%; at 10% per trade RoR is ~30%. The "1-2% per trade" rule of thumb in retail trading literature is roughly calibrated to keep marginal-edge strategies safely sub-Kelly.

## Why Options Books Are Vulnerable

Options portfolios — particularly short-premium books — have RoR characteristics that the standard formulas under-state, for three reasons:

### 1. Convex Losses on Short Premium

The standard RoR formula assumes a fixed average loss size. Short [[gamma]] / short [[vega]] positions have *convex* loss functions: a 2-sigma move loses 4-5× the 1-sigma loss; a 3-sigma move loses 9-12× the 1-sigma loss. The "average loss" parameter is unstable across regimes — the calm-regime average loss vastly under-states the stress-regime average loss. RoR computed on calm-regime stats is the wrong number.

### 2. Fat Tails and Non-Normal Distributions

Equity returns have excess kurtosis; vol-of-vol has even more. The actual distribution of P&L for a short-strangle book is not Gaussian — it has a thick left tail and a thin right tail. RoR formulas assuming binomial or Gaussian outcomes systematically under-estimate ruin probability for short-vol strategies. The August 5 2024 event ([[vix-august-2024-spike]]) wiped 40-90% of equity for retail short-strangle accounts in a single session — a sample-path event the calm-regime RoR formula would price at <0.1%.

### 3. Correlated Concentration

A book of "diversified" short-premium positions across multiple tickers has effective number of independent bets close to one in stress (see [[correlation-breakdown]] and [[options-concentration-risk]]). The RoR-relevant variance is the stress-regime portfolio variance, not the per-position variance scaled by √N.

The combined effect: the realised RoR of a retail short-premium book is typically 5-20× higher than the model-implied RoR computed with calm-regime inputs.

## Mitigation

Practical levers, in order of impact:

### 1. Position Sizing

The dominant lever. Move from full-Kelly toward quarter- or eighth-Kelly. The growth-rate sacrifice is small; the RoR reduction is enormous. For options books with convex tails, the appropriate fraction is *smaller* than the binary-outcome Kelly suggests.

### 2. Hard Drawdown Circuit Breakers

Pre-commit to mechanical reductions in exposure at drawdown thresholds. A common framework:

| Drawdown | Action |
|----------|--------|
| 5% | Review thesis, no size reduction |
| 10% | Cut gross exposure by 25% |
| 15% | Cut gross exposure by 50% |
| 20% | Halt new positions, defensive only |
| 25% | Stop trading, full review |
| 30% | Hard stop — kill the strategy |

The mechanical nature is the point. Discretionary "I'll size down soon" doesn't protect the bankroll because behavioural biases (loss aversion, hot-hand fallacy, narrative continuation) reliably push traders to *increase* size in drawdowns, not decrease it.

### 3. Kill Criteria

Pre-defined numerical conditions for retiring the strategy. See [[when-to-retire-a-strategy]] and [[kill-criteria]]. Rolling Sharpe < 0 over 6 months, peak drawdown > 20%, win rate degraded > 10pp from backtest, etc.

### 4. Long-Vol or Tail Hedges

For short-premium strategies, allocate 5-15% of premium income to long-vol overlays. This trades a fraction of the calm-regime edge for survivability of the stress-regime path. See [[tail-risk-hedging]] and [[long-vol-vs-short-vol]].

### 5. Cash Reserve

A persistent cash buffer is the lowest-tech RoR mitigation and one of the most effective. Cash earns the risk-free rate but also functions as the absolute floor on the bankroll trajectory.

### 6. Diversification Across *Strategy Types*

Not across tickers within one strategy. Trend, mean-reversion, [[vol-arb]], market-neutral pairs — different P&L generators have different drawdown timing. An aggregate book with three negatively-correlated strategies has materially lower RoR than the same total capital concentrated in one.

### 7. Lower Leverage in Tail-Sensitive Markets

The formulas implicitly assume per-trade variance is bounded. Leveraged exposure in a tail-sensitive market (short-vol, illiquid, levered ETFs, levered crypto perps) violates that. Cut leverage as the relevant tail risk increases.

## Survivability Checklist

Before deploying any strategy, walk through this checklist. It converts "I have an edge" into "I will still be trading in five years":

1. **Estimate the edge out-of-sample.** Use walk-forward or live paper-trading stats, never the in-sample backtest. Haircut the win rate and payoff ratio by 20-30% as an estimation-error buffer.
2. **Compute the [[kelly-criterion\|Kelly]] fraction**, then deploy at 0.25× to 0.5× of it. If the haircut edge is near zero, the strategy is not deployable at any positive size.
3. **Simulate RoR and the drawdown distribution** (block bootstrap, fat-tail-aware) at the intended size and horizon. Reject sizes where the 95th-percentile drawdown exceeds your tolerance.
4. **Check the convex-loss adjustment** for options/leveraged books — the binary-Kelly fraction is too large when the loss function is convex. Size off the *stress-regime* average loss, not the calm-regime one.
5. **Pre-commit drawdown circuit breakers and [[kill-criteria]].** Mechanical, numerical, written down before the first trade.
6. **Hold a cash reserve** as the absolute floor on the bankroll trajectory.
7. **Diversify across strategy *types*** (not tickers within one strategy) so drawdowns are not synchronised.
8. **Re-estimate periodically.** Edge decays; if the live win rate drifts below the deployment assumption, resize down before the formal kill criterion fires.

The checklist is deliberately ordered by impact: sizing dominates everything below it. A perfect edge sized wrong still ruins; a modest edge sized right survives indefinitely.

## RoR vs Drawdown vs Bankruptcy

These are three related but distinct concepts:

- **Drawdown**: peak-to-trough decline; a portfolio property over time
- **Risk of ruin**: probability of hitting an absorbing barrier (typically zero)
- **Bankruptcy**: a legal/operational state — closing the account, defaulting on margin, returning client capital

A trader can suffer a 60% drawdown without being "ruined" in the RoR sense; a fund can be liquidated by investors at 20% drawdown without ever approaching the RoR-zero barrier. RoR is a probability-of-zero metric; drawdown management ([[drawdown-management]], [[max-drawdown]]) is the day-to-day discipline; bankruptcy is the operational endpoint.

For most practical purposes, the trader's goal is not "RoR < 1%" — it is "drawdown trajectory consistent with continuing to trade, with kill criteria that fire well before the formal RoR threshold."

## Common Mistakes

1. **Sizing for expected value, not for survivability.** Maximum-EV sizing is full-Kelly. Maximum-survivability sizing is well below it. The two are different objectives.
2. **Computing RoR from the in-sample backtest.** The in-sample win rate and payoff over-state the live edge by 30-50% on average for retail strategies. RoR computed on in-sample stats is a fantasy.
3. **Ignoring path-dependence.** Two strategies with identical aggregate stats can have wildly different RoR if one has long losing streaks and the other has short ones. The autocorrelation of P&L matters.
4. **Confusing "defined risk" with "low RoR."** Bounded per-trade loss is necessary but not sufficient for low RoR. The aggregate path of bounded losses can still ruin the account.
5. **Ignoring the convex-loss problem on short-premium books.** Calm-regime average loss does not extrapolate to stress regime.
6. **Treating RoR as a probability rather than a guarantee over enough trades.** RoR > 0 means *over enough sample paths, you will land on a ruined one*. The question is not "will I be ruined" but "how many trades before the probability of ruin compounds to certainty."
7. **Adding capital after a drawdown to "rebuild faster."** This is implicit Martingale sizing and pushes RoR toward 100% over the long run.

## Related

- [[kelly-criterion]] — the optimal-growth bet sizing whose fraction defines the RoR-vs-growth tradeoff
- [[position-sizing]] — the practical mechanism for controlling RoR
- [[options-position-sizing]] — options-specific sizing including convex-loss adjustments
- [[options-concentration-risk]] — book-level structure that elevates RoR through stacked exposures
- [[correlation-breakdown]] — the mechanism by which stress regimes blow up modelled RoR
- [[max-drawdown]] / [[maximum-drawdown]] — the path metric most directly tied to surviving toward the long-run edge
- [[drawdown-management]] — discipline for navigating drawdowns short of ruin
- [[ergodicity-economics]] — the framework that makes RoR a non-ergodic problem
- [[when-to-retire-a-strategy]] / [[kill-criteria]] — pre-committed thresholds that prevent terminal RoR
- [[tail-risk]] / [[tail-risk-hedging]] — the structural mitigation
- [[long-vol-vs-short-vol]] — the regime-asymmetric framework that defines short-premium RoR exposure
- [[the-theta-trap]] — the canonical non-ergodic ruin mode for premium-selling books
- [[options-risk-budgeting]] — the multi-Greek budget whose scenario cap enforces survivability
- [[risk-management]] — the parent discipline

## Sources

- Ralph Vince, *The Mathematics of Money Management* (1992) — the trader's reference on RoR formulas, optimal f, and ruin geometry.
- Edward Thorp, *The Kelly Criterion in Blackjack, Sports Betting, and the Stock Market* (1997) — classic exposition of Kelly and fractional Kelly in financial contexts.
- William Feller, *An Introduction to Probability Theory and Its Applications, Vol. 1* (1968), Ch. XIV — the canonical treatment of gambler's ruin.
- Nassim Taleb, *Dynamic Hedging* (1997) and *The Black Swan* (2007) — the convex-loss / fat-tail critique of standard RoR formulas.
- Ole Peters, "The Ergodicity Problem in Economics" (*Nature Physics*, 2019) — the ergodicity argument for why time-average growth (and therefore RoR) differs from expected-value growth.
- [[vix-august-2024-spike]] — empirical case study of stress-regime ruin for retail short-premium books.
