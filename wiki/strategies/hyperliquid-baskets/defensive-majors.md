---
title: "Defensive Majors (Hyperliquid Basket)"
type: strategy
created: 2026-06-16
updated: 2026-06-20
status: good
tags: [crypto, perpetual-futures, hyperliquid, risk-management, trend-following, momentum, quantitative]
aliases: ["Risk-Off Majors Basket", "BTC ETH SOL Defensive Long", "Crypto Capital Preservation Sleeve", "Majors Anchor Basket"]
related: ["[[hyperliquid-baskets-overview]]", "[[macro-trend-regime]]", "[[bitcoin-cycle-regime]]", "[[volatility-regime-classification]]", "[[full-bear-short-book]]", "[[oi-confirmed-trend]]", "[[trend-pullback-rally-fade]]", "[[major-trend-reclaim-rejection]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[hyperliquid-liquidation-engine]]", "[[hyperliquid-funding-rate-microstructure]]", "[[2025-03-jellyjelly-hlp-attack]]", "[[when-to-retire-a-strategy]]", "[[atr-position-sizing]]", "[[leverage]]", "[[volatility-regime-classification]]", "[[bitcoin-dominance-rotation]]", "[[spot-etf-flows]]"]
strategy_type: quantitative
timeframe: position
markets: [crypto]
complexity: intermediate
backtest_status: untested
edge_source: [risk-bearing, structural]
edge_mechanism: "Retail and leveraged altcoin holders bear disproportionate drawdown during uncertainty; majors retain liquidity and ETF-flow support that thinner tokens lack, so the patient long earns the risk-premium without the idiosyncratic wipeout."
data_required: [ohlcv, perp-funding, open-interest, volatility-regime-signal, bitcoin-dominance-data]
min_capital_usd: 5000
capacity_usd: 500000000
crowding_risk: low
expected_sharpe: 0.5
expected_max_drawdown: 0.35
breakeven_cost_bps: 15
kill_criteria: |
  - Basket drawdown > 35% from peak on a rolling 6-month basis
  - BTC closes below the 200-day MA for more than 20 consecutive days with negative ETF flows → reduce to minimum size
  - Rolling 6-month Sharpe < -0.5 while the [[volatility-regime-classification]] overlay signals elevated vol
---

# Defensive Majors (Hyperliquid Basket)

The Defensive Majors basket holds long perpetual positions in the highest-liquidity, highest-market-cap crypto assets — primarily BTC, ETH, and optionally SOL — with deliberately reduced leverage during periods of market uncertainty or elevated volatility. Its core mandate is **capital preservation and portfolio anchoring**, not alpha generation: it sacrifices upside convexity to remain solvent and positioned when other baskets are inactive or net-short.

*Part of the [[hyperliquid-baskets-overview|Hyperliquid basket library]].*

## Edge Source

**Risk-bearing** + **structural** (see [[edge-taxonomy]]).

- **Risk-bearing** — the basket earns the crypto equity risk premium by taking on the directional exposure that short-term traders and altcoin rotators are unwilling to hold through periods of uncertainty. The premium is real: BTC and ETH have historically delivered positive risk-adjusted returns over multi-month holding periods (Source: [[bitcoin-cycle-regime]]).
- **Structural** — BTC and ETH benefit from a structurally reinforced demand floor: [[spot-etf-flows|spot ETF inflows]] from institutional allocators, on-chain accumulation by long-term holders, and BTC's four-year halving cycle. These flows are largely inelastic to short-term volatility and provide support that altcoins lack entirely.

**Honest framing:** at low leverage this is essentially a risk-premium capture strategy with a volatility-regime overlay. The edge is modest and well-known. The basket earns its place by *surviving* conditions that flush higher-leverage altcoin positions.

## Why This Edge Exists

