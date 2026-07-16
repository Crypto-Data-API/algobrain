---
title: "Bounce"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [altcoins, crypto, defi, perpetual-futures, funding-rate, open-interest, liquidations, derivatives]
aliases: ["AUCTION", "Bounce Finance", "BounceBit"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://bounce.finance/"
related: ["[[crypto-markets]]", "[[decentralized-finance]]", "[[ethereum]]", "[[governance-token]]", "[[launchpad]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[cash-and-carry]]", "[[funding-rate-harvest]]"]
---

# Bounce

**Bounce** (AUCTION) is a decentralized [[launchpad]] and auction protocol that lets projects and individuals run permissionless token sales and asset auctions on-chain. Its core product is a configurable auction engine — fixed-price, sealed-bid, Dutch, and English formats — used for token launches, NFT drops, and other digital-asset sales. **AUCTION** is the protocol's [[governance-token]] and staking asset. As of 2026-06-21 AUCTION trades at **$3.73**, ranking **#677** by market capitalization (~**$27.7M**).

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

AUCTION was roughly flat over 24 hours (**-0.29%**) and down **-1.11%** over the trailing week, holding up relatively well against a fearful market (BTC ~$64,180; Fear & Greed Index 22 / Extreme Fear).

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | AUCTION |
| **Market Cap Rank** | #677 |
| **Market Cap** | $27,719,036 |
| **Current Price** | $3.73 |
| **24h Change** | -0.29% |
| **7d Change** | -1.11% |
| **Categories** | Decentralized Finance (DeFi), Launchpad, Ethereum Ecosystem |
| **Notable Backers** | DWF Labs, Coinbase Ventures, Pantera Capital, Blockchain Capital |
| **Website** | [https://bounce.finance/](https://bounce.finance/) |
> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

---

## Overview

Bounce launched in 2020 as a decentralized auction protocol, branding itself an "auction protocol for everything." It provides a toolkit of auction primitives that anyone can deploy:

- **Fixed-swap / fixed-price pools** — sell a token at a set price until supply runs out.
- **Dutch auctions** — price starts high and declines until buyers clear it.
- **Sealed-bid auctions** — bids hidden until settlement, reducing front-running.
- **English auctions** — ascending open bids, common for NFTs.

This makes Bounce a general-purpose [[launchpad]] for token generation events (TGEs), NFT mints, and OTC-style sales, operating across [[ethereum|Ethereum]] and multiple EVM chains. The protocol charges fees on auctions, and **AUCTION** is used for [[governance-token|governance]], staking, and fee/access benefits within the ecosystem. AUCTION has a hard-capped maximum supply of 10 million tokens, making it one of the lower-supply [[decentralized-finance|DeFi]] governance tokens.

---

## Architecture — How the Auction Engine Works

Bounce is fundamentally a set of **on-chain auction smart contracts** plus a front-end that lets non-technical creators configure and launch a sale without writing code. The mechanism design is the product:

**1. Auction format primitives.** Each format encodes a different price-discovery rule on-chain:

- **Fixed-swap pool** — the creator deposits a token and sets a fixed price and total amount; buyers fill at that price until supply is exhausted (first-come-first-served). Simple, predictable, but prone to gas wars and bot front-running on hot launches.
- **Dutch auction** — price starts high and decays over time (or per block) until buyers clear the remaining supply. This surfaces a market-clearing price and discourages bots from sniping the open, at the cost of complexity.
- **Sealed-bid auction** — bids are committed hidden and revealed only at settlement, mitigating front-running and last-second sniping; allocation follows the chosen clearing rule.
- **English auction** — ascending open bids with a settlement to the highest bidder; the natural format for one-of-a-kind NFTs.

**2. Permissionless deployment.** Anyone can spin up an auction pool from the dApp; the contracts hold the deposited tokens in escrow and release them to winners / refund losers programmatically at settlement. Because settlement is enforced by smart contract, the creator cannot run off with bidder funds mid-sale.

**3. Fee capture.** The protocol takes a fee on auctions (typically a percentage of proceeds), which is the revenue line backing AUCTION. The protocol is **chain-agnostic / multi-EVM**, so the same primitives deploy across [[ethereum]] and other EVM chains where launch demand exists.

**4. Anti-bot / fairness tooling.** Sealed-bid and Dutch formats exist precisely to blunt the [[mev|MEV]] / front-running problem that plagues fixed-price launches, a recurring pain point for fair token distribution.

---

## Tokenomics & Value Accrual

**AUCTION** is the protocol's [[governance-token]] and staking asset with a hard cap of **10 million** tokens — unusually scarce for a DeFi governance token. Value-accrual levers:

- **Governance** — holders vote on protocol parameters, fee levels, and treasury use.
- **Staking** — staking AUCTION is used for access/benefits and to align long-term holders.
- **Fee/access benefits** — the token gates or discounts participation and premium features within the ecosystem.

With circulating supply ~7.34M of a 10M cap, the **MC/FDV ratio is ~0.96** — almost fully diluted, so there is little hidden unlock overhang relative to most DeFi tokens. The flip side is that the fundamental backing is **launch-fee throughput**, which is highly cyclical (see Risks).

---

## Comparison vs Competitors

Launchpads are a competitive, reputation-sensitive corner of [[decentralized-finance|DeFi]]. Bounce competes with dedicated IDO/launch platforms and exchange-native sale desks.

| Platform | Model | Sale formats | Token | Differentiator |
|---|---|---|---|---|
| **Bounce** (AUCTION) | Permissionless multi-format auction engine | Fixed-swap, Dutch, sealed-bid, English | AUCTION (10M cap) | Breadth of auction formats; chain-agnostic; tight supply |
| **DAO Maker** (DAO) | Curated IDO / SHO launchpad | Tiered/curated allocations | DAO | Vetting + refundable "SHO" mechanic |
| **Polkastarter** (POLS) | Curated cross-chain IDO | Fixed/Dutch pools | POLS | Cross-chain curated launches |
| **CoinList** | Centralized vetted token sale platform | Fixed-price / lottery | — | Compliance-heavy, off-chain KYC sales |

Bounce's edge is **breadth of auction formats and permissionless, chain-agnostic deployment**; its constraint is that launchpad demand is intensely cyclical — booming when new tokens launch constantly, drying up in bear markets, exactly the current regime.

---

## How & Where It Trades

AUCTION is an Ethereum ERC-20 (`0xa9b1...9096`) and, unlike the thinner names in this cohort, has **real centralized-exchange liquidity** — listed on Binance, Kraken, Upbit, Bitget, and KuCoin per the snapshot (~$4.73M 24h volume). Practical notes:

- **CEX-driven price discovery** — most volume is on centralized order books (Binance AUCTION/USDT, Upbit AUCTION/KRW), so liquidity is materially better than for pure-DEX microcaps.
- **Korean (Upbit) listing** adds a retail-driven, sometimes volatile, demand pocket.
- **Derivatives** — perpetual futures on AUCTION exist on some venues during active periods; treat leverage with caution on a $28M-cap token.

---

## Narrative, Category & Catalysts

AUCTION trades on the **launchpad / new-issuance** narrative: its demand is a leveraged bet on the pace of new token launches. Catalysts include a revival of the IDO/TGE cycle, new auction-format or chain rollouts, and any pivot/expansion within the broader Bounce / BounceBit family. The current **Established Bear Market** (Fear & Greed 21, Extreme Fear; 2026-06-22) is the worst backdrop for the category — primary issuance slows sharply when risk appetite collapses.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 7.34M AUCTION |
| **Total Supply** | 7.64M AUCTION |
| **Max Supply** | 10.00M AUCTION |
| **Fully Diluted Valuation** | $35.51M |
| **Market Cap / FDV Ratio** | 0.96 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $70.44 (2021-04-12) |
| **Current vs ATH** | -93.40% |
| **All-Time Low** | $3.16 (2025-10-10) |
| **Current vs ATL** | +47.25% |
| **24h Change** | -2.30% |
| **7d Change** | +0.74% |
| **30d Change** | -0.78% |
| **1y Change** | -61.05% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xa9b1eb5908cfc3cdf91f9b8b3a74108598009096` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | AUCTION/USDT | N/A |
| Kraken | AUCTION/USD | N/A |
| Upbit | AUCTION/KRW | N/A |
| Bitget | AUCTION/USDT | N/A |
| KuCoin | AUCTION/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://bounce.finance/](https://bounce.finance/) |
| **Twitter** | [@bounce_finance](https://twitter.com/bounce_finance) |
| **Telegram** | [bounce_finance](https://t.me/bounce_finance) (8,214 members) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $4.73M |
| **Market Cap Rank** | #672 |
| **24h Range** | $4.64 — $4.78 |
| **Last Updated** | 2026-04-09 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## History / Timeline

- **2020** — Bounce launches as a decentralized auction protocol ("auction protocol for everything").
- **All-time high $70.44** on **2021-04-12** (CoinGecko price history), at the height of DeFi/NFT launchpad mania.
- The Bounce ecosystem later expanded into adjacent products and branding (including CeDeFi/restaking initiatives associated with the broader **BounceBit** family), reflecting a pivot from a pure auction tool toward a wider DeFi suite.
- **All-time low $3.16** on **2025-10-10**; AUCTION now sits ~93% below its 2021 ATH.

> *Notable additional events will be added through the wiki's source ingestion workflow as relevant articles are processed. Dates above are from CoinGecko price history; undocumented milestone dates are intentionally omitted rather than invented.*

A capped 10M supply and a roster of credible backers (DWF Labs, Coinbase Ventures, Pantera, Blockchain Capital) give AUCTION relatively tight tokenomics for the category.

---

## Risks

- **Cyclicality** — Launchpad revenue tracks the pace of new token launches, which collapses in risk-off markets like the current Extreme Fear regime; this is the dominant risk.
- **Reputation risk** — Launchpads are judged by the quality of projects they host; failed or fraudulent launches damage the platform's standing.
- **Competitive saturation** — Many launchpad and IDO platforms (DAO Maker, Polkastarter, CoinList, exchange Launchpads) compete for the same project pipeline.
- **Smart-contract risk** — Auction and pool contracts hold escrowed funds and are attack surfaces; exploits can cause direct loss.
- **Microcap volatility** — At ~$27.7M market cap, AUCTION is a small-cap token subject to sharp drawdowns despite better-than-peer liquidity.

This is not investment advice; figures above are point-in-time market data, not a valuation.

---

## Trading Playbook (bear / Extreme-Fear regime)

- **Regime:** Established Bear Market, Extreme Fear (F&G 21, 2026-06-22). AUCTION is a *high-beta bet on issuance demand*, which is precisely what dies in risk-off conditions — fundamentally a defensive-stance asset class right now.
- **Liquidity advantage:** unlike thin DEX-only peers, AUCTION has real CEX depth (Binance/Upbit/Kraken), so execution is cleaner — but that does not protect against directional drawdown.
- **Bull-case trigger:** a measurable revival in primary issuance / IDO activity is the fundamental signal to watch; the token tends to lead when the new-launch cycle reawakens.
- **Risk control:** size for microcap volatility, avoid leverage on a ~$28M-cap name, and pre-define invalidation given how violently launchpad tokens reprice.

> *Not investment advice.*

---

## Trading Profile

### Venues & liquidity

AUCTION is tradable on [[binance]] — both spot (AUCTION/USDT) and a USD-margined [[perpetual-futures|perpetual]], which exposes [[funding-rate|funding]], [[open-interest]], and [[liquidations]] data. It is **NOT** listed on Hyperliquid, so Binance is the primary leveraged venue for the name. Because leverage, borrow, and perp liquidity are concentrated on a single dominant venue, execution and sizing must account for shallow order-book depth relative to majors: at a sub-$30M cap, even modest perp size can move price and skew funding, so scale in, prefer limit orders, and keep leverage low. The Binance spot/perp pairing does, however, make cash-and-carry and funding capture structurally feasible here, unlike pure-DEX microcaps.

### Applicable strategies

- [[funding-rate-harvest]] — a Binance USD-M perp means funding can run persistently rich or negative on a thin-cap launchpad token; harvest the recurring payment while hedging spot.
- [[cash-and-carry]] — with both Binance spot and perp available, long spot / short perp captures basis and funding on an otherwise low-yield DeFi microcap.
- [[crowded-long-funding-fade]] — issuance-narrative spikes draw retail perp longs; fade over-crowded positioning when funding turns extreme.
- [[liquidation-cascade-fade]] — a small-cap perp with concentrated OI is prone to violent liquidation flushes; fade the over-extension after forced selling exhausts.
- [[breakout-and-retest]] — AUCTION reprices sharply on IDO-cycle revival; trade confirmed breakouts of range boundaries with a retest entry to avoid launchpad-token fakeouts.
- [[volatility-targeting]] — microcap beta means realized vol swings wildly; size positions to a vol target rather than fixed notional.

### Volatility & regime character

Small-cap DeFi / [[launchpad]] governance token with high beta to broad crypto risk appetite and strong correlation to BTC/ETH direction. Its demand is a leveraged bet on primary-issuance activity, so it behaves reflexively — leading on the upside when the new-launch cycle reawakens and de-rating hard in risk-off regimes. Expect sharp, low-liquidity repricings rather than smooth trends; realized volatility clusters around narrative catalysts.

### Risk flags

- **Venue concentration** — leverage and perp liquidity are concentrated on Binance; no Hyperliquid fallback, so a venue outage or delisting materially impairs the derivatives thesis.
- **Liquidity / microcap risk** — ~$28M cap means thin depth, wide effective spreads under stress, and slippage on size despite CEX listing.
- **Narrative dependence** — value is tied to the cyclical launchpad/IDO issuance cycle, which collapses in bear regimes.
- **Supply** — near-fully-diluted (MC/FDV ~0.96) limits unlock overhang, but capped 10M supply concentrates float and amplifies volatility.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=AUCTIONUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=AUCTIONUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=AUCTION` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=AUCTION` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=AUCTIONUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=AUCTIONUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=AUCTION"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[launchpad]]
- [[decentralized-finance]]
- [[governance-token]]
- [[mev]]
- [[risk-management]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).
- General market knowledge; no additional specific wiki source ingested yet.

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---
