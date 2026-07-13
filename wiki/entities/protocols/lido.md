---
title: "Lido Finance"
type: entity
created: 2026-04-15
updated: 2026-06-21
status: excellent
tags: [crypto, defi, ethereum]
entity_type: protocol
founded: 2020
website: "https://lido.fi"
aliases: ["Lido", "Lido Finance", "Lido DAO"]
related: ["[[ethereum]]", "[[defi]]", "[[eth-staking]]", "[[steth]]", "[[makerdao]]", "[[aave]]", "[[curve-finance]]", "[[uniswap]]", "[[chainlink]]", "[[yearn]]"]
---

# Lido Finance

**Lido Finance** is the largest liquid staking protocol in [[defi|decentralized finance]], enabling users to stake [[ethereum|ETH]] and receive a liquid derivative token (**stETH**) that represents their staked position plus accruing rewards. Launched in December 2020 ahead of Ethereum's transition to proof-of-stake, Lido solved a critical problem: native ETH staking required locking up a minimum of 32 ETH (worth over $50,000 at typical prices) with no ability to withdraw or use those assets until the Shanghai/Capella upgrade in April 2023. Lido removed both constraints -- users could stake any amount, and the stETH token remained liquid, tradeable, and usable as collateral across DeFi protocols.

At its peak, Lido controlled approximately **30% of all staked ETH** on the Ethereum network, making it one of the most systemically important protocols in the ecosystem. By early 2026 that share had drifted down to roughly **23-24% (~$100B in assets as of February 2026)**, eroded mainly by large new entrants to staking such as BitMine and Grayscale rather than by rival liquid-staking protocols. This concentration raised significant decentralization concerns: if a single entity controls too large a share of validators, it could theoretically influence consensus, censor transactions, or become a single point of failure. The Ethereum community debated whether Lido should self-impose a cap on its market share, and the protocol's governance (conducted through the LDO token by the Lido DAO) has been a focal point of broader debates about DeFi governance concentration. Competitors including Rocket Pool (rETH), Coinbase (cbETH), and Frax (sfrxETH) emerged to provide alternatives, though Lido maintained its dominant position through first-mover advantage, deep DeFi integrations, and strong liquidity for stETH.

The LDO governance token grants holders voting rights over protocol parameters, fee structures, and node operator selection. Lido charges a **10% fee on staking rewards**, split between node operators and the DAO treasury. stETH has become one of the most important assets in DeFi, widely accepted as collateral on lending platforms like [[aave|Aave]] and [[makerdao|MakerDAO]], and serving as a base pair in decentralized exchanges. The protocol's TVL (total value locked) has consistently ranked among the top three in all of DeFi, reflecting the massive scale of Ethereum staking and Lido's role as the primary intermediary between retail stakers and the Ethereum consensus layer.

---

## At a Glance

| Attribute | Detail |
|---|---|
| **Type** | [[liquid-staking]] protocol on [[ethereum]] |
| **Founded** | December 2020 |
| **Governed by** | Lido DAO (LDO token); dual governance live since mid-2025 |
| **User-facing tokens** | stETH (rebasing), wstETH (non-rebasing wrapper) |
| **Governance token** | LDO |
| **What you deposit** | ETH (any amount; no 32 ETH minimum) |
| **What you receive** | stETH redeemable ~1:1 for ETH plus accrued staking rewards |
| **Staking yield** | ~3-4% APR in ETH terms (varies with network conditions) |
| **Protocol fee** | 10% of staking rewards (split node operators / DAO treasury) |
| **Market position** | Largest liquid-staking protocol; ~23-24% of all staked ETH (early 2026; ~30% at peak) |
| **Withdrawals** | Enabled since Shanghai/Capella (April 2023) via a withdrawal queue |

---

## Architecture and How It Works

Lido sits between retail stakers and Ethereum's consensus layer. When a user deposits ETH, Lido pools it, allocates 32-ETH validator units across a **curated set of professional node operators**, and mints stETH to the depositor. Rewards earned by the validators flow back into the protocol and are reflected as a daily increase in stETH balances. Withdrawals are processed through a queue: a holder burns stETH and, after the queue clears, receives the underlying ETH.

