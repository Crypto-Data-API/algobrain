---
title: "Funding vs Basis Rotation"
type: strategy
created: 2026-07-19
updated: 2026-07-19
status: good
tags: [combinations, meta-strategy, arbitrage, funding-rate, derivatives, perpetual-futures, quantitative, crypto]
aliases: ["Carry Rotation", "Funding-Basis Switcher", "Perp-vs-Dated Carry Rotation"]
strategy_type: hybrid
timeframe: position
markets: [crypto]
complexity: advanced
backtest_status: untested

edge_source: [structural, analytical]
edge_mechanism: "Retail/leverage demand creates an excess structural premium in whichever carry instrument is currently in favour — perp funding when the crowd is long-perp, dated-futures basis when the calendar curve steepens; the rotation framework extracts the highest-available carry by switching between the two and avoids leaving premium on the table by sitting in the cheaper instrument while the better one is running."

data_required: [funding-rates, dated-futures-prices, spot-price, days-to-expiry, ohlcv-daily, open-interest]
min_capital_usd: 25000
capacity_usd: 500000000
crowding_risk: high

expected_sharpe: 1.4
expected_max_drawdown: 0.08
breakeven_cost_bps: 15

decay_evidence: "Both the perp-funding carry (BIS WP 1087, Schmeling et al. 2023) and the dated-futures basis carry have compressed since 2024 as Ethena/Resolv industrialised perp carry and ETF-arbitrage desks tightened the basis curve. The combination still holds value: the *relative* ranking between the two instruments is less crowded than either alone, and the rotation avoids the worst draw periods of each in isolation."

kill_criteria: |
  - strategy drawdown > 8% from high-water mark
  - annualised carry of the active instrument falls below 3% (cost floor: execution + venue fees consume the premium)
  - rolling 6-month Sharpe < 0.3 on minimum 12 rotation decisions
  - switching frequency exceeds 4 full rotations per calendar month for 2 consecutive months (regime is too noisy for stable carry harvesting)

