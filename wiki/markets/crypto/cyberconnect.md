---
title: "CyberConnect (CYBER)"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [altcoins, crypto, nft]
aliases: ["CYBER", "Cyber", "CyberConnect"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://cyber.co/"
related: ["[[crypto-markets]]", "[[dao]]", "[[ethereum]]", "[[layer-2]]", "[[socialfi]]"]
---

# CyberConnect (CYBER)

**CYBER** is the native token of **CyberConnect**, a [[socialfi]] project that began as a **decentralized social graph protocol** — a portable, user-owned layer for social connections and identity — and has since evolved into **"Cyber," an [[layer-2|Layer-2]] network purpose-built for social applications**. The Cyber L2 is part of the Optimism Superchain and offers account abstraction, gas sponsorship, and tooling (the CyberConnect protocol, CyberDB) so developers can build web2-like social apps with web3 ownership. It ranks **#732** by market capitalization.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

As of 2026-06-21, CYBER trades at **$0.369171** with a market capitalization of **$24,800,069** (rank **#732**). The token is up **+2.68%** over 24h and **+7.64%** over the trailing 7 days — outperforming a generally risk-off market (BTC ~$64,180; Fear & Greed Index 22 — "Extreme Fear").

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | CYBER |
| **Market Cap Rank** | #732 |
| **Market Cap** | $24,800,069 |
| **Current Price** | $0.369171 |
| **24h Change** | +2.68% |
| **7d Change** | +7.64% |
| **Categories** | SocialFi, Smart Contract Platform, NFT, Layer 2 (L2), Decentralized Identifier (DID), BNB Chain Ecosystem, Ethereum Ecosystem, Optimism Superchain Ecosystem, Governance, Animoca Brands Portfolio, Multicoin Capital Portfolio, YZi Labs (Prev. Binance Labs) Portfolio, Delphi Ventures Portfolio |
| **Website** | [https://cyber.co/](https://cyber.co/) |
> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

---

## Overview

**Cyber** is positioned as the [[layer-2|Layer-2]] for social applications. It enables developers to build apps in which users own their social connections, content, and identity. The stack integrates high-throughput L2 infrastructure (low fees, high TPS, built on the OP Stack / Optimism Superchain) with purpose-built social tooling — most notably the **CyberConnect protocol** (the decentralized social graph) and **CyberDB**. To deliver a familiar, web2-like UX, Cyber emphasizes **native account abstraction** and **seedless/gas-sponsored wallets**, lowering the onboarding friction that has historically held back [[socialfi]] adoption.

### From CyberConnect protocol to the Cyber L2

The project's evolution is central to understanding the token:

1. **CyberConnect (the protocol)** — launched as a decentralized **social graph**: a shared, portable data layer where follows, profiles, and content links are user-owned [[nft]]-style records (e.g., profile NFTs, "W3ST" attestations), so social capital is not locked inside a single platform.
2. **Cyber (the L2)** — the protocol expanded into its own **Layer-2 network** for social apps, rebranding around "Cyber" and the `cyber.co` domain, with the CYBER token serving the network rather than just the original protocol.

This protocol → L2 trajectory is the project's defining narrative and distinguishes it from single-app SocialFi projects.

### How the social graph works

The original CyberConnect protocol decomposed "social" into a small set of composable, user-owned primitives:

- **Profile NFTs** — a user's social identity is minted as an [[nft]], so the account itself is a portable, tradeable, self-custodied asset rather than a row in a platform database. The profile carries the user's handle and serves as the anchor for follows and content.
- **Subscriptions / follows** — when a user follows a profile, the relationship is recorded on-chain (historically as "Subscribe NFTs"), making the follow graph itself portable across any application that reads the protocol.
- **W3ST (Web3 Status Tokens)** — non-transferable, [[attestation]]-style tokens that represent achievements, memberships, or status within a community. Because they are soulbound-style records, they function as on-chain reputation that an app cannot fabricate or revoke unilaterally.
- **Essences** — monetizable content units (posts, collectibles) a creator can mint and that followers can collect, giving creators a native primitive for content ownership and monetization.

The defining property is **composability**: any app built on the graph reads the same follows, profiles, and reputation, so a user's social capital is not trapped inside one product. This is the core [[socialfi]] thesis — break the data moat that lets web2 platforms lock in users.

### The Cyber L2 stack

Cyber is built on the **OP Stack** and participates in the [[optimism|Optimism]] Superchain, so it inherits Ethereum-aligned security and shared-sequencing/interop roadmaps while adding social-specific tooling on top:

- **Native account abstraction (ERC-4337-style)** — users get smart-contract wallets out of the box, enabling seedless onboarding, social recovery, and batched transactions that feel like a normal app login rather than a crypto wallet flow.
- **Gas sponsorship / paymasters** — apps can pay or subsidize user gas, removing the "buy ETH before you can post" barrier that kills mainstream onboarding.
- **CyberDB and indexing** — purpose-built data and indexing layer so social apps can query the graph efficiently instead of scanning raw chain state.
- **CYBER as the gas token** — transactions on the Cyber L2 are denominated in CYBER, which is the central value-accrual lever (see [[#Value accrual]]).

### Token role

The **CYBER** token functions as:

- **Gas / network token** for the Cyber L2 (paying for transactions, sponsoring user gas via account abstraction).
- **Governance** — a [[governance-token]] for protocol/network decisions, aligned with the project's [[dao]] direction.
- **Staking / utility** within the ecosystem to secure and participate in the network.

CYBER had a fixed-cap distribution and was featured via Binance Launchpool and CoinList, with backing from notable funds (Animoca Brands, Multicoin Capital, Delphi Ventures, and Binance Labs / YZi Labs).

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | ~61.24M CYBER |
| **Total / Max Supply** | 100.00M CYBER |
| **Market Cap / FDV Ratio** | ~0.61 |

CYBER has a relatively small, **hard-capped 100M max supply** — distinguishing it from the multi-billion-supply gaming reward tokens covered elsewhere in this wiki. The MC/FDV of ~0.61 indicates that a meaningful but not extreme portion of supply remains to unlock, so some future dilution is expected but the [[emissions]] profile is far tamer than uncapped reward tokens like [[smooth-love-potion|SLP]].

### Value accrual & governance

CYBER's value-accrual story rests on three legs, in roughly increasing order of importance:

1. **Network gas demand.** As the Cyber L2's gas token, CYBER captures fee demand from social activity on the chain. This is the strongest potential accrual mechanism, but it is contingent on real transaction throughput from deployed apps — a bet, not yet a realized cash flow at scale.
2. **Staking / security & participation.** CYBER can be staked to participate in and secure the ecosystem, locking float and aligning holders with network usage.
3. **Governance.** As a [[governance-token]], CYBER votes on protocol parameters, treasury, and grants in the project's [[dao]] direction.

The key caveat common to all infrastructure tokens applies: **product usage does not automatically translate into token demand** unless gas, staking, or fee mechanics force it. The thinner the link between app activity and required CYBER spend, the weaker the accrual.

### Competitive comparison

| Project | Token | Primary form | Differentiator | Edge / risk |
|---|---|---|---|---|
| **CyberConnect / Cyber** | CYBER | Social graph protocol **+ dedicated L2** | Owns both the graph and the chain; native AA + gas sponsorship | Full-stack control vs. unproven app demand |
| [[lens-protocol\|Lens Protocol]] | — | Social graph protocol (Polygon → own L2 "Lens Chain") | Large developer mindshare, profile-NFT graph | Strong protocol but app traction still early |
| **Farcaster** | — (no L1 token) | Sufficiently-decentralized social protocol + Warpcast client | Highest real DAU among web3 social; Frames | Tokenless; competes on usage, not token narrative |
| **Friend.tech** | — | SocialFi app (keys/shares on Base) | Viral creator-monetization mechanic | Fad-prone; retention collapse risk |

Against pure protocols (Lens) and tokenless networks (Farcaster), Cyber's wager is that bundling a low-friction, social-optimized L2 with the graph attracts more app deployment. The corresponding risk is that the most-used web3 social network so far (Farcaster) has no token at all, so the category does not obviously reward token-bearing infrastructure.

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $15.79 (2023-09-01) |
| **Current vs ATH** | ~-98% |
| **24h Change** | +2.68% |
| **7d Change** | +7.64% |

CYBER spiked to **~$15.79 shortly after its September 2023 listing** — a low-float launch with heavy exchange attention — then fell ~98% as the initial float expanded and SocialFi hype cooled. At ~$0.37 it trades as a discounted [[socialfi]] / [[layer-2]] infrastructure token. Its recent +7.6% weekly gain stands out as relative strength versus the broader risk-off tape.

---

## History & Timeline

> Dated events below are limited to those that are well established. Where a precise date is not verified, the entry is kept qualitative rather than invented.

- **2021–2022** — CyberConnect launches as a decentralized **social graph protocol**, backed by funds including Animoca Brands, Multicoin Capital, Delphi Ventures, and (then) Binance Labs.
- **2023-08** — CYBER featured via **Binance Launchpool** and a CoinList sale, drawing major exchange attention to a low-float token.
- **2023-09** — CYBER lists on Binance and other venues; price spikes to its **all-time high of ~$15.79 (2023-09-01)** before the float expands.
- **2023–2025** — Project rebrands around **"Cyber,"** pivoting from a standalone protocol to a dedicated [[layer-2|Layer-2]] for social apps on the OP Stack / [[optimism|Optimism]] Superchain, consolidating around the `cyber.co` domain.

---

## Narrative, Category & Catalysts

CYBER sits at the intersection of three crypto narratives, which is both its appeal and its volatility source:

- **DeSoc / [[socialfi|SocialFi]]** — the thesis that users should own their social graph; re-rates with renewed interest in on-chain social (e.g. Farcaster/Lens cycles).
- **[[layer-2|Layer-2]] / Superchain** — exposure to the OP Stack and [[optimism|Optimism]] interop roadmap; benefits from "app-chain / vertical L2" narratives.
- **Decentralized identity (DID)** — profile NFTs and W3ST [[attestation]]s tie it to the on-chain-identity theme.

**Potential catalysts:** a breakout consumer social app deployed on the Cyber L2 driving measurable gas demand; Superchain interop milestones; renewed SocialFi mania led by a peer (Farcaster/Lens) lifting the whole category; exchange or staking-program announcements. **Anti-catalysts:** the absence of a flagship app, continued SocialFi apathy, and Farcaster's tokenless success implicitly questioning whether the category needs an infrastructure token at all.

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x14778860e937f509e651192a90589de711fb88a9` |
| Cyber | `0x14778860e937f509e651192a90589de711fb88a9` |
| Binance Smart Chain | `0x14778860e937f509e651192a90589de711fb88a9` |
| Optimistic Ethereum | `0x14778860e937f509e651192a90589de711fb88a9` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | CYBER/USDT | N/A |
| Kraken | CYBER/USD | N/A |
| Upbit | CYBER/KRW | N/A |
| Bitget | CYBER/USDT | N/A |
| KuCoin | CYBER/USDT | N/A |
| Crypto.com Exchange | CYBER/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| [[hyperliquid|Hyperliquid]] | CYBER-PERP | Perpetual |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://cyber.co/](https://cyber.co/) |
| **Twitter** | [@BuildOnCyber](https://twitter.com/BuildOnCyber) |
| **Telegram** | [buildoncyber](https://t.me/buildoncyber) (20,366 members) |
| **Discord** | [https://discord.com/invite/buildoncyber](https://discord.com/invite/buildoncyber) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **Market Cap Rank** | #732 |
| **Price (2026-06-21)** | $0.369171 |
| **Derivatives** | CYBER-PERP listed on [[hyperliquid|Hyperliquid]] and major CEX perp venues |
| **Last Updated** | 2026-06-21 |

CYBER enjoys strong exchange coverage relative to its market cap — listed on Binance, Kraken, Bitget, KuCoin, Crypto.com, and Upbit, with perpetual futures on [[hyperliquid|Hyperliquid]] and major CEX perp venues. The low-float September 2023 launch contributed to high early volatility; active derivatives markets continue to amplify swings. **How & where it trades:** primary spot liquidity is on Binance (CYBER/USDT) with a strong Korean bid via Upbit (CYBER/KRW), which can create a "Kimchi"-style basis during local sentiment spikes. The deep CEX coverage relative to a ~$25M cap means CYBER is unusually liquid for its size — but that same coverage, combined with perps, makes it a popular vehicle for leveraged momentum trades and consequently prone to funding-driven squeezes and liquidation cascades in both directions.

---

## Competitive Position

Cyber competes in **SocialFi / decentralized-social infrastructure**, a segment that also includes protocols like Lens Protocol and Farcaster, and broadly overlaps with the decentralized-identity ([[dao]] / DID) theme. Its differentiator is the full-stack approach: it owns both the **social graph protocol** and a dedicated **[[layer-2]] network** optimized for social UX (account abstraction, gas sponsorship). The bet is that giving developers an end-to-end, low-friction social platform — rather than just a protocol — drives more app deployment. The risk is that SocialFi adoption broadly remains early and no decentralized social network has yet reached durable mainstream scale.

---

## Risks

- **SocialFi adoption risk** — the entire [[socialfi]] category is unproven at scale; user retention and network effects are hard to win against incumbent web2 social platforms.
- **Narrative/sentiment dependence** — re-rates with SocialFi, [[layer-2]], and DID narratives; sentiment has been soft.
- **Pivot/execution risk** — the protocol → L2 rebrand is ambitious; value accrual to CYBER depends on real app and transaction demand on the Cyber chain.
- **Low-float legacy & unlocks** — the volatile low-float launch and remaining ~39% of supply to unlock create dilution/overhang considerations (see [[emissions]]).
- **Small-cap volatility** — a ~$25M cap with active perps; exposed to leverage-driven moves in risk-off regimes (Fear & Greed 22 / Extreme Fear).

---

## Trading Playbook (bear / Extreme-Fear regime)

> Context: as of 2026-06-22 the market is in an established **bear market** with Fear & Greed at **21 (Extreme Fear)** and market-health 30/100; BTC ~$64.2k (~16% below its 200-day MA). Small-cap narrative tokens like CYBER are high-beta to this tape. This is informational, not financial advice.

- **Default stance: cautious / underweight.** In Extreme Fear, SocialFi micro-caps tend to bleed regardless of project-specific news. Survival of capital outranks chasing a re-rate that the macro regime is actively suppressing.
- **Relative-strength filter.** CYBER's recent +7.6% weekly outperformance is notable but thin-conviction in a risk-off tape; treat single-week strength as a trade, not a trend, until breadth and BTC structure improve.
- **Use the perp/funding signal.** Because CYBER has active perps, watch funding and open interest: persistently negative funding into a flat/up spot is a contrarian squeeze setup; euphoric positive funding into resistance is a fade setup.
- **Catalyst-gated longs only.** Size up only on a genuine fundamental catalyst (flagship app launch, Superchain milestone, staking program) confirmed by volume — not on narrative chatter alone.
- **Hard risk control.** Define invalidation against the structural levels (e.g. loss of recent range lows) and respect the ~98%-from-ATH drawdown as evidence that "cheap" can get cheaper. Avoid leverage on a name this volatile during Extreme Fear.

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *See [[#History & Timeline]] for dated milestones. Further notable events will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[socialfi]]
- [[layer-2]]
- [[optimism]]
- [[attestation]]
- [[dao]]
- [[governance-token]]
- [[lens-protocol]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]]) — initial market snapshot
- Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).
- General market knowledge; no specific wiki source ingested yet for project history and architecture.
