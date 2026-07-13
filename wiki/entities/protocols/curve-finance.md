---
title: "Curve Finance"
type: entity
created: 2026-04-15
updated: 2026-06-20
status: excellent
tags: [crypto, defi, ethereum, liquidity]
entity_type: protocol
founded: 2020
website: "https://www.curve.finance"
aliases: ["Curve Finance", "Curve", "CRV", "Curve DAO", "crvUSD", "Curve DAO Token"]
related: ["[[defi]]", "[[ethereum]]", "[[uniswap]]", "[[balancer]]", "[[yearn]]", "[[aave]]", "[[lido]]", "[[decentralized-exchanges]]", "[[smart-contracts]]", "[[convex]]", "[[curve-dao-token]]", "[[stablecoins]]", "[[binance]]", "[[bnb]]"]
---

# Curve Finance

**Curve Finance** is a [[decentralized-exchanges|decentralized exchange]] optimized for extremely efficient stablecoin and pegged-asset swaps -- [[stablecoins]] (USDC/USDT/DAI), wrapped Bitcoin variants, and liquid staking derivatives (stETH/ETH) -- using a specialized bonding curve (the StableSwap invariant) that concentrates liquidity around a 1:1 price ratio. Launched on [[ethereum]] in January 2020 by Michael Egorov, Curve has become foundational infrastructure for [[defi]] -- its deep stablecoin liquidity is relied upon by lending protocols, yield aggregators, and arbitrage bots across the ecosystem, and it remains the venue of choice for large stablecoin swaps due to superior execution quality. At its peak in early 2022 Curve's TVL exceeded **$24 billion**, briefly making it the largest DeFi protocol by that metric. Curve's vote-escrow tokenomics (veCRV, introduced with the CRV token in August 2020) sparked the "Curve Wars," one of the most important yield-maximization dynamics in DeFi history.

---

## At a Glance

| Field | Detail |
|---|---|
| **Type** | [[decentralized-exchanges\|Decentralized exchange]] (AMM) + stablecoin issuer |
| **Category** | [[defi]] liquidity infrastructure |
| **Launched** | January 2020 ([[ethereum]] mainnet) |
| **Founder** | Michael Egorov |
| **Native token** | CRV (see [[curve-dao-token]]) — governance, gauge voting, fee share |
| **Stablecoin** | crvUSD (LLAMMA soft-liquidation mechanism) |
| **Governance** | Vote-escrow (veCRV): lock CRV up to 4 years for votes, boost, and 50% of swap fees |
| **Specialty** | Lowest-slippage swaps between pegged assets ([[stablecoins]], stETH/ETH, wrapped BTC) |
| **Canonical frontend** | curve.finance (migrated after the May 2025 `curve.fi` DNS hijack) |
| **Key dependency for** | [[lido]] stETH, [[yearn]] vaults, [[aave]], stablecoin issuers |

---

## Key Features

| Feature | Detail |
|---|---|
| **Model** | StableSwap AMM -- optimized for pegged-asset pairs with minimal slippage |
| **Chains** | [[ethereum]] (primary), [[arbitrum]], [[polygon]], Optimism, Base, Avalanche, and others |
| **Token** | CRV -- governance, yield boosting, gauge voting |
| **Governance Model** | Vote-escrow (veCRV): lock CRV for up to 4 years to vote on emissions and earn fees |
| **TVL** | ~$2-2.5B (early 2026; peak $24B in early 2022 -- verify on DefiLlama) |
| **crvUSD** | Curve's native stablecoin with LLAMMA liquidation mechanism |
| **Pool Factory** | Permissionless pool creation for anyone to deploy new Curve pools |

---

## How It Works

### StableSwap Invariant

Unlike [[uniswap]]'s constant-product formula (x*y=k), Curve uses a hybrid invariant that behaves like a constant-sum curve near the peg (extremely low slippage) and reverts to constant-product behavior as prices deviate. This makes Curve the lowest-slippage venue for swapping between assets that should trade near parity: USDC/USDT, DAI/USDC, stETH/ETH, WBTC/renBTC, etc.

### Liquidity Pools

