---
title: "Commercial Hedger Positioning"
type: concept
created: 2026-04-14
updated: 2026-06-11
status: good
tags: [commodities, futures, indicators]
aliases: ["Commercial Positioning", "Commercial Hedger Analysis", "Smart Money Positioning"]
domain: [indicators]
difficulty: intermediate
prerequisites: ["[[cot-report-analysis]]", "[[open-interest]]"]
related: ["[[cot-report-analysis]]", "[[speculative-positioning]]", "[[open-interest]]", "[[hedging-pressure]]", "[[cftc]]", "[[cot-data]]", "[[commodities]]"]
---

# Commercial Hedger Positioning

How to interpret commercial hedger (producer/consumer) positioning from the [[cot-report-analysis|CFTC Commitments of Traders (COT) report]]. Commercials -- defined by the CFTC as entities that use commodity futures to hedge a commercial business -- are widely regarded as the "smart money" of commodity markets because they have the best information about physical supply and demand conditions. Their positioning data, published weekly, provides a window into how the most informed participants view the market (Source: [[2026-04-14-commodities-research-framework]]).

## Overview

The COT report categorizes market participants into three groups (legacy report) or four groups (disaggregated report):

### Legacy Report Categories
1. **Commercials**: Producers, processors, merchants, and other entities that use futures to hedge physical commodity exposure. They file CFTC Form 40 certifying their commercial interest.
2. **Non-commercials (speculators)**: Large traders (hedge funds, CTAs, commodity pools) that trade futures for speculative profit.
3. **Non-reportable**: Small traders below the CFTC's reporting threshold.

### Disaggregated Report Categories (more granular)
1. **Producer/Merchant/Processor/User**: The core commercial category.
2. **Swap Dealers**: Banks and dealers who run swap books (hedging OTC positions). Hybrid -- partially commercial, partially speculative.
3. **Managed Money**: Hedge funds, CTAs, commodity pools. The speculative category.
4. **Other Reportables**: Entities that don't fit the above categories.

For commercial hedger analysis, focus on the **Producer/Merchant/Processor/User** category from the disaggregated report (or Commercials from the legacy report) (Source: [[2026-04-14-commodities-research-framework]]).

## Why Commercials Are "Smart Money"

1. **Information advantage**: A copper miner knows their production pipeline, cost structure, and sees physical demand from customers before it shows up in financial data. An oil refiner knows their run schedule, product demand, and crude supply conditions. This information is not fully reflected in futures prices.
2. **Skin in the game**: Commercials have actual physical inventory and production at risk. Their hedging decisions reflect genuine business assessments, not speculative views.
3. **Systematic behavior**: Commercials tend to sell into rallies (producers locking in margins) and buy into dips (consumers securing supply). This creates mean-reverting patterns that can be exploited when commercial positioning reaches extremes.
4. **Contrarian to speculators**: When [[speculative-positioning|speculative positioning]] is at an extreme, commercial positioning is typically at the opposite extreme. Historically, commercials have been on the right side of major reversals more often than speculators (Source: [[2026-04-14-commodities-research-framework]]).

## Key Metrics

### Net Commercial Position
**Net Position = Long Contracts - Short Contracts**

In most commodity markets, commercials are **structurally net short** because producers (who sell futures to hedge) outnumber consumers (who buy futures to hedge). Therefore, the absolute level of net commercial position is less meaningful than its **change relative to historical norms**.

### Percentile of Historical Range
The most useful way to evaluate commercial positioning:

**Percentile = (Current Net Position - 3-Year Low) / (3-Year High - 3-Year Low) x 100**

