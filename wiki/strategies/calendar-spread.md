---
title: "Calendar Spread"
type: strategy
created: 2026-04-15
updated: 2026-06-21
status: excellent
tags: [options, derivatives, volatility, swing-trading]
aliases: ["Calendar Spread", "Time Spread", "Horizontal Spread"]
related: ["[[theta-decay]]", "[[options]]", "[[implied-volatility]]", "[[options-pricing]]", "[[covered-calls]]", "[[credit-spread]]", "[[cash-secured-puts]]", "[[edge-taxonomy]]", "[[options-premium-selling]]", "[[short-put-spread]]", "[[iron-fly]]", "[[iv-crush]]", "[[vega]]", "[[theta]]", "[[market-regime]]", "[[variance-risk-premium]]"]
strategy_type: technical
timeframe: swing
markets: [stocks, options]
complexity: intermediate
backtest_status: untested
edge_source: [risk-bearing, structural]
edge_mechanism: "Short-dated option buyers (hedgers and lottery-ticket speculators) overpay for near-term time value, letting the calendar seller harvest the steepest part of the theta curve while owning slower-decaying back-month vega."
data_required: [options-chain, iv-term-structure, ohlcv-daily]
min_capital_usd: 2000
capacity_usd: 5000000
crowding_risk: low
expected_sharpe: 0.5
expected_max_drawdown: 0.20
breakeven_cost_bps: 50
---

# Calendar Spread

A calendar spread (also called a time spread or horizontal spread) is an [[options]] strategy in which a trader sells a near-term option and simultaneously buys a longer-term option at the same strike price. The strategy profits primarily from the differential rate of [[theta-decay]] between the two expirations -- the short-dated option loses time value faster than the long-dated option, creating a net credit as time passes. Risk is defined: the maximum loss is the net debit paid to enter the spread.

## Edge source

Per the [[edge-taxonomy]], the calendar spread draws on two of the five edge categories:

- **Risk-bearing**: the seller of the front-month option is paid a volatility risk premium for bearing short-term gamma risk. Implied volatility on short-dated options persistently exceeds subsequently realized volatility on average, so systematically selling near-term time value collects that premium.
- **Structural**: time decay is non-linear. Theta accelerates as expiration approaches (roughly proportional to 1/√T for at-the-money options), so an option with 7 days to expiration decays much faster per day than one with 60 days. The calendar is a structural harvest of this curvature -- short the fast-decaying leg, long the slow-decaying leg.

## Why this edge exists

The counterparties buying short-dated options fall into two main groups, and both have non-profit motives for transacting:

1. **Hedgers** buying near-term protection (e.g., ahead of earnings, FOMC, or CPI prints) pay up for insurance and accept negative expected value, exactly as home insurance buyers do. They keep "losing" because they are buying certainty, not expectancy.
2. **Retail speculators** buying short-dated, cheap-in-dollar-terms options for leveraged directional bets. The growth of 0DTE and weekly options since 2022 has institutionalized this lottery-ticket demand, which inflates front-of-curve implied volatility relative to realized.

The calendar seller is on the other side of that flow. The edge is modest and persistent rather than large and episodic; it is compensation for bearing pin/assignment risk and short-gamma exposure on the front leg.

## Null hypothesis

If options were fairly priced across the term structure (no volatility risk premium, no term-structure mispricing), the expected value of a calendar spread at front-month expiry would equal the debit paid, and the strategy's P&L would be zero in expectation **before** costs and negative after the four commissions and two bid-ask spread crossings required per round trip. Under the null, a long history of calendar trades should show win rate consistent with the breakeven zone width (typically 50-65% of trades profitable on ATM calendars) but mean P&L per trade ≈ -costs. Any backtest of the strategy must beat this cost-drag baseline, not zero.

## Rules

### Entry
1. Select a strike near the current underlying price (at-the-money). Sell the front-month option and buy the back-month option at the same strike; pay the net debit.
2. **Ideal conditions**: low-to-moderate [[implied-volatility]] (e.g., IV rank < 40), expectation of range-bound behavior for the front-month duration, and no major catalysts between entry and front-month expiry -- unless deliberately placing the spread so a known catalyst falls *between* the two expirations to exploit relative IV.
3. Prefer term structures in contango (front-month IV at or below back-month IV). Avoid entering when the front month trades at a large IV premium to the back month (backwardation), which compresses profit potential.

### Exit
4. **Profit-taking**: close at roughly 25-50% of the maximum theoretical profit, or at front-month expiry if the underlying is near the strike (sell the back-month option, let the front month expire or buy it back for pennies).
5. **Stop**: close the spread if its value falls to roughly 50% of the debit paid, or if the underlying moves far enough from the strike that both legs trade near intrinsic/parity.
6. Never hold the short leg through expiration while it is near-the-money -- close or roll to avoid pin risk and assignment.