1. **Majors have institutional backstops that alts lack.** Spot BTC and ETH ETFs create structural demand from allocators who rebalance on drawdowns. This sets a soft floor that thinner tokens do not have. Source: [[institutional-flow-regime]], [[spot-etf-flows]].
2. **Volatility creates forced sellers who aren't you.** During elevated-vol regimes, leveraged altcoin holders face margin calls and liquidations; majors receive their liquidation flows as buyers rotate to safety within crypto. The defensive long sits on the receiving end of that rotation. Source: [[volatility-regime-classification]].
3. **Bitcoin dominance rises in uncertainty.** When risk appetite deteriorates, [[bitcoin-dominance-rotation|BTC dominance]] historically rises as capital concentrates in the perceived safer layer of crypto. The basket is over-weighted to that dynamic.
4. **Funding is often cheaper on majors.** In periods of uncertainty, retail leveraged-long activity — and thus positive funding that shorts earn — often concentrates in altcoins, not BTC. BTC funding can be near-zero or even negative (shorts pay longs) during corrections, providing benign carry for a defensive long. Source: [[hyperliquid-funding-rate-microstructure]].
5. **Counterparty:** short-term traders, leveraged altcoin speculators, and panic sellers who exit at the worst entry point for mean-reverting drawdowns.

## Null Hypothesis

Under no-edge conditions, BTC/ETH perps at low leverage simply replicate spot exposure minus funding costs and fees, delivering the underlying risk premium without strategy alpha. In a persistent bear market (falling lower highs, sustained negative ETF flows, deteriorating on-chain), the basket earns no premium and accumulates drawdown alongside the market. A prolonged sideways regime with positive funding also erodes returns via carry cost if the basket switches to net-positive-funding names.

**Disconfirming evidence to monitor:**
- BTC dominance falling while the basket is long majors only (rotating into alts would outperform).
- Spot ETF outflows sustained for more than 4 consecutive weeks (structural floor weakens).
- [[volatility-regime-classification]] confirming the vol overlay should have reduced size, but the basket remained full.
- Macro correlation spiking (crypto trading as high-beta Nasdaq); if equities correct sharply the "defensive" posture still posts large losses.

## Rules

**Universe.** BTC-PERP, ETH-PERP, and optionally SOL-PERP on [[hyperliquid|Hyperliquid]]. No altcoins. SOL inclusion is conditional on its [[liquidity-depth-regime|order-book depth]] supporting the target position size without meaningful market impact.

**Regime gate.** The basket is designed to be *active* during:
- [[macro-trend-regime]] in accumulation, early-bull, or bear-but-stabilising phase.
- [[volatility-regime-classification]] signal: compressed-to-moderate vol (not expansion).
- [[bitcoin-cycle-regime]] not in confirmed distribution (rising OI + price stalling + negative ETF flows = reduce).

**Entry:**
1. On basket activation (regime gate passes), establish BTC-PERP at 1.5–2x leverage, ETH-PERP at 1–1.5x, SOL-PERP at 1x (optional).
2. Build in thirds over 3 days to avoid block-entry slippage on large books.
3. Use limit orders near the [[vwap|VWAP]] of the prior session; never chase.

**Position sizing.** Allocate 20–35% of total book capital to this basket when active. Scale down via the [[atr-position-sizing]] overlay when 14-day ATR exceeds 1.5× its 90-day median. This is the portfolio's low-leverage anchor — over-sizing it defeats the defensive purpose.

**Exit / de-risk:**
- Reduce to 50% allocation if the [[volatility-regime-classification]] moves into expansion phase.
- Reduce to minimum (1% of book per leg) if BTC breaks below its 200-day MA and sustains below for 10 days.
- Full exit if the [[macro-trend-regime]] confirms a full-bear phase AND ETF flows are persistently negative — hand off to [[full-bear-short-book]].

**Funding management.** If BTC-PERP or ETH-PERP funding rate exceeds +0.10% per 8h (annualised ~136%), the carry cost materially erodes the defensive logic — trim to 50% and await normalisation. Deeply negative funding (shorts pay longs >0.05%/8h) is actually a tailwind; maintain full allocation.

## Implementation Pseudocode

