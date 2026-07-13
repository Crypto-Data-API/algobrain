---
title: "EthereumPoW"
type: entity
created: 2026-04-09
updated: 2026-06-22
status: excellent
tags: [crypto, altcoins, ethereum]
aliases: ["ETHW", "ETHPOW", "EthereumPoW"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://ethereumpow.org/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[proof-of-work]]", "[[the-merge]]"]
---

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

# EthereumPoW

**EthereumPoW** (ETHW, also ETHPOW) is the **[[proof-of-work]] fork of [[ethereum|Ethereum]]** created in September 2022 by miners who opposed Ethereum's transition to [[proof-of-stake]]. When Ethereum completed [[the-merge|The Merge]] on 2022-09-15 and switched its consensus from PoW to PoS, the now-idle GPU/ASIC mining community hard-forked the chain to preserve a mineable, proof-of-work version of Ethereum. ETHW is the native asset of that fork. As of 2026-06-22 ETHW trades at **$0.237534**, ranked **#713** by market capitalization with a market cap of roughly **$25.61M** (24h **-1.81%**, 7d **-2.39%**) — down more than 99% from its launch-week high, reflecting the fork's limited adoption (Fear & Greed 21 / Extreme Fear; BTC ~$64,508).

---

## Origin: The PoW Fork After The Merge

[[the-merge|The Merge]] retired Ethereum's [[proof-of-work]] consensus, eliminating mining rewards and rendering billions of dollars of mining hardware economically obsolete on Ethereum mainnet. A faction of miners and their backers, organized partly around the figure Chandler Guo, executed a hard fork days after The Merge to continue an ETH chain secured by mining. The result is **EthereumPoW (ETHW)**: a separate Layer 1 that inherited Ethereum's pre-Merge state (so holders of ETH at the fork block received an equivalent ETHW balance) but follows its own PoW chain thereafter.

Early ETHW also traded as **IOU / pre-fork futures** on several exchanges before the fork finalized — the original page text reflects that "IOU markets" framing. Today ETHW trades as a live spot asset.

---

## Mechanism & Architecture

- **Consensus** — [[proof-of-work]] (Ethash-style GPU mining), deliberately retaining what Ethereum abandoned at The Merge.
- **EVM compatibility** — as an Ethereum fork it is EVM-compatible and inherited the pre-Merge contract state, so existing tooling and contracts could in principle run on it.
- **Independent Layer 1** — ETHW maintains its own chain, block production, and (unlimited) issuance schedule via mining rewards, separate from Ethereum mainnet.
- **Native asset** — ETHW (circulating ≈ 107.82M, with an **unlimited** max supply since new coins are minted as mining rewards).

---

## The ETHW Token

ETHW is the chain's gas and block-reward asset. Unlike a fixed-supply token, its **max supply is unlimited** — new ETHW is continuously issued to miners as PoW block rewards, which is inflationary and stands in contrast to post-Merge Ethereum's low/sometimes-negative net issuance. The token's roles are the standard L1 set: paying transaction fees (gas), rewarding miners who secure the chain, and serving as the unit of account for any applications deployed on the fork.

### Value accrual (ETHW)

ETHW has **no token-engineered value-capture** beyond base-layer monetary demand:

- **Gas demand** — value rests on people actually transacting on the ETHW chain, which has been minimal versus PoS [[ethereum]] and its L2s.
- **Miner economics** — continuous PoW issuance means miners are persistent natural sellers (they sell rewards to cover electricity/hardware), creating structural sell pressure absent on low-issuance PoS Ethereum.
- **No burn / no staking yield** — unlike post-EIP-1559 PoS Ethereum (fee burn + staking), ETHW offers neither a meaningful burn sink nor staking yield, so there is no mechanism offsetting inflationary issuance.
- There is **no governance token model**; ETHW is purely an L1 gas/reward asset whose price is a speculative bet on the PoW-fork's relevance.

### Comparison vs related PoW chains

| Dimension | EthereumPoW (ETHW) | Ethereum Classic (ETC) | Ethereum (ETH, PoS) | Bitcoin (BTC) |
|---|---|---|---|---|
| **Origin** | 2022 PoW fork after The Merge | 2016 DAO-fork split (PoW retained) | Canonical chain (PoS since 2022) | Original PoW chain |
| **Consensus** | [[proof-of-work]] (Ethash-style) | [[proof-of-work]] (Etchash) | [[proof-of-stake]] | [[proof-of-work]] (SHA-256) |
| **Supply** | Unlimited (mining-issued) | Capped (~210.7M) | Low/variable net issuance, fee burn | Capped 21M |
| **EVM** | Yes (inherited) | Yes | Yes | No |
| **Ecosystem/liquidity** | Minimal | Modest (largest ETH-PoW chain) | Dominant | Dominant store-of-value |
| **Security budget** | Low fork hashrate | Higher than ETHW, still attack-prone historically | Large staked base | Highest PoW hashrate |

ETHW's closest analogue is **Ethereum Classic** — both are PoW chains positioned as "the un-changed Ethereum" — but ETC predates ETHW by six years and has materially more liquidity, miner support, and recognition. ETHW must compete with ETC for the same "Ethereum-but-PoW" mindshare while offering no clear advantage.

---

## Adoption and Security Trade-offs (Honest Assessment)

The PoW-fork thesis — keep Ethereum mineable — has seen **limited adoption**, and ETHW's collapse from a ~$58 launch-week high to under $0.25 reflects that:

- **Weak network effects** — developers, liquidity, stablecoins, and DeFi overwhelmingly stayed on PoS [[ethereum|Ethereum]] (and its L2s). A fork inherits code and state but not the community, liquidity, or application ecosystem.
- **Lower security budget** — a fork's hashrate is only a fraction of what once secured Ethereum, and a much smaller, lower-value chain is comparatively cheaper to attack (51% / reorg risk) than the chain it copied.
- **Oracle / bridge / replay hazards** — forked EVM chains face replay-attack and stale-oracle issues (e.g. price feeds and stablecoins that are only meaningfully backed on the canonical chain), undermining DeFi usability.
- **No clear differentiation** — beyond "PoW instead of PoS," ETHW offers no distinct technical advantage over both Ethereum and other established PoW chains.

In short, ETHW functions mainly as a miner-aligned, ideologically-motivated fork with a small, speculative market rather than a thriving smart-contract ecosystem.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | ETHW |
| **Market Cap Rank** | #713 |
| **Market Cap** | $25,606,900 |
| **Current Price** | $0.237534 |
| **24h Change** | -1.81% |
| **7d Change** | -2.39% |
| **Categories** | Smart Contract Platform, EthereumPoW Ecosystem, Proof of Work (PoW) |
| **Website** | [https://ethereumpow.org/](https://ethereumpow.org/) |

---

## Overview

This page refers to **Ethereum Proof of Work (ETHW or ETHPOW)**, the [[proof-of-work]] fork that split from [[ethereum|Ethereum]] when the original chain migrated to [[proof-of-stake]] at [[the-merge|The Merge]] in September 2022. Initially ETHW traded via IOU / pre-fork futures markets across a number of exchanges before the fork finalized; it now trades as a live spot asset on its own Layer 1 chain.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 107.82M ETHW |
| **Total Supply** | 107.82M ETHW |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $28.24M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $58.54 (2022-09-03) |
| **Current vs ATH** | ~-99.6% |
| **All-Time Low** | $0.2398 (2026-03-29) |
| **24h Change** (2026-06-22) | -1.81% |
| **7d Change** (2026-06-22) | -2.39% |

---

## Platform & Chain Information

**Native Chain:** Own blockchain (Layer 1)

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Bitget | ETHW/USDT | N/A |
| KuCoin | ETHW/USDT | N/A |
| Crypto.com Exchange | ETHW/USD | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://ethereumpow.org/](https://ethereumpow.org/) |
| **Twitter** | [@EthereumPoW](https://twitter.com/EthereumPoW) |
| **Telegram** | [ethereumpow_official](https://t.me/ethereumpow_official) (6,440 members) |
| **Discord** | [https://discord.gg/apcxzJdZaU](https://discord.gg/apcxzJdZaU) |
| **GitHub** | [https://github.com/ethereumpow](https://github.com/ethereumpow) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **Market Cap Rank** | #713 |
| **Market Cap** | $25,606,900 |
| **Price** | $0.237534 |
| **24h Change** | -1.81% |
| **7d Change** | -2.39% |
| **Last Updated** | 2026-06-22 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## History & Timeline

Real, dated events (this fork has a well-documented origin):

- **2022-09-03** — ETHW (trading as IOU / pre-fork futures ahead of the split) prints its all-time high of $58.54 as anticipation peaks.
- **2022-09-15** — [[the-merge|The Merge]] completes: Ethereum mainnet switches consensus from [[proof-of-work]] to [[proof-of-stake]], ending ETH mining and stranding GPU/ASIC mining hardware.
- **Mid-September 2022** — Miners (organized partly around Chandler Guo) execute the **EthereumPoW (ETHW) hard fork** days after The Merge, preserving a mineable, PoW version of Ethereum that inherited pre-Merge state (ETH holders at the fork block received equivalent ETHW). The chain immediately faced replay-attack and stale-oracle issues common to forked EVM chains.
- **2026-03-29** — Recorded all-time low of $0.2398.
- **2026-06-22** — ETHW ~$0.238, rank ~#713, down >99% from the launch-week high — reflecting the fork's limited adoption amid Extreme Fear (F&G 21).

## Narrative, Category & Catalysts

- **Category** — ideological [[proof-of-work]] fork of Ethereum; a miner-aligned "keep Ethereum mineable" play competing with Ethereum Classic for the PoW-Ethereum narrative.
- **Bull catalysts** — renewed PoW ideological/mining interest, a broad altcoin-fork rotation, or exchange/listing events that temporarily lift speculative volume.
- **Bear catalysts** — structural: persistent miner sell pressure (unlimited issuance), weak network effects (developers/liquidity stayed on PoS Ethereum + L2s), low security budget (51%/reorg risk), bridge/oracle/replay hazards, and fork-chain decay over time. Risk-off regimes (current backdrop) compound the bleed.

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Trading Playbook (bear / Extreme-Fear regime)

Context: 2026-06-22, established bear market, Extreme Fear (F&G 21). For a ~$26M-cap fork chain in long-term structural decline (down >99% from ATH):

- **Fade the structural decay** — the dominant force is fork-chain entropy plus continuous miner selling; absent a real catalyst, the path of least resistance is down/sideways. This is not a buy-and-hold thesis.
- **Event-driven only** — any tradeable interest tends to come from short-lived catalysts (listings, PoW-narrative spikes, sympathy moves with ETC). Treat rallies as mean-reversion fades rather than trend changes, and respect that liquidity can vanish fast.
- **Liquidity / venue** — trades on CEXs (Bitget, KuCoin, Crypto.com) but with thin depth for a ~$26M chain; use limit orders and assume [[slippage]] on size.
- **Risk control** — inflationary unlimited supply is a permanent headwind; size for total loss, predefine invalidation, and benchmark vs ETH/ETC rather than USD alone. See [[risk-management]], [[position-sizing]], and the honest-assessment section above.

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[proof-of-work]]
- [[the-merge]]
- [[proof-of-stake]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-22 via cryptodataapi.com / CoinGecko.
- General market knowledge; no specific protocol source ingested yet.
