---
title: "Aave"
type: entity
created: 2026-04-06
updated: 2026-06-21
status: excellent
tags: [crypto, defi, ethereum]
aliases: ["AAVE", "ETHLend", "Aave Protocol"]
entity_type: protocol
founded: 2017
headquarters: "Decentralized (Aave Labs: London, UK)"
website: "https://aave.com"
related: ["[[defi]]", "[[ethereum]]", "[[smart-contracts]]", "[[arbitrum]]", "[[polygon]]", "[[lido]]", "[[curve-finance]]", "[[uniswap]]", "[[chainlink]]", "[[makerdao]]"]
---

# Aave

**Aave** is the largest [[defi|decentralized finance]] [[lending|lending and borrowing]] protocol by total value locked (TVL), enabling users to supply crypto assets to earn interest or borrow against their collateral without intermediaries. Originally launched as ETHLend in 2017, Aave operates across [[ethereum]], [[arbitrum]], [[polygon]], Optimism, Avalanche, Base, and other chains. It pioneered several DeFi primitives including flash loans and efficiency mode (e-mode) for correlated-asset borrowing, and issues the native overcollateralized stablecoin [[gho|GHO]].

---

## At a Glance

| Attribute | Detail |
|---|---|
| **Type** | Overcollateralized [[lending|money market]] (supply / borrow / liquidate) |
| **Launched** | 2017 as **ETHLend**; rebranded to Aave (Finnish for "ghost") in 2018 |
| **Steward** | Aave Labs (London, UK); governed by the Aave DAO |
| **Latest version** | v4 (Ethereum mainnet, 2026) — hub-and-spoke liquidity; v3 across ~21 chains |
| **Governance token** | AAVE — voting + Safety Module / Umbrella staking |
| **Native stablecoin** | [[gho|GHO]] — overcollateralized, governance-set borrow rate |
| **Receipt tokens** | aTokens (interest-bearing supply receipts), variable/stable debt tokens |
| **Signature primitives** | Flash loans, e-mode, isolation mode, Portals (cross-chain) |
| **Oracle** | [[chainlink]] price feeds for collateral valuation and liquidation |
| **Closest peers** | Compound, [[makerdao]] / Spark, Morpho |

---

## Key Features

| Feature | Detail |
|---|---|
| **Function** | Overcollateralized lending and borrowing |
| **Chains** | [[ethereum]], [[arbitrum]], [[polygon]], Optimism, Avalanche, Base, and others |
| **Token** | AAVE -- governance and safety module staking |
| **Flash Loans** | Uncollateralized loans that must be repaid within a single transaction (0.05% fee) |
| **Version** | Aave v4 live on Ethereum mainnet since March-April 2026; v3 remains deployed across 21 chains |
| **TVL** | ~$14.5B (May 2026, all versions/chains); peaked at $30.25B in November 2025 |
| **GHO** | Aave's native overcollateralized stablecoin (~$584M supply, June 2026) |

---

## How It Works

- **Suppliers** deposit assets into lending pools and earn variable interest rates driven by utilization
- **Borrowers** post collateral (overcollateralized) and borrow other assets; they pay interest that flows to suppliers
- **Liquidations** occur when a borrower's collateral value falls below the required threshold -- liquidators repay debt and claim collateral at a discount (typically 5-10% bonus)
- **Flash loans** allow developers to borrow any amount with zero collateral, provided the loan is repaid atomically within the same transaction -- used for [[arbitrage]], liquidations, and collateral swaps
- **Interest rates** are algorithmically determined by utilization: low utilization = low rates; high utilization = rates spike to incentivize repayment

### aTokens and Debt Tokens

When a user supplies an asset, they receive an **aToken** (e.g., supplying USDC mints aUSDC) at a 1:1 ratio. aTokens are **interest-bearing and rebasing** — the balance grows in real time as interest accrues, and they are redeemable 1:1 for the underlying. Because they are standard ERC-20s, aTokens are themselves composable collateral elsewhere in [[defi|DeFi]]. Borrowers symmetrically receive **variable debt tokens** (and, historically, stable debt tokens) that track their growing obligation. This receipt-token design is what lets Aave positions plug into looping, yield, and [[arbitrage]] strategies across the ecosystem.

