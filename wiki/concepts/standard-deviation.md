---
title: "Standard Deviation"
type: concept
created: 2026-04-15
updated: 2026-06-22
status: excellent
tags: [risk-management, quantitative, volatility]
aliases: ["Standard Deviation", "Std Dev", "SD", "Sigma"]
domain: [risk-management, portfolio-theory]
prerequisites: ["[[normal-distribution]]"]
difficulty: beginner
related: ["[[volatility]]", "[[bollinger-bands]]", "[[sharpe-ratio]]", "[[value-at-risk]]", "[[normal-distribution]]", "[[variance]]", "[[kurtosis]]"]
---

Standard deviation is a statistical measure of the dispersion of data points around a mean — the square root of the [[variance]]. In finance it is the most common proxy for [[volatility]]: the standard deviation of an asset's returns quantifies how much those returns vary from their average. A higher standard deviation indicates greater uncertainty and risk; a lower standard deviation indicates more stable, predictable returns.

## Definition and Formula

For a series of observations $x_1, \dots, x_n$ with mean $\bar{x}$, the population standard deviation is:

$$\sigma = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(x_i - \bar{x})^2}$$

The **sample** standard deviation uses $n-1$ in the denominator (Bessel's correction) to give an unbiased estimate of the population variance from a sample:

$$s = \sqrt{\frac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar{x})^2}$$

In trading, $x_i$ is typically a periodic return (daily, weekly, monthly), so $\sigma$ has units of "return per period." It is the square root of [[variance]], which makes it directly comparable to the returns themselves (variance is in squared units and harder to interpret).

The choice between $n$ and $n-1$ matters most for small samples. With 20 daily returns, dividing by 19 instead of 20 raises the estimate by ~2.6%; with 252 returns the difference is negligible. Most spreadsheet and library functions default to the **sample** form (`STDEV`/`STDEV.S` in Excel, `numpy.std(ddof=1)` is *not* the default — NumPy uses `ddof=0` and gives the population form unless told otherwise), a common silent source of small discrepancies between platforms.

### Worked Example

Five daily returns: +1.0%, −0.5%, +2.0%, −1.5%, +0.5%.

1. Mean: $\bar{x} = (1.0 - 0.5 + 2.0 - 1.5 + 0.5)/5 = 1.5/5 = 0.30\%$
2. Squared deviations (in %²): $(0.7)^2=0.49,\ (-0.8)^2=0.64,\ (1.7)^2=2.89,\ (-1.8)^2=3.24,\ (0.2)^2=0.04$
3. Sum = 7.30; sample [[variance]] $s^2 = 7.30 / (5-1) = 1.825\,\%^2$
4. Sample standard deviation $s = \sqrt{1.825} \approx 1.35\%$ per day
5. Annualized: $1.35\% \times \sqrt{252} \approx 21.4\%$

So this (tiny, illustrative) sample implies ~21% annualized [[volatility]] — in the typical range for a single equity. Five points is far too few for a reliable estimate; practitioners use 20–252 observations.

## Interpreting Standard Deviation

Under a [[normal-distribution|normal distribution]] assumption, approximately 68% of observations fall within 1 standard deviation of the mean, 95% within 2 standard deviations, and 99.7% within 3 (the "68-95-99.7 rule"). In practice, financial returns exhibit fat tails ([[kurtosis]]) and negative skew, meaning extreme moves (3+ sigma events) occur far more often than a normal model predicts. The 2008 financial crisis and the March 2020 COVID crash both produced daily moves that were 5-10+ standard-deviation events under a normal model — a reminder that standard deviation systematically *understates* tail risk. This is the core critique behind the use of [[value-at-risk]] add-ons and fat-tailed models.

The table below contrasts how often a given sigma move "should" occur under a Gaussian versus how often markets actually deliver them — the gap is the practical meaning of [[fat-tails|fat tails]]:

| Move | Normal-model probability (one tail) | Expected frequency (252 trading days/yr) | Empirical reality |
|------|-------------------------------------|------------------------------------------|-------------------|
| ±1σ  | 15.9%                               | ~40 days/year each side                  | Roughly matches   |
| ±2σ  | 2.3%                                | ~6 days/year                             | Roughly matches   |
| ±3σ  | 0.13%                               | once every ~1.5 years                    | Several times/year |
| ±4σ  | 0.003%                              | once every ~125 years                    | Multiple times/decade |
| ±5σ  | 0.00003%                            | once every ~14,000 years                 | Multiple times/decade |

A "10-sigma event" under a normal model is so improbable it should not occur in the lifetime of the universe — yet equity indices have printed such days repeatedly. The lesson is not that the math is wrong but that the *model* (Gaussian returns) is wrong in the tails. See [[fat-tails]], [[kurtosis]], and [[black-swan]].

## Z-Scores and Standardization

A **z-score** restates any observation as the number of standard deviations it sits from the mean:

$$z = \frac{x - \bar{x}}{\sigma}$$

This standardization is the workhorse of [[mean-reversion]] and [[statistical-arbitrage]] entries. If a [[pairs-trading|pairs]] spread has a 60-day mean of 0 and a standard deviation of $1.20, a current spread of +$2.40 is a z-score of +2.0 — two sigma rich — a common short-the-spread trigger; traders typically exit near z = 0 (mean) and stop out beyond z = ±3. Bollinger %b and the RSI's statistical cousins are all z-score relatives. Worked: with mean 0.30% and σ 1.35% from the example above, a +3.0% return is $z = (3.0 - 0.30)/1.35 \approx +2.0$ — a two-sigma up-day.

## Annualization

