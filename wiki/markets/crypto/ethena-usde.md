---
title: "Ethena USDe"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, stablecoins]
aliases: ["Ethena", "USDE", "USDe", "sUSDe"]
entity_type: protocol
founded: 2023
headquarters: "Decentralized"
website: "https://app.ethena.fi/"
related: ["[[aave]]", "[[binance]]", "[[bitcoin]]", "[[carry-trade]]", "[[crypto-markets]]", "[[ethena]]", "[[ethereum]]", "[[funding-rates]]", "[[hyperliquid]]", "[[stablecoin]]", "[[stablecoin-depeg-profit-capture]]", "[[stablecoin-yield]]"]
---

# Ethena USDe

**Ethena USDe** (USDe) is a **"synthetic dollar"** — not a fiat-backed [[stablecoin]] but a **delta-neutral** position: [[ethena|Ethena]] holds staked ETH/BTC/SOL collateral and shorts an equal notional in perpetual futures, capturing staking yield plus perp funding rates and passing it to holders of staked USDe (sUSDe). For traders, USDe is effectively the tokenized crypto [[carry-trade|carry trade]] — its supply is a real-time gauge of how crowded the basis/funding trade is, and its growth/contraction cycles move [[funding-rates|funding rates]] across the entire perp market.

---

## Market Data

| Field | Value |
|---|---|
| **Market Cap Rank** | #23 |
| **Market Cap** | $4.50B |
| **Current Price** | $0.9990 |
| **24h Volume** | $47.11M |
| **24h Change** | -0.002% |
| **7d Change** | -0.06% |
| **Circulating Supply** | 4.504B USDe |
| **Total Supply** | 4.504B USDe |
| **Max Supply** | Unlimited (elastic mint/redeem) |
| **All-Time High** | $1.034 (2025-12-09) |
| **All-Time Low** | $0.9295 (2024-10-04) |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

