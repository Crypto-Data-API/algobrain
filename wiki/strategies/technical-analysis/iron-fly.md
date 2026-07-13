---
title: "Iron Fly"
type: strategy
created: 2026-05-07
updated: 2026-06-21
status: excellent
tags: [options, volatility, derivatives, swing-trading, quantitative]
aliases: ["Iron Butterfly", "Iron Fly", "ATM Iron Condor"]
strategy_type: quantitative
timeframe: swing
markets: [stocks, options]
complexity: advanced
backtest_status: untested
edge_source: [risk-bearing, behavioral]
edge_mechanism: "A short ATM straddle wrapped in long OTM wings: collects the maximum at-the-money variance risk premium with a hard cap on tail loss, in exchange for accepting heavy gamma exposure around the short strike."
data_required: [options-chain, implied-volatility-surface, vix-term-structure, ohlcv-daily]
min_capital_usd: 25000   # smallest NAV where a SPY-sized fly's max loss fits the 2-3% per-trade cap in Rules
capacity_usd: 500000000
crowding_risk: medium
expected_sharpe: 0.5
expected_max_drawdown: 0.25
breakeven_cost_bps: 40
related: ["[[iron-condor]]", "[[short-straddle]]", "[[short-strangle]]", "[[strangle]]", "[[options-premium-selling]]", "[[theta-targeting]]", "[[vega-budgeting]]", "[[managing-winners]]", "[[zero-dte-options]]", "[[gamma-explosion]]", "[[probability-of-touch]]", "[[implied-volatility]]", "[[volmageddon]]"]
---

# Iron Fly

