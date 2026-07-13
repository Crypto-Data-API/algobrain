---
title: "Dividend Capture"
type: strategy
created: 2026-04-06
updated: 2026-04-07
status: good
tags: [dividends, income, fundamental-analysis, ex-dividend, yield, passive-income]
aliases: ["Dividend Capture Strategy", "Ex-Dividend Trading", "Dividend Stripping"]
strategy_type: fundamental
timeframe: swing
markets: [stocks]
complexity: beginner
backtest_status: untested
related: ["[[value-investing-strategy]]", "[[sector-rotation]]", "[[covered-call]]", "[[options-strategies]]", "[[dividend-yield]]", "[[book-the-intelligent-investor]]"]
---

# Dividend Capture

## Overview

The Dividend Capture strategy attempts to collect dividend payments by purchasing a stock shortly before its **ex-dividend date** and selling it shortly after. To receive the dividend, you must own shares before the ex-date -- shares purchased on or after the ex-date do not qualify. In theory, the stock price drops by roughly the dividend amount on the ex-date, so the strategy only profits if the dividend exceeds the price drop plus transaction costs, or if the stock recovers quickly.

This is one of the simplest [[fundamental-analysis]] strategies but is often misunderstood. Graham emphasized that dividends are a key component of total return and a sign of financial health in defensive stock selection (Source: [[book-the-intelligent-investor]]). The price adjustment on the ex-date is mechanical and well-known, so pure dividend capture has a razor-thin edge at best. The strategy works best with **high-yield stocks** (4%+ annual yield), during **strong bull markets** (where the ex-date dip is quickly recovered), and with **low or zero commission** brokers. Many practitioners combine it with [[covered-call]] writing to enhance returns.

## Rules

### Entry
1. **Screen for upcoming ex-dividend dates** using tools like Nasdaq's dividend calendar, Seeking Alpha, or your broker's screener. Target stocks with dividend yields above 3% annually (or per-share payouts above $0.50 for quarterly dividends).
2. **Buy shares 1-2 days before the ex-dividend date.** You must be the shareholder of record by market close the day before the ex-date.
3. **Confirm the stock is in an uptrend** or at least not in a severe downtrend. Check that the 20-day [[moving-average]] is flat or rising. Avoid catching dividends on stocks that are falling apart fundamentally.
4. **Check for options availability** -- if the stock has liquid options, consider selling a [[covered-call]] simultaneously to collect additional premium.

### Exit
1. **Sell on the ex-date or 1-3 days after.** The goal is to exit as soon as the stock recovers the dividend-induced price drop.
2. **Maximum hold: 5 trading days.** If the stock has not recovered by then, exit to free capital for the next opportunity.
3. **Stop-loss:** Set at 2-3% below entry (excluding the expected dividend drop). If the stock falls further than the dividend justifies, cut the position.

### Position Sizing
Allocate larger positions (5-10% of portfolio) since holding periods are very short. Ensure commission costs are negligible relative to the dividend received.

## Indicators Used
- Ex-dividend date calendar
- [[dividend-yield]] (annualized and per-share payout)
- [[moving-average]] (20-day) for trend confirmation
- [[volume]] -- avoid illiquid stocks where the bid-ask spread erodes the dividend
- Payout ratio -- avoid companies with unsustainably high payout ratios (risk of dividend cut)

## Example Trade
**Asset:** Verizon (VZ) with a quarterly dividend of $0.665/share (~6.5% annualized yield)
1. VZ is trading at $41.00 with ex-dividend date on Thursday. The 20-day MA is flat, and the stock is in a stable range.
2. Buy 500 shares on Wednesday at $41.00. Total investment: $20,500.
3. Thursday (ex-date): VZ opens at $40.40, down $0.60 (slightly less than the $0.665 dividend). You are entitled to the dividend.
4. By Friday close, VZ recovers to $40.85. Sell 500 shares at $40.85.
5. **Result:** Capital loss of $0.15/share ($75 total) + dividend income of $0.665/share ($332.50 total) = **net profit of $257.50** (1.26% return in 2 days). Annualized, this is attractive if repeatable.

## Performance Characteristics
- **Win Rate:** 50-60%. In bull markets, the ex-date dip recovers more reliably. In bear markets, the dip often deepens.
- **Profit Factor:** 1.1-1.5. Gains per trade are small, so consistency matters.
- **Best Market Conditions:** Stable or rising markets. Low [[volatility]] environments where the ex-date price drop is small relative to the dividend.
- **Worst Market Conditions:** Bear markets, high-volatility environments, or periods of rising interest rates where high-yield stocks face selling pressure.
- **Annual Opportunities:** Hundreds. Major dividend-paying stocks go ex-dividend quarterly, and the universe spans REITs, utilities, telecoms, and energy companies.

## Advantages
- Very simple to understand and execute -- ideal for beginners learning about dividends and market mechanics
- Short holding period limits exposure to market risk
- Can be systematized and repeated across dozens of stocks each quarter
- Generates actual cash income (dividends) regardless of price movement
- Works well as a complement to other strategies during low-volatility periods

## Disadvantages
- **Tax inefficiency:** Dividends held less than 60 days are taxed as ordinary income, not the lower qualified dividend rate. This can significantly erode after-tax returns.
- The ex-date price drop is theoretically efficient -- the stock should drop by exactly the dividend amount, leaving zero edge before costs
- Wash sale rules can complicate tax reporting if trading the same stocks repeatedly
- Requires significant capital to generate meaningful dollar returns from small per-share dividends
- Dividend cuts or suspensions can cause large losses that wipe out months of captured dividends

## Sources

- [[book-the-intelligent-investor]] — Graham's discussion of dividends as a component of defensive investing and total return

## See Also
- [[value-investing-strategy]] -- longer-term approach that also favors dividend-paying companies
- [[covered-call]] -- selling calls on dividend stocks enhances yield
- [[sector-rotation]] -- utilities and staples (high-dividend sectors) are favored in late cycle and recession
- [[options-strategies]] -- various ways to enhance income around dividend dates
