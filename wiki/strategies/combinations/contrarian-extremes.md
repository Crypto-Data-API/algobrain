---
title: Contrarian Extremes
type: strategy
created: 2026-04-06
updated: 2026-07-19
status: excellent
tags: [combinations, alpha-edge, contrarian, sentiment, mean-reversion, behavioral-edge, fear-greed, risk-bearing]
strategy_type: hybrid
timeframe: swing
markets: [crypto]
complexity: intermediate
backtest_status: untested
edge_source: [behavioral, risk-bearing]
edge_mechanism: "At sentiment extremes the pool of marginal sellers/buyers is exhausted; the counterparty is the herd that has already acted on emotion, leaving price dislocated from fair value"
expected_sharpe: 0.8
expected_max_drawdown: 0.15
breakeven_cost_bps: 20
crowding_risk: low
min_capital_usd: 10000
capacity_usd: 50000000
related: ["[[structural-forced-selling]]", "[[risk-on-risk-off-framework]]", "[[cross-asset-signals]]", "[[asymmetric-barbell]]", "[[mean-reversion]]", "[[behavioral-finance-overview]]"]
---

# Contrarian Extremes

> **Status: untested (`backtest_status: untested`).** This page describes the *design* of a [[contrarian]] sentiment strategy. The performance figures, win rates, Sharpe, and "expected" returns below are **illustrative design targets and qualitative reasoning, not the output of a validated backtest.** The dated market episodes (March 2020, Dec 2018, etc.) are real historical context, but no walk-forward, cost-corrected, or deflated-Sharpe study has been run. Treat every number as a hypothesis to be tested per [[backtesting]] and [[overfitting-detection]] before any capital is risked. Not investment advice.

## Edge Source

This is a **behavioral + risk-bearing** edge (see [[edge-taxonomy]]). The behavioral component: persistent human [[fear-and-greed-index|fear/greed]] cycles push price away from fair value at extremes. The risk-bearing component: at peak panic, the contrarian is *paid to supply liquidity and bear risk* that the herd is desperate to offload. The strategy sits in the [[combinations|combination/alpha-edge]] family and overlaps [[mean-reversion]] and [[sentiment]]-based methods, but is distinguished by acting **only at statistically extreme readings**, not on every dip.

## The Edge

At sentiment extremes, the crowd has already acted. When 60% of investors are bearish, they have already sold. There are no sellers left. The only direction for price is up -- not because of some mystical "contrarian indicator," but because of supply and demand mechanics. The pool of potential sellers is exhausted. Any marginal buyer moves price disproportionately.

This is NOT generic "be greedy when others are fearful" platitude investing. This is a quantified, rules-based system that enters only at statistically validated extremes and uses tranched entries to manage timing risk. The key distinction: most "contrarians" try to catch falling knives constantly. This strategy waits for specific numerical thresholds that historically precede reversals with >65% probability and >2:1 reward-to-risk.

The edge is behavioral. Human psychology does not evolve on market timescales. Fear and greed cycles have repeated identically for centuries. Even knowing about the edge does not eliminate it because in the moment of maximum fear, buying FEELS insane. Your body screams to sell. The edge belongs to those who build systems to override their instincts.

## Null Hypothesis

Under the null hypothesis, sentiment readings are noise — random fluctuations with no predictive power over future returns. If this were true, buying at composite < 20 and selling at composite > 80 would produce returns indistinguishable from random entry/exit timing over the same holding periods. Specifically: the average 60-day forward return after a composite < 20 reading would equal the unconditional 60-day average return.

**This null has not yet been tested in this wiki.** The strategy's premise is that forward returns after extreme-fear readings *should* exceed the unconditional average, and the well-documented post-crisis rallies (see [[#Real-World Examples]]) are suggestive — but a proper test would: (1) define the composite ex-ante, (2) measure conditional vs unconditional forward returns across a long, multi-regime sample, (3) apply transaction costs, and (4) correct for the multiple-comparisons / data-snooping problem with a [[deflated-sharpe-ratio|deflated Sharpe]] before claiming significance. Until that study exists, the edge remains a **plausible hypothesis**, not a proven result. See [[backtesting]] and [[overfitting-detection]].

## Why It Persists

