---
title: "Sui"
type: entity
created: 2026-04-09
updated: 2026-06-20
status: excellent
tags: [crypto, altcoins]
aliases: ["SUI", "Sui Network"]
entity_type: protocol
founded: 2023
headquarters: "Mysten Labs — Palo Alto, USA"
website: "https://sui.io/"
related: ["[[crypto-markets]]", "[[solana]]", "[[aptos]]", "[[cetus-protocol]]", "[[hyperliquid]]", "[[bitcoin-etfs]]", "[[move-language]]", "[[proof-of-stake]]", "[[layer-1-blockchains]]", "[[near]]"]
---

# Sui

**Sui** (SUI) is a [[move-language|Move]]-language Layer 1 blockchain launched in May 2023 by Mysten Labs (ex-Meta/Diem engineers), built around an object-centric data model that enables parallel transaction execution. For traders it is a core "high-performance L1" basket asset alongside [[solana|Solana]] and [[aptos|Aptos]], notable in 2025–2026 for two defining events: the **$223M Cetus DEX hack and validator-coordinated fund freeze** (May 2025), and the launch of **US spot SUI ETFs** (February 2026).

---

## Market Data

| Metric | Value |
|---|---|
| **Market Cap Rank** | #32 |
| **Market Cap** | $2.89B |
| **Current Price** | $0.7161 |
| **24h Volume** | $250.79M |
| **24h Change** | +0.45% |
| **7d Change** | -6.16% |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

