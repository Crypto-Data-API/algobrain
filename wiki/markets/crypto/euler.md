---
title: "Euler"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, ethereum, lending, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, altcoins]
aliases: ["EUL", "Euler Finance", "Euler v2"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.euler.finance/"
related: ["[[aave]]", "[[compound]]", "[[crypto-markets]]", "[[defi]]", "[[ethereum]]", "[[flash-loan]]", "[[governance-token]]", "[[lending]]", "[[smart-contract-risk]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[funding-rate-harvest]]", "[[cash-and-carry]]"]
---

# Euler

**Euler Finance** ([[eul|EUL]]) is a permissionless [[lending]] and borrowing protocol built on [[ethereum]] and deployed across many EVM chains. Its defining feature is **permissionless market creation** — anyone can list a market for almost any [[erc-20]] token using risk parameters derived from on-chain liquidity, rather than relying on the manually curated, governance-gated asset lists used by first-generation lenders like [[aave]] and [[compound]]. Euler is best known both for that technical ambition and for surviving one of the largest [[flash-loan]] exploits in [[defi]] history — a ~$197M hack in March 2023 — after which essentially all of the stolen funds were returned and the protocol relaunched as **Euler v2**.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

As of 2026-06-22, EUL trades at **$1.076**, ranked **#707** by market capitalization with a market cap of **$25,940,278**. The token was up modestly over the prior day (**+1.19%** 24h) and was a relative outperformer over the week (**+5.51%** 7d) against a weak bear-market backdrop (BTC ~$64,508; Fear & Greed Index 21, "Extreme Fear"). EUL remains far below its 2025 all-time high.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | EUL |
| **Market Cap Rank** | #707 |
| **Market Cap** | $25,940,278 |
| **Current Price** | $1.076 |
| **24h Change** | +1.19% |
| **7d Change** | +5.51% |
| **Categories** | Lending/Borrowing Protocols, Ethereum Ecosystem, BNB Chain Ecosystem, Avalanche Ecosystem, Arbitrum Ecosystem, Base Ecosystem, Berachain Ecosystem, Paradigm Portfolio, Coinbase Ventures Portfolio, Sonic Ecosystem, Swellchain Ecosystem, Unichain Ecosystem, TAC Ecosystem, Plasma Ecosystem, BOB Network Ecosystem |
| **Website** | [https://www.euler.finance/](https://www.euler.finance/) |
> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

---

## Overview

In [[defi|decentralized finance]], trusted and permissioned third-parties are replaced by trustless, permissionless [[lending]] protocols running on the blockchain. Among the first generation of DeFi lenders are [[compound]] and [[aave]], which provide lending and borrowing for a handful of the most liquid [[erc-20]] tokens. However, those protocols were not designed to handle the risks of lending and borrowing illiquid or volatile assets, and therefore relied on a permissioned, governance-gated listing system.

Euler was built to serve the unmet demand for lending and borrowing the **long tail** of crypto assets. Depositors earn yield and can take leveraged long positions; borrowers reduce volatility exposure and can take leveraged short positions. To do this safely without a centralized listing committee, Euler combined several innovations (notably in its v1 design): permissionless market creation, **risk-based asset tiers** (collateral / cross / isolated) to contain contagion from risky tokens, time-weighted-average-price ([[twap]]) oracles, and a soft/Dutch-auction liquidation engine designed to reduce liquidator MEV.

Euler is backed by notable investors including Paradigm and Coinbase Ventures.

---

## Mechanism & Architecture

Euler's core proposition is **permissionless, modular lending**. Rather than a fixed set of pooled markets, Euler lets anyone deploy a lending market ("vault") for an asset, isolating risk so that a bad listing cannot endanger the whole protocol.

Key mechanisms across Euler's design:

- **Asset tiers / isolation** — assets are classified by risk so that exotic or illiquid tokens are quarantined from blue-chip collateral, limiting cross-contamination.
- **Risk-adjusted parameters** — borrow/collateral factors set per market based on liquidity and volatility.
- **Oracle design** — reliance on on-chain price feeds (including TWAP and external oracles) to value collateral.
- **Liquidation engine** — a soft-liquidation / Dutch-auction model intended to be fairer and less MEV-extractive than fixed-discount liquidations.

**Euler v2 (relaunched 2024)** generalizes this further with the **Euler Vault Kit (EVK)** and **Ethereum Vault Connector (EVC)** — a framework that turns lending into composable, permissionlessly created vaults that can be linked into custom credit markets. This modular "lending-as-a-toolkit" approach is Euler's principal differentiator in the post-hack era.

### Euler v2 building blocks

- **Euler Vault Kit (EVK)** — an open-source toolkit for deploying ERC-4626-style lending vaults with configurable parameters (oracle, interest-rate model, collateral/borrow factors, caps, governance/ownership). A vault can be *governed* (a manager can tune parameters) or *ungoverned/finalized* (immutable), letting builders choose between flexibility and trust-minimization.
- **Ethereum Vault Connector (EVC)** — the shared "operating system" that lets vaults recognize each other as collateral and lets a single account hold positions across many vaults under one unified health check. The EVC enables cross-vault collateralization, batched/deferred liquidity checks, and operator permissions — turning isolated vaults into composable credit networks.
- **Curated vs. permissionless markets** — anyone can spin up a vault, but in practice most user deposits flow into **curated clusters** (e.g., risk-managed vault sets run by professional risk teams), giving users a choice between vetted, conservatively parameterized markets and the full permissionless long tail.

### Worked illustration: leveraged staking-yield trade

A user wanting leveraged exposure to ETH staking yield could: (1) deposit wstETH ([[liquid-staking|liquid-staking]] ETH) as collateral into an Euler vault, (2) borrow WETH against it, (3) swap the WETH for more wstETH, (4) redeposit, and repeat. If wstETH yields ~3% and the WETH borrow cost is ~2%, each loop earns the ~1% spread on borrowed capital — at, say, 3x leverage the net staking yield is amplified, but a drop in the wstETH/ETH ratio or a borrow-rate spike can trigger liquidation. Euler's EVC makes this loop a single batched transaction with one health check rather than many separate calls. This is a representative DeFi "looping" strategy, not advice; it concentrates [[smart-contract-risk]], oracle risk, and liquidation risk.

---

## Token Role (EUL)

EUL is Euler's [[governance-token]]. Its primary function is governance of the Euler protocol — voting on parameters, market/vault standards, treasury, and upgrades through the Euler DAO. Holders can delegate and vote on proposals that shape risk frameworks and incentive programs. Circulating supply is a large fraction of total supply, with a market-cap/FDV ratio near 0.9, leaving some remaining emission/unlock overhang.

**Value-accrual question:** like most pure governance tokens, EUL's link to protocol cash flows is indirect — fees are generated by lending spreads and originate at the vault level, and whether (and how) those route to EUL holders is a DAO decision. The bull case is that as Euler v2 adoption and TVL grow, the DAO turns on fee capture (e.g., a protocol fee switch directed to a treasury or to EUL stakers); the bear case is that governance-token value remains decoupled from usage. EUL was used to bootstrap the post-hack relaunch (reimbursement, incentives), and ongoing emissions/incentive programs are a recurring governance topic.

---

## History & Notable Events

- **2021–2022** — Euler v1 launches on Ethereum as a permissionless lending protocol, growing to substantial TVL and becoming one of the more technically respected DeFi lenders.
- **13 March 2023 — the Euler hack.** An attacker exploited a flaw in Euler v1's `donateToReserves` function combined with a missing health check, using a [[flash-loan]] to drain roughly **$197M** in assets ([[dai]], [[ethereum|stETH/WETH]], [[usdc]], wBTC). It was one of the largest DeFi exploits ever and briefly threatened the protocol's solvency.
- **March–April 2023 — funds returned.** After on-chain negotiation, public appeals, and an offered bounty, the attacker **returned essentially all of the recoverable funds** over the following weeks — an unusual and closely watched outcome that allowed Euler to make users whole. Euler subsequently ran a reimbursement process for affected depositors.
- **2024 — Euler v2 relaunch.** Euler returned to production with a rebuilt, heavily audited architecture centered on the **Euler Vault Kit (EVK)** and **Ethereum Vault Connector (EVC)**, pivoting from a single monolithic protocol to a modular lending framework.
- **2024–2026** — Multi-chain expansion across many EVM ecosystems (Arbitrum, Base, BNB Chain, Avalanche, Berachain, Sonic, Unichain, and others).

The hack-and-full-recovery episode is central to Euler's identity: it is simultaneously a cautionary tale about the danger of complex DeFi lending code and a rare example of nearly complete restitution.

---

## Competitive Position

Euler competes in DeFi lending against incumbents [[aave]] and [[compound]], and against modular/isolated-lending peers such as Morpho and Fraxlend. Euler's edge is its **permissionless, modular vault framework** (v2), which targets builders who want to spin up custom credit markets rather than fit into a curated pool. Its disadvantages are a smaller TVL and user base than Aave, and the lingering reputational shadow of the 2023 exploit — partially offset by the goodwill generated by the full return of funds.

| Protocol | Architecture | Listing model | Differentiator | Relative scale |
|---|---|---|---|---|
| **Euler v2** | Modular vaults (EVK) linked by the EVC | **Permissionless** vaults; curated clusters on top | Lending-as-a-toolkit; cross-vault collateral | Mid-tier (smaller than Aave) |
| [[aave\|Aave]] | Pooled, multi-asset, isolation mode | Governance-gated listings | Deepest liquidity, blue-chip brand, GHO stablecoin | Largest |
| [[compound\|Compound]] | Pooled (v2) / isolated "Comet" markets (v3) | Governance-gated | First-mover; simple, conservative | Large but shrinking share |
| Morpho | Minimal immutable primitive + curated vaults (MetaMorpho) | Permissionless markets, curated vaults | Singleton, immutable core; risk curators | Fast-growing |
| Fraxlend | Isolated lending pairs | Permissionless pairs | Tight integration with the [[frax-share\|Frax]] stack | Niche |

Euler and Morpho occupy the same conceptual frontier — minimal, permissionless lending primitives with a layer of professional risk-curation on top — competing for the builders and risk teams who would rather construct bespoke markets than accept Aave's one-size-fits-all pools.

---

## Risks

- **Smart-contract / exploit risk** — Euler has a demonstrated history of a catastrophic exploit (2023). The v2 codebase is more modular and audited, but complexity and permissionless market creation expand the attack surface.
- **Oracle and liquidation risk** — like all on-chain lenders, vulnerable to oracle manipulation and to liquidation cascades in volatile markets.
- **Permissionless-listing risk** — the same flexibility that enables long-tail markets can create thin, manipulable, or mis-parameterized vaults; risk isolation mitigates but does not eliminate this.
- **Microcap token risk** — at a ~$25M market cap, EUL is small and volatile; price can move sharply on low volume.
- **Governance/treasury risk** — value accrual to EUL depends on DAO decisions and on Euler v2 adoption.

This is not investment advice; figures are point-in-time and crypto assets are highly volatile.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 24.14M EUL |
| **Total Supply** | 27.18M EUL |
| **Max Supply** | 27.18M EUL |
| **Fully Diluted Valuation** | $26.85M |
| **Market Cap / FDV Ratio** | 0.89 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $15.81 (2025-07-11) |
| **Current vs ATH** | -93.75% |
| **All-Time Low** | $0.7233 (2026-03-29) |
| **Current vs ATL** | +36.75% |
| **24h Change** | +5.80% |
| **7d Change** | +0.60% |
| **30d Change** | +7.47% |
| **1y Change** | -82.44% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xd9fcd98c322942075a5c3860693e9f4f03aae07b` |
| Arbitrum One | `0x462cd9e0247b2e63831c3189ae738e5e9a5a4b64` |
| Base | `0xa153ad732f831a79b5575fa02e793ec4e99181b0` |
| Binance Smart Chain | `0x2117e8b79e8e176a670c9fcf945d4348556bffad` |
| Unichain | `0xe9c43e09c5fa733bcc2aeaa96063a4a60147aa09` |
| Plasma | `0xca632fa58397391c750c13f935daa61abbe0baa6` |
| Sonic | `0x2117e8b79e8e176a670c9fcf945d4348556bffad` |
| Berachain | `0xeb9b5f4eb023ae754ff59a04c9c038d58606dac6` |
| Swellchain | `0x80ccfbec4b8c82265abdc226ad3df84c0726e7a3` |
| Tac | `0x38c043856a109066d64a60c82e07848a1c58e7dc` |
| Bob Network | `0xde1763afa5eb658cffffd16835afeb47e7ac0b8d` |
| Avalanche | `0x9ceed3a7f753608372eeab300486cc7c2f38ac68` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | EUL/USDT | N/A |
| Kraken | EUL/USD | N/A |
| Upbit | EUL/BTC | N/A |
| KuCoin | EUL/USDT | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0XD9FCD98C322942075A5C3860693E9F4F03AAE07B/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |
| Uniswap V2 (Ethereum) | 0XD9FCD98C322942075A5C3860693E9F4F03AAE07B/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |
| Balancer V2 | 0XD9FCD98C322942075A5C3860693E9F4F03AAE07B/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.euler.finance/](https://www.euler.finance/) |
| **Twitter** | [@eulerfinance](https://twitter.com/eulerfinance) |
| **Telegram** | [eulerfinance_official](https://t.me/eulerfinance_official) (8,404 members) |
| **Discord** | [https://discord.com/invite/CdG97VSYGk](https://discord.com/invite/CdG97VSYGk) |
| **GitHub** | [https://github.com/euler-xyz](https://github.com/euler-xyz) |
| **Whitepaper** | [https://docs.euler.finance/getting-started/white-paper](https://docs.euler.finance/getting-started/white-paper) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **Current Price** | $1.076 |
| **Market Cap** | $25,940,278 |
| **Market Cap Rank** | #707 |
| **24h Change** | +1.19% |
| **7d Change** | +5.51% |
| **Last Updated** | 2026-06-22 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

- **March 2023** — ~$197M flash-loan exploit; subsequently the attacker returned essentially all recoverable funds (see History above).
- **2024** — Euler v2 relaunch with the Euler Vault Kit and Ethereum Vault Connector.

---

## Trading Profile

### Venues & liquidity

EUL is tradable on [[binance]] — **spot** (EUL/USDT) plus a **USD-margined perpetual** with the usual derivatives surface: [[funding-rate|funding]], [[open-interest]], and [[liquidations]]. It is **not** listed on Hyperliquid, so Binance is the **primary leveraged venue** for EUL. Additional spot liquidity exists on Kraken, Upbit, and KuCoin, but leveraged flow, funding, and OI concentrate almost entirely on Binance. As a ~#734-ranked, ~$25M-cap microcap, EUL's order books are thin: the single dominant perp venue means funding and liquidation signals are clean but easily distorted, spreads widen quickly, and slippage on size is material. Sizing should be conservative — small clip sizes, wide-but-respected stops, and awareness that a modest notional can move price and trigger cascades. Perp availability enables shorting and carry structures otherwise impossible for a thinly held governance token, but leverage on such an illiquid market amplifies liquidation risk in both directions.

### Applicable strategies

- [[funding-rate-harvest]] — the single Binance USD-M perp lets a trader collect funding when EUL's crowded, one-sided positioning pushes rates persistently positive or negative.
- [[crowded-long-funding-fade]] — narrative-driven pops on a microcap this thin frequently over-extend perp longs; fading elevated positive funding into exhaustion is a recurring setup.
- [[liquidation-cascade-fade]] — with all leverage on one venue and shallow books, forced-liquidation flushes overshoot; fading the wick after a cascade targets the snap-back.
- [[cash-and-carry]] — long Binance spot versus short the USD-M perp captures basis/funding when the perp trades rich, a clean carry given EUL's single perp venue.
- [[rsi-mean-reversion]] — low-liquidity microcaps whipsaw around fair value, so oscillator-based mean reversion on stretched intraday moves fits EUL's range-bound regimes.
- [[breakout-and-retest]] — EUL's sharp, narrative-led expansions off compressed ranges reward trading confirmed breakouts and their retests rather than chasing.

### Volatility & regime character

EUL is a **small-cap DeFi/infra governance token** (lending protocol), not a memecoin — its moves are driven more by protocol adoption, TVL, unlock/emission news, and DeFi-sector rotation than pure reflexive hype. It carries **high beta to BTC/ETH**: in risk-off tape it bleeds with the broad altcoin complex, and in DeFi-sector risk-on it can outperform sharply. Realized volatility is large relative to majors given the microcap float; price gaps and reflexive squeezes are common on thin liquidity. Correlation to ETH (its native chain and sector anchor) tends to run higher than to BTC during DeFi-specific narratives.

### Risk flags

- **Liquidity / venue concentration** — leveraged trading, funding, and OI sit almost entirely on Binance; a single-venue outage, delisting, or fee change disproportionately affects EUL execution.
- **Microcap thinness** — ~$25M cap and modest depth mean large slippage, wide spreads, and susceptibility to manipulation and stop-runs.
- **Unlocks / emissions** — market-cap/FDV near 0.9 leaves some remaining emission and incentive-program overhang that can pressure price on supply events; see [[token-unlock-supply-event]] dynamics.
- **Narrative / adoption dependence** — value accrual to EUL hinges on DAO fee decisions and Euler v2 adoption; sentiment can shift abruptly on protocol news.
- **Reputational / smart-contract shadow** — the 2023 exploit history (fully recovered) still colors sentiment and can amplify downside on any security-related headline.

---

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=EULUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=EULUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=EUL` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=EUL` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=EULUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=EULUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=EUL"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---

## Related

- [[lending]]
- [[defi]]
- [[flash-loan]]
- [[aave]]
- [[compound]]
- [[frax-share]]
- [[governance-token]]
- [[smart-contract-risk]]
- [[erc-20]]
- [[ethereum]]
- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko snapshot).
- General market knowledge (publicly documented Euler v1/v2 architecture, EVK/EVC, and the March 2023 exploit and recovery); no specific narrative wiki source ingested yet.
