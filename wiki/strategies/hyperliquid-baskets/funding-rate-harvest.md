---
title: "Funding-Rate Harvest (Hyperliquid Basket)"
type: strategy
created: 2026-06-16
updated: 2026-07-13
status: good
tags: [crypto, perpetuals, hyperliquid, funding-rate, quantitative, derivatives, risk-management]
aliases: ["Perp Funding Carry", "Funding Yield Harvest", "Delta-Neutral Funding Collect", "HL Carry Basket"]
related: ["[[hyperliquid-baskets-overview]]", "[[basis-carry-regime]]", "[[derivatives-native-regime]]", "[[funding-rate-arbitrage]]", "[[crowded-short-funding-fade]]", "[[crowded-long-funding-fade]]", "[[volatility-carry]]", "[[pairs-trading]]", "[[statistical-arbitrage]]", "[[grid-trading]]", "[[funding-rate]]", "[[hyperliquid-funding-rate-microstructure]]", "[[hyperliquid-liquidation-engine]]", "[[hyperliquid-vault-architecture]]", "[[open-interest]]", "[[perpetual-futures]]", "[[basis]]", "[[funding-by-hour]]", "[[coinglass]]", "[[hypurrscan]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[cryptodataapi]]"]
strategy_type: quantitative
timeframe: swing
markets: [crypto]
complexity: intermediate
backtest_status: naive-backtested
edge_source: [structural, risk-bearing]
edge_mechanism: "Perpetual futures carry a persistent funding premium because speculative demand for leveraged long (or short) exposure exceeds the supply of counterparties willing to take the other side; the harvest captures this structural imbalance by running on the paid side of the trade with minimal directional exposure."
data_required: [perp-funding, open-interest, liquidation-feed, order-book-depth, funding-rate-history, spot-price]
min_capital_usd: 10000
capacity_usd: 25000000
crowding_risk: high
expected_sharpe: 1.0
expected_max_drawdown: 0.18
breakeven_cost_bps: 25
kill_criteria: |
  - Rolling 30-day annualised funding yield falls below 8% APY across the basket (carry has compressed; edge arb'd away)
  - Drawdown > 15% on this basket over rolling 6 months
  - Three consecutive months of negative net P&L after funding income
  - Single-leg liquidation event (isolated margin breach) on any position
---

# Funding-Rate Harvest (Hyperliquid Basket)

A **delta-neutral or near-neutral carry strategy** that collects [[funding-rate|funding payments]] from the leveraged side of perpetual futures markets without taking significant directional price risk. When funding is persistently positive (longs paying shorts), the basket opens a short perp position to collect the rate; when persistently negative (shorts paying longs), it opens a long. Where possible, directional exposure is hedged with an offsetting spot or equivalent position to isolate the funding yield. The strategy works best during rangebound, high-leverage market conditions where the underlying asset's price drifts predictably while funding remains elevated.

*Part of the [[hyperliquid-baskets-overview|Hyperliquid basket library]].*

---

## Edge Source

**Structural** + **risk-bearing** (see [[edge-taxonomy]]).

- **Structural (primary).** The funding rate mechanism in perpetual futures is a structural market-plumbing feature: the rate is mechanically determined by the deviation of the perp's mark price from the underlying oracle price. When retail demand for leveraged exposure skews persistently to one side, the funding rate reflects a genuine supply-demand imbalance between those wanting levered directional exposure and those willing to be their counterparty. That imbalance is systematic and recurring — not a random noise event to be timed.
- **Risk-bearing (secondary).** The harvest strategy is essentially providing directional liquidity to the levered speculative side. The risk is directional mark-to-market loss; the compensation is the funding stream. In a pure delta-neutral hedge, the risk-bearing is bounded; in a near-neutral or single-leg version, the residual directional exposure is the source of both additional upside and the primary failure mode.

**Relationship to [[funding-rate-arbitrage]]:** The [[funding-rate-arbitrage]] strategy typically runs a full "cash-and-carry" construction — short perp + long spot on the same asset, fully hedged. The harvest basket here runs a **single-leg perp carry** (or near-neutral partial hedge), sacrificing full delta-neutrality for operational simplicity. The two strategies sit on a spectrum:
- Full arbitrage (cash-and-carry): zero directional risk, requires capital on both spot and perp legs.
- Harvest (this basket): minimal to zero hedge on the spot leg, accepts residual directional exposure, requires less capital but carries more mark-to-market risk.

See [[funding-rate-arbitrage]] for the fully-hedged version. This basket is the **funding-yield-focused sibling** that trades some of the neutrality for operational flexibility and capital efficiency.

---

## Why This Edge Exists

Crypto perpetuals carry a systematic positive-funding bias in bull markets. The mechanism:

1. **Retail demand is long-biased.** Most individual traders on Hyperliquid want leveraged upside exposure. This creates persistent excess long demand for perp contracts relative to the supply of natural shorts.
2. **The funding rate restores equilibrium.** As the perp mark trades above oracle, the hourly funding rate rises, making long positions more expensive to hold and incentivising shorts to enter. The harvest takes the short (or long in bear regimes) position that this mechanism incentivises.
3. **The premium is structural, not ephemeral.** BIS Working Paper 1087 (Schmeling, Schrimpf, Todorov 2023) documents persistent funding-rate premia in crypto perps across multiple years and market regimes, with annualised Sharpe ratios of 0.8–1.5 on carry strategies. The persistence reflects the structural long-bias of retail crypto participation, which does not disappear cycle-to-cycle.
4. **Hyperliquid's hourly cadence amplifies capture.** On an 8h CEX, a funding spike of +0.2%/h that lasts only 3 hours produces only ~0.6% total funding income on a $1M position. On Hyperliquid, the same spike produces 3 × 0.2% = 0.6% capture in 3 separate hourly settlements. The arithmetic is the same, but the hourly granularity means entries and exits can be timed to the spike — a CEX operator must hold through the entire 8h window to collect. Source: [[hyperliquid-funding-rate-microstructure]].

**Who is on the other side?** Retail leveraged long-holders who are paying 40–100% APY annualised to maintain directional exposure. They accept this cost because their expected price appreciation (or fear of missing out) exceeds the funding cost — or because they don't realise how much the cost compounds over time.

---

## Null Hypothesis

Under "no edge," funding rates are fairly priced: the carry income is exactly offset by the expected adverse mark-to-market returns (the asset appreciates when you are short, or depreciates when you are long). The harvest would net to zero or negative after costs.

Empirically, this null is rejected in historical data for the long-funding-collect-short (bull-regime) version: crypto assets do *not* systematically appreciate by the amount of funding paid during elevated-funding periods. The funding income exceeds average adverse price moves over the holding period across most trailing samples. However, the null is *not* rejected for individual events (a 50% price rally while short wipes more carry than several months of elevated funding), and regime-shift events remain dangerous.

**Disconfirming evidence to monitor:**
- Annualised funding yield across the basket falls below 8% APY — funding has compressed to where carry barely covers fees and risk.
- Major pairs (BTC, ETH) show funding persistently *below* the interest baseline (~0.00016%/h) — indicating the structural long bias has reversed or been arb'd away.
- A significant price move against the position direction erases more than 3 months of collected funding — the carry/risk tradeoff has broken down.
- New large-scale delta-neutral carry funds (Ethena-style) have industrialised the trade and compressed the yield to near-baseline.

---

## Rules

**Universe:** Hyperliquid perp markets where funding is elevated relative to baseline. Selection criteria:
- Hourly funding rate > +0.015%/h (+13% APY) for short-collect positions, OR < −0.015%/h for long-collect positions — a threshold meaningfully above the ~0.00016%/h interest baseline.
- Daily volume > $5M (minimum execution quality).
- Position must survive a 20% adverse price move without liquidation at chosen leverage.

Priority assets: BTC, ETH, SOL for stability and depth. FARTCOIN-class memecoins can have exceptional carry (64% APY) but with high squeeze risk — size them at ≤ 0.5% of basket equity. See [[hyperliquid-funding-rate-microstructure]] for the FARTCOIN example.

**Near-neutral construction (preferred):**
- Open a perp position on the side that collects funding (short if positive funding, long if negative).
- Hedge 50–80% of the directional notional via a spot purchase or sale on a CEX (Binance, Bybit, Coinbase) where the asset has deep spot liquidity.
- Residual 20–50% directional exposure is accepted as a calculated risk in exchange for reduced capital requirements and the ability to concentrate in higher-yielding, less-liquid assets.

**Single-leg construction (simplified, for assets without hedgeable spot):**
- Open only the perp position.
- Accept full directional exposure.
- Compensate with smaller position size (max 2% of equity) and tighter stop-loss.

**Entry:** Enter when funding has been above/below the threshold for ≥ 3 consecutive hours (confirmed elevated, not a transient spike). Use limit orders at the best available bid/ask to minimise taker fees. Near the hourly settlement mark (last ~5 minutes), funding is "locked in" for that hour — entering just before settlement captures the first collection without waiting.

**Exit — carry-driven:**
- Close when funding returns to within 20% of the 30-day mean (carry has normalised; the premium has been collected).
- On Hyperliquid's hourly cadence, this is often 1–7 days of holding.

**Exit — risk-driven:**
- Hard stop: directional loss (on the perp leg) exceeds 3 months of collected funding income.
- Maximum hold: 14 days. If funding hasn't normalised in 14 days, it may be structural at that level and a dedicated arb desk is likely compressing it — exit and reassess.

**Sizing:** 3–8% of basket equity per position (near-neutral) or 1–2% (single-leg). Aggregate basket notional capped at 40% of equity — this is a carry sleeve, not a directional sleeve.

---

## Implementation Pseudocode

```python
# Funding-Rate Harvest — basket module
# Regime: basis-carry-regime + derivatives-native-regime
# Target: near-neutral perp carry with partial spot hedge

FUNDING_ENTRY_LONG   = -0.00015    # collect when short-paying: < -0.015%/h
FUNDING_ENTRY_SHORT  = 0.00015     # collect when long-paying: > +0.015%/h
MIN_SUSTAINED_HOURS  = 3           # confirmed elevated, not transient
HEDGE_RATIO          = 0.65        # hedge 65% with spot leg
LEVERAGE             = 2.0         # conservative; isolated margin
SIZE_HEDGED          = 0.06        # 6% equity — near-neutral positions
SIZE_UNHEDGED        = 0.015       # 1.5% equity — single-leg positions
MAX_HOLD_DAYS        = 14
MAX_BASKET_NOTIONAL  = 0.40        # 40% of equity aggregate cap

def evaluate_funding_harvest(pair, state, equity):
    funding_hours = get_hourly_funding_history(pair, hours=3)
    funding_now = funding_hours[-1]
    oi_30d_mean = rolling_mean(get_oi_history(pair), days=30)
    spot_available = has_deep_spot_market(pair)    # CEX spot hedge available

    # Skip if basket already at notional cap
    if state.basket_notional_pct(equity) >= MAX_BASKET_NOTIONAL:
        return

    # Long-collect (funding negative — shorts paying longs)
    if all(f < FUNDING_ENTRY_LONG for f in funding_hours):
        size_pct = SIZE_HEDGED if spot_available else SIZE_UNHEDGED
        notional = equity * size_pct * LEVERAGE
        entry_px = get_mark_price(pair)
        state.open_long_perp(pair, notional, entry_px,
                             deadline_days=MAX_HOLD_DAYS, tag="funding-harvest-long")
        if spot_available:
            spot_notional = notional * HEDGE_RATIO
            state.open_short_spot(pair, spot_notional,
                                  venue="cex", tag="funding-harvest-hedge")

    # Short-collect (funding positive — longs paying shorts)
    elif all(f > FUNDING_ENTRY_SHORT for f in funding_hours):
        size_pct = SIZE_HEDGED if spot_available else SIZE_UNHEDGED
        notional = equity * size_pct * LEVERAGE
        entry_px = get_mark_price(pair)
        state.open_short_perp(pair, notional, entry_px,
                              deadline_days=MAX_HOLD_DAYS, tag="funding-harvest-short")
        if spot_available:
            spot_notional = notional * HEDGE_RATIO
            state.open_long_spot(pair, spot_notional,
                                 venue="cex", tag="funding-harvest-hedge")

    # Exit logic (run separately)
    if state.has_position(pair):
        pos = state.get_position(pair)
        funding_now = get_hourly_funding(pair)
        funding_30d = rolling_mean(get_hourly_funding_history(pair, days=30))
        cumulative_carry = state.funding_collected(pair)
        directional_loss = state.perp_mark_to_market_loss(pair)

        # Carry normalised — primary exit
        within_20pct_of_mean = abs(funding_now - funding_30d) <= 0.20 * abs(funding_30d)
        if within_20pct_of_mean:
            state.close_all_legs(pair, tag="carry-normalised")
        # Risk stop: directional loss > 3 months collected carry
        elif directional_loss > 3 * cumulative_carry:
            state.close_all_legs(pair, tag="carry-ratio-stop")
        # Time stop
        elif state.days_held(pair) >= MAX_HOLD_DAYS:
            state.close_all_legs(pair, tag="time-stop")
```

---

## Indicators / Data Used

- **[[funding-rate]] (hourly)** — the primary yield signal. Source: Hyperliquid `fundingHistory` and `predictedFundings` API; [[coinglass]] cross-venue aggregation; [[funding-by-hour]] for intraday pattern analysis.
- **[[open-interest]]** — confirms the long/short imbalance driving the funding. High OI + high funding = confirmed structural demand imbalance (not a momentary tick).
- **[[basis]]** — monitors the perp-to-spot spread directly; a premium that persists across the hourly settlements is the same signal as elevated positive funding.
- **Spot price feed** — for sizing the hedge leg and tracking the delta of the combined position.
- **[[hypurrscan]] / [[coinglass]]** — cross-venue funding comparison; identifies whether the Hyperliquid rate is elevated vs CEX equivalents (higher HL funding = better carry opportunity here vs hedging on CEX).

---

## Example Trade

**Illustrative only — not a backtest.**

Scenario: SOL/USDC-PERP on Hyperliquid, February 2026. SOL is in a high-momentum bull phase. Funding settles at +0.035%/h (+30.7% APY annualised) for 6 consecutive hours. OI is 140% of the 30-day mean. SOL has deep spot liquidity on Binance.

| Construction | Detail |
|---|---|
| **Perp leg** | Short $120,000 notional SOL perp @ $150, 2× leverage, isolated margin |
| **Spot hedge** | Long $78,000 notional SOL spot on Binance (65% hedge ratio) |
| **Net delta** | Short ~$42,000 SOL (35% of notional — residual directional exposure) |
| **Funding rate** | +0.035%/h = $42/h on $120k notional (collected every hour) |
| **Hold period** | 6 days until funding drops to +0.008%/h |
| **Funding collected** | 0.035% × 144h × $120k = $6,048 |
| **SOL price change** | SOL −5% during hold → perp P&L: +$6,000; spot P&L: −$3,900 |
| **Net P&L** | $6,048 (carry) + $6,000 (perp) − $3,900 (spot) − fees ≈ **+$7,700 (~6.4% on $120k)** |

*Illustrative, not a backtest. Favourable outcome shown. An adverse scenario: SOL +15% during hold; perp loss ~$18,000; spot gain ~$11,700; carry ~$6,048; net ~−$252 before fees — carry roughly covers the hedged loss, but directional damage dominates.*

---

## Performance Characteristics

- **Return shape:** steady, low-vol carry income interrupted occasionally by sharp directional losses when price moves significantly against the residual delta. The Sharpe of the pure carry income stream (before directional) is 1.3–1.5; the combined Sharpe degrades based on hedge ratio.
- **Expected Sharpe:** ~1.0 at the 65% hedge ratio; degrades toward 0.5–0.7 at 0% hedge (pure single-leg) in volatile regimes.
- **Max drawdown:** ~18% at the recommended near-neutral construction. Worst drawdowns occur when a large price move against residual delta coincides with a spike in per-leg funding being charged (e.g., being short while funding flips negative during a cascade).
- **Correlation:** near-neutral construction has low correlation to market direction; the residual 35% delta creates slight positive exposure to the asset — slight negative correlation to [[crowded-short-funding-fade]] (which is a full directional long).
- **Carry yield range (illustrative, annualised):** 8–30% APY on near-neutral construction depending on funding regime. Lower in compressed-funding environments (post-Ethena industrialisation of BTC/ETH carry).

---

## Capacity Limits

The primary capacity constraint is the availability of a spot hedge counterpart. BTC and ETH: ~$10M per pair comfortable; SOL: ~$5M; mid-caps: ~$1–3M. Unhedged single-leg carries no spot-side constraint but the position concentration limits apply.

Aggregate basket capacity estimate: **$25M** near-neutral, with significant degradation above $15M on non-major pairs. Beyond this scale, the strategy's own short perp positions suppress funding (contributing to the carry normalising), and the spot legs on CEXs begin to face meaningful slippage.

Note that [[ethena-usde]], Resolv, and Pendle have already industrialised the BTC/ETH cash-and-carry trade at billions in scale — this basket competes in the same space and will see compressed carry on majors. The edge is therefore most concentrated in:
1. Hyperliquid-specific pairs without CEX equivalents (mid-caps, HL-native tokens)
2. Transient funding spikes (1–7 day windows) that large arb desks haven't positioned for at scale
3. The negative-funding direction (less competed, as fading bear sentiment is less comfortable for most carry traders)

---

## What Kills This Strategy

See [[failure-modes]]:

1. **Carry compression by large-scale arb capital.** The biggest structural threat: as more capital chases the funding harvest, the funding rates compress toward the interest baseline. BTC/ETH carry on CEXs has already compressed significantly post-2023 as Ethena and similar protocols scaled. Hyperliquid's thinner mid-cap pairs are the remaining reservoir of elevated carry.
2. **Directional move overwhelming carry.** A 20–30% price move against the residual delta destroys multiple months of carry income in a single day. The hedge ratio dampens this but doesn't eliminate it — full elimination requires the [[funding-rate-arbitrage]] cash-and-carry construction.
3. **Spot hedge leg disruption.** If the CEX spot hedge position cannot be closed (exchange halt, withdrawal limit, bridge risk), the position is no longer delta-neutral and becomes fully directional. This is a structural operational risk.
4. **Funding flip during hold.** If funding flips direction while a position is open (e.g., from positive to negative while short), the position now *pays* funding rather than collecting it. The carry-ratio stop addresses this but not instantaneously.
5. **Hyperliquid operational risk.** ADL, oracle issues, chain congestion. See [[hyperliquid-liquidation-engine]].

---

## Kill Criteria

Per [[when-to-retire-a-strategy]]:

- **Rolling 30-day annualised funding yield < 8% APY** across the basket — carry has compressed below a meaningful threshold; fees + operational overhead are consuming most of the edge.
- **Drawdown > 15%** over rolling 6 months — directional losses are overwhelming the carry.
- **Three consecutive months of negative net P&L** — strategy is not working in current regime.
- **Single isolated-margin liquidation event** — a leg was sized incorrectly or market moved too fast; full review before any re-entry.

---

## Advantages

- **Near-directional-neutral** — compared to the crowded-fade baskets, this basket tolerates adverse price moves much better due to the hedged construction.
- **Structural, documented premium** — funding-rate carry in crypto perps has decades of empirical data supporting positive expected returns. Source: BIS WP1087; [[funding-rate-arbitrage]].
- **Hyperliquid-specific yield uplift** — hourly settlement cadence and the availability of mid-cap + HL-native perps provides carry opportunities that do not exist on 8h-cadence CEXs.
- **Flexible hedging** — the near-neutral (vs fully-neutral) construction allows operation on pairs where a perfect spot hedge is unavailable.
- **Steady, compounding income** — unlike the funding-fade baskets which rely on squeeze events, this basket generates predictable hourly cash flows.

---

## Disadvantages

- **Heavily competed on majors** — large-scale protocols (Ethena) have compressed BTC/ETH carry substantially; this basket's edge is concentrated in HL-specific and mid-cap pairs.
- **Residual directional risk** — the near-neutral construction accepts some directional exposure; a bad enough price move will overwhelm carry.
- **Capital intensity** — a properly hedged position ties up capital on both the perp and spot leg simultaneously.
- **Operational complexity** — running positions simultaneously on Hyperliquid (perp) and a CEX (spot hedge) requires monitoring two venues, bridging capital, and managing rebalancing.
- **Carry asymmetry** — negative-funding carry (shorts paying longs; go long perp) is less systematically profitable than positive-funding carry because bear-regime persistence creates larger adverse directional moves.

---

## Hyperliquid Execution Notes

**Funding direction precision:**
- **Positive funding → longs pay shorts.** Open a *short* perp to *collect* the rate.
- **Negative funding → shorts pay longs.** Open a *long* perp to *collect* the rate.
- Confirm direction via `fundingHistory` API: positive `fundingRate` field = longs paying = short collects.

**Hourly settlement timing.** Funding is transferred at the top of each UTC hour. Entering a position at 23:58 UTC means collecting the first funding payment in ~2 minutes. Entering at 00:02 UTC means waiting 58 minutes for the first collection. For positions where the carry thesis is time-sensitive (spike decay expected within hours), entry timing relative to the settlement hour matters meaningfully.

**`predictedFundings` advantage.** The in-flight TWAP exposed via this endpoint allows positioning approximately 30 minutes before the settlement, capturing the next hour's payment from the first minute of hold. This is unique to Hyperliquid among major perp venues. Source: [[hyperliquid-funding-rate-microstructure]].

**HLP interaction.** This basket's short-perp positions interact with HLP (Hyperliquid's market-maker vault). HLP typically holds a net short book in bull regimes, meaning HLP is *also* collecting positive funding. The harvest basket competes with HLP for the same carry yield, but at different scales and with different exit conditions — HLP's positions are much larger and more persistent. See [[hyperliquid-vault-architecture]].

