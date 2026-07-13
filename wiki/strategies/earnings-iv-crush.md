---
title: "Earnings IV Crush"
type: strategy
created: 2026-05-07
updated: 2026-06-20
status: excellent
tags: [options, volatility, derivatives, stocks, quantitative, event-driven]
aliases: ["IV Crush Trade", "Earnings Vol Sale"]
strategy_type: quantitative
timeframe: intraday
markets: [stocks, options]
complexity: advanced
backtest_status: untested
edge_source: [behavioral, structural, risk-bearing]
edge_mechanism: "Sells the front-cycle IV peak immediately before a scheduled earnings announcement to harvest the deterministic post-print IV crush; the seller is paid for absorbing fat-left-tail outlier prints that the bulk of distribution does not deliver"
data_required: [options-chain, earnings-calendar, historical-implied-vol, realized-vol, options-skew]
min_capital_usd: 25000
capacity_usd: 3000000
crowding_risk: medium
expected_sharpe: 0.6
expected_max_drawdown: 0.30
breakeven_cost_bps: 80
decay_evidence: "Edge has compressed since the mid-2010s as more retail and quant capital sells earnings premium; outlier prints (NFLX 2022-04, META 2022-02, SNAP 2022-05, NVDA 2024 multiple cycles) deliver outsized losses to the short-vol cohort"
deploy_date: 2026-05-07
capital_allocation: "5% sleeve of options book"
kill_criteria: |
  - drawdown > 25% from peak equity on this sleeve
  - 3 consecutive quarterly cycles with sleeve P&L < 0
  - rolling 12-month average realized move > average implied move (edge sign flip)
  - 2 single-name losses each exceeding the sleeve's annual expected P&L
last_review: 2026-05-07
next_review: 2026-08-07
related: ["[[earnings-volatility]]", "[[earnings-volatility-trading]]", "[[implied-earnings-move]]", "[[iv-crush]]", "[[implied-volatility]]", "[[short-straddle]]", "[[short-strangle]]", "[[iron-condor]]", "[[double-calendar]]", "[[volatility-skew]]", "[[theta-targeting]]", "[[vega-budgeting]]", "[[options-portfolio-construction]]", "[[diversification-in-options]]", "[[variance-risk-premium]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]"]
---

The earnings IV crush trade sells [[options]] premium into the front-cycle [[implied-volatility|IV]] peak immediately before a scheduled corporate earnings announcement and closes the position the next morning after IV has collapsed. The trade harvests the **deterministic post-print [[iv-crush|IV crush]]** — the 30–50% absolute IV decline that occurs on the front-cycle contracts within seconds of the headline, regardless of the direction of the underlying move. This page covers the focused short-vol structure (short straddle, short strangle, iron condor, double calendar); for the broader long-vol-and-short-vol coverage of the earnings cycle, see [[earnings-volatility-trading]]. For the underlying conceptual cycle, see [[earnings-volatility]].

## Edge Source

This strategy draws on three of the five edge categories from [[edge-taxonomy]]:

- **Behavioral** — Retail and discretionary traders systematically overpay for binary-event optionality, anchoring on prior outlier prints and treating short-dated OTM calls and puts as cheap lottery tickets when they are not cheap in vol terms.
- **Structural** — Equity options market makers cannot delta-hedge gap risk; they price in a risk premium for the binary jump exposure they are forced to warehouse, and that premium accrues to the patient short-vol seller. (Source: [[2026-04-22-gap-finder-options-portfolios]])
- **Risk-bearing** — The seller is being paid to absorb the rare-but-severe fat-left-tail outcome (a NFLX-35%, META-25%, SNAP-40% type print). The edge is real on average but pays out as a positive mean with severe negative skew.

## Why This Edge Exists

Around an earnings print, the [[implied-earnings-move|implied move]] (≈ ATM straddle / spot, on the first expiry after the report) embeds the market's risk-neutral expectation of the surprise. Across large universes of liquid US single names and many years of data, the **average realised move is ~5–20% smaller than the average implied move** (Dubinsky, Johannes, Kaeck & Seeger, 2019, *Review of Financial Studies*; multiple [[tastytrade]] portfolio studies). The seller is paid this gap.

