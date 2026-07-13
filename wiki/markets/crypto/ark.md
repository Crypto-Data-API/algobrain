---
title: "ARK"
type: entity
created: 2026-04-09
updated: 2026-06-23
status: excellent
tags: [crypto, altcoins, interoperability]
aliases: ["ARK", "Ark Ecosystem"]
entity_type: protocol
founded: 2017
headquarters: "Decentralized"
website: "https://ark.io/"
related: ["[[crypto-markets]]", "[[layer-1]]", "[[delegated-proof-of-stake]]", "[[interoperability]]", "[[smart-contracts]]"]
---

# ARK

**ARK** is an interoperability-focused [[layer-1|Layer-1]] blockchain whose design goal is to let many independent chains link together through a "SmartBridge" mechanism, forming an ecosystem of interconnected blockchains. It runs on a [[delegated-proof-of-stake|Delegated Proof-of-Stake (DPoS)]] consensus with a fixed set of elected forging delegates, and ships developer tooling (the ARK Deployer / Core framework) intended to let teams spin up customizable "bridgechains." The ARK token is the native asset used for transaction fees, delegate voting, and staking-style participation. As of 2026-06-21 ARK trades at **$0.115524**, ranked **#759** with a market cap of **$22,796,901**; it is **+1.55%** over 24h and **-4.68%** over 7 days.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | ARK |
| **Market Cap Rank** | #759 |
| **Market Cap** | $22,796,901 |
| **Current Price** | $0.115524 |
| **24h Change** | +1.55% |
| **7d Change** | -4.68% |
| **Consensus** | [[delegated-proof-of-stake|Delegated Proof-of-Stake (DPoS)]] — 51 active delegates |
| **Categories** | [[layer-1|Layer 1 (L1)]], [[interoperability|Interoperability]] |
| **Website** | [https://ark.io/](https://ark.io/) |

---

## Overview

ARK is a [[layer-1|Layer-1]] blockchain built around the idea of **interoperability**: rather than being a single monolithic chain, ARK is designed as a hub for an ecosystem of linked, independently deployable chains ("bridgechains"). Its **SmartBridge** technology is the cross-chain messaging concept that allows these chains — and, in principle, external networks — to communicate and trigger actions between one another. ARK also provides desktop and mobile wallets that connect to network peers without downloading the full chain, and developer tooling aimed at making it easy to launch a new chain from the ARK Core framework.

ARK launched in 2017 by a distributed team. Its architecture draws on lineage from earlier projects such as Lisk, Crypti, and BitShares; CTO **François-Xavier Thoorens** had previously contributed to Lisk. Over time the project repositioned around developer experience and chain-deployment tooling rather than competing head-on as a general smart-contract platform.

---

## Architecture — How It Works

ARK's design philosophy is the inverse of the monolithic-L1 thesis. Instead of forcing every application onto a single shared chain, ARK promotes a **"network of networks"**: many purpose-built chains, each tuned for its own use case, that can interoperate. Three pieces make this possible.

**1. ARK Core (the framework).** ARK Core is the modular node software that runs the main ARK chain and, crucially, can be forked and reconfigured to launch an independent **bridgechain**. A team can change the token name, supply schedule, block time, delegate count, and transaction types, then deploy a fully functional [[delegated-proof-of-stake|DPoS]] chain without writing a blockchain from scratch. The historical **ARK Deployer** tooling automated much of this scaffolding. This positions ARK closer to an *app-chain SDK* (conceptually similar to what the [[cosmos|Cosmos]] SDK does for IBC chains) than to a general smart-contract VM.

**2. SmartBridge.** SmartBridge is ARK's interoperability layer. Every ARK transaction carries an optional **vendor field** that can hold arbitrary data; SmartBridge uses this to encode cross-chain instructions, so a transaction on one ARK-based chain can trigger an action on another (or, with an "encoded listener," on an external network). It is a lightweight messaging convention rather than a trust-minimised proof system — closer in spirit to a notarised message bus than to a zk- or light-client [[cross-chain-bridge|bridge]]. That keeps it simple and cheap but means cross-chain security leans on the honesty of the connected delegate sets rather than cryptographic verification.

**3. Consensus — DPoS with 51 delegates.** Instead of energy-intensive mining, the network is secured by **delegates**: ARK holders continuously vote, and the top **51** vote-weighted delegates become the active block-producing ("forging") set. Each holder votes for a single delegate, with voting power proportional to ARK held, and delegates typically share block rewards back to their voters. Blocks are produced in deterministic round-robin order on a fixed ~8-second cadence, giving fast, predictable finality at the cost of a smaller, semi-permissioned validator set — a recognised [[delegated-proof-of-stake|DPoS]] trade-off shared with relatives like Lisk and BitShares.

The combination — a forkable Core, a 51-delegate DPoS chain, and SmartBridge messaging — defines ARK's niche: *make it easy to spin up your own chain and wire it into a wider ecosystem.* The weakness is that the modular-app-chain narrative was later captured far more completely by [[cosmos|Cosmos]] (IBC), Polkadot (parachains), and Avalanche subnets, which built much larger developer ecosystems.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 195.74M ARK |
| **Total Supply** | 195.74M ARK |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $32.89M |
| **Market Cap / FDV Ratio** | 1.00 |

ARK uses an **inflationary, uncapped** supply: new ARK is minted as block rewards and paid to forging delegates (who redistribute to voters), so there is no hard cap. In practice nearly all supply is already circulating (**MC/FDV ≈ 1.00**), which is unusual and valuable for a small cap — it means there is **no large locked-team or unlock overhang** waiting to hit the market, unlike the steep dilution profiles on [[stronghold-token|SHX]], [[audiera|BEAT]], or [[chain-2|XCN]]. The trade-off is a steady low background emission rather than a one-off cliff.

### Value Accrual & Governance

- **Fees** — ARK pays transaction fees in the native token; the network has experimented with dynamic and near-zero fee models.
- **Staking-via-voting** — holders earn a share of block rewards by voting for a delegate that shares its rewards. Voting power is proportional to balance, so ARK is the unit of both security and governance.
- **Governance** — the elected 51-delegate set effectively governs protocol direction; whoever controls the most vote-weight controls block production. This concentrates influence and is ARK's core decentralisation trade-off.
- **Demand driver** — ultimately ARK's value rests on demand to *launch and operate bridgechains* and on SmartBridge usage; without that throughput, the token is a low-utility infrastructure relic from the 2017 cycle.

---

## Competitor Comparison

ARK competes in the app-chain / interoperability niche, where it was an early mover but has been heavily out-scaled.

| Project | Token | Model | Interop mechanism | Relative scale |
|---|---|---|---|---|
| **ARK** | ARK | Forkable DPoS app-chain framework (51 delegates) | SmartBridge (vendor-field messaging) | Micro-cap (~$23M), legacy 2017 cohort |
| [[cosmos\|Cosmos]] | ATOM | App-chain SDK + Tendermint | IBC (light-client trust-minimised) | Large ecosystem, hundreds of chains |
| Polkadot | DOT | Shared-security parachains | XCM + relay chain | Large, pooled-security model |
| Lisk | LSK | Sidechain/app-chain SDK (DPoS sibling) | Inter-chain bridging | Small/mid cap, shared lineage |
| Avalanche | AVAX | Subnets / custom chains | Cross-subnet + Warp | Large, strong DeFi traction |

ARK's edge is simplicity and a long uptime record; its disadvantage is that every larger rival offers a richer developer ecosystem, more trust-minimised interop, and deeper liquidity. SmartBridge's notarised-message approach is also less secure than IBC-style light-client verification.

---

## How & Where It Trades

- **Spot (CEX):** ARK is listed on Binance (ARK/USDT), Upbit (ARK/KRW — Korea is historically a strong ARK market), Bitget, and Crypto.com. Korean Won pairs can be a meaningful share of volume.
- **DEX / derivatives:** A perpetual market exists on [[hyperliquid|Hyperliquid]] (ARK-PERP), giving some ability to short or hedge — rare for a token this size — though perp liquidity is thin and funding can be erratic.
- **Liquidity read:** ~$0.95M of 24h volume against a ~$23M cap (~4% turnover) is tradeable but thin; the order book is shallow and large market orders will move price. There is **no unlock overhang** to worry about (MC/FDV ≈ 1.0), so price action is driven by flow and broad sentiment rather than supply cliffs.

---

## Narrative, Category & Catalysts

ARK's narrative is **legacy interoperability / app-chain infrastructure**. It predates the modular and L2 era and reads today more as a long-lived survivor than a frontier project. Potential catalysts are mostly idiosyncratic: a renewed Core/SmartBridge release, a notable bridgechain deployment, a tier-1 exchange relisting or volume surge from a Korean-market spike, or a broad "old-coin rotation" in which 2017-cycle infrastructure tokens catch a bid. Absent fresh developer traction, ARK trades primarily as a high-beta proxy for small-cap altcoin sentiment.

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $10.22 (2018-01-10) |
| **Current vs ATH** | ~-98.9% |
| **All-Time Low** | $0.0339 (2017-03-22) |
| **24h Change** | +1.55% |
| **7d Change** | -4.68% |

> ARK sits roughly 99% below its January-2018 peak, a typical profile for a 2017-cycle infrastructure token that never recaptured prior highs. With a market-cap-to-FDV ratio near 1.0, nearly all supply is circulating. The -4.68% week aligns with the broad **Extreme Fear** backdrop (Fear & Greed 22, [[btc-bitcoin|BTC]] ~$64,180 on 2026-06-21).

---

## Platform & Chain Information

**Native Chain:** Own [[layer-1|Layer-1]] blockchain ([[delegated-proof-of-stake|DPoS]], 51 delegates)

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | ARK/USDT | N/A |
| Upbit | ARK/KRW | N/A |
| Bitget | ARK/USDT | N/A |
| Crypto.com Exchange | ARK/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| [[hyperliquid|Hyperliquid]] | ARK-PERP | Perpetual |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://ark.io/](https://ark.io/) |
| **Twitter** | [@ArkEcosystem](https://twitter.com/ArkEcosystem) |
| **Reddit** | [https://www.reddit.com/r/ArkEcosystem](https://www.reddit.com/r/ArkEcosystem) |
| **Telegram** | [arkannouncements](https://t.me/arkannouncements) (1,552 members) |
| **Discord** | [https://discord.gg/arkcoin](https://discord.gg/arkcoin) |
| **GitHub** | [https://github.com/ArkEcosystem/core](https://github.com/ArkEcosystem/core) |
| **Whitepaper** | [https://arkscic.com/whitepaper.pdf](https://arkscic.com/whitepaper.pdf) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 346 |
| **GitHub Forks** | 279 |
| **Pull Requests Merged** | 3,403 |
| **Contributors** | 49 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $946,701.00 |
| **Market Cap Rank** | #743 |
| **24h Range** | $0.1674 — $0.1715 |
| **Last Updated** | 2026-04-09 |

---

## Distinguishing Features

- **SmartBridge interoperability** — ARK's signature concept for linking independent chains and triggering cross-chain actions.
- **Bridgechain tooling** — frameworks (ARK Core / Deployer) aimed at letting developers launch customizable chains quickly.
- **DPoS with 51 delegates** — fast, deterministic block production secured by a fixed elected validator set (see [[delegated-proof-of-stake]]).
- **Cross-platform wallets** — desktop and mobile wallets that connect to peers without a full-node download.

## Risks

**Technology & decentralisation**
- **Validator centralization** — a 51-delegate set is a relatively small, semi-permissioned validator group; vote-weight can concentrate, a recognized [[delegated-proof-of-stake|DPoS]] decentralization trade-off.
- **Weak interop security** — SmartBridge is a notarised-message convention, not a trust-minimised light-client bridge; cross-chain security leans on delegate honesty.

**Adoption & competition**
- **Competitive pressure** — the [[interoperability|interoperability]] niche is now dominated by [[cosmos|Cosmos]] (IBC), Polkadot, and Avalanche subnets with far larger ecosystems and trust-minimised messaging.
- **Adoption / relevance** — ARK predates the modern modular and L2 era and has limited DeFi/dapp traction relative to newer L1s; the bridgechain thesis never achieved scale.

**Market & liquidity**
- **Liquidity / small-cap risk** — ~$23M market cap (rank ~#759) implies thin liquidity and high volatility, especially under the current Extreme-Fear regime.
- **Deep, durable drawdown** — ~99% below its Jan-2018 ATH with no recovery to prior highs; a typical "dead-cycle" infrastructure-token profile.
- **Inflation drip** — uncapped supply means a continuous low-level emission to delegates, a mild structural headwind.

> *This page is informational, not investment advice. Small-cap crypto assets are highly volatile and can lose most of their value rapidly.*

---

## Trading Playbook (bear / Extreme-Fear, bottoming regime)

*Context: 2026-06-23 macro is Extreme Fear (F&G 21), market-health 29/100 bearish, long-horizon regime "bottoming / accumulation." ARK is a thin micro-cap with no fresh catalyst.*

- **Default stance: avoid / underweight.** In Extreme Fear, illiquid 2017-cycle micro-caps like ARK bleed against [[btc-bitcoin|BTC]] and gap on low volume. There is no edge in holding a low-utility infrastructure relic through a bear without a specific catalyst.
- **If accumulating the bottoming thesis:** size tiny, scale in, and treat it as a high-beta altcoin-sentiment proxy rather than a fundamentals bet. The clean MC/FDV ≈ 1.0 (no unlock cliff) is a genuine structural positive versus heavily-locked peers like [[stronghold-token|SHX]] or [[audiera|BEAT]].
- **Catalyst triggers to watch:** a Core/SmartBridge release, a real bridgechain launch, a Korean-market (Upbit) volume spike, or a broad old-coin rotation. Without one, expect drift.
- **Risk controls:** assume meaningful slippage on size; the [[hyperliquid|Hyperliquid]] ARK-PERP allows a hedge/short but with thin liquidity and noisy funding. Hard-size limits and a sentiment-based stop (e.g., exit if BTC breaks the bottoming range) are prudent.

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## History / Timeline

*Dated events below are drawn from public market data and project history; undated milestones are omitted to avoid fabrication.*

- **2017** — ARK launches after a 2016 crowdsale; team draws on lineage from Lisk, Crypti, and BitShares (CTO François-Xavier Thoorens previously contributed to Lisk).
- **2017-03-22** — Recorded all-time low of **$0.0339**.
- **2018-01-10** — All-time high of **$10.22**, near the top of the 2017–18 bull cycle.
- **2018 onward** — Project repositions around developer experience and chain-deployment tooling (ARK Core / Deployer, SmartBridge); never recaptures prior highs.
- **2026-06-21** — Trades at **$0.115524** (~99% below ATH), rank ~#759, amid an Extreme-Fear, bottoming-regime backdrop.

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]
- [[layer-1]]
- [[delegated-proof-of-stake]]
- [[interoperability]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- General market knowledge; no additional specific wiki source ingested yet.
