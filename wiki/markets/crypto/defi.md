---
title: "DeFi (Decentralised Finance)"
type: market
created: 2026-04-06
updated: 2026-06-21
status: excellent
tags: [crypto, defi, lending, dex, yield-farming, derivatives, regulation, ai-trading, market-microstructure]
aliases: ["decentralized-finance", "decentralised-finance", "DeFi", "Decentralized Finance", "Decentralised Finance"]
related: ["[[smart-contracts]]", "[[ethereum]]", "[[solana]]", "[[decentralized-exchanges]]", "[[uniswap]]", "[[aave]]", "[[curve-dao-token]]", "[[pendle]]", "[[lido-dao]]", "[[blockchain]]", "[[automated-market-maker]]", "[[defi-lending]]", "[[impermanent-loss]]", "[[liquidity-pools]]", "[[liquid-staking]]", "[[stablecoins]]", "[[staking]]", "[[gas-fees]]", "[[defi-yield-farming]]", "[[mev-strategies]]", "[[defi-hacks-and-exploits]]", "[[centralized-vs-decentralized-finance]]"]
markets: [crypto, defi]
---

**Decentralised Finance (DeFi)** is an ecosystem of financial applications built on public [[blockchain]] networks using [[smart-contracts]], enabling lending, borrowing, trading, and asset management without traditional intermediaries like banks or brokers. Users retain full custody of their assets, interact directly with protocols, and operate in permissionless systems without institutional gatekeepers. DeFi emerged primarily on [[ethereum]] during "DeFi Summer" (2020) and has since expanded across [[solana]], [[arbitrum]], [[polygon]], and dozens of other chains, reaching a record **$237 billion TVL** in Q3 2025. (Source: [[2026-04-15-defi-wiki-content-guide]])

---

## Core Architecture

Three layers underpin every DeFi interaction:

- **Blockchain Layer** -- the distributed ledger (e.g., [[ethereum]], [[solana]]) that stores state and executes code
- **Smart Contract Layer** -- self-executing [[smart-contracts]] with terms written directly into code; they automate financial processes without intermediaries and form the backbone of all dApps
- **Application Layer** -- user-facing dApps ([[uniswap]], [[aave]], [[jupiter-exchange-solana|Jupiter]]) that wrap smart contracts into usable products

Unlike traditional finance, DeFi eliminates central intermediaries by using smart contracts on public blockchains to execute financial transactions automatically. The shift starts with a non-custodial wallet, which acts as the user's gateway to the entire ecosystem. See [[centralized-vs-decentralized-finance]] for a full comparison across 11 dimensions. (Source: [[2026-04-15-defi-wiki-content-guide]])

---

## Protocol Categories

| Category | What It Does | Examples |
|---|---|---|
| **DEX (Spot)** | Peer-to-pool token swapping via [[automated-market-maker|AMMs]] | [[uniswap]], [[curve-dao-token|Curve]], [[jupiter-exchange-solana|Jupiter]], [[raydium|Raydium]] |
| **Lending/Borrowing** | Collateralised loans, interest markets | [[aave]], [[compound]], [[kamino|Kamino]] |
| **Perpetual DEX** | Leveraged derivatives trading on-chain | [[hyperliquid]], [[gmx]], [[dydx]] |
| **Yield/Vaults** | Automated yield optimisation strategies | [[pendle]], [[yearn]], [[convex]], DeFiSaver |
| **[[liquid-staking\|Liquid Staking]]** | Stake assets while keeping them liquid | [[lido-dao\|Lido]] (stETH), Marinade (mSOL), [[jito-governance-token\|Jito]] |
| **[[stablecoins\|Stablecoins]]** | Algorithmic or collateral-backed USD pegs | [[dai\|DAI]] ([[makerdao]]), [[usdc\|USDC]], [[gho\|GHO]], crvUSD ([[curve-dao-token\|Curve]]) |
| **Bridges** | Cross-chain asset movement | Wormhole, Stargate, Thorchain |
| **Real World Assets (RWA)** | Tokenised bonds, treasuries, real estate | [[ondo-finance]], [[blackrock\|BlackRock]] BUIDL |

(Source: [[2026-04-15-defi-wiki-content-guide]])

> **Per-vertical hubs:** [[stablecoins]] (USD pegs and peg mechanisms), [[staking]] / [[liquid-staking]] (PoS yield), [[gas-fees]] (execution cost), [[decentralized-exchanges]] (DEX deep-dive).

