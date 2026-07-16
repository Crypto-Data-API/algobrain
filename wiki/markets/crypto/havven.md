---
title: "Synthetix"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: good
tags: [crypto, defi, derivatives, hyperliquid, perpetual-futures, funding-rate, open-interest, liquidations, altcoins]
aliases: ["Havven", "SNX"]
entity_type: protocol
founded: 2018
headquarters: "Decentralized"
website: "https://www.synthetix.io/"
related: ["[[crypto-markets]]", "[[decentralized-exchange]]", "[[ethereum]]", "[[funding-rate]]", "[[hyperliquid]]", "[[perpetual-futures]]", "[[open-interest]]", "[[cash-and-carry]]", "[[funding-rate-harvest]]"]
---

# Synthetix

**Synthetix** (SNX, originally launched as *Havven*) is a veteran [[ethereum|Ethereum]] DeFi protocol that evolved from a synthetic-asset issuance system into a **decentralized derivatives / [[perpetual-futures|perpetual futures]] liquidity layer**. SNX is staked as collateral to back synthetic assets and the protocol's perp markets, with stakers earning protocol fees and absorbing first-loss risk. Synthetix has run on Ethereum Mainnet, Optimism, and Base, and its liquidity has powered front-ends like Kwenta and other perp DEXs.

---

## Market Data

| Field | Detail |
|---|---|
| **Ticker** | SNX |
| **Market Cap Rank** | #303 |
| **Market Cap** | $83.08M |
| **Current Price** | $0.241223 |
| **24h Change** | -0.83% |
| **7d Change** | +0.75% |
| **24h Volume** | $7.35M |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

