---
title: "Probabilistic Sharpe Ratio"
type: concept
created: 2026-04-10
updated: 2026-04-10
status: good
tags: [backtesting, metrics, statistics, performance]
aliases: ["PSR"]
domain: [backtesting, statistics]
difficulty: advanced
related: ["[[backtesting-overview]]", "[[sharpe-sortino-calmar]]", "[[deflated-sharpe-ratio]]", "[[minimum-track-record-length]]"]
---

# Probabilistic Sharpe Ratio

The probabilistic Sharpe ratio (PSR) computes the probability that the *true* Sharpe ratio of a strategy exceeds some benchmark threshold, given the observed Sharpe and the higher moments of the return distribution. Introduced by Bailey and López de Prado as a precursor to the deflated Sharpe ratio. Where DSR corrects for *multiple testing*, PSR corrects for *finite-sample uncertainty in a single observed Sharpe*.

## The Idea

A Sharpe ratio computed from a finite sample is a noisy estimate of the true Sharpe. If you observe Sharpe = 1.0 over 5 years, the true value could plausibly be anywhere from 0 to 2. The PSR turns this fuzziness into a probability statement: "given what I observed, what's the probability that the true Sharpe is greater than X?"

## The Formula

```
PSR(SR*) = Φ(((SR_observed − SR*) × √(T − 1)) / √(1 − γ₃ × SR_observed + ((γ₄ − 1)/4) × SR_observed²))
```

Where:
- `Φ` = CDF of the standard normal distribution
- `SR_observed` = the observed (sample) Sharpe ratio
- `SR*` = the threshold Sharpe you want to beat (often 0)
- `T` = number of return observations
- `γ₃` = skewness of returns
- `γ₄` = kurtosis of returns

For `SR* = 0`, this is the probability that the strategy has any positive Sharpe at all. For `SR* = 1`, it's the probability of beating Sharpe 1.

## Relationship to the Deflated Sharpe Ratio

Compare to the [[deflated-sharpe-ratio]] formula:

```
DSR = PSR(SR₀(N))
```

That is, DSR is just PSR with the threshold set to the expected maximum Sharpe under the null after N independent trials. PSR is the more general tool; DSR is the special case used for multiple-testing correction.

If you only ran one strategy with no selection bias, use PSR with `SR* = 0`. If you ran multiple strategies and selected the best, use DSR (which is PSR with `SR* = SR₀(N)`).

## A Worked Example

Strategy with:
- Observed Sharpe = 1.2
- 3 years of daily data (T = 756)
- Skewness = -0.3
- Excess kurtosis = 1.5

PSR(0):
```
denom = √(1 − (−0.3)(1.2) + (1.5/4)(1.2²))
      = √(1 + 0.36 + 0.54)
      = √1.90
      ≈ 1.378

z = ((1.2 − 0) × √755) / 1.378
  = (1.2 × 27.48) / 1.378
  = 32.97 / 1.378
  ≈ 23.9

PSR(0) ≈ Φ(23.9) ≈ 1.0
```

So you can be highly confident that the true Sharpe is positive. But:

PSR(1.0):
```
z = ((1.2 − 1.0) × √755) / 1.378
  = (0.2 × 27.48) / 1.378
  ≈ 3.99

PSR(1.0) ≈ Φ(3.99) ≈ 0.99997
```

You can be highly confident that the true Sharpe is at least 1.0.

PSR(1.5):
```
z = ((1.2 − 1.5) × √755) / 1.378
  = (−0.3 × 27.48) / 1.378
  ≈ −5.98

PSR(1.5) ≈ Φ(−5.98) ≈ 0.0000
```

You can be confident the true Sharpe is *not* above 1.5.

The PSR thus gives you a probabilistic confidence interval: with high confidence, the true Sharpe is between 1.0 and 1.5.

## Why This Matters

A traditional point estimate ("Sharpe = 1.2") is misleading because it suggests a precision that isn't there. PSR exposes the actual uncertainty.

Two strategies might both report Sharpe = 1.2:
- Strategy A: 10 years of data, Gaussian returns. PSR(0) ≈ 1.0, PSR(1) ≈ 0.85
- Strategy B: 1 year of data, fat tails, negative skew. PSR(0) ≈ 0.93, PSR(1) ≈ 0.40

The same headline number represents very different evidence. Strategy A has high confidence of true Sharpe near 1.2; strategy B is consistent with anything from -0.3 to 2.5.

## Common Uses

- **Manager evaluation:** "How confident are we that this manager has true skill above 0.8?"
- **Strategy comparison:** "Strategies with the same observed Sharpe but different sample sizes are not equally trustworthy."
- **Capital allocation:** "Allocate based on PSR(target), not raw Sharpe."
- **Track record marketing:** "A 3-year Sharpe of 1.5 sounds great until you see PSR(1) = 60%."

## Limitations

Same as the underlying Sharpe ratio:
- Assumes returns are stationary (no regime shifts)
- Sensitive to higher-moment estimation noise in short samples
- Cannot detect lookahead, survivorship, or selection bias
- Cannot detect crowding or future regime change

PSR fixes the *finite-sample uncertainty* problem. It does not fix any of the other backtest pathologies.

## Sources

- Bailey & López de Prado (2012) "The Sharpe Ratio Efficient Frontier" — *Journal of Risk*
- Bailey & López de Prado (2014) "The Deflated Sharpe Ratio" — *Journal of Portfolio Management*
- [[book-advances-in-financial-machine-learning]] — Chapter 14

## Related

- [[backtesting-overview]]
- [[sharpe-sortino-calmar]]
- [[deflated-sharpe-ratio]]
- [[minimum-track-record-length]]
- [[data-snooping-and-p-hacking]]
