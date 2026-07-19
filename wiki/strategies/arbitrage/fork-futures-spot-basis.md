---
title: "Fork Futures / Spot IOU Basis Arbitrage"
type: strategy
created: 2026-04-27
updated: 2026-07-19
status: excellent
tags: [arbitrage, crypto, futures, derivatives, event-driven]
aliases: ["IOU Basis Trade", "Pre-Fork Futures Arb", "Fork IOU Arbitrage"]
related: ["[[fork-airdrop-triangulation]]", "[[hard-fork]]", "[[crypto-spot-perp-futures-triangle]]", "[[basis-trading]]", "[[2022-09-ethereum-merge-fork-arbitrage]]", "[[ethereum-pow-iou]]"]
strategy_type: quantitative
timeframe: swing
markets: [crypto, futures]
complexity: advanced
backtest_status: live
edge_source: [structural, analytical, behavioral]
edge_mechanism: "Pre-fork IOU futures markets price the expected airdrop value before the snapshot. Retail and narrative-driven traders systematically over-price these IOUs vs. realized post-fork distribution value, allowing sophisticated participants to short pre-fork IOUs and deliver the airdropped asset at distribution."
data_required: [pre-fork-iou-prices, exchange-credit-policies, snapshot-block-height, parent-spot-price, historical-fork-iou-decay]
min_capital_usd: 100000
capacity_usd: 200000000
crowding_risk: medium
expected_sharpe: 1.3
expected_max_drawdown: 0.20
breakeven_cost_bps: 80
decay_evidence: "ETHW (Sep 2022) peak IOU $140 vs realized $5-10. UNI futures pre-launch over-priced by 30-50% on dYdX. Pattern repeats but each instance increasingly competitive."
---

# Fork Futures / Spot IOU Basis Arbitrage

The strategy of **shorting pre-fork IOU futures (or pre-launch perpetuals) against an expected delivery of the forked / airdropped asset at the snapshot**. It is an event-driven [[arbitrage]] trade in the basis/convergence family — conceptually a crypto cousin of risk-arbitrage, where the "deal" is the fork/snapshot event and the convergence is the IOU price falling to realized post-fork distribution value. Specialization within [[fork-airdrop-triangulation]] focused specifically on the futures-vs-spot basis rather than cross-exchange spot lag. The canonical execution venue is OKEx (historical), Poloniex, [[hyperliquid|Hyperliquid]], MEXC, and Bybit; the canonical example is the [[2022-09-ethereum-merge-fork-arbitrage|ETHW Merge fork]] of September 2022.

### Pre-fork IOU vs. analogous "claim-below-intrinsic" trades

| Trade | What is mispriced | Convergence catalyst |
|-------|-------------------|----------------------|
| Fork IOU basis | Pre-fork IOU *over*-priced vs realized fork value | Snapshot + post-fork price discovery |
| [[gbtc-discount-arbitrage]] | Closed-end claim vs NAV | ETF conversion |
| [[lst-depeg-arbitrage]] | LST claim below ETH | Withdrawal queue / mean-reversion |
| [[bankruptcy-claim-arbitrage]] | Claim below recovery | Court plan + distribution |

Note the *sign asymmetry*: in the GBTC/LST/bankruptcy cases the claim trades **below** intrinsic and the arb is long; in the fork-IOU case the IOU trades **above** realized value and the arb is short. The unifying principle is the same — a narrative-driven, retail-dominated, hard-to-arbitrage price ([[limits-to-arbitrage]]) converging to a structurally determinable terminal value.

## Edge Source

**Structural** + **analytical** + **behavioral**.

- **Structural:** IOU futures often launch 4-8 weeks before the snapshot. The market must price an asset that does not yet exist using only narrative and prior-fork comparables.
- **Analytical:** Modeling realistic post-fork distribution value requires hashrate forecasts, exchange credit policies, mining economics, and historical fork-coin decay curves.
- **Behavioral:** Retail enthusiasm for "the next BCH-style windfall" + speculative narrative trading + low IOU market depth combine to systematically over-price IOUs vs. realized fork value.

## Why This Edge Exists

Pre-fork IOU markets are populated by:

- **Speculators** chasing fork narrative without modeling realistic post-fork supply/demand.
- **Long-only retail** treating the IOU as a directional bet on "fork token survives."
- **Exchanges** facilitating trading because IOU volume is profitable regardless of settlement outcome.

Sophisticated participants who can:

- Forecast realistic post-fork distribution value (using hashrate, mining economics, and historical comparables).
- Hold spot parent asset through the snapshot to deliver the airdropped asset.
- Manage the operational risk of cross-exchange settlement, replay protection, and exchange credit policies.

...can short the over-priced IOU and deliver the cheap-to-acquire airdropped asset at settlement.

The counterparty is mostly retail/speculative long-IOU exposure plus a smaller cohort of yield-seeking parent-chain holders who lend out their parent asset to short-IOU desks for fee.

## Null Hypothesis

Under no-edge conditions, pre-fork IOU prices would be unbiased estimates of post-fork distribution value: the realized-value-to-IOU-price ratio would center on 1.0 with symmetric errors, and shorting IOUs at any multiple of modeled fair value would return zero net of carry and delivery costs. The historical record rejects this: across BCH (2017), BTG, BCD, ETHW (2022), and pre-launch airdrop perps (ARB 2023, EIGEN 2024), the fork/airdrop asset settled below its pre-event IOU trading range in the large majority of cases, with median realized value well under half of peak IOU price. The residual null to keep testing: if the mispricing is merely compensation for short-side frictions (borrow cost, exchange credit uncertainty, settlement-failure tail — the ~80 bps breakeven plus BSV-2018-style path risk), the strategy is collecting risk premium, not alpha. Distinguish by stress-testing returns against contested-fork scenarios; if expected PnL survives a 2x model miss, the edge is real.

## Variants

| Variant | Description | Example |
|---------|-------------|---------|
| **Short pre-fork IOU + long parent spot** | Classic basis trade | ETHW Sep 2022: short ETHW IOU @ $80 / long ETH spot @ $1,600 |
| **Short pre-fork IOU + long parent futures** | Removes spot custody risk | ETHW: short ETHW IOU on OKEx / long ETH-PERP on dYdX |
| **Long IOU then short post-launch perp** | Front-run the launch sell-off | Buy IOU at IOU listing; close + flip short on launch venue |
| **Cross-IOU basis arb** | Arb between IOU listings on different venues | OKEx ETHW IOU vs Poloniex ETHW IOU (typically 5-15% spread pre-fork) |
| **Pre-launch airdrop futures** | Same template applied to protocol airdrops | EIGEN Oct 2024: pre-launch perp $5+ vs realized launch $2-3 |

## Rules

For chain hard-forks:

1. **Identify IOU listings.** Monitor OKEx, Poloniex, MEXC, Hyperliquid, Bybit for pre-fork IOU products.
2. **Forecast realistic distribution value.** Base case (median): ~5-15% of parent value within 30 days of fork. Bull case: 20-30%. Bear case: 1-3%.
3. **Build distribution-value confidence interval.** Hashrate projections, mining-cost-curve analysis, exchange-listing announcements.
4. **Short IOU at >2x realistic distribution value.** Avoid shorting at <1.5x — costs and risk eat the edge.
5. **Hold parent spot or parent futures hedge.**
6. **At fork:** receive airdrop, deliver to close short, capture the spread.
7. **If exchange refuses credit:** use spot acquisition on a venue that lists the forked coin. Bridge if needed.

For protocol airdrops (e.g., ARB, EIGEN, JTO):

1. **Identify pre-launch perp listings.** Hyperliquid, dYdX, Bybit, OKEx routinely list pre-launch perps 1-4 weeks before TGE.
2. **Compare pre-launch perp price to airdrop-criteria-based valuation.** Use eligible-address counts × per-address allocation × estimated FDV.
3. **Short the perp if it implies an FDV >2-3x base-case.** Especially common for hyped airdrops (EIGEN, LayerZero).
4. **Acquire airdrop allocation.** Either through eligible activity, OTC purchase from farmers, or wash-allocations.
5. **Deliver at TGE.**

### Position Sizing

Size is bounded by **IOU market depth** (the dominant constraint — these markets are thin) and by **delivery certainty**. Practical rules used by fork-IOU desks:

1. Never short more IOU than you can cover via guaranteed delivery (held parent spot + confirmed exchange credit policy). The gap between modeled and *deliverable* size is the path-risk that BSV-2018 exposed.
2. Cap per-venue short at a fraction of visible IOU open interest to avoid moving the IOU against yourself.
3. Scale short size with the *multiple* over fair value: short aggressively only at >2x modeled value; trim at <1.5x where costs eat the edge.
4. Reserve margin buffer for the parent-asset hedge so a parent rally during the hold does not force a cover.

## Implementation Pseudocode

