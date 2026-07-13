---
title: "GHO"
type: entity
created: 2026-04-09
updated: 2026-06-20
status: excellent
tags: [crypto, defi, ethereum]
aliases: ["GHO", "Aave GHO", "sGHO"]
entity_type: protocol
founded: 2023
headquarters: "Decentralized (Aave DAO governance)"
website: "https://gho.xyz/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[aave]]", "[[stablecoins]]", "[[stablecoin-yields]]"]
---

# GHO

**GHO** (ticker **GHO**, native to [[ethereum|Ethereum]]) is [[aave|Aave]]'s decentralized, overcollateralized USD [[stablecoin]], launched on Ethereum mainnet in July 2023 and minted against collateral supplied to Aave markets, with interest paid by minters flowing to the Aave DAO treasury. For traders, GHO matters less as a directional asset than as DeFi plumbing: its borrow rate is set by Aave governance (a policy lever, not a market rate), its peg behavior signals Aave-ecosystem stress, and its **sGHO** savings wrapper anchors the DeFi stablecoin yield curve.

---

## Market Data

| Metric | Value |
|---|---|
| **Market Cap Rank** | #91 |
| **Market Cap** | ~$598.1M |
| **Current Price** | $0.99848 |
| **24h Volume** | ~$3.71M |
| **24h Change** | +0.01% |
| **7d Change** | -0.06% |
| **Circulating Supply** | ~599.0M GHO |
| **Max Supply** | Unlimited (governance-capped via facilitator buckets) |
| **All-Time High** | $1.03 (2024-02-28) — **-3.05%** |
| **All-Time Low** | $0.91707 (2023-10-24) — **+8.88%** |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

GHO holds its **soft peg** tightly at ~$0.998 (within ~0.15% of $1), consistent with the tight ±0.1–0.3% peg behavior seen since the 2023 depeg phase resolved. Supply has grown to **~$598M**, up from ~$584M at the April 2026 snapshot — continued, steady expansion of Aave borrowing demand. Against the **Fear & Greed = 23 / "Established Bear Market"** macro backdrop (2026-06-20), GHO's stability is the point: it is a cash/yield leg, not a beta trade. See [[market-regime]].

---

## Technology / Protocol

GHO is the native stablecoin of the [[aave|Aave Protocol]]. Unlike fiat-backed stablecoins ([[tether|USDT]], USDC), GHO is **created when users borrow it against overcollateralized positions on Aave**, and all interest paid on GHO debt accrues to the Aave DAO rather than to suppliers.

- **Facilitators** — governance-whitelisted contracts (e.g., the Aave V3 Ethereum market, the Flash Minter) that can each mint up to a **bucket cap**, giving the DAO direct, granular control over supply growth.
- **Governance-set borrow rate** — the GHO borrow APR is a *policy lever* set by Aave governance, not a market-cleared rate. This lets the DAO steer GHO supply and peg.
- **Mint/burn** — GHO is minted on borrow and **burned on repayment**, keeping supply tied to outstanding Aave debt.
- **Cross-chain** — GHO moves across chains via **Chainlink CCIP**.

GHO traded persistently below $1 in its first months (ATL $0.917, Oct 2023) until incentive and rate adjustments restored the peg in early 2024 — a useful case study in how decentralized stablecoins establish peg credibility.

---

## Peg Mechanism, Collateral & De-Peg Risk

- **Peg type** — soft peg to USD, defended by an **arbitrage-and-rate model** rather than a hard redemption window. When GHO trades **below $1**, borrowers are incentivized to repay (buy GHO cheap, burn at $1 of debt); when **above $1**, minting/selling is profitable. Aave governance backstops this by adjusting the borrow rate.
- **Collateral / backing** — **overcollateralized** by the basket of assets supplied to Aave (ETH, stETH, wBTC, stablecoins, etc.), each with its own loan-to-value and liquidation threshold. GHO is therefore as safe as the underlying Aave collateral and liquidation engine.
- **De-peg / redemption risk** — there is **no 1:1 fiat redemption**; the peg relies on arbitrage and governance. Risks: (1) a sharp drawdown in volatile collateral triggering a **liquidation cascade** in an Aave-wide event; (2) governance setting the borrow rate too low, weakening the repay-arbitrage and dragging GHO below peg (the 2023 dynamic); (3) smart-contract / oracle failure. See [[stablecoin-depegs]], [[stablecoin-depeg-history]].

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~599.0M GHO |
| **Total Supply** | ~599.0M GHO |
| **Max Supply** | Unlimited (capped per-facilitator) |
| **Fully Diluted Valuation** | ~$598.1M |
| **Market Cap / FDV Ratio** | 1.00 |

