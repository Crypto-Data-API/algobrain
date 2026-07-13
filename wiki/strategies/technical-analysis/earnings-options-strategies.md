---
title: "Earnings Options Strategies"
type: strategy
created: 2026-04-13
updated: 2026-06-20
status: excellent
tags: [options, earnings, volatility, event-driven, technical-analysis]
aliases: ["Earnings Plays", "Earnings Straddle", "Earnings Options", "Event-Driven Options"]
strategy_type: technical
timeframe: swing
markets: [stocks, options]
complexity: intermediate
backtest_status: untested
edge_source: [behavioral, analytical]
edge_mechanism: "IV consistently overestimates earnings moves (sellers profit from variance risk premium), while specific event-driven setups reward informed positioning before catalysts"
data_required: [options-chain, earnings-calendar, implied-volatility]
min_capital_usd: 5000
capacity_usd: 100000000
crowding_risk: medium
expected_sharpe: 0.5
expected_max_drawdown: 0.25
breakeven_cost_bps: 40
related: ["[[earnings-iv-crush]]", "[[earnings-volatility-trading]]", "[[earnings-volatility]]", "[[iv-crush]]", "[[implied-earnings-move]]", "[[implied-volatility]]", "[[straddle-strangle]]", "[[iron-condor]]", "[[calendar-spread]]", "[[volatility-risk-premium]]", "[[variance-risk-premium]]", "[[tastytrade-mechanics]]", "[[volatility-skew]]", "[[earnings]]", "[[earnings-calendar]]", "[[edge-taxonomy]]", "[[failure-modes]]"]
---

Earnings announcements are the single most predictable source of [[implied-volatility]] inflation and subsequent collapse in equity options. The pattern is reliable: IV rises into earnings as uncertainty builds, then crashes immediately after the announcement as the binary event resolves. This "[[iv-crush|IV crush]]" is the core dynamic of earnings options trading — every strategy is either exploiting it, hedging against it, or positioning around it. This page is the **catalog of earnings-options structures** (sell-premium, buy-vol, post-earnings); for the focused, single-structure short-vol trade around the print see [[earnings-iv-crush]], for the broader strategy class see [[earnings-volatility-trading]], and for the underlying cycle see [[earnings-volatility]].

## Edge Source

In the wiki's [[edge-taxonomy]] terms, earnings-options strategies sit on two edge categories, with the dominant one depending on which side of the trade you take:

- **Behavioral** (primary, for sellers): Retail traders consistently overpay for pre-earnings options, treating them as lottery tickets on the binary outcome — a textbook prospect-theory probability distortion (see [[behavioral-finance]]). This creates inflated IV that systematically exceeds realized earnings moves. Academic studies (Goyal & Saretto 2009, among others) document that selling [[straddle-strangle|straddles]] around earnings has historically been profitable across the broad market. This is the earnings-specific expression of the [[variance-risk-premium]].
- **Analytical** (secondary): Traders who accurately model expected earnings moves (using historical move distributions, options-implied moves, and fundamental analysis) can identify specific names where IV overprices or underprices the event. The edge is in the residual — the difference between what the market expects and what is likely.
- **Risk-bearing** (the honest re-framing of "behavioral" for the seller): the premium is also compensation for warehousing un-hedgeable binary gap risk. The seller is paid because the rare large gap (a NFLX-35% print) is genuinely costly. This is *not* a free lunch — see the null hypothesis below.

## Why This Edge Exists

The other side of earnings options trades consists of:
- **Directional speculators** who buy calls or puts expecting a specific post-earnings direction — they pay inflated IV for a coin-flip-like outcome
- **Portfolio hedgers** who buy protective puts before earnings regardless of pricing
- **Volatility buyers** who pay the variance risk premium in exchange for the possibility of an extreme move

The edge for sellers exists because realized earnings moves are typically smaller than what IV implies. This is the earnings-specific manifestation of the broader [[volatility-risk-premium]].

## Null Hypothesis

The IV premium before earnings fairly compensates for the risk of extreme moves (gap risk, tail events). Any apparent profitability from systematic earnings selling is compensation for bearing concentrated tail risk — a few disastrous outcomes (earnings gaps of 20%+) offset the many small wins.

## Key Concepts

### The Implied Earnings Move

The options market prices an expected earnings move into the front-month options. This can be extracted:

```
Implied Move ≈ ATM Straddle Price / Stock Price × 100%
```