The iron fly (also called the iron butterfly) is a four-leg [[options]] structure that combines a [[short-straddle]] at the at-the-money strike with two long out-of-the-money wings. Mechanically it is a [[short-straddle]] wrapped in protection: sell the ATM call and ATM put, then buy a further-OTM call and a further-OTM put with the same expiration to cap the disaster scenarios. The result is a defined-risk neutral structure with **the highest theta-per-dollar of any common premium-selling spread**, paid for by **the highest [[gamma]] exposure of any common premium-selling spread** -- a classic high-decay, high-path-risk profile that lives at the gamma-heavy end of the [[theta-targeting#Theta-to-Vega Ratio (T/V)|T/V curve]].

## Edge source

Primarily **risk-bearing**, secondarily **behavioral** (see [[edge-taxonomy]] and [[options-premium-selling]]).

- **Risk-bearing** -- the seller is the insurer at the most expensive strike on the surface (ATM, where extrinsic value peaks). The wings transform the unbounded short-straddle tail into a defined-loss insurance contract sold to the dealer.
- **Behavioral** -- ATM premium is structurally rich because hedgers, structured-product desks, and gamma-trading dealers are persistent net buyers of ATM optionality at any given moment. The seller of the iron fly is, in effect, the residual seller filling that demand at a price the buyer is willing to pay.

The behavioral edge concentrates at the body strike: the price of an ATM straddle is the market's median expected move, and this median is consistently *high* relative to subsequently realised volatility on liquid index products. The iron fly captures that overpricing in concentrated form.

## Why this edge exists

ATM options are where the [[variance-risk-premium]] (VRP) is mechanically largest in absolute dollar terms. An ATM straddle's price is itself the market's expected absolute move out to expiration (approximately 0.8x the one-sigma move); OTM strangles capture only a slice of it. The buyer of an ATM straddle is paying for the most-likely-to-be-exercised optionality on the chain, and is paying a premium relative to how much the underlying actually moves on average. Iron fly sellers harvest that overpricing, with the wings capping the cost of the days when the buyer is right.

The other side of the trade is dominated by **structured-product hedgers** (auto-callable issuers who must dynamically buy ATM gamma), **systematic vol-targeting funds** (which mechanically buy puts when realised vol rises), and **dealers who short gamma at the ATM and need to scalp it back**. None are price-insensitive -- but together they form a persistently price-elevated bid for ATM extrinsic value.

## Null hypothesis

If [[implied-volatility|IV]] exactly equalled subsequently realised volatility at the ATM strike on average, the iron fly would earn **zero** before costs and **negative** after costs and slippage. The position would still have negative skew (the short body dominates the wings) but the long-run mean would be flat. Practitioner backtests (tastytrade-style studies of SPX 30-45 DTE iron flies managed at 25% of max profit and 21 DTE) report positive expectancy before costs on the order of 4-7% per year on margin, dropping to roughly 1-3% after realistic round-trip costs and slippage — directionally consistent with the broader [[variance-risk-premium]] literature but not independently validated for this wiki. The edge exists but is **fragile to costs** because the structure is four-legged and traded frequently.

## Rules

**Universe**: SPX, SPY, QQQ, RUT, NDX as the core. Single-name iron flies are technically possible but the bid-ask drag almost always makes them economically unattractive at retail size.

**Entry**:

- Sell the ATM call and ATM put (both at the same strike, or the closest available pair) at **30-45 DTE** for the standard income variant; **0-2 DTE** for the [[zero-dte-options|0DTE]] variant (much higher gamma risk -- see below).
- Buy long wings symmetric around the body, sized relative to the at-the-money [[expected-move]]: typically **around 1x the expected move** for the 30-45 DTE income variant (roughly **250-350 points on SPX** at 5,200 with VIX 16; **25-35 points on SPY**). For the 0-2 DTE variant the expected move itself is far smaller, so **30-50-point SPX wings** are the norm there. Wing width is the most important sizing decision -- it sets max loss directly. Wings far *inside* the expected move neutralise the structure's theta and vega along with its tail (the fly barely decays and prices at nearly full width); wings far *outside* add max loss without buying meaningful extra credit.
- Enter only when [[ivr|IV Rank]] (or VIX percentile) is **above 30**; the iron fly's edge is a function of IV, and selling ATM gamma at 12-VIX is the [[theta-targeting#The Theta Trap|theta trap]] in concentrated form.
- Avoid earnings on single names; for index trades avoid the 24h before scheduled FOMC, CPI, NFP unless explicitly trading the post-event IV crush.

**Position sizing**:

- Per-trade max loss capped at **2-3% of NAV** (max loss = wing width − net credit, times multiplier).
- Aggregate iron-fly [[gamma]] capped against a session-level "1% adverse move" budget: simulate a 1σ move and ensure the implied P&L hit is below ~5% of NAV.
- Vega budget shared with the rest of the [[options-premium-selling|short-premium book]] per [[vega-budgeting]].

**Exit**:

- Close at **25% of max profit** for iron flies (lower than the 50% used on [[iron-condor]]/[[short-strangle]]) -- the body's gamma profile means realised P&L deteriorates rapidly past the easy-money zone. See [[managing-winners]].
- Close at **21 DTE** regardless of P&L. The iron fly's gamma curve is unmanageable inside three weeks.
- Close immediately if the underlying trades through a breakeven (body strike ± net credit) *and* the position is showing more than 1.5x credit lost -- a sustained trend through a breakeven toward a wing is the structure's worst path.

## Implementation pseudocode

```python
def open_iron_fly(market, underlying="SPX", dte=35, wing_width=300):
    # wing_width ~= 1x the ATM expected move for the 30-45 DTE variant
    spot = market.spot(underlying)
    body_strike = round_to_nearest_strike(spot, increment=5)

    # Sell the body
    short_call = market.option(underlying, body_strike, "call", dte)
    short_put  = market.option(underlying, body_strike, "put",  dte)

    # Buy the wings
    long_call  = market.option(underlying, body_strike + wing_width, "call", dte)
    long_put   = market.option(underlying, body_strike - wing_width, "put",  dte)

    credit = short_call.bid + short_put.bid - long_call.ask - long_put.ask
    max_loss = wing_width - credit  # times multiplier (100 for SPX index)

    if credit < 0.40 * wing_width:
        return None  # premium too thin for an ATM fly at this width -- skip

    return Position(
        legs=[("sell", short_call), ("sell", short_put),
              ("buy",  long_call),  ("buy",  long_put)],
        credit=credit,
        max_loss=max_loss,
        breakevens=(body_strike - credit, body_strike + credit),
    )

def manage_iron_fly(position):
    if position.pct_max_profit_realized() >= 0.25:
        close(position, reason="25pct_profit_target")
    elif position.dte() <= 21:
        close(position, reason="21dte_time_exit")
    elif position.spot_beyond_breakeven() and position.pnl < -1.5 * position.credit:
        close(position, reason="breakeven_breach_stop")
```

## Indicators / data used

- Real-time [[options-chain]] with greeks for ATM and wing strikes.
- [[vix]] level and [[vix-term-structure]] for regime context.
- [[ivr|IV Rank]] / IV Percentile for the underlying.
- [[expected-move]] (≈ ATM straddle price) -- the iron fly *is* a sale of the expected-move band, so this is the trade's mechanical reference.
- [[realized-volatility]] vs IV for VRP capture diagnostics.
- Earnings, FOMC, CPI, NFP calendars for blackout windows.

## Payoff & Greeks

The iron fly's payoff is a **sharp tent**: a single peak at the body strike (max profit = net credit when the underlying pins the body), sloping down linearly on both sides to a flat max-loss floor at each wing. It is the defined-risk version of a [[short-straddle]] — the same A-frame, with the bottom corners clipped by the long wings.

```
Iron fly P&L at expiration

 +credit ┤              ╱╲              ← max profit at the body strike Kb
         │             ╱  ╲
    0  ──┼────────────╱────╲──────────────
         │      BE_lo╱      ╲BE_hi
 −maxloss┤━━━━━━━━━━╱        ╲━━━━━━━━━━━━  ← capped at the wings
         └──────────────────────────────────
            Kp(put wing)  Kb  Kc(call wing)
         breakevens = Kb ± net_credit
         max_loss   = wing_width − net_credit   (× multiplier)
```

The breakevens (body ± credit) sit *well inside* one [[expected-move]] of entry — which is exactly why breakeven touches are so frequent and why the body's [[gamma]] dominates the P&L path.

Net Greeks (the most concentrated short-vol Greeks of the common defined-risk structures):

| Greek | Sign | Magnitude vs [[iron-condor]] | Comment |
|---|---|---|---|
| [[delta]] | ~0 at entry | similar | symmetric; flips fast once price leaves the body |
| [[gamma]] | **strongly negative** | **highest** of common short-premium spreads | the dominant risk; a 1% adverse session can re-mark 15-25% of credit; see [[gamma-explosion]] |
| [[theta]] | **strongly positive** | **highest** per dollar at risk (~2x a same-width condor) | the income engine; accelerates violently inside 21 DTE |
| [[vega]] | **negative** | high | a large fraction of early P&L is [[iv-crush]] rather than raw theta; the wings mute the very early decay |

The structure is the extreme corner of the [[theta-targeting#Theta-to-Vega Ratio (T/V)|T/V curve]]: maximum theta and maximum gamma for a given wing width. That is the whole trade — you are paid the richest ATM [[variance-risk-premium]] in exchange for bearing the worst path risk among defined-risk premium sellers. Compare the gentler Greek profile of the OTM-bodied [[iron-condor]] and the directional [[short-put-spread]].

## Example trade

*Illustrative only -- not a recommendation. Prices are approximate, Black-Scholes-consistent marks for the stated vol and tenor (same SPX regime as the [[theta-targeting]] worked example).*

- **Date**: 2026-04-15. SPX = 5,200. VIX = 16. IVR = 35. 35 DTE. One-sigma expected move ≈ ±260 points; ATM straddle ≈ $205.
- **Trade** (1 contract, 300-point wings ≈ 1.15x the expected move):
  - Sell SPX 5,200 call at $104.00.
  - Sell SPX 5,200 put at $101.00.
  - Buy SPX 5,500 call at $16.00.
  - Buy SPX 4,900 put at $24.00 (put wing richer than the call wing because of index skew).
  - **Net credit**: $104 + $101 − $16 − $24 = **$165 per fly** ($16,500 / contract).
  - **Wing width**: 300 points.
  - **Max loss**: $300 − $165 = **$135 per fly = $13,500** (hit only if SPX settles beyond a wing).
  - **Breakevens at expiration**: 5,365 (up) and 5,035 (down) -- about ±3.2%, well inside the wings but ~0.6x the expected move.
  - **Theta at entry**: roughly +$1.5/day per fly in index points (≈ $150/contract/day), accelerating sharply inside three weeks.
  - **Vega**: ~−$6 per IV point in index points (≈ −$600/contract).
  - **Gamma**: concentrated at the body; a 1% adverse session can re-mark the position by 15-25% of credit.
- **Day 14 (21 DTE)**: SPX has drifted to 5,225 and IV has crushed 16 → 13.5. The fly marks at ~$125. **Profit: $40/fly = ~24% of max profit** -- the 25% profit target and the 21-DTE time stop trigger essentially together; close.

The iron fly's signature profile is visible here: in the first weeks most of the P&L comes from **IV crush rather than raw theta** -- the long wings mute net decay early, and decay concentrates violently inside 21 DTE, which is exactly the window the management rules refuse to hold through. The same body gamma that would accelerate profit near expiry is what makes the loss path fast in adverse moves.

## Performance characteristics

- **Theoretical theta-per-dollar-at-risk** is ~2x that of a comparable [[iron-condor]] at the same wing width. The iron fly does in 1 week what a 16-delta condor does in 2-3.
- **Hit rate**: ~50-60% of trades reach the 25% profit target before expiry; ~70-80% finish profitable if held to expiration *and* the underlying stays inside the breakevens. Breakeven touches are common (~40-50% of trades) because the breakevens sit well inside one expected move of the entry price.
- **Win/loss ratio**: small wins, large losses. Average winner ~25% of max profit; average loser ~60-80% of max loss. Profit factor 1.0-1.5 in mixed regimes; <1.0 in trending markets.
- **Sharpe** (in-sample, before costs): 0.6-1.0. Net of round-trip costs (4 legs × spread): 0.3-0.7. Iron flies are **cost-fragile** -- on weekly options the effective edge can be entirely eaten by spread+commission.
- **Best regime**: post-shock, vol-mean-reverting; high IVR, range-bound underlying with no scheduled events.
- **Worst regime**: trending markets where the underlying drifts steadily through the body; or [[volmageddon|vol shocks]] where the ATM strike collapses to deep ITM on either side.

### Regime conditioning

The iron fly is the most [[market-regime|regime]]-fragile member of the premium-selling family because its breakevens sit inside one expected move:

| [[market-regime\|Regime]] | Behaviour | Action |
|---|---|---|
| Post-shock, vol mean-reverting | the ideal: high IVR, range-bound, IV crushing back to realised | best entries |
| Calm, low-IVR grind | thin credit, the [[theta-targeting#The Theta Trap\|theta trap]] in concentrated form | stand aside; sell wider [[iron-condor]] instead |
| Trending / directional drift | underlying walks through a breakeven toward a wing | the most common loss path; cut on breakeven breach |
| Vol shock | ATM body reprices past the credit; wings cap but realise the loss | defined risk holds, but it is still the worst path |

Because exposure is gamma-dominant rather than vega-dominant, a static [[long-vol-overlay]] calibrated for [[short-strangle|strangle]]-style vega does **not** hedge the iron fly well — manage the gamma directly via the wing width and the mechanical 21-DTE exit.

## Capacity limits

- Index iron flies (SPX, SPY, QQQ): capacity is large -- single funds run multi-hundred-million books in this structure on 0-2 DTE. Practical retail/small-fund cap is the trader's [[buying-power]] and risk tolerance, not the market's depth.
- Single-name iron flies: capacity tight; typically a few million per name before bid-ask drag and crossing the four-leg spread destroys the edge.
- Capacity is constrained by [[gamma-explosion|gamma]] absorption capacity in the trader's NAV: every additional iron fly adds gamma that must be borne through the body region.

## What kills this strategy

The dominant failure modes (see [[failure-modes]]):

1. **Trend through a breakeven** -- a steady directional drift that takes the underlying through a breakeven and toward a wing. Iron flies hate trending markets; this is the most common loss path.
2. **Assignment risk near the body on physically-settled products** -- on SPY or single names, settling within pennies of the body strike leaves one short leg's assignment uncertain, creating an unhedged overnight share position. (Cash-settled SPX flies do not have this problem -- settling at the body there is the *max-profit* outcome.)
3. **[[gamma-explosion]] near expiry** -- the body's gamma in the final 7 DTE can turn a +5% position into a -50% position in hours.
4. **Vol shock** -- IV expansion of 5+ points reprices the body short strikes by more than the credit collected; if the trader exits in panic, the wings provide capped but realised loss.
5. **Cost drag** -- on weekly cycles, four-leg round-trip costs of 30-50 bps eat the entire structural edge.
6. **Earnings or event surprise** on single-name iron flies -- a binary gap through the body is the textbook ruin path.

## Kill criteria

Mechanical retirement triggers (see [[when-to-retire-a-strategy]]):

- **Drawdown**: strategy-level drawdown exceeds 15% -> halve size; 25% -> halt new entries pending review.
- **Realised hit rate** below 40% on a rolling 50-trade window -> review entry filters and DTE selection.
- **Realised P&L per trade** below 10% of credit on a rolling 50-trade window -> review (the structural edge is failing or costs are too high).
- **Round-trip cost** rises above 40 bps -> review; above 60 bps -> retire on this product.
- **Breakeven-touch frequency** above 70% on a rolling window -> realised vol is running too hot for this structure; pause and switch to wider [[iron-condor|condors]].

## Advantages

- **Highest theta-per-dollar** of common premium-selling spreads -- excellent income velocity in calm regimes.
- **Defined risk** -- max loss is known and capped at entry, unlike [[short-strangle|short strangles]] or [[short-straddle|short straddles]].
- Capital-efficient under [[portfolio-margin]] and reasonable under T-Reg margin.
- Symmetric -- no directional bias; the structure simply needs the underlying to stay near where it started.
- Natural fit for **range-bound, post-shock, mean-reverting** SPX/SPY tape.

## Disadvantages

- **Highest [[gamma]] of common short-premium spreads** -- a single 1% adverse session can produce a loss equal to many days of theta accrued. Path risk dominates outcome.
- **Asymmetric realized win/loss**: under the 25%-of-max-profit / 21-DTE management regime, average losers run roughly 1.5-2.5x average winners, so losers must stay infrequent for the book to profit.
- **Cost-fragile**: 4-leg round-trip on weeklies often consumes a meaningful fraction of the credit.
- **Pin/assignment risk** at the body in the final hours of expiration on physically-settled underlyings (SPY, single names); cash-settled index flies (SPX) avoid this but still carry settlement-print gamma.
- **Short ATM gamma** is the canonical short-vol crash exposure -- iron flies amplify the [[volmageddon]]-style blowup risk relative to wider structures, even though they are technically defined-risk.
- **Frequent profit targets** mean high trade count, high commission drag, high mental overhead.
- Does **not pair well** with a static [[long-vol-overlay]] -- the overlay is calibrated for [[short-strangle|strangle]]-like vega exposure, while the iron fly's exposure is gamma-dominant.

## Sources

- [[book-option-volatility-and-pricing]] -- Natenberg on the iron fly's gamma profile and the relationship between body and wings.
- [[tastytrade]] research archive -- 25%-of-max-profit and 21-DTE management studies on iron flies vs iron condors.
- [[options-premium-selling]] -- the broader VRP context.
- [[zero-dte-options]] -- the modern 0DTE iron fly variant and its regulatory context.
- [[volmageddon]] -- the 2018 short-vol blowup and what it implies for iron-fly tail behaviour despite the wings.

## Related

- [[iron-condor]] -- the wider, lower-theta, lower-gamma sibling. Most income books prefer condors; iron flies appear when [[theta-targeting|theta targets]] need a boost or when IV is rich enough to justify the gamma exposure.
- [[short-straddle]] -- the iron fly without wings. Higher theta, undefined risk.
- [[short-strangle]] / [[strangle]] -- the canonical OTM-body short premium structure.
- [[options-premium-selling]] -- the umbrella strategy this lives inside.
- [[theta-targeting]] -- where the iron fly fits in a theta-budgeted book.
- [[vega-budgeting]] -- the complementary vega constraint.
- [[managing-winners]] -- the 25% / 21-DTE management rules.
- [[zero-dte-options]] -- 0DTE iron flies as a separate (much more dangerous) variant.
- [[gamma-explosion]] -- the path-risk mechanism that dominates iron-fly P&L distribution.
- [[probability-of-touch]] -- why ATM body strikes touch so often.
- [[short-put-spread]] -- the directional, lower-gamma defined-risk cousin.
- [[calendar-spread]] -- a long-vega alternative for low-IV regimes (the opposite vega sign).
- [[implied-earnings-move]] -- sets the expected-move band an earnings-cycle iron fly sells.
- [[iv-crush]] -- the early-P&L driver, especially in event-timed flies.
- [[theta]] / [[vega]] / [[gamma]] -- the Greeks whose extreme values define this structure.
- [[market-regime]] -- regime conditioning for this gamma-heavy structure.
- [[expected-move]] -- the band the iron fly is mechanically a sale of.
