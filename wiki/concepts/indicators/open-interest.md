---
title: "Open Interest"
type: concept
created: 2026-04-06
updated: 2026-04-14
status: good
confidence: medium
tags: [derivatives, indicators, open-interest, futures, commodities]
aliases: ["OI"]
domain: [derivatives, indicators, market-microstructure]
prerequisites: ["[[perpetual-futures]]", "[[futures-overview]]"]
difficulty: beginner
related: ["[[perpetual-futures]]", "[[funding-rate]]", "[[volume]]", "[[liquidation]]", "[[cot-report-analysis]]", "[[futures-overview]]", "[[speculative-positioning]]", "[[commercial-hedger-positioning]]", "[[commodities]]"]
---

# Open Interest

**Open interest (OI)** is the total number of outstanding [[derivatives]] contracts (such as [[perpetual-futures]], [[futures]], or [[options]]) that have not been settled or closed. Each contract represents one long and one short position, so OI counts the number of *pairs*, not the sum of all positions.

## Definition and Mechanics

Open interest changes only when new contracts are created or existing ones destroyed:

| Buyer Action | Seller Action | OI Effect |
|-------------|--------------|-----------|
| New buyer opens long | New seller opens short | OI **increases** |
| Existing long closes | Existing short closes | OI **decreases** |
| New buyer opens long | Existing long sells to close | OI **unchanged** (transfer) |
| Existing short buys to close | New seller opens short | OI **unchanged** (transfer) |

OI rises when new money enters the market and falls when money exits. A transfer of an existing contract does not change OI.

## Open Interest vs. Volume

| Metric | Measures | Resets? | Interpretation |
|--------|---------|---------|---------------|
| **[[volume]]** | Total contracts traded in a period | Yes (daily) | Activity, [[liquidity]] |
| **Open Interest** | Outstanding contracts right now | No (cumulative) | Capital committed, positioning |

A day can have high [[volume]] with no OI change (all transfers between existing participants). Example: market starts at 1,000 OI. Trader A opens 100 new long, B opens 100 new short (OI = 1,100). C transfers 50 existing longs to D (OI unchanged). A and B close (OI = 1,000). Daily volume = 250, but OI returned to start.

## OI + Price Analysis

The relationship between OI changes and price changes is one of the most practical tools in [[derivatives]] analysis:

| Price | OI | Interpretation | Signal |
|-------|-----|---------------|--------|
| Rising | Rising | New longs entering aggressively | **Strong bullish** |
| Rising | Falling | Short covering rally; existing shorts closing | **Weak bullish** (may fade) |
| Falling | Rising | New shorts entering aggressively | **Strong bearish** |
| Falling | Falling | Long capitulation; longs giving up | **Weak bearish** (may exhaust) |

**Rising price + rising OI** is the healthiest bull signal -- new capital flowing in with conviction. **Rising price + falling OI** is a short squeeze, fueled by closing positions rather than new capital, often unsustainable. **Falling price + falling OI** is capitulation that often precedes bottoms as selling pressure exhausts.

## Live Market Data

Current open interest on [[hyperliquid]]:

| Asset | Open Interest (native) | Approx. Notional |
|-------|----------------------|-------------------|
| BTC | 28,766 BTC | ~$2.0 billion |
| ETH | 560,526 ETH | ~$1.2 billion |
| HYPE | 21.8 million HYPE | Varies |

The BTC OI of 28,766 BTC on [[hyperliquid]] alone represents enormous leveraged exposure. Across all exchanges, total BTC [[perpetual-futures]] OI typically ranges from 200,000 to 500,000 BTC.

## OI on Perps vs. Traditional Futures

On [[perpetual-futures]], OI reflects real-time positioning with no periodic rollover drops. Traditional [[futures]] OI follows expiry cycles: it builds after launch, peaks mid-lifecycle, and declines as expiry approaches and traders roll to the next contract. This rollover pattern can cause temporary price dislocations.

## OI Concentration and Risk

