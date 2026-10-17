---
title: Gamma Exposure (GEX) Trading
type: strategy
created: 2026-04-06
updated: 2026-09-16
status: review
tags: [combinations, alpha-edge, options, gamma, dealer-hedging, market-microstructure, volatility, crypto, derivatives]
strategy_type: hybrid
markets: [crypto]
complexity: advanced
backtest_status: untested
related: ["[[expiration-and-rebalancing-flows]]", "[[cross-asset-signals]]", "[[dvol]]", "[[deribit]]", "[[max-pain]]", "[[gamma-scalping]]", "[[cryptodataapi]]"]

# Edge characterization
edge_source: [structural, analytical]
edge_mechanism: "Deribit market-makers must delta-hedge their net option positions mechanically; above the gamma-flip level their hedging stabilises price (buy dips, sell rallies), below it they amplify moves (sell dips, buy rallies); knowing the aggregate net gamma position predicts whether the next daily move will be mean-reverting or trending."

# Data and infrastructure requirements
data_required: [options-chain, open-interest, max-pain, dvol-index, funding-rates]
min_capital_usd: 10000
capacity_usd: 200000000
crowding_risk: medium

# Performance expectations
expected_sharpe: 0.8
expected_max_drawdown: 0.20
breakeven_cost_bps: 25

# Kill criteria
kill_criteria: |
  - GEX regime prediction success rate (positive-GEX = range, negative-GEX = trend) drops below 55% over 3 months
  - crypto options market structure changes materially (e.g., Deribit loses dominant OI share)
  - drawdown > 15% while GEX signal is active

