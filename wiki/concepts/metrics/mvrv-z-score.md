---
title: "MVRV Z-Score"
type: concept
created: 2026-06-24
updated: 2026-06-24
status: draft
tags: [crypto, bitcoin, indicators, valuation, market-microstructure, behavioral-finance]
aliases: ["MVRV Z-Score", "MVRV Z Score", "mvrv-zscore", "Bitcoin MVRV Z-Score"]
domain: [market-microstructure]
prerequisites: ["[[mvrv]]", "[[realized-price]]"]
difficulty: intermediate
related: ["[[mvrv]]", "[[realized-price]]", "[[nupl]]", "[[sopr]]", "[[on-chain-analysis]]", "[[market-capitalization]]", "[[bitcoin]]", "[[market-cycle]]", "[[glassnode]]", "[[cryptoquant]]", "[[behavioral-finance]]"]
---

The **MVRV Z-Score** is a standardised version of the [[mvrv|MVRV Ratio]] that expresses the gap between an asset's [[market-capitalization|market cap]] and its [[realized-price|realized cap]] in units of standard deviation. By normalising the spread, it produces a smoother cycle oscillator that has *historically* helped identify [[bitcoin]] cycle tops and bottoms more cleanly than the raw MVRV ratio. It is a staple [[on-chain-analysis|on-chain]] cycle gauge on platforms such as [[glassnode]] and [[cryptoquant]].

## How It Is Computed

```
MVRV Z-Score = (Market Cap − Realized Cap) / stddev(Market Cap)
```

- **Market Cap − Realized Cap** is the aggregate *unrealized* profit/loss in absolute terms — how far market value has stretched away from the supply's [[realized-price|cost basis]].
- **stddev(Market Cap)** is the standard deviation of the historical market-cap series, which rescales that gap into comparable units across time.

Dividing the unrealized-profit spread by the volatility of market cap means the Z-Score grows large only when price has stretched *unusually* far above realized cap relative to its own historical variability, rather than simply because the asset is bigger.

## Interpretation / How Traders Use It

The MVRV Z-Score is read as a cycle-extreme oscillator with informal "zones":

- **High / "red" zone** (deep positive Z-Score): market value sits many standard deviations above realized cap — extreme aggregate unrealized profit. *Historically*, very high readings have coincided with overheated, late-cycle conditions and elevated distribution risk.
- **Mid zone**: market value is moderately above realized cap — neutral-to-trending conditions.
- **Low / "green" zone** (Z-Score at or below zero, approaching/under realized cap): market value at or below the supply's cost basis. *Historically*, deeply depressed readings have aligned with capitulation and cycle-low accumulation phases.

The specific numeric band edges drift between cycles, so they should be treated qualitatively, not as fixed thresholds. Analysts typically confirm a red/green Z-Score signal with [[sopr]] (profit/loss actually realised), [[nupl]] (the percentage-based unrealized P/L), and supply-age tools like [[hodl-waves]] and flow metrics like [[exchange-netflow]].

## Illustrative Example

When [[bitcoin]] is deep in a bull market and price has run far above the average price the supply last moved, market cap pulls sharply above realized cap and the gap is large relative to the historical volatility of market cap — pushing the Z-Score into the upper "red" zone and flagging an overextended, top-risk environment. Conversely, in a deep bear market, price falls toward or below realized cap, the gap shrinks or goes negative, and the Z-Score sinks into the "green" zone — the kind of reading that has historically marked exhaustion and bottoming, without pinpointing the exact low.

## Limitations and Pitfalls

- **Lagging by construction**: like [[mvrv]], the Z-Score is a *valuation* measure that confirms regimes rather than calling exact turns; it can sit in an extreme zone for an extended stretch.
- **Standard-deviation window sensitivity**: the denominator depends on the lookback window used for `stddev(Market Cap)`. Different providers and window choices shift the absolute Z values, so the same date can read differently across sources.
- **Cross-cycle drift**: the Z-Score levels that flagged previous tops and bottoms have compressed as the asset has matured (smaller percentage swings on a larger base), so historical red/green edges are not guaranteed to repeat.
- **Lost-supply and entity caveats**: it inherits realized cap's weaknesses — lost coins, dormant supply, and internal exchange transfers distort the cost basis (see [[mvrv]] and [[on-chain-analysis#Leading vs Lagging, and Data Caveats]]).
- **Best for mature assets**: most reliable for [[bitcoin]]; on thin or newer chains the realized cap and its volatility are noisy, weakening the signal.

## Related

- [[mvrv]] — The raw ratio this metric standardises
- [[realized-price]] — Realized cap underlies both numerator and the cost-basis concept
- [[nupl]] — The percentage-based expression of the same unrealized P/L spread
- [[sopr]] — Confirms whether profit/loss is actually being realised
- [[on-chain-analysis]] — Parent mechanics page
- [[market-cycle]] — The cycle the Z-Score is read against
- [[hodl-waves]] — Supply-age companion for cycle context
- [[glassnode]], [[cryptoquant]] — Providers that popularised the metric

## Sources

General market knowledge; no specific wiki source ingested yet.
