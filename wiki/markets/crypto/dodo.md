---
title: "DODO"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, ethereum, altcoins]
aliases: ["DODO"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://dodoex.io/"
related: ["[[automated-market-maker]]", "[[binance]]", "[[chainlink]]", "[[crypto-markets]]", "[[decentralized-exchange]]", "[[ethereum]]", "[[governance-token]]", "[[impermanent-loss]]", "[[range-mean-reversion]]", "[[slippage]]", "[[volatility-breakout]]"]
---

# DODO

**DODO** (DODO) is a multi-chain [[decentralized-exchange|decentralized exchange]] (DEX) and liquidity protocol built around the **Proactive Market Maker (PMM)** algorithm — an oracle-aided pricing model designed to deliver lower [[slippage]] and higher capital efficiency than the constant-product [[automated-market-maker|AMM]] curves used by [[uniswap]]-style DEXs. Originally launched on [[ethereum]] and BNB Chain, DODO now operates across many chains and offers spot trading, liquidity pools, single-token and tokenized-asset issuance, and a cross-chain aggregator.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko). Price $0.01620678 · rank #917 · market cap $16,202,810 · 24h +0.68% · 7d +4.77%. Market-wide sentiment: Fear & Greed Index 21 (Extreme Fear).*

As of 2026-06-22, DODO trades at **$0.01620678**, ranked **#917** by market capitalization with a market cap of **$16,202,810**. The token was up modestly over the prior day (**+0.68%** 24h) and stronger over the week (**+4.77%** 7d), notably outperforming a fearful tape (Fear & Greed Index 21, Extreme Fear). DODO remains down more than 99% from its February 2021 all-time high near $8.38.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | DODO |
| **Market Cap Rank** | #917 |
| **Market Cap** | $16,202,810 |
| **Current Price** | $0.01620678 |
| **24h Change** | +0.68% |
| **7d Change** | +4.77% |
| **Core model** | Proactive Market Maker (PMM), oracle-anchored |
| **Categories** | Decentralized Exchange (DEX), Exchange-based Tokens, Decentralized Finance (DeFi), BNB Chain Ecosystem, Binance Launchpool, Polygon Ecosystem, Near Protocol Ecosystem, Arbitrum Ecosystem, Ethereum Ecosystem, DWF Labs Portfolio, Coinbase Ventures Portfolio, Alameda Research Portfolio, DeFiance Capital Portfolio, Pantera Capital Portfolio, Aurora Ecosystem, Energi Ecosystem, YZi Labs (Prev. Binance Labs) Portfolio, Galaxy Digital Portfolio, Made in China |
| **Website** | [https://dodoex.io/](https://dodoex.io/) |
> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko). Fear & Greed Index 21 (Extreme Fear).*

---

## Overview

DODO is a Decentralized Exchange (DEX) running on Ethereum and Binance Smart Chain.&nbsp;

Developed by the DODO team, Proactive Market Maker (PMM) is an oracle-aided algorithm with an advanced pricing formula that provides contract-fillable liquidity. Traders get lower slippage with PMM than Automated Market Maker (AMM).

PMM leverages price oracles to retrieve accurate market prices of assets as input. It then aims to provide sufficient liquidity near the market price for every asset, so that liquidity decreases rapidly as price moves away from the oracle mid. This concentrates capital where most trading occurs, mimicking the tight order book of a [[centralized-exchange|centralized exchange]] rather than spreading liquidity thinly across an entire price range as a constant-product AMM does.

---

## Mechanism & Architecture

The **Proactive Market Maker (PMM)** is DODO's core innovation. Whereas a constant-product AMM (e.g., [[uniswap]]) sets price purely from pool reserves along a fixed `x*y=k` curve, PMM uses an external [[chainlink|oracle]] price as an anchor and a tunable parameter `k` that flattens the curve near the market price. Effects:

- **Lower [[slippage]]** for trades near the oracle price, improving execution for traders.
- **Higher capital efficiency** for liquidity providers — capital is concentrated around the market price rather than diluted across all prices.
- **Single-token liquidity provision** — because pricing is oracle-anchored, providers can supply just the base or quote asset, reducing the [[impermanent-loss]] profile of paired AMM LPing (though IL is not eliminated, especially during oracle/market divergence).

