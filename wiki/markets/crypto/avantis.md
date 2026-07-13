---
title: "Avantis"
type: entity
created: 2026-04-09
updated: 2026-06-20
status: excellent
tags: [crypto, defi, derivatives, perpetuals]
aliases: ["AVNT"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.avantisfi.com/"
related: ["[[crypto-markets]]", "[[base]]", "[[perpetual-futures]]", "[[decentralized-exchange]]", "[[real-world-assets]]", "[[hyperliquid]]", "[[edgex]]", "[[coinbase]]"]
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