---

## Key Terms Glossary

- **[[automated-market-maker|AMM (Automated Market Maker)]]** -- algorithm that uses [[liquidity-pools]] instead of order books to determine exchange rates; the constant product formula x * y = k governs most AMMs
- **TVL (Total Value Locked)** -- the aggregate value of assets deposited into DeFi protocols; the primary gauge of ecosystem health
- **APY / APR** -- Annual Percentage Yield (with compounding) vs Annual Percentage Rate (without); the difference matters significantly in [[defi-yield-farming|yield farming]]
- **[[liquidity-pools|Liquidity Pool]]** -- a smart contract holding paired token reserves that enables decentralised trading and earns fees for depositors
- **LP Token** -- receipt token issued to liquidity providers representing their share of a pool
- **[[impermanent-loss|Impermanent Loss]]** -- the opportunity cost LPs face when token prices in a pool diverge from their entry prices; can erode yield farming returns
- **[[yield-farming|Yield Farming]] / [[liquidity-mining|Liquidity Mining]]** -- depositing assets into protocols to earn interest, trading fees, and governance token rewards
- **[[flash-loans|Flash Loan]]** -- an uncollateralised, instant loan that must be borrowed and repaid within a single transaction block; used in arbitrage and exploits
- **[[mev-strategies|MEV (Maximal Extractable Value)]]** -- value extracted by validators/searchers who reorder, include, or exclude transactions within a block; an "invisible tax" on users
- **CDP (Collateralised Debt Position)** -- a mechanism where users deposit collateral to mint stablecoins ([[makerdao|MakerDAO]]); subject to liquidation if collateral value falls below a threshold
- **Liquidation** -- the automatic forced sale of a borrower's collateral when their loan-to-value ratio breaches a safety threshold
- **[[oracle-manipulation|Oracle]]** -- off-chain data feeds (e.g., Chainlink) that supply real-world prices to smart contracts
- **DAO (Decentralised Autonomous Organisation)** -- a protocol governed by token holders via on-chain voting rather than a central management team
- **Governance Token** -- a token granting voting rights over a protocol's parameters and treasury; also distributed as liquidity mining rewards
- **Front-Running** -- an MEV tactic where a searcher copies a pending profitable transaction and submits it with a higher gas fee to execute first
- **Sandwich Attack** -- an MEV exploit where a bot places buy and sell orders around a victim's large swap, profiting from the resulting price impact

(Source: [[2026-04-15-defi-wiki-content-guide]])

---

## Trading Strategies

### Beginner

- **[[defi-yield-farming|Yield Farming / Passive LP]]** -- deposit token pairs into an AMM pool and earn a share of trading fees plus native token incentives. Key risk: [[impermanent-loss]]. Track via DeFi Llama, [[kamino|Kamino]] on Solana
- **[[stablecoin-yield|Stablecoin Farming]]** -- provide liquidity in stablecoin-only pools (e.g., USDC/USDT on [[curve-finance|Curve]]) for yield with near-zero impermanent loss risk. Lower APY but far more predictable
- **DCA into Protocols** -- gradually accumulate positions in high-quality DeFi tokens rather than timing the market

### Intermediate

- **Looping / Recursive Lending** -- borrow against deposited collateral, swap borrowed assets back to the original collateral, and re-deposit to amplify yield. Platforms like [[kamino|Kamino]] automate this. High liquidation risk if prices drop sharply
- **Cross-Chain Yield Farming** -- stake or provide liquidity across multiple chains simultaneously via bridges, targeting the highest APY across ecosystems
- **[[liquid-staking|Liquid Staking]] + Re-deployment** -- stake ETH via [[lido]] to receive stETH, then use stETH as collateral in [[aave]] to borrow stablecoins for additional farming. Lido held over $38.32B in staked ETH as of late 2025

### Advanced

