---
title: "Skew"
type: concept
created: 2026-05-07
updated: 2026-06-11
status: good
tags: [options, volatility, statistics, portfolio-theory, indicators, disambiguation]
aliases: ["Skew", "Skewness", "Statistical Skew", "Third Moment"]
related: ["[[volatility-skew]]", "[[negative-skew]]", "[[volatility-smile]]", "[[implied-volatility]]", "[[options-pricing]]", "[[fat-tails]]", "[[long-vol-vs-short-vol]]", "[[variance-risk-premium]]", "[[sharpe-ratio-pitfalls]]", "[[deflated-sharpe-ratio]]", "[[cboe-skew-index]]", "[[options-risk-budgeting]]", "[[volatility-regime]]"]
domain: [options, statistics, portfolio-theory]
difficulty: intermediate
---

In trading, **skew** refers to two distinct but historically related concepts that share a name and are frequently conflated. *Volatility skew* (also "options skew", "vol skew", "put skew") is a property of the [[implied-volatility|implied volatility]] surface — specifically the asymmetric variation of IV across strikes for options of the same expiration. *Statistical skew* (also "skewness", "negative skew", "left-skew") is the third standardized moment of a return distribution — a property of *realised* historical returns, not of options prices. Both notions describe asymmetry, and both are central to understanding tail risk, but they are computed from different inputs and apply at different layers of the trading stack.

## Overview

The two senses share an etymology: both describe distributions with one tail materially fatter or longer than the other. Where they differ is in the underlying object.

| | Volatility Skew | Statistical Skew |
|---|---|---|
| Object | The implied-volatility surface | A realised return distribution |
| Asymmetry of | Option *prices* across strikes | *Returns* around their mean |
| Time orientation | Forward-looking (priced today) | Backward-looking (computed from history) |
| Primary use | Options structuring; volatility trading | Strategy evaluation; risk reporting |
| Canonical formula | IV(K_low) − IV(K_high), or 25Δ-put IV − 25Δ-call IV | E[(R − μ)^3] / σ^3 |
| Equity sign | Negative slope (puts > calls); sometimes called "put skew" | Typically negative for equities (left tail) |
| Dedicated wiki page | [[volatility-skew]] | [[negative-skew]] |

The naming overlap is not coincidental. The reason equity-index volatility skew is *negatively sloped* (OTM puts more expensive than OTM calls) is precisely that the realised return distribution of equities is *negatively skewed* (large drops more likely than large rallies). Options markets price what realised distributions deliver; the two skews co-vary even though they are formally distinct quantities. See [[volatility-skew]] for why this connection holds in equity markets.

## Volatility Skew (options pricing)

**Volatility skew** describes how [[implied-volatility|implied volatility]] varies across strikes for options of a single expiration. In equity-index options, OTM puts trade at materially higher IV than OTM calls — typically 4–10 vol points apart at the 25-delta level for SPX in calm regimes, and substantially wider in stress.

Standard measurements:

- **25-delta skew**: IV(25Δ-put) − IV(25Δ-call), same expiration.
- **90/100 skew**: IV(90% strike put) − IV(100% strike ATM).
- **CBOE [[cboe-skew-index|SKEW Index]]**: a single-number summary of S&P 500 OTM put skew, scaled so that 100 = symmetric.

The phenomenon is partly post-1987-crash institutional pricing of crash risk, partly the leverage effect, and partly persistent supply/demand imbalance from institutional [[protective-puts|protective put]] buyers. See [[volatility-skew]] for the full discussion of mechanism, term structure of skew, and skew-trading strategies.

In an options book context, "watching skew" means tracking the IV(put) − IV(call) gap as a regime indicator: skew steepening often precedes broader vol expansion. See [[options-risk-budgeting]] §"Net Vega Budget" for how the skew dimension feeds into the vega budget.

→ **Canonical reference: [[volatility-skew]]**

## Statistical Skew (return distributions)

