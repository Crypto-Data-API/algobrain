---
title: "Iron Condor"
type: strategy
created: 2026-04-06
updated: 2026-04-07
status: good
tags: [options, premium-selling, iron-condor, defined-risk, neutral, credit-spread, SPY-weekly]
aliases: ["IC", "Iron Condor Spread"]
strategy_type: quantitative
timeframe: swing
markets: [stocks]
complexity: intermediate
backtest_status: untested
related: ["[[covered-call]]", "[[straddle-strangle]]", "[[implied-volatility]]", "[[theta]]", "[[delta]]", "[[bollinger-bands]]", "[[option-volatility-and-pricing]]"]
---

# Iron Condor

## Overview

The Iron Condor is a **market-neutral**, defined-risk options strategy that profits when the underlying asset stays within a range. It combines two [[credit-spread]]s: a short [[put-spread]] below the current price and a short [[call-spread]] above it. Premium is collected from both sides, and the trade profits as long as the price remains between the two short strikes at expiration. Maximum loss is capped at the width of the wider spread minus the total premium received.

Iron Condors are one of the most popular strategies among retail options traders, especially on high-liquidity underlyings like SPY, QQQ, and IWM weeklies. The strategy thrives in low-[[volatility]], range-bound markets and exploits the tendency of [[implied-volatility]] to overstate actual realized moves (Source: [[book-option-volatility-and-pricing]]). Traders who sell Iron Condors are essentially betting that the market will be less dramatic than the options market expects.

## Rules

### Entry
1. **Identify a range-bound underlying** with elevated [[implied-volatility]] (IV rank > 30, ideally > 50). SPY weekly options are the most common choice.
2. **Sell the put spread:** Sell an OTM put at approximately 0.15-0.20 [[delta]], buy a further OTM put 1-5 strikes below as protection.
3. **Sell the call spread:** Sell an OTM call at approximately 0.15-0.20 delta, buy a further OTM call 1-5 strikes above.
4. **Expiration:** 30-45 DTE for standard monthly cycles; 7-14 DTE for weekly SPY condors.
5. **Target credit:** Aim to collect at least 1/3 of the spread width as premium (e.g., $1.00 credit on $3-wide spreads).

### Exit
1. **Profit target:** Close the entire position when 50-75% of maximum profit is captured. Do not hold to expiration hoping for the last few cents.
2. **Stop-loss:** Close if the position reaches 1.5-2x the credit received in losses. Alternatively, close the tested side when the short strike is breached.
3. **Roll the tested side:** If the price approaches one short strike, buy back the threatened spread and sell a new one further out in time and/or price for a credit.
4. **Expiration management:** If holding into the final week, close any spread where the short strike is within 1-2% of the current price to avoid [[gamma]] risk and pin risk.

### Position Sizing
Risk no more than 2-5% of the account per condor. The max loss per condor is (spread width - credit received) x 100. Size positions so that losing on three consecutive condors does not materially damage the account.

## Indicators Used
- [[implied-volatility]] / IV rank -- enter when IV is elevated relative to its recent range
- [[delta]] -- guides short strike selection (0.15-0.20 delta targets ~70-80% probability OTM)
- [[bollinger-bands]] -- visually confirm that price is mean-reverting within a range
- [[atr]] -- validate that expected move is contained within the short strikes
- [[theta]] -- daily P&L from time decay; the engine of the strategy
- [[vega]] -- exposure to IV changes; a drop in IV after entry accelerates profits

## Example Trade
**Asset:** SPY trading at $520, 35 DTE, IV rank at 45
1. **Sell 1 SPY $500/$495 put spread** for $0.85 credit.
2. **Sell 1 SPY $540/$545 call spread** for $0.80 credit.
3. **Total credit:** $1.65 ($165 per condor). **Max loss:** $5.00 - $1.65 = $3.35 ($335).
4. **Break-even points:** $498.35 on the downside, $541.65 on the upside.
5. After 20 days, SPY has drifted from $520 to $525. Both spreads have decayed significantly. The condor can be closed for $0.50, locking in $1.15 profit (70% of max).
6. **Result:** +$115 per condor on $335 max risk = 34.3% return on risk in ~20 days.

## Performance Characteristics
- **Win Rate:** 70-85% when short strikes are set at 0.15-0.20 delta.
- **Profit Factor:** 1.2-1.8. High win rate offset by occasional max losses that erase several winners.
- **Best Market Conditions:** Low-volatility, range-bound markets with elevated IV rank. Post-[[vix]]-spike environments are ideal.
- **Worst Market Conditions:** Trending markets, sudden gaps (earnings, geopolitical events), and prolonged low-IV environments where premiums are too thin.
- **Key Metric:** Long-term profitability depends on average winner vs. average loser ratio. Mechanical management rules (50% profit target, 2x loss stop) are critical.

## Advantages
- **Defined risk:** Maximum loss is known at entry -- no margin calls or unlimited exposure
- **High probability of profit:** Short strikes with 0.15-0.20 delta have 70-85% chance of expiring OTM
- **Benefits from [[theta]] decay:** Profits accumulate daily as long as the price stays in range
- **Benefits from IV crush:** A drop in [[implied-volatility]] after entry accelerates the position's profit
- **Market-neutral:** No need to pick direction; only needs the underlying to stay within a range

## Disadvantages
- **Asymmetric risk/reward:** You risk $3-4 to make $1-2 per condor; one max loss erases 2-3 winners
- **[[gamma]] risk near expiration:** If the price is near a short strike in the final days, the position becomes extremely sensitive to small moves (Source: [[book-option-volatility-and-pricing]])
- **Requires active management:** Cannot simply set and forget; rolling, adjusting, and closing are frequent
- **Poor in trending markets:** A sustained directional move will breach one side and produce a max loss
- **Commission drag:** Four legs per trade means higher transaction costs, especially on weeklies

## Iron Condors in Long/Short Portfolios

The itpm methodology generally favors directional options strategies (long calls/puts) over premium-selling strategies like iron condors. However, iron condors may be used within a long-short-equity portfolio when:

- Markets are range-bound and the [[eighty-twenty-analysis|80/20 framework]] identifies low volatility conditions
- As a complement to directional positions to generate income during the 80% of time when markets lack sufficient volatility for directional trading

## See Also
- [[straddle-strangle]] -- the opposite thesis: buying volatility instead of selling it
- [[covered-call]] -- a simpler premium-selling strategy for stock owners
- [[implied-volatility]] -- understanding IV is essential for iron condor timing
- [[theta]] -- the primary profit mechanism for iron condors
- [[credit-spread]] -- the building block of the iron condor (each side is a credit spread)
- [[iron-condor-vs-iron-butterfly]] -- comparison of these two neutral premium-selling structures

## Sources
- [[book-option-volatility-and-pricing]] — Natenberg's treatment of multi-leg spreads, gamma risk near expiration, and the volatility risk premium that iron condors exploit
