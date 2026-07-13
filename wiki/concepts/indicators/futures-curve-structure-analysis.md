---
title: "Futures Curve Structure Analysis"
type: concept
created: 2026-04-14
updated: 2026-06-21
status: excellent
tags: [commodities, futures, indicators]
aliases: ["Term Structure Analysis", "Futures Curve Analysis", "Curve Structure", "Forward Curve Analysis"]
domain: [indicators]
difficulty: advanced
prerequisites: ["[[contango]]", "[[backwardation]]", "[[roll-yield]]", "[[convenience-yield]]"]
related: ["[[contango]]", "[[backwardation]]", "[[roll-yield]]", "[[convenience-yield]]", "[[cost-of-carry]]", "[[storage-economics]]", "[[commodity-carry-strategy]]", "[[calendar-spread-arbitrage]]", "[[commodities]]"]
---

# Futures Curve Structure Analysis

How to read and interpret the entire commodity futures curve -- not just the front-month price, but the full term structure of prices across all listed expiration months. The shape of the futures curve encodes the market's collective assessment of future [[supply-demand-balance]], [[storage-economics]], [[convenience-yield]], risk premiums, and seasonal patterns. For commodity traders, curve structure is often more informative than outright price level -- a commodity at $100 in steep [[backwardation]] tells a fundamentally different story than the same commodity at $100 in steep [[contango]] (Source: [[2026-04-14-commodities-research-framework]]).

## Overview

A commodity futures curve plots the prices of futures contracts with different expiration dates, from the nearest month out to the longest-dated contract (which can be 1-5+ years forward depending on the commodity). The curve shape reflects the net balance of several forces:

1. **Storage cost** (upward pressure on deferred months): Holders of physical inventory must pay for storage, insurance, and financing. This pushes deferred prices above spot/near-month (all else equal).
2. **[[convenience-yield]]** (downward pressure on deferred months): Holding physical commodity provides optionality value (ability to meet unexpected demand, keep a refinery running). This pushes deferred prices below spot/near-month.
3. **Risk premium / [[hedging-pressure]]**: Producer hedging depresses deferred prices; consumer hedging supports them.
4. **Market expectations**: If the market expects a future surplus, deferred prices may be lower than near-month. If the market expects a future deficit, deferred prices may be higher.
5. **Seasonal patterns**: Agricultural and energy commodities have predictable seasonal supply/demand cycles that create seasonal curve shapes (Source: [[2026-04-14-commodities-research-framework]]).

## Quick-Reference: Curve Shape Decision Table

The fastest way to read a curve is to classify its shape, then map it to inventory state, [[roll-yield]] sign, and the trade it favors. The table below is the at-a-glance summary; each row is expanded in the sections that follow.

| Curve Shape | Front vs. Deferred | Inventory State | [[convenience-yield]] | [[roll-yield]] (long) | Typical Fundamental | Trade Bias |
|-------------|--------------------|-----------------|------------------------|------------------------|----------------------|------------|
| Full [[backwardation]] | Front > all deferred | Low / drawing | High | Positive (earn carry) | Acute tightness, supply shock | Long front, [[commodity-carry-strategy]] long |
| Full [[contango]] | Front < all deferred | High / building | Low | Negative (pay carry) | Surplus, weak demand | Short / spread, avoid passive long |
| Flat | Front ≈ deferred | Balanced | ≈ storage cost | ≈ 0 | Equilibrium | Neutral, fundamental-driven |
| Kinked (near bwd, far cont) | Front > 2nd, far rises | Temporary draw | Elevated near | Positive near only | Transient disruption | Long near / short deferred spread |
| Inverted kink (near cont, far bwd) | Front < 2nd, far falls | Surplus now, deficit later | Low near, rising far | Negative near | Expected future tightness | Long deferred / short near spread |
| "Super-contango" | Steep front < deferred, > full-carry | Storage near capacity | ~Zero | Strongly negative | Glut, storage scarce | Cash-and-carry storage play |

A practical shorthand: **backwardation = market is willing to pay up for it NOW** (tight); **contango = market would rather have it LATER** (loose). The steeper the slope in either direction, the stronger the signal.

## Curve Shapes and Their Meanings

