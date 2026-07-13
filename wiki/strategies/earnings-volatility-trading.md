---
title: "Earnings Volatility Trading"
type: strategy
created: 2026-05-03
updated: 2026-06-21
status: excellent
tags: [options, volatility, derivatives, mean-reversion, stocks, event-driven]
aliases: ["Earnings Vol", "Earnings Straddle"]
strategy_type: quantitative
timeframe: intraday
markets: [stocks, options]
complexity: advanced
backtest_status: untested
edge_source: [behavioral, structural, risk-bearing]
edge_mechanism: "Sells the volatility risk premium embedded in options around earnings — implied moves systematically exceed realized moves on average across liquid single names, because hedgers and speculators bid up event-vol; the seller is paid to bear tail risk on outlier prints"
data_required: [options-chain, earnings-calendar, historical-implied-vol, realized-vol]
min_capital_usd: 25000
capacity_usd: 5000000
crowding_risk: medium
expected_sharpe: 0.7
expected_max_drawdown: 0.30
breakeven_cost_bps: 80
decay_evidence: "Edge has shrunk since 2010s as more retail and quant capital sells earnings premium; outlier prints (e.g. NFLX 2022, META 2022, GOOG 2024) deliver outsized losses to the short-vol cohort"
kill_criteria: |
  - drawdown > 25% from peak equity
  - 3 consecutive losing earnings cycles with losses > 2x expected per-trade loss
  - rolling 12-month average realized move > average implied move (edge sign flip)
related: ["[[earnings-iv-crush]]", "[[implied-earnings-move]]", "[[options]]", "[[implied-volatility]]", "[[iron-condors]]", "[[short-strangle]]", "[[straddle]]", "[[long-straddle]]", "[[volatility-trading]]", "[[earnings-calendar]]", "[[options-greeks]]", "[[vega]]", "[[theta]]", "[[gamma]]", "[[delta]]", "[[volatility-skew]]", "[[volatility-risk-premium]]", "[[probability-of-profit]]", "[[deflated-sharpe-ratio]]"]
---

Earnings volatility trading is a class of [[options]] strategies that takes a position on the magnitude of the post-earnings move relative to what [[implied-volatility]] is pricing. The two canonical flavors are **long volatility into earnings** (buying optionality in the run-up, hoping IV expansion outpaces [[theta]]) and **short volatility through earnings** (selling premium right before the print to harvest the [[earnings-iv-crush|IV crush]] that follows). The short-vol flavor is the more durable systematic trade; the long-vol flavor is generally a poor expected-value bet because the market has already priced the event move into the option. For the focused short-vol implementation (structures, screening filters, sizing), see [[earnings-iv-crush]]; for the market-implied move computation, see [[implied-earnings-move]].

The single number that governs every variant of this trade is the **[[implied-earnings-move|implied move]]** — the post-earnings displacement the option market is pricing, approximately the ATM straddle price (for the first expiry after the print) divided by spot. The whole trade reduces to a bet on whether the **realized move** will be larger or smaller than this implied move, after accounting for the [[earnings-iv-crush|volatility crush]] that mechanically deflates extrinsic value the moment uncertainty resolves.

| Dimension | Long-vol into earnings | Short-vol through earnings |
|---|---|---|
| Net [[vega]] | Long | Short |
| Net [[theta]] | Negative (paying decay) | Positive (collecting decay) |
| Wins when | Realized move >> implied move | Realized move < implied move |
| Crushed by | [[earnings-iv-crush|IV crush]] at the print | A genuine outlier print |
| Edge sign | Usually negative EV (priced in) | Positive EV with negative skew |
| Tail exposure | Capped loss (premium paid) | Severe left tail (unless wing-protected) |
| Systematic? | No — episodic, name-specific | Yes — diversifiable across many events |

## Edge Source

Earnings vol selling draws on **behavioral**, **structural**, and **risk-bearing** edges (see [[edge-taxonomy]]):