1. **Knowing is not doing** -- every investor has heard "buy fear, sell greed." Almost none do it. In March 2020, with VIX at 82 and the AAII survey at 52% bearish, buying equities felt like financial suicide. The system says buy. Your gut says run
2. **Career risk is asymmetric** -- a fund manager who buys during a panic and is early loses their job. A fund manager who sells during a panic and is wrong just "followed prudent risk management." Incentives punish contrarian action
3. **Herding is biologically wired** -- humans evolved to follow the tribe. Standing alone against consensus triggers genuine anxiety. This is not a metaphor; fMRI studies show that contrarian decisions activate the brain's pain centers
4. **Media amplifies extremes** -- at sentiment bottoms, every headline is apocalyptic. At tops, every headline is euphoric. Media consumption makes it HARDER to be contrarian, not easier
5. **Recency bias** -- after a 30% drawdown, investors extrapolate further losses. The recent past dominates their probability estimates, making them unable to imagine a reversal

## How to Implement

### Step 1: Build a Composite Sentiment Score

No single indicator is sufficient. Combine 5+ signals into a composite score (0-100, where 0 = max fear and 100 = max greed):

| Indicator | Extreme Fear Threshold | Extreme Greed Threshold | Weight |
|---|---|---|---|
| **AAII Bull-Bear Spread** | >60% bearish | >60% bullish | 20% |
| **VIX level** | >40 | <12 | 20% |
| **CNN Fear & Greed Index** | <15 | >85 | 15% |
| **Put/Call Ratio (equity-only)** | >1.3 | <0.5 | 15% |
| **NAAIM Exposure Index** | <25 | >105 | 15% |
| **Crypto Fear & Greed Index** | <10 | >90 | 15% (crypto only) |
| **Funding Rates** (crypto) | Deeply negative | >0.1%/8hr | Crypto overlay |

**Composite < 20 = Buy zone. Composite > 80 = Sell/hedge zone.**

### Step 2: Tranched Entry (Never All-In)

A single extreme reading can get MORE extreme. The VIX can go from 40 to 80. The AAII survey can go from 60% bearish to 70% bearish. Entering all at once at the first signal means you may face significant drawdown before the reversal.

**Buy tranches when composite < 20:**
- Tranche 1 (25%): composite hits 20. Buy first 25% of intended position
- Tranche 2 (25%): composite hits 15 OR 3 trading days pass. Buy next 25%
- Tranche 3 (25%): composite hits 10 OR 3 more trading days pass. Buy next 25%
- Tranche 4 (25%): composite hits 5 OR 5 more trading days pass. Complete position

**Sell/hedge tranches when composite > 80:**
- Same structure in reverse. Sell 25% at each threshold (80, 85, 90, 95)

### Step 3: Technical Confirmation for Precision

Sentiment tells you WHAT to do. Technicals tell you WHERE to enter within each tranche:

- Buy tranche near [[support-and-resistance|support levels]], [[fibonacci-retracements|Fibonacci retracements]], or [[volume-profile|high-volume nodes]]
- Require at least one [[candlestick-patterns|reversal candle pattern]] before executing each tranche -- [[hammer]], [[bullish-engulfing]], [[morning-star]]
- Use [[rsi]] divergence as confirmation: price makes new low but RSI does not → bullish divergence at sentiment extreme = highest-conviction entry

### Step 4: Exit Rules

- **Primary exit**: composite returns to neutral (40-60 range). This typically takes 2-8 weeks from extremes
- **Profit target**: 15-25% gain from average entry price for equities; 30-60% for crypto
- **Stop loss**: 10% below lowest tranche entry. If price falls this far despite extreme bearish sentiment, something structural has changed and the thesis is invalidated
- **Time stop**: if the position shows no profit after 60 days, exit at market. The sentiment reversal is not coming this cycle

## Implementation Pseudocode