### Position sizing
7. Risk no more than 1-2% of account equity per spread (the debit is the max loss). Diversify across underlyings and entry dates rather than concentrating in one expiry cycle.

### Management
8. Monitor the underlying's proximity to the strike. If the stock drifts, consider rolling the short leg to the next weekly cycle, or converting to a diagonal by re-striking the new short leg toward the current price.

## Implementation pseudocode

```python
# ATM calendar spread, daily scan
for symbol in universe:
    chain = get_option_chain(symbol)
    iv_rank = iv_rank(symbol, lookback_days=252)
    front = chain.expiry(closest_to_dte=14)
    back  = chain.expiry(closest_to_dte=45)

    # entry filters
    if iv_rank > 40:                       continue  # too rich, vega-crush risk
    if front.atm_iv > back.atm_iv * 1.05:  continue  # backwardation, skip
    if has_event_before(symbol, front.expiry):  continue  # earnings/FOMC in front cycle

    K = nearest_strike(chain, spot(symbol))
    debit = back.call(K).mid - front.call(K).mid
    if debit > 0.02 * account_equity:      continue  # size limit (1-2% risk)

    sell(front.call(K)); buy(back.call(K))           # open calendar

# daily management
for pos in open_calendars:
    pnl_frac = (pos.value - pos.debit) / pos.max_theoretical_profit
    if pnl_frac >= 0.40:                   close(pos)        # take profit
    if pos.value <= 0.50 * pos.debit:      close(pos)        # stop loss
    if dte(pos.front) <= 1 and is_near_money(pos.front):
        close_or_roll_short_leg(pos)                          # avoid pin/assignment
```

## Indicators / data used

- Full **options chain** with bid/ask for at least two expiration cycles
- **IV term structure** (front-month vs back-month ATM IV) -- the key entry filter
- **IV rank / IV percentile** over a 252-day lookback
- **Earnings and macro event calendar** (to place or avoid catalysts deliberately)
- Daily OHLCV of the underlying for range-bound/trend assessment
- Greeks: theta, vega, and net delta of the combined position

## Payoff & Greeks

The calendar's payoff (evaluated **at front-month expiration**) is a smooth, rounded tent peaking at the strike — the mirror image in profit-zone shape of a [[short-strangle]] but built from a net debit. Maximum profit is realised when the underlying sits exactly at the strike at front-month expiry (the short leg expires worthless while the long back-month leg retains its full time value). Loss is capped at the net debit on a large move in either direction.

```
Calendar spread P&L at FRONT-month expiration

  +max  ┤            ╱▔▔╲              ← peak at strike K
        │          ╱      ╲
    0 ──┼────────╱──────────╲────────────
        │       ╱            ╲
 −debit ┤━━━━━━╱              ╲━━━━━━━━━━  ← capped loss = net debit (large move either way)
        └──────────────────────────────────
              BE_lo      K     BE_hi
        max_loss = net debit paid
        profit zone is widest at K; both breakevens move with IV
```

Unlike the short-vol credit structures in [[options-premium-selling]], the calendar is **net long vega** — the back-month long leg has more vega than the front-month short leg, so the position *gains* when [[implied-volatility]] rises. This is the single most important distinction in the options-premium family: the calendar is the structure you reach for when [[ivr|IV Rank]] is *low* and you expect IV to rise, exactly the regime in which you would NOT sell a strangle or [[iron-fly]].

Net Greeks (a long-vega, positive-theta, defined-risk structure):

| Greek | Sign | Comment |
|---|---|---|
| [[theta]] | **positive** | the front short leg decays faster than the back long leg — the core profit driver while price stays near K |
| [[vega]] | **positive** | the defining sign; the back-month leg dominates. A rise in [[implied-volatility]] widens the spread; an [[iv-crush]] in the back month is a primary loss mode |
| [[delta]] | ~0 near K | small near the strike; grows directional as price drifts away (long-ish above K for a call calendar, short-ish below) |
| [[gamma]] | **negative** | the front short leg's gamma dominates near expiry, which is why the short leg must be closed/rolled before front-month expiry to avoid pin risk |

The positive-theta / **positive-vega** combination is rare and valuable: it is one of the few defined-risk ways to be long volatility and still collect time decay. The cost is a narrow profit zone — the trade needs the underlying to stay near K. See implied-earnings-move for the event-timed variant (placing the calendar so an earnings catalyst falls *between* the two expirations to capture the front-vs-back IV differential).