| Component | Role |
|---|---|
| **Staking pool contract** | Accepts ETH deposits, mints/burns stETH, tracks the exchange rate |
| **Node operators** | ~30+ vetted professional operators run the validators; chosen by the DAO |
| **Oracle / accounting** | Reports validator balances and rewards on-chain so stETH can rebase |
| **Withdrawal queue** | Processes stETH → ETH redemptions in order; can lengthen under stress |
| **Slashing insurance fund** | Limited DAO-held buffer to offset slashing penalties |
| **stVaults (V3)** | Modular vaults letting institutions configure their own validator sets while minting stETH |

Compared with **native solo staking** (run your own validator, need 32 ETH, no fee, full control) and **centralized staking** (Coinbase, Binance: custodial, regulated, simple), Lido's trade-off is: any deposit size, full DeFi liquidity and composability, at the cost of a 10% fee and smart-contract + validator-concentration risk. See [[liquid-staking]] and [[eth-staking]].

---

## Key Features

| Feature | Detail |
|---|---|
| **Function** | Liquid staking -- stake ETH, receive stETH (liquid derivative) |
| **Token** | LDO (governance), stETH/wstETH (liquid staking derivative) |
| **ETH Staking Market Share** | ~23-24% of all staked ETH as of early 2026 (~30% at peak; verify on Dune Analytics) |
| **Staking Reward** | ~3-4% APR on staked ETH (varies with network conditions) |
| **Fee** | 10% of staking rewards (5% to node operators, 5% to DAO treasury) |
| **TVL** | Among the top 1-3 DeFi protocols globally (verify on DefiLlama) |
| **wstETH** | Wrapped stETH -- non-rebasing version used as collateral in DeFi |

---

## stETH Mechanics

### Rebasing vs. Wrapped

- **stETH** is a **rebasing token**: the balance in your wallet increases daily as staking rewards accrue. If you hold 10 stETH today, you might hold 10.001 stETH tomorrow
- **wstETH** (wrapped stETH) is a **non-rebasing token**: the balance stays fixed, but each wstETH is worth an increasing amount of stETH over time. wstETH is preferred for DeFi integrations ([[aave]], [[curve-finance]], [[uniswap]]) because rebasing tokens create accounting complexity in smart contracts

### stETH/ETH Peg

stETH should trade very close to 1:1 with ETH, since each stETH represents 1 staked ETH plus accrued rewards. It is a *soft* peg backed by redeemability rather than a fiat-style hard peg (contrast with [[stablecoin-depegs|stablecoin de-pegs]]). However, the peg can deviate during market stress:

- **June 2022 depeg**: During the 3AC/Terra collapse, stETH traded as low as ~0.93 ETH due to forced selling by leveraged positions. This created a significant buying opportunity for those who understood the depeg was a liquidity event, not a solvency event
- **Post-Shanghai (April 2023)**: Once ETH withdrawals were enabled, the fundamental reason for persistent depeg risk was largely removed -- stETH holders could redeem 1:1 with underlying staked ETH, though with a withdrawal queue delay
- **Peg monitoring**: Track the stETH/ETH ratio on [[curve-finance]] (the primary stETH/ETH liquidity venue) and DefiLlama

---

## 2025-2026 Developments

### Dual Governance (live mid-2025)

In 2025 Lido DAO approved and activated **dual governance**, a long-debated mechanism giving stETH holders a structural check on LDO voting power (approved June 2025, on-chain by early July 2025). If stakers object to a DAO proposal, they can escrow stETH to **delay execution for up to ~45 days while exiting their staked ETH** — a "rage quit" channel designed to prevent hostile governance takeovers and to soften the principal-agent problem between LDO voters and stETH holders. For traders, this materially reduces the governance-capture tail risk that lending protocols price into stETH collateral parameters.

### Lido V3 and stVaults (January-March 2026)