The other side of the trade is hedgers buying portfolio insurance against gap risk and retail speculators buying near-binary OTM contracts. They keep doing this — and continue to systematically lose on average — because the option pays them in the rare regime where the realised move is enormous, and that rare payout is exactly what they want from insurance. Insurance buyers do not need to win on average; they need to be hedged when it matters. The seller is the structural counterparty.

The edge is *not* a free lunch. It is a payment for warehousing left-tail jump risk. The realised distribution looks like *many small wins, occasional very large losses*. The trade survives only when sized to absorb the worst historical print without ruin.

## Null Hypothesis

Under the null, **realised move = implied move on average** with no risk premium for the seller. A delta-neutral short straddle held from T-1 close to T+0 open should earn zero net P&L gross of costs, and lose money net of costs. Rejecting the null requires demonstrating that the average realised move is statistically significantly below the average implied move across:

- A representative cross-section of liquid single names (300+ tickers minimum).
- A multi-year window covering at least one bull regime and one bear regime.
- A [[deflated-sharpe-ratio]] that survives the implicit selection bias of trading only liquid names.

A naive backtest is insufficient — costs (four-leg spread crossing, two round trips), survivorship (delisted names), and clustering (sector earnings weeks) materially shrink the apparent edge.

## Rules

### Universe and filtering

- US single-name options with **front-cycle open interest > 10,000 contracts** at the strike of interest.
- **Implied move > 1.10 × historical realised move** (last 8 cycles) — only sell when premium is rich relative to the name's surprise distribution.
- **No overlapping binary catalysts** — no FDA decision, lawsuit ruling, regulatory event, or other binary in the same window.
- **Skew check** — if [[volatility-skew|put skew]] is more than 2 standard deviations richer than the name's own history, the market is signalling a left-tail concern. Either skip or shift to a defined-risk structure with tighter wings on the put side.
- **No more than 2 names per sector per earnings week** — clustered surprises destroy diversification (see [[diversification-in-options]]).

### Entry timing

- **T-1, 30–60 minutes before close** — late enough that most of the IV ramp is in, early enough that liquidity has not thinned.
- For after-market reports (AMC), enter same-day late session; for before-market reports (BMO), enter prior-day close.
- Avoid sub-15-minute pre-close entries — fills deteriorate sharply.

### Structures (in order of conservatism)

1. **[[iron-condor|Iron condor]]** — short put and short call at ~1.0 × implied move from spot, long wings 1.5–2.0× implied move out. Defined risk; preferred for sleeves of any size.
2. **[[double-calendar]]** — sell front-cycle ATM straddle, buy back-cycle ATM straddle. Profits from the *term-structure normalisation* (front IV crushes more than back IV) rather than from the magnitude of the front crush alone. Lower expected return, lower variance, much lower tail risk.
3. **[[short-strangle]]** — short put and short call, no wings. Higher credit, undefined risk. Only acceptable if [[portfolio-margin]] and explicit sizing for a 4-SD print.
4. **[[short-straddle]]** — both legs ATM. Maximum credit, maximum gamma exposure, undefined risk. Reserved for extreme over-priced setups (implied move > 1.5× historical realised) and small per-trade size.

| Structure | Risk profile | Credit captured | Tail exposure | Best when | Suitable for |
|-----------|--------------|-----------------|---------------|-----------|--------------|
| [[iron-condor]] | Defined | Moderate | Capped at wing width | Implied/realised ratio 1.1–1.4, normal skew | Any book size |
| [[double-calendar]] | Defined (mostly) | Low | Lowest of the four | Front/back IV term inversion is steep | Risk-averse, smaller edge tolerance |
| [[short-strangle]] | Undefined | High | Severe (4-SD prints) | Implied/realised ratio > 1.4, portfolio-margin account | [[portfolio-margin]] only, sized for tail |
| [[short-straddle]] | Undefined | Highest | Most severe (ATM gamma) | Extreme overpricing (> 1.5×), small clip | Experts only, tiny per-trade size |

### Strike selection

- Anchor on **implied move**, not delta. A 16-delta strike inside the implied move on an earnings week is far riskier than a 16-delta strike on a non-event week.
- For iron condors, **wings 1.5× to 2.0× implied move from spot** balance defined-risk floor against credit captured.
- For names with heavy [[volatility-skew|put skew]], place the put leg further OTM (e.g. 1.2× implied move on the put side, 1.0× on the call side) to compensate.

### Position sizing

