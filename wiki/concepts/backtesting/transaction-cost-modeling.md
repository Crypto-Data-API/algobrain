---
title: "Transaction Cost Modeling"
type: concept
created: 2026-04-10
updated: 2026-06-21
status: excellent
tags: [backtesting, transaction-costs, slippage, market-impact, execution]
aliases: ["TCA", "Transaction Cost Analysis", "Cost Modeling"]
domain: [backtesting, market-microstructure]
difficulty: intermediate
related: ["[[backtesting-overview]]", "[[market-impact-models]]", "[[slippage-modeling]]", "[[bid-ask-spread]]", "[[execution-algorithms]]", "[[slippage]]", "[[implementation-shortfall]]", "[[failure-modes]]", "[[strategy-monitoring]]", "[[when-to-retire-a-strategy]]", "[[backtesting]]", "[[capacity-constraints]]"]
---

# Transaction Cost Modeling

A backtest without realistic transaction costs is fiction. Most strategies that look profitable on paper are unprofitable after honest cost accounting — and the gap between gross and net P&L is the single most common reason "great" strategies fail in production (see [[failure-modes]], failure mode "The Edge Was Never Real" and "Cost Inflation"). This page covers the components of trading cost, how to estimate them, and how to incorporate them into a [[backtesting|backtest]].

## Cost Components at a Glance

The full cost stack, summarised before the detail. Note which components are *explicit* (appear on a statement) versus *implicit* (you only see them by comparing your fill to a benchmark), and which scale with size:

| Component | Explicit/Implicit | Scales with | Hardest to model? | Typical share of total |
|---|---|---|---|---|
| Commissions | Explicit | Trade count | No | Small (often <1 bp equities) |
| [[bid-ask-spread\|Bid-ask spread]] | Implicit | Trade count | No | Moderate; dominant for liquid small trades |
| Market impact | Implicit | √(size/ADV) | **Yes** | Dominant at institutional size |
| [[slippage\|Slippage]] / [[implementation-shortfall]] | Implicit | Latency, volatility | Yes (HFT) | Dominant for HFT |
| Borrow / stock loan | Explicit | Short notional × time | No | Decisive for HTB shorts |
| Funding / financing | Explicit | Leverage × time | No | Can be a *return* (crypto perps) |
| Taxes | Explicit | Realised gains × rate | No | Decisive for taxable high-turnover |

The single most useful mental model: **explicit costs you can read off a statement; implicit costs you only discover by measuring your realised fill against a decision-time benchmark.** Backtests routinely capture the explicit layer and ignore the implicit one — which is exactly backwards, because the implicit layer is usually larger.

## The Components

A complete cost model has seven layers. Strategies vary in which layers dominate, but every layer applies to every strategy at some level.

### 1. Commissions

The explicit per-trade fee charged by the broker or exchange. The simplest component to model; usually the smallest.

- **US equities:** $0 retail (Robinhood, IBKR Lite), ~$0.005/share institutional. ~0-1 bps total.
- **Options:** $0.50-$0.75 per contract retail. Per-contract, not per-notional, so cost is high on cheap options.
- **Futures:** $0.85-$2.50 per side per contract.
- **Crypto:** 0-10 bps per side, depending on venue, tier, and maker/taker. Top crypto venues have maker rebates.
- **Forex:** spread-only at most retail brokers; commission models exist for ECN brokers (~$3/lot/side).

For most equities strategies, commissions are <1 bp — small but non-zero. For high-turnover strategies they accumulate. A strategy that trades 5x daily at 1 bp commission round-trip eats 1250 bps per year — destroying most edges.

### 2. Bid-Ask Spread

The difference between the best bid and the best offer. Crossing the spread (taking liquidity) costs you half the spread per side, so a full round-trip is one full spread.

- **Mega-cap equities (SPY, AAPL):** 1-2 bps round-trip
- **Large-cap equities:** 2-5 bps
- **Mid-cap equities:** 5-15 bps
- **Small-cap equities:** 15-50 bps
- **Microcap / illiquid:** 50-500+ bps
- **Liquid futures (ES, CL):** 1-3 bps
- **Liquid crypto pairs (BTC/USD):** 1-5 bps on top venues
- **Liquid options (SPY ATM):** 2-10 bps relative to underlying notional
- **Illiquid options (deep OTM, weekly):** 50-500+ bps

In a backtest, the conservative assumption is "I always cross the spread." A more realistic assumption is "I cross half the spread on average" (some trades are price-improved, some are paid-up). For market-making strategies, the assumption inverts — you collect the spread, not pay it, and the model becomes a fill-probability problem.

### 3. Market Impact

The price movement *caused by your own trade*. This is the dominant cost for institutional sizes and frequently the largest cost overall. It is also the hardest to model and the most often ignored.

The most cited model is the **square-root law**:

