---
title: "Request"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, payment-solutions, hyperliquid, perpetual-futures, funding-rate, open-interest, altcoins]
aliases: ["REQ", "Request Network"]
entity_type: protocol
founded: 2017
headquarters: "Decentralized"
website: "https://request.network"
related: ["[[crypto-markets]]", "[[defi]]", "[[ethereum]]", "[[stablecoins]]", "[[hyperliquid]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[hl-vs-cex-funding-divergence]]", "[[cash-and-carry]]"]
---

# Request

**Request** (REQ) is the utility token of the **Request Network**, an [[ethereum|Ethereum]]-based decentralized payment and invoicing system that lets anyone create an on-chain request for payment and receive funds peer-to-peer. Launched in 2017, REQ secures the network and is used to pay protocol fees; the network spans [[ethereum|Ethereum]] and Polygon.

The Request Network removes third-party processors from the payment loop: a user defines a recipient address and amount, optionally attaching terms to turn a simple request into a full invoice, then shares it for one-click, push-based settlement. Every request and payment is documented on-chain, making it useful for accounting and crypto invoicing.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | REQ |
| **Chain** | [[ethereum]] (also Polygon) |
| **Current Price** | $0.055346 |
| **Market Cap** | $41.20M |
| **Market Cap Rank** | #517 |
| **Fully Diluted Valuation** | ~$55.3M (price × max supply) |
| **24h Volume** | $1.44M |
| **24h Change** | +1.49% |
| **7d Change** | -2.28% |
| **Circulating Supply** | ~744.29M REQ |
| **All-Time High** | $1.059 (2018-01-06) |
| **All-Time Low** | $0.00454707 (2020-03-13) |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

Trading backdrop: the broad crypto market is in **extreme fear** ([[fear-and-greed-index|Crypto Fear & Greed Index]] = 23) within an **established bear market** as of 2026-06-20. REQ is up ~1.5% on the day and down ~2% on the week — a thin small-cap drifting with the risk-off tape, trading ~95% below its 2018 ATH.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~744.29M REQ |
| **Total Supply** | ~999.42M REQ |
| **Max Supply** | 1,000,000,000 REQ |
| **Fully Diluted Valuation** | ~$55.3M (price × max supply) |
| **Market Cap / FDV** | ~0.74 |
| **Genesis Date** | 2017-10-07 |

With ~74% of max supply already circulating, REQ has a relatively high market-cap-to-FDV ratio — meaning comparatively low future-emission overhang versus newer small-caps. As payments flow through the network, a portion of REQ is consumed/burned to pay fees, giving the token a usage-linked sink.

### Categories

Polygon Ecosystem, Ethereum Ecosystem, Payment Solutions.

### Contract Addresses

| Chain | Address |
|---|---|
| [[ethereum|Ethereum]] | `0x8f8221afbb33998d8584a2b05749ba73c37a938a` |
| Polygon PoS | `0xb25e20de2f2ebb4cffd4d16a55c7b395e8a94762` |

---

## How & Where It Trades

### Spot venues (CEX)

| Exchange | Pair |
|---|---|
| [[binance|Binance]] | REQ/USDT |
| [[kraken|Kraken]] | REQ/USD |
| KuCoin | REQ/USDT |
| Crypto.com Exchange | REQ/USD |

### Derivatives & DEX

| Venue | Pair | Type |
|---|---|---|
| [[hyperliquid\|Hyperliquid]] | REQ-PERP | [[perpetual-futures\|Perpetual]] |
| Uniswap V2/V3 ([[ethereum\|Ethereum]]) | REQ/DAI, REQ/WETH | Spot ([[decentralized-exchange\|DEX]]) |

REQ is a relatively thin small-cap: ~$1.4M of 24h volume against a ~$41M market cap (turnover ~3.5% of cap), so it is far less liquid than payment peers like [[huma-finance|HUMA]]. A REQ [[perpetual-futures|perp]] is listed on [[hyperliquid|Hyperliquid]], though [[open-interest|open interest]] and [[funding-rate|funding]] on small-cap perps tends to be low and can swing sharply.

### Protocol mechanics (payment requests / invoicing)

The Request Network's "market" is the issuance and settlement of payment requests:

1. A payer or payee creates a **request** on-chain specifying recipient, amount, currency, and optional invoice terms.
2. Because payments are **push-generated** (the counterparty pays an invoice they receive) rather than pull-generated, users never have to share account credentials — a structural privacy advantage over card/ACH rails.
3. Settlement happens peer-to-peer in supported tokens/[[stablecoins]]; the request and payment are recorded immutably for accounting.

---

## Use Case, Narrative & Category

Request is one of the oldest crypto **payments / invoicing** protocols, predating the modern PayFi wave. Its niche is on-chain invoicing, accounting, and B2B/freelancer payment requests, with tooling for [[stablecoins|stablecoin]] invoicing. It competes in the same broad payments category as [[huma-finance|Huma Finance]] but targets invoicing/accounting rather than receivable financing.

---

## Valuation Framing (qualitative)

- **MC/FDV ~0.74** — moderate future-emission overhang (~256M REQ still to enter circulation) but far cleaner than recent-launch tokens; most of the supply is already live.
- **Usage-linked sink** — a portion of REQ is consumed/burned to pay protocol fees, so sustained invoicing volume is the real value driver; the question is whether on-chain invoicing throughput justifies a ~$41M cap.
- **Longevity premium / decay** — REQ is a 2017-era survivor (~95% below ATH) trading on durability and a small fee sink rather than growth; it is priced as a mature, low-momentum payments small-cap.
- **Liquidity discount** — ~$1.4M/day volume means the effective tradeable cap is smaller than the headline; size positions for [[slippage]].

---

## Peer Comparison (crypto payments / invoicing, 2026-06-20)

| Asset | Price | Market Cap | Rank | MC/FDV | Niche |
|---|---|---|---|---|---|
| **Request (REQ)** | $0.055346 | $41.20M | #517 | ~0.74 | On-chain invoicing / accounting |
| [[huma-finance\|Huma Finance (HUMA)]] | — | (small/mid-cap) | — | low | PayFi / receivable financing |
| [[xdce\|XDC Network (XDC)]] | — | (mid-cap) | — | high | Trade-finance / enterprise payments |

> REQ targets invoicing/accounting; [[huma-finance|Huma]] targets receivable financing; XDC targets trade-finance settlement — adjacent payments/PayFi niches. REQ is the older, more decayed, lower-FDV-overhang name; HUMA is the newer, higher-momentum PayFi entrant.

---

## Notable History

- **Founded 2017** by Christophe Lassuyt (CFO) and Etienne Tatur (CTO), both previously co-founders of MONEYTIS. Genesis date 2017-10-07.
- All-time high of **$1.059** was reached on 2018-01-06 during the prior bull cycle; the token trades ~95% below that peak.
- All-time low of **$0.00454707** printed on 2020-03-13 (the COVID liquidity crash).
- The project has continued to ship invoicing and accounting tooling over multiple cycles, making it one of the longer-lived crypto-payments protocols.

> *Additional verified protocol events and news will be added through the wiki's source-ingestion workflow.*

---

## Risks

- **Liquidity risk:** thin ~$1.6M daily volume means wider spreads and higher [[slippage]] on size; small-cap perps add gap-risk.
- **Competitive risk:** the payments/invoicing niche is crowded (PayFi, stablecoin rails, fintech); REQ must keep attracting real invoicing volume to sustain its fee sink.
- **Regulatory risk:** on-chain invoicing and payments intersect with money-transmission, tax, and compliance rules across jurisdictions.
- **Smart-contract risk:** funds and logic live in [[smart-contracts]] on [[ethereum]] and Polygon.
- **Market regime:** with the [[fear-and-greed-index|Fear & Greed Index]] at 23 (extreme fear) in an established bear market, low-liquidity small-caps like REQ are prone to outsized drawdowns.

---

## Related