- **Behavioral** — Retail and discretionary traders systematically overpay for binary-event optionality, treating earnings as a "lottery ticket" event. Anchoring on prior outlier prints (e.g. an 18% gap) inflates demand for OTM puts and calls into the print.
- **Structural** — Equity options market makers must hedge their gamma through earnings; they price in a risk premium for the binary jump risk they cannot delta-hedge cleanly. That premium accrues to the patient short-vol seller.
- **Risk-bearing** — The short-vol seller is being paid to absorb left-tail outcomes. The edge is real but not free: it shows up as a positive mean with severe negative skew. This is the same family of risk premium that drives [[iron-condors]] and short [[straddle]]s in non-event contexts. (Source: [[2026-04-22-gap-finder-options-portfolios]])

## Why This Edge Exists

Around an earnings print, the options market quotes an "implied move" — roughly the price of the ATM straddle expiring shortly after the print, divided by the underlying. Across large universes of liquid single names, the **average realized move is smaller than the average implied move** by 5–20%, depending on regime and name. The other side of the trade is hedgers buying portfolio insurance against gap risk, and retail speculators buying cheap-looking OTM contracts that are not actually cheap when expressed in vol terms. They keep losing because they are paying a premium for convexity that, on average, the underlying does not deliver.

This is not a free lunch. The edge is a payment for bearing the rare-but-severe outlier print — a NFLX -35%, a META -25%, a SNAP -40%. On those events, the short-vol seller loses many cycles of accumulated profit in a single trade. Iron-condor wings cap the damage but also cap the upside; naked strangles maximize edge but expose the trader to ruin.

## Null Hypothesis

The null is that **realized move = implied move on average**, with no systematic premium for the seller. Under the null, a delta-neutral short straddle held from T-1 close to T+0 open earns zero net P&L before costs, and loses money after costs. To reject the null, the trader must demonstrate (with a [[deflated-sharpe-ratio]] or equivalent) that the average realized move is significantly below the average implied move across a representative universe and across a sufficient number of earnings cycles (typically several hundred).

## Rules

### Long-vol flavor (generally not recommended systematically)

- **Entry**: Buy ATM [[straddle]] or slightly-OTM [[long-straddle|strangle]] 2–4 weeks before earnings, when IV term structure is still relatively flat
- **Exit**: Close 1 day before earnings, before the front-month IV ramps fully
- **Thesis**: IV expansion outpaces theta decay
- **Reality**: Market makers anticipate this trade and price the IV ramp in advance. Net edge is usually negative after [[bid-ask-spread]] costs

### Short-vol flavor (the systematic trade)

- **Universe**: Liquid single names with options open interest > 10k contracts at the front-week, no FDA/legal/binary catalysts overlapping
- **Entry**: T-1 (last trading day before earnings), enter ~30–60 minutes before close to let the IV crush priced into the close work in your favor at fill
- **Structure**: Either short [[short-strangle|strangle]] at 1-SD strikes, or [[iron-condors|iron condor]] with shorts at 1 SD and longs ~50% wider
- **Exit**: T+0 (morning of the post-earnings trading day), within the first 30 minutes of cash open, after IV has collapsed
- **Position sizing**: 1–3% of buying power per single trade; max 15–20% of book in concurrent earnings positions across a single week to diversify away clustered surprises

## Implementation Pseudocode

```python
for ticker in earnings_universe:
    if not has_liquid_options(ticker, min_oi=10000):
        continue
    if has_overlapping_catalyst(ticker):
        continue

    earnings_date = get_earnings_date(ticker)
    if today != earnings_date - 1:
        continue

    iv_implied_move = atm_straddle_price(ticker, exp=earnings_date + 1) / spot(ticker)
    historical_realized = avg_abs_earnings_move(ticker, last_n=8)

    # Only sell when IV richly prices the event vs. realized history
    if iv_implied_move < 1.10 * historical_realized:
        continue  # not enough premium

    short_put = sell(ticker, "put", strike=spot * (1 - iv_implied_move))
    short_call = sell(ticker, "call", strike=spot * (1 + iv_implied_move))

    # Iron-condor wings cap tail risk
    long_put = buy(ticker, "put", strike=short_put.strike * 0.95)
    long_call = buy(ticker, "call", strike=short_call.strike * 1.05)

    size = 0.02 * buying_power / max_loss_of_condor()

# Next morning
for position in open_earnings_positions:
    close_at_market(position, time="open + 30min")
```

