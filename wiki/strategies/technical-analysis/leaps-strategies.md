---
title: "LEAPS Strategies"
type: strategy
created: 2026-04-06
updated: 2026-06-20
status: excellent
tags: [options, LEAPS, long-term, stock-replacement, poor-mans-covered-call, equity-options, capital-efficient, diagonal-spread]
aliases: ["Poor Man's Covered Call", "PMCC", "LEAPS Strategy", "leaps-strategy"]
strategy_type: quantitative
timeframe: position
markets: [stocks]
complexity: intermediate
backtest_status: untested
edge_source: [structural, analytical]
edge_mechanism: "Deep ITM LEAPS replicate stock exposure at 15-25% of capital cost, freeing capital for additional deployment or income generation; the counterparty is the options market maker providing leverage at a known cost (extrinsic value)"
expected_sharpe: 0.6
expected_max_drawdown: 0.30
breakeven_cost_bps: 50
crowding_risk: medium
min_capital_usd: 5000
capacity_usd: 10000000
related: ["[[covered-call]]", "[[synthetic-long-stock]]", "[[synthetic-long]]", "[[diagonal-spread]]", "[[collar]]", "[[delta]]", "[[theta]]", "[[vega]]", "[[gamma]]", "[[vertical-spreads]]", "[[implied-volatility]]", "[[long-call]]", "[[leaps]]", "[[managing-winners]]", "[[market-regime]]"]
---

# LEAPS Strategies

LEAPS (Long-Term Equity Anticipation Securities) are options with expirations ranging from **1 to 2+ years**. Their extended duration makes them effective tools for stock replacement and capital-efficient income generation. The two primary LEAPS strategies are **stock replacement** (buying deep ITM LEAPS calls to simulate long exposure) and the **Poor Man's Covered Call** (PMCC), which layers short-term call selling on top of the LEAPS position to generate recurring income — replicating a [[covered-call]] at a fraction of the capital.

## Edge Source

**Structural + Analytical.** The structural edge is capital efficiency: a deep ITM LEAPS call costing $15-25 per share provides nearly identical delta exposure to owning $100+ shares. The freed capital can earn risk-free returns or fund additional positions, improving portfolio-level returns on equity. The analytical edge in the PMCC variant comes from systematically selling [[theta]] to short-term options buyers — capturing the well-documented time-decay premium that accelerates as options approach expiration. The counterparty on the short calls is typically retail traders buying short-dated directional bets, who overpay for gamma.

## Why This Edge Exists

Options market makers are willing to sell you a deep ITM LEAPS call at intrinsic value plus a modest extrinsic premium because they can delta-hedge it. You are paying for leverage at a transparent cost (the extrinsic value). Meanwhile, short-dated OTM call buyers systematically overpay for lottery-ticket upside. By selling to them monthly, you harvest the theta premium that academic literature has documented as one of the most persistent risk premia in equity markets.

## Null Hypothesis

Under the null, the cost of extrinsic value paid on the LEAPS call would exactly offset the theta income collected from short calls, producing returns identical to simply buying and holding the stock (minus transaction costs). If the PMCC consistently produces higher risk-adjusted returns than stock ownership over multiple roll cycles, the null is rejected. Empirically, deep ITM LEAPS with low extrinsic value (~2-5% of stock price) paired with 30-45 DTE short calls at delta 0.20-0.30 have shown positive theta capture after LEAPS decay costs, especially in moderate-IV environments.

## Rules

### Poor Man's Covered Call (PMCC)

**Entry:**
1. **Buy 1 deep ITM LEAPS call** — [[delta]] of 0.75-0.85, 12-18 months to expiration. Choose the strike deep enough to minimize extrinsic value (typically 15-25% below current stock price)
2. **Sell 1 short-term OTM call** — 30-45 DTE, delta 0.20-0.30. This creates a [[diagonal-spread]]
3. Ensure the short call's strike is **above** the LEAPS cost basis (LEAPS strike + premium paid) to avoid a guaranteed loss if assigned