```python
UNIVERSE = ["BTC", "ETH", "SOL"]  # SOL conditional on depth check
LEVERAGE  = {"BTC": 2.0, "ETH": 1.5, "SOL": 1.0}
MAX_ALLOC = 0.35   # fraction of book
MIN_ALLOC = 0.01   # skeleton when near-exit

def defensive_majors(state, book_size):
    # --- Regime gate ---
    if not state.macro_trend_regime.in_state(["accumulation", "early_bull", "range", "bear_stabilising"]):
        return []  # basket inactive; full-bear hands off to full-bear-short-book
    if state.volatility_regime == "expansion":
        alloc_scalar = 0.50  # half-size in vol expansion
    elif state.volatility_regime == "compressed":
        alloc_scalar = 1.00
    else:
        alloc_scalar = 0.75

    # --- ATR-based size reduction ---
    atr_scalar = 1.0
    for tok in UNIVERSE:
        atr14 = compute_atr(tok, 14)
        atr90_med = compute_atr(tok, 90, stat="median")
        if atr14 > 1.5 * atr90_med:
            atr_scalar = min(atr_scalar, 0.60)

    target_alloc = MAX_ALLOC * alloc_scalar * atr_scalar
    legs = []
    for tok in UNIVERSE:
        if tok == "SOL" and not hl_book_depth_ok(tok, target_alloc * book_size / 3):
            continue
        funding = perp_funding_8h(tok)
        if funding > 0.0010:          # >0.10%/8h → trim carry cost
            size_scalar = 0.50
        elif funding < -0.0005:       # deeply negative → tailwind, hold full
            size_scalar = 1.00
        else:
            size_scalar = 1.00
        notional = book_size * target_alloc / len(UNIVERSE) * size_scalar
        legs.append(long_perp(tok,
                               notional=notional,
                               leverage=LEVERAGE[tok],
                               margin="isolated",
                               order_type="limit_vwap"))

    # --- De-risk triggers ---
    if state.btc_below_200dma_days > 10 and state.etf_flows_negative_weeks >= 2:
        legs = [resize(l, l.notional * (MIN_ALLOC / MAX_ALLOC)) for l in legs]

    # --- Kill switch ---
    if state.basket_drawdown_6m > 0.35 or state.rolling_6m_sharpe < -0.5:
        return []  # flatten

    return legs
```

## Indicators / Data Used

- **[[volatility-regime-classification]]** — the primary size overlay; ATR and realized-vol regime determine whether to hold full or half allocation.
- **[[atr-position-sizing]] / [[average-true-range]]** — 14-day ATR vs 90-day median as the per-name size scaler.
- **[[funding-rate]]** — hourly funding on BTC-PERP / ETH-PERP via Hyperliquid `predictedFundings` endpoint; carries early-warning on crowd positioning and carry cost. Source: [[hyperliquid-funding-rate-microstructure]].
- **[[open-interest]]** — rising OI into a stalling price (distribution signal) triggers the de-risk ladder.
- **[[spot-etf-flows]]** — weekly ETF inflow/outflow data (Farside Investors, Bloomberg) as the structural-floor confirmation signal.
- **[[bitcoin-dominance-rotation]]** — BTC dominance rising signals flight to safety within crypto; supports the basket's thesis.
- **[[200-day-moving-average]]** — the BTC 200-day MA is the hard de-risk line.
- Data sources: [[coinglass]] (OI, liquidation heatmaps), [[cryptoquant]] (exchange flows), [[hypurrscan]] (Hyperliquid-native on-chain).

## Example Trade

**Illustrative — not a backtest.** Setup: early Q1 2026, post-correction, [[macro-trend-regime]] in "bear-stabilising" after a 30% BTC drawdown. ETF inflows positive for 3 weeks. [[volatility-regime-classification]] showing compressed vol. ATR back at 90-day median.

| Leg | Notional | Leverage | Entry (approx) | Hypothetical 8-wk exit | P&L |
|-----|----------|----------|----------------|------------------------|-----|
| BTC-PERP long | $35,000 | 2x | $62,000 | $78,000 (+26%) | +$9,100 |
| ETH-PERP long | $25,000 | 1.5x | $2,400 | $2,950 (+23%) | +$5,750 |
| SOL-PERP long | $15,000 | 1x | $120 | $148 (+23%) | +$3,450 |
| Funding earned (positive) | — | — | — | — | +$350 |
| Fees (taker + slippage) | — | — | — | — | −$180 |
| **Total** (on $75K deployed) | | | | | **+$18,470 (~25%)** |

