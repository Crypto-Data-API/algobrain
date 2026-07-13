---
title: "Beta"
type: concept
created: 2026-04-13
updated: 2026-06-11
status: good
tags: [portfolio-theory, risk-management, indicators, correlation]
aliases: ["Beta", "Beta Coefficient", "market beta", "β"]
domain: [portfolio-theory, risk-management]
prerequisites: ["[[volatility]]", "[[correlation]]"]
difficulty: intermediate
related: ["[[capm]]", "[[alpha]]", "[[sharpe-ratio]]", "[[volatility]]", "[[correlation]]", "[[diversification]]", "[[beta-weighted-delta]]"]
---

**Beta** (β) measures the sensitivity of an asset's returns to the returns of a benchmark, usually a broad market index such as the S&P 500. A beta of 1.0 means the asset tends to move in line with the market; above 1.0 means it amplifies market moves (more systematic risk); below 1.0 means it dampens them (more defensive). Beta is the central risk measure of the [[capm|Capital Asset Pricing Model]] and the primary tool for separating a portfolio's market-driven returns (beta) from its skill-driven returns ([[alpha]]).

## How It Is Calculated

Beta is the slope of the regression of asset returns on market returns. Equivalently, it is the asset–market covariance scaled by the market variance:

```
beta = Cov(R_asset, R_market) / Var(R_market)
     = corr(R_asset, R_market) × (sigma_asset / sigma_market)
```

The second form makes the two drivers explicit: an asset's beta is its [[correlation]] with the market multiplied by the ratio of its [[volatility]] to the market's. A highly volatile stock that is uncorrelated with the market can still have a low beta; a moderately volatile stock that is tightly correlated can have a high one.

Practical notes:
- Beta is **estimation-window dependent** — a 5-year monthly beta and a 1-year daily beta for the same stock often differ materially. Providers (Bloomberg, Yahoo) typically publish a 5-year monthly or 2-year weekly figure.
- **Raw vs. adjusted beta**: Bloomberg-style "adjusted beta" shrinks the raw estimate toward 1.0 (`adj = 0.67 × raw + 0.33 × 1.0`), reflecting the empirical tendency of betas to mean-revert toward the market over time.
- Beta is **non-stationary** — it shifts with leverage, business mix, and regime. It typically rises in crises as correlations spike toward 1 (the "correlation goes to one in a crash" effect).

## Decomposing Risk and Return

In the [[capm]], an asset's expected return is driven entirely by its beta:

```
E[R_asset] = R_f + beta × (E[R_market] − R_f)
```

Total portfolio risk splits into:
- **Systematic (market) risk** — the `beta × R_market` component, undiversifiable; this is what beta captures.
- **Idiosyncratic risk** — the residual, diversifiable away by holding many positions.

[[diversification]] removes idiosyncratic risk but not beta. A portfolio of 200 high-beta stocks is still a high-beta portfolio.

## Trading Relevance

Beta is load-bearing in several practical contexts:

- **Portfolio construction** — targeting a desired market exposure. A manager who wants 0.8× market exposure builds a portfolio with weighted-average beta of 0.8. Defensive, low-beta names (utilities, infrastructure such as transurban, consumer staples) are held to lower portfolio beta; cyclicals and high-growth tech raise it.
- **Hedging** — beta tells you how many index futures or how much [[beta-weighted-delta|beta-weighted option delta]] to short to neutralize market exposure. A $1M long book with beta 1.2 requires shorting ~$1.2M of index exposure to be market-neutral.
- **Performance attribution** — separating beta (cheap, replicable with an index fund) from [[alpha]] (genuine skill). A fund returning 12% in a year the market returned 10% with beta 1.2 actually *underperformed* its beta-implied 12% — its alpha was zero. This is the core of "are you paying for beta dressed up as alpha?"
- **Smart-beta and factor investing** — "low-beta" is itself a documented anomaly: low-beta stocks have historically delivered higher risk-adjusted returns than CAPM predicts (the *betting-against-beta* effect, Frazzini and Pedersen 2014), because leverage-constrained investors overpay for high-beta exposure.

## Limitations

- **Backward-looking** — beta is estimated from history and may not hold forward, especially through regime changes.
- **Benchmark-dependent** — a stock's beta to the S&P 500 differs from its beta to a sector index or to a global index; "the" beta does not exist without specifying the benchmark.
- **Linear and single-factor** — beta assumes a linear relationship to one factor. Multi-factor models (Fama-French) and downside-beta measures address cases where a single market beta is too coarse.
- **Unstable in tails** — the diversification beta promises breaks down precisely when it matters most, as cross-asset correlations converge in crises.

## Related

- [[capm]] — the model in which beta is the sole priced risk factor
- [[alpha]] — return *not* explained by beta
- [[sharpe-ratio]] — risk-adjusted return using total volatility rather than beta
- [[volatility]] — total risk; beta scales the market-correlated portion of it
- [[correlation]] — one of the two components of beta
- [[diversification]] — removes idiosyncratic risk but leaves beta intact
- [[beta-weighted-delta]] — applying beta to translate option deltas into index-equivalent exposure

## Sources

- Sharpe, William F. "Capital Asset Prices: A Theory of Market Equilibrium under Conditions of Risk," *Journal of Finance* (1964) — the origin of beta as the priced risk measure
- Bodie, Kane, and Marcus. *Investments* — standard textbook derivation of beta, the security market line, and risk decomposition
- Frazzini, A. and Pedersen, L. H. "Betting Against Beta," *Journal of Financial Economics* (2014) — documents the low-beta anomaly
- Blume, Marshall E. "Betas and Their Regression Tendencies," *Journal of Finance* (1975) — basis for adjusted-beta shrinkage toward 1.0
