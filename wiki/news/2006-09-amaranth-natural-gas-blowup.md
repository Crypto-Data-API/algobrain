---
title: "Amaranth Advisors Natural Gas Blowup (September 2006)"
type: news
created: 2026-04-28
updated: 2026-06-12
status: good
tags: [news, commodities, natural-gas, derivatives, risk-management, history]
aliases: ["Amaranth Blowup", "Brian Hunter Blowup", "$6 Billion Natural Gas Loss", "Arnold vs Hunter"]
event_date: 2006-09-21
markets_affected: [commodities]
impact: high
verified: true
sources_count: 5
related: ["[[brian-hunter]]", "[[john-arnold]]", "[[counterparty-stress-arbitrage]]", "[[natural-gas]]", "[[calendar-spread-arbitrage]]", "[[commodities]]", "[[liquidation-cascade-arbitrage]]", "[[fastest-profitable-trades]]", "[[risk-management]]", "[[history-overview]]", "[[2022-06-three-arrows-blowup]]"]
---

In September 2006, Amaranth Advisors — a multi-strategy hedge fund managing approximately **$9.2 billion** at peak — lost approximately **$6.6 billion in a single week** on a concentrated bet that the spread between March and April natural-gas futures would widen. On the other side of the trade, [[john-arnold|John Arnold]]'s Centaurus Energy is widely believed to have made approximately **$1 billion** by recognizing that Amaranth's positions were so large that an unwind was inevitable, then trading the forced-liquidation path. The episode is the canonical post-2000 case study of **counterparty-stress arbitrage** — see [[counterparty-stress-arbitrage]] for the strategy generalization, [[fastest-profitable-trades]] for the broader pattern, and [[brian-hunter]] / [[john-arnold]] for trader detail.

## Headline facts

| Field | Detail |
|-------|--------|
| **Date of blowup** | September 14-21, 2006 (final unwind through Sept 21) |
| **Loser** | Amaranth Advisors (Brian Hunter, head of energy desk) |
| **Loss** | ~$6.6 billion in one week (~$5B+ in single-day moves) |
| **AUM at peak** | ~$9.2 billion |
| **Counter-trade winner** | Centaurus Energy (John Arnold) |
| **Estimated Centaurus profit** | ~$1 billion |
| **Position type** | Calendar-spread positions in NYMEX natural-gas futures, primarily Mar07 vs Apr07 ("widow-maker spread") |
| **Position size** | Reported ~100,000 contracts of natural-gas futures and options at peak — multiple times average daily NYMEX volume |
| **Market impact** | Multi-day disorderly liquidation; NYMEX gas futures gapped multiple sigma intraday |

## What was the trade

### The "widow-maker" spread

Natural gas has the strongest seasonal pattern of any major commodity. Inventories build through summer (low demand) and draw through winter (heating). The futures curve reflects this: winter months trade at a premium to shoulder months (March, October, April).

The **March-April spread** is the single most volatile calendar spread in commodities — known as the "widow-maker." March is the last winter contract; April is the first shoulder contract. If winter is colder than expected, March prices spike and the March-April spread widens dramatically. If winter is mild, March collapses toward April and the spread compresses.

[[brian-hunter|Brian Hunter]] — Amaranth's head of energy trading and a 32-year-old former Calgary trader — built a massive position betting that:

- **Long March 2007 futures** (and March 2008, March 2009 in deferred years).
- **Short April 2007 futures** (and April 2008, April 2009).
- **Long winter calls / short summer calls**: option positions that paid off if winter '06-'07 was cold or natural-gas storage drew faster than expected.

The thesis was: the prior winter (2005-06) had seen historically low storage and elevated prices following Hurricane Katrina; Hunter expected a similar pattern in 2006-07.

### Position size relative to market liquidity

Hunter's position was, by mid-2006, **multiple times the open interest** in some contract months. NYMEX disclosures and post-blowup CFTC investigation revealed:

- Amaranth held an estimated **40% of the total open interest** in some natural-gas contract months.
- The position required Amaranth to be effectively the largest counterparty in the entire NYMEX natural-gas futures market.
- Many of the positions were also held on ICE (Intercontinental Exchange), which at the time had less reporting/visibility than NYMEX, allowing Amaranth to circumvent NYMEX position limits.

Position size of this magnitude is itself a market structure problem: any forced unwind would move the market against the unwinder by amounts proportional to the position size, creating a death-spiral feedback loop.

## Why Amaranth was wrong

The 2006-07 winter was warm. By August 2006:

- Natural-gas storage levels were the highest in decades.
- The Atlantic hurricane season was unexpectedly quiet (no major Gulf landfalls).
- LNG imports increased.
- Demand was soft.

The March-April 2007 spread, instead of widening, began compressing. Hunter doubled down through August into September — believing the move was a mispricing rather than a thesis breakdown.

