---
title: "Crypto Payments"
type: concept
created: 2026-07-19
updated: 2026-10-17
status: draft
tags: [crypto]
aliases: ["Crypto Payments", "Payments", "Payment Tokens", "Stablecoin Payments"]
domain: [crypto, stablecoins]
prerequisites: ["[[stablecoins]]"]
difficulty: beginner
related: ["[[stablecoins]]", "[[payments-basket]]", "[[stablecoin-regulation]]", "[[xrp]]", "[[stellar]]", "[[tron]]", "[[narrative-trading]]", "[[cryptodataapi-sentiment]]"]
---

# Crypto Payments

**Crypto payments** covers the use of blockchains to move money: stablecoin settlement, cross-border remittances, merchant acceptance, crypto cards, and the payment-focused chains and tokens built for them. In practice the sector has split in two. **Stablecoins** carry most real payment volume, while **payment tokens** such as [[xrp|XRP]] and [[stellar|XLM]] trade mainly on adoption and regulatory headlines. Payment tokens are repeatedly rerated on that news, which makes the sector a recurring narrative trade.

## Overview

Payments was the original crypto use case: Bitcoin's white paper describes "peer-to-peer electronic cash". Volatile assets proved poor money, though, and by the 2020s the payment rail that actually scaled was dollar [[stablecoins]], [[usdt|USDT]] and [[usdc|USDC]] above all. They settle around the clock, cross borders without correspondent banks, and are used heavily for remittances and dollar savings in emerging markets. [[tron|Tron]] became a major USDT transfer network because transfers there are cheap.

The sector has four layers:

- **Settlement rails** — stablecoins on Ethereum, Tron, [[solana|Solana]] and others; payment-optimised chains such as [[xrp|XRP Ledger]], [[stellar|Stellar]], [[celo|Celo]] and [[nano|Nano]].
- **Payment-native coins** — [[litecoin|LTC]], [[bitcoin-cash|BCH]] and Bitcoin's Lightning Network, aimed at cheap transfers of the base asset.
- **Merchant and consumer apps** — point-of-sale and card products such as [[pundi-x-2|Pundi X]], [[metal|Metal Pay]], [[uquid-coin|UQUID]] and [[electroneum|Electroneum]].
- **Traditional payment firms adopting crypto rails** — card networks settling in stablecoins and fintechs issuing their own.

## Key Milestones

- **September 2021** — El Salvador made bitcoin legal tender; the law was amended in early 2025 to make acceptance voluntary.
- **13 July 2023** — a US federal court ruled in SEC v. Ripple that XRP's programmatic exchange sales were not securities offerings, and XRP rallied sharply. It is the clearest single example of a payment token rerating on a legal headline.
- **August 2023** — PayPal launched its [[pyusd|PYUSD]] stablecoin; the next month Visa extended USDC settlement to Solana.
- **2024-2025** — Stripe bought the stablecoin-infrastructure firm Bridge (announced October 2024), signalling mainstream payment processors moving onto stablecoin rails.
- **18 July 2025** — the US GENIUS Act became law, the first federal framework for payment stablecoins (see [[stablecoin-regulation]]).

## Trading Relevance

- **Sector basket.** [[payments-basket]] trades payment tokens (XRP, XLM, XNO, CELO, REQ) as a sector on Hyperliquid perps; payments is an institutional and regulation-driven sector that tends to move on legal and partnership news rather than DeFi activity.
- **Narrative and rotation.** Regulatory wins, bank or card-network partnerships and ETF filings for payment tokens are classic catalysts in the [[narrative-trading]] and [[sector-rotation]] playbooks. The catalyst is usually priced within days, so most of the move is front-run.
- **Stablecoin supply as a liquidity signal.** Growth in stablecoin supply is both a measure of payment-rail adoption and a proxy for dry powder entering crypto; see [[stablecoin-flow-anomaly]].
- **Peg trades.** Payment stablecoins occasionally trade away from $1 on specific venues; [[stablecoin-pair-arbitrage]] covers those dislocations and [[depeg-risk|depeg risk]] covers the tail.
- **Valuation caveat.** Most payment volume runs on stablecoins, not on payment tokens, so adoption of crypto rails does not automatically flow to a payment token's price. That is why the sector trades mostly on narrative.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/sentiment/stablecoins` — total stablecoin market cap with 14-day and 90-day flows

**Historical data:**
- `GET /api/v1/sentiment/stablecoins/history` — stablecoin market-cap history time series
- `GET /api/v1/market-intelligence/stablecoin-history` — stablecoin market-cap history time series

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/sentiment/stablecoins"
```

Auth: `X-API-Key` header. Endpoint catalog: [[cryptodataapi-sentiment]]. Payment-token prices are on the standard coin and market-data endpoints ([[cryptodataapi-coins]]).

## Related

- [[stablecoins]] — the rail that carries most crypto payment volume
- [[stablecoin-regulation]] — GENIUS Act and other stablecoin rules
- [[payments-basket]] — the payment-token sector basket
- [[xrp]], [[stellar]], [[tron]], [[litecoin]], [[celo]], [[nano]] — payment-focused chains
- [[pundi-x-2]], [[metal]], [[uquid-coin]], [[electroneum]] — merchant and consumer payment projects
- [[usdt]], [[usdc]], [[pyusd]], [[circle]], [[tether-limited]]
- [[narrative-trading]], [[sector-rotation]]
