---
title: "Sharpe, Sortino, and Calmar Ratios"
type: concept
created: 2026-04-10
updated: 2026-06-21
status: excellent
tags: [backtesting, metrics, performance, risk-adjusted-returns]
aliases: ["Sharpe Ratio", "Sortino Ratio", "sortino-ratio", "Calmar Ratio", "Risk-Adjusted Return Ratios"]
domain: [backtesting, performance-measurement]
difficulty: beginner
related: ["[[backtesting-overview]]", "[[sharpe-ratio]]", "[[sortino-ratio]]", "[[deflated-sharpe-ratio]]", "[[probabilistic-sharpe-ratio]]", "[[minimum-track-record-length]]", "[[information-ratio]]", "[[maximum-drawdown]]", "[[value-at-risk]]", "[[tail-risk]]", "[[geometric-mean]]"]
---

# Sharpe, Sortino, and Calmar Ratios

The three classic risk-adjusted return ratios. Each tries to express "return per unit of risk" but uses a different definition of risk. Each is misleading on its own, and each has specific failure modes that make it unsuitable for some kinds of strategies.

## At a Glance

| Ratio | Numerator | Denominator (risk) | Best for | Blind spot |
|---|---|---|---|---|
| [[sharpe-ratio\|Sharpe]] | excess return | total std dev | Gaussian, similar-skew strategies | punishes upside; assumes normality |
| [[sortino-ratio\|Sortino]] | excess (vs target) | downside std dev | positively-skewed strategies | noisier; still drawdown-blind |
| **Calmar** | annualized return | max drawdown | long, stable track records | single-point; needs ≥ 5 yrs |

