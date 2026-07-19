---
title: "Intermarket Analysis"
type: concept
created: 2026-04-14
updated: 2026-06-11
status: good
tags: [technical-analysis, indicators, commodities, portfolio-theory]
aliases: ["Intermarket Analysis", "Intermarket Technical Analysis", "Cross-Asset Analysis"]
domain: [indicators, portfolio-theory]
prerequisites: ["[[indicators-ta-primer]]", "[[commodities]]", "[[futures-overview]]"]
difficulty: advanced
related: ["[[john-murphy]]", "[[technical-analysis-of-the-financial-markets]]", "[[cross-asset-signals]]", "[[dxy-commodity-correlation]]", "[[commodity-inflation-link]]", "[[real-interest-rates]]", "[[sector-rotation]]", "[[commodities]]", "[[gold]]", "[[crude-oil]]", "[[global-macro]]", "[[trend-following-cta]]"]
---

Intermarket analysis is the study of relationships between asset classes -- stocks, bonds, commodities, and currencies -- to gain broader market context that single-market analysis misses. Pioneered by [[john-murphy]] in *Intermarket Technical Analysis* (1991), it shows that no market moves in isolation. Murphy's framework is the foundation for macro-technical trading and remains a core component of institutional cross-asset research. (Source: [[book-technical-analysis-of-the-financial-markets]])

## Murphy's Four-Market Framework

Murphy's central thesis is that the four major asset classes -- bonds, stocks, commodities, and currencies -- are linked through economic forces (inflation, interest rates, growth) and that these relationships produce tradeable signals. (Source: [[book-technical-analysis-of-the-financial-markets]])

### Bonds and Stocks

Bond prices (inverse of yields) tend to lead stock prices. Falling bond prices (rising yields) eventually pressure stocks as borrowing costs rise, corporate profit margins compress, and the discount rate for future earnings increases. Rising bond prices (falling yields) support stocks by easing financial conditions. The bond market typically turns 3-6 months before the stock market, making it a leading indicator for equity investors.

Key relationship: When the [[yield-curve]] inverts (short-term rates exceed long-term rates), it has historically preceded recessions and bear markets with a 12-18 month lead time.

### Dollar and Commodities

The US dollar has a historically inverse relationship with [[commodities]], especially [[gold]] and [[crude-oil]]. Because most commodities are priced in USD, a falling dollar makes them cheaper for foreign buyers, increasing demand and supporting prices. A rising dollar has the opposite effect. The [[dxy-commodity-correlation]] typically ranges from -0.3 to -0.6, with gold showing the strongest inverse correlation. (Source: [[book-technical-analysis-of-the-financial-markets]])

### Commodities and Bonds

Rising commodity prices signal [[commodity-inflation-link|inflation]], which is bearish for bonds (bond prices fall when inflation expectations rise, as investors demand higher yields). Falling commodity prices signal disinflation or deflation, which supports bonds. The CRB Index (now Refinitiv/CoreCommodity CRB) is Murphy's preferred gauge for tracking this relationship. When commodity prices break out, watch for bond prices to follow with a decline.

### The Intermarket Chain

Murphy's relationships connect into a causal chain:

**Inflationary sequence:** Dollar down -> commodities up -> inflation up -> bonds down -> (eventually) stocks down

**Deflationary sequence:** Dollar up -> commodities down -> deflation -> bonds up -> stocks up

This chain does not move simultaneously -- each link has a lead/lag relationship, creating windows where one asset class has already turned while another has not. These divergences are the primary trading signals in intermarket analysis.

## Sector Rotation and the Business Cycle

Murphy extended intermarket analysis to show that different equity sectors lead at different stages of the economic cycle. The intermarket chain determines where the economy sits in the cycle, which in turn predicts [[sector-rotation]]:

- **Late expansion / inflationary phase** (commodities rising, bonds falling): Energy, materials, and commodity stocks lead. [[crude-oil]] stocks and mining equities outperform.
- **Early recession** (commodities peaking, bonds bottoming): Utilities, healthcare, and consumer staples (defensives) outperform. [[gold]] often rallies.
- **Early recovery** (bonds rising, stocks bottoming): Financials, technology, and consumer discretionary lead. Interest-rate-sensitive sectors benefit from falling rates.
- **Mid expansion** (stocks rising, broad participation): Industrials, technology, and broad market strength. The sweet spot for equity bulls.