USDe sits at **rank #23 (~$4.50B)**, holding its $1 soft peg tightly ($0.999, within a few basis points) as a pegged asset should — for a synthetic dollar, *deviations from $1 are the signal, not the price level*. The ~$4.5B supply confirms the continued contraction from the **~$14B peak in late 2025** (see 2025–2026 Developments). The broad market is risk-off — [[fear-and-greed-index|Fear & Greed]] = 23 ("extreme fear"), "Established Bear Market" regime as of 2026-06-20 — a backdrop that suppresses perp funding and therefore USDe's native yield, reinforcing the redemption cycle that shrank supply through 2026.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | USDe (governance token: ENA) |
| **Market Cap / Supply** | ~$4.50B (2026-06-20 snapshot) — down from ~$14B peak in late 2025 |
| **Rank** | #23 overall; ~4th–5th largest stablecoin at peak |
| **Peg** | $1.00 soft peg via delta-neutral hedge (not fiat reserves) |
| **Sector** | Synthetic dollar / yield-bearing stablecoin / basis trade |
| **Chain** | Ethereum-native, deployed on 25+ chains (Solana, Base, Arbitrum, TON, HyperEVM, etc.) |
| **Yield (sUSDe)** | ~3.7% as of early 2026; ranged ~4–15% during 2025 |
| **Issuer** | Ethena Labs (founder: Guy Young) |
| **Website** | [https://app.ethena.fi/](https://app.ethena.fi/) |

---

## Overview

Ethena is a delta-hedged synthetic dollar with native crypto yield derived from staking and perpetual funding rates. Minting USDe: a whitelisted market maker deposits collateral (stETH, BTC, SOL, liquid stables); Ethena simultaneously shorts perps of equal notional on CEXs and [[hyperliquid]], holding collateral with off-exchange custodians. The position is delta-neutral: collateral price moves are offset by the short. Revenue = staking yield + funding payments received on the short leg (funding is positive most of the time because crypto perps trade long-biased). That revenue flows to sUSDe stakers.

The structural risk is the inverse: in prolonged negative-funding regimes Ethena pays funding rather than earning it, eroding the reserve fund and incentivizing redemptions — which is exactly what played out in late 2025.

---

## 2025–2026 Developments

- **Supply peak (2025)** — USDe surged past **$14B**, nearly 5% of the total stablecoin market, becoming the fastest-growing dollar asset in crypto. Growth was turbocharged by the [[aave]]–Pendle looping trade (deposit sUSDe/PT tokens, borrow stables, re-mint USDe).
- **GENIUS Act tailwind (July 2025)** — the US stablecoin law prohibited regulated issuers from paying yield on stablecoins, giving USDe's offshore, unregulated yield model a competitive moat against USDC/USDT — but also keeping it outside the regulated perimeter (no iUSDe-style institutional wrapper had fully launched as of mid-2026; iUSDe remains the planned regulated product).
- **October 2025 deleveraging event** — the crypto-wide liquidation cascade of October 2025 flipped funding negative and triggered an unwind of the Aave–Pendle loop. USDe supply collapsed from $14B+ to ~$8.5B within weeks.
- **Continued contraction into 2026** — supply kept bleeding: ~$5.9B by mid-March 2026 and roughly **$4.5B by June 2026 (approximate)**. sUSDe yield compressed to ~3.7% (vs 4–15% range in 2025) as funding stayed muted. Notably, sUSDe DEX liquidity hit an ATH of ~$248M in November 2025 even as supply halved — exit liquidity deepened.
- ENA (the governance token) sold off with supply contraction; protocol revenue at peak ran at ~$50M+/month, falling materially in 2026.

---

## Trading Relevance

- **Funding-rate barometer**: USDe supply growth ≈ aggregate appetite for the long-perp carry. Expanding supply compresses positive funding (Ethena is the marginal short); contracting supply removes short pressure. Watch supply via DefiLlama as an input to [[funding-rates]]-based strategies on [[hyperliquid]] and Binance.
- **sUSDe carry trade**: holding sUSDe is a tokenized basis trade. Compare sUSDe yield vs T-bill yield: when the spread goes negative (as in early 2026), rotation out of USDe is mechanical.
- **Depeg/stress monitoring**: USDe traded to $0.9295 in the October 2024 stress and wobbled again in October 2025. Key risk indicators: reserve fund size vs supply, negative funding persistence, Aave sUSDe utilization, redemption queue. A forced unwind is the tail risk that would hit ETH/BTC spot via collateral sales and squeeze perp shorts.
- **Loop-unwind contagion**: the Aave–Pendle–Ethena loop is the canonical example of reflexive stablecoin leverage; its 2025 unwind is a case study for spotting crowded on-chain carry.
- **Where it trades**: deep spot pairs on Binance, Bitget, KuCoin, Kraken (USDE/EUR), Curve and Uniswap pools; ENA perps everywhere. USDe itself is the collateral asset on several perp DEXs.

---

## Tokenomics & Supply

> *Refreshed from the 2026-06-20 snapshot. Supply is elastic (mint/redeem); see 2025–2026 Developments for trajectory.*

| Metric | Value |
|---|---|
| **Circulating Supply** | 4.504B USDe |
| **Total Supply** | 4.504B USDe |
| **Max Supply** | Unlimited (elastic) |
| **Fully Diluted Valuation** | ~$4.50B |
| **Market Cap / FDV Ratio** | 1.00 |

Unlike a fixed-supply token, USDe has **no max supply and no dilution schedule** — circulating ≡ total ≡ FDV because every unit is created by a 1:1 mint against collateral and destroyed on redemption. The "dilution" risk is inverted relative to a normal token: supply *contracting* (as in 2026) is the bearish signal, because it means the carry trade is unwinding and yield is compressing. Supply is therefore best read as a real-time leverage gauge, not a cap-table.

---

## Price History

> *Refreshed from the 2026-06-20 snapshot. As a pegged asset, deviations from $1 are the signal.*

| Metric | Value |
|---|---|
| **All-Time High** | $1.034 (2025-12-09) |
| **All-Time Low** | $0.9295 (2024-10-04) |
| **24h Change** | -0.002% |
| **7d Change** | -0.06% |
| **Current price** | $0.999 (holding peg) |

The two ATL/ATH extremes bracket the peg: the $0.9295 low (Oct 2024) and a brief $0.929 wobble in Oct 2025 are the historical depeg-stress markers, while the $1.034 high reflects transient redemption-premium / DEX-pool imbalance rather than a sustained departure from $1.

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x4c9edd5852cd905f086c759e8383e09bff1e68b3` |
| Plasma | `0x5d3a1ff2b6bab83b63cd9ad0787074081a52ef34` |
| Zircuit | `0x5d3a1ff2b6bab83b63cd9ad0787074081a52ef34` |
| Metis Andromeda | `0x5d3a1ff2b6bab83b63cd9ad0787074081a52ef34` |
| Morph L2 | `0x5d3a1ff2b6bab83b63cd9ad0787074081a52ef34` |
| Swellchain | `0x5d3a1ff2b6bab83b63cd9ad0787074081a52ef34` |
| Kava | `0x5d3a1ff2b6bab83b63cd9ad0787074081a52ef34` |
| Berachain | `0x5d3a1ff2b6bab83b63cd9ad0787074081a52ef34` |
| Linea | `0x5d3a1ff2b6bab83b63cd9ad0787074081a52ef34` |
| Scroll | `0x5d3a1ff2b6bab83b63cd9ad0787074081a52ef34` |
| X Layer | `0x5d3a1ff2b6bab83b63cd9ad0787074081a52ef34` |
| Binance Smart Chain | `0x5d3a1ff2b6bab83b63cd9ad0787074081a52ef34` |
| Hyperevm | `0x5d3a1ff2b6bab83b63cd9ad0787074081a52ef34` |
| Mode | `0x5d3a1ff2b6bab83b63cd9ad0787074081a52ef34` |
| Fraxtal | `0x5d3a1ff2b6bab83b63cd9ad0787074081a52ef34` |
| Mantle | `0x5d3a1ff2b6bab83b63cd9ad0787074081a52ef34` |
| The Open Network | `EQAIb6KmdfdDR7CN1GBqVJuP25iCnLKCvBlJ07Evuu2dzP5f` |
| Hyperliquid | `0x2e6d84f2d7ca82e6581e03523e4389f7` |
| Aptos | `0xf37a8864fe737eb8ec2c2931047047cbaed1beed3fb0e5b7c5526dafd3b9c2e9` |
| Solana | `DEkqHyPN7GMRJ5cArtQFAWefqbZb33Hyf6s5iCwjEonT` |
| Base | `0x5d3a1ff2b6bab83b63cd9ad0787074081a52ef34` |
| Avalanche | `0x5d3a1ff2b6bab83b63cd9ad0787074081a52ef34` |
| Zksync | `0x39fe7a0dacce31bd90418e3e659fb0b5f0b3db0d` |
| Manta Pacific | `0x5d3a1ff2b6bab83b63cd9ad0787074081a52ef34` |
| Blast | `0x5d3a1ff2b6bab83b63cd9ad0787074081a52ef34` |
| Optimistic Ethereum | `0x5d3a1ff2b6bab83b63cd9ad0787074081a52ef34` |
| Arbitrum One | `0x5d3a1ff2b6bab83b63cd9ad0787074081a52ef34` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | USDE/USDT | N/A |
| Kraken | USDE/EUR | N/A |
| Bitget | BTC/USDE | N/A |
| KuCoin | USDE/USDT | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | USDe/USDC | Spot |
| Curve (Ethereum) | USDe pools | Spot (deepest stable liquidity) |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://app.ethena.fi/](https://app.ethena.fi/) |
| **Twitter** | [@ethena_labs](https://twitter.com/ethena_labs) |
| **Whitepaper** | [https://ethena-labs.gitbook.io/](https://ethena-labs.gitbook.io/) |

---

## Trading Characteristics

> *Refreshed from the 2026-06-20 snapshot.*

| Characteristic | Detail |
|---|---|
| **24h Volume** | $47.11M |
| **Market Cap Rank** | #23 |
| **Price** | $0.999 (tight to peg) |
| **24h / 7d** | -0.002% / -0.06% |

The ~$47M/24h figure is USDe *spot* turnover; the asset's economically important "volume" is mint/redeem flow and its role as collateral on perp DEXs, not exchange trading. A pegged synthetic dollar should show near-zero price volatility — the relevant tape to watch is supply (DefiLlama) and the sUSDe yield, not the spot chart.

---

## Peer Comparison

| Stablecoin | Backing model | Yield to holders | ~Rank | Key risk |
|---|---|---|---|---|
| **USDe** | Delta-neutral (staked collateral + perp short) | Yes, via sUSDe (funding-driven) | #23 | Negative-funding regimes; exchange/custody counterparty |
| [[tether\|USDT]] | Fiat + reserves (offshore) | No (banned under GENIUS Act for regulated issuers) | top 3 | Reserve transparency, regulatory |
| [[usd-coin\|USDC]] | Fiat + reserves (regulated, US) | No | top 6 | Banking exposure (e.g. 2023 SVB depeg) |
| DAI / USDS | Crypto-overcollateralized (MakerDAO/Sky) | Via savings rate | mid | Collateral volatility, governance |

USDe is the largest **yield-bearing synthetic dollar** and structurally distinct from the fiat-backed giants: its yield comes from a real (if cyclical) source — perp funding plus staking — rather than from passing through T-bill interest. The [[carry-trade|carry-trade]] nature is both its edge (native, regulation-resistant yield) and its core fragility (the yield can go negative). Compared to overcollateralized DAI, USDe is more capital-efficient (1:1, not over-collateralized) but carries CEX/custody and funding risk that DAI does not.

---

## Valuation Framing

A pegged asset is not "valued" by price — the analytical questions are about **peg robustness** and **sustainable yield**:

- **Supply trajectory** — the single best gauge. Growth = the long-perp carry is profitable and crowding in; contraction (2026) = funding is muted/negative and the trade is unwinding. From $14B → ~$4.5B is a ~68% supply drawdown that mirrors the funding-rate cycle.
- **Yield spread vs T-bills** — sUSDe yield (~3.7% in early 2026, vs 4–15% in 2025) compared to the risk-free rate. When the spread turns negative, rotation out of USDe is mechanical; this drove much of the 2026 contraction.
- **Reserve-fund coverage** — the reserve fund must cover negative-funding periods without the protocol selling collateral. Reserve size relative to supply is the de-facto solvency buffer.
- **ENA (governance token)** — captures protocol fees and trades as a *levered bet on USDe supply*; it sold off hard with the supply contraction (peak protocol revenue ~$50M+/month fell materially in 2026).

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. Key concentration to monitor: Aave sUSDe/PT collateral and Pendle markets, which drove the 2025 reflexive loop.*

---

## Major News & Events

- 2025-07 — GENIUS Act bans yield on regulated stablecoins, advantaging USDe's offshore model
- 2025 H2 — USDe supply peaks above $14B (~5% of stablecoin market)
- 2025-10 — Crypto deleveraging event; Aave–Pendle loop unwinds; supply falls to ~$8.5B in weeks
- 2026-03 — Supply ~$5.9B; sUSDe yield compressed to ~3.7%
- 2026-06 — Supply ~$4.50B, rank #23 among all crypto assets (2026-06-20 snapshot); peg holding at $0.999

---

## Related

- [[crypto-markets]]
- [[ethereum]] — primary collateral (stETH) and home chain
- [[bitcoin]] — secondary hedge collateral
- [[hyperliquid]] — perp venue used for hedging; HyperEVM USDe deployment
- [[aave]] — center of the 2025 looping trade
- [[funding-rates]] — the revenue engine and the key risk variable
- [[stablecoin]] — synthetic vs fiat-backed dollar context
- [[ethena]] — issuer / ENA governance token
- [[carry-trade]] — the underlying basis/funding trade USDe tokenizes

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data refreshed 2026-06-20 from `raw/data/crypto-loop/coingecko-markets.json` (cryptodataapi.com / CoinGecko snapshot); macro backdrop (Fear & Greed 23, "Established Bear Market") from the crypto-loop digest.
- Stablecoin Insider — "Ethena's USDe Q1 2026 Report": https://stablecoininsider.org/ethena-usde-q1-2026-report/
- CryptoDaily — "Ethena's USDe Supply Drop: Is ENA Losing Its Synthetic-Dollar Momentum?" (May 2026): https://cryptodaily.co.uk/2026/05/ethena-usde-supply-drop-ena-momentum
- Messari — Ethena USDe project page (yield data): https://messari.io/project/ethena-usde
- CoinMarketCap stablecoin rankings (USDe ~$4.49B, June 2026): https://coinmarketcap.com/view/stablecoin/
- Verified via Perplexity sonar + web search, 2026-06-10

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 4.02B USDE |
| **Total Supply** | 4.02B USDE |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $4.02B |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Trading Profile

### Venues & liquidity

USDe is a USD-pegged synthetic dollar traded primarily on Binance (USDE/USDT), with additional spot venues (Kraken USDE/EUR, Bitget, KuCoin) and deep on-chain liquidity via Curve and Uniswap. It is a **peg / cash-management instrument, not a directional asset** — the trade is about peg stability, backing/reserves, depeg risk, and yield/arbitrage, never momentum. Practical implications: leverage is rarely used on the stablecoin leg itself (there is no directional edge in a $1 asset); position sizing is driven by mint/redeem parity, redemption capacity, and available exit liquidity rather than a price target. Binance-centric spot depth plus Curve/Uniswap pools means execution and sizing hinge on which venue offers the tightest deviation from $1.00 at the moment; because economically important flow is mint/redeem rather than exchange turnover, large size is best worked through primary redemption or the deepest stable pools to avoid moving the peg.

### Applicable strategies

- [[stablecoin-depeg-profit-capture]] — USDe has printed genuine depeg stress ($0.9295 in Oct 2024, a wobble in Oct 2025); buying below par and holding to re-peg is the canonical trade when backing is intact.
- [[synthetic-stablecoin-depeg-arbitrage]] — as a delta-neutral synthetic dollar (not fiat-backed), USDe's depegs are driven by funding/collateral stress, so its dislocations require this synthetic-specific arb rather than a naive reserve-backed model.
- [[stablecoin-yield]] — staking into sUSDe captures funding-plus-staking yield; the trade is sizing yield vs T-bills and rotating out mechanically when the spread turns negative.
- [[stablecoin-pair-arbitrage]] — spreads between USDE/USDT on Binance, USDE/EUR on Kraken, and Curve/Uniswap USDe pools open small, capturable dislocations.
- [[mint-parity-arbitrage]] — the 1:1 mint/redeem against collateral anchors USDe to $1.00; deviations between secondary-market price and mint/redeem parity are directly arbitrageable by whitelisted flow.
- [[carry-trade]] — USDe *is* the tokenized crypto carry (staked collateral long + perp short); holding sUSDe expresses the basis/funding carry directly.

### Volatility & regime character

As a pegged synthetic dollar, USDe should show near-zero price volatility — it holds tightly around $1.00 (recently ~$0.999, within a few basis points), and *deviations from $1 are the signal, not the price level*. Historical depeg episodes bracket the peg: an all-time low of $0.9295 (Oct 2024) and a repeat wobble in Oct 2025, versus a transient $1.034 high (Dec 2025) reflecting redemption-premium / pool imbalance. The backing model is delta-neutral (staked ETH/BTC/SOL collateral hedged by an equal-notional perp short) rather than fiat reserves, so peg tightness is a function of funding regimes and reserve-fund coverage. Redemption mechanics are elastic 1:1 mint/redeem against collateral, which is the mechanism that pulls price back to par — but prolonged negative funding erodes the reserve and incentivizes the supply contraction seen through 2026.

### Risk flags

- **Depeg risk** — real, not theoretical: negative-funding regimes force the protocol to pay rather than earn, stressing the peg (see the Oct 2024 / Oct 2025 wobbles).
- **Reserve / backing transparency** — solvency depends on reserve-fund size relative to supply and on off-exchange custody of collateral; opacity here is the core credit risk.
- **Redemption gating** — mint/redeem is whitelisted market-maker flow; a stressed unwind can back up the redemption queue, widening secondary-market discounts before parity restores.
- **Regulatory** — USDe's yield model is offshore/unregulated (advantaged by, but outside, the GENIUS Act perimeter); a regulatory clampdown on yield-bearing stablecoins is a tail risk.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for peg monitoring (auth via `X-API-Key`). Watch for depeg events.

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=USDEUSDT` — current price (peg deviation vs 1.00)
- `GET /api/v1/market-data/ticker/24hr?symbol=USDEUSDT` — 24h range (intraday peg stress)

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=USDEUSDT&interval=1h&limit=1000` — peg history / past depegs
- `GET /api/v1/backtesting/klines` — deep archive for depeg backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/ticker/price?symbol=USDEUSDT"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---