### Isolation Mode and Portals

- **Isolation mode** lets governance list riskier or newer assets as collateral with a **debt ceiling** and a restricted set of borrowable assets, containing the blast radius if that asset misbehaves.
- **Portals** allow supplied liquidity to move across Aave deployments on different chains, supporting Aave's cross-chain liquidity footprint.

### Efficiency Mode (e-Mode)

Aave v3 introduced **e-mode** for correlated asset pairs, allowing significantly higher loan-to-value (LTV) ratios. For example, borrowing ETH against [[lido|wstETH]] collateral can reach **85% LTV** (vs. ~75% for standard mode), because the price correlation between wstETH and ETH is extremely high. This enables capital-efficient looping strategies and is one of Aave's most important features for active DeFi traders.

### GHO Stablecoin

[[gho|GHO]] is Aave's native overcollateralized stablecoin, minted by borrowers against their Aave collateral. GHO borrowing rates are set by governance (not algorithmically), and stkAAVE holders receive a discount on GHO borrow rates. Because GHO is minted directly by the protocol, the interest paid by GHO borrowers accrues to the Aave DAO treasury rather than to suppliers — making GHO a direct protocol-revenue lever distinct from the standard pooled-lending markets. GHO adoption has been gradual but steady: supply reached approximately **$584 million** by mid-May 2026, trading at $0.999 (within 0.1% of peg), with 2026 expansion focused on additional chains (Avalanche, Gnosis, with Plasma and Linea planned). See [[gho]] for the full mechanism, peg-stability tooling, and facilitator model.

### 2025-2026 Protocol Developments

- **Aave v4 launched on Ethereum mainnet in March-April 2026**, introducing a hub-and-spoke liquidity architecture (a unified liquidity "hub" per network with specialized "spokes" borrowing from it) and targeting real-world credit markets. It spans the chains previously covered by v3.
- **Horizon** (launched 2025 by Aave Labs) — an institutional RWA (real-world asset) market allowing tokenized money-market funds and treasuries to be used as collateral for stablecoin borrowing.
- **Umbrella** (2025) — replaced the legacy Safety Module with an automated staking/slashing system where staked aTokens directly absorb bad debt.
- **TVL cycle**: Aave TVL peaked at **$30.25 billion in November 2025**, then declined roughly 52% to **$14.49 billion by mid-May 2026** as the broader crypto market corrected — Aave remained the largest DeFi lending protocol by TVL throughout.

---

## Liquidations in Detail

Liquidations are Aave's core risk-control mechanism and the most important dynamic for traders to understand:

