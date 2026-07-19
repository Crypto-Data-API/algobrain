---
title: "Market Making Strategy (CEX)"
type: strategy
created: 2026-04-06
updated: 2026-07-19
status: draft
tags: [market-making, crypto, binance, bybit, spread-capture, inventory-management, adverse-selection, quantitative, scalping, perpetual-futures, funding-rate]
aliases: ["CEX Market Making", "Crypto Market Making", "Spread Capture", "Binance Market Making", "Bybit Market Making"]
strategy_type: quantitative
timeframe: scalp
markets: [crypto]
complexity: advanced
backtest_status: untested

# Edge characterization
edge_source: [structural, risk-bearing, latency]
edge_mechanism: "Uninformed crypto takers (leveraged retail, liquidations, momentum flow) cross the spread on a CEX order book; the maker is paid the spread plus fee rebates to warehouse inventory and bear the adverse-selection risk of trading against informed flow."
data_required: [l2-order-book, trade-prints, realized-volatility, funding-rates, open-interest]
min_capital_usd: 25000
capacity_usd: 25000000
crowding_risk: high

# Performance expectations (net of fees, funding, slippage)
expected_sharpe: 2.5
expected_max_drawdown: 0.20
breakeven_cost_bps: 2

# Decay history
decay_evidence: "Majors (BTC/ETH) on Binance/Bybit are saturated by professional MM firms (Wintermute, GSR, Jump, Amber) and exchange MM programs; retail cannot win the latency/rebate game there. Edge has migrated to thin/newly-listed alt perps where spreads are wide but adverse selection and inventory risk are far higher."

related: ["[[hyperliquid-market-making]]", "[[market-making]]", "[[adverse-selection]]", "[[avellaneda-stoikov]]", "[[scalping]]", "[[order-flow-scalping]]", "[[vwap-trading]]", "[[statistical-arbitrage]]", "[[funding-rate]]", "[[funding-rate-arbitrage]]", "[[vpin]]", "[[order-flow]]", "[[binance]]", "[[bybit]]", "[[inventory-risk]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[book-trading-and-exchanges]]", "[[book-algorithmic-and-high-frequency-trading]]", "[[book-high-frequency-trading-aldridge]]", "[[cryptodataapi]]"]
---

# Market Making Strategy (CEX)

CEX market making is a **be-the-maker** strategy that continuously posts a two-sided bid and ask on a centralized crypto exchange ([[binance|Binance]], [[bybit|Bybit]], OKX), profiting from the [[bid-ask-spread]] plus maker fee rebates while managing inventory with an [[avellaneda-stoikov|Avellaneda-Stoikov]] skew. It is the centralized-venue counterpart to on-chain [[hyperliquid-market-making|Hyperliquid market making]] — the same spread-capture-versus-[[adverse-selection|adverse-selection]] trade-off, but on a private microsecond matching engine where latency is a co-location arms race, fees run on VIP/MM-program tiers, and perp inventory accrues 8-hour [[funding-rate|funding]]. In crypto it is almost exclusively algorithmic and, on majors, dominated by professional firms (Wintermute, GSR, Jump, Amber); the realistic retail-accessible edge lives in thinner, newly-listed alt perps where spreads are wide — and adverse selection is vicious.

## Edge source

Per [[edge-taxonomy]], CEX market making is a **structural + risk-bearing** edge with a decisive **latency** component:

- **Structural.** The exchange needs resting liquidity and pays makers (rebates, VIP/MM-program fee tiers) to provide it. The spread is the compensation for standing ready to trade; the flow is contractual, not a forecast.
- **Risk-bearing.** The maker is paid to warehouse inventory and to absorb the [[adverse-selection]] risk of occasionally being on the wrong side of an informed trade. Spread is the premium; inventory and toxic flow are the underwritten risks.
- **Latency.** On a CEX the matching engine cycles in microseconds, so being first in the queue at a price level (price-time priority) and cancelling faster than informed traders can pick you off is a genuine, capital-intensive advantage — the source of the professional moat on majors.

