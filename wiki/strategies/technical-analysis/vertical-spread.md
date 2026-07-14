---
title: "Vertical Spread"
type: strategy
created: 2026-04-13
updated: 2026-06-20
status: excellent
tags: [options, derivatives, technical-analysis, risk-management]
aliases: ["Vertical Spread", "Vertical Spreads", "Bull Call Spread", "Bear Put Spread", "Bull Put Spread", "Bear Call Spread", "Debit Spread", "Debit Vertical Spread"]
strategy_type: technical
timeframe: swing
markets: [options]
complexity: intermediate
backtest_status: untested
edge_source: [risk-bearing, analytical]
edge_mechanism: "Credit verticals harvest the variance risk premium on a short OTM strike with a bought wing capping the tail; debit verticals monetize a directional/technical view while financing it by selling back further-OTM optionality the market prices richly."
data_required: [options-chain, implied-volatility-surface, ohlcv-daily, earnings-calendar]
min_capital_usd: 2000
capacity_usd: 200000000
crowding_risk: medium
expected_sharpe: 0.4
expected_max_drawdown: 0.20
breakeven_cost_bps: 30
related: ["[[call-option]]", "[[put-option]]", "[[covered-call]]", "[[iron-condor]]", "[[options-overview]]", "[[options]]", "[[credit-spread]]", "[[call-spread]]", "[[trade-repair-and-rolling]]", "[[gamma-risk]]", "[[theta-decay]]", "[[position-sizing]]", "[[support-and-resistance]]", "[[implied-volatility]]"]
---

# Vertical Spread

A vertical spread is an [[options]] strategy involving simultaneously buying and selling two options of the same type (both calls or both puts) on the same underlying with the same expiration but different strike prices. Vertical spreads cap both maximum profit and maximum loss, making them a defined-risk alternative to outright option purchases. They are among the most commonly traded multi-leg options structures due to their simplicity and flexibility, and come in four flavours: two debit (bull call, bear put) and two credit (bull put, bear call).

## Edge source

Per [[edge-taxonomy]], the vertical spread is a *wrapper*, and its edge depends on which side of the premium it sits:

- **Risk-bearing** (credit verticals, dominant) -- the seller of a bull put or bear call spread is selling insurance at the short strike and buying cheaper reinsurance at the long strike, keeping the spread between the two. The net credit is compensation for bearing a defined slice of the [[variance-risk-premium]]: OTM options on equity indices and large caps are persistently priced above their actuarial value because hedgers and lottery-ticket buyers are willing overpayers.
- **Analytical** (debit verticals) -- a bull call or bear put spread has no structural edge by itself; its expectancy is the trader's directional/technical forecast. The structure's contribution is *efficiency*: the sold leg recovers part of the premium (and the richest part of the skew, when selling further-OTM puts in a bear put spread), so a correct directional call costs less per unit of payoff than an outright long option.

A vertical spread program with no forecasting skill and no IV selectivity is approximately a zero-edge structure minus costs -- the wrapper defines risk, it does not create expectancy.

## Why this edge exists

**Credit side**: the counterparty buying the short strike is typically a hedger (protective-put buyers below the market, covered-call-style upside buyers above it) or a convexity speculator. Both buy for utility or lottery payoff rather than expectancy, which keeps OTM premium structurally rich -- the same mechanism documented in the [[variance-risk-premium]] literature. The credit-vertical seller collects a retail-accessible, defined-risk slice of that premium. The buyers "keep losing" in expectation deliberately: they are paying for protection or for skewed payoffs, exactly as insurance customers do.

**Debit side**: the spread buyer is exploiting the *shape* of the surface rather than its level -- selling the further-OTM leg back to the same overpaying crowd. In a bear put spread, the sold lower-strike put sits further down the (expensive) put skew, so the spread buyer is partially financed by skew richness. The residual bet is directional, and the "other side" is simply whoever is wrong about direction; there is no persistent counterparty class, which is why debit verticals are only as good as the trader's signal.

## Null hypothesis

If implied volatility equalled subsequently realised volatility on average and the trader's directional calls were coin flips:

- **Credit verticals** would show their characteristic high win rate (a 30-delta short strike wins roughly 70% of the time by construction) but expectancy would be exactly zero before costs -- the ~3:1 loss-to-win size ratio cancels the win rate. After two-leg bid-ask costs each way, expectancy would be **negative**.
- **Debit verticals** would win roughly at the rate implied by the breakeven's distance from spot, with the max-profit/max-loss ratio cancelling it; net of costs, also negative.