- **[[flash-loan-arbitrage|Flash Loan Arbitrage]]** -- borrow large sums from [[aave]] or [[dydx]] without collateral, execute multi-DEX trades in a single transaction, and repay instantly. No upfront capital required but requires advanced Solidity/Rust
- **Perpetuals Trading** -- leveraged positions on [[hyperliquid]] (up to 100x). Hyperliquid captured 74-80.6% of decentralised perpetual market by mid-2025 with $375B cumulative volume
- **[[mev-strategies|MEV Extraction]]** -- running MEV bots (arbitrage, liquidation, sandwich) to capture on-chain value leakage. [[jito-governance-token|JITO]] on [[solana]] is the dominant MEV infrastructure
- **Yield Tokenisation ([[pendle]]-style)** -- split yield-bearing assets into principal tokens (PT) and yield tokens (YT), then trade them separately for fixed-yield strategies or leveraged yield speculation
- **[[concentrated-liquidity|Concentrated Liquidity]]** -- Uniswap v3 range orders for capital-efficient LP positions
- **[[delta-neutral-yield-farming|Delta-Neutral Yield Farming]]** -- hedged LP positions to isolate yield from price risk
- **[[jit-liquidity|Just-in-Time Liquidity]]** -- flash LP around large swaps for guaranteed fee capture

### Strategy Comparison

| Strategy | Skill Level | Risk | Potential Yield | Capital Needed |
|---|---|---|---|---|
| Stablecoin farming | Beginner | Low | 4-12% APY | Low |
| LP yield farming | Beginner-Mid | Medium | 10-40% APY | Low-Medium |
| Looping | Intermediate | High | 20-60% APY | Medium |
| Flash loan arbitrage | Advanced | Medium (technical) | Variable | Near-zero |
| Perp DEX trading | Advanced | Very High | Unlimited/Total loss | Medium |
| MEV botting | Expert | Medium | Variable | High (infra costs) |

See also: [[crypto-yield-stack]] for combining multiple DeFi yield sources, [[cefi-yield-vs-defi-yield]] for CeFi vs DeFi yield comparison. (Source: [[2026-04-15-defi-wiki-content-guide]])

---

## Market State (2025-2026)

### TVL and Market Overview

DeFi TVL hit a record **$237 billion** in Q3 2025, though daily active wallets fell 22% over the same period -- suggesting institutional/whale capital has grown while retail participation has cooled. [[ethereum]] accounted for 49% of total DeFi TVL (~$119B). DeFi transaction volumes are projected to exceed **$3 trillion** in 2026, with total TVL forecast to reach $500 billion. See [[2025-defi-renaissance]] for the full recovery narrative. (Source: [[2026-04-15-defi-wiki-content-guide]])

### Protocol Winners

- **[[hyperliquid]]** -- breakout story of 2025, capturing 74-80.6% of decentralised perpetual market share. [[hype-token|HYPE]] token surged 926% since Nov 2024 airdrop. ~35% of total blockchain protocol revenue by July 2025
- **[[jupiter-exchange-solana|Jupiter]]** -- [[solana]]'s default DEX aggregator, ~$101M in 30-day fees, single largest fee earner across all of DeFi
- **[[aave]]** -- dominant lending protocol with ~$42.47B TVL, ~$96M monthly fees. $122M per quarter as of early 2026
- **[[lido]]** -- liquid staking backbone with $38.32B in staked ETH, ~$9.25M monthly revenue
- **[[pendle]]** -- yield tokenisation pioneer with ~$13.3B TVL
- **[[uniswap]]** -- ~$77M monthly fees (v3 + v4) but zero protocol revenue (fee switch remains off)

### Protocol Losers

- **[[gmx]]** -- lost dominance to [[hyperliquid]], <2% perp DEX market by mid-2025. Suffered $42M exploit in July 2025
- **Blast, Zora** -- posted negative net revenue in March 2026; spending more on incentives than earned in fees
- **[[solana]] memecoins** -- TVL fell 33% in Q3 2025 due to diminishing memecoin/Pump.fun interest

### Institutional Entry

JPMorgan launched a $100M tokenised money market fund on [[ethereum]] in 2025. The tokenised RWA market surged to $25B in Q2 2025, with BlackRock's BUIDL fund holding $2.88B in tokenised Treasuries. (Source: [[2026-04-15-defi-wiki-content-guide]])

---

## Key Metrics Traders Watch