## Types of Calendar Spreads

### Call Calendar Spread
Sell a near-term call and buy a longer-term call at the same strike. Slightly bullish to neutral bias, as the position benefits from the stock staying near or slightly above the strike.

### Put Calendar Spread
Sell a near-term put and buy a longer-term put at the same strike. Slightly bearish to neutral bias, as the position benefits from the stock staying near or slightly below the strike.

### Diagonal Spread
A variation where the two options have different strike prices in addition to different expirations. For example, sell a near-term $105 call and buy a longer-term $110 call. Diagonals combine calendar spread mechanics with directional positioning and can be tailored to a specific price forecast.

### Double Calendar Spread
Involves placing two calendar spreads at different strikes -- typically one put calendar below the current price and one call calendar above it. This widens the profit zone significantly but increases the net debit and requires even tighter management.

## Volatility exposure

Calendar spreads have positive vega exposure overall, meaning they benefit when [[implied-volatility]] rises. This occurs because the long-dated option has higher vega than the short-dated option. An increase in IV inflates the value of the long option more than the short option, widening the spread.

This makes calendars attractive when IV is relatively low and expected to rise -- for instance, when placing a calendar ahead of an earnings announcement or economic report that falls between the two expirations. Conversely, a sharp drop in IV can damage the position even if the underlying price cooperates.

A critical nuance: the two expirations may have different implied volatilities (term structure). If the near-term IV is elevated relative to the far-term IV (backwardation), the calendar costs more to enter and has a compressed profit potential. If the near-term IV is lower than the far-term IV (contango), the spread is cheaper and has higher profit potential.

## Example trade

A trader believes AAPL ($185) will stay range-bound for the next two weeks but expects volatility to pick up over the following month. They enter a call calendar spread:

- **Sell**: 1 AAPL May 2 $185 Call (14 DTE) for $3.20
- **Buy**: 1 AAPL May 30 $185 Call (42 DTE) for $5.80
- **Net debit**: $2.60 ($260 per contract)

If AAPL closes at $185 at the May 2 expiration, the short call expires worthless, and the long call (now with 28 DTE) might be worth $4.50. The trader sells it for $4.50, realizing a profit of $4.50 - $2.60 = $1.90 ($190 per contract), a 73% return on risk.

If AAPL rallies to $200 or drops to $170, both options converge toward intrinsic value, the time-value spread collapses, and the trader likely loses most of the $2.60 debit.

## Performance characteristics

Realistic expectations, net of costs:

- **Win rate**: roughly 50-65% on ATM calendars managed at partial profit targets; the payoff is asymmetric (winners around +25-50% of debit when managed early, full-debit losses on large moves if unmanaged).
- **Per-trade economics**: a $2.60 debit spread crosses four bid-ask spreads per round trip. On a liquid name with $0.03-0.05 option spreads plus ~$0.65/contract commissions, total friction is roughly $0.15-0.25 per spread -- about 6-10% of the debit. On illiquid chains with $0.20+ spreads, costs alone can consume the expected edge; this is why the frontmatter breakeven is set near 50 bps of notional round-trip.
- **Expected portfolio Sharpe**: ~0.4-0.6 for a diversified, systematically managed calendar program -- the theta/vega premium is real but small, and occasional gap moves and IV crushes produce clustered losses.
- **Drawdown profile**: worst stretches come in fast trending or vol-crush regimes (e.g., a market that grinds 10% higher in a month while IV falls); a 15-20% peak-to-trough drawdown on allocated capital is a reasonable planning assumption, matching the frontmatter estimate of 0.20.
- Returns are lumpy and regime-dependent: calendars do best in quiet, range-bound tape with stable-to-rising back-month IV.

### Regime conditioning

Because the calendar is **long vega** it is the regime-opposite of the short-vol structures in [[options-premium-selling]]:

| [[market-regime\|Regime]] | IV / term structure | Calendar outcome | Action |
|---|---|---|---|
| Low-IVR, quiet, IV bottoming | contango, low IV | the ideal: cheap entry, IV upside, range-bound price | best entries |
| Rising IV, range-bound | IV expanding, price stable near K | both theta and vega work in your favour | hold/add |
| Trending / large move | price gaps away from K | both legs converge to parity; lose most of debit | the dominant loss path |
| Backwardation / event spike | front IV rich to back | calendars expensive to enter, existing ones underwater | no new entries (see kill criteria) |
| Post-event IV crush | back-month vega deflates | loss even if price cooperates | avoid holding a calendar *through* an unfavourable crush |

The contrast with [[short-put-spread]] and [[iron-fly]] is the key portfolio insight: those want **high** IVR to sell; the calendar wants **low** IVR to buy. A balanced options book can pair them so that the long-vega calendar partially offsets the short-vega credit structures across the [[market-regime|regime]] cycle.

