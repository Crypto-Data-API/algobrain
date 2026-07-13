---
title: "Staking"
type: concept
created: 2026-04-07
updated: 2026-06-21
status: excellent
tags: [crypto, defi, yield]
aliases: ["Proof of Stake Staking", "Crypto Staking", "ETH staking", "ETH-staking"]
related: ["[[ethereum]]", "[[proof-of-stake]]", "[[defi]]", "[[staking-yield-arbitrage]]", "[[liquid-staking]]", "[[restaking]]", "[[lido-dao]]", "[[babylon]]", "[[slashing]]", "[[crypto-yield-stack]]"]
domain: [crypto, defi]
difficulty: beginner
---

Staking is the process of locking [[crypto|cryptocurrency]] in a [[proof-of-stake|proof-of-stake (PoS)]] network to participate in transaction validation, block production, and network security. In return, stakers earn staking rewards -- typically 3-8% annual percentage yield (APY) -- paid in the network's native token. This page is the **reference hub** for staking; see the [[liquid-staking]], [[restaking]], and [[slashing]] pages for deeper coverage of each branch.

### The Staking Stack (Map of This Topic)

| Layer | What It Is | Key Pages | Example Protocols |
|---|---|---|---|
| **Native staking** | Run a validator yourself; bond the network's token directly | [[proof-of-stake]] | Solo ETH validator, Solana validator |
| **Delegated staking** | Delegate to a validator without running infra | this page | Cosmos, Polkadot, Cardano delegation |
| **Liquid staking (LST)** | Receive a tradeable derivative (stETH, JitoSOL) while staked | [[liquid-staking]], [[lido-dao]] | [[lido-dao\|Lido]], Rocket Pool, Jito, Marinade |
| **Restaking (LRT)** | Re-pledge staked ETH to secure additional services | [[restaking]] | EigenLayer, Symbiotic |
| **Bitcoin staking** | Stake native BTC to secure PoS chains without bridging | [[babylon]] | [[babylon\|Babylon]] |

## Overview

Staking is the PoS equivalent of mining in proof-of-work (PoW) networks like [[bitcoin|Bitcoin]]. Instead of expending computational energy to validate transactions, PoS validators lock up ("stake") tokens as economic collateral. Validators who behave honestly earn rewards; those who act maliciously (double-signing, prolonged downtime) are "slashed" -- losing a portion of their staked tokens.

