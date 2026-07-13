---
title: "Uniswap"
type: entity
created: 2026-04-06
updated: 2026-06-21
status: excellent
tags: [crypto, defi, ethereum, liquidity]
entity_type: protocol
founded: 2018
headquarters: "New York, USA (Uniswap Labs)"
website: "https://uniswap.org"
aliases: ["UNI", "Uniswap Labs", "Uniswap Protocol"]
related: ["[[decentralized-exchanges]]", "[[defi]]", "[[ethereum]]", "[[smart-contracts]]", "[[arbitrum]]", "[[curve-finance]]", "[[balancer]]", "[[aave]]", "[[chainlink]]"]
---

# Uniswap

**Uniswap** is the largest [[decentralized-exchanges|decentralized exchange (DEX)]] by trading volume, pioneering the **automated market maker (AMM)** model that became the standard for on-chain token swapping. Launched on [[ethereum]] in 2018 by Hayden Adams, Uniswap enables permissionless token listing and trading through liquidity pools governed by [[smart-contracts]]. The protocol crossed **$3 trillion in all-time volume on Ethereum mainnet** (announced 5 May 2026) and roughly **$4 trillion all-time across all chains** by mid-2026, with ~119 million cumulative swappers and ~$2.6B TVL (Uniswap Labs; CoinLaw). Since the December 2025 "UNIfication" vote, UNI has a live protocol fee switch and burn mechanism, making it a fee-accruing, deflationary asset rather than a pure governance token.

---

## At a Glance

| Attribute | Detail |
|---|---|
| **Type** | [[decentralized-exchanges\|Decentralized exchange (DEX)]] / [[automated-market-maker\|automated market maker (AMM)]] |
| **Founded** | 2018 by Hayden Adams |
| **Operator** | Uniswap Labs (New York, USA); protocol governed by the Uniswap DAO |
| **Home chain** | [[ethereum]] mainnet; deployed across many L2s + its own L1-anchored L2, Unichain |
| **Governance token** | UNI -- now fee-accruing and deflationary post-UNIfication |
| **Live versions** | v3 (concentrated liquidity) and v4 (hooks, singleton) are active; v2 still operational |
| **Custody** | Non-custodial; self-custody via user wallet |
| **KYC** | None at the protocol layer (permissionless) |
| **Primary use** | Spot token swaps, price discovery for new ERC-20s, LP yield |
| **Position** | Largest DEX by volume; most-forked protocol in [[defi]] history |

---

## Key Features

| Feature | Detail |
|---|---|
| **Model** | Automated Market Maker (AMM) -- constant product formula |
| **Chains** | [[ethereum]], [[arbitrum]], [[polygon]], Optimism, Base, BNB Chain, Unichain, and others |
| **Token** | UNI -- governance token |
| **Version** | v3 (concentrated liquidity) and v4 (hooks, launched 31 January 2025) are the active generations |
| **Permissionless** | Anyone can create a new trading pair by providing initial liquidity |
| **TVL** | ~$2.6B across all chains as of mid-2026 (verify on DefiLlama) |
| **L2** | Unichain — Uniswap's own Ethereum L2, mainnet live 11 February 2025 |

---

## How It Works

Uniswap is an [[automated-market-maker|automated market maker (AMM)]]: instead of matching buyers and sellers in an order book, it prices trades algorithmically against pooled liquidity. Liquidity providers (LPs) deposit two tokens into a pool; traders swap against the pool and pay a fee that accrues to LPs. The original v2 design used the **constant product formula** $x \cdot y = k$, where the product of the two reserve balances stays constant, so every trade moves the price along a hyperbola.

Uniswap v3 uses **concentrated liquidity** -- liquidity providers (LPs) allocate capital to specific price ranges rather than across the entire curve, dramatically improving capital efficiency. Traders swap tokens against these pools, paying a fee (typically 0.3% or 0.05%) that is distributed to LPs.

The protocol requires no sign-up, no KYC, and no order matching -- trades execute instantly against available pool liquidity.

### AMM Architecture Across Versions

| Version | Launched | Core Innovation | Capital Efficiency | Trader Implication |
|---|---|---|---|---|
| **v1** | Nov 2018 | ETH-paired pools only; constant product | Low | Proof of concept; deprecated |
| **v2** | May 2020 | Arbitrary ERC-20/ERC-20 pairs; flash swaps; on-chain price oracle (TWAP) | Low (full-range LP) | Made Uniswap the default listing venue; v2 still carries the protocol fee post-UNIfication |
| **v3** | May 2021 | Concentrated liquidity; multiple fee tiers; range orders | High (10-4000x v2 for tight ranges) | LPs become active range managers; capital-efficient but exposed to [[impermanent-loss]] amplification |
| **v4** | Jan 2025 | Hooks; singleton contract; native ETH; flash accounting | High + programmable | Custom pool logic (dynamic fees, on-chain limit orders, TWAMM); lower gas via singleton |