## Screening Filters (short-vol)

The short-vol flavor lives or dies on selection. The screen below promotes only names where the premium is rich relative to history and the structure is operationally clean. Each filter removes a known failure mode.

| Filter | Threshold (illustrative) | Why it matters |
|---|---|---|
| Front-week options open interest | > 10,000 contracts | Liquidity to exit at the cash open without paying a punitive [[bid-ask-spread]] |
| Implied / historical move ratio | > 1.10 | Only sell when the [[implied-earnings-move|implied move]] is at least 10% richer than the trailing realized average |
| Overlapping binary catalyst | None (no FDA, court ruling, M&A vote near the print) | A second catalyst breaks the single-event vol-crush thesis |
| Term-structure inversion | Front-week IV > back-month IV | Confirms the market is pricing a discrete event the crush will resolve |
| [[volatility-skew|Put skew]] | Not extreme | Heavy put skew flags a left-tail concern the short-vol seller is selling into |
| Recent outlier history | < 1 outlier (> 2x implied) in last 8 cycles | A name that routinely gaps double its implied move is a serial seller-killer |
| Earnings timing | Confirmed BMO/AMC on [[earnings-calendar]] | Avoids holding the wrong expiry or being caught off-cycle |

## Payoff and Greeks

The short-vol earnings structure is **short [[vega]], long [[theta]], short [[gamma]]** going into the print, and its P&L is dominated by two effects that fire simultaneously the instant earnings drop:

1. **The [[earnings-iv-crush|IV crush]] (vega P&L).** Front-week IV collapses from an event-elevated level (often 60–120%) to a post-event baseline (often 25–40%) the moment uncertainty resolves. For a net-short-vega book this is the primary source of profit and it is largely deterministic in *direction* — the crush happens whether the stock rises or falls.
2. **The realized move (gamma P&L).** The actual gap is a short-gamma exposure: a small move leaves the short strikes intact (keep the credit), a large move blows through them (losses accelerate quadratically). This is the source of the negative skew.

| Greek | Sign (short-vol pre-print) | Behavior through the event |
|---|---|---|
| [[delta]] | ~0 at entry (delta-neutral strikes) | Becomes sharply directional if the gap is large |
| [[gamma]] | Short | The source of outlier losses; magnitude scales with how far ITM the gap pushes a short strike |
| [[vega]] | Short | The source of the harvested premium via [[earnings-iv-crush|IV crush]] |
| [[theta]] | Long | Small contribution over a one-night hold; the crush dwarfs calendar theta |

The defined-risk [[iron-condors|iron condor]] wrapper truncates the short-gamma tail: beyond the long wing, gamma flips back to flat and the loss is capped at wing-width minus credit. The naked [[short-strangle|strangle]] leaves the short-gamma tail open, which is why it carries unbounded loss and is inappropriate for a finite-capital book.

The breakeven points of the structure are the short strikes ± the net credit. Because the strikes are placed at roughly the implied move (1 SD), the position is profitable whenever the realized move lands inside the implied move plus the credit cushion — which, when the implied/realized gap is positive, is the majority of the time. See [[probability-of-profit]] for the strike-selection metric.

## Indicators / Data Used

- [[earnings-calendar]] — confirmed report dates and BMO/AMC timing
- [[implied-volatility]] term structure — front-week vs. back-week IV ratio (a steeply inverted term structure flags the binary event)
- [[implied-earnings-move]] — the ATM straddle price as the market-implied move
- Historical realized post-earnings moves (8–16 prior cycles per ticker)
- [[earnings-iv-crush]] — the front-week IV level pre-print and the expected post-print baseline
- [[volatility-skew]] — heavy put skew can flag a left-tail concern the seller should respect
- [[options-greeks]] — net [[vega]], [[theta]], [[gamma]] exposure of the open book

