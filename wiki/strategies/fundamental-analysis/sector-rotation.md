---
title: "Sector Rotation"
type: strategy
created: 2026-04-06
updated: 2026-04-07
status: good
tags: [sector-rotation, business-cycle, macro, fundamental-analysis, ETF, asset-allocation]
aliases: ["Business Cycle Investing", "Sector Cycling", "Stovall Sector Rotation"]
strategy_type: fundamental
timeframe: position
markets: [stocks]
complexity: intermediate
backtest_status: untested
related: ["[[value-investing-strategy]]", "[[growth-investing-strategy]]", "[[factor-investing]]", "[[trend-following-cta]]", "[[relative-strength]]", "[[book-how-to-make-money-in-stocks]]", "[[book-one-up-on-wall-street]]"]
---

# Sector Rotation

## Overview

Sector Rotation is a top-down [[fundamental-analysis]] strategy that shifts capital between equity sectors based on the current stage of the **business cycle**. Different sectors outperform at different phases of economic expansion and contraction, and by identifying the current phase, traders can overweight sectors poised to benefit and underweight those likely to lag. The framework was popularized by **Sam Stovall** of S&P Global and is used by institutional asset allocators worldwide.

The business cycle is typically divided into four stages: **Early Recovery** (coming out of recession), **Mid Expansion** (economy growing steadily), **Late Expansion** (economy overheating), and **Recession** (contraction). Each stage favors specific sectors due to shifting consumer behavior, interest rates, and corporate earnings trends. O'Neil's CANSLIM method emphasizes identifying leading industry groups as a key factor in stock selection (Source: [[book-how-to-make-money-in-stocks]]), while Lynch observed that understanding which sectors benefit from economic shifts is essential for finding growth opportunities (Source: [[book-one-up-on-wall-street]]). Implementation is straightforward using sector [[etf|ETFs]] like the SPDR Select Sector series (XLK, XLF, XLE, etc.).

## Rules

### Entry
1. **Identify the business cycle stage** using leading indicators: ISM Manufacturing PMI, yield curve shape, unemployment claims, [[fed-funds-rate]] trajectory, and Conference Board Leading Economic Index.
2. **Rotate into favored sectors:**
   - **Early Cycle:** [[consumer-discretionary]], [[financials]], [[real-estate]] -- consumers spend again, banks benefit from steepening yield curve.
   - **Mid Cycle:** [[technology]], [[industrials]], [[materials]] -- capex increases, business investment drives growth.
   - **Late Cycle:** [[energy]], [[materials]], [[healthcare]] -- commodity demand peaks, defensive positioning begins.
   - **Recession:** [[utilities]], [[healthcare]], [[consumer-staples]] -- defensive, dividend-paying sectors hold up best.
3. **Overweight 2-3 sectors** by allocating 60-70% of the portfolio to favored groups. Maintain 30-40% in broad market exposure.
4. Use [[relative-strength]] rankings to confirm: favored sectors should be showing improving relative performance vs. SPY.

### Exit
1. **Cycle transition:** When leading indicators signal the business cycle is moving to the next stage, begin rotating out of current holdings and into the next set of favored sectors.
2. **Relative weakness:** Exit a sector position if it drops below its 10-month moving average or shows deteriorating relative strength for 2+ consecutive months.
3. **Full defensive:** In confirmed recession, reduce overall equity exposure and concentrate in defensive sectors.

### Position Sizing
Allocate capital across 2-4 sector ETFs. No single sector should exceed 30% of total portfolio. Rebalance quarterly or when the cycle stage changes.

## Indicators Used
- ISM Manufacturing PMI and ISM Services PMI
- [[yield-curve]] shape (2s/10s spread)
- Unemployment claims (initial and continuing)
- [[fed-funds-rate]] direction and Fed policy stance
- Conference Board Leading Economic Index (LEI)
- Sector [[relative-strength]] vs. S&P 500

## Example Trade
**Scenario:** Economy transitioning from recession to early recovery (Q2 2020 analog)
1. Leading indicators turn: PMI rises above 50, unemployment claims peak and begin declining, the Fed is holding rates near zero, yield curve steepens.
2. Rotate into early-cycle sectors: Buy XLY (Consumer Discretionary) at $120, XLF (Financials) at $23, and XLRE (Real Estate) at $33. Allocate 25% each, with 25% in SPY.
3. Over the next 9 months, XLY rallies to $175 (+46%), XLF to $34 (+48%), XLRE to $42 (+27%).
4. PMI is now consistently above 55, capex is rising, and employment is strong -- signals mid-cycle. Rotate: sell XLY and XLRE, buy XLK (Technology) and XLI (Industrials).
5. **Result:** Portfolio gained ~38% during early-cycle phase vs. SPY's ~28%, generating significant alpha through sector selection.

## Performance Characteristics
- **Win Rate:** Not applicable in traditional sense -- measured by relative outperformance vs. benchmark.
- **Expected Alpha:** 2-5% annually over a full business cycle when rotation timing is reasonable.
- **Best Market Conditions:** Clear business cycle transitions with distinct economic phases. The 2009-2020 expansion provided multiple rotation opportunities.
- **Worst Market Conditions:** Unusual cycles (e.g., pandemic-driven), policy-distorted markets where normal sector relationships break down, or extended mid-cycle phases where rotation signals are ambiguous.
- **Holding Period:** 6-18 months per sector rotation, aligning with typical cycle stage duration.

## Advantages
- Grounded in well-established economic theory and decades of historical sector performance data
- Simple to implement using liquid sector ETFs with low expense ratios
- Forces a disciplined, macro-aware framework that prevents emotional trading
- Can be combined with [[factor-investing]] for enhanced returns (e.g., value factor in early cycle, momentum in mid cycle)

## Disadvantages
- **Cycle identification is difficult in real-time** -- leading indicators give mixed signals, and the NBER only dates recessions retroactively
- Rotation timing can be early or late by months, causing underperformance during transitions
- Does not work when sectors decouple from traditional business cycle patterns (e.g., tech dominance 2017-2024)
- Transaction costs and tax implications from quarterly rebalancing can erode returns
- Requires macro-economic literacy that goes beyond pure [[technical-analysis]]

## Sources

- [[book-how-to-make-money-in-stocks]] — O'Neil's emphasis on leading industry groups and the "L" factor in CANSLIM
- [[book-one-up-on-wall-street]] — Lynch's insights on sector and industry awareness in stock selection

## See Also
- [[factor-investing]] -- quantitative approach to systematic factor exposure that complements rotation
- [[value-investing-strategy]] -- often outperforms in early-cycle recoveries
- [[growth-investing-strategy]] -- typically dominates mid-cycle expansion phases
- [[trend-following-cta]] -- captures macro trends across asset classes, not just equities
- [[relative-strength]] -- key tool for confirming sector rotation signals
- [[sector-momentum-screen]] -- screening for sector momentum signals to inform rotation timing
