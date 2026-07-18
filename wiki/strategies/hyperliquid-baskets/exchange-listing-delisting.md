---
title: "Exchange Listing / Delisting (Hyperliquid Basket)"
type: strategy
created: 2026-06-16
updated: 2026-07-13
status: good
tags: [crypto, perpetual-futures, hyperliquid, algorithmic, event-driven, quantitative]
aliases: ["Listing Pump Basket", "Delisting Short Basket", "Exchange Listing Event", "HL Listing Catalyst"]
related: ["[[hyperliquid-baskets-overview]]", "[[event-catalyst-regime]]", "[[policy-shock-regime]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[hyperliquid-liquidation-engine]]", "[[hyperliquid-funding-rate-microstructure]]", "[[hyperliquid-oracle-mechanics]]", "[[2025-03-jellyjelly-hlp-attack]]", "[[2025-10-crypto-liquidation-cascade]]", "[[liquidation-cascade-fade]]", "[[funding-rate]]", "[[open-interest]]", "[[perpetual-futures]]", "[[liquidity]]", "[[squeeze]]", "[[momentum-rotation]]", "[[when-to-retire-a-strategy]]", "[[token-unlock-supply-event]]", "[[meme-coin-cycle]]", "[[cross-sectional-relative-value]]", "[[macro-event-pump]]", "[[etf-and-institutional-flow]]", "[[2026-06-03-cryptodataapi-14-basket-regime-framework]]", "[[cryptodataapi]]"]
strategy_type: algorithmic
timeframe: scalp
markets: [crypto]
complexity: advanced
backtest_status: naive-backtested
edge_source: [informational, latency, behavioral]
edge_mechanism: "Retail and momentum chasers systematically bid confirmed listings before the event resolves, creating a predictable pump-then-fade cycle that a fast-entry short-to-neutral book can harvest; on the delisting side, panic selling by holders unable to bear the regulatory / liquidity loss is the forced counterparty."
data_required: [listing-announcement-feed, exchange-official-channels, hyperliquid-perp-oi, hyperliquid-perp-funding, ohlcv-1m, social-volume, order-book-depth]
min_capital_usd: 10000
capacity_usd: 15000000
crowding_risk: high
expected_sharpe: 0.7
expected_max_drawdown: 0.25
breakeven_cost_bps: 45
kill_criteria: |
  - rolling 3-month strategy drawdown > 25%
  - 3 consecutive listing trades produce < 0 net P&L after costs
  - signal-to-entry latency regularly exceeds 5 minutes (edge likely arbed away)
  - rolling 6-month Sharpe < 0
---

# Exchange Listing / Delisting (Hyperliquid Basket)

An event-driven [[trading-strategy-baskets|basket]] that captures the predictable price impact of new exchange listings (pump) and delistings (dump) by entering [[perpetual-futures|perpetual]] positions on [[hyperliquid|Hyperliquid]] immediately upon a confirmed announcement, targeting the initial speculation surge on the long side and the panic-selling cascade on the short side. Hold times are measured in hours to days; the edge lives almost entirely in the first few hours after confirmation. Speed of signal ingestion is the core operational requirement. It is the [[event-catalyst-regime]] expression within the [[market-regime]] framework.

> **Not investment advice.** This is a design document for a systematic strategy. All performance figures are illustrative estimates, not backtest results.

*Part of the [[hyperliquid-baskets-overview|Hyperliquid basket library]].*

## Edge Source

**Informational + latency + behavioral** (see [[edge-taxonomy]]).

- **Informational** — exchange listing announcements are public but unevenly consumed. A systematic feed watcher detects the event within seconds; the median retail participant learns minutes to hours later via social media.
- **Latency** — the listing-pump effect is front-loaded: the highest-velocity price move occurs in the 0–120 minute window after confirmation. Every minute of delay erodes expected capture materially.
- **Behavioral** — FOMO is the dominant driver of the initial pump. Retail traders chase the price higher in anticipation of a liquidity wave that may or may not materialize. The mirror image on delistings is panic selling driven by loss-aversion and exchange-reachability concerns, not fundamental reassessment.

## Why This Edge Exists

Exchange listings are among the most reliably tradeable events in crypto because the mechanism is structural, not random:

1. **Demand shock is immediate and visible.** A Binance or Coinbase listing announcement instantly expands the potential buyer universe. The marginal buyer knows a supply of new demand is coming and bids preemptively.
2. **The Hyperliquid perp often lists before or independently of the spot listing.** This creates an asymmetry: perpetual traders gain exposure to the announcement before spot markets are fully accessible to the incoming buyer wave, generating a short-lived but exploitable dislocation between Hyperliquid's mark price and the expected spot equilibrium. See [[hyperliquid-oracle-mechanics]] for how HL marks against a median of external exchange prices — a newly-listed perp may be priced against thin oracle sources.
3. **Delistings are structurally bearish.** Exchange removals reduce liquidity, trigger forced selling by custodial users unable to withdraw in time, and signal regulatory or reputational problems. Panic is rational for holders who cannot move assets quickly.
4. **Counterparty identification is clear.** On the long side: late retail entering after the pump is exhausted. On the short side: momentum chasers who overbid the announcement and are caught in the fade. On delistings: liquidity providers and market makers who cannot exit fast enough.

The well-documented "listing pump / post-listing dump" pattern in academic and practitioner research provides the theoretical prior. The edge is not that listings always pump — it is that the initial reaction *over-extends* relative to the fundamental shift in demand, creating a mean-reversion opportunity in the 24–72 hours post-peak.

## Null Hypothesis

Under no-edge conditions, exchange listing announcements are already fully priced by the time any systematic trade can be entered (i.e., faster participants have extracted all excess return), and the residual price move is symmetric noise around a new fair value. For delistings, the null is that prices have already drifted lower from leaked information or on-chain signals before the official announcement.

**Disconfirming evidence to watch:**

- Funding rates spike to extreme levels (> 0.15% / 8h) immediately on announcement, suggesting the crowd is already positioned and the trade is crowded before entry.
- Average entry-to-peak return compresses to < 5% net of costs across a rolling 20-trade window — the latency edge has been arbed.
- Newly listed perps on Hyperliquid show extreme slippage (> 100 bps on standard size) at announcement time — liquidity has not kept pace with interest.
- Multiple algorithmic competitors confirm entries in the first 30 seconds via on-chain OI spikes (readable via [[hyperliquid-liquidation-engine]] data feeds).

## Rules

**Universe:** Any asset with a live Hyperliquid perpetual that receives a confirmed listing or delisting announcement from Binance, Coinbase, OKX, Bybit, or Kraken. Priority to Binance (highest demand multiplier), then Coinbase (regulatory signal).

**Signal sources (in descending reliability):**
1. Official exchange blog / announcement pages (highest confidence, slight latency)
2. Official exchange social/X accounts — monitored via API with keyword alerts
3. Hyperliquid OI spike anomaly detector (> 3σ OI growth in < 5 min on a given asset = possible leak signal; entry conditional on confirming catalyst within 60 s)

**Entry — Listing Long:**
- Enter long immediately on confirmed announcement, within 120 seconds of first official source.
- Size: 0.5–1.5% of book in the named asset, isolated margin.
- Leverage: 3–5x. Never higher — the goal is to survive a gap against you before the thesis resolves.
- Avoid assets where funding rate is already > +0.10% / 8h at entry (crowd is pre-positioned; squeeze risk elevated on any unwind).

**Entry — Delisting Short:**
- Enter short on confirmed delisting announcement. The magnitude of the dump is correlated with: (a) how illiquid the asset's off-exchange withdrawal paths are, and (b) whether HL perp liquidity has already dried up.
- Size: 0.5–1.0% of book, isolated margin, leverage 2–3x. Delistings are structurally more dangerous to short on a thin perp — see Hyperliquid Execution Notes below.

**Exit — Listing Long:**
- Primary: trail a 20% drawdown from peak once the move is > 15% from entry; or time-exit at 24h if no move has materialized.
- Secondary: if funding flips > +0.15% / 8h (crowd fully in), take profit immediately — the fade is imminent.
- Hard stop: −10% from entry.

**Exit — Delisting Short:**
- Cover into the panic low — price often overshoots fair value; cover at a pre-set target (−20% to −40% from announcement depending on liquidity profile) or when selling pressure visibly exhausts on the 15m chart.
- Hard stop: +15% from entry (short squeeze on thin perp — cover immediately per JELLY protocol).

**Position caps:** never > 2% of book in any single listing / delisting name. Run no more than 2 simultaneous event positions.

## Implementation Pseudocode