## Example Trade

Stock XYZ, $100, reports earnings AMC tomorrow. Front-week ATM straddle priced at $5.00, implying a ~5% move. Last 8 earnings moves averaged 3.6% absolute. Trader sells:

- Sell $95 put @ $1.80
- Buy $90 put @ $0.70
- Sell $105 call @ $1.70
- Buy $110 call @ $0.60

Net credit: $2.20. Max loss: $5.00 width − $2.20 = $2.80. The next morning XYZ opens at $102 (a 2% move, well inside the short strikes). IV crushes from 80% to 30%. The condor is bought back for $0.40. Net profit: $1.80 per share over a single overnight hold. (Source: [[2026-04-22-gap-finder-options-portfolios]])

## Performance Characteristics

Academic and practitioner literature places the long-run Sharpe of disciplined short-earnings-vol strategies at roughly **0.5–1.0** net of costs, with several caveats:

- **Highly negative skew** — the return distribution has a long left tail. A handful of outlier prints per year deliver multi-sigma losses
- **Average win rate** ~65–75% — most cycles profit, but losing cycles can be 3–5x the average winner
- **Drawdown profile** — clustered earnings shocks (e.g. Q1 2022 large-cap tech) can produce 20–30% portfolio drawdowns within weeks
- **Cost sensitivity** — short single-name premium pays the [[bid-ask-spread]] on entry and exit on four legs; a strategy with 20+ bps round-trip cost per leg can erase the edge entirely

### Cost-aware illustration (NOT a backtest)

The numbers below are **illustrative arithmetic**, not the output of any backtest — they show how transaction cost stacks against the per-trade edge. They are not a claim about realized performance. The point is to demonstrate that the edge survives only when round-trip cost stays well under the harvested premium.

| Component | Per-trade value (illustrative) | Note |
|---|---|---|
| Gross credit captured (avg winner) | +$1.80 / share | The harvested [[earnings-iv-crush|crush]] when realized < implied |
| Avg loser (move blows through short strike) | −$2.80 / share | Capped at iron-condor wing width minus credit |
| Win rate | ~70% | Most cycles profit |
| Gross expected value | ≈ 0.70 × 1.80 − 0.30 × 2.80 = **+$0.42** | Before any cost |
| Round-trip cost (4 legs × 2 sides) | −$0.20 to −$0.40 | The [[bid-ask-spread]] paid eight times |
| **Net expected value** | **≈ +$0.02 to +$0.22** | The edge is thin and cost-fragile |

The lesson the arithmetic makes concrete: **the per-trade edge is small and the cost is large relative to it.** A trader paying the upper end of the cost band has essentially no edge; a trader with tight execution on liquid names keeps most of it. This is why the [[bid-ask-spread]] discipline and the open-interest screen are not optional — they are the difference between a positive-EV and a negative-EV book. No deflated-Sharpe significance is claimed here; see [[deflated-sharpe-ratio]] for the bar a real deployment must clear.

### Variant payoff comparison

| Structure | Max gain | Max loss | Net vega | Capital efficiency | When to use |
|---|---|---|---|---|---|
| Short [[straddle]] | Full credit | Unbounded | Very short | Poor (high margin) | Never for finite capital |
| Short [[short-strangle\|strangle]] | Full credit | Unbounded | Short | Poor (high margin) | Only for desks that can true-tail-hedge |
| [[iron-condors\|Iron condor]] | Net credit | Wing width − credit | Short | Good (defined risk) | The default systematic structure |
| Long [[straddle]] (long-vol) | Unbounded | Premium paid | Long | Moderate | Episodic, name-specific convexity bets only |
| Calendar / diagonal | Limited | Limited | Net long front-crush | Good | Plays the [[earnings-iv-crush\|term-structure crush]] directly |

## Capacity Limits