gates:
  - id: options_liquid_majors
    role: universe
    rule: "BTC and ETH only: the coins with a liquid Deribit options book, whose dealer hedging the edge relies on"
    runnable: true
    endpoint: /api/v1/volatility/implied
    field: items[].symbol
    note: "/quant/gex (Pro) covers every Hyperliquid perp, about 230 coins, because it is a perp analog built from market-maker positioning, not from options. The options-side data is narrower: DVOL and the expiry list are BTC and ETH, max pain is BTC only."
  - id: gex_read_has_mm_book
    role: filter
    rule: "Act on a coin's GEX read only when regime.coverage is full (a real market-maker book behind it), not funding_only or none"
    runnable: true
    endpoint: /api/v1/quant/gex?symbol={coin}
    field: coins.{coin}.regime.coverage
    note: "From the page's AI-agent workflow. regime.confidence (0-1) in the same block weights a thin-sample read."
  - id: positive_gex_regime
    role: filter
    rule: "Positive-GEX regime (dealers stabilise): regime.score at or below -0.20, the API's dampen state. Only here sell premium, fade extremes and trade mean-reversion"
    runnable: true
    endpoint: /api/v1/quant/gex?symbol={coin}
    field: coins.{coin}.regime.score
    replay: /api/v1/quant/gex/history?symbol={coin}&from={start}
    replay_field: points[].regime_score
    note: "Crypto mapping: /quant/gex is the perp analog of options GEX (Hyperliquid market-maker inventory, liquidation clusters near mark, funding and OI), not Deribit options dealer gamma, and the page's SPX straddles and iron condors become Deribit BTC/ETH option legs, whose prices we do not serve. Thresholds are in meta.regime_rules. A score between -0.20 and 0.35 is transitional, which the page's table has no row for. The hourly history covers 30 days from 2026-09-09; older reads are in /backtesting/snapshots?data_type=gamma_exposure."
  - id: negative_gex_regime
    role: filter
    rule: "Negative-GEX regime (dealers amplify): regime.score at or above 0.35, the API's amplify state. Trade momentum and breakouts, buy straddles, never fade the move"
    runnable: true
    endpoint: /api/v1/quant/gex?symbol={coin}
    field: coins.{coin}.regime.score
    replay: /api/v1/quant/gex/history?symbol={coin}&from={start}
    replay_field: points[].regime_score
    note: "Same perp analog as positive_gex_regime, not options dealer gamma."
  - id: high_vs_low_positive_gex
    role: sizing
    rule: "High positive GEX: full premium-selling and fade size. Low positive GEX: directional trades at moderate size"
    runnable: partial
    endpoint: /api/v1/quant/gex?symbol={coin}
    field: coins.{coin}.regime.score
    replay: /api/v1/quant/gex/history?symbol={coin}&from={start}
    replay_field: points[].regime_score
    note: "Both rows sit inside the dampen state (score -1.0 to -0.20). The page draws no line between high and low positive GEX and gives no sizes, so the cut is the desk's call. distribution_context.regime_score_pctile ranks today's score against 30 days."
  - id: deeply_negative_gex
    role: sizing
    rule: "Deeply negative GEX (crash or melt-up risk): maximum hedging and tail-risk plays"
    runnable: partial
    endpoint: /api/v1/quant/gex?symbol={coin}
    field: coins.{coin}.regime.score
    replay: /api/v1/quant/gex/history?symbol={coin}&from={start}
    replay_field: points[].regime_score
    note: "Inside the amplify state (score 0.35 to 1.0). The page gives no cutoff for 'deeply' and no hedge size, so both are the desk's call. regime.rationale says when a realized liquidation cascade is firing."
  - id: price_above_flip
    role: filter
    rule: "Price above the gamma flip: range-bound, mean-reverting playbook (sell premium, fade extremes). dist_to_flip_pct below 0 means the flip is under the mark"
    runnable: partial
    endpoint: /api/v1/quant/gex?symbol={coin}
    field: coins.{coin}.dist_to_flip_pct
    replay: /api/v1/quant/gex/history?symbol={coin}&from={start}
    replay_field: points[].dist_to_flip_pct
    note: "dist_to_flip_pct = (gamma_flip - mark) / mark x 100, null when there is no flip. Our gamma_flip is the perp analog: the price where market-maker long liquidations below balance short liquidations above, searched only near the mark. The API scores only the distance to it (within 2% = on the line), not which side price is on, so whether this line stands in for the options flip is the desk's call. positive_gex_regime is the served stabilise-or-amplify read."
  - id: price_below_flip
    role: filter
    rule: "Price below the gamma flip: volatile, trending playbook (buy protection, trade breakouts, do not fade). dist_to_flip_pct above 0 means the flip is over the mark"
    runnable: partial
    endpoint: /api/v1/quant/gex?symbol={coin}
    field: coins.{coin}.dist_to_flip_pct
    replay: /api/v1/quant/gex/history?symbol={coin}&from={start}
    replay_field: points[].dist_to_flip_pct
    note: "Same perp-analog caveat as price_above_flip. On 2026-10-17 BTC sat 27% below its flip while its regime read dampen, so the two reads can disagree."
  - id: realized_vol_agrees
    role: filter
    rule: "Realized-vol state agrees with the GEX regime: mean_reverting with positive GEX, expanding with negative GEX"
    runnable: true
    endpoint: /api/v1/volatility/regime/{coin}
    field: regime
    note: "The page's AI-agent cross-check. The other states (compressed, normal, vol_shock) are not named by the page."
  - id: technical_entry_timing
    role: entry
    rule: "GEX sets how to trade, not when: time each entry with technical analysis (fade range extremes in positive GEX, take breakouts in negative GEX)"
    runnable: partial
    endpoint: /api/v1/indicators/technical?symbol={coin}
    field: items[].range_state.zone
    note: "The page names no indicator or level. zone near_high or near_low marks a range extreme to fade, and a close through it is the breakout. Which technical trigger to use is the desk's call."
  - id: opex_window
    role: entry
    rule: "Open pinning trades 3-5 days before the monthly options expiry: expiry_days 3 to 5 on Deribit's last-Friday expiry"
    runnable: true
    endpoint: /api/v1/volatility/implied
    field: items[].term_structure[].expiry_days
    note: "Crypto mapping: the page's third-Friday OpEx is the SPX calendar. Deribit's monthly and quarterly BTC/ETH options settle on the last Friday of the month at 08:00 UTC. Pick that row by its expiry code (30OCT26 is the last Friday of October); the list also holds daily and weekly expiries, nearest 12 only. term_structure is Pro Plus and is empty on lower tiers."
  - id: max_pain_target
    role: entry
    rule: "In the OpEx window, price is expected to gravitate toward the max-pain strike: trade toward it or sell premium centred on it"
    runnable: partial
    endpoint: /api/v1/market-intelligence/options
    field: data[].max_pain
    replay: /api/v1/backtesting/snapshots?data_type=coinglass_options&start={start}
    replay_field: snapshots[].data[].max_pain
    note: "BTC only; no ETH max pain is served. It is computed on the Deribit expiry with the largest open interest, often the quarterly rather than the upcoming monthly, and the response does not name that expiry, so whether it is this OpEx's pin is the desk's call. Compare it with the mark from /quant/gex (coins.{coin}.mark)."
  - id: largest_oi_strikes
    role: entry
    rule: "Identify the largest open-interest call strike and put strike for the expiry: the magnets around max pain"
    runnable: false
    note: "We serve no per-strike open interest. /market-intelligence/options carries BTC aggregate OI, the put/call ratio and one max-pain strike only; per-strike OI needs Deribit's book summary per instrument."
  - id: opex_week_conviction
    role: sizing
    rule: "OpEx week is the highest-conviction GEX period: full size in it, smaller GEX positions the rest of the month"
    runnable: partial
    input: derived
    inputs: [opex_window]
    note: "OpEx week = expiry_days 0-6 on the monthly expiry. The page gives no size for the rest of the month."
  - id: regime_turns_exit
    role: exit
    rule: "Stop selling premium and close fade trades as soon as GEX is no longer positive (regime.score above -0.20); switch to the momentum playbook once it reaches 0.35"
    runnable: true
    endpoint: /api/v1/quant/gex?symbol={coin}
    field: coins.{coin}.regime.score
    replay: /api/v1/quant/gex/history?symbol={coin}&from={start}
    replay_field: points[].regime_score
    note: "GEX can shift intraday: re-poll rather than read once a day. Positions behind the read refresh every 5-15 minutes; regime.since says when the current state was committed."
  - id: pin_release_exit
    role: exit
    rule: "Close pin trades at the expiry settlement: the pin releases after it and suppressed moves often accelerate (the OpEx volatility pop)"
    runnable: true
    input: derived
    inputs: [opex_window]
    note: "The page's 'Monday after OpEx' is SPX. Deribit settles Friday 08:00 UTC, so the release starts then."
  - id: cut_losses_negative_gex
    role: stop
    rule: "In negative GEX never average down, and cut losing trades fast: moves can run 2-3x the normal daily range"
    runnable: partial
    input: position
    endpoint: /api/v1/quant/gex?symbol={coin}
    field: coins.{coin}.regime.score
    note: "Not adding to a loser while regime.score is at or above 0.35 is checkable from the position record. The page gives no stop distance for cutting fast, so that is the desk's call."
  - id: max_position_size
    role: sizing
    rule: "At most 3% of the portfolio in any single GEX-based trade"
    runnable: true
    input: position
