---
title: "Factor Investing"
type: strategy
created: 2026-04-06
updated: 2026-04-07
status: good
tags: [factor-investing, quantitative, Fama-French, smart-beta, multi-factor, value-factor, momentum-factor, quality, size]
aliases: ["Smart Beta", "Multi-Factor Investing", "Factor-Based Investing", "Fama-French Model"]
strategy_type: quantitative
timeframe: long-term
markets: [stocks]
complexity: advanced
backtest_status: untested
related: ["[[value-investing-strategy]]", "[[growth-investing-strategy]]", "[[trend-following-cta]]", "[[sector-rotation]]", "[[momentum]]", "[[book-inside-the-black-box]]", "[[book-the-intelligent-investor]]"]
---

# Factor Investing

## Overview

Factor Investing is a systematic, rules-based strategy that constructs portfolios by targeting specific **return drivers** (factors) that have been shown to deliver risk-adjusted excess returns over long periods. The approach is rooted in academic finance, primarily the work of **Eugene Fama** and **Kenneth French**, whose three-factor model (1993) demonstrated that stock returns are explained by market risk, **size** (small beats large), and **value** (cheap beats expensive). Since then, additional factors have been documented: **momentum** (winners keep winning), **quality** (profitable firms outperform), and **low volatility** (less risky stocks paradoxically deliver higher risk-adjusted returns).

Factor investing bridges [[fundamental-analysis]] and [[algorithmic-trading]]. Factors are identified through academic research but implemented through systematic, quantitative portfolio construction (Source: [[book-inside-the-black-box]]). The strategy is used by major institutional firms including **AQR Capital Management**, **Dimensional Fund Advisors**, **BlackRock** (via iShares factor ETFs), and **Two Sigma**. Assets managed using factor strategies exceed $2 trillion globally.

## Rules

### Entry
1. **Select target factors** based on investment goals and beliefs:
   - **Value:** Buy stocks in the cheapest quintile by P/B, P/E, or EV/EBITDA. Sell/avoid the most expensive quintile. The [[value-investing-strategy|value premium]] has averaged 3-5% annually (Source: [[book-the-intelligent-investor]]).
   - **Momentum:** Buy stocks with the highest 12-month returns (excluding the most recent month). Sell/avoid the worst performers. The [[momentum]] premium has averaged 4-8% annually.
   - **Quality:** Buy stocks with high ROE, low debt, stable earnings growth. Avoid unprofitable, highly leveraged firms. Quality premium: 2-4% annually.
   - **Size:** Overweight small-cap stocks relative to large-caps. The size premium has averaged 2-3% annually (though it has weakened post-publication).
   - **Low Volatility:** Buy stocks with the lowest realized volatility or beta. The low-vol anomaly: lower risk, similar or higher returns.
2. **Construct a multi-factor portfolio** by combining 2-4 factors. Multi-factor approaches are more diversified than single-factor bets because factors have low correlations with each other.
3. **Rebalance systematically** at fixed intervals: monthly for momentum, quarterly or semi-annually for value, quality, and size. Do not deviate from the schedule based on discretion.
4. **Market-neutral option:** Go long top-quintile factor stocks and short bottom-quintile stocks to isolate pure factor returns from market direction.

### Exit
1. **Rebalance-driven exit:** Stocks are sold when they no longer rank in the target quintile at the next rebalance date. This is purely mechanical.
2. **Factor timing (advanced):** Some practitioners reduce factor exposure when the factor's spread (valuation gap between cheap and expensive) is historically narrow, suggesting less opportunity.
3. **Risk management:** If the portfolio drawdown exceeds a predefined threshold (e.g., 20%), reduce overall exposure, not individual factor allocations.

### Position Sizing
Equal-weight or risk-parity across factors. Within each factor, equal-weight the constituent stocks (typically 50-200 stocks per factor quintile). Total portfolio: 200-500 stocks for broad diversification.

