---
title: "Credit Spread"
type: strategy
created: 2026-04-15
updated: 2026-06-20
status: excellent
tags: [options, derivatives, risk-management, swing-trading, volatility]
aliases: ["Credit Spread", "Credit Spreads", "Vertical Credit Spread", "Bull Put Spread", "Bear Call Spread"]
related: ["[[options]]", "[[options-pricing]]", "[[risk-management]]", "[[theta-decay]]", "[[implied-volatility]]", "[[covered-calls]]", "[[iron-condor]]", "[[trade-repair-and-rolling]]", "[[gamma-risk]]", "[[vertical-spread]]", "[[delta]]", "[[theta]]", "[[vega]]", "[[gamma]]", "[[variance-risk-premium]]", "[[options-premium-selling]]", "[[iv-rank-and-iv-percentile]]", "[[market-regime]]", "[[edge-taxonomy]]", "[[position-sizing]]", "[[volatility-trading]]", "[[wheel-strategy]]", "[[tradestation-options-workflow]]"]
strategy_type: technical
timeframe: swing
markets: [stocks, options]
complexity: intermediate
backtest_status: untested
edge_source: [risk-bearing, behavioral]
edge_mechanism: "Sells overpriced OTM options to hedgers and lottery-ticket buyers, harvesting the variance risk premium while the long leg caps tail exposure"
data_required: [options-chain, ohlcv-daily, implied-volatility]
min_capital_usd: 5000
capacity_usd: 25000000
crowding_risk: medium
expected_sharpe: 0.6
expected_max_drawdown: 0.25
breakeven_cost_bps: 25
---

A credit spread is an [[options]] strategy in which a trader simultaneously sells a higher-premium option and buys a lower-premium option of the same type (both calls or both puts) with the same expiration date but different strike prices. The net effect is a credit received at entry, which represents the maximum possible profit. The bought option limits the maximum possible loss, making this a defined-risk strategy that is widely used for income generation and directional betting with controlled downside.

## Overview

Credit spreads are one of the most popular options strategies among active traders because they offer a favorable combination of defined risk, high probability of profit, and capital efficiency. Unlike naked option selling, where the potential loss is theoretically unlimited, a credit spread's maximum loss is capped at the width of the strikes minus the credit received. This defined-risk profile also means credit spreads require significantly less margin than naked positions.

The strategy profits primarily from [[theta-decay]]: as time passes, the sold option (which has more time value because it is closer to the money) decays faster than the bought option, and the spread narrows toward zero if the underlying stays in a favorable zone. The full credit is kept if both options expire worthless.

Credit spreads come in two primary forms based on directional bias: **bull put spreads** (bullish) and **bear call spreads** (bearish). Both can be combined into an [[iron-condor]] (selling both a bull put spread and a bear call spread simultaneously) to create a non-directional credit strategy. The credit spread is the canonical defined-risk building block of the broader [[options-premium-selling]] family and the structural complement of the [[vertical-spread]] (the credit spread *is* a vertical spread sold for a net credit rather than bought for a net debit).

### Credit spread vs. related structures

| Structure | Net cash flow | Directional bias | Risk profile | When preferred |
|-----------|---------------|------------------|--------------|----------------|
| **Credit spread** (this page) | Credit in | Bullish (put) / bearish (call) | Defined risk, defined reward | Elevated IV, high-POP income |
| Debit [[vertical-spread]] | Debit out | Directional | Defined risk, defined reward | Low IV, directional conviction |
| Naked short option | Credit in | Directional | Defined reward, ~unlimited risk | Never recommended for retail |
| [[iron-condor]] | Credit in (×2) | Neutral | Defined risk both sides | Range-bound, high IV |
| [[covered-calls]] | Credit in | Mildly bullish | Stock downside + capped upside | Hold underlying, generate yield |

## Edge source

**Risk-bearing**, with a **behavioral** component (per [[edge-taxonomy]]).

- *Risk-bearing*: short options harvest the **[[variance-risk-premium]]** — [[implied-volatility]] in equity index and most single-stock options has persistently traded above subsequently realized volatility (typically by a few volatility points on average for index options across multi-decade samples). The option seller is paid an insurance premium for bearing the risk of adverse moves; the long leg of the spread re-insures the tail, keeping part of the premium while capping ruin risk.
- *Behavioral*: the buyers of the OTM options being sold are often hedgers who systematically overpay for protection (puts) and speculators who overpay for lottery-like convexity (cheap OTM calls/puts). Both flows are price-insensitive relative to fair value, sustaining the premium.

