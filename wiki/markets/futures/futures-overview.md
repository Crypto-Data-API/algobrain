---
title: "Futures Markets"
type: index
created: 2026-04-06
updated: 2026-06-19
status: excellent
tags: [futures, markets, index]
---

# Futures Markets

The hub for futures — standardized exchange-traded contracts to buy or sell an asset at a set price on a future date. Futures trade on regulated venues like [[cme-group|CME]] and ICE, which act as central counterparties and largely eliminate bilateral credit risk. They require margin rather than full payment (built-in leverage) and settle daily through mark-to-market, so gains and losses are realized every session.

Mastering futures means understanding contract specifications, margin and mark-to-market, roll dates, the [[contango]]/[[backwardation]] term structure, and physical-vs-cash settlement. In crypto, [[perpetual-futures|perpetual futures]] — contracts that never expire and stay tethered to spot via a [[funding-rate]] — have become the most-traded instrument by volume.

## How Margin, Leverage & Mark-to-Market Work

Futures are a *margined* instrument, not a purchase — you post a fraction of the contract's notional value and settle the difference daily:

- **Initial margin** — the good-faith deposit required to open a position (a small percentage of notional, set by the exchange/clearing house). This is the source of the **leverage**: controlling a large notional with a small deposit.
- **Maintenance margin** — the floor your equity must stay above; falling below it triggers a **margin call** (variation-margin top-up) or forced liquidation.
- **Mark-to-market** — at each session's close the clearing house revalues every position to the settlement price and moves cash between accounts. Gains are credited and losses debited *daily*, so there is no accumulating unrealized loss as in a stock — you either meet the call or get closed out.
- **Notional vs. margin** — a single contract's economic exposure (price × multiplier) can be many times the margin posted; this magnifies both returns and losses, which is why position sizing and the kill-criteria discipline of [[risk-management]] matter more here than in spot.
- **Settlement** — contracts resolve by **physical delivery** (e.g. crude, grains) or **cash settlement** (e.g. equity indices, VIX). Knowing which determines whether you must roll before first-notice/expiry to avoid delivery.

Because of daily settlement and central clearing through venues like [[cme-group|CME]] and ICE, counterparty credit risk is largely mutualized away — the key risk shifts from "will my counterparty pay?" to "can I meet variation margin?"

## Contract Categories

The futures complex spans every major asset class. The big categories and their flagship contracts:

| Category | Representative contracts | Primary use |
|---|---|---|
| **Equity index** | E-mini & Micro S&P 500 (ES/MES), Nasdaq-100 (NQ/MNQ), EURO STOXX 50 (FESX) | Hedging/positioning equity beta |
| **Rates / fixed income** | Treasury note & bond futures (ZN/ZB), SOFR/Fed Funds | Duration and rate-path views; the [[yield-curve]] |
| **Energy** | [[crude-oil\|WTI & Brent crude]], [[natural-gas]], gasoline, heating oil | Physical energy supply/demand |
| **Metals** | [[gold]], silver, [[copper]], platinum | Monetary hedge (gold) and industrial cycle (copper) |
| **Agriculturals (ags)** | [[corn]], soybeans, wheat, sugar, coffee | Harvest/weather-driven physical markets |
| **FX / currencies** | EUR, JPY, GBP futures | Currency exposure vs the [[eurusd\|spot FX]] market |
| **Crypto** | [[cme-bitcoin-futures\|CME Bitcoin/Ether futures]], [[perpetual-futures\|exchange perps]] | Regulated and leveraged digital-asset exposure |
| **Volatility** | [[vix-futures\|VIX futures]] | Trading or hedging the equity-vol term structure |

## Core Mechanics

- [[perpetual-futures]] — Expiry-free crypto futures; dominant by volume
- [[funding-rate]] — The periodic payment that anchors perps to spot
- [[contango]] — Forward price above spot; negative roll yield for longs
- [[backwardation]] — Forward price below spot; positive roll yield for longs
- [[roll-yield]] — The return earned or paid rolling expiring contracts forward
- [[span-margin]] — Portfolio-margining methodology for futures and options

## Term Structure: Contango vs Backwardation

The shape of the forward curve determines the hidden cost or benefit of holding a futures position over time:

- **[[contango]]** — further-dated contracts trade *above* spot (the normal state for storable commodities, reflecting storage and financing costs). A long roller sells the cheaper expiring contract and buys the dearer next one, paying **negative roll yield** — the structural drag behind many commodity ETFs (see [[commodity-futures-vs-etfs]]).
- **[[backwardation]]** — further-dated contracts trade *below* spot (typical when there is a supply squeeze or strong convenience yield). A long roller earns **positive roll yield**, the basis harvested by [[commodity-carry-strategy|carry strategies]].
- The curve shape, not just spot direction, is often the dominant P&L driver for a held futures position — and is precisely what [[trend-following-cta|CTAs]] and carry traders are positioned around.

## Products

- [[vix-futures]] — Volatility futures; the term structure traders sell or hedge
- [[crude-oil]], [[gold]], [[natural-gas]], [[copper]], [[corn]] — Major commodity contracts
- [[cme-bitcoin-futures]] — Regulated, cash/physically-settled BTC exposure

## Exchanges & Infrastructure

- [[cme-group]] — The largest derivatives exchange; equity, rate, FX, and commodity futures
- [[london-metal-exchange]] — Benchmark venue for industrial metals

## Strategy & Risk

- [[trend-following-cta]] — The dominant systematic futures strategy family
- [[commodity-carry-strategy]] — Harvesting term-structure roll yield
- [[cot-report-analysis]] — Reading Commitments of Traders positioning

## Comparisons

- [[options-vs-futures]] — Non-linear vs linear derivative payoffs
- [[spot-vs-futures-trading]] — Direct ownership vs leveraged contracts
- [[commodity-futures-vs-etfs]] — Futures vs ETFs for commodity exposure

## See Also

- **Mechanics:** [[span-margin]] · [[roll-yield]] · [[contango]] · [[backwardation]] · [[funding-rate]] · [[mark-to-market]]
- **Venues:** [[cme-group]] · intercontinental-exchange · [[london-metal-exchange]]
- **Contracts:** s-and-p-500 · [[crude-oil]] · [[gold]] · [[natural-gas]] · [[copper]] · [[corn]] · [[vix-futures]] · [[cme-bitcoin-futures]] · [[perpetual-futures]]
- **Strategy & risk:** [[trend-following-cta]] · [[commodity-carry-strategy]] · [[cot-report-analysis]] · [[risk-management]] · [[leverage]]
- **Hubs:** [[markets-overview]] · [[commodities-overview]] · [[options-overview]] · [[crypto-overview]]

## Pages

```dataview
TABLE status, updated, tags
FROM "wiki/markets/futures"
WHERE type != "index"
SORT updated DESC
```

## Sources

- General market knowledge; no specific wiki source ingested yet.
