---
title: "Gap Trading (Crypto)"
type: strategy
created: 2026-06-30
updated: 2026-07-14
status: good
tags: [technical-analysis, day-trading, swing-trading, breakout, crypto]
aliases: ["gap trading", "CME gap", "CME gap fill", "weekend gap", "gap fill", "gap fade", "gap and go", "bitcoin gap"]
strategy_type: technical
timeframe: intraday|swing
markets: [crypto]
complexity: intermediate
backtest_status: untested

# Edge characterization
edge_source: [behavioral, structural, informational]
edge_mechanism: "When a lower-liquidity venue (CME futures over the weekend) closes while 24/7 spot keeps trading, price reopens at a distance from its prior close, leaving an untraded gap; that gap is a reference level clustered with resting orders and stops, and price is repeatedly drawn back to fill it (fade) unless a genuine catalyst carries it (continuation)."

# Data and infrastructure requirements
data_required: [ohlcv-intraday, ohlcv-daily, cme-futures-close, spot-price, funding-rates, open-interest, liquidations]
min_capital_usd: 2000
capacity_usd: 5000000
crowding_risk: medium

# Performance expectations (net of fees and slippage)
expected_sharpe: 0.4
expected_max_drawdown: 0.25
breakeven_cost_bps: 15

# Decay history
decay_evidence: "The 'BTC always fills the CME gap' folklore had a high historical fill rate (often quoted >90% eventually), but the reliable, quick fills of 2018-2020 have become less dependable as the pattern became consensus, weekend liquidity thinned further, and spot ETF flows shifted more BTC price discovery into US cash-equity hours. Gap fills now routinely take weeks and some large catalyst gaps have stayed open for months."

# Retirement conditions
kill_criteria: |
  - fill rate on classified weekend/CME gaps falls below the no-edge base rate over a 40-trade sample
  - fades repeatedly run over by catalyst gaps (classifier is broken)
  - realised open/reopen slippage consistently exceeds planned per-trade risk

related: ["[[breakout-trading]]", "[[opening-range-breakout]]", "[[fair-value-gaps]]", "[[support-and-resistance]]", "[[vwap]]", "[[volume]]", "[[trend]]", "[[mean-reversion]]", "[[atr]]", "[[liquidation]]", "[[funding-rate]]", "[[open-interest]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[cryptodataapi]]"]
---

# Gap Trading (Crypto)

**Gap trading** in crypto exploits the price gap that forms when a lower-liquidity venue reopens at a materially different level than its prior close, leaving an empty "gap" on the chart with no trading in between. Because crypto *spot* trades 24/7, the classic equity opening gap does not exist on the spot chart — but gaps are still a first-class crypto phenomenon in three specific places: the **CME Bitcoin/Ether futures gap** (CME closes Friday and reopens Sunday while spot never stops), the **weekend / low-liquidity range gap**, and the intrabar **fair value gap** left by a violent, one-sided move (a [[liquidation]] cascade or news spike). Traders take one of two opposing stances: **gap-and-go** (trade in the direction of the gap, betting the move continues on real information) or **gap fade / gap fill** (trade against it, betting price retraces to fill the gap back to the prior reference). Which stance is correct depends almost entirely on the *type* of gap and the [[volume]], [[funding-rate|funding]], and [[open-interest|OI]] context around it.

## Edge source

Mapping to the six categories in [[edge-taxonomy]], gap trading is a hybrid of three:

1. **Structural.** The CME futures contract mechanically stops trading from Friday ~22:00 UTC to Sunday ~23:00 UTC while Binance/Coinbase/Hyperliquid spot and perps trade the whole weekend. Any weekend move in spot re-prints on CME's Sunday reopen as a literal untraded gap. The gap boundary and the Friday close become reference levels that thousands of chart-watchers anchor to — a self-reinforcing structural artefact, not an opinion.
2. **Behavioural.** Weekend crypto liquidity is thin: market-maker inventory is smaller, US institutional desks are dark, and a single large order or a small [[liquidation]] pocket can push price a long way. Many weekend gaps are therefore *overreactions* that the deeper Monday US-hours book corrects — paying the fade trader who supplies liquidity against the weekend panic or euphoria.
3. **Informational.** A gap that forms on a genuine weekend catalyst (an exchange hack, a stablecoin depeg, a surprise macro or regulatory headline, a large on-chain move) reflects real new information the market is still digesting. That gap often *keeps going* in its direction — favouring continuation.

There is **no latency edge** for a discretionary trader, and the whole difficulty (and most of the losses) sit in correctly classifying the gap.

## Why this edge exists

Crypto never closes, but its *liquidity* is deeply uneven across the week. US cash-equity hours (13:30-20:00 UTC, Mon-Fri) concentrate the deepest books, spot-ETF creation/redemption flow, and macro reaction; weekends and the Asia-only hours are the thinnest. Two persistent tendencies create the opportunity:

- **Overreaction in thin books.** A weekend move on low volume is frequently an emotional or liquidity-driven dislocation. When the deep Monday book returns, the dislocation is often corrected — the gap fills. The popular "CME gap always fills" belief is the crowd's shorthand for this mean-reverting tendency.
- **Underreaction to genuine news.** A real catalyst gap (a hack, an ETF-approval leak, a hot CPI print that hits crypto through its equity correlation) often keeps running for hours or days as slower money repositions — favouring continuation.

The trader's job is to distinguish which regime they are in, using volume, the presence/absence of a hard catalyst, funding/OI context, and the gap's location relative to [[support-and-resistance]] and the prevailing [[trend]].

## Types of crypto gaps

| Gap type | Where it occurs | Typical behaviour | Bias |
|----------|-----------------|-------------------|------|
| **CME gap** | CME BTC/ETH futures Sunday reopen vs Friday close, after a weekend spot move | Statistically tends to fill, often within days | Fade / fill |
| **Weekend range gap** | Any venue's Monday repricing after a thin-liquidity weekend drift | Usually mean-reverts if no catalyst | Fade / fill |
| **Catalyst / breakaway gap** | Weekend or intrabar move on real news (hack, depeg, ETF, macro) + heavy volume | Starts or extends a trend; often does *not* fill soon | Continuation |
| **Liquidation-cascade candle (FVG)** | Intrabar vertical move that liquidates one side, leaving a [[fair-value-gaps|fair value gap]] | Imbalance often revisited, then trend resumes | Depends on context |
| **Exhaustion gap** | Late in an extended run, on climactic volume + funding blow-off | Marks a local top/bottom; tends to reverse | Fade |

The single most useful tells are **volume** and **derivatives context**: a breakaway/continuation gap is validated by real spot volume and a *sustained* OI build, while a low-volume, no-news gap into resistance is a fill candidate. A gap created purely by a funding-driven perp squeeze (spot barely moved) is especially prone to reverting.

## Null hypothesis

Under a random walk with no information content, a gap has no directional edge: continuation and fill are roughly equally likely and, after fees and weekend spreads, expectancy is negative. The observed, exploitable behaviour is regime-dependent — thin-liquidity no-news gaps fill more often than chance, while high-volume catalyst gaps continue more often than chance. A backtest showing a *single* blanket rule ("always fill the CME gap" or "always chase the gap") with a high win rate across all gap types is almost certainly overfit and survivorship-biased toward the 2018-2021 sample; the edge lives in the *classification*, not in a blanket direction. If your classified-setup win rate collapses to the no-edge base rate over a meaningful sample, the regime (or the classifier) has changed.

## Rules

### Gap fill / fade (the mean-reversion side — the classic CME/weekend play)

