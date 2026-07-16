---
title: "GMX"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, derivatives, hyperliquid, perpetual-futures, funding-rate, open-interest, liquidations, altcoins]
aliases: ["GMX"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://gmx.io/"
related: ["[[arbitrum]]", "[[crypto-markets]]", "[[perpetual-futures]]", "[[hyperliquid]]", "[[funding-rate]]", "[[hl-vs-cex-funding-divergence]]", "[[narrative-trading]]"]
---

# GMX

**GMX** (GMX) is a leading decentralized **perpetual-futures exchange** (perp DEX) that lets users trade 60+ assets with up to 100x leverage directly from a self-custody wallet, with no order book — trades execute against a shared liquidity pool priced by oracles. The protocol is live on [[arbitrum|Arbitrum]], Avalanche, and (more recently) [[solana|Solana]], and the GMX token is the protocol's governance and fee-sharing asset. It is one of the defining on-chain derivatives venues of the [[defi|DeFi]] era.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | GMX |
| **Market Cap Rank** | #374 |
| **Market Cap** | $65.11M |
| **Fully Diluted Valuation** | $65.11M |
| **Current Price** | $6.26 |
| **24h Volume** | $3.41M |
| **24h Change** | +11.97% |
| **7d Change** | +11.60% |
| **All-Time High** | $91.07 (2023-04-18) |
| **All-Time Low** | $5.07 (2026-06-05) |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

GMX is bouncing sharply (+12% on both 24h and 7-day windows) but trades just above a fresh all-time low ($5.07, printed 2026-06-05) and ~93% below its 2023 ATH of $91.07, against an **extreme-fear** backdrop ([[crypto-fear-and-greed-index|Fear & Greed Index]] ≈ 23) and a long-horizon **"Established Bear Market"** regime as of 2026-06-21. As a perp-DEX governance token, GMX's price is sensitive to DeFi trading-volume trends and fee revenue; thin spot turnover (~$3.4M/24h, only ~5% of cap) means the token is easily moved by small flows in both directions.

---

## Technology / Protocol

GMX is an **oracle-priced, order-book-free** [[perpetual-futures|perpetuals]] and spot [[dex|DEX]]. Instead of matching buyers and sellers in a [[order-book|central limit order book]], trades execute at an oracle-fed mark price against a shared pool of liquidity providers who collectively act as the house.

**Liquidity architecture (across two protocol generations):**

| Generation | LP primitive | Mechanism |
|---|---|---|
| **GMX V1** | **GLP** | A single multi-asset basket (BTC, ETH, stablecoins, etc.). LPs mint GLP and earn 70% of trading/swap fees; GLP holders are the counterparty to *all* trader PnL across every market, so they are long the basket and short trader skill. |
| **GMX V2** | **GM pools** | Per-market isolated pools (e.g. ETH/USD GM), each backed by a long-collateral and short-collateral token. Isolating risk per market stops one toxic market from draining the whole book. |
| **GMX V2** | **GLV vaults** | Aggregated vaults that auto-allocate deposits across multiple GM pools, giving passive LPs diversified exposure without picking individual markets. |

**Pricing and risk controls:** GMX V2 introduced **funding fees** (paid by the heavier side of [[open-interest]] to the lighter side) and **price-impact** mechanics (skew-dependent execution pricing) that nudge longs and shorts toward balance, shrinking the directional risk LPs carry versus the V1 GLP design. Borrow fees accrue continuously to LPs. Execution is two-step (request → keeper-executed) using low-latency oracle prices (Chainlink + a custom GMX oracle), which mitigates front-running but exposes the system to oracle staleness in fast markets.

Because GMX is itself a perp venue, it is a natural component of [[perp-dex-aggregation|perp-DEX aggregation]] routing layers that source liquidity across GMX, [[hyperliquid|Hyperliquid]], dYdX and others to find best execution for a given leveraged order.

---

## Tokenomics & Supply

GMX is a low-supply, near-fully-circulating governance/fee token.

| Metric | Value |
|---|---|
| **Circulating Supply** | ~10.42M GMX |
| **Total Supply** | ~10.42M GMX |
| **Max Supply** | 13.25M GMX |
| **Circulating / Max** | ~0.79 |
| **Contract (Arbitrum)** | `0xfc5a1a6eb076a2c7ad06ed22c90d7e710e35ad0a` |
| **Contract (Avalanche)** | `0x62edc0692bd897d2295872a9ffcac5425011c661` |

- **Real-yield fee share:** historically, staked GMX earned a share of protocol trading fees paid in ETH/AVAX (plus escrowed esGMX rewards), making GMX an early poster child for the **"real yield"** narrative — distributing actual revenue rather than inflationary emissions.
- **Liquidity model:** the protocol's liquidity comes from **GM pools** (per-market) and **GLV vaults** (aggregated), which take the other side of trader PnL and earn fees; the prior generation used the multi-asset **GLP** pool (GMX V1).
- **Near-capped float:** with ~78% of max supply circulating, dilution risk is comparatively low for this cohort.

---

## How & Where It Trades

GMX is unusual in this group: **the protocol itself is a perp DEX**, while the GMX governance token trades on both spot venues and external perp markets.

**The GMX protocol (the product):**
- Oracle-priced, order-book-free perpetuals on [[arbitrum|Arbitrum]], Avalanche, and Solana.
- Liquidity providers (GM/GLV/GLP) act as the counterparty to traders; LPs profit when traders lose and pay out when traders win.
- **Funding & price impact:** GMX V2 introduced funding fees and price-impact mechanics that nudge open interest toward balance between longs and shorts, reducing LP directional risk versus V1.

**The GMX token (the asset you trade):**

| Venue | Type | Typical Pair |
|---|---|---|
| Binance | CEX (spot) | GMX/USDT |
| Kraken | CEX (spot) | GMX/USD |
| Bitget / KuCoin | CEX (spot) | GMX/USDT |
| Crypto.com | CEX (spot) | GMX/USD |
| [[hyperliquid\|Hyperliquid]] | Perp DEX | GMX-PERP |

- The GMX token has a perpetual listing on [[hyperliquid|Hyperliquid]] and CEX derivatives desks. As a small-cap DeFi governance token in a downtrend, its perp funding and [[open-interest]] swing with DeFi-sector sentiment; thin spot volume (~$3.4M/24h) means the token itself can be moved by relatively small flows.

---

## Peer Comparison — On-Chain Perp DEXs

| Protocol | Token | Model | Positioning (2026) |
|---|---|---|---|
| **GMX** | GMX | Oracle-priced, GM/GLV pool liquidity (no order book) | Pioneer of pool-based perps; lost share but still a major Arbitrum/Avalanche venue |
| [[hyperliquid\|Hyperliquid]] | HYPE | On-chain CLOB on a purpose-built L1 | Dominant on-chain perp venue by volume and OI |
| dYdX | DYDX | App-chain order book (Cosmos) | Long-running order-book perp DEX; share eroded by Hyperliquid |
| Jupiter Perps | JUP | Oracle/pool model on [[solana\|Solana]] | Leading Solana perp venue, GMX-like LP design |

GMX's structural distinction is its **passive-LP-as-counterparty** design: liquidity providers earn real fees but bear trader PnL, versus order-book venues (Hyperliquid, dYdX) where market makers, not a shared pool, take the other side. This makes GMX simpler for LPs but caps capacity and concentrates directional risk in the pool.

---

## Valuation Framing (qualitative)

- **Real-yield / fee-multiple lens:** GMX historically traded as a claim on protocol trading fees. With cap ≈ FDV (near-full float) and a ~$65M cap, the implied valuation is a low multiple of compressed bear-market fee revenue — cheap if on-chain perp volume recovers, a value trap if [[hyperliquid|Hyperliquid]] keeps taking share.
- **Near-capped supply** (~79% of max circulating) means little structural dilution, so price is driven by *demand and fee growth* rather than emission decay — unlike heavily-locked peers such as [[spark-2|SPK]] or [[huma-finance|HUMA]].
- **High beta to the perp-DEX narrative:** GMX rallies and falls with on-chain leverage demand; the +12% week here is a sentiment bounce off ATL, not a fundamentals re-rate.
- **Key swing factor:** GMX's fortunes hinge on whether pool-based perps can defend a niche against order-book L1s. If perp-DEX aggregation routes meaningful flow back to GMX liquidity, fees re-accelerate.

---

## Use Case / Narrative / Category

GMX is a flagship **perp-DEX / DeFi derivatives** token.

- **Decentralized leverage trading:** lets users take leveraged long/short positions on majors and select alts on-chain, self-custodied, without KYC or a centralized intermediary.
- **Real-yield DeFi:** the fee-sharing design made GMX a reference point for sustainable, revenue-backed token economics during 2022–2023.
- **Categories:** [[defi|DeFi]], Derivatives, [[perpetual-futures|Perpetuals]], [[arbitrum|Arbitrum Ecosystem]], Avalanche Ecosystem. It helped anchor Arbitrum's early DeFi TVL.

---

## Notable History

- **2021:** Launched on [[arbitrum|Arbitrum]] (evolving from the earlier Gambit protocol), pioneering the GLP shared-liquidity perp model.
- **2022–2023:** Rapid growth made GMX one of the highest fee-generating DeFi protocols; GMX token reached its all-time high near $91 (April 2023) on the real-yield narrative.
- **2024:** Rolled out **GMX V2** with isolated GM pools, funding fees, and price-impact mechanics; later expanded toward multichain access and a Solana deployment.
- **2025:** Suffered a notable **exploit/hack** on a V1 contract (a reminder of smart-contract risk in leveraged DeFi), with the protocol working through remediation.
- **2026:** Trading around $6.26 just above a fresh ATL ($5.07, 2026-06-05), deep below the $91 ATH, tracking the broad DeFi-token bear and compressed on-chain trading volumes; a ~12% weekly bounce off lows amid extreme-fear conditions.

---

## Risks

- **Smart-contract & oracle risk:** leveraged DeFi is a prime exploit target; GMX has direct history here, and oracle-priced execution can be gamed or stale in fast markets.
- **LP directional risk:** GM/GLP liquidity providers can take losses when traders are net-right; sustained trader profitability erodes LP returns and protocol attractiveness.
- **Volume/fee dependence:** GMX token value tracks protocol trading volume and fees, which fall sharply in bear markets — exactly the current **extreme-fear, established-bear** regime.
- **Intense competition:** competes with [[hyperliquid|Hyperliquid]] (now the dominant on-chain perp venue), dYdX, and CEX derivatives; perp-DEX market share is fiercely contested.
- **Small-cap liquidity:** thin token volume amplifies volatility on both up and down moves.

> *Risk note: small-cap DeFi derivatives token with direct exploit history and heavy dependence on on-chain trading volume. Leverage and smart-contract risk are core to the thesis.*

---

## Related

- [[crypto-markets]]
- [[arbitrum]]
- [[perpetual-futures]]
- [[defi]]
- [[dex]]
- [[hyperliquid]]
- [[perp-dex-aggregation]]
- [[solana]]
- [[open-interest]]
- [[crypto-fear-and-greed-index]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-21 from cryptodataapi.com / CoinGecko (`raw/data/crypto-loop/coingecko-markets.json`).

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | GMX |
| **Market Cap Rank** | #372 |
| **Market Cap** | $62.22M |
| **Current Price** | $5.96 |
| **Categories** | Decentralized Finance (DeFi), Derivatives, Perpetuals |
| **Website** | [https://gmx.io/](https://gmx.io/) |

---

## Overview

GMX is a leading permissionless onchain exchange, enabling you to trade 70+ assets with up to 100x leverage from your self-custody wallet. The DEX is live on Arbitrum, Avalanche, and Solana, and in the process of enabling multichain access from all popular EVM blockchains. Trading on GMX is facilitated by isolated GM pools and capital-efficient GLV vaults, enabling anyone to provide liquidity and earn fees.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 10.44M GMX |
| **Total Supply** | 10.44M GMX |
| **Max Supply** | 13.25M GMX |
| **Fully Diluted Valuation** | $62.22M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $91.07 (2023-04-18) |
| **Current vs ATH** | -93.44% |
| **All-Time Low** | $5.07 (2026-06-05) |
| **Current vs ATL** | +17.80% |
| **24h Change** | +0.22% |
| **7d Change** | +1.65% |
| **30d Change** | +0.82% |
| **1y Change** | -54.60% |

---

## Platform & Chain Information

**Native Chain:** Arbitrum One

### Contract Addresses

| Chain | Address |
|---|---|
| Arbitrum One | `0xfc5a1a6eb076a2c7ad06ed22c90d7e710e35ad0a` |
| Avalanche | `0x62edc0692bd897d2295872a9ffcac5425011c661` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | GMX/USDT | N/A |
| Kraken | GMX/USD | N/A |
| Bitget | GMX/USDT | N/A |
| KuCoin | GMX/USDT | N/A |
| Crypto.com Exchange | GMX/USD | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://gmx.io/](https://gmx.io/) |
| **Twitter** | [@GMX_IO](https://twitter.com/GMX_IO) |
| **Telegram** | [GMX_IO](https://t.me/GMX_IO) (8,395 members) |
| **Discord** | [https://discord.com/invite/H5PeQru3Aa](https://discord.com/invite/H5PeQru3Aa) |
| **GitHub** | [https://github.com/xvi10/gambit-contracts](https://github.com/xvi10/gambit-contracts) |
| **Whitepaper** | [https://docs.gmx.io/](https://docs.gmx.io/) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $4.15M |
| **Market Cap Rank** | #372 |
| **24h Range** | $5.93 — $6.09 |
| **CoinGecko Sentiment** | 100% positive |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Trading Profile

**Venues & liquidity** — The GMX *token* trades on both [[binance|Binance]] (spot GMX/USDT plus a USD-margined GMX perpetual) and [[hyperliquid|Hyperliquid]] (GMX-PERP, roughly 40–50x max leverage), making it a genuine two-venue derivatives market rather than a single-venue thin-book alt. That said, spot turnover is modest for a small-cap DeFi governance token, so realized depth is thinner than the venue count implies — the two-venue setup mainly helps by giving arbitrageurs a canonical CEX reference against the on-chain HL perp, keeping the mark honest and enabling clean cross-venue funding/basis comparisons. For execution, size in and out patiently: split larger orders, lean on the deeper Binance book for the spot leg, and treat the HL perp as the leverage/short-side venue. Venue redundancy reduces single-venue gap risk but does not remove the small-cap slippage penalty on aggressive market orders.

**Applicable strategies**
- [[hl-vs-cex-funding-divergence]] — GMX runs on both a Binance USD-margined perp and the HL GMX-PERP, so funding can diverge between the CEX desk and the on-chain venue; capture the spread by going long the cheap-funding side and short the rich-funding side.
- [[funding-rate-harvest]] — as a high-beta DeFi token that pushes to crowded directional extremes on sentiment swings, GMX perp funding can run persistently one-sided, letting a delta-hedged position collect carry.
- [[cash-and-carry]] — with liquid spot on Binance and a perp on both venues, long spot / short perp locks the basis when the GMX perp trades at a premium during DeFi-narrative pumps.
- [[liquidation-cascade-fade]] — thin small-cap depth plus up-to-50x HL leverage makes GMX prone to over-extended liquidation flushes; fading the wick after forced selling exhausts targets the mechanical rebound.
- [[oi-price-exhaustion]] — pairing [[open-interest]] with price on a low-float token flags exhausted crowded positioning where a leveraged move is running out of fuel and vulnerable to reversal.
- [[narrative-trading]] — GMX price is tightly coupled to the on-chain perp-DEX / real-yield narrative and DeFi-sector rotations, so trading the narrative cycle (aggregation flow, fee recovery, Hyperliquid share shifts) is a core alpha driver.

**Volatility & regime character** — GMX behaves as a high-beta DeFi / perp-DEX infrastructure token: a small-cap ($60–65M) governance asset with near-full float, so price is driven by demand and on-chain trading-volume trends rather than emission decay. It is strongly correlated to broad DeFi-sector risk appetite and carries elevated beta to BTC/ETH — amplifying both up- and down-moves versus large caps — and reacts sharply to shifts in on-chain leverage demand and perp-DEX market-share narratives. Expect reflexive, sentiment-driven swings (e.g. the +12% bounce off a fresh ATL under extreme-fear conditions) rather than orderly large-cap ranges.

**Risk flags**
- **Small-cap liquidity / venue concentration** — thin spot turnover (~single-digit $M/24h) means aggressive orders move price; a stress event on Binance or Hyperliquid concentrates flow onto the remaining venue and widens spreads.
- **Narrative dependence** — value tracks the perp-DEX / real-yield story and on-chain fee revenue; a loss of DeFi-derivatives share (notably to Hyperliquid) can de-rate the token regardless of BTC.
- **Perp funding dislocations** — with up-to-50x HL leverage and crowded directional positioning on a low-float token, funding can spike and swing hard, punishing one-sided carry and forcing liquidations.
- **Smart-contract / protocol overhang** — GMX has direct exploit history on a V1 contract; protocol-level bad news can hit the token independently of market beta.
- **Regime sensitivity** — in an established-bear, extreme-fear regime, compressed on-chain volumes suppress fees and keep the token in a structural downtrend prone to sharp counter-trend bounces.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/summary?coin=GMX` — all-in-one perp data (mark, funding, OI)
- `GET /api/v1/hyperliquid/prices` — all mid prices
- `GET /api/v1/hyperliquid/l2-book?coin=GMX` — L2 order-book depth
- `GET /api/v1/hyperliquid/open-interest` — all-asset open interest

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=GMX&interval=1h&limit=1000` — OHLCV candles
- `GET /api/v1/hyperliquid/funding-rates?coin=GMX&limit=100` — funding history
- `GET /api/v1/daily/hyperliquid` — daily bulk snapshot of ~230 HL perps

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/summary?coin=GMX"
```

Auth: `X-API-Key` header. Endpoint catalog: [[cryptodataapi-hyperliquid]]. See also [[cryptodataapi]].

---

## See Also

- [[crypto-markets]]
- [[arbitrum]]

---