---

# Gamma Exposure (GEX) Trading

## Edge source

**Structural** and **analytical**. See [[edge-taxonomy]].

Deribit market-makers hedge their net delta position continuously. That hedging is mechanical and non-discretionary — they have no choice. When net dealer gamma is positive (they are net long gamma), they sell into rallies and buy into dips to stay delta-neutral, creating a stabilising force. When net dealer gamma is negative, they must do the opposite — amplifying moves. Knowing which regime the market is in (via [[max-pain]] and OI-weighted gamma sums) is free public information; few retail traders have the tools to act on it.

**Crypto specifics:** The equity GEX infrastructure (SpotGamma, Squeezemetrics) does not cover Deribit. Crypto GEX must be computed manually from Deribit's public API (per-strike delta, gamma, OI) or sourced from [[greeks-live]]. The crypto effect is measurably weaker than equities because (1) crypto options volume is still a fraction of perp/spot volume and (2) hedging happens via perp rather than spot, which adds funding-rate noise. The OpEx pinning effect near the last-Friday settlement and the quarterly expiry is the most robust crypto GEX signal.

## Null hypothesis

If dealer hedging flows are negligible relative to directional perp flow (which they often are in crypto), GEX regime prediction is noise. Positive and negative GEX periods would show the same distribution of daily returns, and the strategy would earn ≈ 0 above costs. The counter-evidence: the empirical max-pain drift in the final 48 hours of monthly/quarterly Deribit expiries is observable in public data.

## The Edge

Options dealers do not speculate. They market-make, collecting the bid-ask spread, and then hedge their directional exposure away. This hedging is mechanical, predictable, and enormous in scale. When you know the dealer's gamma position, you know whether the market will be pinned or explosive -- before it happens.

**Gamma** is the rate of change of [[delta]]. When dealers are **long gamma** (net sold puts that moved in-the-money, or bought calls), they must buy dips and sell rips to stay delta-neutral. This stabilizes price -- the market feels "sticky," bouncing in a narrow range. When dealers are **short gamma** (net sold calls near the money, large put walls), they must sell into selloffs and buy into rallies to hedge -- amplifying the move. The market becomes a pinball machine.

The edge: by tracking aggregate dealer gamma exposure, you can predict whether the market will mean-revert or trend on any given day. This is not a guess. It is a consequence of the largest participants in the market being forced to hedge mechanically.

## Why It Persists