The maker takes **no directional view**. It is delta-neutral by design and holds directional exposure only through inventory it is forced to accumulate.

## Why this edge exists

- **Crypto takers are structurally uninformed on average.** The marginal Binance/Bybit taker is a leveraged retail long, a momentum chaser, or a forced liquidation — flow that crosses the spread for reasons unrelated to short-horizon fair value. The maker captures spread from the uninformed majority and pays it back only to the informed minority.
- **Liquidations are non-economic flow.** When exchange risk engines market-sell liquidated positions into the book, a maker with a resting bid gets filled by supply that *had* to hit it — the same non-economic-flow edge harvested in [[liquidation-cascade-fade]] from the other side.
- **Fee rebates pay you to provide a service.** At high VIP/MM-program tiers, maker fees go negative (a rebate), so the exchange literally pays the maker on every fill — often the difference between a profitable and unprofitable book on majors.

## Null hypothesis

Under a no-edge world, a two-sided maker earns zero after costs:

- Fill flow is **symmetrically informed**: every fill is, on average, immediately followed by an adverse move exactly equal to the captured spread (zero markout), so adverse selection precisely offsets spread + rebate.
- Inventory follows a random walk with no mean reversion, so inventory-skew quoting adds nothing.
- Funding paid/received on warehoused perp inventory nets to zero.
- Realized Sharpe is indistinguishable from zero; the equity curve is a driftless random walk minus fees.

The null is rejected when **markout on maker fills is positive at short horizons**, **inventory mean-reverts** (rewarding skewed quoting), and the flow mix is uninformed enough that spread + rebate exceeds toxic-fill losses. Persistently negative short-horizon markout on a symbol means the null holds for that symbol — stop quoting it.

## Rules

### Quoting (entry)

Quote around the [[avellaneda-stoikov|Avellaneda-Stoikov]] reservation price (the same model derived in full on [[hyperliquid-market-making]]):

- **Reservation price:** `r = s − q·γ·σ²·τ` — mid `s` skewed against signed inventory `q`; long inventory pushes `r` down, biasing the maker to sell.
- **Optimal half-spread (risk component):** `½·(γ·σ²·τ) + (1/γ)·ln(1 + γ/k)` — widens with volatility `σ`, risk aversion `γ`, horizon `τ`; `k` from order-arrival intensity.
- **Fee floor:** actual half-spread = `max(risk half-spread, min_half_spread)`, where `min_half_spread` covers maker round-trip fees plus target edge. On a positive-fee tier this floor forces wider quotes; on a rebate tier it can be very tight.
- **Bid** = `r − half_spread`; **Ask** = `r + half_spread`, snapped to tick.
- **Re-quote** on any of: mid move > ½ tick, inventory change, or a toxicity trigger — as fast as latency and rate limits allow.

Concrete BTCUSDT-perp parameterization (mid `s` = $100,000, ~50% annualized vol):

| Parameter | Symbol | Value | Meaning |
|---|---|---|---|
| Inventory risk aversion | γ | 8×10⁻⁴ | 1 BTC of net inventory skews `r` ~$19 |
| Volatility (1s, price) | σ | ~$8.9 /√s | from ~50% annualized BTC vol |
| Quote horizon | τ | 300 s | stationary tuning constant |
| Book liquidity decay | k | 1.4 | taker arrival intensity λ(δ)=A·e^(−kδ) |
| Min half-spread | — | ~1 bp on a rebate tier | fee floor |
| Max inventory | q_max | ±3 BTC | hard cap → one-sided quotes beyond |

Yields a risk half-spread ≈ $10 (~1 bp) and ~$19 skew per BTC held. On majors this is razor-thin and only works at a rebate tier; on thin alts the risk term (larger σ) does the work and quotes are naturally wide.

### Inventory / exit

