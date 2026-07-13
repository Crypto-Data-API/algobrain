---
title: "Drawdown"
type: concept
created: 2026-04-13
updated: 2026-06-11
status: good
tags: [risk-management, backtesting, portfolio-theory]
aliases: ["Maximum Drawdown", "MaxDD", "Drawdown", "Drawdown Management", "Managing Drawdowns", "Underwater Equity"]
domain: [risk-management]
difficulty: beginner
prerequisites: ["[[risk-management-overview]]"]
related: ["[[equity-curve]]", "[[sharpe-ratio]]", "[[calmar-ratio]]", "[[risk-management-overview]]", "[[risk-of-ruin]]", "[[position-sizing]]", "[[market-crashes]]", "[[tail-risk]]", "[[trend-plus-tail-hedge]]", "[[value-at-risk]]", "[[crisis-alpha]]"]
---

# Drawdown

Drawdown is the peak-to-trough decline in portfolio value before a new high is reached. Maximum drawdown (MaxDD) is the largest such decline over a period — it measures the worst-case loss an investor would have experienced. Drawdown depth, duration, and recovery time are critical risk metrics alongside [[sharpe-ratio]]. A strategy with high returns but deep drawdowns may be psychologically impossible to hold through.

## Types of Drawdown

There are several ways to measure and characterize drawdowns:

- **Maximum drawdown (MaxDD)**: The deepest peak-to-trough decline over the entire measurement period. This is the single worst experience an investor would have endured. Formula: `DD = (Peak - Trough) / Peak`. A portfolio that rises from $100 to $200 and then falls to $120 has a maximum drawdown of 40% (($200 - $120) / $200).
- **Average drawdown**: The mean of all individual drawdown episodes. This captures the "typical" pain level rather than the worst case. A strategy with a low average drawdown but high maximum drawdown has one catastrophic episode and many mild ones.
- **Longest drawdown (recovery time)**: The calendar time from a peak to when a new peak is reached. The S&P 500 took over 5 years to recover from the 2008 crisis peak and over 7 years to recover from the 2000 peak. For investors who need liquidity or who lose patience, duration can be more damaging than depth.

## Historical Drawdowns

Major drawdowns in equities and crypto illustrate the severity of [[tail-risk]] events:

| Market | Event | Period | Maximum Drawdown |
|--------|-------|--------|-----------------|
| S&P 500 | Great Depression | 1929-1932 | -86% |
| S&P 500 | Oil embargo / Watergate | 1973-1974 | -48% |
| S&P 500 | Dot-com bust | 2000-2002 | -49% |
| S&P 500 | Global financial crisis | 2007-2009 | -57% |
| S&P 500 | COVID crash | Feb-Mar 2020 | -34% |
| S&P 500 | Rate hiking cycle | 2022 | -25% |
| Bitcoin | Crypto winter | 2017-2018 | -84% |
| Bitcoin | FTX / LUNA collapse cycle | 2021-2022 | -77% |

These are not outliers — they are the recurring cost of holding risky assets. Any long-term investor will experience multiple severe drawdowns across a career.

## Drawdown vs Volatility

Volatility (standard deviation of returns) and drawdown are both risk metrics, but they measure fundamentally different things:

- **Volatility is symmetric** — it penalizes upside moves and downside moves equally. A strategy that gains 5% one day and loses 5% the next has high volatility but zero drawdown.
- **Drawdown is asymmetric** — it only measures losses from peaks. This makes it a more intuitive measure of investor pain, since investors do not suffer from upside volatility.
- **Low volatility does not guarantee shallow drawdowns.** Mean-reversion strategies can have low day-to-day volatility for months, then experience sudden catastrophic drawdowns when the mean fails to revert (e.g., a pairs trade where the spread blows out permanently). The strategy looks calm on a volatility basis but devastating on a drawdown basis.
- **MaxDD is more intuitive for investors** than standard deviation. Telling an investor "your strategy has 15% annualized volatility" means little. Telling them "you could lose 40% before recovering" is immediately understood.

For these reasons, many practitioners prefer drawdown-based risk metrics ([[sharpe-ratio]] penalizes all volatility; the Calmar ratio — return divided by max drawdown — specifically penalizes downside extremes).

## Recovery Math

The mathematics of recovery from drawdowns is deeply asymmetric:

| Drawdown | Gain Required to Recover |
|----------|-------------------------|
| -10% | +11.1% |
| -20% | +25.0% |
| -30% | +42.9% |
| -50% | +100.0% |
| -75% | +300.0% |
| -90% | +900.0% |

A 50% drawdown requires a 100% gain to recover. A 75% drawdown requires 300%. This asymmetry is why [[tail-risk]] management matters so profoundly — deep drawdowns are mathematically devastating. A portfolio that falls 90% (as the S&P 500 did during the Great Depression, or as Bitcoin did in 2018) needs to increase tenfold just to break even. At historical equity return rates of ~10% annually, a 90% drawdown would take approximately 24 years to recover from.

This recovery math is the core argument for strategies like [[trend-plus-tail-hedge]] that sacrifice some upside in normal markets to prevent catastrophic drawdowns.

## The Ulysses Contract Problem