**Roll cycle:**
4. When the short call reaches 50-75% of max profit, or 14 DTE, buy it back and sell a new 30-45 DTE call
5. If the stock rallies through the short strike, roll up and out — move to a higher strike and later expiration for a credit or small debit

**LEAPS management:**
6. When the LEAPS reaches 6 months to expiration, roll to a new 12-18 month LEAPS to avoid accelerating [[theta]] decay
7. If the stock drops >20% from entry, evaluate whether the thesis still holds before rolling

### LEAPS as Stock Replacement

1. **Buy 1 deep ITM LEAPS call** (delta 0.80+) to simulate long stock exposure at 15-25% of the share price
2. Accept that extrinsic value paid will erode over the life of the option — this is the cost of leverage
3. Roll to a new LEAPS when the current one reaches 6 months to expiry

### Position Sizing

- Size the LEAPS position so that the total debit (worst-case loss) is the amount you would be comfortable losing on a stock position
- Do not lever up — the capital savings should improve diversification, not increase concentration
- Maximum 5-8% of portfolio in any single PMCC position

## Implementation Pseudocode

```python
def setup_pmcc(stock, portfolio):
    price = get_price(stock)
    
    # Select LEAPS: 12-18 months out, delta 0.75-0.85
    leaps = select_option(
        stock, type='call',
        min_dte=365, max_dte=540,
        min_delta=0.75, max_delta=0.85,
        sort_by='lowest_extrinsic'
    )
    
    # Ensure position size is within limits
    max_debit = portfolio.value * 0.05  # 5% max per position
    if leaps.ask > max_debit:
        return None  # stock too expensive for this account
    
    buy(leaps)
    cost_basis = leaps.strike + leaps.ask  # breakeven stock price
    
    # Sell short call: 30-45 DTE, delta 0.20-0.30, above cost basis
    short_call = select_option(
        stock, type='call',
        min_dte=30, max_dte=45,
        min_delta=0.20, max_delta=0.30,
        min_strike=cost_basis  # must be above breakeven
    )
    sell(short_call)
    
    return Position(leaps, short_call, cost_basis)

def manage_pmcc(position):
    # Roll short call at 50% profit or 14 DTE
    if (position.short_call.pnl_pct > 0.50 or
        position.short_call.dte < 14):
        close(position.short_call)
        position.short_call = sell_new_short_call(position)
    
    # Roll LEAPS at 6 months remaining
    if position.leaps.dte < 180:
        close(position.leaps)
        position.leaps = buy_new_leaps(position.stock)
    
    # Stop loss: thesis invalidation
    if position.stock.price < position.leaps.strike * 0.80:
        close_all(position)  # stock down 20%+ from LEAPS strike
```

## Indicators / Data Used

- [[delta]] — Primary selection criterion for both LEAPS and short calls
- [[theta]] — Decay rate; minimize on the long leg, maximize on the short leg
- [[implied-volatility]] — Prefer entering PMCC when IV is moderate (30-50th percentile); avoid buying LEAPS at extreme high IV
- [[vega]] — LEAPS are long vega; a volatility crush after entry hurts the position
- Bid-ask spread width — Critical for long-dated options; avoid LEAPS with spreads > 3% of option price

## Payoff & Greeks

### Payoff sketch (PMCC / diagonal at the short-call expiry)

The PMCC is a [[diagonal-spread]]: a deep-ITM long LEAPS call (≈ stock-like upside) with a near-dated short OTM call sold against it. The payoff resembles a [[covered-call]] — upside is capped near the short strike, downside is bounded at the net debit minus collected premiums (far better than owning the LEAPS naked).

```
 P/L
  │                  ┌───────────────────  ← gains capped near short-call strike
  │                 /                        (roll up/out to lift the cap)
  │                /
 0│──────────────/──────────────────────── spot →
  │             /
  │ ___________/                            ← max loss ≈ net debit − premiums collected
  │          BE  Kshort
  │          ↑   ↑
  │      breakeven  short call strike
  │   (≈ LEAPS strike + net debit)
   Pure stock-replacement (no short call) = the same long-LEAPS line
   WITHOUT the cap: uncapped upside, downside bounded at premium paid.
```

