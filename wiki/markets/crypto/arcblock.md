---
title: "Arcblock"
type: entity
created: 2026-04-09
updated: 2026-06-22
status: excellent
tags: [crypto, altcoins, ai-trading, decentralized-identity]
aliases: ["ABT", "ArcBlock"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.arcblock.io/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[decentralized-identity]]", "[[smart-contracts]]"]
---

# Arcblock

**ArcBlock** (ABT) is a blockchain application platform and developer-tooling ecosystem focused on building decentralized applications (dApps), [[decentralized-identity]] (DID), and — more recently — AI agent infrastructure. Founded in 2017 with its token sale in early 2018, ArcBlock positions itself not as a base-layer chain but as an *abstraction and tooling layer* that lets developers assemble cloud-native, blockchain-backed services. The ABT token is an ERC-20 asset on [[ethereum]].

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).* ABT trades at **$0.204303**, ranked **#829** by market capitalization (~**$20.09M**), up **+3.48%** over 24h and essentially flat over 7 days (**-0.08%**). The token remains roughly 90%+ below its May 2024 all-time high near $4.69, against a fearful market backdrop (Fear & Greed Index 22, "Extreme Fear").

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | ABT |
| **Market Cap Rank** | #829 |
| **Market Cap** | ~$20.09M |
| **Current Price** | $0.204303 |
| **24h Change** | +3.48% |
| **7d Change** | -0.08% |
| **Categories** | Artificial Intelligence (AI), Infrastructure, Ethereum Ecosystem, AI Framework, Made in USA |
| **Token Standard** | ERC-20 ([[ethereum]]) |
| **Website** | [https://www.arcblock.io/](https://www.arcblock.io/) |
> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

---

## Overview

ArcBlock launched in 2017–2018 as one of the more prominent ICO-era projects pitching a "third generation" of blockchain applications. Its original thesis was that mainstream developers found existing blockchains too hard to build on, and that an abstraction layer — bridging dApps to underlying chains and to conventional cloud infrastructure — would unlock broader adoption. Over the following years the project moved away from grand multi-chain interoperability marketing toward a concrete product stack centered on **Blocklets**, the **ABT Node**, decentralized identity, and AI agents.

Rather than competing as a raw high-throughput [[layer-1]], ArcBlock occupies the "application platform / middleware" niche — comparable in spirit to a decentralized application server. Its long-term relevance depends on developer adoption of its tooling rather than on consensus-layer performance.

---

## Architecture and Product Stack

- **Blocklets** — modular, composable application components (the project's analog to micro-apps or serverless functions) that developers package and deploy. They are the core unit of ArcBlock's "build by assembly" model.
- **ABT Node** — the runtime/server that hosts and orchestrates Blocklets, providing identity, storage, and chain-connectivity services to applications.
- **DID / Decentralized Identity** — ArcBlock implements [[decentralized-identity]] primitives (a DID Wallet and verifiable credentials) so applications can offer self-sovereign login and credentialing instead of relying on centralized identity providers.
- **AIGNE** — the project's AI framework / agent layer, reflecting its repositioning toward AI agent infrastructure built on top of the Blocklet/ABT Node stack. This is why CoinGecko tags ABT under "Artificial Intelligence (AI)" and "AI Framework."

The ABT token pays for fees and services within the ArcBlock platform and supports staking/incentive mechanisms tied to its node and identity services. As an ERC-20 token, ABT does not secure a standalone consensus network; settlement and transfers occur on [[ethereum]].

### How the pieces fit together

The mental model is a **decentralized application server (PaaS)**: a developer runs an **ABT Node** (self-hosted or cloud), installs **Blocklets** (composable app components from a marketplace) to assemble a service, uses the built-in **DID Wallet / verifiable credentials** for self-sovereign login, and — in the newer phase — wires in **AIGNE** AI-agent components. ABT is the settlement/access asset that meters services and incentivizes node operators and Blocklet developers. Critically, this is **off-chain-heavy infrastructure** with on-chain settlement and identity anchoring; most compute happens on the node, not on Ethereum. That makes ArcBlock more like a Web3-flavored Heroku/Vercel than a base layer.

---

## Token Utility & Value Accrual

ABT functions as the platform's utility and incentive token: paying for platform/cloud services, accessing Blocklet marketplace functionality, and aligning incentives between node operators, developers, and users. Because the project is an application platform rather than a sovereign chain, ABT's value accrual is tied to usage of ArcBlock's hosted services and developer ecosystem rather than to block rewards or gas on a native chain.

**Value accrual critique:** the bull case requires real, paying developer usage of ABT Node / Blocklets / AIGNE that routes value through the token. This is hard to verify externally, and a PaaS can in principle be paid for in fiat or stablecoins, weakening the token's necessity. Supply is **not fully circulating** (MC/FDV ≈ 0.53), so there is a meaningful future-dilution overhang versus circulating cap — a structural headwind if demand does not grow into the diluted supply. The recent re-rating into the "AI framework / AI agent" narrative has been **sentiment-led** (see the +106% 30-day move recorded in Price History) rather than driven by demonstrable revenue.

---

## Comparison vs Web3 App-Platform / DID / AI-Infra Peers

| Dimension | **ArcBlock (ABT)** | [[internet-computer\|Internet Computer (ICP)]] | Fetch.ai / ASI (FET) | Civic / DID projects |
|---|---|---|---|---|
| **Type** | Web3 app-platform / PaaS + DID + AI agents | L1 hosting full dapps on-chain | AI-agent network + token | Decentralized identity |
| **Where compute runs** | ABT Node (off-chain), settles on Ethereum | On-chain canisters (subnets) | Agent network / off-chain | Off-chain + on-chain attest |
| **Identity** | Native DID Wallet + verifiable credentials | Internet Identity | n/a | Core focus |
| **AI angle** | AIGNE agent framework (newer) | Compute for AI dapps | AI agents core thesis | Limited |
| **Token role** | Service fees, node/Blocklet incentives | Gas (cycles), governance, staking | Agent fees, staking | Identity/attestation fees |
| **Scale/cap** | Micro-cap (~$20M) | Large-cap L1 | Large/mid-cap AI token | Small-cap |

ArcBlock's relative strength is a long-lived, integrated dev stack with native DID. Its relative weaknesses are micro-cap scale, weak external evidence of paid adoption, and a token whose necessity in the stack is not obviously enforced.

---

## Risks

- **Small-cap / illiquidity risk** — at ~$20M market cap and modest reported volumes, ABT is thinly traded and prone to high volatility and slippage.
- **Narrative-dependence** — the "AI framework / AI agent" tagging is heavily marketing-driven; rallies and drawdowns in low-cap AI tokens tend to be sentiment- rather than fundamentals-led.
- **Adoption uncertainty** — as a tooling/middleware platform, ArcBlock's value depends on developers actually building on Blocklets and the ABT Node; this is hard to verify externally and competitive (it competes with mainstream Web2/Web3 dev stacks).
- **Drawdown** — the token is down >90% from its 2024 peak; long underwater positioning is common for ICO-era infrastructure tokens.
- **Counterparty/contract risk** — as an ERC-20, ABT is exposed to smart-contract and bridge risks of the broader [[ethereum]] ecosystem.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 98.58M ABT |
| **Total Supply** | 186.00M ABT |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $63.80M |
| **Market Cap / FDV Ratio** | 0.53 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $4.69 (2024-05-21) |
| **Current vs ATH** | -92.69% |
| **All-Time Low** | $0.0495 (2020-03-13) |
| **Current vs ATL** | +593.18% |
| **24h Change** | -6.36% |
| **7d Change** | +24.61% |
| **30d Change** | +106.12% |
| **1y Change** | -32.37% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xb98d4c97425d9908e66e53a6fdf673acca0be986` |

---

## Exchange Listings

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0XB98D4C97425D9908E66E53A6FDF673ACCA0BE986/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.arcblock.io/](https://www.arcblock.io/) |
| **Twitter** | [@ArcBlock_io](https://twitter.com/ArcBlock_io) |
| **Reddit** | [https://www.reddit.com/r/arcblock/](https://www.reddit.com/r/arcblock/) |
| **Telegram** | [ArcBlock](https://t.me/ArcBlock) (2,902 members) |
| **GitHub** | [https://github.com/ArcBlock/ArcBlock-Token](https://github.com/ArcBlock/ArcBlock-Token) |
| **Whitepaper** | [https://drive.google.com/file/d/1kQ58pxJViKC0I28rZDQ8XzDgwrupLYN/view?usp=sharing](https://drive.google.com/file/d/1kQ58pxJViKC0I28rZDQ8XzDgwrupLYN/view?usp=sharing) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 29 |
| **GitHub Forks** | 11 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $476,978.00 (2026-04-09 snapshot) |
| **Market Cap Rank** | #829 (2026-06-21) |
| **Last Updated** | 2026-06-21 |
> *Older intraday range/volume figures reflect the 2026-04-09 snapshot and are retained for history; current price/rank/market cap are 2026-06-21 (see Key Facts).*

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## How & Where ABT Trades

- **Spot venues:** ABT has historically listed on centralized exchanges (it traded on Binance in earlier years) and on smaller CEXs; current CEX depth is modest. On-chain, ABT is an ERC-20 traded on **Uniswap V3** against WETH.
- **Liquidity profile:** with a ~$20M cap (rank ~#829) and reported 24h volume historically under ~$0.5M, ABT is **very thin**. It is prone to sharp, low-liquidity moves — the +106% 30-day / +24.6% 7-day swings in its own price history illustrate how violently a micro-cap can re-rate on the AI narrative.
- **Derivatives:** little to no meaningful perp coverage; assume spot-only with shallow books.
- **Implication:** ABT is a momentum/narrative micro-cap where a small flow can move price double digits in a day — high reward but high whipsaw and exit-liquidity risk.

---

## Narrative, Category & Catalysts

- **Category:** Web3 application platform / decentralized identity, repositioned into the **AI agent / AI framework** narrative (AIGNE), which is why CoinGecko tags it "Artificial Intelligence (AI)" and "AI Framework."
- **Bull catalysts:** the broad **AI + crypto** narrative; demonstrable developer/enterprise adoption of ABT Node, Blocklets, or AIGNE; DID/verifiable-credential demand; any partnership translating into on-chain ABT usage.
- **Bear/structural headwinds:** narrative-led (not revenue-led) pricing, ICO-era baggage, ~50% future-dilution overhang (MC/FDV ≈ 0.53), micro-cap illiquidity, and competition from far larger AI-infra and L1 platforms.

---

## History / Timeline

- **2017:** ArcBlock founded, pitching a "third-generation" blockchain application platform.
- **2018 (early):** ABT token sale during the ICO boom; positioned as a developer-tooling/abstraction layer.
- **2019–2021:** product stack matured around **Blocklets**, the **ABT Node**, and **DID Wallet / verifiable credentials**.
- **2020-03-13:** all-time low around **$0.0495** during the COVID crash.
- **2024-05-21:** all-time high near **$4.69** (per the page's recorded price history).
- **2024–2026:** repositioning toward **AIGNE** AI-agent infrastructure, riding the AI-crypto narrative; the token saw large sentiment-driven swings.
- **2026-06-21/22:** ABT trades ~$0.20, >90% below ATH, in an Extreme-Fear regime.

> Dates reflect the page's recorded market data and widely documented project history; verify specific adoption/partnership claims independently.

---

## Trading Playbook (bear / Extreme-Fear regime)

> Context: F&G = 21 (Extreme Fear), established bear market, [[btc-bitcoin|BTC]] ~$64k. ABT is a very thin AI-narrative micro-cap with violent swings.

- **Bias:** treat as a high-volatility narrative trade, not an investment. Pricing is driven by AI sentiment and low-float mechanics, not verifiable revenue.
- **Longs:** if trading the AI narrative, size tiny and for total loss; the +100%+ monthly swings cut both ways. Prefer entries after consolidation, not after a vertical spike (which is often exit liquidity).
- **Avoid:** leverage and "investing for fundamentals" without external evidence of paid adoption; also be mindful of the ~50% dilution overhang.
- **Risk controls:** hard stops and predefined invalidation are essential given the whipsaw; do not average down into a thin micro-cap.
- **Watch:** broad AI-token index strength, ABT Node / AIGNE usage signals, and on-chain ABT volume as leading tells.

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[decentralized-identity]]
- [[smart-contracts]]
- [[layer-1]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]]) — initial market-data snapshot
- Market data 2026-06-21: cryptodataapi.com / CoinGecko (price, rank, market cap)
- Architecture and product descriptions (Blocklets, ABT Node, DID, AIGNE): general market knowledge; no specific wiki source ingested yet.
