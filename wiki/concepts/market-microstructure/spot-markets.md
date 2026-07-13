---
title: Spot Markets
type: concept
created: 2026-04-06
updated: 2026-07-01
status: good
tags:
  - market-microstructure
  - liquidity
aliases:
  - spot-markets
  - spot-market
  - cash market
  - spot-trading
  - Spot Trading
related: ["[[spot-price]]", "[[spot-vs-futures-trading]]", "[[futures]]", "[[contango]]", "[[backwardation]]"]
domain: [market-microstructure]
prerequisites: ["[[spot-price]]"]
difficulty: beginner
---

# Spot Markets

**Spot markets** are financial markets where assets are traded for immediate delivery and settlement at the current market price (the [[spot-price]]).

## Spot vs Futures

In a spot market, transactions settle immediately (or within a short settlement window like T+1 for equities). In [[futures]] markets, settlement occurs at a future date. The difference between the futures price and the spot price is called the **basis** or premium. For a detailed comparison, see [[spot-vs-futures-trading]].

Spot prices serve as the reference point for all derivative pricing. Futures, options, and swaps are all ultimately anchored to the spot market.

## Forex Spot Market

The foreign exchange spot market is the largest financial market in the world, with daily turnover exceeding $7.5 trillion. Forex spot trades settle in two business days (T+2) and account for approximately one-third of total FX volume, with the remainder in forwards, swaps, and options.

## Crypto Spot Exchanges

Cryptocurrency spot markets operate 24/7 on exchanges like Binance, Coinbase, and Kraken. Settlement is near-instantaneous on centralized exchanges (though on-chain settlement depends on blockchain confirmation times). Spot trading in crypto is distinguished from perpetual futures and margin trading, and many traders use spot markets for long-term holding while using derivatives for speculation.

## Commodity Spot Markets

Physical commodity spot markets involve the actual delivery of goods -- oil at Cushing, Oklahoma; gold in London vaults; wheat at grain elevators. Spot commodity prices are influenced by supply/demand fundamentals, storage costs, and logistics constraints. The relationship between spot and futures prices reveals market expectations about supply and demand through [[contango]] and [[backwardation]].

## Trading Relevance

Spot markets are where most outright directional exposure is taken without leverage, expiry, or carry. For a trader, the spot market is both the price anchor for derivatives and an arbitrage counterpart: cash-and-carry strategies pair a spot position against a futures position to capture the [[contango|basis]], and in crypto the spot-vs-perpetual basis drives funding-rate arbitrage. Liquidity differs by asset class — spot FX dwarfs everything, while in crypto perpetual-futures volume often exceeds spot, meaning the "reference" market is sometimes thinner than its derivatives.

## Spot vs Derivatives: What You Actually Own

A spot purchase gives you the asset itself — the share, the coin, the bar of gold — with no expiry and no counterparty promising future delivery. That has practical consequences:

- **No time decay or roll.** A spot holding does not expire, so there is no [[roll-yield]] drag or [[cost-of-carry]] to pay, unlike a long [[futures]] position that must be rolled forward.
- **No leverage by default.** You fund the full notional. This caps your loss at 100% (the asset going to zero) and removes [[liquidation-risk|forced-liquidation risk]] — the asset cannot be margin-called out from under you.
- **You receive the cash flows.** Spot equity holders collect dividends and keep voting rights; futures and most [[options]] holders do not.

## Worked Example (Illustrative)

The figures below are hypothetical, chosen only to show how a spot trade settles versus a futures alternative.

Suppose gold trades at a spot price of **$2,400/oz** and you want exposure to 100 oz:

- **Spot route:** you pay 100 × $2,400 = **$240,000** today and take delivery (or hold an allocated claim). You now own the metal outright. If gold rises to $2,520, your position is worth $252,000 — a $12,000 (+5%) gain, with no expiry and no roll.
- **Futures route:** the 3-month future trades at **$2,430** (a $30 [[contango|premium]] reflecting [[cost-of-carry]]). You post, say, $24,000 initial margin for the same 100 oz. You get the same directional exposure with one-tenth the cash, but you face margin calls if gold falls, and at expiry the future converges to spot — so the $30 premium you paid erodes as carry.

The spot price ($2,400) is the gravitational center: the future's $2,430 is just spot plus carry, and as expiry approaches the [[basis-trading|basis]] shrinks toward zero. This convergence is what cash-and-carry [[arbitrage]] enforces.

## Limitations and Pitfalls

- **Capital intensity.** Outright spot ties up the full notional, which is inefficient if you only want directional exposure — a key reason institutions use [[futures]] and [[options]] instead.
- **Custody and settlement risk.** Owning the asset means storing it: vaulting and insurance for [[commodities]], custodian/[[counterparty-risk]] for securities, and self-custody or exchange risk for crypto. Settlement is not always instant — equities settle T+1, FX spot T+2.
- **"Spot" is not always the deepest market.** The reference price can be thinner than its derivatives (notably crypto perps), so the headline spot quote may not reflect where real size trades.
- **No built-in hedge or income.** A naked spot holding has no downside protection; pairing it with [[protective-puts]] or [[covered-calls|covered calls]] is how holders add insurance or yield.

## Related

- [[spot-price]]
- [[spot-vs-futures-trading]]
- [[futures]]
- [[contango]]
- [[backwardation]]
- [[cost-of-carry]]
- [[basis-trading]]
- [[market-microstructure]]

## Sources

- BIS. *Triennial Central Bank Survey of Foreign Exchange and OTC Derivatives Markets* — authoritative FX spot turnover figures.
- Hull, J. *Options, Futures, and Other Derivatives* — spot vs. forward/futures pricing and the cost-of-carry relationship.
- CME Group. *Understanding Basis* — the spot-futures basis, contango, and backwardation.
