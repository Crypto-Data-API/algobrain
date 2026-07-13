---
title: "Value Area"
type: concept
created: 2026-04-15
updated: 2026-06-22
status: excellent
tags: [market-microstructure, technical-analysis, indicators, futures]
aliases: ["Value Area", "Value Area High", "Value Area Low", "VAH", "VAL", "value-area"]
related: ["[[market-profile]]", "[[volume-profile]]", "[[point-of-control]]", "[[vwap]]", "[[support-and-resistance]]", "[[order-flow]]", "[[price-discovery]]", "[[liquidity]]"]
domain: [market-microstructure, technical-analysis]
prerequisites: ["[[market-profile]]", "[[support-and-resistance]]"]
difficulty: intermediate
---

The **Value Area (VA)** is the contiguous price range in which roughly **70% of a session's trading activity** (time or volume) occurred — approximately one standard deviation around the **[[point-of-control|Point of Control (POC)]]**. It is the central concept of [[market-profile]] and [[volume-profile]], representing the prices the auction accepted as "fair," where two-sided trade was facilitated most heavily.

## Overview

In auction market theory, a market spends most of its time near prices where buyers and sellers agree to transact, and only briefly visits prices it rejects. The Value Area captures that zone of acceptance. It is bounded by two reference levels traders watch closely:

- **Value Area High (VAH)** — the upper boundary; the highest price still inside the 70% band.
- **Value Area Low (VAL)** — the lower boundary; the lowest price still inside the band.
- **[[point-of-control|Point of Control (POC)]]** — the single price with the most TPOs (Market Profile) or the most traded volume (Volume Profile); the "fairest" price of the session, usually sitting inside the VA.

| Reference level | Definition | Typical trader use |
|-----------------|------------|--------------------|
| **VAH** | Top of the 70% band | Upper fade/short level on balanced days; breakout trigger on trend days |
| **[[point-of-control\|POC]]** | Single most-traded price | "Magnet" / mean-reversion target; pivot for bias |
| **VAL** | Bottom of the 70% band | Lower fade/long level on balanced days; breakdown trigger on trend days |
| **Naked/virgin POC** | A prior session's POC never revisited | High-probability target on a later day |

## How It Is Calculated

The standard construction (the "70% rule") works outward from the POC:

1. Identify the POC — the price level with the greatest time (TPO count) or volume.
2. Sum the TPOs/volume of the two price levels immediately above the POC and the two immediately below.
3. Add whichever pair (upper or lower) contributes more to the running total.
4. Repeat, always extending toward the side with the larger increment, until the accumulated total reaches ~70% of the session's TPOs/volume.
5. The highest and lowest prices included become the VAH and VAL.

The 70% threshold approximates one standard deviation of a normal distribution, treating the session's traded distribution as roughly bell-shaped. Market Profile counts **time** (30-minute TPO brackets); Volume Profile counts **contracts traded**, producing a Volume Value Area. The two usually agree closely.

### Worked Example

*Illustrative, rounded numbers.* Suppose a futures session trades a total of **10,000 contracts** distributed across price levels (each tick on its own row). The 70% target is **7,000 contracts**. Construction:

| Price | Volume | Step |
|-------|--------|------|
| 102 | 300 | |
| 101 | 900 | added 4th (left side larger) |
| 100.5 | 1,400 | added 3rd |
| **100 (POC)** | **2,000** | start: most-traded price |
| 99.5 | 1,800 | added 1st (compare 1,800+? vs 1,400+? → larger) |
| 99 | 1,100 | added 2nd |
| 98 | 500 | |

Start at the [[point-of-control|POC]] = 100 (2,000 contracts). Compare the *pair* of levels above (100.5 + 101 = 1,400 + 900 = 2,300) versus the pair below (99.5 + 99 = 1,800 + 1,100 = 2,900) and add whichever side adds more. Working outward and accumulating until the running total crosses 7,000 contracts, the included range settles at roughly **VAL = 99 up to VAH = 100.5**, with the POC at 100. The thin tails at 102 and 98 fall *outside* value — prices the auction visited but rejected.

The practical takeaway: value clusters where two-sided trade was heaviest, and the edges (VAH/VAL) mark where the market started saying "too expensive" or "too cheap."

## Trading Relevance

