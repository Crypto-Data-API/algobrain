---
title: "Lisk"
type: entity
created: 2026-04-09
updated: 2026-06-22
status: excellent
tags: [crypto, ethereum, altcoins]
aliases: ["LSK"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://lisk.com"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[layer-2]]", "[[optimism]]", "[[optimistic-rollup]]", "[[superchain]]"]
---

# Lisk

**Lisk** (LSK) is an [[ethereum|Ethereum]] [[layer-2|Layer 2]] built on the **[[optimism|OP Stack]]** ([[optimistic-rollup|optimistic rollup]]) and is a member of the **[[optimism|Optimism]] [[superchain|Superchain]]**. Originally launched in 2016 as a standalone, SDK-based proof-of-stake **Layer 1** (one of the oldest projects in crypto), Lisk **migrated to become an Ethereum L2 in 2024**, repositioning around Web3 adoption in emerging markets with very low fees. As of 2026-06-22 LSK trades at **$0.087526**, ranked **#814** with a market capitalization of **~$20.4M**.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).* LSK trades at **$0.087526**, market cap **$20,400,928** (rank **#814**), down **-1.14%** over 24h and down **-7.02%** over 7 days, in a broad risk-off regime (BTC ~$64,166; Fear & Greed Index 21 / Extreme Fear).

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | LSK |
| **Market Cap Rank** | #814 |
| **Market Cap** | $20,400,928 |
| **Current Price** | $0.087526 |
| **24h Change** | -1.14% |
| **7d Change** | -7.02% |
| **Architecture** | Ethereum L2 — OP Stack optimistic rollup, Optimism Superchain member (formerly SDK-based L1) |
| **Categories** | Smart Contract Platform, Ethereum Ecosystem, Layer 2 (L2), Optimism Superchain Ecosystem, Outlier Ventures Portfolio, Lisk Ecosystem |
| **Website** | [https://lisk.com](https://lisk.com) |
> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko). BTC reference ~$64,166, Extreme Fear regime.*

---

## Overview

Lisk is an [[ethereum|Ethereum]] [[layer-2|Layer 2]]. Today it is an [[optimistic-rollup|optimistic rollup]] built on the **[[optimism|OP Stack]]**, posting data to Ethereum [[layer-1|L1]] for [[data-availability|data availability]] and settlement and inheriting Ethereum-rollup security (fraud-proof windows; a centralized [[sequencer|sequencer]] in the current OP-Stack default). As a member of the **[[optimism|Optimism]] [[superchain|Superchain]]**, Lisk shares standards and aims for native interoperability with other OP-Stack chains such as [[base|Base]], Optimism (OP Mainnet), Mode, and Worldchain.

The product focus is **emerging-markets Web3 adoption**: low, predictable fees and builder programs (grants, tooling, seed liquidity) targeted at developers in cost-sensitive regions. Lisk's long history — it has existed since 2016 — is unusual; its old PoS chain used a delegated-proof-of-stake (DPoS) design with the Lisk SDK, which is why legacy data sources still tag it with a DPoS "hashing algorithm". That model no longer reflects the current OP-Stack L2 architecture.

---

## Architecture & Consensus

### How the OP-Stack rollup works

As an [[optimistic-rollup|optimistic rollup]] on the **[[optimism|OP Stack]]**, Lisk executes transactions off-chain and posts data and state commitments to [[ethereum|Ethereum]] [[layer-1|L1]]:

- A **sequencer** orders and batches L2 transactions, gives users fast "soft" confirmations, and compresses batches before posting them to Ethereum for [[data-availability|data availability]] and settlement.
- Security is **optimistic**: state roots are assumed valid and can be challenged via **fraud proofs** within a dispute window (historically ~7 days for OP-Stack withdrawals). Honest challengers can prove invalid state and prevent fraudulent withdrawals.
- Because data is published to Ethereum, anyone can reconstruct L2 state and submit a challenge, so Lisk inherits Ethereum-rollup security *for funds*, distinct from an alt-L1 or a sidechain.
- Post-EIP-4844, OP-Stack chains post data as cheap **blobs**, materially lowering fees — part of why Lisk can target low-cost emerging-market use.

### Superchain membership

Lisk is a member of the **[[optimism|Optimism]] [[superchain|Superchain]]** — a set of OP-Stack chains sharing a standardized stack, security model, and a roadmap toward **native cross-chain interoperability** and **shared/decentralized sequencing**. Peers include [[base|Base]], OP Mainnet, Mode, and Worldchain. Membership ties Lisk to Optimism Collective governance and standards but also to the same centralized-sequencer limitations that the Superchain is working to decentralize (see [[#Risks]]).

### Comparison with peer Ethereum L2s

| Chain | Stack | Proof system | DA | Differentiator |
|---|---|---|---|---|
| **Lisk (LSK)** | [[optimism\|OP Stack]] (Superchain) | Optimistic (fraud proofs) | Ethereum (blobs) | Emerging-markets adoption; ex-L1 pivot |
| [[base\|Base]] | OP Stack (Superchain) | Optimistic | Ethereum | Coinbase distribution; no native token |
| OP Mainnet | OP Stack (Superchain) | Optimistic | Ethereum | Reference Superchain chain (OP token) |
| Arbitrum One | Nitro (own) | Optimistic (interactive) | Ethereum | Largest L2 by TVL; mature |
| zkSync / Starknet | ZK | Validity proofs | Ethereum | Faster finality, no challenge window |

Versus [[aurora-near|Aurora]] (an EVM-on-[[near-protocol|NEAR]] whose security comes from NEAR, *not* Ethereum), Lisk is a **true Ethereum rollup**: its funds-security ultimately derives from Ethereum L1, a meaningfully stronger trust model. Its competitive challenge is differentiation in a crowded OP-Stack field where it lacks the distribution of [[base|Base]] or the TVL of Arbitrum.

---

## L1 → L2 Migration

Lisk's defining recent event is its **migration from a standalone Layer 1 to an Ethereum Layer 2**. The original Lisk (2016) was an independent DPoS blockchain with its own JavaScript-based SDK for sidechains. After years as an L1, the project re-launched on the **OP Stack** within the **Optimism Superchain** in 2024, with the **LSK token migrating** from the old chain to an ERC-20 on Ethereum (contract `0x6033f7f88332b8db6ad452b7c6d5bb643990ae3f`) and bridged onto the Lisk L2. This is a relatively rare full architectural pivot — abandoning a bespoke L1 to ride Ethereum's security and the Superchain's interoperability.

---

## Token & What It Does

The **LSK** token is the network's governance and ecosystem-incentive asset, and is used within the Lisk L2 ecosystem (staking/incentives, governance, and grants programs). On the OP-Stack L2, gas is paid in ETH per OP-Stack defaults, so LSK functions primarily as a governance/utility token. Total / max supply is 400M LSK with roughly 227M circulating (market-cap-to-FDV ~0.57).

### Staking and value accrual

Lisk runs **LSK staking** programs that let holders lock tokens to participate in governance and earn rewards/airdrops, including allocations tied to ecosystem and Superchain incentive programs. The token's **value-accrual is governance-centric rather than fee-driven**: because gas is paid in ETH (OP-Stack default), L2 transaction fees do not flow to LSK the way native-token gas accrues to an L1. LSK value therefore depends on governance utility, staking incentives, grant/treasury programs, and any future mechanisms the DAO enacts (e.g., revenue sharing or buybacks). Note the **MC/FDV ~0.57** — circulating supply (~227M) is well below the 400M max, so future unlocks/emissions are a potential dilution headwind. Confirm the current staking terms and emission schedule against Lisk's live documentation.

### Governance

LSK is the governance asset of the **Lisk DAO**: holders (often via staking) vote on grants, treasury and ecosystem-fund allocation, and protocol/ecosystem direction. As a Superchain member, Lisk is also subject to **Optimism Collective** standards and shared governance for Superchain-wide parameters (e.g., security council, sequencing roadmap). Practical influence concentrates among large holders, the Lisk Foundation, and the Optimism governance process; verify quorum and turnout independently.

---

## Risks

- **Sequencer centralization** — as a standard OP-Stack chain, Lisk relies on a centralized [[sequencer]] today; censorship/liveness depend on it pending Superchain-wide decentralized sequencing.
- **Rollup security assumptions** — optimistic-rollup safety depends on honest fraud-proof submission within the challenge window and on Ethereum [[data-availability|data availability]]; withdrawal finality is delayed by the dispute window.
- **Weak token value accrual** — gas is paid in ETH, so L2 usage does not directly accrue to LSK; the token relies on governance/incentive demand, which can decouple from real activity.
- **Supply overhang** — MC/FDV ~0.57 means substantial supply is still to enter circulation; unlocks/emissions can pressure price.
- **Migration / legacy risk** — the L1→L2 pivot, token migration, and bridging introduce transitional complexity; legacy holders had to migrate, and the value proposition is now entirely tied to the crowded Ethereum-L2 market.
- **Competition & crowding** — Lisk competes with many other OP-Stack/Superchain L2s ([[base|Base]], OP Mainnet, Mode) and non-OP L2s (Arbitrum, zkSync) for users and liquidity; "emerging-markets" positioning is a thesis, not a moat.
- **Token decay & liquidity** — LSK trades ~99% below its 2018 all-time high (~$20.4M cap, rank #814), reflecting the long timeline and the current Extreme-Fear regime.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 227.31M LSK |
| **Total Supply** | 400.00M LSK |
| **Max Supply** | 400.00M LSK |
| **Fully Diluted Valuation** | $50.96M |
| **Market Cap / FDV Ratio** | 0.57 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $34.92 (2018-01-07) |
| **Current vs ATH** | -99.64% |
| **All-Time Low** | $0.1017 (2017-03-01) |
| **Current vs ATL** | -13.93% |
| **24h Change** | -1.14% |
| **7d Change** | -7.02% |
| **30d Change** | -1.44% |
| **1y Change** | -68.76% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x6033f7f88332b8db6ad452b7c6d5bb643990ae3f` |
| Base | `0xac485391eb2d7d88253a7f1ef18c37f4242d1a24` |
| Lisk | `0xac485391eb2d7d88253a7f1ef18c37f4242d1a24` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | LSK/USDT | N/A |
| Kraken | LSK/USD | N/A |
| Upbit | LSK/KRW | N/A |
| Bitget | LSK/USDT | N/A |
| KuCoin | LSK/USDT | N/A |
| Crypto.com Exchange | LSK/USD | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://lisk.com](https://lisk.com) |
| **Twitter** | [@Lisk](https://twitter.com/Lisk) |
| **Reddit** | [https://www.reddit.com/r/Lisk](https://www.reddit.com/r/Lisk) |
| **Discord** | [https://discord.com/invite/lisk](https://discord.com/invite/lisk) |
| **GitHub** | [https://github.com/LiskHQ/lisk-sdk](https://github.com/LiskHQ/lisk-sdk) |
| **Whitepaper** | [https://docs.lisk.com](https://docs.lisk.com) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 2,741 |
| **GitHub Forks** | 481 |
| **Commits (4 weeks)** | 4 |
| **Pull Requests Merged** | 3,695 |
| **Contributors** | 66 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **Price (2026-06-22)** | $0.087526 |
| **Market Cap (2026-06-22)** | $20,400,928 |
| **Market Cap Rank** | #814 |
| **24h Change** | -1.14% |
| **7d Change** | -7.02% |
| **24h Volume / Range (2026-04-09 snapshot)** | $1.68M / $0.1272 — $0.1307 |
| **Last Updated** | 2026-06-22 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

- **2016 launch (L1):** Lisk launched as an independent **delegated-proof-of-stake** Layer 1 with a JavaScript-based SDK for building sidechains — one of the oldest projects in crypto. It raised a sizable ICO in BTC at the time.
- **2018 all-time high:** LSK peaked at **$34.92** on 2018-01-07 during the prior cycle; it has since fallen ~99.6% from that peak.
- **2024 L1→L2 migration:** Lisk re-launched on the **[[optimism|OP Stack]]** within the **[[superchain|Optimism Superchain]]**, migrating the **LSK token** to an ERC-20 on [[ethereum|Ethereum]] (`0x6033...ae3f`) and bridging it onto the Lisk L2 — a rare full architectural pivot from a bespoke L1 to an Ethereum rollup.
- **Emerging-markets focus:** post-migration, Lisk repositioned around Web3 adoption in emerging markets, launching builder/grant programs and seed-liquidity initiatives.
- **2026 small-cap drawdown:** amid the broad altcoin washout, LSK weakened; as of 2026-06-22 it is **-7.02% over 7 days** and **-1.14% on the day** in an Extreme-Fear market (BTC ~$64,166).

> *Notable events and news will continue to be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[layer-1]]
- [[layer-2]]
- [[optimism]]
- [[optimistic-rollup]]
- [[superchain]]
- [[sequencer]]
- [[data-availability]]
- [[base]]
- [[aurora-near]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-22 via cryptodataapi.com / CoinGecko; BTC ~$64,166, Fear & Greed 21 / Extreme Fear.
- General market knowledge; no additional specific wiki source ingested yet for architecture/history claims.
