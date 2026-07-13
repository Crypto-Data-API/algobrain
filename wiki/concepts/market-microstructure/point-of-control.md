---
title: "Point of Control (POC)"
type: concept
created: 2026-06-19
updated: 2026-06-20
status: good
tags: [market-microstructure, technical-analysis, indicators, volume, futures]
aliases: ["POC", "Point of Control", "Volume Point of Control", "VPOC", "Naked POC", "Virgin POC"]
related: ["[[volume-profile]]", "[[value-area]]", "[[value-area-high-and-low]]", "[[volume-nodes]]", "[[market-profile]]", "[[support-and-resistance]]", "[[vwap]]", "[[volume-profile-trading-strategy]]"]
domain: [market-microstructure, technical-analysis]
prerequisites: ["[[volume-profile]]", "[[value-area]]"]
difficulty: intermediate
---

The **Point of Control (POC)** is the single price level at which the most volume traded over a given period — the tallest bar in the [[volume-profile]] histogram. It is widely described as the session's "fairest price" or "fair value," because it is the price at which buyers and sellers facilitated the most two-sided trade. The POC acts as a magnet that price tends to rotate back toward, and as a structural [[support-and-resistance]] reference once price leaves it.

## Overview

In auction-market theory, the market searches for a price that facilitates trade. The price where the most contracts (or shares) changed hands is, by definition, the price the most participants agreed was acceptable — hence "control." The POC sits inside the [[value-area]] and, together with the [[value-area-high-and-low|VAH and VAL]], forms the three reference levels that anchor most [[volume-profile-trading-strategy|volume-profile strategies]].

There are two closely related constructs worth distinguishing:

- **Volume POC (VPOC)** — the price with the greatest *traded volume* (the standard meaning in [[volume-profile]]).
- **TPO POC** — in [[market-profile]], the price with the greatest *time* (time-price-opportunity count). The two usually sit at or near the same price but can diverge when a market spends a lot of time at one price without heavy volume.

## How it is computed

1. Aggregate all trades in the period into price buckets (the "row size" / tick increment of the profile).
2. Sum the volume in each bucket.
3. The bucket with the maximum summed volume is the POC.

Because the POC depends on the bucket size and the period, the same data can yield slightly different POCs on different settings. Platforms such as [[sierra-chart]], [[ninjatrader]], quantower, bookmap and tradingview let the user set the row size and the profile range (session, composite, or fixed/visible range).

## Session POC vs developing POC

- **Session (or final) POC** — the POC of a completed period (e.g. yesterday's full session). It is fixed and used as a reference level for the next session.
- **Developing POC** — the POC *as it forms* during the live session. It migrates as volume builds at new prices. Traders watch the direction of POC migration: a POC that keeps drifting higher through the day signals buyers accepting higher prices (value migrating up), and vice versa. A POC that stalls and "locks" in one place signals balance.

Tracking the developing POC is one of the cleaner real-time reads of who is winning the auction, complementing the [[vwap]] as a dynamic fair-value benchmark.

## Naked / virgin POC

A **naked POC** (also "virgin POC", nPOC) is a prior session's POC that price has **not yet returned to** since it formed. Because the POC marks a price of heavy agreement, an untested one tends to act as an unfinished-business magnet: price often gravitates back to it eventually. Traders use naked POCs as:

- **Targets** — trading *toward* an overhead or underlying naked POC, expecting price to reach it.
- **Reaction levels** — once price finally touches the naked POC, it frequently reacts (the level "fills" and stops being naked).

Naked POCs from higher-timeframe or composite profiles carry more weight than intraday ones. They are a staple of the naked-POC-retest setup in the [[volume-profile-trading-strategy]].

## How traders use the POC

| Use | Behaviour |
|-----|-----------|
| Magnet / target | On rotational days, price drifts back to the POC; a common first target for value-area rotation trades |
| Support / resistance | Once price is above the POC it can act as support; below it, as resistance |
| Value migration read | Direction of the developing POC over the session signals acceptance of higher/lower prices |
| Naked POC | Unfilled prior POC as a magnet target and later reaction level |
| Confluence | A POC that coincides with [[vwap]], a swing high/low, or a composite [[volume-nodes|HVN]] is a stronger level |

## Worked Example

The following is a qualitative, hypothetical illustration — no real prices are implied.

**Naked POC retest.** A trader reviews the prior session and notes its final POC sat in the upper part of the day's range. Overnight, price gaps lower and opens well below that level, leaving a **naked POC** (untested since it formed) hanging above the market. Because a POC marks a price of heavy prior agreement, the trader treats the naked POC as unfinished-business *magnet* and a likely *reaction* level:

1. **As a target.** Early in the session price stabilises and begins drifting up. With no opposing structure in between, the trader takes a long with the naked POC overhead as the objective, reasoning the auction is likely to revisit the unfilled fair-value price.

2. **As a reaction level.** Price reaches the naked POC. Now the level has "filled," so the trader expects a reaction. Watching the **developing POC** and [[cumulative-volume-delta|CVD]]: if volume stalls at the naked POC and CVD diverges (buying aggression fading into it), the trader fades the touch back toward the developing POC / [[value-area]] below. If instead price *accepts* through it — volume builds above and the developing POC migrates up — the naked POC has become support and the trader stands aside or flips bias to the long side.

The same level is first a target, then a decision point. The POC supplies the *where*; price action and CVD supply the *when* and *which way*.

## Limitations and risks

- **Parameter sensitivity** — the POC shifts with bucket size and profile range; a "POC" is only as meaningful as the period it summarises.
- **Single-print fragility** — on thin or fast markets the tallest bar can be a quirk of one large trade rather than genuine acceptance; cross-check with the broader profile and [[order-flow]].
- **Not a signal by itself** — the POC is context, not a trigger. It tells you where fair value is, not when to enter; confirmation from price action or [[cumulative-volume-delta|CVD]] is needed.
- **Session convention on 24/7 markets** — crypto has no natural session, so the POC depends entirely on an arbitrary daily cut; composite and fixed-range profiles are often more robust there.

## Related

- [[volume-profile]] — the histogram the POC is read from
- [[value-area]] — the ~70% acceptance band the POC sits inside
- [[value-area-high-and-low]] — the VAH/VAL boundaries around the POC
- [[volume-nodes]] — the POC is the single highest-volume node
- [[composite-profile]] — multi-session composite POCs are the heaviest references
- [[initial-balance]] — POC migration relative to the IB reads day type
- [[market-profile]] — TPO-based sibling with its own POC
- [[order-flow]] / [[cumulative-volume-delta]] — confirm reactions at the POC
- [[volume-profile-trading-strategy]] — setups built on the POC
- [[support-and-resistance]] — the POC acts as volume-based structural S/R
- [[vwap]] — complementary dynamic fair-value benchmark

## Sources

- Gap-finder Perplexity deep research, "Volume profile indicator as a trading strategy" (2026-06-19).
- Reference video: https://www.youtube.com/watch?v=YmygDgtoxO8
- General market knowledge.
