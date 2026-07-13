---
title: "crvUSD"
type: entity
created: 2026-04-09
updated: 2026-06-21
status: excellent
tags: [crypto, defi]
aliases: ["CRVUSD", "Curve USD", "Savings crvUSD", "scrvUSD"]
entity_type: protocol
founded: 2023
headquarters: "Decentralized"
website: "https://curve.finance"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[curve-finance]]", "[[stablecoins]]", "[[liquidation]]"]
---

# crvUSD

**crvUSD** is the decentralized, crypto-collateralized (CDP) stablecoin of [[curve-finance]], created by Curve founder Michael Egorov and launched in May 2023. Its distinguishing feature is **LLAMMA** (Lending-Liquidating AMM Algorithm), which replaces hard liquidations with continuous *soft liquidation* across price bands — making it the reference design traders study for liquidation-cascade-resistant lending, and a core yield instrument via the **scrvUSD** savings vault.

---

## Market Data

| Field | Detail |
|---|---|
| **Ticker** | crvUSD (ERC-20 on [[ethereum]]; bridged to Arbitrum, Optimism, Base, BNB Chain, Polygon, Gnosis, Fraxtal, Taiko) |
| **Type** | Crypto-backed CDP [[stablecoin]], USD peg, overcollateralized (collateral: WBTC, WETH, wstETH, sfrxETH, tBTC, etc.) |
| **Market Cap Rank** | #172 |
| **Market Cap / Supply** | $207.64M / ~207.88M crvUSD |
| **Current Price** | $0.998957 (effectively pegged at $1.00) |
| **24h Volume** | $6.98M |
| **24h Change** | -0.01% |
| **7d Change** | -0.03% |
| **All-Time High** | $1.11 (2024-06-13) |
| **All-Time Low** | $0.949016 (2023-08-08) |
| **Peg mechanism** | LLAMMA soft liquidations + PegKeepers (algorithmic mint/absorb vs major stablecoin pools) + dynamic borrow rates |
| **Yield wrapper** | scrvUSD (Savings crvUSD) — ERC-4626 vault paying a share of borrower interest |
| **Launched** | May 2023 |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

As a USD-pegged stablecoin crvUSD is not a directional bet — it held the peg tightly (~$0.999, ±0.03% on the week) even as the broader market sat in **extreme fear (Fear & Greed = 23)** within an **Established Bear Market** regime. The flat-to-down read on supply (~$208M circulating, off the ~$290M+ levels reported earlier in 2026) reflects the bear-market contraction in on-chain leverage demand: crvUSD is minted against borrowing, so its float shrinks when traders deleverage. Because every crvUSD is overcollateralized and minted on demand, **MC = FDV** by construction (no unvested overhang) — the relevant "dilution" question is collateral quality and PegKeeper debt, not token unlocks.

---

## Overview

crvUSD is minted by depositing volatile collateral into Curve's lending markets. Unlike MakerDAO/Sky-style vaults that liquidate a position in one shot when health drops below a threshold, crvUSD's **LLAMMA** spreads each position's collateral across a range of price bands. As price falls through the bands, collateral is *gradually* converted to crvUSD (and converted back if price recovers). Borrowers in "soft liquidation" bleed small rebalancing losses instead of suffering a single catastrophic liquidation; the system avoids dumping large collateral blocks into thin markets.

Peg stability is maintained by **PegKeepers** — contracts that mint uncollateralized crvUSD into Curve stablecoin pools when crvUSD trades above $1 and withdraw/burn when below — plus a monetary-policy rate that rises when the peg is soft to incentivize debt repayment.

### scrvUSD (Savings crvUSD)

Launched by CurveDAO (in partnership with Yearn Finance, on Yearn V3 vaults) in November 2024, scrvUSD passes a DAO-set share of crvUSD borrower interest to stakers — minimum 5%, maximum 50% of protocol revenue. In its first six months it delivered roughly 3.8% total yield to depositors, and by 2026 scrvUSD typically holds **20–30% of circulating crvUSD**, fluctuating with the prevailing savings APR. This gives crvUSD a native "risk-free rate" analogous to Sky's sUSDS/DSR.

### 2025–2026 developments

- **May 2025**: crvUSD supply reached a then-all-time high of ~$181M ("crvUSD: 2 Years On", Curve News, May 2025); growth continued into 2026 with supply roughly doubling to ~$290M+ by June 2026.
- **2025**: Egorov launched **Yield Basis**, a new protocol built around crvUSD/CRV designed to capture BTC/ETH AMM yield while mitigating impermanent loss — adding a new structural demand sink for crvUSD (details still maturing; treat early APY claims with caution).
- Continued multichain expansion (Base-native deployment, Fraxtal, Taiko).

---

## Trading Relevance

- **Not a directional asset** — crvUSD trades $0.995–$1.005 in normal conditions. Relevance to traders:
  1. **Yield leg**: scrvUSD as the carry leg in delta-neutral structures; its rate tracks crvUSD borrow demand, so it rises in leverage-hungry bull phases.
  2. **Peg monitoring as a risk signal**: a sustained crvUSD discount signals stress in Curve's lending markets or collateral (echoes of the June 2024 CRV/Egorov liquidation episode, which crvUSD's LLAMMA design weathered without bad-debt spirals on its own markets).
  3. **DeFi-health barometer**: crvUSD supply growth is a clean read on on-chain leverage appetite; the PegKeeper debt level is a public dashboard metric worth watching for [[stablecoins]] stress.
  4. **Where it trades**: almost entirely on-chain — Curve pools (crvUSD/USDC, crvUSD/USDT, etc.) and Uniswap v3; no meaningful CEX listings. Execution at size means routing through Curve.