When OI is highly concentrated in a single direction, markets become vulnerable to cascading [[liquidation]] events. Extreme long OI + slight price decline triggers [[liquidation|liquidations]], which are market sell orders that push price lower, triggering more liquidations in a feedback loop. Markets with high OI and extreme [[funding-rate|funding rates]] are prone to violent reversals.

**OI heatmaps** show where large clusters of open interest exist at different price levels, representing potential [[liquidation]] levels that can act as magnets for price.

## Practical Applications

- **Trend confirmation**: Healthy uptrend = price up, OI up, moderate [[funding-rate]]. Suspect uptrend = price up, OI flat/down, extreme funding.
- **Crowded trade detection**: Rising OI + elevated [[funding-rate]] in one direction signals vulnerability to reversal.
- **Market interest**: Sustained OI growth indicates growing trader interest and [[liquidity]]; declining OI signals waning interest.
- **Event positioning**: OI building into major events (FOMC, CPI, token unlocks) = directional bets; declining OI = [[derisking]].

## Common Misconceptions

1. **"High OI means the price will go up"** -- OI is direction-agnostic. For every long there is a short.
2. **"OI is the same as volume"** -- [[volume]] measures activity (flow); OI measures positioning (stock).
3. **"OI counts longs and shorts separately"** -- OI counts *contracts*, each with one long and one short side. OI of 10,000 means 10,000 longs and 10,000 shorts.
4. **"Rising OI always means trend continuation"** -- If OI rises too fast, it signals overcrowding and increases [[liquidation]] cascade risk.
5. **"OI drops mean people are bearish"** -- Falling OI means positions are closing. Whether longs or shorts closed depends on price action.

## COT Report Breakdown (Commodity Futures)

The CFTC's [[cot-report-analysis|Commitments of Traders (COT) report]] disaggregates open interest in U.S. futures markets into three categories:

- **Commercials** (hedgers): Producers, consumers, and intermediaries using futures to manage physical commodity risk. See [[commercial-hedger-positioning]].
- **Non-commercials** (large speculators): Managed money, hedge funds, and [[trend-following-cta|CTAs]] taking directional positions. See [[speculative-positioning]].
- **Non-reportable** (small speculators): Positions below the CFTC's reporting threshold — typically retail traders and small funds.

This breakdown adds a critical layer of information: not just how much open interest exists, but *who* holds it. Extreme positioning by one category relative to historical norms can signal potential reversals. COT data goes back to 1986 (legacy format) and 2006 (disaggregated format) (Source: [[2026-04-14-commodities-research-framework]]).

## OI Across Asset Classes

- **Commodity futures**: OI data is reported daily by exchanges with a one-day lag. Expiration events cause mechanical drops in OI as contracts settle or roll — not a sentiment signal.
- **Options**: Options open interest is reported separately and reflects outstanding option contracts. High put OI at a strike can indicate hedging demand or speculative positioning.
- **Crypto perpetual futures**: "Open interest" refers to the notional value of open perpetual swap positions — a similar concept but without expiration mechanics (see sections above).

## Further Reading

- [[perpetual-futures]] -- The primary instrument where OI is most closely watched in crypto
- [[cot-report-analysis]] -- Weekly CFTC report breaking OI into trader categories
- [[funding-rate]] -- Complementary metric for reading market positioning
- [[volume]] -- The activity counterpart to OI's positioning metric
- [[liquidation]] -- What happens when concentrated OI unwinds violently
- [[market-microstructure]] -- Broader framework for understanding market dynamics
- [[speculative-positioning]] -- How speculator OI at extremes signals reversals
- [[commercial-hedger-positioning]] -- How commercial hedger OI reflects fundamental conditions
- [[commodities]] -- Physical commodity markets where OI analysis originated

## Related

- [[derivatives-native-regime]] -- OI as a regime signal (OI divergence, squeeze setups)
- [[liquidity-depth-regime]] -- OI vs order-book depth as the pre-cascade fragility signal
- [[crypto-market-regime-taxonomy]] -- the 14-basket crypto regime framework

## Sources

- (Source: [[2026-04-14-commodities-research-framework]])
