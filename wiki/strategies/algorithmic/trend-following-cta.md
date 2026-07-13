---
title: "Trend Following CTA"
type: strategy
created: 2026-04-06
updated: 2026-04-14
status: good
tags: [trend-following, CTA, managed-futures, systematic, time-series-momentum, breakout, commodities]
aliases: ["Managed Futures", "CTA", "CTA Strategy", "CTA Strategies", "Commodity Trading Advisor", "Systematic Trend Following", "Time-Series Momentum"]
strategy_type: quantitative
timeframe: position
markets: [futures, commodities, forex]
complexity: advanced
backtest_status: untested
related: ["[[factor-investing]]", "[[moving-average-crossover]]", "[[turtle-trading]]", "[[momentum]]", "[[breakout-trading]]", "[[commodity-momentum]]", "[[commodity-carry-strategy]]", "[[cot-report-analysis]]", "[[commodities]]", "[[crisis-alpha]]", "[[convexity]]", "[[dragon-portfolio]]", "[[trend-plus-tail-hedge]]"]
---

# Trend Following CTA

## Overview

Trend Following CTA (Commodity Trading Advisor) is a systematic strategy that trades the direction of persistent price trends across a broad universe of **50-100+ futures markets** spanning commodities, currencies, government bonds, and equity indices. The strategy uses quantitative signals -- typically [[moving-average]] crossovers, channel breakouts, or time-series momentum -- to identify and ride trends until they reverse. It is the dominant strategy in the **managed futures** industry, employed by firms like **Man AHL**, **Winton Group**, **AQR**, **Graham Capital**, and **Millburn Ridgefield**.

The core principle is **time-series momentum**: assets that have been rising tend to continue rising, and assets that have been falling tend to continue falling, over horizons of 1-12 months. This persistence has been documented in academic literature across all major asset classes and over 100+ years of data. The CTA approach distinguishes itself from equity-only [[momentum]] by trading **both long and short** across **dozens of uncorrelated markets**, providing genuine diversification and the ability to profit in any market environment, including equity bear markets.

## Rules

### Entry
1. **Universe:** Trade 50-100 liquid futures contracts: agricultural [[commodities]] ([[corn]], [[wheat]], [[soybeans]]), metals ([[gold]], [[silver]], [[copper]]), energy ([[crude-oil|crude oil]], [[natural-gas|natural gas]]), currencies (EUR, JPY, GBP, AUD), bonds (U.S. Treasuries, German Bunds, JGBs), and equity indices (S&P 500, Euro Stoxx 50, Nikkei).
2. **Signal generation** (choose one or blend):
   - **Moving Average Crossover:** Go long when a short MA (e.g., 50-day) is above a long MA (e.g., 200-day). Go short when below. See [[moving-average-crossover]].
   - **Channel Breakout:** Go long when price breaks above the highest high of the past N days (e.g., 100 days). Short when price breaks below the lowest low. See [[turtle-trading]].
   - **Time-Series Momentum:** Go long if the 12-month return is positive. Go short if negative. Simplest and most robust signal.
3. **Confirmation:** Use multiple lookback windows (short: 20-day, medium: 60-day, long: 200-day) and blend their signals to smooth out entries and reduce whipsaws.
4. **Enter when the signal flips** from neutral/opposite to the new trend direction. Use limit orders at next session's open.

### Exit
1. **Signal reversal:** Exit when the trend signal flips to the opposite direction. For MA crossover, this means the short MA crosses back through the long MA.
2. **Trailing stop:** Use a 2-3x [[atr]] trailing stop to lock in profits during extended trends and exit before a full signal reversal.
3. **Volatility-based exit:** If realized volatility doubles (e.g., market enters crisis mode), reduce position size or exit to avoid outsized losses.

### Position Sizing
This is critical and often the most important component of a CTA system:
1. **Volatility targeting:** Size each position so that it contributes equal risk. Position size = Target Risk / (ATR x Point Value). If targeting 1% risk per position, a more volatile market gets fewer contracts.
2. **Portfolio volatility target:** Scale the total portfolio to target 10-15% annualized volatility. If all positions combined would produce 20% vol, scale everything down proportionally.
3. **Maximum correlation adjustment:** Reduce exposure when many markets are trending in the same direction (correlation clustering), as the portfolio becomes less diversified.

## Indicators Used
- [[simple-moving-average]] and [[exponential-moving-average]] (50, 100, 200-day)
- Channel breakout (Donchian Channel, highest high / lowest low over N days)
- Time-series momentum (12-month return sign)
- [[atr]] for position sizing and stop-loss placement
- Realized [[volatility]] for portfolio risk targeting
- Cross-market correlation for diversification monitoring

