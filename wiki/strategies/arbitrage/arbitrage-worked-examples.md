---
title: "Arbitrage Worked Examples"
type: reference
created: 2026-04-21
updated: 2026-06-20
status: excellent
tags: [arbitrage, backtesting, execution, education, meta]
aliases: ["Arb Examples", "Real Arbitrage Trades", "Arbitrage Case Studies"]
strategy_type: quantitative
timeframe: scalp|intraday|swing|position
markets: [crypto, futures, options]
complexity: intermediate
backtest_status: untested
related: ["[[arbitrage-overview]]", "[[arbitrage-parameter-cheatsheet]]", "[[arbitrage-live-performance]]", "[[funding-rate-arbitrage]]", "[[cross-exchange-arbitrage]]", "[[flash-loan-arbitrage]]", "[[transaction-cost-modeling]]", "[[fees]]"]
---

# Arbitrage Worked Examples

Individual strategy pages describe mechanics abstractly. This page walks through **specific trades with real market data** — dated prices, actual fee rates, exact P&L. Each example is reconstructed from publicly observable data (exchange rates, deal announcements, on-chain transactions) so the reader can verify the numbers.

> **Purpose:** Calibrate expectations. The theoretical return of a strategy means nothing if you don't know what a *single trade* actually looks like — including the friction, timing, and surprises.

> **Data disclaimer:** Examples 1-3 and 5 are reconstructed from publicly observable data (exchange prices, deal filings, on-chain ratios) but the exact fills, fee tiers, and intra-window numbers are *illustrative reconstructions*, not audited trade records. Example 4 is explicitly a *representative* pattern, not a specific transaction. Treat every figure as an order-of-magnitude teaching aid, not a promised return. Cross-check against [[arbitrage-live-performance]] and [[arbitrage-parameter-cheatsheet]] before sizing real capital.

## Examples at a Glance

| # | Strategy | Asset / Date | Horizon | Gross edge | What ate the edge | Net outcome (illustrative) |
|---|---|---|---|---|---|---|
| 1 | [[funding-rate-arbitrage]] | BTC, Nov 2024 | 15 days | ~0.08%/8h funding | Entry/exit fees, basis drift | Positive (golden period, atypical) |
| 2 | [[cross-exchange-arbitrage]] | SOL, Mar 2024 | ~4 s | 0.34% quoted spread | Taker fees + slippage | Thin positive; fee-tier dependent |
| 3 | merger-arbitrage | ATVI/MSFT, 2022-23 | 15 months | 22.6% deal spread | Deal-break risk, opportunity cost | Positive vs risk-free; tail was symmetric loss |
| 4 | [[flash-loan-arbitrage]] | ETH/USDC, representative | 1 block | 0.37% pool spread | 0.30%×2 swap fees + gas | **Negative** — instructive failure |
| 5 | [[lst-depeg-arbitrage\|stETH depeg]] | Jun 2022 | ~6 months | 5.9% discount | Smart-contract / depeg tail risk | Positive if hedged; convergence + yield |

The pattern across all five: **the gross edge is the easy part; the friction and the residual risk are where trades live or die.** Two of the five (flash loan, cross-exchange at retail fees) are unprofitable once costs are counted honestly.

---

## Example 1: Funding Rate Arbitrage (BTC, November 2024)

**Context:** Post-US-election crypto bull run. BTC surging from $70K to $90K+ in November 2024. Leveraged longs piling in, pushing funding rates to extreme levels.

### Entry: November 10, 2024

| Parameter | Value | Source |
|---|---|---|
| BTC spot price (Binance) | $81,500 | Binance spot market |
| BTC perp price (Binance) | $81,680 (0.22% premium) | Binance BTCUSDT perp |
| Funding rate (8h, Binance) | 0.0800% ($65.20 per BTC per 8h) | Coinglass historical |
| Annualized rate | 0.08% × 3 × 365 = **87.6% APY** | Calculation |
| Fee tier | VIP 1: 0.04% maker / 0.06% taker | Binance fee schedule |

**Trade execution:**
1. Buy 1.0 BTC spot at $81,500 (limit order, maker fee: $32.60)
2. Short 1.0 BTC perp at $81,680 (limit order, maker fee: $32.67)
3. Total entry cost: **$65.27** in fees

### Holding Period: November 10-25, 2024 (15 days, 45 funding periods)

