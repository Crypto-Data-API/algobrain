---
title: "Stock Markets"
type: index
created: 2026-04-06
updated: 2026-06-17
status: excellent
tags: [stocks, markets, index]
aliases: ["Stocks Overview", "Stock Markets Section"]
---

# Stock Markets

The navigation hub for the equities section: the instrument, market structure, indices, ETFs, sectors, mega-cap names, and the concepts that tie them together. Stocks represent ownership in companies (see [[stocks]]) and are the most widely traded financial instrument in the world. The [[s-and-p-500]] — tracking ~500 of the largest US companies — is the single most-watched benchmark in global finance.

> **New here?** Read [[stocks]] (what a share is) → [[stock-markets]] (how shares trade) → [[equity-index]] (how benchmarks are built). Those three plus [[s-and-p-500]] are the core of this section.

## Foundations

- [[stocks]] — the equity instrument: ownership rights, common vs preferred, dividends and buybacks, why prices move
- [[stock-markets]] — market structure: exchanges, auctions, [[order-types]], market makers, lit vs dark, T+1 settlement, circuit breakers
- [[equity-index]] — what an index is: weighting schemes, float adjustment, reconstitution, major global indices
- [[market-microstructure]] — the theory of order flow and price formation

## Major Indices

- [[s-and-p-500]] — 500 large-cap US companies (~80% of US market cap); the global benchmark
- [[dow-jones]] — 30 blue-chip US stocks, **price-weighted**; the oldest major index
- [[qqq]] — NASDAQ-100 ETF: largest non-financial NASDAQ stocks, tech-heavy
- [[euro-stoxx]] — EURO STOXX 50, the eurozone blue-chip benchmark

## Index ETFs

- [[spy]] — SPDR S&P 500 ETF, the most liquid equity ETF in the world
- [[qqq]] — Invesco NASDAQ-100 ETF
- [[index-funds]] — passive replication vehicles and how they work
- [[index-options]] — cash-settled SPX/NDX and ETF options for hedging and volatility trades

## GICS Sectors

The [[gics-classification|GICS system]] divides the stock market into 11 sectors. Each sector page lists its S&P 500 constituents; [[sector-rotation]] between them is a key macro signal.

| Sector | S&P 500 Weight | Description |
|--------|---------------|-------------|
| [[technology|Information Technology]] | ~32% | Software, semiconductors, IT services, hardware |
| [[financials|Financials]] | ~13% | Banks, insurance, capital markets, payments |
| [[communication-services|Communication Services]] | ~11% | Digital media, telecom, entertainment |
| [[consumer-discretionary|Consumer Discretionary]] | ~10% | Retail, autos, restaurants, apparel |
| [[healthcare|Health Care]] | ~9% | Pharma, biotech, medical devices, insurers |
| [[industrials|Industrials]] | ~9% | Aerospace, transport, machinery, construction |
| [[consumer-staples|Consumer Staples]] | ~6% | Food, beverages, household products, tobacco |
| [[energy|Energy]] | ~3.5% | Oil & gas exploration, refining, services |
| [[utilities|Utilities]] | ~2.5% | Electric, gas, water, renewables |
| [[materials|Materials]] | ~2% | Chemicals, mining, construction materials, packaging |
| [[real-estate|Real Estate]] | ~2% | REITs: data centres, industrial, residential, retail |

## Mega-Cap Stocks

- [[nvidia]] — the AI-era semiconductor leader
- [[tesla]] — high-volatility EV and energy stock
- [[intel]] — legacy semiconductor maker in turnaround
- [[coinbase-stock]] — listed proxy for crypto-market activity

## Key Concepts

- [[market-capitalization]] — how company size is measured and why it drives index weight
- [[dividend]] — cash distributions; see also [[dividend-yield]] and [[dividend-investing]]
- [[valuation]] — estimating intrinsic value (multiples, DCF)
- [[order-types]] — market, limit, stop, and advanced order controls
- [[short-selling]] — profiting from price declines
- [[market-makers]] — liquidity provision and the bid-ask spread

## S&P 500 Companies

```dataview
TABLE ticker AS "Ticker", sector AS "Sector"
FROM "wiki/entities/companies"
WHERE sp500 = true
SORT sector ASC, title ASC
```

## All Stock Market Pages

```dataview
TABLE status, updated, tags
FROM "wiki/markets/stocks"
WHERE type != "index"
SORT updated DESC
```

## Comparisons

- [[stocks-vs-crypto]] — comparing equity and cryptocurrency markets

## Related Sections

- [[bond-market]] — the debt counterpart to equities
- [[forex]] · [[commodities]] — adjacent macro markets
- [[futures]] · [[options]] — derivative exposure to equities and indices
