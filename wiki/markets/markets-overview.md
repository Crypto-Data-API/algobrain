---
title: "Markets"
type: index
created: 2026-04-06
updated: 2026-06-19
status: excellent
tags: [markets, index]
---

# Markets

The top-level hub for every market the wiki covers. Each market has its own structure, participants, liquidity profile, fee model, margin regime, and trading hours, and a strategy that thrives in one can fail outright in another. Use this page to jump to the right sub-hub, then drill into individual instruments from there.

The defining differences are practical: [[bitcoin|Bitcoin]] and [[crypto-markets|crypto]] trade 24/7 with extreme volatility and permissionless leverage; equities follow exchange sessions with overnight and weekend gaps; forex runs continuously across overlapping global sessions driven by rate differentials; commodities are anchored to physical supply and demand; and derivatives (options and futures) layer leverage, expiry, and non-linear payoffs on top of any of the above.

## Market Sub-Hubs

| Sub-hub | What it covers | Trading hours | Distinguishing trait |
|---|---|---|---|
| [[crypto-overview\|Crypto]] | Cryptocurrencies, DeFi, exchanges, stablecoins, on-chain analytics | 24/7 | Highest volatility; permissionless leverage |
| Stocks | Equities, indices, IPOs, exchange microstructure | Exchange sessions | Overnight/weekend gaps; earnings-driven |
| [[forex-overview\|Forex]] | Currency pairs, central banks, carry | ~24/5 continuous | Largest market by turnover; rate-differential driven |
| [[commodities-overview\|Commodities]] | Energy, metals, agricultural markets | Venue sessions | Anchored to physical supply/demand and storage |
| [[options-overview\|Options]] | Greeks, volatility surface, pricing, 70+ strategy pages | Tied to underlying | Non-linear payoffs; expiry and time decay |
| [[futures-overview\|Futures]] | Standardized contracts, margin, mark-to-market, roll, crypto perps | Near-24h electronic | Built-in leverage; daily settlement |
| [[bonds\|Bonds]] | Fixed income, treasuries, credit, the yield curve | OTC + exchange | The risk-free anchor that reprices everything |

## Equity Indices

The major regional benchmarks — useful for cross-market relative-value and macro positioning:

| Index | Region | Construction note |
|---|---|---|
| s-and-p-500 | United States | 500 names, free-float cap; the global risk benchmark |
| EURO STOXX 50 | Eurozone | 50 blue chips, free-float cap; banks/luxury/semis tilt |
| ftse-100 | United Kingdom | 100 names; energy/miners/banks, mostly non-GBP earners |
| nikkei-225 | Japan | 225 names, **price-weighted** |
| asx-200 | Australia | 200 names; banks + materials, China-demand proxy |
| Shanghai Composite | Mainland China | All-share, total-cap; retail-led, capital-controlled |

## Most-Referenced Instruments

- [[bitcoin]] — The original cryptocurrency and most liquid digital asset; market bellwether
- [[ethereum]] — Smart-contract settlement layer underpinning DeFi
- [[crude-oil]] — The most actively traded physical commodity; macro growth proxy
- [[gold]] — Monetary metal and safe-haven hedge
- [[eurusd]] — The most liquid currency pair in the world

## How the Pieces Relate

The asset classes are not independent silos — they are linked through a few master variables:

- **The risk-free rate** ([[yield-curve|yield curve]], set off [[bonds|government bonds]]) is the discount rate for every other asset. When it moves, equities, gold, FX, and crypto all reprice.
- **The US dollar** ([[eurusd|FX]]) is the global funding and pricing unit: a stronger dollar pressures [[commodities-overview|commodities]] (priced in USD) and emerging-market equities.
- **Volatility** ([[vix|VIX]] / [[options-overview|options]]) is the cross-asset risk barometer — equity vol bleeds into credit spreads and FX carry unwinds.
- **Leverage and term structure** ([[futures-overview|futures]], [[perpetual-futures|perps]]) determine how positioning unwinds in stress: margin calls and [[funding-rate|funding]] flips can cascade across markets faster than spot fundamentals change.
- **Risk-on / risk-off** rotation links them all: in risk-off, capital flows from equities and crypto toward [[bonds|treasuries]], [[gold]], and the dollar.

## Cross-Market Concepts

- [[perpetual-futures]] — Expiry-free crypto futures; the most-traded crypto instrument by volume
- [[contango]] and [[backwardation]] — Term-structure shapes that govern roll yield
- [[funding-rate]] — The mechanism that tethers perps to spot
- [[carry-trade]] — Earning the rate/yield differential across forex and crypto
- [[yield-curve]] — The fixed-income term structure that reprices every asset class
- [[vix]] — The equity-volatility gauge watched across all risk assets
- [[liquidity]] and [[slippage]] — Why the same strategy behaves differently per market
- [[correlation]] — How asset-class linkages tighten in stress

## Market Comparisons

- [[stocks-vs-crypto]] — Equity vs cryptocurrency markets: hours, volatility, regulation
- [[crypto-vs-forex]] — On-chain assets vs foreign exchange
- [[spot-vs-futures-trading]] — Direct ownership vs leveraged derivatives
- [[options-vs-futures]] — Non-linear vs linear derivative payoffs

## See Also

- stocks-overview · [[crypto-overview]] · [[forex-overview]] · [[commodities-overview]] · [[options-overview]] · [[futures-overview]] · [[bonds]]
- [[bitcoin]] · [[ethereum]] · [[crude-oil]] · [[gold]] · [[eurusd]]
- [[risk-management]] · [[portfolio-theory]] · [[market-microstructure]]

## All Market Pages

```dataview
TABLE status, updated, tags
FROM "wiki/markets"
WHERE type != "index"
SORT updated DESC
```

## Sources

- General market knowledge; no specific wiki source ingested yet.
