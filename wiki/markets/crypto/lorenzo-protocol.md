---
title: "Lorenzo Protocol"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [bitcoin, crypto, defi, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, altcoins]
aliases: ["BANK"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://lorenzo-protocol.xyz/"
related: ["[[bitcoin]]", "[[bnb]]", "[[crypto-markets]]", "[[defi]]", "[[governance-token]]", "[[liquid-restaking]]", "[[liquid-staking]]", "[[real-world-assets]]", "[[restaking]]", "[[stablecoin]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[funding-rate-harvest]]", "[[cash-and-carry]]"]
---

# Lorenzo Protocol

**Lorenzo Protocol** (BANK) is a [[bitcoin|Bitcoin]] [[liquid-staking|liquid-staking]] and on-chain asset-management protocol that positions itself as a **"financial abstraction layer"** for tokenized, yield-bearing financial products. It lets users stake/restake BTC to receive liquid representations (such as **stBTC** and the wrapped **enzoBTC**) and provides structured, fund-like on-chain products (e.g., **USD1+** yield funds). Built in the [[bnb|BNB Chain]] ecosystem and backed by YZi Labs (formerly Binance Labs), it sits in the **BTCfi** (Bitcoin DeFi) category. **BANK** is its [[governance-token|governance token]].

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

As of 2026-06-22, BANK traded at **$0.03796252**, ranked **#916** by market capitalization with a market cap of approximately **$16,125,028**. It declined over the short term — **-1.68% over 24 hours** and **-5.58% over the trailing 7 days** — against an "Extreme Fear" market (Fear & Greed Index **21**). BANK trades well below its October 2025 all-time high near $0.23, having retraced sharply since launch.

---

## What Lorenzo Protocol Does

Lorenzo is a BTCfi and on-chain asset-management platform with two intertwined pillars:

1. **Bitcoin liquid staking / restaking** — users deposit BTC and receive liquid, transferable tokens that represent the staked position and accrue yield. The protocol separates principal and yield concepts so that the liquid token can be used elsewhere in [[defi]] while the underlying BTC earns rewards. Key tokens include **stBTC** (a liquid staked-BTC representation) and **enzoBTC** (a wrapped/standardized BTC representation for use across chains and products).
2. **Financial Abstraction Layer (on-chain asset management)** — Lorenzo packages strategies into tokenized, fund-like products. Its **USD1+** offering is a stablecoin-denominated yield fund concept that abstracts underlying yield strategies into a single on-chain token, giving holders exposure to managed yield without operating the strategies themselves.

The "financial abstraction layer" framing means Lorenzo aims to be the issuance and accounting layer that turns off-chain and on-chain yield strategies into composable, tokenized products — effectively bringing structured-product and fund mechanics on-chain.

---

## Mechanism and Architecture

- **Liquid staking tokens (LSTs)** — staking BTC mints a liquid receipt token ([[liquid-staking]]). This preserves capital efficiency: the staked BTC keeps earning while its tokenized form remains usable as collateral or in other protocols.
- **Principal/yield separation** — Lorenzo's design distinguishes principal tokens from yield-accruing tokens, enabling structured-product construction.
- **Wrapped/standardized BTC (enzoBTC)** — a normalized BTC representation that improves composability across chains and within Lorenzo's product suite.
- **Tokenized funds (USD1+ and similar)** — on-chain vehicles that route deposits into yield strategies and represent ownership with a single fund token, with NAV/accounting handled by the protocol's abstraction layer.
- **Bitcoin-staking foundation** — Lorenzo's BTC yield is connected to the broader Bitcoin-staking trend (e.g., Babylon-style BTC staking infrastructure), which underpins much of the current BTCfi wave.

---

## Token Role: BANK

BANK is Lorenzo's [[governance-token|governance token]]:

- **Governance** — voting on protocol parameters, product approvals, and treasury decisions, commonly via a vote-escrow (veBANK) model that rewards long-term lockups with greater voting weight.
- **Incentives** — directing emissions/rewards across the protocol's products and liquidity.
- **Value alignment** — tying long-term holders to the growth of Lorenzo's staking and asset-management products.

### Value accrual and veBANK

- **Vote-escrow (veBANK).** BANK uses a [[curve-finance|Curve]]-style vote-escrow design: locking BANK for a time period mints non-transferable veBANK, whose weight scales with lock duration. veBANK confers heavier voting power and a larger share of protocol incentives/rewards, aligning governance influence with long-term commitment.
- **Fee / incentive direction.** veBANK holders steer where emissions and incentives flow across Lorenzo's products (stBTC, enzoBTC, USD1+ funds and their liquidity), analogous to gauge-voting in other DeFi protocols. This makes BANK a meta-token over Lorenzo's product suite rather than a direct claim on a single asset.
- **Real-yield dependency.** Durable BANK value accrual depends on Lorenzo capturing fees from genuine asset-management activity (AUM in its funds, BTC-staking flows) rather than on emissions alone — the same emissions-vs-fees tension that defines the BTCfi category.

BANK has a large max supply (2.10B) with only a portion circulating, so future unlocks and emissions represent a meaningful dilution consideration.

---

## Competitive Position

Lorenzo competes in the fast-growing **BTCfi / Bitcoin liquid-staking** arena alongside protocols such as Lombard (LBTC), Solv, pStake, and other BTC-yield issuers, as well as broader on-chain asset managers. Its differentiators are the "financial abstraction layer" framing (structured, fund-like products rather than a single LST), the stBTC/enzoBTC token suite, USD1+ funds, and backing from YZi Labs within the [[bnb|BNB Chain]] ecosystem. The category is competitive and depends on the durability of [[bitcoin|Bitcoin]]-staking yield sources; share is not yet settled among the leaders.

| Protocol | Liquid token(s) | Underlying yield source | Distinguishing angle | Chain focus |
|---|---|---|---|---|
| **Lorenzo** | stBTC, enzoBTC; USD1+ fund | Babylon-style BTC staking + managed strategies | "Financial abstraction layer": tokenized fund/structured products, principal/yield separation | [[bnb\|BNB Chain]] |
| **Lombard** | LBTC | Babylon BTC staking | Largest BTC-LST by adoption; DeFi-integration breadth | Multi-chain |
| **Solv Protocol** | SolvBTC (+ yield variants) | Aggregated BTC yield (staking, basis, RWA) | BTC "yield aggregator" / reserve abstraction | Multi-chain |
| **pStake (BTCfi)** | yBTC / stkBTC | Babylon BTC staking | Persistence-team BTC staking | Multi-chain |
| **Babylon** | (native staking) | Bitcoin self-custodial staking (security layer) | The base BTC-staking infrastructure others build on | Bitcoin + BSNs |

Lorenzo's positioning is less "just an LST" and more an **on-chain asset manager**: stBTC/enzoBTC are inputs, and the headline product is the packaging of yield strategies into single fund tokens (USD1+ and similar). That broadens its addressable market beyond pure BTC stakers but also means it competes with on-chain asset managers and structured-product issuers, not only BTC-LST rivals.

---

## Risks

- **Smart-contract and bridging risk** — liquid-staking and wrapped-BTC systems involve complex contracts and cross-chain components; exploits or bridge failures can cause loss of underlying BTC.
- **Peg / redemption risk** — stBTC and enzoBTC rely on maintaining a tight peg and reliable redemption to underlying BTC; stress events can cause depegs.
- **Yield-source / counterparty risk** — fund products (e.g., USD1+) depend on underlying strategies whose returns and counterparties carry risk; advertised yields are not guaranteed.
- **Micro-cap token volatility** — at ~$16.4M (rank #912), BANK is a small-cap that has fallen sharply from its all-time high.
- **Dilution overhang** — a large gap between circulating and max supply implies future emissions/unlocks.
- **Dependence on BTC-staking infrastructure** — Lorenzo's core yield is tied to the broader Bitcoin-staking ecosystem; changes there propagate to Lorenzo.

> **Data disclaimer:** Figures above are point-in-time market snapshots (2026-06-22) and qualitative descriptions of mechanism. TVL, yields/APY, peg status, and audit details are not independently verified here and should be confirmed against official documentation and on-chain analytics before any decision.

---

## Platform & Chain Information

**Native Chain:** [[bnb|BNB Chain]] (Binance Smart Chain)

### Contract Addresses

| Chain | Address |
|---|---|
| BNB Chain | `0x3aee7602b612de36088f3ffed8c8f10e86ebf2bf` |

---

## Tokenomics

| Metric | Value |
|---|---|
| **Max Supply** | 2.10B BANK |
| **Market Cap / FDV** | Partial supply circulating (dilution overhang) |

*Note: exact circulating supply and FDV change with each snapshot; re-verify at source.*

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair |
|---|---|
| Binance | BANK/USDT |
| Bitget | BANK/USDT |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://lorenzo-protocol.xyz/](https://lorenzo-protocol.xyz/) |
| **Twitter** | [@LorenzoProtocol](https://twitter.com/LorenzoProtocol) |
| **Telegram** | [LorenzoProtocol](https://t.me/LorenzoProtocol) |
| **Docs** | [https://docs.lorenzo-protocol.xyz/](https://docs.lorenzo-protocol.xyz/) |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Trading Profile

### Venues & liquidity

BANK is tradable on [[binance]] — both **spot** (BANK/USDT) and a **USD-margined [[perpetual-futures|perpetual]]** contract, which exposes [[funding-rate|funding]], [[open-interest]], and [[liquidations|liquidation]] data. It is **not** listed on Hyperliquid, so Binance is the primary leveraged venue and the dominant source of price discovery for both cash and derivatives. Because leverage, funding, and OI flow are concentrated on a single exchange, execution and hedging depend heavily on Binance depth: as a micro-cap (~rank #709) the perp order book is thin relative to majors, so sizing should account for wider spreads, slippage on market orders, and elevated liquidation risk during volatility spikes. The lack of a second deep perp venue also limits cross-exchange arbitrage and makes any funding/basis dislocations harder to hedge away.

### Applicable strategies

- [[funding-rate-harvest]] — the single-venue Binance perp on a low-cap governance token tends to swing between funding extremes; collect funding by holding the side paid to carry, hedged against spot.
- [[crowded-long-funding-fade]] — after sharp rallies (BANK has shown large multi-day pumps), retail crowding into longs drives funding positive; fade the crowded long as funding overheats.
- [[cash-and-carry]] — pair long Binance spot BANK against short USD-M perp to monetize positive perp basis without directional exposure, the cleanest carry structure given the single leveraged venue.
- [[liquidation-cascade-fade]] — thin perp depth plus high leverage on a micro-cap makes liquidation wicks common; fade the over-extended cascade once forced selling/buying exhausts.
- [[volatility-breakout]] — BANK exhibits high realized volatility and unlock/emission-driven regime shifts; trade confirmed breakouts from compression with defined invalidation.
- [[oi-confirmed-trend]] — use Binance open-interest changes to confirm whether a BANK move is backed by fresh positioning rather than a squeeze, filtering false trends.

### Volatility & regime character

BANK is a **micro-cap DeFi/BTCfi governance token** with high beta and pronounced reflexivity — it has whipsawed from a ~$0.23 ATH down to the low single-cent range and back with large multi-day swings, so realized volatility runs far above BTC/ETH. Direction is highly correlated to broad crypto risk-on/risk-off and to the BTCfi/liquid-staking narrative; in fear regimes it tends to sell off harder than majors, and in narrative-driven rallies it can spike violently on thin liquidity. Treat it as a small-cap altcoin whose moves are amplified versions of the broader BTC/ETH tape rather than an independent driver.

### Risk flags

- **Venue concentration** — leveraged liquidity is concentrated on Binance; a listing change, outage, or funding dislocation there has outsized impact with no deep secondary perp venue to hedge.
- **Unlocks / emissions dilution** — large max supply (2.10B) with only a portion circulating means scheduled unlocks and veBANK emissions are a recurring supply overhang that can pressure price.
- **Narrative dependence** — valuation leans on the durability of the BTCfi / Bitcoin-staking narrative and real fee capture; narrative fatigue or emissions-over-fees dynamics can compress the token.
- **Liquidity / micro-cap risk** — thin order books amplify slippage and make liquidation cascades and stop-runs more violent; size conservatively.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=BANKUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=BANKUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=BANK` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=BANK` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=BANKUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=BANKUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=BANK"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[bnb]]
- [[bitcoin]]
- [[liquid-staking]]
- [[defi]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko snapshot); Fear & Greed Index 21 (Extreme Fear).
- General market knowledge; no additional specific wiki source ingested yet.

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | BANK |
| **Market Cap Rank** | #707 |
| **Market Cap** | $26.08M |
| **Current Price** | $0.0613 |
| **Categories** | Liquid Staking, BTCfi Protocol |
| **Website** | [https://lorenzo-protocol.xyz/](https://lorenzo-protocol.xyz/) |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.2307 (2025-10-18) |
| **Current vs ATH** | -73.74% |
| **All-Time Low** | $0.0224 (2026-06-05) |
| **Current vs ATL** | +169.98% |
| **24h Change** | +39.76% |
| **7d Change** | +74.21% |
| **30d Change** | +46.53% |
| **1y Change** | +0.12% |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $30.33M |
| **Market Cap Rank** | #707 |
| **24h Range** | $0.0438 — $0.0607 |
| **CoinGecko Sentiment** | 75% positive |
| **Last Updated** | 2026-07-16 |

---
