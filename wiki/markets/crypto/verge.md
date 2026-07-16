---
title: "Verge"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, altcoins]
aliases: ["XVG"]
entity_type: protocol
founded: 2014
headquarters: "Decentralized"
website: "http://vergecurrency.com/"
related: ["[[bitcoin]]", "[[crypto-markets]]", "[[monero]]", "[[privacy-coins]]", "[[verus-coin]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[liquidation-cascade-fade]]", "[[oi-confirmed-trend]]"]
---

# Verge

**Verge** (ticker **XVG**) is a privacy-focused Layer-1 cryptocurrency launched in 2014 (originally as *DogecoinDark*). It is one of the older [[privacy-coins|privacy coins]], built to obfuscate user IP addresses by routing transactions over anonymity networks such as **Tor** and **I2P**, with optional on-chain privacy via its **Wraith Protocol**. It is open-source, community-run, and was neither ICO-funded nor premined.

---

## Overview

Verge began its journey in 2014 under the name **DogecoinDark**, created to offer a "truly private" cryptocurrency. Its founder felt [[bitcoin|Bitcoin]] was insufficiently anonymous and built a chain where transactions and identities are harder to trace. Verge uses anonymity-centric networks (**TOR** and **I2P**) to fully obfuscate user IP addresses; its Core QT wallet ships with built-in Tor integration and SSL encryption.

Verge is an open-source project with a globally distributed, volunteer-style development team in close contact with its community. Notably, it is **not** a private company funded through an ICO or premine.

**Wraith Protocol** is Verge's technology package enabling private sends/receives via stealth addressing, and migrating QT wallet users off clearnet onto SSL-enabled Tor. Wraith lets users **switch between public and private ledgers** on the same blockchain — when Wraith is switched ON, transaction data is not visible even via the blockchain explorer, and IP addresses are obscured in both modes. Verge advertises fast transaction speed (~5 seconds) using Simple Payment Verification (SPV).

> The above descriptive content is preserved from the original project description (Source: [[coingecko-top-1000-2026-04-09]]).

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | XVG |
| **Market Cap Rank** | #506 |
| **Current Price** | $0.00255329 |
| **Market Cap** | $42.18M |
| **24h Volume** | $2.79M |
| **24h Change** | +2.30% |
| **7d Change** | +3.03% |
| **Circulating Supply** | ~16.52B XVG |
| **All-Time High** | $0.261874 (2017-12-24), -99.0% |
| **All-Time Low** | $0.00000223 (2015-12-16) |
| **Genesis Date** | 2014-10-09 |
| **Hashing Algorithm** | Scrypt (multi-algorithm Proof-of-Work) |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

The snapshot lands in an **"Established Bear Market"** with the Crypto Fear & Greed Index at **~23 (Extreme Fear)**. XVG was modestly green on the day and week. Reported 24h volume (~$2.79M) was firmer than the prior snapshot but still light against a ~$42M cap — a recurring liquidity problem for XVG (see Risks), driven structurally by the ongoing delisting of privacy coins from major regulated exchanges.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~16.52B XVG |
| **Total Supply** | ~16.56B XVG |
| **Max Supply** | Unlimited |
| **Market Cap / FDV** | ~1.00 |

Verge is a Proof-of-Work coin with a very large, mining-emitted supply (tens of billions of XVG) and **no hard max supply cap**, so it remains mildly inflationary via block rewards. Nearly all supply is mined and circulating (MC/FDV ≈ 1.00).

---

## How & Where It Trades

**Spot (CEX):** XVG retains a major listing on Binance (XVG/USDT) plus various second-tier exchanges. However, its venue access is **structurally constrained**: many regulated exchanges have delisted or restricted [[privacy-coins|privacy coins]] (Verge among them) to satisfy AML/KYC and travel-rule requirements, particularly in markets like the EU, the UK, Japan and South Korea. This shrinks the addressable trading audience and concentrates liquidity on fewer venues.

**Liquidity profile:** XVG's daily turnover is light relative to its market cap (~$2.8M against ~$42M, ~6.6% velocity at the snapshot). Combined with delisting pressure, this makes execution of larger orders difficult without slippage, and turnover can swing sharply between snapshots.

**Derivatives:** Verge has little to no meaningful perpetual-futures footprint on major derivatives venues — a contrast with the meme tokens elsewhere in this wiki, and partly a downstream effect of the same privacy-coin delisting/compliance dynamics that limit its spot listings.

---

## Valuation Framing (qualitative)

XVG is a **legacy privacy coin** valued on residual brand and a long survival record rather than on usage or fundamentals. Lenses:

