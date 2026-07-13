---
title: "Jupiter"
type: entity
created: 2026-04-09
updated: 2026-06-20
status: excellent
tags: [crypto, defi, derivatives, altcoins, exchange]
aliases: ["JUP", "Jupiter Exchange", "Jupiter Aggregator"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://jup.ag/"
related: ["[[crypto-markets]]", "[[solana]]", "[[raydium]]", "[[orca]]", "[[uniswap]]", "[[hyperliquid]]", "[[gmx]]", "[[kamino]]", "[[jupiter-lend]]"]
---

# Jupiter

**Jupiter** (JUP) is a cryptocurrency exchange platform on the Solana blockchain, offering features such as token swapping, limit orders, dollar-cost averaging, and a bridge for asset transfers to Solana. It provides users with tools to find the best trading prices and includes a beta version for perpetual futures trading. It ranks **#94** by market capitalization.

> **Disambiguation:** This page covers **Jupiter Exchange** (the DEX aggregator and JUP token). For Jupiter's lending and money-market product (launched August 2025; ~$1.65B TVL Q1 2026), see [[jupiter-lend]].

---

## Market Data

| Field | Value |
|---|---|
| **Current Price** | $0.1993 |
| **Market Cap** | $661.45M |
| **Market Cap Rank** | #87 |
| **Fully Diluted Valuation** | $1.37B |
| **24h Volume** | $32.04M |
| **24h Range** | $0.1834 — $0.2001 |
| **24h Change** | +6.50% |
| **7d Change** | +14.38% |
| **Circulating Supply** | 3.32B JUP |
| **Total Supply** | 6.86B JUP |
| **Max Supply** | 10.00B JUP |
| **MC / FDV** | 0.48 |
| **All-Time High** | $2.00 (2024-01-31) — currently -90.06% |
| **All-Time Low** | $0.1358 (2026-02-12) — currently +46.45% |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

**Macro backdrop (2026-06-20):** Crypto Fear & Greed Index at **23 (Extreme Fear)** in an **Established Bear Market**. JUP nonetheless outperformed over the prior week (+14.4% / 7d) — high-beta [[solana|Solana]] DeFi names tend to whipsaw hardest in both directions. It trades ~90% below its January 2024 ATH but ~46% above its February 2026 ATL.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | JUP |
| **Market Cap Rank** | #87 |
| **Native Chain** | [[solana|Solana]] (also deployed to Unichain) |
| **Sector** | [[decentralized-exchange|DEX]] aggregator + perp venue + lending; Solana DeFi |
| **Categories** | Decentralized Exchange (DEX), Exchange-based Tokens, Decentralized Finance (DeFi), Perpetuals, Solana Ecosystem, Launchpad, GMCI DeFi Index, Dex Aggregator, GMCI Index, Made in USA, Unichain Ecosystem |
| **Website** | [https://jup.ag/](https://jup.ag/) |

---

## Overview

Jupiter is a cryptocurrency exchange platform on the [[solana|Solana]] blockchain, offering features such as token swapping, limit orders, dollar-cost averaging, and a bridge for asset transfers to Solana. It provides users with tools to find the best trading prices and includes a perpetual futures product. Jupiter finds the best price route for your swap by aggregating all the major liquidity sources on Solana.

---

## Protocol & Technology

Jupiter is not a single AMM — it is a **routing and liquidity-orchestration layer** plus a vertically integrated DeFi stack on [[solana|Solana]].

### DEX aggregation engine
- Jupiter's router (the **Metis** routing algorithm) splits a single swap across many underlying liquidity sources — [[raydium|Raydium]], [[orca|Orca]], Meteora, Lifinity, Phoenix, and others — to minimize price impact and slippage.
- It supports complex multi-hop and split routes, so it consistently quotes best execution without operating its own pools for every pair. This is why the **vast majority of Solana swap volume** routes through Jupiter.
- Smart-contract integrations let any Solana wallet, app, or bot embed Jupiter as its swap backend (the de-facto Solana swap API).

### Jupiter Perps (it is itself a perp venue)
Jupiter operates a native **perpetual futures exchange** on Solana — a major distinction from a pure aggregator. It competes directly with [[hyperliquid|Hyperliquid]], [[gmx|GMX]], and [[dydx-chain|dYdX]]:
- **Up to 100x leverage** on SOL, ETH, and BTC perps.
- **Oracle-based pricing** via Pyth feeds, reducing on-chain front-running.
- **Pool-backed model** (the JLP pool, below) rather than a central limit order book — traders trade against the LP pool, GMX-style.

### JLP pool (Jupiter Liquidity Provider)
The **JLP pool** backs Jupiter Perps. Depositors mint JLP tokens representing a share of a basket (SOL, ETH, BTC, USDC, USDT) and earn ~75% of perp trading fees plus net trader PnL losses. JLP is effectively the **counterparty to all Jupiter perp trades** — a bet that leveraged traders lose money over time (historically well-supported), with directional exposure to the underlying basket.

### Broader stack
Token swap, limit orders, on-chain DCA, a Solana bridge, the **LFG launchpad**, predictions, and lending ([[jupiter-lend|Jupiter Lend]], Aug 2025) — making JUP a proxy on the entire Solana on-chain finance economy, not just spot swaps.

---

## Tokenomics & Supply

| Metric | Value (2026-06-20) |
|---|---|
| **Circulating Supply** | 3.32B JUP |
| **Total Supply** | 6.86B JUP |
| **Max Supply** | 10.00B JUP |
| **Fully Diluted Valuation** | $1.37B |
| **MC / FDV** | 0.48 |
| **Circulating / Max** | ~33.2% |

**Emissions / dilution flag.** Only ~33% of the 10B max supply circulates and MC/FDV is **0.48** — a **significant dilution overhang**. Future unlocks (team, ecosystem, and airdrop allocations) are an ongoing source of structural sell pressure; the gap between circulating (~3.32B) and total (~6.86B) is the near-term vesting pipeline. Jupiter has periodically burned tokens and adjusted emissions via governance, but JUP remains a high-float-risk name. Fee revenue may accrue to stakers through governance, the key offset to dilution.

---

## Price History

| Metric | Value (2026-06-20) |
|---|---|
| **All-Time High** | $2.00 (2024-01-31) |
| **Current vs ATH** | -90.06% |
| **All-Time Low** | $0.1358 (2026-02-12) |
| **Current vs ATL** | +46.45% |
| **24h Change** | +6.50% |
| **7d Change** | +14.38% |

---

## Platform & Chain Information

**Native Chain:** Solana

### Contract Addresses

| Chain | Address |
|---|---|
| Solana | `JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN` |
| Unichain | `0xbe51a5e8fa434f09663e8fb4cce79d0b2381afad` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | JUP/USDT | N/A |
| Kraken | JUP/USD | N/A |
| Upbit | JUP/KRW | N/A |
| Bitget | JUP/USDT | N/A |
| KuCoin | JUP/USDT | N/A |
| Crypto.com Exchange | JUP/USDT | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| [[hyperliquid|Hyperliquid]] | JUP-PERP | Perpetual |
| Orca | JUPYIWRYJFSKUPIHA7HKER8VUTAEFOSYBKEDZNSDVCN/SO11111111111111111111111111111111111111112 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://jup.ag/](https://jup.ag/) |
| **Twitter** | [@JupiterExchange](https://twitter.com/JupiterExchange) |
| **Discord** | [https://discord.com/invite/jup](https://discord.com/invite/jup) |
| **GitHub** | [https://github.com/jup-ag](https://github.com/jup-ag) |

---

## Trading Characteristics

| Characteristic | Detail (2026-06-20) |
|---|---|
| **24h Volume** | $32.04M |
| **Market Cap Rank** | #87 |
| **24h Range** | $0.1834 — $0.2001 |
| **CoinGecko Sentiment** | 100% positive (April 2026 reading) |
| **Last Updated** | 2026-06-20 |

---

## Market Structure & Derivatives

| Layer | Detail |
|---|---|
| **Spot CEX** | Binance (JUP/USDT), Kraken (JUP/USD), Upbit (JUP/KRW — Korean flow), Bitget, KuCoin, Crypto.com |
| **Spot DEX** | Orca (Solana); JUP itself is the routing layer for Solana spot |
| **Perps on JUP token** | JUP-PERP on [[hyperliquid|Hyperliquid]] and major CEX futures |
| **Jupiter *as* a perp venue** | Jupiter Perps offers up to 100x on SOL/ETH/BTC, Pyth-oracle priced, JLP-pool backed — a top-tier on-chain perp venue competing with [[hyperliquid|Hyperliquid]], [[gmx|GMX]], [[dydx-chain|dYdX]] |
| **JLP yield** | JLP LPs historically earned ~20–60% APY in active markets from perp fees + net trader losses; directional exposure to the SOL/ETH/BTC basket |
| **Funding / OI** | On Jupiter Perps, funding/borrow rates accrue to the JLP pool; crowded one-sided positioning drains or feeds the pool depending on trader PnL |

Trading JUP is effectively a **levered bet on total Solana DeFi throughput** — swap volume, perp volume, and meme-coin activity all flow through Jupiter.

---

## Valuation Framework

JUP is one of the few tokens with **real protocol revenue** to anchor valuation:

- **Aggregator swap volume / fees** — total Solana swaps routed through Jupiter and the take rate; the core revenue line.
- **Perp volume + JLP fee capture** — Jupiter Perps notional volume and the ~75% of perp fees flowing to JLP; a second revenue engine.
- **Protocol revenue / FDV (P/S analog)** — compare against [[hyperliquid|Hyperliquid]], [[gmx|GMX]], and [[uniswap|Uniswap]] for relative value; JUP's high FDV vs realized fees is the bear case.
- **Fees accruing to JUP stakers** — governance-directed buybacks/distributions are the mechanism by which usage translates into token value.
- **TVL across the stack** — JLP pool, [[jupiter-lend|Jupiter Lend]] (~$1.65B Q1 2026), launchpad activity.

*(No invented values: the wiki holds no live fee series; track via Jupiter analytics / DefiLlama.)*

---

## Competitive Positioning

| Venue | Type | Token | Chain | vs Jupiter |
|---|---|---|---|---|
| **Jupiter** | Aggregator + perps + lending | JUP | [[solana]] | Solana's dominant router + integrated DeFi stack |
| [[raydium\|Raydium]] | AMM (liquidity source) | RAY | [[solana]] | Jupiter routes *through* it; complement, not pure rival |
| [[orca\|Orca]] | Concentrated-liquidity AMM | ORCA | [[solana]] | Liquidity source Jupiter aggregates |
| [[uniswap\|Uniswap]] | AMM + aggregation (UniswapX) | UNI | Ethereum/L2s | Cross-chain rival; Jupiter also deployed on Unichain |
| [[hyperliquid\|Hyperliquid]] | Perp DEX (order book) | HYPE | Own L1 | Direct perp competitor; CLOB vs JLP-pool model |
| [[gmx\|GMX]] | Perp DEX (pool-backed) | GMX | Arbitrum/Avax | GLP vs JLP — near-identical model on other chains |
| [[dydx-chain\|dYdX]] | Perp DEX (order book) | DYDX | Own Cosmos L1 | Order-book perp competitor |

Jupiter's moat is **aggregation dominance on Solana + a vertically integrated stack** (swap, perps, lend, launchpad). Its risk: as Solana's de-facto router, it lives and dies with Solana's market share and uptime.

---

## History

| Date | Event |
|---|---|
| **2021–2023** | Jupiter emerges as the leading DEX aggregator on [[solana]] during the Solana DeFi build-out |
| **2024-01-31** | JUP token TGE and large airdrop; ATH $2.00 amid Solana meme-coin mania |
| **2024–2025** | Expands into Perps (JLP pool), DCA, limit orders, LFG launchpad; survives 2024 Solana volatility |
| **Aug 2025** | [[jupiter-lend|Jupiter Lend]] launches; TVL reaches ~$1.65B by Q1 2026 |
| **2026-02-12** | ATL $0.1358 during the established bear market |
| **2026-06-20** | ~$0.1993, #87 by market cap; +14.4%/7d outperformance |

---

## Jupiter as Solana's Dominant DEX Aggregator

Jupiter is the undisputed liquidity routing layer on [[solana]]. When a user swaps any token pair on Solana, Jupiter splits the order across multiple DEXes ([[raydium]], [[orca]], Meteora, Lifinity, and others) to find the optimal execution price. This aggregator model means Jupiter captures the vast majority of Solana swap volume without needing its own liquidity pools for every pair.

**Why this matters for traders:** Jupiter's dominance means that JUP token price is effectively a proxy bet on total Solana DeFi trading volume. When meme coin activity surges on Solana, Jupiter volume spikes, and fee revenue flows to the protocol.

---

## Trading Products

### Limit Orders

Jupiter supports on-chain limit orders, a feature rare among DEX aggregators. Traders can set a price target for any Solana token pair, and the order executes when market conditions are met. Orders are filled by Jupiter's keeper network, which monitors prices across all integrated DEXes.

- **Use case:** Avoid slippage on volatile Solana meme coins by setting a limit price rather than market-buying into a pump
- **Fee:** Small keeper fee on execution

### Dollar-Cost Averaging (DCA)

Jupiter's DCA feature lets users split a large buy or sell order into smaller chunks executed over a configurable time period (minutes, hours, days). This is implemented entirely on-chain.

- **Use case:** Accumulate [[solana|SOL]] or JUP over weeks without timing the market
- **Advantage over CEX DCA:** Fully non-custodial, executes through the aggregator for best prices
- **Cost:** Minor platform fee per DCA execution

### Perpetual Trading

Jupiter operates a perpetual futures exchange (Jupiter Perps) directly on Solana, competing with [[hyperliquid]], [[gmx]], and [[dydx-chain|dYdX]].

- **Leverage:** Up to 100x on SOL, ETH, and BTC perpetuals
- **Oracle-based pricing:** Uses Pyth oracles for price feeds, minimizing front-running
- **Liquidity pool:** Funded by the JLP pool (see below)
- **Trading fees:** Competitive with centralized perp exchanges given Solana's low gas costs

---

## JLP Pool (Jupiter Liquidity Provider)

The **JLP pool** is Jupiter's liquidity pool backing its perpetual trading product. It functions similarly to [[gmx|GMX's]] GLP pool: depositors provide liquidity that traders trade against, and earn yield from trader losses, borrowing fees, and swap fees.

### How JLP Works

| Component | Detail |
|---|---|
| **Assets in pool** | SOL, ETH, BTC, USDC, USDT |
| **Yield sources** | 75% of perpetual trading fees + trader PnL losses |
| **Risk** | Pool loses when perp traders are net profitable |
| **Mechanism** | Depositors mint JLP tokens representing their share of the pool |

### JLP as a Trading Strategy

JLP is effectively a bet that **most leveraged traders lose money over time** -- a historically well-supported thesis. The pool acts as the counterparty to all Jupiter perp trades.

- **Bull case:** High trading volume + net trader losses = strong yield (historically 20-60% APY during active markets)
- **Bear case:** A period of highly directional markets where leveraged traders are net winners drains the pool
- **Correlation:** JLP is long the underlying assets (SOL, ETH, BTC) in the pool, so it has directional exposure plus fee yield
- **Comparison to GLP:** Similar concept to [[gmx|GMX's GLP]], but benefits from Solana's faster settlement and lower gas costs

---

## JUP Token Trading Analysis

### What Drives JUP Price

1. **Solana ecosystem activity** -- JUP is a high-beta play on Solana DeFi volume. When Solana meme coin or DeFi activity surges, Jupiter volume explodes
2. **Fee revenue** -- protocol fees from swaps, perps, and DCA flow to the treasury and may accrue to JUP stakers via governance votes
3. **Token unlock schedule** -- with only ~3.32B of 10B max supply circulating (~33.2%), future unlocks create sell pressure
4. **Governance power** -- JUP stakers vote on fee distribution, new product launches, and protocol grants
5. **Airdrop speculation** -- Jupiter has conducted multiple large airdrops to active users, driving Solana ecosystem activity

### Trading Characteristics (Extended)

- **High beta to SOL:** JUP typically moves 1.5-2.5x the magnitude of SOL price moves
- **Volume correlation:** Trading volume for JUP itself spikes during Solana meme coin seasons
- **Liquidity:** Deep CEX liquidity on [[binance]] (JUP/USDT), plus perpetual trading on [[hyperliquid]]
- **Volatility:** Extremely high -- ~90% drawdown from ATH of $2.00 to current levels (~$0.20, 2026-06-20)

### Risk Factors

- **Solana dependency:** A Solana network outage or loss of market share to other L1s directly impacts Jupiter
- **Token dilution:** Only ~33% of max supply is circulating; vesting schedule creates ongoing sell pressure (MC/FDV 0.48)
- **Competition:** [[raydium]], [[orca]], and new Solana DEXes could erode Jupiter's aggregator dominance
- **Regulatory risk:** DEX aggregators may face regulatory scrutiny as DeFi regulation evolves

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

### 2025-2026 Update (as of June 2026)

- **Status: active.** Jupiter remains the dominant DEX aggregator on [[solana]] and has expanded into a broader on-chain finance stack: spot/aggregated swaps, perpetuals, **lending ([[jupiter-lend|Jupiter Lend]], launched August 2025)**, predictions, and a developer API suite.
- **Price/market cap (2026-06-20):** JUP trades **$0.1993** with a market cap of **$661.45M**, ranked **#87** (Source: cryptodataapi.com / CoinGecko, 2026-06-20). Earlier mid-2026 readings put it at $0.15-$0.18 / ~$490M-$580M (Verified via Perplexity (sonar), 2026-06-11).
- No exploit, shutdown, or token migration has been reported through mid-2026. JUP outperformed (+14.4%/7d) into the 2026-06-20 snapshot despite the broader extreme-fear backdrop.

> *Earlier notable events will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]
- [[solana]]
- [[raydium]] -- Solana AMM, major liquidity source for Jupiter
- [[orca]] -- Solana concentrated liquidity DEX
- [[gmx]] -- comparable perp DEX model (GLP vs JLP)
- [[hyperliquid]] -- perp DEX competitor
- [[kamino]] -- Solana DeFi protocol with complementary yield products

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data 2026-06-20 — cryptodataapi.com / CoinGecko markets snapshot (`raw/data/crypto-loop/coingecko-markets.json`)
- [CoinGecko — Jupiter](https://www.coingecko.com/en/coins/jupiter)
- [CoinMarketCap — Jupiter](https://coinmarketcap.com/currencies/jupiter-ag/)
- Verified via Perplexity (sonar), 2026-06-11
