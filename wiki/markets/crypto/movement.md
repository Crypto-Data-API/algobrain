---
title: "Movement"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, hyperliquid, perpetual-futures, funding-rate, open-interest, altcoins, ethereum]
aliases: ["MOVE"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.movementnetwork.xyz/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[hyperliquid]]", "[[layer-1]]", "[[staking]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[hl-vs-cex-funding-divergence]]", "[[cash-and-carry]]"]
---

# Movement

**Movement** (ticker **MOVE**) is a blockchain network built around the **Move programming language** — the smart-contract language originally developed for Meta's Diem/Libra project and now used by Aptos and Sui. Movement positions itself as a way to bring Move's resource-oriented, security-focused execution model to the broader [[ethereum]] ecosystem, combining a Move-based execution environment with Ethereum settlement to behave as a high-performance Layer 2 / modular network. The native token, MOVE, is used for transaction fees and [[staking]] to secure the network. It is a small-cap asset, ranked **#467** by market capitalization as of this snapshot.

---

## Market Data

| Field | Detail |
|---|---|
| **Ticker** | MOVE |
| **Current Price** | $0.01209540 |
| **Market Cap** | $48.48M |
| **Market Cap Rank** | #467 |
| **24h Volume** | $10.25M |
| **24h Change** | +0.77% |
| **7d Change** | -1.14% |
| **All-Time High** | $1.45 (2024-12-10) — **-99.2%** |
| **All-Time Low** | $0.01097586 (2026-06-06) |
| **Fully Diluted Valuation** | $121.13M |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

The broader market backdrop on this date is bearish: the [[fear-and-greed-index|Crypto Fear & Greed Index]] reads **23 (Extreme Fear)**, and conditions are characterized as an **Established Bear Market**. MOVE trades roughly **-99.2%** below its all-time high of $1.45 (2024-12-10) and sits just above its all-time low of $0.01097586 (2026-06-06), placing it firmly among the deeply drawn-down small-caps in the current cycle.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~4.00B MOVE |
| **Total Supply** | 10.00B MOVE |
| **Max Supply** | 10.00B MOVE |
| **Fully Diluted Valuation** | $121.13M |
| **Market Cap / FDV Ratio** | ~0.40 |

Roughly 40% of the maximum 10B MOVE supply is in circulation. The gap between market cap (~$48M) and FDV (~$121M) means substantial future unlocks/emissions are still pending — a meaningful **dilution overhang** for holders, as additional tokens entering circulation can pressure price absent matching demand. MOVE is used to pay network transaction fees and can be staked to help secure the network and earn rewards; staking inflation/emissions are part of how new supply is distributed over time. With ~60% of supply still to enter circulation, MOVE's dilution profile is far heavier than fully-circulating peers like [[multiversx]] (EGLD) or [[kusama]] (KSM), and comparable to other recent VC/airdrop launches such as [[plasma]] (XPL).

---

## Market Structure & Derivatives

**Spot venues (centralized):**

| Exchange | Pair | Type |
|---|---|---|
| Binance | MOVE/USDT | CEX spot |
| Upbit | MOVE/KRW | CEX spot (Korea) |
| Bitget | MOVE/USDT | CEX spot |
| KuCoin | MOVE/USDT | CEX spot |
| Crypto.com Exchange | MOVE/USD | CEX spot |

**Spot venues (decentralized):** Uniswap V3 on [[ethereum]] (MOVE/WETH) and DEXs across the [[base|Base]] and HyperEVM ecosystems.

**Derivatives:** A **MOVE-PERP** perpetual market is listed on [[hyperliquid]], so traders can take leveraged long/short exposure on-chain. Perpetual venues expose [[funding-rate]] dynamics and open-interest swings; in an extreme-fear regime, funding can stay persistently negative as shorts dominate. Granular funding/OI figures are not captured in this snapshot — confirm live on the venue before sizing a position.