- **Setup:** BTC or ETH prints a weekend or CME-reopen gap on unremarkable spot volume, *no* hard catalyst, into or away from an established [[support-and-resistance]] level. Funding is not extreme in the gap's direction.
- **Entry:** Fade once momentum stalls (failure to extend, a rejection candle, loss of [[vwap]]), targeting the prior reference (the unfilled gap edge / Friday close).
- **Stop:** Beyond the gap's far extreme, with a buffer for crypto wick noise (use a % or [[atr]] multiple, never a fixed tick). Gaps that *don't* fill can run hard.
- **Target:** The gap-fill level (full fill) or its midpoint (partial). Scale out; do not marry the fade.

### Gap-and-go (continuation)

- **Setup:** Gap on a real catalyst and heavy spot volume, breaking out of a base or through major structure, with OI building in the gap's direction (fresh positioning, not just short covering).
- **Entry:** Buy/sell a break of the post-gap opening range (e.g. the first 15-60 min of US-hours trade) or a hold beyond the gap level and [[vwap]].
- **Stop:** Back inside the gap or below [[vwap]] / the opening range — whichever defines invalidation.
- **Target:** Trail with [[atr]] or prior swing structure; catalyst gaps can trend for days.

**Sizing (both):** risk a fixed small percentage of capital per trade; let the defined gap structure set the [[stop-loss]] distance. In crypto, cap leverage hard — a wide gap plus perp leverage is how accounts die on the reopen.

## Implementation pseudocode

```python
# Crypto gap classifier + router (illustrative; not investment advice)
def classify_crypto_gap(gap, ctx):
    # gap.pct = (reopen_or_current - prior_reference) / prior_reference
    if abs(gap.pct) < 0.005:                      # < 0.5% — too small to matter
        return "no_trade"

    strong_vol   = ctx.spot_volume_z > 1.5        # spot volume z-score vs 30d
    oi_building  = ctx.oi_change_z  > 1.0         # fresh positioning, not just squeeze
    has_catalyst = ctx.catalyst                   # hack / depeg / ETF / macro headline
    into_level   = ctx.location == "into_sr"      # gap runs into prior S/R

    # continuation: real news + real volume + fresh OI, breaking structure
    if has_catalyst and strong_vol and oi_building and ctx.location == "breakout":
        return "gap_and_go"

    # fill/fade: no news, thin weekend/CME gap, stalling into resistance
    if (not has_catalyst) and (not strong_vol) and into_level:
        return "gap_fade"

    return "wait"                                 # ambiguous -> stand aside

# Execution keys off the US-hours opening range and VWAP:
#   gap_and_go -> trade the ORB break, stop back inside gap / under VWAP, trail
#   gap_fade   -> fade the failure, target the unfilled gap edge (the fill)
```

The real bot wraps this with a weekend-liquidity guard (skip if depth at ±25 bps is below a threshold), a funding filter (do not fade a gap that funding is actively pushing), and a hard leverage cap.

## Indicators / data used

- **CME Friday close vs Sunday reopen** — defines the CME gap (measured off CME/TradingView; the *fill* plays out on spot, which CryptoDataAPI serves).
- **Prior reference and gap boundaries** — the untraded zone and its proximal/distal edges.
- **Spot [[volume]] vs 30-day average** — the primary filter separating catalyst gaps from noise.
- **[[open-interest]] and [[funding-rate]]** — is the gap fresh positioning (continuation) or a leverage/squeeze artefact (fade)?
- **[[liquidation]] clusters** — where forced-order pockets sit around the gap; the fuel for both the spike and the snap-back.
- **US-hours opening range + [[vwap]]** — intraday trigger and line-in-the-sand for the continuation side.
- **[[atr]]** — stop/target sizing and the buffer against wick noise.

## Example trade

**Setup (illustrative, BTC/USDT):** BTC closes CME futures on Friday at **$62,400**. Over a quiet weekend with no catalyst, thin books drift spot down to **$60,800** by Sunday. CME reopens Sunday 23:00 UTC and prints a **down gap** from $62,400 to ~$60,900 — an unfilled CME gap at **$60,900-$62,400**. Weekend volume was below average; funding is mildly positive but not extreme; OI actually *fell* over the weekend (deleveraging, not fresh shorting).

