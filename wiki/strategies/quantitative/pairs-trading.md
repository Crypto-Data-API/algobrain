---
title: "Pairs Trading"
type: strategy
created: 2026-04-06
updated: 2026-04-07
status: good
tags: [mean-reversion, pairs-trading, statistical-arbitrage, market-neutral, quantitative, cointegration]
aliases: ["Pairs Trade", "Statistical Pairs Trading", "Stat Arb Pairs"]
strategy_type: quantitative
timeframe: swing|position
markets: [stocks, crypto]
complexity: advanced
backtest_status: untested
related: ["[[statistical-arbitrage]]", "[[mean-reversion]]", "[[bollinger-band-reversion]]", "[[correlation]]", "[[market-neutral]]", "[[book-algorithmic-trading-ernest-chan]]", "[[book-statistical-arbitrage-pole]]", "[[book-pairs-trading-vidyamurthy]]"]
---

# Pairs Trading

## Overview

Pairs trading is a classic [[statistical-arbitrage]] strategy that identifies two historically correlated or cointegrated assets, then profits from temporary divergences in their price relationship. When the spread between the two assets widens beyond its historical norm, you go **long the underperformer** and **short the outperformer**, betting that the spread will revert to its mean. The strategy is [[market-neutral]] -- it profits regardless of overall market direction because you hold both a long and short position simultaneously.

The strategy was pioneered at Morgan Stanley in the 1980s by quantitative trader Nunzio Tartaglia and his team (Source: [[book-pairs-trading-vidyamurthy]]). It has since become a staple of quantitative hedge funds and a foundational concept in [[statistical-arbitrage]].

The critical distinction is between **correlation** and **cointegration**. Two assets can be correlated (move in the same direction) without being cointegrated (maintaining a stable long-term relationship). Pairs trading requires **cointegration** -- the spread between the assets must be mean-reverting (Source: [[book-algorithmic-trading-ernest-chan]]). Testing for cointegration uses methods like the **Engle-Granger two-step test** or the **Johansen test**.

## Rules

### Pair Selection
1. Identify candidate pairs from the same sector, industry, or asset class (e.g., Coca-Cola/PepsiCo, BTC/ETH, Gold miners).
2. Test for **cointegration** using the Engle-Granger test (p-value < 0.05) or Johansen test. Correlation alone is insufficient.
3. Calculate the **hedge ratio** (beta) using linear regression: how many shares of Asset B to trade per share of Asset A (Source: [[book-algorithmic-trading-ernest-chan]]).
4. Compute the **spread** = Price_A - (hedge_ratio x Price_B). Verify the spread is stationary (Augmented Dickey-Fuller test).

### Entry
1. Calculate the spread's z-score: z = (current_spread - mean_spread) / std_spread.
2. **Long Entry:** When z-score drops below -2.0 (spread is unusually narrow): buy Asset A, short Asset B.
3. **Short Entry:** When z-score rises above +2.0 (spread is unusually wide): short Asset A, buy Asset B.
4. Some traders use 1.5 standard deviations for more frequent signals, or 2.5 for higher conviction.

### Exit
1. **Mean Reversion Exit:** Close both legs when the z-score returns to 0 (spread reverts to mean).
2. **Partial Exit:** Take partial profits at z = 0.5 on the way back to zero.
3. **Stop-Loss:** Close both legs if z-score reaches +/- 3.5-4.0 (spread is diverging further, cointegration may be breaking down).
4. **Time Stop:** If the spread hasn't reverted within 20-30 trading days, close and reassess.

### Position Sizing
Size each leg proportionally using the hedge ratio. For dollar-neutral exposure: Long Position Value = Short Position Value (adjusted by beta).

## Indicators Used
- **Spread** (price difference adjusted by hedge ratio)
- **Z-Score** of the spread
- **Cointegration tests:** Engle-Granger, Johansen
- **Augmented Dickey-Fuller test** for stationarity
- [[bollinger-bands]] applied to the spread (visual z-score representation)
- **Rolling correlation** to monitor relationship stability

