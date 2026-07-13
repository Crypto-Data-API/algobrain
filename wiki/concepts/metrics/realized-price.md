---
title: "Realized Price & Realized Cap"
type: concept
created: 2026-06-24
updated: 2026-06-24
status: draft
tags: [crypto, bitcoin, indicators, valuation, market-microstructure, behavioral-finance]
aliases: ["Realized Price", "Realized Cap", "Realized Capitalization", "realized-cap", "realized-capitalization", "Realised Price", "Realised Cap"]
domain: [market-microstructure]
prerequisites: ["[[on-chain-analysis]]", "[[market-capitalization]]"]
difficulty: intermediate
related: ["[[mvrv]]", "[[mvrv-z-score]]", "[[nupl]]", "[[sopr]]", "[[on-chain-analysis]]", "[[market-capitalization]]", "[[bitcoin]]", "[[market-cycle]]", "[[hodl-waves]]", "[[glassnode]]", "[[cryptoquant]]", "[[behavioral-finance]]"]
---

**Realized Price** and **Realized Cap** (realized capitalization) are foundational [[on-chain-analysis|on-chain]] valuation measures that value each coin not at the current market price but at the **price it last moved** on-chain. Realized cap sums those last-moved values across the entire supply, giving the market's aggregate **cost basis**; realized price divides that by supply to express it as a single per-coin figure. Together they underpin a whole family of derived metrics — [[mvrv|MVRV]], [[mvrv-z-score|MVRV Z-Score]], and [[nupl|NUPL]] — and the realized price itself is widely watched as a dynamic support/resistance level. Both were popularised by analytics firms such as [[glassnode]] and [[cryptoquant]] (and originate in work by Coin Metrics).

## How It Is Computed

```
Realized Cap   = Σ ( each coin (or UTXO) × price at the time it last moved on-chain )
Realized Price = Realized Cap / Circulating Supply
```

The intuition: every coin carries an on-chain "timestamp of last movement," and the asset's price at that moment is treated as the cost basis for that coin. By valuing the whole supply at its respective last-moved prices instead of today's spot price, realized cap effectively *discounts* coins that have not moved in a long time at their (usually much lower) acquisition price, and weights recently transacted coins near current prices.

Contrast with conventional [[market-capitalization]]:

- **Market cap** = current price × supply — values *every* coin at today's price.
- **Realized cap** = Σ (coin × last-moved price) — values *each* coin at its own cost basis.

Because of this, realized cap is far less volatile than market cap: it only changes when coins actually move (and re-anchor at a new price), so it behaves like a slow-moving "aggregate purchase price" of the market.

> **Note:** *Realized cap* and *realized capitalization* are aliases for the same quantity; *realized price* is realized cap normalised per coin.

## Interpretation / How Traders Use It

- **Aggregate cost basis / break-even line**: realized price is the average price at which the supply was last acquired. When market price trades **above** realized price, the market is in aggregate profit; **below**, in aggregate loss. This makes the realized price a natural dividing line between bull and bear regimes.
- **Dynamic support and resistance**: in uptrends the realized price has *historically* acted as a support floor (dip buyers defend the aggregate cost basis); in downtrends it acts as overhead resistance. Reclaiming or losing the realized price is treated as a meaningful regime event in a [[market-cycle]].
- **Denominator for valuation metrics**: realized cap is the denominator of [[mvrv]] and the subtrahend in [[nupl]] and [[mvrv-z-score]]. Understanding realized cap is a prerequisite for reading those.
- **Cohort cost bases**: restricting the calculation to coin-age cohorts yields **Short-Term Holder** and **Long-Term Holder realized price**, revealing the cost basis of recent speculators versus seasoned holders — a powerful overlay alongside [[hodl-waves]] and [[sopr]].

## Illustrative Example

Imagine [[bitcoin]]'s supply: a large block of coins last moved years ago at low prices, and a smaller block changed hands recently near current prices. Market cap values *all* of it at today's price, but realized cap values the old block at its low acquisition price — so realized cap (and thus realized price) sits well below spot. If spot price then falls during a bear market toward that realized price, analysts watch closely: a bounce off the realized price signals the aggregate cost-basis floor is holding, while a decisive break below it pushes the average holder into loss and historically precedes capitulation conditions (visible in [[sopr]] dropping below 1 and [[nupl]] turning negative).

## Limitations and Pitfalls

- **Lost and dormant supply**: coins that are provably lost or have not moved for a decade are still valued at their (very low) last-moved price, dragging realized cap downward and biasing every derived metric ([[mvrv]], [[nupl]]). There is no on-chain way to fully distinguish "lost" from "diamond-handed HODL."
- **Internal transfers pollute cost basis**: an exchange or custodian reshuffling coins between its own wallets resets the "last-moved price" without any real change of ownership. **Entity-adjusted** realized cap attempts to filter these, but the entity labels are provider-produced and revised over time (see [[on-chain-analysis#Leading vs Lagging, and Data Caveats]]).
- **Account-based vs UTXO chains**: realized cap is cleanest on UTXO chains like [[bitcoin]]; on account-based chains (e.g. Ethereum) the "last-moved price" must be approximated, making the figure noisier.
- **Slow to update**: because it only changes when coins move, realized cap can lag genuine shifts in holder cost basis during fast accumulation/distribution.
- **Provider differences**: dust filters, exchange labelling, and supply definitions differ between [[glassnode]], [[cryptoquant]], and others, so realized-price levels for the same date can vary across sources.

## Related

- [[mvrv]] — Uses realized cap as its denominator
- [[mvrv-z-score]] — Standardises the market-cap-minus-realized-cap spread
- [[nupl]] — Expresses unrealized profit/loss relative to market cap
- [[sopr]] — Per-spend version of the realized-vs-paid idea
- [[market-capitalization]] — The spot-priced counterpart contrasted here
- [[on-chain-analysis]] — Parent mechanics page
- [[market-cycle]] — Realized price as a bull/bear dividing line
- [[hodl-waves]] — Supply-age companion for cohort cost-basis context
- [[glassnode]], [[cryptoquant]] — Providers that popularised the metric

## Sources

General market knowledge; no specific wiki source ingested yet.
