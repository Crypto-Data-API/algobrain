---
title: "PancakeSwap"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, hyperliquid, perpetual-futures, funding-rate, open-interest, altcoins]
aliases: ["CAKE", "PancakeSwap Token"]
entity_type: protocol
founded: 2020
headquarters: "Decentralized (anonymous team, BNB Chain origin)"
website: "https://pancakeswap.finance/"
related: ["[[aerodrome-finance]]", "[[automated-market-maker]]", "[[base]]", "[[bnb]]", "[[crypto-markets]]", "[[decentralized-exchange]]", "[[ethereum]]", "[[hyperliquid]]", "[[solana]]", "[[uniswap]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[cash-and-carry]]", "[[oi-confirmed-trend]]"]
---

# PancakeSwap

**PancakeSwap** (CAKE) is the dominant [[decentralized-exchange|decentralized exchange]] on [[bnb|BNB Chain]] and one of the highest-volume DEXes in all of crypto, launched September 2020 as an [[automated-market-maker|automated market maker]] (AMM). It has expanded multichain (BNB, Ethereum, Base, Arbitrum, Solana, Aptos, zkSync, Linea, opBNB) and into perps and a launchpad. For traders, CAKE is the liquid proxy for BNB Chain DeFi activity — and since the April 2025 **Tokenomics 3.0** overhaul it is run as a deflationary burn asset rather than a yield/governance token.

---

## Market Data

| Metric | Value |
|---|---|
| **Current Price** | $1.38 |
| **Market Cap** | $445,544,107 (~$445.5M) |
| **Market Cap Rank** | #110 |
| **Fully Diluted Valuation** | $462,555,897 (~$462.6M) |
| **24h Volume** | $49,168,295 (~$49.17M) |
| **24h Change** | +2.01% |
| **7d Change** | +3.62% |
| **Circulating Supply** | 324,094,573 CAKE (~324.1M) |
| **Total Supply** | 336,469,170 CAKE (~336.5M) |
| **Max Supply** | 400,000,000 CAKE (400M) |
| **MC / FDV** | ~0.96 |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

