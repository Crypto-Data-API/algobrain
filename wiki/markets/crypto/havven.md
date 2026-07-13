---
title: "Synthetix"
type: entity
created: 2026-04-09
updated: 2026-06-20
status: good
tags: [crypto, defi, derivatives]
aliases: ["SNX", "Havven"]
entity_type: protocol
founded: 2018
headquarters: "Decentralized"
website: "https://www.synthetix.io/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[hyperliquid]]", "[[decentralized-exchange]]", "[[perpetual-futures]]", "[[funding-rate]]"]
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