- **Skew first, cross last.** Let the A-S skew attract offsetting flow before paying the taker fee to flatten.
- **Soft cap (½ q_max):** widen the far side, tighten the near side to accelerate mean reversion.
- **Hard cap (q_max):** quote one-sided; if inventory persists over cap for > N seconds, **cross the spread to flatten** — inventory risk now dominates spread income.
- **Funding-aware hold:** perp inventory accrues 8-hour funding on Binance/Bybit. Warehousing long inventory into positive funding is a carry cost — fold it into `γ` and bias skew toward flat before each funding stamp.
- **Loss limit / session flatten:** hard daily P&L stop; flatten and stand down on breach.

### Sizing

- Quote small clips (e.g. 0.05–0.3 BTC) laddered across 3–5 levels; total resting notional a small fraction of top-of-book depth.
- Margin sized to support q_max with a large buffer — **never** run the market-making book at high leverage; a maker liquidated on its own inventory has failed catastrophically.
- Separate books and q_max per symbol; treat majors and thin alts as different risk regimes.

## Implementation pseudocode

```python
# cex_market_maker.py — Avellaneda-Stoikov two-sided quoter for Binance/Bybit perps
import numpy as np

GAMMA, TAU, K   = 8e-4, 300.0, 1.4
MIN_HALF_BPS    = 1.0        # requires a rebate/low-fee VIP tier on majors
Q_MAX           = 3.0
TOXIC_MARKOUT_BPS = -0.8
FUNDING_SKEW_MULT = 1.5

def quotes(mid, inv, sigma_1s, funding_8h, markout_bps, tick):
    skew = inv * GAMMA * sigma_1s**2 * TAU
    r = mid - skew
    risk_half = 0.5*(GAMMA*sigma_1s**2*TAU) + (1.0/GAMMA)*np.log(1 + GAMMA/K)
    half = max(risk_half, MIN_HALF_BPS*1e-4*mid)
    if markout_bps < TOXIC_MARKOUT_BPS:            # toxic-flow defense
        half *= 3.0
    # funding-aware push to flat (8h funding pro-rated to hold)
    if (inv > 0 and funding_8h > 0) or (inv < 0 and funding_8h < 0):
        r -= FUNDING_SKEW_MULT * funding_8h * mid
    bid = round_to_tick(r - half, tick)
    ask = round_to_tick(r + half, tick)
    if inv >=  Q_MAX: bid = None                   # one-sided beyond cap
    if inv <= -Q_MAX: ask = None
    return bid, ask

def on_tick(state, book):
    mid = 0.5*(book.best_bid + book.best_ask)
    bid, ask = quotes(mid, state.inv, state.sigma, state.funding_8h,
                      state.markout_bps, book.tick)
    exchange.cancel_all(state.symbol)
    if bid: exchange.post_only_buy(state.symbol, state.clip, bid)
    if ask: exchange.post_only_sell(state.symbol, state.clip, ask)
    if abs(state.inv) > Q_MAX and state.secs_over_cap > N_MAX:
        exchange.market_flatten(state.symbol, state.inv)   # accept taker fee
```

Production adds: `post_only`/maker-only order flags; queue-position tracking; co-located/low-latency feed and order gateway; per-symbol live markout and toxicity ([[vpin]]-style) monitoring; rate-limit-aware cancel/replace; and a global kill switch.

## Indicators / data used

| Data | Purpose |
|---|---|
| L2 order book | Depth for clip sizing and `k`; queue position |
| Trade prints / fills | Per-fill **markout** at 1s/5s/30s — the [[adverse-selection]] gauge |
| Realized volatility (1-min) | Feeds reservation skew and risk half-spread |
| [[funding-rate]] (8h) | Carry on warehoused perp inventory; funding-aware skew |
| [[open-interest]] | Regime context; heavy long skew flags liquidation-prone flow |
| Order-flow toxicity ([[vpin]]) | Widen/pull trigger |
| Correlation matrix | Hedge-instrument selection when running a cross-venue hedge |