Supply is **demand-elastic, not pre-minted** — every GHO is matched by Aave debt, and the DAO caps growth via facilitator buckets. **No dilution risk** in the equity sense (MC = FDV); the relevant gauge is supply *growth*, which tracks Aave borrowing appetite. GHO crossed $500M in 2025, reached ~580M+ by March 2026, and stands at ~$598M as of June 2026; holder count grew ~300% from January 2025 to ~23,000.

---

## 2025–2026 Developments

- **Multi-chain expansion** — Avalanche (2025-06-27), Gnosis Chain (2025-08-07), Ink via Chainlink CCIP (2025-10-02), plus Base — extending GHO from its earlier Ethereum + Arbitrum footprint.
- **sGHO launch (July 2025)** — Savings GHO, a yield-bearing vault with **no lockup and instant withdrawals**, paying roughly **5–7% APY** funded by protocol revenue; available on Arbitrum, Base and Gnosis. sGHO anchors the DeFi stablecoin yield curve and competes with sUSDS (Sky) and sUSDe.
- **Supply growth** — crossed $500M, ~580M+ by March 2026, ~$598M by June 2026.
- **Peg** — tight (±0.1–0.3%) through 2025–2026, a marked improvement over the 2023 depeg phase.

---

## Market Structure & Trading Relevance

- **Not a directional trade** — GHO is a peg asset. The tradeable angles are: (1) **peg-deviation arbitrage** on Curve/Uniswap/Balancer pools when GHO drifts a few bps from $1 (see [[stablecoin-pair-arbitrage]]); (2) **carry** — borrowing GHO at the governance-set rate when it sits below market stablecoin rates is a structural funding trade; (3) **sGHO yield** as a benchmark leg in [[stablecoin-yield]] strategies.
- **Signal value** — GHO supply growth tracks Aave borrowing demand and DeFi leverage appetite, a useful on-chain risk-appetite indicator alongside total [[stablecoin-supply]].
- **Venues** — overwhelmingly **DEX-traded** (Balancer V2, Uniswap V3, Curve); minimal CEX presence (Bitget GHO/USDT). **No meaningful perp market** — directional Aave exposure is via the **AAVE token** instead.

### Exchange Listings