## Why this edge exists

- **Who is on the other side**: (1) institutional hedgers — funds mandated or incentivized to buy index put protection regardless of price; (2) retail speculators buying cheap OTM options for leveraged directional bets; (3) structured-product desks hedging exotic books.
- **Why they keep "losing"**: hedgers are not trying to win — they pay the premium deliberately, the way homeowners pay for fire insurance; the premium is the cost of tail protection and sleep. Lottery-ticket buyers persistently overpay because of probability-weighting bias (overweighting small probabilities, per prospect theory) — a stable behavioral trait, not a correctable mistake. These flows regenerate every expiration cycle.
- **Why it persists**: bearing this risk is genuinely painful. The strategy's payoff is short-volatility — many small wins punctuated by occasional large losses clustered in crashes, exactly when everything else in a portfolio is also losing. Most capital cannot stomach that profile, so the premium is not fully arbitraged away. The compensation is real, but it is compensation for risk, not free money.

## Null hypothesis

If options were priced exactly fairly (implied volatility = subsequent realized volatility, no variance risk premium), a systematically sold credit spread would have an expected P&L of approximately **zero before costs and negative after costs**. The high win rate would persist — a 0.20-delta spread would still win ~80% of the time — but the occasional max losses would exactly consume the accumulated credits. This is the critical insight: **a high win rate is not evidence of edge.** Under the null, the strategy is a negative-cost lottery-ticket-selling operation with the same expected value as a coin flip levered into a skewed payout. Any realized edge must show up as long-run average P&L per trade exceeding what the delta-implied probabilities predict, after slippage and commissions.

## Bull Put Spread (Bullish)

A bull put spread involves selling a put at a higher strike and buying a put at a lower strike, both with the same expiration.

**Example**: Stock XYZ is at $100. The trader sells a $95 put for $2.50 and buys a $90 put for $1.00.
- **Net credit**: $1.50 ($150 per contract)
- **Max profit**: $1.50 (if XYZ stays above $95 at expiration)
- **Max loss**: ($95 - $90) - $1.50 = $3.50 ($350 per contract, if XYZ falls below $90)
- **Breakeven**: $95 - $1.50 = $93.50

The trader profits if XYZ stays above $93.50. Full profit is achieved if XYZ closes above $95 at expiration. The trade loses money below $93.50 and reaches max loss below $90.

## Bear Call Spread (Bearish)

A bear call spread involves selling a call at a lower strike and buying a call at a higher strike, both with the same expiration.

**Example**: Stock XYZ is at $100. The trader sells a $105 call for $2.00 and buys a $110 call for $0.75.
- **Net credit**: $1.25 ($125 per contract)
- **Max profit**: $1.25 (if XYZ stays below $105 at expiration)
- **Max loss**: ($110 - $105) - $1.25 = $3.75 ($375 per contract, if XYZ rises above $110)
- **Breakeven**: $105 + $1.25 = $106.25

The trader profits if XYZ stays below $106.25 at expiration.

## Probability of Profit

One of the key attractions of credit spreads is the ability to structure trades with a high probability of profit. A credit spread sold far out of the money -- for example, 10-15% away from the current stock price -- might have an 80-90% probability of expiring worthless (full profit). However, this comes with a tradeoff: the risk-to-reward ratio is unfavorable. A spread with a 90% win rate might offer $0.50 of credit against $4.50 of max loss, meaning one loss wipes out nine wins.

The probability of profit (POP) can be approximated using the option's delta. A short option with a delta of 0.20 has approximately an 80% chance of expiring OTM. Traders select their strike placement based on their desired probability:

| Delta of Short Strike | Approximate POP | Credit Size | Risk/Reward |
|----------------------|-----------------|-------------|-------------|
| 0.30 | ~70% | Higher | More balanced |
| 0.20 | ~80% | Moderate | Moderately unfavorable |
| 0.10 | ~90% | Lower | Highly unfavorable |

Many professional credit spread sellers target the 0.15-0.25 delta range as a balance between win rate and risk/reward.

## Payoff and Greeks profile

A credit spread is a short-volatility, positive-theta, negative-gamma structure with a bounded payoff. Understanding the net Greeks is the difference between sizing it deliberately and being surprised by it.