- **0-10th percentile (extreme net short)**: Commercials are hedging aggressively -- they are selling futures at historically high rates. Two interpretations:
  - **Bearish**: Producers expect lower prices and are locking in currently high margins.
  - **Neutral-to-bullish contrarian**: If the market is already overbought, extreme producer hedging may be a contrarian indicator (they're hedging into strength).

- **90-100th percentile (least net short / net long)**: Commercials have reduced hedges significantly. Interpretations:
  - **Bullish**: Producers expect higher prices and don't want to sell at current levels.
  - **Or**: Production is declining (fewer hedges needed because there is less production to hedge).

### Net Position as % of Open Interest
Normalizes for market size changes over time:

**Commercial Net % = Net Commercial Position / Total [[open-interest|Open Interest]] x 100**

### Rate of Change
Weekly change in net commercial position. A rapid shift in hedging behavior is more significant than a gradual one.

## Interpretation Framework

### Signal 1: Commercial Extreme vs. Speculative Extreme
The **most powerful signal** occurs when commercials and speculators are at opposite extremes:

| Commercials | Speculators | Signal |
|-------------|-------------|--------|
| Extreme net short (0-10th pctl) | Extreme net long (90-100th pctl) | **Bearish** -- market is crowded long, smart money hedging aggressively |
| Least net short (90-100th pctl) | Extreme net short (0-10th pctl) | **Bullish** -- speculators are overly bearish, commercials see value |

This divergence is not a timing signal -- it's a **condition** that can persist for weeks or months. Combine with price action and fundamental catalysts for timing.

### Signal 2: Change in Commercial Positioning Trend
If commercials have been steadily increasing net short positions (adding hedges) for months and then suddenly reverse (reducing hedges), this shift may signal a change in their fundamental outlook. Look for:
- 3+ consecutive weeks of positioning change in the same direction
- Positioning change occurring against the price trend (commercials reducing hedges while prices rise = bullish)

### Signal 3: Commercial Positioning vs. Curve Shape
Cross-reference commercial positioning with [[futures-curve-structure-analysis|futures curve structure]]:
- Extreme commercial short + steep [[backwardation]] = producers aggressively hedging a tight market. The backwardation may persist (producers have a reason to hedge despite high prices -- they see supply coming).
- Reduced commercial hedging + deepening [[contango]] = producers not hedging because prices are too low. Potentially near a bottom.

## Example Analysis

**Crude Oil, December 2023:**

1. **COT data**: Producer/Merchant net short at -380,000 contracts. 3-year range: -250,000 to -450,000. Percentile: 35th (moderately net short -- near the middle of the range).
2. **Managed Money**: Net long at +150,000 contracts. 3-year range: -50,000 to +300,000. Percentile: 60th.
3. **Interpretation**: Neither commercials nor speculators at extremes. No strong positioning signal. Neutral.

**Wheat, March 2024:**
1. **COT data**: Commercial net short at -25,000 contracts. 3-year range: -20,000 to -180,000. Percentile: 97th (very little hedging -- near the least net short in 3 years).
2. **Managed Money**: Net short at -90,000 contracts. 3-year range: -100,000 to +80,000. Percentile: 5th (near record short).
3. **Interpretation**: **Bullish divergence.** Producers have largely stopped hedging (they expect higher prices or have very little production to hedge). Speculators are near-record short (crowded bearish). Conditions are ripe for a short-covering rally if any bullish catalyst appears (Source: [[2026-04-14-commodities-research-framework]]).

## Important Caveats

1. **Commercials are not always right**: They are structurally better informed about physical fundamentals, but they can be wrong about macro factors (financial crises, policy changes) that override fundamentals.
2. **Positioning is a condition, not a timing signal**: Extremes can persist for months during strong trends. Use a price trigger (breakout, reversal pattern) to time entries.
3. **CFTC category definitions are imperfect**: Some entities classified as "commercial" may actually be speculating. Swap dealers, in particular, run a mix of hedging and proprietary activity.
4. **Data lag**: The COT report reflects positions as of Tuesday, published Friday afternoon. By the time you see it, the market may have moved.
5. **Structural changes in hedging behavior**: If producers permanently change their hedging strategy (e.g., airlines that stopped hedging fuel after 2020), historical comparisons become misleading.

## Related

- [[cot-report-analysis]] -- the report that provides commercial positioning data
- [[speculative-positioning]] -- the other side of the positioning equation
- [[open-interest]] -- total market activity that contextualizes positioning
- [[hedging-pressure]] -- the theoretical framework for why commercial hedging creates a risk premium
- [[cftc]] -- the regulator that publishes the COT report
- [[cot-data]] -- data source details
- [[commodities]] -- market overview
- [[commodity-carry-strategy]] -- strategy connected to hedging pressure dynamics

## Sources

- CFTC Commitments of Traders Report, published weekly.
- Bessembinder, H. (1992). "Systematic Risk, Hedging Pressure, and Risk Premiums in Futures Markets." *Review of Financial Studies.*
- De Roon, F.A., Nijman, T.E. & Veld, C. (2000). "Hedging Pressure Effects in Futures Markets." *Journal of Finance.*
- (Source: [[2026-04-14-commodities-research-framework]])