Context: the snapshot sits within an Established [[bear-market|Bear Market]] regime with [[fear-and-greed-index|Fear & Greed]] = 22 (extreme fear). SUI is roughly flat on the day (+0.45%) but down ~6% on the week — underperforming the L1 cohort, consistent with its standing structural **unlock overhang** (MC/FDV ~0.40). Price is ~86.6% below the January 2025 ATH of $5.35 and ~96% above the October 2023 ATL of $0.3648.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | SUI |
| **Market Cap Rank** | #32 (2026-06-20) |
| **Market Cap** | $2.89B (2026-06-20) |
| **Chain / Sector** | Own L1, [[move-language|Move]] language, object model, PoS; sectors: high-throughput L1, DeFi, consumer/gaming |
| **Categories** | Smart Contract Platform, Binance Launchpool, Layer 1 (L1), Sui Ecosystem, Coinbase Ventures Portfolio, Proof of Stake (PoS), Andreessen Horowitz (a16z) Portfolio, YZi Labs (Prev. Binance Labs) Portfolio, GMCI Layer 1 Index, Circle Ventures Portfolio, GMCI Index, Made in USA |
| **Website** | [https://sui.io/](https://sui.io/) |

---

## Overview

Sui is a Layer 1 blockchain developed by Mysten Labs, a team founded by former lead engineers from Meta's blockchain research division. It is designed for global adoption by providing a secure, high-speed environment for digital asset ownership and removing technical barriers for Web3 applications. The platform utilizes the [[move-language|Move]] programming language to create a safe framework and supports horizontal scaling to keep fees stable and speeds high as the network grows. Significant institutional support comes from major venture capital firms including Andreessen Horowitz, Coinbase Ventures, Circle Ventures, and YZi Labs.

The system functions by organizing data into independent objects rather than a single ledger of accounts. This object-centric data model enables parallel execution, allowing the network to process many transactions simultaneously instead of waiting for one to finish before starting the next. This architecture is built for rapid transaction finalization to ensure near-instant results. To maintain long-term stability, the network collects fees into a storage fund that rewards validators for keeping data on the network indefinitely.

Sui offers several advanced tools including zkLogin for easier account access and sponsored transactions that allow users to interact with apps without managing complex wallets or immediate fees. Developers can also create tailored object types that work across the entire network, which encourages innovation and deep composability.

The SUI token is central to the ecosystem, serving as the primary asset for transaction fees and on-chain utility within decentralized exchanges and lending platforms. Users participate in a proof-of-stake mechanism by locking their tokens to support validators and secure the blockchain in exchange for rewards. Additionally, token holders have a role in governance.

---

## Technology & Consensus

Sui's two technical signatures are the **[[move-language|Move]] programming language** and the **object-centric data model**, which together enable parallel transaction execution.

| Component | Detail |
|---|---|
| **Smart-contract language** | Sui Move — an adaptation of the Move language (originally from Meta's Diem); resource-oriented, with assets as first-class typed objects |
| **Data model** | Object-centric: every on-chain asset is an object with a unique ID and explicit ownership, rather than entries in a global account ledger |
| **Parallel execution** | Transactions touching *independent* objects execute in parallel; only transactions sharing the same object need sequencing |
| **Consensus** | Delegated [[proof-of-stake|PoS]]; Mysticeti DAG-based BFT consensus for shared-object transactions, with a fast "owned-object" path that bypasses full consensus for simple transfers |
| **Finality** | Sub-second for owned-object (single-writer) transactions via the fast path; consensus path for shared objects |
| **Account UX** | zkLogin (OAuth-based, no seed phrase), sponsored transactions (apps pay gas), programmable transaction blocks |

**Why the object model matters.** In account-based chains ([[ethereum|Ethereum]]), all transactions contend for global state, forcing sequential execution. Sui's object model makes data dependencies *explicit*: a simple coin transfer touches only the sender's and receiver's objects, so it takes a consensus-free "fast path" and finalizes in well under a second. Only transactions over *shared* objects (e.g. a DEX pool) require the Mysticeti consensus layer. This is the same parallel-execution thesis that powers [[aptos|Aptos]] (also Move) and [[solana|Solana]] (Sealevel), but Sui's owned-vs-shared object distinction is its distinctive design.

**Move safety.** Move's resource semantics make assets impossible to accidentally copy or destroy at the language level — a security improvement over Solidity. The trade-off: novel-language complexity created the surface for the **Cetus exploit** (below), which was a *contract-math* bug, not a Move-language flaw.

---

## Tokenomics & Supply

| Metric | Value (2026-06-20) |
|---|---|
| **Circulating Supply** | ~4,029,196,852 SUI |
| **Total Supply** | 10,000,000,000 SUI |
| **Max Supply** | 10,000,000,000 SUI |
| **Market Cap / FDV Ratio** | ~0.40 |

- **Fixed 10B cap** with the majority of supply still locked at the 2026-06-20 snapshot (circulating ~4.03B of 10B).
- **Unlock overhang**: with MC/FDV ~0.40, scheduled monthly unlocks remained a recurring sell-pressure event throughout 2025–2026, frequently traded around by SUI-perp shorts. This is the single most important supply fact for SUI traders and the cleanest contrast with fully-unlocked peers like [[near|NEAR]].
- **Staking**: SUI is staked to validators (delegated PoS); rewards come from gas fees plus a subsidy from the **storage fund** (fees collected for perpetual data storage), which is designed to taper subsidies over time.
- **Storage fund**: an unusual mechanism — storage fees are pooled and used to compensate future validators for retaining historical data, smoothing long-run validator economics.

---

## Ecosystem & Use Cases

- **DeFi** — the largest vertical; [[cetus-protocol|Cetus]] (concentrated-liquidity DEX), plus lending, perps and liquid-staking protocols. DeFi TVL recovery post-Cetus is a key fundamentals signal.
- **Consumer & gaming** — Mysten markets Sui for high-throughput consumer apps; zkLogin (sign in with Google/Apple) and sponsored transactions target mainstream onboarding.
- **Stablecoins / payments** — Circle Ventures backing and native USDC support position Sui for payments use cases.
- **DePIN / data** — Walrus decentralized storage (Mysten) extends Sui beyond pure DeFi.
- **NFTs / objects** — the object model makes rich, composable NFTs and game items first-class, a recurring marketing angle.

---

## Market Structure & Derivatives

- **Spot venues**: deep spot on [[binance|Binance]] (SUI/USDT), [[coinbase|Coinbase]], [[kraken|Kraken]] (SUI/USD), Upbit (SUI/KRW), Bitget, KuCoin, Crypto.com. ~$251M reported 24h volume (2026-06-20).
- **Perps / funding / OI**: perps on [[hyperliquid|Hyperliquid]] (SUI-PERP) and every major derivatives venue (Binance, Bybit, OKX). SUI-perp funding and OI cluster around **monthly unlock dates** — the dominant recurring negative catalyst — and around ETF-flow prints. Funding tends to flip negative ahead of large unlocks as shorts position for supply.
- **ETF exposure**: 21Shares launched a **2x leveraged SUI ETF in December 2025**; the **first US spot SUI ETFs went live in February 2026** — Canary Capital's SUIS (with staking) and the Grayscale Sui Staking ETF, followed days later by 21Shares' spot TSUI on Nasdaq. Bitwise and Grayscale filings extended the pipeline. Staking ETFs absorb float, a mild structural counterweight to unlocks.
- **Native chain address**: `0x0000000000000000000000000000000000000000000000000000000000000002::sui::SUI`.

---

## Trading Playbook

- **Narrative baskets**: "alt-L1 / Solana-killer" basket ([[solana|Solana]], [[aptos|Aptos]], [[avalanche|Avalanche]]); **[[move-language|Move]]-language pair trade vs [[aptos|Aptos]]** (both Move chains, often traded as a relative-value pair); ETF-flow basket since February 2026.
- **Unlock playbook**: the defining SUI trade is positioning around monthly unlocks — fade strength into unlock dates, watch perp funding turn negative as shorts crowd in, then watch for relief rallies once supply is absorbed.
- **Catalysts**: ETF inflow prints (staking ETFs absorb float), monthly token unlocks (dominant recurring negative catalyst at MC/FDV ~0.40), DeFi TVL recovery post-Cetus, Mysten ecosystem launches (zkLogin consumer apps, gaming, Walrus).
- **Risk profile**: traded ~86.6% below its January 2025 ATH ($5.35) at the 2026-06-20 snapshot; high beta with a structural unlock overhang. The **Cetus freeze precedent cuts both ways**: tail-risk mitigation for holders, but a governance/centralization discount for credible-neutrality purists.
- **Regime note (2026-06-20)**: SUI's -6% week into extreme fear and an Established Bear Market shows it underperforming cleaner-supply L1s; size for high beta and unlock-driven air pockets.

---

## History

- **2022** — Mysten Labs (ex-Meta/Diem engineers, incl. Evan Cheng) raises large a16z-led rounds; testnet.
- **May 2023** — Mainnet launch; SUI token generation event.
- **2024** — Ecosystem build-out (Cetus, lending, NFTs); SUI runs to its ATH of **$5.35 (2025-01-04)**.
- **22 May 2025** — **Cetus hack**: ~$223M drained from the largest DEX on Sui via a u256 overflow bug in concentrated-liquidity math; ~$60M bridged to Ethereum, ~$162M still on-chain.
- **29 May 2025** — Validators (>90% of stake) vote to **freeze and return** the on-chain $162M; Cetus relaunches 17 days post-hack with a $30M Sui Foundation loan. Landmark case study in L1 "freezability."
- **Dec 2025** — 21Shares 2x leveraged SUI ETF launches.
- **Feb 2026** — First **US spot SUI ETFs** go live (Canary SUIS with staking, Grayscale Sui Staking ETF, 21Shares TSUI on Nasdaq).
- **2026** — Bear-market derating; unlock overhang and extreme-fear regime weigh on price (~$0.72 at 2026-06-20).

---

## Competitive Positioning

| Project | Language / model | Parallelism | Supply / MC-FDV | MC rank (2026-06-20) |
|---|---|---|---|---|
| **Sui** | [[move-language|Move]], object-centric | Owned/shared object parallelism (Mysticeti) | 10B cap, MC/FDV ~0.40 (unlock overhang) | #32 |
| [[aptos|Aptos]] | [[move-language|Move]], account model | Block-STM optimistic parallelism | Uncapped, unlock schedule | mid-cap |
| [[solana|Solana]] | Rust (Sealevel) | Sealevel parallel runtime | Uncapped, disinflationary | top 10 |
| [[near|NEAR]] | Rust/JS (Wasm), Nightshade [[sharding]] | Sharded | Uncapped, ~2.5% infl., fully unlocked | #34 |
| [[avalanche|Avalanche]] | EVM (Subnets) | Subnet horizontal scaling | Capped 720M | mid-cap |

Sui's clearest peer is **[[aptos|Aptos]]** (the other major Move chain) — the two are often traded as a relative-value pair. Versus [[solana|Solana]] it competes on parallel-execution throughput; versus [[near|NEAR]] its main disadvantage is supply structure (heavy unlock overhang vs. NEAR's fully-unlocked float), while its advantage is a larger, more active DeFi ecosystem.

---

## Regulatory

- **Asset classification**: SUI is a PoS utility/staking token; the live US spot ETFs (Canary SUIS, Grayscale, 21Shares TSUI) imply a commodity-style treatment is expected. The CLARITY Act market-structure process is a sector tailwind for utility L1 tokens.
- **Staking-in-ETF**: Canary's SUIS includes staking, making SUI an early test case for whether US spot ETFs can pass through staking yield — a regulatory question that affects effective ETF demand.
- **Centralization optics**: the Cetus validator freeze (May 2025) demonstrated that Sui validators can coordinate to freeze/return funds — useful for victim recovery but a regulatory/credible-neutrality discussion point, since it shows the network is not maximally censorship-resistant.

---

## Risks

- **Unlock overhang** — MC/FDV ~0.40 means substantial supply still to be released; monthly unlocks are a persistent headwind in a bear tape.
- **Smart-contract risk** — the Cetus exploit ($223M) showed DeFi-math vulnerabilities can hit the flagship ecosystem app, dragging sentiment even when the L1 itself is sound.
- **Centralization discount** — validator freezability undermines pure credible-neutrality narratives.
- **Competition** — direct collision with [[aptos|Aptos]] (Move), [[solana|Solana]] (throughput), and the broader alt-L1 field for developer mindshare and DeFi TVL.
- **High beta / macro** — large-cap alt L1; ~86.6% off ATH in an Established Bear Market with extreme fear.
- **ETF path dependence** — discrete ETF-flow catalysts can reverse if filings are denied or inflows disappoint.

---

## Platform & Chain Information

**Native Chain:** Sui

### Contract Addresses

| Chain | Address |
|---|---|
| Sui | `0x0000000000000000000000000000000000000000000000000000000000000002::sui::SUI` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | SUI/USDT | N/A |
| Kraken | SUI/USD | N/A |
| Upbit | SUI/KRW | N/A |
| Bitget | SUI/USDT | N/A |
| KuCoin | SUI/USDT | N/A |
| Crypto.com Exchange | SUI/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| [[hyperliquid|Hyperliquid]] | SUI-PERP | Perpetual |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://sui.io/](https://sui.io/) |
| **Twitter** | [@SuiNetwork](https://twitter.com/SuiNetwork) |
| **Discord** | [https://discord.gg/sui](https://discord.gg/sui) |
| **GitHub** | [https://github.com/MystenLabs/sui](https://github.com/MystenLabs/sui) |
| **Whitepaper** | [https://github.com/MystenLabs/sui/blob/main/doc/paper/sui.pdf](https://github.com/MystenLabs/sui/blob/main/doc/paper/sui.pdf) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 5,403 |
| **GitHub Forks** | 12,286 |
| **Commits (4 weeks)** | 219 |
| **Pull Requests Merged** | 9,209 |
| **Contributors** | 218 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Related

- [[crypto-markets]]
- [[cetus-protocol]] — the May 2025 $223M hack on Sui
- [[solana]], [[aptos]], [[avalanche]] — high-performance L1 peers
- [[aptos]] — fellow [[move-language|Move]] chain, primary pair-trade leg
- [[near]] — AI/L1 peer with contrasting (fully-unlocked) supply
- [[hyperliquid]] — SUI-PERP venue
- [[bitcoin-etfs]] — ETF-wave context
- [[move-language]], [[proof-of-stake]], [[layer-1-blockchains]]

---

## Sources

- CoinGecko top-1000 snapshot 2026-04-09 (Source: [[coingecko-top-1000-2026-04-09]])
- cryptodataapi.com / CoinGecko markets snapshot, 2026-06-20 (current Market Data block)
- [Cyfrin — Inside the $223M Cetus Exploit: Root Cause and Impact Analysis](https://www.cyfrin.io/blog/inside-the-223m-cetus-exploit-root-cause-and-impact-analysis)
- [The Defiant — Sui Validators Vote to Restore $162 Million to Hacked Cetus Users (May 2025)](https://thedefiant.io/news/blockchains/sui-validators-vote-to-restore-usd162-million-to-hacked-cetus-users)
- [The Block — Cetus restarts platform after recovering from $223M exploit (June 2025)](https://www.theblock.co/post/357386/sui-dex-cetus-protocol-restarts-platform-after-recovering-from-223-million-exploit)
- [The Block — First spot SUI ETFs debut as Canary Capital and Grayscale launch funds with staking (Feb 2026)](https://www.theblock.co/post/390271/first-spot-sui-etf-goes-live-as-canary-capital-launches-suis-fund-with-staking)
- [The Block — 21Shares rolls out spot SUI ETF (TSUI) on Nasdaq (Feb 2026)](https://www.theblock.co/post/391084/21shares-spot-sui-etf-marking-latest-fund-to-launch)
- [Sui Blog — Canary Capital Launches First Spot SUI ETF (Nasdaq: SUIS)](https://blog.sui.io/canary-capital-staking-spot-sui-etf-nasdaq-suis/)
- Verified via Perplexity (sonar) and web search, 2026-06-10.