### Net-Greeks table (PMCC, at/near entry)

| Greek | LEAPS leg (long) | Short call leg | Net position | Implication |
|-------|------------------|----------------|--------------|-------------|
| [[delta]] | +0.75 to +0.85 | −0.20 to −0.30 | ≈ +0.45 to +0.65 | Net long, stock-like but de-levered by the short call |
| [[theta]] | Slightly negative (slow LEAPS decay) | Positive (fast near-dated decay) | **Net positive** in moderate IV | The income engine — short-call theta outpaces LEAPS theta |
| [[vega]] | Strongly positive (long-dated) | Slightly negative | **Net positive** | An IV crush after entry hurts; prefer entering at moderate IV |
| [[gamma]] | Small positive | Small negative (rises near short expiry) | ≈ near zero, tilts negative as short call nears expiry | Manage the short call before its gamma steepens |

The PMCC is **net long delta, net long vega, and net positive theta** — it behaves like a de-levered, income-generating long-stock proxy. Its key vulnerability versus owning stock is the **long-vega** exposure: buying the LEAPS at high [[implied-volatility]] and watching IV normalise erodes the position even if the underlying is flat. The pure **stock-replacement** variant (no short call) is simply a high-delta [[long-call]] — net long delta, long gamma, long vega, modest negative theta — used as a leveraged stock substitute. See [[managing-winners]] for the short-call roll discipline.

### Scenario payoff matrix

| Scenario | PMCC Outcome | Stock Replacement Outcome |
|---|---|---|
| Stock rises moderately | Short call decays; LEAPS appreciates; ideal outcome | LEAPS appreciates dollar-for-dollar (delta ~0.80) |
| Stock rises sharply | Short call goes ITM; roll up/out or accept capped gain | Full participation minus extrinsic value cost |
| Stock flat | Short call decays (profit); LEAPS loses small theta | LEAPS loses extrinsic value slowly |
| Stock drops moderately | LEAPS loses value; short call premium partially offsets | LEAPS loses value; loss capped at premium paid |
| Stock drops significantly | LEAPS can lose 50-80% of value; short premiums soften the blow | LEAPS can lose most of its value |

**Max profit (PMCC)** = short call strike - LEAPS strike - net debit + cumulative short call premiums collected.

**Max loss** = net debit paid for the LEAPS minus total short call premiums collected.

## Example Trade

**AAPL PMCC — January 2025 setup:**

| Component | Detail |
|---|---|
| AAPL stock price | $195 |
| **Long leg** | Buy Jan 2026 $160 call @ $42.00 (delta 0.82, 390 DTE) |
| **Short leg** | Sell Feb 2025 $205 call @ $3.50 (delta 0.25, 35 DTE) |
| **Net debit** | $42.00 - $3.50 = $38.50 per share ($3,850 per contract) |
| **Cost basis** | $160 + $38.50 = $198.50 (breakeven stock price) |
| **Capital vs shares** | $3,850 vs $19,500 (80% capital savings) |
| **Max profit (this cycle)** | ($205 - $160 - $38.50) + $3.50 = $10.00/share ($1,000) |

**Month 1 outcome:** AAPL rises to $200. Short call decays to $1.20, bought back for 66% profit ($2.30 collected). Sell new Mar $210 call for $3.20. Rolling income continues.

**After 6 months:** Collected ~$15 in short call premiums across 5 rolls. LEAPS appreciated from $42 to $50 (AAPL at $210). Net position P&L: +$23/share on $38.50 invested = 60% return. Equivalent stock return: ($210-$195)/$195 = 7.7%.

## Performance Characteristics

| Metric | PMCC | Stock Replacement |
|---|---|---|
| **Capital efficiency** | 15-25% of stock cost | 15-25% of stock cost |
| **Expected annual return on capital** | 15-30% (in moderate uptrend) | Mirrors stock return, amplified by leverage |
| **Max drawdown** | 30-50% of debit in a stock crash | Up to 100% of premium paid |
| **Win rate (monthly rolls)** | ~70-75% of short calls expire profitable | N/A |
| **Sharpe ratio** | ~0.6 | Similar to underlying stock |
| **Ideal environment** | Slowly rising, moderate IV | Any bullish thesis |