```python
on fork_or_airdrop_announced(parent_asset, snapshot_block, target_fork_token):
    iou_venues = identify_iou_listings(target_fork_token)
    realistic_value_dist = monte_carlo_post_fork_value(
        hashrate_models, mining_cost_curves,
        exchange_listing_announcements, historical_fork_decay
    )
    p50_realistic = realistic_value_dist.percentile(50)

    for venue in iou_venues:
        iou_price = venue.get_iou_price(target_fork_token)
        if iou_price > 2 * p50_realistic:
            short_size = capacity_constraint(venue) * confidence_factor
            venue.short_iou(target_fork_token, short_size, iou_price)
            hedge_with_parent_spot_or_perp(parent_asset, short_size)

    on snapshot_block:
        verify_airdrop_credit(target_fork_token, exchanges_holding_parent)
        for venue in iou_venues:
            if venue.allows_delivery(target_fork_token):
                deliver_airdrop_to_close_short(venue, target_fork_token)
            else:
                buy_to_close(venue, target_fork_token)  # at post-launch spot
```

## Indicators / Data Used

- Pre-fork IOU prices (OKEx, Poloniex, MEXC, Hyperliquid, Bybit).
- Snapshot block height + estimated UTC timestamp.
- Hashrate distribution forecasts (for PoW forks).
- Exchange credit / listing announcements (Binance, Coinbase, Kraken, OKX).
- Historical fork-coin price decay curves (BCH, BSV, ETHW, BTG, BCD).
- Parent asset spot and perp basis for hedge sizing.
- Funding rates on IOU perps (negative funding implies short crowding; reduce size).

## Example Trades

**ETHW IOU short (August-October 2022).** See [[2022-09-ethereum-merge-fork-arbitrage]].

- Pre-fork: ETHW IOU on OKEx peaked at $138 in late August. Realistic-value model: $20-50.
- Trade: short $10M notional ETHW IOU at $80-100; long $10M ETH spot.
- Post-fork: ETHW spot at $58 (Poloniex listing), declined to $5-10 within 6 weeks.
- Outcome: short returned 90%+ on notional; hedge offset most of ETH's parallel decline.
- Realized PnL: $7-9M on $10M notional in 6-8 weeks.

**EIGEN pre-launch perp (September-October 2024).**

- Pre-launch perp on Hyperliquid traded $5.50-8.00 in late September.
- Realistic FDV model based on eligibility criteria: $2-4 launch.
- Trade: short EIGEN-PERP at $6-7; acquire airdrop allocation through restaking activity.
- Outcome: launch at $5+, declined to $2-3 within 4 weeks.
- Realized PnL: 40-60% on notional, partly offset by Sybil-resistance reducing eligible allocation.

**ARB pre-launch perp (March 2023).**

- Pre-launch perp on Hyperliquid traded $1.50-2.00.
- Launch price $1.20-1.30; declined to $1.00 within 4 weeks.
- Realized PnL: 30-50% on the basis trade.

## Performance Characteristics

> **Data disclaimer:** These are *qualitative practitioner estimates* and reconstructed event outcomes (e.g., ETHW IOU peaking ~$138 on OKEx vs. realized ETHW spot of $5–10 within weeks), not an audited backtest. The strategy is episodic, so any annualized figure is conditional on a major event occurring in the period.

Specialized fork-IOU desks report **8-15% annualized contribution** from this strategy alone in years with major events; nothing in years without. Sharpe 1.0-1.5 once risk-adjusted for the long flat periods between events. Max drawdown 15-25% from misjudged events (e.g., the 2018 BSV hash war confusion).

### Cost overlay (what eats the short-IOU edge)

| Cost / friction | Effect |
|-----------------|--------|
| IOU borrow / short-funding | The ~80 bps breakeven assumption; can spike with short crowding |
| Negative IOU perp funding | Short pays when too many desks are short — a crowding tax |
| Parent-asset hedge carry | Funding/roll on the long ETH/BTC leg over the hold |
| Settlement-failure tail | Exchange refuses delivery → forced buy-to-close at post-launch spot |
| Cross-exchange / bridge ops | Replay protection, custody, transfer latency |
| Contested-fork path risk | A hash war (BSV 2018) can freeze settlement exactly when needed |

## Capacity Limits

Per-event capacity bound by IOU market depth:

- **Major events (ETHW, BCH 2017):** $50-200M per desk.
- **Major airdrops (ARB, EIGEN):** $20-50M per desk.
- **Minor forks/airdrops:** $1-5M per desk.

Total annual addressable: $200-500M industry-wide.

## What Kills This Strategy