| Date | Funding Rate (8h) | Daily Funding Received | BTC Spot Price |
|---|---|---|---|
| Nov 10-12 | 0.0650-0.0900% | $159-$234 | $81,500-$87,000 |
| Nov 13-15 | 0.0500-0.0700% | $135-$189 | $87,000-$91,000 |
| Nov 16-18 | 0.0800-0.1200% | $216-$351 | $91,000-$93,000 |
| Nov 19-21 | 0.0600-0.0800% | $171-$228 | $90,000-$96,000 |
| Nov 22-25 | 0.0300-0.0500% | $87-$150 | $95,000-$98,000 |

**Total funding received over 15 days:** approximately **$2,700-$3,100**

### Exit: November 25, 2024

| Parameter | Value |
|---|---|
| BTC spot price | $97,200 |
| Sell spot | $97,200 (maker fee: $38.88) |
| Close short perp | $97,350 (maker fee: $38.94) |
| Exit fees | **$77.82** |
| Spot P&L | +$15,700 (bought $81,500, sold $97,200) |
| Perp P&L | -$15,670 (shorted $81,680, covered $97,350) |
| Net directional P&L | **+$30** (near-zero, as expected for delta-neutral) |

### Final P&L

| Component | Amount |
|---|---|
| Funding income received | +$2,900 (estimated midpoint) |
| Entry fees | -$65.27 |
| Exit fees | -$77.82 |
| Net directional | +$30 |
| **Net profit** | **~$2,787** |
| Return on $81,500 capital | **3.4% in 15 days (83% APY)** |

### Lessons

1. **Funding rates are volatile:** Ranged from 0.03% to 0.12% per 8h during this 15-day window. The "average" rate of 0.08% was often not the actual rate
2. **Entry timing matters:** Entering on Nov 10 at peak funding was optimal. By Nov 25, rates had compressed to 0.03% — half the profitability
3. **The directional P&L was not exactly zero:** BTC moved +19% during the hold. The spot and perp legs tracked closely but not perfectly (basis drift), resulting in a small +$30 directional residual
4. **This was a golden period.** 83% APY is not normal — see [[arbitrage-seasonality]] for typical rate ranges

---

## Example 2: Cross-Exchange Arbitrage (SOL, March 2024)

**Context:** SOL volatile during the March 2024 memecoin season. Exchange prices temporarily diverged during a liquidity event.

### Opportunity Detected: March 15, 2024, ~14:32 UTC

| Parameter | Coinbase | Binance |
|---|---|---|
| SOL ask | $178.50 | $178.80 |
| SOL bid | $178.20 | $179.10 |
| **Spread** | — | **$0.60 (0.34%)** |

Buy on Coinbase at $178.50 ask, sell on Binance at $179.10 bid.

### Cost Analysis

| Cost Component | Amount | Calculation |
|---|---|---|
| Coinbase taker fee (Advanced Trade, $100K+ volume) | $0.107 | $178.50 × 0.06% |
| Binance taker fee (VIP 0) | $0.179 | $179.10 × 0.10% |
| Expected slippage (Coinbase) | $0.02 | Estimate based on book depth |
| Expected slippage (Binance) | $0.01 | Deeper book |
| **Total costs per SOL** | **$0.316** | |
| **Net spread per SOL** | **$0.284** | $0.60 - $0.316 |
| **Net spread %** | **0.159%** | |

### Execution (10 SOL)

| Leg | Actual Fill | Slippage |
|---|---|---|
| Buy 10 SOL on Coinbase | $178.52 avg (vs $178.50 ask) | $0.02 |
| Sell 10 SOL on Binance | $179.08 avg (vs $179.10 bid) | $0.02 |
| **Actual spread** | **$0.56 per SOL** | Narrower than quoted |

### Final P&L

| Component | Amount |
|---|---|
| Gross profit (10 × $0.56) | +$5.60 |
| Coinbase fees (10 × $0.107) | -$1.07 |
| Binance fees (10 × $0.179) | -$1.79 |
| **Net profit** | **$2.74** |
| Execution time | ~4 seconds (API orders) |
| Return on capital deployed ($1,785) | **0.15%** |

### Lessons

1. **Tiny absolute profit:** $2.74 on $1,785 capital. You need to do this hundreds of times per day for meaningful returns
2. **Slippage ate into the spread:** Quoted spread was $0.60, actual was $0.56. This 7% slippage degradation is typical
3. **Fee tier is destiny:** At retail Coinbase fees (0.60% taker), this trade would have been **unprofitable**. VIP/Advanced Trade fees were essential
4. **The opportunity lasted ~15 seconds.** By the time a manual trader could react, it was gone. Automation is mandatory
5. **Capital was pre-positioned** on both exchanges — no transfer delay

