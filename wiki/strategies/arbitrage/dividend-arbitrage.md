---
title: "Dividend Arbitrage"
type: strategy
created: 2026-04-07
updated: 2026-04-07
status: good
tags: [arbitrage, dividend, options, ex-dividend, put, tax-arbitrage, income, equities]
aliases: ["Dividend Arb", "Ex-Date Arbitrage", "Dividend Capture with Hedge"]
strategy_type: hybrid
timeframe: swing
markets: [stocks]
complexity: intermediate
backtest_status: untested
related: ["[[dividend-capture]]", "[[married-put]]", "[[options]]", "[[covered-call]]", "[[ex-dividend-date]]"]
---

# Dividend Arbitrage

## Overview

Dividend arbitrage is an options-based strategy that seeks to capture a stock's dividend while hedging the downside risk of the ex-dividend price drop using a protective [[married-put|put option]]. The theoretical basis is straightforward: on the [[ex-dividend-date]], a stock's price drops by approximately the dividend amount. By purchasing the stock before the ex-date and simultaneously buying a put, the trader collects the dividend while the put protects against the price decline. The strategy profits if the dividend exceeds the cost of the put plus transaction costs.

A second, more sophisticated variant exploits international dividend withholding tax treaties. Different countries apply different withholding tax rates on dividends paid to foreign investors. By routing dividend income through entities in jurisdictions with favorable tax treaties, institutions can recover withholding taxes that other investors cannot -- effectively arbitraging the tax code. This "dividend tax arbitrage" has been the subject of major regulatory crackdowns (the German cum-ex scandal resulted in billions in fines).

## How It Works

**Basic dividend arbitrage:**
1. Identify a stock with an upcoming dividend that is relatively large compared to the at-the-money put premium.
2. Buy the stock before the ex-dividend date (must be the record date holder).
3. Buy a protective put at or near the current stock price, expiring shortly after the ex-date.
4. Collect the dividend on the payment date.
5. After the ex-date, the stock drops by approximately the dividend amount, but the put increases in value by a similar amount (for deep in-the-money puts, delta is near -1).
6. Close both positions. The net result is the dividend minus the put cost minus transaction costs.

**Why it works:** [[options]] pricing models (Black-Scholes) account for expected dividends, but in practice, the pricing of short-dated puts around ex-dates can be imprecise, especially for stocks with irregular or special dividends. The arb exists in the gap between the actual dividend and the market's pricing of the ex-date drop.

## Entry/Exit Rules

### Entry
1. **Screen for candidates:** Find stocks with dividend yield > 1% (per payment), ex-date within 1-5 days, and liquid [[options]] markets.
2. **Calculate profitability:** Dividend per share minus cost of near-the-money put minus round-trip commissions minus bid-ask spread on the put. Only proceed if net is positive.
3. **Buy stock:** Purchase shares before the ex-date (must settle by record date, typically T+1).
4. **Buy put:** Purchase a put option with strike at or slightly below the current price, expiring within 1-2 weeks after the ex-date. The shorter the duration, the cheaper the put (less time premium).

### Exit
1. **After ex-date:** Once the stock goes ex-dividend, evaluate the position. If the stock dropped by approximately the dividend amount (normal), close both legs.
2. **Exercise the put** if the stock has dropped significantly (deep in the money) -- exercising may be more efficient than selling.
3. **Hold if favorable:** If the stock rises despite going ex-dividend (general market rally), the put may expire worthless but the stock gain plus dividend exceed the put cost.

## Example Trade

**Stock:** Johnson & Johnson (JNJ) trading at $160.00. Quarterly dividend: $1.24 per share. Ex-date: tomorrow.

1. **Buy 1,000 shares of JNJ** at $160.00 = $160,000.
2. **Buy 10 JNJ $160 puts** expiring in 10 days at $1.05 per contract ($0.105 per share x 1,000) = **$1,050**.
3. **Collect dividend:** 1,000 x $1.24 = **$1,240**.
4. **Ex-date price drop:** JNJ opens at $158.80 (dropped $1.20, slightly less than the $1.24 dividend).
5. **Put value increases:** The $160 put is now $1.20 in the money. With remaining time value, the put is worth ~$1.35.
6. **Close position:** Sell 1,000 shares at $158.80. Sell 10 puts at $1.35 ($1,350).
7. **P&L:** Stock loss: ($160.00 - $158.80) x 1,000 = -$1,200. Put gain: $1,350 - $1,050 = +$300. Dividend: +$1,240. Commissions: -$30.
8. **Net profit:** -$1,200 + $300 + $1,240 - $30 = **$310**.

## Risk Management

- **Dividend cut or cancellation:** If the company cuts or eliminates the dividend after you have entered the position, the entire premise collapses. The stock may drop on the news, and the put only partially offsets. Focus on [[blue-chip]] companies with long dividend histories.
- **Put pricing:** If implied [[volatility]] is elevated, puts will be expensive and may eliminate the profit. Screen for low IV environments.
- **Early assignment risk:** If using American-style puts, the counterparty may exercise early around the ex-date. This is especially relevant for deep in-the-money calls if you are short them.
- **Tax treatment:** Dividends held less than 60 days may be classified as ordinary income rather than qualified dividends, reducing after-tax profitability. The tax arb variant faces increasing regulatory scrutiny globally.
- **Large capital requirement:** Buying the stock outright requires significant capital, even for a short holding period.
- **Execution risk:** Bid-ask spreads on the put option can erode the small profit margin. Use limit orders.

## Advantages
- **Defined risk** -- the maximum loss is the put premium minus the dividend (assuming no dividend cut)
- **Short holding period** -- typically 1-5 days, freeing capital for reuse
- **Non-directional** -- profits do not depend on the stock going up or down, only on the dividend being paid
- **Works in any market environment** -- dividends are paid in bull and bear markets
- **Tax arb variant** can generate significant institutional returns by exploiting treaty differences

## Disadvantages
- **Small profits per trade** -- the edge is narrow, requiring scale and volume
- **Put cost often exceeds edge** -- for most liquid stocks, put pricing accurately reflects the expected ex-date drop, leaving no arb
- **Transaction costs matter** -- commissions and bid-ask spreads on both legs can eliminate the profit
- **Capital intensive** -- buying stock plus puts for meaningful position sizes requires substantial capital
- **Tax arb is under regulatory attack** -- the German cum-ex scandal (over EUR 10 billion in disputed taxes) has led to global crackdowns
- **Limited opportunity set** -- only a subset of stocks have dividends large enough relative to put premiums to create an arb

## Real-World Examples
- **German cum-ex scandal:** From 2001-2012, banks exploited a loophole to claim dividend tax refunds on shares they did not actually own around ex-dates, extracting an estimated EUR 55 billion from European treasuries. Multiple bankers were convicted.
- **Special dividends:** When companies announce large one-time special dividends (e.g., Costco's $15/share special dividend in 2020), the arb opportunity can be significantly larger than with regular dividends, as options markets may misprice the event.
- **Institutional dividend recapture:** Large pension funds and endowments systematically run dividend capture strategies combined with [[options]] hedges as a portfolio income overlay.

## See Also
- [[dividend-capture]] -- the unhedged version of dividend arbitrage
- [[married-put]] -- the protective put technique used in this strategy
- [[options]] -- the derivative instrument used for hedging
- [[ex-dividend-date]] -- the critical date that determines dividend eligibility
- [[covered-call]] -- a related income strategy using options
