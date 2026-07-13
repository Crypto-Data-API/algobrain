---
title: "Mantle"
type: entity
created: 2026-04-09
updated: 2026-06-20
status: excellent
tags: [crypto, defi, ethereum]
aliases: ["MNT", "Mantle Network", "BitDAO"]
entity_type: protocol
founded: 2023
headquarters: "Decentralized (DAO; ex-BitDAO, Bybit-affiliated origins)"
website: "https://group.mantle.xyz/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[layer-2]]", "[[restaking]]", "[[hyperliquid]]", "[[bybit]]", "[[narrative-trading]]"]
---

# Mantle

**Mantle** (MNT) is an [[ethereum]] [[layer-2|Layer 2]] and on-chain financial ecosystem that emerged from the 2023 BitDAO rebrand, distinguished by one of the largest treasuries in crypto (**>$6.2B** in MNT, ETH, BTC and stablecoins) and a deliberate pivot toward bridging TradFi and DeFi — "blockchain for banking." In 2025–2026 it transitioned from an optimistic rollup to a **ZK validity rollup** (OP Succinct), becoming the largest ZK rollup by TVL (>$2B), and launched the **UR neobank** app. Market cap is **$1.75B, rank #47 (2026-06-20)**.

---

## Market Data

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

Backdrop: the [[crypto-fear-and-greed-index|Fear & Greed Index]] reads **22 (extreme fear)** in an **established bear market**. MNT is roughly flat on the day and down ~2.6% on the week — relatively stable, consistent with the "treasury-backed floor" thesis (treasury value > market cap).