**Read:** no catalyst + weak volume + falling OI = **fade toward the fill**, not a breakaway.

1. Into Monday US hours, BTC bases at $61,000 and reclaims [[vwap]]. Enter long at **$61,050**.
2. Stop below the weekend low with a buffer: **$60,300** (risk ~$750, ~1.2%).
3. Target the top of the gap (Friday close / fill) at **$62,400**.
4. Deeper US-hours liquidity lifts BTC back through the gap; it fills at $62,400 on Monday afternoon. Scale 50% at $62,000, exit the rest at **$62,400**.

**Result:** avg exit ~$62,250 vs entry $61,050 on ~$750 risk — roughly **1.6:1**. (Illustrative scenario, not a recorded trade.) Contrast the fade with a *catalyst* gap: if the same down move had been driven by a Sunday exchange-hack headline on rising volume and building short OI, the correct trade is gap-and-go *short* on the breakdown, not a fade into a falling knife.

## Performance characteristics

Gap trading in crypto is a discretionary, regime-dependent edge, not a high-Sharpe systematic one. Realistic picture:

| Metric | Value | Note |
|---|---|---|
| Net Sharpe (target) | ~0.4 | Entirely dependent on correct classification; negative if the classifier is broken. |
| Win rate (classified fills) | 55-70% | Weekend/CME fills historically high, but decaying and slow. |
| Max drawdown | 20-25% | Driven by fading catalyst gaps that never fill (the dominant loss mode). |
| Payoff | Fades: modest, high-hit-rate; continuations: fewer, larger winners. | Mixing the two books smooths the curve. |
| Breakeven cost budget | ~15 bps round trip | Spot taker ~5-10 bps/side plus weekend spread widening. |

The "fill rate" folklore is real but overstated and slow: a gap that eventually fills months later is worthless to a swing trader with a stop. Treat published >90% fill statistics as *eventual*, survivorship-biased, and decaying.

## Capacity limits

High relative to the strategy's frequency, bounded by weekend book depth. On BTC and ETH majors, an individual operator can work **$100k-$5M** per gap before their own fills move the thin weekend/reopen book. On smaller alts, capacity collapses to tens of thousands because the same book thinness that *creates* the gap also punishes size. The binding constraint is not AUM but the **low frequency** of clean, classifiable gaps — a handful of high-quality CME/weekend gaps per month.

## What kills this strategy

Mapped to [[failure-modes]]:

1. **Misclassification (dominant loss mode).** Fading a catalyst/breakaway gap that keeps running — e.g. shorting the fill during an exchange-insolvency weekend — is how the whole year's edge is given back in one trade.
2. **"Gaps always fill" myth.** Strong catalyst gaps can take months to fill or never do. A fade with a loose stop courts open-ended loss ([[failure-modes|tail realised]]).
3. **Weekend liquidity traps / stop-hunts (crypto-acute).** Thin weekend books make it cheap for a large player to spike *through* the obvious gap edge, trip stops and a [[liquidation]] pocket, then reverse — punishing tight stops placed at the visually obvious level.
4. **Liquidation cascades.** A gap that coincides with a cascade can extend far beyond any reasonable fade target before reverting; leverage on the fade leg is fatal.
5. **Crowding.** The CME-gap play is consensus; enough traders now front-run the fill that quick, clean fills have become less reliable ([[failure-modes|edge got crowded out]]).
6. **Regime change.** Post-ETF, more BTC price discovery happens in US cash-equity hours, weakening the weekend-gap mean-reversion the strategy relied on.

## Kill criteria