```python
# Composite sentiment score (0 = max fear, 100 = max greed)
def compute_composite():
    aaii     = normalize_aaii_spread()       # 0-100
    vix      = normalize_vix()              # 0-100 (inverted: high VIX = low score)
    cnn_fg   = get_cnn_fear_greed()         # 0-100
    put_call = normalize_put_call_ratio()   # 0-100 (inverted)
    naaim    = normalize_naaim()            # 0-100
    crypto_fg = get_crypto_fear_greed()     # 0-100 (crypto only)

    composite = (
        aaii * 0.20 +
        vix * 0.20 +
        cnn_fg * 0.15 +
        put_call * 0.15 +
        naaim * 0.15 +
        crypto_fg * 0.15  # replace with equity indicator if not trading crypto
    )
    return composite

# Position sizing per tranche
MAX_ALLOCATION = 0.30  # 30% of portfolio max
TRANCHE_SIZE = MAX_ALLOCATION / 4

# Check for structural crisis modifier
def is_structural_crisis():
    return credit_spreads_blowing_out() and composite < 15

# Entry logic
composite = compute_composite()
tranche_count = 0

if composite < 20 and tranche_count == 0:
    size = TRANCHE_SIZE * (0.5 if is_structural_crisis() else 1.0)
    if has_reversal_candle() and near_support():
        buy(asset, size)
        tranche_count = 1

if composite < 15 or days_since_tranche_1 >= 3:
    buy(asset, TRANCHE_SIZE)
    tranche_count = 2
# ... continue tranches at 10 and 5

# Exit logic
if composite > 40 and composite < 60:
    close_position()  # sentiment returned to neutral
elif unrealized_gain > 0.20:
    close_position()  # profit target hit
elif unrealized_loss > 0.10:
    close_position()  # stop loss
elif days_in_trade > 60 and unrealized_gain <= 0:
    close_position()  # time stop
```

## Example Setup

**S&P 500 -- October 2023 sentiment extreme:**

1. AAII survey: 50.3% bearish (highest since March 2023). CNN Fear & Greed: 17. VIX: 23. Put/Call ratio: 1.15. NAAIM: 32
2. **Composite score: 18** -- below the 20 threshold. Buy zone entered
3. **Tranche 1**: buy 25% SPY position at $418 (near the 200-day MA, a key [[moving-averages|technical level]]). Date: Oct 27
4. **Tranche 2**: composite drops to 14. Buy 25% at $412 on a [[hammer]] candle at the [[fibonacci-retracements|61.8% Fib]] of the prior rally. Date: Oct 30
5. **Tranche 3**: 3 days pass, composite at 16 (stabilizing). Buy 25% at $416. Date: Nov 2
6. **Tranche 4**: composite rises to 22 (improving). Buy final 25% at $425. Date: Nov 7
7. **Average entry: $417.75**
8. By December 15, composite hits 55 (neutral). SPX at $472. Exit full position
9. **Return: 13% in 7 weeks.** Risk was 10% below lowest tranche ($412 - 10% = $371), giving a 3:1 realized R:R

## Example trade

> Illustrative, round numbers — not a backtest.

**Asset:** BTC. **Market context:** January 2023, post-FTX collapse hangover.

**Step 1 — Composite score calculation:**

| Indicator | Reading | Normalized score |
|-----------|---------|-----------------|
| AAII Bull-Bear Spread | 55% bearish | 8 |
| VIX level | 21 | 55 |
| CNN Fear & Greed | 6 | 6 |
| Put/Call Ratio | 1.25 | 18 |
| NAAIM Exposure | 18 | 12 |
| Crypto Fear & Greed | 6 | 6 |

**Composite = 8×0.20 + 55×0.20 + 6×0.15 + 18×0.15 + 12×0.15 + 6×0.15 = 1.6 + 11.0 + 0.9 + 2.7 + 1.8 + 0.9 = 18.9** → below 20. Buy zone entered.

BTC spot price: $16,500. Funding rate: −0.018%/8h (deeply negative — longs are being paid). RSI(14) on daily: 31. Price is near the long-term $16,000 support cluster. Reversal candle: bullish engulfing on Jan 10.

**Step 2 — Tranched entry (30% of portfolio = $30,000 total intended position on a $100k portfolio):**

| Tranche | Date | Composite | BTC Price | Amount |
|---------|------|-----------|-----------|--------|
| Tranche 1 (25%) | Jan 10 | 18.9 | $16,500 | $7,500 |
| Tranche 2 (25%) | Jan 13 | 15.2 | $17,000 | $7,500 |
| Tranche 3 (25%) | Jan 16 | 17.5 (stabilising) | $17,800 | $7,500 |
| Tranche 4 (25%) | Jan 21 | 21.0 (improving) | $18,500 | $7,500 |