| Venue | Pair | Type |
|---|---|---|
| Balancer V2 (Ethereum) | GHO/USDC | Spot (DEX) |
| Uniswap V3 (Ethereum) | GHO/USDC | Spot (DEX) |
| Curve (Ethereum) | GHO stable pools | Spot (DEX) |
| Bitget | GHO/USDT | Spot (CEX) |

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x40d16fc0246ad3160ccc09b8d0d3a2cd28ae6c2f` |
| Arbitrum One | `0x7dff72693f6a4149b17e7c6314655f6a9f7c8b33` |
| Base | `0x6bb7a212910682dcfdbd5bcbb3e28fb4e8da10ee` |
| Gnosis (xDai) | `0xfc421ad3c883bf9e7c4f42de845c4e4405799e73` |
| Avalanche | `0xfc421ad3c883bf9e7c4f42de845c4e4405799e73` |
| Ink | `0xfc421ad3c883bf9e7c4f42de845c4e4405799e73` |
| Plasma | `0xb77e872a68c62cfc0dfb02c067ecc3da23b4bbf3` |

---

## Narrative & Category

GHO is a **DeFi-native, decentralized, overcollateralized stablecoin** — the same category as Sky's [[usds|USDS]]/[[dai|DAI]] and Usual's [[usual-usd|USD0]], and a contrast to fiat-backed [[tether|USDT]]/USDC and the political/fiat-backed [[usd1-wlfi|USD1]]. Its strategic role is to (1) capture interest revenue for the Aave DAO that previously leaked to external stablecoin issuers, and (2) give Aave a controllable monetary lever. The narrative is "Aave's own dollar," and its health is read as a proxy for Aave-ecosystem strength.

---

## Valuation Framing (qualitative)

As a peg asset, GHO itself is not "valued" — the relevant valuation lens is on **AAVE**, which captures GHO's economics (borrow interest to the treasury, the GHO buyback/discount programs for stkAAVE holders). Frame GHO via: GHO supply and its growth rate, the spread between the GHO borrow rate and market stablecoin rates (carry attractiveness), sGHO APY vs sUSDS/sUSDe (yield competitiveness), and peg tightness. Rising GHO supply at a stable peg is a bullish read-through for AAVE.

---

## Peer Comparison

| Stablecoin | Model | Backing | Mkt Cap (rank) | Yield wrapper |
|---|---|---|---|---|
| **GHO** | Decentralized, overcollateralized | Aave collateral (ETH/stables/etc.) | ~$598M (#91) | sGHO (~5–7%) |
| [[usds\|USDS]] | Decentralized + RWA | Crypto + treasuries (Sky) | ~$10.3B (#12) | sUSDS (SSR) |
| [[dai\|DAI]] | Decentralized, overcollateralized | Crypto + RWA (Sky legacy) | large | DSR (legacy) |
| [[usual-usd\|USD0]] | RWA-backed | Tokenized T-bills | mid-cap | USD0++ |
| [[tether\|USDT]] / USDC | Fiat-backed (centralized) | Cash + T-bills | huge | none native |

> *Peer market caps point-in-time (2026-06-20 where shown); others are category context.*

---

## Risks

- **Smart-contract risk** — bugs in GHO core, facilitators, or sGHO vaults.
- **Governance rate-setting risk** — a mis-set borrow rate can pull GHO off peg (the 2023 dynamic) or stall supply.
- **Collateral-cascade risk** — an Aave-wide liquidation event in a sharp drawdown could stress the peg.
- **Oracle / CCIP risk** — cross-chain GHO depends on Chainlink CCIP integrity.
- **Competitive yield drift** — if sUSDS/sUSDe out-yield sGHO, GHO loses savings deposits and supply momentum.
- **Regulatory** — evolving US/EU treatment of decentralized stablecoin issuers (see [[usds]], [[usd1-wlfi]] for the fiat-backed contrast under the GENIUS Act).

> *This page is informational, not investment advice. As a stablecoin, deviations from $1 are the signal to watch.*

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 264 |
| **GitHub Forks** | 119 |
| **Pull Requests Merged** | 239 |
| **Contributors** | 24 |
| **Repo** | [aave/gho-core](https://github.com/aave/gho-core) |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://gho.xyz/](https://gho.xyz/) |
| **Twitter** | [@GHOAave](https://twitter.com/GHOAave) |
| **Telegram** | [Aavesome](https://t.me/Aavesome) (~17,688 members) |
| **Whitepaper** | [GHO Technical Paper](https://github.com/aave/gho-core/blob/main/techpaper/GHO_Technical_Paper.pdf) |

---

## Related

- [[crypto-markets]]
- [[ethereum]]
- [[aave]]
- [[stablecoins]], [[stablecoin-yields]], [[stablecoin-supply]]
- [[stablecoin-pair-arbitrage]], [[stablecoin-yield]]
- [[stablecoin-depegs]], [[stablecoin-depeg-history]]
- [[usds]], [[dai]] — Sky's decentralized stablecoins
- [[usual-usd|Usual USD (USD0)]] — competing DeFi-native stablecoin
- [[tether]] — fiat-backed contrast

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]]) — April 2026 market snapshot
- Market data 2026-06-20 from `raw/data/crypto-loop/coingecko-markets.json` (cryptodataapi.com / CoinGecko); macro backdrop from `raw/data/crypto-loop/_digest.md`.
- Aave GHO documentation — https://aave.com/help/gho-stablecoin/gho
- GHO Technical Paper — https://github.com/aave/gho-core/blob/main/techpaper/GHO_Technical_Paper.pdf
- The Defiant: "Aave's GHO Stablecoin Supply Hits $500M" — https://thedefiant.io/news/defi/aave-gho-stablecoin-market-cap-breaks-usd500-million
- Messari GHO project page — https://messari.io/project/gho
- Verified via Perplexity (sonar) + web search, 2026-06-10
