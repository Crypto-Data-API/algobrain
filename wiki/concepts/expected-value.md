---
title: "Expected Value"
type: concept
created: 2026-07-01
updated: 2026-07-01
status: review
tags: [risk-management, quantitative, behavioral-finance]
aliases: ["Expected Value", "EV", "Expectancy", "Trade Expectancy", "Positive Expectancy"]
domain: [risk-management, behavioral-finance]
prerequisites: ["[[probability]]", "[[risk-reward-ratio]]"]
difficulty: beginner
related: ["[[expected-return]]", "[[kelly-criterion]]", "[[win-rate]]", "[[probability-of-profit]]", "[[risk-of-ruin]]", "[[asymmetric-risk-reward]]", "[[risk-reward-ratio]]", "[[position-sizing]]", "[[probability]]", "[[base-rate]]", "[[law-of-large-numbers]]"]
---

**Expected value (EV)** is the probability-weighted average of every possible outcome of a decision — the long-run average result if the same bet were repeated many times. In trading it is the single most important number behind any system: a strategy with **positive expected value** (positive *expectancy*) makes money over a large enough sample, and one with negative EV loses, no matter how good or bad any individual trade feels. EV is the bridge between [[probability]] and profit.

## Definition and Formula

For a set of mutually exclusive outcomes:

```
EV = Σ ( p_i × x_i )
```

where `p_i` is the probability of outcome `i` and `x_i` is its payoff (gains positive, losses negative). A bet is "fair" at EV = 0, profitable above it, and a losing proposition below it.

### Trade expectancy

For a trading system with just two outcomes — a win or a loss — EV collapses to the familiar **expectancy** formula:

```
Expectancy = (Win% × Average Win) − (Loss% × Average Loss)
```

Expressed per dollar risked (in "R-multiples," where 1R is the amount risked per trade):

```
Expectancy (in R) = (Win% × AvgWin_R) − (Loss% × 1)
```

A system with positive expectancy is profitable *on average per trade*; multiplying expectancy by the number of trades gives the expected profit, and trade frequency turns a small per-trade edge into a meaningful return stream.

## Worked Example

A setup wins 40% of the time. Winners average +2.5R; losers average −1R.

```
Expectancy = (0.40 × 2.5) − (0.60 × 1.0)
           = 1.00 − 0.60
           = +0.40R per trade
```

Despite **losing 60% of its trades**, the system makes +0.40R on average because the [[risk-reward-ratio|reward-to-risk]] more than compensates for the low [[win-rate]]. Over 200 trades risking 1% each, the expected gain is roughly 80% of the per-trade risk unit summed — the precise outcome varies with sequencing and compounding, but the *direction* is fixed by the positive sign of EV. This is why a high win rate is neither necessary nor sufficient: it is the *combination* of hit rate and payoff that determines EV (see [[asymmetric-risk-reward]]).

## Win Rate and Payoff Are a Trade-off

For breakeven (EV = 0), the required win rate is a function of the reward-to-risk ratio `b` (average win ÷ average loss):

```
Breakeven Win% = 1 / (1 + b)
```

- A 1:1 payoff needs to win **50%** of the time to break even.
- A 2:1 payoff needs only **33%**.
- A 3:1 payoff needs only **25%**.

Trend-following systems live in the low-win-rate / high-payoff corner; mean-reversion and premium-selling systems live in the high-win-rate / low-payoff corner. Both can have positive EV — they just earn it differently.

## EV in Options

Options make EV explicit because both legs are quantifiable. A trade's [[probability-of-profit|probability of profit (POP)]], its maximum gain, and its maximum loss define an EV directly. A high-POP credit trade (e.g. selling an out-of-the-money put) can still be **negative EV** if the occasional large loss outweighs the many small wins — the classic "picking up pennies in front of a steamroller" payoff. Conversely a low-POP long option can be positive EV if the rare payoff is large enough. POP alone never tells you whether a trade is worth taking; only EV does.

## EV vs Expected Return

Expected value and [[expected-return|expected return]] are closely related but used in different contexts:

- **Expected value** is the general decision-theory quantity — the probability-weighted payoff of *any* bet, trade, or scenario, usually expressed in dollars or R-multiples.
- **[[expected-return]]** is EV applied specifically to an asset's *percentage return distribution*, the central input to portfolio construction and [[capm|CAPM]]-style pricing.

The same arithmetic underlies both; "expected value" is the term traders reach for when sizing an individual trade or system, "expected return" the term used for allocating across assets.

## Why Positive EV Is Not Enough

Positive expected value is **necessary but not sufficient** for survival, because EV describes the long-run *average* and ignores the *path*:

- **Variance and ruin.** A positive-EV bet sized too large can still bankrupt you before the long run arrives — the [[risk-of-ruin|gambler's ruin]] problem. EV tells you *whether* to bet; the [[kelly-criterion|Kelly criterion]] and [[position-sizing]] tell you *how much* so that variance does not lead to [[risk-of-ruin|ruin]].
- **The law of large numbers is slow.** EV only manifests over many independent repetitions ([[law-of-large-numbers]]). A small sample can deviate wildly from EV, which is why edge takes a long time to confirm and why traders over-react to recent results ([[base-rate|base-rate neglect]]).
- **Estimation error.** The `p_i` and `x_i` are estimates. Overstating win rate or average win — common after a naive backtest — flips a real edge into an imagined one.
- **Fat tails and non-stationarity.** A single extreme outcome can dominate the average, and an edge that existed historically can decay. EV computed on a regime that has ended is misleading.

## Related

- [[expected-return]] — EV applied to asset return distributions
- [[kelly-criterion]] — turning positive EV into optimal bet size
- [[win-rate]] / [[risk-reward-ratio]] — the two ingredients of trade expectancy
- [[probability-of-profit]] — the options analogue, and why it is not EV
- [[risk-of-ruin]] — why sizing matters even with positive EV (a.k.a. the gambler's ruin)
- [[asymmetric-risk-reward]] — earning EV through payoff rather than hit rate
- [[law-of-large-numbers]] — why EV only shows up over many trades
- [[base-rate]] — the probability inputs EV depends on

## Sources

- Expected value is a foundational result of probability theory (Huygens, 1657; Pascal–Fermat correspondence, 1654).
- Edward Thorp, *Beat the Dealer* (1962) and *A Man for All Markets* (2017) — applying positive-expectation betting and sizing to blackjack and markets.
- Van K. Tharp, *Trade Your Way to Financial Freedom* — the trading "expectancy" and R-multiple framing.