```python
MAJOR_EXCHANGES = ["binance", "coinbase", "okx", "bybit", "kraken"]
LISTING_LONG_MAX_DELAY_SEC = 120
MAX_POSITION_PCT = 0.015          # 1.5% of book per name
MAX_LEVERAGE = 5
DELISTING_MAX_LEVERAGE = 3
CROWDED_FUNDING_THRESHOLD = 0.0010  # 0.10% / 8h

def on_listing_announcement(event, state, book_size):
    if event.exchange not in MAJOR_EXCHANGES:
        return None
    if event.age_seconds > LISTING_LONG_MAX_DELAY_SEC:
        return None  # edge window closed
    
    token = event.token
    if not hyperliquid_has_liquid_perp(token):
        return None
    if hl_daily_volume(token) < 1_000_000:
        return None  # too thin — JELLY guard
    
    current_funding = hl_funding_rate(token)
    if current_funding > CROWDED_FUNDING_THRESHOLD:
        return None  # already crowded
    
    size = min(MAX_POSITION_PCT * book_size, hl_max_safe_size(token))
    return long_perp(
        token, size=size, leverage=MAX_LEVERAGE,
        margin="isolated",
        stop_loss_pct=0.10,
        trailing_stop_from_peak_pct=0.20,
        time_exit_hours=24,
        funding_exit_threshold=0.0015
    )

def on_delisting_announcement(event, state, book_size):
    if event.exchange not in MAJOR_EXCHANGES:
        return None
    
    token = event.token
    if not hyperliquid_has_liquid_perp(token):
        return None
    if hl_daily_volume(token) < 500_000:
        return None  # too thin — hard skip
    
    size = min(0.010 * book_size, hl_max_safe_size(token))
    return short_perp(
        token, size=size, leverage=DELISTING_MAX_LEVERAGE,
        margin="isolated",
        stop_loss_pct=0.15,  # tight — JELLY guard
        cover_target_pct=0.30
    )

def monitor_open_positions(positions, state):
    for pos in positions:
        if pos.is_short and pos.pnl_pct > 0.15:   # short squeezing
            return cover_immediately(pos, reason="squeeze_guard")
        if pos.funding_rate < -0.0015:             # paying to short
            return cover_immediately(pos, reason="negative_carry")
    return positions
```

## Indicators / Data Used

- **Listing announcement feed** — custom webhook monitoring official exchange announcement APIs and X accounts for keywords: "listing," "will list," "trading begins," "delisting," "will delist." Latency target: < 30 seconds from publication to signal.
- **Hyperliquid perp data** — OI, funding rate (8h and predicted), order-book depth, last price, mark price vs oracle divergence. Source: [[hyperliquid-funding-rate-microstructure]].
- **Social volume spike** (secondary confirmation) — Twitter/X mention velocity for the token symbol; a spike before the official announcement is a potential leak signal.
- **On-chain exchange flow** — large deposits or withdrawals to the listing exchange in the 48h window can be an early signal.
- **Coinglass** — cross-exchange OI and funding snapshot to measure whether Hyperliquid's perp is leading or lagging other venues. Source: [[coinglass]].

**Data-feed mapping (cryptodataapi.com).** The venue-side inputs the basket gates on — Hyperliquid perp [[open-interest]], [[funding-rate]] (8h and predicted), order-book depth, mark-vs-oracle divergence, and 1m OHLCV — are read from cryptodataapi.com's Hyperliquid endpoints. The listing/delisting announcement feed itself is exogenous (exchange blogs and X accounts); cryptodataapi supplies the real-time perp microstructure used by the crowded-funding filter, the thin-perp (`<$1M OI`) guard, and the post-entry OI/funding monitors.

## Example Trade

**Illustrative — not a backtest.** Representative listing-pump scenario.

| Parameter | Detail |
|-----------|--------|
| Event | Confirmed Binance spot listing announcement for a mid-cap L1 token |
| Hyperliquid perp | Already live; $8M daily volume; funding at +0.03% / 8h (mild) |
| Entry | Long at $4.20, 3 minutes after official announcement, 4x leverage, isolated margin, 1% of book |
| Peak (T+90 min) | $5.75 (+37%); funding spikes to +0.18% / 8h → exit trigger fires |
| Exit | Covered at $5.60 on funding-exit trigger |
| Gross P&L | +33.3% on position → +133% on capital deployed (4x leverage) |
| Costs (fees + funding) | ~60 bps round trip; slippage ~30 bps on entry into rising market |
| Net P&L | ~131% on capital, ~1.3% of book |

**Counter-example (fade fails):** Listing for a low-liquidity DeFi token; announcement leaked 4h prior; funding already +0.20% / 8h at signal detection. Trade skipped by the crowded-funding filter. Asset subsequently pumps another 15% then dumps 40% — illustrating why the filter exists.

