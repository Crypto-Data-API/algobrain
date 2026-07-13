---
title: "Value Investing Strategy"
type: strategy
created: 2026-04-06
updated: 2026-04-07
status: good
tags: [value-investing, fundamental-analysis, contrarian, long-term, margin-of-safety, Buffett, Graham]
aliases: ["Value Investing", "Deep Value", "Contrarian Value Strategy"]
strategy_type: fundamental
timeframe: long-term
markets: [stocks]
complexity: intermediate
backtest_status: untested
related: ["[[growth-investing-strategy]]", "[[dividend-capture]]", "[[factor-investing]]", "[[sector-rotation]]", "[[earnings-momentum]]", "[[book-the-intelligent-investor]]", "[[book-security-analysis]]", "[[book-common-stocks-and-uncommon-profits]]"]
---

# Value Investing Strategy

## Overview

Value Investing is the practice of buying stocks that trade below their **intrinsic value** -- what the business is actually worth based on its assets, earnings, and cash flows (Source: [[book-security-analysis]]). The approach was pioneered by **Benjamin Graham** and **David Dodd** at Columbia Business School in the 1930s and refined by Graham's most famous student, **Warren Buffett**, into the dominant investment philosophy of the 20th century. The core idea is simple: buy dollar bills for fifty cents, then wait for the market to recognize the true value.

The strategy relies on the concept of a **margin of safety** -- the gap between the purchase price and intrinsic value (Source: [[book-the-intelligent-investor]]). This margin protects against errors in analysis and unexpected deterioration. Value investors use metrics like [[price-to-earnings|P/E ratio]], [[price-to-book|P/B ratio]], [[discounted-cash-flow|DCF analysis]], EV/EBITDA, and free cash flow yield to identify undervaluation. The approach is inherently **contrarian** -- you are buying what the market dislikes and selling what it loves. This requires patience and emotional discipline, as value stocks can remain cheap for years before re-rating.

## Rules

### Entry
1. **Screen for undervaluation:** Look for stocks trading below historical averages on P/E, P/B, EV/EBITDA, or free cash flow yield. Compare to sector peers. A P/E below 12-15 or P/B below 1.5 are common starting filters.
2. **Perform [[discounted-cash-flow|DCF analysis]]:** Build a conservative DCF model using below-average growth assumptions. If the DCF-derived intrinsic value is 30-50%+ above the current price, a margin of safety exists.
3. **Assess business quality:** Check for durable competitive advantages ([[economic-moat]]), consistent free cash flow generation, manageable debt levels (debt/equity below 0.5), and competent management with insider ownership.
4. **Wait for a catalyst (optional):** New management, activist investor involvement, spin-off, or cyclical recovery can unlock value. Pure deep-value investors buy without catalysts, trusting that cheapness alone will be rewarded.

### Exit
1. **Intrinsic value reached:** Sell when the stock price reaches or exceeds your estimate of fair value. Do not hold hoping for further upside beyond fair value.
2. **Thesis broken:** Exit immediately if the fundamental thesis deteriorates -- e.g., the competitive moat erodes, debt becomes unsustainable, or management makes value-destroying acquisitions.
3. **Better opportunity:** Sell to reallocate into a more undervalued stock with a wider margin of safety (opportunity cost rotation).
4. **Time stop:** If a stock has not moved toward fair value after 2-3 years with no fundamental improvement, consider exiting.

### Position Sizing
Concentrated portfolio of 10-20 positions. Top-conviction ideas at 8-12% of portfolio. Minimum position size 3%. Diversify across sectors but do not over-diversify into mediocre ideas.

## Indicators Used
- [[price-to-earnings|P/E ratio]] (trailing and forward) vs. historical and sector average
- [[price-to-book|P/B ratio]] -- especially relevant for financials and asset-heavy businesses
- [[discounted-cash-flow|DCF model]] with conservative assumptions
- EV/EBITDA -- enterprise value metric that accounts for debt
- Free cash flow yield (FCF/market cap) -- should exceed 6-8%
- Debt/equity ratio and interest coverage
- Return on invested capital (ROIC) -- prefer companies earning above their cost of capital

## Example Trade
**Asset:** Bank of America (BAC) during 2011-2012 recovery
1. In late 2011, BAC trades at $5.50 with a P/B ratio of 0.33 (tangible book value ~$13.50). The market fears ongoing mortgage litigation costs. P/E is depressed due to one-time charges.
2. Analysis: Estimate normalized earnings of $1.50-2.00/share once litigation resolves. At 10x normalized P/E, intrinsic value is $15-20. Margin of safety exceeds 60%.
3. Buy BAC at $5.50. Position size: 8% of portfolio. No stop-loss -- value investing accepts volatility in exchange for buying cheaply.
4. Over the next 3 years, mortgage fears subside, earnings normalize, and BAC re-rates. Sell at $17.00 in 2014.
5. **Result:** +$11.50 per share (209% gain). Dividends added another ~5%. Total holding period: ~3 years.

## Performance Characteristics
- **Win Rate:** 55-65% on a per-position basis over full holding periods.
- **Profit Factor:** 2.0-4.0. Winners are held for large gains; losers are cut when the thesis breaks.
- **Best Market Conditions:** Recoveries after market crashes (2009, 2020), periods of rising interest rates that favor financials and cyclicals, and markets where growth stocks have become overvalued.
- **Worst Market Conditions:** Extended growth-stock bull markets (2015-2020) where value underperforms for years. "Value traps" -- stocks that are cheap for good reasons and keep getting cheaper.
- **Benchmark Alpha:** Academic research (Fama-French) shows value stocks outperform growth by 3-5% annually over long periods, though with significant stretches of underperformance.

## Advantages
- Backed by the longest and most robust track record of any investment strategy (Graham/Buffett spanning 90+ years)
- Buying below intrinsic value provides a natural margin of safety against permanent capital loss
- Contrarian nature means buying when others are fearful, which is psychologically advantageous
- Lower turnover than most strategies, reducing transaction costs and tax drag
- Forces deep understanding of businesses and their economics

## Disadvantages
- **Value traps:** Cheap stocks can stay cheap or get cheaper if the business is genuinely deteriorating
- **Requires extreme patience** -- positions may underperform for 1-3 years before the thesis plays out
- Long periods of underperformance vs. growth strategies (the "value winter" of 2017-2020 tested even the most disciplined value investors)
- Fundamental analysis is subjective -- two analysts can derive very different intrinsic values from the same data
- Does not work well in speculative manias when fundamentals are temporarily irrelevant

## Sources

- [[book-the-intelligent-investor]] — Graham's definitive guide to value investing principles, margin of safety, and the Mr. Market allegory
- [[book-security-analysis]] — Graham & Dodd's rigorous framework for analyzing securities based on financial statements and intrinsic value
- [[book-common-stocks-and-uncommon-profits]] — Fisher's complementary approach emphasizing qualitative business analysis alongside quantitative value metrics

## See Also
- [[growth-investing-strategy]] -- the philosophical opposite that pays premium prices for growth
- [[factor-investing]] -- value is one of the core factors in multi-factor models
- [[earnings-momentum]] -- can complement value by timing entry around positive earnings surprises
- [[dividend-capture]] -- many value stocks also offer attractive dividend yields
- [[sector-rotation]] -- value sectors (financials, energy) are favored in early and late business cycle