More precisely, isolate the "earnings IV" by comparing the front-month (spanning earnings) to the back-month (not spanning earnings):

```
Earnings IV² ≈ Front-Month IV² × T_front - Back-Month IV² × T_back
```

Where T is time to expiration in years. This removes the "background" volatility and isolates the event premium.

### IV Crush Magnitude

Typical IV crush patterns:

| Stock Type | Pre-Earnings IV Rank | Post-Earnings IV Drop | Typical Implied Move |
|------------|---------------------|----------------------|---------------------|
| Mega-cap (AAPL, MSFT) | 60-80 | 30-50% IV decline | 3-5% |
| Large-cap growth (NFLX, TSLA) | 70-90 | 40-60% IV decline | 6-10% |
| Small-cap / biotech | 80-100 | 50-70% IV decline | 8-15% |
| Low-vol utilities | 50-70 | 20-40% IV decline | 2-4% |

### Historical Move vs. Implied Move

Tracking how often a stock's actual earnings move exceeds the implied move:

- **Most stocks**: Actual move < implied move about 70-80% of the time
- **High-vol stocks** (TSLA, NFLX): More frequent exceedances — implied moves are more accurately priced
- **Stable names** (JNJ, PG): Implied moves rarely exceeded — richest IV premium for sellers

### Payoff and Greeks

Every earnings-options structure is, at its core, a **bet on the relationship between vega (IV) and gamma (realized move)** across the print. The seller and buyer take opposite signs of the same two Greeks:

| Greek | Premium seller (short straddle/condor/calendar) | Volatility buyer (long straddle) |
|-------|--------------------------------------------------|----------------------------------|
| Vega | Short — profits from the IV crush | Long — hurt by the IV crush (the buyer's main enemy) |
| Gamma | Short — convex loss on a large gap | Long — convex gain on a large gap |
| Theta | Long — minor over the short hold | Short — bleeds into the event |
| Delta | ~0 at entry, one-sided after the gap | ~0 at entry, one-sided after the gap |

The asymmetry that defines the whole space: **the IV crush is near-deterministic, the realized move is not.** Sellers win the certain vega collapse but risk the uncertain gamma gap; buyers must overcome the certain vega loss before the uncertain gamma gain pays. This is why naked long straddles into earnings are a structurally losing trade for most names (the "reality check" below) and why the [[calendar-spread]] — long back-month vega, short front-month vega — is the most surgical way to isolate the term-structure crush while minimizing gamma exposure.

## Strategies

### Premium Selling (Benefit from IV Crush)

#### Short Straddle / Short Strangle

- **Setup**: Sell ATM [[straddle-strangle|straddle]] (or OTM strangle) in the expiration spanning earnings
- **When**: IV rank > 50 and historical move < implied move for at least 70% of recent quarters
- **Exit**: Close immediately after earnings announcement (do not hold for further decay)
- **Risk**: Unlimited for strangles, very large for straddles. A 20%+ gap destroys many quarters of profit.
- **Sizing**: Conservative — max 1-2% of account at risk

#### Iron Condor / Iron Butterfly

- **Setup**: Sell [[iron-condor]] or [[iron-butterfly]] with short strikes at ±1 standard deviation (approximately the implied move)
- **When**: Same criteria as short straddle, but with defined risk
- **Exit**: Close after earnings. Target 50% of max profit.
- **Risk**: Defined (width of wings minus credit). This is the preferred retail approach because risk is capped.
- **Sizing**: Max loss per trade = 2-3% of account

#### Calendar Spread (Volatility Crush Play)

- **Setup**: Sell the front-month option (spanning earnings) and buy the back-month option (same strike, not spanning earnings)
- **Mechanism**: The front-month option has inflated earnings IV that will crush. The back-month option has normal IV that is relatively stable. When front-month IV crushes, the spread profits.
- **Risk**: If the stock moves significantly, both options lose, but the short front-month (higher gamma) loses more. Calendar spreads have gamma risk around earnings.
- **Best for**: Stocks with consistently overstated implied moves

### Volatility Buying (Expect Larger Move Than Implied)

#### Long Straddle / Long Strangle

- **Setup**: Buy ATM [[straddle-strangle|straddle]] before earnings
- **When**: IV is historically low for this name's pre-earnings cycle (IV rank < 30), or fundamental analysis suggests an unusually high-conviction catalyst
- **The problem**: IV crush almost always erodes part of the position, even if the stock moves in your favor. The stock must move MORE than the implied move for the straddle to profit.
- **Exit**: Close immediately after the move. Every hour of holding post-earnings bleeds theta.
- **Reality check**: Buying pre-earnings straddles is a losing strategy for most names most of the time. The seller's edge is well-documented.

#### Pre-Earnings Run-Up

- **Setup**: Buy OTM calls 1-2 weeks before earnings on stocks with a history of pre-earnings price run-ups
- **Mechanism**: IV increases into earnings lift option prices independent of the stock move. You're buying vol before it peaks.
- **Exit**: Sell the day before or morning of earnings — do NOT hold through the event
- **Edge**: The IV expansion in the days before earnings is predictable and often exceeds the theta cost of holding

### Post-Earnings Strategies

#### Post-Earnings Drift Play

- **Setup**: After earnings, buy options in the direction of the earnings surprise (calls for beats, puts for misses)
- **Mechanism**: Academic research documents post-earnings announcement drift (PEAD) — stocks that beat expectations continue to drift up for 30-60 days, and vice versa
- **When**: Strong earnings surprise (> 10% above/below consensus), high volume confirmation
- **IV advantage**: IV is at its lowest immediately after earnings (IV crush). Options are cheap. This is the rare window where long options have a structural IV advantage.

#### Fade the Overreaction

- **Setup**: Sell options (or take a position) opposing the initial earnings move when it appears excessive
- **When**: Stock gaps far beyond the implied move, opens at extremes of pre-market range, initial move is driven by algorithmic selling/buying rather than fundamental reassessment
- **Risk**: Catching falling knives. The initial move may be the beginning, not the end.

## Implementation Pseudocode

```python
def earnings_iron_condor(stock, chain, account_value):
    # Get earnings date and implied move
    earnings_date = get_next_earnings(stock)
    front_expiry = get_expiry_spanning(earnings_date, chain)
    
    atm_straddle = get_atm_straddle_price(chain, front_expiry)
    implied_move_pct = atm_straddle / stock.price
    
    # Check historical move vs implied
    hist_moves = get_historical_earnings_moves(stock, quarters=12)
    pct_under_implied = sum(1 for m in hist_moves 
                           if abs(m) < implied_move_pct) / len(hist_moves)
    
    if pct_under_implied < 0.65:
        return None  # implied move not rich enough
    
    # Set short strikes at ~1x implied move
    short_call_strike = round_to_strike(stock.price * (1 + implied_move_pct))
    short_put_strike = round_to_strike(stock.price * (1 - implied_move_pct))
    
    # Wings 5-10% beyond short strikes
    wing_width = max(5, round(stock.price * 0.05))
    
    credit = calculate_condor_credit(chain, front_expiry,
                                      short_put_strike, short_put_strike - wing_width,
                                      short_call_strike, short_call_strike + wing_width)
    
    max_loss = wing_width - credit
    max_contracts = int(account_value * 0.025 / (max_loss * 100))
    
    return {
        'contracts': max_contracts,
        'credit': credit,
        'profit_target': credit * 0.50,
        'close_timing': 'immediately after earnings release'
    }
```

## Example Trade

**AAPL Earnings Iron Condor (Q1 2026)**:
- AAPL at $185, earnings after close on Thursday
- Friday expiration straddle at $8.50 → implied move ≈ 4.6%
- Historical: AAPL has moved less than 4.6% on earnings day in 9 of last 12 quarters
- Sell 177/172 put spread for $0.65
- Sell 194/199 call spread for $0.55
- Total credit: $1.20 per contract ($120)
- Max loss: $5.00 - $1.20 = $3.80 ($380)
- AAPL reports, gaps to $189 (+2.2%) — both spreads expire worthless
- Profit: $120 per contract
- IV crushed from 45% to 22% overnight — the IV crush alone would have made the short options profitable even without spread protection

## Performance Characteristics

| Metric | Earnings Selling | Earnings Buying |
|--------|-----------------|----------------|
| Win rate | 65-80% | 20-35% |
| Avg win/loss ratio | 0.3-0.5x | 2-4x |
| Key risk | Single massive gap (think NFLX -35%) | Chronic IV crush erosion |
| Best environment | Predictable, low-surprise names | High-conviction catalysts, cheap IV |
| Sharpe (realistic) | 0.3-0.7 (strategy-dependent) | -0.2 to 0.3 (highly variable) |

## Capacity Limits

Capacity is **low to moderate** and bound entirely by single-name front-cycle option liquidity:

- On the most liquid names (AAPL, MSFT, NVDA, TSLA), positions of a few hundred contracts per leg can be worked without moving the [[bid-ask-spread]]; beyond that, market makers see and skew against the flow.
- A diversified earnings-selling sleeve trading 20–40 names per quarter scales to roughly the low tens of millions of risk capital before adverse selection and impact materially degrade the edge (consistent with the `capacity_usd: 100000000` upper bound in the frontmatter, which assumes the most liquid mega-cap universe).
- The binding cost is not commission but the four-to-eight times the [[bid-ask-spread]] is crossed on a multi-leg structure per round trip; on small credits this can be the difference between a viable and a non-viable trade (`breakeven_cost_bps: 40`).
- Index-level vol selling (SPX/RUT) scales far further but is a different, non-event strategy — see [[tastytrade-mechanics]] and [[variance-risk-premium]].

## What Kills This Strategy

- **Regime shift**: In periods of genuine fundamental uncertainty (2008, 2020), earnings surprises become larger and more frequent, making implied moves more accurate or too low
- **Black swan earnings**: A single -30% gap on a company that "never moves" (GE 2017, META 2022) can destroy a year of premium collection
- **Correlation of earnings**: When multiple portfolio names report in the same week, a sector-wide surprise creates correlated losses
- **IV term structure shifts**: If back-month IV also crushes (sympathy moves), calendar spreads fail
- **Crowding**: As more retail traders sell earnings premium (popularized by tastytrade), credits compress

## Kill Criteria

- Rolling 4-quarter P&L negative after costs
- Two max-loss events in a single earnings season
- Average realized move / implied move ratio exceeding 1.0 across the portfolio (edge has disappeared)

## Advantages

- Predictable calendar — you know exactly when the event occurs
- IV crush is the most reliable volatility pattern in equity options
- Defined-risk structures cap losses
- High win rate provides psychological comfort
- Can be systematized and backtested against historical earnings data

## Disadvantages

- Gap risk — stocks open at the post-earnings price with no opportunity to manage during the move
- Earnings are binary — no opportunity for gradual stop-loss management
- Concentrated calendar risk — many earnings cluster in 4-week windows each quarter
- Requires accurate assessment of whether implied move is rich or cheap
- Transaction costs consume a meaningful portion of small credits

## Sources

- [[book-option-volatility-and-pricing]] — Natenberg on event-driven IV dynamics and pre/post-event volatility behavior
- [[volatility-risk-premium]] — the academic foundation for why selling earnings premium has positive expected value
- Goyal, A. & Saretto, A. (2009) — "Cross-section of option returns and volatility," *Journal of Financial Economics* — documents that selling straddles where implied exceeds historical vol is profitable across the cross-section
- Bernard, V. & Thomas, J. (1989) — the canonical post-earnings-announcement drift (PEAD) studies underpinning the post-earnings-drift play
- [[tastytrade]] — multi-year published research on earnings short-premium expected value and win rate
- General market knowledge; specific figures above are illustrative and cost-aware, not backtested by this wiki.

## Related

- [[earnings-iv-crush]] — the focused single-structure short-vol trade around the print
- [[earnings-volatility-trading]] — the broader strategy class (long-vol and short-vol)
- [[earnings-volatility]] — the conceptual earnings cycle these strategies harvest
- [[iv-crush]] — the post-event IV collapse phenomenon in isolation
- [[implied-earnings-move]] — extracting the market's expected move for strike placement
- [[implied-volatility]] — IV crush is the central mechanism
- [[straddle-strangle]] — the building block of earnings vol trades
- [[iron-condor]] — defined-risk earnings premium selling
- [[calendar-spread]] — exploiting term structure around earnings
- [[volatility-risk-premium]] — the structural reason sellers profit
- [[variance-risk-premium]] — the broader premium of which earnings premium is one slice
- [[tastytrade-mechanics]] — the systematic premium-selling playbook adjacent to event selling
- [[volatility-skew]] — asymmetric pricing of left-tail earnings risk
- [[earnings]] — earnings as a fundamental catalyst
- [[earnings-calendar]] — timing earnings trades
- [[edge-taxonomy]] — behavioral/analytical/risk-bearing edge classification
- [[behavioral-finance]] — why retail overpays for binary-event optionality
- [[failure-modes]] — historical blow-ups of premium-selling books