## Capacity Limits

Limited by options liquidity on the underlying. LEAPS on mega-cap stocks (AAPL, MSFT, AMZN, SPY) have excellent liquidity with tight spreads. Mid-caps and small-caps often have wide LEAPS spreads (5-10% of option price), making the strategy uneconomical. Estimated capacity per name: $5-10M in mega-caps, $1-2M in liquid large-caps, impractical below $500M market cap. Total portfolio capacity across multiple names: $10M+ is feasible.

## What Kills This Strategy

- **Sharp, sustained stock decline** — A 30%+ drop wipes out most of the LEAPS value. Short call income is a thin buffer. Unlike stock ownership, the LEAPS expires — you cannot simply hold through a multi-year recovery without rolling (at additional cost)
- **IV crush after entry** — Buying LEAPS at elevated IV means overpaying for extrinsic value. If IV normalizes, the LEAPS loses vega value even if the stock is flat
- **Early assignment on short call** — If the short call goes deep ITM near [[dividend|ex-dividend date]], the holder may exercise early. This forces an unplanned close of the diagonal
- **LEAPS expiration neglect** — Failing to roll the LEAPS before the final 3-4 months means accelerating theta decay eats into the position. The roll itself costs money (new extrinsic)
- **Overconcentration** — The capital savings tempt traders to run 10-20 PMCC positions simultaneously. In a broad market selloff, all positions lose together

## Kill Criteria

- Underlying stock drops >25% from LEAPS entry and fundamental thesis is broken → close the entire position
- Cumulative short call income fails to exceed LEAPS theta decay over 6 months → the IV environment is wrong for PMCC, switch to stock replacement or exit
- LEAPS bid-ask spread widens to >5% → liquidity has deteriorated, roll to a more liquid expiration or exit
- Rolling the LEAPS costs >8% of the new LEAPS price → extrinsic is too expensive, the strategy is not working on this name

## Advantages

- Dramatically lower capital requirement — often 15-25% of buying 100 shares
- PMCC generates recurring income similar to a traditional [[covered-call]]
- Long time horizon reduces the impact of short-term [[volatility]] and [[theta]] decay
- [[delta]] exposure is nearly identical to stock ownership with deep ITM LEAPS
- Defined risk — maximum loss is known at entry (LEAPS premium minus income)
- Freed capital improves portfolio diversification or earns risk-free returns

## Disadvantages

- The LEAPS call carries extrinsic value that will decay, especially in the final 6 months
- No [[dividend]] income — a meaningful gap for high-yield stocks (LEAPS holders do not receive dividends)
- Wide bid-ask spreads on long-dated options can increase entry/exit costs significantly
- If the stock drops sharply, the LEAPS can lose substantial value despite its long duration
- Assignment risk on the short call can force early closure of the diagonal spread
- Requires active management — monthly rolling is not set-and-forget
- [[vega]] risk: buying LEAPS at high IV means overpaying if volatility normalizes

## Sources

- CBOE educational materials on LEAPS and diagonal spreads
- Options mechanics from [[option-volatility-and-pricing|Option Volatility and Pricing]] (Natenberg)

## Related

- [[covered-call]] — the traditional version requiring full stock ownership
- [[diagonal-spread]] — the broader category that includes the PMCC structure
- [[synthetic-long-stock]] — another capital-efficient stock replication method
- [[synthetic-long]] — call + put combination replicating stock
- [[collar]] — hedging a LEAPS or stock position with a protective put
- [[vertical-spreads]] — simpler directional options structures
- [[long-call]] — the stock-replacement variant is a deep-ITM long call; LEAPS are its long-dated form
- [[managing-winners]] — the roll discipline for the short-call leg of the PMCC
- [[implied-volatility]] / [[vega]] — the volatility input and the LEAPS leg's primary risk
- [[delta]] / [[theta]] / [[gamma]] — the position's Greek profile across the diagonal
- [[market-regime]] — PMCC thrives in slowly-rising, moderate-IV regimes; suffers in sharp selloffs