## Performance Characteristics

*All figures are illustrative estimates based on the known academic and practitioner literature on listing effects, not live backtest results.*

- **Return distribution:** strongly right-skewed on wins but with fat left tail from squeeze events. A handful of large listing pumps drive most of the annual return.
- **Win rate (listing long):** historically ~55–65% of confirmed listing trades are profitable before costs; net win rate closer to 45–55% after costs and slippage.
- **Average holding period:** 4–18 hours for listing longs; 6–48 hours for delisting shorts.
- **Expected Sharpe:** ~0.7 (net, assuming 2–4 events per month with realistic execution); high variance.
- **Expected max drawdown:** ~25% — most likely from a squeeze on a delisting short (thin perp + forced covering) or from a string of listings that immediately dump post-entry.
- **Breakeven cost:** ~45 bps round trip; above this, the expected edge is consumed by friction. Taker fees on Hyperliquid run ~2.5 bps; slippage on mid-cap perps is the dominant cost.
- **Funding carry:** typically neutral to slightly positive on listing longs (funding elevated but held briefly); negative on delisting shorts where funding may flip negative as shorts crowd in.

## Capacity Limits

The strategy is capacity-constrained by two factors. First, perp liquidity on newly-listed or delisting assets is thin — often < $5M OI on Hyperliquid; a position > $500K–$1M notional will move the market and generate adverse slippage. Second, the signal is inherently non-scalable: there are a limited number of high-quality listing events per month, and each has a fixed edge window. Strategy-level capacity is approximately **$15M** across concurrent positions before market impact dominates and the strategy becomes its own alpha-destroye. Individual position caps of 1.5% of book implicitly size this at the right scale for a < $100M book.

## What Kills This Strategy

The most likely failure modes (see [[failure-modes]]):

1. **Latency race loss.** HFT and MEV bots with < 1 second announcement-to-entry latency extract the first move before the strategy enters. If the median latency gap widens > 5 minutes, the edge disappears.
2. **Short squeeze on a thin delisting perp (the JELLY pattern).** A coordinated spot buy into a delisting short squeezes the perp on low liquidity, liquidates the short into HLP, and may trigger governance intervention ([[2025-03-jellyjelly-hlp-attack]]). This is the primary downside risk on the short side.
3. **Crowded trades.** When the listing pump is consensus-known, funding explodes before entry is possible and the position is entered into a crowded setup — any macro sell-off squeezes longs and flips the P&L.
4. **Oracle / mark price manipulation.** On newly listed Hyperliquid perps, the oracle may reference thin external markets. A coordinated external price move can force liquidation on the HL mark even if the true fair value has not moved. See [[hyperliquid-oracle-mechanics]].
5. **Signal-source latency blowout.** If the exchange API feed goes down or the monitoring webhook delays, the strategy enters stale — outside the 120-second window where most of the edge lives.
6. **Regulatory listing approval revoked.** Edge case: a listing is announced and then cancelled within hours (regulatory pressure, technical issues). The position is now long a pump with no fundamental driver.
7. **Strategy crowding from wiki publication.** If the basket logic becomes widely known, competitors front-run the signal, compressing edge. This is a meta-risk for any published systematic strategy.

## Kill Criteria

Numeric kill rules (see [[when-to-retire-a-strategy]]):

- Rolling 3-month strategy drawdown > **25%** → stop all new entries and full review.
- Three consecutive listing trades produce < 0 net P&L after costs → investigate signal quality; likely latency regression.
- Signal-to-entry latency regularly exceeds **5 minutes** → edge window has closed; retire.
- Rolling 6-month Sharpe < **0** → strategy is generating noise; retire or rebuild.
- Any single position moves > **+25% against** a short within 60 minutes on thin volume → JELLY guard: cover immediately; re-evaluate delisting-short sleeve.

## Hyperliquid Execution Notes

This basket has acute venue-specific risks that must shape every sizing decision:

**Thin-perp squeeze risk.** Newly listed and to-be-delisted tokens on Hyperliquid are exactly the JELLY squeeze setup: low OI, shallow order books, high retail participation, and a narrative that can turn reflexively violent. The [[2025-03-jellyjelly-hlp-attack|March 2025 JELLY event]] showed that a coordinated external spot buy can push the HL mark far from fair value, squeeze shorts into HLP, and force a governance delist with force-settlement — leaving the short with a worse-than-expected exit. Mitigation: hard skip any perp with < $1M OI or < $500K 24h volume; enter delisting shorts at reduced size with a tight stop.