So neither a high credit-spread win rate nor an occasional debit-spread multi-bagger is evidence of edge. Evidence is positive expectancy after costs, sustained across IV regimes -- for credit verticals via the VRP, for debit verticals via demonstrable forecast skill.

## Rules

### The four structures

**Debit spreads** require a net cash outlay at entry and profit when the underlying moves in the expected direction.

**Bull Call Spread** — Buy a lower-strike [[call-option|call]], sell a higher-strike call (same expiration). Bullish, defined risk.

*Example*: Stock at $100, 30 DTE.
- Buy $100 call for $4.00
- Sell $105 call for $2.00
- **Net debit**: $2.00 ($200 per contract)
- **Max profit**: ($105 - $100) - $2.00 = $3.00 ($300) — if stock closes above $105 at expiry
- **Max loss**: $2.00 ($200) — if stock closes below $100 at expiry
- **Breakeven**: $100 + $2.00 = $102.00

The long call provides upside exposure while the short call reduces cost but caps profit.

**Bear Put Spread** — Buy a higher-strike [[put-option|put]], sell a lower-strike put (same expiration). Bearish.

*Example*: Stock at $100, 30 DTE.
- Buy $100 put for $3.50
- Sell $95 put for $1.50
- **Net debit**: $2.00 ($200 per contract)
- **Max profit**: ($100 - $95) - $2.00 = $3.00 ($300) — if stock closes below $95 at expiry
- **Max loss**: $2.00 ($200) — if stock closes above $100 at expiry
- **Breakeven**: $100 - $2.00 = $98.00

Cheaper than buying a put outright because the sold put offsets part of the cost.

**[[credit-spread|Credit spreads]]** collect a net premium at entry and profit when the underlying stays away from the short strike.

**Bull Put Spread** — Sell a higher-strike put, buy a lower-strike put. Bullish to neutral.

*Example*: Stock at $100, 30 DTE.
- Sell $95 put for $2.00
- Buy $90 put for $0.80
- **Net credit**: $1.20 ($120 per contract)
- **Max profit**: $1.20 — if stock stays above $95 at expiry
- **Max loss**: ($95 - $90) - $1.20 = $3.80 ($380) — if stock falls below $90
- **Breakeven**: $95 - $1.20 = $93.80

Profits from [[theta-decay|time decay]] and the underlying staying above the short put strike.

**Bear Call Spread** — Sell a lower-strike call, buy a higher-strike call. Bearish to neutral.

*Example*: Stock at $100, 30 DTE.
- Sell $105 call for $1.80
- Buy $110 call for $0.70
- **Net credit**: $1.10 ($110 per contract)
- **Max profit**: $1.10 — if stock stays below $105 at expiry
- **Max loss**: ($110 - $105) - $1.10 = $3.90 ($390) — if stock rises above $110
- **Breakeven**: $105 + $1.10 = $106.10

### When to use each

| Strategy | Outlook | IV Environment | Preferred When |
|----------|---------|----------------|----------------|
| Bull Call Spread | Bullish | Low IV (debit is cheaper) | Expecting a move up, want defined risk |
| Bear Put Spread | Bearish | Low IV | Expecting a move down, want defined risk |
| Bull Put Spread | Neutral to Bullish | High IV (credit is richer) | Expecting support to hold, selling premium |
| Bear Call Spread | Neutral to Bearish | High IV | Expecting resistance to hold, selling premium |

### Entry

- **Universe**: liquid optionable underlyings only -- SPY/SPX/QQQ/IWM and large caps with penny-to-nickel-wide markets. Wide single-name spreads consume the edge (see Performance characteristics).
- **Credit verticals**: short strike at **25-30 delta** (roughly 70-75% probability of expiring OTM) *or* one strike beyond a tested [[support-and-resistance|support/resistance]] level; **30-45 DTE**; prefer IV Rank > 30 so the credit is worth the risk. Target a credit of at least **one-third of the spread width** (e.g., ≥ $1.65 on a $5-wide), otherwise the risk/reward is structurally poor.
- **Debit verticals**: buy the ATM or first-ITM strike, sell the strike at or just beyond the technical price target; **30-60 DTE**; prefer low-IV environments where the debit is cheap. Pay no more than **half the spread width** (e.g., ≤ $2.50 for a $5-wide) so max profit at least equals max loss.
- **Avoid** holding short strikes through scheduled binary events (earnings, FDA dates) unless the trade is explicitly an event trade.

