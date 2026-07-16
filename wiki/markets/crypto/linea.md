---
title: "Linea"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto]
aliases: ["LINEA"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://linea.build/association"
related: ["[[consensys]]", "[[crypto-markets]]", "[[ethereum]]", "[[layer-2]]", "[[zero-knowledge-proofs]]"]
---

# Linea

**Linea** (ticker **LINEA**) is a [[layer-2]] [[zero-knowledge-proofs|zk]]-rollup for [[ethereum]], built by [[consensys]] (the company behind MetaMask and Infura). It is a Type-2 zkEVM — fully Ethereum-equivalent at the bytecode level — that batches transactions off-chain and posts validity proofs to Ethereum [[mainnet]]. Its design is explicitly aligned with Ethereum: LINEA tokenomics route protocol revenue into burning both ETH and LINEA, positioning the chain as an ETH-aligned execution layer rather than a competing [[layer-1]]. Governance sits with the Linea Association, a non-profit consortium of Ethereum-native builders.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | LINEA |
| **Market Cap Rank** | #391 |
| **Market Cap** | $61.63M |
| **Current Price** | $0.00254735 |
| **24h Change** | +3.75% |
| **7d Change** | -2.34% |
| **24h Volume** | $9.94M |
| **All-Time High** | $0.04667 (September 2025) |
| **All-Time Low** | $0.00226 |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

The broader tape is risk-off: the crypto [[fear-and-greed-index|Fear & Greed Index]] sits at **23 (extreme fear)** and the long-horizon regime reads as an **Established Bear Market** as of 2026-06-21. LINEA is one of the firmer names in this peer group on the day (+3.75%) but still trades roughly 13% above its all-time low (~$0.00226) and about 95% below its September-2025 all-time high (~$0.0467) — a typical post-airdrop drawdown profile for a recently launched [[layer-2]] token.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~24.17B LINEA |
| **Total Supply** | ~71.59B LINEA |
| **Max Supply** | ~72.01B LINEA |
| **Fully Diluted Valuation (FDV)** | ~$183.43M |
| **Market Cap / FDV** | ~0.34 |

With circulating supply only ~34% of fully diluted supply, a large share of tokens remains locked in ecosystem and contributor allocations, implying meaningful future emission and dilution pressure. Notably, LINEA is **not** the gas token of the network — transactions on Linea are paid in [[ethereum|ETH]]. The token's value accrual is driven by a dual-burn mechanism: a portion of net protocol fees (in ETH) is used to burn ETH, and the remainder buys back and burns LINEA, tying token scarcity to network usage rather than to staking inflation. There is no native LINEA staking-for-security model in the conventional [[proof-of-stake]] sense, since the chain's security inherits from Ethereum via validity proofs.

---

## How & Where It Trades

**Spot venues.** LINEA is listed on major centralized exchanges including [[binance]] (LINEA/USDT), [[kraken]] (LINEA/USD), Upbit (LINEA/KRW), Bitget, KuCoin, and Crypto.com. On-chain, it trades on Uniswap V3 (Ethereum) and DEXs within the Linea ecosystem.

**Derivatives.** A LINEA perpetual is listed on [[hyperliquid]] (LINEA-PERP), alongside perp markets on the major centralized derivatives venues. As a small-cap (~$59M) token, open interest and funding are thin and prone to sharp swings; funding/OI should be checked live before sizing any leveraged position. Liquidity is concentrated in USDT pairs, and 24h volume (~$9.7M) is modest relative to market cap, so slippage on larger orders is a real concern.

---

## Technology & Consensus

Linea is a **Type-2 zkEVM** — bytecode-equivalent to Ethereum, meaning existing Solidity contracts and developer tooling work unchanged. The architecture follows the standard zk-rollup pattern:

- A **sequencer** orders and executes transactions off-chain.
- A **prover** generates succinct [[zero-knowledge-proofs|zero-knowledge validity proofs]] (using a lattice-based proof system) attesting that the state transition is correct.
- Proofs and compressed transaction data are posted to [[ethereum|Ethereum L1]], which acts as the settlement and data-availability layer.

Because correctness is enforced cryptographically by validity proofs (not by an optimistic challenge window), withdrawals do not require the multi-day fraud-proof delay associated with optimistic rollups like [[arbitrum]] and [[optimism]]. Security ultimately inherits from Ethereum.

---

## Use Case, Narrative & Category

Linea sits in the **Ethereum-scaling / zkEVM L2** category alongside [[zksync]], [[starknet]], Polygon zkEVM, and [[scroll]]. Its differentiated narrative is "ETH alignment": the chain is marketed as the place where ETH capital is most productive (native yield on bridged ETH, ETH burn, deep DeFi integration), leaning on Consensys's distribution through MetaMask and Infura. Categories tagged on the asset include Smart Contract Platform, Ethereum Ecosystem, Layer 2 (L2), Zero Knowledge (ZK), Linea Ecosystem, and Consensys Portfolio.

---

## Valuation Framing (qualitative)

Linea is a ~$62M-cap zkEVM L2 token with a distinctive value-accrual design: it is **not** the gas token (gas is paid in [[ethereum|ETH]]), and instead accrues value through a dual-burn of ETH and LINEA funded by protocol fees. That makes the bull case explicitly a *usage-and-burn* flywheel — if Linea captures meaningful L2 activity, the burn tightens supply — backed by [[consensys]]'s MetaMask/Infura distribution. The bear case is twofold: MC/FDV ≈ 0.34 means ~66% of supply is still locked and emitting, a structural overhang; and post-EIP-4844 blob pricing has compressed L2 fees across the board, shrinking the revenue that powers the burn just as zkEVM competition (zkSync, Starknet, Scroll, Polygon zkEVM) intensifies. A young, unproven flywheel against a deep dilution schedule. Not investment advice.

---

## Peer Comparison

| Project | Ticker | Category | MC Rank | Market Cap | MC/FDV | Gas token |
|---|---|---|---|---|---|---|
| **Linea** | LINEA | zkEVM [[layer-2]] | #391 | $61.63M | ~0.34 | [[ethereum\|ETH]] (not LINEA) |
| [[zksync]] | ZK | zkEVM L2 | — | — | — | ETH |
| [[starknet]] | STRK | zk-rollup L2 | — | — | — | STRK / ETH |
| [[mina-protocol]] | MINA | Succinct zk [[layer-1]] | #427 | $54.22M | ~1.00 | MINA |
| [[astar]] | ASTR | Multi-chain L1/L2 (zkEVM) | #475 | $47.34M | ~0.87 | ASTR |

*Among ZK peers, Linea is unusual in not using its own token for gas — value accrual rests entirely on the ETH/LINEA dual-burn rather than on gas demand or staking inflation.*

---

## Notable History

- Linea launched its mainnet (alpha) in mid-2023, incubated by [[consensys]].
- The **LINEA token generation event** occurred in September 2025; the token printed its all-time high (~$0.0467) shortly after launch before entering a prolonged decline.
- As of 2026-06-21 the token trades near its all-time low (~$0.00226), down ~95% from ATH — consistent with broad post-airdrop unwinding and the prevailing bear-market regime, though it posted a modest daily bounce against the peer set.

---

## Risks

- **Dilution.** Circulating supply is only ~34% of total; ongoing unlocks of ecosystem and contributor allocations are a structural overhang.
- **Centralization (current).** Like most rollups, Linea's sequencer and prover are not yet fully decentralized, creating censorship and liveness risk and a trusted operator dependency.
- **Intense L2 competition.** zkEVM is a crowded field; fee compression (post-EIP-4844 blob pricing) squeezes the revenue that funds the burn mechanism.
- **Value-accrual uncertainty.** Since gas is paid in ETH, LINEA's value depends entirely on the burn/buyback mechanism scaling with usage — an unproven flywheel for a young chain.
- **Liquidity / volatility.** Small-cap microstructure: thin order books, ~$9.7M daily volume, and an extreme-fear macro backdrop amplify drawdowns.

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[layer-2]]
- [[zero-knowledge-proofs]]
- [[consensys]]
- [[hyperliquid]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-21 (cryptodataapi.com / CoinGecko bulk endpoint), `raw/data/crypto-loop/coingecko-markets.json`.

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | LINEA |
| **Market Cap Rank** | #384 |
| **Market Cap** | $59.21M |
| **Current Price** | $0.00244928 |
| **Categories** | Smart Contract Platform, Layer 2 (L2), Zero Knowledge (ZK), Binance Alpha Spotlight |
| **Website** | [https://linea.build/association](https://linea.build/association) |

---

## Overview

Linea is the Layer 2 built from first principles to strengthen Ethereum and the entire ETH economy. Every aspect of its design—from its productive ETH burn mechanics, and capital efficient native yield, to its underlying Ethereum-equivalent zk tech—amplifies the value and utility of Ethereum Mainnet. All of this is backed by the largest ecosystem fund in the space, managed by the most trusted Ethereum builders. With institutional-grade infrastructure, and deep integration across DeFi, Linea is the best chain for ETH capital, where every transaction and every block strengthens Ethereum.
Linea is where Ethereum wins.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 24.17B LINEA |
| **Total Supply** | 71.59B LINEA |
| **Max Supply** | 72.01B LINEA |
| **Fully Diluted Valuation** | $175.35M |
| **Market Cap / FDV Ratio** | 0.34 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.0467 (2025-09-10) |
| **Current vs ATH** | -94.75% |
| **All-Time Low** | $0.00221220 (2026-06-26) |
| **Current vs ATL** | +10.72% |
| **24h Change** | -0.90% |
| **7d Change** | +1.24% |
| **30d Change** | -5.92% |
| **1y Change** | +0.00% |

---

## Platform & Chain Information

**Native Chain:** Linea

### Contract Addresses

| Chain | Address |
|---|---|
| Linea | `0x1789e0043623282d5dcc7f213d703c6d8bafbb04` |
| Ethereum | `0x1789e0043623282d5dcc7f213d703c6d8bafbb04` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | LINEA/USDT | N/A |
| Kraken | LINEA/USD | N/A |
| Upbit | LINEA/KRW | N/A |
| Bitget | LINEA/USDT | N/A |
| KuCoin | LINEA/USDT | N/A |
| Crypto.com Exchange | LINEA/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0X1789E0043623282D5DCC7F213D703C6D8BAFBB04/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://linea.build/association](https://linea.build/association) |
| **Twitter** | [@LineaBuild](https://twitter.com/LineaBuild) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $7.75M |
| **Market Cap Rank** | #384 |
| **24h Range** | $0.00243871 — $0.00251654 |
| **CoinGecko Sentiment** | 83% positive |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---
