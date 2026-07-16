---
title: "Sky"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, ethereum]
aliases: ["MakerDAO", "SKY", "Sky Ecosystem", "Sky Protocol"]
entity_type: protocol
founded: 2014
headquarters: "Decentralized (DAO; founded as MakerDAO by Rune Christensen)"
website: "https://sky.money/"
related: ["[[aave]]", "[[crypto-markets]]", "[[decentralized-exchange]]", "[[ethena]]", "[[ethereum]]", "[[hyperliquid]]", "[[real-world-assets]]", "[[stablecoin-yields]]", "[[stablecoins]]", "[[uniswap]]"]
---

# Sky

**Sky** (SKY) is the governance and staking token of Sky Protocol — the 2024 rebrand of **MakerDAO**, DeFi's original decentralized stablecoin issuer (DAI, est. 2017). Sky issues the **USDS** stablecoin (which grew ~86% in 2025 to $9.86B and peaked near **$12B in April 2026**), pays a Sky Savings Rate on sUSDS, and runs an aggressive **SKY buyback program** (~$114.5M spent, ~1.83B SKY removed by early 2026). Market cap **$1.359B, rank #57 (2026-06-20)** — the flagship of the "fee-revenue + buyback" DeFi basket alongside [[uniswap|UNI]] and [[aave|AAVE]].

---

## Market Data

| Metric | Value (2026-06-20) |
|---|---|
| **Price** | $0.058353 |
| **Market Cap** | $1.359B |
| **Market Cap Rank** | #57 |
| **24h Volume** | $9.93M |
| **24h Change** | -0.79% |
| **7d Change** | +3.27% |
| **Circulating Supply** | 23.29B SKY |
| **Total Supply** | 23.46B SKY |
| **Max Supply** | 23.46B SKY |
| **Fully Diluted Valuation** | $1.369B |
| **MC / FDV** | 0.99 |
| **All-Time High** | $0.100535 (2024-12-04) — now ~-42.0% |
| **All-Time Low** | $0.03582727 — now ~+63% above ATL |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

