---
title: "Exchanges"
type: index
created: 2026-04-06
updated: 2026-06-21
status: excellent
tags: [exchanges, entities, index]
---

# Exchanges

Stock exchanges, cryptocurrency exchanges, and derivatives platforms.

Exchanges are the central venues where buyers and sellers meet. They define the rules of engagement -- fee structures, order types, listing standards, margin requirements, and regulatory jurisdiction. Understanding the differences between exchanges is critical when choosing where to trade, especially in crypto where exchange risk (as FTX demonstrated) is a major factor.

This section covers both centralized exchanges (CEXs) and decentralized exchanges (DEXs), across equities, derivatives, and crypto. It is structured as a **hub**: the tables below categorize venues by type, region, and asset class, and link to each exchange's own entity page.

## Start Here

- [[exchange-data-sources]] -- Master reference of official data endpoints for all major exchanges
- [[nyse-vs-nasdaq]] -- Comparison of the two dominant US exchanges
- [[centralized-vs-decentralized-exchanges]] -- The CEX/DEX trade-off (custody, KYC, liquidity, smart-contract risk)
- [[exchange-risk]] -- Counterparty and solvency risk (the [[ftx]] case study)

## How to Navigate This Hub

| Axis | Sections |
|------|----------|
| By venue type | [[#Centralized Crypto Exchanges (CEX)\|CEX]] · [[#Decentralized Crypto Exchanges (DEX)\|DEX]] · [[#Crypto Derivatives Venues\|Derivatives]] · [[#Traditional Exchanges\|Equities]] |
| By region | [[#Exchanges by Region\|Region table]] |
| By asset class | [[#Exchanges by Asset Class\|Asset-class table]] |
| Reference | [[#How Exchanges Differ\|How exchanges differ]] · [[exchange-data-sources]] |

## Traditional Exchanges

| Exchange | Ticker Prefix | Market Cap | Region |
|----------|--------------|------------|--------|
| [[nyse]] | — | ~$28T | USA |
| [[nasdaq]] | — | ~$25T | USA |
| [[london-stock-exchange]] | LON | ~$3.5T | UK |
| [[hong-kong-stock-exchange]] | HKG | ~$4T | Asia |
| [[national-stock-exchange-india]] | NSE | — | India |
| [[bombay-stock-exchange]] | BOM | — | India |
| [[asx-limited]] | ASX | ~AUD $1.5T | Australia |
| [[euronext]] | — | — | Europe (pan-EU) |
| [[deutsche-borse]] | ETR | — | Germany |
| [[six-swiss-exchange]] | SIX | — | Switzerland |
| [[tokyo-stock-exchange]] | TYO | — | Japan |
| [[toronto-stock-exchange]] | TSE | — | Canada |

Market-cap figures are approximate and move with the market; see each exchange's page for current detail. The two dominant US venues are compared in [[nyse-vs-nasdaq]]; the broader institutional plumbing is covered under [[market-microstructure]].

## Centralized Crypto Exchanges (CEX)

Centralized exchanges custody user funds and run an internal matching engine. They offer the deepest liquidity and fiat on-ramps but concentrate counterparty risk — see [[exchange-risk]] and the [[ftx]] collapse.

| Exchange | Region / Status | Founded | Notable for |
|----------|-----------------|---------|-------------|
| [[binance]] | Global (offshore) | 2017 | Largest spot + derivatives volume and liquidity; founded by [[changpeng-zhao]] |
| [[coinbase]] | US-regulated | 2012 | Institutional gateway; [[coinbase-prime]] custody behind US [[bitcoin-etfs]] |
| [[kraken]] | US / global | 2011 | Long-running, security-focused, deep fiat pairs |
| [[okx]] | Global (offshore) | 2017 | Large derivatives and spot venue |
| [[bybit]] | Global (offshore) | 2018 | Derivatives-heavy, high perp volume |
| [[bitstamp]] | EU | 2011 | One of the oldest exchanges, EU-regulated |
| [[gemini]] | US-regulated | 2014 | NY trust-chartered, compliance-first |

A CEX combines four functions that are separated across the traditional-finance stack: it is exchange (matching engine), broker (custody and order entry), clearinghouse (it nets and settles internally), and often market maker. That bundling is what gives a CEX its deep liquidity and fast settlement — and what makes its solvency a single point of failure. The [[ftx]] collapse (November 2022) and the [[binance]] $4.3B DOJ settlement (November 2023, under [[changpeng-zhao]]) are the two reference cases for why CEX counterparty risk is treated separately under [[exchange-risk]].

## Decentralized Crypto Exchanges (DEX)

Decentralized exchanges are non-custodial: trades settle on-chain via smart contracts and users keep their keys. They remove counterparty/solvency risk but add smart-contract risk, MEV exposure, and gas costs. See [[centralized-vs-decentralized-exchanges]].

| Exchange | Model | Chain / Notable for |
|----------|-------|---------------------|
| [[uniswap]] | AMM (spot) | The reference Ethereum AMM; deepest DEX liquidity |
| [[hyperliquid]] | On-chain order-book perps | Sub-second finality, transparent order book |
| [[raydium]] | AMM (spot) | Leading Solana AMM; memecoin graduation venue |
| [[pumpswap]] | AMM (spot) | [[pump-fun]]'s native graduate DEX on Solana |
| [[jupiter-exchange-solana]] | Aggregator | Routes swaps across Solana AMMs |
| [[curve-finance]] | Stable-AMM | Stablecoin and pegged-asset swaps |
| [[gmx]] | On-chain perps | Oracle-priced perpetuals on Arbitrum/Avalanche |
| [[asterdex]] | On-chain perps | Perp DEX with hidden-order microstructure |

For strategy maps built on these venues, see [[hyperliquid-perp-trading-map]], [[asterdex-perp-trading-map]], and [[low-cap-crypto-trading-map]].

## Crypto Derivatives Venues

| Venue | Type | Notable for |
|-------|------|-------------|
| [[cme-group]] / [[cme-bitcoin-futures]] | Regulated futures + options | The US institutional BTC/ETH futures anchor; cash-settled |
| [[deribit]] | Crypto options | Dominant BTC/ETH options venue by open interest |
| [[binance]] | Perps + options | Largest offshore [[perpetual-futures]] book |
| [[bybit]] / [[okx]] | Perps + options | Major offshore derivatives venues |
| [[hyperliquid]] | On-chain perps | Largest decentralized perp venue |

## Pages

```dataview
TABLE status, updated, tags
FROM "wiki/entities/exchanges"
WHERE type != "index"
SORT updated DESC
```

## NFT Marketplaces

- [[opensea]] -- The first and most recognized NFT marketplace (2017)
- [[blur]] -- Professional NFT trading platform, zero fees (2022)
- [[magic-eden]] -- Multi-chain NFT marketplace, Solana and Bitcoin Ordinals leader (2021)
- [[looksrare]] -- Token-incentivized NFT marketplace, wash trading case study (2022)

## Australian Brokers & Platforms

For a comprehensive overview of the Australian investment landscape — including CHESS sponsorship, franking credits, superannuation, and the ASX — see [[australian-investing]].

| Broker | Type | ASX Fee | Key Feature |
|--------|------|---------|-------------|
| [[commsec]] | Bank-owned (CBA) | $10–$29.95 | Australia's largest broker, 3M+ accounts, comprehensive research |
| [[selfwealth]] | Discount | $9.50 flat | Flat-fee disruptor, social portfolio comparison |
| [[nabtrade]] | Bank-owned (NAB) | $14.95–0.11% | NAB banking integration, options, international shares |
| [[morgans]] | Full-service | Adviser-negotiated | Largest full-service firm, 40+ offices, IPO access, in-house research |
| [[stake]] | Fintech | $3 flat | Low-cost US share access, mobile-first |
| [[superhero]] | Fintech | $2 flat ($0 ETFs) | Cheapest ASX brokerage, free ETF trades |
| [[cmc-markets]] | CFD + Shares | $11 or 0.10% | CFDs and CHESS shares on one platform, advanced charting |
| [[ig-markets]] | CFD + Shares | $8 flat | 17,000+ markets, 50+ year track record, ProRealTime |
| [[bell-direct]] | Mid-range | $15–0.10% | Bell Potter research access, options, AutoInvest |

All Australian brokers listed above are CHESS-sponsored for ASX share trading (Superhero transitioned to CHESS in 2023).

## Exchanges by Region

| Region | Equities | Crypto |
|--------|----------|--------|
| North America | [[nyse]], [[nasdaq]], [[toronto-stock-exchange]] | [[coinbase]], [[kraken]], [[gemini]], [[cme-group]] |
| Europe | [[london-stock-exchange]], [[euronext]], [[deutsche-borse]], [[six-swiss-exchange]] | [[bitstamp]] |
| Asia-Pacific | [[hong-kong-stock-exchange]], [[tokyo-stock-exchange]], [[national-stock-exchange-india]], [[bombay-stock-exchange]], [[asx-limited]] | [[okx]], [[bybit]] |
| Global / offshore | — | [[binance]], [[hyperliquid]], [[uniswap]], [[deribit]] |

## Exchanges by Asset Class

| Asset class | Primary venues |
|-------------|----------------|
| Equities | [[nyse]], [[nasdaq]], [[london-stock-exchange]], [[euronext]] |
| Crypto spot (CEX) | [[binance]], [[coinbase]], [[kraken]], [[okx]] |
| Crypto spot (DEX) | [[uniswap]], [[raydium]], [[curve-finance]], [[jupiter-exchange-solana]] |
| Crypto derivatives | [[cme-group]], [[deribit]], [[hyperliquid]], [[binance]] |
| NFTs | [[opensea]], [[blur]], [[magic-eden]] |

## How Exchanges Differ

Choosing a venue is a function of several axes that the entity pages detail individually:

- **Custody model.** CEXs hold your funds (counterparty/solvency risk — see [[exchange-risk]] and [[ftx]]); DEXs are non-custodial (smart-contract and MEV risk instead).
- **Regulation and jurisdiction.** US-regulated venues ([[coinbase]], [[gemini]], [[cme-group]]) vs offshore ([[binance]], [[bybit]]) carry very different compliance, recourse, and access profiles.
- **Liquidity and fees.** Depth, [[slippage]], and [[fee-structures|maker/taker fees]] vary widely; deeper books mean tighter spreads.
- **Order types and microstructure.** Lit order books vs AMM curves vs hidden-order books shape which strategies are viable — see [[market-microstructure]] and the [[hyperliquid-perp-trading-map]]/[[asterdex-perp-trading-map]] maps.
- **Margin and leverage.** Regulated futures ([[cme-bitcoin-futures]]) impose conservative margin; offshore [[perpetual-futures]] venues offer far higher leverage with corresponding liquidation risk.
- **Settlement.** Equities settle [[t-plus-2|T+2]] (the US moved to [[t-plus-1|T+1]] in May 2024) via clearinghouses; crypto spot settles near-instantly; CME crypto futures are cash-settled.

## CEX vs DEX at a Glance

The single biggest structural decision in crypto venue choice is custodial vs non-custodial. The two models trade one risk for another rather than eliminating risk:

| Dimension | Centralized (CEX) | Decentralized (DEX) |
|-----------|-------------------|---------------------|
| Custody | Exchange holds funds | User holds keys (non-custodial) |
| Primary risk | Counterparty / solvency ([[exchange-risk]], [[ftx]]) | Smart-contract bug, [[mev]], oracle failure |
| Matching | Internal order book | On-chain AMM curve or order book |
| Liquidity depth | Deepest (e.g. [[binance]]) | Thinner, fragmented across pools |
| Fiat on-ramp | Yes | No (needs a CEX or on-ramp first) |
| KYC / identity | Required on regulated venues | None at the protocol level |
| Speed | Sub-millisecond matching | Bound by block time / finality |
| Cost | [[fee-structures|Maker/taker fees]] | Swap fee + gas + price impact |
| Recourse | Support, sometimes deposit insurance | None — code is law |

The deeper trade-off is covered in [[centralized-vs-decentralized-exchanges]].

## Choosing a Venue (Decision Table)

| If you want to... | Prefer | Why |
|-------------------|--------|-----|
| Fiat on-ramp + deep liquidity, US-regulated | [[coinbase]], [[kraken]], [[gemini]] | Banking rails, segregated custody, recourse |
| Maximum spot/derivatives depth | [[binance]] | Largest book; tightest spreads |
| Regulated, cash-settled BTC/ETH futures | [[cme-group]] / [[cme-bitcoin-futures]] | Institutional venue, conservative margin |
| Crypto options by open interest | [[deribit]] | Dominant BTC/ETH options venue |
| Non-custodial spot swaps on Ethereum | [[uniswap]] | Reference AMM, deepest DEX liquidity |
| On-chain perps with a transparent book | [[hyperliquid]] | Sub-second finality, on-chain order book |
| US equities | [[nyse]], [[nasdaq]] | Deepest equity liquidity (see [[nyse-vs-nasdaq]]) |
| ASX shares from Australia | [[commsec]], [[selfwealth]], [[stake]] | CHESS-sponsored brokers (see [[australian-investing]]) |

## Related

- [[exchange-data-sources]] -- official data endpoints for all major exchanges
- [[exchange-risk]] -- counterparty and solvency risk
- [[centralized-vs-decentralized-exchanges]] -- the CEX/DEX trade-off
- [[nyse-vs-nasdaq]] -- the two dominant US equity venues
- [[market-microstructure]] -- how venue design shapes execution
- [[cme-bitcoin-futures]] -- the regulated US crypto-futures anchor
- [[perpetual-futures]] -- the offshore derivatives product
- [[australian-investing]] -- the ASX broker landscape in depth

## Sources

General market knowledge; no specific wiki source ingested yet.