Capacity is **low to moderate**. Single-name options liquidity dominates the constraint — even on names like NVDA or AAPL, a position larger than a few hundred contracts per leg starts to push the [[bid-ask-spread]] and signal flow to market makers. A diversified earnings-vol book trading 30–50 names per quarter can scale to roughly **$5–10M** of risk capital before market impact and adverse selection meaningfully degrade the edge. Index-level vol selling (SPX, RUT) scales further but sits adjacent to this strategy, not within it.

## What Kills This Strategy

The strategy is most vulnerable to the failure modes catalogued in [[failure-modes]]:

1. **Regime shift** — Q1 2020 (Covid) earnings season produced realized moves 2–3x implied across most names; short-vol books were obliterated
2. **Clustered surprises** — When several mega-cap names beat or miss in the same week, the short-vol book compounds losses with no diversification to fall back on
3. **Market underpricing the implied move** — When dealer positioning is short gamma and the market chronically underprices event vol (rare but it happens), the edge inverts
4. **Crowding** — As more retail and quant capital piles into short earnings vol, the implied-vs-realized gap shrinks. Edge decay since the mid-2010s is documented (Source: [[2026-04-22-gap-finder-options-portfolios]])
5. **Operational error** — Mis-timed exits, wrong-week expirations, or holding through a halt can blow a position past the wing protection on an iron condor

## Kill Criteria

Retire (or pause and review — see [[when-to-retire-a-strategy]]) the book if **any** of:

- Drawdown exceeds 25% from peak equity
- 3 consecutive earnings cycles each lose more than 2x the expected per-trade loss
- Trailing 12-month average realized move exceeds average implied move across the universe (sign flip on the core edge)
- Per-trade [[breakeven-cost]] rises above 80 bps round-trip due to spread widening or slippage

## Advantages

- **Persistent edge** when sized and diversified — short-event-vol is one of the better-documented [[volatility-risk-premium]] expressions
- **Defined risk** when expressed as an [[iron-condors|iron condor]]
- **Short hold time** — typically <24 hours per position, capital recycles fast
- **Theta and vega both work for the seller** simultaneously across the IV crush
- **Diversifiable** across many uncorrelated single-name events per quarter

## Disadvantages

- **Severe negative skew** — small consistent gains, occasional catastrophic losses
- **Operationally intensive** — requires per-name research, an earnings calendar, and disciplined T-1/T+0 execution
- **Capacity constrained** — single-name options liquidity caps deployable capital
- **Costly** — four-legged spreads pay [[bid-ask-spread]] eight times per round trip
- **Crowding risk** — increasingly populated trade since the mid-2010s
- **Naked-strangle variant is unbounded-loss** — only iron-condor or wing-protected variants are appropriate for a finite-capital book

## Sources

- (Source: [[2026-04-22-gap-finder-options-portfolios]])
- Dubinsky, A., Johannes, M., Kaeck, A., & Seeger, N. (2019) — "Option Pricing of Earnings Announcement Risks", *Review of Financial Studies* — academic evidence that option-implied earnings moves systematically exceed realized moves on average. Verified via Perplexity (sonar), 2026-06-10.
- [[tastytrade]] — published practitioner studies on earnings short-premium win rates and expected value.

## Related

- [[earnings-iv-crush]] — the focused short-vol implementation page
- [[options]] — the instrument family
- [[implied-volatility]] — the input that drives the trade
- [[volatility-risk-premium]] — the broader edge category this trade expresses
- [[iron-condors]] — the defined-risk wrapper for the short-vol flavor
- [[short-strangle]] — the undefined-risk version
- [[straddle]], [[long-straddle]] — the long-vol flavor
- [[volatility-trading]] — the broader discipline
- [[earnings-calendar]] — the data feed that drives entry timing
- [[options-greeks]], [[vega]], [[theta]], [[gamma]] — the risk decomposition
- [[volatility-skew]] — the cross-strike pricing context
- [[probability-of-profit]] — strike-selection metric for premium sellers
