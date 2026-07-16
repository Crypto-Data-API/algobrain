---
title: "Somnia"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [altcoins, crypto, gamefi, perpetual-futures, funding-rate, open-interest, liquidations, derivatives]
aliases: ["SOMI", "Somnia Network"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://somnia.network/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[gamefi]]", "[[layer-1]]", "[[smart-contracts]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[token-unlock-supply-event]]", "[[liquidation-cascade-fade]]"]
---

# Somnia

**Somnia** (SOMI) is an **EVM-compatible [[layer-1]]** blockchain built for high-throughput, real-time consumer applications — games, [[gamefi]], the metaverse, and on-chain social. Because it is EVM-compatible, developers can deploy Solidity [[smart-contracts]] using familiar [[ethereum]] tooling while targeting much higher transaction rates. Somnia's design centers on a **MultiStream** architecture that parallelizes the chain to chase very low latency and high throughput. It currently ranks **#883** by market capitalization.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

As of 2026-06-21 SOMI trades at **$0.109955** with a market cap of **$17,603,481** (rank **#883**), down **-0.95%** over 24h and down **-1.31%** over the prior 7 days — roughly flat in an Extreme Fear market (Fear & Greed 22; BTC ~$64,180).

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | SOMI |
| **Market Cap Rank** | #883 |
| **Market Cap** | $17,603,481 |
| **Current Price** | $0.109955 |
| **24h Change** | -0.95% |
| **7d Change** | -1.31% |
| **Type** | EVM-compatible [[layer-1]] (gaming / consumer / metaverse) |
| **Categories** | Layer 1 (L1), Gaming Blockchains, Binance HODLer Airdrops, Binance Alpha Spotlight |
| **Website** | [https://somnia.network/](https://somnia.network/) |
> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

---

## Overview

Somnia is an EVM-compatible [[layer-1]] blockchain designed for high-performance, real-time applications across gaming, metaverse and social ecosystems. Because it is EVM-compatible, developers deploy [[smart-contracts]] with standard [[ethereum]] tooling, then benefit from Somnia's throughput-oriented runtime for high-frequency on-chain interactions inside persistent virtual environments.

Its **MultiStream** architecture is the headline differentiator: the project describes separating/parallelizing data production from consensus so many "streams" can be processed concurrently, paired with a custom database (IceDB) and compiled-EVM execution. **The project claims throughput on the order of 1,000,000+ transactions per second with sub-second finality**; such figures are vendor claims/benchmarks and should be treated as marketing until independently verified under realistic, decentralized conditions.

---

## Architecture & Edge

Somnia's thesis is that **fully on-chain consumer apps** — games where every action, item and state change lives on-chain, plus metaverse and social experiences — require throughput and latency that general-purpose L1s cannot deliver. Most "blockchain games" today keep gameplay off-chain and only settle assets; Somnia targets the harder problem of running the *interactions themselves* on-chain at consumer scale. Value to SOMI is designed to scale with **on-chain transaction volume from real consumer apps** — the open question is whether those apps materialize.

- **MultiStream consensus (claimed)**: the design separates/parallelizes **data production** (many independent validator "streams") from **consensus/ordering**, so transactions can be ingested concurrently and ordered downstream, targeting very high throughput and low latency. Paired with a custom database (**IceDB**) and **compiled-EVM execution** (compiling contracts to native machine code rather than interpreting bytecode).
- **Performance claims (treat as vendor benchmarks)**: the project claims **1,000,000+ TPS with sub-second finality**. These are marketing/lab figures and should be treated as unverified until reproduced under realistic, decentralized, adversarial conditions — sustained decentralized throughput is typically far below lab peaks.
- **EVM compatibility**: lowers porting cost for existing [[ethereum]]/[[solidity]] teams while offering a faster execution environment — a deliberate trade of novelty for developer reach versus non-EVM gaming chains.
- **Consumer/gaming focus**: optimized for the high-frequency, low-value interactions typical of [[gamefi]] and metaverse apps (in-game actions, item transfers, social actions) where mainnet gas and latency are prohibitive.
- **Backing/launch**: SOMI launched in 2025 (associated with a Binance HODLer airdrop / Alpha listing), giving it CEX distribution from the start.

---

## Comparison vs Competing Gaming / High-Throughput L1s

Somnia competes for scarce game-developer and player mindshare against both gaming-specific chains and general high-throughput L1s:

| Dimension | **Somnia (SOMI)** | **Ronin (RON)** | **Immutable (IMX)** | **[[solana]] (SOL)** |
|---|---|---|---|---|
| **Type** | EVM L1 (MultiStream) | EVM gaming L1 (Axie origin) | Ethereum L2 for gaming (zk) | High-throughput L1 |
| **VM** | EVM (compiled) | EVM | zkEVM rollup | SVM (Sealevel) |
| **Headline perf** | "1M+ TPS" (claimed) | High, proven at Axie scale | Inherits Ethereum security | ~Thousands TPS sustained |
| **Proven hit games** | Not yet | Axie Infinity, Pixels | Several titles | Several titles |
| **Edge** | Raw throughput claim | Established game distribution | Ethereum-security + tooling | Broad ecosystem, liquidity |

Somnia's pitch is the **most aggressive raw-performance claim**, but it is the **least proven on real adoption** — [[ronin]] and Immutable already host live games with real users, and Solana offers a deep, liquid ecosystem. In gaming, distribution and a hit title matter more than benchmark TPS, which is Somnia's core challenge. See [[layer-1]] and [[gamefi]].

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 160.20M SOMI |
| **Total Supply** | 1.00B SOMI |
| **Max Supply** | 1.00B SOMI |
| **Fully Diluted Valuation** | $160.60M |
| **Market Cap / FDV Ratio** | 0.16 |

A ~0.16 cap/FDV ratio means only ~16% of the 1B max supply circulates — the **lowest float in this batch**, alongside [[caldera|ERA]]. The remaining ~84% (team, investors, ecosystem, airdrop tranches) represents a heavy **unlock overhang**: SOMI's price is structurally pressured by future supply regardless of fundamentals, and trades below its prior recorded ATL. Contrast fair-launch [[ergo|ERG]] (no unlocks).

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.84 (2025-09-07) |
| **Current vs ATH** | -91.28% |
| **All-Time Low** | $0.109955 (2026-06-21) |
| **24h Change (2026-06-21)** | -0.95% |
| **7d Change (2026-06-21)** | -1.31% |

> *Earlier 30d/1y figures from the 2026-06-12 snapshot are superseded by the 2026-06-21 figures above. SOMI's 2026-06-21 price ($0.109955) sits below the prior recorded ATL, reflecting a deep drawdown (~94%) from its 2025-09 ATH of $1.84.*

---

## SOMI Token

SOMI is the native [[layer-1]] coin of Somnia (total/max supply 1B; ~160M circulating, so most supply remains locked/unvested). It is used to:

- **Pay gas** for transactions and [[smart-contracts]] on the Somnia chain;
- **Stake / secure** the network (validator and delegation economics);
- **Govern** protocol parameters.

The low circulating-to-total ratio (~16%) means future unlocks are a significant supply overhang.

---

## How & Where It Trades

- **Spot venues:** SOMI has strong CEX distribution from its Binance launch — **Binance** (SOMI/USDT), **Kraken** (SOMI/USD), **Upbit** (SOMI/KRW), **Bitget** and **KuCoin** (SOMI/USDT). As a native L1 coin it is the chain's gas token rather than an ERC-20.
- **Liquidity profile:** ~$5.3M reported 24h volume against a ~$17.6M cap. The Binance + Upbit listings give SOMI broader reach than most tokens this size, but it remains a thin small-cap dominated by supply/unlock dynamics and speculative flow. CoinGecko sentiment was 100% positive in the earlier snapshot — a contrarian caution flag for a token down ~94%.
- **Derivatives:** as a Binance-listed token, SOMI-USDT perpetuals are generally available; OI is modest. Primarily a spot/unlock-driven name; perp shorts carry small-cap gap risk.
- **Korea + airdrop dynamics:** the Upbit KRW pair can drive sharp Korea-led moves, and HODLer-airdrop recipients realizing allocations add persistent sell pressure.

---

## Narrative, Category & Catalysts

Somnia rides the **gaming / metaverse / consumer L1** narrative with a **raw-performance ("1M+ TPS")** hook. It is a "build the high-performance rails and the games will come" bet — historically a difficult thesis, as gaming L1s have repeatedly struggled to convert technical capability into durable players.

**Potential catalysts:**
- **A real hit game or breakout consumer app** shipping on Somnia with genuine, retained users — by far the most important driver.
- Independent verification of throughput claims under realistic conditions (would de-risk the technical story).
- A broad **GameFi / metaverse narrative** revival lifting the category.
- Mainnet maturity, ecosystem grants, and notable studio partnerships.

**Headwinds:**
- **Heavy unlock overhang** (~84% of supply still locked) into a bear market.
- The recurring failure of gaming L1s to attract durable users ("build-it-and-they-will-come" risk).
- Crowded field competing with [[ronin]], Immutable, [[solana]] and many app-chains for scarce developer/player mindshare.
- Unverified performance claims that may disappoint under real, decentralized load.

---

## Platform & Chain Information

**Native Chain:** Own blockchain (Layer 1)

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | SOMI/USDT | N/A |
| Kraken | SOMI/USD | N/A |
| Upbit | SOMI/KRW | N/A |
| Bitget | SOMI/USDT | N/A |
| KuCoin | SOMI/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://somnia.network/](https://somnia.network/) |
| **Twitter** | [@somnia_network](https://twitter.com/somnia_network) |
| **Telegram** | [somnianetwork](https://t.me/somnianetwork) (83,552 members) |
| **Discord** | [https://discord.com/invite/somnia](https://discord.com/invite/somnia) |
| **Whitepaper** | [https://docs.somnia.network/](https://docs.somnia.network/) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $5.27M |
| **Market Cap Rank** | #879 |
| **24h Range** | $0.1594 — $0.1654 |
| **CoinGecko Sentiment** | 100% positive |
| **Last Updated** | 2026-04-09 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## History & Timeline

| Date | Event |
|---|---|
| **2025-09-07** | All-time high of **$1.84** around the token's launch / listing. |
| **2025** | SOMI launches via a **Binance HODLer airdrop / Alpha listing**, giving immediate CEX distribution. |
| **2025–2026** | ~94% drawdown from ATH as unlocks meet a weakening market and consumer adoption lags the technical roadmap. |
| **2026-06-21** | Recorded all-time low of **$0.109955**, below the prior ATL, reflecting continued unlock-driven drawdown. |

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Risks

> *Not investment advice. Crypto assets are highly volatile and can go to zero.*

**Technical / protocol**
- **Unverified performance claims**: the headline "1M+ TPS" is a vendor benchmark; real-world, decentralized throughput and the security tradeoffs of the MultiStream design are not independently confirmed here.

**Adoption / economic**
- **"Build-it-and-they-will-come" risk**: gaming and metaverse L1s have repeatedly struggled to attract durable users and hit games; SOMI's value hinges on **real consumer apps shipping and retaining players**, which has not yet been demonstrated.
- **Crowded gaming-L1 field**: competes with [[ronin]], Immutable, [[solana]] and many app-chains for the same scarce developer and player mindshare.

**Market / supply**
- **Deep drawdown + severe unlock overhang**: SOMI is down ~94% from its 2025 ATH, and only ~16% of supply circulates, so token unlocks are a **sustained, structural headwind** — the dominant near-term driver.
- **Airdrop sell pressure + contrarian sentiment**: HODLer-airdrop realization plus uniformly positive retail sentiment on a token down ~94% are caution flags.

**Liquidity**
- **Micro-cap liquidity**: at ~$17.6M and rank #883, the token is thin and volatile despite its Binance listing.

---

## Trading Playbook

> *Educational framing, not advice.*

- **Regime read (2026-06-22):** Established Bear Market, Extreme Fear (F&G 21). SOMI is at/near all-time lows, driven by **unlock supply** and the absence of proven adoption — a fundamentally weak setup that the broad risk-off only amplifies.
- **What to watch (bullish):** a genuine **hit game / breakout consumer app** with retained users (the only catalyst that really matters), independent verification of throughput claims, and a GameFi/metaverse narrative revival.
- **What to watch (bearish):** the **unlock calendar** (~84% locked — track it), continued lack of flagship apps, fading Korea/Binance flow, and new BTC lows dragging small caps.
- **Mechanics:** Binance + Upbit listings give decent liquidity and make a perp short feasible, but gap risk is high and sentiment is one-sided. For longs, the unlock overhang plus unproven adoption argue for small size and patience; the asymmetric upside is entirely contingent on a real consumer app landing.

---

## Trading Profile

### Venues & liquidity

SOMI is tradable on **Binance** — both **spot** (SOMI/USDT) and a **USD-margined perpetual** with funding, open interest, and liquidation data. It is **NOT listed on Hyperliquid**, so **Binance is the primary leveraged venue** and effectively the reference market for both spot price discovery and derivatives. This single-venue concentration for perps means funding, OI, and liquidation signals should be read from Binance rather than aggregated across DEX perps. With a micro-cap footprint and thin depth, leverage availability does not imply deep leveraged liquidity: order-book slippage and gap risk are high, so size positions small, favor limit execution over market fills, and treat any perp short as carrying meaningful small-cap gap/squeeze risk. Additional Korea-led flow via the Upbit KRW spot pair can front-run Binance moves.

### Applicable strategies

- [[token-unlock-supply-event]] — ~84% of the 1B supply is still locked; scheduled unlocks are the dominant structural driver, making the unlock calendar the key edge for positioning around supply cliffs.
- [[liquidation-cascade-fade]] — thin depth plus Binance perp leverage makes SOMI prone to violent liquidation wicks at/near all-time lows, offering fade opportunities into forced-seller exhaustion.
- [[crowded-long-funding-fade]] — one-sided retail positioning (100% positive sentiment on a token down ~94%) can push funding positive, setting up fades of crowded longs when funding overheats.
- [[narrative-trading]] — SOMI trades on the GameFi/metaverse "1M+ TPS" narrative and hit-game catalysts; positioning around narrative revivals or milestone news is a primary discretionary edge.
- [[breakout-and-retest]] — sitting below its prior ATL, SOMI is range-compressed; breakouts from established ranges with a retest confirmation help filter the many failed moves typical of a thin small-cap.
- [[volatility-targeting]] — extreme, unlock-driven volatility argues for sizing inversely to realized vol so position risk stays bounded across regime shifts.

### Volatility & regime character

SOMI is a **micro-cap, high-beta [[gamefi]] / consumer L1 token** (~rank #918, ~$17M cap) with extreme reflexive volatility driven far more by **unlock supply and speculative flow** than by fundamentals. It behaves as a high-beta risk asset: it amplifies BTC/ETH risk-on/risk-off swings on the way up but is dominated by idiosyncratic supply overhang on the way down. Correlation to majors is real but secondary to unlock mechanics and narrative cycles; expect memecoin-like reflexivity and one-sided sentiment despite the infra/gaming framing.

### Risk flags

- **Venue concentration:** Binance is the primary (effectively sole major) leveraged venue; no Hyperliquid presence means limited cross-venue perp liquidity and single-exchange dependence for derivatives signals.
- **Unlock / emissions overhang:** only ~16% of the 1B max supply circulates — a sustained, structural sell-pressure headwind that dominates near-term price.
- **Micro-cap liquidity:** thin depth (~$5M 24h volume vs ~$17M cap) means high slippage, gap risk, and squeeze potential on both long and short perps.
- **Narrative dependence:** value hinges on an unproven "build-it-and-they-will-come" GameFi thesis; without a retained hit game, the story can fade fast.
- **Airdrop sell pressure:** HODLer-airdrop recipients realizing allocations add persistent, ongoing supply.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=SOMIUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=SOMIUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=SOMI` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=SOMI` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=SOMIUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=SOMIUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=SOMI"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[layer-1]]
- [[ethereum]]
- [[smart-contracts]]
- [[gamefi]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- General market knowledge; no specific wiki source ingested yet.

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---