By early September 2006:
- The spread had collapsed from $2.50/MMBtu to under $1.00/MMBtu.
- Amaranth's mark-to-market losses approached $1B and rose daily.
- The fund's prime brokers (JPMorgan, Goldman, others) began margining harder.
- News leaked of Amaranth's distress.

Once the unwinding began, the spread compressed further as Amaranth was forced to *exit* its long-March / short-April book — *selling March, buying April* — exactly the trades that would push the spread further against the original position.

## How John Arnold positioned the counter-trade

[[john-arnold|John Arnold]] founded Centaurus Energy in 2002 after his Enron natural-gas trading desk's de-facto liquidation. By 2006, Centaurus had grown to ~$3-4B AUM and was widely regarded as the most sophisticated natural-gas trader in the market. Arnold's approach to the Amaranth setup combined:

### 1. Recognizing the position size

Centaurus's position monitoring (via brokers' large-trader reports, NYMEX commitment-of-traders data, and direct inference from price action) allowed Arnold to identify by mid-2006 that one large counterparty was building anomalously concentrated calendar-spread positions.

### 2. Recognizing the position direction

By tracking *which* contract months were most affected by the anomalous flow, Arnold inferred Amaranth's directional exposure: long March, short April; long winter, short summer.

### 3. Recognizing fundamental mispricing

Independent of Amaranth's positioning, Arnold's view of natural-gas fundamentals (high storage, mild winter outlook, no hurricane disruption) suggested the calendar spreads were too wide on a fundamental basis. Hunter's bullish bias was overpaying for winter risk.

### 4. Positioning for the eventual forced unwind

When fundamental disagreement and position-stress alignment converge, the trade has two legs:

- **Fundamental leg**: short the spread (long April, short March; long summer, short winter) on the conviction that storage and weather would compress winter premium.
- **Liquidation leg**: increase position size as the spread moved against Amaranth, knowing each tick of adverse movement raised Amaranth's margin pressure and accelerated the eventual forced unwind.

When Amaranth began liquidating in mid-September, Arnold was on the buy side of every Mar07 the fund had to sell, and the sell side of every Apr07 they had to buy. Centaurus's gains compounded as Amaranth's losses did.

### Estimated Centaurus P&L: ~$1 billion

Public reporting after the blowup put Centaurus's profit on the Amaranth-driven natural-gas trade at approximately **$1 billion** for the fund — one of the largest single-trade profits in commodities history.

## Timeline

| Date | Event |
|------|-------|
| 2005 (winter) | Hurricane Katrina disrupts Gulf gas production; spreads widen; prior winter sets template |
| 2006 Q1-Q2 | Hunter builds large long-March / short-April position across multiple contract years |
| 2006 Q2-Q3 | Position grows to ~40% of open interest in affected contract months |
| 2006 Aug | High storage levels, mild summer demand; spreads begin compressing |
| 2006 Sep 1-13 | Position losses accelerate; estimated mark-to-market loss approaches -$1B |
| **2006 Sep 14-15** | **Single-day losses of $560M+** as spreads compress further |
| 2006 Sep 16-17 (weekend) | Amaranth seeks emergency capital; talks with Goldman, Citadel, JPMorgan |
| 2006 Sep 18-20 | JPMorgan and Citadel jointly assume Amaranth's energy book in a "rescue" transaction; spreads compress further as the new counterparties continue unwinding |
| 2006 Sep 21 | Amaranth officially announces ~$6.6B in losses; fund unwinds |
| 2006 Sep-Oct | Centaurus crystallizes ~$1B profit |
| 2007 | CFTC and FERC enforcement actions against Hunter for attempted market manipulation; FERC initially sought a ~$30M penalty; litigation and settlements continued for years |

## Why it worked: the structural pattern

Counterparty-stress arbitrage — see [[counterparty-stress-arbitrage]] — has four conditions:

1. **A counterparty has a position larger than market-clearing liquidity.** Position size > daily turnover means an unwind cannot happen at current prices. The market must move against the unwinder to clear.
2. **The counterparty's capital structure exposes them to forced liquidation.** Margin calls, redemption pressure, regulatory limits, or reputational concerns force action at a specific date or price.
3. **The position is identifiable through public or semi-public data.** Large-trader reports, commitment-of-traders, on-chain data, exchange disclosures, prime-broker risk reports leaked or rumored.
4. **The price impact path of the unwind is predictable.** You know which assets they'll sell, in what order, and roughly when.

When all four align, you can position to receive the price impact of the forced unwind. The Amaranth case satisfied all four:

1. ✅ 40% of OI on certain contract months
2. ✅ Margin pressure from prime brokers; LP redemption rights
3. ✅ NYMEX large-trader reports + ICE position inference
4. ✅ Calendar-spread unwinds had to happen in March / April 2007 contract months