## Example trade

**BTCUSDT perp, mid $100,000, quiet regime, maker at a rebate VIP tier.** Inventory flat.

1. **Quote:** reservation = mid. Half-spread = fee floor $10. Post bid $99,990 / ask $100,010, clip 0.2 BTC, post-only.
2. **Fill:** an uninformed taker lifts the ask → maker **short 0.2 BTC** at $100,010, earns the rebate.
3. **Skew:** inventory −0.2 → reservation shifts up ~$3.8. New quotes biased to buy back.
4. **Offset:** a taker hits the bid at $99,992 → maker buys 0.2, **flat**. Round-trip captured $100,010 − $99,992 = **$18 (1.8 bps)** + two rebates − ~0 taker fees − negligible funding ≈ **+$4** on $20k notional.
5. **Scale:** ~2,000 clean round trips/day → gross ~$8,000/day *before* the toxic-fill tail. A single adversely-selected fill in a 30 bps move (−$60 on the clip) erases ~15 clean round trips.

**Thin-alt caveat.** The same bot on a newly-listed mid-cap alt perp: quoted spread is naturally wide (say 12 bps) because σ is ~120% annualized and the book is thin — looks lucrative. But the flow is far more toxic (listing hype, insider/informed flow, thin depth), so markout on fills is frequently −8 to −15 bps, and a single momentum leg pins inventory at q_max with no offsetting flow. Wide spreads on thin alts are **compensation for a much worse adverse-selection distribution**, not free money; the bot must run a much wider fee floor, a smaller q_max, and a hair-trigger toxicity kill — or skip the symbol until the book deepens.

## Performance characteristics

Realistic, cost-corrected picture:

| Metric | Value | Note |
|---|---|---|
| Gross spread capture (per round trip) | 1.5–3 bps (majors); 5–15 bps (thin alts) | Before adverse selection |
| Adverse-selection drag | 1–2.5 bps (majors); 5–15 bps (thin alts) | The loss distribution's driver |
| Maker fee / rebate | −0.005% to +0.02% | Binance/Bybit perp maker; negative at top VIP/MM tiers |
| Taker fee (flattening) | 0.04–0.055% | Every forced flatten is expensive |
| Funding drag on inventory | variable, 8h | Punitive if warehousing against funding |
| Target net Sharpe | 2.5+ (majors, benign) | Professional books exceed 3.0 (Source: [[book-high-frequency-trading-aldridge]]) |
| Max drawdown | 15–20% | Inventory blowouts in one-directional moves |
| Breakeven cost budget | ~2 bps round trip | Above this the book is unprofitable |

**Cost overlay (Binance/Bybit-specific):**
- Perp maker fee base ~0.02%; reduced by VIP tier (30-day volume + balance) and, on Binance, **negative maker rebates at top VIP**; Bybit runs a dedicated market-maker program with rebates. *The strategy on majors is only viable at a rebate/low-fee tier.*
- Perp taker fee ~0.04–0.055% — makes every forced flatten costly; inventory discipline is the whole game.
- Funding: 8-hourly on warehoused inventory; can dominate P&L if the book runs persistent one-sided inventory.
- Slippage/impact when flattening at size: 2–10 bps majors, far worse on thin alts.
- Infrastructure: co-located servers, low-latency feeds, exchange VIP status — a real, recurring cost that gates retail participation on majors.

## Capacity limits

Capacity is bounded by **book depth and competition from professional MMs**:

- **BTC/ETH on Binance/Bybit:** deep but saturated by pro firms and exchange MM programs; an independent maker captures only the flow it can out-queue. Realistic single-symbol working capacity: **~$5–25M** turnover before self-impact turns fills toxic.
- **Thin/newly-listed alt perps:** wider spreads, thinner competition, but far lower absolute depth ($100k–$2M) and worse toxicity — capacity is fragmented across many small, risky books.
- **Aggregate across a diversified symbol book:** low-to-mid eight figures for a well-run operation (`capacity_usd` ≈ $25M), above which you are competing head-to-head with Wintermute/GSR-class latency and must win on infrastructure, not presence.