### Exit

- **Credit verticals**: take profit at **50% of the credit received**; close or roll at **21 DTE** regardless (see The 21-DTE Rule below); hard stop when the loss reaches **2x the credit received**.
- **Debit verticals**: take profit at **50-75% of maximum value** or at the technical target; exit at **21 DTE** if neither the target nor the stop has been hit; hard stop at **−50% of the debit paid** or on a close beyond the technical invalidation level, whichever comes first.
- **Assignment hygiene**: close any American-style short leg that goes ITM into an ex-dividend date (short calls) or deep ITM near expiry (short puts) to avoid early assignment.

### Strike width and position sizing

The width between strikes determines the risk/reward profile:

| Spread Width | Max Loss | Max Profit | Characteristics |
|-------------|----------|------------|----------------|
| Narrow ($1-$2) | Lower | Lower | Higher transaction cost relative to gain; more trades needed |
| Medium ($5) | Moderate | Moderate | The sweet spot for most retail traders |
| Wide ($10+) | Higher | Higher | Better risk/reward ratio but requires more capital |

Typical strike selection targets the short strike at or near a key technical level ([[support-and-resistance|support/resistance]]) and uses 30-45 DTE for optimal [[theta-decay|theta]] characteristics. [[position-sizing|Position sizing]] is straightforward since max loss is defined: risk a fixed percentage of the account per spread (the [[position-sizing|2% rule]]). (Source: [[recovering-losing-options-positions]])

Book-level: cap aggregate vertical-spread max loss at **10% of NAV**, and avoid stacking multiple short strikes at the same price area across names that are correlated (a single index move can put every short strike ITM at once).

## Implementation pseudocode

```python
def open_bull_put_spread(market, underlying, width=5):
    # credit vertical: sell ~30-delta put, buy the wing `width` lower
    if market.iv_rank(underlying) < 30:
        return None                                  # credit too thin
    if market.has_event_before(underlying, dte=45):  # earnings/FDA filter
        return None
    chain  = market.options_chain(underlying)
    expiry = pick_expiry(chain, target_dte=40, range=(30, 45))
    short_put = chain.strike_by_delta(expiry, delta=-0.30)
    long_put  = chain.strike(expiry, short_put.strike - width)
    credit = short_put.bid - long_put.ask
    if credit < width / 3:                           # min 1/3-width credit
        return None
    max_loss = (width - credit) * 100
    qty = floor(0.02 * account.nav() / max_loss)     # 2% rule
    return sell(short_put, qty), buy(long_put, qty)

def manage(spread):
    if spread.is_credit:
        if spread.profit >= 0.50 * spread.credit:  close(spread)   # 50% take
        if spread.loss   >= 2.00 * spread.credit:  close(spread)   # 2x stop
        if spread.dte <= 21:                       close_or_roll(spread)
    else:  # debit
        if spread.value >= 0.75 * spread.width:    close(spread)   # near max
        if spread.value <= 0.50 * spread.debit:    close(spread)   # -50% stop
        if spread.dte <= 21:                       close(spread)

def roll(spread):
    # only roll credit spreads, and only for net credit or tiny debit
    new = same_strikes_next_cycle(spread)
    if net_cost(close(spread), open(new)) <= 0:
        execute_roll(spread, new)
```

## Indicators / data used

- **Options chain with Greeks** -- strike selection by delta (credit side) and by price target (debit side).
- **[[implied-volatility|IV]] Rank / percentile** -- regime selector: high IV favours credit structures, low IV favours debit structures.
- **[[support-and-resistance|Support/resistance]] levels** -- short-strike placement for credit spreads; targets for debit spreads.
- **Earnings calendar** and ex-dividend dates -- event and assignment-risk filters.
- **Daily OHLCV** -- trend context and technical invalidation levels.
- **Open interest and bid-ask width** at candidate strikes -- liquidity screen; reject markets wider than ~2% of the underlying-adjusted option price.

## Payoff diagram & Greeks profile

Every vertical spread has the same expiration payoff *skeleton*: **a sloped ramp between the two strikes that flattens into a floor on one side and a ceiling on the other**. Both max profit and max loss are fixed and known at entry — the structure's whole reason to exist. The difference between the four flavours is only *where* the ramp sits relative to spot and whether you paid (debit) or were paid (credit) to enter.

