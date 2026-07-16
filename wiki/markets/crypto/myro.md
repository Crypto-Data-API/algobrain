---
title: "MYRO"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, hyperliquid, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, memecoins]
aliases: ["MYRO"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://myrothedog.com"
related: ["[[crypto-markets]]", "[[solana]]", "[[hyperliquid]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[liquidation-cascade-fade]]"]
---

# MYRO

**MYRO** (MYRO) is the dog: Named after Solana Co-Founder Raj Gokal’s dog Myro. It ranks **#2148** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | MYRO |
| **Market Cap Rank** | #2148 |
| **Market Cap** | $2.20M |
| **Current Price** | $0.00220251 |
| **Categories** | Meme, Dog-Themed, Solana Meme |
| **Website** | [https://myrothedog.com](https://myrothedog.com) |

---

## Overview

Myro the dog: Named after Solana Co-Founder Raj Gokal’s dog Myro.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 999.98M MYRO |
| **Total Supply** | 999.98M MYRO |
| **Max Supply** | 1.00B MYRO |
| **Fully Diluted Valuation** | $2.20M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.4428 (2024-03-09) |
| **Current vs ATH** | -99.50% |
| **All-Time Low** | $0.00016073 (2026-07-09) |
| **Current vs ATL** | +1270.33% |
| **24h Change** | +1.71% |
| **7d Change** | -11.24% |
| **30d Change** | -11.21% |
| **1y Change** | -90.25% |

---

## Platform & Chain Information

**Native Chain:** Solana

### Contract Addresses

| Chain | Address |
|---|---|
| Solana | `Bm3dgkZrjH7eaz1GBH1R2ZHkp7nZUoPNJhjekoxepump` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| KuCoin | MYRO/USDT | N/A |
| Crypto.com Exchange | MYRO/USD | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://myrothedog.com](https://myrothedog.com) |
| **Twitter** | [@myrosol](https://twitter.com/myrosol) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $4.84M |
| **Market Cap Rank** | #2148 |
| **24h Range** | $0.00216551 — $0.00228943 |
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

### Venues & liquidity

MYRO is a **perp-first** asset: it trades on **Hyperliquid** as **MYRO-PERP** with leverage up to roughly **40-50x**, but it is **not listed on Binance**. Spot access is limited and offshore (a handful of CEX pairs such as KuCoin and Crypto.com plus on-chain Solana DEX liquidity), so directional and speculative flow concentrates on the Hyperliquid perp rather than spot. Given the small market cap and thin cross-venue spot depth, the HL order book is the primary price-discovery and execution venue for leveraged traders. Book depth is shallow relative to large-cap alts, so realistic size is modest — slippage and market impact grow quickly on larger clips, and traders should scale orders, use limit/passive fills, and lean on L2 depth checks before sizing. The absence of a deep Binance spot market also means classic spot-hedged carry is harder to run cleanly; funding and basis dislocations on the perp can persist longer than they would on a mega-cap.

### Applicable strategies

- [[funding-rate-harvest]] — collect funding on the isolated MYRO-PERP when persistent one-sided positioning pins funding, since there is no competing deep Binance perp to arbitrage it flat.
- [[crowded-long-funding-fade]] — memecoin rallies on MYRO routinely drive crowded longs and richly positive funding; fading the crowd when funding spikes is a core reflexive edge.
- [[liquidation-cascade-fade]] — thin depth plus high leverage (up to ~50x) makes MYRO prone to violent liquidation wicks; fading overshoots into forced deleveraging can capture sharp mean-reversion.
- [[post-liquidation-rebound]] — after a cascade flushes leveraged positions on the HL perp, the snap-back rebound is often outsized on a low-liquidity memecoin like MYRO.
- [[oi-price-exhaustion]] — rising open interest into a stalling MYRO price flags exhausted, overcrowded positioning ripe for a reversal on the perp.
- [[meme-coin-cycle]] — as a Solana dog-themed memecoin, MYRO is driven by narrative reflexivity and rotation cycles rather than fundamentals, making meme-cycle timing central to its trade.

### Volatility & regime character

MYRO is a **micro-cap Solana memecoin** exhibiting extreme memecoin reflexivity: sharp, sentiment-driven pumps and dumps, a >99% drawdown from its 2024 all-time high, and outsized intraday ranges relative to majors. It carries high beta to BTC/ETH in risk-off regimes (it sells off hard when majors drop) but its upside is dominated by idiosyncratic Solana meme narrative flow and SOL beta rather than broad-market correlation. Regime alternates between illiquid, drifting chop and violent narrative-driven expansion.

### Risk flags

- **Liquidity & venue concentration** — no Binance listing; thin offshore spot and a single dominant HL perp mean gaps, wide spreads, and elevated slippage.
- **Narrative dependence** — value is almost entirely reflexive/meme-driven; sentiment shifts can evaporate liquidity and price with no fundamental floor.
- **Micro-cap fragility** — very small market cap makes it vulnerable to single-whale moves, on-chain holder concentration, and manipulation.
- **Perp funding dislocations** — with limited spot to arbitrage against, funding can run extreme and persist, punishing crowded leveraged positioning.
- **Leverage / liquidation risk** — up to ~50x on a shallow book produces frequent cascade wicks that stop out or liquidate positions abruptly.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/summary?coin=MYRO` — all-in-one perp data (mark, funding, OI)
- `GET /api/v1/hyperliquid/prices` — all mid prices
- `GET /api/v1/hyperliquid/l2-book?coin=MYRO` — L2 order-book depth
- `GET /api/v1/hyperliquid/open-interest` — all-asset open interest

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=MYRO&interval=1h&limit=1000` — OHLCV candles
- `GET /api/v1/hyperliquid/funding-rates?coin=MYRO&limit=100` — funding history
- `GET /api/v1/daily/hyperliquid` — daily bulk snapshot of ~230 HL perps

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/summary?coin=MYRO"
```

Auth: `X-API-Key` header. Endpoint catalog: [[cryptodataapi-hyperliquid]]. See also [[cryptodataapi]].

---

## See Also

- [[crypto-markets]]
- [[solana]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])