## What kills this strategy

Mapped to [[failure-modes]]:

1. **Toxic flow / adverse selection (primary).** A regime where informed flow dominates flips markout persistently negative; the spread cannot cover it. Worst on thin alts and around listings/catalysts.
2. **Inventory blowout in a trend.** A one-directional move fills one side repeatedly; inventory pins at q_max and the forced flatten crystallizes a directional loss — the classic MM death (see the LUNA-era MM blowups).
3. **Fee-tier regression (crowding / decay).** Losing VIP/MM-program status pushes maker fees positive, turning a profitable majors book negative overnight.
4. **Latency loss.** Slower cancels than informed traders means resting stale quotes that get picked off — the reason majors are a professional-only game.
5. **Exchange operational risk.** Cascades coincide with exchange degradation/outages (Binance down 2021-05-19); a live inventory position during downtime can blow through limits with no escape.
6. **Funding drag.** Persistent one-sided inventory into adverse funding quietly bleeds the book.

## Kill criteria

Pause (not retire) the book on any of:

- **Rolling 30-min markout on maker fills < −0.5 bps** on a symbol → stop quoting it (toxic-flow kill).
- **Inventory above q_max for > 10 minutes** more than 3× in a session → mean-reversion assumption broken; flatten and stand down.
- **Sleeve drawdown > 12%** in any rolling 7-day window.
- **Net maker fee reverts positive (lost tier)** and spreads cannot widen enough to stay above breakeven → economics gone.
- **Funding drag > spread income** over a rolling 24h → reduce q_max toward zero.
- **Exchange halt / degraded matching** → flatten all, kill immediately.

Re-deploy when markout is positive, inventory mean-reverts in paper, and the fee tier is restored. Pause-able like [[hyperliquid-market-making]] and [[funding-rate-arbitrage]]: the spread mechanism does not vanish, only the flow toxicity changes. See [[when-to-retire-a-strategy]].

## Advantages

- **Direction-neutral by construction** — no price forecast required; the maker warehouses only forced inventory.
- **High-frequency, high-Sharpe when flow is benign** — thousands of small round trips compound; pro books exceed Sharpe 3.
- **Fee rebates pay you** at top tiers — often the decisive edge on majors.
- **Deep, mature venues** — Binance/Bybit offer the deepest crypto books, tightest ticks, and richest MM programs.
- **Complements the on-chain book** — pairs with [[hyperliquid-market-making]] and [[funding-rate-arbitrage]] as a delta-neutral income sleeve across venues.

## Disadvantages

