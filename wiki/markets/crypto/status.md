---
title: "Status"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [altcoins, crypto, ethereum]
aliases: ["SNT", "Status Network"]
entity_type: protocol
founded: 2017
headquarters: "Decentralized"
website: "https://status.im/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[layer-1]]", "[[smart-contracts]]", "[[socialfi]]"]
---

# Status

**Status** (SNT) is an open-source mobile client for the [[ethereum|Ethereum]] network that bundles a private peer-to-peer messenger, a non-custodial crypto wallet, and a Web3 dapp browser into a single mobile application. The SNT token is an ERC-20 utility token used inside the Status ecosystem for features such as username registration (ENS-style names), push notifications, sticker purchases, and community/governance functions. As of 2026-06-21 SNT trades at **$0.00733287**, ranked **#654** by market capitalization with a market cap of **$29,041,821**; it is **+1.76%** over 24h and **-1.88%** over 7 days.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | SNT |
| **Market Cap Rank** | #654 |
| **Market Cap** | $29,041,821 |
| **Current Price** | $0.00733287 |
| **24h Change** | +1.76% |
| **7d Change** | -1.88% |
| **Genesis Date** | 2017-06-19 |
| **Token Standard** | ERC-20 (on [[ethereum|Ethereum]]) |
| **Categories** | Infrastructure, [[socialfi|SocialFi]], Ethereum Ecosystem, Messaging, Wallet |
| **Website** | [https://status.im/](https://status.im/) |

---

## Overview

Status is a mobile client that aims to make the [[ethereum|Ethereum]] network usable directly from a smartphone. It combines three core products: an end-to-end encrypted, peer-to-peer **private messenger** (historically built on the Whisper / Waku messaging protocols rather than centralized servers), a **non-custodial wallet** for holding ETH and ERC-20 assets, and a **Web3 dapp browser** for interacting with [[smart-contracts|smart contracts]] and decentralized applications. The goal is to lower the barrier to Ethereum adoption for everyday mobile users.

Status is developed by the broader Status organization, which also funds infrastructure projects such as the Waku messaging network, the Nimbus Ethereum client, and the Keycard hardware wallet. The first public presentation of the concept came in September 2016 at DevCon2, the annual Ethereum developer conference, where co-founders **Carl Bennetts** and **Jarrad Hope** revealed plans for an Ethereum light client.

In more recent development, the Status organization launched **Status Network**, an Ethereum [[layer-2|Layer-2]] rollup positioned as a "gasless" L2 for community and consumer applications, extending the SNT ecosystem beyond the original mobile client. The Status Network L2 is built using the **Linea** zk-rollup stack (a Consensys/zkEVM technology) and aims to sponsor user gas so that SNT, not ETH, anchors the network's economic loop. SNT plays a role in the network's incentive, staking, and fee-sponsorship mechanisms. Treat the precise L2 design and SNT sink mechanics as evolving — verify against current Status Network documentation.

SNT historically traded on major venues including Binance, Upbit, KuCoin, and Bitget, and is liquid on Ethereum decentralized exchanges such as [[uniswap|Uniswap]] V2/V3.

---

## Architecture: How Status Works (deep dive)

Status is best understood as a **stack of independently valuable infrastructure** wrapped in a consumer app, funded by one organization:

- **Status mobile/desktop client** — the consumer-facing app bundling messenger + non-custodial wallet + dapp browser. Keys are generated and held on-device; there is no custodial server holding funds.
- **Waku (formerly Whisper)** — the **decentralized messaging protocol** that routes messages peer-to-peer with metadata protection, rather than through centralized chat servers. Waku is a generalized messaging layer used by Status and made available to other Web3 apps. This is arguably Status's most reused piece of infrastructure.
- **Nimbus** — a lightweight, resource-efficient **Ethereum consensus/execution client** designed to run on consumer hardware (including phones and embedded devices), contributing to Ethereum's client diversity and decentralization.
- **Keycard** — a **hardware wallet** in a smartcard/NFC form factor for secure key storage and signing.
- **Status Network (L2)** — the newer **Linea-based gasless Layer-2** targeting community and consumer apps, where SNT is positioned as the economic asset (sponsored gas, staking, incentives).
- **ENS-style usernames** — SNT is burned/locked to register human-readable Status usernames (a naming demand sink).

The organization is structured as a network of project teams (Status, Waku, Nimbus, Logos/Codex research) coordinated around the broader thesis of a decentralized, censorship-resistant communication and application stack.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 3.96B SNT |
| **Total Supply** | 6.80B SNT |
| **Max Supply** | Unlimited |
| **Market Cap / FDV Ratio** | ~0.58 |

SNT is an ERC-20 [[utility-token|utility token]] originally distributed via a 2017 token sale. It does not secure the Ethereum chain (Ethereum [[proof-of-stake|proof-of-stake]] is secured by staked ETH) — instead SNT is consumed and used *within* Status's applications for naming, stickers, push-notification deposits, community curation, and governance-style signalling.

### Value accrual & governance

- **Demand sinks (legacy app):** ENS-style username registration, sticker market purchases, push-notification deposits (spam-prevention bonds), and "tribute to talk" anti-spam deposits — all narrow, low-volume sinks historically.
- **New demand sink (Status Network L2):** the gasless L2 thesis is the main attempt to give SNT a *structural* role — as the staking/incentive/fee-sponsorship asset of a consumer-app rollup. Whether this materially increases SNT demand depends entirely on L2 adoption.
- **Governance:** SNT has been used for community signalling and is positioned for governance over network parameters and treasury direction. Treat governance scope as evolving.
- **Core critique:** with an **unlimited max supply** and historically weak coupling between app usage and token demand, SNT's value accrual has been the project's persistent weakness — a free, open-source app does not inherently force token buying.

---

## Comparison vs Web3 Wallet / Messenger Peers

| Dimension | **Status (SNT)** | [[metamask\|MetaMask]] (no public token) | Trust Wallet (TWT) | Session / other P2P messengers |
|---|---|---|---|---|
| **Primary product** | Messenger + wallet + dapp browser + L2 | Wallet + dapp browser (browser-first) | Multi-chain mobile wallet | Private messenger only |
| **Messaging** | Decentralized (Waku, E2E encrypted) | None | None | Decentralized/onion-routed |
| **Custody** | Non-custodial, on-device keys | Non-custodial | Non-custodial | n/a |
| **Token role** | SNT: names, stickers, L2 staking/gas-sponsorship | No token | TWT: discounts/governance | Varies |
| **Differentiator** | Bundled comms + funds Waku/Nimbus/Keycard public goods | Dominant EVM distribution | Binance-affiliated reach | Pure privacy comms |
| **Weakness** | Narrow token sinks; mainstream-messenger competition | No token to value | Centralized affiliation | No wallet/dapp layer |

Status's structural edge is that it bundles **private messaging + non-custodial funds + a dapp browser** and funds genuinely reused infrastructure (Waku, Nimbus). Its structural weakness is competing for wallet mindshare against MetaMask's distribution and for messenger mindshare against entrenched mainstream apps.

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.6849 (2018-01-03) |
| **Current vs ATH** | ~-98.9% |
| **All-Time Low** | $0.00592935 (2020-03-13) |
| **24h Change** | +1.76% |
| **7d Change** | -1.88% |

> Like most 2017-era infrastructure tokens, SNT sits far below its bull-market peak, reflecting both the broad market cycle and the difficulty of monetizing a free, open-source mobile client. The current **Extreme Fear** market backdrop (Fear & Greed Index 22 on 2026-06-21, [[btc-bitcoin|BTC]] ~$64,180) weighs on small-cap altcoin liquidity.

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x744d70fdbe2ba4cf95131626614a1763df805b9e` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Upbit | SNT/KRW | N/A |
| Bitget | SNT/USDT | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0X744D70FDBE2BA4CF95131626614A1763DF805B9E/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |
| Uniswap V2 (Ethereum) | 0X744D70FDBE2BA4CF95131626614A1763DF805B9E/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://status.im/](https://status.im/) |
| **Twitter** | [@ethstatus](https://twitter.com/ethstatus) |
| **Reddit** | [https://www.reddit.com/r/statusim/](https://www.reddit.com/r/statusim/) |
| **GitHub** | [https://github.com/status-im/status-react](https://github.com/status-im/status-react) |
| **Whitepaper** | [https://status.im/whitepaper.pdf](https://status.im/whitepaper.pdf) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 3,867 |
| **GitHub Forks** | 983 |
| **Commits (4 weeks)** | 115 |
| **Pull Requests Merged** | 7,629 |
| **Contributors** | 246 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $1.96M |
| **Market Cap Rank** | #646 |
| **24h Range** | $0.00973326 — $0.0100 |
| **Last Updated** | 2026-04-09 |

---

## Distinguishing Features

- **Mobile-first Ethereum client** — combines messenger, wallet, and dapp browser, unusual for the era when most wallets were single-purpose.
- **Decentralized messaging** — uses the Waku/Whisper family of protocols rather than centralized chat servers, so messages route peer-to-peer.
- **Privacy focus** — non-custodial keys held on-device; end-to-end encryption.
- **Ecosystem funding** — the Status organization bankrolls public-good infrastructure (Waku, Nimbus consensus client, Keycard) beyond the consumer app.
- **Status Network L2** — a newer Ethereum [[layer-2|Layer-2]] rollup pivot targeting gasless consumer apps.

## Risks

- **Monetization** — SNT's in-app utility is narrow (names, stickers, notifications); demand for the token is not strongly tied to messenger usage, a recurring weakness for utility tokens.
- **Adoption** — competes against entrenched mainstream messengers and large custodial wallets (e.g., MetaMask, Coinbase Wallet) for mindshare.
- **Liquidity / small-cap risk** — sub-$30M market cap at rank #654 means thin order books and high volatility, amplified in the current Extreme-Fear regime.
- **Token-vs-network decoupling** — SNT does not secure Ethereum, so its value depends entirely on product-driven demand sinks.

> *This page is informational, not investment advice. Small-cap crypto assets are highly volatile and can lose most of their value rapidly.*

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## How & Where SNT Trades

- **Spot venues:** SNT lists on **Binance**, **Upbit** (SNT/KRW — a historically high-volume Korean-retail pair), **KuCoin**, and **Bitget**. Korean-Won liquidity has periodically driven outsized SNT moves.
- **On-chain / DEX:** SNT is a liquid ERC-20 traded on **Uniswap V2 and V3** against WETH/USDC; on-chain liquidity is reasonable for a token of its size.
- **Liquidity profile:** with ~$2M reported 24h volume against a ~$29M cap (rank ~#654), SNT is a thin small-cap. Spreads widen on size and CEX pairs dominate price discovery.
- **Derivatives:** perp/futures coverage is limited versus large caps; do not assume deep continuous leverage liquidity.

---

## Narrative, Category & Catalysts

- **Category:** Ethereum-ecosystem infrastructure / SocialFi / privacy + Web3 wallet, now with an L2 (Status Network) angle.
- **Bull catalysts:** meaningful **Status Network (Linea-based L2)** adoption that creates real SNT staking/gas-sponsorship demand; a privacy/decentralized-comms narrative revival; Waku/Nimbus adoption translating into ecosystem prestige and SNT demand; ENS-style name adoption.
- **Bear/structural headwinds:** weak token demand coupling, unlimited supply, fierce competition from MetaMask and mainstream messengers, and a multi-cycle pattern of strong tech but weak token monetization.

---

## History / Timeline

- **2016-09:** concept first presented at **DevCon2** by co-founders **Carl Bennetts** and **Jarrad Hope** as an Ethereum light client.
- **2017-06:** SNT token sale / genesis (genesis date 2017-06-19).
- **2018-01-03:** all-time high of **$0.6849** during the prior cycle peak.
- **2019–2022:** mainnet app releases, Waku messaging protocol development, Nimbus Ethereum client and Keycard hardware wallet shipped.
- **2020-03-13:** all-time low around **$0.00593** during the COVID crash.
- **2024–2026:** organization repositioned around **Status Network**, an Ethereum L2 (Linea-based, gasless) aiming to give SNT a structural staking/incentive role.
- **2026-06-21/22:** SNT trades ~$0.0073, ~99% below ATH, in an Extreme-Fear regime.

> Dates reflect widely documented project history and the page's recorded market data; verify specific L2 launch/parameters against primary sources.

---

## Trading Playbook (bear / Extreme-Fear regime)

> Context: F&G = 21 (Extreme Fear), established bear market, [[btc-bitcoin|BTC]] ~$64k. SNT is a thin ERC-20 small-cap with weak token demand sinks.

- **Bias:** capital-preservation. SNT is a "good tech, weak token" infrastructure play with no proven demand sink large enough to anchor value; its bull case hinges on speculative L2 adoption.
- **Longs:** treat as a small asymmetric bet on the Status Network L2 actually creating SNT demand — size for total loss. Prefer accumulation near historical support rather than chasing Upbit-driven spikes.
- **Avoid:** leverage on a thin small-cap; KRW-pair volatility produces violent wicks.
- **Risk controls:** predefine invalidation (e.g., new ATL on rising volume, or L2 traction failing to appear); treat sharp CEX pumps as exit liquidity.
- **Watch:** Status Network L2 TVL/active users and any SNT staking/sink go-live as the key fundamental tell before price.

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[layer-1]]
- [[socialfi]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- General market knowledge; no additional specific wiki source ingested yet.