### Payoff at expiration

For a bull put spread (short put at strike `K_s`, long put at strike `K_l`, `K_l < K_s`, net credit `C`):

```
Payoff(S) = C                                    for S >= K_s        (max profit)
          = C - (K_s - S)                        for K_l < S < K_s   (linear decay)
          = C - (K_s - K_l)                      for S <= K_l        (max loss)

Max profit   = C
Max loss     = (K_s - K_l) - C        [width minus credit]
Breakeven    = K_s - C                [bull put]   /   K_s + C [bear call]
```

The payoff is a bounded, kinked line — the long leg is what flattens the loss below `K_l` and converts the position from "naked-short-option" risk into "defined-risk." This is the single most important structural property of the spread.

### Net Greeks (bull put spread, before expiration)

| Greek | Sign | Meaning for the seller | Behaviour over the trade |
|-------|------|------------------------|--------------------------|
| **[[delta]]** | Positive (small) | Mild long-underlying exposure (you want the stock up/stable) | Grows toward +1 spread-equivalent as short strike is tested |
| **[[theta]]** | Positive | Time decay works *for* you; the core profit engine | Accelerates as expiry nears — but so does gamma |
| **[[vega]]** | Negative | A vol spike *increases* the spread's value against you | Largest near the money; shrinks as either leg goes deep ITM/OTM |
| **[[gamma]]** | Negative | Adverse convexity — losses accelerate as the short strike is breached | Spikes sharply inside ~21 DTE → the basis of the 21-DTE rule |

