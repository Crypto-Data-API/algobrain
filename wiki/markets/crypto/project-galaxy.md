---
title: "Galxe (GAL)"
type: entity
created: 2026-04-09
updated: 2026-06-22
status: excellent
tags: [crypto, altcoins, web3]
aliases: ["GAL", "Galxe", "Project Galaxy", "Gravity", "G"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://galxe.com/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[decentralized-identity]]", "[[web3]]", "[[layer-1]]"]
---

# Galxe (GAL)

**Galxe** (GAL) is a Web3 credential, identity, and community-growth network, originally launched as **Project Galaxy** before rebranding to Galxe in 2022. The platform lets projects design on-chain campaigns, quests, and credential-based rewards, and lets users build a portable on-chain reputation via **Galxe ID** and Galxe Passport. **GAL** is the network's utility and governance token; Galxe has subsequently built its own [[layer-1]] chain, **Gravity**, with a native token **G** to which GAL holders can migrate.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

As of 2026-06-22, GAL trades at **$0.263092**, ranked **#603** by market capitalization with a market cap of roughly **$33.51M**. The token is up **+0.45%** over 24 hours but down **-6.28%** over the trailing 7 days, broadly in line with a risk-off market backdrop (Bitcoin near $64,508; Crypto Fear & Greed Index at 21, "Extreme Fear").

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | GAL |
| **Market Cap Rank** | #603 |
| **Market Cap** | $33.51M |
| **Current Price** | $0.263092 |
| **24h Change** | +0.45% |
| **7d Change** | -6.28% |
| **Categories** | SocialFi, [[decentralized-identity\|Decentralized Identifier (DID)]], Quest-to-Earn, [[web3]] Infrastructure, BNB Chain Ecosystem, Ethereum Ecosystem, Zero Knowledge (ZK) |
| **Website** | [https://galxe.com/](https://galxe.com/) |
> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

---

## Overview

Galxe (formerly **Project Galaxy**, rebranded to **Galxe** in 2022) is a [[web3]] community-growth and credential network. Its core product lets projects launch **campaigns and quests** — on-chain and off-chain tasks (token swaps, governance votes, social actions, app usage) — that issue verifiable **Galxe credentials** and reward participants with NFTs, allowlist spots, or tokens. These credentials accumulate into a portable [[decentralized-identity|on-chain identity]] via **Galxe ID** and the **Galxe Passport**, letting users carry reputation and proof-of-personhood across applications.

The platform positions itself as a Web3 user-acquisition and engagement layer, used by many projects to bootstrap and retain communities. Galxe operates across multiple chains, with credentials and campaigns spanning [[ethereum]], BNB Chain, and other ecosystems.

### Architecture — How the credential network works

Galxe is best understood as a **credential data network plus a campaign/distribution layer** sitting on top of it:

**1. Credential issuance and the data layer.** Galxe maintains a large repository of **on-chain and off-chain credentials** — verifiable records that an address (or person) performed some action: held a token, voted in a DAO, swapped on a DEX, used a dApp, or completed an off-chain social task. On-chain credentials are computed from blockchain data (anyone can curate a query that classifies addresses); off-chain credentials come from integrations (Twitter, Discord, Snapshot, etc.) and oracle-style attestations. These credentials are the raw material the rest of the system consumes.

**2. Campaigns and quests (the application layer).** Projects assemble credentials into **campaigns** — a quest is essentially a boolean over credentials ("hold X *and* voted in Y → eligible"). Participants who satisfy the conditions claim rewards: NFTs (often issued as the proof-of-completion), allowlist/whitelist spots, points, or tokens. This is the **"quest-to-earn"** loop that drives most platform activity.

**3. Galxe ID, Passport, and proof-of-personhood.** Completed credentials accumulate into a portable [[decentralized-identity|on-chain identity]] — **Galxe ID** — and **Galxe Passport** adds a KYC-style proof-of-personhood/[[sybil-resistance|Sybil-resistance]] layer so projects can target real users rather than airdrop farmers. Some credential verification uses [[zk-snark|zero-knowledge]] techniques so users can prove eligibility without exposing all underlying data.

**4. Sybil resistance.** Because incentive campaigns attract farmers running thousands of wallets, Galxe layers Sybil-detection (analysis of address clustering / farming patterns) and Passport personhood checks to keep distributions targeting genuine participants — an ongoing arms race rather than a solved problem.

### Token role and the Gravity migration

**GAL** is the network's native utility and governance token. Within the Galxe ecosystem it has been used to:

- Pay platform/campaign fees when projects create credential campaigns
- Participate in governance over the protocol and treasury
- Stake to access certain features and rewards

To pursue greater scalability, Galxe built its own [[layer-1]] blockchain, **Gravity**, with a native token **G**. GAL holders can migrate GAL to G; **G** serves as the gas token of Gravity, secures the network through [[staking]], and underpins governance and payments across the broader Galxe ecosystem. (The GAL ticker remains actively traded during the migration period — see official migration docs at https://help.galxe.com/en/articles/9576881-how-to-migrate-gal-to-g.)

### Competitive position

Galxe competes in the Web3 "growth and credentials" space alongside platforms such as Layer3, QuestN, and zkPass-style attestation providers, and overlaps conceptually with broader [[decentralized-identity]] efforts. Its differentiation is scale of campaign distribution and the breadth of integrated chains and projects; its dependence on incentive-driven "quest-to-earn" activity is also a key risk (see Risks).

#### Comparison vs competitors

| Platform | Core model | Identity layer | Token | Differentiator |
|---|---|---|---|---|
| **Galxe** (GAL→G) | Credential data network + quests | Galxe ID / Passport (proof-of-personhood) | GAL / G | Largest campaign distribution; own L1 (Gravity); broad chain coverage |
| **Layer3** | Quest / engagement platform | XP + reputation | L3 | Heavy gamified quest UX, points economy |
| **QuestN** (formerly Quest3) | Quest / task campaigns | Task completion records | — | Lightweight campaign tooling, SMB-focused |
| **zkPass** | ZK attestation of private web data | ZK proofs of off-chain data | — | Privacy-preserving credential primitive (not a full quest hub) |

Galxe's edge is **distribution scale and an integrated identity stack**; the trade-off is that much of its measured activity is incentive-driven and Sybil-prone (see Risks).

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 127.75M GAL |
| **Total Supply** | 200.00M GAL |
| **Max Supply** | 200.00M GAL |
| **Fully Diluted Valuation** | $65.88M |
| **Market Cap / FDV Ratio** | 0.64 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $18.32 (2022-05-06) |
| **Current vs ATH** | -98.20% |
| **All-Time Low** | $0.0742 (2026-01-28) |
| **Current vs ATL** | +344.10% |
| **24h Change** | +0.45% |
| **7d Change** | -6.28% |
| **1y Change** | -66.86% |

The token remains roughly **98% below** its 2022 all-time high of ~$18.32, reflecting the broad de-rating of "GameFi/SocialFi growth platform" tokens since the 2021–22 cycle.

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x5faa989af96af85384b8a938c2ede4a7378d9875` |
| Binance Smart Chain | `0xe4cc45bb5dbda06db6183e8bf016569f40497aa5` |

---

## Exchange Listings

> *No major exchange listings found in CoinGecko data.*

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://galxe.com/](https://galxe.com/) |
| **Twitter** | [@Galxe](https://twitter.com/Galxe) |
| **Telegram** | [Galxe](https://t.me/Galxe) (187,070 members) |
| **Discord** | [https://discord.com/invite/galxe](https://discord.com/invite/galxe) |
| **Whitepaper** | [https://docs.galxe.com/](https://docs.galxe.com/) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $4.81 |
| **Market Cap Rank** | #577 |
| **24h Range** | $0.3281 — $0.3372 |
| **Last Updated** | 2026-04-09 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## How & Where It Trades

GAL is a multi-chain ERC-20, deployed on [[ethereum]] (`0x5faa...9875`) and BNB Chain (`0xe4cc...7aa5`). The token is liquid enough to have been listed across major venues historically, though the CoinGecko snapshot for this entry shows limited venue data and very thin recorded 24h volume — partly an artifact of the **GAL→G migration** redistributing liquidity toward the new G token. Practical notes:

- **Migration fragmentation** — liquidity and price discovery are split between GAL and G during the migration window; traders must confirm which ticker a venue actually settles.
- **Multi-chain** — GAL exists on both Ethereum and BNB Chain; bridge/contract confusion is a real execution risk on a microcap.
- **Spot-only for most** — no deep, durable derivatives market at this cap; treat as a spot position.

---

## Major News & Events

- **2022 — Rebrand:** Project Galaxy rebranded to **Galxe**.
- **All-time high $18.32** on **2022-05-06** (CoinGecko price history).
- **All-time low $0.0742** on **2026-01-28**.
- **Gravity L1 launch & GAL→G migration:** Galxe introduced its own [[layer-1]] chain (Gravity) with token **G**, and opened migration for GAL holders (see official migration docs).

> *Additional notable events will be added through the wiki's source ingestion workflow. Undocumented dates are intentionally omitted rather than invented; the dates above are from CoinGecko price history and Galxe's own migration documentation.*

---

## Risks

- **Token migration overhang:** The GAL→G migration creates uncertainty around the long-term role and liquidity of the GAL ticker; holders must track migration mechanics and deadlines.
- **Incentive-dependence:** Galxe's activity is heavily driven by reward campaigns ("quest-to-earn"). Sybil/airdrop-farming behavior can inflate engagement metrics, and activity can fall sharply when incentives dry up.
- **Sector de-rating:** Down ~98% from its 2022 ATH; SocialFi/growth-platform tokens have been structurally weak.
- **Competition:** A crowded field (Layer3, QuestN, attestation providers) and the broader [[decentralized-identity]] race.
- **Liquidity & market risk:** Small-cap (#603, ~$33.5M) and sensitive to the risk-off regime (Fear & Greed 21 as of 2026-06-22). Position sizing and slippage matter — see [[risk-management]].

> *Not investment advice. Figures are point-in-time and crypto markets are highly volatile.*

---

## Trading Playbook (bear / Extreme-Fear regime)

- **Regime:** Established Bear Market, Extreme Fear (F&G 21, 2026-06-22). SocialFi/growth-platform tokens have been structurally de-rated (~98% off ATH); this is a capital-preservation regime, not a chase.
- **Migration first:** before trading, confirm GAL vs G mechanics and which ticker your venue settles — the migration is the dominant idiosyncratic factor and the largest avoidable execution error.
- **Fundamental signal:** real, *non-incentivized* campaign usage and Galxe ID/Passport adoption matter more than quest-farming volume; discount engagement spikes that coincide with reward campaigns.
- **Risk control:** size for microcap volatility and migration/liquidity-fragmentation risk; pre-define invalidation. See [[risk-management]].

> *Not investment advice.*

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[decentralized-identity]]
- [[web3]]
- [[layer-1]]
- [[sybil-resistance]]
- [[risk-management]]
- [[staking]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko). General market knowledge; no additional specific wiki source ingested yet.