Context: with the market in **extreme fear** (Fear & Greed = 22) and an **Established Bear Market** regime as of 2026-06-20, SNX trades as a small-cap (#303) DeFi token far below its prior-cycle highs, with modest daily turnover relative to its float.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~344.52M SNX |
| **Total Supply** | ~344.94M SNX |
| **Max Supply** | ~344.94M SNX |
| **Market Cap / FDV** | ~1.00 |

SNX is effectively **fully circulating** (circulating ≈ total ≈ max supply), so there is no meaningful unlock overhang — a contrast with newer low-float perp tokens like [[lighter|Lighter]]. SNX's defining mechanic is **staking-as-collateral**: SNX locked by stakers backs synthetic-asset issuance (e.g., sUSD) and the solvency of the protocol's liquidity vaults. Stakers earn protocol fees but take on debt-pool and first-loss exposure, and historically faced inflationary staking rewards (since reduced).

---

## How & Where It Trades

**Spot venues (CEX):** SNX trades on Binance (including SNX/TRY), Kraken, Upbit, Bitget, KuCoin, and Crypto.com Exchange.

**On-chain spot:** Deeply liquid on Uniswap V2/V3, SushiSwap, and Balancer V2 (Ethereum) against WETH; also deployed to Optimism, Base, and other chains.

**The protocol's own venue:** Synthetix is a **derivatives liquidity backend**, not a simple AMM. Its hybrid design pairs off-chain order matching on a high-performance CLOB with on-chain settlement, aiming for low latency, deep liquidity, and MEV-resistant execution. SNX stakers collectively act as the counterparty/backstop to traders via the staked-collateral debt pool — a distinctive "pooled-counterparty" model rather than peer-to-peer order books.

**Derivatives on SNX itself:** SNX is listed as a perpetual on [[hyperliquid|Hyperliquid]] (SNX-PERP). As a smaller-cap token, its perp [[funding-rate|funding rate]] and open interest can move sharply with DeFi-sector sentiment and any protocol-upgrade catalysts; thin spot liquidity makes the perp sensitive to liquidation cascades.

---

## Use Case / Narrative / Category

Synthetix pioneered **on-chain synthetic assets** and pivoted toward being the **liquidity infrastructure for decentralized derivatives** — a "DeFi primitive" other protocols build on top of. The long-running narrative is that Synthetix supplies pooled liquidity and a perps engine that front-ends and integrators consume, with SNX stakers earning the resulting fees. The bull case is becoming the default decentralized-derivatives liquidity layer; the bear case is fee/value capture lagging amid fierce perp-DEX competition.

---

## Notable History

- **2017–2018:** Launched as **Havven**, a stablecoin/synthetic-asset project; rebranded to **Synthetix** (genesis ~2018-03).
- **2019–2021:** Built out synthetic assets (sUSD, sETH, synthetic equities/commodities) and a debt-pool staking model; SNX reached an all-time high near $28 in early 2021.
- **2020 onward:** Migrated significant activity to Optimism for cheaper transactions; spawned ecosystem front-ends like Kwenta.
- **Perps pivot:** Reoriented toward perpetual-futures liquidity (Synthetix Perps / v3), positioning SNX collateral as the derivatives backstop.
- SNX has drawn down ~99% from its ATH over the multi-year DeFi derating.

---

## Risks

- **Debt-pool / collateral risk:** SNX stakers bear the protocol's collective debt and first-loss exposure; adverse skew in synth/perp positions can impair staker collateral.
- **Complexity:** The staking, debt-pool, and synth-issuance mechanics are notoriously complex, raising operational and smart-contract risk.
- **Competition:** Perp-DEX rivals (Hyperliquid, dYdX, GMX, Lighter) compete for the same derivatives volume.
- **Bear-market beta:** As a small-cap DeFi token in an extreme-fear / Established Bear Market regime, SNX carries high volatility and drawdown risk.
- **Token value capture:** Persistent question of whether fees and tokenomics adequately reward SNX holders relative to risk taken.

---

## Trading Profile

### Venues & liquidity

SNX trades a **deep, liquid two-venue market**. On **Binance** it has both **spot** (SNX/USDT and others) and a **USD-margined perpetual**; on **Hyperliquid** it lists as **SNX-PERP** with leverage up to roughly **40-50x**. The CEX spot book underpins price discovery while the two perp venues concentrate directional and funding flow. Having both a Binance perp and a Hyperliquid perp means the same exposure can be built on either rail, so execution and sizing benefit from splitting orders across venues to limit slippage on this modest-cap token, and any cross-venue mark or funding gap is directly tradable rather than a data artifact. Depth is respectable for a rank-~216 name but thinner than large caps, so aggressive size still moves the book and can seed liquidation cascades.

### Applicable strategies

- [[funding-rate-harvest]] — collect funding on SNX-PERP when DeFi-sector sentiment pushes crowded directional positioning; sized against thinner spot depth.
- [[hl-vs-cex-funding-divergence]] — arb the funding spread between Hyperliquid SNX-PERP and Binance's USD-margined SNX perp, a clean two-venue setup.
- [[cash-and-carry]] — SNX is fully circulating (MC/FDV ~1.0) with no unlock overhang, so long spot / short perp carry is not distorted by emissions.
- [[liquidation-cascade-fade]] — thin spot liquidity makes SNX prone to sharp perp liquidation flushes that overshoot and mean-revert.
- [[oi-confirmed-trend]] — use SNX-PERP open interest to confirm whether a DeFi-narrative move is backed by real positioning or just noise.
- [[mean-reversion]] — a range-bound, deeply-derated small cap that oscillates within regimes absent a fresh catalyst.

### Volatility & regime character

SNX is a **high-beta DeFi / derivatives infrastructure token** — a small/mid-cap altcoin that amplifies broad crypto risk-on/risk-off swings. It is highly correlated to **ETH** (its native ecosystem) and to BTC beta, and additionally sensitive to **DeFi-sector rotation** and perp-DEX competitive narratives. Down ~99% from its cycle ATH, it behaves as a deep-value / mean-reverting name that trends only on decisive sector catalysts, otherwise ranging with elevated intraday volatility.

### Risk flags

- **Liquidity/venue concentration:** modest cap and thin spot depth mean perp-driven moves can outrun spot, amplifying liquidation cascades.
- **Narrative dependence:** price hinges on DeFi-derivatives sentiment and perp-DEX competition (Hyperliquid, dYdX, GMX, Lighter) rather than idiosyncratic flow.
- **Perp funding dislocations:** two active perp venues can diverge in funding/mark during stress, a risk to one-sided carry and a source of cross-venue arb.
- **Protocol/collateral risk:** SNX staking, debt-pool, and synth-issuance mechanics add smart-contract and first-loss exposure that can transmit to token price.
- **Emissions:** although effectively fully circulating today, historical inflationary staking rewards mean supply policy changes remain worth monitoring.

---

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/summary?coin=SNX` — all-in-one perp data (mark, funding, OI)
- `GET /api/v1/hyperliquid/prices` — all mid prices
- `GET /api/v1/hyperliquid/l2-book?coin=SNX` — L2 order-book depth
- `GET /api/v1/hyperliquid/open-interest` — all-asset open interest

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=SNX&interval=1h&limit=1000` — OHLCV candles
- `GET /api/v1/hyperliquid/funding-rates?coin=SNX&limit=100` — funding history
- `GET /api/v1/daily/hyperliquid` — daily bulk snapshot of ~230 HL perps

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/summary?coin=SNX"
```

Auth: `X-API-Key` header. Endpoint catalog: [[cryptodataapi-hyperliquid]]. See also [[cryptodataapi]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[hyperliquid]]
- [[lighter]]
- [[dydx-chain]]
- [[perpetual-futures]]
- [[funding-rate]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]]) — historical snapshot context
- Market data as of 2026-06-20 from the crypto-loop CoinGecko markets snapshot (cryptodataapi.com / CoinGecko).
- General market knowledge; no specific wiki source ingested yet for protocol mechanics.

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | SNX |
| **Market Cap Rank** | #216 |
| **Market Cap** | $132.96M |
| **Current Price** | $0.2288 |
| **Genesis Date** | 2018-03-11 |
| **Categories** | Decentralized Exchange (DEX), Exchange-based Tokens, Decentralized Finance (DeFi), Yield Farming, Derivatives, Synthetic Issuer, Synthetic, Governance (+1 more) |
| **Website** | [https://www.synthetix.io/](https://www.synthetix.io/) |

---

## Overview

Synthetix is a decentralized perpetual futures protocol built on Ethereum Mainnet. Synthetix uses a hybrid design — off-chain order matching on a high-performance CLOB with on-chain settlement — to deliver low latency, deep liquidity, and MEV-resistant execution while keeping custody and finality on Ethereum. Traders get CEX-like performance with on-chain security and composability. The protocol’s liquidity is provided by the Synthetix Liquidity Provider (SLP) vault and backstopped by staked SNX collateral, which underwrites the issuance of the sUSD stablecoin and the solvency of the SLP vault.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 580.98M SNX |
| **Total Supply** | 581.40M SNX |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $133.05M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $28.53 (2021-02-14) |
| **Current vs ATH** | -99.20% |
| **All-Time Low** | $0.0348 (2019-01-06) |
| **Current vs ATL** | +558.47% |
| **24h Change** | -0.98% |
| **7d Change** | +2.15% |
| **30d Change** | -10.89% |
| **1y Change** | -65.57% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xc011a73ee8576fb46f5e1c5751ca3b9fe0af2a6f` |
| Harmony Shard 0 | `0x7b9c523d59aefd362247bd5601a89722e3774dd2` |
| Huobi Token | `0x777850281719d5a96c29812ab72f822e0e09f3da` |
| Fantom | `0x56ee926bd8c72b2d5fa1af4d9e4cbb515a1e3adc` |
| Base | `0x22e6966b799c4d5b13be962e1d117b56327fda66` |
| Near Protocol | `c011a73ee8576fb46f5e1c5751ca3b9fe0af2a6f.factory.bridge.near` |
| Energi | `0xa255461ff545d6ece153283f421d67d2de5d0e29` |
| Polygon Pos | `0x50b728d8d964fd00c2d0aad81718b71311fef68a` |
| Optimistic Ethereum | `0x8700daec35af8ff88c16bdf0418774cb3d7599b4` |
| Avalanche | `0xbec243c995409e6520d7c41e404da5deba4b209b` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | SNX/USDT | N/A |
| Kraken | SNX/USD | N/A |
| Bitget | SNX/USDT | N/A |
| KuCoin | SNX/USDT | N/A |
| Crypto.com Exchange | SNX/USDT | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V2 (Ethereum) | 0XC011A73EE8576FB46F5E1C5751CA3B9FE0AF2A6F/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |
| Uniswap V3 (Ethereum) | 0XC011A73EE8576FB46F5E1C5751CA3B9FE0AF2A6F/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |
| Balancer V2 | 0XC011A73EE8576FB46F5E1C5751CA3B9FE0AF2A6F/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.synthetix.io/](https://www.synthetix.io/) |
| **Twitter** | [@synthetix](https://twitter.com/synthetix) |
| **Reddit** | [https://www.reddit.com/r/synthetix_io/](https://www.reddit.com/r/synthetix_io/) |
| **Discord** | [https://discord.com/invite/synthetix](https://discord.com/invite/synthetix) |
| **GitHub** | [https://github.com/Synthetixio/synthetix](https://github.com/Synthetixio/synthetix) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $13.92M |
| **Market Cap Rank** | #216 |
| **24h Range** | $0.2254 — $0.2352 |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---