- **3pool** (USDC/USDT/DAI) -- the foundational stablecoin pool, used as base liquidity for many metapools
- **Metapools** -- pair a new token against 3pool LP tokens, bootstrapping liquidity without fragmenting the underlying stable liquidity
- **Crypto Pools (v2)** -- Curve v2 introduced pools for volatile pairs (e.g., CRV/ETH, tricrypto) using a modified invariant with internal oracles
- **Factory Pools** -- permissionless pool creation; anyone can deploy a Curve pool for any pair

### crvUSD and LLAMMA

Curve launched **crvUSD**, its native stablecoin, backed by crypto collateral with a novel liquidation mechanism called LLAMMA (Lending-Liquidating AMM Algorithm). Unlike traditional lending protocols where liquidation is a discrete event, LLAMMA gradually converts collateral into stablecoins as the price drops ("soft liquidation") and reconverts as the price recovers. This reduces the severity of liquidation events but introduces continuous conversion costs to borrowers.

---

## The Curve Wars: veCRV, Convex, and Votium

The **Curve Wars** are the competitive dynamics around directing CRV token emissions to specific liquidity pools. This is arguably the single most important yield strategy ecosystem in DeFi.

### How It Works

1. **CRV emissions** are distributed to liquidity pools via "gauges" -- each pool has a gauge that receives a share of weekly CRV emissions
2. **veCRV holders** vote on how emissions are allocated across gauges. More votes for your pool = more CRV rewards = higher APY = more liquidity attracted
3. **Locking CRV** for up to 4 years grants veCRV, which provides: governance voting power, a share of protocol trading fees (50% of all swap fees), and a "boost" of up to 2.5x on personal CRV farming rewards
4. Protocols that need deep Curve liquidity (e.g., [[lido]] for stETH, FRAX for FRAX, [[aave]] for GHO) compete to accumulate veCRV voting power to direct emissions to their pools

### Convex Finance

**Convex Finance** (CVX token) is a protocol built on top of Curve that aggregates veCRV voting power. Instead of individually locking CRV for 4 years, users deposit CRV into Convex (receiving cvxCRV) and benefit from Convex's massive collective veCRV position. Convex controls a dominant share of all veCRV -- making CVX token holders effectively the kingmakers of Curve gauge votes. Staking CVX allows participation in gauge voting with Convex's aggregated power.

### Votium and Bribe Markets

**Votium** is a bribe marketplace where protocols pay CVX holders to vote for their preferred Curve gauges. If a protocol wants deep liquidity in its Curve pool, it pays Votium bribes (in USDC, their native token, etc.) to CVX voters who direct emissions there. This creates a measurable "price of liquidity" in DeFi:

- Protocol pays $X in bribes → CVX holders direct CRV emissions to the protocol's pool → CRV rewards attract LPs → deeper liquidity forms
- The bribe yield for CVX holders (8-25% APY from bribes alone, on top of CRV yield) makes this one of the highest-yield strategies in DeFi that is backed by real economic demand rather than pure token inflation

---

## Trading Strategies

### 1. veCRV/Convex Yield Farming (Moderate difficulty -- THE Curve strategy)

- **Mechanism**: Buy CVX, stake it, participate in gauge voting via Votium to earn bribes + CRV + CVX rewards
- **Example**: $30,000 in CVX staked → vote on high-bribe gauges via Votium → earn $10,000-$20,000/year in mixed rewards (CRV, CVX, USDC bribes, protocol tokens)
- **APY**: 15-50% depending on bribe market conditions and gauge selection (realistic sustained: 20-30% after gas)
- **Capital requirement**: $20,000+ to justify gas costs and Votium interaction overhead
- **Difficulty**: Intermediate -- requires understanding gauge voting, bribe markets, and weekly vote optimization
- **Why it works**: Protocols have genuine economic demand for Curve liquidity. Bribes represent real money being paid for a real service (directing emissions). This is not pure inflationary yield
- (Source: [[2026-04-22-perplexity-defi-trading-strategies-sweep]])

### 2. Stablecoin LP on Curve (Very low difficulty, baseline yield)

