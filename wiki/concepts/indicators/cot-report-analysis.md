---
title: "COT Report Analysis"
type: concept
created: 2026-04-14
updated: 2026-06-11
status: good
tags: [commodities, futures, indicators]
aliases: ["Commitments of Traders", "COT Report", "CFTC COT"]
related: ["[[cftc]]", "[[open-interest]]", "[[commercial-hedger-positioning]]", "[[speculative-positioning]]", "[[futures-overview]]", "[[trend-following-cta]]", "[[commodities]]", "[[cot-data]]"]
domain: indicators
prerequisites: ["[[futures-overview]]", "[[open-interest]]"]
difficulty: intermediate
---

The Commitments of Traders (COT) report is a weekly publication by the [[cftc|Commodity Futures Trading Commission (CFTC)]] that breaks down the [[open-interest]] in U.S. futures markets by trader category. Published every Friday at 3:30 PM ET (reflecting positions as of the prior Tuesday's close), the COT report is the primary public data source for understanding who is positioned where in commodity and financial futures markets.

## Report Structure and Trader Categories

The COT report classifies traders into three main categories based on the purpose of their trading:

### Commercials (Hedgers)
Firms that use futures to hedge a physical business activity. These include producers (oil companies, farmers, miners), consumers (refiners, food processors, manufacturers), and intermediaries (commodity merchants, swap dealers). Commercials are generally considered the "smart money" in commodity markets — they have direct knowledge of physical supply-demand conditions and are acting to manage real business risk, not to speculate on price direction.

### Non-Commercials (Large Speculators)
Managed money accounts, hedge funds, [[trend-following-cta|CTAs]], and other institutional speculators whose positions exceed the CFTC's reporting threshold. These traders are in the market to profit from price movements, not to hedge physical exposure. Their positioning tends to be momentum-driven and can amplify trends.

### Non-Reportable (Small Speculators)
Traders whose positions fall below the CFTC's reporting threshold. This category is calculated as a residual: total open interest minus commercial minus non-commercial positions. Historically considered the least informed category, though this generalization has weakened as retail trading has become more sophisticated (Source: [[2026-04-14-commodities-research-framework]]).

## Legacy vs Disaggregated Reports

The CFTC publishes two main versions of the COT:

- **Legacy COT**: The original format, available back to 1986. Splits open interest into commercials, non-commercials, and non-reportable. Simple and widely used.
- **Disaggregated COT** (from 2006): Breaks down the categories further — producers/merchants/processors/users, swap dealers, managed money, and other reportables. This provides clearer insight because the legacy "commercial" category lumps together physical hedgers and swap dealers (who may be passing through speculative risk from OTC clients).

For commodity analysis, the disaggregated report's **managed money** category is more useful than the legacy non-commercial category because it isolates true speculative positioning (Source: [[2026-04-14-commodities-research-framework]]).

## How to Use COT Data

### Extreme Positioning as a Contrarian Signal

The most common COT-based signal is identifying extreme positioning relative to historical norms:

- **Speculators net long at multi-year extremes**: Suggests crowded bullish positioning. If the fundamental catalyst stalls, a wave of long liquidation can trigger sharp declines. This represents potential top/reversal risk.
- **Speculators net short at multi-year extremes**: Suggests crowded bearish positioning. Any bullish catalyst can trigger a short squeeze as shorts rush to cover. This represents potential squeeze risk.

The typical approach is to compute a percentile ranking of net speculative positioning over a lookback window (e.g., 3 years) and flag readings above the 90th or below the 10th percentile as extreme.

### Commercial Positioning as a Fundamental Signal

Because commercials have direct knowledge of physical market conditions, their positioning can serve as a leading indicator:

- **Commercials unusually net long**: May signal that physical market participants expect prices to rise — they are willing to take on speculative-type long exposure in addition to their normal hedging.
- **Commercials unusually net short**: Producers are locking in historically attractive prices via forward sales — they see current prices as high relative to their cost structure.

### Combining COT with Other Signals

COT data works best as a confirmation or warning signal, not a standalone trading system. It is most powerful when combined with:

- **Price and trend analysis**: Extreme speculative positioning against the prevailing trend suggests the trend may be exhausting
- **Futures curve structure**: [[contango]]/[[backwardation]] context adds depth to positioning analysis
- **Inventory data**: Physical inventory levels validate whether commercial positioning reflects genuine supply-demand tightness
- **Seasonality**: Some commodities have predictable seasonal positioning patterns (e.g., natural gas heating season, agricultural planting/harvest cycles)

## Data Access and Timeliness

- Published weekly — reflects prior Tuesday close, released Friday at 3:30 PM ET
- Available for free at [cftc.gov](https://www.cftc.gov/MarketReports/CommitmentsofTraders/index.htm) and via [[cot-data|data vendors]]
- 3-day lag (Tuesday positions, Friday release) limits usefulness for short-term trading
- Historical data back to 1986 (legacy) and 2006 (disaggregated) allows robust backtesting of positioning signals

## Limitations

- **Lagged data**: Three-day-old positioning snapshots can be stale in fast-moving markets
- **Category misclassification**: Swap dealers in the legacy report blur the commercial/speculative distinction
- **No intraday granularity**: Only a weekly snapshot — positioning can change significantly within the week
- **Only U.S. futures**: Does not cover OTC derivatives, foreign futures exchanges, or spot market positions
- **Reporting thresholds change**: CFTC periodically adjusts position reporting levels, affecting time-series consistency

## Related

- [[cftc]]
- [[open-interest]]
- [[commercial-hedger-positioning]]
- [[speculative-positioning]]
- [[cot-data]]
- [[futures-overview]]
- [[trend-following-cta]]
- [[commodities]]
- [[commodity-trading]]

## Sources

- CFTC, "Commitments of Traders" — official report and explanatory notes, cftc.gov/MarketReports/CommitmentsofTraders.
- Briese, Stephen. *The Commitments of Traders Bible: How to Profit from Insider Market Intelligence.* Wiley, 2008.
- (Source: [[2026-04-14-commodities-research-framework]])