```
 Bull call (debit)           Bull put (credit)
 P&L                         P&L
  |     ______ max profit      |  ____ max profit (= credit)
  |    /                       | /
  |---/----------- long K      |/----------- short K
  |  /                         /
  |_/____ max loss (= debit)  /____ max loss (= width - credit)
  +-------------> price        +-------------> price
```

| Flavour | Net | Profits when | Max profit | Max loss |
|---|---|---|---|---|
| Bull call (debit) | Pay | Underlying rises above long strike | Width − debit | Debit paid |
| Bear put (debit) | Pay | Underlying falls below long strike | Width − debit | Debit paid |
| Bull put (credit) | Receive | Underlying stays above short strike | Credit received | Width − credit |
| Bear call (credit) | Receive | Underlying stays below short strike | Credit received | Width − credit |

The credit-side risk/reward is structurally unattractive at the headline level — risk ~3 to make ~1 on a 30-delta / $5-wide spread — but is offset by a ~70-75% win rate. The debit side is the reverse: a low hit rate carried by occasional payoffs up to ~1.5x the risk. Neither is "free" — see Null hypothesis above.

### Greeks profile (the offsetting-leg dampening)

The bought leg partly cancels the sold leg, so a vertical is a *muted* version of a single option's Greeks — closer to a pure price/probability bet than an outright:

| Greek | Credit vertical | Debit vertical |
|---|---|---|
| [[delta]] | Small (the structure is a probability bet) | Larger — the directional engine of the trade |
| [[gamma-risk\|gamma]] | Negative near the short strike (the 21-DTE trap) | Net long from the bought leg, partly offset |
| [[theta-decay\|theta]] | Positive — time decay is the income | Negative — the bought leg bleeds, partly financed by the sold leg |
| [[vega]] | Negative — short vol; an IV spike marks it down | Positive — long vol; suffers IV crush after events |

This is the key to the [[implied-volatility\|IV]]-regime selection rule in "When to use each": sell credit verticals when IV is *rich* (you are short vega and want it to fall), buy debit verticals when IV is *cheap* (you are long vega and want the cheap entry). The same [[volatility-risk-premium]] that powers [[covered-calls]] and the [[iron-condor]] is what the credit vertical harvests — a vertical is simply one half of an iron condor.

## Example trade

Bull put spread on a stock at $100 holding a tested $96 support level, 30 DTE, IV Rank 45:

1. Sell the $95 put (≈30 delta) for $2.00; buy the $90 put for $0.80. **Net credit $1.20** ($120), max loss $3.80 ($380), breakeven $93.80. On a $25,000 account the 2% rule allows one contract ($380 ≤ $500).
2. Over the next three weeks the stock chops between $97 and $103. Theta does the work: at 21 DTE with the stock at $101, the spread marks at $0.55.
3. Buying it back at $0.55 banks **$65 of the $120 credit (54%)** -- past the 50% take-profit trigger -- and eliminates three more weeks of [[gamma-risk|gamma]] exposure for the remaining $55 of potential profit.
4. Counterfactual discipline path: had the stock broken $96 early and the spread marked at $3.60 (a $240 loss = 2x credit), the rules close it there -- well above the $380 max loss -- or roll it out/down for a net credit per the rolling framework below.

## Adjustments and rolling

Vertical spreads — both debit and credit — can be adjusted when they move against the trader. See [[trade-repair-and-rolling]] for the complete rolling framework.

### Rolling a credit spread

When the underlying approaches the short strike of a credit spread:

1. **Roll out**: Buy back the current spread, sell the same strikes at a later expiration for a net credit. Buys time for the thesis to work.
2. **Roll out and away**: Move both strikes further OTM *and* extend expiration. Lowers the danger zone at the cost of extending duration.
3. **Key rule**: Only roll for a net credit or small net debit. Never add significant debit to a losing credit spread. (Source: [[recovering-losing-options-positions]])

### Rolling a debit spread

When the underlying moves against a debit spread (the wrong direction):

1. **Roll out**: Close the current spread, open the same strikes at a later expiration. Only costs a small additional debit if there is remaining time value.
2. **Roll out and further OTM**: For a losing long vertical, roll the whole spread out in time and further OTM — but only without adding net debit. Adding debit adds risk to an already losing trade. (Source: [[recovering-losing-options-positions]])