- **Mechanism**: Deposit stablecoins (USDC/USDT/DAI) into 3pool or other stable pools, earn swap fees + CRV emissions
- **APY**: 3-6% from swap fees alone; 8-15% with CRV incentives (if boosted via veCRV)
- **Capital requirement**: $5,000+ on L2; $10,000+ on mainnet
- **Difficulty**: Beginner -- deposit and earn
- **Risk**: Minimal impermanent loss for stable pairs (unless a stablecoin depegs); smart contract risk
- **Comparison**: Higher yield than [[aave]] supply-side for stablecoins, with slightly more complexity
- (Source: [[2026-04-22-perplexity-defi-trading-strategies-sweep]])

### 3. Bribe Farming via Votium (Moderate difficulty)

- **Mechanism**: Accumulate CVX or vlCVX (vote-locked CVX), vote for gauges offering the highest bribe yield per CVX
- **APY**: 8-25% pure bribe yield (on top of base CRV/CVX staking yield)
- **Capital requirement**: $20,000+ for meaningful bribe income
- **Difficulty**: Intermediate -- requires tracking bribe markets, voting weekly, and optimizing gauge selection
- **Tools**: Votium dashboard, Llama Airforce (bribe analytics), DefiLlama yields section
- **Profitability**: $2,000-$5,000/month on a $50,000 position in good bribe market conditions
- (Source: [[2026-04-22-perplexity-defi-trading-strategies-sweep]])

### 4. crvUSD Leverage Looping (High difficulty, dangerous)

- **Mechanism**: Deposit collateral, mint crvUSD, deploy crvUSD into Curve pools for yield, use yield to mint more crvUSD (recursive leverage)
- **Example**: $50,000 collateral → mint $30,000 crvUSD → farm $30,000 in Curve pools → use LP tokens as additional collateral → mint more
- **APY**: 20-60% gross (before liquidation and LLAMMA conversion costs)
- **Capital requirement**: $50,000+
- **Difficulty**: Advanced -- requires continuous monitoring of soft-liquidation ranges and LLAMMA conversion costs
- **Risk**: EXTREME. LLAMMA soft-liquidation erodes capital during volatility even if final liquidation is avoided. One sharp collateral decline can wipe the leveraged position entirely
- (Source: [[2026-04-22-perplexity-defi-trading-strategies-sweep]])

---

## How Curve Is Used — Summary

| User | Use of Curve | Why Curve specifically |
|---|---|---|
| Large stablecoin swappers | Execute size between USDC/USDT/DAI | Lowest slippage near the peg (StableSwap invariant) |
| Passive LPs | Deposit into stable pools for fees + CRV | Minimal impermanent loss on pegged pairs |
| Yield maximizers | veCRV / Convex / Votium bribe farming | Real economic demand for emissions, not pure inflation |
| Arbitrage bots | Route flash-loan arbs through deep pools | Deepest pegged-asset liquidity; integrates with [[aave]] |
| Protocols ([[lido]], issuers) | Bootstrap liquidity for their token via gauges | Curve Wars flywheel directs emissions to their pool |
| Borrowers | Mint crvUSD against collateral | LLAMMA soft-liquidation smooths liquidation risk |

For the trading-strategy mechanics behind these rows, see the **Trading Strategies** section above. For the token itself, see [[curve-dao-token]].

## Risk Framework

### CRV Token Inflation and Dilution

CRV has a high inflation rate (~20% annually in early years, declining over time). If CRV price declines faster than emissions decrease, the real yield from CRV farming compresses. The token's value is ultimately supported by protocol revenue (swap fees) and bribe demand. A sustained collapse in CRV price would undermine the entire Curve Wars yield ecosystem.

### Smart Contract Exploits

Curve suffered a major exploit in July 2023 when a Vyper compiler bug was exploited across multiple Curve pools, resulting in ~$70M+ in losses. The pools affected used older Vyper versions. This demonstrated that Curve's complexity (custom AMM math, Vyper language, factory pools) creates meaningful smart contract surface area. Curve has since undergone additional audits, but the incident is a reminder that even battle-tested protocols carry risk.

### Founder Concentration Risk

