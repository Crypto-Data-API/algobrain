---
title: "Sophon"
type: entity
created: 2026-04-09
updated: 2026-06-23
status: excellent
tags: [crypto, altcoins]
aliases: ["SOPH"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://sophon.xyz/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[zksync]]", "[[zk-rollup]]", "[[gamefi]]"]
---

# Sophon

**Sophon** (token: **SOPH**) is a consumer-entertainment-focused Layer-2 chain built as a modular [[zk-rollup]] using the **ZK Stack** — the same toolkit that powers [[zksync]] — and secured by validity proofs settling to [[ethereum]]. Rather than competing for existing DeFi users, Sophon targets entertainment verticals with proven traction (gaming, gambling/sports betting, ticketing, social, and consumer AI), wrapping them in consumer-grade UX: gasless transactions, social-login account abstraction, and "invisible" blockchain. It ranks **#859** by market capitalization.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).* SOPH trades at **$0.00534809**, market cap **$18.47M** (rank **#859**), **+1.54%** on the day but **-5.55%** over 7 days, lagging the broad market amid "Extreme Fear" conditions (BTC ~$64,180, Fear & Greed Index 22).

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | SOPH |
| **Market Cap Rank** | #859 |
| **Market Cap** | $18,465,404 |
| **Current Price** | $0.00534809 |
| **24h / 7d** | +1.54% / -5.55% |
| **Categories** | Smart Contract Platform, BNB Chain Ecosystem, Polygon Ecosystem, Arbitrum Ecosystem, Layer 2 (L2), Base Ecosystem, Binance HODLer Airdrops, Binance Alpha Spotlight, Base Native |
| **Website** | [https://sophon.xyz/](https://sophon.xyz/) |
> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

---

## Overview

Sophon is a consumer-entertainment platform-and-chain that aims to onboard mainstream users by making blockchain "invisible." It is built as a modular [[zk-rollup]] on the **ZK Stack** (the open-source rollup framework behind [[zksync]]), inheriting that codebase's proving system and account-abstraction features while customizing the chain for entertainment apps. SOPH was distributed in part via a **Binance HODLer Airdrop**.

### Mechanism / architecture

- **ZK Stack rollup on [[ethereum]]** — Sophon batches transactions and posts validity (zero-knowledge) proofs to Ethereum, inheriting L1 security with low fees. See [[zk-rollup]] and [[zksync]].
- **Native account abstraction** — users sign up with familiar Google/Apple logins, with self-custodial wallets created transparently in the background.
- **Gasless experience** — via paymasters from the ZKsync codebase, Sophon can sponsor fees so end users never see gas, a major UX unlock for consumer apps.
- **Social Oracle / zkTLS** — Sophon uses zkTLS to bring users' off-chain achievements, reputation, and social signals on-chain without exposing personal data, turning everyday online activity into verifiable, user-owned assets.
- **Entertainment focus** — the chain courts gaming, gambling/sports betting, ticketing, social, and consumer-AI apps rather than DeFi power users. See [[gamefi]].

### Token role

The **SOPH** token is the native asset of the Sophon ecosystem: it is used for network fees / gas economics (even when end-user transactions are sponsored), staking and securing the rollup, ecosystem incentives, and governance over the chain. As an L2/entertainment-chain token, its value is tied to the chain's transaction throughput, the success of apps built on it, and the broader [[zk-rollup]] and consumer-crypto narratives — not to any direct cash flow.

### Value accrual & governance

For an L2 token, value accrual runs through a few channels — each with caveats:

- **Sequencer / fee economics** — to the extent the chain earns sequencer revenue (the spread between L2 fees collected and L1 settlement/DA costs paid), that surplus can accrue to stakers or a treasury. With gasless consumer flows, much of this is subsidized by apps/paymasters rather than charged to users, so fee accrual depends on real, paid throughput.
- **Staking & security** — SOPH staking is intended to help secure the rollup and align operators, earning incentives in return; this is an inflationary reward in the bootstrap phase, not a fee dividend.
- **Governance** — SOPH governs chain parameters, incentive allocation, and ecosystem grants. As with most app-chain tokens, governance value is contingent on the treasury and emissions being large enough to matter.

The honest read: like most early L2 tokens, SOPH today is primarily a *liquidity/incentive and governance* asset whose price tracks narrative and on-chain activity, not a cash-flow instrument. The thin MC/FDV ratio (≈0.31) means emissions are a structural headwind to value accrual until paid usage scales.

### Deep dive — how a ZK Stack chain works

Sophon is a member of the **ZKsync "Elastic Chain"** family: a network of independent ZK Stack rollups (and validiums) that share the same prover, bridging hub, and interoperability layer rather than living as siloed chains. The relevant primitives:

- **Validity (ZK) proofs vs. fraud proofs** — unlike optimistic rollups ([[base]], Arbitrum) that assume transactions are valid and allow a multi-day challenge window, a ZK rollup posts a cryptographic *validity proof* (a SNARK/STARK) with each batch. Once Ethereum verifies the proof, state is final, so withdrawals do not wait a 7-day challenge period. See [[zk-rollup]].
- **Data availability mode** — ZK Stack chains can run as a *rollup* (transaction data posted to Ethereum L1 / blobs) or as a cheaper *validium* (data kept off-chain with a DA committee). The DA choice is the dominant lever on both fee level and trust assumptions. Sophon, optimizing consumer-app cost, leans on the low-fee end of this spectrum.
- **Native account abstraction (AA)** — AA is built into the protocol rather than bolted on (as with [[ethereum|Ethereum]]'s ERC-4337). Every account can be a smart account, enabling social login, session keys (sign once, play many transactions), and paymaster-sponsored gas without a separate bundler ecosystem.
- **Paymasters** — contracts that pay gas on behalf of users, optionally accepting an ERC-20 (or nothing) instead of ETH. This is what makes "gasless" consumer flows possible.
- **zkTLS / Social Oracle** — zkTLS lets a user prove a fact about a TLS (HTTPS) session — e.g., "I have >10k followers" or "I hold this game achievement" — without revealing the underlying credentials, porting Web2 reputation on-chain privately.

### Competitive position

Sophon competes against other consumer-and-gaming-oriented L2s and app-chains, and against general-purpose L2s that also court games:

| Project | Type | Core thesis | Stack / settlement | Differentiator vs. Sophon |
|---|---|---|---|---|
| **Sophon** | Consumer/entertainment L2 | Make blockchain invisible for gaming, gambling, social, consumer-AI | ZK Stack (ZK rollup) → [[ethereum]] | Entertainment focus + gasless + social login + zkTLS Social Oracle |
| **Abstract** | Consumer L2 | Consumer-app chain from the Pudgy Penguins / Igloo team | ZK Stack (ZK rollup) → Ethereum | Same ZK Stack lineage; brand-led (Pudgy) vs. vertical-led (Sophon) |
| **[[ronin]]** | Gaming chain | Purpose-built chain originally for Axie Infinity | Sidechain / its own validators | Established gaming flagship and player base; less general consumer scope |
| **Immutable (IMX)** | Gaming L2 | Web3 gaming platform, zkEVM + order-book | Immutable zkEVM (Polygon CDK) | Deep games pipeline + minting/marketplace tooling |
| **[[base]]** | General-purpose L2 | Coinbase-backed onboarding rail | OP Stack (optimistic) → Ethereum | Far larger TVL/liquidity and distribution; not entertainment-specialized |

Sophon's edge is a focused consumer/entertainment thesis with strong UX primitives (gasless, social login, zkTLS) and the maturity of the underlying ZK Stack; its challenge is the intensely crowded L2 landscape, where attracting and retaining flagship apps and real on-chain activity is the decisive factor. Its closest "ZK Stack consumer L2" peer is Abstract, making narrative differentiation and flagship-app traction critical.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 3.15B SOPH |
| **Total Supply** | 10.00B SOPH |
| **Max Supply** | 10.00B SOPH |
| **Fully Diluted Valuation** | $86.11M |
| **Market Cap / FDV Ratio** | 0.31 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.1108 (2025-05-28) |
| **Current vs ATH** | -92.24% |
| **All-Time Low** | $0.00796068 (2026-03-28) |
| **Current vs ATL** | +7.97% |
| **24h Change** | -1.46% |
| **7d Change** | +2.21% |
| **30d Change** | +1.76% |
| **1y Change** | +0.00% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x6b7774cb12ed7573a7586e7d0e62a2a563ddd3f0` |
| Polygon Pos | `0xeb971fd26783f32694dbb392dd7289de23109148` |
| Sophon | `0x000000000000000000000000000000000000800a` |
| Arbitrum One | `0x31dba3c96481fde3cd81c2aaf51f2d8bf618c742` |
| Binance Smart Chain | `0x31dba3c96481fde3cd81c2aaf51f2d8bf618c742` |
| Base | `0x31dba3c96481fde3cd81c2aaf51f2d8bf618c742` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | SOPH/USDT | N/A |
| Upbit | SOPH/KRW | N/A |
| Bitget | SOPH/USDT | N/A |
| KuCoin | SOPH/USDT | N/A |
| Crypto.com Exchange | SOPH/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| [[hyperliquid|Hyperliquid]] | SOPH-PERP | Perpetual |
| Uniswap V3 (Ethereum) | 0X6B7774CB12ED7573A7586E7D0E62A2A563DDD3F0/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

### How & where it trades

- **Spot** — SOPH is broadly listed across major CEXs (Binance, Upbit, Bitget, KuCoin, Crypto.com), with on-chain spot depth on Uniswap V3 (Ethereum). The token is bridgeable across several ecosystems (contract addresses on Ethereum, Polygon, Arbitrum, BSC, Base and Sophon itself), so liquidity is fragmented across venues.
- **Derivatives** — a SOPH-PERP perpetual trades on [[hyperliquid|Hyperliquid]], giving traders leveraged long/short exposure and a funding-rate signal for positioning. For a sub-$20M-cap token, perp open interest and funding can be more informative (and more violent) than spot.
- **Liquidity & float** — at an ~$18M cap with ~$9M daily volume, SOPH is thin: book depth is shallow, so size moves price and [[slippage]] is material. The low MC/FDV (~0.31) plus Binance HODLer-airdrop distribution means recipients' sell pressure and future unlocks weigh on the float. Treat it as a low-float, high-beta L2 token. See [[liquidity]].

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://sophon.xyz/](https://sophon.xyz/) |
| **Twitter** | [@sophon](https://twitter.com/sophon) |
| **GitHub** | [https://github.com/sophon-org](https://github.com/sophon-org) |
| **Whitepaper** | [https://docs.sophon.xyz/](https://docs.sophon.xyz/) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $9.42M |
| **Market Cap Rank** | #782 |
| **24h Range** | $0.00859110 — $0.00903698 |
| **Last Updated** | 2026-04-09 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Risks

- **Crowded L2 competition** — the consumer/gaming L2 field is saturated; without sticky flagship apps and genuine activity, a chain token struggles to hold value.
- **Adoption / activity risk** — token value depends on real transaction throughput and app usage, which are hard to bootstrap and easy to overstate.
- **Large unlock overhang** — only ~3.15B of a 10B max supply circulates (MC/FDV ≈ 0.31), so substantial future emissions and team/investor unlocks pose dilution pressure; the ~92% drawdown from the 2025 ATH partly reflects post-airdrop and unlock selling.
- **Airdrop selling** — distribution via a Binance HODLer airdrop tends to seed concentrated early sell pressure from recipients.
- **Narrative dependence** — exposure to both the [[zk-rollup]] / L2 narrative and the entertainment-crypto theme, either of which can cool quickly.
- **Liquidity** — despite broad CEX listings and a [[hyperliquid|Hyperliquid]] perp, an ~$18M-cap L2 token is thin for large trades. See [[liquidity]] and [[slippage]].

---

## Narrative, Category & Catalysts

Sophon sits at the crossroads of two narratives: **ZK / L2 scaling** (the ZK Stack "Elastic Chain" thesis that many app-specific ZK chains share one prover and interop hub) and **consumer crypto / entertainment** (gaming, gambling, social, consumer-AI as the next on-chain user wave). Potential catalysts to watch:

- A flagship app (a hit game, a high-volume betting/social app) that produces sustained, *paid* on-chain activity rather than incentive-farmed transactions.
- ZK Stack ecosystem momentum (shared liquidity/interop across Elastic Chain members like Abstract and [[zksync]]).
- Exchange / derivatives expansion deepening liquidity beyond the current perp + CEX spot.
- Token sinks (fee burns, staking demand) that improve the weak value-accrual picture.

Headwinds: the consumer-L2 field is crowded, the token's float is small and emission-heavy, and "Extreme Fear" macro (F&G 21, market-health 29/100, June 2026) compresses risk appetite for micro-cap L2 bets.

---

## Major News & Events

> *Real, dated timeline. Undated qualitative items are flagged.*

| Date | Event |
|---|---|
| 2025-05-28 | SOPH all-time high of **$0.1108** (CoinGecko price history). |
| 2026-03-28 | SOPH all-time low of **$0.00796068** (CoinGecko price history). |
| 2026-06-21 | Snapshot: SOPH ~$0.00535, ~$18.5M cap (rank #859), -92% from ATH; Extreme Fear tape. |

> *Additional dated protocol milestones (mainnet, app launches) will be added as sources are ingested. Distribution via a Binance HODLer Airdrop is documented in the token's category tags.*

---

## Trading Playbook (bear / Extreme-Fear + bottoming regime)

> *Educational framing of how this asset behaves in the current regime — not advice.*

- **Regime context (2026-06-23):** market-health 29/100 (bearish), Fear & Greed 21 (Extreme Fear), long-horizon regime shifting to *Bottoming / Accumulation* with neutral on-chain health (48.5). High-beta micro-cap L2 tokens like SOPH typically underperform on the way down and overshoot on relief rallies.
- **Beta & correlation:** SOPH is a high-beta proxy for the ZK/L2 and consumer-crypto themes; it tends to amplify BTC/ETH moves. In Extreme Fear, low-float L2 tokens are sold first and bounce hardest on sentiment reversals.
- **Liquidity discipline:** with ~$18M cap and thin books, size into limits, expect [[slippage]], and avoid market orders. The Hyperliquid perp's funding rate is a useful crowd-positioning gauge.
- **Risk events:** token unlocks / continued airdrop distribution are the main idiosyncratic drawdown catalysts given MC/FDV ≈ 0.31. Map the unlock schedule before sizing.
- **Bottoming-regime stance:** accumulation theses here hinge on *real* app traction, not price alone — a chain token with no sticky flagship app can stay cheap indefinitely. Treat SOPH as a speculative call option on Sophon's consumer-app thesis, sized accordingly. See [[risk-management]] and [[position-sizing]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[zksync]]
- [[zk-rollup]]
- [[gamefi]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- General market knowledge; market data as of 2026-06-21 (cryptodataapi.com / CoinGecko). No additional specific wiki source ingested yet.