## Example Trade
**Market:** Crude Oil (CL) futures, daily chart
1. Crude oil has been falling for 3 months. The 50-day SMA crosses below the 200-day SMA. The 12-month return is -25%. The 100-day channel low is broken. All three signal types agree: short.
2. Sell 5 contracts at $72.00 (sized for 1% portfolio risk based on ATR of $2.50 and $1,000/point value). Trailing stop at $78.00 (2.4x ATR above entry).
3. Crude continues its downtrend over the next 4 months, reaching $54.00. The trailing stop has moved down to $60.00, locking in significant profit.
4. After 5 months, crude bounces sharply. The 50-day MA crosses above the 200-day. Exit short at $61.00 (trailing stop triggered).
5. **Result:** +$11.00/contract x 5 contracts x $1,000 = $55,000 profit. Simultaneously, the system was long gold and short EUR/USD during this period, adding diversified returns.

## Performance Characteristics
- **Win Rate:** 35-45%. Trend following has a low win rate but profits from fat-tailed, extended trends that produce outsized gains.
- **Profit Factor:** 1.3-2.0. The strategy relies on a few big winners each year to offset many small losses.
- **Best Market Conditions:** Strong, persistent trends in any direction across any market. Crisis periods (2008, 2022) often produce excellent CTA returns because bonds, currencies, and commodities trend violently.
- **Worst Market Conditions:** Choppy, range-bound, mean-reverting markets (2011-2013, 2015-2016). Extended low-volatility environments with no sustained trends.
- **Annual Returns:** 8-15% annualized at 10-12% volatility. Sharpe ratio: 0.5-0.8 over full cycles.
- **Crisis Alpha:** The strategy's greatest value is its negative correlation to equities during crashes. In 2008, trend-following CTAs returned +15-25% while equities fell 40%+.
- **Drawdowns:** Expect 15-25% peak-to-trough drawdowns lasting 1-3 years during trendless environments.

## Advantages
- Genuine portfolio diversifier: low to negative correlation with stocks and bonds, especially during crises
- Trades both long and short across all major asset classes -- profits in any macro environment
- Over 100 years of backtested evidence and 40+ years of live track records from top CTAs
- Fully systematic and rules-based, removing emotional decision-making
- Benefits from [[volatility]] -- crisis periods often produce the best returns
- Scalable: manages billions of dollars without significantly impacting markets due to the liquidity of futures

## Disadvantages
- **Extended drawdowns in trendless markets** can last 2-3 years, testing investor patience severely
- Low win rate (35-45%) is psychologically difficult even when long-term results are positive
- **Capacity constraints:** As more capital enters trend following, the strategies can become crowded, and trend reversals become sharper as everyone exits simultaneously
- Requires sophisticated infrastructure: futures accounts, margin management, real-time data, and risk systems
- Transaction costs from frequent trading across dozens of markets reduce returns
- The "crisis alpha" benefit is episodic and unpredictable -- investors must hold through years of mediocre returns to capture the rare but lucrative crisis profits

## Commodity Futures: The Core CTA Asset Class

[[commodities|Commodity futures]] are the **core asset class** for most CTA programs and typically represent the largest allocation in diversified trend-following portfolios. This is for several reasons:

- **Trend persistence**: Commodities tend to exhibit stronger and more sustained trends than equities, driven by physical [[supply-demand-balance|supply/demand]] dynamics, [[commodity-super-cycle|super cycles]], and [[capex-cycle|capex cycles]] that unfold over years
- **Diversification**: Commodity markets (energy, metals, agriculture) have low correlation to each other and to financial assets, providing genuine portfolio diversification
- **Two-sided opportunity**: Commodity prices can decline as readily as they rise (unlike equities which have a long-term upward bias), making the short side equally productive for trend followers
- **Historical performance**: The original CTA programs (including [[turtle-trading|Turtle Trading]]) were primarily commodity-focused. Academic research (Moskowitz, Ooi, Pedersen 2012) shows time-series momentum is strongest in commodity and currency markets.
- **Related strategies**: CTA programs often combine trend signals with [[commodity-momentum|cross-sectional momentum]] and [[commodity-carry-strategy|carry]] signals to enhance returns. [[cot-report-analysis|COT positioning data]] can provide additional context for timing entries and exits.

A typical CTA program allocates 40-60% of its risk budget to commodity futures, with the remainder split between currencies, fixed income, and equity index futures. (Source: [[2026-04-14-commodities-research-framework]])

## See Also
- [[turtle-trading]] -- the most famous trend-following system, which uses channel breakouts
- [[moving-average-crossover]] -- the core signal used by many CTA systems
- [[factor-investing]] -- time-series momentum is a factor that can be accessed in equities too
- [[momentum]] -- the underlying concept that drives trend following returns
- [[breakout-trading]] -- channel breakout methodology used in CTA systems
- [[commodity-momentum]] -- cross-sectional momentum in commodity futures
- [[commodity-carry-strategy]] -- systematic carry trading in commodity futures
- [[cot-report-analysis]] -- positioning data analysis for futures markets
- [[commodities]] -- the commodity markets overview