The July 2023 exploit also triggered a near-systemic crisis because founder Michael Egorov had pledged roughly 427-460 million CRV (close to half the circulating supply at the time) as collateral for over $100M in stablecoin loans across multiple lending protocols. A CRV crash threatened cascading liquidations across DeFi; OTC sales to investors defused the situation. In **June 2024**, falling CRV prices did force the liquidation of Egorov's remaining CRV-backed loan positions across several protocols, after which he stated all positions were closed and contributed to covering resulting bad debt. The episode is the canonical example of insider-leverage concentration risk in DeFi governance tokens.

### Gauge Voting Manipulation

Whales holding large CVX or veCRV positions can direct emissions to pools that benefit them at the expense of smaller LPs. Governance attacks (accumulating enough voting power to pass harmful proposals) are a theoretical risk, though the 4-year lock-up mitigates short-term manipulation.

### crvUSD / LLAMMA Risk

LLAMMA's soft-liquidation mechanism is novel and less battle-tested than traditional liquidation models. During high-volatility periods, the continuous conversion between collateral and crvUSD generates losses for borrowers ("soft-liquidation losses") that can accumulate significantly even without full liquidation. Borrowers should model these conversion costs before deploying capital.

### Stablecoin Depeg Risk

Curve pools are optimized for pegged assets. If a stablecoin in a pool depegs (as USDC briefly did during the Silicon Valley Bank crisis in March 2023), Curve LPs absorb disproportionate losses as arbitrageurs drain the "good" stablecoin and leave the pool holding the depegged asset.

---

## Timeline of Key Events (2023-2026)

- **2023-03** — USDC depeg (SVB collapse) stress-tested Curve's stable pools; LPs absorbed depeg losses.
- **2023-07** — Vyper compiler exploit drains ~$70M+ from multiple pools; Egorov collateral crisis (see Risk Framework).
- **2024-06** — Egorov's remaining CRV-backed loans liquidated as CRV fell; positions closed and bad debt addressed.
- **2025-03** — Llamalend / crvUSD ecosystem continues expanding as Curve's lending arm.
- **2025-05-05** — Curve's official X account hijacked to post a phishing "CRV airdrop."
- **2025-05-12** — DNS hijack of the `curve.fi` domain redirected users to a wallet-drainer clone; the protocol itself was unaffected. Curve migrated its canonical frontend to **curve.finance**. CRV traded ~$0.69 at the time.
- **2025-Q3** — DAO approved **Yield Basis**, an Egorov-founded venture routing crvUSD liquidity into Bitcoin pools (WBTC, cbBTC, tBTC; initially capped at $10M each) designed to neutralize impermanent loss, with partial revenue back to veCRV holders.
- **2025-12-15** — DAO proposal for a $6.6M grant funding a 25-person team for major 2026 upgrades.
- **2026-03-05** — Executed proposal adding CRV and YB rewards to PegKeeper pools to stabilize crvUSD.
- **2026-05-28** — A StakeDAO exploit rippled into the Curve ecosystem.
- **2026-06-02** — [[binance|Binance]] delisted the CRV/BTC pair.

## Key Metrics (as of mid-2026)

| Metric | Approximate Range | Notes |
|---|---|---|
| **TVL** | ~$2.0-2.5B (primarily stablecoin pairs) | ~$2.08B as of 2026-02-26; peak $24B early 2022. Verify on DefiLlama |
| **Daily Volume** | $200M-$1B | Stables are high-volume, low-slippage |
| **CRV Price** | ~$0.20 (June 2026 CoinMarketCap snapshot; some venues quoted higher) | Down from ~$0.69 in May 2025; ATH $60.50 (2020-08-14). Verify on CoinGecko |
| **CRV Circulating Supply** | ~1.41B CRV | Market cap roughly $0.3-0.6B depending on snapshot |
| **CVX Price** | ~$1-2 range (2025-2026) | See [[convex]] |
| **crvUSD** | Two crvUSD pools rank in Curve's top 10 by volume (2026) | Backbone for Llamalend and Yield Basis |
| **veCRV Locked** | ~40-50% of circulating CRV | Check Dune Analytics |
| **Convex veCRV Share** | Dominant position (~40%+ of all veCRV) | Verify on Convex dashboard |