related: ["[[funding-rate-arbitrage]]", "[[cash-and-carry]]", "[[basis-trading]]", "[[crypto-spot-perp-futures-triangle]]", "[[hl-vs-cex-funding-divergence]]", "[[carry-with-tail-hedge]]", "[[funding-filtered-momentum]]", "[[funding-skewed-grid]]", "[[funding-rate]]", "[[basis]]", "[[perpetual-futures]]", "[[open-interest]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
---

# Funding vs Basis Rotation

Funding vs basis rotation is an **allocation-layer strategy** that holds a single carry book on BTC/ETH and switches its expression — either perp-funding carry (long spot, short perpetual) or dated-futures basis carry (long spot, short a quarterly/monthly future) — depending on which instrument is currently paying a higher annualised yield, net of venue and execution costs. The primitive edge is structural carry; the overlay is dynamic selection of the highest-paying carry instrument. The strategy makes no directional bet; it is always market-neutral and always earning carry — the decision variable is *which carry* to earn.

This is explicitly the **allocation layer** between [[funding-rate-arbitrage]] (perp funding carry) and [[cash-and-carry]] / [[basis-trading]] (dated-futures basis carry), not a restatement of either. Those pages describe the primitives; this page describes the decision rule for choosing between them. The combination is additive because both primitives rely on the same long-spot hedge: the only cost of rotating is the close-and-reopen on the short leg when switching instruments, and that cost is bounded. The benefit is always earning the fatter carry.

This is differentiated from [[hl-vs-cex-funding-divergence]] — that strategy exploits the spread *between* funding rates across venues on the same instrument. This page exploits the spread *between instrument types* (perp vs dated future) on the same venue or across venues.

## Edge source

Per [[edge-taxonomy]], **structural + analytical**:

- **Structural (primary)** — both perp funding and dated-futures basis are structural premia: the perp settlement mechanism contractually transfers carry from the crowded directional side to the carry trader; the futures premium over spot reflects cost-of-carry, convenience yield, and leveraged-long demand for dated contracts. Neither premium requires forecasting direction.
- **Analytical (secondary)** — the rotation decision adds analytical edge: comparing two observable yields and picking the higher one. The counterparty to the analytical layer is the passive carry trader who stays in the lower-yielding instrument out of inertia, operational simplicity, or venue preference. The rotation framework captures the *premium difference* between instruments, not just the level of carry.

## Why this edge exists

**The two carry instruments are imperfect substitutes.** Perp funding and dated-futures basis move with partially independent drivers:

1. **Perp funding** is driven by *instantaneous* leveraged-long demand for perpetual exposure. It spikes in short-lived, sentiment-driven bull runs when traders want leveraged long exposure *without* an expiry date.
2. **Dated-futures basis** is driven by *term* leveraged demand: traders willing to roll a quarterly contract, institutionals using calendar futures (CME, Deribit), and basis arbitrage desks deploying capital across expiries. The basis curve can stay structurally steep even when perp funding is compressed, because institutional calendar demand is stickier than retail perp demand.

These two curves decorrelate in specific regimes: perp funding can spike while the basis is flat (retail-driven momentum), or the basis can steepen while perp funding is compressed (institutional accumulation into dated futures, hedged spot ETF demand). The rotation framework captures the dominant source of structural pay in each regime.

3. **Switch hysteresis prevents churn.** The rotation does not trigger on every tick of relative value. A threshold buffer (the carry differential must exceed switching costs × a multiplier, sustained for a minimum confirmation period) ensures the trade only rotates when the relative advantage is genuine, not noise. This hysteresis is the key operational discipline.

**Who is on the other side:** the passive carry trader who stays in whichever instrument they habitually trade, forfeiting 10-100+ bps annually by not optimising the instrument selection.

## Null hypothesis

Under the null, the carry differential between perp funding (annualised) and dated-futures basis (annualised) is mean-zero and unpredictable. Specifically:
- The annualised yield of the "winning" instrument at rotation time should not exceed the "losing" instrument's yield in the subsequent hold period, net of switching costs.
- The aggregate carry collected by the rotation strategy should not differ materially from a static commitment to either instrument alone.
- Switching frequency should have no relationship with carry improvement — rotating more often should not improve performance.

The null is currently not rejected in this wiki (`backtest_status: untested`). Testable prediction: regress the carry premium of the chosen instrument minus the unchosen instrument (post-rotation) on the carry differential at rotation time; a positive, statistically significant slope rejects the null and validates the decision rule.

## Rules

### Carry measurement

Define the annualised carry of each instrument net of one-way execution cost:

**Perp carry (C_perp):**
```
C_perp = funding_8h_rate × 3 × 365 × 100  — (taker_fee_bps × 2 / 100)
```
`funding_8h_rate` = current 8h rate (e.g. 0.01% = 0.0001). Three periods per day. Subtract estimated round-trip fee annualised (small at multi-week holding periods, but non-trivial for high-frequency entries).

**Basis carry (C_basis):**
```
C_basis = (futures_price / spot_price − 1) × (365 / days_to_expiry) × 100 — (taker_fee_bps × 2 / 100) — roll_cost_bps / hold_period_years
```
`roll_cost_bps` = estimated cost to roll to the next contract before expiry.

Both expressed as **net annualised % yield** on the spot-neutral hedge.

### Active-instrument decision rule

1. **On initialisation or review (every 8h):** compute C_perp and C_basis for each available expiry (front, quarterly, back-quarter).
2. **Stay in current instrument** unless the alternative's carry exceeds the current instrument by the **switch threshold**:
   ```
   switch if: C_alternative − C_current > SWITCH_THRESHOLD
   ```
   `SWITCH_THRESHOLD` = 2.0% annualised by default. Rationale: at $100K deployed, 2% = $2,000/year marginal gain; if the switch costs $100 in fees and slippage (2 × taker), the threshold is cleared when the differential persists for >18 days — a realistic minimum hold.
3. **Confirmation period:** the differential must persist for a minimum of **2 consecutive 8h periods** before the rotation executes (avoids flipping on a single anomalous funding spike or thin-order-book basis print).
4. **Dated-futures expiry selection:** prefer contracts with ≥ 30 days to expiry (eliminates roll-convergence drag that compresses annualised basis near expiry). Within that, prefer the contract with the highest C_basis. Recompute every 8h.

### Rotation execution

1. **Close the short leg** of the departing instrument (close the perp short, or buy back the dated future). Use limit orders where possible; accept taker on the dated-futures leg if the spread is thin.
2. **Open the short leg** of the incoming instrument. No change to the long spot leg — the spot book does not rotate.
3. **Cost budget**: tolerate up to **SWITCH_THRESHOLD / 2 × hold_period_years** in execution cost before the rotation erodes its own premium.

### Position sizing

- Long spot notional: fixed for the duration of the carry book; rotations only change the short leg.
- Max deployed capital: operator-defined; carry is not vol-scaled (it is market-neutral).
- Reserve 10% cash buffer for margin on the short leg (dated futures may require larger initial margin than perps; buffer avoids forced liquidation if spot price moves).

### Kill conditions

- Annualised carry of both instruments < 3%: no viable carry to earn; park in spot and wait.
- Extreme funding (> 0.10%/8h on perp): high risk of perp squeeze / basis blowout; reduce the short leg, do not add.
- Regime = `Structural Shock` (via `/api/v1/regimes/current`): the basis and funding can gap violently in crash regimes; flatten the short legs.

## Implementation pseudocode

```python
# funding_vs_basis_rotation.py — allocation layer between perp and dated carry

from dataclasses import dataclass, field
from typing import Optional

# ---- constants ----
SWITCH_THRESHOLD_PCT   = 2.0      # annualised % differential to trigger rotation
CONFIRM_PERIODS        = 2        # consecutive 8h periods differential must hold
MIN_CARRY_PCT          = 3.0      # below this, no instrument is worth trading
MIN_EXPIRY_DAYS        = 30       # avoid near-expiry convergence drag
EXTREME_FUNDING_8H     = 0.0010   # 0.10%/8h: reduce risk
CASH_BUFFER_PCT        = 0.10     # margin reserve on short leg
DRAWDOWN_KILL          = 0.08

@dataclass
class InstrumentCarry:
    name: str          # "perp" | "front_quarter" | "back_quarter"
    carry_ann_pct: float    # net annualised carry after fees
    days_to_expiry: Optional[int]   # None for perp

@dataclass
class RotationState:
    active: str        # current instrument name
    confirm_counter: int = 0
    candidate: Optional[str] = None

def best_instrument(carries: list[InstrumentCarry]) -> InstrumentCarry:
    eligible = [c for c in carries
                if c.carry_ann_pct >= MIN_CARRY_PCT
                and (c.days_to_expiry is None or c.days_to_expiry >= MIN_EXPIRY_DAYS)]
    if not eligible:
        return None
    return max(eligible, key=lambda c: c.carry_ann_pct)

def rotation_decision(state: RotationState, carries: list[InstrumentCarry],
                      funding_8h: float, regime: str, book_drawdown: float) -> dict:
    # kill conditions
    if book_drawdown > DRAWDOWN_KILL:
        return {"action": "FLATTEN_SHORTS", "reason": "drawdown kill"}
    if funding_8h > EXTREME_FUNDING_8H:
        return {"action": "REDUCE_PERP_SHORT", "reason": "extreme funding — squeeze risk"}
    if regime == "Structural_Shock":
        return {"action": "FLATTEN_SHORTS", "reason": "structural shock regime"}

    best = best_instrument(carries)
    if best is None:
        return {"action": "PARK", "reason": "no carry above minimum"}

    current_carry = next((c.carry_ann_pct for c in carries if c.name == state.active), 0.0)
    differential = best.carry_ann_pct - current_carry

    if best.name == state.active:
        # no rotation needed; reset confirmation
        state.confirm_counter = 0
        state.candidate = None
        return {"action": "HOLD", "active": state.active,
                "carry_ann_pct": current_carry}

    if best.name != state.candidate:
        # new candidate — reset confirmation
        state.candidate = best.name
        state.confirm_counter = 1
        return {"action": "WAIT_CONFIRM", "candidate": best.name,
                "differential_pct": differential, "periods_remaining": CONFIRM_PERIODS - 1}

    state.confirm_counter += 1
    if state.confirm_counter >= CONFIRM_PERIODS and differential >= SWITCH_THRESHOLD_PCT:
        state.active = best.name
        state.confirm_counter = 0
        state.candidate = None
        return {"action": "ROTATE",
                "from": carries[0].name,   # placeholder: previous active
                "to": best.name,
                "differential_pct": differential,
                "note": "close old short leg, open new short leg; spot unchanged"}

    return {"action": "WAIT_CONFIRM", "candidate": best.name,
            "differential_pct": differential,
            "periods_remaining": CONFIRM_PERIODS - state.confirm_counter}
```

The production system adds: real-time funding polling via the CryptoDataAPI derivatives endpoint; dated-futures prices from the exchange API; a carry ledger tracking basis income per unit of basis carry vs funding income per unit of perp carry; and a daily attribution report separating rotation alpha from carry beta.

## Indicators / data used

- **[[funding-rate]] (8h)** — primary perp carry signal. Polled at every 8h settlement period.
- **Dated-futures price + spot price + days-to-expiry** — annualised basis calculation.
- **[[open-interest]] per instrument** — secondary signal: which instrument carries more leveraged-long demand, confirming the carry signal.
- **Regime classification** — `/api/v1/regimes/current` to detect crash/shock regimes where the basis can gap.
- **Taker buy/sell ratio** — `/api/v1/market-intelligence/taker-buy-sell` as a secondary sentiment check: extreme taker buy pressure is consistent with elevated perp funding and may precede a basis spike on the dated curve.

## Example trade

**Setup (illustrative, not a historical backtest):**

- Asset: BTC. Book size: $100,000 long spot (held constant).
- **Period 1 (perp active):** BTC funding = +0.030%/8h (≈ 32.9% APY). Quarterly future (90 DTE) annualised basis = 12.1%. C_perp net ≈ 32.9% − 0.9% (fees) ≈ **32.0% ann.** C_basis net ≈ 12.1% − 0.5% ≈ **11.6% ann.** → Carry perp; earn ~$32,000/year on $100K deployed.
- **Period 2 (rotation signal):** BTC funding drops to +0.006%/8h (≈ 6.6% APY) — perp market has cooled. Quarterly future (80 DTE) basis: $103,200 vs spot $100,000 → (3.2%) × 365/80 ≈ **14.6% ann.** C_perp net ≈ 5.7%. C_basis net ≈ 14.1%. Differential = 8.4% > 2.0% threshold. Held for 2 consecutive 8h periods → **ROTATE.**
- **Rotation cost:** Close BTC perp short (taker, 0.045% on $100K = $45). Open quarterly short (taker, 0.04% = $40). Total switching cost: **$85**.
- **Post-rotation (hold 60 days to near expiry):** Earn basis carry: 14.1% × (60/365) × $100,000 ≈ **$2,318**. Minus carry earned if stayed in perp at 5.7% × 60/365 × $100K ≈ $937. Rotation gain (gross): **+$1,381**, minus $85 switching cost = **+$1,296** marginal benefit from rotating (net, over 60 days on $100K).

**Net round-trip carry (perp 30 days + basis 60 days on $100K):** ≈ $2,630 + $2,318 − $85 = **$4,863** (~17.7% annualised blended, vs staying in perp alone at 32% for 30 days then 5.7% for 60 days = ~$2,630 + $937 = $3,567, so rotation added ~+$1,296 over the period).

*(Illustrative. Actual results depend on funding, basis, and execution quality.)*

## Performance characteristics

| Metric | Value | Note |
|---|---|---|
| Expected net Sharpe | ~1.4 | Carry strategies have high Sharpe in normal markets; the rotation adds analytical edge, estimated +0.1-0.3 vs static perp-only carry |
| Expected max drawdown | ~8% | Carry drawdowns come from basis blowouts or perp squeezes; kill triggers contain these |
| Active instrument | ~65% perp, 35% basis (rough historical estimate) | Perp funding has historically dominated; the basis leg is primarily active in post-bull compression regimes |
| Rotation frequency | ~2-6 switches/year (design target) | Hysteresis ensures low churn; switching costs are small relative to carry differential |
| Breakeven cost budget | 15 bps round-trip | Carry strategies can absorb low costs; the rotation adds ~1-3 switches × $100-200 cost per switch annually |

**Cost overlay:**
- Perp entry/exit: ~4-9 bps taker (Hyperliquid) or ~4-10 bps on Binance.
- Dated futures entry/exit: ~4-10 bps taker on major venues (CME Bitcoin futures: ~0.5 bps, but minimum notional is large).
- Spot leg: held constant; no rotation cost on the long side.
- The rotation adds a bounded switching cost: at 4 full rotations per year × $100 per rotation = $400 on $100K (0.4% annual drag) — offset by a differential of 2%+ per rotation trigger.

## Capacity limits

- **Perp carry (short leg):** the perp funding carry is bounded by how much long-spot / short-perp inventory the market can absorb without moving funding toward zero. At ~$500M+ notional deployed across the market, arb desks have historically compressed perp funding. Reflected in `capacity_usd: 500000000` (shared ceiling with the underlying carry primitives).
- **Basis carry (short leg):** on CME Bitcoin futures, open interest exceeds $30B; on Deribit and Binance quarterly futures, aggregate OI is $5-15B. The rotation strategy's basis leg can scale to hundreds of millions before creating self-reinforcing basis compression.
- **Binding constraint:** the *decision rule* itself has no capacity constraint — it is pure algebra on observable prices. The constraint is the underlying instrument capacity.

## What kills this strategy

Mapped to [[failure-modes]]:

1. **Basis blowout in crash regime (#6).** During a sharp sell-off, the basis on dated futures can invert (futures trade below spot as sellers dump futures contracts); simultaneously, perp funding can go deeply negative. Both carry instruments are suddenly paying nothing or paying negative — the carry book earns zero while the long spot leg marks down. The carry level itself is not at risk (the book is delta-neutral) but the regressive P&L during the shock can trigger the drawdown kill.
2. **Carry compression crowding (#4).** Both perp carry and basis carry have been compressed by systematic arb desks since 2024 (Ethena/Resolv on perps; ETF arbitrage on dated futures). If both converge to near-zero simultaneously, the rotation framework has nothing to switch between.
3. **Venue risk (#7).** The strategy simultaneously relies on a spot venue (long), a perp venue (short leg option A), and a dated-futures venue (short leg option B). A venue failure — Hyperliquid exploit, FTX-style insolvency — during active positions creates an unhedged directional book. Operating across regulated/trusted venues and maintaining per-venue exposure caps mitigates this.
4. **Basis curve noise near expiry (#5).** Within 10 days of a futures expiry, the annualised basis collapses due to convergence even when the carry was genuine. The 30-day minimum expiry filter prevents entering a basis position that will immediately compress.
5. **Switch-cost underestimation (#7: Operational).** If execution costs are misjudged (especially on less-liquid dated futures), the rotation erodes its own premium. The 2% switch threshold includes a buffer for this; it fails if slippage is persistently above estimates.

## Kill criteria

Pause (not retire) on any of:

1. **Carry book drawdown > 8%** in any rolling 30-day window.
2. **Both instruments' annualised carry < 3% net** for 14+ consecutive days — no viable carry; park in spot.
3. **Rolling 6-month Sharpe < 0.3** on minimum 12 rotation decisions — the decision rule is not adding analytical value.
4. **Switching frequency > 4 full rotations per calendar month for 2 consecutive months** — the carry signals are unstable; the hysteresis threshold must be recalibrated.

See [[when-to-retire-a-strategy]] for the broader framework.

## Advantages

- **Always earning carry:** the book is never flat (unless both instruments are below the minimum carry floor). The rotation ensures the strategy is always in the higher-yielding carry instrument available.
- **No new positions to learn:** the rotation uses the same long-spot / short-derivative structure as the underlying primitives. The only new skill is computing relative yields and confirming the switch.
- **Delta-neutral throughout:** both legs are market-neutral. A rotation does not introduce directional exposure.
- **Hysteresis reduces churn:** the confirmation period and minimum differential filter prevent the strategy from switching on noise, keeping switching costs bounded.
- **Naturally separates two regimes:** perp carry is dominant in retail-driven momentum regimes; basis carry is dominant in institutional, steady-accumulation regimes. The rotation is implicitly a regime classifier for the *type* of bullish leverage in the market.

## Disadvantages

- **Complexity overhead:** maintaining two types of short positions (perp and dated futures) requires managing different margin structures, different settlement mechanics, and different roll schedules. The operational complexity is non-trivial.
- **Both instruments can be compressed simultaneously:** in a carry drought (low funding, flat basis curve — often in deep bear markets), the rotation framework has nothing to do. The strategy is inactive exactly when passive carry traders are also idle.
- **Switching costs are not always bounded:** if basis or funding exhibits a rapid oscillation pattern (spike-and-compress several times per month), the confirmation period will trigger repeated switches, and cumulative switching costs can exceed the carry differential.
- **Roll risk on dated futures:** a dated futures position must be rolled before expiry. The cost and execution of the roll affect the realised carry. Perp positions have no explicit roll, but pay/receive funding continuously — a different risk texture.
- **Requires multi-venue infrastructure:** running two potential short-leg instruments simultaneously (to be able to switch without delay) requires margin posted at multiple venues — capital-inefficient for small books.

## Sources

- BIS Working Papers No 1087, *Crypto carry* — Schmeling, Schrimpf, Todorov (BIS, 2023). Documents the structural premium in perp funding driven by leveraged retail; the regime-dependence of carry magnitude is the foundation for the rotation decision. https://www.bis.org/publ/work1087.pdf
- He, Manela, Xu, Yan (2022/2024), *Fundamentals of Perpetual Futures*. Documents perp funding as a convergence mechanism and its relationship to dated-futures basis; the two instruments' co-movement and divergence is the rotation opportunity. arxiv.org/abs/2212.06888.
- [[cash-and-carry]] — the dated-futures basis carry primitive and its cost structure.
- [[funding-rate-arbitrage]] — the perp funding carry primitive and its decay dynamics.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — current 8h funding rate; primary perp carry input
- `GET /api/v1/market-intelligence/funding-rates` — cross-exchange funding (top coins, default HL); cross-venue confirmation
- `GET /api/v1/market-intelligence/open-interest` — cross-exchange OI; confirms which instrument has more leveraged-long demand
- `GET /api/v1/regimes/current` — regime classification; triggers the crash-regime kill

**Historical data:**
- `GET /api/v1/derivatives/binance/funding-rates?symbol=BTCUSDT&limit=500` — funding history for rotation backtest
- `GET /api/v1/derivatives/binance/history?days=90` — daily derivatives series (funding + OI) for regime and carry analysis
- `GET /api/v1/backtesting/funding` — deep funding archive (2020+) for multi-regime carry comparison
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=200` — spot OHLCV for the delta-neutral hedge computation

Note: dated-futures prices (quarterly/monthly BTC/ETH contracts) must be sourced from exchange APIs directly (Binance, CME, Deribit) — CryptoDataAPI covers perp funding and OI comprehensively; it does not currently document a specific dated-futures price series endpoint. Annualised basis must be computed from `futures_price / spot_price` using exchange-native dated-futures feeds.

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/funding-rates?coin=BTC"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-intelligence]], [[cryptodataapi-regimes]].

## Related

- [[funding-rate-arbitrage]] — the perp carry primitive; one of the two instruments in the rotation
- [[cash-and-carry]] — the dated-futures basis carry primitive; the other rotation option
- [[basis-trading]] — the theory of basis formation and convergence
- [[crypto-spot-perp-futures-triangle]] — the three-instrument spread that includes both rotation legs
- [[hl-vs-cex-funding-divergence]] — cross-venue funding divergence (different axis: venue spread, not instrument spread)
- [[carry-with-tail-hedge]] — carry book with tail-risk overlay; stackable with this rotation
- [[funding-filtered-momentum]] — funding as a filter on momentum; shares the funding data rail
- [[funding-skewed-grid]] — carry as a grid skew; a different carry-enhancement approach
- [[funding-rate]] — the contract mechanism behind perp carry
- [[basis]] — the concept underlying dated-futures carry
- [[perpetual-futures]] — the instrument carrying the perp leg
- [[edge-taxonomy]] — structural + analytical edge classification
- [[failure-modes]] — basis blowout, carry compression, venue risk
- [[when-to-retire-a-strategy]] — kill vs pause framework
