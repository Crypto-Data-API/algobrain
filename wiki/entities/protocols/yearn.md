---
title: "Yearn Finance"
type: entity
created: 2026-04-15
updated: 2026-06-21
status: excellent
tags: [crypto, defi, ethereum]
entity_type: protocol
founded: 2020
website: "https://yearn.fi"
aliases: ["Yearn", "Yearn Finance", "YFI", "yearn.finance"]
related: ["[[defi]]", "[[ethereum]]", "[[curve-finance]]", "[[aave]]", "[[lido]]", "[[uniswap]]", "[[smart-contracts]]"]
---

# Yearn Finance

**Yearn Finance** is a [[defi|decentralized finance]] yield aggregator that automatically optimizes [[yield-farming|yield farming]] strategies across multiple protocols. Launched in 2020 by Andre Cronje, Yearn pioneered the concept of **vaults** -- smart contract-managed pools that accept user deposits and deploy capital across the highest-yielding opportunities in DeFi, auto-compounding returns without requiring manual intervention. Yearn's vaults abstract away the complexity of [[yield-farming]], making sophisticated multi-protocol strategies accessible to depositors who simply deposit an asset and receive optimized yield.

> **Disambiguation:** This is the **protocol/entity** page. YFI as a *traded token* (price, market cap, supply mechanics) and YFI trading strategies are out of scope here beyond the governance role; this page covers architecture, products, governance, and how traders *use* the protocol. Verify all metrics on-chain (DefiLlama, yearn.fi, CoinGecko) — figures here are historical ranges, not live data.

---

## History and Timeline

| Date | Event |
|------|-------|
| **Feb 2020** | Andre Cronje launches iEarn (yield-routing across lenders) — the precursor to Yearn |
| **Jul 2020** | YFI governance token launched with **zero pre-mine / zero founder allocation** — fully distributed to liquidity providers, an early "fair launch" milestone in [[defi]] |
| **2020** | Vaults v1 introduced — strategy-managed auto-compounding pools |
| **Feb 2021** | DAI vault exploit (~$11M lost via a flash-loan-assisted strategy manipulation) |
| **2021** | "Merger" wave — Yearn announced collaborations/partnerships with Cream, Cover, Pickle, SushiSwap, Akropolis (loose alliances, not full token mergers) |
| **2021** | Vaults v2 ships — multi-strategy vaults (capital split across several strategies per vault) |
| **2022** | yCRV relaunch and veYFI vote-escrow governance introduced (Curve-style) |
| **2023** | yETH liquid-staking-derivative basket launched; Vaults **v3** rollout begins (modular, ERC-4626-aligned, permissionless strategy/vault factory) |
| **Nov 2025** | Legacy yETH stableswap pool exploit (~$9M via infinite-mint; ~$2.39M clawed back); v2/v3 vaults and yCRV unaffected |

Andre Cronje stepped back from active development in 2022; the protocol is maintained by contributor teams and yearn DAO governance. Cronje's later projects (Fantom/Sonic, Keep3r, Solidly) are distinct from Yearn.

---

## Key Features

| Feature | Detail |
|---|---|
| **Function** | Automated yield optimization via vaults |
| **Chains** | [[ethereum]] (primary), [[arbitrum]], Optimism, Polygon, and others |
| **Token** | YFI -- governance token (one of the lowest-supply tokens in crypto: 36,666 total) |
| **Version** | v3 vaults are the current generation |
| **TVL** | Verify on DefiLlama (historically $3-6B at peak; varies with market conditions) |
| **Governance** | veYFI model (vote-escrow, inspired by [[curve-finance|Curve]]) |

---

## How It Works

### Vault Architecture

1. **User deposits** a single asset (e.g., USDC, ETH, DAI) into a Yearn vault
2. The vault deploys that capital across one or more **strategies** -- smart contracts that interact with external protocols ([[curve-finance]], [[aave]], Compound, [[lido]], Convex, etc.)
3. Strategies harvest yields, sell reward tokens for the base asset, and **auto-compound** -- reinvesting profits back into the vault
4. Users receive a vault token (yvToken) representing their share of the growing pool
5. Yearn charges a **management fee** (typically 2%) and **performance fee** (typically 20% of profits), similar to a traditional hedge fund fee structure