Beyond PMM pools, DODO offers:

- **Asset issuance / "Crowdpooling" and SmartTrade** — tooling for new tokens to bootstrap fair-launch liquidity.
- **DODO Aggregator (SmartTrade)** — routes orders across DODO pools and external DEXs for best execution.
- **Multi-chain deployment** — Ethereum, BNB Chain, Polygon, Arbitrum, Aurora/NEAR, and others.

### The `k` parameter, intuitively

PMM exposes a curve-flatness parameter `k` in `[0, 1]`:

- `k = 1` reproduces the constant-product `x*y=k` curve of a classic [[automated-market-maker|AMM]] — liquidity spread across all prices.
- `k → 0` flattens the curve into a near-flat line at the oracle price — behaving like a tight [[order-book]] / [[centralized-exchange|CEX]] quote, with almost all depth at the mid.

A stablecoin pool can run a very low `k` (price barely moves, minimal [[slippage]]), while a volatile pair runs a higher `k` for safety. This single knob is what lets DODO mimic either an AMM or an order book from the same math.

### Worked example (illustrative)

Consider a USDC/USDT pool. Under a constant-product AMM, even a swap of a few hundred thousand dollars nudges the price off peg and incurs slippage. Under PMM with a low `k`, the [[chainlink|oracle]] pins the mid near $1.00 and the flat curve quotes nearly the entire pool at the peg, so the same trade clears with only a few basis points of slippage — closer to a CEX fill. Conversely, if the oracle feed were stale or manipulated away from the true market, that same flatness becomes a liability: arbitrageurs (or an attacker) can transact against a mispriced flat curve and drain it. The strength and the vulnerability share one root — oracle dependence.

---

## Comparison vs Competitors

| Protocol | Core model | LP style | Distinctive edge | Primary risk |
|---|---|---|---|---|
| **DODO** | Proactive Market Maker (oracle-anchored, tunable `k`) | Single-token possible | CEX-like depth near mid; asset-issuance tooling + aggregator | Oracle dependence |
| [[uniswap\|Uniswap]] | Constant product (V2) / continuous concentrated (V3) | Paired (V2), ranged NFT (V3) | Deepest liquidity, broadest reach | Capital dilution (V2); IL |
| [[curve-finance\|Curve]] | StableSwap invariant | Paired, correlated | Best stable/pegged swaps | Narrow to correlated assets |
| [[joe\|Trader Joe / LFJ]] | Liquidity Book (discrete-bin concentrated) | Fungible bins | Zero-slippage bins + dynamic fees | Avalanche concentration |
| [[woo-network\|WOOFi]] | sPMM (oracle + live MM quote) | MM-provided | Shared multi-chain "liquidity-as-a-service" | Oracle / MM dependence |
| 1inch / Matcha (aggregators) | Routing across DEXs | n/a | Best-execution routing | Reliant on underlying venue liquidity |

DODO sits at the intersection of the oracle-anchored AMM family (alongside [[woo-network|WOOFi]]) and the aggregator family (SmartTrade), which broadens its surface but pits it against both Uniswap-scale liquidity and dedicated routers.

---

## Token Role (DODO)

DODO is the protocol's [[governance-token]] and incentive asset:

- **Governance (vDODO model)** — holders can lock/stake DODO (historically as **vDODO**) to gain governance weight and a share of protocol fees and rewards.
- **Liquidity incentives** — DODO emissions reward liquidity providers and traders.
- **Fee sharing / value capture** — a portion of protocol trading fees is directed to staked/locked DODO holders.

Supply is fully circulating at ~1B DODO (market-cap/FDV ≈ 1.0), so there is little remaining unlock-driven dilution.

---

## History & Notable Events

- **2020** — DODO launches with the PMM model; backed by prominent investors including Pantera, Coinbase Ventures, Binance Labs, and others.
- **February 2021** — DODO reaches its all-time high (~$8.38) during the DeFi/AMM boom.
- **March 2021** — DODO's V2 Crowdpooling smart contracts suffered an exploit (a fake-token / initialization vulnerability) that drained funds from certain pools; the team and a "white-hat" actor recovered a portion of the losses.
- **2021–2026** — Expansion to a multi-chain aggregator and liquidity stack; continued iteration on PMM (V2/V3) and trading infrastructure amid intense competition in the DEX/aggregator space.
- **2026-02-06** — DODO printed an all-time low near **$0.0130** during the deep bear; it has since recovered modestly, trading ~$0.0162 as of 2026-06-22 amid an Extreme-Fear market (Fear & Greed 21).