**Lido V3 went live on 2026-01-30**, the protocol's largest upgrade since launch. Its centerpiece is **stVaults** — modular, customizable staking vaults that turn Lido from a single pooled product into shared staking infrastructure:

- stVaults let institutions, custodians, and node operators configure validator sets, fee structures, and risk parameters while still minting stETH against their stake — aimed squarely at **institutional/ETF staking demand**.
- Rollout was phased: Phase 2 on 2026-01-29, **Phase 3 (permissionless stETH minting from vaults) on 2026-03-02**.
- The companion **Lido Earn** product reached ~61K ETH TVL in its early months, with custodian and ETF integrations underway (Lido tokenholder update, February 2026); partners such as Kiln are building institutional stVault offerings.
- stVaults preserve an exit path from Lido governance (similar in spirit to dual governance), addressing the centralization critique that drove the "cap Lido at 22%" debate.

### Market-share dynamics

Lido's decline from ~30% to ~23-24% of staked ETH (2024 → 2026) came mostly from **new institutional stakers (BitMine, Grayscale and other ETF/treasury vehicles) staking directly or via custodians**, not from users leaving Lido. stVaults are Lido's competitive response — capture that institutional flow as infrastructure rather than compete with it as a retail pool.

---

## LDO Governance and Tokenomics

LDO is the governance token of the Lido DAO. Holders vote on the parameters that matter most to stETH economics and risk: the node-operator set, the 10% fee split, treasury spending, and protocol upgrades. Historically LDO was concentrated among early investors and the DAO treasury, which is the root of the **principal-agent problem** -- LDO voters set policy, but stETH holders bear the staking risk.

| Element | Detail |
|---|---|
| **Token** | LDO -- governance only (no direct fee accrual to LDO holders) |
| **Voting** | LDO-weighted on-chain votes via Aragon; off-chain Snapshot signaling first |
| **Dual governance** | Live since mid-2025: stETH holders can escrow stETH to delay a contentious proposal up to ~45 days while exiting (a "rage quit" channel) |
| **Fee** | 10% of staking rewards; DAO controls the split between operators and treasury |
| **Key debate** | Whether to self-cap Lido's share of staked ETH (the "cap at 22%" discussion) to protect Ethereum decentralization |

For traders, the dual-governance upgrade is the headline change: it converts governance-capture from a *trapped-capital* risk into an *exit-with-delay* risk, which lending protocols can price more comfortably into stETH collateral parameters. See [[dao-governance]] and [[tokenomics]].

---

## How Traders and Investors Use Lido

- **Base ETH yield**: HODLers stake ETH for stETH to earn ~3-4% APR while keeping a liquid, transferable position (vs. locking ETH in a solo validator).
- **DeFi collateral**: wstETH is accepted on [[aave]] (e-mode), [[makerdao]], and others; it is the backbone of leveraged "staking loop" strategies.
- **Liquidity provision**: stETH/ETH on [[curve-finance]] is one of DeFi's deepest pools; the ratio there is the canonical peg gauge.
- **Peg arbitrage**: traders buy discounted stETH during liquidity-driven depegs and redeem/hold for the recovery (see strategies below).
- **Macro proxy**: stETH supply and the stETH/ETH peg are read as barometers of ETH-staking demand and DeFi leverage stress.
- **Institutional rails (V3)**: custodians and ETF vehicles use stVaults to stake with bespoke validator/risk configs while still minting stETH.

---

## Trading Strategies

### 1. Basic stETH Staking (Very low difficulty)

- **Mechanism**: Stake ETH via Lido, receive stETH, hold and earn staking rewards
- **APY**: ~3-4% in ETH terms (varies with network activity; higher during periods of elevated transaction fees)
- **Capital requirement**: Any amount (no 32 ETH minimum)
- **Difficulty**: Beginner -- single transaction
- **Risk**: Smart contract risk; Lido validator risk; opportunity cost vs. other yield sources
- **Use case**: Base layer ETH yield for HODLers who want passive income on their ETH position

### 2. stETH/ETH Peg Trading (Moderate difficulty)