---

## Example 3: Merger Arbitrage (Activision Blizzard / Microsoft, 2022-2023)

**Context:** Microsoft announced acquisition of Activision Blizzard on January 18, 2022 for $95.00/share (all cash). The deal faced significant regulatory opposition and took 21 months to close.

### Entry: July 2022 (Post-FTC Lawsuit Filing)

| Parameter | Value |
|---|---|
| ATVI price (July 15, 2022) | $77.50 |
| Deal price | $95.00 |
| Spread | $17.50 (22.6%) |
| Expected close date | Q1-Q2 2023 (estimated ~9 months) |
| Annualized spread | 22.6% × (12/9) = **30.1%** |
| Risk-free rate (July 2022) | ~3.0% |
| Excess spread over risk-free | **27.1%** |

**Why the spread was wide:** FTC filed to block the deal. CMA (UK) was also investigating. Market priced in ~25-30% deal-break probability.

### Position

| Leg | Detail |
|---|---|
| Long 1,000 ATVI | $77,500 deployed |
| No short leg needed | All-cash deal (no exchange ratio to hedge) |

### Timeline

| Date | Event | ATVI Price | Spread |
|---|---|---|---|
| Jul 2022 | FTC suit filed | $77.50 | 22.6% |
| Nov 2022 | EU approves with conditions | $74.00 | 28.4% (widened) |
| Jan 2023 | Judge skeptical of FTC case | $79.00 | 20.3% |
| Apr 2023 | UK CMA blocks deal | $77.50 | 22.6% (panic) |
| Jul 2023 | FTC injunction denied by federal judge | $89.00 | 6.7% |
| Aug 2023 | UK CMA re-examines; restructured deal | $91.50 | 3.8% |
| Oct 13, 2023 | **Deal closes at $95.00** | $95.00 | 0% |

### Final P&L (15-month hold)

| Component | Amount |
|---|---|
| Shares received at close | 1,000 × $95.00 = $95,000 |
| Entry cost | $77,500 |
| Gross profit | +$17,500 |
| Commission (buy + sell) | ~$10 (negligible at modern brokers) |
| Opportunity cost (risk-free, 15 months) | $77,500 × 4% × 15/12 = -$3,875 |
| **Net profit (vs. risk-free)** | **$13,625** |
| **Annualized return** | **17.6%** |
| **Annualized excess return** | **13.6%** over risk-free |

### Lessons

1. **Wide spread = wide risk:** The 22.6% spread existed because there was real deal-break probability. The CMA block in April 2023 could have killed the deal
2. **If the deal had broken**, ATVI would have dropped to ~$60-65 (pre-announcement range). Loss would have been **-$12,500 to -$17,500** — nearly the full profit in reverse
3. **Position sizing matters:** At 5% portfolio allocation, a deal break would cost ~1% of portfolio. At 100% allocation, it's devastating
4. **Patience required:** 15 months of capital lock-up through regulatory drama. Multiple points where the spread widened (drawdown) before eventually converging
5. **Risk-adjusted, this was good:** 13.6% annualized excess over risk-free, with ~75% historical base-rate for deal completion. Expected value positive

---

## Example 4: Flash Loan Arbitrage (ETH/USDC, Ethereum Mainnet)

**Context:** A price discrepancy between Uniswap V3 and SushiSwap on Ethereum mainnet, captured via Aave flash loan.

### Opportunity: A representative flash loan arb (reconstructed from typical on-chain patterns)

| Parameter | Uniswap V3 | SushiSwap |
|---|---|---|
| ETH/USDC price | 3,400.00 | 3,412.50 |
| Spread | — | **$12.50 (0.37%)** |
| Pool depth at quote | $500K+ | $200K+ |

### Transaction Structure

```
1. Borrow 100,000 USDC via Aave V3 flash loan (0% fee)
2. Swap 100,000 USDC → 29.4118 ETH on Uniswap V3 (at $3,400)
3. Swap 29.4118 ETH → 100,367 USDC on SushiSwap (at $3,412.50)
4. Repay 100,000 USDC to Aave
5. Keep profit: 367 USDC
```

### Cost Analysis

