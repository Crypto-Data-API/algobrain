---
title: "Monte Carlo Backtesting"
type: concept
created: 2026-04-06
updated: 2026-04-07
status: good
tags: [ai-trading, backtesting, methodology, statistics]
related:
  - "[[walk-forward-optimization]]"
  - "[[backtesting-pitfalls]]"
  - "[[vectorbt]]"
  - "[[bot-risks-and-pitfalls]]"
  - "[[book-building-winning-algo-trading-systems]]"
  - "[[book-fooled-by-randomness]]"
  - "[[book-probabilistic-ml-for-finance]]"
---

# Monte Carlo Backtesting

Monte Carlo simulation assesses strategy robustness by generating **thousands of randomized variations** of the historical backtest. Instead of relying on one historical path, you test whether the strategy works across a distribution of plausible outcomes. If it only works on the exact historical sequence, it is fragile. If it works across 1,000 randomized paths, it is robust.

---

## Overview

A single backtest shows what *did* happen, not what *could* have. Monte Carlo methods explore the space of possibilities by randomizing aspects of the backtest while preserving core statistical properties. This complements [[walk-forward-optimization]] (temporal robustness) by testing **distributional robustness**.

---

## Randomization Methods

1. **Trade Shuffling**: Randomly reorder completed trades 1,000+ times. Tests whether the equity curve (especially max drawdown) was lucky or structural (Source: [[book-building-winning-algo-trading-systems]]).
2. **Return Resampling (Bootstrap)**: Sample returns with replacement, creating synthetic series with same statistical properties but different paths (Source: [[book-probabilistic-ml-for-finance]]).
3. **Noise Injection**: Add random slippage to fills, skip some orders, vary timing.
4. **Parameter Perturbation**: Vary parameters within a small range. If strategy breaks with 10% change, it is [[backtesting-pitfalls|overfit]].

---

## Output: Distribution of Outcomes

Each Monte Carlo run produces a different equity curve. From 1,000 runs, you get distributions of:

| Metric | What It Tells You |
|---|---|
| **Final return** | Range of realistic outcomes (5th, 50th, 95th percentile) |
| **Max drawdown** | Worst-case drawdown you should prepare for |
| **Sharpe ratio** | Confidence interval around risk-adjusted return |
| **Consecutive losses** | Longest likely losing streak |
| **Time to recovery** | How long drawdowns typically last |

The **5th percentile max drawdown** is critical -- this is the drawdown you should size your position for, not the single historical drawdown.

---

## Example

```python
import numpy as np
trade_returns = np.array([0.02, -0.01, 0.03, -0.02, ...])
results = []
for _ in range(1000):
    shuffled = np.random.permutation(trade_returns)
    equity = np.cumprod(1 + shuffled)
    results.append(equity[-1] - 1)
print(f"Median: {np.median(results):.2%}, 5th pct: {np.percentile(results, 5):.2%}")
```

[[vectorbt]] makes this particularly fast -- 1,000 simulations in seconds.

---

## Interpretation

**Narrow distribution** = robust; **wide** = fragile (Source: [[book-fooled-by-randomness]]). If the 5th percentile is still positive, the strategy likely has a real edge. The 95th percentile max drawdown is the drawdown to plan for. Monte Carlo should be the **final validation step**: develop idea, [[walk-forward-optimization|walk-forward test]], Monte Carlo, paper trade, then deploy live.

---

## Sources

- [[book-building-winning-algo-trading-systems]] — Monte Carlo simulation as a core validation step, including trade shuffling, parameter perturbation, and distribution-based position sizing
- [[book-fooled-by-randomness]] — the philosophical case for why single-path backtests are dangerous and why distributional thinking is essential
- [[book-probabilistic-ml-for-finance]] — Tatsat et al. (2023) cover Monte Carlo simulation methods for financial applications, including bootstrapping, Bayesian approaches to uncertainty quantification, and probabilistic portfolio risk assessment

## See Also

- [[walk-forward-optimization]] -- Complementary temporal robustness testing
- [[backtesting-pitfalls]] -- The sins Monte Carlo helps detect
- [[vectorbt]] -- Fast enough to run 1000+ simulations efficiently
- [[bot-risks-and-pitfalls]] -- Live deployment risks after validation
