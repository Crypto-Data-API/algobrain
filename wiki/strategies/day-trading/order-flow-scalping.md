---
title: "Order Flow Scalping (Crypto Perps)"
type: strategy
created: 2026-04-06
updated: 2026-07-14
status: good
tags: [scalping, order-flow, crypto, perpetual-futures, market-microstructure, day-trading, hyperliquid, liquidations]
aliases: ["CVD Scalping", "Footprint Scalping", "Tape Reading (Crypto)", "Delta Divergence Scalp", "Order Flow Trading"]
strategy_type: hybrid
timeframe: scalp
markets: [crypto]
complexity: advanced
backtest_status: untested

# Edge characterization
edge_source: [informational, behavioral, structural]
edge_mechanism: "You read the aggressor imbalance (CVD) and the absorption of forced/impatient flow a beat before price adjusts; the counterparties are momentum-chasing takers and liquidation engines dumping non-economic supply — but co-located market makers see the same book faster, so the retail edge is thin and fee-sensitive."

# Data and infrastructure requirements
data_required: [trades-tick, cvd-tick, l2-orderbook, liquidation-feed, funding-rates]
min_capital_usd: 2000
capacity_usd: 1000000
crowding_risk: high

# Performance expectations (net of taker/maker fees + slippage)
expected_sharpe: 0.5
expected_max_drawdown: 0.30
breakeven_cost_bps: 8

# Decay history
decay_evidence: "The manual tape-reading edge has been compressed by co-located HFT market makers on Binance/Bybit and by on-chain CLOBs (Hyperliquid) where the aggressor tape and L2 book are public and machine-read in microseconds. Free real-time CVD and liquidation feeds (Coinglass, exchange WebSockets) democratised the signal, so any imbalance visible to a human is already priced by bots. Net taker-fee scalping on crypto perps is structurally marginal-to-negative EV; the surviving edge is maker-side or genuine sub-second micro-alpha."

# Lifecycle
kill_criteria: |
  - rolling 30-trade win rate below 52% (edge no longer overcomes fees)
  - net-of-fee expectancy per trade below 0 over any 100-trade window
  - median realised slippage exceeds 1.5x the modelled slippage for 2 weeks (book too thin / too fast)
  - three consecutive sessions where taker fees + funding exceed gross P&L

