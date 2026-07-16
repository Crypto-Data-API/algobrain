---
title: "Astar"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, altcoins]
aliases: ["ASTR", "Astar Network"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://astar.network/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[layer-1]]", "[[layer-2]]", "[[polkadot]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[funding-rate-harvest]]", "[[cash-and-carry]]"]
---

# Astar

**Astar** (ticker **ASTR**) is a multi-chain smart-contract platform originally launched as **Plasm Network** and best known as a leading [[polkadot]] parachain. It supports both EVM and WebAssembly (WASM) smart contracts, and has expanded into an Ethereum-aligned presence via **Astar zkEVM** (a [[layer-2]] built on Polygon's CDK). ASTR is the ecosystem's economic and governance token, and Astar is notable for its **dApp Staking** model, which directs a share of inflation to developers whose applications attract staked tokens — an attempt to align token emissions with real on-chain usage.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | ASTR |
| **Market Cap Rank** | #475 |
| **Market Cap** | $47.34M |
| **Current Price** | $0.005428 |
| **24h Change** | -3.72% |
| **7d Change** | -5.48% |
| **24h Volume** | $5.62M |
| **All-Time High** | $0.4216 (January 2022) |
| **All-Time Low** | $0.005184 |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

The macro backdrop is risk-off: the crypto [[fear-and-greed-index|Fear & Greed Index]] reads **23 (extreme fear)** and the long-horizon regime is an **Established Bear Market** as of 2026-06-21. ASTR remains among the weakest performers in this peer group, down -3.72% on the day and -5.48% over the week. It trades only ~5% above its all-time low (~$0.0052) and about 99% below its January-2022 all-time high of $0.422.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~8.71B ASTR |
| **Total Supply** | ~8.71B ASTR |
| **Max Supply** | 10.00B ASTR |
| **Fully Diluted Valuation (FDV on max supply)** | ~$54.28M |
| **Market Cap / FDV (max)** | ~0.87 |
| **Market Cap / Total Supply** | ~1.00 |

Circulating supply is essentially equal to *total* supply, so there is minimal locked-token overhang from team/investor cliffs — but the **10B max supply** sits ~15% above current circulation, and ASTR is **inflationary**, with new tokens minted to fund block production and the dApp Staking program. On a max-supply basis MC/FDV ≈ 0.87; the gap to total supply is closed, so future dilution is emission-driven (a flow) rather than a discrete unlock event. The token's signature mechanism is **dApp Staking**: holders stake ASTR toward specific dApps, and a portion of network inflation is distributed to those projects, aligning emissions with applications that draw usage. ASTR also serves as gas (on Astar's Substrate/EVM environments) and governance.

---

## How & Where It Trades

**Spot venues.** ASTR is listed on [[binance]] (ASTR/USDT), [[kraken]] (ASTR/USD), Upbit (ASTR/KRW), Bitget, KuCoin, and Crypto.com. It carries an [[ethereum]] contract (`0xf274...9689`) reflecting its multi-chain footprint.

**Derivatives.** ASTR perpetuals are available on major centralized derivatives venues. The wiki's prior snapshot did **not** record an ASTR perp on [[hyperliquid]], so do not assume one exists — verify the live venue list before trading derivatives. With a ~$46M market cap and ~$3.6M daily volume, derivatives and spot liquidity are thin; funding/OI should be checked live before any leveraged position.

---

## Technology & Consensus

Astar is built on **Substrate** (the [[polkadot]] SDK) and historically secured by leasing a Polkadot parachain slot, inheriting shared security from the Polkadot relay chain via [[polkadot|nominated proof-of-stake]]. Key technical traits:

- **Dual VM support** — runs both EVM (Solidity) and WASM (ink!) smart contracts, letting developers from the Ethereum and Polkadot/Substrate worlds deploy on one chain.
- **Cross-consensus / interoperability** — uses Polkadot's XCM messaging to communicate with other parachains, and Astar zkEVM extends reach into the [[ethereum]] [[layer-2]] landscape (Polygon CDK).
- **dApp Staking** — a protocol-level incentive that routes inflation to developers, distinct from generic validator-only staking.

Astar's positioning straddles two ecosystems (Polkadot and Ethereum), which is both its differentiator and a source of strategic complexity.

---

## Use Case, Narrative & Category

Astar sits in the **multi-chain smart-contract platform** category, simultaneously tagged as a Polkadot Ecosystem chain, a Layer 1 (L1), and an Ethereum-ecosystem Layer 2 (L2) (via Astar zkEVM). Its narrative centers on being a developer-and-business onboarding hub — notably strong brand presence in Japan and Asia, with enterprise and Web3-entertainment partnerships — and on aligning token emissions with real dApp usage. Tagged categories include Smart Contract Platform, Polkadot Ecosystem, Layer 1 (L1), Ethereum Ecosystem, Layer 2 (L2), plus VC-portfolio tags (OKX Ventures, Binance Labs/YZi).

---

## Valuation Framing (qualitative)

ASTR is the smallest cap in this peer group (~$47M, rank #475) and trades within ~5% of its all-time low after a ~99% drawdown from its 2022 peak. The differentiated asset is **dApp Staking** — routing inflation to developers whose apps attract stake — and a genuine dual-VM (EVM + WASM) build with strong Japan/Asia and enterprise brand presence. The bear case is that ASTR's fortunes are tethered to two ecosystems whose narratives have both faded: [[polkadot]] parachain economics have seen reduced demand, and the Ethereum-side Astar zkEVM competes in a crowded zkEVM field. Persistent emissions plus a strategic straddle across two stacks make the value case usage-dependent in a way the chart does not yet reflect. Among the deepest-drawdown, lowest-momentum names here. Not investment advice.

---

## Peer Comparison

| Project | Ticker | Category | MC Rank | Market Cap | MC/FDV | Anchor ecosystem |
|---|---|---|---|---|---|---|
| **Astar** | ASTR | Multi-chain L1/L2 | #475 | $47.34M | ~0.87 | [[polkadot]] + [[ethereum]] |
| [[mina-protocol]] | MINA | Succinct zk [[layer-1]] | #427 | $54.22M | ~1.00 | Standalone |
| [[zetachain]] | ZETA | Omnichain L1 | #426 | $54.23M | ~0.70 | Cross-chain |
| [[linea]] | LINEA | zkEVM [[layer-2]] | #391 | $61.63M | ~0.34 | [[ethereum]] |

*Astar is the only name here straddling two base ecosystems (Polkadot Substrate + Ethereum zkEVM via Polygon CDK), which is both its reach and its strategic-focus risk.*

---

## Notable History

- Launched as **Plasm Network** in 2019–2020, later rebranded to Astar; its legacy Telegram is still "PlasmOfficial."
- ASTR printed its all-time high of **$0.422 in January 2022** during the prior bull cycle.
- It has since declined ~99%, with an all-time low near $0.0052 around February 2026.
- As of 2026-06-21 it trades at ~$0.0054, just above the low, and remains one of the worst 24h/7d performers in this peer set — consistent with weak Polkadot-ecosystem sentiment in the current bear regime.

---

## Risks

- **Inflationary dilution.** Ongoing emissions to fund dApp Staking dilute non-stakers; sustained price requires usage that justifies the inflation.
- **Polkadot-ecosystem dependence.** Astar's fortunes are tied to Polkadot's parachain economics and relay-chain security model, which have faced reduced demand and attention.
- **Strategic straddle.** Splitting effort across Polkadot (Substrate) and Ethereum ([[layer-2]] zkEVM) risks diluting focus and liquidity.
- **Competition.** Crowded smart-contract-platform field on both sides of its straddle.
- **Severe drawdown / liquidity.** Down ~99% from ATH, near all-time lows, with thin (~$3.6M/day) volume and an extreme-fear macro backdrop.

---

## Trading Profile

### Venues & liquidity

ASTR is tradable on [[binance]] — both spot (ASTR/USDT) and a USD-margined [[perpetual-futures|perpetual]] contract, which is where [[funding-rate|funding]], [[open-interest]], and [[liquidations]] data live. It is **NOT** listed on [[hyperliquid]], so Binance is the primary (effectively sole major) leveraged venue. With market cap around rank #459 and thin daily volume, the perp order book is shallow: leverage is available but liquidity concentration on a single venue means slippage on size, wider effective spreads, and funding/OI that can whip on modest flow. Venue concentration argues for small clip sizes, limit-order execution over market fills, and treating Binance funding/OI as the definitive read since there is no deep secondary perp market to cross-check or hedge against.

### Applicable strategies

- [[funding-rate-harvest]] — collect Binance perp funding when the single-venue ASTR perp trades at a persistent premium/discount to spot; the only major venue makes the funding print clean but one-sided.
- [[crowded-long-funding-fade]] — small-cap ASTR pumps on Polkadot/Japan narrative headlines often over-lever longs; fade when funding spikes richly positive into a stalled price.
- [[cash-and-carry]] — long Binance spot ASTR versus short the USD-M perp to lock the basis when funding is durably positive, avoiding directional exposure on a deeply drawn-down token.
- [[liquidation-cascade-fade]] — thin ASTR order books make leveraged flushes overshoot; fade forced-liquidation wicks back toward the mean once the cascade exhausts.
- [[rsi-mean-reversion]] — ASTR trades within ~5-10% of its all-time low in a bear regime, where oversold bounces off compressed ranges are frequent and tradable.
- [[oi-price-exhaustion]] — rising Binance open interest against a failing price on a low-float, single-venue perp flags exhausted positioning ripe for a reversal.

### Volatility & regime character

ASTR is a **small-cap infra/L1-L2 token** (rank ~#459) exhibiting high beta to broad crypto risk sentiment and strong correlation to BTC/ETH drawdowns, amplified by its Polkadot-ecosystem and Japan/Asia narrative dependence. It is not a memecoin, but its low float and thin liquidity produce memecoin-like reflexivity on headlines and liquidation events. In the current Established Bear Market it prints low-momentum, mean-reverting behavior near its all-time low, with sharp but short-lived narrative-driven spikes rather than sustained trends.

### Risk flags

- **Liquidity / venue concentration** — leveraged trading effectively lives on one venue (Binance); no Hyperliquid perp and thin spot depth mean fills, exits, and hedges are all constrained.
- **Emissions / inflation** — ASTR is inflationary via dApp Staking; ongoing emission (a flow) dilutes holders even without discrete unlock cliffs.
- **Narrative dependence** — price is tethered to Polkadot parachain economics and Astar zkEVM sentiment, both of which have faded; moves are headline-driven and reflexive.
- **Deep drawdown** — down ~99% from its 2022 ATH and near all-time lows, so ranges are compressed and momentum is weak, punishing trend-following while favoring mean reversion.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=ASTRUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=ASTRUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=ASTR` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=ASTR` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=ASTRUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=ASTRUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=ASTR"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[polkadot]]
- [[ethereum]]
- [[layer-1]]
- [[layer-2]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-21 (cryptodataapi.com / CoinGecko bulk endpoint), `raw/data/crypto-loop/coingecko-markets.json`.

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | ASTR |
| **Market Cap Rank** | #459 |
| **Market Cap** | $45.49M |
| **Current Price** | $0.00521218 |
| **Categories** | Smart Contract Platform, Layer 1 (L1), Layer 2 (L2) |
| **Website** | [https://astar.network/](https://astar.network/) |

---

## Overview

Astar is a web3 collective building products that bring users onchain and generate long term value for ASTR. It operates as a multi chain ecosystem that coordinates products and contributors through a shared economic and governance framework. 

At the center is Astar Network, which provides the foundation for governance, security, and economic alignment across the ecosystem. Astar supports a growing set of products and integrations designed to drive real onchain usage and sustainable economic activity. Product development is guided by the Astar Stack, a unified product stack that turns blockchain infrastructure and finance into secure and user friendly applications aligned with Astar’s economic goals. 

ASTR acts as the ecosystem’s economic and governance token, aligning network activity, product growth, and long term value creation.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 8.73B ASTR |
| **Total Supply** | 8.73B ASTR |
| **Max Supply** | 10.00B ASTR |
| **Fully Diluted Valuation** | $45.50M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.4216 (2022-01-17) |
| **Current vs ATH** | -98.77% |
| **All-Time Low** | $0.00472940 (2026-07-01) |
| **Current vs ATL** | +9.90% |
| **24h Change** | +1.85% |
| **7d Change** | +3.98% |
| **30d Change** | -13.11% |
| **1y Change** | -79.62% |

---

## Platform & Chain Information

**Native Chain:** Multiple chains (see contract addresses below)

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xf27441230eadeac85b764610325cc9a0d7859689` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | ASTR/USDT | N/A |
| Kraken | ASTR/USD | N/A |
| Upbit | ASTR/KRW | N/A |
| Bitget | ASTR/USDT | N/A |
| KuCoin | ASTR/USDT | N/A |
| Crypto.com Exchange | ASTR/USD | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://astar.network/](https://astar.network/) |
| **Twitter** | [@AstarNetwork](https://twitter.com/AstarNetwork) |
| **Telegram** | [PlasmOfficial](https://t.me/PlasmOfficial) (13,895 members) |
| **Discord** | [https://discord.gg/astarnetwork](https://discord.gg/astarnetwork) |
| **GitHub** | [https://github.com/AstarNetwork/Astar](https://github.com/AstarNetwork/Astar) |
| **Whitepaper** | [https://github.com/AstarNetwork/plasmdocs/blob/master/wp/en.pdf](https://github.com/AstarNetwork/plasmdocs/blob/master/wp/en.pdf) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 774 |
| **GitHub Forks** | 528 |
| **Commits (4 weeks)** | 4 |
| **Pull Requests Merged** | 1,017 |
| **Contributors** | 45 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $3.18M |
| **Market Cap Rank** | #459 |
| **24h Range** | $0.00509308 — $0.00525583 |
| **CoinGecko Sentiment** | 100% positive |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---
