---
title: "LST Depeg Arbitrage (stETH / rETH / cbETH)"
type: strategy
created: 2026-04-24
updated: 2026-06-21
status: excellent
tags: [arbitrage, crypto, defi, ethereum, mean-reversion]
aliases: ["stETH Arb", "Liquid Staking Depeg", "LST Peg Trade", "stETH/ETH Arb"]
strategy_type: quantitative
timeframe: position
markets: [crypto, defi]
complexity: advanced
backtest_status: retired
edge_source: [structural, behavioral]
edge_mechanism: "Liquid staking tokens are claims on staked ETH redeemable through a withdrawal queue, not at-will. Forced selling during liquidity crises temporarily breaks the peg below intrinsic value."
data_required: [steth-price, eth-price, curve-pool-balances, validator-queue, gas-price]
min_capital_usd: 50000
capacity_usd: 100000000
crowding_risk: medium
expected_sharpe: 1.2
expected_max_drawdown: 0.20
breakeven_cost_bps: 50
decay_evidence: "Post-Shapella (April 2023) withdrawals enabled; depegs now shallow (<1%)."
related: ["[[funding-rate-arbitrage]]", "[[stablecoin-pair-arbitrage]]", "[[depeg-risk]]", "[[lido]]", "[[rocket-pool]]", "[[curve-finance]]", "[[2022-05-terra-luna-depeg-arb]]", "[[three-arrows-capital]]", "[[celsius]]", "[[ethena]]"]
---

# LST Depeg Arbitrage

Liquid Staking Token (LST) depeg arbitrage captures the spread between a [[liquid-staking]] derivative (stETH, rETH, cbETH) and underlying ETH when forced selling temporarily pushes the LST below its 1:1 redemption value. It is a convergence [[arbitrage]] trade: the LST is a *claim* on staked ETH redeemable only through a withdrawal queue, so the trader buys the discounted claim and either waits for the peg to mean-revert or redeems 1:1 through the queue. The flagship trade was the June 2022 stETH depeg, when [[three-arrows-capital]] and [[celsius]] forced-sold stETH on [[curve-finance]] driving the price to **0.935 ETH** before mean-reverting through the post-Shapella (April 2023) withdrawal queue.

Structurally this is the on-chain analog of the [[gbtc-discount-arbitrage|GBTC discount trade]]: a claim trades below intrinsic value while the redemption mechanism is constrained, and the discount closes when redemption opens (Shapella ≈ ETF conversion). The same [[limits-to-arbitrage]] logic applies — the discount is compensation for queue duration, smart-contract risk, and the inability to redeem on demand.

## Edge Source

**Structural** + **behavioral** (see [[edge-taxonomy]]). LSTs are tokenized claims on staked ETH. Pre-Shapella (April 12, 2023) there was no withdrawal mechanism at all; post-Shapella, withdrawals are queued and can take days to weeks. During liquidity crises, holders who *need* ETH right now (margin calls, redemption pressure) sell the LST at any price, while patient capital can absorb the supply and wait for the queue to clear.

## Why This Edge Exists

LSTs are not literally redeemable at 1:1 on demand. Three frictions create the depeg:

1. **Withdrawal queue:** Validator exit queue is rate-limited (per epoch). In normal conditions, ~1–7 days. During mass exit events (e.g., post-Pectra), >30 days.
2. **Liquidity asymmetry:** Secondary liquidity for stETH lives mostly on the [[curve-finance]] stETH/ETH pool. When pool reserves tilt, slippage explodes nonlinearly.
3. **Forced selling:** Levered holders facing liquidations or redemptions cannot wait for the queue. They dump into the pool, blowing past the small "patient" bid.

## Null Hypothesis

If LST holders could redeem 1:1 at any time with zero friction, the LST/ETH spread would oscillate within transaction costs (~5–20 bps). Persistent multi-day deviations of >1% reject that null.

## Rules

### Entry
1. **Trigger:** stETH/ETH (or rETH/ETH, cbETH/ETH) drops below 0.97 with elevated [[curve-finance]] pool imbalance (>70% LST-side).
2. **Confirm forced-seller dynamics:** Look for on-chain liquidations, large fund flows from known wallets (Celsius, Aave whales).
3. **Long LST:** Buy stETH / rETH / cbETH on Curve, [[uniswap]], or CEX (Coinbase for cbETH).
4. **Short ETH:** Open ETH perp short ([[binance]], [[bybit]], [[hyperliquid]]) or borrow + sell spot ETH on [[aave]].
5. **Match notional 1:1** — true delta-neutral unless explicit directional view.

### Exit
1. **Peg restoration:** Spread narrows to within 30–50 bps.
2. **Withdrawal:** Submit unstake to Lido / Rocket Pool, exit queue, redeem 1:1, close ETH short.
3. **Catalyst close:** End of forced-selling event (bankruptcy resolution, liquidation completion).
4. **Stop-loss:** Spread widens beyond entry by >2% AND queue length increases beyond expected hold (re-evaluate).