## Capacity limits

Capacity is bounded by options market depth at a single strike in two expiries:

- **Single-name equity calendars**: ATM open interest in non-index names is often only a few thousand contracts per strike/expiry; executing more than 50-200 spreads without moving the market is difficult. A program spread across ~20 liquid names supports roughly **$1-5M** of debit-at-risk before slippage dominates -- hence the conservative $5M capacity in frontmatter.
- **Index/ETF calendars** (SPX, SPY, QQQ): far deeper, plausibly $50M+, but the edge per spread is thinner because index term structure is heavily arbitraged by professional vol desks.
- Market-impact shows up as paying through the spread on four legs; at scale, execution quality (legging, mid-price fills) becomes the dominant P&L driver.

## What kills this strategy

- **Large directional moves**: a gap through the profit zone sends both legs to parity and destroys the time-value differential -- the single most common loss mode.
- **IV crush on the back month**: a broad collapse in implied volatility (e.g., after a feared event passes) deflates the long leg's vega value even if price sits at the strike.
- **Persistent backwardation regimes**: in stressed markets, front-month IV trades rich to back-month for weeks, making new calendars structurally expensive and existing ones underwater.
- **Early assignment / pin risk** on the short leg near expiry, particularly American-style equity options around ex-dividend dates.
- **Transaction-cost creep**: widening bid-ask spreads in less liquid names can quietly turn a positive-expectancy program negative.
- **Crowding of short-vol flows**: when systematic premium-selling is over-popular, front-month IV compresses and the decay differential shrinks.

## Kill criteria

Retire or pause the strategy when any of the following triggers:

- Rolling 12-month P&L on the calendar book is negative after costs across **≥ 40 trades** (enough sample to rule out bad luck at typical win rates)
- Peak-to-trough drawdown on allocated capital exceeds **20%**
- Average realized round-trip cost exceeds **15% of average debit** (liquidity has deteriorated)
- Front-month/back-month ATM IV ratio for the traded universe stays above **1.05 for 3+ consecutive months** (structural backwardation; no new entries until contango returns)
- Win rate over the last 40 trades falls below **40%** (profit zone is being gapped through more than the model assumes)

## Advantages

- **Defined risk**: maximum loss is the net debit paid upfront
- **Theta-positive**: earns money from time decay when the underlying stays near the strike
- **Capital-efficient**: requires less capital than buying stock or naked options
- **Vega-positive**: benefits from rising implied volatility
- **Flexible**: can be adjusted by rolling the short leg or converting to a diagonal

## Disadvantages

- **Narrow profit zone**: requires the underlying to stay close to the strike price
- **Sensitive to IV changes**: a collapse in implied volatility can cause losses even at the right price
- **Pin risk at expiration**: if the stock is right at the strike at front-month expiry, the short option may be assigned
- **Requires active management**: not a set-and-forget strategy; rolling or adjusting is often needed
- **Transaction costs**: two legs (four total option transactions to open and close) increase commission drag

## Sources

- Natenberg, Sheldon. *Option Volatility and Pricing* (2nd ed., 2014) -- term structure, theta curvature, and calendar/time-spread mechanics
- McMillan, Lawrence. *Options as a Strategic Investment* (5th ed., 2012) -- calendar and diagonal spread construction and management
- Hull, John. *Options, Futures, and Other Derivatives* -- non-linear time decay of option value (theta ∝ 1/√T for ATM options)
- CBOE education materials on calendar spreads and volatility term structure

## Related

- [[theta-decay]] -- the primary profit driver for calendar spreads
- [[implied-volatility]] -- calendars are sensitive to vega and term structure
- [[options]] -- the instruments used
- [[options-pricing]] -- understanding how time and vol affect option prices
- [[credit-spread]] -- an alternative defined-risk options strategy
- [[covered-calls]] -- another theta-harvesting strategy
- [[cash-secured-puts]] -- short-put premium harvesting with full collateral
- [[edge-taxonomy]] -- the five edge categories referenced above
- [[volatility-risk-premium]] -- the underlying premium the short leg collects
- [[options-premium-selling]] -- the short-vol family this is the long-vega complement to
- [[short-put-spread]] / [[iron-fly]] -- short-vega credit structures the calendar pairs against
- [[iv-crush]] -- the back-month vega-collapse loss mode (and the event-timed opportunity)
- [[vega]] / [[theta]] -- the defining Greeks (long vega, positive theta)
- [[market-regime]] -- the regime conditioning that makes calendars the IVR-opposite of credit spreads