### Full Backwardation (Front > Deferred Across All Tenors)
- **What it means**: Acute near-term supply tightness. The market values physical commodity today more than in the future.
- **Fundamental backdrop**: Low inventories, strong current demand, supply disruption (war, sanctions, weather), low [[convenience-yield]] threshold breached.
- **Trading implication**: Bullish for spot/near-month. Long positions earn positive [[roll-yield]] (selling expensive near-month, rolling into cheaper deferred). Favors [[commodity-carry-strategy]] longs.
- **Examples**: Crude oil during OPEC supply cuts (2022), wheat during the Russia-Ukraine war (2022), copper during Chinese demand surges.

### Full Contango (Front < Deferred Across All Tenors)
- **What it means**: Near-term oversupply. Storage costs dominate the curve because there is ample physical supply.
- **Fundamental backdrop**: High inventories, weak demand, supply surplus. Physical commodity is readily available, so [[convenience-yield]] is low and storage cost is the dominant factor.
- **Trading implication**: Bearish for spot. Long positions suffer negative [[roll-yield]] (buying cheap near-month, rolling into more expensive deferred). Passive commodity index funds ([[commodity-index-rebalancing]]) bleed returns. Favors short positions or spread trades.
- **Examples**: Crude oil in 2015-2016 (shale oversupply), natural gas in mild winters, base metals during global recession.

### Super-Contango (Steeper Than Full Carry)
- **What it means**: A contango so steep that the front-to-deferred spread *exceeds* the full economic [[cost-of-carry]] (storage + insurance + financing). This signals that physical storage capacity is becoming scarce -- producers are paying anyone with a tank to take the commodity.
- **Fundamental backdrop**: Extreme oversupply colliding with finite storage. The classic case is the **April 2020 WTI crude collapse**, when the May contract settled at **-$37.63/bbl** (negative) because Cushing storage was nearly full and longs holding expiring contracts had nowhere to take delivery.
- **Trading implication**: Opens a textbook **cash-and-carry**: buy spot, pay to store, sell the rich deferred contract, lock in a near-riskless spread if you control storage. For traders without storage access it is a warning, not an opportunity -- being long a front contract into a super-contango squeeze is how accounts get destroyed.

### Flat Curve
- **What it means**: Balanced market. Storage costs roughly offset [[convenience-yield]], and the market does not see significant future supply/demand shifts.
- **Trading implication**: Neutral. Low [[roll-yield]] (positive or negative). Spread trades have less opportunity. Outright directional views depend on fundamental analysis rather than curve signals.

### Kinked Curve (Backwardation in Near Months, Contango in Deferred)
- **What it means**: Short-term tightness that the market expects to resolve. Near-term supply disruption (maintenance, weather, logistics) but the market expects supply to recover and inventories to rebuild in the medium term.
- **Trading implication**: Favors long near-month / short deferred calendar spreads. The near-term premium may persist until the disruption resolves.
- **Examples**: Seasonal refinery maintenance in crude oil (tight products now, expected recovery when refineries restart).

### Inverted Kink (Contango Near, Backwardation Deferred)
- **What it means**: Near-term surplus but expected future tightness. The market is well-supplied now but sees a deficit developing (e.g., due to expected [[capex-cycle]] impacts, regulatory changes, or demand growth).
- **Trading implication**: Favors long deferred / short near calendar spreads. This shape is relatively rare (Source: [[2026-04-14-commodities-research-framework]]).

## Key Metrics

### Front-to-Second Spread
The price difference between the nearest and second-nearest futures contracts. This is the most liquid and tightly traded spread for each commodity.
- **Calculation**: Front Month Price - Second Month Price
- **Positive** = backwardation (near-month is more expensive)
- **Negative** = contango (near-month is cheaper)
- **Annualized**: (Spread / Second Month Price) x (12 / months between contracts)

### Calendar Spread
The price difference between any two contract months. Common pairs: front-second, front-deferred (6 months out), seasonal (e.g., December-March for heating oil).

### Time Spread Curve Shape
Plotting all calendar spreads gives the "shape" of the curve -- concave, convex, flat, kinked. Changes in shape often precede changes in outright price.

### Roll Yield (Annualized)
The return earned (or lost) from rolling a futures position from near-month to the next contract:
- **[[roll-yield]] = (Near Month - Deferred) / Deferred x (12 / months between contracts)**
- Positive roll yield = backwardation = long positions earn carry
- Negative roll yield = contango = long positions pay carry

