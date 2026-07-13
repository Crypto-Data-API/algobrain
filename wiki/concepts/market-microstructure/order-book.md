---
title: Order Book
type: concept
created: 2026-04-06
updated: 2026-07-13
status: good
tags: [market-microstructure, liquidity, order-types]
aliases: [order-books, "Order Books", depth-of-market, "Depth of Market", DOM, "Level 2", "Level 1", "limit order book"]
domain: [market-microstructure]
prerequisites: ["[[order-types]]", "[[bid-ask-spread]]"]
difficulty: intermediate
related:
  - "[[cryptodataapi]]"
  - "[[bid-ask-spread]]"
  - "[[liquidity]]"
  - "[[market-maker]]"
  - "[[order-flow]]"
  - "[[depth-of-market]]"
  - "[[order-types]]"
  - "[[order-flow-imbalance]]"
---

The order book is the real-time, continuously updated record of all outstanding buy (bid) and sell (ask) limit orders for an asset, organized by price level and time priority. It is the central data structure of any modern electronic exchange and the venue where [[liquidity]] visibly resides.

## Overview

Every limit order that is not immediately executable rests in the order book until it is filled, cancelled, or expires. The book displays the available liquidity at each price point, showing where buyers and sellers are willing to transact. Reading the order book provides insight into supply/demand dynamics, potential [[support-and-resistance]], and the likely cost of executing orders of various sizes (the [[market-impact|market impact]] of a trade).

Most modern exchanges operate a **central limit order book (CLOB)** matched by a **price-time priority** rule: orders are filled first by best price, and within a price level, in the order they arrived (FIFO). Some venues use pro-rata or size-priority matching for certain products (e.g., short-dated interest-rate futures).

## How It Works

- **Bid side**: All resting buy orders, sorted from highest to lowest price. The highest bid is the *best bid* (best available buy price).
- **Ask (offer) side**: All resting sell orders, sorted from lowest to highest price. The lowest ask is the *best ask* (best available sell price).
- **[[bid-ask-spread]]**: The gap between the best bid and best ask. The tighter the spread, the more liquid the market.
- **Top of book / inside quote**: The best bid and best ask together — the prices a marketable order will touch first.
- **Depth**: The cumulative volume of resting orders at and beyond each price level. Deep books absorb large orders without significant price impact; thin books gap.

When a marketable order arrives, it "walks the book," consuming resting liquidity at successively worse prices until filled — this is the source of [[slippage]] on large orders.

## Level 1 vs. Level 2 Data

- **Level 1 (L1) data** — the *top of book*: best bid, best ask, their sizes, plus the last trade price and size. This is the most basic feed and is sufficient for most discretionary retail trading. L1 tells you the current spread and the most recent transaction.
- **Level 2 (L2) data** — the full *depth of market* ([[depth-of-market|DOM]]): every resting limit order at every price level on both sides. L2 lets traders see where large resting orders are clustered, identify potential support/resistance from order concentration, and gauge the true liquidity available at each price. L2 is the raw input for [[order-flow-analysis|order flow analysis]] and [[order-flow-imbalance|OFI]] signals.
- **Level 3 / full order-by-order feeds** (e.g., Nasdaq TotalView-ITCH) expose individual order add/cancel/execute events, used by [[high-frequency-trading|HFT]] and quantitative execution systems.

## Key Concepts

- **Bid/ask walls**: Unusually large resting size at a single level. A large bid wall suggests support; a large ask wall suggests resistance — but walls can be pulled in an instant.
- **Iceberg (reserve) orders**: Large orders that display only a small "tip" on the book while hiding the true size, refreshing as each tranche fills. Designed to minimize signalling and market impact.
- **Spoofing / layering**: Placing large orders with no intent to execute to manipulate other participants' perception of supply/demand, then cancelling before they fill. Illegal in regulated markets under Dodd-Frank.
- **Queue position**: For a passive (maker) limit order, where it sits in the FIFO queue at its price level determines fill probability — a core concern of market makers.

## Trading Relevance

Active traders use the order book to gauge real-time supply/demand imbalance and to estimate execution cost before sending an order. A bid-heavy book signals short-term buying pressure; an ask-heavy book the reverse. But the book is a *snapshot of intentions, not commitments* — resting orders can be cancelled at any moment, and displayed size understates true interest (icebergs) or overstates it (spoofs).

For this reason, [[order-flow]] analysis — tracking the actual *execution* of aggressive orders against resting liquidity — provides more reliable signals than the static book alone. Algorithmic execution systems consume L2/L3 books to drive [[smart-order-routing]] and to compute microstructure signals such as [[order-flow-imbalance|order flow imbalance]].

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/liquidity/depth` — per-coin depth/spread at 10/25/50/100 bps
- `GET /api/v1/liquidity/oi-divergence` — OI vs price divergence (1h/4h/24h)
- `GET /api/v1/hyperliquid/l2-book?coin=BTC` — raw L2 order book snapshot

**Historical data:**
- `GET /api/v1/liquidity/depth/{coin}` — 24h rolling depth history, 1-min samples (BTC free)

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/liquidity/depth"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-regimes]].

## Related

- [[bid-ask-spread]] — defined by the top of book
- [[liquidity]] — the order book is where liquidity lives
- [[depth-of-market]] — the L2 view of the book
- [[market-maker]] — populates both sides of the book
- [[order-flow]] — tracks actual executions against the book
- [[order-types]] — the instructions that create entries in the book
- [[order-flow-imbalance]] — a quantitative measure of net book pressure

## Sources

- Larry Harris, *Trading and Exchanges: Market Microstructure for Practitioners* (Oxford University Press, 2003) — canonical treatment of limit order books and matching priority.
- Maureen O'Hara, *Market Microstructure Theory* (Blackwell, 1995).
- Nasdaq TotalView-ITCH and NYSE OpenBook product specifications — real-world depth-of-book feed documentation.