This same pattern recurred in [[2022-06-three-arrows-blowup]] (3AC), [[2022-11-ftx-collapse-arbitrage]] (FTX/Alameda), and the LRT depeg cascades documented in [[2026-04-kelp-stable-sympathy-depeg]]. The instruments differ; the structural logic does not.

## Why most traders cannot replicate it

The Amaranth/Arnold trade is widely cited but not easily repeated. Three specific barriers:

1. **Position-size visibility requires institutional infrastructure**. Arnold knew Amaranth's positioning through prime-broker conversations, large-trader reports, and inferential trading-desk intel. Retail traders rarely have this visibility — though [[on-chain-analytics]] now provides analogous transparency for crypto.
2. **You need fundamental conviction independent of the counterparty thesis**. Arnold's view of gas fundamentals had to be correct on its own merits. If you only short because you think someone is forced to sell, you can be right on the unwind but wrong on the eventual recovery direction.
3. **Sizing and timing are non-trivial**. If you size too aggressively too early, you take the same losses as the eventual loser before the unwind. If you wait too late, the spreads have already moved. The Centaurus structure was built over months, not days.

The crypto-era analogs (DeFi liquidations, stablecoin depegs, exploit-driven cascades) compress these barriers — large positions are visible on-chain; protocol mechanics make liquidation paths deterministic; oracle thresholds make timing precise. Per [[liquidation-cascade-arbitrage]] and [[counterparty-stress-arbitrage]], the framework is more accessible to retail / mid-tier funds in crypto than it ever was in commodities.

## Lessons for repeatability

1. **The biggest single-trade wins of the modern era are counter-trades against forced sellers.** Arnold 2006, Burry 2007-08 (against banks holding the toxic tranches), Ackman 2020 (against firms pricing zero recession risk), and the Soros 1992 trade all share this structure: identify someone whose capital structure forces them to act suboptimally, position to receive the impact.
2. **Position size disclosure is the most underused input.** NYMEX large-trader reports, CFTC commitment-of-traders, 13F filings, on-chain whale tracking — the data exists. Most traders don't read it.
3. **Capital structure → position predictability**. A hedge fund near peak drawdown with ~10% LP redemption gates is forced to unwind in defined windows. A protocol with hardcoded liquidation thresholds will sell at deterministic prices. Map the capital structure of the counterparty; the trade follows.
4. **Crypto compresses the timeline**. Where Amaranth's blowup played out over weeks, the equivalent pattern in crypto (3AC, Terra/Luna, FTX, KelpDAO contagion) plays out in hours to days. Faster opportunities, smaller windows.
5. **Asymmetric info beats fundamental analysis when convergence is forced**. Arnold didn't need to outpredict the weather; he needed to recognize that Hunter would have to sell regardless of the weather. The forced-seller has a non-fundamental marginal price that diverges from fundamental value.

## Modern analogs

Counterparty-stress arbitrage applied to current markets:

- **Crypto liquidation cascades**: Hyperliquid HLP vault stress, AAVE / Compound / Euler oracle-cascade events. See [[liquidation-cascade-arbitrage]].
- **DeFi exploits with bad-debt overhang**: per [[2026-04-18-kelp-layerzero-exploit]] — Aave's $123-230M bad debt set up a forced-liquidation path that traders pre-positioned around.
- **Forced-selling on margin in equities**: hedge-fund deleveraging events (Archegos 2021), prime-broker risk-rebalancing.
- **Validator-node stress on PoS chains**: large staking operators with redemption pressure.
- **Dual-currency note unwinds**: structured-product-driven forced selling in volatility / vol-of-vol products.

In each case the pattern is the same: counterparty A has a position that exceeds market-clearing liquidity at current prices, capital pressure forces unwind, the trade is to sell-then-buy or buy-then-sell on the structural path of that unwind.

## Related

- [[brian-hunter]] — the trader who blew up
- [[john-arnold]] — the trader who profited
- [[counterparty-stress-arbitrage]] — repeatable strategy generalization
- [[fastest-profitable-trades]] — pattern-extraction across history
- [[natural-gas]] — commodity context
- [[calendar-spread-arbitrage]] — the underlying spread structure
- [[liquidation-cascade-arbitrage]] — modern crypto analog
- [[2022-06-three-arrows-blowup]] — same structure, different decade and instrument
- [[2022-11-ftx-collapse-arbitrage]] — same structure, exchange version
- [[risk-management]] — sizing framework

## Sources

- CFTC investigation reports on Amaranth (2007-2008)
- Roger Lowenstein's reporting on Amaranth (NYT Magazine 2006)
- Hilary Till, "EDHEC Comments on the Amaranth Case: Early Lessons from the Debacle" (2007)
- Public reporting: Bloomberg, FT, WSJ September 2006-January 2007
- John Arnold profiles in Forbes, Texas Monthly (2007-2012)