| Cost Component | Amount |
|---|---|
| Flash loan fee (Aave V3) | $0 (0% premium) |
| Uniswap V3 swap fee (0.30%) | $300 |
| SushiSwap swap fee (0.30%) | $301 |
| Gas cost (flash loan + 2 swaps, ~800K gas at 25 gwei) | ~$60 |
| Flashbots builder bid (90% of remaining profit) | Varies |
| **Total costs before builder bid** | **$661** |

### P&L

| Component | Amount |
|---|---|
| Gross spread captured | +$367 |
| Swap fees | -$601 |
| **Net P&L before gas** | **-$234** |

**This trade is UNPROFITABLE.** The 0.37% spread sounds attractive, but the 0.30% swap fee on each leg (0.60% total) consumes the entire edge and more.

### When Flash Loan Arb IS Profitable

For the same trade to be profitable, the spread must exceed:
```
min_spread > fee_pool_1 + fee_pool_2 + gas_as_pct_of_notional
min_spread > 0.30% + 0.30% + 0.06% = 0.66%
```

At the 0.05% fee tier (Uniswap V3 concentrated liquidity pools for stablecoin/ETH):
```
min_spread > 0.05% + 0.05% + 0.06% = 0.16%
```

**Key insight:** Pool fee tiers determine arb viability. The 0.30% standard fee makes most DEX-DEX arbs unprofitable. The 0.05% and 0.01% fee tiers on concentrated liquidity pools are where flash loan arbs actually work — and those are the pools that professional searchers monitor.

### Lessons

1. **Most obvious arbs are unprofitable after fees.** If you can see a spread on a block explorer, it's probably already been evaluated and rejected by searchers
2. **Pool fee tier is the binding constraint**, not the spread. Target 0.05% and 0.01% fee tier pools
3. **Multi-hop routes** (3+ pools) can find profitable paths that two-pool arbs miss, because the intermediate pools have different fee tiers
4. **Gas cost matters less on L2:** This same arb on Arbitrum would cost $0.30 in gas instead of $60 — making many more arbs viable
5. **Zero capital required** but zero profit is also likely. The edge is in the path-finding algorithm, not in the capital

---

## Example 5: Staking Yield Arbitrage (stETH Discount, June 2022)

**Context:** Following the Terra/LUNA collapse and Three Arrows Capital bankruptcy, fear of crypto contagion caused Lido's stETH to trade at a 5-7% discount to ETH.

### Opportunity: June 14, 2022

| Parameter | Value |
|---|---|
| ETH price | $1,220 |
| stETH price | $1,148 (5.9% discount to ETH) |
| stETH/ETH ratio | 0.941 |
| Normal stETH/ETH ratio | ~0.999-1.001 |
| Staking APR (Lido) | ~4.2% |

### Trade

| Leg | Action |
|---|---|
| 1. Buy 10 stETH at $1,148 each | Cost: $11,480 |
| 2. Optional hedge: short 10 ETH perp to remove directional exposure | Locks in the discount, not ETH price direction |

### Outcome (December 2022)

stETH/ETH ratio recovered to 0.998 by late 2022 (post-Shanghai upgrade confidence).

| Component | Amount |
|---|---|
| stETH purchased | 10 stETH at $1,148 = $11,480 |
| stETH sold (Dec 2022) | 10 stETH at ~0.998 × $1,200 = $11,976 |
| Staking rewards earned (6 months × 4.2%) | +0.21 ETH (~$252) |
| **Gross P&L (unhedged)** | **+$748** (6.5% in 6 months) |
| If hedged (short ETH perp): directional P&L neutralized | Capture only the discount convergence + staking yield |
| **Hedged P&L** | ~$680 + $252 = **~$932 (8.1% in 6 months, ~16.2% annualized)** |

### Lessons

