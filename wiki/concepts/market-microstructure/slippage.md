---
title: Slippage
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags: [slippage, market-microstructure, liquidity, backtesting]
aliases: [price slippage, execution slippage, Slippage]
domain: [market-microstructure]
prerequisites: ["[[liquidity]]", "[[order-book]]", "[[bid-ask-spread]]"]
difficulty: beginner
related:
  - "[[liquidity]]"
  - "[[order-book]]"
  - "[[bid-ask-spread]]"
  - "[[trading-volume]]"
  - "[[slippage-modeling]]"
  - "[[market-impact]]"
  - "[[transaction-costs]]"
---

# Slippage

Slippage is the difference between the price a trader expects for a trade and the price at which it actually fills. It is one of the core components of transaction cost — alongside commissions and the [[bid-ask-spread]] — and it is the part most likely to make a backtested edge disappear in live trading.

## Overview

Slippage arises whenever execution price diverges from the price observed at decision time. It is most visible with market orders (and stop orders that trigger into the market), which take whatever liquidity is available. Slippage can be favorable (a better fill than expected) or adverse (worse), but adverse slippage dominates in practice because orders compete for the same scarce liquidity that everyone else is also chasing during volatile or thin conditions.

## How It Works

The mechanics tie directly to the [[order-book]]:

- A market buy lifts the best ask, then the next ask level, and so on until filled. If the order is larger than the size resting at the best ask, the average fill price is **worse than the quoted ask** — this excess is slippage from walking the book.
- The minimum achievable slippage on any round trip is roughly the [[bid-ask-spread]]: you buy at the ask and sell at the bid.
- Between order submission and execution, the quote can move (latency + volatility), adding a second source of slippage independent of order size.

A simple decomposition: `realized cost ≈ ½ spread + market impact + timing/delay cost`, where market impact scales with order size relative to available depth.

## Causes

- **Low [[liquidity]]** — thin [[order-book]]s force the order through multiple price levels.
- **High [[volatility]]** — rapid price changes between submission and fill.
- **Large order size** — big orders relative to depth cause [[market-impact]].
- **Market orders during news/events** — liquidity often vanishes and the [[bid-ask-spread]] widens around major announcements, open/close auctions, and economic releases.

## How to Minimize Slippage

1. Use **limit orders** instead of market orders when immediacy is not required.
2. Trade **liquid markets** with tight spreads and deep books.
3. **Break up large orders** into smaller child orders (iceberg, TWAP, VWAP, or POV algorithms) to reduce impact.
4. **Avoid low-liquidity windows** (pre/post-market, holidays, weekend crypto, the seconds around major data prints).
5. On DEX/AMM trades, **set a slippage tolerance** to cap acceptable price impact and protect against sandwich attacks.

## Trading Relevance

Slippage is a hidden, recurring cost that compounds against active traders. In [[backtesting]], unmodeled or underestimated slippage is a leading cause of strategies that look profitable on paper and lose money live — high-turnover and short-holding-period strategies are most exposed. Always overlay a realistic slippage and [[market-impact]] estimate (see [[slippage-modeling]]) before trusting backtest results. For large institutional positions, slippage and impact frequently exceed commissions and become the dominant component of [[transaction-costs]], which is why execution quality (and execution algorithms) is itself a measurable edge.

## Sources

- Kissell, R. (2013), *The Science of Algorithmic Trading and Portfolio Management* — transaction-cost and market-impact modeling
- Almgren, R. & Chriss, N. (2000), "Optimal Execution of Portfolio Transactions," *Journal of Risk* — the canonical impact/slippage execution framework
- SEC Rule 605/606 disclosures — execution-quality and price-improvement reporting

## Related

- [[liquidity]] — the primary determinant of slippage
- [[order-book]] — depth determines how far an order walks
- [[bid-ask-spread]] — the minimum slippage on any round trip
- [[market-impact]] — the size-driven component
- [[slippage-modeling]] — accounting for it in backtests
