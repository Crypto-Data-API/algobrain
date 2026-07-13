---
title: "Points Farming"
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [crypto, defi, points, airdrops, loyalty, sybil, protocols, farming, token-generation-event]
aliases: ["Points Meta", "Airdrop Farming", "Loyalty Points Farming", "Points Season"]
strategy_type: hybrid
timeframe: position|long-term
markets: [crypto]
complexity: intermediate
backtest_status: untested
related: ["[[restaking-strategies]]", "[[defi-yield-farming]]", "[[airdrop-farming]]", "[[points-farming]]"]
---

# Points Farming

## Overview

Points farming is the practice of interacting with crypto protocols to accumulate proprietary loyalty points that are expected to convert into governance tokens via future airdrops. Since 2023, protocols have increasingly used points systems (instead of direct token rewards) to incentivize early adoption while deferring the token generation event (TGE). Major points programs have included EigenLayer (restaking points), Blast (yield + referral points), Ethena (sats/shards), and Hyperliquid. The strategy involves deploying capital and activity across multiple protocols simultaneously to maximize point accumulation, while carefully managing the risk that points may convert at a low ratio or not at all.

## How It Works

1. **Identify active points programs:** Monitor crypto Twitter, DeFi dashboards, and airdrop tracking sites for protocols running points campaigns before their TGE.
2. **Deploy capital strategically:** Deposit assets into the protocol as required (provide liquidity, stake tokens, bridge assets). Larger deposits and longer lock-ups typically earn more points.
3. **Maximize multipliers:** Many programs offer bonus multipliers for referrals, specific actions (bridging, swapping, holding NFTs), or early participation. Optimize for these boosts.
4. **Diversify across programs:** Run 5-10 points programs simultaneously. Not all will convert favorably, so portfolio diversification across protocols reduces single-program risk.
5. **Track and harvest:** Monitor point balances, airdrop announcements, and TGE timelines. When tokens are distributed, evaluate whether to sell immediately or hold.

## Example

A farmer allocates $50,000 across three active points programs. (1) Deposits $20,000 in ETH into ether.fi for EigenLayer + ether.fi dual points -- earns restaking yield plus points over 4 months. (2) Bridges $15,000 to Blast L2 and provides liquidity in DEX pools, accumulating Blast Gold and Points. (3) Deposits $15,000 USDC into Ethena to mint USDe and stake for sats. After 4-6 months, ether.fi conducts TGE and distributes ETHFI tokens worth $3,200 based on accrued points. Blast airdrop yields $1,800 in BLAST tokens. Ethena airdrop pending. Total realized airdrop income: $5,000 on $50,000 deployed (~10% return in 4-6 months), plus any base yields earned during the farming period.

## Advantages

- **Outsized early returns** -- successful airdrop conversions have delivered 20-100%+ returns on deployed capital
- **Stackable with other strategies** -- points accumulate alongside base yields from staking, lending, or LP positions
- **Low direct cost** -- points are earned through protocol usage, not purchased; capital remains deployed in yield-bearing positions
- **Network effects** -- referral multipliers reward community building and can significantly boost allocations

## Disadvantages

- **Uncertain conversion** -- points have no guaranteed value; the token-to-points ratio is revealed only at TGE, and many airdrops disappoint
- **Capital lockup risk** -- funds deployed in pre-TGE protocols may be locked or illiquid during the farming period
- **Sybil crackdowns** -- protocols increasingly use Sybil detection to exclude multi-wallet farmers, reducing or zeroing allocations
- **Opportunity cost** -- capital deployed in speculative points programs could earn guaranteed yield elsewhere
- **Protocol risk** -- pre-TGE protocols are often unaudited, newer, and more vulnerable to exploits

## See Also

- [[airdrop-farming]] -- the predecessor strategy of earning tokens through early protocol interaction
- [[restaking-strategies]] -- a key source of dual-layer points (EigenLayer + LRT protocol points)
- [[defi-yield-farming]] -- the base yield strategies that points farming builds upon
