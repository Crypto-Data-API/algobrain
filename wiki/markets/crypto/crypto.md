---
title: Crypto
type: concept
created: 2026-04-06
updated: 2026-06-21
status: excellent
tags:
  - crypto
  - markets
aliases:
  - crypto
  - cryptocurrency
  - crypto-market
  - crypto-trading
related: ["[[crypto-markets]]", "[[bitcoin]]", "[[ethereum]]", "[[defi]]", "[[stablecoins]]", "[[decentralized-exchanges]]"]
---

# Crypto

**Crypto** refers to the broad ecosystem of cryptocurrency markets — digital assets that settle on public blockchains rather than through banks or central clearing houses. It spans [[bitcoin|Bitcoin]], [[ethereum|Ethereum]], thousands of altcoins, [[defi|decentralized finance]], [[stablecoins]], and [[nft|NFTs]]. This page is the umbrella entry; for deeper market-structure detail see [[crypto-markets]].

## Core Building Blocks (Hub)

The crypto wiki is organised around a handful of recurring concepts. Use this table as a map into the deeper pages:

| Layer | Key idea | Pages |
|-------|----------|-------|
| **Assets** | The major tradeable instruments | [[bitcoin\|Bitcoin]], [[ethereum\|Ethereum]], [[stablecoins]], [[nft\|NFTs]], altcoins |
| **Venues** | Where trading happens | [[centralised-exchanges\|CEXs]], [[decentralized-exchanges\|DEXs]], OTC desks |
| **DeFi primitives** | On-chain finance | [[defi]], [[liquidity-pools]], [[uniswap\|Uniswap]], [[aave\|Aave]], [[perpetual-futures]] |
| **Microstructure** | How orders and blocks clear | [[mempool]], [[mev]], [[flashbots]], [[gas-fees]], [[funding-rate]] |
| **On-chain analysis** | Reading the public ledger | [[on-chain-analysis]], [[whale]], [[exchange-flows]], [[on-chain-smart-money-tracking]] |
| **Plumbing & risk** | Custody, identity, counterparty | [[kyc]], [[aml-ctf]], [[counterparty-risk]], [[contagion]] |
| **Regulation** | Rules of the road | [[regulation]], [[vasp-regulation]], [[austrac]] |

## Market Size and Context

The total crypto market capitalisation has historically cycled with extreme amplitude — from under $20 billion in early 2017, to a ~$3 trillion peak in November 2021, down to roughly $800 billion in the 2022 bear market, and back toward multi-trillion levels after the 2024 spot Bitcoin [[etf|ETF]] approvals. [[bitcoin|Bitcoin]] alone typically accounts for 40–60% of total crypto market cap ("Bitcoin dominance"), with [[ethereum]] the second largest. Even at its peak, crypto remained small relative to traditional markets: global equities are ~$100+ trillion and the US Treasury market alone is larger than all of crypto combined. This relative smallness is a key reason crypto is more volatile and more easily moved by flows.

## Market Structure

The crypto ecosystem is organised into several distinct sectors:

| Sector | What it is | Examples |
|--------|------------|----------|
| **Layer 1 (L1) blockchains** | Base settlement layers with their own consensus and security | [[bitcoin\|Bitcoin]], [[ethereum\|Ethereum]], Solana, Avalanche, BNB Chain |
| **Layer 2 (L2) scaling** | Networks that batch transactions and settle back to an L1 (mostly Ethereum) for cheaper, faster throughput | Arbitrum, Optimism, Base, zkSync, Polygon |
| **DeFi** | On-chain financial primitives — exchanges, lending, derivatives — run by smart contracts | [[uniswap\|Uniswap]], [[aave\|Aave]], Curve, [[defi]] |
| **Stablecoins** | Tokens pegged to fiat (usually USD), the unit of account and settlement rail of crypto | [[stablecoins\|USDT, USDC, DAI]] |
| **NFTs** | Non-fungible tokens representing unique digital assets | [[nft\|CryptoPunks, Bored Apes]] |
| **Memecoins** | Tokens with no utility claim, driven by social momentum | DOGE, SHIB, PEPE |