- **Mechanism**: Monitor stETH/ETH price on [[curve-finance]] and secondary markets. Buy stETH at a discount to ETH during depeg events (fear, forced liquidations), hold or redeem via withdrawal queue for 1:1
- **Profit potential**: 2-7% per depeg event (June 2022 offered ~7% discount; smaller depegs of 0.5-2% occur periodically)
- **Capital requirement**: $10,000+ (ideally $50,000+ to justify monitoring effort)
- **Difficulty**: Intermediate -- requires market timing, understanding of withdrawal queue mechanics, and patience
- **Risk**: The depeg could worsen before recovering (if it is a genuine solvency event rather than a liquidity event); withdrawal queue can take days to weeks during high-demand periods
- **Historical edge**: Every stETH depeg since Lido's launch has fully recovered. Past performance does not guarantee future results, but the structural backstop of ETH withdrawal creates a fundamental floor

### 3. stETH as DeFi Collateral (Moderate difficulty)

- **Mechanism**: Deposit wstETH as collateral on [[aave]] (e-mode), borrow ETH at 85% LTV, stake the borrowed ETH via Lido for more stETH, repeat (leverage loop)
- **APY**: 8-15% on the leveraged staking spread (stETH yield minus ETH borrow cost, amplified by leverage)
- **Capital requirement**: $25,000+
- **Difficulty**: Intermediate -- requires understanding of liquidation mechanics and continuous monitoring
- **Risk**: Liquidation if stETH/ETH peg breaks beyond the e-mode liquidation threshold; smart contract risk across both Lido and [[aave]]; borrow rate spikes could make the spread negative
- **Note**: This is one of the most popular "DeFi-native" yield strategies. [[yearn]] vaults and other aggregators automate this loop
- (Source: [[2026-04-22-perplexity-defi-trading-strategies-sweep]])

### 4. stETH Yield + DeFi Stacking (Moderate difficulty)

- **Mechanism**: Hold stETH, deposit into [[curve-finance]] stETH/ETH pool for swap fees, stake Curve LP tokens on Convex for CRV + CVX rewards
- **APY**: 7-15% total (stETH staking yield + Curve swap fees + CRV/CVX emissions)
- **Capital requirement**: $20,000+ on mainnet
- **Difficulty**: Intermediate -- requires multiple protocol interactions
- **Risk**: Smart contract risk across Lido, Curve, and Convex; impermanent loss if stETH depegs; CRV/CVX emission value compression

---

## Risk Framework

### Validator Concentration Risk (Systemic)

Lido's share of all staked ETH (~30% at peak, ~23-24% in early 2026) creates **systemic risk for the entire Ethereum network**. If Lido's validators simultaneously go offline (due to a software bug, governance attack, or coordinated slashing event), it could disrupt Ethereum consensus. The Ethereum community considers this the single biggest centralization risk in the ecosystem. Lido DAO has debated self-imposed caps but has not implemented one.

### Slashing Risk

Ethereum validators can be **slashed** (penalized) for malicious behavior or technical failures (e.g., double-signing). Lido diversifies across multiple node operators to mitigate correlated slashing risk, but a coordinated failure across node operators using the same client software could result in significant slashing penalties. Lido maintains a slashing insurance fund, but its coverage is limited.

### Smart Contract Risk

Lido's contracts have been audited extensively and have secured tens of billions in value. However, the stETH/wstETH token contracts are among the most value-dense smart contracts in existence, making them high-value targets. Any exploit would be catastrophic for Lido and for DeFi protocols that accept stETH as collateral ([[aave]], [[makerdao]], [[curve-finance]]).

### stETH Depeg Risk (Post-Shanghai)

Since the Shanghai/Capella upgrade enabled ETH withdrawals, the fundamental depeg risk for stETH has decreased significantly. However, a withdrawal queue bottleneck during extreme market stress (if many holders try to redeem simultaneously) could create temporary depegs that trigger liquidations on lending protocols.

### Governance Concentration