### Vault Generations

| Generation | Key change | Significance for users |
|------------|-----------|------------------------|
| **v1** (2020) | Single-strategy auto-compounding vault | Proved the auto-compounding concept |
| **v2** (2021) | **Multi-strategy** vault — capital allocated across several strategies with debt ratios | Diversifies strategy risk within one vault |
| **v3** (2023+) | Modular, **ERC-4626**-aligned, permissionless vault + strategy factory; "Yearn Allocator" vaults route between v3 "Tokenized Strategies" | Composability with the rest of DeFi; anyone can deploy a vetted strategy; current generation |

The move to the **ERC-4626** tokenized-vault standard in v3 matters because it makes yvTokens drop-in compatible with other DeFi protocols (lending markets, aggregators), reinforcing Yearn's role as composable yield infrastructure. See [[smart-contracts]] and [[defi]].

### Product Family

Yearn is broader than stablecoin vaults. The main products:

| Product | What it is | Underlying |
|---------|------------|------------|
| **Vaults (v3)** | Core auto-compounding yield vaults | Stables, ETH, [[curve-finance|Curve]] LP, etc. |
| **yCRV** | Liquid wrapper for Yearn's locked CRV (veCRV) position | [[curve-finance]] |
| **yETH** | Diversified LSD basket (stETH, rETH, sfrxETH, …) | [[lido]] + other LSDs |
| **yPRISMA / partner LSTs** | Liquid wrappers for partner governance locks | Partner protocols |
| **veYFI** | Vote-escrowed YFI for governance + fee share | YFI |
| **Vault factory** | Permissionless deployment of v3 vaults/strategies | Any ERC-20 |

### Strategy Examples

- **Curve-based strategies**: Deposit stablecoins into [[curve-finance]] pools, stake LP tokens in Convex for boosted CRV + CVX rewards, harvest and sell rewards for the base asset, redeposit
- **Lending-based strategies**: Supply assets to [[aave]] or Compound, earn lending interest, rebalance between protocols to chase the highest rate
- **Liquid staking strategies**: Deposit ETH into [[lido]] for stETH yield, then deploy stETH into Curve/Aave for additional layers of yield
- **Looping strategies**: Supply an asset to Aave, borrow against it, re-supply the borrowed asset, creating leveraged yield exposure

### veYFI Governance

Yearn adopted the vote-escrow model from [[curve-finance]]: YFI holders lock their tokens for veYFI, which grants governance voting power, protocol fee sharing, and the ability to direct vault incentives via gauge voting. This aligns long-term holders with protocol governance decisions.

### yETH

**yETH** is Yearn's basket product for liquid staking derivatives (LSDs). It holds a diversified mix of [[lido|stETH]], rETH, sfrxETH, and other ETH staking derivatives, providing exposure to ETH staking yield with reduced single-protocol risk compared to holding any individual LSD.

> **⚠ November 2025 exploit**: On 30 November 2025 the legacy yETH weighted stableswap pool on Ethereum was drained of roughly **$9M** via an infinite-mint attack — a complex sequence pushed the pool's internal solver into a divergent state and triggered an arithmetic underflow, letting the attacker mint an astronomically large yETH balance from a 16-wei deposit (The Block, Yellow/Nansen). Yearn confirmed **v2 and v3 vaults and yCRV were unaffected** (the bug was limited to the legacy yETH implementation), clawed back ~$2.39M, and published a remediation plan. Protocol TVL remained above ~$600M through the incident (CoinGecko, Dec 2025).

---

## Trading Strategies

### 1. Stablecoin Vault Deposits (Very low difficulty, set-and-forget)

