---
title: "Seasonal Spread Trading"
type: reference
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [seasonal, spread-trading, calendar-spread, commodity-cycles, agriculture, energy, seasonality]
aliases: ["Seasonal Commodity Spreads", "Calendar Spread Trading", "Seasonal Futures Trading"]
strategy_type: fundamental
timeframe: swing|position
markets: [commodities]
complexity: intermediate
backtest_status: untested
related: ["[[crack-spread]]", "[[crush-spread]]", "[[spark-spread]]", "[[basis-trading]]", "[[sector-rotation]]"]
---

# Seasonal Spread Trading

## Overview

Seasonal spread trading exploits **recurring, calendar-driven patterns** in commodity futures prices by trading the spread between different contract months or related commodities. Unlike outright directional commodity trading, spread trading isolates the seasonal component while hedging out much of the broader price risk. The strategy is grounded in physical market fundamentals: planting and harvest cycles in agriculture, heating and cooling demand in energy, and inventory build/draw patterns across all commodity sectors.

The foundational observation is that commodities have **predictable supply/demand cycles** tied to the calendar. Heating oil demand peaks in winter. Gasoline demand peaks in summer. Grain supplies surge at harvest and deplete through the marketing year. Natural gas storage builds in spring/summer and draws in winter. These cycles create recurring patterns in the **term structure** of futures -- the price relationship between near-month and deferred contracts -- that can be traded systematically.

A **calendar spread** (also called a time spread or intra-commodity spread) involves buying one contract month and selling another in the same commodity. For example, buying July corn and selling December corn profits if the July-December spread widens (old crop tightens relative to new crop). An **inter-commodity spread** involves related commodities in different seasonal phases -- for example, long heating oil / short gasoline in autumn as heating demand strengthens relative to driving demand.

Seasonal spread trading has been practiced by commodity traders for decades. Moore Research Center (MRCI) and other services publish historical seasonal patterns with win rates, making this one of the most data-rich strategies in commodity trading.

## How It Works

### Calendar Spreads
The price relationship between near and deferred futures contracts reflects the market's expectation of supply/demand over time:
- **Contango** (deferred > nearby): Normal when supply is adequate. Reflects storage costs, insurance, and financing (cost of carry).
- **Backwardation** (nearby > deferred): Supply is tight. The market pays a premium for immediate delivery. Common during harvest shortfalls, demand surges, or supply disruptions.

Seasonal patterns cause predictable shifts between contango and backwardation. For example, natural gas typically moves from contango in summer (supply builds) to backwardation as winter approaches (demand expectations).

### Inter-Commodity Spreads
Trade the seasonal shift in relative demand between related commodities:
- **Heating oil vs. gasoline:** Heating oil strengthens relative to gasoline in fall/winter (heating demand). Gasoline strengthens in spring/summer (driving demand). This is a component of the [[crack-spread]].
- **Wheat vs. corn:** Wheat tends to gain a premium in spring (crop uncertainty) and narrow at harvest (new supply).
- **Live cattle vs. feeder cattle:** The spread widens when feed costs (corn) are low and narrows when feed costs are high.

### Historical Pattern Analysis
For each spread, analyze 15-30 years of historical data:
1. Calculate the spread value for each trading day of the year across all years.
2. Compute the average seasonal pattern (mean spread by calendar day).
3. Calculate the **win rate** (percentage of years the spread moved in the expected direction during the trade window).
4. Identify the **optimal entry and exit dates** that maximize the average return and win rate.

## Rules / Application

### Trade Selection
1. Screen for seasonal patterns with **win rates > 70%** over the past 15+ years using historical databases (MRCI, Seasonal Algo, or custom analysis).
2. Verify the pattern has a **fundamental explanation** (not just data mining). A pattern driven by a known physical cycle (harvest, heating season) is more reliable than a statistical artifact.
3. Confirm current fundamentals **align with the seasonal expectation.** If a drought is devastating the corn crop, a typical harvest-pressure seasonal short may not work.
4. Prioritize spreads with consistent historical returns and low maximum adverse excursion (MAE).

### Entry and Exit Rules
1. **Enter** within 5 trading days of the historical optimal entry date.
2. **Exit** at the historical optimal exit date, or earlier if the spread reaches the historical average move.
3. **Stop-loss:** Set at 1.5-2x the average maximum adverse excursion for the pattern. If the pattern typically sees $500 adverse movement before working, stop at $750-$1,000.
4. **Time stop:** If the spread is not working within 2/3 of the historical trade duration, exit to free capital.

### Position Sizing
- Size each spread trade to risk 1-2% of trading capital per trade.
- Reduce size when current fundamentals partially contradict the seasonal pattern.
- Diversify across multiple seasonal patterns in different commodities to smooth returns.

## Example

**Setup:** Long heating oil / short gasoline spread, entering mid-September, targeting winter heating demand.

1. **Historical pattern:** Over the past 20 years, the HO-RB spread (heating oil minus RBOB gasoline) has widened from mid-September through mid-December with a **75% win rate** and an average gain of $4,500 per spread unit.
2. **September 15:** HO December at $2.60/gal, RB December at $2.45/gal. Spread = $0.15/gal.
3. **Enter:** Buy 1 HO December contract, sell 1 RB December contract.
4. **October-November:** Heating season begins. Inventory draws in distillate. HO rises to $2.85/gal, RB falls slightly to $2.40/gal.
5. **December 10:** Spread = $2.85 - $2.40 = $0.45/gal. Spread widened by $0.30/gal.
6. **Exit:** Profit = $0.30/gal x 42,000 gal/contract = **$12,600** per spread unit.
7. This year's result exceeded the 20-year average due to a colder-than-normal autumn, but the directional move was consistent with the seasonal pattern.

## Advantages

- **High historical win rates:** Well-documented seasonal patterns often show 65-80% win rates over 15-30 year histories
- **Fundamentally grounded:** Patterns are driven by real physical cycles (weather, planting, harvest, consumption), not ephemeral market microstructure
- **Lower risk than outright positions:** Calendar spreads hedge much of the directional price risk; margin requirements are significantly reduced
- Hundreds of documented patterns across all major commodity sectors provide a large opportunity set
- **Diversifiable:** Running 10-20 seasonal trades simultaneously across grains, energy, metals, and softs creates a portfolio effect
- Data-rich: decades of futures data are available for backtesting with organizations like MRCI publishing pre-built seasonal studies

## Disadvantages

- **Seasonals can fail:** Current fundamentals can overwhelm historical patterns. A drought during a typically bearish harvest period can cause massive losses for a short-corn seasonal
- **Win rate is not everything:** A 75% win rate with a 1:3 reward-to-risk ratio can still lose money if the losing trades are large
- Requires **commodity market expertise** to evaluate whether current fundamentals support or contradict the seasonal pattern
- **Data mining risk:** With thousands of possible spreads and date combinations, many "patterns" are statistical noise that will not repeat
- Seasonal patterns may be **degrading over time** as more traders and algorithms exploit them
- Calendar spreads can become illiquid in deferred months, leading to wide bid-ask spreads and slippage
- Some seasonal patterns require holding trades for 2-4 months, tying up capital and margin for extended periods

## See Also

- [[crack-spread]] -- petroleum seasonal spreads (summer gasoline, winter heating oil)
- [[crush-spread]] -- agricultural processing margin with seasonal patterns
- [[spark-spread]] -- power generation spreads with weather-driven seasonality
- [[sector-rotation]] -- the equity market equivalent of seasonal/cyclical allocation
- [[basis-trading]] -- location-based commodity spreads that interact with seasonal patterns