| Annualized Roll Yield | Curve Implication | Effect on Passive Long | Strategy Reading |
|------------------------|-------------------|------------------------|-------------------|
| > +10% | Steep [[backwardation]] | Strong tailwind | High-conviction carry long |
| +2% to +10% | Mild backwardation | Modest tailwind | Carry-favorable |
| -2% to +2% | Flat | Negligible | Carry-neutral |
| -2% to -10% | Mild [[contango]] | Headwind; index bleed | Avoid passive long |
| < -10% | Steep contango | Severe drag | Storage / short bias |

The total return of an unleveraged commodity futures position decomposes into **spot return + roll yield + collateral yield**. Over long horizons, roll yield has historically explained the majority of the *dispersion* in commodity index returns -- which is why curve shape, not spot direction, is the dominant driver of [[commodity-index-rebalancing]] performance.

### Curve Slope (Term Structure Momentum)
The change in curve shape over time. If the curve is flattening from contango toward backwardation, the market is tightening even if outright prices haven't moved yet. Curve slope momentum can be a leading indicator for price (Source: [[2026-04-14-commodities-research-framework]]).

## Analytical Applications

### 1. Curve Shape as a Trading Signal
Research shows that curve shape (specifically, [[roll-yield]]) is a significant predictor of subsequent commodity returns. The [[commodity-carry-strategy]] formalizes this: long backwardated commodities, short contango commodities.

### 2. Curve Shape Change as a Leading Indicator
Changes in curve shape often lead outright price moves by days to weeks. A shift from contango to backwardation (steepening of near-month premium) signals tightening fundamentals before the outright price fully reflects it. Monitoring the first derivative of curve shape (is the curve getting more backwardated or more contango?) can provide early entry signals.

### 3. Seasonal Curve Patterns
Many commodities have predictable seasonal curve shapes:
- **Natural gas**: Typically contango in summer (storage injection season), backwardated or flat in winter (heating demand).
- **Gasoline**: Backwardated heading into summer driving season.
- **Grains**: Curve reflects planting and harvest cycles (tight pre-harvest, loose post-harvest).

### 4. Curve Shape and Inventory
Curve shape is highly correlated with inventory levels (the "convenience yield" channel):
- **Low inventories** → high [[convenience-yield]] → steep [[backwardation]]
- **High inventories** → low [[convenience-yield]] → steep [[contango]]
- Tracking the relationship between curve shape and reported inventories can identify when the curve is "mispriced" relative to fundamentals.

### 5. Spread Trading
Instead of taking outright directional positions, traders can express views through calendar spreads (long one contract month, short another). This isolates the curve shape view from the directional price view, reducing risk. See [[calendar-spread-arbitrage]] (Source: [[2026-04-14-commodities-research-framework]]).

## Reading the Curve: Practical Guide

### Step 1: Pull the Full Curve
Use exchange data (CME, ICE, LME) or a terminal (Bloomberg, Refinitiv) to display all listed contract months and their settlement prices.

### Step 2: Classify the Shape
Is it backwardated, contango, flat, or kinked? Compare to the same curve 1 week, 1 month, and 3 months ago. Is the shape changing?

### Step 3: Compute Key Spreads
Calculate front-second spread, 1-year spread (front vs. 12 months deferred), and the annualized roll yield.

### Step 4: Compare to Inventory
Overlay the curve shape (or front-second spread) with reported inventory data. Are they telling the same story? If inventories are drawing but the curve is in contango, something is disconnected -- investigate.

### Step 5: Check Seasonal Context
Is the current curve shape consistent with the seasonal pattern? If natural gas is in backwardation during summer injection season, something unusual is happening (bullish).

### Step 6: Identify Trade Opportunities
- **Curve mispriced vs. fundamentals**: Take a spread position to capture the expected correction.
- **Curve shape change**: Position for continued change (momentum) or reversion.
- **Carry**: Harvest positive roll yield from backwardated positions.

## Worked Example (Qualitative)

Suppose a crude oil trader pulls the WTI curve and sees the following stylized settlements:

| Contract | Price ($/bbl) |
|----------|---------------|
| Front month (M1) | 84.00 |
| M2 | 83.20 |
| M3 | 82.60 |
| 6-month deferred | 81.00 |
| 12-month deferred | 79.50 |

**Step 1 -- Classify the shape.** Front > all deferred, declining monotonically: this is **[[backwardation]]**.