### Position Sizing
Cap exposure at the depth available on Curve pool without >2% slippage on exit. For institutional size, split execution across multiple days. Account for ETH perp funding (which often goes deeply negative during these events — a tailwind for the short leg).

## Implementation Pseudocode

```python
def lst_depeg_arb():
    spread = steth_price() / eth_price()
    pool_imbalance = curve_steth_pool_lst_share()

    if spread < 0.97 and pool_imbalance > 0.70:
        notional = sizing_function(curve_depth_2pct())

        steth = buy_steth_curve(notional)
        short_eth = open_perp_short(notional, venue="binance")

        # Two paths to close
        if steth_eth_spread() > 0.995:                 # peg restored
            sell_steth_curve(steth)
            close_perp(short_eth)
        elif withdrawal_queue_clear() and not_too_long():
            request_lido_unstake(steth)
            wait_for_queue()                            # 1d-30d
            redeem_eth(steth)
            close_perp(short_eth)
```

## Indicators / Data Used

- **stETH/ETH price** (Curve pool, Chainlink oracle)
- **Curve stETH pool composition** (% stETH vs % ETH)
- **Lido withdrawal queue length** (Lido on-chain queue contract)
- **ETH validator exit queue** (beaconcha.in)
- **ETH perp funding rate** (often -100% APR during depegs = short receives)
- **Aave/Compound stETH collateral utilization** (forced-liquidation pipeline)
- **wstETH wrap/unwrap rate** (1 wstETH = N stETH; rate accrues over time)

## Example Trade — June 2022 stETH Depeg

| Date | stETH/ETH | Driver |
|------|-----------|--------|
| 2022-05-08 | 0.998 | Pre-Terra |
| 2022-05-12 | 0.985 | Terra/Luna collapse cross-contagion |
| 2022-06-09 | 0.965 | Celsius withdrawals halt rumors |
| 2022-06-13 | 0.945 | Celsius pauses withdrawals |
| 2022-06-17 | **0.935** | 3AC liquidation reports |
| 2022-07-08 | 0.96 | Bottom established |
| 2023-04-12 | 0.998 | Shapella enables withdrawals |
| 2023-05-15 | 0.999 | Queue clears |

**The trade:**

1. **Entry June 18, 2022:** Buy 5,000 stETH at 0.94 ETH each = 4,700 ETH cost (~$4.7M @ $1,000 ETH).
2. **Hedge:** Short 5,000 ETH perp on Binance at $1,005. Funding was -0.08% per 8h (short receives ~88% APR).
3. **Hold through Shapella:** April 12, 2023.
4. **Unstake:** Submit Lido unstake May 1, 2023. Queue: 4 days. Redeem 5,000 ETH 1:1.
5. **Close perp:** Cover short at $1,840 (loss on perp leg ~$4.2M).
6. **Funding earned:** ~$650K over ~10 months. Funding was deeply negative (−50 to −100% APR, short receives) during the June–July 2022 crisis weeks, then drifted toward zero; the blended average works out to roughly −15% APR on the ~$5M short.
7. **Spot leg:** 5,000 ETH × $1,840 = $9.2M.
8. **Net:**  $9.2M (redeemed) − $4.2M (perp loss) + $650K (funding) − $4.7M (entry cost) ≈ **+$950K**, plus the trade was effectively delta-neutral so the dollar P&L is from the **6% peg restoration + funding harvest**.

## Performance Characteristics

> **Data disclaimer:** The figures below are *illustrative, regime-conditional estimates* reconstructed from the on-chain depeg record (e.g., stETH/ETH printing 0.935 on 2022-06-17). They are not an audited backtest. The "easy" version of this edge is now retired (`backtest_status: retired`) because post-Shapella withdrawals collapsed depeg depth and duration.

- **Win rate:** High (~85-90%) historically when entered below 0.96
- **Best market conditions:** Forced-selling crises, deleveraging cascades
- **Worst conditions:** Smart-contract exploit on Lido / Rocket Pool, validator slashing event
- **Sharpe (when opportunity exists):** 2.0+, but opportunity is intermittent
- **Post-Shapella regime:** Depegs now <1% and close within hours; the "easy" version of this trade is dead

### Cost overlay (what determines net P&L)

| Cost / friction | Effect | Direction |
|-----------------|--------|-----------|
| Curve pool slippage on entry/exit | Large at crisis pool imbalance | Cost |
| ETH perp funding during hold | Often deeply negative (−50 to −100% APR) | **Tailwind** — short receives |
| Gas (wrap/unwrap, unstake) | Spikes during crises | Cost |
| Withdrawal queue duration | Capital locked 1d–30d+ | Opportunity cost |
| Smart-contract / slashing tail | Binary, low-probability | Risk premium |
| Staking yield accrued on LST during hold | rETH/wstETH NAV rises | Minor tailwind |