The three answer different questions: Sharpe asks "how bumpy?"; Sortino asks "how bumpy *to the downside*?"; Calmar asks "what's the worst it got, and how fast did it earn that back?" A complete evaluation reports all three (plus the extras in [[#Combining Metrics]]) because each is gameable in isolation — and the gaming directions differ, so disagreement among them is itself a signal.

## The Sharpe Ratio

The most widely used performance metric. Defined as:

```
Sharpe = (mean return − risk-free rate) / std(returns)
```

Annualized by multiplying by `√T` where T is the number of periods per year (252 for daily, 12 for monthly).

### What it measures
Excess return per unit of volatility. A higher Sharpe means more return per unit of risk *as measured by standard deviation*.

### Rough rule of thumb
- **<0** — losing money
- **0-0.5** — bad
- **0.5-1.0** — okay, market-like
- **1.0-2.0** — good
- **2.0+** — excellent (and often suspicious — see [[deflated-sharpe-ratio]])
- **>4** — almost always either fraud, lookahead bias, or capacity-constrained edge

### Strengths
- Single number, easy to compare
- Widely understood
- Statistically tractable (has known sampling distribution)
- Scale-invariant (doesn't depend on capital size)

### Weaknesses

1. **Penalizes upside volatility.** A strategy with huge winning days and tiny losing days has the same Sharpe as one with the variance reversed. Investors care about downside, not total volatility.

2. **Assumes normal returns.** Sharpe is correctly interpreted only for Gaussian returns. Most trading returns are skewed and fat-tailed; Sharpe overstates the quality of negatively-skewed strategies (selling vol, picking up nickels in front of steamrollers) and understates positively-skewed strategies (trend following, long-vol).

3. **Insensitive to drawdown duration.** A strategy that loses 30% in one month and recovers vs. one that loses 30% over three years can have the same Sharpe. The second is much harder to actually trade.

4. **Easy to game.** Selling out-of-the-money options, leverage stacking, and mark-to-model accounting all inflate Sharpe by hiding tail risk.

5. **Backward-looking.** Past Sharpe is a noisy estimator of future Sharpe. See [[probabilistic-sharpe-ratio]] for confidence intervals.

6. **Selection-biased.** When you pick the best of N strategies, the winning Sharpe is biased upward. See [[deflated-sharpe-ratio]].

### When to use it
- Comparing strategies with similar return distributions (similar skew, kurtosis)
- Communicating with investors who expect it
- Quick first-pass filtering of strategy ideas

### When NOT to use it
- Comparing strategies with very different return distributions
- Evaluating tail-risk strategies (vol selling, naked shorts)
- As the sole criterion for any production decision

## The Sortino Ratio

Defined as:

```
Sortino = (mean return − target return) / downside_std(returns)
```

Where `downside_std` is the standard deviation computed only over periods where returns fell below the target. The target is typically 0 or the risk-free rate.

### What it measures
Excess return per unit of downside risk. Same idea as Sharpe but only counts the bad volatility.

### Why it exists
Sharpe penalizes large positive returns the same as large negative returns. Investors don't experience these symmetrically. Sortino fixes this by ignoring upside volatility.

### Strengths
- More aligned with how investors actually feel about risk
- Better metric for positively-skewed strategies (trend following, long convexity)
- Less easily gamed by adding a wing of high-upside outcomes

### Weaknesses
- Less data to compute (you only have downside observations), so noisier
- Still can't see drawdown duration
- Still can be gamed by negatively-skewed strategies (you reduce downside std by avoiding small losses while building up tail risk)
- No closed-form distribution, harder statistical inference

### When to use it
- Strategies with substantial positive skew where Sharpe undersells them
- When comparing to a target return rather than zero
- Investor reporting where you want to highlight asymmetry

### When NOT to use it
- Comparing strategies with vastly different time series lengths
- As the sole criterion (same warning as Sharpe)

## The Calmar Ratio

Defined as:

```
Calmar = annualized return / max drawdown
```

Where max drawdown is the largest peak-to-trough decline in the equity curve, expressed as a positive number. Sometimes called the MAR ratio (managed account ratio).

### What it measures
Return relative to the worst loss the strategy experienced. A Calmar of 1 means the strategy made back its largest drawdown in one year.

### Strengths
- Aligned with how investors think about risk: "what's the worst that could happen?"
- Drawdown-aware unlike Sharpe and Sortino
- Easy to interpret: a 30% return with a 30% drawdown is Calmar 1.0
- Less gameable by hidden tail risk (the tail eventually shows up in drawdown)

### Weaknesses
- Single-point sensitive: depends entirely on the worst drawdown observation, which is the noisiest summary statistic possible
- Unstable in short backtests (the max drawdown grows with sample size)
- Doesn't capture frequency of drawdowns (one big drawdown vs. many small ones)
- Gives no credit for upside

### When to use it
- Long-running strategies with stable drawdown statistics
- Comparing strategies whose tails matter as much as their means
- Investor communication about worst-case risk

### When NOT to use it
- Short backtests (< 5 years) where max drawdown is highly path-dependent
- Strategies whose drawdown profile changes with regime

## Which Ratio for Which Strategy

The right primary ratio depends on the strategy's return distribution. Pick the one whose risk definition matches what actually hurts the strategy.

| Strategy archetype | Skew | Primary ratio | Why | Trap if you use Sharpe alone |
|---|---|---|---|---|
| Vol selling / [[options-premium-selling\|premium selling]] | negative | Calmar + tail/CVaR | Risk lives in the drawdown tail, not daily std | Sharpe looks great until the tail event |
| [[trend-following\|Trend following]] / [[long-volatility-strategies\|long vol]] | positive | Sortino | Big winners shouldn't be penalized as "risk" | Sharpe *understates* the strategy |
| [[long-vol-overlay\|Long-vol overlay]] (stand-alone) | very positive | Sortino + geometric return | Convexity; downside is the bounded premium | Negative Sharpe hides portfolio-level value |
| Market-neutral / [[pairs-trading\|stat-arb]] | ~symmetric | Sharpe | Returns roughly Gaussian; Sharpe is valid | (few — this is Sharpe's home turf) |
| Active manager vs index | varies | [[information-ratio\|Information ratio]] | Skill measured against a benchmark | Absolute Sharpe ignores the benchmark |
| Managed futures / CTA | varies | Calmar / [[mar-ratio\|MAR]] | Investors size by worst drawdown | Sharpe ignores path and duration |

Rule of thumb: if a strategy's edge **comes from** bearing tail risk (selling insurance), never report Sharpe alone — it is precisely the metric that hides the risk you are paid for. Conversely, a [[long-vol-overlay|long-vol]] or tail-hedge sleeve can show a *negative* Sharpe yet add value to the combined book (its value is convex and shows up in the geometric return and the drawdown profile, not the volatility-scaled mean). See [[vix-calls]] for a worked case of a sleeve with negative stand-alone Sharpe.

## Other Useful Variants

### Information Ratio
```
IR = (strategy return − benchmark return) / std(strategy return − benchmark return)
```
Like Sharpe but relative to a benchmark instead of the risk-free rate. Used heavily in asset management to measure manager skill against an index.

### Omega Ratio
```
Ω(threshold) = E[max(R − threshold, 0)] / E[max(threshold − R, 0)]
```
Ratio of expected gains above a threshold to expected losses below it. Captures the entire return distribution, not just two moments. Theoretically superior to Sharpe but harder to communicate.

### Sterling Ratio
Similar to Calmar but uses the average of the N worst drawdowns rather than just the maximum. Less single-point sensitive.

### MAR (Managed Account Ratio)
Identical to Calmar by some definitions; see Calmar.

## Combining Metrics

No single number is enough. A defensible performance summary includes:

1. **Annualized return** (both arithmetic and geometric)
2. **Annualized volatility**
3. **Sharpe** (raw and deflated — see [[deflated-sharpe-ratio]])
4. **Sortino**
5. **Max drawdown** and **drawdown duration**
6. **Calmar**
7. **Win rate**
8. **Profit factor** (gross gains / gross losses)
9. **Skewness** and **kurtosis**
10. **Tail risk** (CVaR / expected shortfall at 95%)

Together these tell a story that no single ratio can. A Sharpe of 1.5 with negative skew, fat tails, and 50% max drawdown is *not* the same investment as a Sharpe of 1.5 with positive skew, normal tails, and 12% max drawdown — even though both numbers look identical on a one-line summary.

## Worked Example: Same Returns, Three Ratios

*Illustrative arithmetic, not a backtest of any real strategy.* Take a hypothetical 12-month return stream (in %):

```
+3, +2, +4, −1, +3, −6, +2, +5, +1, −2, +4, +3
```

Annual statistics (assume risk-free ≈ 0, target = 0):

- Sum of monthly returns ≈ **+18%** for the year (use as the annualized return figure).
- Mean monthly ≈ +1.5%; monthly std dev ≈ 3.0%.
- Downside-only deviations (months below 0: −1, −6, −2) → downside std ≈ 2.0%.
- Worst peak-to-trough in the equity curve (the −6 month, partly cushioned) → max drawdown ≈ **6%**.

Plugging in (annualizing monthly figures by √12 ≈ 3.46):

| Ratio | Calculation | Result |
|---|---|---|
| [[sharpe-ratio\|Sharpe]] | (1.5% / 3.0%) × √12 | ≈ **1.7** |
| [[sortino-ratio\|Sortino]] | (1.5% / 2.0%) × √12 | ≈ **2.6** |
| Calmar | 18% / 6% | ≈ **3.0** |

The same return stream produces three quite different headline numbers. Sortino > Sharpe because the upside volatility (the +5, +4 months) inflates the Sharpe denominator but not the Sortino denominator — a sign of mild positive asymmetry. Calmar looks strongest of all, but on only 12 months it is the least trustworthy: the −6% drawdown is a single observation, and a 13th bad month could halve it. This is exactly why the page's guidance is to report all three and read their **disagreement** as information, not to anchor on whichever one flatters the strategy.

## Statistical Significance

A Sharpe ratio computed from N years of data has standard error approximately:

```
SE(Sharpe) ≈ √((1 + 0.5 × Sharpe²) / N)
```

Implications:
- A Sharpe of 1.0 over 1 year has SE ≈ 1.22 (essentially uninformative)
- A Sharpe of 1.0 over 5 years has SE ≈ 0.55 (marginally informative)
- A Sharpe of 1.0 over 10 years has SE ≈ 0.39 (informative)
- A Sharpe of 1.0 over 20 years has SE ≈ 0.27 (clearly significant if positive)

Most "great track records" you hear about — three years, Sharpe 2.0 — have huge confidence intervals. The point estimate may be 2.0; the 95% interval may be 0.4 to 3.6.

See [[probabilistic-sharpe-ratio]] and [[minimum-track-record-length]] for the formal versions.

## Sources

- Sharpe (1966) "Mutual Fund Performance" — *Journal of Business* (the original)
- Sortino & Price (1994) "Performance Measurement in a Downside Risk Framework"
- Young (1991) "Calmar Ratio: A Smoother Tool" — *Futures Magazine*
- [[book-advances-in-financial-machine-learning]] — López de Prado on the limitations of Sharpe

## Related

- [[backtesting-overview]] — where these ratios fit in the validation pipeline
- [[sharpe-ratio]] — the dedicated page on the headline ratio
- [[sortino-ratio]] — downside-only variant in depth
- [[deflated-sharpe-ratio]] — correcting Sharpe for multiple testing / selection bias
- [[probabilistic-sharpe-ratio]] — confidence intervals on Sharpe
- [[minimum-track-record-length]] — how long a track record must be to trust it
- [[information-ratio]] — benchmark-relative skill measure
- [[maximum-drawdown]] — the denominator of Calmar
- [[geometric-mean]] — the compounded return ratios should be read alongside
- [[value-at-risk]] — tail-risk metric to report with the ratios
- [[tail-risk]] — what negatively-skewed strategies hide from Sharpe
- [[long-vol-overlay]], [[vix-calls]] — sleeves with negative stand-alone Sharpe but portfolio value