## Classic Pairs Examples
| Pair | Sector | Rationale |
|------|--------|-----------|
| KO / PEP | Consumer Staples | Same industry, similar business models |
| XOM / CVX | Energy | Major oil companies, driven by same commodity |
| BTC / ETH | Crypto | Dominant crypto assets, highly cointegrated historically |
| GLD / SLV | Commodities | Precious metals with historical spread relationship |
| JPM / BAC | Financials | Major banks with correlated earnings drivers |

## Example Trade
**Pair:** Coca-Cola (KO) / PepsiCo (PEP), daily chart
1. Hedge ratio (from 252-day regression): 0.85. Spread = KO - 0.85 x PEP.
2. Mean spread over 252 days: $2.50. Standard deviation: $1.20.
3. KO drops on an earnings miss while PEP holds steady. Current spread: $0.10. Z-score = ($0.10 - $2.50) / $1.20 = **-2.0**.
4. Enter: Buy 1,000 shares KO at $58.00, short 850 shares PEP at $67.00.
5. Over 12 trading days, KO recovers and PEP softens. Spread reverts to $2.50 (z = 0).
6. Exit: Sell KO at $60.00 (+$2,000), cover PEP at $67.65 (-$552.50).
7. **Net Profit:** $2,000 - $552.50 = **$1,447.50** (market-neutral, regardless of S&P direction).

## Performance Characteristics
- **Win Rate:** 60-70% when pairs are properly cointegrated and z-score thresholds are respected.
- **Profit Factor:** 1.5-2.0. The market-neutral design limits both upside and downside.
- **Sharpe Ratio:** Typically 1.0-2.0 in well-constructed portfolios of multiple pairs.
- **Best Market Conditions:** Stable macro environments where sector relationships hold. Range-bound markets.
- **Worst Market Conditions:** Regime changes, sector rotations, or idiosyncratic events (e.g., one company in the pair gets acquired, has a scandal, or fundamentally changes its business).

## Advantages
- [[market-neutral]] -- profits in up, down, or sideways markets
- Reduces exposure to systematic market risk (beta near zero)
- Statistically rigorous framework with well-established academic foundations
- Losses are bounded when stop-losses are respected (both legs partially hedge each other)
- Can be highly automated -- the entire process from pair selection to execution can be coded

## Disadvantages
- **Cointegration can break:** Historical relationships do not guarantee future stability. Structural changes (mergers, regulatory shifts) can permanently alter the spread
- **Requires shorting:** Short selling comes with borrowing costs, short squeeze risk, and regulatory restrictions
- **Execution complexity:** Two simultaneous legs mean double the commissions, slippage, and operational risk
- **Model risk:** Incorrect hedge ratios or lookback periods produce false signals
- **Capital-intensive:** Market-neutral returns are modest per unit of capital, requiring leverage to achieve meaningful absolute returns
- **Crowded strategy:** Widely used by quant funds, which can reduce the available edge (Source: [[book-statistical-arbitrage-pole]])

## Sources

- [[book-algorithmic-trading-ernest-chan]] — the definitive practical reference for pairs trading, including cointegration testing, hedge ratio estimation, the Johansen test, and the connection to [[ornstein-uhlenbeck]] mean-reversion models
- [[book-statistical-arbitrage-pole]] — Pole (2007) covers the statistical foundations of pairs trading within the broader stat arb framework, including mean-reversion modeling and portfolio-level pair selection
- [[book-pairs-trading-vidyamurthy]] — Vidyamurthy (2004) provides the foundational treatment of pairs trading, including cointegration theory, spread modeling, and the historical origins at Morgan Stanley

## See Also
- [[statistical-arbitrage]] -- the broader category that includes pairs trading
- [[mean-reversion]] -- the underlying market behavior pairs trading exploits
- [[bollinger-band-reversion]] -- can be applied to the spread for visual trade identification
- [[market-neutral]] -- the portfolio characteristic pairs trading achieves
- [[correlation]] -- important but not sufficient; cointegration is the real requirement
