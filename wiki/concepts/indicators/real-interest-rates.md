---
title: "Real Interest Rates"
type: concept
created: 2026-04-14
updated: 2026-06-11
status: good
tags: [commodities, indicators, risk-management, gold]
aliases: ["Real Interest Rates", "Real Rates", "TIPS Yield", "real rate", "real yield"]
domain: [indicators]
prerequisites: ["[[interest-rates]]", "[[inflation]]"]
difficulty: intermediate
related: ["[[gold]]", "[[silver]]", "[[dxy-commodity-correlation]]", "[[commodity-inflation-link]]", "[[interest-rates]]", "[[inflation]]", "[[commodities]]"]
---

Real interest rates represent the return on fixed-income investments after adjusting for inflation. They are one of the most important macro drivers for [[gold]], [[silver]], and the broader [[commodities]] complex.

## Definition

The Fisher equation defines the relationship:

**Real rate = Nominal rate - Inflation**

In practice, the best market-based measure is the yield on **TIPS (Treasury Inflation-Protected Securities)**, specifically the 10-year TIPS yield. TIPS yields represent the market's expectation of real returns, incorporating both nominal rate expectations and inflation expectations (breakeven inflation).

- **Positive real rates**: investors earn a return above inflation by holding bonds — opportunity cost of holding non-yielding assets like [[gold]] is high
- **Negative real rates**: cash and bonds lose purchasing power after inflation — holding real assets becomes more attractive
- **Zero real rates**: the breakpoint where the cost of holding non-yielding assets is neutral

## Critical Driver for Gold and Precious Metals

The relationship between real rates and [[gold]] is one of the most reliable macro correlations in financial markets:

- **Rising real rates** → higher opportunity cost of holding non-yielding gold → gold falls
- **Falling/negative real rates** → gold rallies because holding cash loses purchasing power, making gold attractive as a store of value
- The correlation between the 10-year TIPS yield and gold prices has been approximately -0.7 to -0.85 over rolling 5-year windows since 2003

### Key Historical Episodes

- **2020-2021**: Deeply negative real rates (10-year TIPS yield fell to -1.1%) supported gold's move above $2,000. The [[federal-reserve|Fed]] cut rates to zero while [[inflation]] remained positive.
- **2022-2023**: Aggressive Fed hiking pushed real rates sharply positive (10-year TIPS yield rose to +2.5%). Despite strong geopolitical demand and central bank buying, gold was pressured for much of 2022.
- **2024-2025**: Even as real rates remained elevated, massive central bank buying (particularly by China, India, and emerging market central banks) overwhelmed the traditional real rate relationship, pushing gold to new all-time highs — a notable divergence from the historical pattern.

## Impact on Broader Commodity Complex

Real rates affect commodities beyond precious metals through several channels:

1. **Dollar channel**: Higher real rates strengthen the [[dxy-commodity-correlation|dollar]], which is a headwind for commodities priced in USD
2. **Inventory carrying costs**: Higher real rates increase the cost of financing physical commodity inventories, discouraging stockpiling and putting downward pressure on prices
3. **Discount rate effect**: Higher real rates increase the discount rate applied to future commodity production, reducing the present value of resource extraction projects
4. **Capital allocation**: Rising real rates pull capital toward fixed income and away from real assets, reducing speculative demand for [[commodities]]

## How to Track Real Rates

| Measure | Ticker / Source | Notes |
|---------|----------------|-------|
| 10-year TIPS yield | DFII10 on FRED, TIP ETF yield | Best single measure of real rates |
| 10-year breakeven inflation | T10YIE on FRED | Nominal Treasury yield minus TIPS yield |
| 5-year TIPS yield | DFII5 on FRED | Shorter-duration real rate measure |
| 5y5y forward breakeven | T5YIFR on FRED | Market's inflation expectation 5-10 years ahead |
| Real Fed Funds rate | Fed Funds rate minus trailing 12-month CPI | Current real policy rate |

## Practical Trading Application

- **Gold positioning**: when real rates are falling or deeply negative, maintain or increase [[gold]] allocation. When real rates are rising sharply, reduce gold exposure or hedge.
- **Regime identification**: a shift from positive to negative real rates (or vice versa) is a major regime change for precious metals and commodities generally.
- **Divergence signal**: if gold rallies despite rising real rates, non-rate factors (geopolitical demand, central bank buying, supply constraints) are dominating — the move may have structural support beyond the rate cycle.
- **Cross-asset**: real rates also drive [[growth-vs-value|growth vs value]] rotation in equities, making them a useful regime indicator beyond commodities.

## Sources

- (Source: [[2026-04-14-commodities-research-framework]])
- Federal Reserve Economic Data (FRED), series DFII10 / T10YIE / T5YIFR — official real-yield and breakeven-inflation data
- Fisher, I., *The Theory of Interest* (1930) — origin of the nominal-vs-real rate relationship
- U.S. Treasury, "Treasury Inflation-Protected Securities (TIPS)" — official documentation on the instrument used to read market real rates

## Related

- [[gold]]
- [[silver]]
- [[dxy-commodity-correlation]]
- [[commodity-inflation-link]]
- [[interest-rates]]
- [[inflation]]
- [[commodities]]
- [[federal-reserve]]
