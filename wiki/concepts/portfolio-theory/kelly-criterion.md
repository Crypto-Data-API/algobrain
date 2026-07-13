---
title: "Kelly Criterion"
type: concept
created: 2026-04-07
updated: 2026-04-07
status: good
tags: [risk-management, portfolio-theory, position-sizing, quantitative]
aliases: ["Kelly Formula", "Kelly Bet"]
related: ["[[position-sizing]]", "[[ed-thorp]]", "[[risk-management]]", "[[a-man-for-all-markets]]", "[[sharpe-ratio]]", "[[risk-of-ruin]]"]
domain: [risk-management, portfolio-theory]
difficulty: intermediate
---

The Kelly Criterion is a mathematical formula for determining the optimal size of a series of bets or trades to maximize long-term geometric growth of capital. Originally developed by John L. Kelly Jr. at Bell Labs in 1956 for signal noise problems, it was adapted to gambling and financial markets by [[ed-thorp]] and has become a foundational concept in [[position-sizing]] and [[risk-management]].

## Overview

The core insight of the Kelly Criterion is that there exists a mathematically optimal fraction of capital to risk on any given opportunity. Betting too little leaves returns on the table; betting too much increases [[volatility]] and the risk of catastrophic drawdowns. The Kelly fraction maximizes the expected logarithmic growth rate of wealth, which is equivalent to maximizing long-term compounded returns.

The formula in its simplest form for a binary outcome is:

**f\* = (bp - q) / b**

Where:
- **f\*** = fraction of capital to wager
- **b** = net odds received (e.g., 2:1 means b = 2)
- **p** = probability of winning
- **q** = probability of losing (1 - p)

For a trade with a 60% win rate and 2:1 reward-to-risk ratio: f* = (2 x 0.60 - 0.40) / 2 = 0.40, meaning the optimal bet is 40% of capital.

## How It Works

### Mathematical Foundation

The Kelly Criterion maximizes the expected value of the logarithm of wealth, E[log(W)]. This is significant because:

1. **Geometric growth** -- compounded returns depend on the product of (1 + return) across periods, not the sum
2. **Log utility** -- treating the logarithm of wealth as the utility function naturally penalizes large losses more than it rewards equivalent gains
3. **Long-run dominance** -- a Kelly bettor will, with probability approaching 1, eventually outperform any other fixed-fraction strategy over a sufficiently long time horizon

### Continuous Kelly for Trading

In markets with continuous outcomes (not just win/lose), the Kelly fraction generalizes to:

**f\* = mu / sigma^2**

Where **mu** is the expected excess return and **sigma^2** is the variance of returns. This connects Kelly sizing directly to the [[sharpe-ratio]] -- higher Sharpe strategies warrant larger position sizes.

### Fractional Kelly

Full Kelly sizing produces the maximum growth rate but also generates significant [[volatility]] in the equity curve. Drawdowns of 50-80% are mathematically expected even with a genuine edge. For this reason, practitioners almost universally use **fractional Kelly**:

- **Half-Kelly (f\*/2)** -- the most common choice. Achieves approximately 75% of the growth rate with roughly half the volatility. [[ed-thorp]] advocated this approach.
- **Quarter-Kelly (f\*/4)** -- ultra-conservative, used when parameter estimates are uncertain.

The key tradeoff: fractional Kelly sacrifices some growth rate for a dramatically smoother equity curve and reduced [[risk-of-ruin]].

## Trading Applications

### Position Sizing

The Kelly Criterion provides a principled answer to "how much should I risk on this trade?" rather than relying on arbitrary rules like "risk 1% per trade." Steps for application:

1. Estimate the trade's expected return (edge)
2. Estimate the variance or distribution of outcomes
3. Calculate the Kelly fraction
4. Apply a fractional multiplier (typically 0.25 to 0.50) for safety

### Portfolio Allocation

Kelly extends to multiple simultaneous positions. The multi-asset Kelly formula accounts for [[correlation]] between positions and produces an optimal portfolio allocation vector. This connects to [[modern-portfolio-theory]] but optimizes for geometric growth rather than single-period mean-variance.

### Practical Limitations

- **Parameter uncertainty** -- the formula requires accurate estimates of edge and variance; estimation errors can be devastating, especially when they overstate the edge
- **Non-stationary markets** -- win rates and payoff ratios change over time, making historical estimates unreliable
- **Fat tails** -- the formula assumes known distributions; [[black-swan]] events make full Kelly dangerous
- **Psychological tolerance** -- full Kelly drawdowns are psychologically brutal; most traders cannot maintain discipline through them

### Notable Practitioners

- **[[ed-thorp]]** -- pioneered Kelly application in blackjack and convertible-arbitrage, documented in [[a-man-for-all-markets]]
- **Warren Buffett** -- implicitly uses Kelly-like concentration when conviction is highest
- **Jim Simons** -- [[renaissance-technologies]] reportedly uses Kelly-based sizing in its [[medallion-fund]]

## Related

- [[position-sizing]] -- broader topic of determining trade size
- [[risk-management]] -- Kelly is one tool within a comprehensive risk framework
- [[risk-of-ruin]] -- probability of total loss that Kelly aims to minimize
- [[sharpe-ratio]] -- directly related to the continuous Kelly fraction
- [[modern-portfolio-theory]] -- alternative framework optimizing mean-variance rather than geometric growth
- [[correlation]] -- essential input for multi-asset Kelly optimization

## Sources

- [[book-a-man-for-all-markets]] -- Ed Thorp's account of applying Kelly to markets
- [[book-quantitative-trading-ernest-chan]] -- practical implementation of Kelly sizing for algorithmic strategies
