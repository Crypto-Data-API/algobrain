---
title: "Bitcoin Halving Cycle Timing"
type: strategy
created: 2026-07-14
updated: 2026-07-14
status: good
tags: [position-trading, fundamental-analysis, crypto, bitcoin, on-chain, valuation, market-regime]
aliases: ["Halving Cycle Timing", "BTC Cycle Timing", "On-Chain Cycle Timing", "MVRV Cycle Strategy", "Halving Position Trade"]
strategy_type: hybrid
timeframe: long-term
markets: [crypto]
complexity: intermediate
backtest_status: naive-backtested

# Edge characterization
edge_source: [analytical, behavioral, structural]
edge_mechanism: "On-chain cost-basis metrics (MVRV, MVRV-Z, NUPL, realized-price bands) reveal the aggregate unrealized profit/loss of all Bitcoin holders; extremes in that gauge — heavy unrealized profit near cycle tops, deep unrealized loss near bottoms — front-run the distribution and capitulation that recency-biased holders execute late, and the halving supply-issuance clock provides a coarse timing overlay for when those extremes historically cluster."

# Data and infrastructure requirements
data_required: [mvrv, mvrv-z-score, nupl, realized-price, halving-calendar, btc-price-history]
min_capital_usd: 1000
capacity_usd: 1000000000
crowding_risk: medium

# Performance expectations (long-horizon, net of tax and timing error)
expected_sharpe: 0.7
expected_max_drawdown: 0.35
breakeven_cost_bps: 50

# Decay history
decay_evidence: "Cycle amplitude has compressed each cycle: the MVRV-Z score that marked the top fell from ~7 (2017) to ~5 (2021), and NUPL euphoria peaks have declined; spot-ETF demand-side flows since 2024 have blunted the sharp, halving-timed tops/bottoms of the 2013/2017/2021 template. The zones still work directionally but the numeric thresholds drift lower and the timing widens each cycle (Source: [[bitcoin-cycle-regime]])."

# Lifecycle (naive-backtested; not deployed)
capital_allocation: "long-horizon core sleeve; accumulate in capitulation zone, distribute in euphoria zone, DCA-scaled"
kill_criteria: |
  - MVRV-Z zone thresholds fail to mark a top/bottom for a full cycle (template break)
  - realized-price support decisively lost with on-chain health collapsing (structural bear)
  - concentration/position exceeds long-horizon risk budget
  - a credible protocol-level or regulatory event invalidates the 4-year supply cycle
last_review: 2026-07-14
next_review: 2026-10-14

related: ["[[mvrv]]", "[[mvrv-z-score]]", "[[nupl]]", "[[realized-price]]", "[[bitcoin-halving]]", "[[sopr]]", "[[bitcoin-cycle-regime]]", "[[market-cycle]]", "[[on-chain-analysis]]", "[[on-chain-regime]]", "[[dollar-cost-averaging]]", "[[buy-and-hold]]", "[[miner-capitulation-bottom]]", "[[position-sizing]]", "[[bitcoin]]", "[[btc-dominance]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi-on-chain]]", "[[cryptodataapi]]"]
---

# Bitcoin Halving Cycle Timing

Bitcoin Halving Cycle Timing is a **long-horizon position strategy** that uses on-chain valuation to identify cycle accumulation (bottom) and distribution (top) zones, overlaid on the [[bitcoin-halving|halving]] supply-issuance clock. It reads the aggregate cost-basis metrics — [[mvrv|MVRV]], [[mvrv-z-score|MVRV-Z]], [[nupl|NUPL]], and [[realized-price|realized-price]] bands — to gauge whether the average holder sits on heavy unrealized profit (distribution risk) or deep unrealized loss (accumulation opportunity), and times exposure using months-since-halving as a coarse overlay. The trade is not a short-term signal: it accumulates BTC spot in capitulation zones, holds through the cycle, and distributes into euphoria zones, sizing positions to a multi-year risk budget rather than to price momentum.

Unlike the reflexive, high-frequency crypto strategies elsewhere in this wiki, this is a **patient, valuation-anchored** approach. Its edge is in acting against the recency bias of the crowd at cycle extremes — and its central risk is that the 4-year cycle template, already softening, breaks under spot-ETF-era demand dynamics.

## Edge Source

Per [[edge-taxonomy]], three edges combine:

- **Analytical (primary).** [[mvrv|MVRV]] and its cousins convert opaque holder behaviour into a quantified over/undervaluation oscillator. Realized cap values every coin at the price it last moved (its aggregate on-chain cost basis); the market/realized ratio measures aggregate unrealized profit. Extremes in that gauge have historically bounded cycle tops and bottoms *before* price confirmed — an analytical edge from a data source (on-chain) that has no equity equivalent.
- **Behavioral.** The metrics work *because* the crowd is recency-biased: holders extrapolate recent price, buy euphorically near tops (when MVRV/NUPL scream overvaluation) and capitulate near bottoms (when the average holder is underwater and NUPL is negative). The strategy is the disciplined counter-party to that late, emotional flow — accumulating when [[nupl|NUPL]] is in capitulation and distributing when it is in euphoria.
- **Structural.** The [[bitcoin-halving|halving]] mechanically halves new issuance every ~210,000 blocks (~4 years), a scheduled, credibly-committed supply shock. The shock is *gradual* — it builds over the 6-18 months after the date, not on the date — but it provides a structural timing prior for when the demand-vs-issuance imbalance historically tightened into a top.

The edge is **not** latency or informational-in-the-fast-sense — these are daily/weekly metrics visible to everyone on Glassnode, CryptoQuant, and [[cryptodataapi-on-chain|CryptoDataAPI]]. The edge is the *temperament* to act on valuation extremes against the tape, on a multi-year horizon.

## Why This Edge Exists

1. **On-chain cost basis is a genuinely informative valuation anchor.** Because Bitcoin's ledger is public, the aggregate cost basis of the entire supply is computable ([[realized-price]]). No other asset exposes this. When market price is 3-4× the realized price ([[mvrv|MVRV]] ~3-4), the average holder sits on large unrealized gains and distribution pressure builds; when price falls below realized price (MVRV < 1), the average holder is underwater — historically an accumulation zone. This is a structural information advantage, not a behavioural anomaly.
2. **Recency bias is durable.** Retail (and much of institutional) crypto demand is performance-chasing: inflows and euphoria peak *after* large price gains, capitulation peaks *after* large losses. This lag is why valuation extremes lead the crowd's action — the metrics flag "overvalued" while money is still pouring in.
3. **The supply schedule is credibly fixed.** Unlike discretionary monetary policy, Bitcoin's issuance is protocol-enforced and known years ahead. The halving is not a surprise, but its *demand-side reflexivity* (narrative, miner economics, media attention) has repeatedly turned a scheduled supply cut into a multi-quarter momentum regime.

## Null Hypothesis

Under no-edge conditions, on-chain valuation metrics carry no forward information beyond price itself (they are, after all, derived from price and supply), and the halving is fully priced the instant it is scheduled. In that world:

- MVRV/NUPL extremes would not lead tops/bottoms — they would coincide with them, useless for timing.
- Accumulating at low MVRV-Z and distributing at high MVRV-Z would not beat simple [[buy-and-hold]] or [[dollar-cost-averaging|DCA]] after costs and tax.
- Months-since-halving would have no relationship to forward returns.

Empirically, across 2013/2017/2021, MVRV-Z extremes *did* bound the cycle turns and a zone-based accumulate/distribute rule outperformed naive buy-and-hold on a risk-adjusted basis — **but** the sample is only three completed cycles, the thresholds drifted lower each time, and the halving-to-top lag varied (roughly 12-18 months). The null is **not** cleanly rejected going forward: with only ~3 cycles and a structurally changing demand base (spot ETFs), the timing edge is a *prior*, not a law. The strategy explicitly treats the zones as probabilistic and never bets the whole book on the cycle repeating.

## Rules

### Zone definitions (accumulation vs distribution)

Read the composite of four metrics; act when they *agree*, not on any single one:

| Zone | [[mvrv-z-score\|MVRV-Z]] | [[mvrv\|MVRV]] | [[nupl\|NUPL]] | Price vs [[realized-price]] | Action |
|---|---|---|---|---|---|
| **Deep capitulation** | < 0 | < 1.0 (~0.7-0.85 lows) | < 0 (capitulation) | below realized price | Accumulate aggressively |
| **Accumulation** | 0 to ~2 | 1.0-1.5 | 0-0.25 (hope/fear) | at/near realized price | Accumulate / DCA |
| **Neutral / hold** | ~2 to ~4 | 1.5-2.5 | 0.25-0.5 (optimism) | above realized price | Hold; no new adds |
| **Distribution** | ~4 to ~6 | 2.5-3.5 | 0.5-0.75 (belief/greed) | far above realized | Begin scaling out |
| **Euphoria** | > ~5-6 (cycle-declining) | > 3.5 | > 0.75 (euphoria) | extreme premium | Distribute aggressively |

Thresholds drift **lower each cycle** — use the *percentile within the current cycle's range* and the *agreement of the four metrics*, not fixed lines (Source: [[mvrv]] cross-cycle-drift caveat; [[bitcoin-cycle-regime]]).

### Halving overlay (timing prior)

- **Pre-halving (~60-90 days before):** modest accumulation bias; the supply cut approaches.
- **Post-halving (0-6 months):** neutral — the supply shock builds slowly; do **not** treat the halving date as a price trigger.
- **6-18 months post-halving:** the historical window in which euphoria zones (cycle tops) have clustered — tighten distribution discipline as valuation metrics enter the distribution/euphoria bands.
- **~12-15 months before the next halving:** the historical window for capitulation bottoms — lean into accumulation when valuation confirms.

### Sizing (long-horizon)

- **Core + tactical split:** a long-horizon core BTC holding, plus a tactical sleeve that scales with the valuation zone (larger in capitulation, trimmed toward zero in euphoria).
- **Zone-scaled DCA:** buy on a schedule, but *scale the buy size inversely to MVRV-Z* — bigger buys deep in capitulation, smaller (or none) in distribution. Distribute symmetrically into euphoria.
- **Risk budget, not conviction:** cap the tactical sleeve so a full cycle drawdown (BTC −70-80% peak-to-trough is normal) does not breach the operator's multi-year risk tolerance. See [[position-sizing]].
- **No leverage on the core.** Cycle drawdowns are deep and long; leverage converts a survivable hold into a liquidation. (A separately-risk-budgeted perp overlay is possible but is a different trade.)

### Exit / distribution

- Scale out across the distribution and euphoria zones (do not try to nail the top); realize into strength as MVRV-Z and NUPL enter historical distribution bands.
- Retain the long-horizon core through the cycle unless the *structural* thesis breaks (realized-price support decisively lost with on-chain health collapsing — see Kill Criteria).

## Implementation Pseudocode

```python
# btc_halving_cycle_timing.py — long-horizon on-chain zone accumulate/distribute
# Status: naive-backtested (3 cycles). Metrics from CryptoDataAPI on-chain endpoints.

def cycle_zone(m):
    # m: dict of current on-chain metrics (percentile-within-cycle preferred over fixed lines)
    if m.mvrv_z < 0 and m.nupl < 0:            return "DEEP_CAPITULATION"
    if m.mvrv_z < 2 and m.nupl < 0.25:         return "ACCUMULATION"
    if m.mvrv_z < 4 and m.nupl < 0.5:          return "NEUTRAL"
    if m.mvrv_z < 5.5 and m.nupl < 0.75:       return "DISTRIBUTION"
    return "EUPHORIA"

def halving_bias(months_since_halving):
    if months_since_halving < 0:               return "PRE_HALVING_ACCUM"    # <0 = before
    if months_since_halving <= 6:              return "POST_HALVING_NEUTRAL"
    if 6 < months_since_halving <= 18:         return "TOP_WINDOW"
    return "BOTTOM_WINDOW"                       # deep into cycle, next halving nearing

def monthly_action(book, m, months_since_halving, nav):
    zone = cycle_zone(m)
    bias = halving_bias(months_since_halving)
    # size scalar: inverse to valuation, amplified in the corroborating halving window
    scale = {"DEEP_CAPITULATION": 1.5, "ACCUMULATION": 1.0,
             "NEUTRAL": 0.0, "DISTRIBUTION": -1.0, "EUPHORIA": -1.5}[zone]
    if zone in ("DEEP_CAPITULATION", "ACCUMULATION") and bias == "BOTTOM_WINDOW":
        scale *= 1.25   # valuation + timing agree -> lean in
    if zone in ("DISTRIBUTION", "EUPHORIA") and bias == "TOP_WINDOW":
        scale *= 1.25   # valuation + timing agree -> distribute harder

    base = 0.02 * nav   # 2% NAV base DCA clip
    if scale > 0:
        return buy_spot("BTC", notional=min(scale, 1.5) * base)
    if scale < 0:
        return sell_spot("BTC", notional=min(-scale, 1.5) * base * book.tactical_frac)
    return hold("neutral zone")

def structural_kill(m):
    # retain core unless the cycle thesis itself breaks
    return (m.price < m.realized_price and m.onchain_health < 30
            and m.realized_price_trend_down)
```

