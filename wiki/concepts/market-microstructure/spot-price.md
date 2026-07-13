---
title: Spot Price
type: concept
created: 2026-04-06
updated: 2026-07-01
status: good
tags: [market-microstructure, valuation, liquidity, derivatives]
aliases: [cash price, spot rate, "spot market price", Spot Price]
related:
  - "[[spot-markets]]"
  - "[[spot-vs-futures-trading]]"
  - "[[contango]]"
  - "[[backwardation]]"
  - "[[trading-volume]]"
  - "[[bid-ask-spread]]"
  - "[[order-book]]"
  - "[[cost-of-carry]]"
  - "[[basis-trading]]"
domain: [market-microstructure]
prerequisites: ["[[spot-markets]]"]
difficulty: beginner
---

# Spot Price

The spot price is the current market price at which an asset can be bought or sold for **immediate delivery and settlement**, as opposed to a futures or forward price, which applies to a transaction agreed today but settled at a future date. It is the "price now" — the number quoted on a ticker, the last trade on an exchange, the live FX rate — and it answers the everyday trader question *"is the price I see on the screen the 'real' price?"* For a stock, the answer is essentially yes: the quoted price is a spot price for near-immediate settlement.

## How the Spot Price Is Determined

In a continuous, order-driven market the spot price is set by the [[order-book]] — the standing buy ([[bid-ask-spread|bid]]) and sell (ask) orders. In practice "the spot price" can mean any of several closely related numbers:

- **Last traded price** — the price of the most recent execution (what most tickers display).
- **Mid price** — the midpoint of the best bid and best ask, often used for marking and valuation.
- **NBBO / best quote** — for US equities, the National Best Bid and Offer consolidated across venues.

Because of the [[bid-ask-spread|bid-ask spread]], there is never a single price to *transact* at: you buy at the ask and sell at the bid. The spot "price" is a convenient summary of a two-sided, constantly updating market.

## Spot vs. Futures (the basis)

The spot price reflects real-time supply and demand. Futures and forward prices incorporate the **[[cost-of-carry]]** — financing, storage, and the [[convenience-yield]] of holding the asset until delivery:

```
Futures ≈ Spot × e^((r + storage − convenience-yield) × t)
Basis   = Futures − Spot
```

The relationship between spot and futures determines whether a market is in [[contango]] (futures > spot, positive basis) or [[backwardation]] (spot > futures, negative basis). A key fact: **at expiry the futures price converges to the spot price**, because at that moment the two contracts are equivalent. The gap between them — the basis — is what [[basis-trading]] and [[cash-and-carry]] arbitrage capture.

### Worked example (illustrative)

Suppose gold trades at a spot price of **$2,000/oz**, the risk-free rate is 5%, and one-year storage/financing costs add 1%. The fair one-year futures is roughly `2000 × (1 + 0.06) = $2,120`, a **$120 basis** (contango). An arbitrageur who can store gold cheaply could buy spot, sell the future, and lock in the spread; that arbitrage is exactly the force tethering the future to spot. (Numbers are illustrative.)

## Where Spot Prices Are Used

- **Equities** — Stock prices are effectively spot prices, settled at T+1 (one business day) in the US since 2024. The quote you see is the spot.
- **Forex** — Most currency trading is spot, conventionally settled at T+2.
- **Commodities** — Gold, oil, and agricultural products have well-established physical spot (cash) markets alongside their futures curves.
- **Crypto** — Exchange prices for immediate delivery (e.g. BTC/USD on a major venue) are spot prices, distinct from perpetual-futures prices.

## Trading Relevance

The spot price is the **anchor for all derivative pricing**. Arbitrageurs keep futures, forwards, and options tethered to spot through cash-and-carry and reverse cash-and-carry strategies, so a mispriced derivative is pulled back toward fair value relative to spot. In crypto, the *basis* between a perpetual future and spot drives funding rates and creates a continuous carry trade. For valuation and accounting, positions are typically **marked to market** at the prevailing spot price, which is why a stale or illiquid spot quote can distort reported portfolio value.

## Spot Market Characteristics

Spot markets generally offer the most transparent and direct price exposure. They involve **no leverage by default** (unlike futures), no expiration, and no funding costs. The trade-offs:

- They may have **lower [[trading-volume]]** than their derivatives counterparts in some asset classes — notably crypto, where perpetual futures often trade higher volume than spot, so the derivative can actually *lead* price discovery.
- A spot price from a single venue can be **stale or unrepresentative** in thin names; the consolidated/NBBO price is more reliable.
- The displayed spot is a **midpoint or last trade**, not the price a large order would actually achieve after [[slippage]].

## Limitations

1. **Not a transactable single number** — the real cost to trade includes the [[bid-ask-spread|spread]] and [[slippage]], especially for size.
2. **Venue dependence** — different exchanges can show slightly different spot prices; arbitrage usually keeps them close but not identical.
3. **Spot ≠ fair value** — the market spot price is what people will pay *now*, which can diverge from an analyst's estimate of intrinsic-value.

## Related

- [[spot-markets]] — the venues where spot prices are set
- [[spot-vs-futures-trading]] — the spot-vs-derivative comparison
- [[contango]], [[backwardation]] — spot-futures basis regimes
- [[cost-of-carry]] / [[basis-trading]] — what links spot to the futures curve
- [[bid-ask-spread]] / [[order-book]] — how the spot price is actually formed
- [[trading-volume]] — liquidity context

## Sources

- Hull, J. *Options, Futures, and Other Derivatives* — spot price as the anchor for forward/futures pricing via cost-of-carry.
- CME Group. *Understanding Basis* — the relationship between spot (cash) and futures prices.
- BIS. *Triennial Central Bank Survey* — FX spot conventions and T+2 settlement.
- SEC, "Shortening the Securities Transaction Settlement Cycle" (2023) — adoption of T+1 settlement for US equities.