| Metric | What It Tells You | Where to Find It |
|---|---|---|
| **TVL (Total Value Locked)** | Aggregate capital in protocols; the headline health gauge (per-chain and per-protocol) | DeFiLlama |
| **Protocol revenue / fees** | Whether a protocol earns more than it pays in incentives (real vs mercenary yield) | DeFiLlama, Token Terminal |
| **Fees vs. emissions** | Negative net revenue (Blast, Zora 2026) = unsustainable incentive farming | DeFiLlama |
| **Stablecoin supply on-chain** | Dry powder available for deployment; rising = risk-on (see [[stablecoins]]) | DeFiLlama |
| **DEX/CEX volume ratio** | Migration of flow on-chain; structural adoption signal | DeFiLlama, The Block |
| **Lending utilisation rate** | How borrowed a market is; drives variable borrow/supply APYs and liquidation risk | [[aave]], protocol dashboards |
| **Perp open interest & [[funding-rates]]** | Leverage and directional crowding in on-chain derivatives | [[hyperliquid]], Coinglass |
| **LST/restaking TVL** | Staking-derived capital recycling through DeFi (see [[liquid-staking]], [[restaking]]) | DeFiLlama |
| **Active wallets** | Retail vs whale participation; falling actives with rising TVL = whale-driven | Artemis, Token Terminal |

In an [[market-cycles|established bear market]] (Fear & Greed ~23), watch for **TVL holding while active wallets fall** — the 2025 pattern where whale/institutional capital stayed while retail cooled.

---

## Security & Exploits

Crypto theft reached **$3.4 billion** overall in 2025. DeFi security breaches exceeded $3.1 billion in H1 2025 alone, surpassing 2024's total of $2.85 billion. See [[defi-hacks-and-exploits]] for the master timeline and [[2024-2025-major-defi-exploits]] for recent incidents. (Source: [[2026-04-15-defi-wiki-content-guide]])

### Biggest 2025 Hacks

| Protocol | Date | Loss | Vector |
|---|---|---|---|
| Bybit | Feb 2025 | $1.46B | Supply chain / signing infrastructure |
| Cetus (Sui) | May 2025 | $223M | Integer overflow in liquidity calculations |
| Balancer v2 | 2025 | $120M | Smart contract exploit |
| Nobitex (Iran) | Jun 2025 | $90M | Compromised private keys |
| Phemex | Jan 2025 | $73-85M | Hot wallet private key compromise |
| GMX V1 | Jul 2025 | $40-42M | Mint/burn function manipulation |

### 2026 Shift in Attack Vectors

Q1 2026 saw $169M stolen across 34 exploits -- down 89% year-over-year. However, the biggest losses shifted from [[smart-contracts]] bugs to **private key theft**, cloud infrastructure compromise, and [[oracle-manipulation]]. Access control vulnerabilities accounted for 59% of total 2025 losses. The Lazarus Group (North Korea) was responsible for a substantial portion of 2025 theft.

### Security Checklist

- Smart contract audits -- mandatory before deploying significant capital (Certik, OpenZeppelin, Halborn)
- Private key hygiene -- hardware wallets, multi-sig (Squads V4 on [[solana]])
- [[oracle-manipulation]] risks -- especially for smaller tokens
- Rug pull signals -- unlocked liquidity, anonymous teams, unaudited contracts
- MEV protection -- [[jito-governance-token|JITO]] bundles on [[solana]], private RPCs elsewhere

---

## AI x DeFi ("DeFAI")

By 2026, DeFi platforms are integrating AI to enhance automation, security, and decision-making at every layer. CoinGecko tracked nearly 150 DeFAI projects with a combined market cap of ~$1.62 billion as of mid-2025. See [[artificial-intelligence]] for the broader AI narrative. (Source: [[2026-04-15-defi-wiki-content-guide]])

### Five Key AI Applications in DeFi

1. **Automated Security Audits** -- AI continuously scans [[smart-contracts]] for vulnerability patterns
2. **AI-Driven Risk Management** -- models analyse historical data, liquidity patterns, and user behaviour to pre-calculate risk on lending and derivatives positions (see [[ml-defi-risk-models]])
3. **Automated Trading Bots** -- AI bots automate arbitrage, day trading, and swing trading strategies
4. **Personalised Portfolio Management** -- AI analyses wallet balances and past patterns to generate suggestions for staking, LP positions, and risk exposure
5. **Cross-Chain Intelligence** -- AI systems monitor bridge performance, latency, and congestion to optimise cross-chain routing

### DeFAI Projects to Watch

- **[[bittensor|Bittensor (TAO)]]** -- decentralised "global brain" for AI model training and inference on-chain
- **[[artificial-superintelligence-alliance|Artificial Superintelligence Alliance (FET)]]** -- merger of Fetch.ai, SingularityNET, and Ocean Protocol; autonomous agents for on-chain tasks
- **Theoriq Labs** -- AI agent infrastructure integrating reasoning with DeFi execution
- **DeFiSaver** -- automated vault management integrating AI coordination across bots

