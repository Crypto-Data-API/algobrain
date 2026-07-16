---
title: "Cash Cat"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, hyperliquid, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, memecoins, altcoins]
aliases: ["CASHCAT"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://cashcattoken.xyz/"
related: ["[[crypto-markets]]", "[[hyperliquid]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[liquidation-cascade-fade]]", "[[meme-coin-cycle]]"]
---

# Cash Cat

**Cash Cat** (CASHCAT) is a Solana Ecosystem, Meme, Cat-Themed, 4chan-Themed, Robinhood Ecosystem, Yoink.fun Launchpad, Robinhood Chain Meme project. It ranks **#276** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | CASHCAT |
| **Market Cap Rank** | #276 |
| **Market Cap** | $92.61M |
| **Current Price** | $0.0950 |
| **Categories** | Meme, Cat-Themed, 4chan-Themed, Yoink.fun Launchpad, Robinhood Chain Meme |
| **Website** | [https://cashcattoken.xyz/](https://cashcattoken.xyz/) |

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 991.31M CASHCAT |
| **Total Supply** | 991.31M CASHCAT |
| **Max Supply** | 1.00B CASHCAT |
| **Fully Diluted Valuation** | $92.61M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.2278 (2026-07-11) |
| **Current vs ATH** | -57.71% |
| **All-Time Low** | $0.00000010 (2026-07-05) |
| **Current vs ATL** | +99444997.56% |
| **24h Change** | -19.31% |
| **7d Change** | +0.67% |
| **30d Change** | +0.00% |
| **1y Change** | +0.00% |

---

## Platform & Chain Information

**Native Chain:** Robinhood

### Contract Addresses

| Chain | Address |
|---|---|
| Robinhood | `0x020bfc650a365f8bb26819deaabf3e21291018b4` |
| Solana | `CashcatZMRn4Jv8sPQZUSsbTLi2PcPe1ssqbHcnaJqSS` |

---

## Exchange Listings

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Orca | CASHCATZMRN4JV8SPQZUSSBTLI2PCPE1SSQBHCNAJQSS/EPJFWDD5AUFQSSQEM2QN1XZYBAPC8G4WEGGKZWYTDT1V | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://cashcattoken.xyz/](https://cashcattoken.xyz/) |
| **Twitter** | [@cashcat_token](https://twitter.com/cashcat_token) |
| **Telegram** | [cashcat_robinhood](https://t.me/cashcat_robinhood) (2,068 members) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $55.63M |
| **Market Cap Rank** | #276 |
| **24h Range** | $0.0873 — $0.1347 |
| **CoinGecko Sentiment** | 36% positive |
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

CASHCAT is a **perp-first** asset: it trades on **Hyperliquid** as **CASHCAT-PERP** with leverage up to roughly **40-50x**, but is **not listed on Binance**. Spot access is limited and largely offshore/on-chain (Solana DEXs such as Orca), so there is no deep, well-arbitraged centralized spot market to anchor price discovery. As a result, directional and speculative flow concentrates on the Hyperliquid perp, which typically holds the most usable liquidity and the tightest quotes for the name. Book depth is thin relative to majors and can gap during fast moves, so position sizing should assume meaningful slippage on large clips, wider stops than a large-cap would need, and staged entries/exits rather than single market orders. The absence of a Binance venue also means the HL perp is the primary hedging and price-reference instrument, concentrating basis and funding risk in one venue.

### Applicable strategies

- [[liquidation-cascade-fade]] — thin perp depth and high leverage make forced-liquidation flushes overshoot; fading the wick after a cascade exhausts can capture the snap-back.
- [[post-liquidation-rebound]] — after a leveraged long/short cluster is wiped out on the HL book, the subsequent mean-reverting bounce is a repeatable memecoin pattern here.
- [[crowded-long-funding-fade]] — as a hyped meme perp, one-sided long crowding drives funding sharply positive; fading over-extended longs when funding spikes is a natural setup.
- [[funding-rate-harvest]] — persistent positive funding on a crowded meme perp lets a delta-neutral or hedged position collect carry from over-leveraged longs.
- [[oi-price-exhaustion]] — rising open interest into a stalling price flags a crowded, reflexive position that is prone to a violent unwind, useful for timing exits/reversals.
- [[meme-coin-cycle]] — CASHCAT is a cat/4chan meme with reflexive attention-driven cycles; trading the launch-hype-fade rhythm frames both entries and risk.

### Volatility & regime character

CASHCAT is a **high-beta memecoin** (Solana/Robinhood-ecosystem cat meme) with reflexive, attention-driven price action. Volatility is very high and event-clustered: its ATH and near-zero ATL sit only days apart, reflecting a freshly launched, sentiment-dominated token. Beta to BTC/ETH is high on the downside (broad risk-off crushes small memes disproportionately) but idiosyncratic on the upside, where narrative, social virality, and launchpad/ecosystem catalysts dominate over macro crypto trends. Expect regime shifts to be abrupt rather than gradual.

### Risk flags

- **Venue concentration** — perp liquidity and price discovery are concentrated on a single venue (Hyperliquid); no Binance backstop means execution, hedging, and outages all funnel through one book.
- **Thin liquidity / slippage** — limited spot depth and shallow perp books amplify slippage and gap risk on size.
- **Narrative dependence** — value is driven by meme/social attention; interest can evaporate quickly, leaving little fundamental support.
- **Funding dislocations** — one-sided leveraged positioning can push funding to extremes and trigger cascading liquidations on the HL perp.
- **Reflexivity / drawdown** — high leverage plus a young, sentiment-led token creates sharp, self-reinforcing drawdowns.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/summary?coin=CASHCAT` — all-in-one perp data (mark, funding, OI)
- `GET /api/v1/hyperliquid/prices` — all mid prices
- `GET /api/v1/hyperliquid/l2-book?coin=CASHCAT` — L2 order-book depth
- `GET /api/v1/hyperliquid/open-interest` — all-asset open interest

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=CASHCAT&interval=1h&limit=1000` — OHLCV candles
- `GET /api/v1/hyperliquid/funding-rates?coin=CASHCAT&limit=100` — funding history
- `GET /api/v1/daily/hyperliquid` — daily bulk snapshot of ~230 HL perps

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/summary?coin=CASHCAT"
```

Auth: `X-API-Key` header. Endpoint catalog: [[cryptodataapi-hyperliquid]]. See also [[cryptodataapi]].

---

## See Also

- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])
