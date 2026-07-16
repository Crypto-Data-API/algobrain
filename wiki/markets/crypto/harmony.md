---
title: "Harmony"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [altcoins, crypto]
aliases: ["Harmony ONE", "Harmony Protocol", "ONE"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://harmony.one/"
related: ["[[consensus-mechanism]]", "[[cross-chain-bridge]]", "[[crypto-markets]]", "[[ethereum]]", "[[icon]]", "[[iotex]]", "[[layer-1]]", "[[proof-of-stake]]", "[[smart-contracts]]", "[[staking]]"]
---

# Harmony

**Harmony** (ONE) is the native protocol token of the Harmony blockchain, a sharded, EVM-compatible [[layer-1|layer-1]] using a [[proof-of-stake]] [[consensus-mechanism]] called **Effective Proof of Stake (EPoS)**. Harmony's design goal is high throughput and low fees via state sharding (the network splits transaction processing across multiple shards) while remaining compatible with Ethereum tooling. ONE pays gas, secures the chain through [[staking]], and confers governance rights. It ranks **#797** by market capitalization. The chain is best known beyond its technology for the **June 2022 Horizon [[cross-chain-bridge]] hack (~$100M)**, detailed below.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).* ONE trades at **$0.00142649**, market cap **$21,170,979** (rank **#797**), down **-2.09%** over 24h and down **-7.48%** over 7 days, in a broad bear-market regime (BTC bear market; Fear & Greed Index 21 / Extreme Fear).

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | ONE |
| **Market Cap Rank** | #797 |
| **Market Cap** | $21,170,979 |
| **Current Price** | $0.00142649 |
| **24h Change** | -2.09% |
| **7d Change** | -7.48% |
| **Categories** | Smart Contract Platform, Layer 1 (L1), Sharded Blockchain, Harmony Ecosystem, Binance Launchpad |
| **Website** | [https://harmony.one/](https://harmony.one/) |
> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

---

## Overview

Harmony is an open, decentralized [[layer-1]] network whose native token, ONE, incentivizes and rewards developers, validators/stakers, and community members who develop, secure, and govern the chain. Users pay transaction (gas) fees in ONE, and the token is bonded to validators to participate in consensus and earn block rewards. Harmony aligns the incentives of stakeholders so they can build open marketplaces of fungible and non-fungible tokens, with EVM compatibility making it straightforward to port Ethereum dApps and tooling.

---

## Architecture & Consensus

- **Sharded layer-1:** Harmony divides the network into multiple shards (historically four, including a beacon shard) that process transactions in parallel. The **beacon shard** coordinates consensus, manages staking/validator registration, and supplies a verifiable random function (VRF) plus a verifiable delay function (VDF) used to assign validators to shards unpredictably, which reduces the risk of an attacker concentrating malicious stake in a single shard. The goal is to scale throughput horizontally while keeping fees very low.
- **Effective Proof of Stake (EPoS):** a [[proof-of-stake]] [[consensus-mechanism]] variant designed to spread stake across many validators. EPoS adjusts rewards so that **over-staked validators earn proportionally less**, nudging delegators toward smaller validators and discouraging the stake concentration that pure DPoS tends to produce. Validators are **slashed** for double-signing, and unresponsive validators can be removed from the elected set. Block production within shards uses a Fast BFT (FBFT) process for quick finality.
- **EVM compatibility:** Harmony runs an Ethereum-compatible virtual machine, so Solidity [[smart-contracts]] and standard wallets/tooling (MetaMask, Hardhat, etc.) work with minimal changes — a deliberate choice to inherit the EVM developer pool, in contrast to non-EVM peers like [[radix]], [[casper-network]], and [[icon]].
- **Cross-shard transactions:** value can move between shards, with the beacon shard helping coordinate; cross-shard composability is more complex than single-shard execution, a general trade-off of sharded designs.
- **Fast finality and low fees** are the chain's primary marketing claims (historically "2-second finality, sub-cent fees"); concrete throughput figures vary by source and are not asserted as audited here.

---

## Comparison vs Peer Layer-1s

| Network | Consensus | Sharded | EVM-compatible | Distinctive feature |
|---|---|---|---|---|
| **Harmony** ([[harmony]]) | Effective PoS (FBFT) | Yes (beacon + shards) | Yes | Low-fee sharded EVM; Horizon bridge hack (2022) |
| [[ethereum]] | PoS (Gasper) | No (rollup-centric scaling) | Yes (native) | Deepest liquidity; scales via [[layer-2]] |
| [[iotex]] | Roll-DPoS | No | Yes | DePIN / real-world devices |
| [[icon]] | Delegated PoS (P-Reps) | No | Partial | Cross-chain messaging (xCall) |
| [[radix]] | Cerberus (sharded BFT PoS) | Yes | No | Asset-oriented DeFi safety |
| [[casper-network]] | PoS → Zug (BFT) | No (single shard) | No | Enterprise / RWA |

Harmony's bet was that a **sharded, EVM-compatible** chain could offer high throughput at very low fees while still letting Solidity developers port apps directly — combining Ethereum's tooling with horizontal scaling. The strategy was undermined less by its technology than by the 2022 Horizon [[cross-chain-bridge]] exploit and the subsequent loss of confidence, liquidity, and developers.

---

## What the ONE Token Does

- **Gas:** transaction, contract-execution, and storage fees are denominated in ONE.
- **Staking:** ONE is delegated/bonded to validators under EPoS to secure the chain and earn rewards (with slashing risk). EPoS's reward curve specifically penalizes over-staked validators to push delegation toward smaller operators.
- **Governance:** ONE is used to vote on protocol governance, including the contentious post-hack reimbursement proposals (see Notable History).

---

## Governance

Harmony governance combines **on-chain validator/staking participation** with off-chain community processes (forum proposals, community votes) and significant direction from the founding team and **Harmony Foundation** (the project was founded by Stephen Tse and launched via a Binance Launchpad sale in 2019). The most consequential governance episode was the **post-Horizon-hack reimbursement debate** in mid-2022: the team floated proposals to compensate affected users by minting large quantities of new ONE, which the community largely rejected over the heavy inflation/dilution it implied. That standoff — recovery options that were either inflationary or inadequate — illustrated how a major exploit can capture and paralyze a chain's governance. As with all delegated systems, effective governance power tracks staked-ONE concentration among validators.

---

## Ecosystem & Adoption

At its 2021 peak, Harmony hosted a sizable EVM DeFi ecosystem — DEXes, lending, yield, and bridged assets flowing through the **Horizon bridge** — and ran ecosystem-growth and grant programs to attract builders. The June 2022 Horizon hack was an inflection point: it drained bridged liquidity, shattered user confidence, and was followed by sharp contraction in TVL, active developers, and dApps. Subsequent ecosystem activity has been a fraction of the peak, and Harmony competes in a crowded field of EVM [[layer-1]]s and [[ethereum]] [[layer-2]] rollups for the same liquidity and builders. Current ecosystem metrics should be verified on-chain rather than inferred from historical highs.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 14.87B ONE |
| **Total Supply** | 14.87B ONE |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $31.74M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.3790 (2021-10-26) |
| **Current vs ATH** | -99.44% |
| **All-Time Low** | $0.00127355 (2020-03-13) |
| **Current vs ATL** | +67.88% |
| **24h Change** | -3.98% |
| **7d Change** | -0.25% |
| **30d Change** | -10.83% |
| **1y Change** | -76.64% |

---

## Platform & Chain Information

**Native Chain:** Own blockchain (Layer 1)

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | ONE/USDT | N/A |
| Bitget | ONE/USDT | N/A |
| KuCoin | ONE/USDT | N/A |
| Crypto.com Exchange | ONE/USD | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://harmony.one/](https://harmony.one/) |
| **Twitter** | [@harmonyprotocol](https://twitter.com/harmonyprotocol) |
| **Reddit** | [https://www.reddit.com/r/harmony_one/](https://www.reddit.com/r/harmony_one/) |
| **Telegram** | [harmony_one](https://t.me/harmony_one) (12,373 members) |
| **GitHub** | [https://github.com/harmony-one/harmony](https://github.com/harmony-one/harmony) |
| **Whitepaper** | [https://harmony.one/whitepaper](https://harmony.one/whitepaper) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 1,453 |
| **GitHub Forks** | 287 |
| **Pull Requests Merged** | 3,061 |
| **Contributors** | 82 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $2.40M (2026-04-09 snapshot) |
| **Market Cap Rank** | #797 |
| **Price (2026-06-22)** | $0.00142649 |
| **24h Change (2026-06-22)** | -2.09% |
| **7d Change (2026-06-22)** | -7.48% |
| **24h Range (2026-04-09 snapshot)** | $0.00213436 — $0.00225911 |
| **CoinGecko Sentiment** | 100% positive |
| **Last Updated** | 2026-06-22 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Notable History & Major Events

- **2019 — Launch via Binance Launchpad.** Harmony, founded by Stephen Tse (a former engineer at Google, Apple, and Microsoft), raised funds through a Binance Launchpad IEO in 2019 and launched its sharded, EVM-compatible mainnet, positioning around scalability and low fees.
- **October 2021 — All-time high.** ONE peaked at **$0.379** on 2021-10-26 during the bull market, buoyed by its DeFi ecosystem and ecosystem-incentive programs; it has since declined more than 99%, compounded by the 2022 bridge hack and the broader bear market.
- **June 2022 — Horizon bridge hack (~$100M):** Harmony's **Horizon** [[cross-chain-bridge]] connecting Harmony to Ethereum (and BNB Chain) was exploited on/around 23 June 2022, with attackers draining roughly **$100 million** in assets. The breach was attributed to **compromise of the bridge's multisig signing keys** — the bridge required only **2 of 5** signatures to move funds, so compromising two keys was enough to authorize withdrawals: a single-point-of-failure design flaw and a textbook custodial-bridge weakness. On-chain analysis (Elliptic and others) and later U.S. government attribution (FBI) linked the theft to the North Korea-affiliated **Lazarus Group**, which laundered the proceeds through **Tornado Cash** and other mixers. Harmony proposed reimbursing affected users by **minting new ONE** — a plan that would have been heavily inflationary and was largely rejected by the community; alternative recovery proposals also stalled. The incident severely and durably damaged confidence, TVL, and ONE's price. It is a canonical example of [[cross-chain-bridge]] risk: bridges have repeatedly been among the largest single sources of crypto losses (Ronin, Wormhole, Nomad, Poly Network, and Harmony together account for billions in stolen funds), almost always via key/validator-set compromise rather than the underlying chains' own cryptography.
- **Post-hack period (2022–onward).** The bridge exploit and the failed reimbursement governance triggered developer and liquidity attrition; Harmony's relevance among EVM [[layer-1]]s declined sharply, and the chain has since traded as a thin small-cap.
- **March 2020 — All-time low.** ONE printed an all-time low near **$0.00127355** on 2020-03-13 during the COVID crash; current prices sit above that level (+68%) but far below the 2021 peak.

> *Notable events will continue to be added through the wiki's source ingestion workflow.*

---

## Risks

- **Bridge / smart-contract risk:** the 2022 Horizon exploit demonstrated concrete custodial and key-management weaknesses (a 2-of-5 multisig single point of failure); [[cross-chain-bridge]] security remains a structural concern for any cross-chain ecosystem, and the reputational scar persists.
- **Reputational overhang:** a ~$100M hack attributed to a state-linked actor (Lazarus) is a lasting credibility weight that deters institutional and developer adoption.
- **Inflation from reimbursement / staking:** ONE has an **uncapped supply**, and the minting-based recovery proposals raised acute dilution concerns; ongoing staking emissions also dilute non-stakers.
- **Ecosystem and developer attrition:** post-hack, TVL and developer activity contracted sharply; the chain competes with many other EVM [[layer-1]]s and [[ethereum]] [[layer-2]] rollups for scarce liquidity and builders.
- **Governance paralysis risk:** the inability to agree on a hack-recovery path showed how a crisis can deadlock governance, leaving affected users without remedy.
- **Small-cap liquidity & drawdown:** at ~$21M market cap (rank #797) and down >99% from ATH amid an Extreme Fear regime, ONE is highly volatile and thinly traded.

---

## See Also

- [[crypto-markets]]
- [[layer-1]]
- [[layer-2]]
- [[proof-of-stake]]
- [[consensus-mechanism]]
- [[smart-contracts]]
- [[staking]]
- [[cross-chain-bridge]]
- [[ethereum]]
- [[icon]]
- [[iotex]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko; BTC bear regime, Fear & Greed Index 21 / Extreme Fear).
- General market knowledge; no additional specific wiki source ingested yet.

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---
