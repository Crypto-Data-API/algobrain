---
title: "Covered Call"
type: strategy
created: 2026-04-06
updated: 2026-04-07
status: good
tags: [options, income, premium-selling, covered-call, hedging, equity-options]
aliases: ["Buy-Write", "Covered Call Writing", "covered-calls", "covered-call-strategy"]
strategy_type: hybrid
timeframe: swing|position
markets: [stocks, crypto]
complexity: beginner
backtest_status: untested
related: ["[[wheel-strategy]]", "[[iron-condor]]", "[[straddle-strangle]]", "[[implied-volatility]]", "[[delta]]", "[[option-volatility-and-pricing]]"]
---

# Covered Call

## Overview

The Covered Call is the most common [[options]] income strategy. The trader owns 100 shares of the underlying stock (or equivalent crypto position) and sells one [[call-option]] against those shares, collecting the option [[premium]] as immediate income. The premium lowers the effective cost basis of the position, providing a small downside buffer, while capping the upside at the chosen [[strike-price]] (Source: [[book-option-volatility-and-pricing]]). The strategy is inherently **bullish-to-neutral** -- it performs best when the underlying drifts sideways or rises modestly, allowing the sold call to expire worthless so the trader keeps both the shares and the full premium.

Covered calls are popular among long-term investors who want to generate yield on holdings they intend to keep. In sideways or slightly bullish markets, they consistently outperform a simple buy-and-hold approach. The trade-off is clear: you sacrifice unlimited upside potential in exchange for guaranteed premium income today.

## Rules

### Entry
1. **Own 100 shares** (or the equivalent lot size) of the underlying asset. Ensure you are comfortable holding this stock long-term.
2. **Sell 1 OTM call option** per 100 shares, typically 1-2 strikes above the current price. Select a strike with a [[delta]] of 0.20-0.35 for a balanced premium vs. assignment probability.
3. **Choose expiration:** 30-45 days to expiration (DTE) captures the steepest portion of the [[theta]] decay curve. Weekly expirations offer more frequent premium but require more management.
4. Favor periods of elevated [[implied-volatility]] (IV rank above 30) to maximize the premium collected.

### Exit
1. **Max profit exit:** The call expires worthless (price stays below strike). Keep the premium and sell a new call for the next cycle.
2. **Roll up and out:** If the stock rallies through your strike before expiration, buy back the call and sell a higher strike / further-dated call for a net credit.
3. **Close early:** Buy back the call when it has decayed to 50-80% of the premium collected, then re-sell a new one.
4. **Stop-loss on shares:** If the stock drops significantly (e.g., below a key [[support]] level), close the entire position. The collected premium provides only a small cushion, not full protection.

### Position Sizing
Risk no more than 5-10% of the portfolio in a single covered call position. Diversify across multiple underlyings to reduce concentration risk.

## Indicators Used
- [[implied-volatility]] / IV rank -- higher IV means richer premiums
- [[delta]] -- guides strike selection (0.20-0.35 OTM is typical)
- [[theta]] -- measures daily time decay working in the seller's favor
- [[support-and-resistance]] -- avoid selling calls below key resistance where a breakout is likely

## Example Trade
**Asset:** AAPL trading at $185
1. Own 100 shares of AAPL (cost basis $180).
2. Sell 1 AAPL $195 call, 35 DTE, for $3.20 premium ($320 total). The $195 strike has a delta of ~0.25.
3. **Scenario A -- stock stays below $195:** The call expires worthless. Keep $320 premium. Annualized yield: ($320 / $18,500) x (365/35) = ~18%. Sell a new call for the next cycle.
4. **Scenario B -- stock rallies to $200:** Shares are called away at $195. Profit: ($195 - $180) x 100 + $320 = $1,820. Good return, but you missed the move from $195 to $200.
5. **Scenario C -- stock drops to $170:** Option expires worthless (keep $320), but shares lost $1,500 in value. Net loss: $1,180. The premium offset only ~21% of the decline.

## Performance Characteristics
- **Win Rate:** 70-85%, since OTM calls expire worthless the majority of the time.
- **Profit Factor:** 1.5-2.0. Frequent small wins offset by occasional larger losses when the stock drops sharply.
- **Best Market Conditions:** Sideways to slightly bullish. Low-to-moderate [[volatility]] environments.
- **Worst Market Conditions:** Strong bull markets (upside is capped) and sharp sell-offs (premium cushion is insufficient).
- **Benchmark:** The CBOE S&P 500 BuyWrite Index (BXM) has historically matched or slightly trailed the S&P 500 in total return but with noticeably lower volatility.

## Advantages
- Simple to understand and execute -- the ideal first options strategy for beginners
- Generates consistent income on existing long positions, lowering cost basis over time
- Reduces portfolio [[volatility]] compared to holding shares alone
- [[theta]] decay works in your favor every day
- Defined maximum loss (stock goes to zero minus premium received)

## Disadvantages
- **Capped upside:** You forgo all gains above the strike price, which stings in strong rallies
- **Limited downside protection:** The premium collected is a small buffer, not a hedge
- **Opportunity cost:** If the stock surges, you underperform simple buy-and-hold significantly
- **Capital intensive:** Requires owning 100 shares per contract, which is expensive for high-priced stocks
- **Assignment risk:** Early assignment is possible, especially near ex-dividend dates (Source: [[book-option-volatility-and-pricing]])

## Covered Calls in Long/Short Portfolios

Within a long-short-equity framework (as taught by itpm), covered calls play a specific role:

- Used to generate income on long equity positions while waiting for a fundamental catalyst
- The sold call partially funds the purchase of put options on short positions, reducing overall portfolio cost
- [[trade-repair-and-rolling|Rolling up and out]] is a key management technique when the underlying rallies through the strike
- In the ITPM methodology, covered calls are a component of portfolio construction rather than a standalone strategy

## See Also
- [[wheel-strategy]] -- extends the covered call into a full income cycle with cash-secured puts
- [[iron-condor]] -- a defined-risk premium-selling strategy that does not require owning shares
- [[implied-volatility]] -- the key driver of option premium pricing
- [[theta]] -- the Greek that makes covered calls profitable over time
- [[cash-secured-put]] -- the other side of the wheel, and a natural companion to covered calls
- [[trade-repair-and-rolling]] -- techniques for managing covered calls that go against you
- [[covered-call-vs-cash-secured-put]] -- side-by-side comparison of these two income strategies

## Sources
- [[book-option-volatility-and-pricing]] — Natenberg covers covered call mechanics, early assignment risk near dividends, and the trade-off between premium income and capped upside
