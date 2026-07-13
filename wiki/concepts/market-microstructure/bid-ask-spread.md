---
title: Bid-Ask Spread
type: concept
created: 2026-04-06
updated: 2026-07-01
status: good
tags: [market-microstructure, liquidity, slippage]
aliases: [bid-ask, bid-offer-spread, bid-ask-spreads]
domain: [market-microstructure]
prerequisites: ["[[order-book]]", "[[liquidity]]"]
difficulty: beginner
related:
  - "[[spread]]"
  - "[[order-book]]"
  - "[[liquidity]]"
  - "[[market-maker]]"
  - "[[slippage]]"
  - "[[book-trading-and-exchanges]]"
---

# Bid-Ask Spread

The bid-ask spread is the difference between the highest price a buyer is willing to pay (bid) and the lowest price a seller is willing to accept (ask) for an asset.

## Overview

The bid-ask spread is the most fundamental measure of [[liquidity]] and represents the minimum transaction cost of executing a round-trip trade (Source: [[book-trading-and-exchanges]]). It is the primary revenue source for [[market-maker]]s, who profit by continuously buying at the bid and selling at the ask.

## How It Works

- **Bid**: The best (highest) price at which a buyer is willing to purchase. If you sell at market, you receive the bid.
- **Ask (offer)**: The best (lowest) price at which a seller is willing to sell. If you buy at market, you pay the ask.
- **Spread**: Ask - Bid. Commonly expressed in absolute terms ($0.01) or as a percentage of the mid-price.
- **Mid-price**: (Bid + Ask) / 2. The theoretical "fair value" between buyer and seller.

## What Determines the Spread

The spread a [[market-maker]] quotes decomposes into three classic components (Source: [[book-trading-and-exchanges]]):

1. **Order-processing costs** — the operational cost of providing the quote (exchange [[fees]], technology, clearing).
2. **Inventory-holding costs** — compensation for the risk a market maker bears while holding an unwanted position before it can be offloaded.
3. **[[adverse-selection]] costs** — the loss a market maker expects from trading against better-informed counterparties (insiders, faster traders). This component widens spreads in names where informed trading is likely and is why spreads gap out around news and earnings.

## What the Spread Signals

- **Tight spread (small)**: High liquidity, active market-making, many participants, low uncertainty. Examples: major stocks (AAPL), BTC/USDT on top exchanges.
- **Wide spread (large)**: Low liquidity, few participants, high uncertainty or risk. Examples: small-cap stocks, illiquid altcoins, during market panics.
- **Spread widening**: Often a leading indicator of market stress, reduced confidence, or impending volatility (Source: [[book-trading-and-exchanges]]).

## Trading Relevance

Every market order crosses the spread, making it a guaranteed cost. For active traders, the spread can dwarf commission costs. When evaluating a trading venue or asset, always check the typical spread -- a strategy that requires frequent entries and exits becomes less viable in wide-spread markets. Limit orders placed inside the spread can achieve better fills but risk non-execution.

## Worked Example (Illustrative)

The numbers below are hypothetical and chosen only to make the cost arithmetic concrete.

**Tight-spread stock.** A liquid stock is quoted **50.00 bid / 50.02 ask** (mid 50.01). You buy 1,000 shares at market for $50.02 and immediately sell at market for $50.00:

- Round-trip spread cost = (50.02 − 50.00) × 1,000 = **$20**, or about 4 bps (0.04%) of notional. The half-spread you "lose" the instant you buy is $0.01/share = $10.

**Wide-spread small-cap.** A thinly traded micro-cap is quoted **5.00 bid / 5.20 ask** (mid 5.10). The same round trip on 1,000 shares:

- Round-trip spread cost = (5.20 − 5.00) × 1,000 = **$200**, or about 3.9% of notional — roughly **100× more expensive** than the liquid name, before any [[market-impact]] from walking the [[order-book|book]].

The takeaway: a strategy that needs to enter and exit frequently can be profitable in the first stock and structurally unviable in the second, even with identical commissions. Spread cost scales with how often you trade and how illiquid the name is, not with how good your thesis is.

## How to Reduce Spread Cost

- **Use limit orders inside the spread.** Posting a buy at 50.01 (the mid) earns the spread instead of paying it — but risks non-execution if the market moves away.
- **Trade liquid hours.** Spreads are widest at the open, near the close, in [[extended-hours-trading|pre/post-market]], and around news; they are tightest during the deep, high-volume midday session.
- **Avoid crossing on size.** Large orders consume multiple price levels, so the *effective* spread is wider than the top-of-book quote (see [[market-impact]] and [[slippage]]).
- **Prefer instruments with natural market-making competition** — major index ETFs and large caps over illiquid single names or far out-of-the-money [[options]].

## Limitations and Pitfalls

- **The quoted spread is a best case.** It applies to the displayed top-of-book size only. A large order pays a wider *effective* spread as it walks the book — the headline 1-cent spread can become several cents on real size.
- **Spreads are not constant.** They gap out precisely when you most want to trade — around earnings, macro releases, and crashes — because [[adverse-selection]] and inventory risk spike. Backtests that assume a fixed spread overstate live performance.
- **Tight spread ≠ deep liquidity.** A 1-cent spread on top of a paper-thin book ([[high-frequency-trading|HFT]] quoting tiny size, or [[spoofing|spoofed]] orders) can vanish the instant you send an order. Always check depth, not just the spread.
- **Crossing the spread compounds.** A high-turnover strategy pays the spread on every entry and exit; what looks negligible per trade can dominate net returns over thousands of round trips.

## Sources

- [[book-trading-and-exchanges]] — comprehensive treatment of the bid-ask spread, including its components (adverse selection, inventory, order processing costs), determinants, and role in market microstructure

## Related

- [[spread]] -- broader context on spread types
- [[order-book]] -- where the bid-ask spread is visible
- [[liquidity]] -- tight spreads indicate liquid markets
- [[market-maker]] -- profits from capturing the spread
- [[slippage]] -- spread is the minimum slippage cost
- [[market-impact]] -- the extra cost of crossing the spread on size
- [[adverse-selection]] -- the component that widens spreads around news