*All figures illustrative. Actual outcomes depend on regime persistence, funding fluctuations, and execution quality.*

## Performance Characteristics

- **Return shape:** low-frequency, trending — most returns arrive during sustained bull or recovery phases; flat-to-negative in rangy or bear markets.
- **Expected Sharpe (illustrative estimate):** ~0.4–0.6 net over a full cycle. Low relative to higher-leverage baskets; the value is *survival and optionality* in adverse conditions.
- **Funding carry:** structurally near-neutral or mildly positive in most regimes; becomes a headwind when retail leverage spikes (positive funding) near tops.
- **Max drawdown estimate:** ~30–35% following BTC/ETH drawdowns in a bear phase — unavoidable without exiting into the [[full-bear-short-book]].
- **Realistic round-trip cost:** ~10–20 bps per leg per rebalance (maker/taker fees at low leverage, minimal slippage on liquid perps).
- **Correlation:** highly correlated to spot BTC/ETH — do not expect alpha over passive holding except through the volatility and funding overlays.

## Capacity Limits

BTC-PERP and ETH-PERP on Hyperliquid support multi-hundred-million dollar positions; SOL-PERP is shallower. Realistic strategy-level capacity is bounded by the total book size, not the venue — at small systematic-portfolio scale ($10K–$100K range) this basket operates well inside any liquidity constraint. At institutional scale ($50M+) BTC/ETH perps remain liquid but block-entry requires TWAP execution to avoid moving the mark. SOL-PERP caps out around $5–10M comfortable notional.

## What Kills This Strategy

The most likely failure modes (see [[failure-modes]]):

1. **Extended bear market.** The basket is long by design; a full bear regime (lower highs, persistent ETF outflows) will produce sustained drawdown. Mitigant: the regime gate and 200-day MA de-risk ladder exit before drawdown becomes terminal.
2. **Volatility expansion mis-timed.** A sudden vol expansion — cascade liquidation event, black-swan news — hits before the overlay reduces size. The 1.5–2x leverage limits the damage vs higher-leverage baskets.
3. **Funding cost spikes.** Near cycle tops, BTC/ETH funding can hit 0.20%+/8h (>270% annualised), rapidly eroding the defensive logic. The funding trim rule (>0.10%/8h → 50% size) mitigates but does not eliminate this.
4. **Bitcoin/Ethereum-specific systemic risk.** A protocol-level bug, regulatory action, or ETF suspension targeting BTC or ETH specifically would violate the structural-floor assumption. Low probability but not zero.
5. **Macro correlation shock.** During high-correlation regimes ([[crypto-macro-correlation-regime]]), BTC/ETH trade as high-beta Nasdaq; a sharp equity selloff (FOMC surprise, geopolitical shock) hits the basket despite it being "defensive" in crypto terms.
6. **Opportunity cost.** In a raging altcoin season ([[meme-speculative-regime]]), staying defensive in majors is correct risk management but produces large relative underperformance — a behavioural pressure to over-trade.

## Kill Criteria

See [[when-to-retire-a-strategy]] for the general framework. Specific numeric conditions:

- **Basket drawdown > 35%** from rolling 6-month peak → flatten, reassess regime.
- **BTC below 200-day MA for > 20 consecutive days AND ETF flows negative** → reduce to minimum size; hand directive to [[full-bear-short-book]].
- **Rolling 6-month Sharpe < −0.5** during elevated vol → full review; default to flatten.
- **Funding cost > 0.15%/8h sustained > 5 days** → trim to 25% allocation, not a kill but a structural stress flag.

## Advantages

- **Simplicity and clarity** — one regime gate, three liquid perps, defined ladders. Easy to monitor and audit.
- **Massive liquidity buffer** — BTC/ETH perps on Hyperliquid are the most liquid instruments on the venue; execution is clean even in stressed markets.
- **Low crowding risk** — this is not an obscure strategy; however, the basket's *safety function* means being long alongside many others is often correct (trend-following into strength).
- **Portfolio anchor function** — provides positive delta when the other baskets are inactive, so the system always has a market-facing position during constructive regimes.
- **Funding neutrality** — at low leverage, funding costs are manageable; near tops, the 0.10%/8h trim rule limits carry bleeding.

