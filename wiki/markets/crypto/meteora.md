---
title: "Meteora"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, hyperliquid, perpetual-futures, funding-rate, open-interest, altcoins]
aliases: ["MET"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.meteora.ag/"
related: ["[[automated-market-maker]]", "[[crypto-markets]]", "[[decentralized-exchange]]", "[[ethereum]]", "[[hyperliquid]]", "[[liquidity-pool]]", "[[orca]]", "[[solana]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[hl-vs-cex-funding-divergence]]", "[[cash-and-carry]]"]
---

# Meteora

**Meteora** (ticker **MET**) is the governance/exchange token of Meteora, a leading liquidity and [[decentralized-exchange|DEX]] protocol on [[solana|Solana]]. Meteora is best known for its **DLMM (Dynamic Liquidity Market Maker)** — a concentrated-liquidity [[automated-market-maker|AMM]] using discrete price "bins" — and for being a primary liquidity backbone for Solana token launches (a core venue behind launchpad/memecoin activity).

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | MET |
| **Native Chain** | [[solana|Solana]] |
| **Market Cap Rank** | #338 |
| **Market Cap** | $74.41M |
| **Current Price** | $0.14021 |
| **24h Volume** | $67.48M |
| **24h Change** | +0.73% |
| **7d Change** | +33.57% |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

Context: this strength is notable because the broader market is in an **Established Bear Market** with the Crypto [[fear-and-greed-index|Fear & Greed Index]] at **23 (extreme fear)** as of 2026-06-21. MET is sharply outperforming — roughly flat on the day but up ~34% on the week — and its 24h volume ($67.5M) is ~91% of its market cap, signaling intense turnover and speculative interest. (The prior snapshot's ~+14% daily / +43% weekly has cooled to ~+0.7% / +34% as the move consolidates.)

---

## Technology & Protocol

Meteora is a native [[solana|Solana]] liquidity protocol whose differentiator is **bin-based concentrated liquidity** plus deep launchpad integration:

- **DLMM (Dynamic Liquidity Market Maker)** — Meteora's flagship [[automated-market-maker|AMM]]. Instead of a continuous price curve, DLMM organizes liquidity into discrete **price bins**; LPs place liquidity into specific bins for zero-slippage swaps *within* a bin and high capital efficiency. DLMM supports **dynamic fees** that rise with volatility, helping LPs capture more during volatile launches and partially offset [[impermanent-loss]]. This bin design contrasts with [[orca|Orca]]'s continuous-range Whirlpools and Uniswap V3.
- **Dynamic Pools / DAMM** — auto-rebalancing pools that route idle liquidity to lending venues for extra yield, then back to the pool as needed.
- **Launch liquidity backbone** — Meteora is a primary venue for **Solana token launches** (memecoins and new projects), supplying the initial DLMM liquidity. This ties a large share of its volume to the high-velocity Solana launch ecosystem.
- **MET token & "Stimulus" distribution** — MET launched comparatively recently (2025) with a large airdrop/community allocation; protocol fees from DLMM and dynamic pools are designed to accrue value to the MET token / DAO.
- **Solana speed/cost** — sub-cent fees and sub-second blocks make high-frequency bin rebalancing and launch trading practical.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | 529.91M MET |
| **Total Supply** | 997.73M MET |
| **Max Supply** | 1.00B MET |
| **Circulating / Max** | ~53% |
| **Fully-Diluted Value** | ~$140M |
| **MC / FDV** | ~0.53 |
| **All-Time High** | $0.6869 (2025-10-23) |
| **All-Time Low** | $0.094642 |

MET has a **1B hard cap** with roughly **53% circulating**, meaning a significant ~47% dilution overhang remains (FDV ~$140M, ~1.9x market cap) — a key risk for a relatively young token whose future unlocks could weigh on price. The token is a comparatively recent launch (ATH set October 2025, ATL ~$0.095). Protocol fees from DLMM and dynamic pools are designed to accrue value to the MET token / DAO, making fee value-capture the central tokenomics question.

---

## Market Structure & Derivatives

**Centralized venues:** MET is broadly listed — **Binance** (MET/USDT), **Kraken** (MET/USD), **Bitget**, **KuCoin**, **Crypto.com**, and **Upbit** (as MET2/KRW). Tier-1 CEX coverage plus Upbit gives deep liquidity and Korean retail access.

**On-chain / fee capture:** Meteora *is* the venue. Its **DLMM** places liquidity into discrete bins for concentrated, low-slippage swaps, and its **Dynamic Pools** auto-rebalance and earn yield on idle liquidity. MET trades on-chain against USDC via **[[orca|Orca]]** and Meteora's own pools on [[solana]]. Meteora is a top source of organic DEX volume on Solana and a key liquidity layer for new-token launches; protocol/LP fees are the economic engine intended to back the token.

**Derivatives:** MET has a perpetuals market on **[[hyperliquid]]** (MET-PERP), so [[funding-rate|funding rate]] and open interest are live signals — elevated positive funding during this ~+34% weekly run would indicate crowded longs and squeeze/fade risk (see [[funding-rate]], [[perpetual-futures]]). The ~91%-of-cap daily volume underscores how perp/spot speculation drives short-term price.

---

## Narrative & Category

Meteora rides the **Solana DeFi + launchpad** narrative. As one of the dominant AMMs on Solana, it captures fee flow from both blue-chip swaps and the high-velocity memecoin/launch ecosystem. Its DLMM design directly competes with [[orca|Orca]]'s Whirlpools and Raydium for Solana liquidity. The current outperformance vs. a bearish tape reflects this idiosyncratic, Solana-launch-driven demand.

---

## Valuation Framing

Qualitatively, MET is a **high-beta, fee-rich but dilution-heavy** Solana DEX bet. The bull case is straightforward: Meteora is among the highest-volume venues on Solana and earns real DLMM/dynamic-pool fees, so a token that captures even a slice of that flow has a credible cash-flow anchor. The bear case is structural — only ~53% of supply circulates (MC/FDV ~0.53), much of its volume is tied to cyclical memecoin launches, and its market cap roughly equals one day of trading volume, marking it as a momentum-driven name. Relative to [[orca|Orca]] (similar ~$74M cap but lower dilution and steadier flow), MET offers more launchpad upside but more unlock and crowding risk. A durable re-rating needs both sustained Solana volume share and clear fee accrual to MET.

---

## Peer Comparison

| DEX | Token | AMM Model | MC Rank | Market Cap | Notes |
|---|---|---|---|---|---|
| **Meteora** | MET | DLMM (bin-based) + Dynamic Pools | #338 | ~$74M | Launchpad liquidity backbone; ~47% to unlock |
| [[orca\|Orca]] | ORCA | Whirlpools (concentrated) | #340 | ~$74M | Retail-UX leader; lower dilution |
| Raydium | RAY | Hybrid AMM + CLMM | mid-cap | — | Long-standing Solana DEX/launchpad |
| [[uniswap\|Uniswap]] | UNI | V3 concentrated | top-25 | multi-B | Ethereum/L2 benchmark CLMM |

*Figures for non-Meteora peers are illustrative category placement, not snapshot data.*

---

## Notable History

- Built within the Solana DeFi ecosystem as a successor/evolution of earlier dynamic-vault and AMM work.
- Pioneered the **DLMM** bin-based concentrated-liquidity model on Solana.
- Token launched recently, with ATH **$0.6869** in October 2025; subsequently retraced into the $0.09–0.15 range during the bear market before the June 2026 bounce.

---

## Risks

- **Dilution overhang** — only ~53% of supply circulates (MC/FDV ~0.53); future unlocks could pressure price.
- **Memecoin/launch dependence** — much of Meteora's volume is tied to speculative Solana launches; that flow is cyclical and can evaporate.
- **Volatility / crowded longs** — a ~+34% weekly move into extreme-fear conditions (F&G 23) is fragile; check [[hyperliquid]] funding/OI for squeeze risk.
- **Smart-contract & oracle risk** — DLMM bin logic and dynamic rebalancing are complex.
- **Solana network risk** — outages or congestion on [[solana]] directly impair the protocol.

---

## Related

- [[crypto-markets]]
- [[solana]]
- [[orca]]
- [[decentralized-exchange]]
- [[automated-market-maker]]
- [[liquidity-pool]]
- [[impermanent-loss]]
- [[hyperliquid]]
- [[funding-rate]]
- [[fear-and-greed-index]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-21 from CoinGecko markets feed (`raw/data/crypto-loop/coingecko-markets.json`).
- General market knowledge; no specific wiki source ingested yet for protocol mechanics.

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | MET |
| **Market Cap Rank** | #1201 |
| **Market Cap** | $9.17M |
| **Current Price** | $1.06 |
| **Categories** | Decentralized Finance (DeFi), Synthetic Issuer |
| **Website** | [https://metronome.io/](https://metronome.io/) |

---

## Overview

Metronome, found online at Metronome.io, under the symbol MTN. The cryptocurrency promises to deliver “institutional-class endurance” with cross-blockchain compatibility.The currency is being developed by Bloq, which announced Metronome in October 2017. Metronome is launched in early December 2017, with the first cross-chain transfers (between Ethereum and Ethereum Classic) scheduled for Q1 2018.

Metronome released in December 2017. By Q1 2018, Metronome aims to become the world’s first cross-chain compatible cryptocurrency by adding Ethereum Classic support (the currency is initially built on Ethereum). Metronome’s cross-chain compatibility system involves creating exit receipts when leaving the chain and entering a new chain.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 8.65M MET |
| **Total Supply** | 14.38M MET |
| **Max Supply** | 14.38M MET |
| **Fully Diluted Valuation** | $15.23M |
| **Market Cap / FDV Ratio** | 0.60 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $8.90 (2023-04-15) |
| **Current vs ATH** | -88.09% |
| **All-Time Low** | $0.00148609 (2022-08-23) |
| **Current vs ATL** | +71185.30% |
| **24h Change** | +3.47% |
| **7d Change** | +8.31% |
| **30d Change** | +35.04% |
| **1y Change** | +146.98% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x2ebd53d035150f328bd754d6dc66b99b0edb89aa` |

---

## Exchange Listings

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0X2EBD53D035150F328BD754D6DC66B99B0EDB89AA/0XA0B86991C6218B36C1D19D4A2E9EB0CE3606EB48 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://metronome.io/](https://metronome.io/) |
| **Twitter** | [@MetronomeDAO](https://twitter.com/MetronomeDAO) |
| **Reddit** | [https://www.reddit.com/r/MetronomeToken/](https://www.reddit.com/r/MetronomeToken/) |
| **Telegram** | [metronometoken](https://t.me/metronometoken) (1,448 members) |
| **Discord** | [https://discord.gg/metronome](https://discord.gg/metronome) |
| **GitHub** | [https://github.com/autonomoussoftware/metronome.io](https://github.com/autonomoussoftware/metronome.io) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 4 |
| **GitHub Forks** | 8 |
| **Pull Requests Merged** | 199 |
| **Contributors** | 13 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $9,729.35 |
| **Market Cap Rank** | #1201 |
| **24h Range** | $1.02 — $1.09 |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Trading Profile

### Venues & liquidity

MET (Meteora) is tradable on **BOTH** [[binance|Binance]] (spot MET/USDT plus a USD-margined perpetual) and **[[hyperliquid|Hyperliquid]]** (MET-PERP, leverage up to ~40-50x). This is a deep, liquid two-venue market, with additional tier-1 CEX coverage (Kraken, Bitget, KuCoin, Crypto.com) and Upbit for Korean retail. The dual Binance/Hyperliquid perp footprint means execution can be split across venues, funding can be compared and arbitraged between CEX and the on-chain [[hyperliquid|Hyperliquid]] book, and position sizing benefits from aggregated depth rather than a single thin venue. For a ~#293-rank alt, this two-venue liquidity is unusually good and supports both delta-one basis structures and directional perp trades; still, size relative to on-book depth since order-book liquidity thins fast on sharp Solana-launch-driven moves.

### Applicable strategies

- [[hl-vs-cex-funding-divergence]] — MET trades on both Binance's perp and Hyperliquid MET-PERP, so funding can diverge between the CEX and on-chain book and be harvested directly.
- [[cash-and-carry]] — Binance spot MET plus a short USD-margined/HL perp captures basis and positive funding on a token whose ~91%-of-cap daily turnover keeps funding lively.
- [[funding-rate-harvest]] — elevated positive funding during MET's speculative launchpad-driven runs pays shorts a carry that can be systematically collected.
- [[crowded-long-funding-fade]] — sharp weekly rips into extreme-fear tape (F&G 23) crowd longs; fade overheated funding/OI once momentum stalls.
- [[liquidation-cascade-fade]] — high leverage (~40-50x) plus thin off-peak depth makes MET prone to liquidation cascades that overshoot and mean-revert.
- [[breakout-and-retest]] — MET's Solana-launch narrative produces clean volatility breakouts; entering on the retest filters false starts on this high-beta name.

### Volatility & regime character

MET is a **high-beta Solana DeFi / launchpad-infrastructure token** with strong memecoin-cycle reflexivity — much of its volume and volatility is driven by the high-velocity Solana token-launch ecosystem it provides liquidity for. It behaves as a risk-on, high-beta alt: it tends to amplify BTC/ETH beta on the upside and downside, while also carrying idiosyncratic, Solana-ecosystem-specific swings (it can decouple and outperform, as in its ~+34% weekly move against a bearish tape). Expect wide realized-volatility ranges and momentum-driven turnover far exceeding a typical large-cap.

### Risk flags

- **Dilution / emissions** — only ~53% of supply circulates (MC/FDV ~0.53); ~47% unlock overhang can pressure price and distort perp funding around vesting events.
- **Narrative dependence** — much of the volume is tied to cyclical Solana memecoin/launch activity; that flow is fickle and can evaporate.
- **Perp funding dislocations** — crowded longs during launch-driven rips can spike funding and set up squeeze/cascade risk, especially at high leverage.
- **Liquidity/venue concentration** — despite two-venue perps, on-book depth thins quickly on volatile moves; large orders move price and stops can slip.
- **Solana network risk** — Solana congestion or outages directly impair the underlying protocol and can gap the token.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/summary?coin=MET` — all-in-one perp data (mark, funding, OI)
- `GET /api/v1/hyperliquid/prices` — all mid prices
- `GET /api/v1/hyperliquid/l2-book?coin=MET` — L2 order-book depth
- `GET /api/v1/hyperliquid/open-interest` — all-asset open interest

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=MET&interval=1h&limit=1000` — OHLCV candles
- `GET /api/v1/hyperliquid/funding-rates?coin=MET&limit=100` — funding history
- `GET /api/v1/daily/hyperliquid` — daily bulk snapshot of ~230 HL perps

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/summary?coin=MET"
```

Auth: `X-API-Key` header. Endpoint catalog: [[cryptodataapi-hyperliquid]]. See also [[cryptodataapi]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---
