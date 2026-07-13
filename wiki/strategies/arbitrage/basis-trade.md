---
title: "Basis Trade"
type: strategy
created: 2026-06-22
updated: 2026-06-22
status: good
tags: [arbitrage, quantitative, futures, leverage, market-neutral, crypto, risk-management]
aliases: ["Cash-and-Carry", "Basis Trading", "Treasury Basis Trade", "Spot-Futures Basis"]
strategy_type: quantitative
timeframe: position
markets: [bonds, futures, crypto]
complexity: advanced
backtest_status: untested
edge_source: [structural, risk-bearing]
edge_mechanism: "Captures the convergence of a futures (or perpetual) price to its underlying cash asset at delivery — the buyer of the basis earns the spread plus repo carry by warehousing balance sheet, financing, and liquidity risk that the marginal futures long does not want to hold."
data_required: [ohlcv-daily, futures-term-structure, repo-rates, funding-rates, deliverable-basket]
min_capital_usd: 25000
capacity_usd: 50000000000
crowding_risk: high
expected_sharpe: 1.5
expected_max_drawdown: 0.10
breakeven_cost_bps: 5
related: ["[[cash-and-carry]]", "[[basis]]", "[[arbitrage]]", "[[futures]]", "[[repo]]", "[[funding-rate]]", "[[funding-rate-arbitrage]]", "[[contango]]", "[[edge-taxonomy]]"]
---

# Basis Trade

The basis trade is the classic **cash-and-carry [[arbitrage]]**: hold the cash (spot) asset and short the corresponding [[futures]] contract (or vice versa) to capture the **[[basis]]** — the difference between the futures price and the spot price — as it converges to zero at delivery. Because both legs reference the same underlying and settle to the same price, the position is directionally market-neutral; the P&L is the locked-in basis plus or minus financing carry. The trade has two canonical incarnations: the **Treasury basis trade** (cash bond vs. bond future, financed in [[repo]], run at extreme leverage by hedge funds and flagged repeatedly as a systemic-risk concern) and the **crypto cash-and-carry** (spot vs. perpetual/dated future, where the "basis" is largely the [[funding-rate]]).

## Edge source

Per [[edge-taxonomy]], the basis trade is primarily a **structural** edge with a large **risk-bearing** component:

- **Structural** — the basis exists because different participants face different costs and constraints. Asset managers and convexity buyers want leveraged or capital-efficient long exposure via futures and are willing to pay up for it (futures rich); the basis trader supplies that exposure synthetically by buying the cheap cash asset and shorting the rich future. In crypto, levered longs bid perpetuals above spot, pushing [[funding-rate]] positive.
- **Risk-bearing** — the trader is paid to warehouse balance-sheet usage, financing/[[repo]] risk, liquidity risk, and the risk that the basis widens before it converges. The "near-arbitrage" return is really a fee for renting your balance sheet and tolerating mark-to-market and margin volatility on the way to a guaranteed terminal convergence.

## Why this edge exists

- **Who is on the other side (Treasury)**: real-money long-only managers, pension funds, and macro accounts that prefer the operational simplicity and capital efficiency of long Treasury *futures* over holding the physical bond. Their demand makes the future expensive relative to the cheapest-to-deliver cash bond. The basis trader buys the cash bond, finances it in [[repo]], and sells the rich future, collecting the spread to delivery.
- **Who is on the other side (crypto)**: leveraged retail and prop longs who pay positive [[funding-rate]] to hold perpetual longs in a bull market. The cash-and-carry trader is short the perp / dated future against long spot and collects that funding.
- **Why they keep paying**: the futures/perp long is buying *leverage and convenience*, not making a valuation error. They rationally pay the basis as a financing-and-access cost. The trade is not free money — it is compensation for capital, balance sheet, and the tail risk of a disorderly unwind.

## Null hypothesis