The 2026 bottleneck is coordination: making specialised but isolated agents (trading bots, liquidation bots, MEV searchers) work together rather than in silos. See [[llm-defi-interfaces]] and [[decentralized-ai]].

---

## DeFi on Solana

[[solana]]'s DeFi TVL reached **$13 billion** by May 2025, positioning it as the second-largest DeFi ecosystem behind [[ethereum]]. The Firedancer upgrade pushed throughput to 65,000 TPS (internal testing: 1M TPS), with 100% uptime throughout 2025. Over 2,100 active dApps operated on Solana as of Q1 2025. (Source: [[2026-04-15-defi-wiki-content-guide]])

### Top Solana DeFi Protocols

| Protocol | Category | Notes |
|---|---|---|
| [[jupiter-exchange-solana|Jupiter]] | DEX Aggregator | Largest DeFi fee earner globally; $101M 30-day fees |
| [[jito-governance-token|Jito]] | Liquid Staking + MEV | Dominant MEV infrastructure; critical for bot builders |
| [[kamino|Kamino Finance]] | Lending + Yield Vaults | Automated concentrated liquidity strategies |
| Marinade Finance | Liquid Staking | mSOL for liquid staking on Solana |
| Drift Protocol | Perp DEX | Suffered oracle/admin key exploit in early 2026 |
| Raydium | AMM/DEX | Deep liquidity for Solana token launches |

### Solana-Specific Considerations

- **[[jito-governance-token|Jito]] bundles** -- MEV-protected transaction bundles; critical for any bot or arbitrage work
- **Durable Nonces** -- enables offline transaction signing for automated systems
- **PDA vaults** -- programme-derived accounts as treasury infrastructure
- **Token2022 / Token Extensions** -- advanced token standards enabling confidential transfers and transfer hooks

---

## Real World Assets (RWA)

RWA tokenisation has become DeFi's fastest-growing vertical. The tokenised RWA market hit **$25 billion** in Q2 2025, with RWA-driven DeFi platforms averaging 185.8% ROI in 2025. Tokenised RWA collateral drove a 72% surge in DeFi TVL. (Source: [[2026-04-15-defi-wiki-content-guide]])

Key developments:
- **BlackRock BUIDL** -- $2.88B in tokenised U.S. Treasuries on [[ethereum]]
- **Figure** -- $14.7B in tokenised private credit
- **[[aave]] Horizon** and **[[ondo-finance|Ondo Finance]]** -- $400M+ TVL through programmable yield on tokenised assets
- **Yield-Bearing Stablecoins** -- on-chain equivalents of money market instruments

RWA tokenisation is projected to reach $23B TVL by Q4 2026, with the broader market growing from $1.1 trillion to $2 trillion in 2026.

---

## Derivatives & Perpetuals

Perpetual DEXs emerged in 2025 as the most technically advanced layer of DeFi execution, approaching CEX-level performance. The total decentralised perp market reached **$18.5B monthly volume** by late 2025, growing 420% year-over-year, though still representing only ~3% of centralised exchange volumes. (Source: [[2026-04-15-defi-wiki-content-guide]])

| Platform | Monthly Volume | Notes |
|---|---|---|
| [[hyperliquid]] | Dominant (74% share) | 200k orders/second, gasless, 0.2s latency |
| [[dydx]] v4 | $8.2B | Cosmos appchain architecture |
| [[gmx]] v2 | $4.1B | Pool-based model; impacted by $42M exploit |
| [[synthetix]] Perps v3 | $1.5B | Synthetic asset model |

See [[hyperliquid-perp-trading-map]] for detailed Hyperliquid strategies, [[hyperliquid-vs-dydx-vs-gmx]] for platform comparison.

---

## Regulation

### MiCA (EU)

The EU's Markets in Crypto-Assets regulation fully came into effect December 30, 2024. MiCA primarily regulates centralised entities (issuers and CASPs) -- fully decentralised protocols with no central entity currently remain outside scope. The grandfathering period ends July 1, 2026. The European Commission has launched a DeFi pilot project to study regulatory approaches, with dedicated DeFi regulation expected in future implementation. (Source: [[2026-04-15-defi-wiki-content-guide]])