- **Key risks**: smart-contract risk across many deployed markets; oracle manipulation of LLAMMA bands; governance risk (CRV-weighted DAO); competition from larger decentralized stables (Sky/USDS, Ethena's USDe).

---

## Tokenomics & Supply

crvUSD has **no fixed supply and no max supply** — every unit is minted when a borrower opens a CDP against accepted collateral and burned when debt is repaid or PegKeepers absorb excess. Consequently **market cap equals fully-diluted valuation** (MC/FDV = 1.00): there is no team allocation, VC vesting, or emission schedule to dilute holders, unlike a typical governance token such as [[curve-dao-token|CRV]]. The economically meaningful supply metrics are instead:

| Metric | Value / Note |
|---|---|
| **Circulating = Total supply** | ~207.88M crvUSD (1:1 with outstanding debt) |
| **Max supply** | None (mint/burn against collateral; capped only by per-market debt ceilings) |
| **scrvUSD share** | ~20–30% of float typically wrapped into the savings vault |
| **PegKeeper debt** | Public dashboard metric — the algorithmic stabilizer's net minted balance; a key risk gauge |

Because dilution is collateral-driven rather than schedule-driven, the watch-items are **collateral concentration** (how much float is backed by volatile assets like WETH/WBTC vs. LSTs) and **PegKeeper debt levels** (high balances mean the algorithm is working hard to defend the peg).

---

## Peer Comparison

| Stablecoin | Model | Backing | MC/FDV | Native yield wrapper | Notes |
|---|---|---|---|---|---|
| **crvUSD** | CDP / LLAMMA soft-liq | Volatile crypto (WBTC, WETH, LSTs) | 1.00 | scrvUSD | Liquidation-cascade-resistant by design |
| [[dai|DAI]] / USDS (Sky) | CDP + RWA | Crypto + [[real-world-assets]] | n/a | sUSDS / DSR | Largest decentralized stable; hard liquidations |
| [[ethena|USDe]] (Ethena) | Synthetic / basis carry | Perp short + spot | n/a | sUSDe | Yield from funding, not borrow interest |
| [[frax|FRAX]] | Hybrid (now fully collateralized) | Crypto + RWA | n/a | sFRAX | Historically fractional-algorithmic |
| GHO (Aave) | CDP | Crypto on [[aave]] | n/a | stkGHO | Aave-native borrow stable |

crvUSD's differentiator is **LLAMMA's continuous soft liquidation**, which trades small ongoing rebalancing losses for protection against the single-shot liquidation cascades that have repeatedly stressed hard-liquidation CDP stables.

---

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xf939e0a03fb07f59a73314e73794be0e57ac1b4e` |
| Arbitrum One | `0x498bf2b1e120fed3ad3d42ea2165e9b73f99c1e5` |
| Optimism | `0xc52d7f23a2e460248db6ee192cb23dd12bddcbf6` |
| Base | `0x417ac0e078398c154edfadd9ef675d30be60af93` |
| BNB Chain | `0xe2fb3f127f5450dee44afe054385d74c392bdef4` |
| Polygon PoS | `0xc4ce1d6f5d98d65ee25cf85e9f2e9dcfee6cb5d6` |
| Gnosis (xDai) | `0xabef652195f98a91e490f047a5006b71c85f058d` |
| Fraxtal | `0xb102f7efa0d5de071a8d37b3548e1c7cb148caf3` |
| Taiko | `0xc8f4518ed4bab9a972808a493107926ce8237068` |

### Social

| Platform | Link |
|---|---|
| **Twitter** | [@curvefinance](https://twitter.com/curvefinance) |
| **GitHub** | [curvefi](https://github.com/curvefi/curve-contract) |
| **Docs** | [https://resources.curve.finance/crvusd/](https://resources.curve.finance/crvusd/) |

---

## Related

- [[curve-finance]]
- [[stablecoins]]
- [[ethereum]]
- [[crypto-markets]]
- [[liquidation]]
- [[defi-yield-farming]]
- [[makerdao]]

---

## Sources

- CoinGecko / cryptodataapi.com top-1000 snapshot, 2026-06-21 (rank #172, $207.64M mcap, $0.998957) (Source: [[coingecko-top-1000-2026-04-09]])
- CoinGecko, crvUSD page snapshot 2026-04-09 (Source: [[coingecko-top-1000-2026-04-09]])
- Curve Resources — scrvUSD: https://resources.curve.finance/crvusd/scrvusd/ (5% min / 50% max revenue share)
- Curve News — "Introducing Savings crvUSD": https://news.curve.finance/introducing-scrvusd/
- Curve News — "crvUSD: 2 Years On" (May 2025, ~$181M supply ATH): https://news.curve.finance/crvusd-2-years-on/
- CoinGecko — crvUSD: https://www.coingecko.com/en/coins/crvusd (supply ~293M, retrieved 2026-06-10)
- DefiLlama — crvUSD stablecoin page: https://defillama.com/stablecoin/crvusd
- Perplexity verification, 2026-06-10 (LLAMMA mechanics confirmed; supply figures cross-checked across CoinGecko/CryptoRank, ~$290–370M range)