---

## Competitive Position

| Competitor | Curve Advantage | Competitor Advantage |
|---|---|---|
| [[uniswap]] | Far lower slippage on stablecoin/pegged pairs; veCRV yield wars create deep liquidity incentives | Uniswap dominates volatile pair volume; simpler UX; larger total TVL |
| [[balancer]] | More established in stable/pegged asset swaps; deeper stablecoin liquidity | Balancer's weighted pools offer more flexibility; Aura Finance mirrors Convex model |
| Maverick | Established network effects and integrations | Maverick offers directional liquidity similar to Uniswap v3 with better capital efficiency |

Curve's moat is the **veCRV/Convex flywheel**: protocols need Curve liquidity, so they pay bribes, which sustains high yields, which attracts LPs, which deepens liquidity. This self-reinforcing cycle is unique to Curve and has no direct equivalent elsewhere in DeFi. [[yearn]] vaults, [[lido]] stETH pools, and numerous stablecoin issuers all depend on Curve liquidity.

---

## CRV Tokenomics

| Parameter | Detail |
|---|---|
| **Max Supply** | 3.03B CRV |
| **Initial Distribution** | 62% to LPs, 30% to shareholders, 5% to early users, 3% to employees |
| **Emission Schedule** | Declining ~15% annually; front-loaded inflation |
| **Lock Duration** | 1 week to 4 years (longer lock = more veCRV per CRV) |
| **Fee Sharing** | 50% of all swap fees to veCRV holders; 50% to LPs |

---

## Related

- [[defi]] -- The broader DeFi ecosystem
- [[ethereum]] -- Primary chain for Curve
- [[convex]] -- veCRV aggregator at the center of the Curve Wars
- [[curve-dao-token]] -- the CRV governance/utility token in detail
- [[crv]] -- CRV token (redirect to this page)
- [[binance]] -- centralized venue that delisted the CRV/BTC pair (June 2026)
- [[bnb]] -- comparison: a major centralized-exchange-linked token
- [[uniswap]] -- Primary competitor for DEX volume
- [[balancer]] -- Competing AMM with weighted pools
- [[yearn]] -- Yield aggregator that routes significant capital through Curve
- [[aave]] -- Lending protocol; flash loan arbitrage frequently uses Curve pools
- [[lido]] -- stETH/ETH pool on Curve is one of the deepest liquidity venues
- [[decentralized-exchanges]] -- Broader DEX category
- [[stablecoins]] / [[stablecoin-depegs]] -- the asset class Curve is built around
- [[chainlink]] -- Oracle infrastructure for crvUSD
- [[2023-03-usdc-svb-depeg]] -- the depeg event that stress-tested Curve pools

---

## Sources

- Curve DAO governance portal — https://www.curve.finance/dao/
- DefiLlama, "Curve Finance TVL, Fees, Revenue & Volume" — https://defillama.com/protocol/curve-finance
- Decrypt, "Curve Finance Hit by DNS Record Attack, Warns Users to Avoid Main Site" (May 2025) — https://decrypt.co/319414/curve-finance-dns-record-attack
- Protos, "Curve Finance warns users after website and X account hacks" (May 2025) — https://protos.com/curve-finance-warns-users-after-website-and-x-account-hacks/
- CoinMarketCap, "Latest Curve DAO Token News" (June 2026 snapshots: CRV ~$0.20; Dec 2025 grant; Mar 2026 PegKeeper rewards; May 2026 StakeDAO ripple; June 2026 Binance CRV/BTC delisting) — https://coinmarketcap.com/cmc-ai/curve-dao-token/latest-updates/
- CoinDCX, "What is Curve DAO (CRV) Token? A Beginner's Guide to Curve Finance in 2026" — https://coindcx.com/blog/cryptocurrency/what-curve-dao-token/ (Yield Basis, crvUSD status)
- Verified via Perplexity (sonar) and web search, 2026-06-10
- (Source: [[2026-04-22-perplexity-defi-trading-strategies-sweep]]) — trading-strategy sections
