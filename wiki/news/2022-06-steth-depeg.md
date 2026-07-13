---
title: "stETH-ETH Depeg — June 2022 Liquidity Crisis"
type: news
created: 2026-04-24
updated: 2026-06-12
status: good
tags: [news, arbitrage, crypto, defi, ethereum]
event_date: 2022-06-13
markets_affected: [crypto, defi, staking]
impact: high
verified: true
sources_count: 4
related:
  - "[[lst-depeg-arbitrage]]"
  - "[[lido]]"
  - "[[curve-finance]]"
  - "[[2022-05-terra-luna-depeg-arb]]"
  - "[[ethereum]]"
---

# stETH-ETH Depeg -- June 2022 Liquidity Crisis

In **June 2022**, Lido Staked ETH (stETH) -- a liquid staking token representing [[ethereum|ETH]] staked in the Beacon Chain -- broke its informal 1:1 peg with ETH and traded as low as **0.9346 ETH on June 13, 2022**, a depeg of roughly **6.5%**. The dislocation triggered cascading liquidations across Celsius, [[three-arrows-capital]], and several smaller funds, and exposed a critical design assumption: that stETH would trade near parity even though no redemption mechanism existed yet. Post-Shapella (April 2023), withdrawals are live and stETH has held within ~0.5% of peg through every subsequent stress event.

## Background -- Liquid Staking Without Withdrawals

By early 2022, [[lido|Lido Finance]] dominated liquid staking with roughly **30%** of all staked ETH (over **4 million ETH**). When users staked ETH via Lido, they received stETH 1:1 and could use it across DeFi while still earning ~5% staking yield.

**The catch**: Ethereum's Beacon Chain did not yet support withdrawals. ETH staked into Lido was locked indefinitely until two future upgrades:

- **The Merge** (transition to PoS) -- expected mid-to-late 2022.
- **Shapella** (Shanghai + Capella, enabling withdrawals) -- not yet scheduled.

Until then, the only way to convert stETH back to ETH was to **sell it on secondary markets** -- primarily the [[curve-finance|Curve Finance]] stETH/ETH pool, which held ~75% of all on-chain stETH liquidity at peak.

## What Happened