The net P&L is essentially **peg-restoration capture + funding harvest − slippage − queue opportunity cost**. In the canonical June 2022 trade the funding tailwind (short receives during the panic) was a material part of the return, not the peg snap-back alone.

## LST-Specific Variants

| LST | Issuer | Mechanic | Peg behavior |
|-----|--------|----------|--------------|
| **stETH** | [[lido]] | Rebasing (balance grows daily) | Largest pool; Curve is primary venue. Depegged to 0.935 in June 2022. |
| **wstETH** | Lido (wrapped) | Non-rebasing, accrues via exchange rate | Same economic claim as stETH; preferred for DeFi integrations. |
| **rETH** | [[rocket-pool]] | Non-rebasing, exchange rate accrues | Smaller liquidity; traded at a market *premium to NAV* during 2021–22 deposit-pool congestion. Because the redemption rate (NAV) accrues staking rewards — rising well above 1.10 ETH by 2024 — its "peg" must be measured against NAV, not 1.00. |
| **cbETH** | [[coinbase]] | Non-rebasing, centralized issuer | Held a -3% to -5% discount through 2022 due to centralized counterparty risk. |
| **frxETH/sfrxETH** | Frax | Two-token model | Smaller liquidity, higher volatility around the peg. |

## Capacity Limits

- Pre-Shapella stETH depegs absorbed **$50–100M** without moving the price meaningfully
- Curve pool depth (~$200–500M during crisis) capped single-trade size
- Post-Shapella, liquidity has thinned; meaningful discounts now <0.5% and capacity is **<$10M per cycle**

## What Kills This Strategy

- **Smart contract exploit** in Lido, Rocket Pool, or the Curve pool itself
- **Mass slashing event** that breaks LST/ETH parity permanently
- **Withdrawal queue blocked** indefinitely (governance attack, EIP rollback)
- **Crowding** — if too much capital chases the same depeg, peg restores in minutes and capacity collapses
- **Perp funding inverts** during the hold (rare, but possible if extreme bull rally during a depeg)

## Kill Criteria

- LST/ETH spread widens beyond entry by >3% with worsening on-chain liquidations
- Withdrawal queue exceeds 60 days
- Issuer governance event or audit failure
- Aggregate position > 5% of Curve pool depth
- Perp funding flips materially positive for 3+ consecutive funding intervals

## Advantages

- **Asymmetric:** intrinsic redemption value floor at 1.0 (post-Shapella)
- **Funding tailwind:** ETH perp funding usually negative during depegs (short receives)
- **Composable:** can use [[aave]] to lever the spread
- **Quantifiable target** — peg = 1.0
- **Clear catalyst** — Shapella was a known dated trigger

## Disadvantages

- **Smart contract risk** stacked across multiple protocols (Lido + Curve + Aave + perp venue)
- **Validator queue uncertainty** — exit times can blow out unpredictably
- **Slashing tail risk** — extremely unlikely but binary
- **Post-Shapella, edge is much smaller** — <1% depegs now
- **Capital lock-up** during the queue wait
- **Counterparty risk** for cbETH (Coinbase corporate)

## Historical Context

- **June 2022 cascade:** [[three-arrows-capital]] held an estimated 240K stETH (contemporary estimates valued the position around $400–600M depending on the date marked). Its forced unwind through Curve was a proximate cause of the 6.5% peg break, which fed the contagion around [[celsius]]'s insolvency (Celsius had paused withdrawals on June 12–13, 2022, days before the 3AC liquidation reports). [[ethena]] later commercialized a *funding-rate* version of this kind of trade (separate but conceptually adjacent).
- **April 2023 Shapella:** First successful ETH withdrawals. The trade thesis ("hold until you can redeem") paid off cleanly for funds that absorbed mid-2022 dislocations.
- **2024+ Pectra anticipation:** Subsequent upgrades changed validator exit dynamics, briefly creating shallow re-pegs.

## Sources

- Lido official disclosures, Curve pool analytics
- Three Arrows Capital bankruptcy filings (BVI, July 2022)
- Celsius Network Chapter 11 disclosures (July 2022)
- Ethereum Foundation Shapella upgrade documentation (April 2023)

## Related

- [[arbitrage]] — parent concept
- [[liquid-staking]] — the underlying primitive (stETH/rETH/cbETH)
- [[limits-to-arbitrage]] — why the discount can persist through a queue
- [[gbtc-discount-arbitrage]] — same "claim trades below intrinsic until redemption opens" structure
- [[funding-rate-arbitrage]], [[stablecoin-pair-arbitrage]], [[cross-chain-arbitrage]]
- [[depeg-risk]], [[2022-05-terra-luna-depeg-arb]]
- [[lido]], [[rocket-pool]], [[curve-finance]], [[ethena]]
- [[hyperliquid]] — a venue for the ETH perp short leg
- [[three-arrows-capital]], [[celsius]] — forced sellers in the canonical event
