---
title: "Metal DAO"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [altcoins, crypto, payments, perpetual-futures, funding-rate, open-interest, liquidations, derivatives]
aliases: ["MTL", "Metal Pay", "Metallicus"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.metalpay.com/"
related: ["[[crypto-markets]]", "[[governance-token]]", "[[payments]]", "[[stablecoin]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[funding-rate-harvest]]", "[[liquidation-cascade-fade]]"]
---

# Metal DAO

**Metal DAO** (ticker **MTL**) is the governance and utility token associated with **Metal Pay**, a consumer [[payments]] and crypto-rewards application built by the U.S. fintech studio **Metallicus**. MTL governs the stablecoin **Metal Dollar (XMD)** and provides tiered fee discounts to holders who buy and sell crypto inside the Metal Pay app. The token trades on the **Metal L2** chain (an ERC-20-style asset, also liquid on Ethereum DEXs). As of 2026-06-21 MTL trades at **$0.249498**, ranking **#764** by market capitalization (~**$22.6M**).

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

At current levels MTL was up **+1.35%** over 24 hours but down **-1.87%** over the trailing week, broadly in line with a risk-off market (BTC ~$64,180; Fear & Greed Index 22 / Extreme Fear).

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | MTL |
| **Market Cap Rank** | #764 |
| **Market Cap** | $22,610,173 |
| **Current Price** | $0.249498 |
| **24h Change** | +1.35% |
| **7d Change** | -1.87% |
| **Categories** | Payments, Made in USA |
| **Website** | [https://www.metalpay.com/](https://www.metalpay.com/) |
> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

---

## Overview

Metal Pay was developed and launched by **Metallicus** in 2016 as a peer-to-peer money app that lets users send and receive cash and cryptocurrency. Its original distribution mechanism, **Proof-of-Processed-Payments (PoPP)**, rewarded users with MTL tokens for making real payments — an early attempt to bootstrap a [[payments]] network by paying people to transact rather than to mine or stake. Metallicus later expanded into infrastructure with the **Metal Blockchain**, an Avalanche-derived, compliance-focused chain aimed at banks and regulated fintechs.

MTL itself functions as a [[governance-token]] and loyalty token rather than a base-layer gas asset. Its principal roles are:

- **Stablecoin governance** — MTL holders govern the **Metal Dollar (XMD)** [[stablecoin]], including the composition of its backing basket and the admission of new stablecoin issuers (e.g., community banks or fintechs).
- **Fee discounts** — Holding MTL grants tiered reductions on in-app crypto trading fees; large holders historically qualified for zero-fee purchases.

This positions Metal DAO at the intersection of consumer [[payments]], rewards, and stablecoin governance, rather than as a general smart-contract platform.

---

## Architecture — How the Stack Fits Together

Metallicus operates three layers that MTL ties together:

1. **Metal Pay (consumer app).** The front end — a P2P money and crypto app where users buy/sell crypto and send cash. This is where MTL's fee-discount utility is consumed and where PoPP originally distributed tokens.
2. **Metal Blockchain (infrastructure).** An **Avalanche-derived**, compliance-oriented chain (subnet architecture, KYC/AML-aware) aimed at banks, fintechs, and regulated issuers — the institutional play distinct from the consumer app.
3. **Metal Dollar / XMD (stablecoin).** A stablecoin whose backing basket and issuer admissions are subject to **MTL holder governance**, intended to let multiple regulated entities (e.g. community banks) issue against shared rails.

MTL's value thesis depends on demand flowing through all three: app users wanting fee discounts, and governance demand from XMD's adoption by issuers. The central open question is whether infrastructure usage (Metal Blockchain, XMD) accrues value to MTL or whether MTL remains primarily a consumer discount/governance coupon.

---

## Tokenomics & Value Accrual

| Metric | Value |
|---|---|
| **Circulating Supply** | 90.64M MTL |
| **Total Supply** | 90.64M MTL |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $25.63M |
| **Market Cap / FDV Ratio** | 1.00 |

With MC/FDV ≈ 1.00, there is little hidden supply overhang — most tokens are already circulating, so dilution risk is low relative to tokens with large locked allocations. **Value accrual** runs through (a) fee-discount demand from active Metal Pay traders and (b) governance demand tied to XMD adoption. Neither is a hard fee-capture mechanism, so MTL's value is more "utility/loyalty coupon" than "cash-flow claim" — a structural weakness if app usage stalls.

---

## Comparison vs Other Payments / Exchange-Utility Tokens

MTL competes in the crowded consumer-payments-token niche, where the loyalty/discount model is under pressure from tokenless mainstream fintechs.

| Token | Backing app / chain | Token role | Distinguishing trait |
|---|---|---|---|
| **MTL** (Metal DAO) | Metal Pay / Metal Blockchain | Fee discounts + XMD governance | U.S.-domiciled, compliance-oriented; stablecoin-governance angle |
| **[[crypto-com-coin|CRO]]** (Cronos) | Crypto.com app / Cronos chain | Fee discounts, staking, card tiers | Much larger consumer app + card program; broader utility |
| **[[binance-coin|BNB]]** (BNB Chain) | Binance / BNB Chain | Fee discounts, gas, launchpad | Exchange-backed mega-cap; the archetype of the fee-discount token |
| **[[pax-dollar|USDP]] / similar** | — | Stablecoin | XMD's peers as a governed stablecoin product |

MTL's defensible angle is **regulatory positioning** — a U.S. team building compliance-oriented infrastructure for banks and fintechs — rather than scale. Against exchange-backed tokens (CRO, BNB) it is tiny and lacks a comparably large consumer funnel.

---

## How & Where It Trades / Where It's Used

- **Centralized exchanges.** Liquid on **Binance** (MTL/USDT), **Upbit** (MTL/KRW), **Bitget** (MTL/USDT), and **KuCoin** (MTL/USDT) — notably strong Korean-market presence via Upbit.
- **DEX liquidity.** **Uniswap V2/V3 (Ethereum)** against USDC/WETH.
- **Where it's used.** Inside Metal Pay for fee discounts and in XMD governance; MTL is also held speculatively, with most volume on CEXs rather than in-app.

---

## Narrative, Category & Catalysts

MTL sits in the **payments + stablecoin-infrastructure** narrative. Catalysts:

- **U.S. stablecoin regulation.** A clearer U.S. stablecoin regime could benefit XMD and, by extension, MTL's governance demand — though regulation cuts both ways.
- **Metal Blockchain / institutional adoption.** Banks or fintechs adopting Metal Blockchain or issuing via XMD would be the structural catalyst that moves value toward MTL.
- **Metal Pay growth.** Active-trader growth increases fee-discount demand.
- **Caveat.** In an Extreme-Fear bear regime (2026-06-22), small-cap payments tokens with long downtrends face weak demand and elevated drawdown risk.

---

## History / Timeline

- **2016** — Metallicus launches Metal Pay as a P2P money app.
- **2017** — The MTL token launches (ICO-era), with Proof-of-Processed-Payments (PoPP) rewarding payments with MTL.
- **2018-06-21** — MTL records its all-time high of **$17.03** during the original ICO-era altcoin cycle.
- **2020-03-13** — MTL records its all-time low of **$0.1173** (COVID crash).
- **Later** — Metallicus pivots toward infrastructure with the **Metal Blockchain** (Avalanche-derived, compliance-focused) and the **XMD** stablecoin, seeking durable utility beyond the rewards mechanic.

The token has since fallen more than 98% from its 2018 all-time high, mirroring the fate of most first-cycle payments tokens.

---

## Competitive Position

Crypto-rewards [[payments]] apps occupy a crowded and difficult niche. Metal Pay competes for mindshare against far larger consumer on-ramps such as exchange-backed apps (Coinbase, Binance) and fintech incumbents (PayPal, Cash App, Revolut), most of which now offer crypto buying without requiring a separate loyalty token. The defensible angle for Metallicus is regulatory positioning — a U.S.-domiciled team building compliance-oriented infrastructure (Metal Blockchain, XMD) for banks and fintechs. Whether MTL accrues value from that infrastructure, versus serving mainly as a discount/governance coupon, remains the central open question for the token.

---

## Risks

- **Utility concentration** — MTL's value is tied to Metal Pay app usage and XMD governance; if app adoption stalls, fee-discount and governance demand are thin.
- **Competitive pressure** — Mainstream fintechs offer crypto purchasing without a native token, undercutting the rewards model.
- **Liquidity and microcap volatility** — At a ~$22.6M market cap and modest daily volume, MTL is a small-cap altcoin subject to sharp drawdowns and slippage.
- **Stablecoin/regulatory exposure** — XMD ties part of the thesis to the evolving and uncertain U.S. stablecoin regulatory regime.
- **Long downtrend** — Down ~98% from its 2018 ATH, MTL has shown no sustained recovery across multiple cycles.

This is not investment advice; figures above are point-in-time market data, not a valuation.

---

## Trading / Usage Playbook

- **As a payments-narrative trade:** MTL is a small-cap proxy for the "compliant payments + stablecoin infra" theme; it reacts to U.S. stablecoin-regulation and Metal Blockchain headlines more than to broad crypto beta.
- **Utility use:** Hold MTL for in-app fee discounts only if you trade actively in Metal Pay; otherwise the holding is speculative.
- **Risk control:** Respect the long multi-cycle downtrend (-98% from ATH) and thin liquidity — size small and treat it as high-risk microcap exposure.

---

## Platform & Chain Information

**Native Chain:** Metal L2

### Contract Addresses

| Chain | Address |
|---|---|
| Metal L2 | `0xbcfc435d8f276585f6431fc1b9ee9a850b5c00a9` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | MTL/USDT | N/A |
| Upbit | MTL/KRW | N/A |
| Bitget | MTL/USDT | N/A |
| KuCoin | MTL/USDT | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V2 (Ethereum) | 0XF433089366899D83A9F26A773D59EC7ECF30355E/0XA0B86991C6218B36C1D19D4A2E9EB0CE3606EB48 | Spot |
| Uniswap V3 (Ethereum) | 0XF433089366899D83A9F26A773D59EC7ECF30355E/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.metalpay.com/](https://www.metalpay.com/) |
| **Twitter** | [@metalpaysme](https://twitter.com/metalpaysme) |
| **Reddit** | [https://www.reddit.com/r/MetalPay/](https://www.reddit.com/r/MetalPay/) |
| **Telegram** | [MetalPayCommunity](https://t.me/MetalPayCommunity) (2,114 members) |
| **Discord** | [https://discord.gg/B2QDmgf](https://discord.gg/B2QDmgf) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $1.06M |
| **Market Cap Rank** | #755 |
| **24h Range** | $0.2824 — $0.2971 |
| **Last Updated** | 2026-04-09 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $17.03 (2018-06-21) |
| **Current vs ATH** | -98.34% |
| **All-Time Low** | $0.1173 (2020-03-13) |
| **Current vs ATL** | +140.88% |
| **24h Change** | -2.74% |
| **7d Change** | +1.93% |
| **30d Change** | +6.04% |
| **1y Change** | -57.13% |

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

The MTL token launched in 2017 and peaked near **$17** in mid-2018 during the original ICO-era altcoin cycle. It has since fallen more than 98% from that all-time high, mirroring the fate of most first-cycle payments tokens. The project's later pivots — the Metal Blockchain and the XMD stablecoin — are attempts to find durable utility beyond the original rewards mechanic.

---

## Trading Profile

### Venues & liquidity

MTL is tradable on **[[binance]]** — both **spot** (MTL/USDT) and a **USD-margined perpetual** that exposes [[funding-rate|funding]], **open interest**, and **liquidations** data. It is **NOT listed on Hyperliquid**, so Binance is the primary — effectively the only major — leveraged venue for MTL. This concentration means perp liquidity, order-book depth, and leverage availability all hinge on a single exchange: crowded positioning, funding dislocations, and liquidation cascades tend to originate and resolve on Binance. As a sub-$25M-cap microcap, MTL perp depth is thin, so position sizing should assume meaningful slippage on market orders and treat Binance funding/OI as the definitive read on leveraged flow. Spot liquidity is further fragmented across Upbit (KRW), Bitget, and KuCoin, but derivative exposure is Binance-centric.

### Applicable strategies

- [[funding-rate-harvest]] — collect Binance perp funding when MTL's thin, retail-driven perp skews persistently positive or negative against a hedged spot leg.
- [[crowded-long-funding-fade]] — MTL's small-cap reflexivity produces episodic crowded longs on payments/stablecoin headlines; fade over-extended funding into mean reversion.
- [[liquidation-cascade-fade]] — single-venue Binance concentration and thin depth make MTL prone to sharp liquidation wicks; fade the flush once the cascade exhausts.
- [[cash-and-carry]] — capture spot-perp basis by pairing long Binance spot MTL against the short perp when the term structure pays.
- [[range-mean-reversion]] — outside catalyst windows MTL grinds in defined ranges within its long downtrend, favoring reversion at range extremes.
- [[news-trading]] — MTL reacts more to U.S. stablecoin-regulation and Metal Blockchain/XMD headlines than to broad crypto beta, rewarding fast catalyst-driven entries.

### Volatility & regime character

MTL is a **small-cap altcoin** (rank ~#808, sub-$25M cap) with elevated idiosyncratic volatility and modest daily volume. It behaves as a **payments/stablecoin-infrastructure narrative token** rather than a pure BTC-beta proxy — it can decouple sharply on regulation or Metallicus/XMD news, while still absorbing broad risk-off drawdowns amplified by its microcap size. Its multi-cycle downtrend (~-98% from the 2018 ATH) and low float mean moves are reflexive and mean-reverting rather than trend-persistent, with a strong Korean-retail (Upbit) footprint that can drive volume spikes disconnected from Western sessions.

### Risk flags

- **Venue concentration** — leveraged exposure lives entirely on Binance; a listing change, funding regime shift, or depth withdrawal there dominates MTL's derivative risk.
- **Microcap liquidity** — sub-$25M cap and ~$1M daily volume mean wide spreads, slippage, and outsized wick risk on both spot and perp.
- **Narrative dependence** — value thesis rests on Metal Pay adoption, XMD governance demand, and U.S. stablecoin regulation; catalysts cut both ways and drive gap risk.
- **Regulatory exposure** — the XMD/stablecoin angle ties MTL to an evolving and uncertain U.S. regulatory regime.
- **Structural downtrend** — down ~98% from ATH with no sustained multi-cycle recovery; leveraged longs fight a persistent bearish backdrop.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=MTLUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=MTLUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=MTL` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=MTL` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=MTLUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=MTLUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=MTL"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[payments]]
- [[stablecoin]]
- [[governance-token]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).
- General market knowledge; no additional specific wiki source ingested yet.

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 92.07M MTL |
| **Total Supply** | 92.07M MTL |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $20.60M |
| **Market Cap / FDV Ratio** | 1.00 |

---
