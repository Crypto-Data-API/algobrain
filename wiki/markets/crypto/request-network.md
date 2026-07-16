---
title: "Request"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, payment-solutions]
aliases: ["REQ", "Request Network"]
entity_type: protocol
founded: 2017
headquarters: "Decentralized"
website: "https://request.network"
related: ["[[crypto-markets]]", "[[defi]]", "[[ethereum]]", "[[stablecoins]]"]
---

# Request

**Request** (REQ) is the utility token of the **Request Network**, an [[ethereum|Ethereum]]-based decentralized payment and invoicing system that lets anyone create an on-chain request for payment and receive funds peer-to-peer. Launched in 2017, REQ secures the network and is used to pay protocol fees; the network spans [[ethereum|Ethereum]] and Polygon.

The Request Network removes third-party processors from the payment loop: a user defines a recipient address and amount, optionally attaching terms to turn a simple request into a full invoice, then shares it for one-click, push-based settlement. Every request and payment is documented on-chain, making it useful for accounting and crypto invoicing.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | REQ |
| **Chain** | [[ethereum]] (also Polygon) |
| **Current Price** | $0.055346 |
| **Market Cap** | $41.20M |
| **Market Cap Rank** | #517 |
| **Fully Diluted Valuation** | ~$55.3M (price × max supply) |
| **24h Volume** | $1.44M |
| **24h Change** | +1.49% |
| **7d Change** | -2.28% |
| **Circulating Supply** | ~744.29M REQ |
| **All-Time High** | $1.059 (2018-01-06) |
| **All-Time Low** | $0.00454707 (2020-03-13) |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

Trading backdrop: the broad crypto market is in **extreme fear** ([[fear-and-greed-index|Crypto Fear & Greed Index]] = 23) within an **established bear market** as of 2026-06-20. REQ is up ~1.5% on the day and down ~2% on the week — a thin small-cap drifting with the risk-off tape, trading ~95% below its 2018 ATH.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~744.29M REQ |
| **Total Supply** | ~999.42M REQ |
| **Max Supply** | 1,000,000,000 REQ |
| **Fully Diluted Valuation** | ~$55.3M (price × max supply) |
| **Market Cap / FDV** | ~0.74 |
| **Genesis Date** | 2017-10-07 |

With ~74% of max supply already circulating, REQ has a relatively high market-cap-to-FDV ratio — meaning comparatively low future-emission overhang versus newer small-caps. As payments flow through the network, a portion of REQ is consumed/burned to pay fees, giving the token a usage-linked sink.

### Categories

Polygon Ecosystem, Ethereum Ecosystem, Payment Solutions.

### Contract Addresses

| Chain | Address |
|---|---|
| [[ethereum|Ethereum]] | `0x8f8221afbb33998d8584a2b05749ba73c37a938a` |
| Polygon PoS | `0xb25e20de2f2ebb4cffd4d16a55c7b395e8a94762` |

---

## How & Where It Trades

### Spot venues (CEX)

| Exchange | Pair |
|---|---|
| [[binance|Binance]] | REQ/USDT |
| [[kraken|Kraken]] | REQ/USD |
| KuCoin | REQ/USDT |
| Crypto.com Exchange | REQ/USD |

### Derivatives & DEX

| Venue | Pair | Type |
|---|---|---|
| [[hyperliquid\|Hyperliquid]] | REQ-PERP | [[perpetual-futures\|Perpetual]] |
| Uniswap V2/V3 ([[ethereum\|Ethereum]]) | REQ/DAI, REQ/WETH | Spot ([[decentralized-exchange\|DEX]]) |

REQ is a relatively thin small-cap: ~$1.4M of 24h volume against a ~$41M market cap (turnover ~3.5% of cap), so it is far less liquid than payment peers like [[huma-finance|HUMA]]. A REQ [[perpetual-futures|perp]] is listed on [[hyperliquid|Hyperliquid]], though [[open-interest|open interest]] and [[funding-rate|funding]] on small-cap perps tends to be low and can swing sharply.

### Protocol mechanics (payment requests / invoicing)