### Converting a losing long option to a spread

A powerful recovery tactic: when a single long call or put is losing, sell a further OTM option of the same type to convert it into a vertical spread:

- **Losing long call** → Sell a higher-strike call (creates a bull call spread). The credit reduces cost basis.
- **Losing long put** → Sell a lower-strike put (creates a bear put spread). The credit reduces cost basis.

This caps the maximum profit but also reduces the amount at risk. (Source: [[recovering-losing-options-positions]])

### The 21-DTE rule

Credit vertical spreads carry [[gamma-risk]] near expiration. At ~21 DTE, gamma spikes for ATM options, making delta shifts rapid and unpredictable. Many professional spread sellers close or roll at 21 DTE to avoid the "gamma trap." Debit spreads are less affected since the long leg benefits from gamma, but the short leg partially offsets this advantage. (Source: [[recovering-losing-options-positions]])

## Performance characteristics

- **Credit verticals (systematic, index, 30-delta short / 5-wide / 50% management)**: theoretical win rate ~70% at entry, rising to ~80-85% with the 50% take-profit because many spreads are closed before the short strike is ever tested. The cost: average winners (~$60 on the example spread) are far smaller than average losers (~$240 at the 2x-credit stop). Net expectancy is thin -- the structure hands back roughly a third of the gross VRP edge to costs. Realistic net Sharpe for a disciplined index program is in the **0.3-0.5** range; the frontmatter carries 0.4. Not independently backtested for this wiki (`backtest_status: untested`).
- **Debit verticals**: expectancy equals directional skill minus costs. With no skill they are a slow bleed; with a genuine technical edge they are one of the most capital-efficient ways to express it, since max loss is small and known.
- **Cost overlay**: four executions per round trip (two legs in, two out). On penny-wide SPY options the round trip costs roughly $4-8 per spread plus commissions (~1-3% of a typical $200 debit/credit); on nickel-to-dime-wide single names it can reach 5-10%, which alone can flip a thin credit-spread edge negative. The frontmatter `breakeven_cost_bps: 30` (of spread notional, round trip) is the threshold above which the systematic credit version stops paying.
- **Return profile**: credit verticals -- steady small gains, occasional 3x-sized losses, negative skew; debit verticals -- frequent small losses, occasional ~1.5x payoffs, positive skew. Max program drawdown expectation ~20% of allocated capital (frontmatter), typically realised when a trending market runs through clustered short strikes.

## Capacity limits

Effectively unconstrained at retail and small-fund size on index products: SPY and SPX verticals at 25-30 delta routinely have tens of thousands of contracts of open interest per strike, supporting programs well into the **low hundreds of millions of dollars** of spread notional (frontmatter `capacity_usd: 200000000` is conservative). Practical limits bind earlier elsewhere:

- **Single names**: OI at OTM strikes is often only a few thousand contracts; beyond ~$1-5M notional per name per cycle, the trader becomes the market and pays measurable impact on both legs.
- **Execution capacity**: spreads must be worked as single complex orders at mid; size beyond what the complex order book absorbs forces legging, which adds slippage and leg risk.
- **Crowding**: the 30-45 DTE, ~30-delta, 50%-management credit-spread template is taught by every options education platform, so the exact strikes are crowded (`crowding_risk: medium`); the dealer community prices this flow, gradually thinning the retail-accessible credit.

## What kills this strategy

- **Gap risk through the short strike** -- an overnight earnings gap or macro shock can take a credit spread from a small unrealised loss straight to near max loss, jumping past the 2x-credit stop. Defined risk caps the damage but does not prevent it.
- **Trending markets vs. credit spreads** -- a persistent trend (e.g., a 2022-style decline) repeatedly runs through bull-put short strikes; "support" levels fail in sequence and the high win rate inverts.
- **Vol regime shift** -- credit verticals sold in low IV are short vega with a thin credit; an IV expansion marks them down even when the underlying has not moved. Debit verticals bought in high IV suffer the mirror-image IV crush.
- **The gamma trap** -- holding short strikes inside 21 DTE; small underlying moves produce violent delta swings near expiry ([[gamma-risk]]).
- **Cost drag and over-trading** -- narrow spreads on wide-market underlyings can have round-trip friction exceeding 10% of max profit; the strategy dies quietly through a thousand spreads.
- **Assignment / pin risk** -- early assignment on ITM American-style short legs (especially short calls before ex-dividend), and expiration pin risk when the underlying closes at the short strike, leaving an unhedged stock position over the weekend.
- **Skill decay (debit side)** -- if the underlying technical signal stops working, the debit-vertical program reverts to the negative-expectancy null.