- **Per-name max loss ≤ 1% of book equity**. On a $250K book, no single earnings position can lose more than $2,500 at the wings.
- **Total earnings exposure ≤ 15% of book buying power** in any single week.
- **Vega contribution to the broader book ≤ 20%** of the [[vega-budgeting|vega budget]] aggregated across all single-name event positions in a week.

### Exit

- **T+0 morning, within first 30–60 minutes of cash open** — captures the bulk of the IV crush after the post-call repricing has settled.
- **Stop-loss at 2× credit received** — if the position is losing 2× the credit collected, close before further deterioration. This caps single-name damage even on tail prints (subject to gap risk).
- **Holiday/weekend bridge**: avoid carrying earnings positions across weekends; close T+0 even at a smaller-than-target profit.

## Implementation Pseudocode

```python
def screen_earnings_candidates(date):
    candidates = []
    for ticker in earnings_calendar(date):
        if not has_liquid_options(ticker, min_oi=10000):
            continue
        if has_overlapping_binary(ticker):
            continue
        if sector_count_this_week(ticker.sector) >= 2:
            continue

        implied_move = atm_straddle(ticker, exp=next_expiry_after(date)) / spot(ticker)
        realized_move = avg_abs_earnings_move(ticker, last_n=8)
        if implied_move < 1.10 * realized_move:
            continue

        skew_z = put_skew_zscore(ticker, lookback=252)
        if skew_z > 2.0:
            structure = "iron_condor_skewed"  # widen put wing
        else:
            structure = "iron_condor"

        candidates.append((ticker, implied_move, structure))
    return candidates


def open_position(ticker, implied_move, structure, book):
    s = spot(ticker)
    short_put_k = round_strike(s * (1 - implied_move))
    short_call_k = round_strike(s * (1 + implied_move))
    long_put_k = round_strike(s * (1 - 1.75 * implied_move))
    long_call_k = round_strike(s * (1 + 1.75 * implied_move))

    expiry = next_expiry_after(earnings_date(ticker))

    legs = build_iron_condor(ticker, expiry, short_put_k, short_call_k,
                             long_put_k, long_call_k)
    max_loss = wing_width(legs) - net_credit(legs)
    contracts = floor((0.01 * book.equity) / max_loss)

    if vega_contribution(legs, contracts) > 0.20 * book.vega_budget:
        contracts = scale_to_vega_budget(legs, contracts, book)

    submit(legs, contracts, time_in_force="DAY",
           entry_window=("T-1 15:00", "T-1 15:45"))


def manage_position(position):
    # Exit the morning after the print
    if now() in ("T+0 09:30", "T+0 10:30"):
        close(position, order_type="LIMIT", aggressive=True)

    # Hard stop on disasters
    if mark_to_market(position) <= -2.0 * position.credit_received:
        close(position, order_type="MARKET")
```

## Indicators / Data Used

- [[earnings-calendar]] — confirmed report dates, BMO/AMC timing, conference-call timing.
- [[implied-volatility]] front-cycle and term structure — the inversion magnitude is itself a screening filter.
- [[implied-earnings-move]] — primary anchor for strike placement.
- Historical realised post-earnings moves (8–16 prior cycles) — for the implied-vs-realised filter.
- ATM straddle price for the first expiry after the report.
- [[volatility-skew]] — z-score of front-cycle put skew vs the name's own history.
- [[options-greeks]] — delta, vega, gamma, theta of the open book; aggregate vega exposure.

## Payoff and Greeks

The earnings IV-crush trade is a **short-vega, short-gamma, positive-theta** position that profits from a single overnight repricing of [[implied-volatility]] rather than from the slow accrual of time decay. The dominant P&L driver is **vega** — the post-print collapse in front-cycle IV (often 30–50 absolute vol points) marks the short legs down sharply regardless of direction. The dominant *risk* driver is **gamma**: a large underlying gap delivers convex losses on the short strikes that vega gains cannot offset.

| Greek | Sign at entry | Role |
|-------|---------------|------|
| Vega | Short (negative) | The source of edge — IV crush is the payday. A short straddle/strangle/condor gains as IV falls. |
| Theta | Long (positive) | Minor over a sub-24-hour hold; the trade is a vol-event trade, not a theta-harvest trade. |
| Gamma | Short (negative) | The killer — a gap through the short strike produces accelerating, convex loss. Worst inside the print. |
| Delta | ~0 at entry | Set up delta-neutral; becomes one-sided fast once the underlying gaps. |

