---
title: "Scalping (Crypto Perps)"
type: strategy
created: 2026-04-06
updated: 2026-07-14
status: good
tags: [scalping, day-trading, crypto, perpetual-futures, market-microstructure, funding-rate, hyperliquid]
aliases: ["Crypto Scalping", "Perp Scalping", "Spread Scalping", "Micro Mean-Reversion Scalp", "High-Frequency Retail Scalping"]
strategy_type: hybrid
timeframe: scalp
markets: [crypto]
complexity: advanced
backtest_status: untested

# Edge characterization
edge_source: [structural, behavioral, latency]
edge_mechanism: "Capture the bid-ask spread and micro mean-reversion by resting maker orders that earn rebates while impatient takers cross the spread into you; funding, fees, and fill quality — not the price view — decide whether the pennies net positive."

# Data and infrastructure requirements
data_required: [trades-tick, l2-orderbook, funding-rates, fee-schedule]
min_capital_usd: 2000
capacity_usd: 2000000
crowding_risk: high

# Performance expectations (net of maker/taker fees + funding + slippage)
expected_sharpe: 0.6
expected_max_drawdown: 0.25
breakeven_cost_bps: 5

# Decay history
decay_evidence: "The retail scalping edge has been competed away by co-located and on-chain market makers who quote the same books tighter and faster. Taker-fee scalping on crypto perps is structurally negative-EV: round-trip taker is ~8-10 bps against 5-20 bps targets. The only durable variant is maker/rebate scalping, which requires fee-tier volume most retail never reaches; Binance/Bybit spot maker fees and Hyperliquid maker rebates have compressed, and 24/7 funding adds a carry cost that time-limited equity/forex scalping never faced."

# Lifecycle
kill_criteria: |
  - rolling 200-trade net expectancy below 0 after fees, funding, and slippage
  - maker fill ratio drops below 70% (forced into taker fees that break the edge)
  - median slippage exceeds modelled by 1.5x for 2 weeks
  - gross-to-net ratio below 1.5 (fees/funding eating >1/3 of gross P&L)