**Statistical skew** (or *skewness*, often `g_1` or `G_1`) is the standardized third central moment of a probability distribution:

```
skew(R) = E[(R − μ)^3] / σ^3
```

The sample estimator on `T` observations:

```
g_1 = (1/T) Σ_t ((r_t − r_mean) / s)^3
```

Sign convention universal in finance:

- **Positive skew** — long *right* tail. Many small losses, occasional large wins. Long volatility, [[long-vol-vs-short-vol|long-vol]] strategies, lottery tickets, OTM call buyers.
- **Zero skew** — symmetric. Gaussian.
- **Negative skew** — long *left* tail. Many small wins, occasional catastrophic losses. Short vol, credit selling, carry trades, OTM put writers.

Negative skew is the structural shape of any strategy that *collects a small premium for taking a tail risk*. The [[variance-risk-premium]] is its canonical example: short-vol strategies earn steady carry and give back multiple years in a single shock. The Sharpe ratio is famously *misleading* under negative skew because it uses only the first two moments — see [[sharpe-ratio-pitfalls]] and the [[deflated-sharpe-ratio]] for the formal corrections.

For monthly equity returns, sample skewness is typically around -0.5 to -1.0. For short-vol strategies measured at daily frequency, skewness can reach -3 to -10 in calm windows (the rare large losses haven't happened yet). Sample skewness systematically *underestimates* true skewness for tail-driven distributions because the worst event hasn't necessarily occurred in any finite sample.

→ **Canonical reference: [[negative-skew]]**

## When the Two Meet

The two skews are independent quantities but they are *empirically correlated* in ways that matter for trading.

### 1. Equity vol skew is steep because equity returns are negatively skewed

Options dealers price the IV surface such that OTM puts trade richer than OTM calls. The reason is that the realised distribution of equity returns has a long left tail; if dealers sold OTM puts at the same IV as OTM calls, they would lose money over time as the realised left tail materialised more often than the right. Vol skew is the *pricing response* to statistical skew. The two co-vary regime-by-regime: in stressed regimes both vol skew and realised statistical skew are deeper than in calm regimes.

### 2. Selling vol skew is selling negative-skew payoff

A trade that sells the expensive OTM put and buys the cheaper OTM call (a [[risk-reversal|risk reversal]]) is *long the underlying* in delta terms and *short the vol skew* in vega terms. Its return distribution inherits both the underlying's negative skew *and* the additional negative skew from being short the put. The Sharpe ratio of risk-reversal carry strategies looks attractive in calm regimes; under [[deflated-sharpe-ratio|skew-adjusted Sharpe]] it is much less attractive.

### 3. SKEW Index measures vol skew but reflects expected statistical skew

The CBOE [[cboe-skew-index|SKEW Index]] is computed from S&P 500 OTM option prices but is *interpreted* as a market-implied probability distribution of returns. A SKEW reading of 130 implies a market-implied negative-skewness in 30-day forward returns; readings above 140 indicate the market is pricing in a substantially fatter left tail. The single index thereby links the vol-skew object (option prices) to the statistical-skew object (return distribution).

### 4. Long-vol strategies are positive-statistical-skew via long-vol-skew exposure

Buying OTM puts (paying the high vol-skew premium) is a *negative-carry* trade in calm regimes. It produces a positive-statistical-skew return distribution: many small premium losses, occasional large gain when the underlying drops. The two skews flip sign in convenient symmetry: paying the *negatively-shaped vol skew* gives you a *positively-shaped statistical skew* return profile. This is the structural argument for the persistent small allocation to long convexity in [[options-risk-budgeting|options-risk-budgeted]] portfolios.

### 5. Regime change links them

In a [[volatility-regime|stressed vol regime]], both vol skew steepens and realised statistical skew turns more negative. The two regime-by-regime track each other; backtests run in calm regimes underestimate both.

## Quick Disambiguation Guide

When someone says "skew" without qualification, infer from context:

| Context cue | Likely meaning | Wiki page |
|---|---|---|
| "selling skew", "skew steepening", "skew flattening", "long skew", "short skew" | Volatility skew | [[volatility-skew]] |
| "skew is rich", "skew is cheap", "the skew is at X vol points" | Volatility skew | [[volatility-skew]] |
| "this strategy has skew of -3", "skewness of returns", "skew-adjusted Sharpe" | Statistical skew | [[negative-skew]] |
| "negative skew", "skew penalty", "skew-driven drawdown" | Statistical skew | [[negative-skew]] |
| "SKEW Index", "CBOE SKEW", "SKEW 135" | Volatility skew | [[volatility-skew]] / [[cboe-skew-index]] |
| "fat left tail", "the skew of this distribution", "third moment" | Statistical skew | [[negative-skew]] |

A useful rule: if the speaker is talking about *option prices*, *vol points*, *strikes*, or *the skew curve*, they mean volatility skew. If they are talking about *returns*, *backtest distributions*, *risk metrics*, or *moments*, they mean statistical skew. If both are involved, name them explicitly.

## Common Confusions

1. **"This strategy has good skew."** Ambiguous. *Good* statistical skew is positive (long right tail). *Selling the skew* in options means receiving premium for a negative-statistical-skew payoff. The two senses can have *opposite* practical meanings.
2. **"Skew is at 125."** Almost always refers to the [[cboe-skew-index|CBOE SKEW Index]] (volatility-skew family), not statistical skewness which is unitless and small.
3. **"Risk reversals trade skew."** Means trading the *vol-skew curve* (selling rich-IV puts vs cheaper-IV calls), but the resulting return profile inherits *negative statistical skew*.
4. **"Skew-adjusted Sharpe."** Refers to the [[deflated-sharpe-ratio]] or similar — adjusting for *statistical* skewness, not vol skew.
5. **"The smile is symmetric, no skew."** In options-pricing context, refers to vol skew (the asymmetric form of the smile). The underlying return distribution can still be statistically skewed even when its options surface is symmetric (as is roughly the case in FX).

## Related

- [[volatility-skew]] — the canonical options-pricing skew page
- [[negative-skew]] — the canonical statistical-skew page
- [[volatility-smile]] — the symmetric form of which vol skew is the asymmetric variant
- [[implied-volatility]] — the metric whose variation across strikes defines vol skew
- [[options-pricing]] — where vol skew lives in the modelling stack
- [[cboe-skew-index]] — the option-priced summary of vol skew
- [[fat-tails]] — kurtosis cousin; usually appears alongside both skews
- [[long-vol-vs-short-vol]] — the posture spectrum that the two skews jointly characterise
- [[variance-risk-premium]] — the structural source of negative statistical skew in short-vol books
- [[sharpe-ratio-pitfalls]] / [[deflated-sharpe-ratio]] — corrections for statistical skew in performance metrics
- [[options-risk-budgeting]] — where both skews enter the risk budget
- [[volatility-regime]] — the regime structure both skews share

## Sources

- Hull, J. *Options, Futures, and Other Derivatives* — standard textbook treatment of volatility skew and the smile.
- Natenberg, S. *Option Volatility and Pricing* — practitioner reference for vol-skew trading.
- CBOE — [[cboe-skew-index|SKEW Index]] methodology white paper.
- Bailey, D. and López de Prado, M. (2014). *The Deflated Sharpe Ratio: Correcting for Selection Bias, Backtest Overfitting, and Non-Normality*. Journal of Portfolio Management. Formal correction for statistical skew in Sharpe ratios.
- Carr, P. and Wu, L. (2009). *Variance Risk Premiums*. Review of Financial Studies. Connects the option-priced VRP to realised return skewness.
- Mandelbrot, B. *The (Mis)Behavior of Markets* (2004). Foundational treatment of statistical skew and fat tails in financial returns.
