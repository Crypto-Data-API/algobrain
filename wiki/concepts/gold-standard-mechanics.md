---
title: "Gold Standard Mechanics"
type: concept
created: 2026-04-24
updated: 2026-06-11
status: good
tags: [history, forex, commodities, gold, arbitrage, market-microstructure]
aliases: ["Classical Gold Standard", "Gold Standard"]
domain: [forex, market-microstructure, history, macro]
prerequisites: ["[[forex-basics]]", "[[fx-spot]]", "[[central-banks]]"]
difficulty: intermediate
related: ["[[gold-point-arbitrage]]", "[[specie-flow-arbitrage]]", "[[mint-parity-arbitrage]]", "[[bretton-woods]]", "[[nixon-shock]]", "[[book-golden-fetters]]", "[[covered-interest-arbitrage]]", "[[historical-cable-arbitrage]]", "[[telegraph-impact-on-arbitrage]]"]
---

# Gold Standard Mechanics

The gold standard is a monetary regime in which a country's currency has a fixed value defined in terms of a specific weight of gold. Between roughly 1870 and 1914 most major economies operated a **classical gold standard** in which free coinage, free convertibility, and free international movement of gold produced a self-adjusting exchange-rate and balance-of-payments system. It is the foundational regime for understanding [[gold-point-arbitrage]], [[specie-flow-arbitrage]], [[mint-parity-arbitrage]], and the pre-fiat history of [[forex]] trading.

## The Three "Freedoms"

A country is on a full (classical) gold standard when its monetary authority permits:

1. **Free coinage** — any individual may bring gold bullion to the mint and receive coin of equivalent weight (less a small brassage fee).
2. **Free convertibility** — paper currency and bank deposits are redeemable on demand for gold coin at the statutory rate.
3. **Free movement of gold** — gold may be exported and imported without licensing or tariff.

If all three hold, the exchange rate between two gold-standard currencies is determined within a narrow band around **mint parity**.

## Mint Parity

Mint parity is the ratio of the gold content of two currencies. Example (classical period):

- US dollar = 23.22 grains of fine gold ($20.67 per troy ounce)
- Pound sterling = 113.0016 grains of fine gold (£3 17s 10½d per troy ounce, or ~$4.8666 per £1)
- Mint parity GBP/USD = 113.0016 / 23.22 ≈ **$4.8666 per £1**

An arbitrageur who observed a market GBP/USD rate significantly different from $4.8666 could profit by shipping gold between London and New York — the basis of [[mint-parity-arbitrage]].

## Gold Points

The exchange rate did not sit exactly at mint parity in the market. It oscillated within a band defined by the **gold export point** and **gold import point**, which account for the round-trip cost of shipping gold:

- Freight, insurance, assay, and financing for gold in transit (~0.3%-0.7% of value under good conditions)
- Opportunity cost of idle gold en route (7-10 days by 1900)

When the market GBP/USD rose above the gold export point (say $4.887), it became profitable for a US holder of dollars to:

1. Buy gold in New York at $20.67/oz
2. Ship it to London
3. Sell it for sterling at £3 17s 10½d/oz
4. Convert back through FX at the favorable rate

This arbitrage pushed demand for sterling down and brought the rate back toward mint parity. Symmetrically, the gold import point capped upside on the dollar side. Together these **gold points** acted as hard trading boundaries — the 19th-century analog of modern [[currency-peg]] bands. See [[gold-point-arbitrage]].

## The Price-Specie-Flow Mechanism

David Hume's 1752 **price-specie-flow mechanism** describes how the standard balances payments:

1. Country A runs a current-account surplus; gold flows in.
2. Gold inflow expands the domestic money supply, raising prices.
3. Higher prices make A's exports less competitive; imports rise.
4. Current account moves back toward balance; gold flow reverses.

In practice central banks accelerated the adjustment through discount-rate policy — see [[specie-flow-arbitrage]] and the "rules of the game" below.

## "Rules of the Game"

Under classical gold standard central banks were expected to reinforce the price-specie-flow mechanism:

