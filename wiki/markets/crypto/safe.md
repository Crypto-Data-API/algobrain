---
title: "Safe"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto]
aliases: ["Gnosis Safe", "SAFE", "Safe{Wallet}"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://safe.global/"
related: ["[[account-abstraction]]", "[[ai-agents]]", "[[crypto-markets]]", "[[ethereum]]", "[[gnosis]]", "[[multisig]]", "[[self-custody]]", "[[smart-contract-wallets]]"]
---

# Safe

**Safe** (ticker **SAFE**) is the governance token of Safe (formerly [[gnosis|Gnosis]] Safe), the [[smart-contract-wallets|smart-account]] / [[multisig|multisignature]] infrastructure that secures a large share of on-chain assets across [[ethereum|Ethereum]] and EVM-compatible chains. Safe{Wallet} is the industry-standard multisig wallet, and Safe{Core} is its [[account-abstraction|account-abstraction]] stack used by 200+ projects. SAFE is an [[ethereum|Ethereum]] ERC-20 token used for protocol governance via SafeDAO.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | SAFE |
| **Chain / Ecosystem** | [[ethereum|Ethereum]] ERC-20 (governance token of SafeDAO) |
| **Current Price** | $0.09028 |
| **Market Cap** | $67,730,538 |
| **Market Cap Rank** | #361 |
| **24h Volume** | $2,150,016 |
| **24h Change** | +5.55% |
| **7d Change** | -3.59% |
| **Fully Diluted Valuation** | $90,328,730 |
| **All-Time High** | $3.56 (2024-04-23) — now ~-97% below ATH |
| **All-Time Low** | $0.083875 (2026-06-19) |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

Context: the broader market backdrop on 2026-06-21 is an **Established Bear Market** with the [[fear-and-greed-index|Crypto Fear & Greed Index]] at **23 (extreme fear)**. SAFE printed a **fresh all-time low of $0.0839 just two days earlier (2026-06-19)** and is bouncing +5.55% on the day off that low, though still down ~3.6% on the week. It trades ~97% below its April 2024 ATH ($3.56) — a stark illustration of how punishing "infra governance token" price action has been despite the underlying protocol's dominance.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~749.82M SAFE |
| **Total Supply** | 1.00B SAFE |
| **Max Supply** | 1.00B SAFE |
| **Fully Diluted Valuation** | ~$90.33M |
| **Market Cap / FDV Ratio** | ~0.75 |

SAFE has a hard-capped 1 billion token supply. The token was distributed to SafeDAO with allocations to the community (including a retroactive airdrop to historical Safe users), core contributors, the foundation/treasury, and ecosystem partners. With roughly three-quarters of the supply circulating, the MC/FDV ratio of ~0.75 implies ~250M SAFE (~25% of cap) of remaining vesting/unlock overhang to be aware of — meaningful but more contained than the deep-overhang AI/DePIN cohort (e.g. [[allora|ALLO]] ~0.30, [[doublezero|2Z]] ~0.35). SAFE confers voting rights in **SafeDAO** governance over treasury, grants, and protocol direction; it does **not** directly capture protocol fees, which is the central tension in its valuation (see below).

---

## How & Where It Trades

**Centralized exchanges (spot):**

| Exchange | Pair |
|---|---|
| Kraken | SAFE/USD |
| Upbit | SAFE/KRW |
| Bitget | SAFE/USDT |
| KuCoin | SAFE/USDT |
| Crypto.com Exchange | SAFE/USD |

**Decentralized exchanges:** Uniswap V3 on [[ethereum|Ethereum]] (SAFE/WETH), plus Gnosis Chain pools.

**Derivatives:** SAFE is a relatively small-cap token; perpetual futures coverage is limited and inconsistent across venues. It is not a core listing on most major derivatives books, and no deep, persistent Hyperliquid perp / funding / open-interest market is established for SAFE. Most price discovery and liquidity is concentrated in spot venues (Kraken, Upbit, Bitget) and the on-chain Uniswap pool. Thin 24h volume (~$1.5M) means slippage and spread risk on larger orders.

---

## Use Case, Narrative & Category

Safe sits in the **smart-account / multisig infrastructure** category. Its products:

- **Safe{Wallet}** — the benchmark multisig wallet for DAOs, funds, treasuries, and high-value individuals (used by Vitalik Buterin and others), and by web2 entities for self-custody of assets and NFTs.
- **Safe{Core}** — an account-abstraction stack (SDK + protocol) enabling gasless transactions, social-recovery, batched transactions, and passkey/Face-ID-style logins. It underpins consumer apps like Gnosis Pay and integrations across 200+ projects, deployed across 15+ networks.

The narrative ties Safe to the broader [[account-abstraction]] thesis: making every [[ethereum|Ethereum]] account a programmable smart account, unlocking DeFi, payments, gaming, and [[ai-agents|AI-agent]] custody. As of 2023 disclosures, 8M+ Safe accounts had been created with 40M+ transactions, securing tens of billions in assets at peak. SAFE itself captures value through governance rather than direct fee accrual, a recurring critique of "infra governance tokens." A live debate within SafeDAO is whether to activate fee switches or value-accrual mechanisms so that the token captures some of the economic activity its infrastructure secures.

---

## Peer Comparison

SAFE is the dominant smart-account / [[multisig|multisig]] infrastructure token, but as a *governance-only* asset it competes more for the "infra value-accrual" debate than for a single product market:

| Token / Asset | Category | Value capture | Note |
|---|---|---|---|
| **Safe (SAFE)** | [[smart-contract-wallets\|Smart-account]] / multisig | Governance only (no direct fees) | Industry-standard multisig; ~97% off ATH |
| [[account-abstraction\|ERC-4337 stack]] | Bundlers / paymasters | Varies (often no token) | Native AA competition to Safe{Core} |
| Other wallet SDKs | Embedded / MPC wallets | Often equity, not token | Compete for the same integrator demand |

Safe's moat is **incumbency and battle-testedness**: its core contracts have secured tens of billions for years with no critical multisig exploit, and 200+ projects depend on Safe{Core}. The risk is that this dominance lives in the *protocol*, not necessarily the *token* — a classic disconnect for governance-only infrastructure assets.

---

## Valuation Framing (qualitative)

SAFE is the textbook case of the **"great protocol, hard-to-value token"** problem. The infrastructure is arguably the most important multisig/smart-account standard in crypto, securing enormous value — yet the token accrues no direct cash flow and trades ~97% below its ATH at a fresh all-time low. Bull case: SafeDAO activates value accrual (fee switch / treasury productivity), and the [[account-abstraction]] + AI-agent-custody wave drives so much usage that governance over that infrastructure becomes genuinely valuable. Bear case: SAFE remains a pure governance token whose price is decoupled from the protocol's success, drifting with mid-cap alt beta. The key catalyst to watch is any **SafeDAO value-capture proposal**; absent that, fundamentals and price stay disconnected. Framing only, not advice.

---

## Notable History

- **2018** — Gnosis Safe contracts deployed on [[ethereum|Ethereum]]; battle-tested and repeatedly audited/formally verified, with no critical contract exploit in the core multisig.
- **2022** — Rebrand from Gnosis Safe to **Safe**, spinning out from [[gnosis|Gnosis]] into an independent organization (Safe Ecosystem Foundation / Core Contributors).
- **2024** — SAFE governance token reaches all-time high of **$3.56** (23 April 2024), per CoinGecko.
- **2025** — Safe infrastructure was implicated as the attack surface in the high-profile Bybit cold-wallet breach (the compromise targeted the signing UI / front-end flow, not the audited contracts), prompting Safe to harden its front-end and transaction-verification tooling.
- **2026-06-19** — SAFE prints a fresh **all-time low of $0.0839** during the established bear market, ~97% below its 2024 ATH; it bounces modestly in the days after.

---

## Risks

- **Governance-token value capture** — SAFE provides voting power but limited direct fee/cash-flow accrual, a common weakness for infrastructure tokens.
- **Supply overhang** — ~25% of supply not yet circulating; future unlocks can pressure price.
- **Liquidity** — thin volume (~$2.2M/24h) relative to market cap; large trades face slippage.
- **Front-end / operational risk** — the Bybit incident showed that the broader Safe stack (UI, signer workflow) is a target even when contracts are sound.
- **Macro / regime** — trading at fresh all-time lows during an Established Bear Market ([[fear-and-greed-index|Fear & Greed]] 23); mid-cap alts are highly sensitive to risk-off conditions.
- **Competition** — competing smart-account / AA stacks (e.g. native ERC-4337 bundlers, other wallet SDKs) could erode Safe's standard-setting position.

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[smart-contract-wallets]]
- [[account-abstraction]]
- [[multisig]]
- [[self-custody]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- General market knowledge; no specific wiki source ingested yet.

