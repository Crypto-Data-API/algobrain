---
title: "ConstitutionDAO"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: review
tags: [crypto, hyperliquid, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, memecoins, ethereum]
aliases: ["PEOPLE"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.constitutiondao.com/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[hyperliquid]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[liquidation-cascade-fade]]"]
---

# ConstitutionDAO

**ConstitutionDAO** (PEOPLE) is a Meme, Ethereum Ecosystem, PolitiFi project. It ranks **#678** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | PEOPLE |
| **Market Cap Rank** | #678 |
| **Market Cap** | $27.12M |
| **Current Price** | $0.005355 |
| **Categories** | Meme, Ethereum Ecosystem, PolitiFi |
| **Website** | [https://www.constitutiondao.com/](https://www.constitutiondao.com/) |
> *Market data refreshed 2026-06-12 (CoinGecko top-1000 snapshot).*

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 5.07B PEOPLE |
| **Total Supply** | 5.07B PEOPLE |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $33.41M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.1850 (2021-12-23) |
| **Current vs ATH** | -96.44% |
| **All-Time Low** | $0.00091940 (2021-11-21) |
| **Current vs ATL** | +617.25% |
| **24h Change** | -4.43% |
| **7d Change** | +0.52% |
| **30d Change** | -11.17% |
| **1y Change** | -42.01% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x7a58c0be72be218b41c608b7fe7c5bb630736c71` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | PEOPLE/USDT | N/A |
| Bitget | PEOPLE/USDT | N/A |
| KuCoin | PEOPLE/USDT | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| [[hyperliquid|Hyperliquid]] | PEOPLE-PERP | Perpetual |
| Uniswap V3 (Ethereum) | 0X7A58C0BE72BE218B41C608B7FE7C5BB630736C71/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.constitutiondao.com/](https://www.constitutiondao.com/) |
| **Twitter** | [@constitutiondao](https://twitter.com/constitutiondao) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $6.08M |
| **Market Cap Rank** | #678 |
| **24h Range** | $0.00657622 — $0.00708856 |
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

PEOPLE trades across two deep venues: **Binance** (spot PEOPLE/USDT plus a USD-margined perpetual) and **Hyperliquid** (PEOPLE-PERP, up to ~40-50x leverage). This gives it a genuine two-venue derivatives market rather than a single-DEX long tail — order books are reasonably liquid and top-of-book depth on both sides supports meaningful position sizing. The dual availability enables true CEX-vs-DEX comparison: mark price, funding, and depth can be sourced independently on each venue, so execution can be routed to the tighter side and basis/funding dislocations between Binance and Hyperliquid become tradable. Despite the depth, PEOPLE is a low-priced small-cap (sub-cent notional), so slippage still widens quickly on aggressive size and stops should account for wide intrabar wicks; scale entries and avoid resting large single clips.

### Applicable strategies

- [[hl-vs-cex-funding-divergence]] — PEOPLE runs on both Binance perp and Hyperliquid, so funding can diverge between venues and be harvested market-neutral.
- [[cash-and-carry]] — long Binance spot against short PEOPLE-PERP captures positive perp funding while staying delta-neutral.
- [[funding-rate-harvest]] — reflexive memecoin flows push funding to extremes on the leveraged perp, paying the side that fades the crowd.
- [[crowded-long-funding-fade]] — PolitiFi/meme narrative pumps attract crowded longs; persistently rich funding flags overheated positioning to fade.
- [[liquidation-cascade-fade]] — thin small-cap depth plus up to ~50x leverage produces sharp liquidation flushes that mean-revert intraday.
- [[narrative-trading]] — as a PolitiFi/meme token, PEOPLE moves on constitutional/political news cycles rather than fundamentals.

### Volatility & regime character

PEOPLE is a **high-beta memecoin** (Meme / Ethereum ecosystem / PolitiFi) with strong reflexivity: moves are narrative- and sentiment-driven and amplified by leverage on the perp. Beta to BTC/ETH is high on broad risk-off days (it sells off with the alt complex), but idiosyncratic PolitiFi/political-event catalysts can decouple it entirely from majors to the upside or downside. Expect wide, wick-heavy ranges and low mean-reversion half-life on flushes.

### Risk flags

- **Small-cap / low notional:** sub-cent price and modest market cap mean depth thins fast; large clips move the book and wicks trigger stops.
- **Narrative dependence:** value is tied to PolitiFi/meme attention cycles — momentum can evaporate abruptly with no fundamental floor.
- **Leverage-driven cascades:** up to ~40-50x on Hyperliquid concentrates liquidation risk; crowded positioning unwinds violently.
- **Perp funding dislocations:** two-venue perp availability means Binance and Hyperliquid funding can diverge sharply during stress, cutting both ways on carry.
- **Venue concentration:** derivatives liquidity is concentrated on two venues, so an outage or funding spike on either can distort marks and squeeze one-sided positioning.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/summary?coin=PEOPLE` — all-in-one perp data (mark, funding, OI)
- `GET /api/v1/hyperliquid/prices` — all mid prices
- `GET /api/v1/hyperliquid/l2-book?coin=PEOPLE` — L2 order-book depth
- `GET /api/v1/hyperliquid/open-interest` — all-asset open interest

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=PEOPLE&interval=1h&limit=1000` — OHLCV candles
- `GET /api/v1/hyperliquid/funding-rates?coin=PEOPLE&limit=100` — funding history
- `GET /api/v1/daily/hyperliquid` — daily bulk snapshot of ~230 HL perps

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/summary?coin=PEOPLE"
```

Auth: `X-API-Key` header. Endpoint catalog: [[cryptodataapi-hyperliquid]]. See also [[cryptodataapi]].

## See Also

- [[crypto-markets]]
- [[ethereum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])