---

## Competitive Position

DODO competes in two overlapping arenas: **spot DEXs/AMMs** ([[uniswap]], [[curve-finance|Curve]], [[pancakeswap]], [[balancer]]) and **DEX aggregators** (1inch, Matcha/0x, Jupiter). Its differentiator is the oracle-anchored PMM curve, which can deliver CEX-like low slippage and single-token liquidity. The trade-offs are oracle dependence and the dominance of incumbents like Uniswap, which command most spot volume and liquidity. DODO's aggregator and asset-issuance tooling broaden its product surface but face crowded competition.

---

## Risks

- **Oracle dependence (primary)** — PMM relies on external price feeds; oracle manipulation, latency, or failure can cause mispriced trades or losses.
- **Smart-contract / exploit risk** — DODO has a prior exploit in its history (2021 Crowdpooling vulnerability); novel pricing logic enlarges the attack surface.
- **Competitive pressure** — spot DEX and aggregator markets are dominated by larger players with deeper liquidity.
- **Liquidity / IL risk** — single-token and concentrated liquidity reduce but do not remove impermanent-loss exposure, especially when oracle and market prices diverge.
- **Microcap risk** — at a ~$16M market cap and >99% below its ATH, DODO is small, volatile, and sentiment-driven (CoinGecko sentiment has at times been weak).