The negative-gamma / positive-theta trade-off is the whole game: you are paid theta every day to bear the risk that gamma turns against you in a fast move. Near expiration the gamma-to-theta ratio collapses (gamma rises faster than the remaining theta you can still collect), which is exactly why the [[#The 21-DTE Rule|21-DTE rule]] exists. A bear call spread has the mirror profile (negative delta, otherwise identical signs on theta/vega/gamma).

### IV and time sensitivity (qualitative)

- **Entering into high IV** (IV rank > ~30-50) maximises the credit collected because the short leg's vega-rich premium is inflated; the subsequent vol mean-reversion (vega working in your favour) plus theta both pay you. This is the intended regime — see [[iv-rank-and-iv-percentile]].
- **Entering into low IV** collects a thin credit against the same defined max loss, so the risk/reward degrades even though POP looks identical. Forcing trades in a low-IV regime is a documented failure mode (see *What kills this strategy*).
- **Holding through an IV spike** marks the spread against you (negative vega) even if the underlying has not moved — a real, often-misunderstood source of mid-trade drawdown.

## Rules

### Entry
1. **Choose direction**: Bullish -> bull put spread. Bearish -> bear call spread.
2. **Prefer elevated IV**: enter when IV rank is above ~30-50; the credit (and the variance risk premium being harvested) is largest when implied volatility is rich relative to its own history.
3. **Select expiration**: 30-45 DTE is common; balances theta decay rate with time for the trade to work.
4. **Select strikes**: Sell the closer-to-the-money strike (typically 0.15-0.25 delta), buy the farther OTM strike. Width of strikes determines max loss (wider = more risk but more credit).
5. **Enter the trade**: Execute as a single spread order (not as separate legs) to ensure the credit is received. Work the mid-price; avoid crossing wide bid-ask spreads.

### Exit / management
- **Take profit**: Many traders close at 50-75% of max profit rather than waiting for expiration to avoid gamma risk
- **Cut losses**: Close if the spread reaches 1.5-2x the credit received, or if the underlying breaches the short strike
- **Time stop**: close or roll at 21 DTE regardless of P&L (see the 21-DTE rule below)
- **Roll**: If the trade is threatened, roll the spread out to a later expiration (and potentially a different strike) for additional credit — see the Adjustments section below
- **At expiration**: If OTM, both options expire worthless and the full credit is kept. If ITM, the spread is at max loss (assuming no earlier management).

### Position sizing
- Risk no more than 1-2% of account equity per spread at max loss; with a $350 max-loss spread, a $35,000 account takes at most 1-2 contracts per position.
- Cap aggregate short-premium exposure: total max loss across all open credit spreads ≤ 20-30% of account equity, because short-volatility positions lose together in a market shock (correlation goes to one in a crash).

## Implementation pseudocode

```python
def credit_spread_engine(account, underlying, config):
    # --- Entry ---
    if not has_open_spread(underlying) and iv_rank(underlying) >= config.min_iv_rank:  # e.g., 30
        bias = directional_bias(underlying)          # trend/levels; trader-defined
        chain = options_chain(underlying, dte_range=(30, 45))
        if bias == "bullish":
            short = select_strike(chain.puts,  delta=-0.20)
            long_ = select_strike(chain.puts,  strike=short.strike - config.width)  # e.g., $5
        elif bias == "bearish":
            short = select_strike(chain.calls, delta=+0.20)
            long_ = select_strike(chain.calls, strike=short.strike + config.width)
        else:
            return
        credit = short.mid - long_.mid
        max_loss = config.width - credit
        contracts = floor(account.equity * 0.01 / (max_loss * 100))   # 1% risk per trade
        if contracts >= 1 and aggregate_short_premium_risk(account) < 0.25 * account.equity:
            sell_spread(short, long_, contracts, limit=credit)        # single spread order

    # --- Management (daily) ---
    for pos in open_spreads(account):
        value = current_spread_value(pos)
        if value <= 0.50 * pos.entry_credit:           # 50% of max profit
            close(pos)
        elif value >= 2.0 * pos.entry_credit:          # loss = 2x credit
            close(pos)                                  # or roll if thesis intact
        elif pos.dte <= 21:
            close_or_roll(pos)                          # gamma-risk time stop
        elif breached(pos.short_strike):
            manage(pos)                                 # roll out/away, or close if thesis broken
```

## Indicators / data used

- **Options chain** with bid/ask, delta, and open interest — strike selection and POP estimation
- **Implied volatility and IV rank/percentile** — entry filter and credit-richness gauge ([[implied-volatility]])
- **Daily OHLCV of the underlying** — directional bias, support/resistance for strike placement
- **DTE / calendar data** — the 30-45 DTE entry window and 21-DTE management rule
- **Earnings and ex-dividend calendar** — avoid holding short calls through ex-dividend (assignment risk) and avoid binary earnings events unless deliberately trading them
- No oscillator-style indicators are required; some traders overlay trend filters (e.g., 50-day moving average) for the directional bias

## Adjustments and Rolling

Credit spreads require active management when the underlying moves toward the short strike. The key adjustment techniques are detailed in [[trade-repair-and-rolling]]; here are the credit-spread-specific applications.

### Rolling Out (Time Extension)

When the underlying approaches the short strike but the directional thesis is intact, roll the entire spread to a later expiration at the same strikes:

1. Buy back the current spread (debit)
2. Sell the same spread at a later expiration (credit)
3. **Goal**: Net credit on the roll, or at worst a small net debit

This buys more time for the underlying to move back in your favor while collecting additional premium that improves the overall breakeven. Only roll if the thesis still holds — rolling "for hope" deepens losses. (Source: [[recovering-losing-options-positions]])

### Rolling Out and Away

The most common defensive roll. Move both the short and long strikes further from the money *and* extend the expiration:

**Example**: Bull put spread $95/$90 is tested (stock at $94). Roll to $90/$85 spread 30 days later for a net credit. This lowers the danger zone by $5 and adds time, at the cost of extending the trade's duration.

### Converting to an Iron Condor

If a bull put spread is tested but the trader expects the stock to stabilize (not keep falling), add a bear call spread above the current price. This converts the position to an [[iron-condor]], collecting additional premium from the call side that partially offsets the put side loss. The risk is that the stock reverses sharply upward and tests the new call side.

### The 21-DTE Rule

Credit spreads carry significant [[gamma-risk]] near expiration. At 21 DTE, gamma on ATM options begins spiking, meaning that small underlying moves cause rapid delta shifts and outsized P&L swings. Many professional credit spread sellers close or roll at 21 DTE to avoid the "gamma trap" — the zone where theta acceleration tempts you to hold but gamma acceleration punishes you for doing so. (Source: [[recovering-losing-options-positions]])

### When NOT to Adjust

- **Thesis is broken**: If the reason you entered the trade is invalidated, close the spread and take the loss. Don't roll a broken thesis.
- **Rolling adds risk**: Never add net debit or uncapped risk to recover a losing spread. The cardinal rule of adjustment is that the recovery trade must stand on its own merits. (Source: [[recovering-losing-options-positions]])
- **Near max loss**: If the spread is deep ITM and close to expiration, the cost of rolling may exceed the potential recovery. Accept the max loss and move on.

## Margin Requirements

The margin requirement for a credit spread is the width of the strikes minus the credit received. For a $5-wide bull put spread receiving $1.50 in credit, the buying power reduction is $3.50 per contract ($350). This is substantially less than the margin required for a naked put, which can be thousands of dollars per contract.

This capital efficiency is a primary reason institutional and retail traders use credit spreads: they can express a view with defined risk and efficient use of buying power.

## Example trade

A trader is moderately bullish on SPY at $500 and wants to generate income. They enter a bull put spread:

- **Sell**: 1 SPY $485 put (30 DTE) for $3.80
- **Buy**: 1 SPY $475 put (30 DTE) for $2.00
- **Net credit**: $1.80 ($180 per contract)
- **Max loss**: ($485 - $475) - $1.80 = $8.20 ($820 per contract)
- **Breakeven**: $485 - $1.80 = $483.20
- **Probability of profit**: approximately 75% (based on the $485 put's delta of ~0.25)

If SPY stays above $485 at expiration, the trader keeps the full $180. If SPY drops to $475 or below, the trader loses $820. The trader sets a management rule: close at $0.90 credit remaining (50% of max profit) or at $3.60 debit (2x the credit received).

## Performance characteristics

- **Benchmark for the premium**: the CBOE S&P 500 PutWrite Index (PUT), which systematically sells ATM index puts, has returned roughly 9-10% annualized since its 1986 backfill start with about two-thirds of the S&P 500's volatility — a long-run Sharpe in the 0.5-0.7 region — and drew down roughly one-third in 2008-09. A defined-risk credit spread program harvests the same premium with the tail capped by the long leg, so expect somewhat lower returns and shallower drawdowns; the frontmatter estimates (Sharpe ~0.6, max drawdown ~25% of allocated capital) assume the position-sizing rules above are followed.
- **Return shape**: strongly negatively skewed — long streaks of small wins (50-80% win rates depending on delta) interrupted by clustered losses in volatility shocks. Monthly P&L is *not* normally distributed; judge the strategy on multi-year samples that include at least one volatility event.
- **Cost overlay (realistic, not naive)**: commissions of ~$0.65 per contract per leg ($2.60 for a spread opened and closed) plus bid-ask slippage of roughly $0.02-0.05 per spread on liquid underlyings (SPY/SPX) — about $5-10 round-trip per spread, i.e. roughly 3-6% of a typical $150-180 credit, or about 1-2 bps of the ~$50,000 underlying notional per SPY contract. The frontmatter's 25 bps breakeven means the edge survives realistic costs by an order of magnitude on liquid index products, but on illiquid single-name chains with $0.20+ spread-wide markets, slippage alone can consume most of the expected edge.
- **Naive-backtest warning**: backtests that fill at mid-price, ignore early assignment, and exclude 2008/2018/2020-style vol events will overstate results dramatically. Cost-corrected, event-inclusive samples are mandatory before sizing up.

### Regime suitability

Credit-spread P&L is highly [[market-regime]]-dependent. The strategy is not a constant edge; it is a regime-conditional one.

| Regime | IV environment | Expected behaviour | Action |
|--------|----------------|--------------------|--------|
| Calm bull / range-bound | Moderate, declining | Best regime — theta + vega mean-reversion both pay | Run at target size |
| High-IV, post-shock | Elevated, falling | Rich credits; vol crush favourable, but realized can stay high | Selective, wider strikes |
| Low-IV grind (e.g. 2017) | Very low | Thin credits vs same max loss; poor risk/reward | Reduce size or stand down |
| Volatility shock / crash | Spiking | Worst regime — negative vega + negative gamma + correlated losses | Defensive; halt new entries |
| Choppy / whipsaw | Mixed | Frequent short-strike tests; roll costs accumulate | Tighten management discipline |

## Capacity limits

- On **index products** (SPX, SPY, NDX), capacity is large: SPY options are among the most liquid instruments in the world, and a program in the low tens of millions of dollars of max-loss exposure can execute at specific 0.15-0.25-delta strikes without materially moving the market. The frontmatter's $25M is a conservative single-program estimate; beyond that, fills degrade at individual strikes and the program must spread across expirations and strikes.
- On **single-stock options**, capacity collapses fast: open interest at OTM strikes is often a few thousand contracts, and a few hundred spreads can become the market at that strike.
- The *premium itself* has macro capacity limits: when too much capital crowds into systematic option selling (as in the 2016-2018 short-vol boom that ended with "Volmageddon" on 5 February 2018, when VIX spiked ~115% in a day and short-vol products like XIV were wiped out), the credit available compresses and the eventual unwind is violent. Crowding risk is rated medium for this reason.

## What kills this strategy

- **Volatility shock / gap risk**: an overnight gap through both strikes produces instant max loss with no chance to manage — the February 2018 Volmageddon, October 2008, and March 2020 are the canonical events. This is failure mode #1 and it is irreducible; the long leg caps it, position sizing makes it survivable.
- **Correlated max losses**: running many spreads across "different" underlyings that are all really the same short-equity-vol bet; in a crash they hit max loss together.
- **Premium compression**: a sustained low-IV regime (e.g., 2017, when VIX averaged ~11) shrinks credits until the risk/reward no longer clears costs; forcing trades in that regime is negative-expectancy.
- **Discipline decay**: a long winning streak (structurally guaranteed by the 70-90% win rate) tempts oversizing right before the loss cluster arrives — the classic short-vol blowup pattern.
- **Early assignment** on the short leg around ex-dividend dates (calls) or deep-ITM puts, creating unintended stock positions and margin calls.
- **Execution erosion**: paying the bid-ask spread on illiquid chains turns a thin edge negative even when the strategy "works."

## Kill criteria

- Program drawdown exceeds **25% of capital allocated** to the strategy → halt new entries, review sizing and underlying selection.
- Rolling 12-month win rate falls below **60%** when strike selection targets ~75-80% POP (0.20-0.25 delta) → the delta-based probability model is mispricing the actual distribution; stop and diagnose.
- **Three consecutive max-loss outcomes** despite following the management rules → regime has changed faster than the rules can adapt; stand down.
- Average collected credit falls below **20% of strike width** at the chosen delta for 3+ months → premium environment too poor to clear costs; pause until IV normalizes.
- Realized round-trip execution cost exceeds **10% of average credit** on the traded underlyings → move to more liquid products or stop.

## Advantages

- **Defined risk**: Maximum loss is known at entry and cannot be exceeded
- **High probability of profit**: Can be structured with 70-90% win rates
- **Capital efficient**: Lower margin requirements than naked options
- **Theta-positive**: Benefits from time decay
- **Flexible**: Can be applied bullish, bearish, or neutral (via iron condor)
- **Scalable**: Easy to adjust size by adding or removing contracts

## Disadvantages

- **Unfavorable risk/reward**: Max loss typically exceeds max profit by 2-5x or more
- **One large loss erases many wins**: The skewed payoff requires disciplined position sizing
- **Early assignment risk**: The short leg can be assigned early, particularly near ex-dividend dates
- **Limited profit potential**: Max profit is capped at the initial credit received
- **Gap risk**: An overnight gap through both strikes can result in immediate max loss with no opportunity to manage

## Sources

- [[recovering-losing-options-positions]] — rolling, adjustment, and 21-DTE management framework cited throughout the Adjustments section
- CBOE S&P 500 PutWrite Index (PUT) methodology and performance history — long-run benchmark for systematic index option premium selling (history backfilled to mid-1986)
- Bakshi, G. & Kapadia, N. (2003), "Delta-Hedged Gains and the Negative Market Volatility Risk Premium," *Review of Financial Studies* — evidence for the variance risk premium harvested by option sellers
- Documented market events referenced: 5 February 2018 "Volmageddon" (VIX +~115% in one session; XIV terminated), October 2008, March 2020 volatility shocks

## Related

- [[options]] — the instruments used
- [[options-pricing]] — understanding how strike selection affects pricing
- [[risk-management]] — position sizing for strategies with skewed payoffs
- [[trade-repair-and-rolling]] — complete rolling and adjustment framework
- [[gamma-risk]] — the risk that drives the 21-DTE rule and adjustment urgency
- [[theta-decay]] — the primary profit driver
- [[implied-volatility]] — affects the credit received
- [[iron-condor]] — combining bull put and bear call spreads
- [[vertical-spread]] — the structural building block of credit spreads
- [[covered-calls]] — an alternative income strategy
- [[edge-taxonomy]] — classification of the edge sources above