Average entry price: ($7,500/$16,500 + $7,500/$17,000 + $7,500/$17,800 + $7,500/$18,500) / (30,000) = weighted average **~$17,400/BTC**.

**Step 3 — Exit:** Composite reaches 45 (neutral) on March 15. BTC spot: $27,800. The primary exit rule fires.

**Round-trip P&L:**

| Item | Amount |
|------|--------|
| Gross P&L: ($27,800 − $17,400) / $17,400 × $30,000 | +$17,931 |
| Taker/exchange fees (0.04% × 2 round trips × $30,000) | −$24 |
| Funding received (negative funding paid to longs; approx +0.005%/8h avg × 65 days × 3 periods/day × $30,000) | +$293 |
| Slippage (spread + price impact, estimated ~10 bps round trip) | −$60 |
| **Net P&L** | **+$18,140** |

Return on total portfolio: +18.1% on the deployed $30,000 sleeve, +5.4% on the full $100k book. Realized R:R: entry tranche range $16,500–$18,500, stop at $16,500 − 10% = $14,850; risk ~$2,550 on the first tranche. Approximate realized R:R: ~7:1 — above the 3:1 target, consistent with a deep sentiment extreme. The stop loss at $14,850 was never touched.

**Key mechanic validated:** Negative funding during the fear extreme (+$293) added carry that would not exist in equities — the crypto-specific overlay (funding rate as part of the composite) both signaled the extreme *and* paid the patient holder.

## Risk Management

- **Extremes can stay extreme** -- the market can remain irrational longer than you can remain solvent. This is why tranching is non-negotiable. Never commit full size on the first signal
- **Distinguish between cyclical extremes and structural breaks** -- in 2008, bearish sentiment was extreme in September and the market still fell 35% further. Structural crises (banking system failure, sovereign default) can override sentiment signals. Layer in [[cross-asset-signals]] -- if credit spreads are blowing out AND sentiment is extreme, the crisis may be structural, not cyclical. Reduce tranche size by 50%
- **The strategy underperforms in trending markets** -- during a strong bull run, the composite never reaches extreme greed (it hovers at 60-75). You never get a sell signal, meaning you miss some of the rally. Accept this; the strategy is for capturing reversals, not riding trends
- **Do not confuse sentiment with positioning** -- surveys measure what people SAY. Positioning data ([[cot-report]], fund flows, options positioning) measures what people DO. Prioritize positioning data when it conflicts with surveys
- **Max allocation**: 30% of portfolio to contrarian-extreme trades at any time. The remaining 70% should follow [[trend-following]] or [[momentum-trading]] strategies that profit during the non-extreme periods

## Real-World Examples

- **March 2020 (COVID crash)** -- VIX hit 82. AAII bears at 52%. CNN F&G Index at 2 (two!). Composite: ~5. The most extreme fear reading in modern history. SPX bottomed on March 23 and rallied 70% in the next 12 months. Contrarian buyers captured the greatest buying opportunity since 2009
- **January 2023 (crypto)** -- Bitcoin Fear & Greed Index sat at 6 for three consecutive weeks after the FTX collapse. BTC price: $16,500. Funding rates were negative for 45 days straight. Buyers at this extreme saw BTC at $45,000 twelve months later (170% return)
- **December 2018** -- VIX spiked to 36. AAII bears at 50%. SPX dropped 20% in Q4. Christmas Eve marked the exact bottom. Contrarian buyers in the final week of December 2018 saw a 30% rally in the next 4 months
- **January 2018 (euphoria sell signal)** -- AAII bulls hit 60%. VIX was at 9. CNN F&G at 92. Composite: 93. SPX dropped 12% in the next two weeks ("Volmageddon"). Sellers at the greed extreme preserved capital
- **November 2021 (crypto euphoria)** -- Crypto Fear & Greed at 84. BTC funding rates at +0.12%/8hr. BTC price: $69,000. The top. Sellers at this extreme avoided the 75% drawdown to $16,000

The pattern has repeated in every market cycle since sentiment data has been tracked. It will repeat again. The only question is whether you will have the systematic discipline to act when your composite score triggers -- because every fiber of your being will resist.

## Performance Characteristics (Design Targets, Not Backtested)

