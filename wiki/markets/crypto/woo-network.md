---
title: "WOO Network"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, derivatives, perpetual-futures, funding-rate, open-interest, liquidations, altcoins]
aliases: ["WOO", "WOO X", "WOOFi"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://woo.org"
related: ["[[automated-market-maker]]", "[[binance]]", "[[centralized-exchange]]", "[[crypto-markets]]", "[[decentralized-exchange]]", "[[ethereum]]", "[[funding-rate]]", "[[funding-rate-harvest]]", "[[liquidity]]", "[[liquidation-cascade-fade]]", "[[market-maker]]", "[[perpetual-futures]]", "[[slippage]]"]
---

# WOO Network

**WOO Network** (WOO) is a liquidity and trading network spanning both centralized and decentralized venues, best known for **WOOFi** (its on-chain spot and perpetuals [[decentralized-exchange|DEX]]) and **WOO X** (its centralized orderbook exchange). Its defining feature is a deep, professionally market-made liquidity layer that is shared across products and partners, with the goal of delivering tight [[slippage|spreads]] and low [[slippage]]. As of 2026-06-22 WOO trades at **$0.01280738**, ranking **#737** by market capitalization with a market cap of roughly **$24.19M**.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko). Price $0.01280738 · rank #737 · market cap $24,185,936 · 24h -1.57% · 7d -5.09%. Market-wide sentiment: Fear & Greed Index 21 (Extreme Fear).*

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | WOO |
| **Market Cap Rank** | #737 |
| **Market Cap** | ~$24.19M |
| **Current Price** | $0.01280738 |
| **24h Change** | -1.57% |
| **7d Change** | -5.09% |
| **Products** | WOOFi (on-chain DEX, spot + perps), WOO X (CEX) |
| **Backers** | DragonFly Capital, YZi Labs (formerly Binance Labs) |
| **Founder** | Kronos Research (quantitative trading firm) |
| **Categories** | Decentralized Exchange (DEX), Exchange-based Tokens, DeFi, Automated Market Maker (AMM), Derivatives, Perpetuals, CEX Token, multi-chain (BNB Chain, Solana, Avalanche, Polygon, Arbitrum, Ethereum, Base, and others) |
| **Website** | [https://woo.org](https://woo.org) |

> Against an [[crypto-market-regime|Extreme-Fear backdrop]] (Fear & Greed Index 21 on 2026-06-22), WOO slipped -1.57% over 24h and -5.09% on the week, tracking the broad mid-cap DeFi tape lower as risk appetite contracted.

---

## Overview

WOO Network was founded by **Kronos Research**, a quantitative trading firm, with the original premise of channeling institutional-grade market-making liquidity into both centralized and decentralized trading products. The ecosystem has two main faces:

- **WOO X** — a centralized exchange offering spot and derivatives trading with deep liquidity sourced from professional market makers.
- **WOOFi** — the on-chain, non-custodial arm: a multi-chain [[decentralized-exchange|DEX]] supporting token **swaps**, **perpetual futures** ([[perpetual-futures|perps]]), staking, and yield. WOOFi's swap engine uses a proprietary **sPMM (synthetic Proactive Market Maker)** design rather than a pure constant-product [[automated-market-maker|AMM]], pricing trades against an off-chain oracle/market-maker quote to achieve lower [[slippage]] than a conventional pool of equivalent depth.

The **WOO token** is the network's utility and incentive asset: it is used for **staking** (which can unlock fee rebates, boosted yields, and platform tiers), **liquidity incentives**, and **governance**. WOOFi Earn and staking vaults let holders earn yield, while staked WOO has historically supported a buyback/value-accrual narrative tied to platform revenue.

> **Note on prior draft:** an earlier version of this page described a "Starchild" AI agent / "vibe trading" platform. WOO Network's established, verifiable products are WOOFi and WOO X as described above; any AI-agent feature claims could not be confirmed and have been removed to keep the page accurate. Update only if a reliable source is ingested.

---

## Mechanism & Architecture: the sPMM

A conventional constant-product [[automated-market-maker|AMM]] such as [[uniswap]] V2 prices trades purely from on-chain pool reserves along a fixed `x*y=k` curve. Depth is set by however much capital LPs have deposited, and slippage rises mechanically with trade size — a thinly funded pool quotes badly even when the true market price is well known elsewhere. WOOFi's **synthetic Proactive Market Maker (sPMM)** breaks that coupling:

1. **Oracle anchor** — the curve is centred on an off-chain mid-price fed in by professional [[market-maker|market makers]] (Kronos and partners), refreshed continuously rather than implied from stale reserves.
2. **Active inventory management** — quotes shift proactively as the market maker's inventory and the reference price move, in the spirit of [[dodo|DODO]]'s PMM but driven by a live trading desk rather than a static `k` parameter.
3. **Capital concentration** — liquidity is concentrated tightly around the oracle mid, so a small notional of capital can quote CEX-like depth at the touch, achieving lower [[slippage]] than a constant-product pool many times its size.

The trade-off is explicit: sPMM execution quality is only as good as the off-chain quote and the oracle feed. If the price feed lags or is manipulated, or the market maker withdraws, the curve degrades — the structural vulnerability behind WOOFi's past oracle exploit (see Risks).

### Worked example (illustrative)

A trader swaps 50,000 USDC into a mid-cap token on WOOFi. The sPMM reads the live oracle mid (say $2.00) and quotes around it; because liquidity is concentrated at the mid, the fill clears near $2.001 — an effective slippage of a few basis points. The same 50,000 USDC routed through a shallow constant-product pool holding only $300k of depth might move the marginal price several percent, producing a materially worse average fill. The numbers are illustrative; the point is the *shape* of the advantage — sPMM converts an off-chain market-maker quote into on-chain depth.

---

## Comparison vs Competitors

| Protocol | Core model | Spot / Perps | Distinctive edge | Primary risk |
|---|---|---|---|---|
| **WOO Network (WOOFi/WOO X)** | sPMM (oracle + MM quote), hybrid CeFi/DeFi | Both | Shared "liquidity-as-a-service" across many chains and partner front-ends | Oracle / market-maker dependence |
| [[dodo\|DODO]] | Proactive Market Maker (PMM), oracle-anchored | Spot | Single-token LP, CEX-like depth near mid | Oracle dependence |
| [[joe\|Trader Joe / LFJ]] | Liquidity Book (discrete-bin concentrated AMM) | Both | Zero-slippage bins, dynamic fees | Avalanche ecosystem concentration |
| [[gmx\|GMX]] | Oracle-priced shared liquidity (GLP/GM pools) | Perps (+ spot) | Zero-slippage oracle execution vs a pooled counterparty | LP exposed to trader PnL; oracle risk |
| [[hyperliquid\|Hyperliquid]] | On-chain central limit order book (own L1) | Perps (+ spot) | Full on-chain CLOB at CEX-like speed | Validator/sequencer centralization |
| [[dydx\|dYdX]] | Order book (app-chain) | Perps | Mature perps order book | Liquidity vs newer venues |

WOO's positioning is less "best perp DEX" and more **liquidity infrastructure**: the same sPMM book is exposed across BNB Chain, Solana, Arbitrum, Base, Avalanche, Polygon and others, and can be embedded into third-party front-ends — a breadth unusual for a protocol of its market-cap size.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | ~1.89B WOO |
| **Total Supply** | ~3.00B WOO |
| **Max Supply** | 3.00B WOO |
| **Fully Diluted Valuation** | ~$38M (scales with price) |
| **Market Cap / FDV Ratio** | ~0.64 |

The WOO token has a fixed maximum supply of 3 billion. A meaningful portion of the value-accrual story has historically depended on platform revenue funding buybacks and on staking demand reducing circulating float.

### Governance & value accrual

- **Staking tiers** — staking WOO unlocks fee rebates, higher [[woofi-earn|WOOFi Earn]] yields, and platform tiers on WOO X; it also functions as the gate to the network's loyalty/benefits programs.
- **Buyback-and-burn narrative** — the protocol has historically directed a slice of trading-fee revenue toward open-market WOO buybacks, tying token value to platform volume. Like all revenue-linked accrual, this strengthens in high-volume regimes and weakens when activity falls (as in the current Extreme-Fear tape).
- **Governance** — WOO holders participate in protocol governance over parameters and incentive allocation.

The core dependency is reflexive: more volume → more fees → more buybacks/staking demand → tighter float, and the reverse in downturns. At a ~$24M market cap with FDV ~$38M (MC/FDV ≈ 0.64), there is meaningful remaining float to absorb before supply pressure eases.

---

## History & Notable Events

- **2019–2020** — WOO Network founded by **Kronos Research**, a quantitative trading firm, with the premise of channelling institutional [[market-maker|market-making]] liquidity into both CeFi and DeFi venues.
- **2021** — WOO X (then WOO Trade / WOO X) and the WOO token gained traction during the bull market; WOO reached its all-time high of **$1.78 on 2021-11-15**.
- **2022** — WOOFi launched as the on-chain arm with the sPMM swap engine, expanding rapidly across chains (BNB Chain, Avalanche, Arbitrum, Polygon and more).
- **2023** — **WOOFi suffered an oracle/price-manipulation exploit** on one supported chain, draining a pool by feeding the sPMM a distorted reference price — a direct demonstration of the model's oracle dependence. Affected liquidity was partly addressed by the team.
- **2023–2024** — Added WOOFi Pro / perpetuals and continued multi-chain rollout (Solana, Base); deepened the "liquidity-as-a-service" partner-integration model.
- **2025–2026** — Operating through the bear regime as a broad multi-chain mid-cap; WOO trades ~99% below its cycle high.

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.78 (2021-11-15) |
| **Current vs ATH** | ~-99% |
| **24h Change** | -1.57% |
| **7d Change** | -5.09% |

WOO trades roughly 99% below its 2021 cycle high, in line with the deep multi-year drawdown across exchange and DeFi tokens. Price action into 2026-06-22 was soft (-1.57% on the day, -5.09% on the week), tracking the broader Extreme-Fear, risk-off market.

---

## Competitive Position

WOOFi competes with other on-chain perp/spot DEXs ([[gmx|GMX]], [[dydx|dYdX]], [[hyperliquid|Hyperliquid]], [[joe|Trader Joe]]) and aggregators, while WOO X competes with mid-tier centralized exchanges. WOO's differentiator is its **liquidity-as-a-service** model — pooling professional market-maker liquidity and exposing it across many chains and partner front-ends via the sPMM. Its multi-chain footprint (BNB Chain, Solana, Arbitrum, Base, Avalanche, Polygon, and more) is unusually broad for a protocol of its size.

---

## Risks

- **Market-maker / oracle dependence:** WOOFi's sPMM relies on off-chain quotes and oracle pricing; oracle manipulation or market-maker withdrawal can degrade execution. WOOFi suffered an oracle/price-manipulation exploit on one chain in the past, underscoring this dependency.
- **Centralization surface:** The hybrid CeFi/DeFi model means parts of the stack (WOO X, liquidity provisioning) are not trustless.
- **Revenue-dependent value accrual:** Buyback/staking narratives weaken when trading volumes fall.
- **Competition & commoditization:** Perp DEX liquidity is highly competitive; spreads and incentives can compress margins.
- **Smart-contract risk** across many supported chains widens the attack surface.

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x4691937a7508860f876c9c0a2a617e7d9e945d4b` |
| Fantom | `0x6626c47c00f1d87902fc13eecfac3ed06d5e8d8a` |
| Linea | `0xf3df0a31ec5ea438150987805e841f960b9471b6` |
| Mantle | `0xf3df0a31ec5ea438150987805e841f960b9471b6` |
| Solana | `Dz8VutERqbHR2aFL5A3s1Ky4dG1unJT1jUFXXPaY9ytX` |
| Near Protocol | `4691937a7508860f876c9c0a2a617e7d9e945d4b.factory.bridge.near` |
| Zksync | `0x9e22d758629761fc5708c171d06c2fabb60b5159` |
| Polygon Pos | `0x1b815d120b3ef02039ee11dc2d33de7aa4a8c603` |
| Binance Smart Chain | `0x4691937a7508860f876c9c0a2a617e7d9e945d4b` |
| Arbitrum One | `0xcafcd85d8ca7ad1e1c6f82f651fa15e33aefd07b` |
| Avalanche | `0xabc9547b534519ff73921b1fba6e672b5f58d083` |
| Base | `0xf3df0a31ec5ea438150987805e841f960b9471b6` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | WOO/USDT | N/A |
| Kraken | WOO/EUR | N/A |
| Bitget | WOO/USDT | N/A |
| KuCoin | WOO/USDT | N/A |
| Crypto.com Exchange | WOO/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V2 (Ethereum) | 0X4691937A7508860F876C9C0A2A617E7D9E945D4B/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |
| Sushiswap | 0X4691937A7508860F876C9C0A2A617E7D9E945D4B/0XA0B86991C6218B36C1D19D4A2E9EB0CE3606EB48 | Spot |
| Uniswap V3 (Ethereum) | 0X4691937A7508860F876C9C0A2A617E7D9E945D4B/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://woo.org](https://woo.org) |
| **Twitter** | [@WOO_ecosystem](https://twitter.com/WOO_ecosystem) |
| **Telegram** | [woo_english](https://t.me/woo_english) (9,619 members) |
| **Discord** | [https://discord.com/invite/woonetwork](https://discord.com/invite/woonetwork) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $9.10M |
| **Market Cap Rank** | #726 |
| **24h Range** | $0.0174 — $0.0188 |
| **Last Updated** | 2026-04-09 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Trading Profile

### Venues & liquidity

WOO is tradable on **Binance** — both **spot** (WOO/USDT) and a **USD-margined perpetual**, which exposes live **funding**, **open interest**, and **liquidation** data. It is **not** listed on Hyperliquid, so **Binance is the primary leveraged venue** for WOO; secondary CEX spot books (Kraken, Bitget, KuCoin, Crypto.com) plus WOOFi's own on-chain sPMM add spot depth but no comparable perp analytics. With a sub-$25M market cap and modest 24h volume, WOO is a thin small-cap: order books are shallow, leveraged positions can move price quickly, and funding/OI can swing sharply. Practically, this concentrates all funding-, basis-, and liquidation-based strategies on the Binance USD-M contract, and argues for conservative position sizing, wider slippage assumptions, and staged entries/exits rather than single large market orders.

### Applicable strategies

- [[funding-rate-harvest]] — collect the Binance USD-M perp funding on WOO when it runs persistently positive/negative, sizing for the thin book.
- [[cash-and-carry]] — pair long Binance spot WOO against a short USD-M perp to capture basis/funding while staying delta-neutral.
- [[crowded-long-funding-fade]] — fade over-leveraged longs on WOO when funding spikes positive into extended OI, a common pattern in low-cap perps.
- [[liquidation-cascade-fade]] — small-cap WOO liquidations cluster; fade the forced-selling wick back toward the sPMM/oracle mid.
- [[oi-confirmed-trend]] — use Binance open-interest changes to confirm whether a WOO move is fresh positioning or short-covering before trend entries.
- [[volatility-breakout]] — WOO's low-liquidity tape produces sharp range expansions; trade confirmed breakouts with ATR-scaled stops.

### Volatility & regime character

WOO is a **small-cap DeFi/exchange-infrastructure token** (rank ~#769, ~$24M cap) trading ~99% below its 2021 high. It behaves as a **high-beta risk asset** with strong positive correlation to BTC/ETH: it tends to lag on rallies and overshoot on drawdowns, amplified by its shallow liquidity. Value accrual is **reflexive** — buyback/staking demand strengthens in high-volume regimes and weakens in risk-off tapes (as in the current Extreme-Fear backdrop). It is not a memecoin, but its low float and thin books give it memecoin-like reflexivity on volume spikes.

### Risk flags

- **Liquidity & venue concentration** — thin spot books and a single dominant perp venue (Binance) mean slippage, gap risk, and cascade risk are elevated; no Hyperliquid fallback.
- **Emissions / remaining float** — MC/FDV ≈ 0.64 leaves meaningful supply to unlock, a structural overhang on price.
- **Narrative & revenue dependence** — buyback/staking value accrual is tied to platform volume; falling activity weakens the bid.
- **Protocol / oracle history** — WOOFi's sPMM depends on off-chain quotes and suffered a past oracle-manipulation exploit; headline protocol risk can spill into WOO token pricing.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=WOOUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=WOOUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=WOO` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=WOO` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=WOOUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=WOOUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=WOO"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[decentralized-exchange]]
- [[automated-market-maker]]
- [[perpetual-futures]]
- [[liquidity]]
- [[defi]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko). Fear & Greed Index 21 (Extreme Fear).
- General market knowledge; no additional specific wiki source ingested yet.
