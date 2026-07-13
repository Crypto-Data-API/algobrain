---
title: Mark Price
type: concept
created: 2026-06-24
updated: 2026-06-24
status: good
tags: [market-microstructure, derivatives, leverage, margin, liquidity]
aliases: [mark-price, marking-price, fair-price, fair-mark-price]
domain: [market-microstructure]
prerequisites: ["[[perpetual-futures]]", "[[spot-price]]", "[[funding-rate]]"]
difficulty: intermediate
related:
  - "[[crypto-perpetual-futures]]"
  - "[[maintenance-margin]]"
  - "[[liquidation]]"
  - "[[liquidation-cascade]]"
  - "[[funding-rate]]"
  - "[[spot-price]]"
  - "[[order-book]]"
  - "[[oracle-manipulation]]"
---

# Mark Price

The mark price is the reference price a derivatives venue uses to value open positions for unrealized PnL and to trigger [[liquidation]], in place of the volatile last-traded price. It is typically anchored to an external [[spot-price]] index plus a basis component, so that brief order-book distortions on a single venue do not unfairly liquidate traders.

## Why a Separate Price Exists

On a leveraged venue, the most recent trade price can be pushed far away from fair value by a single large market order, a thin [[order-book]], or deliberate [[oracle-manipulation]]. If liquidations were driven by the last-traded price, a momentary downward wick could wipe out positions that are otherwise solvent, and an attacker could profit by deliberately spiking the book. The mark price decouples position valuation from the noisy last trade, making liquidations reflect the broader market rather than one venue's microstructure.

## How Venues Compute It

Implementations vary by venue, but the common ingredients are:

- **Index price** — a composite [[spot-price]] aggregated across several large, liquid spot exchanges. Aggregation and outlier-trimming (e.g. dropping the highest/lowest constituent) make the index hard to manipulate on any single venue.
- **Basis / funding component** — for [[crypto-perpetual-futures]], the mark price adds a decaying basis or a fair-value premium so that the contract's mark tracks where the perpetual *should* trade relative to spot, consistent with the [[funding-rate]] mechanism. As funding pulls the contract back toward spot, the basis component shrinks toward zero.
- **Smoothing** — many venues apply an exponentially weighted moving average or a median over a short window to filter single-tick spikes.

A common conceptual form is:

```
mark_price = index_price + decayed_basis
```

where `decayed_basis` reflects the perpetual's premium/discount to the index and decays over the funding interval.

## Worked Illustrative Example

Suppose the aggregated spot index for an asset is 100, and the perpetual is trading at a small premium so the venue's basis component is +0.4. The mark price is 100.4. A trader with a long position has their unrealized PnL and margin checked against 100.4 — not against a one-off trade that briefly printed at 97 on a thin book. Because the mark stayed near fair value, that trader is not liquidated by the wick. (All figures here are illustrative; exact index constituents and basis formulas vary by venue.)

## How Traders Use It / Why It Matters

- **PnL and equity** — your unrealized PnL, account equity, and [[maintenance-margin]] ratio are computed from the mark price, not the last trade you see scroll past.
- **Liquidation distance** — your true liquidation level is the mark price at which equity falls below maintenance margin, so traders track the gap between mark and their liquidation price rather than the last-traded ticker.
- **Funding and arbitrage** — because mark embeds the perpetual basis, it interacts directly with [[funding-rate]] and underpins [[funding-rate-arbitrage]] and [[delta-neutral]] positioning.

## Risks and Pitfalls

- **Index is only as robust as its constituents** — if the underlying spot venues are themselves thin or manipulable, the index (and therefore mark) can still be moved; see [[oracle-manipulation]].
- **Mark can diverge from the venue's own book** — during stress, the price you can actually trade at on one venue may be well away from the mark, so the mark can show you "in profit" at a level you cannot exit at.
- **Liquidation still happens at mark** — a calm-looking last price does not protect you if the *index* moves; [[liquidation-cascade]] events are driven by the mark/index, not the local ticker.
- **Venue discretion** — formulas, smoothing windows, and constituent lists are venue-specific and can change; never assume one venue's mark logic applies to another.

## Related

- [[crypto-perpetual-futures]]
- [[maintenance-margin]]
- [[liquidation]]
- [[liquidation-cascade]]
- [[cross-margin-vs-isolated-margin]]
- [[funding-rate]]
- [[spot-price]]
- [[order-book]]
- [[oracle-manipulation]]
- [[perpetual-futures]]

## Sources

General market knowledge; no specific wiki source ingested yet.