- **Mechanism**: Deposit USDC, DAI, or USDT into a Yearn stablecoin vault. Yearn automatically routes capital to the highest-yielding strategies (Curve + Convex, Aave, Compound, etc.)
- **APY**: 5-12% historically (varies significantly with market conditions; higher during DeFi bull markets when borrow demand and CRV emissions are elevated)
- **Capital requirement**: $5,000+ (smaller amounts viable on L2 deployments)
- **Difficulty**: Beginner -- deposit and wait
- **Advantage over DIY**: Yearn handles gas-expensive harvests, reward selling, rebalancing, and compounding. For a $10,000 position, doing this manually on mainnet would cost hundreds in gas per month; Yearn amortizes gas across all vault depositors
- **Risk**: Smart contract risk (Yearn vault + underlying protocol); strategy risk (if an underlying protocol is exploited, vault depositors can lose funds)
- (Source: [[2026-04-22-perplexity-defi-trading-strategies-sweep]])

### 2. ETH Vault / yETH Staking (Low difficulty)

- **Mechanism**: Deposit ETH into Yearn's ETH vault or yETH product. Yearn stakes ETH via liquid staking protocols and deploys the resulting LSDs into yield-generating strategies
- **APY**: 4-8% (ETH staking base yield + additional DeFi yield layers)
- **Capital requirement**: $5,000+
- **Difficulty**: Beginner
- **Advantage**: Diversified LSD exposure via yETH reduces single-protocol risk compared to holding only [[lido|stETH]]
- **Risk**: Smart contract risk across multiple underlying protocols; LSDs could depeg in extreme market stress

### 3. Curve Pool Vault Deposits (Low-moderate difficulty)

- **Mechanism**: Deposit LP tokens from [[curve-finance]] pools into Yearn vaults for auto-compounded Curve + Convex rewards
- **APY**: 8-20% on stablecoin Curve LP; 15-40% on volatile Curve LP (with higher IL risk)
- **Capital requirement**: $10,000+ on mainnet; $5,000+ on L2
- **Difficulty**: Low-moderate -- requires obtaining Curve LP tokens first, then depositing into Yearn
- **Why use Yearn vs. direct Curve staking**: Yearn auto-compounds (significant APY improvement over time), auto-harvests (saves gas), and rebalances between strategies. The 20% performance fee is often worth it for the convenience and compounding benefit

### 4. Leveraged Yield via Yearn + Aave (Moderate difficulty)

- **Mechanism**: Deposit vault tokens (yvTokens) as collateral in protocols that accept them, borrow against the position, and re-deposit for leveraged yield exposure
- **APY**: 15-30% gross (depending on leverage and underlying vault yield)
- **Capital requirement**: $25,000+
- **Difficulty**: Intermediate -- requires managing liquidation risk on the borrowing side
- **Risk**: Liquidation if vault token value drops (due to smart contract event or underlying yield compression); borrowing cost may exceed vault yield during low-yield periods

---

## Risk Framework

### Smart Contract Composability Risk

Yearn vaults are **composable stacks**: user funds flow through Yearn's vault contract → strategy contract → external protocol (Curve, Aave, Convex, etc.). Each layer adds smart contract risk. A bug or exploit in any layer can result in loss of funds. Yearn has experienced exploits in the past (the February 2021 DAI vault exploit lost ~$11M; the November 2025 legacy yETH pool exploit lost ~$9M, with ~$2.39M recovered). Yearn maintains a comprehensive audit program and security team, but the composable nature of the protocol means risk cannot be fully eliminated.

### Strategy Risk

Individual strategies within a vault can underperform or fail. Yearn's multi-strategy vault architecture mitigates this by diversifying across multiple strategies, but concentrated strategy allocation (e.g., if 80% of a vault's capital is in a single Curve pool) creates concentration risk.

### Yield Compression

Yearn's yields are not guaranteed and fluctuate with DeFi market conditions. During bear markets, borrow demand drops, CRV emissions lose value, and Yearn vault APYs compress toward 2-4% on stablecoins. The protocol's fee structure (2/20) further reduces net yields to depositors.

### Fee Drag