- [[crypto-markets]]
- [[ethereum]]
- [[defi]]
- [[stablecoins]]
- [[huma-finance]]
- [[hyperliquid]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-20 — cryptodataapi.com / CoinGecko markets feed (`raw/data/crypto-loop/coingecko-markets.json`; price/cap/rank/supply baseline)

## Trading Profile

### Venues & liquidity

REQ trades on **both** major venue types: [[binance|Binance]] offers spot (REQ/USDT) and a USD-margined [[perpetual-futures|perpetual]], while [[hyperliquid|Hyperliquid]] lists **REQ-PERP** with leverage up to ~40-50x. This two-venue footprint is unusual for a ~#513-ranked small-cap and gives REQ a genuinely tradeable derivatives market rather than a spot-only microcap profile.

- **Depth is thin in absolute terms.** With roughly single-digit-million daily volume against a ~$40M cap, both order books are shallow; large market orders walk the book and incur meaningful [[slippage]]. Size positions to the visible L2 depth, not the headline cap.
- **Two-venue availability aids execution.** Because the perp lives on both a deep CEX (Binance) and an on-chain venue (Hyperliquid), spreads between them can be worked, funding can diverge, and traders can route where depth is best. This is the structural precondition for the cross-venue and funding strategies below.
- **Leverage cuts both ways.** 40-50x on a thin book means liquidation clusters can move price sharply; keep effective leverage well below the venue max and expect gap risk around low-liquidity hours.

### Applicable strategies

- [[hl-vs-cex-funding-divergence]] — REQ perps run on both Binance (USD-margined) and Hyperliquid, so the same asset can carry different [[funding-rate|funding]] on each venue; harvest the spread when they dislocate.
- [[funding-rate-arbitrage]] — thin small-cap perps like REQ frequently print stretched funding; go long spot / short the richer perp (or vice versa) to collect the rate.
- [[cash-and-carry]] — hold REQ spot on Binance against a short REQ-PERP to lock the basis, a natural fit given the deep spot + perp pairing.
- [[liquidation-cascade-fade]] — with 40-50x leverage on a shallow book, forced-liquidation wicks overshoot; fade the flush back toward the pre-cascade level.
- [[oi-confirmed-trend]] — pair REQ price moves with Hyperliquid [[open-interest]] to separate real, position-backed trends from thin-liquidity noise.
- [[range-mean-reversion]] — as a low-momentum, decayed payments small-cap, REQ often chops in a range; fade the extremes rather than chasing breakouts.

### Volatility & regime character

REQ is a **low-momentum infra/DeFi payments small-cap** — a 2017-era survivor trading ~95% below its ATH. It behaves as a **high-beta alt**: it amplifies broad-market risk-on/risk-off swings while lacking an independent narrative to drive idiosyncratic runs. Correlation to [[bitcoin|BTC]]/[[ethereum|ETH]] beta is high on the downside (it drifts and drops with the risk-off tape) but it participates only weakly in alt rallies. Expect range-bound drift punctuated by liquidity-driven wicks rather than sustained trends.

### Risk flags

- **Liquidity / venue concentration:** thin books on both venues mean wide effective spreads and gap risk; a single large order can dominate the tape.
- **Perp funding dislocations:** low-OI small-cap perps produce erratic funding that can flip sharply — a risk for carry positions but also the source of the funding trades above.
- **Leverage-driven cascades:** 40-50x on a shallow book makes liquidation cascades violent relative to spot depth.
- **Narrative dependence / decay:** REQ trades on durability and a modest fee sink, not growth; absent fresh payments-narrative catalysts it tends to bleed beta.
- **Emission overhang:** ~256M REQ (MC/FDV ~0.74) remains to enter circulation — modest versus new launches, but a slow supply headwind.
- **Regulatory:** on-chain invoicing/payments intersect money-transmission and tax rules across jurisdictions.

---

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/summary?coin=REQ` — all-in-one perp data (mark, funding, OI)
- `GET /api/v1/hyperliquid/prices` — all mid prices
- `GET /api/v1/hyperliquid/l2-book?coin=REQ` — L2 order-book depth
- `GET /api/v1/hyperliquid/open-interest` — all-asset open interest

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=REQ&interval=1h&limit=1000` — OHLCV candles
- `GET /api/v1/hyperliquid/funding-rates?coin=REQ&limit=100` — funding history
- `GET /api/v1/daily/hyperliquid` — daily bulk snapshot of ~230 HL perps

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/summary?coin=REQ"
```

Auth: `X-API-Key` header. Endpoint catalog: [[cryptodataapi-hyperliquid]]. See also [[cryptodataapi]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---