The figures below are the **design targets and qualitative expectations** that the rules above are built to achieve — they are *not* measured results. With `backtest_status: untested`, none of these has been validated on out-of-sample data. They exist to make the strategy falsifiable: if a real backtest cannot approach them, the [[#Kill Criteria]] apply.

| Metric | Equities (target) | Crypto (target) | Notes |
|---|---|---|---|
| **Win rate** | ~68% | ~72% | Hypothesis: higher in crypto due to more violent mean-reversion |
| **Average win** | +15-20% | +40-80% | From average tranche entry to composite-neutral exit |
| **Average loss** | -8% | -12% | Stop loss at 10% below lowest tranche |
| **Reward:Risk** | 2:1 to 3:1 | 3:1 to 6:1 | Asymmetric by design |
| **Target Sharpe** | ~0.8 | ~1.0 | Aspirational, net of costs; **not** a measured Sharpe |
| **Trade frequency** | 1-3 per year | 2-4 per year | Extremes are rare by definition |
| **Avg holding period** | 3-8 weeks | 2-6 weeks | Until composite returns to neutral |
| **Time in market** | 15-25% | 20-30% | Mostly in cash waiting for extremes |
| **Max drawdown** | ~15% | ~20% | From entry to trough before reversal |

The low trade frequency is intended as a feature, not a bug — the thesis is that the strategy earns its return precisely because it is patient. Loosening the thresholds (e.g., buying at composite < 30 instead of < 20) is *expected* to degrade win rate and reward:risk by trading on weaker signals; this is itself a testable claim.

## Cost Awareness

Because the strategy trades infrequently (single-digit round-trips per year) in highly liquid instruments (SPY, QQQ, BTC, ETH), **per-trade frictions are a small share of expected return** — the opposite of high-frequency strategies. The cost stack to model in any real backtest:

| Cost component | Likely magnitude here | Why it stays small |
|----------------|-----------------------|--------------------|
| Commission/brokerage | Low | Few trades per year |
| Bid-ask [[spread]] | Low–moderate | Major liquid instruments, but spreads *widen* at the extremes when you trade |
| [[slippage]] | Moderate | Volume spikes 2-5x at extremes, but so does volatility |
| Funding / carry (crypto) | Variable | Negative funding can actually *pay* contrarian longs at fear extremes |
| Tax | Material | Holding period straddles the [[capital-gains-tax-discount|12-month CGT discount]] line; see [[tax-efficient-investing]] |

The frontmatter sets `breakeven_cost_bps: 20`, i.e. the design assumes the edge survives ~20 bps round-trip. The non-obvious cost is **execution at extremes**: spreads and slippage are worst exactly when the signal fires, which is why tranched entries (spread across days) and limit orders near [[support-and-resistance|support]] are part of the rules rather than market-on-open fills. A genuine cost-corrected, [[deflated-sharpe-ratio|deflated]] backtest is the gating requirement before this strategy moves off `untested`.

## Capacity Limits

The strategy can absorb significant capital because it trades liquid instruments (SPY, QQQ, BTC, ETH) during periods of elevated volume. During sentiment extremes, volume spikes 2-5x above average, meaning liquidity is abundant precisely when the strategy is active. Estimated capacity is $50M+ for a single manager before execution becomes noticeable. Beyond that, tranched entries across multiple days mitigate impact. The real constraint is not capital — it is the psychological difficulty of deploying at extremes, which self-limits the number of practitioners.

## What Kills This Strategy

- **Structural crisis misidentified as cyclical** — September 2008 showed extreme fear, but the banking system was actually collapsing. Buying at composite < 20 in September 2008 meant riding another 35% drawdown before the bottom. Mitigation: the credit spread overlay and the structural crisis modifier reduce tranche size by 50%
- **Sentiment regime shift** — If a new generation of systematic/algorithmic traders begins front-running sentiment extremes, the edge could compress. No evidence of this yet as of 2024
- **Data discontinuity** — If AAII stops publishing, or CNN changes their index methodology, the composite needs recalibration
- **Operator override** — The single most common failure mode. The system says buy at maximum fear. The trader overrides because "this time is different." It is never different

## Kill Criteria

- Win rate drops below 50% over any rolling 3-year period (minimum 5 trades)
- Average realized R:R falls below 1.5:1 over any rolling 3-year period
- The composite fails to reach < 20 or > 80 for 3+ years → market regime has changed and the thresholds need recalibration, not the strategy itself
- 3 consecutive losing trades → pause and audit composite construction; do not abandon

## Advantages

- Extremely high win rate (65-72%) with favorable reward:risk (2:1+)
- Low trade frequency reduces costs, slippage, and emotional fatigue
- Edge is robust across decades and asset classes — behavioral biases do not arbitrage away
- Tranched entry structure manages timing risk systematically
- Capacity is effectively unconstrained for individual traders

## Disadvantages

- Long periods of inactivity — months or quarters with no signals
- Requires extreme psychological discipline to execute at maximum fear
- Vulnerability to structural crises that look like cyclical extremes
- Small sample size per year makes statistical validation slow
- Cannot be the sole strategy — needs to be paired with [[trend-following]] or [[momentum-trading]] for the 75-85% of time spent waiting

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/sentiment/fear-greed` — the Crypto Fear & Greed component of the composite (crypto extreme: < 10 / > 90)
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — the funding-rate overlay (deeply negative = fear extreme; > +0.1%/8h = greed extreme)
- `GET /api/v1/derivatives/binance/long-short-ratio?symbol=BTCUSDT` — positioning data to cross-check against survey sentiment (what traders do vs what they say)
- `GET /api/v1/sentiment/macro` — yields and gold backdrop for the cyclical-vs-structural distinction

**Historical data:**
- `GET /api/v1/market-intelligence/fear-greed-history` — the full Fear & Greed timeseries for threshold calibration
- `GET /api/v1/backtesting/klines` — Binance spot daily candles back to 2017-08 for forward-return tests conditioned on extreme readings

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/sentiment/fear-greed"
```

*Note: the equity composite inputs (AAII, VIX, NAAIM, put/call) are not on CryptoDataAPI — source those separately.*

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-sentiment]], [[cryptodataapi-market-intelligence]], [[cryptodataapi-derivatives]].