The Value Area gives traders a context framework rather than a direct buy/sell signal — it answers "is the market balanced or trending, and where is fair value?"

- **Mean reversion inside balance.** When price is rotating within the VA, traders fade the edges: short near the VAH, long near the VAL, targeting the POC. The POC acts as a magnet on rotational ("normal") days.
- **The "80% rule."** A widely used Market Profile heuristic: if price opens outside the prior day's VA but then trades back inside and spends two consecutive 30-minute periods inside, there is a high probability (~80% in Steidlmayer/Dalton lore) it will traverse the entire VA to the opposite edge.
- **Open relative to prior VA.** Opening *inside* the previous session's VA implies a rotational day; opening *outside* and being accepted flags potential trend continuation.
- **VAH/VAL as [[support-and-resistance]].** These boundaries are common stop-placement and target levels; acceptance beyond them signals value migration to a new range.
- **Value migration.** A sequence of higher VAs (rising POC, VAH, VAL) confirms an uptrend; overlapping VAs confirm balance/consolidation — useful for swing-timeframe context.

The concept originated in [[futures]] markets (index, treasury, energy, agricultural), where session structure is well defined, but is applied to equities and 24/7 crypto by adopting a session convention. Platforms such as Sierra Chart, TradingView, NinjaTrader, and Bookmap plot the VAH, VAL, and POC automatically and carry "developing VA" lines that update intraday, often read alongside the [[vwap]] as a complementary dynamic fair-value benchmark.

## How Traders Use This

- **Set a daily bias from the open.** Open inside the prior VA → expect rotation/mean reversion; trade the edges back toward the POC. Open outside and hold → expect trend/continuation away from old value.
- **Fade the edges in balance.** On rotational days, short tests of VAH and long tests of VAL with a tight stop just beyond the level, targeting the [[point-of-control|POC]] first, then the opposite edge.
- **Trade acceptance vs. rejection.** A quick poke beyond VAH/VAL that snaps back is *rejection* (fade it); sustained trade beyond with building volume is *acceptance* (value is migrating — go with it).
- **Use naked POCs as targets.** Unrevisited prior-session POCs act as magnets; many traders place targets there.
- **Confluence with [[vwap]] and [[support-and-resistance]].** A VAL that lines up with [[vwap]] and a prior swing low is a far stronger long zone than any one level alone.
- **Stack timeframes.** Read the developing intraday VA inside the weekly/composite VA so a mean-reversion fade isn't taken against a larger trend.

## Common Pitfalls and Risks

- **Fading a trend day.** The single biggest mistake: shorting VAH on a strong trend day where price simply keeps accepting higher value. Edges only "hold" on balanced/rotational days — confirm the day type first.
- **The 70% / 80% rules are heuristics, not laws.** The widely-quoted ~80% completion figure is lore from the Market Profile literature, not a guaranteed probability; treat it as a tendency, size accordingly, and always use stops.
- **Session definition matters.** In 24/7 [[crypto]] and overnight [[futures]], where you draw the session start radically changes the VA. Be consistent and know which session your platform is using (RTH vs. ETH).
- **Developing VA repaints intraday.** The "developing" value area shifts as volume accumulates; levels read at midday may not be where they end the session.
- **Low-volume / news distortion.** Thin holiday sessions or news spikes produce ragged, untrustworthy distributions; the VA is most reliable in liquid, two-sided auctions.
- **Volume vs. TPO disagreement.** When the Volume VA and TPO (time) VA diverge sharply, the auction is unusual (e.g., a fast one-sided move) — a signal in itself, not noise to ignore.

## Related

- [[market-profile]] — the parent framework; VA is its core acceptance measure
- [[volume-profile]] — volume-weighted version; produces a Volume Value Area
- [[point-of-control]] — the most-traded price at the center of the VA
- [[vwap]] — dynamic intraday fair-value benchmark used alongside the static POC
- [[support-and-resistance]] — VAH/VAL act as structural levels
- [[order-flow]] — trade-by-trade detail inside the value area
- [[price-discovery]] — the auction process the VA summarizes

## Sources

- J. Peter Steidlmayer & Steven Hawkins, *Steidlmayer on Markets: Trading with Market Profile* (Wiley).
- James Dalton, Eric Jones & Robert Dalton, *Mind Over Markets: Power Trading with Market Generated Information*.
- CME Group educational material on Market Profile and the value area.