- **Fully circulating / no overhang** — MC/FDV ≈ 1.00, so there is no unlock risk; the supply story is mild PoW inflation from an uncapped emission, not vesting.
- **Privacy discount + delisting drag** — the dominant valuation factor is structural: regulated-exchange delistings shrink the addressable buyer base, capping demand regardless of technology. This is a headwind shared with [[monero|Monero]] and Zcash but more acute given Verge's smaller venue footprint.
- **Weaker privacy = weaker moat** — because Verge's IP-obfuscation (Tor/I2P) + optional Wraith model is widely regarded as less robust than Monero's always-on cryptographic privacy, it captures less of the privacy-premium that supports XMR's valuation.

Net: a deep-drawdown legacy asset whose price is dominated by privacy-sector sentiment and liquidity, not protocol cash flows.

---

## Peer Comparison

| Token | Rank | Price | Market cap | Privacy model | Supply | Venue access |
|---|---|---|---|---|---|---|
| **XVG (Verge)** | #506 | $0.00255 | ~$42M | Tor/I2P IP obfuscation + optional Wraith | Uncapped PoW | Constrained (delistings) |
| [[monero\|XMR]] | large-cap | — | — | Always-on (ring sigs, RingCT, stealth) | Tail emission | Constrained (delistings) |
| [[verus-coin\|VRSC]] | #582 | $0.436 | ~$35M | Optional Sapling zk-shielding | ~83.5M cap | Very thin |
| Zcash (ZEC) | mid-cap | — | — | Optional zk-SNARK shielding | 21M cap | Constrained |

Verge sits at the lower-assurance end of the [[privacy-coins|privacy-coin]] spectrum (network-layer obfuscation rather than mandatory cryptographic privacy), which is its core differentiator and its core weakness.

---

## Use Case, Narrative & Category

Verge's category is **privacy**: it is a [[privacy-coins|privacy coin]] competing in the same conceptual space as [[monero|Monero]] (XMR) and Zcash. Its differentiation is network-layer anonymity (Tor/I2P IP obfuscation) plus optional ledger-level privacy via Wraith, and an emphasis on fast, cheap payments. Its narrative leans on being a long-lived, community-run, fairly-launched privacy project. In practice, Verge's privacy model (IP obfuscation + optional stealth) is generally regarded as weaker than Monero's always-on cryptographic privacy (ring signatures, RingCT, stealth addresses).

---

## Notable History

- **2014-10-09** — Genesis as **DogecoinDark**; later rebranded to Verge.
- **2017-12-24** — All-time high of ~$0.2619 during the 2017 bull run; XVG sits roughly **-99.0%** below that ATH as of 2026-06-21.
- **2015-12-16** — All-time low of ~$0.00000223.
- **2018** — Suffered notable **51%-style timestamp/mining exploits** on its multi-algorithm PoW chain, allowing attackers to mint blocks rapidly — a frequently cited security incident for the project.
- **2014–present** — Persisted as a small-cap privacy coin through multiple cycles; ongoing exchange delistings of privacy assets have weighed on liquidity.

---

## Risks

- **Delisting / regulatory risk** — As a privacy coin, XVG faces ongoing removal or restriction from regulated exchanges (AML/KYC, travel rule), shrinking liquidity and accessibility. This is the single most important structural risk.
- **Thin liquidity** — Low 24h volume vs market cap means high slippage and gap risk; exiting size is hard.
- **Weaker privacy guarantees** — Verge's IP-obfuscation + optional Wraith model is generally considered less robust than Monero's always-on cryptographic privacy.
- **Security history** — Past 51%/timestamp exploits (2018) are a reminder of multi-algorithm PoW attack surface.
- **Inflationary, uncapped supply** — No max supply; continued PoW emissions dilute holders over time.
- **Extreme drawdown** — Down ~99.0% from its 2017 ATH; macro backdrop is an established bear market with Fear & Greed at ~23 (extreme fear).

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 1,571 |
| **GitHub Forks** | 388 |
| **Pull Requests Merged** | 288 |
| **Contributors** | 72 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Trading Profile

### Venues & liquidity

XVG is tradable on **Binance** — both **spot** (XVG/USDT) and a **USD-margined perpetual**, which surfaces funding, open interest and liquidation data. It is **NOT** listed on Hyperliquid, so **Binance is the primary (and effectively sole) leveraged venue**. This concentration matters for execution: with light spot turnover (~$1–3M/day against a ~$35M cap) and privacy-coin delisting pressure elsewhere, both the spot book and the perp order book are thin. Available leverage on the Binance perp is typically lower and its liquidation tiers tighter for a low-cap alt like XVG, so **position sizing should be conservative** — large orders will move the book, funding can swing hard on small OI, and there is no second leveraged venue to hedge against or arbitrate a stuck Binance funding print. Route spot execution to Binance where depth is deepest, and treat perp positions as venue-concentrated risk.

