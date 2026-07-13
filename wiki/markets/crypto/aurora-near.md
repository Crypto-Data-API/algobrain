---
title: "Aurora"
type: entity
created: 2026-04-09
updated: 2026-06-22
status: excellent
tags: [crypto, ethereum, altcoins]
aliases: ["AURORA"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://aurora.dev/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[near-protocol]]", "[[layer-2]]"]
---

# Aurora

**Aurora** (AURORA) is an **EVM (Ethereum Virtual Machine) that runs as a smart contract on the [[near-protocol|NEAR Protocol]]** — effectively an Ethereum-compatible execution layer hosted on NEAR rather than a standalone chain or a classic [[ethereum|Ethereum]] rollup. It gives developers a turn-key, Ethereum-compatible, high-throughput environment with very low transaction costs, settling within NEAR's sharded consensus. As of 2026-06-22 AURORA trades at **$0.02625635**, ranked **#851** with a market capitalization of **~$18.8M**.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).* AURORA trades at **$0.02625635**, market cap **$18,788,389** (rank **#851**), down **-0.06%** over 24h and down **-0.45%** over 7 days, in a broad risk-off regime (BTC ~$64,166; Fear & Greed Index 21 / Extreme Fear).

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | AURORA |
| **Market Cap Rank** | #851 |
| **Market Cap** | $18,788,389 |
| **Current Price** | $0.02625635 |
| **24h Change** | -0.06% |
| **7d Change** | -0.45% |
| **Architecture** | EVM implemented as a contract on NEAR Protocol (NEAR-EVM); Rainbow Bridge to Ethereum |
| **Categories** | Near Protocol Ecosystem, Ethereum Ecosystem, DWF Labs Portfolio, Dragonfly Capital Portfolio, Pantera Capital Portfolio, Aurora Ecosystem |
| **Website** | [https://aurora.dev/](https://aurora.dev/) |
> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko). BTC reference ~$64,166, Extreme Fear regime.*

---

## Overview

Aurora is an **EVM built on the [[near-protocol|NEAR Protocol]]**. Rather than being an [[ethereum|Ethereum]] [[layer-2|Layer 2]] rollup, Aurora is the **Aurora Engine**: an EVM implemented *as a WASM smart contract deployed on NEAR*, so Ethereum-style transactions execute inside NEAR's sharded ("Nightshade") runtime. This lets Solidity contracts and standard Ethereum tooling (MetaMask, Hardhat, etc.) work unchanged while benefiting from NEAR's throughput and low, predictable fees. Aurora's security and finality derive from NEAR's proof-of-stake consensus, not from Ethereum.

Connectivity to Ethereum and other chains is provided by the **Rainbow Bridge**, a trustless light-client bridge between NEAR/Aurora and Ethereum that lets assets move across. Aurora also offers "Aurora Chains" / Virtual Chains — app-specific EVM chains powered by the same engine.

---

## Architecture & Consensus

### EVM-as-a-contract, not a rollup

The crucial architectural fact about Aurora is that it is **not** an [[ethereum|Ethereum]] [[layer-2|Layer 2]] rollup. There is no fraud proof, no validity proof, and no posting of compressed transaction data back to Ethereum for [[data-availability|data availability]]. Instead:

- The **Aurora Engine** is a WASM smart contract deployed on [[near-protocol|NEAR]]. It implements the full EVM bytecode interpreter and Ethereum state model.
- Ethereum-style transactions are submitted to this contract, executed inside NEAR's runtime, and their results become part of **NEAR's** state.
- **Security, consensus, and finality come from NEAR's "Nightshade" sharded [[proof-of-stake]]** — *not* from Ethereum. An attacker who could compromise NEAR could compromise Aurora; Ethereum's validator set provides no protection here.

Practically, this means Solidity contracts, MetaMask, Hardhat, Foundry, and standard JSON-RPC tooling work unmodified, while users get NEAR's high throughput and low, predictable fees. The trade-off is the **inverted trust model** relative to a rollup: an L2 user can ultimately exit/verify against Ethereum L1; an Aurora user trusts NEAR.

### Gas in ETH, sharding, and Aurora Chains

- **Gas asset:** to mirror Ethereum UX, gas on Aurora is denominated in **ETH** (bridged), not in AURORA or NEAR. AURORA is therefore a governance/incentive token, not the fee unit (see below).
- **Throughput:** Aurora inherits NEAR's sharded ("Nightshade") scaling, giving high capacity and sub-cent fees.
- **Aurora Chains / Virtual Chains:** app-specific EVM chains spun up from the same engine, letting projects run dedicated EVM environments that still settle on NEAR.

### Comparison: ways to get an EVM with Ethereum compatibility

| Approach | Example | Where security comes from | Bridge dependency | Gas asset |
|---|---|---|---|---|
| **EVM-as-contract on another L1** | **Aurora (on [[near-protocol\|NEAR]])** | NEAR PoS (not Ethereum) | Rainbow Bridge to Ethereum | ETH |
| Optimistic rollup | [[optimism\|Optimism]], [[lisk\|Lisk]], Base | Ethereum (fraud proofs + DA) | Canonical rollup bridge | ETH |
| ZK rollup | zkSync, Starknet | Ethereum (validity proofs + DA) | Canonical rollup bridge | ETH |
| Sidechain | Polygon PoS (legacy) | Own validator set | External bridge | Own token |
| Alt-L1 EVM | BNB Chain, Avalanche C-Chain | Own validator set | External bridge | Own token |

Aurora most resembles an **alt-L1 EVM / sidechain in its trust model** (security from another chain's validators), but is unusual in being literally *a contract on* its host L1 and in using ETH for gas — closer to a sidechain than to a true Ethereum rollup such as [[lisk|Lisk]].

---

## Token & What It Does

The **AURORA** token (ERC-20 on Ethereum, bridged to Aurora and NEAR) is the **governance** token of the Aurora ecosystem and the Aurora DAO, used for protocol governance and ecosystem incentives. Gas on the Aurora EVM is paid in ETH (Aurora uses ETH as its gas asset for Ethereum compatibility), so AURORA itself is a governance/incentive token rather than the gas unit. Total / max supply is ~1.0B AURORA with roughly 695M circulating (market-cap-to-FDV ~0.70), a relatively high circulating ratio versus the other tokens here. AURORA is associated with investors including Pantera, Dragonfly, and DWF Labs.

### Governance and value accrual

Aurora is steered by the **Aurora DAO**, where AURORA holders vote on ecosystem direction, grants, treasury allocation, and protocol parameters. The token has also been used in **AuroraDAO/Aurora+ staking** programs that distribute rewards and ecosystem benefits to stakers.

The token's **value-accrual challenge is structural**: because gas is paid in ETH (not AURORA), the network's fee revenue does not directly flow to AURORA the way gas fees accrue to the native token of an L1 or many rollups. AURORA's value therefore rests primarily on **governance rights, ecosystem incentives, and staking utility** rather than a fee-burn or fee-capture mechanism. This is a common weakness for governance-only tokens: usage can grow without the token capturing it unless governance directs revenue or buybacks to holders. Verify the current staking and treasury policy against Aurora's live documentation.

---

## History

Aurora launched in 2021, developed within the [[near-protocol|NEAR]] ecosystem (by Aurora Labs / "Aurora is NEAR"), to offer an Ethereum-compatible environment on NEAR with the Rainbow Bridge for asset movement. Its token-generation event and **Aurora DAO** formation followed, alongside the **Aurora+ / staking** program. It rode the 2021–2022 cycle — its all-time high of **$35.40** dates to **2022-01-16** — and has since fallen more than 99% from that peak. Over time Aurora introduced **Aurora Chains / Virtual Chains** (app-specific EVM chains) to broaden its offering. Because security and activity are inherited from NEAR rather than Ethereum, Aurora's trajectory is tied closely to NEAR ecosystem health and developer adoption. In 2026 AURORA printed an all-time low of **$0.0236** on 2026-02-06 during the small-cap washout before stabilizing.

### Notable events

- **2021:** Aurora launched as an EVM on NEAR with the Rainbow Bridge.
- **2022-01-16:** All-time high of **$35.40**.
- **2026-02-06:** All-time low of **$0.0236** amid the broad altcoin drawdown.
- **2026-06-22:** Trades at **$0.02625635** (rank #851, ~$18.8M cap), roughly flat on the week (**-0.45% 7d**, **-0.06% 24h**) in an Extreme-Fear market (BTC ~$64,166).

---

## Risks

- **Dependence on NEAR** — Aurora's liveness, finality, and security are inherited from [[near-protocol|NEAR Protocol]]; problems with NEAR consensus, validators, or governance flow directly to Aurora.
- **Bridge risk** — the Rainbow Bridge (and any cross-chain pathways) is a major attack surface; light-client bridges are more trust-minimized than multisigs but still carry implementation and liveness risk. Cross-chain bridges are among the most-exploited components in crypto.
- **Not an Ethereum rollup** — Aurora does *not* inherit Ethereum's security; users assuming "L2 = Ethereum security" are mistaken, since settlement is on NEAR. Its trust model is closer to a sidechain/alt-L1 (see comparison table) than to true rollups like [[lisk|Lisk]] or [[optimism|Optimism]].
- **Weak token value accrual** — gas is paid in ETH, so network usage does not directly accrue to AURORA; the token relies on governance/incentive demand, which can decouple from real activity.
- **Ecosystem concentration** — being tightly coupled to one L1 ecosystem concentrates competitive and liquidity risk; AURORA competes with NEAR's own native dApps and with the broader EVM-L2 landscape for developers.
- **Token decay & liquidity** — AURORA is down ~99%+ from its 2022 ATH (~$18.8M cap, rank #851) with thin 24h volume; large orders can move price materially.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 694.99M AURORA |
| **Total Supply** | 999.81M AURORA |
| **Max Supply** | 1.00B AURORA |
| **Fully Diluted Valuation** | $27.65M |
| **Market Cap / FDV Ratio** | 0.70 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $35.40 (2022-01-16) |
| **Current vs ATH** | -99.92% |
| **All-Time Low** | $0.0236 (2026-02-06) |
| **Current vs ATL** | +11.25% |
| **24h Change** | -0.06% |
| **7d Change** | -0.45% |
| **30d Change** | -7.95% |
| **1y Change** | -57.06% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xaaaaaa20d9e0e2461697782ef11675f668207961` |
| Aurora | `0x8bec47865ade3b172a928df8f990bc7f2a3b9f79` |
| Near Protocol | `aaaaaa20d9e0e2461697782ef11675f668207961.factory.bridge.near` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| KuCoin | AURORA/USDT | N/A |
| Crypto.com Exchange | AURORA/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V2 (Ethereum) | 0XAAAAAA20D9E0E2461697782EF11675F668207961/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://aurora.dev/](https://aurora.dev/) |
| **Twitter** | [@auroraisnear](https://twitter.com/auroraisnear) |
| **Telegram** | [auroraisnear](https://t.me/auroraisnear) (12,032 members) |
| **Discord** | [https://discord.gg/dEFJBz8HQV](https://discord.gg/dEFJBz8HQV) |
| **GitHub** | [https://github.com/aurora-is-near/aurora-engine](https://github.com/aurora-is-near/aurora-engine) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 360 |
| **GitHub Forks** | 100 |
| **Commits (4 weeks)** | 17 |
| **Pull Requests Merged** | 750 |
| **Contributors** | 37 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $551,852.00 |
| **Market Cap Rank** | #842 |
| **24h Range** | $0.0275 — $0.0278 |
| **Last Updated** | 2026-04-09 |

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
- [[near-protocol]]
- [[layer-2]]
- [[proof-of-stake]]
- [[smart-contracts]]
- [[optimism]]
- [[lisk]]
- [[data-availability]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-22 via cryptodataapi.com / CoinGecko; BTC ~$64,166, Fear & Greed 21 / Extreme Fear.
- General market knowledge; no additional specific wiki source ingested yet for architecture/history claims.