**Early June 2022**: [[celsius-network|Celsius Network]] -- one of the largest stETH holders with ~$1.5B exposure -- faced a liquidity crisis. Heavy customer withdrawals after [[2022-05-terra-luna-depeg-arb|Terra's collapse]] forced Celsius to liquidate stETH for ETH to meet redemptions.

**June 8-12, 2022**: Celsius dumped stETH on Curve in increasingly large slugs. The Curve pool, which had been running ~50/50, tilted to **80% stETH / 20% ETH** as arbitrage liquidity was overwhelmed. The peg slipped from 0.998 to 0.97.

**June 12, 2022**: Celsius froze all withdrawals.

**June 13, 2022**: stETH/ETH bottomed at **~0.9346** -- a 6.54% discount. [[three-arrows-capital|3AC]], holding ~$300M+ stETH and unable to meet margin calls, was forced to dump as well.

| Date | stETH/ETH | ETH Price | Curve Pool Imbalance |
|------|-----------|-----------|---------------------|
| May 1 | 0.9985 | $2,800 | ~52/48 |
| Jun 1 | 0.9930 | $1,950 | ~58/42 |
| Jun 8 | 0.9750 | $1,810 | ~70/30 |
| Jun 12 | 0.9520 | $1,210 | ~78/22 |
| **Jun 13** | **0.9346** | **$1,090** | **~82/18** |
| Jun 30 | 0.9560 | $1,070 | ~75/25 |
| Sep 15 (Merge) | 0.9970 | $1,470 | ~55/45 |
| Apr 12, 2023 (Shapella) | 0.9995 | $1,890 | ~50/50 |

## The Arbitrage Trade

The depeg created a textbook -- but illiquid -- arbitrage. The thesis: **1 stETH would eventually equal 1 ETH** once Shapella enabled withdrawals.

The trade structure:

- **Long stETH** at 0.93-0.95 ETH on Curve or Aave.
- **Short ETH** via perps on FTX, Binance, or dYdX (or borrow ETH against stETH collateral on Aave).
- Hold until Shapella unlocked the redemption.

**Risks**:

- **Duration uncertainty**: Shapella had no firm date in June 2022. A "few months" became "10 months."
- **Funding cost**: Short ETH funding rates spiked positive during deleveraging events.
- **Liquidation risk on collateralized positions**: Aave's stETH/ETH borrowing required maintaining a healthy LTV; further depeg could cascade liquidations.
- **Smart contract risk**: Lido governance failure, Curve exploit, or Beacon Chain bug could permanently impair stETH.

Funds that held the trade through Shapella captured roughly **5-6% on the spread** plus continued staking yield (~4-5%) -- a solid but not spectacular return given the duration and risks involved.

## The Exit Queue Mechanic

Post-Shapella, Lido implemented a withdrawal queue. The mechanic enforces the peg:

1. Submit stETH for withdrawal via Lido contract.
2. Wait for queue position (typically 1-5 days, longer during stress).
3. Receive ETH 1:1.

This **direct redemption mechanism** is what enforces the peg. Any sustained discount creates an arbitrage: buy stETH at discount, redeem 1:1 for ETH. The discount cannot exceed the cost of capital across the queue duration.

Post-Shapella stress events (Mar 2023 USDC depeg, Aug 2024 yen carry unwind) have produced only shallow stETH depegs of **0.1-0.3%** -- fully consistent with queue duration arbitrage limits.

## Why the Pre-Shapella Depeg Was Inevitable

The structural mismatch was severe:

- **stETH outstanding**: ~4.2M tokens.
- **Curve pool depth**: ~$1B (~500K ETH equivalent at peak).
- **Forced sellers** (Celsius + 3AC + smaller funds): >$2B notional.

When forced sellers exceeded the AMM's ability to absorb without massive slippage, the price had to gap. There was no withdrawal pressure release valve. The only buyers were patient capital willing to lock funds for an unknown duration -- and they demanded a meaningful premium.

## Trading Lessons

- **No redemption = no peg arbitrage**: Without a hard redemption mechanism, "pegged" assets only trade at peg under normal conditions. See [[2022-05-terra-luna-depeg-arb]] for the catastrophic version.
- **AMM depth defines the breaking point**: Curve's stETH pool absorbed ~$500M of selling before failing. Any forced seller larger than the deepest pool will move the price.
- **Liquidity crises propagate through correlated holders**: Celsius, 3AC, and BlockFi all held overlapping positions in stETH, GBTC, and Anchor UST. One forced seller created the conditions that liquidated the next.
- **Duration risk dominates yield**: A 6% spread sounds attractive, but locking capital for 10 months with ongoing depeg risk requires institutional patience most retail traders lack.
- **Compare to listed [[lst-depeg-arbitrage|LST depeg arbs]] today**: rETH (Rocket Pool), cbETH (Coinbase), wstETH all trade tighter post-Shapella, but the same dynamic applies if withdrawal queues lengthen during a chain-level crisis.

The June 2022 stETH depeg is the cleanest case study of liquidity-driven mispricing in DeFi -- not a credit event, not a smart contract failure, just AMM math meeting forced selling. See also [[lst-depeg-arbitrage]] and [[curve-finance]].

## Sources

- Lido Finance documentation — stETH mechanics, withdrawal queue (post-Shapella), and historical TVL/staked-ETH share.
- Curve Finance stETH/ETH pool analytics — pool imbalance and depth during June 2022.
- CoinDesk, *The Block*, Bloomberg Crypto — contemporaneous June 2022 coverage of the Celsius/stETH liquidity crisis and the 3AC unwind.
- On-chain stETH/ETH price series (Dune, Curve subgraph) — June 13, 2022 low of ~0.9346.
- See also [[2022-06-three-arrows-blowup]] and [[2022-05-terra-luna-depeg-arb]] for the correlated forced-seller context.