The Request Network's "market" is the issuance and settlement of payment requests:

1. A payer or payee creates a **request** on-chain specifying recipient, amount, currency, and optional invoice terms.
2. Because payments are **push-generated** (the counterparty pays an invoice they receive) rather than pull-generated, users never have to share account credentials — a structural privacy advantage over card/ACH rails.
3. Settlement happens peer-to-peer in supported tokens/[[stablecoins]]; the request and payment are recorded immutably for accounting.

---

## Use Case, Narrative & Category

Request is one of the oldest crypto **payments / invoicing** protocols, predating the modern PayFi wave. Its niche is on-chain invoicing, accounting, and B2B/freelancer payment requests, with tooling for [[stablecoins|stablecoin]] invoicing. It competes in the same broad payments category as [[huma-finance|Huma Finance]] but targets invoicing/accounting rather than receivable financing.

---

## Valuation Framing (qualitative)

- **MC/FDV ~0.74** — moderate future-emission overhang (~256M REQ still to enter circulation) but far cleaner than recent-launch tokens; most of the supply is already live.
- **Usage-linked sink** — a portion of REQ is consumed/burned to pay protocol fees, so sustained invoicing volume is the real value driver; the question is whether on-chain invoicing throughput justifies a ~$41M cap.
- **Longevity premium / decay** — REQ is a 2017-era survivor (~95% below ATH) trading on durability and a small fee sink rather than growth; it is priced as a mature, low-momentum payments small-cap.
- **Liquidity discount** — ~$1.4M/day volume means the effective tradeable cap is smaller than the headline; size positions for [[slippage]].

---

## Peer Comparison (crypto payments / invoicing, 2026-06-20)

| Asset | Price | Market Cap | Rank | MC/FDV | Niche |
|---|---|---|---|---|---|
| **Request (REQ)** | $0.055346 | $41.20M | #517 | ~0.74 | On-chain invoicing / accounting |
| [[huma-finance\|Huma Finance (HUMA)]] | — | (small/mid-cap) | — | low | PayFi / receivable financing |
| [[xdce\|XDC Network (XDC)]] | — | (mid-cap) | — | high | Trade-finance / enterprise payments |

> REQ targets invoicing/accounting; [[huma-finance|Huma]] targets receivable financing; XDC targets trade-finance settlement — adjacent payments/PayFi niches. REQ is the older, more decayed, lower-FDV-overhang name; HUMA is the newer, higher-momentum PayFi entrant.

---

## Notable History

- **Founded 2017** by Christophe Lassuyt (CFO) and Etienne Tatur (CTO), both previously co-founders of MONEYTIS. Genesis date 2017-10-07.
- All-time high of **$1.059** was reached on 2018-01-06 during the prior bull cycle; the token trades ~95% below that peak.
- All-time low of **$0.00454707** printed on 2020-03-13 (the COVID liquidity crash).
- The project has continued to ship invoicing and accounting tooling over multiple cycles, making it one of the longer-lived crypto-payments protocols.

> *Additional verified protocol events and news will be added through the wiki's source-ingestion workflow.*

---

## Risks

- **Liquidity risk:** thin ~$1.6M daily volume means wider spreads and higher [[slippage]] on size; small-cap perps add gap-risk.
- **Competitive risk:** the payments/invoicing niche is crowded (PayFi, stablecoin rails, fintech); REQ must keep attracting real invoicing volume to sustain its fee sink.
- **Regulatory risk:** on-chain invoicing and payments intersect with money-transmission, tax, and compliance rules across jurisdictions.
- **Smart-contract risk:** funds and logic live in [[smart-contracts]] on [[ethereum]] and Polygon.
- **Market regime:** with the [[fear-and-greed-index|Fear & Greed Index]] at 23 (extreme fear) in an established bear market, low-liquidity small-caps like REQ are prone to outsized drawdowns.

---

## Related