24h spot turnover of ~$10.25M against a ~$48M market cap implies relatively active rotation for a coin this size (~21% of cap — the highest turnover-to-cap ratio in this cohort), but liquidity is still thin compared with majors, so slippage on larger orders is a real consideration. The combination of high turnover and an available perp makes MOVE more leverage-driven and reflexive than the spot-only names in this group.

---

## Technology & Consensus

Movement's defining feature is the **Move language**, a resource-oriented smart-contract language designed to make assets first-class, non-copyable objects at the language level — reducing whole classes of bugs (e.g., reentrancy, double-spends) common in Solidity. The network's M1/Move execution layer aims to combine Move's parallel-execution performance with Ethereum settlement and data availability, presenting Movement as a **modular** design where execution, settlement, and consensus can be separated. MOVE is the gas and staking asset that secures the validator/sequencer set. (See [[move-language]], [[layer-1]], [[proof-of-stake]].)

---

## Use Case, Narrative & Category

Movement's pitch is **Move-language scalability for Ethereum** — bringing the developer ergonomics and safety of Move (popularized by Aptos and Sui) to an EVM-adjacent, Ethereum-aligned environment. Its category tags span Infrastructure, Smart Contract Platform, Modular Blockchain, and the Ethereum, Base, HyperEVM, and Hyperliquid ecosystems. The narrative is a bet that Move adoption keeps growing and that an Ethereum-settled Move chain captures developers who want both Move's safety model and Ethereum's liquidity/security.

---

## Valuation Framing (qualitative)

MOVE is priced as a **post-hype, heavily-diluted new-L2 launch** that round-tripped from a $1.45 launch-window ATH to near-$0.011 all-time lows — a ~99% drawdown. Two structural overhangs dominate any valuation: (1) **dilution** — only ~40% of the 10B supply circulates, so FDV (~$121M) is ~2.5x market cap and future unlocks/emissions are a standing sell-pressure risk; and (2) **execution/adoption** — the thesis depends on Move-language traction holding up against direct rivals Aptos and Sui plus the broader L2 field. The bull case is that a Move-settled, Ethereum-aligned chain wins a durable developer niche and that TVL/usage inflects; the bear case is that MOVE is one of many over-supplied 2024-25 launches with thin product-market fit. With an active Hyperliquid perp, near-term price is also unusually sensitive to leverage and funding rather than spot demand alone.

---

## Peer Comparison

| Asset | Ticker | Mkt-cap rank | Approach | Supply (circ. / max) | Perp? | From ATH |
|---|---|---|---|---|---|---|
| **Movement** | MOVE | #467 | Move-language modular L2 on [[ethereum]] | ~40% of 10B | [[hyperliquid]] | -99.2% |
| Aptos | APT | top-tier alt | Move L1 (Diem lineage) | inflationary | yes | below ATH |
| Sui | SUI | top-tier alt | Move L1 (Diem lineage) | inflationary | yes | below ATH |
| [[multiversx]] | EGLD | #295 | Sharded L1 | ~fully circulating | no (snapshot) | -99.5% |

MOVE is the smallest and most diluted of the Move-language cohort, differentiated by its Ethereum-settlement / modular framing rather than running as a standalone Move L1 like Aptos and Sui.

---

## Notable History

- **2024-12**: MOVE reached its all-time high of $1.45 shortly after launch (2024-12-10) amid heavy attention and exchange listings.
- Movement Labs attracted backing associated with major crypto investors (the token carries category tags including YZi Labs / former Binance Labs and OKX Ventures portfolios, plus a Binance HODLer Airdrops tag).
- **2026-06-06**: MOVE printed a fresh all-time low of ~$0.011 amid the broader bear market — a ~99% drawdown from the ATH.

---

## Risks