Many investors panic-sell near the bottom of a drawdown. Research consistently shows that retail investors underperform their own funds by 1-2% annually because they buy after rallies and sell during drawdowns. The psychological difficulty of holding through deep or prolonged drawdowns is one of the most important practical constraints in portfolio management.

This creates a paradox: strategies with the highest long-run returns often have the deepest drawdowns, but human psychology makes those drawdowns impossible to sit through. Pure [[tail-risk-hedging]] (like [[universa-investments]]) has enormous long-run expected returns when tail events hit, but it bleeds for years at a time — a drawdown of a different kind that is equally hard to tolerate. [[trend-plus-tail-hedge]] addresses this by keeping the bleed manageable: trend-following profits in normal markets offset hedging costs, making the portfolio psychologically sustainable during the long stretches between crises.

The concept of a "Ulysses contract" — committing in advance to a strategy and removing the ability to deviate during stress — is one approach to the drawdown psychology problem. Systematic, rules-based strategies enforce discipline that discretionary investors cannot maintain.

## Drawdown Management (Trading Relevance)

For a working trader, drawdown is not just a backtest statistic — it is the live constraint that determines whether a strategy stays funded and whether the trader can keep executing it. "Drawdown management" is the set of rules and tools used to keep realised drawdown inside a tolerable band:

- **Drawdown-based position sizing.** Many systematic books de-risk as the equity curve falls below its high-water mark. A common rule scales gross exposure down linearly once a 10% drawdown is breached and halts new risk entirely at a hard ceiling (e.g., 20-25%). This caps the *compounding* of losses precisely when the recovery math (above) is most punishing. See [[position-sizing]] and [[risk-of-ruin]].
- **The Calmar ratio as the headline metric.** The [[calmar-ratio]] (annualised return ÷ maximum drawdown over a trailing 36 months) is the drawdown-native analogue of the [[sharpe-ratio]]. Allocators frequently prefer it because investors experience drawdown, not standard deviation. A strategy with a 1.0+ Calmar is generally considered institutionally allocatable.
- **High-water-mark logic.** Performance fees and many internal risk budgets reset to the high-water mark, so a deep drawdown means the manager works "below the line" — collecting no incentive fee — until the prior peak is recovered. This aligns the manager's incentives with limiting drawdown depth and duration, not just maximising raw return.
- **Drawdown as a kill criterion.** Per [[when-to-retire-a-strategy]], a pre-committed maximum drawdown (e.g., "retire if drawdown exceeds 1.5× the worst in-sample drawdown") is one of the cleanest, least-discretionary signals that a strategy's edge has decayed or was overfit. It converts an emotional decision into a mechanical one.
- **Underwater duration limits.** Some risk frameworks add a *time*-based rule alongside the depth rule: if the book has been below its high-water mark for longer than N months (e.g., 18-24), force a review even if the depth limit was never breached. Prolonged underwater periods are where most discretionary traders abandon a sound strategy at the worst time.

The core practical insight is that drawdown depth and recovery are asymmetric and compounding, so the cheapest place to manage drawdown is *before* it becomes deep — via sizing, diversification ([[crisis-alpha]], [[trend-plus-tail-hedge]]), and pre-committed rules — not by trying to "trade out" of a hole after the fact.

## Related

- [[tail-risk]] -- the probability of extreme events that cause deep drawdowns
- [[trend-plus-tail-hedge]] -- combination strategy designed to limit drawdowns across crisis speeds
- [[sharpe-ratio]] -- risk-adjusted return metric (uses volatility, not drawdown)
- [[value-at-risk]] -- probabilistic loss threshold, related but distinct from drawdown
- [[risk-management-overview]] -- broader context for drawdown within risk management
- [[crisis-alpha]] -- strategies that profit during the drawdown periods of traditional assets
- [[equity-curve]] -- visual representation of drawdowns over time
- [[calmar-ratio]] -- return-over-max-drawdown ratio
- [[risk-of-ruin]] -- the probability that drawdown reaches a terminal threshold
- [[position-sizing]] -- the primary lever for managing drawdown depth
- [[when-to-retire-a-strategy]] -- drawdown-based kill criteria

## Sources

- Magdon-Ismail, M., and Atiya, A. F. (2004). *Maximum Drawdown*. *Risk Magazine*, October 2004. Derives the expected maximum drawdown of a Brownian-motion equity curve and its relationship to Sharpe ratio and horizon.
- Chekhlov, A., Uryasev, S., and Zabarankin, M. (2005). *Drawdown Measure in Portfolio Optimization*. *International Journal of Theoretical and Applied Finance*, 8(1): 13-58. Introduces Conditional Drawdown-at-Risk (CDaR) as an optimisation objective.
- Young, T. W. (1991). *Calmar Ratio: A Smoother Tool*. *Futures Magazine*. Original definition of the return-over-max-drawdown ratio.
- Kahneman, D., and Tversky, A. (1979). *Prospect Theory: An Analysis of Decision under Risk*. *Econometrica*, 47(2): 263-291. Foundation for the loss-aversion / panic-selling behaviour discussed in the psychology section.
- Bailey, D. H., and López de Prado, M. (2014). *The Deflated Sharpe Ratio*. Background on why backtested drawdowns understate live drawdowns under overfitting.