LDO token voting power is concentrated among early investors and the Lido DAO treasury. Governance decisions (node operator selection, fee changes, protocol upgrades) may not reflect the interests of all stETH holders. The "principal-agent problem" -- stETH holders bear staking risk but LDO holders make governance decisions -- is a structural concern. **Partially mitigated since mid-2025**: the dual-governance mechanism lets stETH holders delay contentious proposals up to ~45 days while withdrawing, converting governance capture from a trapped-capital risk into an exit-with-delay risk.

---

## Key Metrics

| Metric | Approximate Range | Notes |
|---|---|---|
| **TVL** | Top 1-3 in all DeFi | Verify on DefiLlama |
| **ETH Staked via Lido** | ~23-24% of total staked ETH (early 2026); ~$100B in assets | Verify on Dune Analytics |
| **stETH APR** | 3-4% | Varies with network activity |
| **LDO Price** | Volatile; verify on CoinGecko | |
| **LDO Market Cap** | ~$1-2B range historically | Verify on CoinGecko |
| **Protocol Revenue** | 10% of staking rewards (~$300M+ annualized at peak) | Split between operators and treasury |
| **Node Operators** | ~30+ professional operators | Verify on Lido operator page |

---

## Competitive Position

| Competitor | Lido Advantage | Competitor Advantage |
|---|---|---|
| Rocket Pool (rETH) | Deeper liquidity; more DeFi integrations; larger scale | More decentralized (permissionless node operators); no governance concentration |
| Coinbase (cbETH) | Non-custodial; DeFi-native | Regulated entity; simpler onboarding for institutional users |
| Frax (sfrxETH) | Larger market share; more established | Frax offers dual-token model with higher yield option |
| Native ETH staking | No 32 ETH minimum; liquid derivative; DeFi composability | No smart contract risk; no 10% fee; full control of validator |
| Eigenlayer restaking | Simpler product (just staking) | Restaking offers additional yield layers on top of staking |

Lido's moat is **liquidity depth and DeFi integration breadth**. stETH is accepted as collateral on virtually every major DeFi protocol, creating a self-reinforcing cycle: more integrations → more demand for stETH → deeper liquidity → more integrations. Breaking this network effect would require a competitor to match Lido's liquidity across dozens of protocols simultaneously.

---

## Related

- [[ethereum]] -- The network Lido stakes on
- [[defi]] -- The ecosystem where stETH is used as collateral
- [[aave]] -- Major lending protocol accepting wstETH as collateral (e-mode)
- [[curve-finance]] -- Primary stETH/ETH liquidity venue
- [[makerdao]] -- Accepts stETH/wstETH as collateral for DAI minting
- [[yearn]] -- Uses stETH in ETH vault strategies and yETH product
- [[chainlink]] -- Provides price feeds for stETH/ETH used by lending protocols

---

## Sources

- (Source: [[2026-04-22-perplexity-defi-trading-strategies-sweep]])
- Lido blog — "Lido V3 Is Live: Modular Infrastructure for a New Paradigm of Ethereum Staking": https://blog.lido.fi/lido-v3-is-live-modular-infrastructure-for-a-new-paradigm-of-ethereum-staking/
- Lido blog — "Recap: Lido Tokenholder Update: February 2026": https://blog.lido.fi/recap-lido-tokenholder-update-february-2026/
- Lido V3 Whitepaper: https://hackmd.io/@lido/v3-whitepaper
- Figment — "Lido V3 Explained: Customizable Staking with stVaults": https://www.figment.io/insights/lido-v3-explained-customizable-staking-with-stvaults/
- Cryptopolitan — "Lido activates dual governance to stop hostile takeovers" (2025): https://www.cryptopolitan.com/lido-activates-dual-governance-to-stop-hostile-takeovers-and-protect-ethereum-stakers/
- BlockEden — "Lido V3 stVaults: How Modular Staking Infrastructure Unlocks Institutional Ethereum" (2026-02-09): https://blockeden.xyz/blog/2026/02/09/lido-v3-stvaults-ethereum-staking/
- Web verification via Perplexity/WebSearch, 2026-06-10.
