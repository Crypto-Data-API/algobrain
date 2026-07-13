---
title: "Ankr Network"
type: entity
created: 2026-04-09
updated: 2026-06-21
status: excellent
tags: [crypto, depin]
aliases: ["ANKR"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.ankr.com/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[depin]]"]
---

# Ankr Network

**Ankr Network** (ticker **ANKR**) is the token of a Web3 decentralized infrastructure provider that delivers RPC endpoints, node hosting, and liquid-staking services across [[ethereum|Ethereum]] and dozens of other chains. The ANKR token is a multi-chain ERC-20-style asset originally launched on Ethereum, now bridged to BNB Chain, Polygon, Arbitrum, Optimism, Avalanche, Fantom, Linea, Scroll, Base/Blast and other ecosystems. Ankr is one of the older [[depin|DePIN]]-adjacent node-infrastructure names, frequently used by developers who need reliable read/write access to multiple blockchains without running their own nodes.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | ANKR |
| **Current Price** | $0.00370604 |
| **Market Cap** | $37.06M |
| **Market Cap Rank** | #555 |
| **24h Volume** | $6.93M |
| **24h Change** | +0.11% |
| **7d Change** | -4.62% |
| **Fully Diluted Valuation** | $37.06M |
| **All-Time High** | $0.213513 (2021-04-16) |
| **All-Time Low** | $0.00070728 (2020-03-13) |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

Context: the broader market is in an **Established Bear Market** with the [[crypto-fear-and-greed-index|Crypto Fear & Greed Index]] at **≈23 (extreme fear)** as of 2026-06-21. ANKR is roughly flat on the day (+0.1%) and down ~4.6% on the week. Its ~$6.9M of daily turnover against a $37.1M cap means liquidity is thin and slippage-prone for larger orders; the token trades ~98% below its 2021 cycle high of $0.2135.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | 10.00B ANKR |
| **Total Supply** | 10.00B ANKR |
| **Max Supply** | 10.00B ANKR |
| **Market Cap / FDV** | 1.00 |

ANKR has a **fully circulating supply** — circulating equals total equals max at 10B tokens, so market cap and FDV are identical and there is **no future unlock/dilution overhang**. This is a meaningful contrast with the newer AI/DePIN launches (see [[cysic]], [[gensyn]]) whose low circulating-to-total ratios imply heavy forward emissions. The flat supply also means ANKR's price is driven by demand and network usage rather than emission mechanics.

---

## How & Where It Trades

**Centralized spot venues:**

| Exchange | Pair |
|---|---|
| Binance | ANKR/USDT |
| Kraken | ANKR/USD |
| Upbit | ANKR/KRW |
| Bitget | ANKR/USDT |
| KuCoin | ANKR/USDT |
| Crypto.com Exchange | ANKR/USD |

**Decentralized venues:** Uniswap V2/V3 and Sushiswap on Ethereum (ANKR/WETH).

**Derivatives:** ANKR has perpetual-futures listings on major derivatives venues (Binance Futures and others have historically carried ANKR perps), though it is **not** a flagship [[hyperliquid|Hyperliquid]] market and open interest is small relative to large caps. Given the modest spot float, funding and OI are not significant price drivers; treat ANKR primarily as a spot instrument.

### Contract Addresses (selected)

| Chain | Address |
|---|---|
| Ethereum | `0x8290333cef9e6d528dd5618fb97a76f268f3edd4` |
| BNB Chain | `0xf307910a4c7bbc79691fd374889b36d8531b08e3` |
| Polygon PoS | `0x101a023270368c0d50bffb62780f4afd4ea79c35` |
| Arbitrum One | `0xaeaeed23478c3a4b798e4ed40d8b7f41366ae861` |
| Optimism | `0xaeaeed23478c3a4b798e4ed40d8b7f41366ae861` |

---

## Use Case, Narrative & Category

Ankr operates a **decentralized node and RPC infrastructure network** — a [[depin|DePIN]]-style category where independent operators run blockchain nodes and Ankr aggregates them into load-balanced public/private RPC endpoints. Core products:

- **RPC / API services** — multi-chain endpoints for dapps and wallets
- **Node hosting / Validator services** — staking infrastructure and node deployment
- **Liquid staking** — Ankr issues liquid staking tokens; ANKR is the governance token for these systems
- **Rollups-as-a-Service (RaaS)** — appchain/rollup deployment tooling

CoinGecko categorizes ANKR under DePIN, Liquid Staking Governance Tokens, Rollups-as-a-Service, and numerous chain-ecosystem tags. The investment narrative is "picks-and-shovels infrastructure for Web3" — Ankr earns where developers need reliable chain access. It is backed by Pantera Capital and YZi Labs (formerly Binance Labs).

---

## Peer Comparison — Web3 Infrastructure / RPC & Node Tokens

| Project | Token | Niche | Supply structure |
|---|---|---|---|
| **Ankr** | ANKR | Multi-chain RPC, node hosting, liquid staking, RaaS | Fully circulating (10B, cap = FDV); no dilution overhang |
| [[the-graph\|The Graph]] | GRT | Decentralized [[indexing]] / data queries | Fully diluted (cap ≈ FDV); ~3% issuance |
| Pocket Network | POKT | Decentralized RPC relay network | DePIN RPC competitor |
| Alchemy / Infura / QuickNode | (private) | Centralized RPC + dev APIs | Ankr's commercial competition |

Versus centralized RPC giants (Alchemy, Infura), Ankr's pitch is **decentralized, multi-chain, no-vendor-lock-in** access; versus [[the-graph|The Graph]] it sits one layer lower (raw RPC/node access rather than indexed/queryable data). Both share the infra-token problem: heavy product commoditization and weak token fee-capture.

---

## Valuation Framing (qualitative)

- **No dilution, low-cap infra token:** with supply fully circulating (cap = FDV ≈ $37M), ANKR has no unlock overhang — a structural positive versus locked peers like [[spark-2|SPK]] and [[huma-finance|HUMA]]. The flip side is no emission-driven incentive flywheel to bootstrap fresh demand.
- **Commoditized revenue base:** RPC/node access is a low-margin, heavily competed product (Alchemy, Infura, public RPCs), capping the fee-capture story that would justify a re-rate.
- **Narrative beta, not fundamentals:** ANKR re-rates mostly when retagged under a hot theme ([[depin|DePIN]], liquid staking, RaaS) rather than on usage metrics — a speculative, mean-reverting pattern.
- **Deep-cycle value vs value trap:** ~98% below ATH with a clean cap structure makes ANKR a deep-cycle bet on Web3 infra demand recovering; the risk is that RPC commoditization means demand never accrues to the token.

---

## Notable History

- **2021-04-16** — All-time high of $0.2135 during the bull-cycle peak.
- Expanded from an Ethereum-native token into a broad multi-chain footprint (12+ chains) as liquid staking and RaaS products launched.
- Like most 2021-era infrastructure tokens, ANKR has spent the subsequent cycle deeply below its ATH (~-98%), reflecting both broad altcoin drawdown and the commoditization of RPC services.

---

## Risks

- **Thin liquidity** — ~$6.9M daily volume on a ~$37M cap; large orders move price and exits can be costly in stressed markets.
- **Commoditized product** — RPC/node infrastructure is competitive (Alchemy, Infura, QuickNode, public RPCs); margin and differentiation pressure is structural.
- **Hype-cycle exposure** — ANKR is repeatedly retagged under whatever narrative is hot (DePIN, liquid staking, RaaS), which can drive speculative spikes that reverse hard, especially in an extreme-fear regime.
- **Bear-market beta** — as a low-cap altcoin it carries high beta to overall crypto risk-off moves; the current "Established Bear Market" backdrop is a headwind.
- **No unlock overhang** is a positive, but the flip side is no emissions-driven incentive flywheel to bootstrap new demand.

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[depin]]
- [[the-graph]]
- [[indexing]]
- [[crypto-fear-and-greed-index]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-21 via cryptodataapi.com / CoinGecko (`raw/data/crypto-loop/coingecko-markets.json`).
