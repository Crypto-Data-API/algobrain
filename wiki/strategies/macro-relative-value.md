---
title: "Macro Relative Value"
type: strategy
created: 2026-04-15
updated: 2026-06-21
status: excellent
tags: [fundamental-analysis, quantitative, bonds, forex, macro-relative-value, mean-reversion]
aliases: ["Macro Relative Value", "Macro RV", "Global Macro Relative Value", "Cross-Market Relative Value"]
related: ["[[global-macro]]", "[[relative-value-arbitrage]]", "[[pairs-trading]]", "[[carry-trade]]", "[[yield-curve]]", "[[swap-spread-arbitrage]]", "[[on-off-the-run-treasury-arbitrage]]", "[[edge-taxonomy]]", "[[failure-modes]]"]
strategy_type: fundamental
timeframe: position
markets: [bonds, forex, stocks, commodities]
complexity: advanced
backtest_status: untested
edge_source: [analytical, structural, risk-bearing]
edge_mechanism: "Macro instruments that share a common driver (rates, growth, inflation) drift apart on flow, policy, or sentiment shocks; the RV trader takes the convergent side of a hedged spread against directional and structurally constrained participants who are forced to be on the other side."
data_required: [ohlcv-daily, macro, fundamentals-pit, rates-curves, fx-spot, futures]
min_capital_usd: 250000
capacity_usd: 2000000000
crowding_risk: medium
expected_sharpe: 0.8
expected_max_drawdown: 0.18
breakeven_cost_bps: 8
---

Macro relative value (macro RV) is a family of **spread trades expressed across markets, countries, and the term structure**, where the trader holds a hedged long/short package whose payoff depends on the *relationship* between two macro-sensitive instruments rather than the absolute direction of any one of them. Where [[global-macro]] takes outright directional bets on rates, currencies, and equities, macro RV isolates the *relative* mispricing — e.g. long German Bunds vs short US Treasuries, long Brazilian rates vs short Mexican rates, or a flattener on the 2s10s curve — sized to be neutral to the dominant first-order risk factor (duration, FX beta, equity beta). It sits between pure [[relative-value-arbitrage]] (near-identical instruments, tight convergence) and outright [[global-macro]] (directional, thematic), trading on macro fundamentals plus a convergence or carry thesis.

### Where macro RV sits on the spectrum

| Dimension | [[relative-value-arbitrage]] | **Macro RV** | [[global-macro]] |
|-----------|------------------------------|--------------|------------------|
| Instruments | Near-identical (on/off-run, cash/futures) | Related, common macro driver | Outright, any asset |
| Convergence | Tight, near-certain (basis) | Probabilistic, fundamentals-driven | None — directional view |
| Horizon | Days–weeks | Weeks–quarters | Weeks–years |
| Primary risk | Funding / basis blowout | De-grossing + fair-value break | Direction wrong |
| Hedged factor | Almost everything | Dominant factor (duration / beta / FX) | Nothing (factor *is* the bet) |
| Example | [[on-off-the-run-treasury-arbitrage]] | DE 10y vs US 10y, 2s10s flattener | "Long USD", "short duration" |

The defining choice is the **hedge**: macro RV deliberately neutralizes the first-order factor (duration via DV01, equity via beta, FX via notional/carry) so the residual P&L is the *relationship*, not the level.

## Edge source

Primarily **analytical** and **structural**, with a **risk-bearing** component (see [[edge-taxonomy]]).

- **Analytical** — the edge comes from a better mapping of macro fundamentals (relative growth, inflation, fiscal/monetary path, terms of trade) onto a fair spread between two instruments, then trading the gap between fair and market value.
- **Structural** — many of the dislocations are produced by non-economic flows: index rebalances, central-bank QE/QT, pension and insurer liability-driven buying, real-money benchmark constraints, and regulatory capital rules that force participants to hold or shed specific tenors and countries regardless of value.
- **Risk-bearing** — the RV trader is paid carry and a convergence premium for warehousing the risk that the spread widens further (mark-to-market and funding risk) before it converges.

## Why this edge exists

The people on the other side are typically not trying to win the spread trade:

- **Real-money and benchmark-constrained investors** (sovereign reserve managers, index funds, insurers) buy or sell instruments to match a benchmark or hedge a liability, not to capture relative value. They will hold a rich bond or sell a cheap one to stay benchmark-neutral.
- **Central banks and policy actors** distort spreads deliberately (QE compresses term premia and peripheral spreads; FX intervention pins a currency). They are price-insensitive.
- **Levered RV desks under stress** are forced to *de-gross* during drawdowns, pushing spreads further from fair value exactly when they are most attractive — the [[ltcm-collapse-1998|LTCM]] dynamic. This both creates the opportunity and is the principal risk.

The edge persists because the dislocations are recurrent (driven by structural flows and policy), the trades require balance-sheet, repo lines, and cross-market infrastructure that constrain who can participate, and the convergence horizon (weeks to quarters) is too long and too drawdown-prone for most discretionary traders.

## Null hypothesis

Under the null, macro spreads are a fair, efficient reflection of relative fundamentals plus a fair risk premium, so the *expected* convergence return net of carry and financing is zero. A macro-RV book run under the null would deliver a Sharpe statistically indistinguishable from zero once realistic financing, bid/ask, and de-grossing tail losses are deducted, and its drawdowns would arrive precisely when the trader most needs liquidity. Concretely: a basket of randomly chosen, beta-hedged country/curve spreads, rebalanced mechanically, should show no positive risk-adjusted return after costs. Beating that null requires demonstrating that the fundamental fair-value signal predicts subsequent convergence out of sample.

## Rules

### Entry
1. **Identify the spread** — pick two macro-sensitive instruments sharing a dominant driver: a curve (2s10s, 5s30s), a cross-country rate pair (DE vs US 10y, BR vs MX 2y), an FX cross (relative-rate or terms-of-trade driven), or a cross-country equity index pair.
2. **Estimate fair value** — model the fair spread from relative fundamentals (growth, core inflation, policy-rate path, fiscal trajectory, real yields, terms of trade). A z-score of (market spread − fair spread) over a 1–3y window is the canonical signal.
3. **Hedge the dominant factor** — size the legs so the package is duration-neutral (rates), beta/notional-neutral (equities), or carry-aware (FX). Use DV01 weighting for rate spreads.
4. **Require a catalyst or carry** — only enter when the trade either pays positive carry while you wait or has an identifiable convergence catalyst (auction, central-bank meeting, index rebalance, election resolution).
5. **Trigger** — enter when |z| ≥ 1.5 and carry is non-negative for the convergent side.

### Exit
- **Take profit** — exit/scale when the spread reverts to z ≈ 0 (fair value) or the carry thesis is realized.
- **Stop / thesis-break** — exit if the fundamental model's fair value moves *with* the market move (the dislocation was information, not flow), or at a hard spread stop (e.g. z ≥ 3.0 against you).
- **Time stop** — exit if convergence has not begun within the expected horizon (typically 1–2 quarters).

### Position sizing
- Size to a target *spread* volatility, not notional — typically risk 0.5–1.0% of book per trade, capped so no single macro theme exceeds ~15–20% of risk.
- Hold a diversified basket (8–20 uncorrelated macro spreads) so idiosyncratic blow-ups do not dominate.
- Pre-commit a **gross-exposure cap** and a **de-grossing schedule** for drawdowns — the failure mode is always leverage in a liquidity crunch.

## Canonical macro-RV expressions

The toolkit is a set of recurring trade structures, each hedged to a different dominant factor:

| Expression | Example legs | Hedged factor | Driver / thesis | Related |
|-----------|--------------|---------------|------------------|---------|
| **Curve trade** | 2s10s flattener / steepener; 5s30s | Level (duration), via DV01 | Policy-path vs term-premium mispricing | [[yield-curve]] |
| **Cross-country rates** | DE 10y vs US 10y; BR 2y vs MX 2y | Global duration | Relative growth / inflation / fiscal | [[global-macro]] |
| **Swap spread** | Swap rate vs sovereign yield | Duration | Funding, balance-sheet, credit-of-government | [[swap-spread-arbitrage]] |
| **On/off-the-run** | Off-run vs on-run Treasury | Duration | Liquidity premium, repo specialness | [[on-off-the-run-treasury-arbitrage]] |
| **FX relative value** | Long high-real-rate vs short low | FX beta / carry-aware | Real-rate or terms-of-trade differential | [[carry-trade]] |
| **Cross-country equity** | Long index A vs short index B | Equity beta / notional | Relative earnings/macro cycle | [[pairs-trading]] |
| **Inflation breakeven RV** | Breakevens across countries/tenors | Real duration | Relative inflation regime | [[yield-curve]] |

