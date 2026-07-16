---
title: "Api3"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, oracle, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, altcoins]
aliases: ["API3"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://api3.org/"
related: ["[[chainlink]]", "[[crypto-markets]]", "[[ethereum]]", "[[oracle-manipulation]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[funding-rate-harvest]]", "[[oi-confirmed-trend]]"]
---

# Api3

**Api3** (ticker **API3**) is the governance token of the API3 DAO, an [[ethereum|Ethereum]]-based oracle protocol built around **first-party oracles** — data feeds operated directly by the API providers themselves rather than by third-party node middlemen. API3 is best known for **dAPIs** (decentralized APIs) and for pioneering **Oracle Extractable Value (OEV)**, a mechanism that recaptures the [[mev|MEV]] normally lost to searchers during oracle updates and returns it to the dApps consuming the data.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | API3 |
| **Chain** | [[ethereum\|Ethereum]] |
| **Current Price** | $0.269453 |
| **Market Cap** | $38.58M |
| **Market Cap Rank** | #542 |
| **24h Volume** | $9.74M |
| **24h Change** | +1.54% |
| **7d Change** | +4.56% |
| **Circulating Supply** | ~142.96M API3 |
| **Total Supply** | ~172.67M API3 |
| **Max Supply** | Uncapped |
| **All-Time High** | $10.30 (2021-04-07) |
| **All-Time Low** | $0.2364 (2026-06-10) |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

API3 is up modestly on the day (+1.5%) and ~+4.6% over the week, showing relative resilience while the broad **Crypto [[fear-and-greed-index|Fear & Greed Index]] reads 23 (extreme fear)** in what analysts call an **Established Bear Market**. The token printed a fresh all-time low of **$0.2364 on 2026-06-10** — it now trades just above that level and roughly **-97% below its 2021 ATH** of $10.30. Daily turnover (~$9.7M on a ~$38.6M cap, ~25%) is unusually high for a token this size, signaling active rotation around the OEV narrative rather than dormant holding.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~142.96M API3 |
| **Total Supply** | ~172.67M API3 |
| **Max Supply** | Uncapped (inflationary staking rewards) |
| **Fully Diluted Valuation** | $46.01M |
| **Market Cap / FDV** | ~0.83 |
| **All-Time High** | $10.30 (2021-04-07) |
| **All-Time Low** | $0.2364 (2026-06-10) |

API3 uses an **inflationary staking model**: stakers lock API3 into a collateral/insurance pool that backstops feed accuracy, and they earn newly minted tokens for doing so. This pool is the protocol's security and accountability layer — if a first-party feed delivers bad data, staked API3 can be used to compensate harmed dApps. Token holders also govern the API3 DAO. Because supply is **uncapped** (staking rewards mint new API3 indefinitely), the MC/FDV near **0.83** understates the open-ended emission schedule — demand must continually outpace inflation to avoid sell pressure.

---

## Technology & Protocol

API3's design departs from the [[chainlink|Chainlink]] third-party-node oracle model:

- **First-party oracles** — Data providers run their own oracle nodes (using API3's **Airnode**), signing data directly. This removes the middleman node layer, improves transparency about data provenance, and lets providers be held accountable via the staking pool.
- **dAPIs (decentralized APIs)** — Aggregated, managed price feeds that dApps subscribe to, available across many EVM chains via the API3 Market.
- **OEV (Oracle Extractable Value)** — API3 auctions the right to trigger oracle updates (e.g., liquidation-triggering price pushes). The value searchers would otherwise extract as [[mev|MEV]] is instead captured and rebated to the dApp, turning the oracle from a cost center into a **revenue source** for [[lending-protocols|lending protocols]] and perp [[dex|DEXs]]. The **OEV Network** is the dedicated chain/auction layer that runs these update-right auctions.

These products make API3 a competitor to [[chainlink|Chainlink]], [[pyth-network]], and [[redstone-oracles]] in [[defi|DeFi]] price feeds, with **OEV** as its strongest differentiator.

## Market Structure & Derivatives

**Spot venues.** API3 lists on Binance (API3/USDT), Kraken (API3/USD), Upbit (API3/KRW), Bitget, KuCoin, and Crypto.com. On-chain liquidity is on [[uniswap]] V2/V3 and SushiSwap against WETH.

**Liquidity & depth.** ~$9.7M daily volume on a ~$38.6M cap is high turnover, but absolute depth remains modest — large orders move price. Spot CEX/DEX flow dominates; API3 is not a flagship perpetual market on [[hyperliquid|Hyperliquid]] or other major perp venues, so leveraged-derivatives exposure is limited and price is driven by spot supply/demand around oracle catalysts.

---

## Peer Comparison

| Oracle | Model | Mcap Rank | Market Cap | Edge |
|---|---|---|---|---|
| [[chainlink\|Chainlink (LINK)]] | Third-party node network | top-20 | multi-$B | Dominant integrations, CCIP, market standard |
| [[pyth-network\|Pyth (PYTH)]] | First-party, pull/low-latency | top-100 | larger | High-frequency feeds from trading firms |
| **Api3 (API3)** | First-party (Airnode) + OEV | #542 | ~$38.6M | OEV revenue recapture; provider accountability |
| [[redstone-oracles\|RedStone]] | Modular pull oracle | — | smaller/private | Cheap on-demand feeds, EVM + non-EVM |

API3 is a **small-cap challenger** to far larger incumbents. Its bet is not to out-integrate Chainlink but to differentiate on **first-party provenance** and **OEV economics** — letting integrators monetize their own liquidations instead of leaking that value to searchers.

---

## Valuation Framing

API3's fundamental value tracks **OEV revenue capture** and **feed adoption**. With an uncapped supply and inflationary staking, the bull case requires OEV fees and dApp subscriptions to grow faster than emissions; the bear case is that adoption stays niche while Chainlink/Pyth dominate distribution. Trading near its all-time low at ~$38M cap, API3 screens as a deep-value / high-optionality oracle bet — qualitative only, not a price target.

---

## Use Case, Narrative & Category

API3 sits in the **oracle / DeFi-infrastructure** category. Its narrative rests on two pillars: (1) **first-party data** as a more transparent, accountable alternative to node-operator oracles, and (2) **OEV** as a way for lending markets and derivatives venues to reclaim value that currently leaks to MEV searchers. As DeFi liquidations and perp funding generate large extractable value, OEV is positioned as a meaningful new revenue primitive — the core of API3's bullish thesis and the source of its "oracles that pay you" tagline.

---

## Notable History

- **2020** — API3 founded out of the CLC Group / Honeycomb API ecosystem; built the **Airnode** first-party oracle to let API providers serve data without intermediaries.
- **2021** — Token launch; API3 reached its ATH of $10.30 in April 2021.
- **2022-2023** — Rollout of **dAPIs** and the API3 Market across EVM chains; expansion of the staking/insurance model.
- **2024** — Launch and promotion of **OEV** as a flagship feature, with the OEV Network designed to auction update rights and rebate value to integrators.
- **2026** — Token set a new all-time low ($0.2364, 2026-06-10) during the broad crypto downturn.

---

## Risks

- **Oracle-manipulation / data-integrity risk** — First-party feeds shift trust to the API providers themselves; a compromised or malicious provider could push bad data, with the staking pool as the only economic backstop. See [[oracle-manipulation]].
- **Coverage adequacy risk** — The insurance/collateral pool must remain large enough to credibly compensate harmed dApps; a sharp API3 price drop shrinks the real-dollar value of that backstop just when it may be needed.
- **Competitive risk** — API3 competes directly with the far larger [[chainlink]] and the high-frequency [[pyth-network]]; OEV adoption is still maturing and faces alternative MEV-redistribution designs.
- **Emission / dilution risk** — Inflationary staking rewards continually mint new supply; demand must outpace emissions to avoid sell pressure.
- **Liquidity & macro risk** — ~$9.7M daily volume is modest in absolute terms, and in an extreme-fear, Established Bear Market regime (Fear & Greed 23) low-cap infra tokens are prone to liquidity drought and underperformance.

---

## Related

- [[crypto-markets]]
- [[ethereum]]
- [[mev]]
- [[defi]]
- [[chainlink]]
- [[pyth-network]]
- [[redstone-oracles]]
- [[uma]]
- [[tellor]]
- [[oracle-manipulation]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-21 (cryptodataapi.com / CoinGecko).

## Trading Profile

**Venues & liquidity.** API3 is tradable on [[binance|Binance]] — both spot (API3/USDT) and a USD-margined [[perpetual-futures|perpetual]], which exposes [[funding-rate|funding]], [[open-interest|open interest]], and [[liquidations]] data. It is **NOT** listed on [[hyperliquid|Hyperliquid]]; Binance is the primary leveraged venue. With derivatives concentrated on a single major CEX, leverage and short-side exposure funnel through Binance's order book and funding mechanism, so the perp funding rate and OI there are the cleanest read on positioning. Absolute depth is modest for a ~#614 mid/small-cap, meaning size must be worked carefully — large market orders slip, and stops/liquidations can chain in thin books. Sizing should assume Binance-centric liquidity and account for gap risk when spot CEX/DEX flow (Kraken, Upbit, Uniswap) diverges from the perp.

**Applicable strategies.**
- [[funding-rate-harvest]] — Binance is the sole major perp venue, so a persistent funding sign can be collected against a spot hedge on the same exchange.
- [[crowded-long-funding-fade]] — deep-value oracle token near its ATL invites reflexive long-chasing on OEV-narrative pops; extended positive funding flags a fade.
- [[cash-and-carry]] — long spot API3/USDT vs short the USD-M perp captures basis when the narrative drives perp premium above spot.
- [[liquidation-cascade-fade]] — thin single-venue derivatives depth makes forced-liquidation flushes overshoot, offering rebound entries after the cascade.
- [[oi-confirmed-trend]] — because leverage is concentrated on Binance, rising OI alongside price gives a clean confirmation/exhaustion signal for trend entries.
- [[rsi-mean-reversion]] — high turnover on a small float around oracle catalysts produces sharp overbought/oversold swings that revert toward range.

**Volatility & regime character.** API3 is a small/mid-cap DeFi-infrastructure (oracle) token with high beta to BTC/ETH risk sentiment and amplified moves in extreme-fear regimes. It is not a memecoin, but its low float and OEV-narrative sensitivity give it reflexive, catalyst-driven bursts of volatility on modest volume. Price action tends to track the broad altcoin risk cycle, decoupling only around oracle-specific news (OEV adoption, feed integrations).

**Risk flags.**
- **Venue concentration** — leveraged liquidity is effectively single-venue (Binance); a listing/delisting or depth shift there dominates tradable derivatives risk.
- **Emission / dilution** — uncapped inflationary staking rewards mint new supply indefinitely, a structural headwind that funding and carry trades must weigh.
- **Narrative dependence** — valuation leans heavily on OEV adoption; stalled traction can drain the speculative bid that drives volume.
- **Liquidity drought** — modest absolute depth on a low-cap infra token makes it prone to slippage and cascade risk in bear/extreme-fear conditions.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=API3USDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=API3USDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=API3` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=API3` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=API3USDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=API3USDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=API3"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---