## Disadvantages

- **No alpha over spot** — the basket at its core replicates BTC/ETH spot exposure; the regime overlay and leverage add sophistication but not guaranteed alpha.
- **Drawdown in bear markets** — the basket is designed to reduce, not eliminate, bear-market exposure; persistent bears will still produce drawdowns before the kill switch fires.
- **Opportunity cost** — capital locked in low-leverage majors cannot chase high-conviction altcoin setups in the other baskets without sizing conflicts.
- **Regime gate lag** — trend-based regime detection is always somewhat lagged; the basket may be slow to exit into a deteriorating macro.
- **SOL liquidity risk** — SOL-PERP is materially thinner than BTC/ETH; in a risk-off cascade SOL can cascade 15–25% faster than BTC, breaking the "defensive" framing.

## Hyperliquid Execution Notes

- **Funding carry direction:** BTC and ETH funding on Hyperliquid tends to be mildly positive (longs pay) in trending markets and near-zero in flat markets. Rarely negative unless a significant short squeeze or market-wide deleveraging is underway. Monitor via `predictedFundings` API — the trim rule at >0.10%/8h prevents runaway carry cost. Source: [[hyperliquid-funding-rate-microstructure]].
- **Single-mark-tick liquidation + ADL:** Even at 2x leverage, a sustained 50%+ adverse move can approach liquidation territory; the 35% kill-switch drawdown is designed to close the position long before that. ADL is a risk at lower-leverage long positions only if a large counter-position triggers forced deleveraging. Source: [[hyperliquid-liquidation-engine]].
- **Isolated margin:** each leg runs in isolated margin — a catastrophic ETH move does not imperil the BTC or SOL leg. Do not use cross-margin on this basket.
- **JELLY-style thin-alt squeeze risk:** not applicable to BTC/ETH-PERP which have billions in daily volume and deep books. SOL-PERP warrants size discipline but is not in JELLY territory. If a new SOL listing or thin alt is ever considered for the universe, apply the JELLY liquidity screen. Source: [[2025-03-jellyjelly-hlp-attack]].

## Sources

- [[2026-06-03-cryptodataapi-14-basket-regime-framework]] — 14-basket regime framework; Defensive Majors as the risk-bearing anchor basket.
- [[macro-trend-regime]] — macro trend backdrop that gates this basket's activation.
- [[bitcoin-cycle-regime]] — BTC four-year cycle signals used for de-risk timing.
- [[volatility-regime-classification]] — the size overlay driving the alloc_scalar.
- [[spot-etf-flows]] — structural demand floor indicator; ETF outflow is the key de-risk signal.
- [[hyperliquid-funding-rate-microstructure]] — funding dynamics on BTC/ETH perps; the carry management framework.
- [[bitcoin-dominance-rotation]] — BTC dominance as a within-crypto risk-on/off signal.

## Related

[[hyperliquid-baskets-overview]] · [[trading-strategy-baskets]] · [[full-bear-short-book]] · [[oi-confirmed-trend]] · [[trend-pullback-rally-fade]] · [[major-trend-reclaim-rejection]] · [[market-regime]] · [[macro-trend-regime]] · [[bitcoin-cycle-regime]] · [[volatility-regime-classification]] · [[institutional-flow-regime]] · [[spot-etf-flows]] · [[bitcoin-dominance-rotation]] · [[atr-position-sizing]] · [[funding-rate]] · [[open-interest]] · [[perpetual-futures]] · [[hyperliquid]] · [[hyperliquid-funding-rate-microstructure]] · [[hyperliquid-liquidation-engine]] · [[breadth-and-momentum-divergence]] · [[breakout-and-retest]] · [[cross-sectional-relative-value]] · [[crowded-short-funding-fade]] · [[distribution-post-peak-short-book]] · [[edge-taxonomy]] · [[failure-modes]] · [[when-to-retire-a-strategy]]