Trading happens across three venue types: **centralized exchanges (CEXs)** like Binance, Coinbase, and OKX ([[centralised-exchanges]]); **[[decentralized-exchanges|decentralized exchanges (DEXs)]]** like [[uniswap|Uniswap]] and Hyperliquid that run on [[liquidity-pools|liquidity pools]]; and **OTC desks** for large institutional blocks that would move thin order books.

## How Crypto Trading Differs from Equities

| Dimension | Equities | Crypto |
|-----------|----------|--------|
| **Hours** | Exchange hours (e.g. 9:30–16:00 ET), closed weekends/holidays | **24/7/365** — no close, no circuit-breaker pause across the whole market |
| **Settlement** | T+1 via clearing houses | Near-instant, on-chain, self-custodial possible |
| **Leverage** | Regulated margin (Reg T ~2×) | Up to 100×+ on perpetual futures venues |
| **Funding** | Dividends, borrow fees | **[[funding-rate\|Funding rates]]** on perpetual swaps — periodic payments between longs and shorts that anchor perp price to spot |
| **Transparency** | Quarterly filings, delayed data | **On-chain data** — wallet balances, flows, and contract state are public in real time |
| **Custody** | Broker/DTCC holds shares | Self-custody possible ("not your keys, not your coins") |
| **Regulation** | Mature (SEC, exchanges) | Fragmented, fast-changing, jurisdiction-dependent |

Three differences are especially important for traders:

- **24/7 markets** mean there is no overnight gap to hide behind — risk must be managed continuously, and liquidity thins dramatically during weekends and Asian-hours lulls, amplifying moves.
- **[[perpetual-futures|Perpetual futures]] and funding rates** are central. Perps have no expiry; a funding mechanism pays longs or shorts every ~8 hours to keep the perp price near spot. Persistently positive funding signals crowded longs and is itself a tradeable sentiment signal.
- **On-chain transparency** enables strategies impossible in equities: tracking whale wallets, exchange in/outflows, stablecoin minting, and [[liquidity-pools|DEX liquidity]] directly from the blockchain.

## Major Historical Events

- **2017** — ICO boom and first Bitcoin run to ~$20,000.
- **2020–2021** — "DeFi summer," NFT mania, and the cycle top near $69,000 BTC (Nov 2021).
- **2022** — Collapse of Terra/LUNA (May), [[three-arrows-capital|Three Arrows Capital]], Celsius, and [[ftx|FTX]] (November), wiping out hundreds of billions and triggering a deep bear market.
- **2023** — Institutional lender [[genesis|Genesis Global]] files for bankruptcy (January), the final domino of the 2022 [[contagion]]; regulatory enforcement intensifies.
- **2024** — US spot Bitcoin [[etf|ETFs]] approved (January), then spot Ether ETFs, channelling institutional capital and reshaping market structure.

## Key Risks for Traders

Crypto's distinctive features cut both ways; the most important risks to internalise:

| Risk | What it is | Mitigation / page |
|------|------------|-------------------|
| **Counterparty / custody** | Exchange or lender insolvency freezes or loses funds | Self-custody; diligence; [[counterparty-risk]], [[contagion]], [[genesis]] |
| **Volatility & leverage** | 100×+ perps make liquidation cascades violent | Position sizing; [[perpetual-futures]], [[funding-rate]] |
| **MEV & execution** | Public [[mempool]] exposes swaps to front-running | Private RPCs; [[mev]], [[flashbots]] |
| **Smart-contract risk** | Bugs/exploits drain DeFi protocols | Audits; protocol maturity; [[defi]] |
| **Liquidity** | Thin books amplify slippage; [[whale]]s can move price | Check depth/concentration; [[liquidity]] |
| **Regulatory** | KYC freezes, geo-blocks, delistings | Compliance awareness; [[kyc]], [[regulation]], [[vasp-regulation]] |
| **Operational** | Lost keys, phishing, scams | Hardware wallets, opsec |

## Related

- [[crypto-markets]] — detailed market-structure page
- [[bitcoin]]
- [[ethereum]]
- [[defi]]
- [[decentralized-exchanges]]
- [[centralised-exchanges]]
- [[liquidity-pools]]
- [[stablecoins]]
- [[nft]]
- [[perpetual-futures]]
- [[funding-rate]]
- [[staking]]
- [[mempool]]
- [[mev]]
- [[whale]]
- [[kyc]]

## Sources

- General market knowledge; no specific wiki source ingested yet.
