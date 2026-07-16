---
title: "Rootstock Infrastructure Framework"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [bitcoin, crypto, defi, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, altcoins]
aliases: ["RIF"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://rif.technology/"
related: ["[[bitcoin]]", "[[crypto-markets]]", "[[decentralized-finance]]", "[[rootstock]]", "[[stablecoins]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[funding-rate-harvest]]", "[[oi-confirmed-trend]]"]
---

# Rootstock Infrastructure Framework

**Rootstock Infrastructure Framework** (ticker **RIF**) is the infrastructure and governance token for **Rootstock (RSK)** — Bitcoin's EVM-compatible DeFi sidechain. RIF powers incentives, infrastructure, and interoperability across the Rootstock ecosystem: community rewards and grants via RootstockCollective, the censorship-resistant stablecoin **USDRIF**, and the **RNS** naming service. Built to complement rather than compete with [[bitcoin]], RIF is the largest-cap token of this group, ranked **#285** by market capitalization (2026-06-21).

---

## Market Data

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

| Field | Value |
|---|---|
| **Ticker** | RIF |
| **Current Price** | $0.090278 |
| **Market Cap** | $90.28M |
| **Market Cap Rank** | #285 |
| **24h Volume** | $19.40M |
| **24h Change** | -2.66% |
| **7d Change** | -12.24% |
| **Fully Diluted Valuation** | $90.28M |
| **Circulating Supply** | 1.00B RIF |
| **All-Time High** | $0.455938 (2021-04-12), -80.17% from ATH |
| **All-Time Low** | $0.0091475 (2019-06-12), +888% from ATL |

Trading backdrop: the broad crypto market sits in **extreme fear** (Crypto Fear & Greed Index ≈ 23) amid an **Established Bear Market** as of 2026-06-21. A sharp **counter-trend spike that lifted RIF ~+26% on 2026-06-20 has now reversed** — RIF is **-2.7% over 24h and -12.2% over the trailing 7 days**, with the rally giving back most of its gains as the rank slipped to **#285** from #268. Volume remains elevated (~$19.4M against a ~$90M cap), consistent with a fast round-trip in a speculative micro/mid-cap rather than durable accumulation. This is exactly the retrace risk flagged earlier: counter-trend rallies in extreme-fear regimes tend not to hold. (No specific catalyst is confirmed in-wiki; treat the prior spike as event-driven and unverified.)

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | 1.00B RIF |
| **Total Supply** | 1.00B RIF |
| **Max Supply** | Uncapped (no hard cap reported) |
| **Market Cap** | $90.28M |
| **Fully Diluted Valuation** | $90.28M |
| **MC / FDV Ratio** | 1.00 |

Full supply already circulates: circulating = total = 1.00B RIF, so **MC = FDV (ratio 1.00)** — there is no unlock overhang or hidden dilution from vesting. CoinGecko reports no fixed max supply, but the entire issued supply is in the market today.

---

## How & Where It Trades

**Spot venues.** RIF trades primarily as **RIF/USDT** on [[binance]] and Bitget, plus across its multi-chain deployments. With ~$19.4M daily volume (still elevated as the spike unwinds) against a ~$90M cap, RIF is the most liquid of this group and the only one with a major-exchange ([[binance]]) USDT pair driving price discovery.

**Rootstock infrastructure mechanics (the actual utility).** RIF is the economic layer of **[[rootstock]]**, Bitcoin's merge-mined, EVM-compatible DeFi sidechain:

- **RootstockCollective** — RIF powers community rewards, governance, and grants for the Rootstock ecosystem.
- **USDRIF** — a censorship-resistant stablecoin underpinned by RIF infrastructure, bringing dollar-denominated DeFi to Bitcoin's sidechain.
- **RNS (Rootstock Name Service)** — human-readable names for wallet addresses, paid/secured via RIF.
- **Bitcoin-aligned DeFi** — Rootstock is secured by Bitcoin miners (merge mining) and pegged to BTC (rBTC), so RIF gives Web3 users exposure to **Bitcoin DeFi** without leaving the Bitcoin security model.

**Cross-chain reach.** Beyond native Rootstock, RIF is bridged to [[ethereum]], Base, Arbitrum, and Solana (CoinGecko ecosystem tags), broadening where the token and its infrastructure can be used.

**Derivatives.** RIF has no significant perpetual-futures / [[hyperliquid]] market; no reliable funding-rate or open-interest data is available. It should be treated as a spot-driven mid/small-cap — the recent spike-and-retrace underscores how thin the durable demand is.

---

## Use Case, Narrative & Category

RIF sits in the **Bitcoin DeFi / infrastructure** category. Its narrative is being the connective tissue and incentive layer for **Rootstock**, the leading attempt at an EVM DeFi layer secured by Bitcoin — riding the BTCfi thesis that Bitcoin's capital should be usable in smart-contract DeFi. RIF's value accrues from demand across Rootstock infrastructure (USDRIF, RNS, RootstockCollective grants) and from overall Rootstock ecosystem adoption.

---

## Notable History

- One of the **oldest tokens in this group**: all-time high of **$0.456 on 2021-04-12**, all-time low of **$0.0091 on 2019-06-12** — RIF has traded since the 2019 era as the RSK/Rootstock infrastructure token.
- Backed by **Outlier Ventures** (CoinGecko portfolio tag).
- Currently ~80% below its 2021 cycle high (the brief +26% counter-trend spike on 2026-06-20 has since reversed).

---

## Risks

- **Catalyst durability** — the +26% spike on 2026-06-20 was a single-day, low-confidence move and has **already retraced** (-12% over the trailing 7d), confirming the pattern that counter-trend rallies in extreme-fear regimes rarely hold.
- **Ecosystem-concentration risk** — RIF depends entirely on Rootstock adoption; Bitcoin sidechain DeFi remains a niche with modest TVL.
- **Stablecoin/peg risk** — USDRIF, as a smaller censorship-resistant stablecoin, carries de-peg and reserve risks.
- **Long-term underperformance** — ~80% below ATH after multiple cycles.
- **Bear-market backdrop** — broad extreme-fear, established-bear-market conditions cap upside for infrastructure alts.

---

## Trading Profile

**Venues & liquidity.** RIF is tradable on [[binance]] as both spot (RIF/USDT) and a USD-margined perpetual, so leveraged traders get [[funding-rate]] prints, [[open-interest]] readings, and [[liquidations]] data on the primary venue. RIF is NOT listed on [[hyperliquid]], making Binance the primary — effectively the sole major — leveraged venue. This concentration means execution and sizing should assume single-venue depth: perp liquidity, funding, and OI all reflect Binance flow, so slippage on larger clips is a real constraint and there is no on-chain perp DEX to cross-check or route around. With a ~#212 rank and thin durable demand, size positions to the Binance order book rather than to notional cap, and treat funding/OI extremes as venue-specific rather than market-wide signals.

**Applicable strategies.**
- [[funding-rate-harvest]] — a single-venue Binance perp lets a delta-neutral book collect funding when RIF perp trades persistently rich or cheap to spot.
- [[crowded-long-funding-fade]] — after counter-trend spikes (like the +26% one-day move that fully retraced), crowded longs paying elevated funding on Binance set up mean-reversion fades.
- [[liquidation-cascade-fade]] — concentrated Binance leverage on a thin small-cap makes forced-liquidation flushes overshoot, offering fades once the cascade exhausts.
- [[oi-confirmed-trend]] — pairing Binance open-interest expansion with price confirms whether a RIF move is real positioning versus a hollow spot squeeze.
- [[breakout-and-retest]] — RIF's wide intraday ranges and sharp spikes favor waiting for a breakout to retest before committing, filtering the frequent failed counter-trend pops.
- [[volatility-targeting]] — RIF's reflexive spike-and-retrace behavior argues for scaling exposure inversely to realized volatility rather than fixed sizing.

**Volatility & regime character.** RIF is a small/mid-cap infrastructure/DeFi token (BTCfi / Rootstock ecosystem) with high beta to Bitcoin and broad-market risk sentiment. It exhibits reflexive, memecoin-like spike-and-retrace dynamics on thin durable demand — sharp counter-trend rallies that give back most gains — rather than durable trends. As a Bitcoin-DeFi infrastructure token its narrative rises and falls with the BTCfi thesis and Rootstock adoption, and it tends to underperform in extreme-fear, established-bear regimes.

**Risk flags.**
- **Venue concentration** — leveraged exposure lives almost entirely on Binance; no Hyperliquid or on-chain perp fallback, so funding/OI/liquidation signals are single-source and venue outages or delistings hit hard.
- **Liquidity** — mid/small-cap depth means larger orders move price; treat funding and OI extremes as thin-book artifacts, not broad conviction.
- **Narrative dependence** — value hinges on Rootstock/BTCfi adoption; a niche with modest TVL, vulnerable to narrative rotation.
- **Reflexivity** — counter-trend spikes in extreme-fear regimes routinely retrace, punishing momentum-chasing longs.
- **Peg-adjacent risk** — RIF underpins USDRIF; a de-peg or reserve event would spill into RIF sentiment.

---

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=RIFUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=RIFUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=RIF` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=RIF` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=RIFUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=RIFUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=RIF"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[bitcoin]]
- [[rootstock]]
- [[decentralized-finance]]
- [[stablecoins]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- General market knowledge; no specific wiki source ingested yet.

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | RIF |
| **Market Cap Rank** | #212 |
| **Market Cap** | $137.35M |
| **Current Price** | $0.1373 |
| **Hashing Algorithm** | Ethash |
| **Categories** | Solana Ecosystem, Arbitrum Ecosystem, Ethereum Ecosystem, Base Ecosystem, Rootstock Ecosystem, Outlier Ventures Portfolio |
| **Website** | [https://rif.technology/](https://rif.technology/) |

---

## Overview

Built to compliment Bitcoin, not compete with it. RIF is designed to accelerate the adoption of Rootstock, Bitcoin’s DeFi Layer by powering incentives, infrastructure and interoperability. RIF is the easiest way for anyone to shape and share in the success of  Bitcoin DeFi.

RIF powers community rewards, governance and grants, on RootstockCollective, the home of the community on Rootstock. RIF underpins key infrastructure powering Bitcoin DeFi on Rootstock including USDRIF, a censorship resistant stablecoin and RNS for simplifying wallet addresses.

RIF gives the wider world of Web3 exposure to the success of Bitcoin DeFi on Rootstock through availability on the top exchanges, leading chains and largest dApps.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 1.00B RIF |
| **Total Supply** | 1.00B RIF |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $137.35M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.4559 (2021-04-12) |
| **Current vs ATH** | -69.90% |
| **All-Time Low** | $0.00914750 (2019-06-12) |
| **Current vs ATL** | +1400.08% |
| **24h Change** | -1.00% |
| **7d Change** | +7.37% |
| **30d Change** | +14.28% |
| **1y Change** | +122.85% |

---

## Platform & Chain Information

**Native Chain:** Rootstock

### Contract Addresses

| Chain | Address |
|---|---|
| Rootstock | `0x2acc95758f8b5f583470ba265eb685a8f45fc9d5` |
| Ethereum | `0x01b603be3d545f096015741e6503440282bf45fb` |
| Base | `0xe5e851b01dd3eda24fde709a407db44555b6d1e0` |
| Solana | `AAeENcfHbTExuTvs4q7r9Bjax98Dg6BGX3aMph4bTLdK` |
| Arbitrum One | `0xe5e851b01dd3eda24fde709a407db44555b6d1e0` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | RIF/USDT | N/A |
| Bitget | RIF/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://rif.technology/](https://rif.technology/) |
| **Twitter** | [@RifTechnology](https://twitter.com/RifTechnology) |
| **Reddit** | [https://www.reddit.com/r/rootstock/](https://www.reddit.com/r/rootstock/) |
| **Telegram** | [rskofficialcommunity](https://t.me/rskofficialcommunity) (2,296 members) |
| **Discord** | [http://discord.gg/rootstock](http://discord.gg/rootstock) |
| **GitHub** | [https://github.com/riflabs](https://github.com/riflabs) |
| **Whitepaper** | [https://rif.technology/static/add903ce229a6f45a606cd78b028cf9e/RIF-whitepaper-V2.pdf](https://rif.technology/static/add903ce229a6f45a606cd78b028cf9e/RIF-whitepaper-V2.pdf) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 9 |
| **GitHub Forks** | 5 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $12.92M |
| **Market Cap Rank** | #212 |
| **24h Range** | $0.1257 — $0.1430 |
| **CoinGecko Sentiment** | 0% positive |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---
