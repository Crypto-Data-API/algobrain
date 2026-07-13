---
title: Momentum Rotation Strategy
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags:
  - momentum
  - factor-investing
  - quantitative
  - cross-sectional
  - portfolio-rotation
  - jegadeesh-titman
strategy_type: momentum
timeframe: position
markets:
  - stocks
  - crypto
complexity: advanced
backtest_status: untested
related:
  - "[[rate-of-change]]"
  - "[[factor-investing]]"
  - "[[mean-reversion]]"
  - "[[risk-parity]]"
---

# Momentum Rotation Strategy

## Overview

Momentum rotation is a [[quantitative-strategies|quantitative]] approach that systematically ranks a universe of assets by their recent performance over lookback periods (typically 3, 6, or 12 months) and rotates capital into the top performers while shorting or avoiding the worst performers. The strategy is grounded in the seminal research of **Jegadeesh & Titman (1993)**, who demonstrated that stocks with strong recent returns tend to continue outperforming over the next 3-12 months. This cross-sectional [[momentum]] effect is one of the most robust anomalies in financial markets and forms a core pillar of [[factor-investing]]. The strategy can be implemented as long-only (buy top decile) or long-short (buy top, sell bottom).

## Rules

### Entry Rules
1. **Universe Selection:** Define a liquid universe of assets (e.g., S&P 500 stocks, top 100 [[crypto]] by market cap).
2. **Ranking:** At each rebalance date, compute the total return for each asset over the lookback window (commonly 12 months minus the most recent 1 month, to avoid [[short-term-reversal]] effects).
3. **Portfolio Construction:** Buy the top decile (top 10%) of ranked assets equally weighted or risk-weighted. For a long-short version, simultaneously short the bottom decile.
4. **Rebalance Frequency:** Monthly rebalancing is standard. Some implementations use weekly or quarterly.
5. **Skip Month:** Exclude the most recent month's return from the lookback to avoid the well-documented 1-month reversal effect.

### Exit Rules
1. **Rotation Exit:** Assets are sold when they fall out of the top decile at the next rebalance date.
2. **Crash Filter:** If the broad market index drops below its 200-day [[moving-average]], move to cash or reduce position sizes by 50%. This protects against [[momentum-crashes]].
3. **Volatility Scaling:** Scale position sizes inversely to each asset's recent [[volatility]] to normalize risk contribution.
4. **Drawdown Limit:** If the portfolio drawdown exceeds a predefined threshold (e.g., 20%), reduce exposure systematically.

## Indicators Used

| Indicator | Settings | Purpose |
|-----------|----------|---------|
| [[rate-of-change]] | 12-month (skip last 1 month) | Asset ranking signal |
| [[moving-average]] (200-day) | 200-period | Market regime / crash filter |
| [[volatility]] (realized) | 60-day window | Position sizing / risk normalization |
| [[correlation-matrix]] | Rolling 60-day | Diversification monitoring |

## Example Trade

**Setup:** Monthly rebalance on a universe of 100 large-cap stocks. Compute 12-1 month returns (12 months total return, skip most recent month). Rank all 100 stocks.

**Entry:** Top 10 stocks by momentum score are: NVDA (+95%), AVGO (+72%), META (+68%), LLY (+61%), AMZN (+58%), GE (+55%), PLTR (+52%), NOW (+49%), ORCL (+47%), COST (+44%). Allocate 10% capital to each.

**Management:** Monitor weekly. Apply inverse-volatility weighting so that higher-volatility names get smaller allocations. NVDA (vol 38%) gets ~6% weight; COST (vol 18%) gets ~14% weight.

**Exit:** At next monthly rebalance, ORCL and GE have fallen out of the top decile. They are replaced by two new entrants. Portfolio turnover is approximately 20-30% per month.

## Performance Characteristics

- **Historical CAGR:** 12-18% for long-only U.S. equities (before transaction costs), per academic literature
- **Sharpe Ratio:** 0.5-0.8 for long-only; 0.7-1.1 for long-short (historically)
- **Best Conditions:** Trending markets with clear sector leadership and dispersion
- **Worst Conditions:** Sharp market reversals ([[momentum-crashes]]) such as March 2009 or the quant quake of August 2007
- **Key Risk:** Momentum strategies are prone to severe, sudden drawdowns during market regime changes

## Advantages

- One of the most well-documented and academically supported [[factor-investing]] strategies
- Systematic and rules-based, removing emotional decision-making
- Works across asset classes: [[stocks]], [[crypto]], commodities, currencies
- Can be combined with other factors ([[value]], [[quality]], [[low-volatility]]) for improved risk-adjusted returns
- Scalable to large portfolios with proper execution

## Disadvantages

- Susceptible to **momentum crashes** -- violent reversals where past losers surge and past winners collapse
- High turnover leads to significant [[transaction-costs]] and tax drag
- Requires a large, liquid universe to be effective; concentration risk with small universes
- The 1-month reversal skip is critical; without it, performance degrades substantially
- Crowding risk: as more funds adopt momentum, the strategy's edge may diminish
- Implementation requires robust infrastructure for ranking, rebalancing, and execution