The payoff diagram of the iron-condor variant is a flat profit plateau between the short strikes (where the position keeps the full credit after the crush) with defined-loss shoulders out to the long wings. The naked [[short-strangle]] / [[short-straddle]] variants replace the defined-loss shoulders with unbounded loss tails — the reason they require [[portfolio-margin]] and explicit 4-SD sizing. Crucially, **the IV crush is symmetric in direction but the trade is not symmetric in P&L**: vega gains are bounded by the credit, while gamma losses on a tail gap are not (until the wings, if any).

## Example Trade

**Setup**: Stock XYZ at $100, reports earnings AMC tomorrow. Front-week ATM straddle = $5.00 → implied move ≈ 5%. Last 8 earnings: average realised move 3.6% absolute. Implied/realised ratio = 1.39. Put-skew z-score = +0.4 (normal). Sector quota: 1 name used this week.

**Structure** (iron condor, expiry day after earnings):

- Sell $95 put @ $1.80
- Buy $90 put @ $0.70  (1.0× and 2.0× implied move on put side)
- Sell $105 call @ $1.70
- Buy $110 call @ $0.60  (1.0× and 2.0× implied move on call side)

Net credit = **$2.20**. Max loss = $5.00 wing − $2.20 credit = **$2.80** per contract = $280.

**Sizing**: $250K book, max 1% per name = $2,500 → 8 contracts.

**Aggregate at entry**: net credit $1,760, max loss $2,240, vega ~$45/IV-pt.

**T+0 morning**: XYZ opens at $102 (+2%, well inside short strikes). IV crushes from 80% to 30% on the front cycle. Iron condor marks at $0.40. Bought back. **Net P&L: $1.80 × 8 × 100 = $1,440** over a single overnight hold. (Source: [[2026-04-22-gap-finder-options-portfolios]])

## Performance Characteristics

Documented and practitioner-estimated metrics for a disciplined, diversified earnings-IV-crush sleeve trading liquid US single names:

- **Sharpe (net of costs)**: 0.5–1.0
- **Win rate**: 65–75% of cycles
- **Loser/winner ratio**: typical loser is 3–5× typical winner
- **Skew**: severe negative — return distribution has a long left tail
- **Drawdowns**: 15–30% on clustered earnings shocks (e.g. Q1 2022 mega-cap tech, Q4 2024 NVDA cycle)
- **Cost sensitivity**: 4-leg spreads pay [[bid-ask-spread|bid-ask spread]] 8 times per round trip; if round-trip cost > 80 bps, the edge is erased
- **Capacity-degraded Sharpe** at full deployment: typically 60–70% of the unconstrained backtest Sharpe

## Capacity Limits

Capacity is **low to moderate**. Single-name front-cycle option liquidity is the binding constraint. Even on the most liquid names (NVDA, AAPL, TSLA), positions of more than a few hundred contracts per leg push the [[bid-ask-spread]] and signal flow to market makers. A diversified sleeve trading 30–50 names per quarter scales to roughly **$2–5M of risk capital** before market impact and adverse selection meaningfully degrade the edge. Index-level vol selling on SPX or RUT scales further but is a different strategy adjacent to this one. See [[capacity-and-decay]].

## What Kills This Strategy

The most likely failure modes from [[failure-modes]]:

1. **Outlier print blow-through wings** — a 3-SD or 4-SD gap (NFLX 2022-04 -35%, META 2022-02 -26%, SNAP 2022-05 -40%) blows the put leg past the long wing on an iron condor or far past the strike on a naked strangle. Even with sized wings, undersized wings on a single trade can erase a year of accumulated edge.
2. **Clustered surprises** — when several mega-cap names in the same sector miss in the same week (Q1 2022 META + NFLX + SNAP within weeks), the short-vol book compounds losses with no diversification.
3. **Regime shift in implied-vs-realised** — an entire quarter where realised exceeds implied across the universe (Q1 2020 Covid earnings; multiple NVDA cycles 2024). The edge inverts and the trade pays the seller nothing.
4. **Crowding-driven decay** — as more retail and quant capital sells earnings premium, the implied-vs-realised gap narrows. The trade has been compressing since the mid-2010s.
5. **Operational error** — wrong expiry selected (selling the contract that does *not* span the earnings date), mis-timed exit (holding through the conference call when policy is to exit at the headline), wrong-direction skew assumption, or holding through a halt that prevents wing-protected exit.
6. **Underestimated [[volatility-skew|skew]]** — symmetric strikes on a heavily skewed name silently asymmetric the risk; left-tail prints disproportionately damage the put leg.
7. **Carrying single-name event vol against an aggregate [[vega-budgeting|vega budget]] computed on index-options assumptions** — the diversification assumption fails in shocks (see [[diversification-in-options]]).

