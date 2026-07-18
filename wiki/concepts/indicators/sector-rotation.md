---
title: "Sector Rotation"
type: concept
created: 2026-04-14
updated: 2026-06-11
status: good
tags: [technical-analysis, indicators, portfolio-theory]
aliases: ["Sector Rotation", "Business Cycle Rotation", "Sector Rotation Model"]
domain: [indicators, portfolio-theory]
prerequisites: ["[[intermarket-analysis]]", "[[technical-analysis-overview]]"]
difficulty: intermediate
related: ["[[intermarket-analysis]]", "[[john-murphy]]", "[[technical-analysis-of-the-financial-markets]]", "[[commodity-inflation-link]]", "[[real-interest-rates]]", "[[dxy-commodity-correlation]]", "[[commodities]]", "[[global-macro]]"]
---

Sector rotation is the pattern of capital flowing between stock market sectors as the economy moves through different phases of the business cycle. [[john-murphy]] integrated sector rotation into his [[intermarket-analysis]] framework, showing how the relationship between bonds, commodities, and the dollar predicts which sectors will outperform. While the concept is widely attributed to Sam Stovall of S&P Global, Murphy's contribution was connecting sector rotation to intermarket signals -- making it a technical, not just fundamental, framework. (Source: [[book-technical-analysis-of-the-financial-markets]])

> **Note:** This page covers sector rotation as a **concept** within intermarket analysis. For the implementable **strategy** with entry/exit rules, position sizing, and backtesting, see [[sector-rotation|Sector Rotation Strategy]].

## The Business Cycle Model

The business cycle creates a predictable (though not perfectly timed) sequence of sector leadership. Each phase favors sectors that benefit from the prevailing economic conditions:

### Early Recovery

**Macro conditions:** Bonds rising (yields falling), stocks bottoming, commodities bottoming. The Fed is at or near peak accommodation. Unemployment is high but peaking. Credit conditions are easing.

**Leading sectors:** Financials, consumer discretionary, technology. Interest-rate-sensitive sectors benefit most from falling rates. Banks see their yield curve steepen (borrowing short, lending long). Consumer discretionary benefits from pent-up demand and improving confidence. Technology benefits from lower discount rates on future earnings.

**Intermarket signal:** Bond prices rallying while stocks are still near lows. The bond-stock lead/lag is at its most visible here.

### Mid Expansion

**Macro conditions:** Stocks rising broadly, bonds flat to slightly declining, commodities beginning to rise. Employment is growing. Consumer and business confidence is strong. Capex is increasing.

**Leading sectors:** Industrials, materials, technology continue. Broad market strength -- most sectors participate. This is the easiest environment for equity investors.

**Intermarket signal:** Stocks rising on expanding breadth. Commodities beginning to firm but not yet surging.

### Late Expansion

**Macro conditions:** Commodities rising sharply, bonds falling (yields rising), stocks peaking or rising on narrowing breadth. Inflation is picking up. The Fed is tightening or preparing to tighten. Wages are rising. Input costs are squeezing margins.

**Leading sectors:** Energy, materials, commodity stocks. These sectors benefit directly from rising commodity prices. [[crude-oil]] stocks and mining equities outperform. Inflation beneficiaries lead while the broad market shows fatigue.

**Intermarket signal:** The CRB Index or commodity sub-indices breaking to new highs while bond prices are making new lows. This is Murphy's classic inflationary signal from the [[intermarket-analysis|intermarket chain]].

### Early Recession

**Macro conditions:** Commodities peaking and falling, bonds bottoming and rising, stocks falling. Corporate earnings are contracting. Layoffs are beginning. The Fed is shifting toward easing.

**Leading sectors:** Utilities, healthcare, consumer staples (defensives). These sectors provide stable dividends, inelastic demand, and relative safety. [[gold]] often rallies as a safe haven and inflation hedge.

**Intermarket signal:** Commodity prices rolling over and bond prices bottoming -- the deflation signal. Stocks have not yet bottomed.

### Full Recession

**Macro conditions:** Stocks falling, commodities falling, bonds rising. Economic contraction is broad-based. Fear dominates.

**Favored positions:** Cash, bonds, [[gold]]. Risk-off. This phase sets up the next early recovery.

## Murphy's Intermarket Rotation Indicators