Daily standard deviation is annualized by multiplying by the square root of the number of trading periods: **annualized SD = daily SD × √252** (or √52 for weekly, √12 for monthly). This "square-root-of-time" scaling assumes returns are independent and identically distributed (i.i.d.), which is only approximately true — [[volatility-clustering|volatility clustering]] (today's large move predicts tomorrow's large move) and autocorrelation violate the assumption. Despite this limitation, annualized standard deviation remains the industry-standard expression of [[volatility]] (e.g., "the S&P 500 has realized ~16% annualized vol historically").

| Sampling frequency | Periods per year | Annualization factor |
|--------------------|------------------|----------------------|
| Daily (trading)    | 252              | √252 ≈ 15.87         |
| Daily (calendar)   | 365              | √365 ≈ 19.10         |
| Weekly             | 52               | √52 ≈ 7.21           |
| Monthly            | 12               | √12 ≈ 3.46           |
| Hourly (24/7 crypto) | 8,760          | √8760 ≈ 93.6         |

A useful desk shortcut: divide annualized vol by ~16 (≈√252) to get the implied *daily* move. A 16% annualized [[volatility]] equals roughly a 1% one-standard-deviation daily move; a 32% name moves ~2% per day. This is how options traders translate an [[implied-volatility]] number into an expected daily range in their head.

Note the **square-root, not linear, scaling**: doubling the horizon multiplies vol by only √2 ≈ 1.41, not 2. This is why long-dated risk grows more slowly than naive intuition suggests — provided the i.i.d. assumption holds. When returns are positively autocorrelated (trending), realized vol scales *faster* than √t; when mean-reverting, *slower*.

## Applications in Trading

Standard deviation underpins many widely used tools and metrics:

- **[[bollinger-bands|Bollinger Bands]]** plot bands at ±2 standard deviations from a moving average to flag stretched conditions.
- **[[sharpe-ratio|Sharpe ratio]]** divides excess return by standard deviation to measure risk-adjusted performance.
- **[[value-at-risk|Value at Risk (VaR)]]** uses standard deviation (often adjusted for fat tails) to estimate potential portfolio losses at a given confidence level.
- **[[implied-volatility|Implied volatility]]** in options pricing is itself an annualized standard deviation of expected returns — a 20% IV means the market prices a ~20% one-sigma annual move.
- **Position sizing** frameworks scale exposure inversely to recent realized standard deviation (volatility targeting), so risk per position stays roughly constant across regimes.
- **Z-scores** in [[statistical-arbitrage]] and [[mean-reversion]] express how many standard deviations a spread sits from its mean, defining entry and exit thresholds.

## Pitfalls and Limitations

- **Symmetric treatment of risk.** Standard deviation treats upside and downside dispersion identically, though traders care mostly about downside — hence [[downside-deviation]] and the Sortino ratio as alternatives that penalize only adverse moves.
- **Assumes a stable distribution.** Regime shifts make trailing-window estimates lag: a 60-day window still reflects calm conditions days into a crisis, then over-reflects the crisis for weeks after it ends. [[ewma|EWMA]] and [[garch|GARCH]] weighting partly address this by emphasizing recent observations.
- **Understates tail risk under fat tails and skew** — the recurring lesson of every crisis. A portfolio sized to a "2σ daily loss" VaR is routinely surprised by 4–8σ days.
- **Window-length sensitivity.** A 10-day vol and a 252-day vol of the same asset can differ by a factor of 3 across regimes; quoting "the volatility" without the window is meaningless. See [[volatility-cone]] for the horizon-aware view.
- **Garbage-in from data errors.** A single bad print (split not adjusted, stale quote) creates an enormous spurious return that dominates the squared-deviation sum. Always clean and split/dividend-adjust price series first.
- **Overlapping-return autocorrelation.** Annualizing high-frequency vol via √t breaks under [[volatility-clustering]]; the i.i.d. assumption is the weakest link in the standard pipeline.

## How Traders Use Standard Deviation

- **Volatility targeting / risk parity** — scale each position so its dollar standard deviation contribution is equal, keeping portfolio risk constant across regimes.
- **Setting stops and targets** — express stop distance in multiples of [[average-true-range|ATR]] or daily σ rather than fixed percentages, so stops adapt to the instrument's current volatility.
- **Relative-value entries** — z-score a spread, ratio, or indicator and trade extremes back toward the mean.
- **Performance attribution** — the σ denominator of the [[sharpe-ratio]] is what separates skill from leverage; doubling leverage doubles both return and σ, leaving Sharpe unchanged.
- **Option-implied moves** — convert an [[implied-volatility]] quote into an expected one-σ range for an earnings event or expiry using the √t scaling above.

## Related

- [[volatility]] — the broader concept that standard deviation measures
- [[variance]] — standard deviation is its square root
- [[bollinger-bands]] — technical indicator built on standard deviation
- [[sharpe-ratio]] — risk-adjusted return metric using SD as the denominator
- [[value-at-risk]] — risk measure derived from standard deviation
- [[normal-distribution]] — the theoretical distribution assumed in many SD-based calculations
- [[kurtosis]] — fat tails that make SD understate extreme risk
- [[fat-tails]] — why extreme moves dwarf Gaussian predictions
- [[realized-volatility]] — standard deviation of returns applied as a volatility estimate
- [[implied-volatility]] — the forward-looking option-market analogue
- [[downside-deviation]] — the one-sided alternative used by the Sortino ratio
- [[garch]] / [[ewma]] — time-varying volatility models that relax the constant-σ assumption

## Sources

- Hull, J. C. *Options, Futures, and Other Derivatives* — volatility estimation, square-root-of-time scaling, and the i.i.d. assumption.
- Bodie, Kane & Marcus, *Investments* — standard deviation as the canonical risk measure in portfolio theory and the Sharpe ratio.
- Taleb, N. N. *The Black Swan* / *Fooled by Randomness* — the failure of standard deviation under fat-tailed return distributions.