- [[crypto-markets]]
- [[ethereum]]
- [[defi]]
- [[stablecoins]]
- [[huma-finance]]
- [[hyperliquid]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-20 — cryptodataapi.com / CoinGecko markets feed (`raw/data/crypto-loop/coingecko-markets.json`; price/cap/rank/supply baseline)

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | REQ |
| **Market Cap Rank** | #513 |
| **Market Cap** | $40.44M |
| **Current Price** | $0.0543 |
| **Genesis Date** | 2017-10-07 |
| **Categories** | Payment Solutions |
| **Website** | [https://request.network](https://request.network) |

---

## Overview

What Is Request (REQ)?
The Request (REQ) utility token, launched in 2017, ensures the performance and stability of the Request Network. The Request Network itself is an Ethereum-based decentralized payment system where anyone can request a payment and receive money through secure means. It removes the requirement for third parties in order to provide a cheaper, more secure payment solution that works with all global currencies.

When a user creates a request for payment, they define to which address the payment needs to be allocated and what the amount is. The user can also define the terms and conditions of the payment, upgrading a simple request into an invoice. Once this is completed, the user can share their request to be paid by their counterparty.

Every step is documented and stored on the Request network, allowing everyone involved to easily keep track of all the invoices and payments for accounting purposes.

Request is also integrated with legislation across the world to remain compliant with the trade laws of each individual country.

Who Are the Founders of Request?
The founders of Request are Christophe Lassuyt and Etienne Tatur.

Christophe Lassuyt is currently the chief financial officer at Request. Before this position, he co-founded MONEYTIS.

Etienne Tatur is the chief technical officer of Request. Prior to this, he also co-founded MONEYTIS and worked as a lead developer at QOBUZ, a music streaming service.

What Makes Request Unique?
The payments on Request are performed by simply sending an invoice through the blockchain; the counterparty can then detect the request and pay it with one click in a peer-to-peer manner. The fact that the payments are push-generated instead of pull-generated is one of Request’s key advantages. There is no need for users to share their account information. The use of blockchain technology also eliminates the need for third-party processors, resulting in a reduction in transaction costs.

The Request Network leverages ...

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 744.29M REQ |
| **Total Supply** | 999.42M REQ |
| **Max Supply** | 1.00B REQ |
| **Fully Diluted Valuation** | $54.30M |
| **Market Cap / FDV Ratio** | 0.74 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.06 (2018-01-06) |
| **Current vs ATH** | -94.87% |
| **All-Time Low** | $0.00454707 (2020-03-13) |
| **Current vs ATL** | +1094.19% |
| **24h Change** | -0.08% |
| **7d Change** | +0.13% |
| **30d Change** | -6.04% |
| **1y Change** | -62.45% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x8f8221afbb33998d8584a2b05749ba73c37a938a` |
| Polygon Pos | `0xb25e20de2f2ebb4cffd4d16a55c7b395e8a94762` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | REQ/USDT | N/A |
| Kraken | REQ/EUR | N/A |
| KuCoin | REQ/USDT | N/A |
| Crypto.com Exchange | REQ/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V2 (Ethereum) | 0X8F8221AFBB33998D8584A2B05749BA73C37A938A/0X6B175474E89094C44DA98B954EEDEAC495271D0F | Spot |
| Uniswap V3 (Ethereum) | 0X8F8221AFBB33998D8584A2B05749BA73C37A938A/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://request.network](https://request.network) |
| **Twitter** | [@requestnetwork](https://twitter.com/requestnetwork) |
| **Reddit** | [https://www.reddit.com/r/RequestNetwork](https://www.reddit.com/r/RequestNetwork) |
| **GitHub** | [https://github.com/RequestNetwork/Request_SmartContracts](https://github.com/RequestNetwork/Request_SmartContracts) |
| **Whitepaper** | [https://request.network/assets/pdf/request_whitepaper.pdf](https://request.network/assets/pdf/request_whitepaper.pdf) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 112 |
| **GitHub Forks** | 7 |
| **Pull Requests Merged** | 5 |
| **Contributors** | 3 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $1.79M |
| **Market Cap Rank** | #513 |
| **24h Range** | $0.0536 — $0.0550 |
| **CoinGecko Sentiment** | 100% positive |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---