SKY is the best-positioned of the six relative to its own history: at ~-42% from ATH it has by far the **shallowest drawdown** of the peer set (most are down 88–96%), reflecting the buyback + real-yield bid. The +3.27% week is modest but in the green against a tape in **extreme fear** (Fear & Greed = 23, "Established Bear Market"). MC/FDV is 0.99 (essentially fully circulating). The standout caution is **liquidity**: 24h volume is just ~$9.93M against a $1.359B cap (turnover ~0.007) — the thinnest of the six, so large orders move price and exits can be costly.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | SKY (1 MKR converted to 24,000 SKY in the 2024–2025 migration) |
| **Type** | DeFi governance/staking token; stablecoin issuer (USDS, plus legacy DAI) |
| **Market Cap** | $1.359B, rank #57 (2026-06-20) |
| **USDS supply** | $9.86B (end-2025, +86% YTD); ATH ~$12B (April 2026); Sky Frontier Foundation projects ~$20.6B for 2026 |
| **Buybacks** | ~$114.5M USDS spent, ~1.83B SKY bought back (through Q1 2026); pace cut from 300K to 37.6K USDS/day on 2026-03-14 |
| **Sub-DAO** | Spark (SPK) — lending/yield "Star", token launched June 2025 (10B genesis supply) |
| **Categories** | DeFi, Stablecoin Issuer, Governance, Ethereum Ecosystem |
| **Website** | [https://sky.money/](https://sky.money/) |

---

## Overview

SKY is the governance token ("digital voting share") of Sky Protocol, launched in 2024 as the rebrand and upgrade of the Maker Protocol. The system centers on **USDS**, a decentralized dollar-pegged stablecoin (the successor to DAI, which still circulates), run entirely by smart contracts and SKY-holder governance — there is no CEO or traditional corporate core.

SKY's two core utilities: **governance voting** on all major system changes, and **staking** in the Staking Engine to secure the system, earn rewards, and unlock USDS borrowing against staked SKY. SkyLink bridges user funds across chains (Ethereum, Solana, Base, Arbitrum and more).

### The Endgame / Star architecture

Rune Christensen's "Endgame" plan reorganized Maker into Sky plus semi-autonomous sub-DAOs ("Stars"). The first, **Spark** (SparkLend, sUSDS yield routing, tokenized-asset allocations), launched its **SPK token in June 2025** with 10B minted at genesis, partly airdropped to the Sky ecosystem; Spark runs its own buybacks and grants (e.g., Feb–Mar 2026 spells).

---

## Protocol & Technology

Sky is a **decentralized stablecoin issuer** governed entirely by smart contracts and SKY-holder votes — there is no CEO or corporate core.

| Component | What it is | Why it matters |
|---|---|---|
| **USDS** | The flagship USD-pegged decentralized stablecoin (successor to DAI, which still circulates) | The revenue engine; minted against crypto + RWA collateral |
| **DAI** | The original Maker stablecoin; convertible 1:1 to/from USDS | Legacy supply; USDS is the forward-facing brand |
| **SKY** | Governance + staking token (1 MKR = 24,000 SKY) | Votes on all system params; staked in the Staking Engine for rewards + USDS borrowing |
| **Sky Savings Rate (SSR) / sUSDS** | Native yield on USDS via sUSDS | Demand driver for USDS; competes with Fed funds and other [[stablecoin-yields\|stablecoin yields]] |
| **Staking Engine** | Stake SKY to earn rewards and borrow USDS against staked SKY | Core SKY utility; locks supply |
| **SkyLink** | Cross-chain bridge for user funds | Extends USDS/SKY to [[ethereum\|Ethereum]], Solana, Base, [[arbitrum\|Arbitrum]] and more |
| **Stars (sub-DAOs)** | Semi-autonomous units (first: **Spark/SPK**) with their own tokens, buybacks, and mandates | The "Endgame" scaling model; each Star can grow independently |

### How Sky makes money (and burns SKY)

USDS is **overcollateralized**: borrowers lock crypto or RWA collateral and mint USDS, paying a **stability fee**. Sky also earns yield on its **RWA reserves** (primarily short-dated US T-bills). The net surplus — stability fees + RWA income minus the Sky Savings Rate paid to sUSDS holders and operating costs — is **protocol revenue**. A Smart Burn–style engine routes surplus into **SKY buybacks** (~$114.5M cumulatively, ~1.83B SKY removed by early 2026), making SKY net-deflationary while buybacks exceed emissions. Crucially, much of the revenue is **rate-sensitive**: lower Fed rates compress T-bill income, the single largest macro swing factor for Sky's earnings.

### Stablecoin peg mechanics

USDS holds its peg via overcollateralization, arbitrage (mint/redeem against collateral), and the Peg Stability Module (1:1 swaps with reserve stablecoins). Unlike [[ethena|Ethena's]] funding-rate-dependent USDe, USDS's stability comes from collateral and reserves rather than a derivatives hedge.

### 2025–2026 developments

- **USDS growth**: +86% YTD 2025 to **$9.86B**; peaked ~**$12B in April 2026** — battling Ethena's USDe for the #3 stablecoin slot behind USDT/USDC. Growth driven by the Sky Savings Rate (sUSDS) and Spark distribution.
- **Buybacks**: the Smart Burn–style engine routed surplus protocol revenue (T-bill RWA income + stability fees) into SKY buybacks — **~$114.5M cumulatively, removing ~1.83B SKY** from circulation.
- **2026-03-05** — governance vote **cut SKY emissions** (slowing new token creation); SKY jumped ~10% on the day as buybacks + lower issuance flipped net supply trajectory.
- **2026-03-14** — buyback pace temporarily reduced from 300,000 to 37,600 USDS/day (capital reprioritization), showing buyback intensity is a governance lever, not a constant.
- MKR→SKY migration was completed with governance deadlines and penalties through 2025, making SKY the sole governance asset.

---

## Trading Relevance

- **Where it trades**: spot on Binance (SKY/USDT), Kraken, Upbit (KRW), Bitget, KuCoin, Crypto.com; perps on [[hyperliquid|Hyperliquid]] (SKY-PERP); on-chain via Uniswap v2/v3 (SKY/WETH, USDS/SKY).
- **Narrative basket**: core **"real yield / buyback" DeFi basket** with [[uniswap|UNI]] (post-UNIfication burns) and AAVE — tokens whose protocols convert revenue into supply reduction. SKY is also a **stablecoin-supply proxy**: USDS growth ≈ revenue growth ≈ buyback capacity.
- **Key dashboards/signals**: USDS/DAI total supply, Sky Savings Rate vs Fed funds (carry competitiveness), monthly buyback spend, emissions schedule votes, Spark TVL/SPK actions.
- **Catalysts**: emission cuts (Mar 2026 vote was the template), USDS hitting new supply highs, further Star launches/airdrops, rate cuts (lower T-bill income compresses revenue — a negative), GENIUS-Act-era competition from regulated stablecoins.
- **Risks**: governance complexity/centralized influence of the founder, RWA counterparty exposure in reserves, DAI/USDS cannibalization, and stablecoin regulatory pressure on decentralized issuers.

---

## Tokenomics & Supply

*(supply shrinking via buybacks; emissions cut 2026-03-05)*

| Metric | Value (2026-06-20) |
|---|---|
| **Circulating Supply** | 23.29B SKY |
| **Total Supply** | 23.46B SKY |
| **Max Supply** | 23.46B SKY (net deflationary while buybacks > emissions) |
| **Fully Diluted Valuation** | $1.369B |
| **Market Cap / FDV Ratio** | 0.99 |

**Dilution flag (LOW).** MC/FDV is 0.99 — essentially fully circulating, no unlock-cliff overhang. SKY's supply is governed by two opposing levers: a (now reduced) emission schedule for staking rewards, and the **buyback engine** that retires SKY. The 2026-03-05 governance vote **cut emissions**, and combined with buybacks flipped the net supply trajectory toward deflation — SKY jumped ~10% on the day. Caveat: buyback intensity is a **governance lever, not a constant** — the pace was cut from 300,000 to 37,600 USDS/day on 2026-03-14, so the deflation is conditional on continued surplus and DAO will.

---

## Price History

| Metric | Value (2026-06-20) |
|---|---|
| **Price** | $0.058353 |
| **All-Time High** | $0.100535 (2024-12-04) — now ~-42.0% (shallowest drawdown of the peer set) |
| **All-Time Low** | $0.03582727 — price ~+63% above ATL |
| **7d Change** | +3.27% |
| **Notable move** | +~10% on the 2026-03-05 emissions-cut vote |

---

## Ecosystem & Use Cases

- **USDS stablecoin** — a decentralized dollar used as collateral, settlement, and savings across [[defi|DeFi]]; battling [[ethena|Ethena's]] USDe for the #3 stablecoin slot behind USDT/USDC.
- **Sky Savings Rate (sUSDS)** — native yield on USDS; a core demand driver and a benchmark in the [[stablecoin-yields|stablecoin-yield]] landscape.
- **SKY staking** — the Staking Engine: stake SKY for rewards and to borrow USDS against staked SKY.
- **Spark (SPK) Star** — SparkLend (lending), sUSDS yield routing, and tokenized-asset allocations; its own token and buybacks.
- **RWA reserves** — USDS is partly backed by tokenized US T-bills, making Sky one of the largest [[real-world-assets|RWA]] allocators in DeFi.
- **Cross-chain (SkyLink)** — USDS/SKY available across Ethereum, Solana, Base, [[arbitrum|Arbitrum]] and more.

---

## Market Structure & Derivatives

- **Spot venues** — [[binance|Binance]] (SKY/USDT), [[kraken|Kraken]], Upbit (KRW), Bitget, KuCoin, Crypto.com; on-chain on Uniswap v2/v3 (SKY/WETH, USDS/SKY). 24h spot volume just ~$9.93M (2026-06-20) — **the thinnest of the six**, a meaningful slippage/exit risk at size.
- **Perpetuals** — SKY-PERP on [[hyperliquid|Hyperliquid]]; thinner perp liquidity than [[aave|AAVE]]/[[ethena|ENA]].
- **Buyback as a structural bid** — the buyback engine is a recurring on-chain buyer; with thin float and low turnover, sustained buybacks have outsized price impact (and pauses/cuts have the reverse effect, as the 2026-03-14 cut showed).
- **Liquidity caveat** — low turnover means SKY can gap on governance headlines (emissions votes) and is harder to trade in size than its $1.36B cap suggests.

---

## Valuation Framework

SKY is one of the most cash-flow-driven tokens in crypto (a "real yield + buyback" asset). Lenses (describe, do not invent values):

- **USDS supply** — the revenue base; USDS growth ≈ revenue growth ≈ buyback capacity. Track via DefiLlama. ($9.86B end-2025; ~$12B April-2026 peak.)
- **Net protocol revenue** — stability fees + RWA (T-bill) income minus the Sky Savings Rate and costs. Highly **rate-sensitive**: Fed cuts compress T-bill income.
- **Buyback yield** — cumulative/annualized buyback spend vs market cap; an effective shareholder-yield floor (when active).
- **Sky Savings Rate vs Fed funds** — the carry competitiveness of sUSDS, which drives USDS demand.
- **MC/FDV (0.99)** — no dilution adjustment needed; valuation hinges on revenue and buyback policy.

---

## Trading Playbook

- **Narrative basket** — the core **"real yield / buyback" DeFi basket** with [[uniswap|UNI]] and [[aave|AAVE]]: protocols that convert revenue into supply reduction. SKY is also a **stablecoin-supply proxy**.
- **Macro context** — in the **extreme-fear / Established Bear Market** regime (F&G = 23), SKY's buyback bid and shallow drawdown (-42% vs ATH, vs 88–96% for peers) make it relatively defensive — but the dominant macro risk is **rate cuts**, which compress T-bill income and revenue.
- **Key dashboards** — USDS/DAI total supply, Sky Savings Rate vs Fed funds, monthly buyback spend, emissions-schedule votes, Spark TVL/SPK actions.
- **Catalysts (bull)** — emission cuts (the Mar-2026 vote is the template), USDS supply highs, further Star launches/airdrops.
- **Catalysts (bear)** — rate cuts (lower T-bill income), buyback pace reductions, GENIUS-Act-era competition from regulated stablecoins, USDS/DAI cannibalization.
- **Risk discipline** — respect the thin liquidity; size for slippage and avoid chasing governance-headline gaps.

---

## History

- **2014** — MakerDAO founded by Rune Christensen.
- **2017** — DAI launched (single-collateral "Sai"); the original decentralized stablecoin.
- **2019** — Multi-Collateral DAI.
- **2020–22** — RWA/T-bill collateral added; MKR governance matures.
- **2023** — "Endgame" plan announced (Sky + Stars sub-DAOs).
- **2024** — rebrand to **Sky Protocol**; **USDS** launched; MKR→SKY migration (1 MKR = 24,000 SKY); SKY ATH $0.100535 (Dec).
- **Jun 2025** — first Star **Spark (SPK)** token launch (10B genesis).
- **2025** — USDS +86% YTD to $9.86B; aggressive SKY buybacks (~$114.5M, ~1.83B SKY).
- **2026** — USDS ~$12B peak (Apr); 2026-03-05 emissions-cut vote (+~10%); 2026-03-14 buyback pace cut; rank #57 at $0.058353 (2026-06-20).

---

## Competitive Positioning

| Issuer | Token / Dollar | Backing model | Differentiator vs Sky |
|---|---|---|---|
| **Sky** (ex-Maker) | SKY / USDS | Overcollateralized crypto + RWA (T-bills); DAO-governed | Oldest decentralized issuer; rate-sensitive RWA revenue; buyback + real yield |
| [[aave\|Aave]] | AAVE / GHO | Overcollateralized against money-market collateral | GHO is newer/smaller; Aave is primarily a lender, Sky primarily an issuer |
| [[ethena\|Ethena]] | ENA / USDe | Delta-neutral basis (long spot + short perp) | Higher native yield but funding-rate dependent; Sky's yield is RWA/fee-based, lower-risk profile |
| Fiat-backed (USDT/USDC) | — | 1:1 fiat/T-bill reserves | Fully redeemable, centralized; Sky is decentralized + yield-bearing |

The cleanest peers are **Sky vs [[aave|Aave]]** (overcollateralized DeFi issuers with buyback-driven tokenomics) and **Sky vs [[ethena|Ethena]]** (USDS vs USDe — collateral/RWA-backed stability and yield vs funding-rate-derived yield). Sky's edge is a longer track record and a lower-risk (RWA/T-bill) yield source; its dependence on interest rates is the macro vulnerability that Ethena's funding-rate model does not share (and vice versa).

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x56072c95faa701256059aa122697b133aded9279` |
| Hydration | `asset_registry/1000795` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair |
|---|---|
| Binance | SKY/USDT |
| Kraken | SKY/USD |
| Upbit | SKY/KRW |
| Bitget | SKY/USDT |
| KuCoin | SKY/USDT |
| Crypto.com Exchange | SKY/USD |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| [[hyperliquid|Hyperliquid]] | SKY-PERP | Perpetual |
| Uniswap V3 (Ethereum) | SKY/WETH | Spot |
| Uniswap V2 (Ethereum) | USDS/SKY | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://sky.money/](https://sky.money/) |
| **Twitter** | [@SkyEcosystem](https://twitter.com/SkyEcosystem) |
| **Whitepaper** | [Sky whitepaper (IPFS)](https://ipfs.io/ipfs/Qmex5coqQPXqo4FvCkPqvKfH2ibBgACTsUV3YrTGaC86LQ) |
| **Research** | [Messari — Sky Protocol](https://messari.io/project/sky-protocol) |

---

## Risks

- **Rate sensitivity (HIGH)** — much of Sky's revenue is RWA/T-bill income; Fed rate cuts directly compress earnings and buyback capacity.
- **Liquidity (MEDIUM-HIGH)** — very thin token turnover (~$9.93M/day vs $1.36B cap) magnifies slippage and exit risk; price gaps on governance headlines.
- **Governance complexity / founder influence** — the multi-Star "Endgame" structure is complex, and Rune Christensen's influence raises centralization-of-direction concerns.
- **RWA counterparty exposure** — tokenized T-bill/RWA reserves carry custodian and counterparty risk.
- **Buyback is conditional** — the bid depends on surplus and DAO will; the 2026-03-14 pace cut shows it can be dialed down.
- **DAI/USDS cannibalization & stablecoin regulation** — GENIUS-Act-era regulated stablecoins compete with decentralized issuers for share.
- **Macro beta** — defensive relative to peers but still a crypto-beta asset in an **Established Bear Market** / extreme-fear regime.

---

## Related

- [[crypto-markets]]
- [[ethereum]]
- [[stablecoins]] — USDS/DAI vs [[usdt]], [[usdc]], Ethena USDe
- [[stablecoin-yields]] — Sky Savings Rate context
- [[real-world-assets]] — T-bill/RWA reserves
- [[decentralized-exchange]] — on-chain venue context
- [[uniswap]] — fellow fee-switch/buyback basket member
- [[aave]] — peer DeFi issuer/lender
- [[ethena]] — peer stablecoin issuer (USDe)
- [[hyperliquid]] — perp venue
- [[narrative-trading]] — real-yield basket
- [[global-dollar]] — regulated-stablecoin competition context

---

## Sources

- Market snapshot 2026-06-20 (cryptodataapi.com / CoinGecko): price $0.058353, mcap $1.359B, rank #57, vol $9.93M, 24h -0.79%, 7d +3.27%, MC/FDV 0.99.
- CoinDesk, "SKY jumps nearly 10% after governance vote slows new token creation while buybacks tighten supply" (2026-03-05) — https://www.coindesk.com/markets/2026/03/05/sky-jumps-nearly-10-after-governance-vote-cuts-emissions-while-buybacks-tighten-supply
- Eco, "Sky Savings Rate Deep Dive 2026: SSR, sUSDS, USDS mechanics" — https://eco.com/support/en/articles/15254003-sky-savings-rate-deep-dive-2026-ssr-susds-usds-mechanics
- OKX Learn, "USDS repurchase and SKY tokenomics" — https://www.okx.com/learn/usds-repurchase-sky-tokenomics-defi
- Messari, Sky Protocol / Spark / Sky Dollar project pages — https://messari.io/project/sky-protocol ; https://messari.io/project/spark-sky-protocol
- Blockster, "Spark Protocol eyes treasury grants, SPK buybacks in new spell" (Feb 2026) — https://blockster.com/spark-protocol-eyes-treasury-grants-spk-buybacks-in-new-spell
- CoinGecko top-1000 snapshot (2026-04-09), original auto-generated data
- Verified via web search, 2026-06-10

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 23.34B SKY |
| **Total Supply** | 23.46B SKY |
| **Max Supply** | 23.46B SKY |
| **Fully Diluted Valuation** | $1.48B |
| **Market Cap / FDV Ratio** | 0.99 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $8.94M |
| **Market Cap Rank** | #51 |
| **24h Range** | $0.0609 — $0.0643 |
| **CoinGecko Sentiment** | 100% positive |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---
