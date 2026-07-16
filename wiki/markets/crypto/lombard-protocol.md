---
title: "Lombard"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [bitcoin, crypto, defi, restaking, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, altcoins]
aliases: ["BARD", "LBTC", "Lombard Protocol"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.lombard.finance/"
related: ["[[babylon]]", "[[bitcoin]]", "[[crypto-markets]]", "[[decentralized-finance]]", "[[defi]]", "[[ethereum]]", "[[liquid-staking]]", "[[restaking]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[funding-rate-harvest]]", "[[token-unlock-supply-event]]"]
---

# Lombard

**Lombard** (BARD) is a Bitcoin-DeFi ("BTCfi") protocol building onchain Bitcoin capital markets. Founded in 2024, it issues **LBTC** — a yield-bearing, liquid representation of [[bitcoin|BTC]] — secured by a decentralized consortium of digital-asset institutions, described as the largest Bitcoin liquid-staking token (LST). BARD is the protocol's native governance token, live on [[ethereum|Ethereum]] and BNB Chain.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | BARD |
| **Chain** | [[ethereum|Ethereum]] (native); also BNB Chain |
| **Current Price** | $0.151979 |
| **Market Cap** | $50,602,405 |
| **Market Cap Rank** | #449 |
| **24h Volume** | $2,801,716 |
| **24h Change** | +0.44% |
| **7d Change** | -7.46% |
| **Fully Diluted Valuation** | $152,044,786 |
| **Market Cap / FDV** | ~0.33 |
| **All-Time High** | $1.70 (2026-03-05) |
| **All-Time Low** | $0.146407 (2026-06-06) |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

Trading context: the market is in **extreme fear** (Crypto [[crypto-fear-and-greed-index|Fear & Greed Index]] = 23) and an **established bear market** as of 2026-06-21. BARD ticked up ~0.4% on the day but is down ~7.5% on the week, trading just above its all-time low (~$0.146, set 2026-06-06) and roughly **91% below its March 2026 ATH of $1.70** — a severe drawdown for a recently launched BTCfi token. The MC/FDV ratio of ~0.33 signals heavy dilution overhang. Note: this market data is for the **BARD governance token**, distinct from **LBTC** (the [[liquid-staking|liquid-staking token]] that tracks the price of [[bitcoin|BTC]]).

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~332.81M BARD |
| **Total Supply** | 1.00B BARD |
| **Max Supply** | 1.00B BARD |
| **Market Cap / FDV** | ~0.33 |

About one-third of max supply is circulating, leaving meaningful **unlock/dilution overhang** (FDV ~$150M vs MC ~$50M). BARD is the governance and incentive token for the Lombard ecosystem; its value thesis is tied to LBTC adoption and the growth of onchain BTC capital markets rather than to BTC's price directly. BARD was distributed in part via a Binance HODLer airdrop and was featured in Binance Alpha Spotlight.

---

## How & Where It Trades

### Protocol mechanics (the venue itself)
Lombard is BTC liquid-staking infrastructure:

- **LBTC mint** — users deposit BTC and receive **LBTC**, a 1:1-backed liquid staking token. BTC is secured through Lombard's **decentralized consortium of digital-asset institutions** (a multi-party custody/validation set) rather than a single custodian, with mint/redeem handled by the protocol.
- **Yield generation** — LBTC is **yield-bearing**: underlying BTC is put to work (historically via Babylon-style Bitcoin staking / restaking and DeFi integrations), so holders earn yield while retaining a liquid, transferable token.
- **DeFi composability** — LBTC can be used as collateral, in liquidity pools, and across lending/restaking venues on EVM chains, letting BTC holders earn DeFi yield without giving up BTC exposure.
- **Staking SDK & infrastructure** — Lombard provides a full-stack BTC staking SDK and supporting services so other protocols and platforms can integrate LBTC and onchain BTC.

### Spot venues for the BARD token
- **Centralized:** Binance (BARD/USDT), Upbit (BARD/KRW), Bitget (BARD/USDT), KuCoin (BARD/USDT).
- **Decentralized:** Uniswap V3 on Ethereum (BARD paired with USDT).

With ~$2.8M/24h volume and a Binance listing, BARD has moderate spot liquidity for a sub-$100M-cap token. Derivatives markets (perp OI/funding) on BARD, where they exist, are venue-specific and not a stable data point at this snapshot. The economically meaningful flow is **LBTC mint/redeem and TVL**, not BARD-token derivatives.

### Contract addresses
| Chain | Address |
|---|---|
| Ethereum | `0xf0db65d17e30a966c2ae6a21f6bba71cea6e9754` |
| BNB Chain | `0xd23a186a78c0b3b805505e5f8ea4083295ef9f3a` |

---

## Use Case / Narrative / Category

Lombard sits in the **BTCfi / Bitcoin [[liquid-staking|liquid staking]] & [[restaking]]** category — the thesis that Bitcoin's enormous idle capital can be made productive onchain. By issuing LBTC, Lombard lets [[bitcoin|BTC]] holders earn yield and access [[restaking]] and [[defi|DeFi]] while staying long BTC. Its differentiator is the institutional consortium securing the asset (multi-party rather than single-custodian) and positioning LBTC as the leading Bitcoin LST. The narrative rides the broader "make BTC productive" wave alongside other Bitcoin-staking and restaking ecosystems (notably [[babylon|Babylon]]-anchored designs).

---

## Valuation Framing (qualitative)

BARD's value thesis decouples from BTC's price: it is a **governance/incentive claim on the growth of LBTC and onchain BTC capital markets**, not a BTC proxy. The relevant drivers are (1) **LBTC TVL** and the share of the Bitcoin LST market Lombard holds, (2) the **fee/yield economics** captured by the protocol and routed to BARD via governance, and (3) whether the institutional-consortium custody model becomes the trusted standard for productive BTC. The valuation tension is acute: BARD has fallen ~91% from ATH and trades at a low MC (~$50M) but a much higher FDV (~$152M), so **roughly two-thirds of supply is still to unlock** — a structural headwind. The bull case is that BTCfi adoption compounds and LBTC entrenches as the category leader; the bear case is that BTC-staking yields and BTCfi demand stay thin while unlocks dilute holders, as the post-launch drawdown illustrates.

---

## Peer Comparison (BTCfi / Bitcoin LSTs)

| Token / Asset | Type | MC Rank | Market Cap | Supply | Notes |
|---|---|---|---|---|---|
| **BARD** (this page) | BTCfi governance token | #449 | ~$51M | 1B cap, ~33% circ | Governs Lombard; LBTC issuer |
| **LBTC** | Bitcoin [[liquid-staking|LST]] (tracks BTC) | — | tied to TVL | 1:1 BTC-backed | The yield-bearing BTC asset itself |
| [[babylon\|Babylon (BABY)]] | Bitcoin staking protocol | mid-cap | mid-cap | Capped | Provides the underlying BTC staking layer |
| [[bitcoin\|wBTC / tBTC]] | Wrapped BTC (no yield) | n/a | large | 1:1 BTC | Non-yield-bearing BTC representations |

BARD is a **token on the BTCfi platform**, not BTC itself — investors must separate exposure to *Bitcoin's price* (hold BTC/LBTC) from exposure to *Lombard's business* (hold BARD). Its closest functional peers are the governance tokens of competing BTC-staking/restaking ecosystems.

---

## Notable History

- Founded 2024; pioneered LBTC as a yield-bearing Bitcoin LST and grew it into (by its own description) the largest Bitcoin LST.
- BARD reached its all-time high of **$1.70** on 2026-03-05 around its token launch/listing phase, then fell sharply — roughly -71% over the 30 days into mid-2026.
- All-time low of **$0.146** printed on 2026-06-06; BARD trades near that level on 2026-06-20.

---

## Risks

- **Custody / consortium risk** — LBTC's backing depends on the decentralized institutional consortium that holds/secures the underlying BTC; a failure, collusion, or compromise of that custody set is the core systemic risk to LBTC's 1:1 backing.
- **Slashing / staking risk** — yield comes from Bitcoin staking/restaking arrangements that can carry slashing or counterparty risk; underlying yield strategies can underperform or incur losses.
- **De-peg risk (LBTC vs BTC)** — under stress or redemption queues, LBTC can trade below BTC parity in secondary markets even if ultimately redeemable.
- **Token dilution** — only ~33% of BARD supply circulates; ongoing unlocks pressure the BARD token specifically.
- **Smart-contract & bridge risk** — mint/redeem and cross-chain LBTC movement rely on contracts and bridges that are high-value targets.
- **Regime risk** — BTCfi yields and token valuations compress in bear markets; BARD's ~91% drawdown from ATH illustrates the sector's volatility.

---

## Related

- [[crypto-markets]]
- [[bitcoin]]
- [[ethereum]]
- [[restaking]]
- [[liquid-staking]]
- [[decentralized-finance]]
- [[defi]]
- [[babylon]]
- [[crypto-fear-and-greed-index]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-21 (cryptodataapi.com / CoinGecko top-1000).
- General market knowledge; no specific wiki source ingested yet.

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | BARD |
| **Market Cap Rank** | #508 |
| **Market Cap** | $40.83M |
| **Current Price** | $0.1227 |
| **Categories** | Decentralized Finance (DeFi), Binance HODLer Airdrops, BTCfi Protocol, Binance Alpha Spotlight, Buidlpad Launchpad |
| **Website** | [https://www.lombard.finance/](https://www.lombard.finance/) |

---

## Overview

Lombard is building onchain Bitcoin capital markets to unlock the full potential of the defining asset of this generation. Founded in 2024, the company pioneered Bitcoin’s integration into DeFi with LBTC — the leading yield-bearing Bitcoin, secured by a decentralized consortium of 14 digital asset institutions — which today stands as the largest Bitcoin LST. Lombard is developing full-stack infrastructure to accelerate onchain BTC adoption for holders, protocols, and platforms, spanning BTC assets, a Staking SDK, and supporting services. The company is built and backed by digital asset leaders, including top DeFi protocols, institutions, and exchanges.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 332.81M BARD |
| **Total Supply** | 1.00B BARD |
| **Max Supply** | 1.00B BARD |
| **Fully Diluted Valuation** | $122.67M |
| **Market Cap / FDV Ratio** | 0.33 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.70 (2026-03-05) |
| **Current vs ATH** | -92.78% |
| **All-Time Low** | $0.1203 (2026-07-15) |
| **Current vs ATL** | +2.07% |
| **24h Change** | +1.04% |
| **7d Change** | -3.51% |
| **30d Change** | -26.69% |
| **1y Change** | +0.00% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xf0db65d17e30a966c2ae6a21f6bba71cea6e9754` |
| Binance Smart Chain | `0xd23a186a78c0b3b805505e5f8ea4083295ef9f3a` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | BARD/USDT | N/A |
| Upbit | BARD/KRW | N/A |
| Bitget | BARD/USDT | N/A |
| KuCoin | BARD/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.lombard.finance/](https://www.lombard.finance/) |
| **Twitter** | [@lombard_finance](https://twitter.com/lombard_finance) |
| **Telegram** | [+FbE6IuGOrak1ZTVh](https://t.me/+FbE6IuGOrak1ZTVh) (5,437 members) |
| **Whitepaper** | [https://docs.lombard.finance/](https://docs.lombard.finance/) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $4.38M |
| **Market Cap Rank** | #508 |
| **24h Range** | $0.1213 — $0.1253 |
| **CoinGecko Sentiment** | 0% positive |
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

BARD is tradable on [[binance|Binance]] as both **spot** (BARD/USDT) and a **USD-margined perpetual**, so leveraged flow (funding, open interest, liquidations) is concentrated on a single primary venue. BARD is **not** listed on [[hyperliquid|Hyperliquid]], so Binance is the only meaningful leveraged venue — there is no deep second perp book to arbitrate against or to absorb size. With a sub-$100M cap and modest spot volume, the perp is the main source of intraday leverage; funding and OI can swing sharply on relatively small notional. Practically, this means: execution and sizing should assume thin depth and wide slippage on aggressive orders, size positions to the Binance book specifically, and treat funding/OI as venue-concentrated signals rather than market-wide ones. Cross-venue spot arbitrage exists (Upbit, Bitget, KuCoin, Uniswap V3) but the derivatives picture is Binance-centric.

### Applicable strategies

- [[funding-rate-harvest]] — collect perp funding on BARD's Binance USD-M contract when funding runs persistently positive/negative in a low-cap that lacks an offsetting perp venue.
- [[crowded-long-funding-fade]] — after a BARD bounce fuels crowded longs and rich positive funding, fade the over-leveraged side into the single Binance book.
- [[liquidation-cascade-fade]] — BARD's thin depth and one-venue perp make forced-liquidation flushes overshoot; fade capitulation wicks near the all-time-low zone.
- [[oi-price-exhaustion]] — rising Binance open interest against a stalling BARD price flags exhausted leverage and a squeeze setup in a supply-overhang token.
- [[token-unlock-supply-event]] — with only ~33% of supply circulating, scheduled BARD unlocks create predictable dilution/supply events to position around.
- [[range-mean-reversion]] — BARD chops in a tight low-cap range just above its ATL; fade extremes back toward the range mid.

### Volatility & regime character

BARD is a **small-cap DeFi / BTCfi governance token** (rank ~508, sub-$100M cap) with high beta and reflexive, low-liquidity price action — sharp drawdowns (~90%+ from ATH) and thin bounces. As a governance/incentive claim it is **narrative-driven** (BTCfi / Bitcoin liquid-staking adoption) rather than a direct BTC proxy: it broadly correlates with [[bitcoin|BTC]]/[[ethereum|ETH]] risk sentiment but its idiosyncratic swings track LBTC TVL, unlock schedules, and BTCfi-narrative flow. Expect large-cap-driven regime shifts to amplify in BARD due to its small float and single leveraged venue.

### Risk flags

- **Venue/liquidity concentration** — leverage lives almost entirely on Binance; no Hyperliquid perp means limited redundancy and higher slippage/liquidation-gap risk.
- **Unlocks / emissions** — ~two-thirds of max supply still to unlock is a persistent dilution headwind for the BARD token.
- **Narrative dependence** — value is tied to BTCfi adoption and LBTC growth; if the "productive BTC" narrative cools, BARD can stay bid-less.
- **Depeg / protocol linkage** — BARD sentiment is sensitive to any LBTC depeg, consortium-custody, or slashing event even though BARD itself is not BTC-backed.
- **Thin sentiment / drawdown regime** — trading near ATL in an established bear market with 0% CoinGecko positive sentiment; low-liquidity reversals can be violent in both directions.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=BARDUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=BARDUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=BARD` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=BARD` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=BARDUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=BARDUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=BARD"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---