Options market-making is dominated by a handful of firms (Citadel Securities, Wolverine, Susquehanna). Their hedging activity moves billions of dollars daily. Yet most equity and crypto traders have never heard of gamma exposure. The edge persists because:

1. **Options literacy is rare** -- most traders learn price action and indicators, not Greeks-based market structure
2. **The data is fragmented** -- computing aggregate GEX requires processing the entire options chain across all strikes and expirations
3. **The effect is invisible on a price chart** -- you cannot see dealer hedging in [[candlestick-patterns]] or [[moving-averages]]. It operates beneath the surface
4. **Dealer behavior is non-discretionary** -- they MUST hedge, regardless of what technicals or fundamentals say. This makes GEX a pure structural signal

## How to Implement

### Step 1: Track GEX Data

Use specialized tools that calculate aggregate dealer gamma across all strikes:

- **SpotGamma** -- industry standard for S&P 500 and single-stock GEX levels
- **Squeezemetrics** -- publishes the DIX (dark pool indicator) and GEX daily
- **Unusual Whales / GammaLab** -- real-time GEX visualization
- **Manual calculation** -- pull open interest per strike from CBOE, multiply by gamma × contract size × 100, assume dealers are short calls and long puts (standard flow assumption)

### Step 2: Identify the Gamma Flip Level

The **gamma flip** is the price level where aggregate dealer gamma switches from positive to negative. Above this level, dealers stabilize the market. Below it, they amplify moves.

- **Price above gamma flip** → market is rangebound, mean-reverts. Strategy: sell [[options-premium-selling|premium]], fade extremes, trade [[mean-reversion]] setups
- **Price below gamma flip** → market is volatile, trends hard. Strategy: buy [[options-strategies|options]] for protection, trade [[breakout-trading|breakouts]], avoid fading moves

### Step 3: Trade the Regime

| GEX Regime | Market Behavior | Strategy |
|---|---|---|
| High positive GEX | Pinned, low vol, narrow range | Sell straddles, iron condors, fade SPX moves |
| Low positive GEX | Mild directional moves possible | Directional trades with moderate sizing |
| Negative GEX | Explosive, trending, high vol | Buy straddles, trade momentum, avoid mean-reversion |
| Deeply negative GEX | Crash/melt-up risk | Maximum hedging, tail-risk plays via [[asymmetric-barbell]] |

### Step 4: OpEx Pinning

Near options expiration (especially monthly OpEx on the third Friday), open interest concentrations create a magnetic effect. Dealers' hedging pulls price toward the strike with the largest open interest -- the "[[max-pain]]" level.

- **3-5 days before OpEx**: identify the max pain strike and the two largest OI call/put strikes
- **Expect price to gravitate** toward max pain as gamma hedging intensifies
- **Post-OpEx (Monday after)**: the pin releases. Gamma clears. Moves that were suppressed often accelerate -- this is the "OpEx volatility pop"

## Example Setup

**S&P 500 -- March 2025 GEX regime trade:**

1. SpotGamma shows gamma flip at 5,150. SPX trading at 5,220 (above flip = positive gamma regime)
2. GEX is $8B positive -- extremely high. Market has been pinned in a 30-point range for 4 days
3. Sell SPX 0DTE iron condors: sell 5190/5250 strangles, buy 5180/5260 wings. Collect $3.50 credit on $10 wide spreads
4. SPX oscillates between 5,195 and 5,245 all day (dealer hedging keeps it pinned)
5. Both short strikes expire OTM. Full credit collected. Repeat daily while high-GEX regime persists
6. **Regime shift**: FOMC meeting causes SPX to drop below 5,150 (gamma flip). GEX turns negative
7. **Switch to momentum**: stop selling premium immediately. Buy puts or trade breakdowns. The dealers are now amplifying the move

## Risk Management

- **GEX is a regime indicator, not an entry signal** -- it tells you HOW to trade, not WHEN. Combine with [[technical-analysis]] for entry timing
- **OpEx week is the highest-conviction GEX period** -- the rest of the month, GEX signals are weaker
- **GEX can shift intraday** -- a large options trade can flip dealer positioning. Monitor in real-time if possible
- **Do not fight negative gamma** -- when GEX flips negative, the market can move 2-3x its normal daily range. Cut losses fast, do not average down
- **The 0DTE explosion** has changed GEX dynamics since 2022 -- daily options expiration means gamma effects reset every day, not just monthly. Track 0DTE flows separately
- Maximum position size: 3% of portfolio in any single GEX-based trade. The regime is probabilistic, not certain

## Real-World Examples

