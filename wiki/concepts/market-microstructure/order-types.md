---
title: "Order Types"
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags: [order-types, market-microstructure, risk-management]
aliases: ["Order Types", "Order Types Overview", "order-types-overview", "Market Order", "Limit Order", "Stop Order", "Stop-Limit Order", "Time in Force"]
domain: [market-microstructure, order-types]
prerequisites: ["[[order-book]]", "[[bid-ask-spread]]"]
difficulty: beginner
related: ["[[order-book]]", "[[market-microstructure]]", "[[liquidity]]", "[[slippage]]", "[[risk-management]]", "[[stop-loss]]", "[[algorithmic-trading]]"]
---

# Order Types

Order types are the instructions a trader gives to an exchange or broker specifying how, when, and at what price a trade should be executed. Each order type is a different rule for interacting with the [[order-book]] — whether to demand immediacy (and pay the spread) or to wait for a price (and risk non-execution). Choosing the right order type is a fundamental skill that directly affects execution quality, [[slippage]], and [[risk-management]].

## Basic Order Types

| Type | Description | Use Case |
|------|-------------|----------|
| **Market order** | Executes immediately at the best available price | When speed matters more than price |
| **Limit order** | Executes only at a specified price or better | When price matters more than speed |
| **Stop order** | Becomes a market order when a trigger price is reached | [[stop-loss]] protection, breakout entries |
| **Stop-limit order** | Becomes a limit order when triggered | Controlled exit with price protection (but may not fill) |

## Advanced Order Types

- **Trailing stop**: A stop order that moves with the price by a fixed amount or percentage. Captures upside in trends while protecting profits.
- **OCO (One-Cancels-Other)**: Two orders linked together; when one executes, the other is automatically canceled. Common for setting both a take-profit and [[stop-loss]].
- **Iceberg order**: Displays only a fraction of the total order size to the market. Used by institutions to minimize market impact.
- **TWAP / VWAP orders**: [[algorithmic-trading]] order types that execute over time to achieve a target average price.

## Time-in-Force

- **GTC (Good-Til-Canceled)**: Remains active until filled or manually canceled.
- **IOC (Immediate-or-Cancel)**: Fills what it can immediately, cancels the rest.
- **FOK (Fill-or-Kill)**: Must fill entirely and immediately, or the entire order is canceled.
- **Day order**: Expires at the end of the trading session.

## Maker vs. Taker

Limit orders that add [[liquidity]] to the order book are "maker" orders (often receiving fee discounts). Market orders and aggressively priced limit orders that remove liquidity are "taker" orders (usually paying higher fees).

## Why It Matters for Traders

Proper order type selection directly impacts trading costs and [[risk-management]]. Using market orders in thin [[liquidity]] causes excessive [[slippage]]. Relying solely on stop-market orders risks poor fills during fast moves — a stop triggered in a gapping market becomes a market order and can fill far below the trigger. A stop-limit avoids that bad fill but risks not filling at all (e.g., price gaps straight through the limit). Understanding the trade-off between *immediacy* and *price certainty* across the full toolkit is essential for efficient execution.

## Related

- [[order-book]] — where limit orders rest and against which market orders execute
- [[bid-ask-spread]] — the cost a market order pays for immediacy
- [[slippage]] — the gap between expected and realized execution price
- [[stop-loss]] — risk-control use of stop orders
- [[algorithmic-trading]] — TWAP/VWAP and other algo order types
- [[liquidity]] — determines how much a market order moves price

## Sources

- Larry Harris, *Trading and Exchanges: Market Microstructure for Practitioners* (Oxford University Press, 2003) — chapter on order types and order-submission strategies.
- SEC Investor.gov, "Types of Orders" — official retail-facing definitions of market, limit, and stop orders.
- CME Group and Nasdaq order-type specifications — exchange documentation for time-in-force and advanced order types.
