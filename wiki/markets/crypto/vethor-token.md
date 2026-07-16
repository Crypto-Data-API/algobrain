---
title: "VeThor"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, altcoins]
aliases: ["VTHO", "VeThor Token"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.vechain.org/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[vechain]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[funding-rate-harvest]]", "[[cash-and-carry]]"]
---

# VeThor

**VeThor** (ticker **VTHO**) is the **gas token** of the [[vechain]] blockchain. VeChain uses a **dual-token model**: **VET** (VeChain Token) is the value-transfer/staking asset, and **VTHO** (VeThor) is the energy/gas token consumed to pay for transactions and smart-contract execution. Crucially, holding VET *generates* VTHO continuously, so network usage costs are decoupled from the price of the primary asset — a design VeChain markets as better suited to enterprises than single-token chains like [[ethereum]].

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | VTHO |
| **Native chain** | VeChainThor (native gas asset) |
| **Price** | $0.00039276 |
| **Market Cap** | $39,554,667 |
| **Market Cap Rank** | #531 |
| **24h Volume** | $715,195 |
| **24h Change** | +1.35% |
| **7d Change** | -2.07% |
| **Circulating Supply** | 100.89B VTHO |
| **Total Supply** | 100.90B VTHO |
| **Max Supply** | Uncapped (inflationary; minted by [[vechain|VET]] holdings) |
| **Fully Diluted Valuation** | ~$39.56M |
| **Market Cap / FDV** | ~1.00 |
| **All-Time High** | $0.04671227 (2018-08-29) — now ~-99.2% |
| **All-Time Low** | $0.00015238 (2020-03-16) — now ~+157.7% |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

Context: VTHO is up ~1.3% on the day but down ~2% on the week, ~99% below its 2018 peak, against a market backdrop of **extreme fear** (Crypto [[crypto-fear-and-greed-index|Fear & Greed Index]] = **23**) and an "Established Bear Market."

---

## Tokenomics & Supply — the VET/VTHO Dual-Token Gas Model

VeChain deliberately separates **store of value** from **cost of use**:

- **VET** is the base asset (staking/value transfer). Simply *holding* VET in a wallet or node continuously **generates VTHO** at a base rate (historically ~0.000432 VTHO per VET per day), similar to the NEO/GAS relationship.
- **VTHO** is the **gas**: every transaction and contract call on VeChain is paid in VTHO, which is then **partially burned** (a portion of VTHO used as gas is destroyed). This creates a generation-vs-burn dynamic.
- **Implication:** if network activity (burn) outpaces VTHO generation, VTHO becomes deflationary; if generation outpaces usage (the common case in low-activity periods), VTHO is **inflationary**, which structurally caps its price and explains the very large supply (~100.88B) and tiny unit price. There is **no fixed max supply** — VTHO is minted perpetually by VET holdings.
- **MC/FDV ≈ 1.00:** total equals circulating, so there is no investor/team unlock cliff; the relevant "dilution" is the ongoing emission driven by VET holders, not a vesting schedule.
- **Enterprise rationale:** because dApp operating costs are paid in VTHO (cheap, separately supplied) rather than in the appreciating base asset, businesses get predictable transaction costs even if VET rises — VeChain's core pitch for enterprise adoption.

---

## How & Where It Trades

- **Spot (CEX):** Binance (VTHO/USDT), Kraken (VTHO/USD), Upbit (VTHO/KRW), Bitget (VTHO/USDT), KuCoin (VTHO/USDT), and Crypto.com Exchange (VTHO/USD).
- **Native chain:** VeChainThor; VTHO is the native gas asset and is not primarily a DEX/AMM asset.
- **Derivatives / Hyperliquid:** VTHO is far less commonly offered as a perpetual than VET; no perp/funding/open-interest data is recorded for VTHO in this snapshot, and traders seeking VeChain-ecosystem derivatives typically use **VET** perps instead. **No VTHO perp recorded.**
- **Liquidity profile:** ~$0.72M of 24h volume on a ~$39.6M cap (turnover <2%) — the thinnest book in this batch, so VTHO is best treated as a utility/gas asset rather than a liquid trading vehicle.

---

## Peer Comparison — Dual-Token Gas Models

| Pair | Value asset | Gas asset | Mechanism | Note |
|---|---|---|---|---|
| **[[vechain|VeChain]]** | VET | **VTHO** | Holding VET mints VTHO; VTHO partly burned as gas | Enterprise/supply-chain L1 |
| NEO | NEO | GAS | Holding NEO mints GAS for fees | The original model VeChain echoes |
| Ontology | ONT | ONG | Holding ONT mints ONG | NEO-derived dual-token design |
| (contrast) [[ethereum]] | ETH | ETH | Single token pays gas (burned via EIP-1559) | Costs rise with ETH price |