- **January 2024 OpEx pin** -- SPX pinned within 10 points of the 4,800 strike (massive OI) for the entire expiration week, then rallied 50 points the following Monday when gamma cleared
- **Volmageddon (Feb 2018)** -- dealers were massively short gamma from structured products. When VIX spiked, their hedging amplified the selloff into a crash. Traders tracking GEX saw the negative gamma regime and stayed short
- **Meme stock squeezes (GME, AMC)** -- dealers who sold call options were short gamma. As price rose, they were forced to buy shares to hedge, which pushed price higher, forcing more buying -- a textbook gamma squeeze
- **Crypto options growth** -- Deribit and CME crypto options now create measurable GEX effects on BTC. Large strike expirations (e.g., $100K BTC calls) create observable pinning behavior near expiry
- **Quad witching** (simultaneous expiry of stock options, index options, index futures, stock futures) creates the highest GEX concentration of the year -- and the most predictable pinning and post-expiry moves

The core insight: in a market dominated by options hedging, understanding dealer positioning is not optional. It is the hidden hand moving price.

## Capacity limits

GEX-based strategies are regime signals applied to directional or premium-selling positions — their capacity is determined by the underlying instrument. For BTC/ETH perp positions sized on GEX signals, $100M–$200M is feasible. The OpEx-pinning play (sell premium near expiry) has lower capacity due to the thinness of near-expiry crypto options outside BTC/ETH.

## What kills this strategy

1. **Perp volume dominates option hedging** — if futures/perp flow is 50× options flow (common in crypto altcoin markets), GEX is irrelevant to price discovery.
2. **Deribit concentration risk** — if the BTC/ETH options market fragments to multiple venues, aggregate GEX from any single venue becomes less representative.
3. **0DTE expansion** — very short-dated options reset gamma daily, making regime signals less persistent (the same dynamic that changed equity GEX after 2022).
4. **Market-maker behaviour change** — if dominant Deribit market-makers shift hedging venues or cadences, the predictable hedging pattern breaks.

## Kill criteria (numeric)

*(From frontmatter — duplicated here for reference)*
- GEX regime prediction success rate < 55% over 3 months
- Deribit loses dominant BTC/ETH OI share
- Drawdown > 15% while GEX signal is active

## Getting the Data (CryptoDataAPI)

- `GET /api/v1/market-intelligence/options` — BTC/ETH options OI, max-pain, GEX-adjacent metrics
- For per-strike delta and gamma: use Deribit API directly or [[greeks-live]]

Full catalog: [[cryptodataapi-market-intelligence]].

**Live dashboards:** [gamma exposure](https://cryptodataapi.com/quant-gamma) · [liquidations](https://cryptodataapi.com/liquidations)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this strategy end-to-end:

- **Signal** — `GET /api/v1/quant/gex` — native Gamma Exposure with MM inventory and liquidation profile (**Pro**, not Pro+ — Pro keys stopped 403'ing on this endpoint 2026-07-10); the positive/negative gamma regime read. A single-symbol query (`?symbol=X`) returns the same bulk envelope as the unfiltered call (`{scope, note, timestamp, meta, coins:{...}}`), narrowed to one coin — read `coins[X]`, not a bare object (breaking change 2026-06-27). `regime.confidence` (0-1) and per-coin `distribution_context` (30d percentile ranks) are now available to weight thin-sample reads; check `regime.coverage` (`full`/`funding_only`/`none`) before trusting a read — a `funding_only` state has no real MM positioning behind it (see [[cryptodataapi-regimes]])
- **Strike context** — `GET /api/v1/market-intelligence/options` — BTC/ETH options OI, volume, and max pain for expiry and pin mapping; per-strike gamma still requires Deribit or [[greeks-live]]
- **Cross-check** — `GET /api/v1/volatility/regime` — verify the realized-vol state (mean_reverting vs expanding) agrees with what the GEX regime implies
- **Backtest** — the backtesting archive now includes a `gamma_exposure` snapshot type (5-min cadence, Pro Plus) via `GET /api/v1/backtesting/snapshots?data_type=gamma_exposure&start=...`, archiving the `/quant/gex` MM-lens per-coin map for point-in-time replay; alternatively replay price action around expiries with `GET /api/v1/backtesting/klines` (1h/4h back to 2017-08) plus point-in-time context from `GET /api/v1/backtesting/daily-snapshots` (since 2026-03-02)
- **Tips** — GEX flips sign fast around large expiries: re-poll `/api/v1/quant/gex` after each Deribit expiry rather than on a fixed clock