## Indicators Used
- [[price-to-book|P/B ratio]], [[price-to-earnings|P/E ratio]], EV/EBITDA for value factor
- 12-1 month price [[momentum]] (12-month total return minus the most recent month)
- Return on equity (ROE), debt/equity, earnings stability for quality factor
- Market capitalization for size factor
- Realized [[volatility]] (standard deviation of returns) or [[beta]] for low-vol factor
- Factor spread (valuation gap between long and short legs) for timing signals

## Example Trade
**Portfolio:** Multi-factor strategy combining value + momentum + quality
1. At quarterly rebalance, screen the Russell 1000 universe. Score each stock on value (P/B rank), momentum (12-1 month return rank), and quality (ROE + debt/equity rank). Composite score = average of three factor ranks.
2. Buy the top 100 stocks by composite score. Each position: 1% of portfolio ($10,000 each on a $1M portfolio).
3. Sell the bottom 100 stocks (market-neutral variant) or simply exclude them (long-only variant).
4. Three months later at next rebalance: 25 stocks have dropped out of the top 100 and 25 new stocks enter. Sell the 25 exits, buy the 25 entries.
5. **Result:** Over a 10-year backtest, the multi-factor portfolio returns 12.5% annualized vs. 10.0% for the market -- a 2.5% annual alpha with similar volatility. The Sharpe ratio improves from 0.55 (market) to 0.75 (multi-factor).

## Performance Characteristics
- **Win Rate:** Not measured per trade -- measured by long-term factor premiums over rolling 5-10 year periods.
- **Expected Alpha:** 2-5% annually for multi-factor strategies over long periods.
- **Best Market Conditions:** Factors perform best when their respective premiums are "on." Value works in recoveries and rising-rate environments. Momentum works in trending markets. Quality works in downturns.
- **Worst Market Conditions:** Factor crashes (momentum crash of 2009, value drawdown of 2018-2020). Factor crowding: when too much capital chases the same factor signals, returns compress and reversals become violent.
- **Sharpe Ratio:** 0.5-0.8 for single factors, 0.7-1.2 for multi-factor combinations.
- **Drawdowns:** Factor portfolios can underperform for 3-5+ years. The value factor underperformed from 2017-2020, testing investor patience.

## Advantages
- Grounded in decades of academic research with robust out-of-sample evidence across countries and time periods
- Highly diversified (hundreds of stocks) reduces single-stock and sector risk
- Systematic, rules-based implementation removes emotional biases and discretionary errors
- Factors are well-understood risk premiums, not market inefficiencies that might disappear
- Low-cost implementation via factor ETFs (iShares, Vanguard, DFA) makes it accessible to individual investors
- Multi-factor combinations provide smoother returns than single-factor bets

## Disadvantages
- **Factor premiums can disappear for extended periods** -- the value factor underperformed for 5+ years, causing enormous investor attrition
- **Factor crowding:** As more capital flows into factor strategies, the premiums may be arbitraged away
- **Implementation costs:** High turnover (especially momentum) creates transaction costs and tax drag that erode theoretical returns
- **Model risk:** Factor definitions vary (P/B vs. P/E vs. EV/EBITDA for value), and different definitions produce materially different returns
- Requires faith in long-term statistical evidence, which is psychologically difficult during multi-year drawdowns
- **Data mining concern:** Some critics argue published factors are artifacts of data snooping, not genuine risk premiums

## Sources

- [[book-inside-the-black-box]] — quant fund architecture for factor-based strategies, including alpha model construction, risk models, and portfolio optimization
- [[book-the-intelligent-investor]] — the intellectual foundation of the value factor, including margin of safety and systematic cheapness as a return driver

## See Also
- [[value-investing-strategy]] -- the fundamental approach to the value factor
- [[momentum]] -- the standalone momentum strategy and its mechanics
- [[trend-following-cta]] -- applies momentum concepts to futures markets
- [[sector-rotation]] -- rotates between sectors using macro signals, complementary to factor rotation
- [[growth-investing-strategy]] -- growth stocks often load negatively on the value factor