## Kill Criteria

Pause and review (see [[when-to-retire-a-strategy]]) the sleeve if **any** of:

- Drawdown exceeds 25% from peak equity on the sleeve.
- 3 consecutive quarterly cycles each lose money on the sleeve.
- Trailing 12-month average realised move > average implied move across the universe (sign flip on the core edge).
- Two single-name losses each exceed the sleeve's annual expected P&L.
- Per-trade [[breakeven-cost]] exceeds 80 bps round-trip due to spread widening or slippage.
- Aggregate single-name event-vega exceeds 20% of book vega budget for two consecutive earnings weeks (concentration-risk breach).

## Advantages

- **Persistent, well-documented edge** when sized and diversified — short event-vol is one of the most-studied [[variance-risk-premium]] expressions.
- **Defined risk** when expressed as an [[iron-condor]] — known max loss per position.
- **Short hold time** — typically <24 hours per position; capital recycles quickly.
- **Theta and vega both work for the seller** simultaneously across the IV crush.
- **Diversifiable** across many uncorrelated single-name events per quarter (subject to sector concentration rules).

## Disadvantages

- **Severe negative skew** — small consistent gains, occasional catastrophic losses.
- **Operationally intensive** — per-name research, an [[earnings-calendar|earnings calendar]], and disciplined T-1/T+0 execution.
- **Capacity constrained** — single-name front-cycle option liquidity caps deployable capital well below index-vol strategies.
- **Costly** — 4-legged spreads pay [[bid-ask-spread]] 8 times per round trip.
- **Crowding risk** — increasingly populated trade since the mid-2010s; edge compressing.
- **Naked-strangle and short-straddle variants are unbounded-loss** — only iron-condor, double-calendar, or wing-protected variants are appropriate for finite-capital books.
- **Tail prints are correlated with bear regimes** — exactly when the rest of the book is also drawing down.

## Sources

- (Source: [[2026-04-22-gap-finder-options-portfolios]])
- Dubinsky, A., Johannes, M., Kaeck, A., & Seeger, N. (2019) — "Option Pricing of Earnings Announcement Risks", *Review of Financial Studies* (earlier circulated as Dubinsky & Johannes, 2006) — the canonical academic treatment of option-implied earnings-announcement moves vs realised moves. Citation corrected from Augustin/Brenner/Subrahmanyam (2014), which concerns informed options trading before *takeover* announcements, not earnings. Verified via Perplexity (sonar), 2026-06-10.
- [[tastytrade]] — multi-year published research on earnings short-premium expected value and win rate.
- [[book-option-volatility-and-pricing]] — Natenberg on event vol and surface dynamics.
- [[itpm-trading-philosophy]] — practitioner sizing of event vol within a multi-strategy options book.

## Related

- [[earnings-volatility]] — the conceptual cycle the trade harvests
- [[earnings-volatility-trading]] — the broader strategy class (includes long-vol flavour)
- [[earnings-vol-mean-reversion]] — adjacent strategy on post-event vol normalisation
- [[implied-earnings-move]] — strike-anchor input
- [[iv-crush]] — the post-event collapse phenomenon in isolation
- [[short-straddle]], [[short-strangle]], [[iron-condor]], [[double-calendar]] — structures
- [[volatility-skew]] — asymmetric pricing of left-tail risk
- [[theta-targeting]], [[vega-budgeting]] — book-level constraints
- [[options-portfolio-construction]] — where this sleeve fits
- [[diversification-in-options]] — why "diversified" earnings-vol can still concentrate factor risk
- [[variance-risk-premium]] — the structural edge underlying short event vol
- [[failure-modes]] — historical blow-ups
- [[when-to-retire-a-strategy]] — kill criteria framework