## Kill criteria

- **Program drawdown > 20% of allocated capital** (matches `expected_max_drawdown`) -- halt and review.
- **Credit-vertical program**: rolling 12-month expectancy negative across **≥ 40 closed spreads**, or win rate below **60%** over the same window (vs. ~70-75% design), indicating strike-placement or regime failure.
- **Debit-vertical program**: rolling 12-month hit rate below **35%** with average winner < 1.5x average loser -- the directional signal is dead.
- **Costs**: measured round-trip slippage + commissions exceed **30 bps of spread notional** (the frontmatter breakeven) for two consecutive quarters.
- **Discipline breach as auto-kill**: any spread held past 2x-credit loss (credit side) or past −50% of debit without a rule-based exit invalidates the live track record and forces a return to paper trading.

## Advantages

- **Defined risk on every trade** -- max loss is known at entry, which makes [[position-sizing]] mechanical and removes blow-up risk entirely (unlike naked short options).
- **Capital-efficient** -- margin equals max loss; far cheaper than cash-secured puts or naked calls for equivalent exposure, and accessible in small accounts (min ~$2,000).
- **Four structures cover every directional/IV combination** -- bullish/bearish crossed with debit/credit lets the trader match the structure to both the price view and the vol regime.
- **Reduced vega and theta sensitivity vs. single legs** -- the offsetting leg dampens IV and time-decay exposure, so the trade is closer to a pure price bet (debit) or pure probability bet (credit).
- **Repairable** -- rolling and conversion tactics ([[trade-repair-and-rolling]]) give losing positions structured second chances without adding open-ended risk.
- **Highly liquid and exchange-supported** -- complex order books execute both legs atomically, removing leg risk at entry.

## Disadvantages

- **Capped upside** -- the sold leg surrenders the tail; a debit spread that catches a 20% move earns the same as one that catches 6%.
- **Poor risk/reward on credit side** -- routinely risking ~3 to make ~1; a few full losses erase many winners, and the high win rate masks this until a trend arrives.
- **Four-leg round-trip costs** -- double the executions of a single option; on anything less liquid than top index products, friction consumes a large share of the edge.
- **Negative skew (credit) / negative carry (debit)** -- each side inherits the unpleasant half of the options P&L distribution.
- **Assignment complexity** -- American-style short legs introduce early-assignment and dividend-risk management that outright long options never face.
- **Pin risk at expiration** when the underlying settles at the short strike.

## Sources

- [[recovering-losing-options-positions]] -- rolling framework, conversion tactics, the 21-DTE rule, and sizing conventions used throughout this page.
- [[book-option-volatility-and-pricing]] -- Natenberg on vertical spread pricing, Greeks, and the relationship between spread width and risk.
- McMillan, L. *Options as a Strategic Investment* (5th ed.) -- standard reference treatment of bull/bear vertical spreads, breakevens, and follow-up action.
- CBOE options education (cboe.com) -- exchange definitions and margin treatment of vertical spreads.

## Related

- [[options]] — options market overview
- [[credit-spread]] — credit spread strategies in depth
- [[call-spread]] — call spread variations
- [[iron-condor]] — combining bull put and bear call spreads
- [[trade-repair-and-rolling]] — rolling and adjustment framework
- [[gamma-risk]] — risk near expiration driving the 21-DTE rule
- [[greeks]] — option sensitivities
- [[theta-decay]] — time decay dynamics
- [[position-sizing]] — sizing based on defined max loss
- [[strangle]] / [[short-strangle]] — undefined-risk premium-selling alternatives
- [[covered-call]] / [[covered-calls]] — a single-leg short-premium relative
- [[cash-secured-put]] — defined-collateral short-put income structure
- [[calendar-spread]] — time-spread alternative to the same-expiry vertical
- [[iron-condor]] — two credit verticals combined into a neutral structure
- [[options-income]] — the income strategy class credit verticals belong to
- [[options-portfolio-construction]] — book-level sizing of multiple spreads
- [[volatility-risk-premium]] — the premium the credit side harvests
- [[vega]] — the IV sensitivity that flips sign between credit and debit verticals
- [[implied-volatility]] — the regime selector between debit and credit structures
