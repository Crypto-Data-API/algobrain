---
title: Volume
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags: [volume, indicators]
aliases: [trading-volume]
domain: [indicators]
difficulty: beginner
related:
  - "[[liquidity]]"
  - "[[obv]]"
  - "[[vwap]]"
  - "[[momentum]]"
  - "[[john-murphy]]"
  - "[[technical-analysis-of-the-financial-markets]]"
  - "[[open-interest]]"
  - "[[futures-overview]]"
  - "[[commodities]]"
  - "[[intermarket-analysis]]"
---

# Volume

Volume is the total number of shares, contracts, or units of an asset traded during a given time period.

## Overview

Volume measures market participation and conviction. It is one of the most fundamental indicators, used to confirm trends, spot reversals, and assess [[liquidity]]. Price moves on high volume carry more significance than those on low volume, because more participants are endorsing the price action.

## Key Details

### Volume Analysis

- **Rising price + rising volume**: Strong bullish conviction. Trend is confirmed.
- **Rising price + falling volume**: Weakening momentum. Potential exhaustion or reversal ahead.
- **Falling price + rising volume**: Strong selling pressure. Bearish confirmation.
- **Falling price + falling volume**: Selling pressure waning. Potential bottom forming.

### Volume Profile

Volume profile displays trading activity at each price level rather than per time period. It reveals:
- **High Volume Nodes (HVN)**: Price levels with heavy activity -- act as support/resistance zones.
- **Low Volume Nodes (LVN)**: Price levels with little activity -- price tends to move quickly through these.
- **Point of Control (POC)**: The single price level with the most volume, often a magnet for price.

### Volume Indicators

- **[[obv]] (On-Balance Volume)**: Cumulative running total that adds volume on up days and subtracts on down days.
- **[[vwap]]**: Volume-weighted average price, a key institutional benchmark.
- **Volume Moving Average**: Compares current volume to its average to spot unusual activity.

## Trading Relevance

Volume is the "fuel" behind price moves. Always confirm breakouts with above-average volume -- breakouts on low volume frequently fail. Volume spikes often mark capitulation bottoms or blowoff tops. For position traders, sustained volume increases signal institutional accumulation or distribution.

## Open Interest in Futures

Murphy covers [[open-interest]] alongside volume as the second key participation metric for commodity futures (Source: [[book-technical-analysis-of-the-financial-markets]]). While volume measures how many contracts changed hands, open interest measures how many contracts remain outstanding. Together they reveal the conviction behind price moves:

| Price | Volume | Open Interest | Interpretation |
|-------|--------|---------------|----------------|
| Rising | Rising | Rising | New money entering -- strong bullish signal |
| Rising | Rising | Falling | Short covering rally -- less bullish, limited upside |
| Falling | Rising | Rising | New shorts entering -- strong bearish signal |
| Falling | Rising | Falling | Long liquidation -- less bearish, selling pressure may exhaust |

Open interest analysis is most useful in commodity [[futures-overview|futures]] where all contracts are created and destroyed (unlike equities where share count is relatively fixed). Rising open interest during a commodity trend confirms conviction; falling open interest during a trend warns of exhaustion. See [[open-interest]] for detailed analysis.

## Commodity Volume Analysis

In commodity futures, volume dynamics are closely tied to fundamental data releases and geopolitical events (Source: [[book-technical-analysis-of-the-financial-markets]]):

- **Energy markets**: Volume spikes around [[eia|EIA]] weekly petroleum status reports (Wednesday 10:30 AM ET) and monthly Short-Term Energy Outlook. [[crude-oil]] and [[natural-gas]] routinely see 2-3x average volume on EIA release days.
- **Agricultural markets**: [[usda|USDA]] WASDE (World Agricultural Supply and Demand Estimates) reports, released monthly, trigger major volume surges in [[corn]], [[wheat]], [[soybeans]], and soft [[commodities]]. USDA planting intention reports (March) and crop production estimates (August-October) are the highest-volume events in agricultural futures.
- **Energy policy events**: [[opec|OPEC]]+ meeting decisions on production quotas create volume spikes across the entire energy complex.

Confirming breakouts with volume is even more critical in commodity markets than in equities because of lower average liquidity. A breakout above resistance on a commodity chart that occurs on low volume is more likely to be a false breakout than the same pattern in a highly liquid equity market. Conversely, high-volume breakouts in commodities tend to produce larger and more persistent follow-through because the lower liquidity amplifies the price impact of new participants entering.

**Volume seasonality** also matters in commodities -- trading volume in agricultural futures peaks around planting and harvest seasons, while energy futures volume peaks during winter heating and summer driving seasons. Low-volume periods are more prone to false signals and erratic price action.

## Sources

- [[book-technical-analysis-of-the-financial-markets]] -- Murphy: "Volume is the fuel behind price moves" and "Volume confirms price." Comprehensive coverage of volume analysis, open interest interpretation in futures, and the volume-price relationship framework (Source: [[book-technical-analysis-of-the-financial-markets]])
- Granville, Joseph (1963), *Granville's New Key to Stock Market Profits* — origin of On-Balance Volume (OBV)
- Steidlmayer, J. Peter & Steidlmayer, Steven (2003), *Steidlmayer on Markets* — Market Profile / volume-at-price (volume profile) framework

## Related

- [[obv]] -- cumulative volume indicator
- [[vwap]] -- volume-weighted price benchmark
- [[liquidity]] -- volume is a proxy for liquidity
- [[momentum]] -- volume confirms momentum signals
- [[open-interest]] -- the second participation metric for futures markets
- [[futures-overview]] -- volume and open interest are core futures analysis tools
- [[commodities]] -- commodity volume analysis requires understanding data release calendars
- [[intermarket-analysis]] -- cross-market volume comparisons reveal capital flows
- [[john-murphy]] -- covers volume as a foundational confirmation tool