**Context:** The snapshot lands inside an **Established Bear Market** regime with the Fear & Greed Index at **23 (extreme fear)**. Against that risk-off tape, CAKE is mildly *outperforming* — up +2.01% on the day and +3.62% on the week while most altcoins bleed — a relative-strength signal that traders watch in DEX/exchange tokens, plausibly reflecting the deflationary burn bid and sustained BNB Chain volume. At ~$445.5M cap (rank #110) CAKE remains a top-tier DEX token; its near-1.0 MC/FDV (~0.96) means almost no overhang dilution — unusual among DeFi peers and a direct consequence of [[#tokenomics--supply|Tokenomics 3.0]].

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | CAKE |
| **Sector** | DEX / AMM, exchange token, DeFi |
| **Rank** | #110 (~$445.5M cap, $1.38 — 2026-06-20 snapshot) |
| **Home chain** | BNB Smart Chain (deployed on 10+ chains) |
| **Supply mechanics** | 400M max; ~324.1M circulating; deflationary since Apr 2025 (target ~4%/yr net deflation, burns > emissions) |
| **Backers** | YZi Labs (prev. Binance Labs) portfolio |
| **Website** | [https://pancakeswap.finance/](https://pancakeswap.finance/) |

---

## Overview

PancakeSwap launched as the "Uniswap of BSC" with food-farm yield mechanics and became BNB Chain's liquidity hub. It runs v2/v3 concentrated-liquidity AMMs across ten-plus chains, plus perpetuals, prediction markets, IFO launchpad, and (2025) "Springboard"-style memecoin tooling. Its volumes benefit directly from Binance-ecosystem activity — notably the 2025 Binance Alpha program routing retail flow through BNB Chain DEX liquidity.

---

## Protocol & Technology

PancakeSwap is a **multichain AMM DEX** — a family of smart contracts deployed across BNB Smart Chain (home), [[ethereum|Ethereum]], [[base|Base]], Arbitrum, [[solana|Solana]], Aptos, zkSync Era, Linea, Polygon zkEVM, and opBNB. Liquidity, routing, and UX are unified through a single front-end, but each chain holds its own pools, so depth is fragmented by chain (BNB Chain remains by far the deepest).

### AMM engine: v2 → v3 → v4

| Generation | Model | What it added |
|---|---|---|
| **v2** | Classic constant-product `x·y=k` AMM (Uniswap-v2-style) | Full-range LP, food-farm yield mining; still the deepest fallback liquidity on BNB Chain |
| **v3** | Concentrated liquidity (Uniswap-v3-style) | LPs allocate capital to chosen price bands → far higher capital efficiency; multiple fee tiers; bulk of large-pair volume routes here |
| **v4** | Modular AMM with **hooks** + customizable pool types (CLAMM / LBAMM) | Singleton architecture, gas savings, dynamic fees, and developer-defined "hooks" (e.g. custom oracles, on-chain limit orders, anti-MEV) — PancakeSwap's answer to [[uniswap|Uniswap]] v4 |

The smart router splits trades across v2/v3 (and stable pools) to minimize slippage, the standard architecture for a modern [[automated-market-maker|AMM]]/[[decentralized-exchange|DEX]].

### Beyond spot AMM

- **Perpetuals** — PancakeSwap Perps (orderbook + AMM-backed) offering leveraged perps on majors; competes with on-chain perp venues and feeds protocol fees.
- **Prediction markets** — fast BNB/CAKE price-direction rounds, a high-frequency retail product unique to the BNB ecosystem.
- **IFO launchpad** — Initial Farm Offerings let projects raise by committing CAKE, historically a key burn/utility sink.
- **Springboard (2025)** — memecoin-launch tooling that routes new-token creation and trading flow through PancakeSwap liquidity, capturing the BNB Chain memecoin season.
- **Gaming/NFT marketplace, syrup pools, liquid-staking integrations** round out the app surface.

---

## Tokenomics & Supply

| Metric | Value (2026-06-20 snapshot) |
|---|---|
| **Circulating Supply** | 324,094,573 CAKE (~324.1M) |
| **Total Supply** | 336,469,170 CAKE (~336.5M) |
| **Max Supply** | 400,000,000 CAKE (400M) |
| **MC / FDV** | ~0.96 |
| **Emission policy** | Post-3.0: net deflationary (~4%/yr target, burns > emissions) |

### CAKE Tokenomics 3.0 (the defining change)

On **Apr 23, 2025**, PancakeSwap shipped **Tokenomics 3.0**, the most consequential redesign in the token's history:

- **Removed veCAKE, CAKE staking, and revenue sharing**, and **unlocked all locked CAKE** — ending the vote-escrow/gauge model entirely (contrast the ve(3,3) model still used by [[aerodrome-finance|Aerodrome]]).
- Pivoted to a **pure burn model**: target **~4% annual net deflation**, ~**5.3M CAKE burned annually**, with daily emissions cut from 29,000 → 20,000 → 14,500 and a stated goal of cutting total supply **~20% by 2030**.
- Contentious rollout: Cakepie DAO (whose business was built on veCAKE) objected, and PancakeSwap offered a **$1.5M CAKE compensation plan**. (Sources: BeInCrypto, crypto.news, ChainPlay)

**Dilution read:** with MC/FDV ~**0.96**, CAKE has almost no unlock overhang — nearly all supply is already circulating, and the *direction of travel is shrinking* supply (burns > emissions), the opposite of most DeFi tokens. The risk shifts from "dilution" to "does fee/volume growth justify the cap without a staking yield to anchor demand" — the classic post-veToken value-accrual question.

---

## Ecosystem & Use Cases

- **CAKE utility today:** trading-fee discounts, IFO participation, prediction-market and gaming sinks, governance, and — most importantly — being the asset the protocol *buys back and burns* with revenue. After 3.0 there is **no native staking yield**, so CAKE is a deflationary "exchange-token" claim on PancakeSwap's activity rather than a cash-flow token.
- **Binance/BNB flywheel:** PancakeSwap is the default DEX liquidity layer for [[bnb|BNB Chain]]. The 2025 **Binance Alpha** program routed large retail flow through BNB Chain DEXes, lifting PancakeSwap volumes to record months and accelerating burns.
- **Memecoin & launch flow:** Springboard plus the IFO launchpad make PancakeSwap the on-ramp for new BNB Chain tokens, capturing speculative seasons directly into protocol fees.
- **Multichain footprint:** while BNB Chain is the core, deployments on [[ethereum|Ethereum]], [[base|Base]], Arbitrum, [[solana|Solana]], Aptos, zkSync, Linea, and opBNB extend reach and diversify volume sources.

---

## Market Structure & Derivatives

- **Spot venues:** Binance, Kraken, Bitget, KuCoin (CEX); native PancakeSwap v2/v3 pools provide deepest on-chain liquidity, primarily on BNB Chain.
- **Perps:** **CAKE-PERP on [[hyperliquid|Hyperliquid]]** is the reference on-chain derivatives venue; CAKE perps also list across major CEXes.
- **Metrics to monitor (not invented here):** perp **funding rate** (persistent negative funding can mark crowded shorts into a relative-strength token like CAKE; positive funding flags leveraged longs), **open interest** (OI build vs spot volume), and CEX-vs-DEX basis. The protocol publishes weekly **burn vs emission** stats and DEX volume that should be cross-checked against on-chain volume dashboards. Daily/weekly spot volume itself (~$49.17M/24h on 2026-06-20) is a liquidity gauge for sizing.

---

## Valuation Framework

CAKE is best valued as an **exchange-token claim on a fee-generating DEX**, not a discounted-cash-flow asset (post-3.0 there is no direct holder revenue share — value accrues via burn). Metrics that drive the thesis:

- **Protocol DEX volume** — the top of the funnel; PancakeSwap is one of the highest-volume DEXes in crypto. Sustained volume is what funds buyback-and-burn.
- **Protocol fees / revenue** — trading fees across v2/v3/v4, perps, and prediction markets.
- **Burn rate vs emission rate** — the core 3.0 metric; *net* deflation (burns > emissions) is the value-accrual lever. Track the published weekly figures and the ~4%/yr / ~5.3M-annual-burn targets.
- **TVL** — liquidity depth that underpins low-slippage routing and volume share.
- **Volume/market-share vs peers** — PancakeSwap's BNB Chain share vs [[uniswap|Uniswap]] (multichain) and Solana DEXes ([[#competitive-positioning|see below]]).

*(Describe-only: no per-metric dollar values are asserted here beyond the dated market-data snapshot.)*

---

## Trading Playbook

- **Where it trades:** Binance, Kraken, Bitget, KuCoin (spot); **[[hyperliquid|Hyperliquid]] CAKE-PERP**; native PancakeSwap pools.
- **Narrative basket:** DEX/exchange tokens ([[uniswap|UNI]], SUSHI, [[aerodrome-finance|AERO]]) and the **BNB-ecosystem beta** basket — CAKE often moves with [[bnb]] and with Binance-driven retail activity waves (memecoin seasons on BNB Chain).
- **Key signals:** weekly burn vs emission stats (published by the team), BNB Chain DEX volume share vs Uniswap/Solana DEXes, Binance Alpha campaign activity, perp funding/OI.
- **Catalysts:** burn-rate acceleration, v4/hooks adoption, multichain expansion announcements, perps volume growth; risk side — BNB Chain activity fading, or Binance distancing itself from the ecosystem.
- **Regime note (2026-06-20):** in an extreme-fear/bear tape, CAKE's relative strength (+2% / +3.6%) is the setup to watch — DEX tokens that hold up on weak days can lead on the bounce, but a deflationary bid does not immunize against a broad altcoin drawdown.

---

## History

- **Sep 2020** — launched as the "Uniswap of BSC" with food-farm yield mining; rapidly became BNB Chain's liquidity hub.
- **Apr 30, 2021** — all-time high **$43.96** during the DeFi/BSC bull run.
- **Nov 3, 2020** — all-time low **$0.194441** in the protocol's earliest days.
- **2021–2023** — v2 → v3 concentrated-liquidity rollout; multichain expansion beyond BNB Chain; veCAKE/gauge model introduced.
- **2024–2026** — CAKE trades in a roughly $1.5–$4 band, structurally lagging the protocol's volume growth (the "fee-rich, token-poor" DEX problem).
- **Apr 23, 2025** — **Tokenomics 3.0** goes live: veCAKE/staking/revenue-share removed, pivot to deflationary burn (see [[#tokenomics--supply|Tokenomics & Supply]]).
- **2025** — record monthly volumes (Binance Alpha flow a major driver), with burns outpacing emissions for sustained periods.
- **2026-06-20** — $1.38, ~$445.5M cap, rank #110; relative strength amid an Established Bear Market.

---

## Competitive Positioning

| Protocol | Home chain | Model | Volume tier | Token model |
|---|---|---|---|---|
| **PancakeSwap (CAKE)** | [[bnb\|BNB Chain]] (multichain) | v2/v3 CL + v4 hooks; perps, prediction, launchpad | Very high (top DEXes) | Deflationary burn (no veCAKE post-3.0) |
| [[uniswap\|Uniswap (UNI)]] | [[ethereum\|Ethereum]] (multichain) | v2/v3 CL, v4 hooks/singleton | Highest (sector leader) | Governance; fee-switch debated |
| [[aerodrome-finance\|Aerodrome (AERO)]] | [[base\|Base]] | ve(3,3) vote-escrow AMM | High on Base | veAERO emissions + bribes (inflationary) |
| SushiSwap (SUSHI) | Multichain | v2/v3 AMM | Mid | xSUSHI fee-share |
| Raydium (RAY) | [[solana\|Solana]] | Hybrid AMM + orderbook (CLMM) | High on Solana | Buyback + emissions |

PancakeSwap's edge is **BNB-ecosystem dominance + volume**; its differentiator vs peers post-3.0 is a *shrinking* float driven by burns, versus the inflationary ve-emission models of [[aerodrome-finance|Aerodrome]] and the governance-only UNI.

---

## Tokenomics

| Metric | Value (2026-06-20 snapshot) |
|---|---|
| **Circulating Supply** | 324.09M CAKE |
| **Total Supply** | 336.47M CAKE |
| **Max Supply** | 400.00M CAKE |
| **MC / FDV** | ~0.96 |
| **Emission policy** | Post-3.0: net deflationary (~4%/yr target, burns > emissions) |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $43.96 (2021-04-30) |
| **All-Time Low** | $0.194441 (2020-11-03) |
| **24h Change** | +2.01% (2026-06-20) |
| **7d Change** | +3.62% (2026-06-20) |

---

## Platform & Chain Information

**Native Chain:** BNB Smart Chain

| Chain | Address |
|---|---|
| BNB Smart Chain | `0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82` |
| Ethereum | `0x152649ea73beab28c5b49b26eb48f7ead6d4c898` |
| Base | `0x3055913c90fcc1a6ce9a358911721eeb942013a1` |
| Solana | `4qQeZ5LwSz6HuupUu8jCtgXyW1mYQcNbFAW1sWZp89HL` |
| Arbitrum One | `0x1b896893dfc86bb67cf57767298b9073d2c1ba2c` |
| Linea | `0x0d1e753a25ebda689453309112904807625befbe` |
| Polygon zkEVM | `0x0d1e753a25ebda689453309112904807625befbe` |
| opBNB | `0x2779106e4f4a8a28d77a24c18283651a2ae22d1c` |
| zkSync | `0x3a287a06c66f9e95a56327185ca2bdf5f031cecd` |
| Aptos | `0x159df6b7...::oft::CakeOFT` |

---

## Social & Community

| Platform | Link |
|---|---|
| **Website** | [https://pancakeswap.finance/](https://pancakeswap.finance/) |
| **Twitter** | [@pancakeswap](https://twitter.com/pancakeswap) |
| **Reddit** | [r/pancakeswap](https://www.reddit.com/r/pancakeswap) |
| **Telegram** | [PancakeSwap](https://t.me/PancakeSwap) (109,733 members, April 2026) |
| **Discord** | [https://discord.com/invite/pancakeswap](https://discord.com/invite/pancakeswap) |
| **GitHub** | [https://github.com/pancakeswap](https://github.com/pancakeswap) |
| **Docs** | [https://docs.pancakeswap.finance/](https://docs.pancakeswap.finance/) |

---

## Risks

- **Value-accrual without yield** — post-3.0 there is no staking yield or revenue share; CAKE relies entirely on burns outpacing emissions, so a volume slowdown directly weakens the deflation thesis.
- **BNB-ecosystem concentration** — most depth and volume sit on [[bnb|BNB Chain]]; fading BNB Chain activity, or Binance distancing itself from the ecosystem, would hit CAKE hard.
- **DEX competition** — [[uniswap|Uniswap]] (multichain, v4 hooks), Solana DEXes (Raydium), and Base DEXes ([[aerodrome-finance|Aerodrome]]) compete for volume and routing.
- **Smart-contract / AMM risk** — multichain deployments widen the attack surface (bridge, pool, and router risk).
- **Liquidity & macro/regime risk** — as a top-100 DeFi token it is still exposed to the prevailing **Established Bear Market** and extreme-fear (F&G 23) conditions; relative strength can reverse quickly in a broad altcoin drawdown.

---

## Related

- [[bnb]] — host-chain beta
- [[uniswap]] — primary DEX competitor
- [[aerodrome-finance]] — ve(3,3) DEX peer (Base)
- [[automated-market-maker]], [[decentralized-exchange]] — protocol category
- [[hyperliquid]] — CAKE-PERP venue
- [[ethereum]], [[base]], [[solana]], [[crypto-markets]]

---

## Sources

- CoinGecko / cryptodataapi.com snapshot, 2026-06-20 (Market Data table)
- CoinGecko top-1000 snapshot, 2026-04-09 (historical market data)
- [PancakeSwap docs — CAKE Tokenomics](https://docs.pancakeswap.finance/protocol/cake-tokenomics)
- [BeInCrypto — PancakeSwap sets date for CAKE Tokenomics 3.0 despite controversy](https://beincrypto.com/pancakeswap-sets-date-for-new-cake-tokenomics/)
- [ChainPlay — PancakeSwap launches CAKE Tokenomics 3.0, retires veCAKE & gauges](https://chainplay.gg/blog/pancakeswap-launches-cake-3-with-major-governance-overhaul/)
- [crypto.news — PancakeSwap implements Tokenomics 3.0](https://crypto.news/pancakeswap-implements-tokenomics-3-0-upgrade-as-cake-rsi-flips-bullish/)
- WebSearch verification, 2026-06-10

## Trading Profile

### Venues & liquidity

CAKE is a **deep, liquid two-venue market**: it trades on **Binance** (CAKE/USDT spot plus a **USD-margined perpetual**) and on **[[hyperliquid|Hyperliquid]]** as **CAKE-PERP** (up to ~40-50x leverage). Binance provides the primary spot depth and the highest-liquidity perp; Hyperliquid supplies a transparent on-chain order book, on-chain funding, and the L2 depth used for programmatic execution. Having a spot leg on Binance *and* two perp venues means the CEX perp and the HL perp can be traded against Binance spot — enabling clean cash-and-carry, basis, and cross-venue funding trades without synthetic legs. Practically: size on Binance for large notional and best top-of-book depth; use Hyperliquid for on-chain funding capture, leverage, and hedged/basis structures. As a rank ~109 alt the book thins on both venues past the front size, so scale entries and respect slippage on aggressive sweeps.

### Applicable strategies

- [[cash-and-carry]] — long Binance spot CAKE vs short the Binance or HL perp to harvest basis when the perp trades at a premium; the genuine spot leg makes the carry fully deliverable.
- [[funding-rate-harvest]] — CAKE perp funding swings with BNB-ecosystem sentiment and memecoin-season leverage; collect funding on the delta-neutral side while it stays rich.
- [[hl-vs-cex-funding-divergence]] — funding on Hyperliquid CAKE-PERP and the Binance USD-margined perp can dislocate; short the richer, long the cheaper for market-neutral spread.
- [[oi-confirmed-trend]] — pair rising open interest with CAKE's relative-strength moves (burn-driven bid, Binance Alpha flow) to filter real trends from thin squeezes.
- [[liquidation-cascade-fade]] — as a high-beta alt, CAKE overshoots on liquidation flushes; fade the cascade extreme back toward VWAP once OI resets.
- [[breakout-and-retest]] — CAKE's multi-year $1.5-$4 band gives clean horizontal levels; trade confirmed breakouts with a retest entry to avoid fakeouts.

### Volatility & regime character

CAKE is a **high-beta DeFi / DEX (exchange) token** — an infra-token proxy for **BNB Chain** activity rather than a large-cap store-of-value. It carries strong positive **beta to BTC/ETH** in risk-on/risk-off regimes, but its idiosyncratic driver is **BNB-ecosystem and memecoin-season flow** (Binance Alpha, Springboard launches), so it can decouple and show relative strength (as in the 2026-06-20 bear-tape snapshot) when BNB Chain volume runs hot. The post-3.0 deflationary burn adds a structural bid but does not damp short-term volatility; expect alt-like drawdowns amplified in extreme-fear regimes.

### Risk flags

- **Venue/liquidity concentration** — depth is thin beyond front size at rank ~109; spot depth concentrates on Binance, so a Binance policy or listing change is an outsized single-venue risk.
- **BNB-ecosystem / narrative dependence** — value tracks BNB Chain volume and Binance-driven retail waves; fading ecosystem activity or Binance distancing directly deflates the thesis.
- **Perp funding dislocations** — funding can spike/flip during memecoin seasons and squeezes; crowded-leverage unwinds drive sharp liquidation cascades.
- **Value-accrual without yield** — post-Tokenomics-3.0 there is no staking yield; the burn-over-emission thesis breaks if volume slows (not a depeg/unlock risk — MC/FDV ~0.96 means minimal unlock overhang).
- **Smart-contract / multichain surface** — bridge, pool, and router risk across 10+ chain deployments.

---

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/summary?coin=CAKE` — all-in-one perp data (mark, funding, OI)
- `GET /api/v1/hyperliquid/prices` — all mid prices
- `GET /api/v1/hyperliquid/l2-book?coin=CAKE` — L2 order-book depth
- `GET /api/v1/hyperliquid/open-interest` — all-asset open interest

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=CAKE&interval=1h&limit=1000` — OHLCV candles
- `GET /api/v1/hyperliquid/funding-rates?coin=CAKE&limit=100` — funding history
- `GET /api/v1/daily/hyperliquid` — daily bulk snapshot of ~230 HL perps

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/summary?coin=CAKE"
```

Auth: `X-API-Key` header. Endpoint catalog: [[cryptodataapi-hyperliquid]]. See also [[cryptodataapi]].

---

## See Also

- [[crypto-markets]]
- [[bnb]]

---