See [[automated-market-maker]] and [[constant-product-amm]] for the underlying math, and [[impermanent-loss]] for the LP risk that all AMM versions share.

### Fee Tiers

Uniswap v3 offers multiple fee tiers to match different pair characteristics:

| Fee Tier | Use Case | Example Pairs |
|---|---|---|
| **0.01%** | Stable-to-stable pairs | USDC/USDT, DAI/USDC |
| **0.05%** | Correlated pairs | ETH/stETH, WBTC/BTC |
| **0.30%** | Standard volatile pairs | ETH/USDC, UNI/ETH |
| **1.00%** | Exotic/low-liquidity pairs | Long-tail tokens |

### Uniswap v4 and Hooks

Uniswap v4 launched on **31 January 2025**. It introduces **hooks** -- custom smart contract logic that can execute before or after pool operations (swaps, LP additions/removals). Hooks enable programmable pool behavior including dynamic fees, on-chain limit orders, time-weighted average market maker (TWAMM) functionality, and custom oracle integrations. This makes Uniswap v4 a platform for building custom AMM logic on top of Uniswap's liquidity infrastructure (Datawallet; Uniswap support docs).

### Unichain

**Unichain**, Uniswap's own Ethereum L2 built on the OP Stack, went live on mainnet **11 February 2025** (Uniswap blog). It offers ~1-second blocks and cheap swaps, and under UNIfication its sequencer fees are routed into the UNI burn mechanism.

### UNIfication (November-December 2025) — fee switch and UNI burn

The defining UNI tokenomics event. On **10 November 2025** Uniswap Labs and the Uniswap Foundation released the **UNIfication** proposal: activate protocol fees, route them to UNI burns, route Unichain sequencer fees into the same burn, build Protocol Fee Discount Auctions (PFDA), burn 100M UNI from the treasury, zero out interface/wallet/API fees, and fund a 20M-UNI-per-year growth budget from 1 January 2026 (Uniswap governance forum).

- **Vote passed 25 December 2025** with ~99.9% support (125.34M UNI for vs 742 against) (CoinDesk, The Defiant).
- **28 December 2025**: 100 million UNI (~10% of total supply, ~$596M at ~$5.96) sent to a dead address; protocol fees activated on v2 and selected v3 mainnet pools — on v2, LPs keep 0.25% and the protocol takes 0.05% for burns (Cointelegraph, CoinMarketCap).
- **26 February 2026**: UNI jumped ~15% as a follow-on governance vote to expand the fee switch to more pools gained momentum (CoinDesk).

---

## UNI Governance and Tokenomics

UNI launched in September 2020 with a 1 billion fixed supply distributed across community (60%), team (~21%), investors (~18%), and advisors. Governance runs through the **Uniswap DAO**: UNI holders (and their delegates) propose and vote on protocol changes via on-chain Governor contracts, with a Timelock enforcing an execution delay. The Uniswap Foundation funds grants and ecosystem work.

| Governance element | Detail |
|---|---|
| **Voting unit** | 1 UNI = 1 vote; holders may delegate to themselves or to delegates |
| **Proposal threshold** | A material UNI delegation is required to submit an on-chain proposal |
| **Process** | Temperature check → consensus check → on-chain Governor vote → Timelock execution |
| **Fee switch** | Activated under UNIfication (Dec 2025); protocol takes a cut of LP fees routed to UNI burns |
| **Supply mechanic** | Originally inflationary tail (2% perpetual from 2024); UNIfication added a deflationary burn that offsets/exceeds issuance when volume is high |

For traders, the practical shift is that UNI moved from a pure governance token (value driven by speculation on a *future* fee switch) to a **cash-flow asset** whose burn rate scales with protocol volume. The relevant valuation question is now "burn rate vs. circulating supply" rather than "will they ever turn on fees". Governance votes that widen the set of fee-bearing pools are direct, datable catalysts (see the 26 Feb 2026 +15% move). See [[dao-governance]] and [[tokenomics]].

### Oracles and TWAP

Since v2, Uniswap pools expose a **time-weighted average price (TWAP)** oracle that many [[defi]] protocols consumed for on-chain pricing. v3 improved oracle granularity. Because the price can be pushed within a single block, low-liquidity Uniswap oracles are manipulable via flash-loan-funded swaps -- a recurring DeFi exploit vector. Most lending protocols now prefer [[chainlink]] feeds or use Uniswap TWAP only over long windows on deep pools. See the Oracle Manipulation risk below and [[oracle-manipulation]].

