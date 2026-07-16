---
title: "Across Protocol"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, ethereum]
aliases: ["ACX"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://across.to/"
related: ["[[cross-chain-bridge]]", "[[crypto-markets]]", "[[ethereum]]", "[[smart-contract-risk]]", "[[uma]]"]
---

# Across Protocol

**Across Protocol** (ACX) is an intents-based, optimistic [[cross-chain-bridge]] for moving assets between [[ethereum]] and major L2s/EVM chains. Instead of locking funds and minting wrapped tokens on the destination chain, Across uses professional **relayers** who front the user's funds on the destination chain almost instantly, then get reimbursed from a single shared liquidity pool. Correct reimbursement is verified by [[uma|UMA's]] optimistic oracle. The result is fast, low-slippage transfers with capital concentrated in one pool rather than fragmented per route.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

As of 2026-06-22, ACX trades at **$0.04150835**, ranked **#651** by market capitalization with a market cap of **~$29,196,527** (24h -0.38%, 7d -2.75%). The token is roughly 97% below its 2024 all-time high, in line with the broader bear regime (BTC ~$64,390; Fear & Greed Index 21 — "Extreme Fear").

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | ACX |
| **Market Cap Rank** | #651 |
| **Market Cap** | ~$29,196,527 |
| **Current Price** | $0.04150835 |
| **24h / 7d Change** | -0.38% / -2.75% |
| **Categories** | Polygon Ecosystem, Arbitrum Ecosystem, Ethereum Ecosystem, Optimism Ecosystem, Bridge Governance Tokens, Cross-chain Communication, Intent, Boba Network Ecosystem, Blockchain Capital Portfolio, Made in USA |
| **Website** | [https://across.to/](https://across.to/) |
> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

---

## Overview

Across is an optimistic [[cross-chain-bridge]] optimized for capital efficiency: a single shared liquidity pool, a competitive relayer market, and a fee model designed to avoid slippage. It is one of the original "intents-based" bridges — the user expresses *what they want* (asset X on chain B) and competing relayers fulfil it, rather than the user interacting with per-chain lock/mint contracts. Across was incubated by Risk Labs, the team behind [[uma]], whose optimistic oracle underpins Across's settlement security.

---

## How Across Works

**The intents + optimistic settlement flow:**

1. **Deposit & intent** — A user deposits funds into the Across SpokePool on the origin chain, specifying the destination chain, output asset, and a maximum fee.
2. **Relayer fills instantly** — A competitive set of **relayers** (market makers) watch for deposits and front the user's funds on the destination chain from their own inventory, usually within seconds. The user never waits for a slow canonical bridge.
3. **Settlement via the HubPool** — Relayers are periodically reimbursed (plus a fee) from Across's central **HubPool** liquidity, into which LPs deposit and earn yield.
4. **Optimistic verification** — Reimbursement claims are validated by [[uma|UMA's]] optimistic oracle: relayer-submitted "root bundles" are assumed valid unless a watcher disputes them within a challenge window. Disputers post a bond; fraudulent or incorrect bundles are slashed. This optimistic model avoids per-message multisig trust but introduces a settlement delay and depends on at least one honest, economically motivated watcher.

**Trust model:** Across is a *liquidity/relayer* bridge with **optimistic-oracle** settlement, not a token-burning lock-and-mint bridge. The destination user receives canonical/native assets from relayer inventory — no new wrapped token is minted for the user — so the bridge's risk centers on (a) the correctness of the optimistic settlement and (b) the security of the pooled LP funds, rather than wrapped-asset depegs.

**What the ACX token does:**

- **Governance** — ACX governs the protocol via the Across DAO: fee parameters, supported routes/chains, treasury, and the optimistic-oracle risk parameters.
- **Incentives** — ACX has been used to reward liquidity providers and relayers and to bootstrap usage.

**How LP yield is generated:** HubPool liquidity providers earn the bridge fees paid by users (and historically ACX incentives). Fees scale with bridging volume; this is genuine usage-based revenue, though competitive pressure among bridges compresses margins.

---

## Architecture Deep Dive

Across is built around a hub-and-spoke contract topology layered on top of [[uma|UMA's]] optimistic oracle. Understanding the moving parts clarifies where trust and capital actually sit:

- **SpokePool contracts** — One deployed on each supported chain. Users deposit here, relayers fill here, and refunds settle here. Spokes hold only transient liquidity; the canonical reserve lives in the HubPool on [[ethereum]].
- **HubPool (Ethereum)** — The single, canonical liquidity pool and accounting hub. Liquidity providers deposit into the HubPool; relayer reimbursements are netted and paid from it. Concentrating reserves in one pool is what gives Across its capital efficiency — but also means a single contract holds the protocol's at-risk LP funds (see Risks).
- **Relayers** — Permissionless, capital-providing market makers who race to fill deposits from their own inventory. They are reimbursed (principal + fee) once a "root bundle" describing the batch of fills is accepted. Relayers absorb the inventory and finality risk in exchange for fees; the user experiences a near-instant fill.
- **Root bundles + UMA optimistic oracle** — A "dataworker" periodically proposes a root bundle summarising which relayers should be reimbursed and how the HubPool should rebalance across spokes. The proposal is posted to [[uma|UMA's]] Optimistic Oracle with a bond; anyone can dispute within a challenge window. If undisputed, it executes; if disputed, UMA's dispute resolution arbitrates and a fraudulent proposer is slashed. This optimistic, dispute-based design replaces the multisig/validator trust used by most other [[cross-chain-bridge|bridges]].
- **Bundle finality delay** — Because settlement is optimistic, relayer reimbursement (not the user fill) waits out the challenge window. Users do not feel this delay; relayers price it into their fees.

**Intents and the broader trend.** Across is one of the canonical examples of the **intents** paradigm now spreading across DeFi (also seen in CoW Protocol, UniswapX, and 1inch Fusion): the user signs *what outcome they want*, and a competitive solver/relayer market figures out *how*. Across' "Across+" and cross-chain action features extend this so a bridge can be bundled with a destination-chain action (swap, deposit, mint) in a single intent.

---

## Comparison vs Competing Bridges

| Dimension | **Across** | [[stargate-finance\|Stargate]] | [[chainflip\|Chainflip]] | Hop / Connext (intents) | Canonical / native bridges |
|---|---|---|---|---|---|
| Trust model | Optimistic ([[uma\|UMA]] oracle) + relayers | [[layerzero\|LayerZero]] DVN messaging | TSS validator vaults | Optimistic / messaging | Rollup security / multisig |
| Liquidity model | **Single shared HubPool** | Unified per-asset pools | JIT market-maker quotes | Per-route AMMs | None (lock/mint) |
| User receives | Native/canonical asset | Native asset | Native asset | Native or hToken | Canonical wrapped/native |
| Speed (user) | Seconds (relayer fill) | Seconds (guaranteed finality) | Minutes (source confirmations) | Seconds–minutes | Minutes–hours (or days for OP withdrawals) |
| Non-EVM support | EVM-focused | Broad (LayerZero chains) | **BTC, SOL + EVM natively** | EVM-focused | Chain-specific |
| Settlement style | Intents / optimistic | Messaging + pooled | Native swap | Intents | Direct |
| Key trust assumption | ≥1 honest disputer in window | Honest DVN set | Honest validator supermajority | Router/relayer honesty | Underlying chain security |

Across' differentiator is capital efficiency (one pool, not per-route fragmentation) and the fact that it avoids minting user-facing wrapped assets, removing depeg risk for the end user. Its trade-off is reliance on the optimistic-dispute game and concentration of LP capital in the HubPool.

---

## Governance & Value Accrual

- **Across DAO** — Governed by ACX holders and an elected set of contributors. The DAO controls fee parameters, which chains/routes are supported, treasury spending, and — critically — the optimistic-oracle risk parameters (bond sizes, challenge windows, identifier choices) that define how secure settlement is.
- **ACX value accrual** — Historically ACX has functioned primarily as a governance and incentive token rather than a hard fee-capture asset; bridge fees accrue first to LPs and relayers. Proposals around directing a share of protocol revenue toward the token/treasury are an ongoing governance theme common to bridge-governance tokens. Investors should treat ACX's value as a claim on governance and future fee-direction decisions, not a guaranteed cash-flow stream.
- **Incentive history** — ACX has been used for liquidity mining (rewarding HubPool LPs), relayer incentives, and a 2022 retroactive airdrop tied to early bridge usage and locked-up referral rewards.

---

## Notable History

- **Incubated by Risk Labs** — Across was launched by Risk Labs, the team behind [[uma]], deliberately reusing UMA's optimistic oracle as the bridge's settlement layer rather than building a fresh validator set.
- **2022 — ACX launch & airdrop** — The ACX token launched in November 2022 with a community airdrop and a locked-up bonding/referral program that distributed tokens to early bridgers.
- **Intents pivot** — Across re-architected around the intents model and a unified, optimistic settlement flow, positioning itself among the leading "fast bridges" for L2 traffic and consistently ranking among the highest-volume bridges by transfer count on EVM rollups.
- **Across+ / cross-chain actions** — Extended the protocol from pure asset transfer to bridge-plus-action intents, letting integrators offer one-click cross-chain deposits and swaps.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 704.32M ACX |
| **Total Supply** | 1.00B ACX |
| **Max Supply** | 1.00B ACX |
| **Fully Diluted Valuation** | $43.54M |
| **Market Cap / FDV Ratio** | 0.70 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.69 (2024-12-06) |
| **Current vs ATH** | -97.42% |
| **All-Time Low** | $0.0312 (2026-02-28) |
| **Current vs ATL** | +39.42% |
| **24h Change** | -2.69% |
| **7d Change** | +1.25% |
| **30d Change** | +30.94% |
| **1y Change** | -75.71% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x44108f0223a3c3028f5fe7aec7f9bb2e66bef82f` |
| Boba | `0x96821b258955587069f680729cd77369c0892b40` |
| Polygon Pos | `0xf328b73b6c685831f238c30a23fc19140cb4d8fc` |
| Arbitrum One | `0x53691596d1bce8cea565b84d4915e69e03d9c99d` |
| Optimistic Ethereum | `0xff733b2a3557a7ed6697007ab5d11b79fdd1b76b` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | ACX/USDT | N/A |
| Kraken | ACX/USD | N/A |
| Bitget | ACX/USDT | N/A |
| KuCoin | ACX/USDT | N/A |
| Crypto.com Exchange | ACX/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0X44108F0223A3C3028F5FE7AEC7F9BB2E66BEF82F/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |
| Balancer V2 | 0X44108F0223A3C3028F5FE7AEC7F9BB2E66BEF82F/0X7F39C581F595B53C5CB19BD0B3F8DA6C935E2CA0 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://across.to/](https://across.to/) |
| **Twitter** | [@AcrossProtocol](https://twitter.com/AcrossProtocol) |
| **Discord** | [https://discord.across.to/](https://discord.across.to/) |
| **GitHub** | [https://github.com/across-protocol](https://github.com/across-protocol) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $4.17M |
| **Market Cap Rank** | #641 |
| **24h Range** | $0.0429 — $0.0448 |
| **Last Updated** | 2026-04-09 |

---

## Risks

Cross-chain bridges are one of the single largest sources of loss in crypto — multiple eight- and nine-figure bridge exploits (e.g., Ronin, Wormhole, Nomad in 2022) define the threat model. Across's specific risk profile:

- **Optimistic-oracle / settlement risk** — Security rests on [[uma|UMA's]] optimistic oracle and the assumption that at least one honest watcher will dispute a fraudulent root bundle within the challenge window. A failure of the dispute/incentive mechanism, or a successful manipulation of the oracle, could allow incorrect reimbursements that drain the HubPool.
- **Pooled-liquidity exposure** — All routes share one HubPool. A [[smart-contract-risk|smart-contract]] bug or governance compromise affecting that pool puts all LP funds at risk at once, rather than isolating losses to a single route.
- **Relayer / liveness risk** — Fast fills depend on a healthy, competitive relayer set. In stressed or extreme-volatility conditions relayers may widen spreads, delay, or stop filling, degrading speed and price.
- **Governance / admin risk** — Like most bridges, upgradeable contracts and DAO/admin controls are a centralization and attack surface; a compromised key or malicious upgrade is a classic bridge failure mode.
- **General [[cross-chain-bridge]] systemic risk** — Bridges aggregate value across chains, making them high-value targets; users should treat any bridge as elevated-risk infrastructure.

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
- [[cross-chain-bridge]]
- [[uma]]
- [[smart-contract-risk]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]]) — historical market-data snapshot
- Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko); Fear & Greed Index 21 (Extreme Fear)
- General market knowledge; no specific narrative wiki source ingested yet for protocol mechanism.
