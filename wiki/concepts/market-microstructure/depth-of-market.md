---
title: "Depth of Market"
type: concept
created: 2026-04-15
updated: 2026-06-11
status: good
tags: [market-microstructure, liquidity]
aliases: ["Depth of Market", "DOM", "Level 2", "Level II", "Order Book"]
domain: [market-microstructure]
difficulty: intermediate
related: ["[[order-flow-analysis]]", "[[market-microstructure]]", "[[bid-ask-spread]]", "[[market-making]]", "[[liquidity]]", "[[liquidity-depth-regime]]", "[[crypto-market-regime-taxonomy]]", "[[open-interest]]", "[[slippage-modeling]]", "[[hyperliquid]]", "[[2025-10-crypto-liquidation-cascade]]"]
---

Depth of Market (DOM), also known as Level 2 data, is a real-time display of all outstanding buy and sell limit orders for a security at each price level. While Level 1 data shows only the best bid and best ask (the inside quotes), DOM reveals the full stack of orders waiting behind the top of book, providing a granular view of supply and demand at every price. DOM is a primary tool for short-term and [[day-trading|day traders]], scalpers, and anyone practicing [[order-flow-analysis]].

## Reading the Order Book

The DOM displays two columns: bids (buy orders) on one side and asks (sell orders) on the other, arranged by price level. Each price level shows the aggregate size (number of shares or contracts) available. A typical DOM view might show:

| Bid Size | Bid Price | Ask Price | Ask Size |
|---|---|---|---|
| | | 100.05 | 200 |
| | | 100.04 | 500 |
| | | 100.03 | 1,200 |
| 800 | 100.02 | | |
| 2,500 | 100.01 | | |
| 150 | 100.00 | | |

In this example, the inside spread is $100.02 bid / $100.03 ask. The ask at 100.03 has "thick" size (1,200 shares), suggesting a potentially significant resistance level. The bid at 100.01 has even thicker size (2,500 shares), acting as nearby support. A trader looking to buy might note that filling a large buy order would first consume the 1,200 shares at 100.03, then the 500 at 100.04, and so on -- the DOM reveals the likely slippage cost of executing different order sizes.

## Key DOM Concepts

**Thick levels** are price levels with unusually large resting order size. They can act as support (large bids) or resistance (large asks) because a significant amount of buying or selling must occur to "eat through" the level. **Thin levels** have minimal size and are easily cleared, meaning price can move through them quickly. **Pulling bids/asks** refers to large orders being withdrawn just before they would be filled -- a sign that the displayed size was not genuine intent to trade. **Spoofing** is the illegal practice of placing large orders with the intent to cancel them before execution, creating a false impression of supply or demand. Spoofing was formally banned in the US under the Dodd-Frank Act (2010) and has been the subject of high-profile enforcement actions, including the case against Navinder Sarao related to the 2010 Flash Crash.

## DOM in Practice

Day traders and scalpers use DOM to time entries and exits with precision. Common techniques include: watching for large resting orders to be absorbed (a large bid being consumed can signal a downward move is starting), identifying "iceberg" orders (large orders that only show a small visible portion, refilling as they are filled), and reading the rate of order flow hitting each side (aggressive buyers lifting offers vs. aggressive sellers hitting bids). DOM is most useful in liquid instruments where the order book is deep enough to provide meaningful information -- in thinly traded stocks, the DOM may contain only a few hundred shares at each level and can be easily manipulated.

## Depth Metrics

Reading the order book qualitatively ("thick here, thin there") is useful for discretionary timing, but systematic work requires quantifying depth. The standard measures are:

- **Top-of-book size** — the resting quantity at the best bid and best ask. The smallest, most fragile slice of the book; it can be refreshed or pulled in milliseconds and is the depth a small marketable order actually interacts with.
- **Cumulative depth within X bps of mid** — the total resting size summed across all price levels within a band (e.g. ±10 bps, ±25 bps, ±50 bps) of the mid price. This is the most decision-useful depth metric because it answers the practical question "how much can I trade before I move the price by X?" A book that holds 5,000 contracts within ±10 bps is far more robust than one with the same top-of-book but only 500 contracts within the band.
- **Bid/ask depth imbalance** — the ratio (or normalized difference) of cumulative bid depth to ask depth within a band: `imbalance = (bid_depth − ask_depth) / (bid_depth + ask_depth)`. Persistent positive imbalance means resting buyers outweigh resting sellers, which is often a short-horizon predictor of upward price pressure (more demand to absorb) — though it is also the exact signal spoofers try to fake.

Depth ties directly to execution cost. The cumulative-depth curve *is* the slippage curve: to estimate the cost of a market order you walk the book, consuming each level until the order is filled, and compare the average fill price to the arrival mid. Using the table above, a 1,000-share buy fills 1,200 available at 100.03 — so it clears entirely at 100.03 for ~1 bp of slippage; a 2,000-share buy takes the full 1,200 at 100.03 then 800 at 100.04, averaging ~100.034 for roughly 4 bps. The marginal cost rises as size climbs because each successive level is further from mid:

- A **thin** book produces a steep, convex slippage curve where even modest size pays large impact.
- A **deep** book produces a shallow curve where size is absorbed cheaply.

This walk-the-book calculation is the empirical foundation underneath any [[slippage-modeling|slippage model]] — square-root impact models are just smooth approximations to the depth profile, and they break down precisely when the real book is thinner than the model assumes.

## OI vs Depth — the Regime Signal

The single most important relationship for crypto-perp risk is **open interest versus order-book depth**. Open interest measures how much leveraged positioning is outstanding (see [[open-interest]]); resting depth measures how much passive liquidity stands ready to absorb flow. When OI grows faster than depth, the market becomes structurally fragile: there is a large stock of positions that *may be forced to transact* sitting on top of a shrinking pool of liquidity to transact *against*. Any forced flow — a liquidation cascade, a margin-driven deleverage, a large stop run — then moves price disproportionately, because the displaced size is large relative to the book it has to clear.

This OI-to-depth ratio was the clearest pre-crash warning ahead of the [[2025-10-crypto-liquidation-cascade|October 2025 liquidation cascade]]: leveraged open interest had climbed to multi-month highs while resting depth thinned, so when the first forced selling hit, each tranche of liquidations consumed the book, dropped the price, and triggered the next tranche — a self-reinforcing spiral. Depth-of-market data is the *mechanics* layer that makes this measurable; the full treatment of how to turn the OI-vs-depth ratio into a tradable regime signal — thresholds, baskets, and regime transitions — lives in [[liquidity-depth-regime]] and the broader [[crypto-market-regime-taxonomy]]. Treat this section as a pointer: DOM tells you *what* depth is and how to measure it, the regime pages tell you *what to do* when it diverges from OI.

## Depth Withdrawal

Depth is not a stable backdrop — it is actively managed, and it disappears exactly when it is most needed. [[market-making|Market makers]] widen quotes and pull size ahead of anticipated volatility (scheduled macro prints, large funding flips, oracle updates, weekend gaps) to avoid being run over by informed or forced flow. The result is **endogenous depth withdrawal**: the book is deepest in calm conditions and thinnest in stress, which is the opposite of what a naive backtest using average depth assumes.

This makes the distinction between **displayed depth** and **real depth** central. Displayed depth includes liquidity that will never actually trade: **spoofed** orders placed to manufacture imbalance and cancelled before they fill, and **fleeting liquidity** — quotes that exist for milliseconds as makers jockey for queue position. Conversely, real depth can exceed displayed depth where **iceberg / hidden** orders refill as they are hit. The practical takeaway: a depth metric computed from a single order-book snapshot overstates resilience, because much of the visible size will evaporate the moment aggressive flow arrives. Robust depth estimates require either time-averaged snapshots or, better, reconciling displayed depth against realized fills.