---

## Trading Strategies

### 1. Concentrated Liquidity LP Farming (Moderate difficulty)

- **Mechanism**: Deploy capital in tight price bands around current trading price to maximize fee capture
- **Example**: ETH/USDC LP at $2,400-$2,600 range during low-volatility consolidation periods
- **APY**: 10-40% realized (before impermanent loss) on tight ranges for major pairs; higher on volatile new-listing pairs but with proportionally higher IL risk
- **Capital requirement**: $25,000+ to overcome gas costs on mainnet; $5,000+ viable on [[arbitrum]] or Base
- **Difficulty**: Intermediate -- requires active range management
- **Tools**: Revert Finance, Range Protocol, and Arrakis automate rebalancing of concentrated positions
- **Key consideration**: Position goes 100% out-of-range in a 15%+ directional move, stopping all fee accrual. Active management or auto-rebalancing vaults are essential
- (Source: [[2026-04-22-perplexity-defi-trading-strategies-sweep]])

### 2. Fee-Tier Arbitrage (Low difficulty)

- **Mechanism**: Same token pair trades across different fee tiers with slightly different prices. Arbitrage the spread between the 0.01% tier and the 0.30% tier for the same pair
- **Example**: USDC/USDT; buy on the 0.01% fee tier, sell on the 0.30% tier, pocket the spread minus gas
- **APY**: 8-15% annually -- modest but reliable
- **Capital requirement**: $10,000+, though gas costs on mainnet eat ~30% of profit at lower capitals
- **Difficulty**: Beginner-intermediate
- **Reality check**: Competition from MEV bots compresses margins; L2 deployments offer better economics for smaller capital
- (Source: [[2026-04-22-perplexity-defi-trading-strategies-sweep]])

### 3. New Token Launch LP (High difficulty, high risk)

- **Mechanism**: Provide early liquidity for newly launched tokens that list on Uniswap before centralized exchanges
- **APY**: Highly variable -- 100%+ fees possible in the first hours/days, but impermanent loss can exceed fee income if the token dumps
- **Capital requirement**: $5,000-$50,000
- **Difficulty**: Advanced -- requires ability to evaluate token contracts for rugs, understand mempool dynamics
- **Risk**: Rug pulls, honeypot tokens, extreme impermanent loss. Not recommended without smart contract auditing skills

### 4. JIT (Just-In-Time) Liquidity

- **Mechanism**: Sophisticated LPs add concentrated liquidity in the same block as a large pending swap, capture the fees, then immediately withdraw. This is a form of [[mev|MEV]] extraction
- **Capital requirement**: $100,000+ and custom smart contract infrastructure
- **Difficulty**: Expert -- requires MEV infrastructure (Flashbots, private transaction submission)
- **Reality check**: Dominated by professional MEV searchers; not viable for retail traders

---

## Risk Framework

### Impermanent Loss (IL)

The dominant risk for Uniswap LPs. In concentrated liquidity (v3), IL is amplified compared to v2 because capital is deployed in a narrower range. A 20% price move on a tight range position can result in 30-50% capital loss relative to simply holding the underlying tokens. IL is not "impermanent" if you withdraw at a loss -- the name is misleading.

### MEV and Sandwich Attacks

Uniswap trades are visible in the public mempool before execution. MEV bots exploit this via **sandwich attacks**: frontrunning your buy to push the price up, then backrunning your trade to sell at the higher price. This costs traders an estimated 0.5-2% in additional effective slippage on large swaps. Mitigations include using Flashbots Protect, MEV Blocker, or private RPC endpoints for transaction submission.

### Smart Contract Risk

Uniswap v3 has been live since May 2021 and has processed hundreds of billions in volume without a direct exploit of its core contracts. However, periphery contracts and integrations have been exploited (the 2023 flash loan exploit on borrowed LP positions). Uniswap v4, being newer code, carries elevated smart contract risk until it has been battle-tested for an extended period.

### Oracle Manipulation

Uniswap v3 pools serve as price oracles for many [[defi]] protocols. Attackers can manipulate these oracle prices via large trades within a single block, potentially causing cascading liquidations on protocols that rely on Uniswap TWAP oracles. [[chainlink]] price feeds are generally preferred for lending protocol oracles for this reason.

---

## Key Metrics

| Metric | Value (June 2026) | Notes |
|---|---|---|
| **TVL** | ~$2.6B (all chains) | Verify on DefiLlama |
| **All-time volume** | $3T on Ethereum mainnet (5 May 2026 milestone); ~$4T all chains | Uniswap Labs / CoinLaw |
| **UNI Price** | ~$2.49 (9 June 2026) | Verify on CoinGecko; was ~$5.96 at the Dec 2025 burn |
| **UNI Supply** | 100M UNI (~10% of supply) burned 28 Dec 2025; ongoing fee burns | Cointelegraph |
| **Cumulative swappers** | ~119M | CoinLaw |
| **Fee Revenue** | Protocol fees live on v2 + selected v3 mainnet pools; routed to UNI burn | Verify on Dune Analytics |

