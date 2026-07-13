---
title: "GMX"
type: entity
created: 2026-04-06
updated: 2026-06-21
status: excellent
tags: [crypto, defi, exchange, futures, derivatives]
entity_type: exchange
founded: 2021
website: "https://gmx.io"
aliases: ["GMX", "GLP", "GMX-Solana"]
related: ["[[decentralized-exchanges]]", "[[perpetual-futures]]", "[[arbitrum]]", "[[defi]]", "[[dydx]]", "[[hyperliquid]]", "[[chainlink]]", "[[uniswap]]", "[[aave]]"]
---

# GMX

**GMX** is a decentralized [[perpetual-futures|perpetual futures]] and spot exchange operating on [[arbitrum|Arbitrum]] and Avalanche. It pioneered a unique liquidity model where traders trade against a multi-asset liquidity pool (GLP/GM) rather than matching with counterparties, enabling zero-slippage trades on major pairs while offering liquidity providers a share of trading fees and trader losses. GMX was one of the earliest protocols to generate "real yield" -- fees paid by actual traders rather than inflationary token emissions -- making it a benchmark for sustainable [[defi|DeFi]] revenue models and a defining example of the pool-as-counterparty design among [[decentralized-exchanges|decentralized exchanges]].

---

## At a Glance

| Attribute | Detail |
|---|---|
| **Type** | Decentralized perp + spot exchange (pool-counterparty model) |
| **Launched** | September 2021 (Arbitrum); evolved from earlier Gambit Financial on BSC |
| **Primary chain** | [[arbitrum|Arbitrum]] One; also Avalanche C-Chain, Solana (GMX-Solana) |
| **Governance** | GMX DAO; GMX token holders vote on listings, fee splits, treasury |
| **Native tokens** | GMX (governance + fee share), GLP (v1 LP), GM (v2 per-market LP), GLV (v2 LP vaults) |
| **Counterparty model** | Traders vs. the GLP/GM liquidity pool, not an order book |
| **Pricing** | [[chainlink]] oracle feeds + keeper execution (low-MEV) |
| **Headline products** | Perpetuals (up to 100x), spot swaps, LP/yield vaults |
| **Revenue model** | "Real yield" — fees in ETH/AVAX split between stakers and LPs |
| **Closest peers** | [[hyperliquid]], [[dydx]], Synthetix Perps, Jupiter Perps |

---

## Key Features

| Feature | Detail |
|---|---|
| **Chains** | [[arbitrum|Arbitrum]] (primary), Avalanche, Solana (GMX-Solana) |
| **Model** | Traders vs pool (GLP/GM) -- not a traditional order book |
| **Leverage** | Up to 100x on major pairs |
| **Tokens** | GMX (governance/revenue share), GLP (v1 liquidity pool), GM (v2 liquidity pools) |
| **Fee Distribution** | 30% to GMX stakers, 70% to GLP/GM holders |
| **Markets** | BTC, ETH, and select altcoin perps + spot swaps |
| **Oracle** | [[chainlink]] price feeds (minimizes frontrunning and MEV) |

---

## The GLP/GM Model

GMX's liquidity model is distinctive:
- **Liquidity providers** deposit assets into the GM pool (v2) and earn fees from every trade, plus a share of trader losses
- **Traders** open leveraged positions against the pool using [[chainlink]] oracle prices (minimizing frontrunning)
- When traders profit, the pool pays out; when traders lose, the pool absorbs the gains
- This creates a dynamic where **LP returns are inversely correlated with trader PnL** -- an important consideration for both sides
- Historically, traders as a group lose money over time (consistent with leverage statistics across all markets), making GLP/GM provision profitable on average

### GMX v1 vs v2

| Feature | v1 (GLP) | v2 (GM) |
|---|---|---|
| **Pool Structure** | Single multi-asset pool (GLP) | Isolated per-market pools (e.g., GM-BTC/USD, GM-ETH/USD) |
| **Risk Exposure** | LP exposed to all listed assets in one pool | LP chooses specific market exposure |
| **Fee Structure** | 70% of all protocol fees to GLP | 63% of fees to GM LPs, 27% to GMX stakers, 10% to protocol |
| **Capital Efficiency** | Lower (capital spread across all assets) | Higher (capital concentrated per market) |
| **Price Impact** | Zero slippage on supported pairs | Price impact model for larger trades |

### GLV — GMX Liquidity Vaults (v2)