| Metric | Value |
|---|---|
| **Price** | $0.528744 |
| **Market Cap** | $1,745,770,126 |
| **Market Cap Rank** | #47 |
| **24h Volume** | $19,654,634 |
| **24h Change** | +0.02% |
| **7d Change** | -2.62% |
| **24h Range** | $0.520973 – $0.534254 |
| **Circulating Supply** | 3,302,294,383 MNT |
| **Total Supply** | 6,219,316,795 MNT |
| **Max Supply** | 6,219,316,795 MNT |
| **Fully Diluted Valuation** | $3,287,864,802 |
| **Market Cap / FDV** | ~0.53 |
| **All-Time High** | $2.86 (2025-10-09) — **-81.48%** from ATH |
| **All-Time Low** | $0.307978 (2023-10-18) — **+71.70%** from ATL |

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | MNT |
| **Type** | [[layer-2\|L2]] smart-contract platform + ecosystem token (gas, governance, staking) |
| **Market Cap** | $1.75B, rank #47 (2026-06-20) |
| **Tech** | ZK validity rollup (migrated from optimistic via Succinct's OP Succinct, 2025); EigenDA data availability |
| **Treasury** | >$6.2B (MNT, ETH, BTC, stablecoins) — among the largest DAO treasuries in crypto |
| **Product pillars** | Mantle Network, mETH Protocol (LST), Function (FBTC), MI4 index fund, Mantle Banking / UR, MantleX (AI) |
| **Categories** | Smart Contract Platform, Layer 2, Ethereum Ecosystem, Neobank |
| **Website** | [https://group.mantle.xyz/](https://group.mantle.xyz/) |

---

## Overview

Mantle is a pioneering on-chain ecosystem dedicated to revolutionizing the future of finance and blockchain scalability, seamlessly bridging traditional finance (TradFi) and decentralized finance (DeFi). Through products like Mantle Network, mETH Protocol, Function (FBTC), and Mantle Index Four (MI4), Mantle aims to be a unified financial-services platform for the Web3 era.

$MNT powers the ecosystem: native gas token on Mantle Network, governance, and staking. The project originated as **BitDAO** (BIT), backed by Bybit, and converted to MNT in 2023 — the giant treasury is the BitDAO inheritance.

### 2025–2026 developments

- **ZK migration** — Mantle moved from optimistic rollup to **ZK validity rollup** using Succinct's OP Succinct stack, cutting withdrawal finality from ~7 days to ~hours; now the **largest ZK rollup by TVL (>$2B)**.
- **Six innovation pillars (2025)** — Mantle Network, mETH Protocol (liquid staking, ~$1B+ TVL at peak), Function (FBTC wrapped-BTC yield), **MI4** (Mantle Index Four, an S&P-style crypto index fund run with Securitize), **Mantle Banking / UR** (a Swiss-account-style crypto neobank app launched 2025 offering fiat IBANs + crypto rails), and **MantleX** (AI agents).
- **Price cycle** — MNT ran to an ATH of **$2.86 on 2025-10-09** (banking-pivot + buyback narratives), then retraced hard with the broader alt market to ~$0.65 by April 2026 and **$0.529 by 2026-06-20 (-81.5% from ATH)** in an extreme-fear tape.
- Listed in indices/portfolios incl. GMCI 30; named in World Liberty Financial portfolio buys (2024–2025).

---

## Protocol & Technology

Mantle is an [[ethereum|Ethereum]] [[layer-2|Layer 2]] plus a vertically integrated on-chain financial group ("blockchain for banking"). MNT is the gas, governance and staking token across the stack.

### Mantle Network (the L2)
- **From optimistic to ZK** — Mantle launched (2023) as an OP-stack **optimistic rollup** with ~7-day withdrawal challenge windows. In 2025 it migrated to a **ZK validity rollup** using **Succinct's OP Succinct** (SP1 zkVM), generating validity proofs of L2 execution and cutting withdrawal finality from ~7 days to ~hours. This made Mantle the **largest ZK rollup by TVL (>$2B)**.
- **Modular data availability** — Mantle uses **EigenDA** ([[restaking|EigenLayer]]'s data-availability service) rather than posting all data to Ethereum L1, sharply lowering data-availability costs. This is a modular-DA bet that ties Mantle to the [[restaking]] thesis and trades some Ethereum-equivalent security for cost.
- **MNT as gas** — MNT (not ETH) is the native gas token on Mantle Network, a deliberate value-capture choice.

### mETH Protocol (liquid staking + restaking)
Mantle's [[ethereum|ETH]] liquid-staking product: users stake ETH for **mETH**, a yield-bearing LST (~$1B+ TVL at peak). **cmETH** extends this into restaking, layering EigenLayer/AVS yield on top — directly plugging Mantle into the [[restaking]] narrative.

### Function (FBTC)
**FBTC** is an omnichain wrapped-BTC standard giving Bitcoin holders DeFi yield across chains — Mantle's bid for the BTCFi flow.

### MI4 (Mantle Index Four)
An **institutional, S&P-style crypto index fund** run with **Securitize**, holding BTC, ETH, SOL and a stablecoin/staking sleeve — a tokenized index product targeting institutional allocators (RWA-adjacent).

### Mantle Banking / UR (the neobank)
**UR** is a crypto-neobank app launched 2025 offering **fiat IBANs + crypto rails** (Swiss-account-style), bridging TradFi banking and on-chain finance — the centerpiece of the "blockchain for banking" pivot and the key revenue bet.

### MantleX (AI)
An AI-agents initiative layered on the ecosystem.

### Treasury & origin
Mantle began as **BitDAO (BIT)**, backed by Bybit, and converted to MNT in 2023. The **>$6.2B treasury** (MNT, ETH, BTC, stablecoins) is the BitDAO inheritance and one of the largest in crypto — it funds buybacks, product development and the banking pivot, and underpins the recurring "treasury > market cap = floor" argument.

---

## Trading Relevance

- **Where it trades**: spot on Bybit (deepest, given shared origins), Kraken, Upbit (KRW), KuCoin, Bitget; perps on [[hyperliquid|Hyperliquid]] (MNT-PERP) and major CEX perp venues. ~$40M+ daily spot volume (April 2026 snapshot).
- **Narrative baskets**: trades with the **L2 basket** (ARB, OP, STRK) but increasingly with **neobank/payments** and **RWA-adjacent** narratives after the UR launch and MI4 — a hybrid profile. Also a "treasury-backed" token: market cap < treasury value has repeatedly been cited as a floor argument (an [[narrative-trading]] staple).
- **Catalysts**: UR user metrics, treasury deployments/buybacks, mETH/FBTC TVL growth, ZK-stack milestones, Bybit ecosystem flows.
- **Risks**: heavy supply concentration (treasury + Bybit nexus), unlock/utilization of the 6.22B max supply (MC/FDV ~0.53), L2 fee compression, and dependence on the banking pivot actually shipping revenue.

---

## Tokenomics & Supply

> *Authoritative figures are in the [[mantle#Market Data\|Market Data]] block (2026-06-20).*

| Metric | Value (2026-06-20) |
|---|---|
| **Circulating Supply** | 3,302,294,383 MNT |
| **Total Supply** | 6,219,316,795 MNT |
| **Max Supply** | 6,219,316,795 MNT |
| **Fully Diluted Valuation** | $3,287,864,802 |
| **Market Cap / FDV Ratio** | ~0.53 |

**Emissions, unlocks & treasury.** MNT has a fixed ~6.22B max supply (the converted BitDAO/BIT base). Only ~53% circulates (~3.30B); the remaining ~47% (~2.92B MNT) sits largely in the **Mantle treasury/DAO** rather than on a hard vesting cliff — meaning the supply overhang is **discretionary** (DAO-controlled deployment, buybacks, ecosystem incentives) more than a scheduled unlock. This cuts both ways: the treasury can support price via buybacks, but DAO sales/incentive emissions are a latent dilution vector. The unusual feature is that the **treasury value (>$6.2B) exceeds the circulating market cap ($1.75B)** — a frequently cited "floor" argument, though treasury MNT marked at market is partly reflexive.

---

## Price History

> *Authoritative current figures are in the [[mantle#Market Data\|Market Data]] block (2026-06-20). Table below is long-horizon reference.*

| Metric | Value |
|---|---|
| **All-Time High** | $2.86 (2025-10-09) — -81.48% |
| **All-Time Low** | $0.307978 (2023-10-18) — +71.70% |
| **24h Change (2026-06-20)** | +0.02% |
| **7d Change (2026-06-20)** | -2.62% |

---

## Platform & Chain Information

**Native Chain:** Ethereum (L2 settles to Ethereum)

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x3c3a81e81dc49a522a592e7622a7e711c06bf354` |
| Mantle | `0xdeaddeaddeaddeaddeaddeaddeaddeaddead0000` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair |
|---|---|
| Bybit | MNT/USDT (+ perps) |
| Kraken | MNT/USD |
| Upbit | MNT/KRW |
| KuCoin | MNT/USDT |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| [[hyperliquid|Hyperliquid]] | MNT-PERP | Perpetual |
| Uniswap V3 (Ethereum) | MNT/USDe | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://group.mantle.xyz/](https://group.mantle.xyz/) |
| **Twitter** | [@Mantle_Official](https://twitter.com/Mantle_Official) |
| **Telegram** | [mantlenetwork](https://t.me/mantlenetwork) (~73K members, Apr 2026) |
| **Discord** | [https://discord.com/invite/0xMantle](https://discord.com/invite/0xMantle) |
| **GitHub** | [https://github.com/mantlenetworkio](https://github.com/mantlenetworkio) |
| **Docs** | [https://docs.mantle.xyz/network/introduction/overview](https://docs.mantle.xyz/network/introduction/overview) |

---

## Ecosystem & Use Cases

- **L2 DeFi** — DEXes, lending and yield protocols on Mantle Network, with MNT as gas; TVL > $2B (largest ZK rollup).
- **Liquid staking / restaking** — mETH (ETH LST) and cmETH (restaked) plug Mantle into the [[restaking|EigenLayer]] yield stack.
- **BTCFi** — FBTC brings Bitcoin liquidity into DeFi across chains.
- **Tokenized index** — MI4 (with Securitize) offers institutional, S&P-style crypto index exposure (RWA-adjacent).
- **Neobank** — UR app: fiat IBANs + crypto rails for consumer/SMB banking — the revenue centerpiece.
- **AI** — MantleX agents initiative.
- **Treasury deployment** — the >$6.2B treasury funds ecosystem grants, buybacks and product build-out.

---

## Market Structure & Derivatives

- **Spot venues**: Bybit (deepest, shared ex-BitDAO origins and price leader), [[kraken|Kraken]], Upbit (KRW), KuCoin, Bitget. On-chain, MNT/USDe on [[uniswap|Uniswap]] v3. Not Coinbase-listed.
- **Perps & funding**: MNT-PERP on [[hyperliquid|Hyperliquid]] and major CEX perp desks (Bybit deepest). With price flat/slightly down, funding sits near neutral.
- **Liquidity**: ~$19.7M 24h volume on a ~$1.75B cap (~1.1% turnover) — thin for a top-50 token, partly because a large share of supply is treasury-held and not freely floating. Real float is smaller than circulating supply implies, which can exaggerate both rallies and drops.
- **Bybit dependence**: liquidity concentration on Bybit is a structural feature (and a risk) given the shared origin.

---

## Valuation Framework

MNT is a hybrid — value it across three lenses:

- **L2 fundamentals** — Mantle Network TVL (>$2B), transaction fees (MNT gas burn/usage), and active addresses; compare to ARB/OP/STRK on MC/TVL and fee capture.
- **Treasury-floor / NAV** — treasury value (>$6.2B) vs circulating market cap ($1.75B); a discount-to-NAV framing, with the caveat that treasury MNT is reflexive (its value falls if MNT falls).
- **Product revenue (the swing factor)** — UR neobank user/revenue metrics, mETH/cmETH and FBTC TVL, MI4 AUM. The bull case requires the banking pivot to ship real, recurring revenue; otherwise MNT is "a treasury with an L2 attached."
- **Restaking optionality** — mETH/cmETH growth ties MNT to the [[restaking]] AVS-yield narrative.
- **MC/FDV ~0.53** — discount for ~47% non-circulating (mostly treasury) supply.

---

## Trading Playbook

- **Multi-basket profile** — MNT trades with the **L2 basket** (ARB, OP, STRK), the **neobank/payments** narrative (post-UR), and **treasury-backed / RWA-adjacent** themes. Pick the dominant narrative for the regime.
- **Treasury-floor mean reversion** — when market cap trades well under treasury value, the "discount-to-NAV" floor argument attracts buyers; fade extreme discounts/premiums to treasury NAV.
- **Buyback catalysts** — DAO treasury buybacks and deployments are recurring catalysts; position around governance signals.
- **Product-metric trades** — UR user growth, mETH/FBTC TVL, ZK-stack milestones, Bybit ecosystem flows.
- **Pairs** — MNT vs an L2 basket (ARB/OP) to isolate Mantle-specific product news; MNT vs a restaking token to trade the EigenLayer-yield angle.
- **Liquidity & float caution** — thin freely-floating supply + Bybit concentration means slippage and exchange-specific risk; size accordingly, especially in extreme fear.

---

## History

| Date | Event |
|---|---|
| 2021 | BitDAO (BIT) launches, backed by Bybit; builds a large treasury |
| 2023-07 | BitDAO rebrands to **Mantle**; BIT → MNT conversion; Mantle Network (optimistic rollup) launches |
| 2023-10 | MNT all-time low $0.308 |
| 2024 | mETH liquid staking; ecosystem build-out; World Liberty Financial portfolio buys |
| 2025 | Six-pillar strategy: ZK migration (OP Succinct), MI4 (with Securitize), **UR neobank**, FBTC, MantleX |
| 2025-10-09 | MNT all-time high $2.86 (banking-pivot + buyback narratives) |
| 2026-04 | Retrace to ~$0.66 with the alt market |
| 2026-06-20 | MNT $0.529, #47, -81.5% from ATH, in an extreme-fear market |

---

## Competitive Positioning

| L2 | Positioning | Edge vs Mantle | Mantle's Edge |
|---|---|---|---|
| Arbitrum (ARB) | Largest L2 by TVL/activity | Deepest DeFi ecosystem, most TVL, brand | Huge treasury; vertically integrated finance stack; ZK migration |
| Optimism (OP) | Superchain leader | Superchain network effects (Base, etc.) | Treasury war-chest; banking/neobank pivot; mETH/restaking |
| Base ([[base]]) | Coinbase consumer L2 | Coinbase distribution + US retail | Own treasury + integrated products; not single-parent-dependent |
| Starknet (STRK) | ZK-native L2 | Native ZK from day one, Cairo VM | EVM-compatibility; larger treasury; financial-product suite |
| Blast / Linea / others | Yield/EVM L2s | Various niche incentives | Scale of treasury and product integration |

Mantle's differentiation is **not** being the biggest or fastest L2 — it is the **treasury + vertically integrated TradFi-DeFi product stack** (neobank, index fund, LST/restaking, BTCFi). The bear case: a treasury looking for a thesis, with the banking pivot unproven. The bull case: a self-funded crypto financial group that can outspend rivals while the L2 monetizes via its own products. Tied to [[bybit]] and the [[restaking]] DA bet.

---

## Risks

- **Banking-pivot execution** — the bull thesis depends on UR/Mantle Banking and MI4 shipping real, recurring revenue; if they stall, MNT is "a treasury with an L2 attached."
- **Supply / float concentration** — ~47% of supply is treasury/DAO-held; discretionary DAO sales or incentive emissions are a latent dilution vector, and thin freely-floating supply amplifies volatility.
- **Bybit dependence** — origin and deepest liquidity tie MNT to Bybit; exchange-specific risk (regulatory, solvency, listing) is concentrated.
- **Modular-DA security trade-off** — using EigenDA ([[restaking]]) instead of Ethereum L1 DA lowers cost but trades some Ethereum-equivalent security/decentralization; an EigenLayer/AVS incident would propagate.
- **L2 fee compression & competition** — L2 fees are racing to zero; Mantle competes with larger ecosystems (Arbitrum, OP, Base) for the same flow.
- **Reflexive treasury valuation** — the "treasury > market cap floor" weakens in a crash because treasury MNT marks down with the token.
- **Bear-market drawdown** — -81.5% from ATH in an established bear market; further alt weakness is a live risk.

---

## Related

- [[crypto-markets]]
- [[ethereum]] — settlement layer
- [[layer-2]] — sector
- [[restaking]] — EigenDA / mETH-cmETH linkage
- [[bybit]] — affiliated exchange (ex-BitDAO)
- [[hyperliquid]] — perp venue
- [[uniswap]] — on-chain spot venue
- [[base]] — peer L2
- [[narrative-trading]] — L2 / neobank / treasury-floor baskets

---

## Sources

- Market data 2026-06-20: cryptodataapi.com / CoinGecko markets snapshot (`raw/data/crypto-loop/coingecko-markets.json`)
- CoinGecko, Mantle page (treasury >$6.2B, ZK rollup status) — https://www.coingecko.com/en/coins/mantle
- CoinMarketCap, Mantle — https://coinmarketcap.com/currencies/mantle/
- Mantle official site / docs — https://group.mantle.xyz/ , https://docs.mantle.xyz/
- CoinGecko top-1000 snapshot (2026-04-09), original auto-generated data
- Verified via web search, 2026-06-10
