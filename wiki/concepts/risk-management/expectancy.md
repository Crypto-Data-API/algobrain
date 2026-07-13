---
title: "Expectancy (Trading)"
type: concept
created: 2026-06-30
updated: 2026-07-01
status: review
tags: [risk-management, quantitative, backtesting]
aliases: ["Expectancy", "Trading Expectancy", "Trade Expectancy", "R-Multiple Expectancy", "System Expectancy"]
domain: [risk-management]
prerequisites: ["[[probability]]", "[[risk-reward-ratio]]"]
difficulty: beginner
related: ["[[risk-reward-ratio]]", "[[expected-return]]", "[[kelly-criterion]]", "[[risk-of-ruin]]", "[[position-sizing]]", "[[take-profit]]", "[[trading-journal]]"]
---

**Expectancy** is the average profit or loss you can expect *per trade* over a large number of trades, given a strategy's win rate and the typical size of its wins and losses. It is the single most important number for judging whether a trading system has a positive edge: a system with positive expectancy makes money on average; one with negative expectancy loses money no matter how the trades are sequenced. Expectancy answers a different question from [[risk-reward-ratio|win rate]] alone — a system can win only 35% of the time and still be highly profitable if the winners are large relative to the losers.

## Definition and formula

The standard per-trade expectancy formula is:

```
Expectancy = (Win% × Average Win) − (Loss% × Average Loss)
```

Where:
- **Win%** = fraction of trades that are profitable (e.g. 0.45)
- **Loss%** = fraction of trades that lose (= 1 − Win%, ignoring breakeven trades)
- **Average Win** = mean profit of winning trades (in currency or %)
- **Average Loss** = mean loss of losing trades (a positive number)

The result is a currency or percentage figure: "this system earns about $X per trade on average." It is mathematically the [[expected-return|expected value]] of a single trade's payoff distribution, simplified to two outcomes (a typical win and a typical loss).

### R-multiple expectancy

Traders following Van Tharp's framework normalize every trade by its initial risk, called **R** (the distance from entry to the [[stop-loss|stop]], in dollars). A win of 3× the risked amount is "+3R"; the stop being hit is "−1R". Expectancy is then measured in **R-multiples**:

```
Expectancy (in R) = average R-multiple across all trades
```

This makes systems comparable regardless of position size or account equity. An expectancy of **+0.4R** means that, on average, every trade returns 0.4 times the amount risked. Multiplying expectancy (in R) by the number of trades and by the dollars risked per trade gives the expected dollar profit — and ties directly into [[position-sizing]].

## Why it matters

- **It separates edge from luck.** A string of winners can come from a negative-expectancy system on a hot streak; positive expectancy is what survives a large sample.
- **It decouples win rate from profitability.** [[trend-following]] systems often win 30–40% of the time yet have strong positive expectancy because the average win dwarfs the average loss. Conversely, many [[options-premium-selling|premium-selling]] systems win 80–90% of trades but can have *negative* expectancy if the rare losses are catastrophic — the classic "picking up pennies in front of a steamroller" payoff.
- **It is the input to sizing.** [[kelly-criterion|Kelly]] sizing and [[risk-of-ruin|risk-of-ruin]] calculations both depend on expectancy. You cannot size a position rationally without knowing whether — and by how much — the edge is positive.

## Rules of thumb

- **Positive expectancy is necessary but not sufficient.** You also need enough trades (frequency) and the ability to survive the drawdowns along the way. Expectancy × trade frequency ≈ expected return over time.
- **Win rate alone tells you almost nothing.** Always pair it with the [[risk-reward-ratio|payoff ratio]] (average win ÷ average loss). The breakeven win rate is `1 / (1 + payoff ratio)` — with a 2:1 payoff you only need to win 33.3% of the time to break even.
- **Measure it from real, post-cost data.** Use your [[trading-journal|trading journal]]: include commissions, [[slippage]], and partial fills. Gross expectancy flatters every system.
- **Watch the sample size.** Expectancy estimated from 20 trades is mostly noise. Aim for 100+ trades, ideally across different market regimes, before trusting the number.
- **A few outliers can dominate.** If one giant winner accounts for most of the positive expectancy, the edge may be fragile. Inspect the distribution, not just the average.

## Worked example (hypothetical)

*Illustrative arithmetic, not a backtest of any real strategy.* A swing-trading system is reviewed over 100 trades:

- 40 winners, average win = **+$600**
- 60 losers, average loss = **−$250**

```
Win% = 0.40,  Loss% = 0.60
Expectancy = (0.40 × $600) − (0.60 × $250)
           = $240 − $150
           = +$90 per trade
```

Despite winning only 40% of the time, the system expects to make about **$90 per trade**. Over 100 trades that is roughly **+$9,000** in expected profit (before compounding and position-size changes). In R-multiple terms, if each trade risked $250 (1R), the average win is +2.4R and the average loss is −1R, giving:

```
Expectancy (R) = (0.40 × 2.4R) − (0.60 × 1R) = 0.96R − 0.60R = +0.36R per trade
```

Now flip the payoff: if the average win were only **+$150** with the same 40% win rate, expectancy becomes `(0.40 × 150) − (0.60 × 250) = 60 − 150 = −$90` per trade — the *same win rate* now bleeds money. This is the central lesson: win rate and expectancy are not the same thing.

## Limitations

1. **Two-outcome simplification.** The basic formula collapses a full distribution into one "typical" win and loss. Real payoffs are skewed and fat-tailed; a single tail loss can swamp many small wins (see [[tail-risk]]).
2. **Assumes stationarity.** Past expectancy predicts future expectancy only if the edge persists. Markets adapt, and edges decay — re-measure regularly.
3. **Sequence and drawdown ignored.** A positive-expectancy system can still produce a [[drawdown]] deep enough to breach your [[risk-tolerance]] (or trigger margin calls) before the average asserts itself. Expectancy says nothing about *path*; pair it with [[risk-of-ruin]].
4. **Estimation error.** Small samples and survivorship/cherry-picking bias inflate measured expectancy, the trade-level analogue of backtest [[overfitting]].
5. **Position size assumed constant.** The simple per-trade figure assumes uniform risk per trade; varying size (e.g. Kelly scaling) changes the realized result.

## Related

- [[risk-reward-ratio]] — the payoff ratio that, with win rate, determines expectancy
- [[expected-return]] — expectancy is the expected value of a trade's payoff distribution
- [[kelly-criterion]] — optimal sizing given a positive expectancy
- [[risk-of-ruin]] — probability of blowing up even with positive expectancy
- [[position-sizing]] — converts R-multiple expectancy into dollar terms
- [[trading-journal]] — the data source for measuring real, post-cost expectancy
- [[take-profit]] / [[stop-loss]] — define the average win and average loss