```
impact (bps) ≈ k × σ × √(Q / ADV)
```

Where:
- `σ` = daily volatility of the asset (in bps)
- `Q` = quantity to trade
- `ADV` = average daily volume
- `k` ≈ 0.5-1.5 depending on asset class and execution style

Implications:
- Impact is roughly proportional to the square root of trade-size-to-volume ratio (so doubling size multiplies impact by ~1.41)
- Impact scales linearly with volatility
- Impact has no lower bound — even tiny trades have some
- Impact is *temporary* (mean-reverting after the trade) plus *permanent* (caused by information signaled by the trade)

For a strategy trading 1% of ADV in a stock with 1.5% daily vol:
```
impact ≈ 0.7 × 150 bps × √(0.01) = 0.7 × 150 × 0.1 = 10.5 bps round-trip
```

For 10% of ADV in the same stock:
```
impact ≈ 0.7 × 150 × √(0.10) = 33 bps round-trip
```

A strategy that's profitable at 1% ADV but not at 10% ADV has discovered its capacity, not its alpha.

See [[market-impact-models]] for the full Almgren-Chriss framework and other variants.

### 4. Slippage (Implementation Shortfall)

The difference between the price you *thought* you'd get and the price you actually got, exclusive of spread and impact. Sources:

- Order arrival latency
- Adverse selection (you got filled because the market moved against you)
- Partial fills and order book churn
- Venue routing decisions

For a backtest, slippage is often modeled as a fixed bps cost per side on top of spread (e.g., +2 bps). For high-frequency strategies it dominates everything else and needs careful per-strategy modeling.

See [[slippage-modeling]] for details.

### 5. Borrow / Stock Loan Costs

Required for short positions. The borrower pays a fee to the lender, expressed as an annual rate on the dollar value of the short.

- **General collateral (most stocks):** 0.25-0.50% annualized
- **Special / hard-to-borrow:** 1-50% annualized
- **GME in early 2021:** spiked to >50% annualized
- **Most crypto perpetuals:** funding rate plays the equivalent role; can be either positive or negative

A short strategy on a HTB stock paying 25% borrow needs 25% of gross alpha *just to break even*. Many "great" short strategies in microcaps die here.

### 6. Funding / Financing Costs

For derivatives and leveraged positions:

- **Perpetual futures:** funding rate paid every 8 hours, can be positive or negative (long pays short or vice versa). Sometimes large positive returns are possible from collecting funding ([[funding-rate-arbitrage]]).
- **Margin loans:** broker call rate × leverage × time
- **Box spreads:** synthetic financing rate via deep ITM options, often cheaper than margin
- **Repo financing:** for institutional fixed-income strategies

### 7. Taxes (When Applicable)

Often left out of backtests but very real for taxable accounts:

- **US short-term capital gains:** ordinary income rate (up to 37% federal + state)
- **US long-term capital gains:** 0/15/20% federal
- **1256 contracts (futures, broad-based index options):** 60/40 long/short blend regardless of holding period
- **Wash sale rules** can defer losses across calendar years

A high-turnover strategy in a taxable account loses ~30-37% of gross gains *off the top* to short-term capital gains. The same strategy in a tax-deferred account loses 0%. This is often the difference between a viable and unviable strategy.

## How Costs Are Modeled in a Backtest

Knowing the cost components is only half the job; the other half is *where in the backtest loop* each cost is applied. There are three standard methods, in increasing order of fidelity:

| Method | How it works | Pros | Cons | When to use |
|---|---|---|---|---|
| **Fixed per-trade bps** | Subtract a constant bps from each fill (e.g. 7.5 bps/side) | Trivial; transparent; fast | Ignores size, volatility, regime | Early research; low-turnover strategies |
| **Component model** | Sum commission + spread + impact(size,ADV,σ) + slippage per fill | Captures size/volatility dependence | Needs ADV and vol inputs; calibration risk | Mid-stage validation; institutional sizing |
| **Tick / order-book replay** | Simulate fills against historical book depth, queue position, latency | Highest fidelity; captures partial fills | Expensive; needs tick data; overfitting risk | Late-stage HFT/market-making validation |

### The mechanics: applying cost at the fill

In a [[backtesting|backtest]] loop, cost is applied at the moment a simulated fill is recorded. The canonical pattern:

```
for each signal that generates an order:
    benchmark_price = decision_price            # mid at signal time
    side_sign       = +1 if buy else -1
    spread_cost     = 0.5 * spread_bps           # half-spread if crossing
    impact_cost     = k * sigma_bps * sqrt(qty / ADV)
    slippage_cost   = fixed_slippage_bps         # arrival latency, adverse selection
    commission      = per_share_or_per_contract_fee

    fill_price = benchmark_price * (1 + side_sign * (spread_cost + impact_cost + slippage_cost) / 1e4)
    cash       -= side_sign * qty * fill_price + commission

# carrying costs accrue per holding period, not per trade:
for each day a short is held:
    cash -= borrow_rate_annual / 252 * abs(short_notional)
for each funding interval a perp is held:
    cash -= funding_rate * perp_notional
```