### Applicable strategies

- [[funding-rate-harvest]] — XVG's single-venue Binance perp with thin OI can hold persistently skewed funding; harvest it by holding the opposite side while delta-hedging with spot.
- [[crowded-long-funding-fade]] — sentiment-driven privacy-coin squeezes on a shallow perp book leave funding overheated on the long side; fade the crowd when funding runs rich.
- [[liquidation-cascade-fade]] — a shallow XVG perp liquidates violently on small flow; fade forced-sale wicks back toward pre-cascade spot value.
- [[oi-confirmed-trend]] — with only Binance OI to watch, rising open interest alongside price gives a cleaner (if noisy) confirmation of directional XVG moves.
- [[breakout-and-retest]] — XVG's deep-drawdown, low-price chart ranges tightly for long stretches then gaps; trade confirmed breakouts on the retest to avoid thin-book fakeouts.
- [[atr-trailing-stop]] — high per-tick volatility on a low-liquidity name demands volatility-scaled trailing stops rather than fixed levels.

### Volatility & regime character

XVG is a **small-cap legacy privacy coin** (rank ~563) with high reflexive volatility on very light liquidity — moves are amplified by thin depth rather than by fundamentals. It is **high-beta to BTC/ETH** in broad risk-on/risk-off swings but also carries idiosyncratic, **privacy-sector-sentiment** and delisting-headline risk that can decouple it from majors. Not a DeFi or infra token; behaviour is closer to a low-float, narrative-and-liquidity-driven altcoin than to a fundamentally valued asset.

### Risk flags

- **Venue concentration** — Binance is the only meaningful spot and the only leveraged venue; a Binance delisting or restriction (a live risk for privacy coins) would gut both liquidity and the perp.
- **Thin liquidity** — low 24h volume vs cap means high slippage, gap risk and violent, low-notional liquidation cascades on the perp.
- **Regulatory / delisting** — as a privacy coin, XVG faces ongoing AML/KYC and travel-rule delisting pressure across regulated exchanges; this is its dominant structural risk.
- **Uncapped inflationary emission** — no max supply; continued PoW block rewards dilute holders and cap sustained upside.
- **Narrative dependence** — price is driven by privacy-sector sentiment and liquidity, not protocol cash flows, so it is vulnerable to headline-driven reversals.

---

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=XVGUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=XVGUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=XVG` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=XVG` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=XVGUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=XVGUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=XVG"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[privacy-coins]]
- [[monero]]
- [[verus-coin]] — fellow fair-launch privacy/identity L1
- [[bitcoin]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko; `raw/data/crypto-loop/coingecko-markets.json`).

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | XVG |
| **Market Cap Rank** | #563 |
| **Market Cap** | $34.78M |
| **Current Price** | $0.00210545 |
| **Genesis Date** | 2014-10-09 |
| **Hashing Algorithm** | Scrypt |
| **Categories** | Smart Contract Platform, Privacy Coins, Proof of Work (PoW), Made in USA, Privacy |
| **Website** | [http://vergecurrency.com/](http://vergecurrency.com/) |

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 16.52B XVG |
| **Total Supply** | 16.55B XVG |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $34.85M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.2619 (2017-12-24) |
| **Current vs ATH** | -99.20% |
| **All-Time Low** | $0.00000223 (2015-02-06) |
| **Current vs ATL** | +94185.23% |
| **24h Change** | -0.48% |
| **7d Change** | -1.02% |
| **30d Change** | -23.29% |
| **1y Change** | -67.73% |

---

## Platform & Chain Information

**Native Chain:** Own blockchain (Layer 1)

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | XVG/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [http://vergecurrency.com/](http://vergecurrency.com/) |
| **Twitter** | [@vergecurrency](https://twitter.com/vergecurrency) |
| **Reddit** | [https://www.reddit.com/r/vergecurrency](https://www.reddit.com/r/vergecurrency) |
| **Telegram** | [officialxvg](https://t.me/officialxvg) (2,634 members) |
| **Discord** | [https://discord.com/invite/vergecurrency](https://discord.com/invite/vergecurrency) |
| **GitHub** | [https://github.com/vergecurrency/verge](https://github.com/vergecurrency/verge) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $1.46M |
| **Market Cap Rank** | #563 |
| **24h Range** | $0.00210452 — $0.00216691 |
| **CoinGecko Sentiment** | 100% positive |
| **Last Updated** | 2026-07-16 |

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---
