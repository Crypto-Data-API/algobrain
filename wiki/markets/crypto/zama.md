---
title: "Zama"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto]
aliases: ["ZAMA"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.zama.org/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[fully-homomorphic-encryption]]", "[[hyperliquid]]", "[[solana]]", "[[zero-knowledge-proofs]]"]
---

# Zama

**Zama** (ZAMA) is the token of Zama, an open-source cryptography company building **[[fully-homomorphic-encryption|Fully Homomorphic Encryption (FHE)]]** infrastructure for blockchains. FHE lets computation run directly on encrypted data without ever decrypting it, enabling **confidential smart contracts** — where transaction amounts, balances, and state can stay private while still being verifiably processed on-chain. The token underpins the Zama Protocol / Zama Gateway, with deployments spanning [[ethereum|Ethereum]], BNB Chain, and [[solana]].

Zama is one of the leading names in the "confidential compute" / privacy-infrastructure narrative, alongside other FHE and [[zero-knowledge-proofs|ZK]]-privacy projects. Its developer toolchain (TFHE-rs, fhEVM/confidential EVM) is widely cited in the FHE space.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | ZAMA |
| **Price** | $0.03449899 |
| **Market Cap** | $75.91M |
| **Market Cap Rank** | #327 |
| **24h Volume** | $8.90M |
| **24h Change** | -1.84% |
| **7d Change** | +7.27% |
| **Fully Diluted Valuation** | ~$379.49M (at 11.00B total supply; no fixed max) |
| **Market Cap / FDV** | ~0.20 |
| **All-Time High** | $0.04103617 |
| **All-Time Low** | $0.01673142 |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

Backdrop: snapshot taken during an **Established Bear Market** with the [[crypto-fear-and-greed-index|Crypto Fear & Greed Index]] at **23 (Extreme Fear)**. Notably, ZAMA is one of the few tokens in this infra cohort showing strength against the tape — **+7.3% over 7 days** despite a modestly red day — supported by solid ~$8.9M daily volume. It trades only ~16% below its ATH, the shallowest drawdown in this group.

---

## Technology & Protocol

Zama productizes **[[fully-homomorphic-encryption|FHE]]** for blockchains:

- **TFHE-rs** — a high-performance Rust library implementing the TFHE (Fast Fully Homomorphic Encryption over the Torus) scheme, enabling Boolean and integer operations directly on ciphertexts.
- **fhEVM / Confidential EVM** — a framework that adds encrypted data types and operations to the EVM, so Solidity developers can write **confidential smart contracts** where inputs, state, and outputs stay encrypted end-to-end while still being processed by validators.
- **Zama Protocol / Gateway** — the coprocessor and cross-chain layer that performs the heavy FHE computation off the base chain and posts verifiable results back, with a threshold-decryption (MPC) committee controlling when, and to whom, results are revealed.

FHE is the **most general privacy primitive**: unlike [[zero-knowledge-proofs|zero-knowledge proofs]] (which prove statements about hidden data) or TEEs (trusted hardware), FHE allows arbitrary computation over encrypted inputs without trusted hardware. The tradeoff is computational cost — FHE operations are far heavier than plaintext, which is the central engineering and adoption challenge.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~2.20B ZAMA |
| **Total Supply** | ~11.00B ZAMA |
| **Max Supply** | No fixed cap |
| **Circulating / Total** | ~20.0% |
| **Market Cap / FDV** | ~0.20 |

Only ~20% of total supply is circulating — the lowest float in this cohort — and there is **no fixed max supply**, so the **MC/FDV of ~0.20 signals a very large forward-dilution overhang**. The bulk of supply remains allocated to team, investors, ecosystem, and protocol incentives, with future unlocks a key risk variable. Utility centers on paying for / securing FHE computation and the Zama Gateway, plus governance. Low float can amplify both upside spikes and downside on unlock events.

---

## Market Structure & Derivatives

- **Spot venues:** ZAMA has tier-1 centralized listings including Binance and Kraken, plus on-chain liquidity via Uniswap V3 on [[ethereum|Ethereum]] (the canonical contract is an ERC-20, with bridged versions on BNB Chain, the Zama Gateway, and [[solana]]). The token came to market via a Binance Wallet IDO and CoinList launchpad.
- **Derivatives / perps:** ZAMA is among the more liquid infra tokens here and has perpetual-futures markets on major derivatives venues; where listed (e.g. large CEX perp books and potentially [[hyperliquid|Hyperliquid]]), funding and OI are available. The 7-day rally with positive momentum suggests demand for long exposure — verify current funding before sizing, as crowded longs into Extreme Fear can mean-revert.
- **Liquidity note:** ~$8.9M daily volume on a ~$75.9M cap makes ZAMA one of the more tradable names in this group.

---

## Use Case, Narrative & Category

Zama anchors the **FHE / confidential-compute** corner of the privacy-infrastructure narrative. CoinGecko categories include Privacy, Privacy Infrastructure, Cross-chain Communication, and multiple chain ecosystems (Ethereum, BNB, Solana).

The thesis: public blockchains are transparent by default, which blocks many institutional and consumer use cases (private DeFi, confidential payments, sealed-bid auctions, private voting, on-chain identity). [[fully-homomorphic-encryption|FHE]] is the most general privacy primitive — it allows arbitrary computation over encrypted inputs — and Zama provides the libraries and a confidential EVM to make it usable. If confidential smart contracts gain real adoption, Zama is positioned as picks-and-shovels infrastructure. The bear case is that FHE remains computationally heavy/expensive, adoption is early, and competing privacy approaches ([[zero-knowledge-proofs|ZK]], TEEs) may win specific niches.

---