The two rules that catch most mistakes:

1. **Per-trade costs** (commission, spread, impact, slippage) hit at the fill.
2. **Carrying costs** (borrow, funding, margin interest) accrue per unit of *time held*, independent of trade count — a common omission that flatters long-held short positions.

### Avoiding the lookahead trap in cost modeling

The benchmark price must be the price *available at decision time*, never the close or the VWAP of the bar you are trading into — using the bar's own close to fill is a subtle [[lookahead-bias|lookahead bias]] that makes impact and slippage vanish. Fill at the *next* bar's open or model an explicit arrival-to-fill delay.

## Building a Cost Model for Your Backtest

A reasonable cost model layers these components by strategy type. Three example calibrations:

### Strategy A: Daily long/short equity, mid-cap universe, 5% daily turnover

```
Commission:    0.5 bps / side
Spread:        4 bps / side
Impact:        2 bps / side (small relative to ADV)
Slippage:      1 bps / side
Borrow:        25 bps / year × short fraction × annualization
Total / side:  ~7.5 bps + borrow
Round-trip:    ~15 bps + borrow
```

A strategy with 20% expected gross annual return and 5% daily turnover (~12.5x annual) eats 15 × 12.5 = 187 bps just in execution. Add ~15 bps borrow on shorts and you're at ~200 bps drag. Net return: ~18%. Still viable.

### Strategy B: Intraday futures (ES) with 100 round-trips per day

```
Commission:    $1.00 / side / contract = ~1 bp on $250K notional
Spread:        1 tick = 0.25 → ~1.5 bps round-trip
Impact:        Small for ES, negligible at retail size
Slippage:      ~1 bp / side
Round-trip:    ~5 bps
```

100 round-trips × 5 bps = 500 bps per day = 125% per year in costs. Strategy needs to *clear* 125% gross just to break even. Most don't.

### Strategy C: Crypto basis trade (perp short + spot long)

```
Commission:    Maker rebate -1 bps / side on top crypto venues, or +5 bps taker
Spread:        1-3 bps round-trip
Impact:        Small at retail size on BTC/ETH; large on alts
Funding:       Variable, often the source of returns rather than cost
Borrow:        N/A
```

Funding becomes the main *return* driver, not a cost. The execution cost layer is small enough that the strategy is viable; the dominant question is whether funding stays positive.

### Round-trip cost cheat sheet by liquidity tier

A consolidated reference for the *typical, calm-market* round-trip cost (spread + commission + small-size impact) by instrument tier. All figures illustrative and regime-dependent — costs widen materially in stress (see the regime note below):

| Tier | Example | Round-trip (calm) | Round-trip (stress) | Dominant component |
|---|---|---|---|---|
| Mega-cap equity / liquid future | SPY, AAPL, ES, CL | 1-3 bps | 5-15 bps | Spread |
| Large-cap equity | most S&P 500 names | 3-8 bps | 15-40 bps | Spread + impact |
| Mid-cap equity | Russell midcap | 8-25 bps | 40-150 bps | Spread + impact |
| Small/micro-cap | sub-$1B mkt cap | 30-500+ bps | often untradeable | Impact + spread |
| Liquid crypto | BTC/USD, ETH/USD top venues | 2-8 bps | 20-100 bps | Spread + impact |
| Alt crypto | thin pairs | 30-300+ bps | gaps | Spread + impact |
| Liquid index options | SPY/SPX ATM | 2-12 bps (vs underlying notional) | 30-200 bps | Spread |
| Illiquid options | deep-OTM weeklies | 50-500+ bps | quote vanishes | Spread |

