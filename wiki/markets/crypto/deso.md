---
title: "Decentralized Social"
type: entity
created: 2026-04-09
updated: 2026-06-23
status: excellent
tags: [crypto, altcoins]
aliases: ["DESO", "DeSo", "BitClout"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.deso.com/"
related: ["[[crypto-markets]]", "[[layer-1]]", "[[socialfi]]", "[[proof-of-stake]]"]
---

# Decentralized Social

**Decentralized Social** (DESO, also written **DeSo**) is a [[layer-1|Layer-1]] blockchain purpose-built to store social-media data on-chain — posts, profiles, follows, and likes — so that decentralized social applications can be built on a shared, open social graph rather than the closed databases of Web2 platforms. It evolved from the **BitClout** project and is backed by prominent venture investors (a16z, Sequoia, Coinbase Ventures, Pantera). The DESO token is the native asset used to pay transaction fees, register profiles, and power on-chain "creator coin" markets. As of 2026-06-21 DESO trades at **$2.92**, ranked **#633** with a market cap of **$30,762,507**; it is **-0.65%** over 24h and **-8.37%** over 7 days.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | DESO |
| **Market Cap Rank** | #633 |
| **Market Cap** | $30,762,507 |
| **Current Price** | $2.92 |
| **24h Change** | -0.65% |
| **7d Change** | -8.37% |
| **Chain** | Own [[layer-1|Layer-1]] blockchain (DeSo chain) |
| **Categories** | [[socialfi|SocialFi]], DeSoc, a16z / Sequoia / Coinbase Ventures / Pantera portfolio |
| **Website** | [https://www.deso.com/](https://www.deso.com/) |

---

## Overview

DeSo (Decentralized Social) is a standalone [[layer-1|Layer-1]] blockchain optimized for the specific data structures of social media. Where general-purpose chains struggle with the storage and indexing cost of high-volume social content, DeSo's protocol natively encodes social primitives — profiles, posts, follows, messages, and tips — as on-chain state. The thesis is that an open, composable **social graph** lets any developer build a client (a Twitter-like app, a creator platform, etc.) on top of the same shared data, breaking the platform lock-in of Web2 [[socialfi|SocialFi]].

The project began life in 2021 as **BitClout**, which let users speculate on tokenized "creator coins" tied to public figures' reputations. It was later rebranded and broadened into the DeSo blockchain and the DeSo Foundation. The network uses a [[proof-of-stake|proof-of-stake]] consensus model (DeSo transitioned to a PoS architecture in its "Revolution" upgrade) and supports features such as creator coins, NFTs, on-chain decentralized exchange, and tipping ("diamonds").

DESO is the native gas and utility token: it pays for transactions, profile creation, and is the settlement asset for creator-coin and DEX activity within the ecosystem.

---

## Architecture & How It Works

DeSo's design choice — a dedicated [[layer-1|Layer-1]] rather than a smart-contract dApp on an existing chain — is driven by the data profile of social media. Social activity is **write-heavy and storage-heavy** (every post, like, follow, and reply is a state change), which is expensive and slow on general-purpose chains where every node must replicate full state. DeSo addresses this with social primitives encoded directly into the protocol and an archival/indexing layer purpose-built for querying the social graph.

- **On-chain social primitives** — profiles, posts, follows, reposts, likes, direct messages, and "diamond" tips are first-class on-chain objects, not application-layer abstractions. Any client (a Twitter-like reader, a creator platform, a messaging app) reads and writes the same shared state, so a user's identity and audience are portable across applications. This is the core anti-lock-in thesis of [[socialfi|SocialFi]] / DeSoc (Decentralized Society).
- **Creator coins** — a bonding-curve market tied to each profile; the price rises as more DESO is bonded into a creator's coin. This BitClout-era primitive lets fans speculate on a creator's reputation and lets creators monetize directly.
- **Native DEX & NFTs** — an on-chain order-book exchange and NFT minting/trading are built into the protocol rather than deployed as separate contracts.
- **Consensus** — DeSo migrated from a [[proof-of-work|PoW]]-style/founder-bootstrapped model to **[[proof-of-stake|Proof-of-Stake]]** in its "Revolution" / PoS upgrade, with validators staking DESO to secure the chain and earn rewards. PoS also reduced block times and improved finality versus the original architecture.
- **Storage offloading** — large media (images, video) is typically stored off-chain (e.g., on content-addressed storage) with on-chain references, keeping the base-layer state focused on the social graph rather than raw bytes.

The protocol is open source and developer-facing: the thesis only works if third-party clients build on the shared graph, so the [[deso-foundation]] funds tooling, indexers, and reference applications.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 10.53M DESO |
| **Total Supply** | 10.81M DESO |
| **Max Supply** | 10.81M DESO |
| **Fully Diluted Valuation** | $50.08M |
| **Market Cap / FDV Ratio** | 0.97 |

The supply structure is unusual for a small-cap: a **low, fixed-ish max supply (~10.81M DESO)** with ~97% already circulating means there is **almost no future unlock/emissions overhang** — the opposite of the heavy-dilution profile seen in newer DePIN/DEX tokens. Block rewards under PoS add modest issuance, but the MC/FDV ratio of ~0.97 confirms dilution is not the dominant risk here; **demand and adoption are**. The legacy of the original "founder reward" / locked-supply controversy from the BitClout era is largely behind the project given how much of supply is now liquid.

---

## Value Accrual & Governance

DESO accrues value through three channels: (1) **gas/fees** for transactions, profile registration, and on-chain actions; (2) **creator-coin bonding** — DESO is locked into bonding curves to mint creator coins, removing it from float; and (3) **staking** under PoS, where validators and delegators lock DESO to secure consensus and earn rewards. Governance is steered by the [[deso-foundation|DeSo Foundation]] alongside validator/community input rather than a fully formalized on-chain token-vote DAO. The key value question is reflexive: DESO's utility demand scales with active social-app usage, so the token is ultimately a bet on whether decentralized social achieves product-market fit.

---

## Comparison vs Decentralized-Social Peers

| Project | Architecture | Token | Approach | Notes |
|---|---|---|---|---|
| **DeSo (DESO)** | Standalone social [[layer-1|L1]], PoS | DESO | Full on-chain social graph + creator coins | Purpose-built storage; a16z/Sequoia-backed |
| **[[farcaster]]** | Hybrid: Ethereum L1 identity + off-chain "hubs" | none (no liquid token historically) | Sufficient-decentralization social protocol | Largest mind-share in crypto-social; powers "Frames" |
| **[[lens-protocol\|Lens Protocol]]** | App-chain / [[polygon\|Polygon]]-based, NFT-based social graph | none/points historically | Composable social NFTs (profiles = NFTs) | [[aave]]-team origin |
| **[[friendtech\|friend.tech]]** | [[base\|Base]] L2 dApp | (FRIEND) | Tokenized "keys" to creator group chats | SocialFi speculation focus; activity collapsed post-2024 |

DeSo is the most **infrastructure-heavy** of the group — it owns the entire chain rather than building on an existing L1/L2 — which is both its differentiator (tailored performance, no host-chain rent) and its burden (it must bootstrap validators, liquidity, and developers alone). Farcaster, by contrast, leans on Ethereum for identity and has captured more developer attention without a tradeable token.

---

## How & Where It Trades

- **Venues:** DESO is a thinly traded micro-cap. CoinGecko's snapshot showed **no major centralized-exchange listing**, and 24h volume of only **~$19.3K** — extremely thin. Most liquidity historically came from earlier listings and the project's own ecosystem rather than tier-1 exchanges.
- **Liquidity / exit risk:** With a ~$31M cap and four-figure daily volume, DESO is effectively illiquid at size — even modest market orders can move price several percent, and exiting a meaningful position without slippage is impractical.
- **No major perps:** No significant perpetual-futures market is evident; this is a spot-only, low-float micro-cap for practical purposes.
- **Float:** ~97% of supply circulates, so there is no "unlock cliff" catalyst to trade around — moves are driven by spot demand and the broad crypto regime.

---

## Narrative, Category & Catalysts

DeSo sits in the **[[socialfi|SocialFi]] / DeSoc** narrative — a recurring but historically underperforming crypto theme. The category periodically reignites (the 2024 Farcaster/Frames wave, friend.tech's 2023 spike) but has yet to produce durable mainstream usage. Potential catalysts specific to DeSo: a breakout consumer app built on the open graph, renewed VC/ecosystem funding, integration of AI-agent social accounts, or a broad SocialFi rotation. Headwinds: the theme has been "early" for years, and DeSo competes with Farcaster's larger crypto-native mind-share.

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $198.68 (2021-06-19) |
| **Current vs ATH** | ~-98.5% |
| **All-Time Low** | $2.70 (2024-11-05) |
| **24h Change** | -0.65% |
| **7d Change** | -8.37% |

> DESO is down sharply from its 2021 launch-era peak and now trades only modestly above its all-time low, with a tight market-cap-to-FDV ratio (~0.97) indicating most supply is already circulating. The 7-day decline of -8.37% tracks the broader **Extreme Fear** regime (Fear & Greed 22, [[btc-bitcoin|BTC]] ~$64,180 on 2026-06-21).

---

## Platform & Chain Information

**Native Chain:** Own [[layer-1|Layer-1]] blockchain (DeSo chain, [[proof-of-stake|proof-of-stake]])

---

## Exchange Listings

> *No major exchange listings found in CoinGecko data.*

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.deso.com/](https://www.deso.com/) |
| **Twitter** | [@desoprotocol](https://twitter.com/desoprotocol) |
| **Reddit** | [https://www.reddit.com/r/DESO](https://www.reddit.com/r/DESO) |
| **Telegram** | [desoblockchain](https://t.me/desoblockchain) (687 members) |
| **Discord** | [https://discord.com/invite/xy3J4Cd3Ww](https://discord.com/invite/xy3J4Cd3Ww) |
| **GitHub** | [https://github.com/deso-protocol/explorer](https://github.com/deso-protocol/explorer) |
| **Whitepaper** | [https://docs.deso.org/about-deso-chain/readme](https://docs.deso.org/about-deso-chain/readme) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 49 |
| **GitHub Forks** | 29 |
| **Pull Requests Merged** | 9 |
| **Contributors** | 3 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $19,297.22 |
| **Market Cap Rank** | #603 |
| **24h Range** | $4.63 — $4.65 |
| **Last Updated** | 2026-04-09 |

---

## Distinguishing Features

- **Purpose-built social L1** — storage and indexing primitives designed specifically for social-media data, not retrofitted onto a general smart-contract chain.
- **Open social graph** — profiles, posts, and follows are on-chain and composable across any client application.
- **Creator coins & native DEX** — built-in tokenized-reputation markets and on-chain exchange, a legacy of its BitClout origins.
- **Tier-1 VC backing** — a16z, Sequoia, Coinbase Ventures, and Pantera participated in funding rounds.
- **PoS architecture** — migrated to [[proof-of-stake|proof-of-stake]] for validator-secured consensus.

## Risks

- **Adoption gap** — on-chain social media has struggled to attract mainstream users; usage metrics remain modest relative to Web2 platforms.
- **Pivot history** — the BitClout-to-DeSo rebrand and creator-coin model drew criticism over the use of public figures' identities without consent.
- **Concentration / liquidity** — small market cap (~$31M, rank #633) and thin trading volume make the token volatile and hard to exit at size.
- **Token-demand dependence** — DESO value relies on sustained social-app activity generating fee and creator-coin demand.
- **Standalone-L1 burden** — owning the whole stack means DeSo must independently sustain validators, security budget, developers, and liquidity, unlike protocols that piggyback on Ethereum/Base.
- **Narrative timing risk** — SocialFi has repeatedly proven "early"; capital rotates out fast when speculative SocialFi cycles cool.

> *This page is informational, not investment advice. Small-cap crypto assets are highly volatile and can lose most of their value rapidly.*

---

## Trading Playbook (Bear / Extreme-Fear, Bottoming Regime)

Context: as of 2026-06-23 the market is in **Extreme Fear** (Fear & Greed = 21) with a long-horizon regime read of **Bottoming / Accumulation**; [[btc-bitcoin|BTC]] ~$64.6K. For a near-illiquid SocialFi micro-cap like DESO:

- **Liquidity first:** the ~$19K daily volume is the binding constraint — position sizing, not direction, is the main risk. Assume you cannot exit at quoted price under stress; size for total loss tolerance.
- **No leverage:** no meaningful perp market exists, and the spot book is too thin to manage a leveraged exit anyway.
- **Catalyst-driven only:** in a bottoming regime, micro-cap SocialFi tokens are pure beta to risk appetite plus idiosyncratic catalysts (app launches, listings, theme rotation). Absent a concrete catalyst, there is no edge in holding through Extreme Fear.
- **Watch the float advantage:** the ~0.97 MC/FDV means no unlock-driven supply shock — a rare positive vs. peers — so any genuine demand returns flows into a near-fixed float. Track on-chain active addresses / app usage as the real signal rather than price alone.
- **Invalidation:** sustained zero-volume sessions or app/foundation stagnation argue against any allocation regardless of price.

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
- [[socialfi]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- General market knowledge; no additional specific wiki source ingested yet.
