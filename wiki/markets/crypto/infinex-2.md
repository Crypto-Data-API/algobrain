---
title: "Infinex"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [altcoins, crypto, defi]
aliases: ["INX", "Infinex Patron"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://infinex.xyz/"
related: ["[[cross-chain]]", "[[crypto-markets]]", "[[defi]]", "[[ethereum]]", "[[synthetix]]"]
---

# Infinex

**Infinex** (INX) is a unified [[defi|DeFi]] access platform — a single front-end / account ("Infinex Account") that aims to let users trade, swap, hold and interact with on-chain protocols across multiple chains without the friction of managing seed phrases, gas tokens and chain-switching directly. It was founded by **Kain Warwick**, the founder of [[synthetix|Synthetix]], and is positioned as a non-custodial alternative to centralized exchanges. It ranks **#938** by market capitalization.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

At the snapshot date INX traded at **$0.00790696** with a market cap of **$15,739,860** (rank #938), down **0.70%** over 24 hours and up **1.10%** over 7 days, against a broad risk-off backdrop (BTC ~$64,508, Fear & Greed Index 21 / "Extreme Fear").

---

## Overview

Infinex's thesis is that self-custodial DeFi remains too hard for mainstream users: people must juggle wallets, seed phrases, multiple chains, bridging and gas tokens. Infinex packages this behind a **single account and unified interface** so the user experience resembles a centralized exchange while custody stays on-chain and non-custodial. The platform aggregates access to swaps, [[defi|DeFi]] protocols and (per its category tags) perpetuals across ecosystems — drawing on liquidity and apps on [[ethereum|Ethereum]], [[bnb|BNB Chain]] and [[solana|Solana]].

### Founder and lineage

Infinex is led by **Kain Warwick**, who previously founded [[synthetix|Synthetix]], one of DeFi's early derivatives/synthetic-asset protocols. This lineage gives Infinex notable credibility and ecosystem connections within DeFi. The project gained attention through its **"Patron"** NFT / membership distribution, which seeded an engaged early community, and was featured in a Binance Alpha spotlight.

### How it works (high level)

- **Unified account** — one Infinex Account abstracts away per-chain wallets; the user signs in and interacts with multiple chains/protocols from one place.
- **[[cross-chain|Cross-chain]] access** — assets and actions span [[ethereum|Ethereum]], [[bnb|BSC]] and [[solana|Solana]] (INX has token deployments on all three).
- **Non-custodial** — the platform is an interface/account abstraction layer rather than a custodian holding user funds, distinguishing it from a centralized exchange.

> **Data caveat:** Feature scope, supported protocols and security/audit status evolve quickly. This wiki does not independently verify TVL, user counts or audit completeness — check primary sources before relying on them.

### Deep dive — the unified-account model

Infinex's core design choice is the **Infinex Account**: a smart-contract account (account abstraction) that becomes the user's single identity across chains, so the friction of per-chain EOAs, seed phrases, and gas tokens is abstracted away. The mechanics that matter:

- **Account abstraction / smart account** — the account can batch actions, sponsor gas, and enforce policies, letting the front-end feel like a CEX while custody stays on-chain.
- **Cross-chain routing** — actions span [[ethereum|Ethereum]], [[bnb|BNB Chain]] and [[solana|Solana]]; under the hood this implies bridging/messaging between ecosystems, which is the chief security surface (see Risks).
- **Aggregation layer** — Infinex aggregates swaps, DeFi protocols and (per its category tags) perps, acting as a routing/UX layer on top of existing liquidity rather than its own AMM or order-book.
- **Patron membership** — the **Patron** NFT distribution seeded the early community and access tier; it functioned as a community-bootstrapping and alignment primitive ahead of the INX token.

This is distinct from a [[wallet]] (key-management only) and from a CEX (custodial). Infinex aims for the middle: CEX-grade UX, self-custodial settlement.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | INX |
| **Market Cap Rank** | #938 |
| **Market Cap** | $15,739,860 |
| **Current Price** | $0.00790696 |
| **24h Change** | -0.70% |
| **7d Change** | +1.10% |
| **Founder** | Kain Warwick (founder of [[synthetix|Synthetix]]) |
| **Categories** | DeFi, Wallets / Access Layer, Cross-chain, Perpetuals, Ethereum / BNB Chain / Solana Ecosystem, Binance Alpha Spotlight |
| **Website** | [https://infinex.xyz/](https://infinex.xyz/) |
> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 1.99B INX |
| **Total Supply** | 10.00B INX |
| **Max Supply** | 10.00B INX |
| **Fully Diluted Valuation** | $125.37M |
| **Market Cap / FDV Ratio** | 0.20 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.0334 (2026-01-30) |
| **All-Time Low** | $0.0107 (2026-02-23) |
| **24h Change** | -0.70% |
| **7d Change** | +1.10% |

INX is a recently launched token (early 2026), so it has a short history. It currently trades well below its January 2026 all-time high and modestly above the February 2026 low, with a small positive weekly move that stands out against an "Extreme Fear" market.

---

## Token Role

| Function | Description |
|---|---|
| **Governance / ecosystem** | INX is the native token aligning Infinex users, contributors and the broader ecosystem. |
| **Incentives** | Used for rewards/incentives tied to platform usage and the Patron community. |
| **Access alignment** | Ties holders to the growth of the unified-access platform. |

Supply: ~1.99B INX circulating of a 10B max (market-cap/FDV ratio ~0.20) — a large share of supply is not yet circulating, a meaningful dilution/unlock consideration.

### Value accrual & governance

As an access-layer token, INX's value accrual is indirect: it does not, in itself, hold custody or earn protocol fees the way a venue token might unless fee-capture is explicitly routed to it. The plausible accrual channels are (a) platform fee-sharing / buybacks if Infinex monetizes swap/perp/DeFi routing flow, (b) governance over the unified-access platform's parameters and incentives, and (c) alignment incentives tying the Patron community and active users to growth. The dominant near-term reality is dilution: only ~20% of the 10B max supply circulates (MC/FDV ≈ 0.20), the lowest float ratio in this cohort, so emissions/unlocks are the heaviest structural headwind here. Governance value is contingent on the treasury and on real, fee-generating usage.

### Competitive position

Infinex straddles two competitor sets — DeFi front-ends/super-apps and centralized exchanges:

| Project | Type | Custody | Core thesis | Vs. Infinex |
|---|---|---|---|---|
| **Infinex (INX)** | Unified DeFi access account | Self-custodial | One account, CEX-like UX across ETH/BNB/SOL | Account abstraction + Patron community + [[synthetix]] lineage |
| **[[infinit\|INFINIT]]** | DeFAI super-app | Self-custodial | NL AI agents plan/execute multi-step DeFi | Infinex is UX/account-led; INFINIT is AI-agent-led |
| **Coinbase / [[base]] app** | CEX + on-chain app | Custodial + smart wallet | Mainstream onboarding | Infinex is fully non-custodial; rivals on UX/distribution |
| **MetaMask / Rabby** | Wallet | Self-custodial | Key management + dApp connectivity | Infinex aims higher: aggregated trading/DeFi, not just signing |
| **Centralized exchanges** | CEX | Custodial | Deep liquidity, fiat rails | Infinex trades custody risk for self-custody, at a liquidity/UX cost |

The decisive question is whether "CEX-grade UX with self-custody" wins enough users to overcome CEX liquidity and convenience advantages — and whether cross-chain account abstraction stays secure at scale.

---

## Platform & Chain Information

**Native Chain:** [[ethereum|Ethereum]] (with [[bnb|BNB Chain]] and [[solana|Solana]] deployments)

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xdef1b2d939edc0e4d35806c59b3166f790175afe` |
| Binance Smart Chain | `0x45f55b46689402583073ff227b6ac20520052a24` |
| Solana | `inxKXw9V2NDZE7hDijzpJaKKUb97NEPJDTCEEiYg4yY` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Kraken | INX/USD | N/A |
| KuCoin | INX/USDT | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Orca | INXKXW9V2NDZE7HDIJZPJAKKUB97NEPJDTCEEIYG4YY/EPJFWDD5AUFQSSQEM2QN1XZYBAPC8G4WEGGKZWYTDT1V | Spot |

### How & where it trades

- **Spot** — INX has CEX listings on Kraken and KuCoin, plus on-chain DEX depth (Orca on [[solana|Solana]]). Token deployments exist on Ethereum, BSC and Solana, so liquidity is split across three ecosystems — a fragmentation that thins effective depth.
- **Derivatives** — no broadly-documented major INX perp at the snapshot; exposure is mainly spot. (Note: Infinex *the platform* surfaces perps for trading other assets — that is product scope, not an INX-token derivative.)
- **Liquidity & float** — ~$15.7M cap, ~$3.98M daily volume, with the lowest float ratio in this cohort (MC/FDV ≈ 0.20). CoinGecko sentiment was 0% positive at an earlier snapshot. Expect shallow books, wide spreads, and meaningful [[slippage]]; the large uncirculated supply is the dominant overhang. See [[liquidity]].

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://infinex.xyz/](https://infinex.xyz/) |
| **Twitter** | [@infinex](https://twitter.com/infinex) |
| **Telegram** | [infinexbroadcast](https://t.me/infinexbroadcast) (2,935 members) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $3.98M |
| **Market Cap Rank** | #852 |
| **24h Range** | $0.0122 — $0.0127 |
| **CoinGecko Sentiment** | 0% positive |
| **Last Updated** | 2026-04-09 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Risks & Considerations

- **Access-layer / smart-contract risk** — as an abstraction layer over many protocols and chains, Infinex inherits the security risk of the underlying protocols plus its own account-abstraction and any bridging components; a bug in the access layer could have broad impact.
- **Large unlock overhang** — only ~20% of max supply circulates; future emissions/unlocks can pressure price.
- **New asset, short history** — launched in early 2026; limited track record and high volatility.
- **Execution risk** — the "CEX-like UX, self-custodial" promise is hard; competition spans both centralized exchanges and other DeFi front-ends/wallets.
- **Founder concentration of narrative** — credibility leans heavily on Kain Warwick / [[synthetix|Synthetix]] lineage; reputational and key-person risk apply.
- *Not investment advice — point-in-time data; micro-cap altcoin risk applies.*

---

## Narrative, Category & Catalysts

Infinex's narrative blends **DeFi UX / self-custody-as-CEX-alternative** with **founder credibility** ([[synthetix|Synthetix]]'s Kain Warwick) and a **community-distribution** story (Patron). The bull case is that a non-custodial "everything app" can win share from CEXs as users prize self-custody after repeated centralized-venue failures. Catalysts to watch:

- Verifiable usage/TVL growth and evidence the Infinex Account retains users beyond the Patron cohort.
- Fee-capture mechanics that route real revenue to INX (improving the weak accrual picture).
- New chain/protocol integrations broadening the aggregated surface.
- Continued security track record on the cross-chain account-abstraction stack.

Headwinds: extremely low float (heavy unlock overhang), a crowded field of wallets/super-apps/CEXs, key-person reliance on Warwick, and Extreme-Fear macro (F&G 21, June 2026) suppressing speculative DeFi microcaps.

---

## Major News & Events

> *Real, dated timeline.*

| Date | Event |
|---|---|
| 2026-01-30 | INX all-time high of **$0.0334** (CoinGecko price history) — early in its post-launch history. |
| 2026-02-23 | INX all-time low of **$0.0107** (CoinGecko price history). |
| 2026-06-22 | Snapshot: INX ~$0.00791, ~$15.74M cap (rank #938); -0.70% (24h), +1.10% (7d) vs. Extreme Fear tape. |

> *Infinex was founded by Kain Warwick (founder of [[synthetix|Synthetix]]); the Patron NFT distribution and Binance Alpha spotlight are documented in the page's lineage/category notes. Additional dated milestones will be added as sources are ingested.*

---

## Trading Playbook (bear / Extreme-Fear + bottoming regime)

> *Educational framing of behavior in the current regime — not advice.*

- **Regime context (2026-06-23):** market-health 29/100 (bearish), Fear & Greed 21 (Extreme Fear), long-horizon regime shifting to *Bottoming / Accumulation*. Low-float DeFi microcaps like INX are high-beta and unlock-sensitive.
- **Beta & correlation:** INX tracks DeFi/altcoin risk appetite and Synthetix-ecosystem sentiment; its small positive weekly move against a red tape reflects idiosyncratic, founder/community-driven flow more than broad strength.
- **Liquidity discipline:** with the lowest float ratio in this cohort and ~$3.98M daily volume across three chains, depth is thin — use limits, expect [[slippage]], avoid market orders.
- **Risk events:** unlocks are the dominant idiosyncratic drawdown catalyst (MC/FDV ≈ 0.20); any cross-chain/account-abstraction security incident would hit hard. Map the unlock schedule before sizing.
- **Bottoming-regime stance:** the accumulation case leans on real, fee-generating adoption of the Infinex Account, not narrative alone. Treat INX as a speculative bet on the non-custodial super-app thesis; size small and apply [[risk-management]] / [[position-sizing]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[defi]]
- [[synthetix]]
- [[cross-chain]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).
- General market knowledge; no additional specific wiki source ingested yet.