If markets are frictionless and the basis is fairly priced, the net return of a fully financed basis trade equals the risk-free financing rate — i.e., **zero excess return** after [[repo]]/funding costs and haircuts. Any apparent profit is then payment for the funding spread, the balance-sheet charge, and the convergence-path risk. A basis trader with no genuine edge in financing or execution should, under the null, earn approximately the carry minus costs and minus the occasional large loss when financing dries up — leaving an expected excess return near zero or negative once a fat-tailed deleveraging event is included.

## Rules

### Entry
1. **Measure the basis.** Treasury: net basis = cash bond price − (futures price × conversion factor), adjusted for carry to delivery; look for a positive *implied repo rate* above your actual repo cost. Crypto: annualized basis = ((future − spot) / spot) × (365 / DTE), or for perps the running [[funding-rate]].
2. **Confirm carry is positive after financing.** Only enter when the basis (or funding) exceeds your all-in financing cost (repo rate + haircut drag, or borrow/exchange fees) by a margin that compensates for path risk.
3. **Buy the cash leg, short the futures/perp leg** in matched notional (delivery-adjusted for Treasuries via the conversion factor and cheapest-to-deliver analysis).
4. **Finance the cash leg** in [[repo]] (Treasuries) or fund the spot purchase (crypto). Lock term repo where possible to avoid overnight rollover risk.

### Exit
1. **Hold to delivery/expiry** — the default. Convergence delivers the basis.
2. **Early unwind on basis compression** — if the spread collapses faster than carry would deliver, close both legs and redeploy.
3. **Roll** — at expiry, roll the short into the next contract if the new basis is attractive (the "roll" is itself a tradable spread).
4. **Emergency unwind** — if repo financing tightens, haircuts spike, or an exchange/counterparty shows stress, exit immediately regardless of basis.

### Position sizing
- Size to *financing capacity and margin survivability*, not to the headline arbitrage profit. Treasury basis trades are run at very high leverage (small haircut on repo), so a modest widening of the basis or a haircut increase can force deleveraging.
- Cap single-counterparty / single-exchange exposure; stress the position against a multi-standard-deviation widening of the basis and a haircut hike *before* sizing.

## Implementation pseudocode

```python
# Generic cash-and-carry basis trade
def basis_trade(spot, future, dte, repo_rate, hurdle_bps):
    # annualized basis (carry yield)
    ann_basis = (future - spot) / spot * (365 / dte)
    net_carry = ann_basis - repo_rate          # after financing
    if net_carry * 1e4 < hurdle_bps:
        return None                            # not worth balance sheet
    notional = size_to_margin_survivability(spot, future)
    buy_cash(spot, notional)                   # long cash / spot
    short_future(future, notional)             # short the rich future
    finance_in_repo(notional, repo_rate)       # Treasuries: term repo

    while not at_delivery(dte):
        if repo_haircut_spiking() or counterparty_stress():
            unwind_all(); break                # disorderly-unwind guard
        roll_repo_if_needed()
    # convergence: future -> cash; realized PnL ≈ initial basis + carry - costs
```

## Indicators / data used
- **[[basis]] / net basis** (Treasury) and **annualized basis or [[funding-rate]]** (crypto) — the core signal.
- **Implied repo rate** vs. **actual [[repo]] rate** — the Treasury go/no-go.
- **Cheapest-to-deliver (CTD) bond and conversion factors** — define the deliverable basket and hedge ratio.
- **Repo haircuts and term-repo availability** — the financing-fragility gauge.
- **Futures open interest / term structure ([[contango]])** — liquidity and roll richness.
- **Funding rates and perp open interest** (crypto) — confirms leveraged-long demand.

## Example trade

*Illustrative, round numbers — not a backtest.*

**Crypto cash-and-carry.** Spot BTC = $100,000; 90-day future = $103,000.
- Annualized basis = (3,000 / 100,000) × (365 / 90) ≈ **12.2% APY**.
- Buy 1 BTC spot, short 1 BTC future. At expiry the future converges to spot; net P&L ≈ $3,000 regardless of where BTC settles (minus fees and funding).

