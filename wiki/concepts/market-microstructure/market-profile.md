---
title: "Market Profile"
type: concept
created: 2026-04-15
updated: 2026-06-11
status: good
tags: [market-microstructure, technical-analysis, indicators, futures]
aliases: ["Market Profile", "TPO Chart", "Time Price Opportunity", "Steidlmayer Profile", "Auction Market Theory"]
related: ["[[volume-profile]]", "[[value-area]]", "[[vwap]]", "[[order-flow]]", "[[support-and-resistance]]", "[[price-discovery]]", "[[liquidity]]", "[[footprint-chart]]"]
domain: [market-microstructure, technical-analysis]
prerequisites: ["[[price-discovery]]", "[[support-and-resistance]]"]
difficulty: intermediate
---

Market Profile is a charting and market-analysis methodology developed by J. Peter Steidlmayer at the Chicago Board of Trade in the 1980s that organizes a session's trading into a horizontal distribution of **Time Price Opportunities (TPOs)** — letter-coded blocks showing how much *time* the market spent at each price. It is the foundational framework behind auction market theory: it treats price as the market's advertising mechanism and value as the range where two-sided trade is accepted, and it underpins the more modern, volume-weighted [[volume-profile]].

## Overview

Market Profile is built on **auction market theory**: a market is a continuous two-way auction whose purpose is to facilitate trade by finding prices at which buyers and sellers transact. Price moves *away* from value to advertise opportunity and is rejected; it rotates *back* toward value when that advertising attracts the opposite side. The profile is the visual record of this process for a single session, revealing where the auction found acceptance (a balanced, well-traded area) versus rejection (thin tails that price moved through quickly).

The defining difference from [[volume-profile]] is the unit of measurement. Market Profile counts **time** — each 30-minute bracket of the session is assigned a letter (A, B, C, …), and a letter is printed at every price touched during that bracket. Stacking the letters horizontally produces a roughly bell-shaped distribution. Volume Profile instead counts **traded contracts** at each price. Time and volume distributions usually agree, but where they diverge (high time / low volume, or vice versa) experienced traders read a clue about whether participation was genuine commitment or mere drifting.

## How It Works

### Building the profile
1. Divide the session into 30-minute periods, each labeled with a letter (A = first half hour, B = second, …).
2. For each period, print its letter at every price the market traded during that period.
3. Push all letters left so they stack against the price axis. Prices touched in many periods accumulate many letters (a wide row); prices touched in only one period show a single letter (a thin row).

### Key structures
- **Point of Control (POC)** — the price with the most TPOs (the longest row), i.e. the price that attracted the most time. The session's "fairest" price.
- **Value Area (VA)** — the contiguous range around the POC containing ~70% of the session's TPOs (one standard deviation), bounded by the **Value Area High (VAH)** and **Value Area Low (VAL)**. See [[value-area]].
- **Initial Balance (IB)** — the price range of the first two periods (first hour, letters A and B). A wide IB suggests an early-committed, often trend day; a narrow IB suggests indecision and room for later range extension.
- **Range extension** — any move beyond the Initial Balance high or low later in the session, signaling that one side took control after the open.
- **Single prints** — prices touched in only one period (a single letter), marking fast, one-sided moves. **Tails** (single prints at the profile extremes) mark aggressive rejection by responsive buyers (lower tail) or sellers (upper tail).
- **Poor highs / poor lows** — extremes with multiple TPOs rather than a clean tail, suggesting the auction did not finish and is likely to be revisited.

### Day types
Steidlmayer classified sessions by profile shape, which guides expectations:
- **Normal / Normal-variation day** — balanced bell shape, range mostly set by the Initial Balance; favors fading the extremes back to the POC.
- **Trend day** — elongated, thin profile with continuous range extension in one direction; the open is near one extreme and the close near the other. Fading is dangerous.
- **Double-distribution day** — two separate bell shapes connected by single prints, where the market migrated from one value area to a new one (a "value migration").
- **Neutral day** — range extension on *both* sides of the Initial Balance, indicating two-sided indecision.

## Trading Relevance

Market Profile gives a trader a language for *context* rather than a buy/sell signal. The core read is whether the market is **balanced** (rotating inside a value area — fade the edges, target the POC) or **imbalanced/trending** (accepting price away from prior value — trade with the extension, do not fade). Practical applications mirror those of [[volume-profile]]:

- **Open relative to prior value.** Opening *inside* the prior session's value area implies a rotational day (mean-revert between VAH and VAL toward the POC). Opening *outside* and being rejected sets up a return to the value-area edge; opening outside and being *accepted* (the "80% rule" failing) flags a trend day.
- **Initial Balance as a risk frame.** The first hour's range anchors stop placement and the expectation for range extension.
- **Value migration.** Successive days' POCs and value areas drifting in one direction confirm a developing trend; overlapping value areas confirm balance/consolidation, useful for swing context.
- **Tails and single prints** as [[support-and-resistance]]: clean tails mark levels defended by responsive participants and tend to hold; poor extremes tend to be revisited.

Market Profile originated in, and remains most popular for, **futures** (index, treasury, energy, agricultural) where session structure is well defined, but the framework is applied to equities and 24/7 crypto by choosing a session convention. Most platforms (Sierra Chart, TradingView, NinjaTrader, Bookmap) now render both the TPO Market Profile and the volume-based [[volume-profile]] side by side; many traders read them together and rely on the [[vwap]] as an intraday fair-value complement to the static POC.

## Related

- [[volume-profile]] — the volume-weighted descendant of Market Profile; same value-area concepts, different unit
- [[value-area]] — the ~70% acceptance range (POC, VAH, VAL)
- [[vwap]] — dynamic intraday fair-value benchmark used alongside the POC
- [[order-flow]] — trade-by-trade detail inside the profile structure
- [[footprint-chart]] — bid/ask volume within each bar, a finer microstructure view
- [[support-and-resistance]] — tails and HVN/LVN equivalents as structural levels
- [[price-discovery]] — the auction process the profile visualizes

## Sources

- J. Peter Steidlmayer & Steven Hawkins, *Steidlmayer on Markets: Trading with Market Profile* (Wiley).
- James Dalton, Eric Jones & Robert Dalton, *Mind Over Markets: Power Trading with Market Generated Information*.
- CME Group educational material on Market Profile and auction market theory.
- [[book-technical-analysis-of-the-financial-markets]] — context for distribution-based analysis.