GMX v2 also offers **GLV (GMX Liquidity Vaults)** — auto-rebalancing vaults that spread capital across multiple GM pools to give LPs diversified, passively-managed market exposure rather than picking a single GM market. GLV abstracts the per-market choice of raw GM tokens while retaining the v2 fee economics, and was one of the assets singled out for additional DAO incentives during the post-exploit recovery (see [[#July 2025 Exploit ($42M)|July 2025 exploit]]).

### Execution Architecture (Keepers + Oracles)

Unlike an automated market maker (AMM) such as [[uniswap]], GMX does **not** price trades off an on-chain reserve curve. Instead:

- Orders are submitted as **two-step requests** (request → execution) and settled by **keepers** against [[chainlink]] low-latency oracle prices, which is what eliminates AMM-style sandwich/front-running on the price leg.
- v2 adds an **execution price-impact model** so that large trades that skew a market's open interest pay a spread, protecting GM LPs from being run over by one-sided flow.
- **Funding** and **borrowing** fees are charged on open positions, rebalancing long/short open interest and compensating LPs for the inventory they warehouse.

This keeper-plus-oracle design is GMX's core technical differentiator versus order-book DEXs like [[hyperliquid]] and [[dydx]]: it trades raw latency/price-discovery quality for self-custody and MEV resistance.

---

## How Traders Use GMX

| User | Goal | Mechanism |
|---|---|---|
| **Leveraged traders** | Directional BTC/ETH/alt exposure up to 100x | Open perps vs. the pool at oracle price; pay funding + borrow fees |
| **Spot swappers** | Self-custody swaps without an AMM curve | Swap against GLP/GM inventory at oracle price |
| **Passive LPs** | "Real yield" on idle capital | Mint GLP / GM / GLV; earn fee share + trader-loss capture |
| **GMX stakers** | Protocol cash-flow exposure | Stake GMX for ETH/AVAX fee share + esGMX |
| **Yield engineers** | Fixed-rate or leveraged LP yield | Tokenize GM/GLP via [[pendle]] PT/YT; loop LP tokens as collateral |
| **Funding arbitrageurs** | Capture CEX-vs-DEX funding spread | Delta-neutral long/short across GMX and a CEX perp |

---

## Trading Strategies

### 1. GM Pool Liquidity Provision (Moderate difficulty, "real yield")

- **Mechanism**: Deposit assets into GM pools (e.g., ETH + USDC into the ETH/USD GM pool). Earn fees from every leveraged trade on that market + absorb trader losses (when traders lose) or pay out trader gains (when traders win)
- **APY**: 15-30%+ historically from organic trading fees (not token emissions). Varies significantly with trading volume and trader PnL
- **Capital requirement**: $10,000+ (Arbitrum gas is cheap, but meaningful yield requires meaningful capital)
- **Difficulty**: Intermediate -- requires understanding of the "LP as counterparty to leveraged traders" dynamic
- **Why it works**: Leverage traders lose money on average (well-documented across all markets). By taking the other side of aggregate trader positions, GM LPs collect this structural edge. However, this is NOT risk-free: during strong trending markets, traders can profit collectively, and GM LPs lose
- **Risk**: Extended trending markets (e.g., BTC rallying 50%+ without pullback) cause GM LPs to pay out more than they collect. This is the core risk of the model: LP returns are negatively correlated with directional market moves that benefit traders
- (Source: [[2026-04-22-perplexity-defi-trading-strategies-sweep]])

### 2. esGMX Staking (Low difficulty, passive)

- **Mechanism**: Stake GMX tokens to receive 30% of all protocol fees (paid in ETH/AVAX) + esGMX (escrowed GMX) token rewards. esGMX can be vested over 12 months into GMX or staked for additional yield
- **APY**: 5-15% from real fee revenue (ETH/AVAX) + esGMX rewards
- **Capital requirement**: Any amount of GMX tokens
- **Difficulty**: Beginner -- stake and earn
- **Advantage**: Fee revenue is paid in ETH, not in the protocol's own token, making it "real yield" rather than inflationary rewards
- **Risk**: GMX token price risk; fee revenue varies with trading volume; esGMX vesting requires 12-month lock

### 3. Leveraged Perp Trading on GMX (High difficulty)

- **Mechanism**: Open long or short leveraged positions on BTC, ETH, and altcoins using GMX's oracle-based execution. Benefit from zero frontrunning (oracle prices, not AMM prices) and low fees
- **Capital requirement**: $1,000+ (Arbitrum gas is minimal)
- **Difficulty**: Advanced -- leveraged trading is inherently high-risk
- **Advantage over CEX perps**: Self-custody; no KYC; no counterparty risk (protocol is the counterparty); oracle-based pricing reduces MEV/sandwich risk
- **Disadvantage**: Limited markets (fewer pairs than [[hyperliquid]] or [[dydx]]); oracle latency can be exploited; funding rates may differ from CEX markets
- **Risk**: Leverage amplifies losses; liquidation risk; oracle price deviation from spot can cause unexpected liquidations

### 4. GMX Funding Rate Arbitrage (Expert difficulty)

- **Mechanism**: When GMX funding rates diverge significantly from CEX perpetual funding rates, arbitrage the spread. Go long on the venue with lower funding and short on the venue with higher funding, collecting the rate differential
- **Capital requirement**: $50,000+ (need to maintain margin on both venues)
- **Difficulty**: Expert -- requires cross-venue position management and funding rate monitoring
- **Risk**: Funding rates can shift quickly; execution risk between CEX and DEX; liquidation risk if positions move against you before funding accrues

---

## July 2025 Exploit ($42M)

On **2025-07-09** an attacker exploited a **reentrancy vulnerability in GMX v1's GLP pool on Arbitrum**, manipulating short average prices for BTC to redeem more than deposited, draining roughly **$40-42 million**. Key facts:

- GMX **halted v1 trading and GLP minting/redemption**; **GMX v2 (GM pools) was not affected** and continued operating.
- GMX offered a **10% white-hat bounty (~$5M)**; the attacker accepted and **returned ~$40.5M** within days.
- GMX ran a **~$44M distribution plan** to compensate affected GLP holders, combining recovered funds with ~$2M from the GMX treasury; the DAO added $500K of incentives for users holding GLV tokens for 3 months.
- The GMX token dropped as much as ~28% on the news; protocol TVL fell from ~$480M to ~$409M before rebounding above **$600M** after the funds were returned.

Lessons for traders/LPs: legacy-version contracts (v1) remained a live attack surface years after v2 launched; "unaffected" newer versions can still suffer token-price and TVL contagion; and white-hat bounty resolution has become a common outcome pattern that compresses the post-hack drawdown window.

---

## History and Governance

| Period | Milestone |
|---|---|
| Pre-2021 | Origins in **Gambit Financial** (BSC), an early pool-counterparty perp experiment |
| Sep 2021 | **GMX v1 (GLP)** launches on [[arbitrum|Arbitrum]] — single multi-asset pool, zero-slippage oracle pricing |
| 2022 | Avalanche deployment; GMX becomes the flagship of the **"real yield"** narrative as token emissions across DeFi collapse |
| 2022-2023 | GLP staking among the most-copied DeFi LP strategies; numerous forks (Mummy, Vela, Level, etc.) |
| 2023-2024 | **GMX v2 (GM pools)** rolls out isolated per-market pools, price-impact model, and GLV vaults |
| Jul 2025 | **v1 GLP reentrancy exploit (~$42M)**; funds returned via white-hat bounty; ~$44M GLP distribution plan |
| 2025-2026 | **GMX-Solana** extends the GM model off-EVM; v2 becomes the primary venue |

GMX is governed by the **GMX DAO**: token holders vote (via Snapshot and on-chain mechanisms) on new market listings, fee-split parameters, treasury deployment, and incentive programs. Governance and the multisig that administers contracts are a centralization vector worth noting — listing decisions and parameter changes are not fully automated.

---

## 2025-2026 Status

- **Multi-chain**: GMX is live on Arbitrum One, Avalanche C-Chain, and **Solana mainnet** (GMX-Solana), extending the GM pool model beyond the EVM.
- **Competitive position**: [[hyperliquid|Hyperliquid]] dominates DEX perps (~70-80% share by August 2025), with GMX, [[dydx|dYdX]], and newer entrants (e.g., Aster) competing for the remainder. GMX's differentiation remains oracle-priced, pool-counterparty execution and "real yield" LP economics rather than CLOB liquidity.
- **TVL**: roughly $400-600M+ range through H2 2025 post-exploit recovery (verify current figure on DefiLlama).

---

## Risk Framework

### LP Counterparty Risk (Trader PnL)

The fundamental risk of GM/GLP provision is that **you are the counterparty to leveraged traders**. If traders collectively profit (during strong trending markets), LPs pay out those profits. Historical data shows traders lose on average, but there are extended periods where traders win, creating drawdowns for LPs. This is analogous to selling insurance: profitable on average, but with occasional large payouts.

### Oracle Risk

GMX relies on [[chainlink]] oracle prices for trade execution. If an oracle feed is delayed, manipulated, or temporarily incorrect, traders can exploit the discrepancy (e.g., executing a trade at an oracle price that diverges from the true market price). GMX has implemented execution price impact and keeper mechanisms to mitigate this, but oracle dependency remains a structural risk.

### Smart Contract Risk

GMX's v2 contracts are significantly different from v1, introducing new attack surface. The isolated GM pool model is more complex than the original GLP model. Audits have been completed, but audits are not a guarantee: the **July 2025 $42M reentrancy exploit hit the older, "battle-tested" v1 GLP contracts**, not v2 — demonstrating that legacy deployments with live TVL remain a tail risk even after a protocol's focus moves to newer versions.

### Liquidity Concentration on Arbitrum

GMX's primary deployment is on [[arbitrum]], making it dependent on Arbitrum's sequencer uptime and security. During Arbitrum outages (which have occurred), GMX positions cannot be managed, potentially leading to forced liquidations. Arbitrum's centralized sequencer is a single point of failure for GMX traders and LPs.

### Competition from Order Book DEXs

[[hyperliquid]] and [[dydx]] offer order book-based perpetual trading with deeper liquidity on more markets, professional trading interfaces, and faster execution. GMX's oracle-based pool model is unique but may lose market share to order book models that provide better price discovery and lower latency.

---

## Key Metrics

| Metric | Approximate Range | Notes |
|---|---|---|
| **TVL** | ~$400-600M+ (post July-2025 exploit recovery) | Verify on DefiLlama |
| **Daily Trading Volume** | $200M-$1B+ | Highly variable with market conditions |
| **GMX Price** | $30-$80 range historically | Verify on CoinGecko |
| **GMX Market Cap** | ~$300M-$700M | Verify on CoinGecko |
| **Protocol Fee Revenue** | $50-200M+ annualized | Verify on Dune Analytics |
| **Open Interest** | $200M-$500M+ | Verify on GMX stats dashboard |
| **GM Pool APY** | 15-30% (varies by market and period) | Check GMX dashboard |

---

## Competitive Position

| Competitor | GMX Advantage | Competitor Advantage |
|---|---|---|
| [[hyperliquid]] | "Real yield" for LPs (fee revenue, not emissions); established on Arbitrum | Order book model with deeper liquidity; more trading pairs; purpose-built L1 chain |
| [[dydx]] | Oracle-based pricing reduces MEV; LP as counterparty model | Full order book; more professional interface; more trading pairs; cosmos-based chain |
| Synthetix Perps (via Kwenta) | More established track record | Synthetix offers synthetic asset exposure beyond perps |
| Centralized exchanges | Self-custody; no KYC; transparent fee distribution; oracle pricing reduces frontrunning | Far deeper liquidity; lower fees; faster execution; more instruments |

GMX's niche is **"real yield" DeFi perps** -- the protocol generates meaningful fee revenue from actual trading activity, which is distributed to GMX stakers and GM/GLP holders. This model attracted significant capital during the "real yield" narrative of 2022-2023. The v2 transition to isolated GM pools improves capital efficiency and risk management for LPs.

---

## Trading Relevance

- GMX demonstrated that DeFi perps could attract significant volume with a pool-based model, inspiring many forks
- GLP/GM yield was one of the most popular "real yield" strategies during 2022-2023, earning 15-30% APR from organic trading fees
- GMX competes with [[dydx]] and [[hyperliquid]] for decentralized derivatives volume
- The oracle-based pricing model reduces MEV risk but introduces oracle manipulation risk
- GMX is a major contributor to [[arbitrum|Arbitrum's]] TVL and ecosystem gravity
- [[pendle]] offers PT/YT tokenization of GLP/GM tokens, enabling fixed-rate yield on GMX LP positions

---

## Related

- [[arbitrum]] -- GMX's primary chain
- [[dydx]] -- Competing decentralized perps exchange
- [[hyperliquid]] -- Leading order book-based DEX perps platform
- [[perpetual-futures]] -- The instrument GMX specializes in
- [[decentralized-exchanges]] -- Broader DEX ecosystem
- [[chainlink]] -- Oracle infrastructure GMX depends on for price feeds
- [[pendle]] -- Enables yield tokenization of GLP/GM positions
- [[defi]] -- The broader DeFi ecosystem

---

## Sources

- (Source: [[2026-04-22-perplexity-defi-trading-strategies-sweep]])
- Halborn — "Explained: The GMX Hack (July 2025)": https://www.halborn.com/blog/post/explained-the-gmx-hack-july-2025
- The Record — "Hacker returns stolen GMX funds for bounty": https://therecord.media/hacker-returns-stolen-gmx-bounty
- CoinCentral — "GMX Concludes $44M Distribution Plan for Affected GLP Holders": https://coincentral.com/gmx-concludes-44m-distribution-plan-for-affected-glp-holders/
- Unchained — "GMX Loses $40 Million in V1 Exploit, Halts Trading and Minting": https://unchainedcrypto.com/gmx-loses-40-million-in-v1-exploit-halts-trading-and-minting/
- DefiLlama — GMX protocol metrics: https://defillama.com/protocol/gmx
- Web verification via Perplexity/WebSearch, 2026-06-10.