**Single-mark-tick liquidation + ADL.** Hyperliquid liquidates on a single mark-price tick; ADL can deleverage winning positions when counterparties blow up. Size every position to survive a **20% adverse move** without liquidation at the chosen leverage level. A 5x long can withstand a 20% adverse move (margin = 20%); a 3x short can withstand a 33% adverse move — these are the outer bounds, not comfortable operating points. See [[hyperliquid-liquidation-engine]].

**Newly listed perps are illiquid and gappy.** If Hyperliquid lists the perp simultaneously with or just before the spot listing, the oracle may reference a single thinly-traded external CEX price. This creates wide bid-ask spreads, gappy fills, and elevated mark-vs-index divergence. Do not enter large positions on a < 48h old perp listing until order-book depth is confirmed.

**Funding rate can spike violently.** In the hours following a listing pump, funding can exceed 0.5% / 8h (> 200% annualized). This makes holding a long position into the next funding interval very expensive. Build the expected funding cost into the exit calculus — the strategy benefits from fast exits, not from riding high-funding positions overnight.

**Transparent positioning as a tool.** Hyperliquid's on-chain OI and leverage data (see [[hyperliquid-vault-architecture]]) lets you confirm in real time whether the crowd has already entered the trade. If OI has tripled in the 5 minutes before your entry, the funding filter should have already blocked you — but a live OI check is a secondary confirmation.

## Advantages

- Concretely actionable edge: the mechanism (announcement → demand shock → price overshoot) is durable and has decades of supporting literature.
- Short hold times mean funding-rate carry risk is limited on the long side.
- The signal is binary and unambiguous — a listing either happens or it does not.
- Hyperliquid's low taker fees make short-hold-time strategies more viable than on traditional CEXs.
- Naturally diversified across events; no single trade dominates risk.

## Disadvantages

- Extremely latency-sensitive; the edge window is measured in minutes.
- Crowding risk is structurally high — listings are the most-watched event catalyst in crypto.
- Delisting shorts carry outsized squeeze risk on thin perps — the worst outcome is a JELLY-style blow-up.
- Strategy capacity is low relative to the book management overhead.
- Funding rate can spike to punitive levels if the position must be held through multiple 8-hour intervals.
- Signal coverage gaps (API downtime, social-media monitoring failures) can cause missed events or stale entries.

## Sources

- [[2026-06-03-cryptodataapi-14-basket-regime-framework]] — 14-basket framework; event-catalyst regime classification
- [[hyperliquid-funding-rate-microstructure]] — HL funding mechanics and crowding signals
- [[hyperliquid-liquidation-engine]] — liquidation, ADL, and thin-perp risk
- [[hyperliquid-oracle-mechanics]] — mark-vs-index behavior on newly listed perps
- [[2025-03-jellyjelly-hlp-attack]] — canonical thin-perp short-squeeze case study
- [[coinglass]] — cross-venue OI and funding data for crowding assessment
- [[event-catalyst-regime]] — regime classification for listing/delisting events

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/event/calendar` — forward catalyst calendar up to 30d out (filter by type/symbol/bias)
- `GET /api/v1/event/regime/score` — event-risk composite (0-100)
- `GET /api/v1/event/regime/{symbol}` — per-symbol pending catalysts

**Historical data:**
- `GET /api/v1/backtesting/daily-snapshots/{date}` — point-in-time snapshots for event backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/event/calendar"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-regimes]].

## Related

[[hyperliquid-baskets-overview]] · [[trading-strategy-baskets]] · [[hyperliquid]] · [[market-regime]] · [[event-catalyst-regime]] · [[policy-shock-regime]] · [[hyperliquid-liquidation-engine]] · [[hyperliquid-funding-rate-microstructure]] · [[hyperliquid-oracle-mechanics]] · [[2025-03-jellyjelly-hlp-attack]] · [[funding-rate]] · [[open-interest]] · [[perpetual-futures]] · [[squeeze]] · [[liquidity]] · [[liquidation-cascade-fade]] · [[momentum-rotation]] · [[token-unlock-supply-event]] · [[meme-coin-cycle]] · [[cross-sectional-relative-value]] · [[macro-event-pump]] · [[etf-and-institutional-flow]] · [[failed-breakout-failed-breakdown]] · [[liquidity-vacuum-momentum]] · [[edge-taxonomy]] · [[failure-modes]] · [[when-to-retire-a-strategy]] · [[coinglass]] · [[2026-06-03-cryptodataapi-14-basket-regime-framework]]