> **Regime caveat:** these are calm-market numbers. In a stress regime spreads widen 3-10×, impact rises with volatility (impact scales linearly with σ in the square-root law), and liquidity in the thinnest tiers can disappear entirely. A cost model calibrated to a calm period systematically understates stress-period drag — the [[failure-modes#5. Cost Inflation|cost inflation]] failure mode.

### Turnover is the multiplier that kills edges

Round-trip cost matters only in proportion to how often you pay it. The annual cost drag is `round-trip cost × annual round-trips`, so turnover is the lever that turns a small cost into a fatal one:

| Strategy style | Approx. annual round-trips | Round-trip cost it can absorb at 15% gross |
|---|---|---|
| Long-term / position | 1-4 | 375-1500 bps |
| Swing | 10-50 | 30-150 bps |
| Daily systematic | ~250 | ~6 bps |
| Intraday | thousands | <1 bp |
| HFT | millions | fractions of a bp |

This is the heart of why high-frequency strategies need vanishingly small per-trade costs and why a "great" intraday strategy with a 5 bps round-trip cost and 100 round-trips/day must clear ~125% gross annually just to break even (Strategy B above). Turnover discipline is a cost-management decision, not just a signal decision.

## Conservative vs. Realistic Modeling

Two approaches in a backtest:

### Conservative
Always assume worst-case fills. Take all liquidity, cross full spread, apply maximum impact. The result is a *lower bound* on net performance. If the strategy is still profitable under this assumption, it is almost certainly profitable in practice.

### Realistic
Model fill probabilities, partial fills, and execution venue routing. Calibrate to historical execution data if available. The result is a *more accurate* expected performance but harder to defend.

Choose conservative for early-stage research and realistic for late-stage validation. A common workflow:

1. **Naive backtest (no costs)** — does the gross effect exist at all?
2. **Conservative backtest** — does it survive worst-case execution?
3. **Realistic backtest** — what's the actual expected net Sharpe?
4. **Live paper trading** — does the realistic model match reality?

## The Cost Sensitivity Plot

For any strategy, plot net Sharpe as a function of round-trip cost (in bps). Net Sharpe should decline smoothly. The point at which net Sharpe crosses zero is the *breakeven cost*.

A strategy with breakeven cost of 30 bps and realistic cost of 5 bps has lots of headroom. A strategy with breakeven cost of 6 bps and realistic cost of 5 bps is on the edge — small cost increases will kill it. The gap between realistic and breakeven cost is the strategy's *cost margin of safety*.

| Breakeven cost | Realistic cost | Margin of safety | Verdict |
|---|---|---|---|
| 30 bps | 5 bps | 25 bps (6×) | Robust — survives cost inflation |
| 12 bps | 5 bps | 7 bps (~2.4×) | Acceptable — monitor cost drift |
| 6 bps | 5 bps | 1 bp (1.2×) | Fragile — kill on any cost spike |
| 4 bps | 5 bps | negative | Already unviable — do not deploy |

## TCA as a Live Signal, Not Just a Research Exercise

Transaction-cost modeling is usually framed as a backtesting step, but its highest-leverage use is *live*. Costs inflate over time — spreads widen, borrow spikes, competition tightens fills — and a strategy that was viable at deployment can quietly cross its breakeven cost months later. This is the [[failure-modes#5. Cost Inflation|cost inflation]] failure mode, and the only defense is to measure realised cost per trade continuously and alert on drift.

The handoff to live monitoring:

| Research artifact | Live monitoring counterpart |
|---|---|
| Modeled cost per trade | Realised cost per trade (compare daily) |
| Breakeven cost from sensitivity plot | Kill criterion when realised cost approaches it |
| Capacity estimate from impact model | Slippage-vs-size tracking as AUM grows |
| Assumed borrow rate | Live borrow-rate alert |

See [[strategy-monitoring]] for the cost-drift alert thresholds (the "Cost drift" and "Borrow rate changes" rows of its L3 edge-health table) and [[when-to-retire-a-strategy]] for the kill decision once realised cost erodes the margin of safety.

## Common Mistakes

1. **Using midpoint fills** — a backtest that fills at the bid-ask midpoint assumes you're posting passively. If your strategy is taking liquidity, this overstates returns by the half-spread.
2. **Ignoring impact at small size** — even at $1M positions in mid-caps, impact is non-zero. Square-root law applies all the way down.
3. **Forgetting borrow** — short backtests without borrow costs are routinely off by 5-25% per year on small caps.
4. **Static cost models** — costs change. A strategy backtested with 2015 spreads may face very different 2024 spreads on the same instruments.
5. **No taxes for taxable accounts** — high-turnover strategies are often only viable in tax-advantaged accounts.

## Sources

- Almgren, Thum, Hauptmann, Li (2005) "Direct Estimation of Equity Market Impact" — RiskMetrics
- Almgren & Chriss (2001) "Optimal Execution of Portfolio Transactions" — *Journal of Risk*
- Kyle (1985) "Continuous Auctions and Insider Trading" — *Econometrica* (foundational impact model)
- [[book-trading-and-exchanges]] — Harris on the full microstructure picture
- [[book-advances-in-financial-machine-learning]] — López de Prado on backtest cost modeling

## Related

- [[backtesting-overview]]
- [[backtesting]]
- [[market-impact-models]]
- [[slippage-modeling]]
- [[slippage]]
- [[bid-ask-spread]]
- [[execution-algorithms]]
- [[implementation-shortfall]]
- [[failure-modes]] — cost inflation as a strategy-mortality mode
- [[strategy-monitoring]] — turning the cost model into a live alert
- [[when-to-retire-a-strategy]] — killing a strategy whose cost margin is gone
- [[capacity-constraints]] — where impact dominates and capacity is reached
- [[lookahead-bias]] — the trap that makes modeled costs vanish