Each row is a hedged package; the convergence signal in every case is a z-score of (market spread − fundamentally-fair spread), and the entry is gated on positive (or at least non-negative) carry on the convergent side.

## Implementation pseudocode

```python
def macro_rv_signals(universe, fundamentals, lookback=750):
    book = []
    for pair in universe:                      # e.g. ("DE10Y","US10Y"), ("2Y","10Y") curve
        leg_a, leg_b = pair
        spread = market_spread(leg_a, leg_b)   # yield diff, log-ratio, or DV01-weighted
        fair   = fair_value_model(pair, fundamentals)  # relative growth/inflation/policy
        z = (spread - fair) / rolling_std(spread - fair, lookback)
        carry = expected_carry(pair)           # roll-down + funding-adjusted

        if abs(z) >= 1.5 and sign_consistent(carry, -z):
            direction = -sign(z)               # fade the dislocation
            w = direction * target_risk / spread_vol(pair)
            book.append(Trade(pair, weight=w, hedge=factor_neutral(pair)))

    book = cap_theme_risk(book, max_theme=0.20)
    book = enforce_gross_cap(book, max_gross=cfg.max_gross)
    return book

def manage(position, fundamentals):
    z = current_z(position)
    if abs(z) <= 0.2:           return "take_profit"
    if fair_moved_with_market(position, fundamentals): return "thesis_break"
    if z * position.entry_sign > 3.0:                  return "stop"
    if position.age > position.horizon:                return "time_stop"
    return "hold"
```

## Indicators / data used

- **Rates** — sovereign yield curves and swap curves by country/tenor; repo and OIS for funding/carry; DV01s for hedge ratios.
- **FX** — spot, forward points, real-rate differentials, terms of trade.
- **Macro fundamentals (point-in-time)** — relative GDP/PMI growth, core inflation, policy-rate paths and central-bank guidance, fiscal balances, current accounts.
- **Flow/structural** — auction calendars, QE/QT schedules, index-rebalance dates, positioning surveys ([[cot-report-analysis|CFTC COT]], dealer surveys).
- **Cross-asset** — equity index futures for cross-country equity RV, commodity terms-of-trade for FX.

## Example trade

In a regime where the market prices the ECB and Fed on convergent paths but US fundamentals (growth, fiscal issuance) argue for higher relative US term premium, the DE–US 10y spread sits at z = −2.0 (Bunds too rich vs Treasuries relative to fair value). The trader goes **long US 10y futures, short German Bund futures, DV01-matched**, earning positive net carry. Over the next quarter, heavy US Treasury supply and a hawkish Fed re-steepen the spread back toward fair value (z → 0); the spread move plus carry yields a return uncorrelated with the outright direction of global rates. If instead US data had collapsed and *fair value itself* shifted toward Bunds, the model would flag thesis-break and the trade is cut before the dislocation became information-driven.

## Performance characteristics (realistic costs)

- **Expected net Sharpe** ~0.6–0.9 for a well-diversified, conservatively levered book; individual themes are far noisier.
- **Return profile** — long stretches of steady carry-plus-convergence punctuated by sharp, fat-tailed drawdowns during liquidity events (2008, March 2020, 2022 gilt LDI crisis). Returns are **negatively skewed**.
- **Costs** — bid/ask on liquid sovereigns and FX is low (≈1–4 bps round trip), but the binding cost is **financing/repo** and the cost of forced de-grossing in stress; emerging-market legs carry much wider spreads and gap risk.
- **Correlation** — low to equities and to outright macro in calm regimes, but correlation *spikes toward 1 across RV books* in crises (common de-grossing).

## Capacity limits

High in developed-market rates and major FX — multi-strategy pods and macro funds run macro-RV books in the **hundreds of millions to low billions** of dollars of risk. Capacity is constrained by repo balance-sheet availability, the depth of the specific spread (EM and off-the-run tenors fill quickly), and crowding among the handful of large RV desks that trade the same dislocations. Estimated practical capacity per individual theme is a few hundred million notional before market impact and crowding erode the edge; the aggregate book can scale to ~$2bn of risk for a top-tier desk.

## Historical de-grossing episodes

The strategy's defining tail risk — convergence trades blowing *wider* in a liquidity crunch — has recurred across decades. These are the canonical case studies a macro-RV trader should internalize:

| Episode | What happened to RV spreads | Lesson |
|---------|----------------------------|--------|
| **1998 [[ltcm-collapse-1998\|LTCM]]** | Swap spreads, on/off-run, and EM convergence trades all widened simultaneously; forced liquidation fed the move | Leverage + correlated "uncorrelated" trades = death spiral |
| **2008 GFC** | Basis trades (CDS-bond, covered-interest-parity) blew out; funding vanished | Funding *is* the trade; repo haircuts can break it |
| **March 2020** | US Treasury cash-futures **basis unwind**; even the "safest" RV trade gapped | Crowded leveraged basis is fragile to a dash-for-cash |
| **2022 UK gilt / LDI** | Forced LDI selling drove gilt yields to extremes against fair value | Structural, non-economic sellers can persist longer than you can fund |

The common thread is **simultaneous spread-widening and funding withdrawal** — the two ingredients that turn a diversified RV book's "uncorrelated" positions into one correlated short-liquidity bet. See [[failure-modes]].

## What kills this strategy

(See [[failure-modes]].)

- **Forced de-grossing / leverage spiral** — the dominant killer; spreads widen against you and funding tightens simultaneously, forcing liquidation at the worst price (the [[ltcm-collapse-1998|LTCM]] pattern).
- **Regime/fair-value break** — a structural shift (new central-bank reaction function, fiscal regime change, default) means the spread should not converge; mean-reversion logic bleeds money.
- **Crowding** — too many RV desks in the same trade amplifies both the dislocation and the de-grossing cascade.
- **Funding shocks** — repo haircuts widen, basis blows out (March 2020 Treasury basis unwind), and the carry that justified the trade inverts.
- **Hidden directional bias** — imperfect hedge ratios leave residual duration/beta that swamps the relative-value P&L.

## Kill criteria

- Rolling 12-month Sharpe < 0 after costs **and** max drawdown > 18% of allocated risk.
- Realized correlation of the RV book to a global de-grossing factor > 0.7 for more than one quarter (the diversification thesis has failed).
- Funding cost (repo/financing spread) exceeds the expected carry on > 50% of the book.
- Single-theme loss > 5% of book in a month from a fair-value/regime break that the model failed to flag.
- Gross exposure breaches the pre-committed cap and cannot be reduced without realizing > 8% loss.

## Advantages

- **Direction-agnostic** — low beta to outright equity and rate markets in normal regimes; a genuine diversifier.
- **Carry-positive** — many trades pay you to wait, unlike pure directional bets.
- **Scalable** in developed-market rates and FX; large capacity for institutional capital.
- **Grounded in fundamentals** — the fair-value model gives a falsifiable, repeatable signal rather than discretionary conviction.

## Disadvantages

- **Negatively skewed, fat-tailed** — small steady gains, occasional catastrophic losses concentrated in liquidity crises.
- **Leverage-dependent** — the raw spread P&L is small, so the strategy needs leverage to be worthwhile, which is what turns drawdowns into blow-ups.
- **Infrastructure-heavy** — requires repo lines, cross-market execution, and modeling capability out of reach for retail.
- **Crowded** — the largest opportunities are known to every macro-RV desk; convergence can be slow and de-grossing fast.
- **Model risk** — the entire edge rests on the fair-value mapping being right; regime changes silently invalidate it.

## Sources

- Drobny, Steven. *Inside the House of Money* (2006) — interviews with global macro and RV traders on cross-market spread trades.
- Lowenstein, Roger. *When Genius Failed: The Rise and Fall of Long-Term Capital Management* (2000) — canonical account of the leverage/de-grossing failure mode in relative value.
- Ilmanen, Antti. *Expected Returns* (2011) — carry, value, and relative-value premia across asset classes.
- BIS Quarterly Reviews on the March 2020 Treasury basis unwind and the 2022 UK gilt/LDI crisis — structural-flow dislocations exploited and feared by macro-RV books.

## Related

- [[global-macro]] — the directional cousin
- [[relative-value-arbitrage]] — the tight-convergence, fixed-income cousin
- [[carry-trade]] — overlapping carry component
- [[pairs-trading]] — the equity-level analogue of relative-value spreads
- [[yield-curve]] — curve trades are a core macro-RV expression
- [[swap-spread-arbitrage]], [[on-off-the-run-treasury-arbitrage]] — specific RV trades within the macro toolkit
- [[edge-taxonomy]], [[failure-modes]]