The dual-token design's selling point is **predictable enterprise transaction costs**: a business pays fees in cheap, separately-supplied VTHO rather than in the appreciating base asset (VET), unlike single-token chains where gas cost tracks the L1 token price.

---

## Valuation Framing (qualitative)

VTHO is **not engineered to appreciate** — it is a deliberately abundant, perpetually-minted gas unit whose price is structurally capped by inflation. Its ~$40M cap is therefore better understood as a function of (1) the size of the VTHO float (~100.9B, continuously growing as [[vechain|VET]] holders generate it) and (2) the burn rate from on-chain activity. When VeChain network usage is low, generation outpaces burn and VTHO drifts down; only sustained, high-throughput enterprise adoption would tip the generation/burn balance toward deflation and support price. Investors seeking value accrual from the VeChain ecosystem typically hold **VET** (which captures the staking/value-transfer role) rather than VTHO. Treat VTHO as an infrastructure/utility holding, not a growth bet. Qualitative framing only — not a price target.

---

## Use Case, Narrative & Category

VTHO's narrative is inseparable from [[vechain]]'s **enterprise blockchain / supply-chain** positioning. VeChain has historically promoted partnerships across automotive and logistics (e.g., BMW, Groupe Renault, DNV GL) and a focus on real-world traceability and sustainability use cases; VTHO is the fuel that powers those on-chain operations. Aggregator categories: Layer 1 (L1), VeChain Ecosystem. As a gas token, VTHO is more of an infrastructure/utility holding than a standalone narrative play.

---

## Notable History