This is not investment advice; figures are point-in-time and crypto assets are highly volatile.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 1.00B DODO |
| **Total Supply** | 1.00B DODO |
| **Max Supply** | 1.00B DODO |
| **Fully Diluted Valuation** | $15.26M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $8.38 (2021-02-20) |
| **Current vs ATH** | ~-99.8% |
| **All-Time Low** | $0.0130 (2026-02-06) |
| **24h Change** | +0.68% |
| **7d Change** | +4.77% |
| **30d Change (2026-04-09 snapshot)** | +8.83% |
| **1y Change (2026-04-09 snapshot)** | -66.67% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x43dfc4159d86f3a37a5a4b3d4580b888ad7d4ddd` |
| Near Protocol | `43dfc4159d86f3a37a5a4b3d4580b888ad7d4ddd.factory.bridge.near` |
| Aurora | `0xe301ed8c7630c9678c39e4e45193d1e7dfb914f7` |
| Energi | `0x4fec4e046e6b8de5d22785c3fbdb104f14f5a306` |
| Polygon Pos | `0xe4bf2864ebec7b7fdf6eeca9bacae7cdfdaffe78` |
| Binance Smart Chain | `0x67ee3cb086f8a16f34bee3ca72fad36f7db929e2` |
| Arbitrum One | `0x69eb4fa4a2fbd498c257c57ea8b7655a2559a581` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | DODO/USDT | N/A |
| Bitget | DODO/USDT | N/A |
| KuCoin | DODO/USDT | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V2 (Ethereum) | 0X43DFC4159D86F3A37A5A4B3D4580B888AD7D4DDD/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://dodoex.io/](https://dodoex.io/) |
| **Twitter** | [@BreederDodo](https://twitter.com/BreederDodo) |
| **Reddit** | [https://www.reddit.com/r/DodoEx/](https://www.reddit.com/r/DodoEx/) |
| **Telegram** | [dodoex_official](https://t.me/dodoex_official) (9,725 members) |
| **Discord** | [https://discord.com/invite/tyKReUK](https://discord.com/invite/tyKReUK) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **Current Price** | $0.01620678 |
| **Market Cap** | $16,202,810 |
| **Market Cap Rank** | #917 |
| **24h Change** | +0.68% |
| **7d Change** | +4.77% |
| **24h Range (2026-04-09 snapshot)** | $0.0152 — $0.0160 |
| **CoinGecko Sentiment (2026-04-09 snapshot)** | 0% positive |
| **Last Updated** | 2026-06-22 (price/cap); intraday range/sentiment from 2026-04-09 snapshot |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Trading Profile

### Venues & liquidity

DODO is tradable on **Binance SPOT only** — there is no liquid perpetual venue for the token, so leverage and short access are limited and this is a **spot-primary asset**. Perp funding/basis/liquidation strategies do **not** apply. Because depth is concentrated on a single centralized-exchange spot book (with thin secondary DEX/CEX liquidity), execution should favor limit orders and patient fills; market orders in size will walk the book and incur meaningful slippage. Venue concentration means position sizing must respect real DODOUSDT spot depth rather than notional headline volume, and gap/halt risk on one venue can dominate. Directional exposure is effectively long-biased (no cheap borrow/short), so shorting the name is impractical for most participants.

### Applicable strategies

- [[breakout-trading]] — a >99%-below-ATH microcap that trades in long compression phases, so range breaks from these bases are the cleaner directional signal on the DODOUSDT spot book.
- [[volatility-breakout]] — DODO's low-cap, sentiment-driven tape produces sharp volatility expansions from quiet periods; entering on a volatility surge (rather than fixed levels) fits its reflexive character.
- [[range-mean-reversion]] — between catalysts DODO chops within a band; fading extremes back toward the range mid suits a spot-only asset where you cannot lean on leverage.
- [[rsi-mean-reversion]] — Extreme-Fear, low-liquidity spikes routinely push a microcap like DODO to oversold/overbought RSI readings that revert, a natural spot mean-reversion trigger.
- [[dca-strategy]] — for accumulators who want DODO exposure without timing a thin single-venue book, spreading spot buys smooths entry across its high volatility.
- [[narrative-trading]] — as a DEX/PMM DeFi governance token, DODO tends to move on DeFi/DEX-rotation narratives; aligning entries with an active narrative improves the odds on an otherwise range-bound microcap.

### Volatility & regime character

Small-cap (rank ~729), high-beta **DeFi/DEX infrastructure** token with a fully-circulating ~1B supply. It behaves as a reflexive microcap: quiet, range-bound drift punctuated by sharp sentiment-driven expansions, and it is strongly correlated to BTC/ETH risk appetite (it tends to under-perform in risk-off, Extreme-Fear tapes and over-shoot in DeFi-rotation risk-on phases). Not a memecoin, but its low float and thin liquidity give it memecoin-like reflexivity. Regime is dominated by broad crypto beta plus DeFi-sector narrative rotation.

### Risk flags

- **Liquidity / venue concentration** — depth is concentrated on Binance spot; no liquid perp venue means limited shorting/hedging and elevated slippage/gap risk in size.
- **Microcap volatility** — ~small-cap valuation and >99% below ATH; sentiment-driven swings and low liquidity amplify drawdowns.
- **Narrative dependence** — price action leans on DeFi/DEX-sector rotation and broad-market risk appetite rather than idiosyncratic demand.
- **Protocol/smart-contract history** — DODO has a prior exploit in its history and novel oracle-anchored PMM logic; protocol events can drive token risk.
- **Emissions/incentives** — supply is fully circulating (limited unlock overhang), but ongoing liquidity-incentive emissions can add sell pressure.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] Binance-spot endpoints (auth via `X-API-Key`). No perp/funding endpoints apply — no liquid perp venue.

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=DODOUSDT` — current price
- `GET /api/v1/market-data/ticker/24hr?symbol=DODOUSDT` — 24h ticker stats (volume, range, change)

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=DODOUSDT&interval=1d&limit=1000` — OHLCV klines
- `GET /api/v1/market-data/volume-history?days=90` — daily volume + buy ratio
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=DODOUSDT&interval=1d&limit=1000"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---

## Related

- [[decentralized-exchange]]
- [[automated-market-maker]]
- [[liquidity-pool]]
- [[slippage]]
- [[impermanent-loss]]
- [[defi]]
- [[uniswap]]
- [[curve-finance]]
- [[chainlink]]
- [[governance-token]]
- [[ethereum]]
- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko snapshot). Fear & Greed Index 21 (Extreme Fear).
- General market knowledge; no specific wiki source ingested yet.