1. **The discount was a risk premium**, not a free lunch. If the Merge had failed or Lido had been exploited, stETH could have gone to deeper discount or zero
2. **Timing the bottom was impossible:** stETH traded at -3% to -7% for weeks. The "optimal" entry at -7% was only obvious in hindsight
3. **The hedge was critical:** Without the ETH short, you'd be long ETH through a 50%+ drawdown. The discount arb was profitable; the directional bet was horrifying
4. **Repeatable pattern:** Similar discounts appeared briefly in November 2022 (FTX) and March 2023 (SVB). The wiki identifies this as a recurring pattern in [[arbitrage-opportunity-map#Hidden Opportunity 3]]

---

## The Cost-Decomposition Framework

Every example above follows the same skeleton. Internalize it and you can evaluate any arb before risking capital:

```
net_edge = gross_spread
           − entry_fees − exit_fees          # explicit, per leg
           − slippage_in − slippage_out       # book depth vs size
           − financing_cost / opportunity_cost  # capital lock-up
           − tail_risk_premium                # the residual risk priced in
```

| Cost component | Where it bit (example) | How to estimate it pre-trade |
|---|---|---|
| Explicit fees | Cross-exchange (Ex.2): fees ≈ half the net | Look up your *actual* fee tier, both venues, maker vs taker |
| Slippage | Cross-exchange (Ex.2): 7% spread degradation | Walk the order book for your size; assume worse |
| Swap/pool fees | Flash loan (Ex.4): 0.60% killed a 0.37% edge | Sum every pool's fee tier on the route |
| Gas / network cost | Flash loan (Ex.4): negligible on L2, fatal at scale on L1 | Estimate gas × gwei; compare to notional |
| Financing / opportunity | Merger (Ex.3): risk-free drag over 15 months | `capital × risk_free × holding_period` |
| Tail-risk premium | stETH (Ex.5), merger (Ex.3): the discount *was* the risk | The spread exists *because* of a real loss scenario — price it |

The single most common retail error is to stop at `gross_spread − explicit_fees` and ignore slippage, financing, and the tail-risk premium. The flash-loan example (Ex.4) is in this page specifically because it shows a "0.37% arb" that is actually a **loss** once both pool fees are counted. See [[transaction-cost-modeling]] and [[arbitrage-parameter-cheatsheet]].

## Pre-Trade Checklist (applies to every example above)

- [ ] **Fee tier confirmed** on *both* legs at *your* actual volume tier — not the headline rate
- [ ] **Order book walked** for your full size; slippage assumed worse than the top-of-book quote
- [ ] **Capital pre-positioned** on every venue — no transfer/bridge delay in the critical path (see [[multi-venue-capital-management]])
- [ ] **Leg order decided** — harder-to-fill leg first; unwind plan if the second leg fails (see [[leg-risk]], [[execution-sequencing]])
- [ ] **Tail scenario priced** — what is the loss if the spread *widens* before it converges? (Ex.3 merger break, Ex.5 deeper depeg)
- [ ] **Hedge in place** for directional residual (Ex.5 stETH: short ETH perp; Ex.1 funding: short perp leg)
- [ ] **Monitoring live** — alerts and a circuit breaker per [[arbitrage-monitoring-setup]]
- [ ] **Position sized** so the worst-case loss is survivable (Ex.3: 5% allocation = ~1% portfolio hit on a break)

## Using These Examples

- **Calibrate expectations:** The funding rate example shows 83% APY was a golden period, not the norm. The cross-exchange example shows $2.74 profit on $1,785 — scale matters
- **Understand cost structure:** Every example decomposes costs. The flash loan example shows how costs can exceed the gross spread
- **Learn from timing:** Merger arb required 15 months of patience. Funding arb peaked in 2 weeks. Cross-exchange arb lasted 15 seconds
- **Apply to parameters:** Cross-reference these numbers with [[arbitrage-parameter-cheatsheet]] to validate the thresholds

## Related

- [[arbitrage-overview]] — the arbitrage strategy hub
- [[arbitrage-parameter-cheatsheet]] — thresholds these examples validate
- [[arbitrage-monitoring-setup]] — the monitoring/circuit-breaker stack for live execution
- [[arbitrage-live-performance]] — whether these strategies are still alive today
- [[arbitrage-seasonality]] — why the Ex.1 funding rate was a "golden period"
- [[transaction-cost-modeling]] — the cost-decomposition framework formalized
- [[leg-risk]] / [[execution-sequencing]] — the operational risks the checklist targets
- [[funding-rate-arbitrage]], [[cross-exchange-arbitrage]], merger-arbitrage, [[flash-loan-arbitrage]], [[lst-depeg-arbitrage]] — the strategies illustrated
- [[limits-to-arbitrage]] — why the residual risk in each example exists at all

## Sources

- Coinglass historical funding rate data (coinglass.com)
- SEC EDGAR filings (Activision/Microsoft merger proxy)
- Etherscan / Dune Analytics (on-chain transaction patterns)
- DefiLlama (stETH/ETH ratio history)
- [[arbitrage-parameter-cheatsheet]]
- [[arbitrage-live-performance]]
- [[transaction-cost-modeling]]