### Global Compliance Landscape

- Over 75% of jurisdictions remain only partially compliant with FATF's AML standards for virtual assets as of June 2025
- The U.S. applies multi-agency oversight through FinCEN, SEC, and OFAC
- **Australia**: AUSTRAC applies to crypto businesses but DeFi protocols sit in a grey area

### KYC/AML in DeFi

The lack of KYC makes DeFi a regulatory target for money laundering and tax evasion concerns. KYT (Know Your Transaction) tools like Chainalysis and TRM Labs enable compliance without full identity collection.

---

## DeFi Risks Reference

| Risk Type | Description | Mitigation |
|---|---|---|
| Smart Contract Risk | Bugs in code lead to fund loss | Use only audited protocols; check Certik/OpenZeppelin audits |
| [[oracle-manipulation|Oracle Manipulation]] | Price feed manipulation triggers false liquidations | Use protocols with multi-oracle setups |
| [[impermanent-loss|Impermanent Loss]] | Token price divergence erodes LP returns | Stick to correlated pairs or stablecoin pools |
| Liquidation Risk | Over-leverage triggers forced collateral sale | Maintain healthy LTV ratios; use alerts |
| [[mev-strategies|MEV / Front-Running]] | Bots exploit pending transactions | Use [[jito-governance-token|JITO]] on [[solana]]; private mempools elsewhere |
| Rug Pull | Dev team abandons or steals funds | Check audit status, team identity, locked liquidity |
| Bridge Risk | Cross-chain bridges are frequent exploit targets | Minimise bridge exposure; use reputable protocols |
| Private Key Compromise | Most expensive 2025-2026 attack vector | Hardware wallets; multi-sig for protocol treasuries |
| Regulatory Risk | Protocols shut down due to regulatory action | Monitor MiCA, FATF updates |

(Source: [[2026-04-15-defi-wiki-content-guide]])

---

## Related

**Concepts**: [[smart-contracts]], [[automated-market-maker]], [[defi-lending]], [[impermanent-loss]], [[liquidity-pools]], [[liquid-staking]], [[restaking]], [[slashing]], [[decentralized-exchanges]], [[oracle-manipulation]]

**Strategies**: [[defi-yield-farming]], [[mev-strategies]], [[crypto-yield-stack]], [[delta-neutral-yield-farming]], [[concentrated-liquidity]], [[jit-liquidity]], [[liquidity-sniping]], [[flash-loan-arbitrage]], [[stablecoin-yield]]

**Protocols**: [[uniswap]], [[aave]], [[compound]], [[makerdao]], [[lido-dao]], [[curve-dao-token]], [[yearn]], [[convex]], [[dydx]], [[gmx]], [[synthetix]], [[sushiswap]], [[hyperliquid]], [[pendle]], [[ondo-finance]], [[jupiter-exchange-solana]], [[jito-governance-token]], [[kamino]], [[bittensor]], [[artificial-superintelligence-alliance]]

**Vertical hubs**: [[stablecoins]], [[staking]], [[liquid-staking]], [[restaking]], [[gas-fees]], [[decentralized-exchanges]]

**Markets**: [[ethereum]], [[solana]], [[bitcoin]], [[stablecoins]], [[yield-farming]], [[liquidity-mining]], [[flash-loans]]

**Comparisons**: [[centralized-vs-decentralized-finance]], [[cefi-yield-vs-defi-yield]]

**History/News**: [[defi-hacks-and-exploits]], [[2025-defi-renaissance]], [[2024-2025-major-defi-exploits]]

**AI x DeFi**: [[ml-defi-risk-models]], [[llm-defi-interfaces]], [[decentralized-ai]], [[artificial-intelligence]]

---

## Sources

- [[2026-04-15-defi-wiki-content-guide]] -- comprehensive DeFi research guide (43 references covering fundamentals, strategies, market state, security, AI integration, Solana DeFi, RWA, derivatives, regulation, and risks)
- [DeFiLlama — TVL dashboard](https://defillama.com/) — live TVL across all chains and protocols
- Market-state figures (TVL, Hyperliquid perp share, Cetus/Bybit/Balancer/GMX exploits) cross-checked and current as of 2026-06-11 (Perplexity sonar). Note: 0DTE-style headline TVL figures move fast; treat $ figures as point-in-time snapshots from late 2025-Q1 2026.