Murphy uses the relative performance of commodity stocks versus technology stocks as a real-time cycle indicator. When commodity stocks outperform, it signals late-cycle/inflationary conditions. When technology outperforms, it signals early/mid-cycle disinflationary conditions. (Source: [[book-technical-analysis-of-the-financial-markets]])

## Post-2008 Modifications

Murphy's original framework was built during a period of relatively normal correlation regimes (1970s-2000s). After 2008, central bank intervention fundamentally altered several key relationships:

- **Quantitative easing (QE)**: Massive bond purchases suppressed yields regardless of commodity prices or inflation, breaking the commodity-bond link for extended periods.
- **ZIRP/NIRP**: Zero and negative interest rate policies compressed the bond-stock lead/lag, as the "discount rate" channel was artificially anchored.
- **Dollar-stock positive correlation**: During risk-on/risk-off regimes (2010-2013, 2020), the dollar and stocks sometimes moved together (both up in risk-on as capital flowed to US assets), defying Murphy's framework.
- **Crypto as a new asset class**: [[bitcoin]] and digital assets introduced a fifth major asset class that sometimes behaves like a risk asset (correlated with tech stocks) and sometimes like digital gold (correlated with inflation hedges).

Modern practitioners adjust Murphy's framework by treating central bank policy as an overriding factor that can suspend normal intermarket relationships, monitoring correlation regime shifts (and noting when correlations revert to historical norms), and incorporating crypto and alternative assets into the cross-asset picture.

## Practical Application

### The Four-Chart Overlay

Overlay the following on the same chart or dashboard:

1. **DXY** (US Dollar Index) -- currency
2. **TLT** or **10-Year Treasury yield** -- bonds
3. **CRB Index** (or GSCI, or BCOM) -- commodities
4. **SPX** (S&P 500) -- equities

### Signal Interpretation

- **All four confirm the same direction per Murphy's chain**: High-conviction signal. Example: dollar falling, commodities rising, bonds falling, stocks still rising but showing fatigue = late-cycle warning.
- **Divergence between links**: Caution signal. Example: commodities rising but bonds also rising = potential regime change or central bank distortion.
- **Complete breakdown of relationships**: Typically occurs during central bank policy shifts, financial crises, or regime transitions. Step aside until relationships re-establish.

### Timeframe

Intermarket analysis is primarily a weekly/monthly-chart discipline. The lead/lag relationships between asset classes unfold over weeks to months, not days. Murphy recommends using intermarket signals to set the macro context, then applying single-market [[indicators-ta-primer|technical analysis]] for timing within that context.

## Criticism

- The framework is inherently backward-looking -- intermarket relationships are identified from historical data and may not persist
- Correlation regimes shift, sometimes for years (see post-2008 discussion)
- The causal chain is an oversimplification of complex, multi-variable economic dynamics
- Timing the lead/lag between asset classes is extremely difficult in real-time
- Murphy's original work focused on US markets; global intermarket dynamics add additional layers of complexity

## Related

- [[john-murphy]] -- creator of the intermarket analysis framework
- [[technical-analysis-of-the-financial-markets]] -- Murphy's comprehensive TA textbook
- [[sector-rotation]] -- applying intermarket signals to equity sector selection
- [[dow-theory]] -- the foundational framework that Murphy built upon
- [[dxy-commodity-correlation]] -- the dollar-commodity inverse relationship in detail
- [[commodity-inflation-link]] -- commodities as inflation signal and hedge
- [[real-interest-rates]] -- the key macro variable linking bonds, gold, and commodities
- [[global-macro]] -- the broader macro trading approach that uses intermarket analysis
- [[trend-following-cta]] -- systematic approach that often exploits intermarket trends
- [[cross-asset-signals]] -- practical implementation of cross-asset trading signals

## Sources

- (Source: [[book-technical-analysis-of-the-financial-markets]]) -- Claim #10: bonds, currencies, commodities, and stocks are interconnected