## Hyperliquid Specifics

Most of the limitations above stem from opacity — fragmented venues, hidden orders, microsecond instability that no public feed captures. Crypto perps on [[hyperliquid|Hyperliquid]] partially break this. Because Hyperliquid runs its order book on-chain, it exposes a transparent, per-minute **Level 2 order-book snapshot feed** across its perpetual markets, alongside on-chain open-interest and funding data. That combination is what makes the OI-vs-depth signal uniquely *trackable* here: an analyst can reconstruct cumulative depth within X bps of mid for every perp, divide by contemporaneous open interest, and watch the ratio evolve minute by minute — all from public on-chain data, with no exchange-proprietary feed required.

In practice the per-minute pipeline for a single perp looks like:

1. Pull the L2 snapshot; sum resting size on each side within ±X bps of mid to get `bid_depth` and `ask_depth`.
2. Compute cumulative depth `D = bid_depth + ask_depth` and the imbalance `(bid_depth − ask_depth) / D`.
3. Pull contemporaneous open interest `OI` for the same perp.
4. Track the fragility ratio `OI / D` over time and flag when it spikes.

The per-minute cadence is coarser than the millisecond churn of an equity DOM, which is actually an advantage for regime work: it filters out fleeting liquidity and gives a cleaner read on *persistent* resting depth. The main caveats remain — snapshots can still contain quotes pulled between intervals, and the on-chain book is one venue among several where the same asset trades — but Hyperliquid is the closest thing crypto has to a fully observable depth-and-positioning dataset, which is why the [[liquidity-depth-regime]] basket is built primarily on its data.

## Limitations

The modern DOM has significant limitations compared to when floor trading dominated. In today's fragmented electronic markets, the DOM for any single exchange shows only orders at that venue, not the consolidated book across all exchanges and dark pools. Hidden order types (iceberg, reserve, dark pool orders) do not appear in the DOM at all. [[high-frequency-trading|High-frequency traders]] can add and remove orders in microseconds, making the displayed book highly unstable -- what you see at one instant may be gone a millisecond later. For these reasons, many professional traders now supplement raw DOM data with aggregated order flow tools, cumulative delta analysis, and [[market-making|market maker]] positioning estimates.

## Related

- [[order-flow-analysis]] — the broader discipline of reading transaction and order data
- [[market-microstructure]] — the academic study of how orders become trades
- [[bid-ask-spread]] — the gap between best bid and best ask visible in DOM
- [[market-making]] — the firms that populate the order book
- [[liquidity]] — what DOM depth represents in concrete terms
- [[liquidity-depth-regime]] — the regime signal built on the OI-vs-depth ratio; uses this page as its mechanics reference
- [[crypto-market-regime-taxonomy]] — where the liquidity/depth regime sits among other crypto regimes
- [[open-interest]] — leveraged positioning; the numerator in the fragility ratio
- [[slippage-modeling]] — turning the cumulative-depth curve into expected execution cost
- [[hyperliquid]] — the venue whose transparent per-minute L2 feed makes depth trackable on-chain
- [[2025-10-crypto-liquidation-cascade]] — case study where rising OI against thinning depth preceded the crash

## Sources

- Harris, L. (2003). *Trading and Exchanges: Market Microstructure for Practitioners.* Oxford University Press — order books, depth, and the mechanics of limit-order markets
- O'Hara, M. (1995). *Market Microstructure Theory.* Blackwell — foundational treatment of liquidity and order flow
- Kyle, A. (1985). "Continuous Auctions and Insider Trading." *Econometrica* — price impact and market depth (Kyle's lambda)
- CFTC v. Navinder Sarao (2015) and U.S. Dodd-Frank Act (2010) anti-spoofing provisions — regulatory treatment of order-book manipulation
- Hyperliquid documentation — on-chain per-minute L2 order-book snapshot feed methodology
