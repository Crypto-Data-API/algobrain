---
title: "XPR Network"
type: entity
created: 2026-04-09
updated: 2026-06-21
status: excellent
tags: [crypto]
aliases: ["XPR", "Proton"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://xprnetwork.org"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[bnb]]", "[[layer-1]]", "[[proof-of-stake]]", "[[metal-blockchain]]", "[[perpetual-futures]]"]
---

# XPR Network

**XPR Network** (ticker **XPR**, formerly **Proton**) is a Layer-1 ([[layer-1|L1]]) public blockchain and smart-contract platform that uses Delegated Proof-of-Stake (DPoS) consensus. Launched in San Francisco, it is designed for consumer applications and peer-to-peer payments, built around a secure identity and financial-settlement layer that lets users link real identity and fiat accounts, on-ramp into crypto, and use it directly in apps. XPR is the native network and governance token.

---

## Market Data

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

| Field | Value |
|---|---|
| **Ticker** | XPR |
| **Current Price** | $0.00224706 |
| **Market Cap** | $64,311,820 (~$64.3M) |
| **Market Cap Rank** | #375 |
| **24h Volume** | $1,228,669 (~$1.2M) |
| **24h Change** | +0.27% |
| **7d Change** | +2.13% |
| **Fully Diluted Valuation** | ~$72.4M |
| **Market Cap / FDV** | ~0.89 |
| **All-Time High** | $0.100088 (2020-04-27), ~-97.8% |
| **All-Time Low** | $0.00054716 |

Market backdrop on this date was bearish: the [[fear-and-greed-index|Fear & Greed Index]] read **~23 ("extreme fear")** in an established bear market with [[bitcoin]] dominance near 59%. XPR was roughly flat on the day (+0.3%) but up ~2.1% over the week — relative outperformance versus many peers, the **strongest 7d return in this batch**. 24h turnover of only ~$1.2M against a ~$64.3M cap is **low** (~1.9% of cap — thin liquidity), the lowest relative volume among the six pages in this batch. XPR trades ~98% below its 2020 all-time high but ~4x its all-time low.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~28.65B XPR |
| **Total Supply** | ~32.20B XPR |
| **Max Supply** | Unlimited (uncapped) |
| **Fully Diluted Valuation** | ~$72.4M |
| **Market Cap / FDV Ratio** | ~0.89 |

Most of the supply is already circulating (MC/FDV ≈ 0.89), limiting near-term unlock overhang from the ~$8M gap to FDV. However, the **max supply is uncapped (unlimited)**, meaning long-term issuance under the DPoS model is a structural inflation consideration — XPR shares this uncapped trait with [[qtum]], in contrast to capped peers like [[metal-blockchain|METAL]] and [[zilliqa]]. XPR is used for staking, governance, and network resource allocation.

---

## How & Where It Trades

### Spot venues (centralized)

| Exchange | Pair |
|---|---|
| KuCoin | XPR/USDT |

Centralized listings are limited (KuCoin is the principal CEX pair captured), which contributes to the asset's thin liquidity profile.

### On-chain / DEX

| Exchange | Type |
|---|---|
| Uniswap V3 (Ethereum) | Spot (XPR/WETH) |

Wrapped/bridged XPR trades on [[ethereum]] (Uniswap) and [[bnb]]; native activity occurs on the XPR Network chain itself.

### Derivatives

No active [[perpetual-futures]] venue for XPR is captured in the current data snapshot, so derivatives coverage is omitted rather than assumed. Combined with low spot turnover, this means hedging and large-size execution are constrained; verify live availability before assuming any leveraged or perp liquidity.

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xd7efb00d12c2c13131fd319336fdf952525da2af` |
| BNB Smart Chain | `0x5de3939b2f811a61d830e6f52d13b066881412ab` |

---

## Technology & Consensus

XPR Network is a [[layer-1]] smart-contract chain built on the **EOSIO/Antelope** technology stack (the same lineage that the [[metal-blockchain|Metal Blockchain]] "A Chain" reuses), using **Delegated Proof-of-Stake (DPoS)**:

- **DPoS consensus:** XPR holders vote for a limited set of **block producers** who validate transactions and produce blocks. This yields high throughput and low/near-zero fees but concentrates block production among the elected set — a decentralization tradeoff versus permissionless [[proof-of-stake]] or [[proof-of-work]] chains.
- **Identity & fiat layer (WebAuth / Proton):** the chain's differentiator is a built-in **verified-identity and fiat-settlement layer** — users can link real identity and bank/fiat accounts, on-ramp into crypto, and spend it directly in apps, abstracting away seed-phrase and on-ramp friction for consumer use cases.
- **WASM smart contracts:** contracts run on a WebAssembly runtime, the Antelope standard, enabling deterministic, resource-metered execution.

---

## Use Case, Narrative & Category

XPR Network is a **[[layer-1]] smart-contract and payments platform**, not a meme. Its differentiator is a built-in identity and fiat-settlement layer: users can link verified identity and bank/fiat accounts, pull funds, buy crypto, and spend it within applications — targeting consumer payments and on-ramping rather than pure DeFi speculation. It uses Delegated [[proof-of-stake|Proof-of-Stake]] for consensus and governance. Categories include Smart Contract Platform, [[bnb|BNB Chain]] Ecosystem, [[ethereum|Ethereum]] Ecosystem, DWF Labs Portfolio, Made in USA, and Governance.

---

## Valuation Framing (Qualitative)

- **Payments-rail optionality:** the ~$64.3M cap prices a consumer-payments-and-fiat-identity thesis whose value depends on real user/merchant adoption — which has not broadly materialized. Today's price is largely an option on that adoption rather than realised transaction-fee capture.
- **Uncapped-supply discount:** unlimited max supply means rational buyers apply an inflation discount; long-run issuance can dilute holders even though near-term MC/FDV (~0.89) is high.
- **Relative-strength note:** XPR's +2.1% 7d return was the best in this batch in an extreme-fear tape — a small positive, but on ~$1.2M/day volume the move is fragile and easily reversed.
- **Thin-liquidity discount:** the lowest turnover of the six pages; the quoted price can move sharply on modest flow, which itself caps the size a disciplined buyer will deploy.

---

## Peer Comparison

| Token | Category | Price | Market Cap | Rank | MC/FDV | Max Supply |
|---|---|---|---|---|---|---|
| **XPR Network (XPR)** | DPoS [[layer-1]] payments | $0.00225 | ~$64.3M | #375 | ~0.89 | Uncapped |
| [[metal-blockchain\|Metal (METAL)]] | [[avalanche]]-fork [[layer-1]] | $0.1247 | ~$63.3M | #379 | ~0.76 | 666.67M |
| [[qtum\|Qtum (QTUM)]] | UTXO+EVM [[layer-1]] | $0.7239 | ~$76.8M | #326 | ~0.98 | Uncapped |
| [[zilliqa\|Zilliqa (ZIL)]] | Sharded [[layer-1]] | $0.00312 | ~$61.0M | #392 | ~0.93 | 21.0B |

*All figures from the 2026-06-21 snapshot. XPR shares the EOSIO/Antelope lineage and a DWF Labs portfolio tag with [[metal-blockchain|METAL]], and an uncapped-supply model with [[qtum]]. It posted the strongest 7d return but has the thinnest liquidity in the cluster.*

---

## Notable History

- Originally launched as **Proton** (rebranded to XPR Network), with roots dating to around 2020.
- All-time high of **$0.100088 (2020-04-27)**; the token now trades ~97.8% below that peak.
- All-time low near **$0.00054716**, with the asset recovering to ~4x that base.
- Associated with DWF Labs in its market-maker/portfolio relationships per categorization.

---

## Risks

XPR is an L1 infrastructure token with a distinct risk set:

- **Thin liquidity** — very low 24h turnover (~$1.2M, ~1.9% of cap) and limited CEX listings imply wide slippage and difficulty exiting size; the thinnest of the six pages in this batch.
- **Uncapped supply / inflation** — unlimited max supply means ongoing issuance can dilute holders over the long run.
- **Adoption risk** — the consumer-payments and fiat-identity thesis requires real user and merchant adoption that has not broadly materialized; competition from larger L1s and payment rails is intense.
- **Centralization considerations** — DPoS concentrates block production among a limited set of elected producers, a governance/decentralization tradeoff.
- **Regulatory risk** — fiat on-ramp and identity-linked settlement features touch regulated payment/KYC domains.
- **Macro / regime risk** — the snapshot date sat in "extreme fear" ([[fear-and-greed-index|Fear & Greed]] ~23) within an established bear market, a poor regime for low-liquidity small caps.

---

## Related

- [[ethereum]]
- [[bnb]]
- [[layer-1]]
- [[proof-of-stake]]
- [[metal-blockchain]]
- [[perpetual-futures]]
- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data snapshot 2026-06-21 (cryptodataapi.com / CoinGecko).