Yearn's 2% management fee + 20% performance fee is among the highest in DeFi yield aggregation. On a 10% gross APY, net yield to depositors is approximately 8.4% after fees. Competing aggregators (e.g., Beefy Finance, Sommelier) may offer similar strategies with lower fees.

### Governance Risk

veYFI governance decisions affect vault parameters, strategy allocation, and fee structures. Concentration of veYFI voting power could lead to decisions that benefit large holders at the expense of smaller depositors.

---

## Key Metrics

| Metric | Approximate Range | Notes |
|---|---|---|
| **TVL** | ~$600M+ as of December 2025 (peak cycles saw $3-6B) | Verify on DefiLlama |
| **YFI Price** | $5,000-$40,000 range historically | Extremely low supply (36,666 YFI) makes price per token high |
| **YFI Market Cap** | $200M-$1B range | Verify on CoinGecko |
| **Number of Active Vaults** | 50-100+ across chains | Verify on yearn.fi |
| **Total Fees Generated** | Check Dune Analytics | Yearn earns meaningful revenue from 2/20 fee structure |
| **Stablecoin Vault APY** | 5-12% (varies with market) | Verify on yearn.fi |

---

## Competitive Position

| Competitor | Yearn Advantage | Competitor Advantage |
|---|---|---|
| Beefy Finance | More established brand; veYFI governance model; sophisticated multi-strategy vaults | Beefy is multi-chain native; lower fees; simpler single-strategy vaults |
| Sommelier | Pioneer of yield aggregation concept; deeper Ethereum integration | Sommelier offers off-chain strategy computation with on-chain execution |
| Convex Finance | Yearn uses Convex internally; Yearn abstracts the complexity | Convex offers direct access to boosted Curve rewards without Yearn's 2/20 fee |
| DIY farming | Auto-compounding saves significant gas; professional strategy management | No fees; full control; customizable |

Yearn's moat is its **strategy sophistication** and **auto-compounding infrastructure**. For depositors who want optimized DeFi yield without daily management, Yearn remains the standard. Its relationship with [[curve-finance]] (Yearn routes enormous capital through Curve/Convex) makes it a major participant in the Curve Wars ecosystem.

---

## See Also

- [[yield-farming]] -- the core activity Yearn automates
- [[defi]] -- The broader DeFi ecosystem
- [[ethereum]] -- Primary chain for Yearn
- [[curve-finance]] -- Primary yield source for many Yearn strategies; Curve Wars participant
- [[convex-finance]] -- Used internally by Yearn for boosted Curve rewards
- [[aave]] -- Lending protocol integrated into Yearn strategies
- [[lido]] -- stETH used in Yearn's ETH-denominated strategies and yETH
- [[uniswap]] -- DEX used for reward token swaps within Yearn strategies
- [[arbitrum]] -- An L2 deployment with lower-cost vaults
- [[smart-contracts]] -- Underlying technology (ERC-4626 vault standard in v3)
- [[liquid-staking]] -- The LSD layer underneath yETH
- [[stablecoin]] -- Base asset for the lowest-risk vaults
- [[smart-contract-risk]] -- The composability risk stacked across vault layers

---

## Sources

- (Source: [[2026-04-22-perplexity-defi-trading-strategies-sweep]])
- The Block, "Yearn Finance details $9 million yETH exploit, confirms partial recovery and outlines remediation plan" (Dec 2025) — https://www.theblock.co/post/381740/yearn-finance-9-million-yeth-exploit-confirms-partial-recovery-outlines-remediation
- Yellow, "Infinite-Mint Vulnerability Behind Yearn Finance's $2.8M yETH Exploit, Nansen Confirms" — https://yellow.com/news/infinite-mint-vulnerability-behind-yearn-finances-dollar28m-yeth-exploit-nansen-confirms
- Phemex News, "Yearn Confirms yCRV Safe After yETH Incident" (Dec 2025) — https://phemex.com/news/article/yearn-confirms-ycrv-unaffected-by-yeth-pool-incident-40977
- Yearn official site — https://yearn.fi/
- Verified via Perplexity (sonar) and web search, 2026-06-10.
