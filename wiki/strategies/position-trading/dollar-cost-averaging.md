---
title: "Dollar-Cost Averaging"
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [accumulation, dca, passive-investing, risk-management, position-trading, beginner]
aliases: ["DCA", "Systematic Investment Plan", "SIP", "Regular Investment"]
strategy_type: fundamental
timeframe: long-term
markets: [crypto]
complexity: beginner
backtest_status: untested
related: ["[[grid-trading]]", "[[risk-management]]", "[[position-sizing]]", "[[value-averaging]]"]
---

# Dollar-Cost Averaging

## Overview

Dollar-Cost Averaging (DCA) is the practice of investing a fixed dollar amount into an asset at regular intervals (weekly, bi-weekly, monthly) regardless of the current price. When prices are high, the fixed amount buys fewer units; when prices are low, it buys more. Over time, this produces an average cost per unit that is lower than the simple average of prices during the investment period -- a mathematical property known as the **harmonic mean advantage**.

DCA is not technically a "trading" strategy in the active sense -- it is a **systematic accumulation approach** designed to reduce the risk of poor market timing. It is by far the most common strategy used by retail investors, whether they realize it or not: every 401(k) contribution, automatic index fund purchase, or recurring crypto buy is DCA in action.

The strategy's power lies in its psychological simplicity. It removes the paralyzing question "is now a good time to buy?" and replaces it with a mechanical process. Research by Vanguard (2012) found that **lump-sum investing outperforms DCA approximately two-thirds of the time** because markets trend upward over long periods. However, DCA significantly reduces volatility and maximum drawdown, making it psychologically easier to stick with -- and the strategy you actually follow beats the optimal strategy you abandon.

## Rules

### Entry
1. **Fixed Amount:** Choose a fixed dollar amount to invest per interval (e.g., $500/month).
2. **Fixed Schedule:** Choose a regular interval: weekly, bi-weekly, or monthly. Set it as an automatic recurring purchase.
3. **Execute Regardless of Price:** Buy at the scheduled time no matter what the market is doing. Do not skip, delay, or "wait for a dip."
4. **Asset Selection:** Choose a broad, diversified asset (index fund like SPY/VTI, BTC for crypto) or a high-conviction individual asset.

### Exit
1. **Goal-Based Exit:** Sell when you reach a financial goal (retirement, house down payment, target portfolio value).
2. **Rebalancing Exit:** Sell as part of portfolio rebalancing when the asset exceeds its target allocation.
3. **Fundamental Deterioration:** Stop DCA-ing into an asset if the fundamental thesis changes (e.g., a company's business model is permanently impaired). This does NOT apply to broad index funds.
4. **There is no technical exit signal.** DCA is a long-term accumulation strategy, not a trading system.

### Variations
| Variation | Description |
|-----------|-------------|
| **Standard DCA** | Fixed amount at fixed intervals. The baseline. |
| **Value Averaging** | Adjust contribution so portfolio value grows by a fixed amount each period. Invest more when prices are low, less when high. |
| **Enhanced DCA** | Increase the buy amount when RSI(14) < 30 or price is below the 200-day SMA. A hybrid with [[rsi-mean-reversion]]. |
| **Lump Sum + DCA** | Invest 50% immediately, DCA the remaining 50% over 6-12 months. Compromise approach. |

## Indicators Used
DCA does not traditionally use indicators, but enhanced versions may incorporate:
- [[simple-moving-average|200-day SMA]] to determine if enhanced (larger) purchases are appropriate during downtrends
- [[rsi]] to scale purchase amounts (buy more when oversold)
- **On-chain metrics** (for crypto): MVRV ratio, NVT ratio to assess value

## Example: DCA into Bitcoin
**Asset:** BTC/USD, monthly purchases of $500
1. **Month 1:** BTC at $40,000. Buy 0.0125 BTC.
2. **Month 2:** BTC drops to $35,000. Buy 0.01429 BTC. (More BTC for the same $500.)
3. **Month 3:** BTC crashes to $25,000. Buy 0.02000 BTC. (Even more BTC.)
4. **Month 4:** BTC recovers to $30,000. Buy 0.01667 BTC.
5. **Month 5:** BTC rallies to $45,000. Buy 0.01111 BTC.
6. **Month 6:** BTC at $42,000. Buy 0.01190 BTC.

**Totals after 6 months:**
- Total invested: $3,000
- Total BTC accumulated: 0.08647 BTC
- Average cost per BTC: $3,000 / 0.08647 = **$34,694**
- Simple average of prices: ($40k + $35k + $25k + $30k + $45k + $42k) / 6 = $36,167
- **DCA cost basis is $1,473 lower** than the simple average price thanks to buying more at lower prices.

## Performance Characteristics
- **Win Rate:** Not applicable in the traditional sense. Over long periods (10+ years), DCA into broad index funds has been profitable in nearly every historical window.
- **vs. Lump Sum:** DCA underperforms lump sum ~66% of the time in rising markets but outperforms in declining or volatile markets.
- **Best Market Conditions:** Volatile, range-bound, or declining markets where the cost-averaging effect is strongest. Also excellent in markets that decline then recover (V-shaped or U-shaped).
- **Worst Market Conditions:** A steadily rising market with no pullbacks. In this case, lump-sum investing is superior because every delayed purchase is at a higher price.

## Advantages
- Eliminates market timing -- the most common source of retail investor underperformance
- Psychologically simple: automate it and forget about market fluctuations
- The harmonic mean advantage guarantees a lower average cost than the simple average of prices
- Disciplined buying during downturns (when others panic-sell) creates the best long-term outcomes
- No expertise required -- ideal for absolute beginners
- Universal access: available through brokerages, 401(k) plans, and crypto exchanges

## Disadvantages
- **Suboptimal in rising markets:** Lump-sum investing beats DCA two-thirds of the time because markets have a long-term upward bias
- **Slow capital deployment:** Holding cash on the sidelines has an opportunity cost, especially in inflationary environments
- **No risk management:** Standard DCA has no stop-loss or exit mechanism. You hold through 50%+ drawdowns.
- **Can become a trap:** DCA-ing into a fundamentally broken asset (a failing company, a dead altcoin) destroys capital systematically
- **Boring:** The lack of active decision-making can lead traders to override the system, usually at the worst possible time

## See Also
- [[grid-trading]] -- a more active version of the DCA concept with profit-taking at defined intervals
- [[risk-management]] -- DCA is itself a form of timing risk management
- [[position-sizing]] -- DCA enforces consistent, mechanical position sizing
- [[value-averaging]] -- a more sophisticated variant that adjusts contribution amounts
- [[rsi-mean-reversion]] -- can be combined with DCA for "enhanced DCA" during oversold periods