## Valuation Framing

- **Picks-and-shovels infra bet** — ZAMA is a leveraged option on confidential-compute adoption; with little current on-chain usage to anchor cash flows, value is mostly narrative- and roadmap-driven.
- **FDV discipline** — the ~$379M FDV vs ~$76M cap (MC/FDV ~0.20, no hard cap) means the market is pricing in significant future supply; any re-rating must overcome persistent unlock pressure.
- **Drawdown context** — uniquely, ZAMA trades only ~16% below ATH, so it is priced as a fresh, in-favor narrative token rather than a deep-bear-market value name; downside on a narrative cooldown is correspondingly larger.

---

## Peer Comparison

| Token | Privacy approach | Mkt Cap | Rank | MC/FDV | 7d | Note |
|---|---|---|---|---|---|---|
| **ZAMA** | [[fully-homomorphic-encryption|FHE]] / confidential EVM | $76M | #327 | 0.20 | +7.3% | Leading FHE infra; very low float, no max cap |
| [[subsquid]] (SQD) | (data infra, not privacy) | $48M | #471 | 0.81 | +7.1% | Contrast: highest float in cohort |
| [[arkham]] (ARKM) | (transparency / forensics) | $86M | #297 | 0.66 | +1.1% | Opposite thesis: de-anonymization |

> Privacy-narrative comparables also include [[zero-knowledge-proofs|ZK]]-based privacy projects and TEE-based confidential-compute networks; Zama's differentiation is the generality of FHE.

---

## Notable History

- **All-Time High:** $0.04103617 — current price is only ~16% below ATH, the shallowest drawdown of this entire cohort.
- **All-Time Low:** $0.01673142 — current price is ~2.1x above ATL.
- ZAMA is a relatively new listing (ATH and ATL both dated to early 2026), and unlike badly-drawn-down infra peers, it is trading close to its highs — reflecting fresh issuance and an active confidential-compute narrative rather than a long post-launch decline.

---

## Risks

- **Extreme dilution overhang:** lowest float in the cohort (~20%) and no fixed max supply; future unlocks/emissions are the dominant risk.
- **Early/unproven adoption:** confidential smart contracts are nascent; revenue and on-chain usage must materialize to justify valuation.
- **Technical risk:** FHE is computationally expensive; performance/cost may limit practical use vs. [[zero-knowledge-proofs|ZK]] or TEE alternatives.
- **Momentum-reversal risk:** a +7.3% week into Extreme Fear can unwind quickly if it was a short-term squeeze, especially with price near ATH.
- **Multi-chain surface:** contracts on Ethereum, BNB, Solana, and the Zama Gateway add bridge/contract complexity.
- **Macro/sentiment risk:** Established Bear Market with Extreme Fear (F&G 23) is a hostile backdrop for high-FDV narrative tokens.

---

## Related

- [[fully-homomorphic-encryption]] — Zama's core technology
- [[zero-knowledge-proofs]] — competing/complementary privacy primitive
- [[ethereum]] — canonical token chain
- [[solana]] — bridged deployment
- [[hyperliquid]] — perp venue
- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-21 (cryptodataapi.com / CoinGecko).

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | ZAMA |
| **Market Cap Rank** | #303 |
| **Market Cap** | $77.90M |
| **Current Price** | $0.0354 |
| **Categories** | Cross-chain Communication, Binance Wallet IDO, CoinList Launchpad, Privacy Infrastructure, Privacy |
| **Website** | [https://www.zama.org/](https://www.zama.org/) |

---

## Overview

Zama is an open source cryptography company that builds state-of-the-art Fully Homomorphic Encryption (FHE) solutions for blockchain.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 2.20B ZAMA |
| **Total Supply** | 11.00B ZAMA |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $389.48M |
| **Market Cap / FDV Ratio** | 0.20 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.0410 (2026-04-14) |
| **Current vs ATH** | -13.72% |
| **All-Time Low** | $0.0167 (2026-02-12) |
| **Current vs ATL** | +111.62% |
| **24h Change** | +4.16% |
| **7d Change** | +4.72% |
| **30d Change** | +6.85% |
| **1y Change** | +0.00% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xa12cc123ba206d4031d1c7f6223d1c2ec249f4f3` |
| Binance Smart Chain | `0x6907a5986c4950bdaf2f81828ec0737ce787519f` |
| Zama Gateway Mainnet | `0xce762c7fdaac795d31a266b9247f8958c159c6d4` |
| Solana | `4Zp52aF4hZi9fzH19xpbWKYKQvgLyCN67KFbrQDqeTKh` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | ZAMA/USDT | N/A |
| Kraken | ZAMA/USD | N/A |
| Upbit | ZAMA/KRW | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0XA12CC123BA206D4031D1C7F6223D1C2EC249F4F3/0XDAC17F958D2EE523A2206206994597C13D831EC7 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.zama.org/](https://www.zama.org/) |
| **Twitter** | [@zama](https://twitter.com/zama) |
| **Reddit** | [https://www.reddit.com/r/zama/](https://www.reddit.com/r/zama/) |
| **Telegram** | [zama_on_telegram](https://t.me/zama_on_telegram) (67,149 members) |
| **Discord** | [https://discord.gg/zama](https://discord.gg/zama) |
| **GitHub** | [https://github.com/zama-ai](https://github.com/zama-ai) |
| **Whitepaper** | [https://docs.zama.org/protocol/zama-protocol-litepaper](https://docs.zama.org/protocol/zama-protocol-litepaper) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $6.36M |
| **Market Cap Rank** | #303 |
| **24h Range** | $0.0337 — $0.0355 |
| **CoinGecko Sentiment** | 50% positive |
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
