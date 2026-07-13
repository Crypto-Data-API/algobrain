---
title: "Legacy Frax Dollar"
type: entity
created: 2026-04-09
updated: 2026-06-21
status: excellent
tags: [crypto, defi]
aliases: ["FRAX", "Legacy FRAX", "Frax stablecoin"]
entity_type: protocol
founded: 2020
headquarters: "Decentralized"
website: "https://frax.finance"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[frax-share]]", "[[frax-usd]]", "[[stablecoins]]", "[[ethena-usde]]", "[[stablecoin]]"]
---

# Legacy Frax Dollar

**Legacy Frax Dollar** (FRAX) is the original Frax Finance stablecoin — launched in December 2020 as the first fractional-algorithmic stablecoin — now formally deprecated. Under Frax's **North Star upgrade (completed 30 April 2025)** it was renamed "Legacy Frax Dollar" with a finalized migration path to the fully-collateralized **[[frax-usd|frxUSD]]**, while the ticker "FRAX" was reassigned to the former governance token FXS (see [[frax-share]]). Traders must understand this ticker split: "FRAX" on data sites can mean two different assets.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | FRAX (legacy stablecoin; ticker now also used by the ex-FXS gas token — check which asset a venue lists) |
| **Asset class** | USD [[stablecoin]] (deprecated/legacy; migration to [[frax-usd\|frxUSD]]) |
| **Native Chain** | [[ethereum\|Ethereum]], bridged to 14+ chains |
| **Market Cap Rank** | #149 |
| **Market Cap** | $240.05M |
| **Fully Diluted Valuation** | $240.05M |
| **Current Price** | $0.992879 |
| **24h Volume** | $0.91M |
| **24h Change** | +0.39% |
| **7d Change** | -0.04% |
| **Circulating = Total Supply** | ~241.75M FRAX |
| **All-Time High** | $1.14 (2021-02-07) |
| **All-Time Low** | $0.8745 (2023-03-11, USDC-depeg weekend) |
| **Categories** | Stablecoins, DeFi, USD Stablecoin, Multichain |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

Context: legacy FRAX trades at **$0.9929**, holding its characteristic slight wind-down discount to the dollar even as the broader market sits in an **Established Bear Market** with the Crypto [[crypto-fear-and-greed-index|Fear & Greed Index]] at **23 (extreme fear)**. As a (deprecated) stablecoin its price is peg-anchored rather than risk-on/risk-off, but supply continues to drift lower (~242M, down from ~276M in April 2026) as holders migrate to [[frax-usd|frxUSD]]. Daily volume is thin (~$0.9M), consistent with a slowly redeeming legacy asset. Note ticker confusion: the **#149-ranked "FRAX" stablecoin here** is distinct from the separate, far smaller volatile **ex-FXS "Frax" gas token** (see [[frax-share]], market cap ~$25M, rank ~#736).

---

## Overview

FRAX launched as the first fractional-algorithmic stablecoin: partially collateralized, partially stabilized algorithmically via the FXS seigniorage token, with the collateral ratio adjusting to market demand. After the 2022 algorithmic-stablecoin collapses (Terra/UST), Frax governance moved FRAX to a ~100% collateral ratio, and the protocol's stablecoin ambitions were ultimately rebuilt around **frxUSD**, a 100%-collateralized, regulation-oriented payment stablecoin (backed by cash-equivalents including tokenized treasury instruments).

### The North Star upgrade (30 April 2025)

The protocol-wide overhaul that defines this asset's current status:

- **FXS → FRAX**: the Frax Share governance token was renamed FRAX and became the gas/commodity token of the Fraxtal L2 (1:1 automatic conversion on Fraxtal; manual bridge for Ethereum holders). A wrapped ERC-20 ("WFRAX") was introduced.
- **FRAX stablecoin → Legacy Frax Dollar**: the original stablecoin (this page's asset) was renamed and given a finalized migration path to **frxUSD**.
- **frxUSD promoted** as the flagship stablecoin, positioned for compliance with U.S. payment-stablecoin legislation.
- **Tail emissions**: new-FRAX emissions set at 8%/yr, phasing down to 3% over five years.

---

## Tokenomics & Supply

| Metric | Value (2026-06-21 snapshot) |
|---|---|
| **Circulating = Total Supply** | ~241.75M FRAX |
| **Max Supply** | None (supply set by mint/redeem, now contracting via migration) |
| **Market Cap / FDV** | 1.00 (no locked/uncirculating overhang) |
| **Backing** | Collateralized (post-2023 ~100% CR); no longer fractional-algorithmic in practice |
| **ATH / ATL** | $1.14 (2021-02-07) / $0.8745 (2023-03-11, USDC-depeg weekend) |

Legacy FRAX has **circulating = total supply** (MC/FDV = 1.00), so there is no unlock/dilution overhang — the relevant supply dynamic is *contraction*, as redemptions and migration to [[frax-usd|frxUSD]] steadily retire tokens (~276M in April 2026 → ~242M by June 2026). Because backing is ~100% collateral, the token behaves as a redeemable dollar claim, not a volatile asset; its small persistent discount reflects redemption friction and migration gating rather than a backing shortfall.

---

## Trading Relevance

- **Ticker-confusion edge**: since April 2025, "FRAX" on CEXs/data aggregators may refer to the **new gas token (ex-FXS, volatile)** rather than this **legacy stablecoin (~$1)**. Mispriced feeds, wrong-asset listings, and bot errors around renames are a real, recurring source of microstructure edge — verify contract address `0x853d955acef822db058eb8505911ed77f175b99e` (Ethereum) for the legacy stablecoin.
- **Wind-down dynamics**: legacy FRAX trades at a persistent small discount (~$0.99). The migration to frxUSD is effectively a slow-motion redemption arb: discount captures are possible but gated by migration mechanics and gas; liquidity (only ~$0.9M daily volume at the 2026-06-21 snapshot) is the binding constraint.
- **Where it trades**: almost entirely DEX-based now — Uniswap v2/v3 and Curve-style stable pools on Ethereum; CEX support has rotated to frxUSD and the new FRAX token.
- **Why it still matters**: FRAX's fractional-algorithmic design is the canonical case study between fully-backed (USDC) and fully-algorithmic (UST) stablecoins — required background for evaluating any new stablecoin design, and its history (e.g. the March 2023 USDC-contagion depeg to $0.87) is a template for stablecoin-depeg trades.
- **Narrative basket**: stablecoins / regulated-stablecoin transition (GENIUS-Act era), alongside [[frax-usd]], [[ethena-usde]], and the broader [[stablecoins]] complex.

### Peer Comparison (USD stablecoins)

| Stablecoin | Design | Backing | Status | Notes |
|---|---|---|---|---|
| **Legacy FRAX** (this page) | Formerly fractional-algorithmic | ~100% collateral | Deprecated, migrating to frxUSD | Canonical hybrid case study |
| [[frax-usd\|frxUSD]] | Fully collateralized | Cash-equivalents / tokenized treasuries | Active flagship | Frax's compliance-oriented successor |
| USDC | Fully collateralized | Cash + short Treasuries | Active | Reference fully-backed peg |
| [[ethena-usde\|USDe]] | Synthetic / delta-neutral | Crypto collateral + perp hedge | Active | Yield from funding, different risk profile |
| UST (defunct) | Pure algorithmic | None (mint/burn LUNA) | Collapsed 2022 | The cautionary extreme |

FRAX historically sat **between USDC (fully backed) and UST (fully algorithmic)** as the canonical fractional-algorithmic design; post-Terra it converged toward the USDC end of the spectrum before being deprecated in favor of frxUSD.

---

## Valuation Framing (qualitative)

A deprecated, ~100%-collateralized stablecoin has **no equity-style valuation** — its "fair value" is $1.00 minus redemption friction. The investable angles are narrow: (1) **redemption/migration arbitrage** capturing the persistent ~70bps discount, capped by thin liquidity and migration gating; and (2) **depeg-tail trades** using FRAX's documented March 2023 contagion depeg to $0.87 as a template for stress events. The token is far more valuable as a **case study and risk template** for evaluating new stablecoin designs than as a directional holding.

### Contract Addresses (legacy stablecoin)

| Chain | Address |
|---|---|
| Ethereum | `0x853d955acef822db058eb8505911ed77f175b99e` |
| Arbitrum One | `0x17fc002b466eec40dae837fc4be5c67993ddbd6f` |
| Optimism | `0x2e3d870790dc77a83dd1d18184acc7439a53f475` |
| Polygon PoS | `0x45c32fa6df82ead1e2ef74d17b76547eddfaff89` |
| Avalanche | `0xd24c2ad096400b6fbcd2ad8b24e7acbc21a1da64` |
| BNB Chain | `0x90c97f71e18723b0cf0dfa30ee176ab653e89f40` |
| Fantom | `0xdc301622e621166bd8e82f2ca0a26c13ad0be355` |
| Polygon zkEVM | `0xff8544fed5379d9ffa8d47a74ce6b91e632ac44d` |
| Moonbeam | `0x322e86852e492a7ee17f28a78c663da38fb33bfb` |
| Moonriver | `0x1a93b23281cc1cde4c4741353f3064709a16197d` |
| Boba | `0x7562f525106f5d54e891e005867bf489b5988cd9` |
| Aurora | `0xe4b9e004389d91e4134a28f19bd833cba1d994b6` |
| Evmos | `0xe03494d0033687543a80c9b1ca7d6237f2ea8bd8` |
| Harmony Shard 0 | `0xfa7191d292d5633f702b0bd7e3e3bccc0e633200` |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://frax.finance](https://frax.finance) |
| **Twitter** | [@fraxfinance](https://twitter.com/fraxfinance) |
| **Telegram** | [fraxfinance](https://t.me/fraxfinance) |
| **Governance** | [https://gov.frax.finance](https://gov.frax.finance) |
| **GitHub** | [https://github.com/fraxfinance](https://github.com/fraxfinance) |

---

## Related

- [[frax-usd]] — frxUSD, the successor stablecoin
- [[frax-share]] — FXS, renamed to FRAX (gas token) in the North Star upgrade
- [[stablecoins]]
- [[ethena-usde]]
- [[ethereum]]
- [[crypto-markets]]

---

## Sources

- CoinGecko April 2026 snapshot (Source: [[coingecko-top-1000-2026-04-09]])
- Frax Governance — "Frax North Star Proposal V1.0": https://gov.frax.finance/t/frax-north-star-proposal-v1-0/3628
- Outposts — "Frax Share (FXS) Rebrands to Frax (FRAX) in North Star Upgrade": https://outposts.io/article/frax-announces-north-star-upgrade-fxs-to-become-gas-token-d071d48b-c584-4a96-97f3-ef6a72855fb2
- PANews — "Frax Finance will undergo North Star upgrade, Frax Share will be renamed Frax and used as gas token": https://www.panewslab.com/en/articledetails/58wra3du.html
- Messari — FRAX (legacy) project page: https://messari.io/project/frax-legacy
- Verified via web search, 2026-06-10