Pause or revise if: the win rate on *classified* setups deteriorates to the no-edge base rate over a 40-trade sample; fades are repeatedly stopped out by non-filling catalyst gaps (the classifier is broken); or realised reopen/weekend slippage consistently exceeds the planned per-trade risk. See [[when-to-retire-a-strategy]].

## Advantages

- Catalysts and session/venue transitions concentrate opportunity into predictable, well-defined moments (the CME reopen, the Monday US open).
- Clear structural reference points — the gap edges, the prior close, [[vwap]], the opening range — make stops and targets objective.
- Works on both intraday and swing horizons and pairs naturally with [[breakout-trading]] and [[fair-value-gaps|FVG]] logic.
- Low data requirement: OHLCV, a volume filter, and basic derivatives context.

## Disadvantages

- Requires accurate gap classification and disciplined execution; unforgiving of hesitation.
- The "gaps always fill" myth lures beginners into fading strong catalyst moves — a classic blow-up, and worse in leveraged crypto.
- Low frequency of clean setups makes statistical validation slow.
- Weekend/reopen liquidity is thin and slippage-prone; leverage magnifies the tail.
- Crowded and decaying as an edge, especially the CME-gap variant.

## Getting the Data (CryptoDataAPI)

Gap trading needs price structure to locate the gap and its fill target, depth to judge weekend liquidity, and derivatives/liquidation context to tell a catalyst gap from a squeeze artefact. See [[cryptodataapi-market-data]], [[cryptodataapi-derivatives]], and [[cryptodataapi-market-intelligence]].

**Live data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1h&limit=500` — spot OHLCV to mark the gap zone and watch the fill.
- `GET /api/v1/liquidity/depth/BTC` — 24h rolling depth/spread; flags thin weekend books that fake breakouts.
- `GET /api/v1/derivatives/open-interest?coin=BTC` — is the gap fresh positioning (OI building) or deleveraging (OI falling)?
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — funding extremes warn against fading a leverage-driven gap.
- `GET /api/v1/market-intelligence/liquidations` — cross-exchange forced-order clusters around the gap.

**Historical data (backtest fill rates and classify gaps):**
- `GET /api/v1/backtesting/klines` — full spot archive from 2020 for systematic weekend/CME-gap testing.
- `GET /api/v1/backtesting/liquidations` — historical liquidation records to tag cascade-driven gaps.

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=1h&limit=500"
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/derivatives/open-interest?coin=BTC"
```

Note: CryptoDataAPI serves Binance spot and crypto derivatives; the CME futures Friday close that *defines* the CME gap comes from CME/TradingView, but the gap's fill plays out on the spot series above. Auth: `X-API-Key` header.

## Related

- [[fair-value-gaps]] — the intrabar imbalance version of a gap, central to the liquidation-cascade case.
- [[breakout-trading]] / [[opening-range-breakout]] — gap-and-go is a breakout off the post-gap range.
- [[support-and-resistance]] / [[trend]] — context that decides fade vs follow.
- [[vwap]] — the intraday reference line for gap setups.
- [[volume]] — the primary filter separating real gaps from noise.
- [[mean-reversion]] — the logic behind the gap-fill side.
- [[liquidation]] / [[funding-rate]] / [[open-interest]] — the crypto derivatives context that classifies a gap.
- [[edge-taxonomy]] — where this strategy sits among the edge categories.
- [[failure-modes]] — the catalog this strategy's kill criteria draw from.

## Sources

- Murphy, John J. *Technical Analysis of the Financial Markets* — classification of common, breakaway, runaway, and exhaustion gaps (the taxonomy adapted here for crypto).
- Bulkowski, T. *Encyclopedia of Chart Patterns* — empirical study of gap behaviour and fill tendencies in traditional markets.
- CME Group Bitcoin/Ether futures contract specifications — trading hours and the Friday-close/Sunday-reopen mechanism that creates the CME gap.
- Public exchange documentation (Binance, Coinbase, Hyperliquid) — 24/7 spot/perp trading and weekend liquidity behaviour.
