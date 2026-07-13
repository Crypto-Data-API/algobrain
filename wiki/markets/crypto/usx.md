---
title: "USX (Solstice)"
type: entity
created: 2026-04-09
updated: 2026-06-21
status: excellent
tags: [crypto, defi, altcoins, stablecoin]
aliases: ["USX", "Solstice USX", "Solstice Finance"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://solstice.finance/"
related: ["[[crypto-markets]]", "[[solana]]", "[[stablecoins]]", "[[stablecoin]]", "[[usdc]]", "[[stablecoin-yields]]", "[[stablecoin-depegs]]", "[[ethena]]"]
---

# USX

**USX** is a [[solana|Solana]]-native [[stablecoin]] issued by Solstice Finance, fully collateralized 1:1 by [[usdc|USDC]] and USDT and positioned as a settlement/liquidity layer for Solana DeFi, with a yield-bearing variant (eUSX) and a native token (SLX, TGE May 2026). For traders it matters less as a directional asset (it pegs to $1) and more as Solana stablecoin infrastructure: a yield venue, a [[stablecoin-depegs|depeg-risk]] monitor, and — via SLX — a tradable claim on the protocol.

---

## Market Data

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

| Metric | Value |
|---|---|
| **Price** | $0.9993 (≈$1.00 peg) |
| **Market cap (= supply at par)** | $507.9M |
| **Market-cap rank** | #102 |
| **24h volume** | $1.67M |
| **24h / 7d change** | −0.03% / −0.01% |
| **Circulating / total supply** | 508.21M USX |
| **Max supply** | None (mint/redeem vs collateral) |
| **All-time high** | $1.038 (2026-01-28, early peg instability) |
| **All-time low** | $0.8285 (2025-12-26, early peg instability) |

Supply has grown markedly — to ~508M (≈$508M cap) from ~363M at the April 2026 snapshot — consistent with Solstice's reported TVL climb past $400M. The peg now holds near $1.00 with the wide Dec-2025/Jan-2026 swings (ATL $0.83, ATH $1.04) behind it, but those early dislocations remain a reminder of liquidity risk for a young stablecoin. Macro backdrop: "Established Bear Market", Fear & Greed ~23.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | USX |
| **Type** | Fully-collateralized USD stablecoin (USDC/USDT-backed at launch) |
| **Market Cap** | ~$508M supply (June 2026 snapshot, up from ~$363M in April); protocol TVL surpassed **$400M by 20 May 2026** ($160M at launch) |
| **Rank** | #102 among all crypto assets (June 2026 snapshot) |
| **Chain** | Solana |
| **Issuer / Backers** | Solstice Finance; backed by Deus X Capital ($1B digital-asset investment firm), with launch support from Galaxy Digital, MEV Capital, Bitcoin Suisse and Auros |
| **Native token** | SLX — TGE 25 May 2026, primary listing on BitMart; community-first distribution (points conversion) |
| **Categories** | Stablecoins, USD Stablecoin, Solana Ecosystem |
| **Website** | [https://solstice.finance/](https://solstice.finance/) |

---

## Overview

USX is a Solana-based stablecoin designed to provide a secure, efficient, and transparent digital dollar for both institutional and retail users. It is created through over-collateralization with leading stablecoins, ensuring that every USX in circulation is backed 1:1 with assets like USDT or USDC. Unlike legacy stablecoins that simply hold reserves, USX is built to integrate directly into the broader DeFi ecosystem, where it acts as a core liquidity layer for trading, lending, and payments. Its purpose is to offer a dollar-pegged asset that can move at the speed and scale of Solana while maintaining reliability for settlements and financial transactions.

The Solstice stack pairs USX with **YieldVault** / **eUSX** (institutional-grade yield strategies on the stablecoin collateral) and the **SLX** utility token, which rewards usage of USX/eUSX across Solana lending markets and liquidity pools.

---

## Mechanism & Backing

| Dimension | USX design |
|---|---|
| **Collateral** | Fully collateralized 1:1 by [[usdc|USDC]] and USDT — a stablecoin-backed stablecoin, not a fractional-reserve or algorithmic design |
| **Peg target** | $1.00; mint USX by depositing USDC/USDT, redeem by burning USX for the underlying collateral |
| **Yield variant (eUSX)** | Wrapping USX into **eUSX / YieldVault** routes the collateral into institutional-grade yield strategies, passing yield to the wrapped token — comparable in concept to [[ethena|Ethena's]] USDe/sUSDe split (see [[stablecoin-yields]]) |
| **Native token (SLX)** | Utility/incentive token; TGE 25 May 2026, primary listing on BitMart, community-first (points-conversion) distribution, no-VC framing |
| **Reserve transparency** | Backing held in USDC/USDT; transparency/attestation depth is a key open question for a young issuer (see Risks) |
| **Custody / permissioning** | DeFi-native on [[solana|Solana]]; USX itself is permissionless to hold and trade on Solana DEXs, unlike institutional [[tokenized-treasuries]] |
| **Backers** | Solstice Finance, backed by Deus X Capital ($1B digital-asset firm) with launch support from Galaxy Digital, MEV Capital, Bitcoin Suisse and Auros |

**De-peg history matters here:** USX is collateralized 1:1, but the Dec-2025 dip to $0.83 and Jan-2026 spike to $1.04 show that *backing ratio ≠ secondary-market peg* when on-chain liquidity is thin — the same lesson as [[true-usd|TUSD]] from the opposite (over-collateralized) direction.

---

## Major News & Events (2025–2026)

- **Launch (late 2025 / early 2026)** — USX and YieldVault went live with **over $160M deposited TVL**, backed by Galaxy Digital, MEV Capital, Bitcoin Suisse, Auros and Deus X Capital.
- **Jan 2026** — USX briefly traded to an ATH of $1.04 (28 Jan) after an ATL of $0.8285 (26 Dec 2025) — early peg instability worth remembering when sizing exposure.
- **20 May 2026** — protocol reported **>$400M TVL** with live revenue-generating products.
- **25 May 2026** — **SLX TGE**: points converted to SLX; BitMart primary listing; no-VC, community-first distribution model.

---

## Trading Relevance

- **Where it trades**: Solana DEXs — Orca (USX pools) and across Solana lending/liquidity venues; not a CEX-listed asset itself. SLX (the protocol token) listed on BitMart from 25 May 2026.
- **Use for traders**: (1) stablecoin-yield farming via eUSX/YieldVault ([[stablecoin-yields]]); (2) SLX incentive farming by deploying USX in Solana DeFi; (3) peg monitoring — the Dec 2025 dip to $0.83 shows early-stage liquidity risk despite 1:1 backing.
- **Narrative basket**: Solana stablecoin/yield infrastructure (comps: [[ethena|Ethena USDe]], other yield-wrapped dollars); RWA-adjacent "institutional yield on-chain".
- **Key risks**: peg/liquidity depth (24h volume only ~$1.67M at the June 2026 snapshot against ~$508M supply), reserve transparency, smart-contract risk in the vault layer.

---

## Peer Comparison — yield-bearing / DeFi-native dollars

| Product | Chain | Backing | Yield variant | Peg track record | Approx. size |
|---|---|---|---|---|---|
| **USX** | [[solana|Solana]] | 1:1 USDC/USDT | eUSX / YieldVault | Wide early swings (ATL $0.83), now ≈$1 | ~$508M (#102) |
| [[ethena|USDe]] | [[ethereum|Ethereum]] | Delta-hedged crypto + cash | sUSDe | Mostly held; funding-dependent | Large |
| [[ylds|YLDS]] | Multi | MMF-style securities | Yield distributed | Tight ±10bp | ~$575M (#93) |
| [[usdc|USDC]] / [[usdt|USDT]] | Multi | Cash + T-bills | None to holder | Very tight | #1–2 |

USX's niche is being a **Solana-native, stablecoin-collateralized dollar with a built-in yield wrapper and a community-distributed governance token** — closer in spirit to Ethena's USDe than to a plain reserve stablecoin, but younger and with a shorter peg history.

---

## Platform & Chain Information

**Native Chain:** Solana

### Contract Addresses

| Chain | Address |
|---|---|
| Solana | `6FrrzDk5mQARGc1TDYoyVnSyRdds1t4PbtohCD6p3tgG` |

---

## Exchange Listings

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Orca (Solana) | USX pools | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://solstice.finance/](https://solstice.finance/) |
| **Twitter** | [@solsticefi](https://twitter.com/solsticefi) |
| **Docs** | [https://docs.solstice.finance/](https://docs.solstice.finance/) |

---

## Risks

| Risk | Assessment |
|---|---|
| **Peg / liquidity** | Elevated for its age — thin secondary depth (24h vol ~$1.67M vs ~$508M supply); the Dec-2025 dip to $0.83 shows real dislocation risk even with 1:1 backing |
| **Reserve transparency** | Open question — backing is USDC/USDT but attestation/disclosure depth is less mature than for established issuers; inherits any [[usdc|USDC]]/USDT de-peg risk |
| **Smart-contract** | Moderate–high — collateral, mint/redeem and the eUSX/YieldVault yield layer are all on-chain code; vault strategies add complexity |
| **Yield-strategy** | eUSX yield depends on the underlying strategies performing; a strategy blow-up could impair the wrapped token |
| **Issuer / governance** | Young protocol; SLX-driven, community-first model with VC backers — governance and incentive sustainability unproven |
| **Concentration** | Single-chain (Solana) and concentrated venue support (Orca pools; SLX on BitMart) |

---

## Related

- [[solana]] — host chain
- [[stablecoins]], [[stablecoin]], [[stablecoin-yields]], [[stablecoin-depegs]], [[usdc]]
- [[ethena]] — comparable yield-dollar design on Ethereum
- [[ylds]] — regulated yield-bearing dollar
- [[crypto-markets]], [[defi]]

---

## Sources

- CoinGecko market data snapshot, 2026-04-09 (CoinGecko top-1000 ingest)
- Solstice Finance — https://solstice.finance/usx and https://solstice.finance/slx
- Unchained / Chainwire press release, "Solstice Finance Officially Launches USX, A Solana-Native Stablecoin With $160M Deposited TVL" — https://unchainedcrypto.com/press-release/solstice-finance-officially-launches-usx-a-solana-native-stablecoin-with-160m-deposited-tvl/
- TheStreet Crypto, "Solstice launches SLX token for fast-growing Solana yield ecosystem" — https://www.thestreet.com/crypto/markets/solstice-launches-slx-token-for-fast-growing-solana-yield-ecosystem
- Verified via web search, 2026-06-10: $160M launch TVL, >$400M TVL May 20 2026, SLX TGE May 25 2026 with BitMart listing, Deus X Capital backing