- **Requires algorithmic + low-latency infrastructure** — manual market making is impossible in modern electronic markets (Source: [[book-flash-boys]]); co-location and VIP status gate majors.
- **Adverse selection is the existential risk** — a minority of toxic fills dominates losses, brutal on thin alts.
- **Inventory risk is unbounded in trends** — the forced flatten is where drawdowns come from.
- **Fee structures make or break it** — even small fee/tier changes eliminate the majors edge.
- **Professional-dominated on majors** — retail cannot match Wintermute/GSR latency and capital; realistic retail edge is the riskier thin-alt tier.
- **Operationally intensive** — queue tracking, live markout/toxicity, funding accounting, rate limits.
- **Negative-skew, positive-mean** — looks great until a trending or toxic regime delivers the tail the spread was pricing.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=BTCUSDT` — current price for mid/marking
- `GET /api/v1/liquidity/depth` — per-coin depth/spread at 10/25/50/100 bps (book context, clip sizing)
- `GET /api/v1/derivatives/binance/funding-rates?symbol=BTCUSDT` — 8h funding for inventory carry
- `GET /api/v1/derivatives/binance/open-interest?symbol=BTCUSDT` — OI regime context
- `GET /api/v1/market-intelligence/taker-buy-sell` — taker buy/sell ratio by exchange (flow-toxicity context)

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1m&limit=1000` — OHLCV to estimate short-horizon realized σ
- `GET /api/v1/derivatives/binance/funding-rates?symbol=BTCUSDT&limit=500` — funding history for carry backtests
- `GET /api/v1/backtesting/klines` — deep archive for backtesting the quoter across regimes

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/liquidity/depth"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-regimes]].

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [order-book depth](https://cryptodataapi.com/quant-order-books) · [open interest](https://cryptodataapi.com/open-interest) · [liquidations](https://cryptodataapi.com/liquidations)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run the research and risk layers of this book (microsecond quoting itself lives on the exchange gateway):

- **Book context** — `GET /api/v1/liquidity/depth` for per-coin depth/spread at 10/25/50/100 bps (clip sizing, symbol selection), `GET /api/v1/market-intelligence/taker-buy-sell` as a flow-toxicity backdrop per venue
- **Regime gate** — `GET /api/v1/liquidity/regime` fragility score: widen quotes or pull when the book cannot absorb a shock; `GET /api/v1/derivatives/binance/open-interest` flags the long-skewed, liquidation-prone regimes worth leaning against
- **Carry** — `GET /api/v1/derivatives/binance/funding-rates?symbol=BTCUSDT` for the 8h funding on warehoused inventory (bias skew toward flat before each stamp)
- **Backtest** — Binance 1m klines from `GET /api/v1/backtesting/klines` exist only since 2026-03-30 (450+ USDT-perp markets, grows forward) — the only resolution meaningful for quoter replay; 1h bars back to 2017-08 support coarse σ/regime studies only. `GET /api/v1/backtesting/funding` (Binance daily since 2026-03-30) replays inventory carry
- **Tips** — markout and queue-position measurement require the exchange WS; use CDA to pick symbols where spread > adverse selection and to kill quoting when the liquidity regime turns fragile

## Related

- [[hyperliquid-market-making]] — the on-chain-CLOB counterpart; read both to see the shared A-S core and the CEX-vs-DEX cost/latency differences
- [[avellaneda-stoikov]] — the inventory-skew model parameterized here
- [[market-making]] — the microstructure concept underneath
- [[adverse-selection]] — the risk the spread compensates for; markout is the gauge
- [[funding-rate]] / [[funding-rate-arbitrage]] — carry on inventory and the adjacent delta-neutral sleeve
- [[liquidation-cascade-fade]] — the other side of the non-economic liquidation flow the maker leans against
- [[scalping]] / [[order-flow-scalping]] / [[vwap-trading]] — adjacent short-horizon strategies
- [[binance]] / [[bybit]] — the venues and their fee/MM-program schedules
- [[edge-taxonomy]] / [[failure-modes]] / [[when-to-retire-a-strategy]] — framing and kill-criteria methodology

## Sources

- [[book-trading-and-exchanges]] — Larry Harris's definitive treatment of market making: adverse-selection models (Glosten-Milgrom, Kyle), inventory management, and the economics of spread capture.
- [[book-algorithmic-and-high-frequency-trading]] — Cartea, Jaimungal, Penalva (2015): the mathematical framework for optimal market making, including the Avellaneda-Stoikov model and optimal quoting under adverse selection.
- [[book-high-frequency-trading-aldridge]] — Aldridge (2013): HFT market-making infrastructure, latency, and empirical MM profitability across venues.
- [[book-flash-boys]] — narrative account of the electronic-market-making infrastructure/latency arms race.
- Avellaneda, Stoikov, *High-frequency trading in a limit order book* (2008), Quantitative Finance — the reservation-price/optimal-spread model.
- Binance and Bybit public fee schedules and market-maker program documentation — VIP tiers, maker rebates, and 8-hour funding mechanics (see [[binance]], [[bybit]]).