## Indicators / Data Used

- **[[mvrv|MVRV]] and [[mvrv-z-score|MVRV-Z]]** — the core over/undervaluation oscillator; MVRV-Z standardises MVRV to flag statistical extremes across cycles.
- **[[nupl|NUPL]]** — net unrealized profit/loss as a % of market cap; its named bands (capitulation → hope/fear → optimism → belief/greed → euphoria) map directly to the zone table.
- **[[realized-price]]** — the aggregate cost-basis "floor"; support in uptrends, resistance in downtrends, and the reference for the deep-capitulation zone.
- **[[bitcoin-halving|Halving calendar]] / months-since-halving** — the timing overlay (halvings: 2012, 2016, 2020, 2024; next ~2028).
- **On-Chain Health composite** — corroborating breadth of on-chain metrics; the structural-kill input.
- **[[sopr|SOPR]]** — confirms whether coins are actually being spent at profit/loss (are paper gains being realized?).
- **[[on-chain-regime]] miner signals / hash ribbon** — miner capitulation historically clusters near cycle bottoms (see [[miner-capitulation-bottom]]).
- **200-day MA / price history** — coarse trend context for the zone reads.

## Example Trade

**Accumulation (illustrative, deep-capitulation zone).** BTC has fallen ~75% from its prior cycle high; price sits *below* [[realized-price|realized price]], [[mvrv|MVRV]] ~0.8 (average holder underwater), [[mvrv-z-score|MVRV-Z]] slightly negative, [[nupl|NUPL]] < 0 (capitulation band). Months-since-halving places the market in the historical bottom window (~12-15 months before the next halving). All four metrics agree on "deep capitulation."

- **Action:** accumulate aggressively — zone scalar 1.5, amplified ×1.25 by the corroborating halving-timing window → the largest DCA clips of the cycle. No leverage; spot only.
- **Rationale:** the average holder is underwater and capitulating; realized-price is historically a durable accumulation floor; the supply cut is approaching. The trade accepts that price may fall further near-term (metrics bound risk, not exact bottoms) and sizes so a further −20% is comfortably held.

**Distribution (illustrative, euphoria zone).** ~15 months post-halving, price is far above realized price, MVRV ~3.5+, MVRV-Z in the cycle's distribution band, NUPL > 0.75 (euphoria), retail inflows and media attention peaking.

- **Action:** distribute the tactical sleeve into strength across the distribution and euphoria zones — scaling *out* rather than trying to pick the exact top. Retain the long-horizon core.
- **Rationale:** aggregate unrealized profit is extreme, distribution pressure is building, and the crowd is buying late. Realizing into euphoria monetises the valuation edge; the retained core preserves upside if the cycle extends.

**Cross-cycle caveat (why this is *timing*, not a formula):** the MVRV-Z that marked the 2017 top (~7) was not reached in 2021 (~5); a strategy waiting for the 2017 number would have failed to distribute in 2021. Always read *percentile-within-the-current-cycle* and metric *agreement*, and expect thresholds to keep drifting lower as ETFs blunt the amplitude ([[bitcoin-cycle-regime]]).

## Performance Characteristics

Realistic, long-horizon picture (naive-backtested across 3 cycles; treat with heavy caution — small sample):

| Metric | Estimate | Note |
|---|---|---|
| Risk-adjusted return vs buy-and-hold | Modestly higher Sharpe (~0.7 vs ~0.5) | From distributing euphoria and accumulating capitulation; the *timing* trims drawdown |
| Max drawdown (with tactical trimming) | 35-50% | Still deep — this is BTC; trimming softens but does not remove cycle drawdowns |
| Trade frequency | Very low (monthly DCA + a handful of distribution events per cycle) | Transaction cost is a minor factor |
| Holding period | Years | The core is multi-year; the tactical sleeve turns once per cycle |
| Correlation to BTC | High (directional long) | This is a long-biased BTC book, not market-neutral |