---

## Competitive Position

| Competitor | Uniswap Advantage | Competitor Advantage |
|---|---|---|
| [[curve-finance]] | Better for volatile pairs and exotic tokens; deeper liquidity on most non-stable pairs | Curve has far lower slippage on stablecoin swaps; veCRV incentive model drives deeper stable liquidity |
| [[balancer]] | Simpler UX; higher volume; more integrations | Balancer offers custom-weighted pools (e.g., 80/20) and composable pool architecture |
| [[sushiswap]] | Higher liquidity and volume on all major pairs | Sushi pioneered multi-chain early; some unique features like Kashi lending |
| [[dydx]] / [[hyperliquid]] | Spot AMM with deep liquidity | These are derivatives/perps platforms (different product category) |
| Centralized exchanges | Permissionless listing; no KYC; self-custody | CEXs have far lower fees, faster execution, and better UX for most traders |

Uniswap's primary moat is **network effects**: it has the deepest liquidity, the most integrations (wallets, aggregators, other protocols), and serves as the default price discovery venue for new ERC-20 tokens. It is the most forked protocol in DeFi history.

---

## Trading Relevance

- Uniswap is the primary price discovery venue for new tokens before they list on centralized exchanges
- New pair listings and sudden volume spikes on Uniswap often signal emerging narratives or scams
- UNI token trades as a proxy for DEX adoption and [[defi]] growth — and since UNIfication (Dec 2025) it is a fee-accruing, deflationary asset: burn rate vs. volume is now a fundamental valuation input
- Governance votes on expanding the fee switch are tradeable catalysts (UNI +15% on 26 Feb 2026 around one such vote)
- LP positions (providing liquidity) are a yield strategy, but carry **impermanent loss** risk when prices move significantly
- MEV bots actively exploit Uniswap trades via sandwich attacks -- private transaction submission (Flashbots) is recommended for larger swaps
- Uniswap pool data (TVL changes, large swaps) is a leading indicator for [[defi]] sentiment
- [[lido|stETH]]/ETH and other liquid staking derivative pairs on Uniswap are frequently used for [[aave]] e-mode strategies

---

## See Also

- [[decentralized-exchanges]] -- The broader DEX category
- [[defi]] -- The ecosystem Uniswap helped build
- [[ethereum]] -- Uniswap's primary chain
- [[smart-contracts]] -- The technology powering Uniswap's pools
- [[arbitrum]] -- Major L2 deployment for cheaper Uniswap trades
- [[curve-finance]] -- Primary competitor for stablecoin swaps
- [[balancer]] -- Competing AMM with weighted pool innovation
- [[chainlink]] -- Oracle infrastructure that Uniswap v4 hooks can integrate

---

## Sources

- (Source: [[2026-04-22-perplexity-defi-trading-strategies-sweep]])
- Uniswap blog, "Unichain Mainnet is Here" (11 Feb 2025) — https://blog.uniswap.org/unichain-mainnet-is-here
- Uniswap support, "Uniswap v2, v3 and v4" — https://support.uniswap.org/hc/en-us/articles/7425482965517-Uniswap-v2-v3-and-v4
- Uniswap governance forum, "UNIfication Proposal" (Nov 2025) — https://gov.uniswap.org/t/unification-proposal/25881
- CoinDesk, "Uniswap's UNI token burn, protocol fee 'UNIfication' proposal backed overwhelmingly by voters" (26 Dec 2025) — https://www.coindesk.com/business/2025/12/26/uniswap-s-token-burn-protocol-fee-proposal-backed-overwhelmingly-by-voters
- Cointelegraph, "Uniswap Burns $596M in UNI After Fee Switch Governance Vote" (Dec 2025) — https://cointelegraph.com/news/uniswap-executes-100m-uni-burn-after-fee-switch-approval
- CoinDesk, "Uniswap's UNI jumps 15% as governance vote to expand fee switch gains momentum" (26 Feb 2026) — https://www.coindesk.com/markets/2026/02/26/uniswap-s-uni-jumps-15-as-governance-vote-to-expand-fee-switch-gains-momentum
- Datawallet, "Uniswap v4 Explained" — https://www.datawallet.com/crypto/uniswap-v4-explained
- CoinLaw, "Uniswap Statistics 2026" — https://coinlaw.io/uniswap-statistics/
- Verified via Perplexity (sonar) and web search, 2026-06-10.
