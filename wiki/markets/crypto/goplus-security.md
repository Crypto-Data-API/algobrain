---
title: "GoPlus Security"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, infrastructure]
aliases: ["GPS", "GoPlus"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://gopluslabs.io/"
related: ["[[base]]", "[[crypto-markets]]", "[[oracle-manipulation]]", "[[smart-contracts]]"]
---

# GoPlus Security

**GoPlus Security** (GPS) is the token of GoPlus, a decentralized **on-chain security layer** for Web3 — a permissionless "User Security Network" that provides risk detection across the user's transaction lifecycle. GoPlus is widely used through its **security API**, which powers token-risk, address-risk, phishing, and approval checks embedded in wallets, [[decentralized-exchange|DEX]] front-ends, and analytics tools. It is a [[base|Base]]-native token also deployed on BNB Chain.

GoPlus's pitch is that the current blockchain stack lacks a dedicated security layer; GoPlus fills that gap with data and detection services that warn users about malicious tokens, contracts, and addresses before they sign.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | GPS |
| **Chain** | [[base]] (also BNB Chain) |
| **Price** | $0.00915103 |
| **Market Cap** | $40,349,113 |
| **Market Cap Rank** | #522 |
| **24h Volume** | $7,547,681 |
| **24h Change** | +5.18% |
| **7d Change** | +26.68% |
| **24h Range** | $0.00864333 — $0.00947973 |
| **Fully Diluted Valuation** | ~$91.5M |
| **All-Time High** | $0.2198 (2025-01-31) |
| **All-Time Low** | $0.00441135 (2025-12-18) |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

Trading backdrop: the broad crypto market is in **extreme fear** (Crypto Fear & Greed Index ≈ 23) within an **Established Bear Market** as of 2026-06-21. GPS is a notable outlier — up ~5% on the day and ~27% on the week — showing strong relative strength against an otherwise risk-off tape. The token trades ~96% below its January-2025 ATH of $0.2198, but has roughly doubled off its December-2025 ATL of $0.00441, so the recent rally is a recovery off a deep base rather than a fresh high.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~4.41B GPS |
| **Total Supply** | 10,000,000,000 GPS |
| **Max Supply** | 10,000,000,000 GPS |
| **Fully Diluted Valuation** | ~$91.5M |
| **Market Cap / FDV** | ~0.44 |

About 44% of max supply circulates (MC/FDV ~0.44) — a **moderate future-unlock overhang**, lighter than several peers in this group (Gensyn ~0.13, KGeN ~0.20) but still meaning ~56% of the supply (~5.6B GPS) remains to enter the market via team, investor, ecosystem, and emission unlocks. The roughly $51M gap between the ~$40M market cap and ~$91.5M FDV is the implicit sell-side pressure buyers are underwriting. GPS is used to access/pay for security services within the network and to coordinate the permissionless security-provider ecosystem; token demand is meant to scale with API/detection usage rather than with speculation on the asset.

### Categories

BNB Chain Ecosystem, Base Ecosystem, Cybersecurity, YZi Labs (prev. Binance Labs) Portfolio, OKX Ventures Portfolio, Binance HODLer Airdrops, Binance Alpha Spotlight, Base Native.

### Contract Addresses

| Chain | Address |
|---|---|
| [[base|Base]] | `0x0c1dc73159e30c4b06170f2593d3118968a0dca5` |
| BNB Chain | `0x9a4a67721573f2c9209dfff972c52be4e3f6642e` |

---

## How & Where It Trades

### Spot venues (CEX)

| Exchange | Pair |
|---|---|
| [[binance|Binance]] | GPS/USDT |
| Bitget | GPS/USDT |
| KuCoin | GPS/USDT |

GPS is liquid for a small-cap: ~$7.5M of 24h volume against a ~$40.3M market cap (turnover ~19% of cap), elevated by the week's strong move. Liquidity is concentrated on major centralized venues, with on-chain depth on [[base|Base]] and BNB Chain DEXs.

### Derivatives

Following its Binance HODLer distribution and CEX listings, GPS has perpetual-futures coverage on major derivatives venues (e.g., Binance Futures GPS-USDT perp), but open interest is modest for a token of this size. There is no flagship [[hyperliquid|Hyperliquid]] GPS-PERP listing in the snapshot. Funding and OI can swing sharply around unlock dates and exchange-program events; verify live funding/OI before taking leverage. Treat GPS as primarily a spot instrument with thin, event-sensitive derivatives.

### Protocol mechanics (security API / User Security Network)

GoPlus's "product" is security data and detection rather than a trading venue:

1. **Security API:** GoPlus exposes endpoints for token risk, malicious-address detection, approval/allowance checks, NFT risk, and phishing-site detection. Wallets and [[decentralized-exchange|DEX]] front-ends integrate these to flag risky tokens and transactions before users sign.
2. **User Security Network:** a permissionless network where security providers contribute detection capabilities and data, coordinated and incentivized via the GPS token.
3. **Coverage:** detection runs across the user transaction lifecycle — pre-trade token vetting, transaction simulation/approval review, and post-trade monitoring.

The token's demand thesis is tied to adoption of these security services across the wallet/DEX ecosystem rather than to trading the asset itself.

---

## Use Case, Narrative & Category

GoPlus sits in the **Web3 security / cybersecurity infrastructure** category and rides the persistent narrative of on-chain safety: with frequent rug-pulls, malicious approvals, and [[oracle-manipulation|exploit]] activity in [[defi|DeFi]], demand for embedded risk-screening keeps growing. Backing from YZi Labs (formerly Binance Labs) and OKX Ventures, plus Binance Alpha/HODLer distribution, gives GoPlus strong ecosystem reach. It is one of the more recognized on-chain security data providers.

### Peer comparison

GoPlus competes in the on-chain security / risk-API niche against both token and tokenless providers. As a rough orientation (figures are approximate, per the 2026-06-21 snapshot where applicable):

| Project | Focus | Token | Market cap | Notes |
|---|---|---|---|---|
| **GoPlus Security** | Token/address/phishing risk API, User Security Network | GPS | ~$40M | Wallet/DEX-embedded detection; YZi Labs + OKX Ventures backed |
| Forta | Decentralized real-time threat detection | FORT | small-cap | Bot-based on-chain monitoring network |
| CertiK (Skynet) | Audits + on-chain risk scoring | tokenless (Skynet) | n/a | Audit-led; enterprise/security ratings |
| Blowfish | Wallet transaction simulation/warnings | tokenless | n/a | Major wallet-integrated tx-scanning provider |
| Webacy | Consumer wallet risk monitoring | tokenless | n/a | Retail-facing risk dashboards |

The category's structural challenge is that much security data can be offered free or bundled by wallets, so GPS's token-value thesis rests on a permissionless, incentivized provider network (the User Security Network) being genuinely differentiated from free APIs.

### Valuation framing (qualitative)

GPS is best framed as a **usage-linked infrastructure token, not a cash-flow asset**: there are no audited protocol revenues disclosed in the snapshot to anchor a multiple, so valuation is narrative- and adoption-driven. At ~$40M market cap / ~$91.5M FDV, the market prices GoPlus as a recognized-but-small security-data provider rather than a category winner. Bulls underwrite rising API/detection adoption across wallets and DEXs (a "security layer of Web3" land-grab); bears point to free competing data, monetization difficulty, and the ~56% supply overhang. In an Established Bear Market, a security/"safety" narrative can attract defensive flows (as the +27% week suggests), but micro-cap relative strength is fragile and reverses quickly.

---

## Notable History

- Backed by **YZi Labs (prev. Binance Labs)** and **OKX Ventures**; distributed via Binance HODLer Airdrops and featured in Binance Alpha Spotlight.
- GPS reached an all-time high of **$0.2198** on 2025-01-31; the token now trades far below that peak.
- All-time low of **$0.00441135** was printed on 2025-12-18 during the bear market; the price has since roughly doubled off that low, including the sharp ~31% 7-day rally noted above.

> *Additional verified protocol events and news will be added through the wiki's source-ingestion workflow.*

---

## Risks

- **Adoption / demand risk:** GPS value depends on continued integration of GoPlus security services by wallets and DEXes; security data can also be offered free, pressuring monetization.
- **Volatility:** the large recent rally (+27% in 7 days) cuts both ways — sharp moves up in extreme-fear regimes can reverse quickly.
- **Dilution:** ~56% of max supply is not yet circulating (MC/FDV ~0.44); future unlocks can pressure price.
- **Competitive risk:** on-chain security/risk-screening is a competitive niche (multiple audit and risk-API providers).
- **Smart-contract risk:** the token and any on-chain coordination live in [[smart-contracts]] on [[base]] / BNB Chain — ironic exposure for a security project, and a reminder that no provider is immune.
- **Market regime:** with the Fear & Greed Index ≈ 23 (extreme fear) in an Established Bear Market, small-cap tokens remain prone to abrupt drawdowns even after strong rallies.

---

## Related

- [[crypto-markets]]
- [[base]]
- [[smart-contracts]]
- [[oracle-manipulation]]
- [[defi]]
- [[decentralized-exchange]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-21: cryptodataapi.com / CoinGecko top-1000 markets data.

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | GPS |
| **Market Cap Rank** | #480 |
| **Market Cap** | $43.68M |
| **Current Price** | $0.00990444 |
| **Categories** | Cybersecurity, Binance HODLer Airdrops, Binance Alpha Spotlight, Base Native |
| **Website** | [https://gopluslabs.io/](https://gopluslabs.io/) |

---

## Overview

GoPlus is revolutionizing Web3 user security through its permissionless and user-driven User Security Network, which provides comprehensive protection across the entire user transaction lifecycle. GoPlus aims to create a more secure and user-friendly Web3 on-chain interaction environment by filling the gap of the security layer in the current blockchain's architecture, providing users with more effective and better-experienced on-chain security protection.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 4.41B GPS |
| **Total Supply** | 10.00B GPS |
| **Max Supply** | 10.00B GPS |
| **Fully Diluted Valuation** | $99.06M |
| **Market Cap / FDV Ratio** | 0.44 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.2198 (2025-01-31) |
| **Current vs ATH** | -95.49% |
| **All-Time Low** | $0.00441135 (2025-12-18) |
| **Current vs ATL** | +124.85% |
| **24h Change** | +3.88% |
| **7d Change** | +2.38% |
| **30d Change** | +12.84% |
| **1y Change** | -58.98% |

---

## Platform & Chain Information

**Native Chain:** Base

### Contract Addresses

| Chain | Address |
|---|---|
| Base | `0x0c1dc73159e30c4b06170f2593d3118968a0dca5` |
| Binance Smart Chain | `0x9a4a67721573f2c9209dfff972c52be4e3f6642e` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | GPS/USDT | N/A |
| Bitget | GPS/USDT | N/A |
| KuCoin | GPS/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://gopluslabs.io/](https://gopluslabs.io/) |
| **Twitter** | [@GoPlusSecurity](https://twitter.com/GoPlusSecurity) |
| **Telegram** | [GoPlusSecurity](https://t.me/GoPlusSecurity) (7,751 members) |
| **Discord** | [https://discord.com/invite/goplus](https://discord.com/invite/goplus) |
| **GitHub** | [https://github.com/GoPlusSecurity/GPS-AUDIT](https://github.com/GoPlusSecurity/GPS-AUDIT) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $4.65M |
| **Market Cap Rank** | #480 |
| **24h Range** | $0.00945131 — $0.00993891 |
| **CoinGecko Sentiment** | 0% positive |
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
- [[base]]

---