related: ["[[order-flow]]", "[[order-flow-analysis]]", "[[order-flow-imbalance]]", "[[cumulative-volume-delta]]", "[[footprint-chart]]", "[[order-book]]", "[[depth-of-market]]", "[[absorption]]", "[[vpin]]", "[[spoofing]]", "[[liquidation]]", "[[forced-liquidation]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[hyperliquid]]", "[[hyperliquid-order-book-microstructure]]", "[[microstructure-noise-low-timeframe]]", "[[vwap]]", "[[vwap-trading]]", "[[scalping]]", "[[market-making-strategy]]", "[[fees]]", "[[slippage]]", "[[liquidation-cascade-fade]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
---

# Order Flow Scalping (Crypto Perps)

Order flow scalping reads the **live aggressor tape** of a crypto perpetual — who is hitting the bid vs lifting the offer, and whether resting liquidity absorbs or gives way — to enter tiny, seconds-to-minutes trades aligned with the dominant *aggressive* flow. On crypto perps (BTC/ETH/SOL on [[hyperliquid|Hyperliquid]], Binance, Bybit) the raw material is the trade tape with the taker-side flag, **[[cumulative-volume-delta|Cumulative Volume Delta]] (CVD)**, [[footprint-chart|footprint]] volume-at-price, the **[[depth-of-market|L2 order book]]/heatmap**, and the **[[liquidation]] feed** — the crypto-native equivalent of forced-selling prints. It is the modern, digital descendant of ticker-tape reading and among the most skill-intensive approaches in [[day-trading|crypto day trading]]. Crucially, on crypto perps the tape, book, and liquidations are *fully public and machine-read*, so the retail edge is thin and dominated by whether fees are paid as taker or captured as maker.

## Edge source

Per [[edge-taxonomy]], crypto order-flow scalping blends three edges — with a fourth (latency) working *against* the retail practitioner:

- **Informational (primary but fragile).** Reading aggressor imbalance, absorption, and stacked footprint imbalances lets you infer the near-term intention of size a fraction of a second before price adjusts. On a public tape this is a *speed race*, and the retail human is slow.
- **Behavioural.** The counterparties are momentum-chasing takers (buying because the tape is green), panic sellers, and stop-runs. Fading their exhaustion or riding their initiation exploits [[behavioral-finance|recency and herd behaviour]].
- **Structural.** [[liquidation|Liquidation]] flow is *non-economic* — the engine market-sells at any price. Reading the [[forced-liquidation|forced-liquidation]] prints on the tape and providing the liquidity that vanished is a structural spread capture, closely related to (and the fast cousin of) the [[liquidation-cascade-fade|liquidation cascade fade]].
- **Latency (against you).** Co-located market makers on Binance/Bybit and on-chain CLOB bots on [[hyperliquid]] see the same book in microseconds and act first. This is the *reason* the retail edge is thin — you are informational-edge long but latency-edge short.

The honest framing: the edge exists in *fragments*, at *key levels*, in *fast tape* where discretionary read still beats naive bots — but it is small, perishable, and only positive after you solve the fee problem (below).

## Why this edge exists

1. **Non-economic and impatient flow overshoots.** Liquidation engines and stop-runs dump supply the book cannot instantly absorb; the impatient taker crosses the spread. Both leave a short-lived price dislocation a fast reader can fade or ride.
2. **Absorption is informative.** When large resting bids soak up wave after wave of aggressive selling without price breaking, the resting side is revealing genuine demand — a read that precedes the bounce by seconds. On crypto this is visible on the [[depth-of-market|DOM]]/heatmap ([[hyperliquid]] L2, Bookmap on CEX feeds).
3. **CVD/price divergence marks exhaustion.** New price low with *rising* CVD (buyers absorbing) is a classic reversal tell; the crowd watching only candles misses it.
4. **24/7, fragmented venues.** Crypto never closes and liquidity is split across CEX perps and on-chain CLOBs, so transient imbalances recur far more often than in a single-venue equity future — more shots on goal, albeit each smaller.

## Null hypothesis

Under a no-edge world, the aggressor tape is a martingale and imbalances predict nothing net of costs:

- Entering with the dominant CVD/footprint imbalance would yield zero average forward return over the 30s-3min horizon.
- The CVD-divergence and absorption filters would not improve the entry distribution.
- Win rate would sit near 50% and net expectancy would be *negative* by exactly the round-trip fee + spread.
- Realised slippage in fast tape would equal the modelled slippage (no adverse selection premium).

Empirically, on liquid crypto perps in fast tape the null is *weakly* rejected for a skilled reader: selective absorption/divergence setups show win rates ~55-65% and small positive forward drift over seconds. **But** the effect is so small that it is entirely consumed by taker fees for most participants — the null is *not* rejected net-of-cost unless the trader captures maker rebates or has genuine sub-second read. This is the central, sobering fact of the strategy: gross edge is real and tiny; net edge depends almost entirely on the fee structure and execution quality.

## Rules

### Market selection

- Trade only the deepest perps: **BTC and ETH** (SOL acceptable in high-vol windows). Alt perps have thin books where slippage swamps the edge.
- Trade only high-flow windows: US/EU macro releases, Asia open, high-[[funding-rate|funding]] regimes, and active [[liquidation]] clusters. Avoid dead low-volume hours where imbalance signals are noise.

### Entry (all must align)

1. **Aggressor imbalance.** Footprint/CVD shows a stacked diagonal imbalance — aggressive volume on one side ≥ **3x** the opposing side across **3+** adjacent price levels.
2. **CVD confirmation or divergence.** Either CVD trending *with* the intended direction (initiation), **or** price makes a new extreme while CVD fails to (absorption/divergence reversal).
3. **Absorption at a level.** Large resting L2 orders soak aggressive flow without price moving through; enter in the direction of the side that holds.
4. **Liquidation context.** A cluster of [[forced-liquidation|forced-liquidation]] prints in your favour (longs flushed below you) strengthens a long fade; see [[liquidation-cascade-fade]] for the larger-timeframe version.

### Exit

1. **Flow reversal (primary):** exit *immediately* when CVD flips against the position or aggressive opposite-side prints appear — do not wait for the stop.
2. **Fixed target:** **15-40 bps** on BTC/ETH (the crypto analogue of "4-10 ticks"). Targets are small by design.
3. **Hard stop:** **10-20 bps**, placed behind the absorption zone / imbalance cluster.
4. **Time stop:** flat within **1-3 minutes** if the move has not resolved — order-flow setups resolve fast or not at all.

### Sizing and fees (the make-or-break rule)

- **Rest as maker wherever possible.** On [[hyperliquid]] and CEX maker tiers, entering with a resting limit order earns a rebate or pays ~0 bps instead of ~4-5 bps taker. Given 15-40 bps targets, paying taker on *both* legs (~8-10 bps round trip) can consume 30-60% of the target. Maker entry / taker exit is the realistic minimum.
- **Per-trade risk:** ≤ 0.5% of equity. **Max concurrent:** 1-2. **No overnight/funding-heavy holds** — the hold is seconds, so funding is usually negligible, but avoid entering just before a funding timestamp on a high-funding perp.

## Implementation pseudocode

```python
# crypto_orderflow_scalp.py — CVD/absorption scalp on a single deep perp
IMBALANCE_RATIO = 3.0     # aggressor vol vs opposing, stacked 3+ levels
CVD_LOOKBACK_S  = 30
TARGET_BPS      = 25      # 0.25%
STOP_BPS        = 15      # 0.15%
TIME_STOP_S     = 180
MAX_CONCURRENT  = 2

def scalp_signal(tape, book, cvd, liqs):
    # stacked diagonal imbalance across >=3 adjacent levels
    stacked = footprint_stacked_imbalance(tape, ratio=IMBALANCE_RATIO, levels=3)
    if not stacked:
        return None
    side = stacked.side  # 'long' if buy-imbalance / absorption on bid

    # absorption: large resting size on 'side' holding vs aggressive opposite flow
    absorbing = book.resting_size(side) > 3 * book.aggressive_flow(opposite(side))

    # CVD confirm (initiation) OR divergence (price new extreme, CVD not)
    cvd_confirm   = cvd.slope(CVD_LOOKBACK_S) * dir(side) > 0
    cvd_divergent = price_new_extreme(opposite(side)) and not cvd_new_extreme(opposite(side))

    # liquidation tailwind: forced flow flushing the opposite side
    liq_tailwind = liqs.recent_notional(opposite(side), window_s=10) > liqs.mean_24h * 2

    if absorbing and (cvd_confirm or cvd_divergent) and liq_tailwind:
        return dict(side=side, target_bps=TARGET_BPS, stop_bps=STOP_BPS,
                    entry="maker_limit_at_absorption")   # rest, don't cross
    return None

def manage(pos, cvd, tape, ts):
    if cvd.slope(5) * dir(pos.side) < 0:                 # flow reversal
        return "EXIT_NOW"
    if pos.pnl_bps >= pos.target_bps:  return "TAKE_PROFIT"
    if pos.pnl_bps <= -pos.stop_bps:   return "STOP"
    if ts - pos.entry_ts >= TIME_STOP_S: return "TIME_STOP"
    return "HOLD"
```

Implementation notes that matter:

- **Liquidation-feed staleness.** Aggregators de-duplicate and delay liquidation prints. Use direct exchange WebSockets (`forceOrder` on Binance, Hyperliquid trades/liquidation stream) — a polled aggregator is 30-90s late, after the entry window has closed.
- **True tick CVD needs the taker flag.** Approximating CVD from 1-second up/down volume loses signal in fast tape and *overstates* backtested edge by 15-30% (the same caveat as [[liquidation-cascade-fade]]).
- **[[mark-price]] vs last.** Use mark for level context; a single liquidation can spike the last-trade print and create a false trigger.
- **[[spoofing]]/layering.** Displayed size on the L2 can be pulled before execution; weight *executed* aggression over *displayed* resting size.

## Indicators / data used

- **Trade tape with taker flag** — the aggressor side; the primary input. Binance `aggTrade`, Hyperliquid trades WS.
- **[[cumulative-volume-delta|CVD]]** — running taker-buy minus taker-sell; trend + divergence. See [[order-flow]], [[order-flow-analysis]].
- **[[footprint-chart|Footprint]]** — bid×ask volume per price; stacked imbalance detection.
- **[[depth-of-market|L2 order book]] / heatmap** — resting liquidity, absorption, pulls ([[hyperliquid]] L2, Bookmap on CEX).
- **[[liquidation|Liquidation]] feed** — forced non-economic flow; the crypto tailwind. See [[forced-liquidation]].
- **[[funding-rate|Funding]]** — regime tell (heavy longs → richer long-liquidation setups) and a cost check near funding timestamps.
- **[[vwap]]** — session/anchored fair-value reference for directional bias.

## Example trade

**Setup (BTC-PERP on Hyperliquid, active US-session tape):** BTC pulls back toward the anchored [[vwap]] at $60,450. The footprint shows aggressive selling (red delta) pushing price down, but resting bids at $60,400-60,450 absorb each sell wave without breaking lower. CVD is *flat* despite the price decline — sellers are not winning. A cluster of long-liquidation prints flushes just below at $60,380.

**Entry:** A stacked buy imbalance of ~4:1 appears at $60,410 / $60,420 / $60,430 as the liquidation supply clears; CVD ticks up. Rest a **maker** bid at $60,420 (filled as the last sell wave hits it) — no taker fee paid.

**Management:** Stop at $60,330 (~15 bps below, behind the absorption zone). Target $60,570 (~25 bps). Time stop 3 minutes.

**Exit:** Aggressive buying accelerates as shorts cover; CVD trends up hard; price reaches $60,570 in ~70 seconds. Exit as taker (0.045%).

**Cost overlay (why this trade is only just profitable):**
- Gross: +25 bps.
- Maker entry: ~0 bps (or a small rebate on Hyperliquid). Taker exit: ~4.5 bps. Slippage on exit in fast tape: ~2-3 bps.
- **Net ≈ 25 − 4.5 − 2.5 ≈ +18 bps** on the position. Had the *entry* also been taker (chasing the fill), it would be ~13 bps — and a single missed read that hits the 15 bps stop (−15 − fees ≈ −22 bps) wipes out the prior winner. Expectancy lives or dies on maker capture and read quality.

## Performance characteristics

Realistic, cost-aware expectations (skilled discretionary/semi-automated operator; **untested** as a systematic backtest because faithful order-flow replay is not achievable):

| Metric | Value | Note |
|---|---|---|
| Gross win rate | 55-65% | On selective absorption/divergence setups only. |
| Net expectancy/trade | +2 to +8 bps | *Only* with maker capture; ~0 or negative on all-taker execution. |
| Trades/session | 5-25 | High-flow windows only. |
| Avg hold | 30s-3min | Fast resolution by design. |
| Net Sharpe | ~0.5 | Thin, execution-dependent, high variance. |
| Max drawdown | ~30% | Bursty; strings of stop-outs when tape regime turns. |
| Breakeven cost budget | ~8 bps round trip | Below this the edge survives; above it it does not. |

**Cost overlay is the whole story.** Round-trip taker on crypto perps is ~8-10 bps (Binance 5 bps + 5 bps; Hyperliquid ~4.5 bps each side); against a 15-40 bps target that is 20-60% of gross. Slippage in cascade/fast tape adds 2-5 bps. The strategy is **structurally negative-EV as a pure taker** and only turns positive with maker rebates, VIP fee tiers, or genuine sub-second edge. Any backtest omitting the taker-vs-maker distinction and fast-tape slippage will wildly overstate this strategy.

## Capacity limits

Capacity is bounded by **top-of-book depth during the entry window** — the same variable being exploited. BTC/ETH perp top-of-book is often only $200-500k, and the strategy needs to enter and exit inside seconds without moving price. Realistic single-operator capacity: **$100k-$1M** on majors. Scaling requires spreading across venues and many small setps on more perps, which trades into thinner books where slippage dominates. This is a solo-operator / satellite strategy, never a primary book at size.

## What kills this strategy

Mapped to [[failure-modes]]:

1. **Latency arms race / crowding (Failure Mode #4).** Co-located MMs and on-chain CLOB bots read the public tape faster; every imbalance a human sees is already acted on. The retail edge shrinks toward zero as automation deepens.
2. **Fees dominate (Failure Mode #3 — costs).** Taker fees + slippage exceed the tiny gross edge for most participants. Loss of maker rebate tier or a venue fee hike can flip the strategy negative overnight.
3. **[[spoofing|Spoofing]]/layering.** Displayed liquidity that is pulled before execution generates false absorption reads.
4. **Regime change (Failure Mode #5).** In slow, low-flow, or purely trending tape the setups either vanish or mean nothing; the strategy needs volatile two-sided flow.
5. **Adverse selection in fast tape.** The exact moments the signal fires (cascades) are when slippage is worst and you are most likely filled by informed flow the instant before an adverse move — see [[vpin]].
6. **Operational/exchange risk.** Perp venue outages coincide with the high-flow windows the strategy targets; a stuck position in a gap blows through the stop.
7. **Human factors.** Mentally exhausting; 6-18 months of screen time to reach proficiency and high burnout — operator error is a dominant real-world failure mode.

## Kill criteria

Pause on any of:

1. **Rolling 30-trade win rate < 52%** — edge no longer overcomes fees.
2. **Net-of-fee expectancy < 0** over any 100-trade window.
3. **Median realised slippage > 1.5x modelled** for 2 weeks — book too thin/fast for the size.
4. **Three consecutive sessions** where taker fees + funding exceed gross P&L — the fee structure has broken the edge.

See [[when-to-retire-a-strategy]]. Order-flow scalping is pausable — the microstructure recurs — but its edge is unusually fragile to fee and latency changes.

## Advantages

- **Most real-time read available** — sees current aggression, not historical candles.
- **Surfaces non-economic flow** (liquidations, stops) invisible on standard charts.
- **Fast capital cycle** — seconds-to-minutes holds; many shots per session; minimal overnight/[[funding-rate|funding]] risk.
- **Works best at key levels** where large participants defend/attack.
- **Diversifying** — fires when trend books stall; low correlation to momentum P&L.
- **Low minimum capital** — works at $2k margin (though capacity caps fast).

## Disadvantages

- **Tiny, fee-sensitive edge** — structurally negative-EV as a pure taker; needs maker capture.
- **Latency disadvantage** — retail is slower than co-located MMs reading the same public tape.
- **Not faithfully backtestable** — order flow is real-time and contextual; simulators overstate edge.
- **Slippage in fast tape** turns winners into losers; adverse selection is worst exactly when signals fire.
- **Spoofing/layering** create false signals.
- **Mentally punishing**; long learning curve; high burnout.
- **Very low capacity**; solo/satellite only.

## Sources

- Bookmap, Coinglass, ATAS, Jigsaw, Exocharts documentation — crypto CVD, footprint, DOM/heatmap tooling and the "selling climax / absorption" archetype. See [[cumulative-volume-delta]], [[order-flow]].
- Easley, López de Prado, O'Hara, *Flow Toxicity and Liquidity in a High-Frequency World* (2012) — VPIN and adverse selection; why fast-tape fills are toxic. See [[vpin]].
- Hyperliquid and Binance/Bybit API documentation — trade tape taker flag, L2 book, `forceOrder`/liquidation streams, maker/taker fee schedules. See [[hyperliquid-order-book-microstructure]], [[fees]].
- Amberdata, *Liquidations in Crypto: How to Anticipate Volatile Market Moves* — practical detection of forced flow from public derivatives data. See [[liquidation-cascade-fade]] for the larger-timeframe expression.

## Getting the Data (CryptoDataAPI)

CryptoDataAPI provides L2 book snapshots, taker buy/sell ratios, liquidation flow, and depth context. True *tick-level* CVD requires the exchange trade WebSocket with the aggressor flag (Binance `aggTrade`, Hyperliquid trades stream) — CryptoDataAPI gives snapshot/aggregate context, not per-tick aggressor data.

**Live data:**
- `GET /api/v1/hyperliquid/l2-book?coin=BTC` — L2 order book snapshot (resting depth / absorption)
- `GET /api/v1/liquidity/depth` — per-coin depth and spread at 10/25/50/100 bps (slippage sizing)
- `GET /api/v1/market-intelligence/taker-buy-sell` — taker buy/sell ratio by exchange (4h aggressor-imbalance proxy)
- `GET /api/v1/market-intelligence/liquidations` — cross-exchange liquidation flow (top coins)
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — funding regime + cost check

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=BTC&interval=1m&limit=1000` — 1-minute perp OHLCV
- `GET /api/v1/backtesting/liquidations` — liquidation records archive
- `GET /api/v1/backtesting/klines` — deep OHLCV archive

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/l2-book?coin=BTC"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-hyperliquid]], [[cryptodataapi-market-intelligence]].

## Related

- [[order-flow]], [[order-flow-analysis]], [[order-flow-imbalance]] — the theory
- [[cumulative-volume-delta]] — the primary signal
- [[footprint-chart]], [[order-book]], [[depth-of-market]], [[absorption]] — the read
- [[vpin]] — flow toxicity / adverse selection
- [[spoofing]] — the false-signal risk
- [[liquidation]], [[forced-liquidation]] — the non-economic tailwind
- [[liquidation-cascade-fade]] — the larger-timeframe version of the same edge
- [[perpetual-futures]], [[funding-rate]] — instrument context
- [[hyperliquid]], [[hyperliquid-order-book-microstructure]], [[microstructure-noise-low-timeframe]] — venue microstructure
- [[vwap]], [[vwap-trading]] — fair-value reference
- [[scalping]], [[market-making-strategy]] — adjacent fast strategies
- [[fees]], [[slippage]] — the costs that decide profitability
- [[edge-taxonomy]], [[failure-modes]], [[when-to-retire-a-strategy]] — methodology
</content>