- **Gold outflow** → raise the discount-rate → attract short-term capital via higher yields, tighten domestic credit, damp prices.
- **Gold inflow** → lower the discount-rate → release gold abroad via lower yields, loosen domestic credit, allow prices to rise.

Compliance was imperfect — the [[bank-of-england]] followed the rules most faithfully (earning it the label "conductor of the international orchestra"); France and Germany often sterilized gold flows to protect domestic economies.

## Regime Phases

| Period | Regime | Notes |
|---|---|---|
| Pre-1870 | Bimetallism / informal gold | UK on gold from 1816/1821; US bimetallic with gold dominant post-1834 |
| **1870-1914** | **Classical gold standard** | Germany (1871), France (1878), US de facto (1879), Japan (1897) |
| 1914-1918 | Suspended | Convertibility dropped during WWI |
| 1925-1931 | Gold exchange standard | UK returned at pre-war parity (Churchill, 1925); central banks held sterling and dollars as gold-equivalent reserves |
| 1931 | Sterling crisis | UK leaves gold Sept 21, 1931 — Eichengreen's key case study in [[book-golden-fetters]] |
| 1933-1934 | US devaluation | Roosevelt raises gold price from $20.67 to $35/oz; private gold ownership prohibited |
| **1944-1971** | **Bretton Woods** | USD pegged to gold at $35/oz; other currencies pegged to USD ([[bretton-woods]]) |
| **Aug 15, 1971** | **Nixon shock** | US closes the gold window; USD becomes inconvertible ([[nixon-shock]]) |
| 1973-present | Fiat / floating | No major currency is directly convertible into gold |

## Trading Implications

For anyone studying historical [[forex]] microstructure, the gold standard explains:

- Why 19th-century FX volatility was an order of magnitude below post-1971 volatility — the gold points pinned rates inside a ~1% band.
- Why [[covered-interest-arbitrage]] only becomes interesting under fiat — under the gold standard, interest-rate differentials were arbitraged primarily via gold movement, not forward FX.
- Why rothschild-family, baring-brothers, and overend-gurney could build multi-generational franchises on seemingly thin spreads — cross-border gold, bill, and FX arbitrage inside tight bands, leveraged many times over.
- The limits of central-bank credibility — when gold reserves are threatened (1931 UK, 1971 US, 1992 UK in ERM), peg breaks generate violent price moves — the template for modern [[central-bank-peg-breaks]] such as [[chf-floor-removal]] (2015).

## Modern Echoes

No currency is on a gold standard today, but several structures mirror its mechanics:

- **[[currency-peg]]s** (HKD-USD, DKK-EUR) — mint-parity analog with central-bank interventions at narrow bands.
- **Currency boards** (HKMA) — require 100% foreign-currency backing for domestic monetary base, mimicking full convertibility.
- **Stablecoins** (USDC, USDT) — free convertibility at par, inventories of reserve assets, and "peg points" defended by redemption arbitrage. The Silicon Valley Bank-triggered USDC depeg in March 2023 closely tracks gold-point mechanics.
- **Gold ETFs** (GLD, IAU) — free convertibility between ETF shares and physical gold via authorized-participant [[etf-creation-redemption-arbitrage]].

## Related

- [[gold-point-arbitrage]]
- [[specie-flow-arbitrage]]
- [[mint-parity-arbitrage]]
- [[bretton-woods]]
- [[nixon-shock]]
- [[covered-interest-arbitrage]]
- [[telegraph-impact-on-arbitrage]]
- [[book-golden-fetters]]

## Sources

- Barry Eichengreen, *Golden Fetters: The Gold Standard and the Great Depression, 1919-1939* (1992) — canonical reference; ingest as [[book-golden-fetters]].
- Michael Bordo and Anna Schwartz (eds.), *A Retrospective on the Classical Gold Standard, 1821-1931* (NBER, 1984).
- David Hume, "Of the Balance of Trade" (1752) — original price-specie-flow mechanism.
- No raw sources ingested yet.