- **IOU markets become too efficient.** As more desks enter, the over-pricing premium compresses (visible in 2024 airdrops where pre-launch perps converged closer to fair value within hours).
- **Exchanges restrict short delivery.** If venues require cash settlement instead of physical delivery, the basis trade becomes path-dependent.
- **Major fork events become rare.** Post-2022 most chains have avoided contentious splits.
- **Regulatory scrutiny on IOU markets.** Some venues delisted pre-launch perps in 2023-2024 under regulatory pressure.

## Kill Criteria

- Mean IOU mispricing over 4 events drops below 25% (currently 50-100%+).
- Cost of capital for short delivery exceeds breakeven 80 bps.
- Realistic post-fork value model misses by >2x for 2 consecutive events (model decay).

## Advantages

- High Sharpe per event (1.5-3.0 annualized over the holding period).
- Asymmetric: limited downside if IOU rallies (parent-asset hedge offsets); large upside if IOU collapses.
- Compatible with [[fork-airdrop-triangulation]] — same parent-asset position serves both strategies.

## Disadvantages

- Episodic — long flat periods between events.
- Operational complexity: cross-exchange settlement, [[replay-attack|replay protection]], airdrop credit policies.
- Path-dependent: a hash-war or contested fork (BSV 2018) can freeze the basis trade exactly when it needs to settle.
- Requires significant size to overcome fixed costs of fork-event monitoring infrastructure.

## Sources

- OKEx ETHW IOU product specification (August 2022).
- Galaxy Research, "Post-Merge Fork Tracker," October 2022.
- Hyperliquid pre-launch perp documentation (2023).
- Wintermute / Cumberland-DRW post-event commentary on 2022 ETHW fork.
- Historical fork-coin price data via CoinGecko + Messari.

## Getting the Data (CryptoDataAPI)

CryptoDataAPI serves the Hyperliquid pre-launch/IOU perp and the parent-spot hedge; OKEx/Poloniex/MEXC IOU books and exchange credit policies are off-API.

**Live data:**
- `GET /api/v1/hyperliquid/prices` / `GET /api/v1/hyperliquid/summary?coin=...` — HL pre-launch perp mids (the IOU short leg where listed on HL)
- `GET /api/v1/hyperliquid/funding-rates?coin=...` — IOU-perp funding (the short-crowding tax)
- `GET /api/v1/market-data/ticker/price?symbol=...` — parent spot (the long hedge leg)
- `GET /api/v1/derivatives/summary?coin=...` — parent perp basis for hedge sizing

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=...&interval=1h` — pre-launch perp OHLCV
- `GET /api/v1/backtesting/klines` / `GET /api/v1/backtesting/funding` — parent leg

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/summary?coin=ETH"
```

Auth: `X-API-Key` header. Full catalogs: [[cryptodataapi-hyperliquid]], [[cryptodataapi-market-data]], [[cryptodataapi-derivatives]].

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [short-term regimes](https://cryptodataapi.com/market-regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can price the short and hedge legs:

- **IOU + hedge legs** — `GET /api/v1/hyperliquid/prices` / `/hyperliquid/summary` price the pre-launch/IOU perp where it lists on Hyperliquid; `GET /api/v1/market-data/ticker/price` marks the parent spot hedge. Other-venue IOU books and credit policies are off-API.
- **Crowding gate** — `GET /api/v1/hyperliquid/funding-rates`: negative IOU-perp funding is the short-crowding tax that erodes the ~80 bp breakeven.
- **Regime gate** — `GET /api/v1/quant/market` for parent-hedge sizing through a contested-fork window.
- **Backtest** — `GET /api/v1/hyperliquid/candles` (IOU-perp history) + `GET /api/v1/backtesting/klines` / `/backtesting/funding` (parent).
- **Tip** — short only at >2x modelled realised value; use the HL feed to track how fast the pre-launch perp converges before committing.

## Related

- [[arbitrage]] — parent concept
- [[limits-to-arbitrage]] — why IOUs stay over-priced
- [[gbtc-discount-arbitrage]], [[lst-depeg-arbitrage]], [[bankruptcy-claim-arbitrage]] — claim-vs-terminal-value siblings
- [[hyperliquid]] — execution venue for pre-launch perps
- [[fork-airdrop-triangulation]] · [[hard-fork]] · [[crypto-spot-perp-futures-triangle]] · [[basis-trading]] · [[2022-09-ethereum-merge-fork-arbitrage]] · [[2017-08-bitcoin-cash-fork-arbitrage]] · [[ethereum-pow-iou]] · [[airdrop-farming]]