- **2018-08-29:** all-time high of $0.04671227, set during VeChain's mainnet-launch era and the token swap from its earlier ERC-20 form on [[ethereum]] to the native VeChainThor chain.
- **2020-03-16:** all-time low of $0.00015238 during the COVID crash.
- **2026-06-21:** trading at $0.00039276 (#531) — ~-99% from ATH but still ~+158% above ATL, reflecting its role as a perpetually-emitted gas asset whose price is structurally suppressed by inflation.

---

## Risks

- **Structural inflation:** VTHO is continuously minted by VET holders; unless on-chain activity (and burn) is high, generation outpaces usage and keeps downward pressure on price.
- **Utility, not appreciation:** by design VTHO is meant to be a cheap, abundant gas unit — it is not engineered as a value-accrual asset, limiting upside versus VET.
- **Dependence on VeChain adoption:** demand for VTHO is a derivative of [[vechain]] network usage; enterprise adoption has been slower and more uneven than early partnerships implied.
- **Liquidity:** the lowest turnover in this group raises execution/slippage risk.
- **Macro/beta:** high sensitivity to a bear market currently at extreme fear ([[crypto-fear-and-greed-index|Fear & Greed]] = 23).

---

## Trading Profile

### Venues & liquidity

VTHO is tradable on [[binance]] — **spot** (VTHO/USDT) plus a **USD-margined perpetual** with funding, open interest, and liquidations. It is **NOT listed on Hyperliquid**, so Binance is effectively the **primary leveraged venue** for VTHO. This makes Binance's perp the single reference point for funding, OI, and liquidation flow — there is no deep alternative order book to arbitrate against or to fall back on. Combined with VTHO's very thin spot turnover (~1-2% of cap per day), this venue concentration means leverage should be sized small: perp liquidity is shallow, funding can whip on modest positioning, and a single venue outage or thin book can amplify slippage. Execution favors patient limit orders, staged entries, and modest notional rather than aggressive market sizing.

### Applicable strategies

- [[funding-rate-harvest]] — collect perp funding on VTHO's Binance USD-M contract when the rate is persistently one-sided; low market cap tokens often carry richer, stickier funding.
- [[crowded-long-funding-fade]] — fade over-leveraged longs when VTHO funding spikes positive into a low-liquidity rally that lacks spot support.
- [[cash-and-carry]] — hedge long VTHO spot against the Binance perp to capture basis/funding while neutralizing directional exposure to a structurally inflationary gas token.
- [[liquidation-cascade-fade]] — thin perp depth makes VTHO prone to sharp liquidation wicks; fade the overshoot once forced selling exhausts.
- [[oi-confirmed-trend]] — use Binance open-interest changes to confirm whether a VTHO move is real positioning or a hollow, liquidity-driven spike.
- [[range-mean-reversion]] — VTHO's inflation-capped price tends to drift and range; mean-revert extremes within its low-volatility band.

### Volatility & regime character

VTHO is a **small-cap infrastructure/gas token** (rank ~530s) with high beta to BTC/ETH and to the broader [[vechain]] ecosystem. Its price is **structurally suppressed by perpetual emission** (VET holders continuously mint VTHO, no max supply), so it lacks the reflexive upside of a memecoin and instead tends to grind and range in quiet markets, with occasional liquidity-driven wicks. It is a derivative bet on VeChain network usage rather than a standalone narrative asset, and it typically underperforms its value-asset counterpart VET on the way up.

### Risk flags

- **Liquidity/venue concentration:** thinnest turnover in its peer group and a single leveraged venue (Binance); no Hyperliquid fallback raises slippage and gap risk.
- **Structural inflation/emissions:** uncapped, continuously minted supply exerts persistent downward pressure — a "unlock-like" dilution that is ongoing rather than scheduled.
- **Narrative dependence:** demand is derivative of [[vechain]] enterprise adoption, which has been slow and uneven; VTHO has no independent catalyst.
- **Macro/beta:** high sensitivity to broad crypto risk sentiment amplifies drawdowns in fear regimes.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=VTHOUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=VTHOUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=VTHO` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=VTHO` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=VTHOUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=VTHOUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=VTHO"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[vechain]]
- [[ethereum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-21 (cryptodataapi.com / CoinGecko top-markets dataset).

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | VTHO |
| **Market Cap Rank** | #537 |
| **Market Cap** | $37.64M |
| **Current Price** | $0.00037074 |
| **Categories** | Layer 1 (L1) |
| **Website** | [https://www.vechain.org/](https://www.vechain.org/) |

---

## Overview

VeChain is also a dual token system consisting of VeChain Token (VET) and VeThor Token (THOR). Network users are rewarded with the latter when they hold the former, which is also the case with NEO &amp; GAS. The VeChain Token can be used to deploy applications on the platform where as VeThor can be used to pay for applications and other transactions over the network. VeChain claims that this economic model is better suited for enterprises than the one in other blockchains, such as Ethereum and Bitcoin, where higher usage drives the cost of the utility token and subsequently the cost of deploying and operations in the protocol.

In an official blog post earlier this year, the foundation announced it’s “grand aspirations to make financial services sector one of the main focuses on our development plan”. They also announced their partnership with a property mortgage loan provider Fanghuwang.com, a subsidiary of Beijing Baisheng Technology Co., Ltd. They also reported partnerships with BMW, Groupe Renault, and DNV GL.
Until now, VeChain has existed in the form of an ERC-20 token on the Ethereum blockchain. In an announcement detailing the roadmap moving forward, the foundation stated that they would engage in negotiations with exchanges to perform the token swap to become an independent network. The roadmap also detailed plans to launch a mobile wallet and ledger integration.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 101.51B VTHO |
| **Total Supply** | 101.51B VTHO |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $37.64M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.0467 (2018-08-29) |
| **Current vs ATH** | -99.21% |
| **All-Time Low** | $0.00015238 (2020-03-16) |
| **Current vs ATL** | +143.67% |
| **24h Change** | -0.57% |
| **7d Change** | +2.54% |
| **30d Change** | -10.48% |
| **1y Change** | -82.67% |

---

## Platform & Chain Information

**Native Chain:** Vechain

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | VTHO/USDT | N/A |
| Kraken | VTHO/USD | N/A |
| Upbit | VTHO/KRW | N/A |
| Bitget | VTHO/USDT | N/A |
| KuCoin | VTHO/USDT | N/A |
| Crypto.com Exchange | VTHO/USD | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.vechain.org/](https://www.vechain.org/) |
| **Twitter** | [@vechainofficial](https://twitter.com/vechainofficial) |
| **Reddit** | [https://www.reddit.com/r/Vechain/](https://www.reddit.com/r/Vechain/) |
| **Telegram** | [vechain_official_english](https://t.me/vechain_official_english) (11,465 members) |
| **GitHub** | [https://github.com/vechain/thor](https://github.com/vechain/thor) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 812 |
| **GitHub Forks** | 274 |
| **Commits (4 weeks)** | 14 |
| **Pull Requests Merged** | 1,162 |
| **Contributors** | 39 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $608,366.00 |
| **Market Cap Rank** | #537 |
| **24h Range** | $0.00037095 — $0.00037792 |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---
