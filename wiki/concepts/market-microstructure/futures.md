---
title: Futures
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags: [futures, derivatives, leverage]
aliases: [futures-contract, futures-contracts, futures contract]
domain: [market-microstructure]
prerequisites: ["[[derivatives]]", "[[margin]]"]
difficulty: intermediate
related:
  - "[[derivatives]]"
  - "[[options]]"
  - "[[leverage]]"
  - "[[margin]]"
  - "[[perpetual-futures]]"
  - "[[arbitrage]]"
  - "[[contango]]"
  - "[[backwardation]]"
---

# Futures

A futures contract is a standardized agreement to buy or sell an asset at a predetermined price on a specific future date.

## Overview

Futures originated in agricultural commodities (the CBOT grain pits, 1860s) but now cover equities, indices, currencies, energy, rates, and crypto. They are traded on regulated exchanges (CME Group, ICE, Eurex) with standardized contract sizes and expiration dates. A central counterparty (the exchange clearing house) stands between every buyer and seller, novating the trade and eliminating bilateral credit risk — the structural feature that distinguishes exchange-traded futures from over-the-counter [[forwards]].

Futures provide [[leverage]] because traders post only [[margin]] (a performance bond, typically 3-15% of notional) rather than the full contract value.

### Margin and mark-to-market

A futures position is **marked to market daily**: at each session's settlement price, gains and losses are credited or debited to the trader's margin account in cash. **Initial margin** is the deposit required to open a position; **maintenance margin** is the lower threshold below which a **margin call** is triggered, requiring the trader to top up or be liquidated. Because P&L is realized daily rather than at expiry, futures carry no accumulated counterparty exposure — a key reason the clearing model is robust. This daily cash flow also distinguishes futures from forwards economically, creating small convexity differences when rates are volatile.

## Key Details

- **Expiry**: Each contract has a settlement date (monthly, quarterly). At expiry, the position is settled or rolled to the next contract.
- **Settlement**: **Physical delivery** means the actual asset changes hands. **Cash settlement** means only the profit/loss is exchanged in cash.
- **Contango**: When futures price > spot price. Common when carrying costs (storage, interest) are positive. Long holders pay a premium over time.
- **Backwardation**: When futures price < spot price. Occurs when near-term demand is high or supply is constrained.
- **Perpetual futures (perps)**: Crypto-native contracts with no expiry that use a funding rate mechanism to anchor price to spot.

## How It Works

A trader goes long one BTC quarterly future at $50,000. If BTC is $55,000 at expiry, they profit $5,000 per contract (cash settled). If it falls to $45,000, they lose $5,000. With 10x leverage, the initial margin was only $5,000 -- meaning the position doubled or was wiped out.

## Trading Relevance

Futures are essential for hedging, speculation, and [[arbitrage]]. The basis (futures - spot) reflects market expectations about future price and carry costs. Monitoring open interest and futures funding rates provides valuable [[sentiment]] data.

## Related

- [[derivatives]] -- futures are a core derivative type
- [[options]] -- another key derivative instrument
- [[leverage]] -- futures inherently provide leverage
- [[arbitrage]] -- basis trades exploit futures vs spot
- [[perpetual-futures]] -- the crypto-native, no-expiry variant anchored by a funding rate
- [[contango]] / [[backwardation]] -- the two states of the futures term structure

## Sources

- John C. Hull, *Options, Futures, and Other Derivatives* — standard reference on contract mechanics, margining, and cost-of-carry pricing ([[book-options-futures-other-derivatives]])
- CME Group — contract specifications, margining methodology (SPAN), and settlement procedures (cmegroup.com)
- Larry Harris, *Trading and Exchanges: Market Microstructure for Practitioners* — clearing, the central counterparty, and basis trading ([[book-trading-and-exchanges]])
- Robert McDonald, *Derivatives Markets* — forward/futures pricing, contango/backwardation, and the convenience yield