related: ["[[order-flow-scalping]]", "[[vwap-trading]]", "[[market-making-strategy]]", "[[hyperliquid-market-making]]", "[[bid-ask-spread]]", "[[spread]]", "[[order-book]]", "[[depth-of-market]]", "[[cumulative-volume-delta]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[funding-by-hour]]", "[[hyperliquid]]", "[[hyperliquid-fee-tiers-and-maker-rebates]]", "[[fees]]", "[[fees-and-friction]]", "[[slippage]]", "[[latency]]", "[[transaction-costs]]", "[[scalping-vs-position-trading]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
---

# Scalping (Crypto Perps)

Scalping extracts many **small profits (5-20 bps)** from brief price movements on crypto [[perpetual-futures|perps]], holding positions for seconds to a few minutes. Crypto scalpers exploit micro-level supply/demand imbalances, spread capture, and short-term momentum bursts on the deepest markets (BTC/ETH/SOL perps on [[hyperliquid|Hyperliquid]], Binance, Bybit). The strategy demands **fast execution**, **tight spreads**, **high volume**, and the ability to read the [[order-book|Level-2 book]] and tick tape. It produces a high volume of trades (50-300+ per day), relying on a slight per-trade edge compounded across many repetitions. In crypto specifically, the two costs that time-limited equity/forex scalpers never faced — **maker/taker fee asymmetry** and **24/7 [[funding-rate|funding]]** — are the dominant determinants of whether the strategy is profitable at all.

## Edge source

Per [[edge-taxonomy]], crypto perp scalping is primarily a *structural* spread-capture edge, with behavioural and latency components:

- **Structural (primary).** Resting maker limit orders capture the [[bid-ask-spread|bid-ask spread]] and, on many venues, a **maker rebate**, when impatient takers cross into them. This is market-making-lite (see [[market-making-strategy]], [[hyperliquid-market-making]]): you are paid to provide immediacy. The edge is the spread + rebate minus adverse selection.
- **Behavioural.** Fading micro-overreactions — a stop-run spike, a single large market order that overshoots — exploits the impatience of takers who pay the spread to get filled now.
- **Latency (double-edged).** Fast entry/exit and cancel-replace let you stay at the top of the queue and pull quotes before adverse fills. But co-located and on-chain MMs are faster, so latency mostly works *against* the retail scalper — the same tension as [[order-flow-scalping]].

The critical, non-obvious point: the scalper's price *view* is almost irrelevant to expectancy. What matters is **fee structure and fill quality**. A taker-only scalper is structurally negative-EV on crypto perps; a maker-rebate scalper with good fills can be positive on the identical price signals.

## Why this edge exists

1. **Impatient flow pays the spread.** Retail takers, liquidation engines, and momentum bots cross the spread to transact immediately. The resting scalper is the counterparty being paid for that immediacy.
2. **Micro mean-reversion.** On sub-minute horizons, single large orders overshoot and revert as the book refills. A scalper who buys the dip of a stop-run and sells the pop captures the reversion — provided fees do not exceed it.
3. **24/7 fragmented liquidity.** Constant trading across many venues creates continuous micro-imbalances — more scalping opportunities than a session-bound equity market, though each is thin.
4. **Rebate economics.** Venues pay maker rebates (or near-zero maker fees) to attract liquidity. That rebate *is* a structural subsidy the disciplined maker-scalper harvests; it is the difference between positive and negative EV.

## Null hypothesis

Under a no-edge world, sub-minute crypto perp returns are a martingale and scalping harvests nothing net of costs:

- Entering on micro-momentum or spread-capture setups yields zero average forward return over the 15s-5min horizon.
- The tick-chart/DOM filters do not improve the entry distribution.
- Win rate sits near 50% and net expectancy equals **minus** the round-trip fee + spread + funding.
- Maker fills are adversely selected exactly enough to offset the rebate (the classic market-maker null).

Empirically, on liquid crypto perps the null is *weakly* rejected for maker-side spread capture — resting quotes earn the spread + rebate and micro-reversion shows small positive drift — **but** it is *not* rejected for taker-side scalping, where fees exceed the tiny gross edge. The honest conclusion mirrors [[order-flow-scalping]]: gross edge is real and tiny; net edge is entirely a function of fees, rebates, funding, and fill quality. Most retail scalpers are net negative because they pay taker fees and funding on a 50/50 price signal.

## Rules

### Market selection

- Trade only the tightest-spread, deepest perps: **BTC, ETH** (SOL in active windows). Wide-spread alt perps are un-scalpable — the spread alone exceeds the target.
- Prefer venues with **maker rebates or near-zero maker fees** at your volume tier (Hyperliquid maker rebate, Binance/Bybit VIP maker). Fee tier selection is a *strategy parameter*, not an afterthought.
- Trade high-volume windows; avoid dead hours and the minutes around a high-[[funding-rate|funding]] timestamp on the perp you hold.

### Entry

1. **Spread scalp (primary):** rest limit orders at/inside the top of book on both sides to capture the [[bid-ask-spread|spread]] + rebate, similar to manual [[market-making-strategy|market making]]. Skew quotes toward the side the CVD/tape favours.
2. **Momentum scalp:** enter *as maker on a pullback* in the direction of a sudden volume/CVD surge; use a fast EMA on a tick/second chart for micro-trend.
3. **Absorption scalp:** when large resting L2 size absorbs aggressive flow without price moving through, join the resting side (see [[order-flow-scalping]]).

### Exit

1. **Fixed target:** **5-20 bps** on BTC/ETH. Take the quick profit; do not hold for larger moves.
2. **Time exit:** flat within **30-90 seconds** if the trade has not moved in favour — scratch at breakeven or a tiny loss.
3. **Hard stop:** **5-15 bps**; the edge is high win rate + tiny losses, not large R:R.
4. **Adverse-flow exit:** if the book suddenly loads against the position (large opposite-side size appears, CVD flips), exit immediately without waiting for the stop.

### Sizing and cost discipline

- **Per-trade risk:** ≤ 0.3-0.5% of equity. **Max concurrent:** 1-3.
- **Maker fill ratio target ≥ 80%.** Chasing fills as taker destroys expectancy; if you cannot get maker fills, the market is too fast for the strategy right now.
- **Funding awareness:** avoid holding across a funding timestamp on a high-funding perp; a single funding payment can exceed a scalp target.

## Implementation pseudocode

```python
# crypto_perp_scalp.py — maker spread-capture scalp with fee/funding guards
TARGET_BPS       = 10       # 0.10%
STOP_BPS         = 10
TIME_STOP_S      = 75
MIN_SPREAD_BPS   = 3        # only scalp if spread wide enough to cover costs
MAKER_FEE_BPS    = -1.0     # rebate (negative = paid); set per venue/tier
TAKER_FEE_BPS    = 4.5
FUNDING_GUARD_S  = 120      # don't open within this of a funding stamp on high-funding perp

def scalp_quote(book, cvd, funding, secs_to_funding):
    spread_bps = (book.ask - book.bid) / book.mid * 1e4
    if spread_bps < MIN_SPREAD_BPS:
        return None                                  # too tight to profit
    if abs(funding.rate_8h) > 0.0005 and secs_to_funding < FUNDING_GUARD_S:
        return None                                  # funding would swamp target
    skew = 1 if cvd.slope(10) > 0 else -1            # lean toward aggressor side
    return dict(bid=book.bid, ask=book.ask, skew=skew, post_only=True)  # maker only

def net_expectancy_bps(win_rate, target, stop, entry_fee, exit_fee, slip):
    gross = win_rate*target - (1-win_rate)*stop
    return gross - (entry_fee + exit_fee) - slip     # entry_fee<0 if maker rebate

def manage(pos, book, cvd, ts):
    if cvd.slope(5) * pos.dir < 0 or book.loading_against(pos.dir):
        return "EXIT_NOW"                            # adverse flow
    if pos.pnl_bps >= TARGET_BPS:  return "TAKE_PROFIT"   # maker exit if possible
    if pos.pnl_bps <= -STOP_BPS:   return "STOP"
    if ts - pos.entry_ts >= TIME_STOP_S: return "SCRATCH"
    return "HOLD"

# sanity check before deploying: expectancy must be > 0 with realistic inputs
assert net_expectancy_bps(0.62, TARGET_BPS, STOP_BPS,
                          MAKER_FEE_BPS, TAKER_FEE_BPS, slip=2.0) > 0
```

## Indicators / data used

| Input | Source | Purpose |
|---|---|---|
| Tick/second price | Exchange WS | Micro price action |
| [[order-book|L2]] / [[depth-of-market|DOM]] | Exchange WS / [[hyperliquid]] L2 | Spread, resting size, absorption |
| [[bid-ask-spread|Spread]] + depth | [[liquidity-depth-regime\|depth]] | Is the spread wide enough to scalp? |
| [[cumulative-volume-delta|CVD]] / tape | Trade WS taker flag | Aggressor lean, adverse-flow exit |
| Fast EMA (tick) | Local | Micro-trend for momentum scalp |
| [[funding-rate|Funding]] + timestamp | Derivatives feed | Carry cost / hold guard |
| Venue [[fees|fee schedule]] / tier | Exchange | The parameter that decides EV |

## Example trade

**Setup:** ETH-PERP on Hyperliquid, active EU session. Mid $3,120, spread $3,120.0/$3,120.6 (~2 bps — a touch tight, so wait). Spread widens to ~4 bps on a burst of activity; CVD leans mildly positive. Funding is a benign +0.006%/8h, next stamp 40 minutes away (funding guard clear).

**Entry:** Post a **maker** bid at $3,120.4. A momentum-chasing taker sell wave crosses into it — filled at $3,120.4, earning a small maker rebate rather than paying a fee.

**Management:** Target $3,123.5 (~10 bps). Stop $3,117.3 (~10 bps). Time stop 75s. CVD stays positive.

**Exit:** Price ticks up to $3,123.5 within 40s; exit — post a maker offer that fills, or cross as taker if the book is moving.

**Cost overlay (the decisive part):**
- Gross: +10 bps.
- Maker entry rebate: ~+1 bp. Exit as maker: ~+1 bp (or −4.5 bps if forced taker). Slippage: ~1-2 bps. Funding: ~0 (short hold, benign rate).
- **Net (both-maker): ≈ 10 + 1 + 1 − 1.5 ≈ +10.5 bps.** **Net (maker in, taker out): ≈ 10 + 1 − 4.5 − 1.5 ≈ +5 bps.** **Net (taker both sides): ≈ 10 − 9 − 1.5 ≈ −0.5 bps — a loser.** Identical price outcome; three different results driven entirely by fees. This is the strategy in one example.

## Performance characteristics

Realistic, cost-aware expectations (disciplined maker-side operator; **untested** as a systematic backtest — faithful sub-minute fill simulation is not achievable):

| Metric | Value | Note |
|---|---|---|
| Gross win rate | 55-70% | Required just to overcome costs. |
| Net expectancy/trade | +1 to +6 bps | Maker-side only; ~0 or negative as taker. |
| Trades/day | 50-300+ | Compounding tiny edges. |
| Avg hold | 15s-3min | Seconds-scale by design. |
| Net Sharpe | ~0.6 | Thin, high-variance, execution-bound. |
| Max drawdown | ~25% | Bursty; regime turns produce stop clusters. |
| Breakeven cost budget | ~5 bps round trip | Requires maker rebates to clear. |

**Cost overlay is the strategy.** On crypto perps round-trip taker is ~8-10 bps against 5-20 bps targets — 40-100% of gross. Add ~1-2 bps slippage and periodic [[funding-rate|funding]]. As a pure taker, expectancy is negative; the only durable variant is **maker/rebate scalping** with ≥80% maker fills and a favourable fee tier. Any backtest that ignores the maker/taker split, funding, and fill probability overstates this strategy dramatically — the classic pitfall in [[fees-and-friction|fee-and-friction]] modelling.

## Capacity limits

Bounded by **top-of-book depth** and the queue you can realistically hold. BTC/ETH perp top-of-book is often $200-500k, and as a maker you only earn when takers cross into your size. Realistic single-operator capacity: **$100k-$2M** on majors. Beyond that, your resting size is a larger fraction of the book (more adverse selection) and your taker exits move price. Not a primary book at scale — a solo-operator/satellite strategy, and at real size it *becomes* [[market-making-strategy|market making]] with its own infrastructure demands.

## What kills this strategy

Mapped to [[failure-modes]]:

1. **Fees/funding dominate (Failure Mode #3 — costs).** The single largest killer. Round-trip taker exceeds the target; funding across a hold exceeds a scalp. Loss of rebate tier or a fee hike flips EV negative overnight.
2. **Latency arms race / crowding (Failure Mode #4).** Co-located and on-chain MMs quote tighter and faster; the retail scalper's queue position and reaction time are structurally inferior.
3. **Adverse selection.** Maker fills cluster right before adverse moves (you get filled because informed flow is crossing you). In fast tape this offsets the rebate — the market-maker's perennial problem (see [[vpin]]-style toxicity).
4. **Regime change (Failure Mode #5).** In low-volume chop or one-way trend, spreads tighten below profitability or micro-reversion vanishes.
5. **Slippage on exit.** Volatile moments turn winners into losers when the taker exit slips through several ticks.
6. **Operational/exchange risk.** Perp outages during volatile windows strand positions; a single stuck trade in a gap erases a day of pennies.
7. **Burnout/operator error.** Sustained focus for hours; high burnout; discretionary override after a bad run is a dominant human failure mode.

## Kill criteria

Pause on any of:

1. **Rolling 200-trade net expectancy < 0** after fees, funding, and slippage.
2. **Maker fill ratio < 70%** — forced into taker fees that break the edge.
3. **Median slippage > 1.5x modelled** for 2 weeks.
4. **Gross-to-net ratio < 1.5** — costs are eating more than a third of gross P&L; the market has tightened past your edge.

See [[when-to-retire-a-strategy]]. Scalping is pausable — the microstructure recurs — but is unusually sensitive to fee/latency shifts, so kill fast and re-validate.

## Advantages

- **Many opportunities** per day; no waiting for setups.
- **Very short exposure** — minimal overnight/gap risk; tiny per-trade loss.
- **Rebate economics** can make it positive-EV where the price signal alone is 50/50.
- **Relatively consistent income** when the maker edge holds.
- **Builds elite microstructure/execution skill.**
- **Low minimum capital** ($2k), though capacity caps quickly.

## Disadvantages

- **Fees/funding can consume all gross profit** — needs low/negative fee structure to survive.
- **Structurally negative-EV as a taker** — most retail scalpers lose here.
- **Latency disadvantage** vs co-located/on-chain MMs.
- **Slippage** in volatile moments flips winners to losers.
- **Not faithfully backtestable**; sub-minute fill simulation overstates edge.
- **Not scalable**; large size moves the market against you and turns it into market making.
- **Mentally punishing; high burnout.**
- **24/7 markets** remove the natural stop that session-bound scalping had — overtrading risk.

## Sources

- Hyperliquid, Binance, Bybit fee-schedule and maker-rebate documentation — the parameters that decide EV. See [[hyperliquid-fee-tiers-and-maker-rebates]], [[fees]].
- Avellaneda & Stoikov (2008), *High-frequency trading in a limit order book* — the market-making/inventory model underlying spread-capture scalping. See [[market-making-strategy]], [[avellaneda-stoikov-model]].
- Easley, López de Prado, O'Hara — flow toxicity/adverse selection on maker fills (why the rebate is not free). See [[vpin]].
- [[scalping-vs-position-trading]] — comparison of the fastest and slowest active styles.
- Practitioner literature on crypto perp funding mechanics and its impact on short-hold strategies. See [[funding-rate]], [[funding-by-hour]].

## Getting the Data (CryptoDataAPI)

CryptoDataAPI provides L2 book snapshots, depth/spread, funding, and pair specs — enough to size the spread-capture edge and check funding. Tick-level fills and the aggressor tape require the exchange trade/L2 WebSocket directly.

**Live data:**
- `GET /api/v1/hyperliquid/l2-book?coin=BTC` — L2 order book snapshot (spread, resting depth)
- `GET /api/v1/liquidity/depth` — depth and spread at 10/25/50/100 bps (is the spread scalp-able?)
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — funding rate + timestamp for the hold guard
- `GET /api/v1/market-data/exchange-info?symbol=BTCUSDT` — tick size / pair specs / fee context
- `GET /api/v1/hyperliquid/summary?coin=BTC` — all-in-one perp snapshot (price, funding, OI)

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=BTC&interval=1m&limit=1000` — 1-minute perp OHLCV
- `GET /api/v1/backtesting/klines` — deep OHLCV archive
- `GET /api/v1/backtesting/funding` — funding history for carry modelling

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/liquidity/depth"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-hyperliquid]], [[cryptodataapi-market-data]].

## Related

- [[order-flow-scalping]] — the CVD/footprint-driven cousin
- [[vwap-trading]] — intraday fair-value reference and slower sibling
- [[market-making-strategy]], [[hyperliquid-market-making]] — what scalping becomes at scale
- [[bid-ask-spread]], [[spread]], [[order-book]], [[depth-of-market]] — the microstructure being harvested
- [[cumulative-volume-delta]] — aggressor lean and adverse-flow exit
- [[perpetual-futures]], [[funding-rate]], [[funding-by-hour]] — instrument and carry
- [[hyperliquid]], [[hyperliquid-fee-tiers-and-maker-rebates]] — venue and the fee tiers that decide EV
- [[fees]], [[fees-and-friction]], [[slippage]], [[transaction-costs]], [[latency]] — the costs that are the whole game
- [[scalping-vs-position-trading]] — style comparison
- [[edge-taxonomy]], [[failure-modes]], [[when-to-retire-a-strategy]] — methodology
</content>