**Treasury basis (qualitative).** A fund buys a $100m cash Treasury, finances ~98–99% of it in overnight [[repo]] (small haircut), and shorts the matched bond future. The captured net basis might be only a few basis points — but financed at, say, 50:1, the *return on equity* is large. This is precisely why the trade is run at extreme leverage and why a small dislocation in repo or the basis can be violent.

## Performance characteristics
- **Return profile**: many small, steady positive carry increments punctuated by rare large losses during financing/liquidity stress — a short-volatility-of-the-basis payoff.
- **Cost sensitivity**: profitability lives or dies on financing cost. In Treasuries the *implied repo vs. actual repo* spread is the whole edge; in crypto, exchange fees and funding-rate sign changes dominate.
- **Best conditions**: steep, stable [[contango]] / persistently positive funding; deep repo liquidity; calm volatility.
- **Worst conditions**: liquidity crises, repo-market stress, haircut spikes, exchange insolvency — exactly when the "arbitrage" deleverages all at once.

## Capacity limits
- **Treasury basis**: enormous in absolute notional (hundreds of billions are estimated to be deployed across funds), but capacity is *systemically* constrained — the aggregate trade has been repeatedly flagged by the Federal Reserve, the BIS, and other regulators as a financial-stability concern, because a forced, simultaneous unwind can dislocate the world's most important bond market (as stress episodes in the Treasury market have illustrated). [[crowding-risk]] is high.
- **Crypto cash-and-carry**: capacity scales with perp/futures open interest and spot depth per venue; tens of billions in aggregate but venue-fragmented and capped by counterparty and withdrawal risk.

## What kills this strategy
- **Financing shock** — repo haircuts jump or term funding vanishes, forcing deleveraging before convergence (see [[failure-modes]]).
- **Basis widening before convergence** — mark-to-market and margin losses can trigger liquidation even though terminal convergence is guaranteed.
- **Counterparty / exchange failure** — the "risk-free" leg evaporates (the FTX collapse is the canonical crypto example).
- **Crowding cascade** — when everyone holds the same leveraged basis position, the unwind is self-reinforcing.

## Kill criteria
- Net carry after all-in financing < 0 for the holding period → do not enter / exit.
- Repo haircut on the cash leg rises by more than ~50% from entry → cut leverage immediately.
- Mark-to-market loss on the spread exceeds 2× the captured carry → reassess and consider unwinding.
- Any credible counterparty-solvency signal → unwind in full, same day.
- Single-venue/single-counterparty exposure > 25% of book → trim.

## Advantages
- Directionally market-neutral; P&L driven by convergence, not price level.
- The terminal payoff (convergence) is mechanically near-certain absent default.
- Scales to very large notional; integrates with [[funding-rate-arbitrage]] in crypto.
- Yield is largely known at entry, aiding planning.

## Disadvantages
- **Picking up pennies in front of a steamroller** — thin per-trade edge magnified by leverage, with fat-tailed unwind risk.
- Highly sensitive to financing cost and haircut changes.
- Capital- and balance-sheet-intensive; opportunity cost over the holding period.
- Counterparty and liquidity risk dominate the tail; "risk-free" is a misnomer.
- Systemic crowding (Treasuries) means your exit door is shared with everyone else's.

## Sources
General market knowledge; no specific wiki source ingested yet.

## Related
- [[cash-and-carry]] — the same trade described for crypto/commodities
- [[basis]] — the spread the trade harvests
- [[funding-rate-arbitrage]] — the perpetual-futures cousin
- [[repo]] — the financing mechanism behind the Treasury version
- [[funding-rate]] — the crypto "basis"
- [[futures]], [[contango]] — the term-structure context
- [[arbitrage]], [[edge-taxonomy]] — classification
