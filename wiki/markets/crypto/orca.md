---
title: "Orca"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, altcoins, perpetual-futures, funding-rate, open-interest, liquidations, derivatives]
aliases: ["ORCA"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.orca.so/"
related: ["[[automated-market-maker]]", "[[crypto-markets]]", "[[decentralized-exchange]]", "[[impermanent-loss]]", "[[meteora]]", "[[solana]]", "[[yield-farming]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[cash-and-carry]]", "[[funding-rate-harvest]]"]
---

# Orca

**Orca** (ticker **ORCA**) is the [[governance-token|governance token]] of Orca, one of the first and most user-friendly general-purpose [[automated-market-maker|AMM]] [[decentralized-exchange|DEXs]] on [[solana|Solana]]. Users swap assets, provide concentrated liquidity, and earn yield through Orca's signature **Whirlpools** (concentrated-liquidity pools). Projects integrate Orca as a "money-lego" for swapping, [[yield-farming|farming]], and on-chain price data.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | ORCA |
| **Native Chain** | [[solana|Solana]] |
| **Market Cap Rank** | #340 |
| **Market Cap** | $73.77M |
| **Current Price** | $1.21 |
| **24h Volume** | $15.67M |
| **24h Change** | +0.00% |
| **7d Change** | +5.70% |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

Context: the broader market is in an **Established Bear Market** with the Crypto [[fear-and-greed-index|Fear & Greed Index]] at **23 (extreme fear)** as of 2026-06-21. ORCA is flat over 24h and up ~5.7% on the week — notable relative strength versus a weak tape, with healthy turnover (~$15.7M daily volume, ~21% of its ~$74M cap), consistent with steady Solana on-chain activity.

---

## Technology & Protocol

Orca is a native [[solana|Solana]] [[automated-market-maker|AMM]] [[decentralized-exchange|DEX]] built for clean retail UX. Core mechanics:

- **Whirlpools (concentrated liquidity)** — Orca's flagship product is a **concentrated-liquidity AMM** akin to [[uniswap|Uniswap]] V3: liquidity providers choose a **price range** in which to deploy capital, earning far higher fee density when price stays in range — at the cost of [[impermanent-loss]] and zero fees when price exits the range. This is far more capital-efficient than legacy constant-product pools.
- **Fee tiers** — pools offer multiple fee tiers so LPs can match fees to expected volatility/volume of a pair.
- **"Fair Price Indicator" & UX** — Orca historically differentiated on transparent pricing warnings and a deliberately simple interface ("DeFi for everyone"), positioning it as the clean alternative to launch/memecoin-heavy venues.
- **Solana speed/cost** — running on Solana gives sub-second swaps and sub-cent fees, enabling tight LP rebalancing and high-frequency routing that 0x/Uniswap aggregators tap.
- **Aggregator integration** — Orca's pools are a major liquidity source routed by Solana aggregators (Jupiter), so much of its volume arrives via routed flow rather than its own front end.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | 60.80M ORCA |
| **Total Supply** | 75.00M ORCA |
| **Max Supply** | 100.00M ORCA |
| **Circulating / Max** | ~60.8% |
| **Fully-Diluted Value** | ~$121M |
| **MC / FDV** | ~0.61 |
| **All-Time High** | $20.33 (2021-10-02) |
| **All-Time Low** | $0.3511 (2022-06-19) |

ORCA has a **100M hard cap** with ~60.8% circulating, so a moderate dilution overhang remains (FDV ~1.65x market cap; ~39M ORCA still to enter circulation via team/treasury/incentive schedules). ORCA is a [[governance-token]] used to vote on protocol parameters, fee tiers, and treasury direction. A portion of swap fees and farming emissions historically routed to the DAO/treasury and liquidity incentives. As with most DEX governance tokens, the persistent question is **fee value capture** — how much of Whirlpool swap-fee revenue ultimately accrues to ORCA versus LPs.

---

## Market Structure & Derivatives

**Centralized venues:** ORCA is well-distributed across CEXs — **Binance** (ORCA/USDT), **Kraken** (ORCA/USD), **Bitget**, **KuCoin**, **Crypto.com**, and **Upbit** (ORCA/KRW).

**On-chain / fee capture:** Orca is itself a [[decentralized-exchange|DEX]]. Its **Whirlpools** are concentrated-liquidity [[automated-market-maker|AMM]] pools (akin to [[uniswap]] V3) where LPs choose price ranges for higher capital efficiency, at the cost of [[impermanent-loss]] when price exits the range. ORCA the token trades on-chain primarily against wrapped SOL/USDC in Orca's own pools. Orca is consistently among the top DEXs by volume on [[solana]], competing with [[meteora|Meteora]] and Raydium; much of its swap flow is routed in via the **Jupiter** aggregator.

**Derivatives:** ORCA is not a major perpetuals listing; price discovery is spot-led across the CEX/DEX venues above, so [[funding-rate|funding]] and open interest are not primary drivers.

---

## Narrative & Category

Orca anchors the **Solana DeFi blue-chip DEX** narrative — positioned as the clean, retail-friendly UX leader for Solana swaps and LPing, in contrast to more launch/memecoin-focused venues. Categories include DEX, AMM, [[yield-farming]], and Solana Ecosystem; backers historically include Coinbase Ventures and DeFiance Capital (per CoinGecko tags). Its thesis is durable Solana on-chain activity translating into steady fee capture.

---

## Valuation Framing

Qualitatively, ORCA is a **real-revenue Solana DEX with a value-capture discount**. Unlike most of the DEX-governance complex, Orca's Whirlpools generate genuine swap-fee flow tied to durable Solana activity, so the token is closer to a "DEX-volume proxy" than a pure narrative play. At ~$74M market cap with healthy turnover, it trades as a mid-tier Solana DeFi name — cheaper than Raydium on some volume metrics, but carrying the same open question of how much fee revenue routes to the token versus LPs. A re-rating would track Solana DEX market-share gains and any tokenomics shift toward holder fee accrual. Its relative-strength week (+5.7% into extreme fear) hints at idiosyncratic Solana DeFi demand.

---

## Peer Comparison

| DEX | Token | AMM Model | MC Rank | Market Cap | Notes |
|---|---|---|---|---|---|
| **Orca** | ORCA | Whirlpools (concentrated) | #340 | ~$74M | Retail-UX leader; Jupiter-routed flow |
| [[meteora\|Meteora]] | MET | DLMM (bin-based) | #338 | ~$74M | Launchpad liquidity backbone |
| Raydium | RAY | Hybrid AMM + CLMM | mid-cap | — | Long-standing Solana DEX/launchpad |
| [[uniswap\|Uniswap]] | UNI | V3 concentrated | top-25 | multi-B | Ethereum/L2 benchmark CLMM |

*Figures for non-Orca peers are illustrative category placement, not snapshot data.*

---

## Notable History

- One of the **first general-purpose AMMs on Solana**, known for a deliberately simple, approachable UX ("DeFi for everyone").
- Launched **Whirlpools**, bringing concentrated liquidity to Solana.
- ATH **$20.33** in October 2021; now trades ~94% below that level after the multi-year DeFi-token drawdown, but has held the low-single-digit-dollar range.

---

## Risks

- **Bear-market beta** — a Solana DeFi governance token; high-beta to crypto risk-off (F&G at 23).
- **Competition** — intense Solana DEX rivalry with [[meteora|Meteora]], Raydium, and aggregator disintermediation (Jupiter) can erode volume share and fee revenue.
- **Dilution overhang** — ~39% of supply not yet circulating (MC/FDV ~0.61); future unlocks/emissions could pressure price.
- **Solana network risk** — outages/congestion directly impair the protocol.
- **Impermanent loss for LPs** — concentrated Whirlpool positions can underperform holding in volatile markets (see [[impermanent-loss]]).
- **Smart-contract risk** — AMM and pool contracts are an attack surface.

---

## Related

- [[crypto-markets]]
- [[solana]]
- [[meteora]]
- [[decentralized-exchange]]
- [[automated-market-maker]]
- [[yield-farming]]
- [[impermanent-loss]]
- [[uniswap]]
- [[fear-and-greed-index]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-21 from CoinGecko markets feed (`raw/data/crypto-loop/coingecko-markets.json`).
- General market knowledge; no specific wiki source ingested yet for protocol mechanics.

## Trading Profile

### Venues & liquidity

ORCA is tradable on [[binance|Binance]] — **spot (ORCA/USDT)** plus a **USD-margined perpetual**, which brings live [[funding-rate|funding]], [[open-interest|open interest]], and [[liquidations|liquidation]] data to what is otherwise a spot-led, on-chain-native name. It is **NOT listed on Hyperliquid**, so Binance is effectively the primary leveraged venue for ORCA. With market-cap rank ~326 and modest daily turnover, order-book depth on the perp is thin relative to majors: leverage is available but slippage and funding whipsaw scale up fast on size. Practically, this means position sizing should stay small relative to visible book depth, entries/exits benefit from limit orders and VWAP-style execution rather than market sweeps, and any basis/carry trade depends on the single Binance perp for the short leg (concentration risk if that listing's liquidity dries up).

### Applicable strategies

- [[funding-rate-harvest]] — the lone Binance perp on a mid-cap DeFi token can run persistently one-sided funding; collect the carry while delta-hedging spot.
- [[cash-and-carry]] — long ORCA spot (Binance or on-chain) versus short the Binance USD-M perp captures any positive basis on a real-revenue Solana DEX token.
- [[liquidation-cascade-fade]] — thin perp depth means forced-liquidation wicks overshoot; fade the flush back toward spot-anchored fair value.
- [[oi-confirmed-trend]] — use Binance open-interest build to confirm that a Solana-DeFi-driven ORCA move is leverage-backed rather than a spot-only blip.
- [[breakout-and-retest]] — ORCA holds well-defined low-single-digit-dollar ranges; trade confirmed breakouts with a retest entry to filter false moves in low liquidity.
- [[rsi-mean-reversion]] — as a range-bound mid-cap, ORCA reverts sharply from stretched RSI extremes when it detaches from its BTC/ETH-correlated drift.

### Volatility & regime character

ORCA is a **small/mid-cap Solana DeFi / DEX governance token** (rank ~326), so it carries high-beta behavior into crypto risk-on/risk-off swings and correlates strongly to BTC/ETH regime plus Solana-ecosystem flows. It is not a memecoin — volatility is driven by durable on-chain DEX activity and Solana DeFi narrative rotation rather than pure reflexive hype, giving it periods of idiosyncratic relative strength (e.g., outperforming a weak tape). Expect trend/mean-reversion behavior within multi-week ranges, punctuated by faster moves when Solana DeFi share or tokenomics narratives shift.

### Risk flags

- **Venue/liquidity concentration** — a single Binance leveraged venue (no Hyperliquid); thin perp depth amplifies slippage and liquidation-driven volatility, and basis trades depend on that one listing.
- **Dilution overhang** — ~39% of supply not yet circulating (MC/FDV well below 1); scheduled team/treasury/incentive emissions can pressure price.
- **Narrative dependence** — value tracks Solana DEX market share and fee-capture-to-token narrative; aggregator disintermediation (Jupiter) and rivals (Meteora, Raydium) can erode the thesis.
- **Correlated drawdowns** — high-beta DeFi token; broad risk-off (Solana network stress, DeFi sector selloffs) hits liquidity and funding simultaneously.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=ORCAUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=ORCAUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=ORCA` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=ORCA` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=ORCAUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=ORCAUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=ORCA"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[solana]]

---