Since [[ethereum|Ethereum's]] transition from PoW to PoS in September 2022 ("The Merge"), staking has become one of the most significant yield-generating activities in crypto, with over $50 billion in ETH staked.

## How Staking Works

### Solo Staking (Native Validation)

Running your own validator node and staking directly with the network.

- **Ethereum**: Requires 32 ETH (approximately $80,000-$100,000 at typical prices), dedicated hardware, and technical knowledge to maintain uptime
- **Solana**: No minimum stake, but effective validation requires significant SOL and high-performance hardware
- **Cardano**: Stake pool operators run infrastructure; delegators can stake any amount

**Advantages**: Full control, no counterparty risk, maximum rewards (no fees to intermediaries).
**Disadvantages**: High capital requirements (Ethereum), technical complexity, slashing risk from misconfiguration.

### Delegated Staking

Delegating tokens to a validator operated by someone else. Available on most PoS networks (Cosmos, Polkadot, Solana, Cardano). The validator runs infrastructure; delegators share in rewards minus a commission (typically 5-15%).

### Liquid Staking

A major innovation that solves the liquidity problem of traditional staking. Liquid staking protocols issue a derivative token representing the staked position:

| Protocol | Staked Token | Derivative Token | Network |
|----------|-------------|------------------|---------|
| **[[lido-dao|Lido]]** | ETH | stETH (wstETH) | Ethereum |
| **Rocket Pool** | ETH | rETH | Ethereum |
| **Coinbase** | ETH | cbETH | Ethereum |
| **Marinade** | SOL | mSOL | Solana |
| **Jito** | SOL | JitoSOL | Solana |

**How it works**: User deposits ETH into [[lido-dao|Lido]], receives stETH. stETH accrues staking rewards automatically (rebasing daily) and can be used in [[defi|DeFi]] -- as collateral on [[aave|Aave]], in [[automated-market-maker|AMM]] liquidity pools, or traded on secondary markets. This enables "double dipping" -- earning staking yield while simultaneously using the capital in DeFi. See [[crypto-yield-stack]] for layering LST yield with lending and LP yield.

[[lido-dao|Lido]] is the largest liquid staking protocol, controlling roughly a quarter to a third of all staked ETH, which has raised persistent **centralization concerns** — a single protocol approaching the consensus-threatening one-third share is treated as a systemic risk by Ethereum researchers. The [[lido-dao|LDO]] governance token controls protocol parameters.

### Restaking (LRTs)

[[restaking]] (pioneered by EigenLayer, with Symbiotic as a competitor) lets users re-pledge already-staked ETH or LSTs to secure additional "Actively Validated Services" (AVSs) — oracles, bridges, data-availability layers, rollups — earning extra rewards in exchange for accepting **additional slashing conditions**. Liquid Restaking Tokens (LRTs) wrap restaked positions into a tradeable derivative, stacking yet another layer onto the yield stack. The trade-off: **stacked, correlated slashing risk** — a fault in any secured service can penalise the same underlying stake.

### Bitcoin Staking

[[babylon|Babylon]] enables native **BTC staking** to secure PoS chains without bridging or wrapping the Bitcoin. Bitcoin holders lock BTC via time-locked scripts on the Bitcoin base layer and earn rewards from the secured chains, with slashing enforced through cryptographic mechanisms (EOTS) rather than a custodial bridge. This extends staking yield to the largest, previously non-yielding crypto asset.

### Exchange Staking

Centralized exchanges (Coinbase, Binance, Kraken) offer staking services where users deposit tokens and the exchange handles validation. Convenient but introduces counterparty risk -- the exchange controls the staked assets. Regulatory scrutiny has increased: the SEC forced Kraken to shut down its US staking program in February 2023.

## Staking Yields

Staking rewards come from two sources:

1. **Protocol inflation**: New tokens minted as block rewards (the primary source on most networks)
2. **Transaction fees**: A share of fees paid by users for on-chain transactions

| Network | Approximate APY | Source |
|---------|----------------|--------|
| Ethereum | 3-5% | Inflation + priority fees + MEV |
| Solana | 6-8% | Inflation (high emission rate) |
| Cosmos (ATOM) | 15-20% | Inflation (designed to incentivize staking) |
| Polkadot | 12-15% | Inflation |
| Cardano | 4-5% | Inflation + fees |

**Important**: Nominal APY can be misleading. If a network inflates its supply at 7% and staking yields 8%, the real yield is only ~1%. Stakers who do not stake are diluted by inflation, making staking partly a defensive necessity rather than pure yield generation.

## Key Metrics Traders Watch

| Metric | What It Tells You | Why It Matters |
|---|---|---|
| **Staking ratio** | % of total supply staked | Higher ratio = less liquid float (price impact), more conviction; also dilutes per-validator yield |
| **Real yield** | Nominal APY minus token inflation | The only yield figure that survives dilution — see warning above |
| **LST/ETH peg** | Discount/premium of stETH, rETH vs ETH | A discount signals exit-queue stress or forced selling (3AC: -6% in June 2022); arbitrage opportunity |
| **Validator queue length** | Entry/exit unbonding backlog | Long exit queue = stakers cannot get liquidity fast; affects LST peg |
| **Lido market share** | Concentration of a single LST provider | Approaching one-third of ETH staked is a consensus/centralisation risk flag |
| **MEV + tip share** | Portion of yield from priority fees/MEV vs inflation | Fee-driven yield is "real" (paid by users), inflation yield is dilutive |
| **Restaking TVL & AVS count** | Adoption and slashing surface of [[restaking]] | More AVSs = more yield but more correlated slashing exposure |

## Risks

### Slashing

Validators can lose a portion of staked tokens (see [[slashing]] for the full mechanism) for:
- **Double signing**: Proposing or attesting to two conflicting blocks
- **Extended downtime**: Failing to participate in consensus for prolonged periods (Ethereum penalizes ~0.001% per day of inactivity)
- **Correlated failures**: If many validators go offline simultaneously (e.g., a cloud provider outage), penalties increase proportionally — Ethereum's "correlation penalty" deliberately punishes coordinated faults far more than isolated ones
- **Restaking amplification**: With [[restaking]], a single stake can be slashed by multiple secured services, so slashing risk compounds across the stack

### Lock-up Periods

- **Ethereum**: Withdrawals require an unbonding queue (typically minutes to days depending on exit demand; post-Shanghai upgrade in April 2023)
- **Cosmos**: 21-day unbonding period -- staked ATOM cannot be transferred or sold for 21 days after initiating unstaking
- **Polkadot**: 28-day unbonding period

During lock-up, stakers cannot sell -- creating significant risk during market crashes.

### Smart Contract Risk (Liquid Staking)

Liquid staking derivatives depend on smart contract security. A bug in Lido's contracts could affect billions in staked ETH. The stETH/ETH peg can also deviate during market stress (stETH traded at a 6% discount during the June 2022 Three Arrows Capital collapse).

### Regulatory Risk

Regulators (particularly the US SEC) have taken the position that some staking services constitute unregistered securities offerings. This has led to enforcement actions against centralized staking providers and uncertainty about the regulatory status of liquid staking tokens.

## Staking vs. Other Yield Sources

| Source | Typical Yield | Risk Profile |
|--------|--------------|-------------|
| **Native staking** | 3-8% | Protocol inflation, slashing, lock-up |
| **Liquid staking** ([[lido-dao\|Lido]], Jito) | 3-8% (+ DeFi reuse) | Above + smart-contract + LST depeg |
| **Restaking** (EigenLayer) | Staking + AVS rewards | Above + correlated/stacked slashing |
| **Lending** (Aave, Compound) | 1-5% | Smart contract, utilization rate |
| **LP fees** (Uniswap) | Variable | [[impermanent-loss]], smart contract |
| **Yield farming** | 5-100%+ | High inflation, rug pulls, complexity |

The yield generally rises as you move down the stack — but so does the **layered, often correlated risk**. A liquid-restaked position earning the highest headline yield is exposed to base-layer slashing, LST smart-contract risk, restaking slashing, and DeFi composability risk simultaneously.

## Related

**Concepts**: [[proof-of-stake]], [[liquid-staking]], [[restaking]], [[slashing]], [[defi]], [[impermanent-loss]]
**Protocols / assets**: [[lido-dao]], [[babylon]], [[ethereum]]
**Strategies**: [[staking-yield-arbitrage]], [[crypto-yield-stack]] -- combining staking with other DeFi yield sources for optimized returns, [[yield-farming]]

## Sources

- General crypto market knowledge; no specific wiki source ingested yet.