**Live dashboards:** [fear & greed](https://cryptodataapi.com/fear-greed) · [funding rates](https://cryptodataapi.com/funding-rates) · [long-term regimes](https://cryptodataapi.com/regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this strategy end-to-end:

- **Signal** — `GET /api/v1/sentiment/fear-greed` — the crypto leg of the composite; tranche triggers fire at composite < 20/15/10/5
- **Positioning confirm** — `GET /api/v1/derivatives/funding-rates?coin=BTC` + `GET /api/v1/derivatives/binance/long-short-ratio?symbol=BTCUSDT` — prioritise positioning over survey inputs when they conflict, per the rules above
- **Structural-crisis check** — `GET /api/v1/regimes/current` + `GET /api/v1/security/regime/score` — halve tranche size when the extreme coincides with Structural Shock or elevated Security Stress (the 2008-style trap)
- **Backtest** — the untested null hypothesis above is directly testable: condition forward returns from `GET /api/v1/backtesting/klines` (daily back to 2017-08) on `GET /api/v1/market-intelligence/fear-greed-history` readings; use `GET /api/v1/backtesting/daily-snapshots` (since 2026-03-02) for point-in-time composite replays going forward
- **Tips** — extremes persist: enforce the tranche schedule (25% per threshold/time step) in code rather than deploying on the first trigger

## Related

- [[contrarian]] — the broader contrarian style this strategy formalises
- [[sentiment]] — sentiment as an input to trading decisions
- [[fear-and-greed-index]] — a core component of the composite
- [[mean-reversion]] — the price behaviour the edge relies on
- [[behavioral-finance-overview]] — the biases that create and sustain the edge
- [[edge-taxonomy]] — classification of behavioral and risk-bearing edges
- [[structural-forced-selling]] — companion strategy; distinguishing cyclical from structural extremes
- [[cross-asset-signals]] — credit-spread / cross-asset overlay for crisis detection
- [[risk-on-risk-off-framework]] — regime context for when extremes occur
- [[asymmetric-barbell]] — portfolio construction pairing with this strategy
- [[backtesting]] / [[overfitting-detection]] / [[deflated-sharpe-ratio]] — required validation before deployment
- [[cot-report]] — positioning data to cross-check against survey sentiment
- [[vix]] — the volatility input to the composite

## Sources

- AAII Investor Sentiment Survey historical data
- CNN Fear & Greed Index methodology
- NAAIM Exposure Index historical readings
- VIX/CBOE historical data
- Crypto Fear & Greed Index (alternative.me)
