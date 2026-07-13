---
title: "ICON"
type: entity
created: 2026-04-09
updated: 2026-06-22
status: excellent
tags: [crypto, altcoins]
aliases: ["ICX"]
entity_type: protocol
founded: 2017
headquarters: "Decentralized"
website: "https://icon.community/"
related: ["[[crypto-markets]]", "[[layer-1]]", "[[interoperability]]", "[[proof-of-stake]]", "[[smart-contracts]]", "[[staking]]", "[[cross-chain-bridge]]", "[[consensus-mechanism]]", "[[harmony]]", "[[casper-network]]"]
---

# ICON

**ICON** (ICX) is an [[interoperability]]-focused [[layer-1]] blockchain that launched in 2017 and has historically been strongly associated with the South Korean crypto market. Its central thesis is cross-chain communication: ICON markets a "Cross-Chain Framework" built around **xCall**, a general message-passing primitive that lets applications send messages and value between connected blockchains. As of 2026-06-22 ICX trades at **$0.02805153**, ranked **#636** by market capitalization (mcap **$30,775,525**), down **1.23%** on the day and down **3.47%** over the trailing week in an overall crypto bear regime (BTC bear market; Fear & Greed Index 21 / Extreme Fear).

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | ICX |
| **Market Cap Rank** | #636 |
| **Market Cap** | $30,775,525 |
| **Current Price** | $0.02805153 |
| **24h Change** | -1.23% |
| **7d Change** | -3.47% |
| **Genesis Date** | 2017-09-19 |
| **Categories** | Smart Contract Platform, Cross-chain Communication, Pantera Capital Portfolio, Governance |
| **Website** | [https://icon.community/](https://icon.community/) |
> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

---

## Overview

Founded in 2017, ICON has spent many years building an [[layer-1]] ecosystem oriented toward cross-chain development infrastructure. Its core product is the **ICON Cross-Chain Framework**, which combines the ICON L1 blockchain with **xCall** general message passing and a growing list of connected blockchains and integrated bridging protocols. The goal is to let applications operate across chains — for example, calling a contract on one chain from another — without each developer having to integrate bridges from scratch. (See [[interoperability]].)

The native **ICX** coin fuels this design: it is the L1 [[smart-contracts|gas]] token, the fee token for xCall cross-chain messages, and the asset used for [[staking]] and governance. A portion of collected fees is burned, giving ICX a deflationary fee-sink alongside its staking issuance.

ICON has long been one of the more recognizable Korea-linked crypto projects; its early "hyperconnect the world" framing targeted bridging Korean institutions, and the project retains a notable presence on Korean exchanges such as Upbit.

---

## Architecture & Consensus

ICON runs a delegated [[proof-of-stake]]-style [[consensus-mechanism]]. Network security and block production are handled by elected **P-Reps (Public Representatives)**: token holders [[staking|stake]] and delegate ICX to candidate validators, and the top-ranked P-Reps validate transactions and earn rewards, which they share with their delegators. This design concentrates block production among a bounded set of validators in exchange for throughput and governance efficiency — a common trade-off among DPoS-style L1s.

The **ICON Cross-Chain Framework / xCall** is the project's main differentiator. Rather than building a single monolithic [[cross-chain-bridge]], ICON exposes a standard message-passing interface that can sit on top of multiple underlying bridge / messaging protocols, so a dApp written once can interact with several connected chains. The framework historically grew out of ICON's earlier **Blockchain Transmission Protocol (BTP)**, a light-client-based [[interoperability]] design that aimed to relay verified state between chains rather than trusting an external custodian.

ICON's [[smart-contracts]] use a framework called **SCORE (Smart Contract on Reliable Environment)**, originally Python-based and run on the **goloop** node implementation. This gives ICON a non-EVM execution environment, though the cross-chain framework lets ICON-based logic reach EVM and non-EVM chains alike through xCall.

### xCall and the trust model of cross-chain messaging

A central question for any [[cross-chain-bridge]] or messaging layer is *who is trusted to confirm that an event happened on the source chain*. Designs range from light-client / on-chain verification (more trust-minimized, more expensive) to external multisig committees or oracle networks (cheaper, but a custodial single point of failure — the design that has produced crypto's largest hacks, including the [[harmony]] Horizon exploit). xCall abstracts over multiple underlying "connections," so its security inherits the assumptions of whichever transport a given route uses; users and developers should understand which transport secures a specific message path rather than assuming uniform safety.

---

## Comparison vs Peer Interoperability / Layer-1s

ICON competes both as a general [[layer-1]] and as an [[interoperability]] layer. The table contrasts its approach with major messaging/bridging designs and with the EVM L1s it connects to. Throughput and adoption figures are qualitative; messaging-layer comparisons focus on trust model.

| Network / Protocol | Type | Core mechanism | Trust model | Notes |
|---|---|---|---|---|
| **ICON** ([[icon]]) | L1 + messaging | xCall over BTP / multiple connections | Varies by transport (light-client to committee) | Korea-linked L1; SCORE smart contracts |
| Cosmos IBC | Native interchain standard | Light-client packet relay | Trust-minimized (light clients) | Standard for the Cosmos app-chain ecosystem |
| LayerZero | Omnichain messaging | Oracle + relayer separation | Configurable security stack | Widely integrated cross-EVM |
| Wormhole / Axelar | Cross-chain messaging | Guardian / validator set attestation | External committee | High integration, committee trust |
| [[harmony]] (Horizon) | EVM L1 + bridge | Multisig-secured bridge | Multisig committee (exploited 2022) | Cautionary [[cross-chain-bridge]] failure |

ICON's bet is that owning both an [[layer-1]] and a chain-agnostic messaging standard is more defensible than competing purely on messaging, where well-funded, deeply integrated rivals (LayerZero, Wormhole, Axelar, Cosmos IBC, Polkadot XCM) dominate developer mindshare.

---

## Governance

ICON uses **on-chain governance** anchored by its **P-Rep** system. The top-ranked Public Representatives (elected via delegated [[staking]]) not only validate blocks but also vote on network proposals, parameter changes, and treasury/funding decisions through the **Contribution Proposal System (CPS)**, which funds ecosystem work from network reserves. ICX holders influence outcomes indirectly by choosing which P-Reps to delegate to, so governance power tracks delegated-stake concentration. As with other delegated systems, a bounded validator set improves coordination speed but raises questions about how decentralized effective control really is. The ICON community and the entities historically behind it (the ICON Foundation / ICONLOOP, a Korea-based enterprise blockchain firm) have shaped roadmap direction over the project's life.

---

## Ecosystem & Adoption

ICON's on-chain ecosystem includes DeFi (DEXes and lending such as Balanced and Omm), NFT, and governance applications, with cross-chain reach as the recurring selling point. ICON has long been one of the more recognizable Korea-linked projects, with deep listing support on Korean venues such as Upbit and a history of enterprise-blockchain work in Korea through ICONLOOP (including government and identity pilots). The project is well past its 2018 bull-market peak (ICX reached ~$13 in January 2018, versus roughly $0.028 today, a drawdown of over 99%), and its current activity and developer mindshare are modest relative to the leading interoperability ecosystems such as Cosmos IBC, LayerZero, and Polkadot. Adoption and integration claims should be read as project positioning unless independently verifiable on-chain.

---

## Notable History

- **2017 — ICO and launch.** ICON raised funds in a prominent 2017 token sale (one of the larger Korean ICOs of that era) under the "hyperconnect the world" banner, with backing that has included Pantera Capital. The mainnet genesis date is **2017-09-19**.
- **January 2018 — All-time high.** ICX peaked near **$13.16** on 2018-01-09 at the top of the 2017–2018 bull market, before a multi-year decline exceeding 99%.
- **BTP → xCall evolution.** ICON re-architected its interoperability stack from the earlier light-client-oriented **Blockchain Transmission Protocol (BTP)** into the broader **xCall** Cross-Chain Framework, repositioning from a standalone L1 toward a chain-agnostic messaging layer.
- **March 2026 — All-time low.** ICX printed an all-time low around **$0.0326** on 2026-03-29 during the small-cap [[crypto-markets]] drawdown.

---

## Risks

- **Crowded interoperability sector** — xCall competes with well-funded, widely integrated messaging layers (LayerZero, Wormhole, Axelar, IBC); standing out is difficult.
- **Validator concentration** — a bounded P-Rep set and delegated staking concentrate block production and governance influence.
- **Bridge / cross-chain risk** — cross-chain messaging and bridging is historically one of crypto's most exploited surfaces (see the [[harmony]] Horizon and many other multi-hundred-million-dollar [[cross-chain-bridge]] hacks); xCall's security inherits the assumptions of whichever transport secures a given route.
- **Non-EVM execution** — SCORE/goloop is not EVM-native, so ICON cannot trivially absorb the large pool of Solidity developers and tooling, even though xCall lets it reach EVM chains.
- **Geographic / regulatory concentration** — heavy reliance on the Korean market and Korean exchange liquidity exposes ICX to Korea-specific regulatory and listing risk.
- **Low liquidity & long decay** — ICX sits near rank #636 with a ~$31M market cap and is down ~99% from its all-time high, implying thin liquidity and weak price momentum.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 1.10B ICX |
| **Total Supply** | 1.11B ICX |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $40.26M |
| **Market Cap / FDV Ratio** | 0.99 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $13.16 (2018-01-09) |
| **Current vs ATH** | -99.72% |
| **All-Time Low** | $0.0326 (2026-03-29) |
| **Current vs ATL** | +11.45% |
| **24h Change** | -2.39% |
| **7d Change** | +2.40% |
| **30d Change** | +4.96% |
| **1y Change** | -51.70% |

---

## Platform & Chain Information

**Native Chain:** Own blockchain (Layer 1)

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | ICX/USDT | N/A |
| Kraken | ICX/USD | N/A |
| Upbit | ICX/KRW | N/A |
| Bitget | ICX/USDT | N/A |
| KuCoin | ICX/USDT | N/A |
| Crypto.com Exchange | ICX/USD | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://icon.community/](https://icon.community/) |
| **Twitter** | [@helloiconworld](https://twitter.com/helloiconworld) |
| **Reddit** | [https://www.reddit.com/r/helloicon](https://www.reddit.com/r/helloicon) |
| **Telegram** | [iconblockchain](https://t.me/iconblockchain) (318 members) |
| **Discord** | [https://discord.com/invite/b5QvCXJjJM](https://discord.com/invite/b5QvCXJjJM) |
| **GitHub** | [https://github.com/icon-project/goloop](https://github.com/icon-project/goloop) |
| **Whitepaper** | [https://icon.community/assets/btp-litepaper.pdf](https://icon.community/assets/btp-litepaper.pdf) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 75 |
| **GitHub Forks** | 44 |
| **Pull Requests Merged** | 71 |
| **Contributors** | 11 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $1.03M (2026-04-09 snapshot) |
| **Market Cap Rank** | #636 |
| **Price (2026-06-22)** | $0.02805153 |
| **24h Change (2026-06-22)** | -1.23% |
| **7d Change (2026-06-22)** | -3.47% |
| **Last Updated** | 2026-06-22 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]
- [[layer-1]]
- [[interoperability]]
- [[cross-chain-bridge]]
- [[proof-of-stake]]
- [[consensus-mechanism]]
- [[smart-contracts]]
- [[staking]]
- [[harmony]]
- [[casper-network]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]]) — market data snapshot
- General market knowledge; no other specific wiki source ingested yet. Market figures dated 2026-06-22 are from cryptodataapi.com / CoinGecko (BTC bear regime; Fear & Greed Index 21 / Extreme Fear).
