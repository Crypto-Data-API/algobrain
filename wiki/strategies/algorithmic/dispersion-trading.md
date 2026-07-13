---
title: "Dispersion Trading"
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [dispersion, volatility, options, correlation, index-options, institutional, quantitative, vega]
aliases: ["Correlation Trading", "Volatility Dispersion", "Index vs. Single-Stock Vol"]
strategy_type: quantitative
timeframe: swing
markets: [stocks]
complexity: advanced
backtest_status: untested
related: ["[[basis-trading]]", "[[options-strategies]]", "[[volatility]]", "[[factor-investing]]", "[[hedging]]"]
---

# Dispersion Trading

## Overview

Dispersion Trading is a sophisticated [[volatility]]-based strategy that profits from the difference between **index implied volatility** and the **implied volatilities of the index's constituent stocks**. The core trade is: **sell index options** (selling [[volatility]] at the index level) and **buy options on individual constituent stocks** (buying volatility at the single-stock level). The trade profits when the **realized correlation** among constituent stocks is lower than the **implied correlation** embedded in index option prices.

The structural edge exists because index options systematically overprice correlation. Portfolio managers, pension funds, and institutions are persistent buyers of index puts for hedging, which inflates index [[implied-volatility]]. This creates a "correlation risk premium" that dispersion traders harvest. The strategy is predominantly used by **institutional volatility desks** at banks (Goldman Sachs, JPMorgan, Barclays) and volatility-focused hedge funds (Capstone, Parallax). It requires deep understanding of [[options-greeks]], correlation dynamics, and portfolio-level risk management.

## Rules

### Entry
1. **Calculate implied correlation:** Derive the implied correlation from the relationship between index option implied vol and constituent option implied vols. IC = (Index IV^2 - Sum of Weighted Single Stock IVs^2) / (Sum of Weighted Cross-Products). Tools like Bloomberg's CORR function simplify this.
2. **Enter when implied correlation is elevated:** If implied correlation is above its 6-12 month average or above 0.65, the premium for selling index vol is rich. Historical realized correlation averages 0.30-0.50 for the S&P 500.
3. **Sell index straddles or strangles:** Sell short-dated (30-45 DTE) ATM straddles or 25-delta strangles on the index (SPX or SPY options).
4. **Buy constituent straddles or strangles:** Buy the same maturity straddles or strangles on the top 20-50 stocks in the index, weighted by their index weight. Focus on the largest-weighted stocks (AAPL, MSFT, AMZN, NVDA, etc.) as they drive most of the index variance.
5. **Vega-neutral construction:** The total [[vega]] of the long single-stock options should approximately equal the total vega of the short index options, so the trade is neutral to a parallel shift in the entire volatility surface.

### Exit
1. **Expiration:** Hold until options expiration. The trade resolves based on realized vs. implied correlation.
2. **Early exit at profit target:** If the trade achieves 60-70% of maximum profit before expiration, close to reduce gamma risk in the final week.
3. **Stop-loss:** If the trade loses more than 1.5x the expected premium (implied correlation continues rising or a market crash causes correlation to spike to 1.0), close all legs.
4. **Correlation spike:** Exit immediately if a systemic event causes all stocks to move in lockstep (e.g., March 2020 crash). When realized correlation approaches 1.0, the short index vol position loses and the long single-stock vol does not compensate enough.

### Position Sizing
Size so that a worst-case correlation spike (realized correlation = 0.90-1.0) produces a maximum loss of 2-3% of portfolio. This typically means the trade is a small allocation (5-10% of a volatility fund). Margin requirements for the short index options are substantial.

## Indicators Used
- Implied correlation (derived from index and single-stock option IVs)
- [[implied-volatility]] of SPX/SPY index options
- [[implied-volatility]] of individual constituent stock options
- Realized correlation (rolling 30-60 day, compared to implied)
- [[vega]], [[gamma]], and [[theta]] for portfolio Greek management
- VIX level and term structure (elevated VIX often coincides with high implied correlation)
- Historical correlation cone (percentile ranking of current implied correlation)

## Example Trade
**Market:** S&P 500 dispersion trade
1. Implied correlation on the S&P 500 is 0.72, well above the trailing 12-month realized correlation of 0.45. The VIX is at 22, and individual stock IVs average 30%.
2. **Sell 10 SPX 30-DTE ATM straddles** at a combined premium of $85,000. This is the short index vol leg.
3. **Buy ATM straddles on the top 30 S&P 500 stocks** (by index weight), sized so total long vega = total short vega. Total premium paid: $72,000.
4. Net premium collected: $13,000. Maximum profit occurs if realized correlation is near zero (stocks move independently while the index barely moves). Maximum loss occurs if correlation spikes to 1.0.
5. Over 30 days, the market drifts sideways. Individual stocks experience idiosyncratic moves (AAPL +5%, JPM -3%, NVDA +8%, JNJ -2%) but these movements largely cancel at the index level. Realized correlation: 0.38.
6. At expiration, the index straddle expires with minimal loss. Several single-stock straddles expire in-the-money.
7. **Result:** Net profit of $18,500 -- the long single-stock options captured enough idiosyncratic movement to offset the index premium sold, plus the correlation risk premium.

## Performance Characteristics
- **Win Rate:** 65-75%. The structural overpricing of index correlation creates a persistent edge, though tail events can cause severe losses.
- **Profit Factor:** 1.5-2.5. Wins are moderate and consistent; losses (during correlation spikes) can be large.
- **Best Market Conditions:** Low to moderate volatility environments with healthy stock-picking (idiosyncratic stock moves). Earnings season is ideal because individual stocks move significantly on their own results while the index remains relatively stable.
- **Worst Market Conditions:** Market crashes and systemic crises (2008, March 2020) when all stocks drop simultaneously. Correlation spikes to 0.90+ destroy dispersion positions.
- **Annual Returns:** 5-15% with moderate volatility. Sharpe ratio: 0.7-1.2 in normal environments.
- **Correlation to Market:** Slightly negative to zero. Performs well in calm, stock-picker markets. Suffers in panics.

## Advantages
- Harvests a well-documented structural risk premium (correlation risk premium) that has persisted for decades
- Market-neutral to directional moves: the trade profits from dispersion, not direction
- Diversified exposure across dozens of constituent names reduces single-stock event risk
- Complements other volatility strategies and provides decorrelated returns to traditional portfolios
- Academic research supports the persistence of correlation overpricing in index options

## Disadvantages
- **Extreme complexity:** Requires managing hundreds of option positions simultaneously across index and constituent stocks
- **Tail risk:** Correlation spikes during crises can cause large, sudden losses that overwhelm months of premium collected
- **Capital intensive:** Margin requirements for short index options are substantial, and long constituent options tie up premium
- **Execution costs:** Crossing bid-ask spreads on dozens of option positions erodes the edge significantly
- **Model risk:** Implied correlation calculations are sensitive to the model used, and small errors can lead to mispriced trades
- **Inaccessible to retail:** Requires institutional-grade options infrastructure, margin, and risk management systems
- [[gamma]] risk intensifies near expiration, especially on the short index options leg

## See Also
- [[volatility]] -- understanding vol dynamics is the foundation of dispersion trading
- [[options-strategies]] -- broader framework for options-based strategies
- [[basis-trading]] -- another relative-value convergence strategy
- [[factor-investing]] -- dispersion returns have some overlap with the low-volatility factor
- [[hedging]] -- the long single-stock options act as a hedge for the short index options