- **Severe drawdown / weak trend**: MOVE is down ~99% from ATH and trading near record lows; there is no demonstrated price-trend support in the current regime.
- **Dilution overhang**: Market cap is far below FDV; future unlocks and staking emissions can pressure price.
- **Small-cap liquidity**: ~$47M market cap with thin order books means high volatility and slippage risk.
- **Competition**: Competes directly with Aptos, Sui (other Move chains) and the broader L2 field for developers and liquidity.
- **Macro / regime risk**: Extreme Fear (index 23) and an Established Bear Market backdrop weigh on all small-cap, high-beta assets.
- **Leverage risk**: With a Hyperliquid perp available, crowded positioning and funding swings can amplify moves in both directions.

---

## Related

- [[crypto-markets]]
- [[ethereum]]
- [[base]]
- [[multiversx]]
- [[layer-1]]
- [[staking]]
- [[hyperliquid]]
- [[move-language]]
- [[fear-and-greed-index]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data snapshot 2026-06-21 (cryptodataapi.com / CoinGecko).

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | MOVE |
| **Market Cap Rank** | #462 |
| **Market Cap** | $45.08M |
| **Current Price** | $0.0108 |
| **Categories** | Infrastructure, Smart Contract Platform, Layer 1 (L1), Zero Knowledge (ZK), Modular Blockchain, Binance HODLer Airdrops, Made in USA, Base Native |
| **Website** | [https://www.movementnetwork.xyz/](https://www.movementnetwork.xyz/) |

---

## Overview

Movement Network is a secure and scalable blockchain designed to make Move programming accessible to developers everywhere. With high-performance execution and security, Movement delivers the infrastructure for the next generation of decentralized applications and unleashes opportunity and financial empowerment for anyone, anywhere.

$MOVE is the native token of Movement Network, for transaction fees and staking to secure the network. The Movement M1 (Layer 1) Network is powered by the Move programming language, unleashing opportunity, accessibility, and financial empowerment for anyone, anywhere.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 4.17B MOVE |
| **Total Supply** | 10.00B MOVE |
| **Max Supply** | 10.00B MOVE |
| **Fully Diluted Valuation** | $108.18M |
| **Market Cap / FDV Ratio** | 0.42 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.45 (2024-12-10) |
| **Current vs ATH** | -99.25% |
| **All-Time Low** | $0.0105 (2026-06-24) |
| **Current vs ATL** | +3.00% |
| **24h Change** | -0.09% |
| **7d Change** | -3.66% |
| **30d Change** | -14.40% |
| **1y Change** | -93.01% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x3073f7aaa4db83f95e9fff17424f71d4751a3073` |
| Movement | `0xa` |
| Base | `0x3073f7aaa4db83f95e9fff17424f71d4751a3073` |
| Hyperevm | `0x3073f7aaa4db83f95e9fff17424f71d4751a3073` |
| Hyperliquid | `0xedfb8d993ee8cb935338601d8673dfcf` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | MOVE/TRY | N/A |
| Upbit | MOVE/KRW | N/A |
| Bitget | MOVE/USDT | N/A |
| KuCoin | MOVE/USDT | N/A |
| Crypto.com Exchange | MOVE/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0X3073F7AAA4DB83F95E9FFF17424F71D4751A3073/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.movementnetwork.xyz/](https://www.movementnetwork.xyz/) |
| **Twitter** | [@movementfdn](https://twitter.com/movementfdn) |
| **Telegram** | [MoveindustriesAnn](https://t.me/MoveindustriesAnn) (12 members) |
| **Discord** | [https://discord.gg/moveindustries](https://discord.gg/moveindustries) |
| **GitHub** | [https://github.com/movementlabsxyz/](https://github.com/movementlabsxyz/) |
| **Whitepaper** | [https://docs.movementnetwork.xyz/](https://docs.movementnetwork.xyz/) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $7.08M |
| **Market Cap Rank** | #462 |
| **24h Range** | $0.0107 — $0.0111 |
| **CoinGecko Sentiment** | 100% positive |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Trading Profile

**Venues & liquidity.** MOVE is a rare small-cap with a genuine two-venue derivatives market: it trades on **Binance** (spot MOVE/USDT and a USD-margined perpetual) and on **[[hyperliquid]]** (MOVE-PERP, with leverage up to roughly ~40-50x). Having both a deep CEX venue and an on-chain perp gives MOVE meaningfully better depth and tighter spreads than perp-only or spot-only micro-caps, and it opens genuine cross-venue execution: traders can route spot on Binance, hedge or express directional views on either perp, and arbitrage price/funding differences between Binance and Hyperliquid. That said, absolute depth is still that of a ~$45-50M-cap alt — order books thin out quickly, so size positions to the shallower of the two venues and expect slippage on larger clips. The dual listing also makes leverage-driven, reflexive moves more likely than in the spot-only names in its cohort.

**Applicable strategies.**
- [[hl-vs-cex-funding-divergence]] — MOVE's presence on both Binance perp and Hyperliquid MOVE-PERP lets you harvest funding-rate gaps between the two venues.
- [[cash-and-carry]] — long Binance spot MOVE against a short perp captures positive basis/funding without directional exposure to the heavily-diluted token.
- [[crowded-short-funding-fade]] — in the extreme-fear regime shorts often dominate; persistently negative funding flags crowded shorts that can be faded into squeezes.
- [[liquidation-cascade-fade]] — thin two-sided depth means leverage flushes overshoot; fading forced-liquidation wicks near the all-time-low zone is a recurring setup.
- [[token-unlock-supply-event]] — with only ~40% of the 10B supply circulating, scheduled unlocks/emissions are tradable supply catalysts.
- [[range-mean-reversion]] — pinned near its ATL in a bear regime, MOVE oscillates in a compressed band that suits reversion around support/resistance.

**Volatility & regime character.** MOVE is a **high-beta, deeply-drawn-down infra/L1 alt** (Move-language modular L2 on Ethereum), currently ~99% below its ATH and hovering near record lows. It behaves with high directional beta to BTC/ETH — it sells off hard in risk-off, extreme-fear conditions and can rip on any broad-alt or Move-narrative relief — but with amplified amplitude and reflexivity because of its small cap, active perps, and heavy dilution overhang. Expect wide intraday ranges relative to majors and outsized reactions to leverage flushes and funding swings rather than to organic spot demand.

**Risk flags.**
- **Liquidity/venue concentration** — real depth lives on just Binance and Hyperliquid; a listing change, outage, or funding dislocation on either venue can whipsaw price and strand hedges.
- **Dilution / token unlocks** — ~60% of the 10B max supply is still to enter circulation; unlocks and staking emissions are standing sell-pressure catalysts.
- **Narrative dependence** — the bid depends on Move-language adoption holding up against Aptos and Sui; adoption stalls disproportionately hurt a post-hype launch like MOVE.
- **Perp funding dislocations** — with an active perp on both venues, crowded positioning and funding spikes can force cascades in either direction; confirm live funding/OI before sizing.
- **Regulatory/regime risk** — Extreme Fear and an Established Bear Market backdrop weigh on all small-cap, high-beta alts.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/summary?coin=MOVE` — all-in-one perp data (mark, funding, OI)
- `GET /api/v1/hyperliquid/prices` — all mid prices
- `GET /api/v1/hyperliquid/l2-book?coin=MOVE` — L2 order-book depth
- `GET /api/v1/hyperliquid/open-interest` — all-asset open interest

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=MOVE&interval=1h&limit=1000` — OHLCV candles
- `GET /api/v1/hyperliquid/funding-rates?coin=MOVE&limit=100` — funding history
- `GET /api/v1/daily/hyperliquid` — daily bulk snapshot of ~230 HL perps

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/summary?coin=MOVE"
```

Auth: `X-API-Key` header. Endpoint catalog: [[cryptodataapi-hyperliquid]]. See also [[cryptodataapi]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---