**Cost overlay — dominated by tax and timing error, not transaction cost:**

| Friction | Magnitude | Note |
|---|---|---|
| Spot fees | 4-10 bps per clip, infrequent | Negligible on a multi-year horizon |
| Slippage | 1-5 bps on BTC at moderate size | Small for BTC even at large size |
| Borrow/funding | Zero (spot, no leverage) | If a perp overlay is used, funding applies — but the core is unlevered |
| **Tax on distribution** | **Large** | Realizing into euphoria triggers capital-gains events; in AU, holding > 12 months halves the CGT — so distribution timing has a *tax* dimension, not just a price one |
| **Timing error** | **The real cost** | Zones bound risk, not exact turns; entering/exiting a few weeks early or late is the dominant P&L driver, dwarfing fees |

The honest framing: this strategy's cost is not the exchange fee — it is **timing error and tax**. The `breakeven_cost_bps: 50` budget is trivially met on transaction cost; the strategy lives or dies on whether the zones keep bounding the cycle and on after-tax realized returns.

## Capacity Limits

- Very high capacity — the trade is long-horizon BTC spot accumulation/distribution in the deepest crypto market. An operator can deploy **hundreds of millions to low billions** with patient execution (VWAP over days) without materially moving price; reflected in `capacity_usd: 1000000000`.
- The binding constraint is not liquidity but **crowding of the signal**: MVRV/NUPL/realized-price are among the most-watched on-chain metrics; if enough capital distributes at the same euphoria threshold, the top flattens and the zone self-defeats (part of the amplitude-compression story).
- Scaling further requires patient, staggered execution across the accumulation/distribution *windows* (weeks-to-months), not point-in-time trades — which suits the strategy's horizon anyway.

## What Kills This Strategy

Mapped to [[failure-modes]]:

1. **Cycle-template break (Failure Mode #5: The Regime Changed).** The dominant risk. Spot-ETF demand flows, institutional custody, and market maturation are **already** blunting the sharp, halving-timed tops/bottoms of 2013/2017/2021 ([[bitcoin-cycle-regime]]). If the 4-year cycle dissolves into a smoother, flow-driven regime, the zone thresholds and halving overlay lose their timing power.
2. **Threshold drift outrunning the model (Failure Mode #4: crowding / over-fit).** Each cycle's top has printed at a *lower* MVRV-Z; a strategy anchored to prior-cycle numbers distributes too late (or never). Using percentile-within-cycle mitigates but does not eliminate this.
3. **Lost/dormant-supply distortion.** Realized cap (the denominator of MVRV) is biased by provably-lost and ancient dormant coins, inflating MVRV and shifting the zones ([[mvrv]] caveats). Entity-adjusted variants help but are provider-produced and revised.
4. **Structural bear / realized-price break (Failure Mode #6).** In a genuine structural bear, price stays below realized price for an extended period and on-chain health collapses — accumulation "into the zone" bleeds for months (2018, 2022). The structural-kill guards this.
5. **Small-sample over-confidence.** Three cycles is a tiny sample; the apparent regularity may be partly luck. The strategy must be sized as if the cycle *might not repeat*.
6. **Behavioral risk (operator).** Distributing into euphoria and buying capitulation is psychologically brutal; the dominant real-world failure is the operator overriding the model at exactly the extremes it is designed for.

## Kill Criteria

Paused or re-scoped on any of:

1. **MVRV-Z zone thresholds fail to mark a top or bottom for a full cycle** → the template has broken; suspend the tactical timing and revert to plain [[dollar-cost-averaging|DCA]].
2. **Realized-price support decisively lost with On-Chain Health composite collapsing (< 30) and trending down** → structural bear; halt accumulation, protect capital.
3. **Tactical sleeve or total position exceeds the multi-year risk budget** → trim to budget (a −80% cycle drawdown must remain survivable).
4. **A credible protocol-level or regulatory event invalidates the 4-year supply cycle** → re-scope the whole thesis.
5. **Metric-provider methodology change** materially shifts the historical zones → re-baseline before acting.

Re-engage: zones and halving overlay realign with a completed cycle turn, and on-chain health recovers above mid-range. See [[when-to-retire-a-strategy]].

## Advantages

- **Valuation-anchored, not momentum-chasing** — acts against the crowd at extremes rather than with it.
- **Uses data no other asset class has** — the public ledger makes aggregate cost basis ([[realized-price]], [[mvrv|MVRV]]) computable; a genuine analytical edge.
- **Low operational burden** — monthly cadence, few trades, no infrastructure or latency requirements; accessible from $1k.
- **Drawdown-softening** — distributing euphoria and accumulating capitulation trims (not eliminates) the brutal BTC cycle drawdown versus naive buy-and-hold.
- **Tax-aware in AU** — the long horizon naturally captures the >12-month CGT discount on the core holding.
- **Complements fast strategies** — a patient long-horizon core underneath a book of reflexive/arb strategies.

## Disadvantages

- **Tiny sample / decaying template** — three cycles, drifting thresholds, and an ETF-era regime change already softening the pattern.
- **Deep, long drawdowns** — even with trimming, holding BTC through a cycle means 35-50%+ drawdowns and multi-year underwater stretches.
- **Directional, long-biased** — no market-neutrality; eats the full crypto beta.
- **Timing error dominates P&L** — zones bound risk, not exact turns; a few weeks' error swamps transaction cost.
- **Psychologically hard** — the correct action (buy capitulation, sell euphoria) is the emotionally hardest; operator override is the main failure mode.
- **Metric distortions** — lost coins, exchange reshuffles, and provider revisions pollute the cost-basis inputs.

## Sources

- [[mvrv]], [[mvrv-z-score]], [[nupl]], [[realized-price]] — the on-chain valuation metrics and their cross-cycle-drift caveats (wiki concept pages).
- [[bitcoin-halving]] — the supply-issuance mechanics and halving calendar.
- [[bitcoin-cycle-regime]] — the wiki's regime framing, including the explicit caution that ETF flows have altered the classic 4-year cycle and that halving dates are *not* mechanical price triggers.
- Glassnode and CryptoQuant on-chain research — the analytics platforms that popularised MVRV/NUPL/realized-price cycle zones (see [[glassnode]], [[cryptoquant]]).
- [[miner-capitulation-bottom]] — the adjacent hash-ribbon/miner-flow bottom signal that corroborates the accumulation zone.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/on-chain/dormancy/btc` — BTC MVRV + supply-shock signals, zone classification (capitulation → euphoria) — the core zone input
- `GET /api/v1/on-chain/score` — On-Chain Health composite (0-100); the structural-kill input
- `GET /api/v1/on-chain/miners/hash-ribbon` — Hash Ribbon state (capitulation/recovery/normal); bottom corroboration
- `GET /api/v1/regimes/current` — current long-horizon 10-state market regime

**Historical data:**
- `GET /api/v1/market-intelligence/btc/cycle-indicators` — all 8 BTC cycle indicators, historical (the cycle-timing battery)
- `GET /api/v1/market-intelligence/btc/cycle-indicators/{indicator}` — single indicator by name (e.g. MVRV-Z), historical
- `GET /api/v1/market-data/btc-price-history?days=730` — BTC price history + 200-day MA
- `GET /api/v1/on-chain/whale-score/BTC` — whale accumulation score timeseries (accumulation-zone corroboration)

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/on-chain/dormancy/btc"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-on-chain]]; cycle indicators on [[cryptodataapi-market-intelligence]].

## Related

- [[mvrv]], [[mvrv-z-score]] — the core valuation oscillator
- [[nupl]] — the unrealized-profit/loss zone bands
- [[realized-price]] — the aggregate cost-basis floor
- [[bitcoin-halving]] — the supply-issuance clock
- [[sopr]] — realized-profit confirmation
- [[bitcoin-cycle-regime]] — the wiki's regime framing and cycle-decay caveats
- [[market-cycle]] — the cycle structure the metrics are read against
- [[on-chain-analysis]], [[on-chain-regime]] — the parent on-chain mechanics
- [[miner-capitulation-bottom]] — adjacent hash-ribbon bottom signal
- [[dollar-cost-averaging]], [[buy-and-hold]] — the passive baselines this strategy times against
- [[position-sizing]] — the long-horizon risk-budget layer
- [[edge-taxonomy]], [[failure-modes]], [[when-to-retire-a-strategy]] — methodology
