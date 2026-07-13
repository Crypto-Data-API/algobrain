---
title: "US Treasury Bonds"
type: market
created: 2026-04-07
updated: 2026-04-07
status: good
tags: [bonds, macro-trading, fixed-income]
aliases: ["Treasuries", "US Treasuries", "T-Bonds"]
related: ["[[yield-curve]]", "[[bonds-overview]]", "[[macro-trading]]", "[[federal-reserve]]", "[[interest-rates]]"]
---

US Treasury securities are debt obligations issued by the United States Department of the Treasury to fund government spending. Backed by the "full faith and credit" of the US government, they are considered the benchmark "risk-free" asset in global finance and serve as the foundation for pricing virtually all other fixed income securities.

## Types of Treasury Securities

| Security | Maturity | Coupon | Auction Frequency |
|---|---|---|---|
| **T-Bills** | 4, 8, 13, 17, 26, 52 weeks | Zero-coupon (sold at discount) | Weekly |
| **T-Notes** | 2, 3, 5, 7, 10 years | Semi-annual fixed coupon | Monthly |
| **T-Bonds** | 20, 30 years | Semi-annual fixed coupon | Monthly |
| **TIPS** | 5, 10, 30 years | Semi-annual (inflation-adjusted) | Quarterly |
| **I-Bonds** | 30 years (redeemable after 1yr) | Fixed + inflation component | Continuous |

## Key Characteristics

### Inverse Price-Yield Relationship
When interest rates rise, existing bond prices fall (and vice versa). The sensitivity of a bond's price to rate changes is measured by **duration**:
- A 30-year bond has much higher duration (~20 years) than a 2-year note (~2 years)
- If rates rise 1%, a bond with duration 20 loses approximately 20% of its value
- This makes long-duration Treasuries highly sensitive to [[federal-reserve|Federal Reserve]] policy and [[inflation]] expectations

### Flight to Safety
During market crises, investors sell risk assets and buy Treasuries, driving yields down and prices up. This "flight to quality" was evident during:
- The 2008 financial crisis (10-year yield fell from 4% to below 2%)
- The March 2020 COVID crash (10-year yield fell to 0.5%)
- Multiple [[stock-market-crash|stock market]] corrections

### Role as Risk-Free Rate
The Treasury yield serves as the baseline for the [[sharpe-ratio|Sharpe Ratio]], [[capital-asset-pricing-model|CAPM]], and virtually all risk-adjusted return calculations. The "risk-free rate" in finance almost always refers to the relevant maturity Treasury yield.

## Trading Treasuries

### Direct Trading
- Treasury futures (ZB, ZN, ZF, ZT) traded on the CME are the most liquid [[futures]] contracts in the world
- Cash Treasuries trade in the over-the-counter (OTC) market with dealers

### ETFs
| ETF | Duration | Exposure |
|---|---|---|
| **SHY** | Short (1-3yr) | Short-term notes |
| **IEF** | Intermediate (7-10yr) | Medium-term notes |
| **TLT** | Long (20+yr) | Long-term bonds |
| **TIP** | Various | Inflation-protected |
| **TMF** | Long (3x leveraged) | Leveraged long-term bonds |

### Common Strategies
- **Duration trading**: Going long/short different maturities based on rate expectations
- **[[yield-curve]] trades**: Steepening/flattening bets on the shape of the curve
- **Risk parity**: Balancing Treasury allocation against equities to equalize risk contribution ([[risk-parity]])
- **Carry trades**: Exploiting the yield differential between Treasuries and other bonds or currencies
- **Hedging**: Using Treasuries to hedge equity portfolio [[tail-risk|tail risk]]

## Market Size and Significance

The US Treasury market is the largest and most liquid securities market in the world:
- **Outstanding debt**: Over $30 trillion
- **Daily trading volume**: Over $700 billion
- **Global reserve asset**: Central banks worldwide hold Treasuries as foreign exchange reserves
- **Benchmark**: Corporate bond spreads, mortgage rates, and other lending rates are quoted as a spread over Treasury yields

## Related

- [[yield-curve]] -- The term structure of Treasury yields across maturities
- [[bonds-overview]] -- Broader fixed income market overview
- [[federal-reserve]] -- The primary driver of short-term Treasury yields
- [[macro-trading]] -- Strategies based on macroeconomic views including rate expectations

## Sources

- US Treasury market fundamentals are documented across fixed income textbooks and Federal Reserve publications