Murphy developed several practical indicators for identifying the current phase:

### Commodity Stocks vs. Technology Stocks

The relative performance of commodity-related stocks (energy, materials, mining) versus technology stocks is Murphy's preferred cycle indicator:

- **Commodity stocks outperforming technology** = late cycle, inflationary, lean toward energy/materials
- **Technology outperforming commodity stocks** = early/mid cycle, disinflationary, lean toward growth sectors

This single ratio captures the inflation/deflation dynamic that drives the entire intermarket chain.

### Bond-Stock Relative Performance

When bonds are outperforming stocks (TLT/SPY rising), the market is signaling a shift toward defensive/recessionary positioning. When stocks outperform bonds, risk-on conditions favor cyclical sectors.

### Dollar Direction

A falling dollar supports commodity sectors and emerging markets. A rising dollar supports domestically-focused sectors like technology and healthcare. The [[dxy-commodity-correlation]] provides the transmission mechanism.

## Practical Tools for Sector Rotation Analysis

### Relative Strength Ratio Charts

Plot sector ETF divided by SPY (e.g., XLE/SPY, XLK/SPY) to see which sectors are gaining or losing relative strength. A rising RS ratio means the sector is outperforming the broad market. Murphy emphasizes that relative strength trends are as important as absolute price trends.

### Relative Rotation Graphs (RRG)

Developed by Julius de Kempenaer, RRGs plot sectors on a four-quadrant chart:

- **Leading** (upper right): Outperforming and momentum improving
- **Weakening** (lower right): Still outperforming but momentum fading
- **Lagging** (lower left): Underperforming and momentum deteriorating
- **Improving** (upper left): Still underperforming but momentum turning up

Sectors rotate clockwise through these quadrants, providing a visual representation of the sector rotation cycle. StockCharts.com (where Murphy served as Chief Technical Analyst) offers RRG tools.

### Sector ETF Pairs

Monitor key pairs that reflect the cycle:

| Pair | Rising Ratio Means |
|------|-------------------|
| XLE/XLK (Energy vs. Tech) | Late cycle, inflationary |
| XLF/XLU (Financials vs. Utilities) | Early cycle, risk-on |
| XLY/XLP (Discretionary vs. Staples) | Expansion, consumer confidence |
| XLB/XLK (Materials vs. Tech) | Commodity demand, inflationary |

## Limitations

The business cycle model is an idealized framework. In practice:

- **Cycles vary in length and intensity**: The 2009-2020 expansion lasted 128 months, far longer than historical averages. Mid-cycle corrections and policy interventions create false rotation signals.
- **Central bank intervention can extend or compress phases**: QE prolonged the mid-expansion phase for years, suppressing the normal late-cycle commodity surge. This distorted Murphy's intermarket signals.
- **Sector definitions change over time**: "Technology" in 2000 (Cisco, Sun Microsystems, AOL) is fundamentally different from "technology" in 2024 (Apple, Microsoft, Nvidia). GICS reclassifications (e.g., Meta and Google moving to Communication Services) affect historical comparisons.
- **Global factors override domestic cycle positioning**: A US early-cycle recovery can be overwhelmed by a Chinese slowdown, European sovereign crisis, or global pandemic.
- **Crowding**: Sector rotation is a well-known framework. When too many participants rotate simultaneously, the expected leaders can become crowded and underperform.

## Related

- [[intermarket-analysis]] -- the broader cross-asset framework that drives sector rotation signals
- [[john-murphy]] -- integrated sector rotation into intermarket analysis
- [[technical-analysis-of-the-financial-markets]] -- covers sector rotation in the intermarket chapters
- [[commodity-inflation-link]] -- the inflation signal that triggers late-cycle rotation
- [[real-interest-rates]] -- the rate environment that drives early-cycle sector leadership
- [[dxy-commodity-correlation]] -- dollar movements that affect sector performance
- [[relative-strength]] -- the primary tool for measuring sector leadership
- [[commodities]] -- the asset class whose price behavior signals cycle transitions
- [[global-macro]] -- the broader macro approach that incorporates sector rotation

## Sources

- (Source: [[book-technical-analysis-of-the-financial-markets]]) -- Claim #10: intermarket relationships between bonds, currencies, commodities, and stocks