**Step 2 -- Compute the key spreads.** Front-to-second = 84.00 - 83.20 = +0.80 (positive, confirms backwardation). Annualized front-second roll = (0.80 / 83.20) x 12 ≈ **+11.5%** -- steep. The 12-month spread = 84.00 - 79.50 = +4.50, also positive.

**Step 3 -- Compare to inventory.** The trader overlays [[eia]] crude stocks (see [[inventory-cycle-analysis]]) and finds Cushing inventories drawing for six consecutive weeks and below the 5-year range. The tight physical market is *consistent* with the backwardated curve -- the signals agree.

**Step 4 -- Seasonal context.** It is early summer, approaching peak driving-season demand, which is a seasonally bullish window for crude. The backwardation is therefore not anomalous; it reflects genuine tightness, not a transient kink.

**Step 5 -- Trade.** A long front-month position earns the **+11.5% annualized positive roll yield** each time the trader rolls into the cheaper next contract, *in addition to* any spot appreciation. This is the [[commodity-carry-strategy]] setup. If the trader is wary of outright direction, an alternative is a long-M1 / short-12M calendar spread that isolates the term-structure view.

**Step 6 -- What would invalidate it.** A surprise inventory **build** larger than consensus, or a flattening of the front-second spread toward zero, would signal the tightness is resolving -- the cue to exit. The curve-slope first derivative (is backwardation steepening or flattening?) is the leading tell.

## Pitfalls in Reading the Curve

- **Confusing curve shape with a directional view.** A backwardated curve says the *physical market is tight*, not that the *price will rise tomorrow*. Spot can fall even in backwardation if demand collapses; roll yield and spot return are separate components.
- **Trusting stale deferred quotes.** Settlements beyond ~12 months are often marked off thin or no trading. Treating an illiquid back-end print as a real signal manufactures false term-structure shape.
- **Ignoring the roll-window distortion.** Large passive index roll flows (see [[commodity-index-rebalancing]]) mechanically depress the front and lift the next contract during the roll period (e.g., the Goldman roll), temporarily exaggerating contango. This is a flow artifact, not a fundamental signal.
- **Cross-commodity contamination.** Comparing curves across delivery points, grades, or settlement methods (WTI vs. Brent, physically vs. cash settled) without adjusting for the basis produces spurious "mispricings."
- **Annualization errors.** Failing to scale the spread by the number of months between contracts makes a 1-month and a 6-month spread look comparable when they are not.
- **Mistaking a kink for full backwardation.** A near-month spike from a transient disruption (refinery outage, weather) can invert the front while the rest of the curve stays in contango. Trading it as structural tightness leads to losses when the disruption resolves.

## Limitations

- **Curve data quality**: Settlement prices for deferred contracts can be stale (low liquidity, wide bid-ask). Use caution with contracts >12 months out.
- **Curve shape reflects expectations, not certainty**: The market's view of future supply/demand can be wrong.
- **Financialization effects**: Large passive index fund flows can distort curve shape (especially during roll windows -- see [[commodity-index-rebalancing]]).
- **Delivery/settlement differences**: Different contracts may have different delivery points, quality specs, or settlement methods, complicating cross-month comparisons.

## Related

- [[contango]] -- the fundamental concept of deferred > spot
- [[backwardation]] -- the fundamental concept of spot > deferred
- [[roll-yield]] -- the return from rolling futures positions
- [[convenience-yield]] -- the benefit of holding physical, driving backwardation
- [[cost-of-carry]] -- storage + financing costs, driving contango
- [[storage-economics]] -- the physical storage cost component
- [[commodity-carry-strategy]] -- strategy that trades on curve shape
- [[calendar-spread-arbitrage]] -- trading calendar spreads
- [[commodity-index-rebalancing]] -- index fund impact on curve during rolls
- [[inventory-cycle-analysis]] -- the inventory data that drives curve shape via the convenience-yield channel
- [[commodity-seasonality-patterns]] -- seasonal shapes the curve takes
- [[commodities]] -- market overview

## Sources

- Fama, E.F. & French, K.R. (1987). "Commodity Futures Prices: Some Evidence on Forecast Power, Premiums, and the Theory of Storage." *Journal of Business.*
- Gorton, G., Hayashi, F. & Rouwenhorst, K.G. (2013). "The Fundamentals of Commodity Futures Returns." *Review of Finance.*
- (Source: [[2026-04-14-commodities-research-framework]])
