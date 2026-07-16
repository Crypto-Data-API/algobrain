---
title: "Avantis"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, derivatives, perpetuals, hyperliquid, perpetual-futures, funding-rate, open-interest, liquidations, altcoins, bitcoin, ethereum]
aliases: ["AVNT"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.avantisfi.com/"
related: ["[[base]]", "[[coinbase]]", "[[crypto-markets]]", "[[decentralized-exchange]]", "[[edgex]]", "[[hyperliquid]]", "[[perpetual-futures]]", "[[real-world-assets]]", "[[funding-rate]]", "[[funding-rate-harvest]]", "[[cash-and-carry]]"]
---

# Avantis

**Avantis** (AVNT) is a [[perpetual-futures|perpetuals]] [[decentralized-exchange|DEX]] built on and backed by [[base|Base]], specializing in real-world-asset (RWA) perps alongside crypto. It lets users trade crypto plus [[real-world-assets|RWAs]] — FX, commodities, indices, and equities — with leverage of up to 500x in a permissionless on-chain environment. It is one of the largest [[decentralized-exchange|DEXes]] on [[base|Base]] by volume.

Avantis is best known for **zero-fee perpetuals (ZFP)** — a structure where traders pay trading fees only on profitable trades — and for bringing leveraged [[real-world-assets|RWAs]] on-chain. The protocol is backed by [[pantera|Pantera]] and [[coinbase|Coinbase]].

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | AVNT |
| **Chain** | [[base]] |
| **Price** | $0.113799 |
| **Market Cap** | $36,916,366 |
| **Market Cap Rank** | #558 |
| **24h Volume** | $10,132,405 |
| **24h Change** | +3.85% |
| **7d Change** | +3.36% |
| **All-Time High** | $2.64 (2025-09-22) — now ~-95.7% |
| **All-Time Low** | $0.098181 |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

Trading backdrop: the broad crypto market is in **extreme fear** ([[crypto-fear-and-greed-index|Crypto Fear & Greed Index]] = 23) within an **established bear market** as of 2026-06-20. AVNT is up on both 24h (+3.85%) and 7d (+3.36%) horizons — one of the stronger relative performers in this cohort despite the risk-off tape — though it trades only modestly above its all-time low. Turnover is healthy (~$10.1M against a ~$36.9M cap, ~27% of cap).

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~324.22M AVNT |
| **Total Supply** | 1,000,000,000 AVNT |
| **Max Supply** | 1,000,000,000 AVNT |
| **Fully Diluted Valuation** | ~$113.8M (price × max supply) |
| **Market Cap / FDV** | ~0.32 |

> **Dilution flag:** only about **one-third of max supply circulates** (MC/FDV ~0.32), leaving ~68% of the token base — roughly 676M AVNT — still to unlock. On a fully-diluted basis AVNT is ~3.1x its current market cap; cliff unlocks to team, investors and incentives are a structural overhang and the single largest token-side risk.

AVNT is used for governance and protocol incentives; trading-fee flows and the protocol's vaults underpin its value-accrual narrative.

### Categories

Decentralized Finance (DeFi), Derivatives, Perpetuals, Binance HODLer Airdrops, Binance Alpha Spotlight, Made in USA, Base Native.

### Contract Address

| Chain | Address |
|---|---|
| [[base|Base]] | `0x696f9436b67233384889472cd7cd58a6fb5df4f1` |

---

## How & Where It Trades

### Spot venues (CEX)

| Exchange | Pair |
|---|---|
| [[binance|Binance]] | AVNT/USDT |
| [[kraken|Kraken]] | AVNT/USD |
| Upbit | AVNT/KRW |
| Bitget | AVNT/USDT |
| KuCoin | AVNT/USDT |
| Crypto.com Exchange | AVNT/USD |

### Derivatives & DEX

| Venue | Pair | Type |
|---|---|---|
| [[hyperliquid\|Hyperliquid]] | AVNT-PERP | [[perpetual-futures\|Perpetual]] |

With ~$9.2M of 24h spot volume against a ~$36.2M market cap (turnover ~25% of cap), the AVNT token itself is reasonably liquid. An AVNT [[perpetual-futures|perp]] is listed on [[hyperliquid|Hyperliquid]]; as with most small-caps, monitor [[open-interest|open interest]] and [[funding-rate|funding rates]] for crowding and squeeze risk.

### Protocol mechanics (perps, leverage, funding)

Avantis is itself a [[perpetual-futures|perpetual-futures]] venue, so its on-chain "market" is the trading product:

1. **Liquidity providers** deposit into Avantis vaults (the counterparty to traders), earning fees and funding.
2. **Traders** open long/short [[perpetual-futures|perpetual]] positions on crypto and [[real-world-assets|RWA]] markets (FX, commodities, indices, equities) with up to **500x** [[leverage]].
3. **Funding** payments transfer between longs and shorts to anchor the perp price to the underlying index; positions are [[liquidation|liquidated]] if margin falls below maintenance.
4. **Zero-fee perpetuals (ZFP):** under this primitive, traders only pay trading fees when a trade is profitable, lowering the cost of entering directional bets.

Because Avantis lists leveraged [[real-world-assets|RWAs]], it brings TradFi exposures (equity indices, FX, commodities) into a permissionless [[base|Base]] [[decentralized-exchange|DEX]] — a distinctive position versus crypto-only perp DEXes like [[hyperliquid|Hyperliquid]].

---

## Use Case, Narrative & Category

Avantis sits in the **on-chain derivatives / perp-DEX** category, with a differentiating **leveraged RWA** angle. It rides two narratives: the rapid growth of [[base|Base]]-native DeFi, and the institutional push to bring [[real-world-assets|real-world assets]] on-chain. Backing from [[pantera|Pantera]] and [[coinbase|Coinbase]] reinforces its Base-ecosystem positioning.

---

## Peer Comparison

AVNT belongs to the 2025–2026 **perp-DEX token** basket — the dominant "real-revenue DEX" narrative. Its differentiator is leveraged [[real-world-assets|RWA]] perps; its weakness is scale versus the category leaders. Figures from the 2026-06-20 snapshot where available.

| Token | Venue type | Chain | MC Rank | Market Cap | Differentiator |
|---|---|---|---|---|---|
| [[hyperliquid\|HYPE]] | Perp DEX (own L1) | Hyperliquid | top-tier | (much larger) | Category leader; deepest [[open-interest\|OI]] |
| [[edgex\|EDGE]] | Orderbook perp DEX | EDGE Chain / [[arbitrum\|Arbitrum]] | #213 | ~$141.8M | CEX-grade matching; equity/RWA perps |
| **AVNT** | Perp DEX (vault model) | [[base\|Base]] | #558 | ~$36.9M | Leveraged RWA perps; zero-fee-perp structure |

Versus crypto-only perp DEXes like [[hyperliquid|Hyperliquid]], Avantis's leveraged-RWA listings (FX, commodities, indices, equities) are its distinctive edge; versus [[edgex|edgeX]] it is smaller and Base-native rather than orderbook-on-L2.

---

## Valuation Framing (Qualitative)

- **MC/FDV ~0.32** — heavy unlock overhang; ~68% of supply still to enter circulation is the dominant valuation headwind.
- **Fee/revenue vs token** — the bull case rests on perp trading-fee flows (and the ZFP structure's effect on volume) accruing to AVNT via vaults/governance; verify live fee capture before crediting it.
- **~-95.7% from ATH but rising** — AVNT trades just above its all-time low yet was a positive outlier in this run (+3–4% on day and week), suggesting fresh interest or short covering rather than a fundamental re-rate.
- **Narrative beta** — AVNT is high-beta to both the perp-DEX and Base-DeFi narratives; it benefits when those catch a bid and carries full retrace risk when they fade.

This is framing, not a price target; the wiki holds no fair-value model for AVNT.

---

## Notable History

- The protocol reports cumulative trading volume in the tens of billions of dollars since launching in early 2024, ranking it among the largest [[decentralized-exchange|DEXes]] on [[base|Base]].
- AVNT reached an all-time high of **$2.64** on 2025-09-22; the token now trades ~96% below that peak.
- All-time low of **$0.098181** was printed during the 2026 bear market, very close to the current price — AVNT is trading near its historical lows.

> *Additional verified protocol events and news will be added through the wiki's source-ingestion workflow.*

---

## Risks

- **Leverage / liquidation risk:** up to 500x leverage means traders (and, indirectly, vault LPs) face severe [[liquidation]] and tail-risk; violent moves can cascade.
- **RWA & oracle risk:** pricing FX/commodity/equity perps depends on reliable price feeds; [[oracle-manipulation|oracle manipulation]] or stale feeds on RWA markets is a structural attack surface for any leveraged DEX.
- **Dilution:** ~68% of max supply is not yet circulating (MC/FDV ~0.32); unlocks can pressure price.
- **Near all-time-low price:** AVNT trades just above its ATL, indicating weak momentum/sentiment.
- **Regulatory risk:** offering leveraged equity/FX/commodity exposure on-chain ("Made in USA") raises securities/derivatives-regulation questions.
- **Smart-contract risk:** vaults and trading logic are [[smart-contracts]] on [[base]].
- **Market regime:** with the Fear & Greed Index at 23 (extreme fear) in an established bear market, leveraged-DEX tokens are highly sensitive to drawdowns and falling trading volume.

---

## Related

- [[crypto-markets]]
- [[base]]
- [[perpetual-futures]]
- [[decentralized-exchange]]
- [[real-world-assets]]
- [[hyperliquid]]
- [[edgex]]
- [[coinbase]]
- [[leverage]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-20: cryptodataapi.com / CoinGecko top-1000 markets data.

## Trading Profile

### Venues & liquidity

AVNT is a genuine two-venue market: it trades **spot on [[binance|Binance]]** (AVNT/USDT) alongside a **USD-margined [[perpetual-futures|perp]] on Binance**, and it has an **AVNT-PERP on [[hyperliquid|Hyperliquid]]** offering up to roughly **40–50x** [[leverage]]. Having both a top-tier CEX and the largest on-chain perp venue quoting the pair gives AVNT deeper, more continuous two-sided depth than a typical rank-~625 alt, and it opens a clean CEX-vs-DEX axis for [[funding-rate|funding]] and price comparison. Practically, that dual listing lets traders route to whichever book is deeper at execution time and split larger clips across venues to limit slippage. Still, at a small market cap the aggregate book is thin in absolute terms — size positions to the visible L2 depth, expect wider spreads and faster funding swings than large-caps, and watch that Binance-perp and Hyperliquid marks can diverge during fast moves.

### Applicable strategies

- [[funding-rate-harvest]] — with the AVNT perp live on both Binance and Hyperliquid, elevated funding on a crowded small-cap can be systematically collected against a spot or opposite-venue hedge.
- [[hl-vs-cex-funding-divergence]] — the Binance-perp vs Hyperliquid-perp pairing is the exact setup for trading funding-rate gaps between a CEX and Hyperliquid on the same AVNT contract.
- [[cash-and-carry]] — deep Binance spot plus a USD-margined perp lets you hold spot AVNT against a short perp to capture positive basis/funding with limited directional risk.
- [[liquidation-cascade-fade]] — high leverage (~40–50x on HL) on a thin-cap token makes AVNT prone to over-extended liquidation flushes that mean-revert, a fadeable extreme.
- [[oi-confirmed-trend]] — reading [[open-interest|OI]] alongside price on both venues helps separate genuine AVNT trends from squeeze-driven spikes.
- [[token-unlock-supply-event]] — with only ~one-third of max supply circulating (MC/FDV ~0.32), scheduled cliff unlocks are recurring, tradable supply events.

### Volatility & regime character

AVNT is a **high-beta DeFi / perp-DEX infrastructure token** — a Base-native leveraged-RWA perp venue — so it behaves like a small-cap alt with amplified moves versus [[bitcoin|BTC]] and [[ethereum|ETH]]: it tends to rally harder than beta in risk-on tapes and retrace fully when the perp-DEX and Base-DeFi narratives fade. It carries reflexive narrative beta to two themes (real-revenue perp DEXes and Base ecosystem growth) layered on top of broad-market direction, and trades near its all-time low, which keeps realized volatility and squeeze sensitivity elevated.

### Risk flags

- **Small-cap / liquidity concentration:** rank ~625 with a modest cap; despite two venues, absolute depth is limited and the market can gap on flow.
- **Token unlocks / emissions:** ~68% of max supply (~676M AVNT) still to unlock (MC/FDV ~0.32) is a structural overhang and a source of supply-driven downside.
- **Narrative dependence:** price is highly sensitive to perp-DEX and Base-DeFi sentiment; a fading narrative removes the primary bid.
- **Perp funding dislocations:** thin small-cap perps can see funding spike and Binance vs Hyperliquid marks diverge, whipsawing leveraged positions.
- **Leverage / cascade risk:** high available leverage makes AVNT prone to fast [[liquidation]] cascades in either direction.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/summary?coin=AVNT` — all-in-one perp data (mark, funding, OI)
- `GET /api/v1/hyperliquid/prices` — all mid prices
- `GET /api/v1/hyperliquid/l2-book?coin=AVNT` — L2 order-book depth
- `GET /api/v1/hyperliquid/open-interest` — all-asset open interest

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=AVNT&interval=1h&limit=1000` — OHLCV candles
- `GET /api/v1/hyperliquid/funding-rates?coin=AVNT&limit=100` — funding history
- `GET /api/v1/daily/hyperliquid` — daily bulk snapshot of ~230 HL perps

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/summary?coin=AVNT"
```

Auth: `X-API-Key` header. Endpoint catalog: [[cryptodataapi-hyperliquid]]. See also [[cryptodataapi]].

---

## See Also

- [[crypto-markets]]
- [[base]]

---