- Each collateral asset has a **loan-to-value (LTV)**, a **liquidation threshold**, and a **liquidation bonus** set by governance/risk parameters.
- A position's **health factor** = (collateral × liquidation threshold) ÷ total borrow value. When the health factor falls **below 1.0**, the position becomes liquidatable.
- A liquidator repays part of the borrower's debt and receives the equivalent collateral **plus the liquidation bonus** (typically a 5-10% discount to market), which is the incentive that keeps the system solvent.
- Liquidations are open and permissionless, so they are dominated by **MEV-driven bots** racing in the mempool — see the Liquidation Hunting strategy below and [[market-microstructure|on-chain microstructure]].
- For traders watching the order book, **clustered liquidation thresholds act like a magnet**: when price approaches a band where large collateralized positions sit, a cascade can amplify the move, which is itself a tradeable signal (see [[#Trading Relevance|Trading Relevance]]).

---

## How Traders Use Aave

| User | Goal | Mechanism |
|---|---|---|
| **Yield suppliers** | Passive interest on idle assets | Deposit; hold rebasing aTokens |
| **Leverage / loopers** | Amplified staking or directional exposure | Supply collateral → borrow → re-supply (e-mode boosts LTV) |
| **Shorts via borrowing** | Bet against a token | Borrow it, sell spot, repay later at a lower price |
| **Flash-loan engineers** | Capital-free [[arbitrage]], collateral swaps, self-liquidation | Borrow + repay atomically within one transaction |
| **Liquidators** | Discounted collateral | Repay unhealthy debt, claim collateral + bonus via bots |
| **GHO borrowers** | Stable-rate, governance-priced credit | Mint [[gho|GHO]] against collateral (stkAAVE discount) |

---

## Trading Strategies

### 1. Supply-Side Yield Farming (Low difficulty, reliable)

- **Mechanism**: Deposit stablecoins (USDC, USDT, DAI) into Aave lending pools and earn variable interest from borrowers
- **Example**: Deposit $50,000 USDC into Aave on Ethereum mainnet, earn ~4-6% APY
- **APY**: 4-6% on stablecoins; variable based on utilization (spikes to 10%+ during high-demand periods)
- **Capital requirement**: $10,000+ (smaller amounts viable on L2 deployments where gas is negligible)
- **Difficulty**: Beginner -- deposit and earn, no active management required
- **Risk**: Smart contract risk; stablecoin depeg risk; variable rates can compress during low-demand periods
- **Profitability**: ~$200-300/month passive income on $50K; truly passive
- (Source: [[2026-04-22-perplexity-defi-trading-strategies-sweep]])

### 2. e-Mode Capital Efficiency Play (Moderate difficulty)

- **Mechanism**: Supply a liquid staking derivative (e.g., [[lido|wstETH]]) as collateral, borrow the underlying asset (ETH) at high LTV (85%), then stake the borrowed ETH for additional yield or sell for leverage
- **Example**: Supply $50K wstETH → borrow ~$42.5K worth of ETH at 85% LTV → stake borrowed ETH via Lido → loop
- **APY**: 8-15% on the leveraged staking spread (wstETH yield minus ETH borrow cost), amplified by leverage
- **Capital requirement**: $25,000+ (gas costs on mainnet for multiple transactions)
- **Difficulty**: Intermediate -- requires understanding of liquidation mechanics and monitoring
- **Risk**: Liquidation if wstETH/ETH peg breaks significantly (the stETH depeg in June 2022 hit 5%); oracle risk; smart contract risk on [[lido]] side
- (Source: [[2026-04-22-perplexity-defi-trading-strategies-sweep]])

### 3. Flash Loan Arbitrage (High difficulty)

- **Mechanism**: Borrow massive capital ($1M-$10M+) within a single atomic transaction, execute a profitable arbitrage (e.g., price discrepancy between [[uniswap]] and [[curve-finance]]), repay loan + 0.05% fee, pocket the profit
- **Example**: Flash borrow $1M USDC → buy USDC on Curve at $0.998 → sell on Uniswap at $1.000 → repay $1M + $500 fee → profit $1,500
- **Capital requirement**: $0 upfront (that is the entire point of flash loans), but requires smart contract development skills and gas for execution
- **Difficulty**: Expert -- requires Solidity development, understanding of DEX mechanics, gas optimization, and competition with professional arbitrage bots
- **Reality check**: Flash loan arbitrage is extremely competitive. Most profitable opportunities are captured by professional MEV bots within milliseconds. Retail traders are unlikely to find consistent edge here without sophisticated infrastructure
- (Source: [[2026-04-22-perplexity-defi-trading-strategies-sweep]])

### 4. Liquidation Hunting (Extreme difficulty)

- **Mechanism**: Monitor Aave loans approaching liquidation thresholds, then call the liquidation function to repay the borrower's debt and claim their collateral at a 5-10% discount
- **Profit**: 2-5% of the liquidated amount per successful liquidation
- **Capital requirement**: $50,000-$100,000+ to sustain bot operations and gas costs
- **Difficulty**: Expert -- requires 24/7 bot infrastructure, on-chain monitoring, and fast execution
- **Reality check**: Professional liquidation bots scan all Aave positions continuously. Manual liquidation hunting is not viable; this is an infrastructure play requiring custom bots, private mempools, and significant capital
- (Source: [[2026-04-22-perplexity-defi-trading-strategies-sweep]])

### 5. GHO Minting Arbitrage (Moderate difficulty, conditional)

- **Mechanism**: Mint GHO against Aave collateral when GHO trades above $1.00 on secondary markets, sell for profit. Buy GHO below $1.00 and repay Aave debt at par
- **Profitability**: Depends entirely on GHO peg deviation frequency and magnitude
- **Difficulty**: Intermediate
- **Risk**: GHO peg could tighten (eliminating arb opportunities) or break downward (minters lose capital)
- **Prerequisite**: Verify GHO market cap and peg stability before deploying capital

---

## History and Governance

| Period | Milestone |
|---|---|
| 2017 | Launches as **ETHLend**, a peer-to-peer crypto lending marketplace |
| 2018 | Rebrands to **Aave**; pivots toward pooled liquidity money markets |
| 2020 | **Aave v1/v2** popularize flash loans and pooled lending; AAVE token + Safety Module introduced |
| 2022 | **Aave v3** ships e-mode, isolation mode, and Portals across many chains |
| 2023 | **[[gho|GHO]]** stablecoin launches on Ethereum |
| 2025 | **Horizon** (institutional RWA market) and **Umbrella** (automated slashing backstop) launch |
| 2026 | **Aave v4** goes live on Ethereum mainnet with hub-and-spoke liquidity architecture |

Aave is governed by the **Aave DAO**: AAVE (and stkAAVE) holders vote on risk parameters, new asset listings, GHO borrow rates, treasury deployment, and protocol upgrades. Risk parameters are stewarded with input from delegated risk teams (e.g., Chaos Labs, Gauntlet historically), making Aave one of the more institutionally-structured DeFi governance systems. This professional risk apparatus is part of why Aave is the protocol most often cited as the candidate "DeFi lending standard" for institutional adoption.

---

## Risk Framework

### Liquidation Cascades

When collateral assets crash 20%+ in a short period, Aave liquidations trigger en masse. Each liquidation creates sell pressure on the collateral asset, potentially pushing other positions underwater and creating a cascade. The March 2020 "Black Thursday" and the May 2022 Terra collapse demonstrated this dynamic across DeFi lending protocols. Aave's risk parameters (LTV, liquidation thresholds, liquidation bonuses) are calibrated to minimize cascade risk but cannot eliminate it.

### Smart Contract Risk

Aave v3 has been audited extensively and has processed tens of billions in volume. However, the protocol's composability -- flash loans interacting with external protocols -- creates attack surface at the integration layer. White-hat and black-hat exploits have targeted Aave-adjacent integrations. The Safety Module (stkAAVE) provides a backstop of staked AAVE tokens that can be slashed to cover bad debt, but this is not unlimited insurance.

### Oracle Risk

Aave relies on [[chainlink]] price feeds for collateral valuation and liquidation triggers. If an oracle feed delivers incorrect prices -- whether through manipulation, latency, or infrastructure failure -- borrowers could be incorrectly liquidated (or not liquidated when they should be). Chainlink's decentralized node network mitigates but does not eliminate this risk.

### Interest Rate Risk

Aave's variable interest rates can spike dramatically during high-demand periods. A borrower who enters a position at 3% borrow rate may suddenly face 15%+ rates if utilization surges, making the position unprofitable. Stable rate borrowing (where available) mitigates this but at a premium.

### Counterparty/Protocol Risk

Aave accepts various collateral types including liquid staking derivatives ([[lido|stETH]], rETH), wrapped tokens (WBTC), and governance tokens. Each collateral type introduces the risk of its underlying protocol. A [[lido]] exploit, for example, could impair stETH collateral across all Aave positions.

---

## Key Metrics

| Metric | Approximate Range | Notes |
|---|---|---|
| **TVL** | $14.5B (May 2026); Nov 2025 peak $30.25B | Verify current on DefiLlama |
| **Utilization Rate** | 70-85% on Ethereum | Higher utilization = higher rates |
| **Stablecoin Supply APY** | 4-6% (USDC/USDT/DAI) | Variable; verify on Aave app |
| **Volatile Asset Borrow APY** | 8-25% | Depends on asset and demand |
| **AAVE Price** | volatile; verify on CoinGecko | Earlier draft cited ~$400-500 (late-2025 area) |
| **AAVE Market Cap** | verify on CoinGecko | |
| **GHO Supply / Market Cap** | ~$584M (June 2026), $0.999 peg | Up from <$100M in early 2024 |
| **Flash Loan Fee** | 0.05% per loan | Fixed by protocol |

---

## Competitive Position

| Competitor | Aave Advantage | Competitor Advantage |
|---|---|---|
| Compound | More chains, more assets, e-mode, flash loans, GHO | Compound is simpler and more battle-tested on Ethereum mainnet |
| [[makerdao]] | Permissionless lending/borrowing; multiple collateral types | MakerDAO is focused on DAI minting (different model); arguably more decentralized governance |
| Morpho | Established liquidity and brand | Morpho offers peer-to-peer rate optimization on top of Aave/Compound |
| Spark (MakerDAO) | Broader multi-chain presence | Spark benefits from MakerDAO's DAI ecosystem and often has competitive rates |

Aave's moat is its **multi-chain liquidity depth**, **e-mode innovation**, and **institutional recognition** as the DeFi lending standard. It is the protocol most likely to benefit from institutional DeFi adoption due to its extensive audit history and governance framework.

---

## Trading Relevance

- Aave borrowing rates serve as a real-time indicator of demand for leverage in specific tokens
- Flash loans enable complex [[arbitrage]] strategies and are a key tool in the DeFi trader's toolkit
- Aave liquidation levels create predictable support/resistance zones -- large liquidation cascades amplify price moves
- AAVE token trades as a proxy for DeFi lending sector growth and protocol revenue
- Monitoring Aave supply/borrow rates helps gauge market sentiment (high borrow demand = bullish positioning or short demand)
- [[lido|stETH]] is one of the most popular collateral types on Aave, linking the two protocols' risk profiles
- [[curve-finance]] pools for stablecoins are frequently used for flash loan arbitrage sourced from Aave

---

## Related

- [[defi]] -- The broader DeFi ecosystem
- [[ethereum]] -- Primary chain for Aave deployments
- [[smart-contracts]] -- The technology enabling trustless lending
- [[arbitrum]] -- Major L2 with significant Aave activity
- [[lido]] -- stETH/wstETH is a primary collateral type on Aave
- [[curve-finance]] -- Frequently used alongside Aave for flash loan arbitrage
- [[chainlink]] -- Oracle infrastructure Aave depends on for price feeds
- [[makerdao]] -- Competing/complementary lending protocol
- [[uniswap]] -- DEX frequently used for Aave flash loan arbitrage execution
- [[gho]] -- Aave's native overcollateralized stablecoin
- [[lending]] -- The broader on-chain lending/money-market concept
- [[gmx]] -- Real-yield DeFi perp protocol (another flagship DeFi venue)

---

## Sources

- (Source: [[2026-04-22-perplexity-defi-trading-strategies-sweep]]) — trading strategies sections
- DefiLlama, Aave protocol page — https://defillama.com/protocol/aave (TVL: $14.49B May 2026; $30.25B Nov 2025 peak)
- CoinLaw, "Aave Statistics 2026" — https://coinlaw.io/aave-statistics/ (TVL decline, GHO supply ~$584M, v4 multi-chain footprint)
- Aave, "2025 Year in Review" — https://aave.com/blog/aave-2025-recap (Horizon, Umbrella, GHO expansion)
- Eco support docs, "Aave V3 vs V4" — https://eco.com/support/en/articles/14800886-aave-v3-vs-v4-what-changed-and-why-it-matters (hub-and-spoke architecture)
- Verified via web search and Perplexity (sonar), 2026-06-10