**Sibling baskets:** [[crowded-short-funding-fade]] and [[crowded-long-funding-fade]] are the *directional* siblings — they take the same funding signal but also bet on a price squeeze. The harvest basket is distinguished by its neutrality objective: it wants to *not* be affected by price direction. The three baskets can run simultaneously; monitor that aggregate short notional across harvest + crowded-long-fade does not create a synthetic large short book on any single pair.

---

## Sources

- [[hyperliquid-funding-rate-microstructure]] — hourly cadence, formula, sign conventions, HLP interaction, spike lifecycle.
- [[funding-rate-arbitrage]] — the full cash-and-carry construction; the harvest basket is the single-leg derivative of this strategy.
- [[2026-06-03-cryptodataapi-14-basket-regime-framework]] — basket design and regime mapping.
- [[coinglass]] — cross-venue funding data.
- [[funding-by-hour]] — intraday funding patterns; useful for optimising entry timing.
- BIS Working Paper No. 1087 (Schmeling, Schrimpf, Todorov, 2023) — empirical foundation for crypto funding-rate carry persistence.
- He, Manela, Xu, Yan, *Fundamentals of Perpetual Futures* (2022) — theoretical framework for perp pricing and carry.
- [[edge-taxonomy]] — edge classification.

---

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — cross-exchange funding rates (Binance + Hyperliquid)
- `GET /api/v1/derivatives/open-interest?coin=BTC` — cross-exchange open interest
- `GET /api/v1/derivatives/binance/long-short-ratio?symbol=BTCUSDT` — top-trader account long/short ratio
- `GET /api/v1/derivatives/summary?coin=BTC` — all-in-one derivatives overview (markdown format available)

**Historical data:**
- `GET /api/v1/derivatives/binance/funding-rates?symbol=BTCUSDT&limit=500` — funding-rate history
- `GET /api/v1/derivatives/binance/history?days=90` — daily derivatives series (funding, OI, long/short)
- `GET /api/v1/backtesting/funding` — deep funding archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/funding-rates?coin=BTC"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-derivatives]].

## Related

[[funding-rate-arbitrage]] · [[crowded-short-funding-fade]] · [[crowded-long-funding-fade]] · [[volatility-carry]] · [[pairs-trading]] · [[statistical-arbitrage]] · [[funding-rate]] · [[basis]] · [[open-interest]] · [[perpetual-futures]] · [[liquidation]] · [[hyperliquid]] · [[hyperliquid-funding-rate-microstructure]] · [[hyperliquid-vault-architecture]] · [[hyperliquid-liquidation-engine]] · [[funding-by-hour]] · [[basis-carry-regime]] · [[derivatives-native-regime]] · [[market-regime]] · [[trading-strategy-baskets]] · [[coinglass]] · [[hypurrscan]] · [[edge-taxonomy]] · [[failure-modes]] · [[when-to-retire-a-strategy]]
