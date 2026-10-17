---
title: "Trend Following + Tail Risk Hedge"
type: strategy
created: 2026-04-06
updated: 2026-10-17
status: review
tags: [combinations, meta-strategy, trend-following, hedging, crisis-alpha, perpetual-futures, crypto, derivatives, options]
aliases: ["Trend + Tail", "CTA Plus Tail Hedge", "Dragon Portfolio Crypto"]
strategy_type: hybrid
timeframe: position
markets: [crypto, futures]
complexity: advanced
backtest_status: untested
related: ["[[trend-following]]", "[[tail-risk-hedging]]", "[[tail-hedging]]", "[[vix-calls]]", "[[dvol]]", "[[deribit]]", "[[funding-rate]]", "[[perpetual-futures]]", "[[crisis-alpha]]", "[[turtle-trading]]", "[[convexity]]", "[[cryptodataapi]]"]

# Edge characterization
edge_source: [structural, risk-bearing, analytical]
edge_mechanism: "Trend following generates crisis alpha in sustained downtrends via short perp positions, while the tail-hedge leg (Deribit OTM puts / long straddles) captures the sudden-onset flash crash that trend signals are too slow to detect; the combination costs less than either component alone because trend income offsets the put-buying bleed, and the counterparty is the leveraged-long perp holder liquidated in the cascade."

# Data and infrastructure requirements
data_required: [ohlcv-daily, funding-rates, open-interest, volatility-regime, options-chain]
min_capital_usd: 50000
capacity_usd: 500000000
crowding_risk: low

# Performance expectations
expected_sharpe: 0.9
expected_max_drawdown: 0.25
breakeven_cost_bps: 20

# Kill criteria
kill_criteria: |
  - trend component: rolling 12-month Sharpe < 0.3 (signals choppy regime killing trend edge)
  - tail hedge: annual cost exceeds 4% of NAV without a cascade payoff in 18 months (re-spec strikes/budget)
  - combined drawdown > 25% — reduce both components to half size
  - DVOL structurally above 90th percentile for > 60 days (new-regime bear; stop adding new put wings at peak cost)
gates:
  - id: trend_universe
    role: universe
    rule: "Trend core on BTC and ETH perps; SOL, BNB and up to 4-5 liquid alt perps as satellites"
    runnable: partial
    endpoint: /api/v1/hyperliquid/open-interest
    field: assets[].coin
    note: "BTC and ETH are fixed. Which alts qualify as liquid satellites is not defined (no volume or OI floor), so the desk picks them; assets[].day_volume and open_interest_usd are on the same rows."
  - id: ema_cross_long
    role: entry
    rule: "Trend long when the 50-day EMA of daily closes is above the 200-day EMA"
    runnable: true
    endpoint: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&limit=600
    field: candles[].close
    replay: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&start={start}
    replay_field: candles[].close
    note: "Compute both EMAs from closed daily bars (drop the forming bar named by forming_bar_timestamp); 600 bars gives the 200-day EMA time to settle. Hyperliquid daily history runs back to 2023."
  - id: ema_cross_short
    role: entry
    rule: "Trend short when the 50-day EMA of daily closes is below the 200-day EMA"
    runnable: true
    endpoint: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&limit=600
    field: candles[].close
    replay: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&start={start}
    replay_field: candles[].close
    note: "Same series as ema_cross_long."
  - id: fast_cross_sleeve
    role: entry
    rule: "Optional faster sub-allocation on the 20-day versus 50-day EMA crossover"
    runnable: partial
    endpoint: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&limit=200
    field: candles[].close
    replay: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&start={start}
    replay_field: candles[].close
    note: "The signal is mechanical, but the page gives no size for the sub-allocation, so that is the desk's call."
  - id: atr_unit_size
    role: sizing
    rule: "N-unit sizing: risk 0.5-1% of the portfolio per market per unit, using the 20-day ATR"
    runnable: true
    endpoint: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&limit=45&atr=20
    field: candles[].atr
    replay: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&start={start}
    replay_field: candles[].high
    note: "Units = risk budget / ATR in USD per coin. The example uses 0.75%. For replay, compute the 20-day ATR from high, low and close."
  - id: correlation_cap
    role: sizing
    rule: "Treat correlated alt perps (about 0.8+ to BTC in risk-off) as one BTC-beta unit for the correlation limits"
    runnable: partial
    endpoint: /api/v1/hyperliquid/candles/batch?coins={coin}&interval=1d&limit=90&closed_only=true
    field: series.{coin}[].close
    note: "Correlate daily returns with BTC's. The page names no correlation window, no exact cutoff and no cap on how many units the combined bucket may hold; those are the desk's call."
  - id: funding_drag
    role: filter
    rule: "Net expected funding against trend expectancy: longs pay positive funding, shorts pay negative funding"
    runnable: partial
    endpoint: /api/v1/hyperliquid/funding-rates?coin={coin}&limit=24
    field: history[].funding_rate
    replay: /api/v1/backtesting/hl-funding-bars?coin={coin}&interval=1d&start={start}
    replay_field: data[].funding_sum
    note: "Sum the last 24 hourly settlements for the daily carry. The page gives no funding level at which to cut or skip a trend position, so the cutoff is the desk's call."
  - id: quant_trend_vs_chop
    role: filter
    rule: "Before the trend leg deploys, use the HMM regime to separate a sustained trend from chop"
    runnable: partial
    endpoint: /api/v1/quant/market
    field: regime.label
    replay: /api/v1/quant/history?scope=market&start={start}
    replay_field: entries[].regime_label
    note: "From the page's data and agent-workflow sections, not its rules. Which labels count as chop (for example choppy_high_vol) and what the trend leg does then are not stated."
  - id: monthly_rebalance
    role: sizing
    rule: "On the first day of each month (or a major expiry), re-mark everything, rebalance trend positions to current signals and resize N-units for the new ATR"
    runnable: true
    input: position
  - id: sleeve_allocation
    role: sizing
    rule: "Allocate 70-80% to the trend core, 10-15% to OTM put wings, 5% to the straddle sleeve and 5-10% to a stablecoin reserve"
    runnable: true
    input: position
  - id: dvol_pctile_low
    role: filter
    rule: "Add put wings and straddles only when the DVOL percentile is below 40"
    runnable: partial
    endpoint: /api/v1/volatility/implied
    field: items[].history[].dvol
    note: "Rank today's dvol within items[].history (daily Deribit DVOL for BTC and ETH, about 180 days from 2026-04-20; history is Pro Plus). The page names no percentile lookback, so the 180-day window is a substitute. /volatility/regime compressed, which the page also cites, is realised vol, not DVOL."
  - id: term_contango
    role: filter
    rule: "Straddles only when the implied-vol term structure is in contango"
    runnable: partial
    endpoint: /api/v1/volatility/implied
    field: items[].term_structure[].atm_iv
    note: "Contango means atm_iv rises with expiry_days. The page does not say which tenors to compare (for example 7 days against 45 days), so that is the desk's call. Pro Plus."
  - id: put_wing_buy
    role: entry
    rule: "Buy BTC/ETH puts 20-35% out of the money, 45-90 days to expiry, USDC-margined, staggered across two expiries"
    runnable: false
    note: "No option chain, strike list or option premium is served; selecting and pricing the wing needs Deribit's chain. Only ATM implied vol per expiry is on /volatility/implied."
  - id: put_budget
    role: sizing
    rule: "Spend about 0.2-0.4% of the total portfolio per month on put premium"
    runnable: true
    input: position
  - id: put_roll
    role: exit
    rule: "Roll the put wings quarterly or when days to expiry fall below 14, into the next 45-90 DTE strike"
    runnable: true
    input: position
  - id: straddle_buy
    role: entry
    rule: "Buy 45-day ATM BTC/ETH straddles when dvol_pctile_low and term_contango hold; roll monthly"
    runnable: false
    note: "The two filters are served, but straddle quotes are not: term_structure gives ATM implied vol per expiry, not tradeable option prices. Price and fill the straddle on Deribit."
  - id: straddle_scale_out
    role: exit
    rule: "Begin scaling out of a straddle once its mark exceeds 2x its cost"
    runnable: false
    note: "Needs the straddle's own option mark, which comes from the Deribit position, not from any served endpoint."
  - id: cascade_monetize
    role: exit
    rule: "When a cascade hits, sell 50-70% of the puts and straddles into the spike instead of holding for maximum payout"
    runnable: partial
    endpoint: /api/v1/market-intelligence/squeeze-alerts?symbol={coin}&window_s=3600&include_quiet=true
    field: alerts[].triggered
    replay: /api/v1/backtesting/hl-liquidation-bars?coin={coin}&interval=1h&start={start}
    replay_field: data[].long_usd
    note: "The page does not define a cascade numerically (its examples are BTC -25% or DVOL 50 to 110). triggered with direction long_flush is the served cascade flag (OKX, Bybit and Hyperliquid; Binance not captured). The option marks to sell at come from Deribit. Replay is Hyperliquid fills from 2026-07-23."
  - id: reload_short
    role: entry
    rule: "After a payoff, use tail-hedge profits to fund new short perp entries once the trend signal confirms the downtrend"
    runnable: true
    input: derived
    inputs: [ema_cross_short]
  - id: profit_sweep
    role: sizing
    rule: "Sweep realised trend profits above the target allocation into the tail-hedge replenishment budget"
    runnable: true
    input: position
  - id: dvol_high_stop_wings
    role: filter
    rule: "Stop adding new put wings when DVOL has stayed above its 90th percentile for more than 60 days"
    runnable: partial
    endpoint: /api/v1/volatility/implied
    field: items[].history[].dvol
    note: "From the kill criteria. The served daily history is about 180 days, so a 90th-percentile rank over a longer base is not possible; the lookback is the desk's call. Pro Plus."
  - id: drawdown_half_size
    role: sizing
    rule: "Combined drawdown above 25%: cut both the trend and the tail components to half size"
    runnable: true
    input: position
---

# Trend Following + Tail Risk Hedge

## Edge source

**Structural**, **risk-bearing**, and **analytical**. See [[edge-taxonomy]].

The structural edge: crypto markets have two distinct crisis modes — slow trend-reversals (multi-week bear markets driven by rate tightening, liquidity withdrawal, or post-mania deleveraging) and sudden flash cascades (exchange insolvencies, stablecoin depegs, weekend liquidation spirals). Each mode defeats one component of the combination: trend-following signals are too slow for flash crashes; tail-hedge premium bleeds in sustained bear recoveries. Together they cover the full crisis-speed spectrum.

The risk-bearing edge: the tail-hedge component accepts premium bleed (paying the variance risk premium) in exchange for the convex payoff when perp longs are being auto-liquidated. The counterparty is the leveraged long who is forced to sell into the crash.

**Crypto implementation note — no tradeable VIX / DVOL future exists.** The equity version of this strategy uses VIX futures/calls as the tail-hedge instrument. In crypto there is no tradeable DVOL future or DVOL ETP. The crypto tail hedge is built entirely from [[deribit]] spot options: deep OTM BTC/ETH put wings and long straddles. Wherever this page references "VIX calls" in its historical context, read it as *Deribit long-straddle / OTM put wing* for crypto implementation. See [[tail-hedging]] and [[vix-calls]] for the full translation.

## Null hypothesis

If trend signals are not faster than the market at identifying sustained directional moves, the trend component earns zero after funding and slippage. If Deribit options are fairly priced (implied vol = subsequent realized), the tail-hedge component earns zero minus Deribit's wide wing spreads — a guaranteed cost. Under both nulls the combination is a negative-carry portfolio. Empirical evidence rejecting both nulls: trend signals on BTC/ETH perps with 50/200-day crossover logic have shown persistent positive returns across multi-year crypto cycles (2020–2024 period, subject to parameter overfitting risk); and BTC/ETH DVOL has historically priced in excess of subsequently realized vol — the variance risk premium — meaning put wings are fairly expensive but occasionally blow out many multiples in flash cascades, making the bleed worthwhile at the portfolio level.

## Overview

Trend following and tail risk hedging are two of the most powerful crisis-fighting strategies, but they cover different types of crises. [[trend-following]] generates "crisis alpha" — profits during sustained market declines — because it systematically goes short as downtrends develop. In crypto, perp-based trend following has caught the 2022 bear (BTC −75%), the post-FTX decline, and multiple altcoin bear cycles, while also running long in bull phases. But trend following is reactive: it needs time to detect and position for a trend. A flash crash, a sudden gap-down, or a one-hour 12% drop (2025-10-10) happens too fast for trend signals to respond.

[[tail-risk-hedging]] — deep out-of-the-money BTC/ETH puts and long straddles on [[deribit]] — provides instant protection against exactly these sudden shocks. But tail hedging is expensive: the constant premium bleed in normal markets consumes 2–4% of portfolio value annually, which is a crushing drag during the majority of time when markets are calm. And Deribit's wide OTM wing spreads (3–8 vol points round-trip) make the cost heavier than the equity equivalent.

**The combination solves both weaknesses.** Trend following covers extended crises and actually profits during most of the year. Tail hedges cover the sudden shocks that trend following misses. The income from trend following in normal markets offsets the cost of tail hedges. Together, they create a portfolio that is protected against both slow and fast crises.

## The Synergy

**Complementary crisis coverage.** Crises come in two speeds:

*Slow crises* (2000-2002 dot-com bust, 2007-2009 financial crisis, 2022 rate hiking cycle): Markets decline over months or years with identifiable trends. Trend following captures these beautifully — CTA indices were up 20-40% in 2008 while the S&P 500 fell 37%. But the initial move can be missed.

*Fast crises* (Black Monday 1987, COVID March 2020, Flash Crash 2010): Markets collapse in days or hours. No trend signal is fast enough. Deep OTM puts and VIX calls explode in value during these events — a VIX call bought at $15 strike might pay out at $80. But between fast crises, these hedges expire worthless month after month.

The combination covers the full speed spectrum of market disaster.

**Cost efficiency through trend-following profits.** The biggest objection to tail risk hedging is cost. If you spend 3% annually on puts and the market goes up, you have a 3% drag that compounds painfully over time. But trend following generates positive returns in normal trending environments (not just crises). In typical years, a diversified trend-following strategy earns 5-15% annually. This income more than offsets the tail hedge premium cost, making the combined portfolio self-funding.

**Portfolio-level convexity.** Trend following has moderate convexity — it profits more in large moves than small ones. Tail hedges have extreme convexity — they are worth nearly zero in normal markets and worth 10-100x in crashes. Combined, the portfolio develops a powerful convex return profile: small losses in choppy markets, reasonable gains in trending markets, and explosive gains in crises.

## Component Strategies

| Component | Allocation | Role | Crypto instrument |
|-----------|-----------|------|---------------|
| [[trend-following]] (crypto perps/futures) | 70–80% | Core strategy, crisis alpha, trend capture | BTC/ETH perps (Binance/Bybit/Hyperliquid), 50/200-day MA crossover |
| Tail hedge — Deribit OTM puts | 10–15% | Flash-crash / sudden-onset protection | 20–35% OTM BTC/ETH puts, 45–90 DTE, USDC-margined |
| Tail hedge — Deribit long straddle sleeve | 5% | DVOL-spike volatility protection; direction-agnostic | 45-day ATM BTC/ETH straddles (the crypto analog of "VIX calls" — there is no DVOL future) |
| Stablecoin reserve | 5–10% | Collateral, rebalancing, reload budget | USDC in exchange or on-chain yield; earns carry while waiting |

**Note on VIX calls:** the equity version of this combination (e.g., "Dragon Portfolio") uses VIX call options — a call on a *tradeable volatility future*. **Crypto has no equivalent.** DVOL is a published reference index, not a tradeable product. The closest crypto analog to a VIX call is a long Deribit straddle (direction-agnostic vol-spike exposure) or a deep OTM put wing (crash-specific). Both decay via option theta rather than through roll-yield mechanics; the cost structure is similar but not identical. See [[vix-calls]] for the detailed translation and [[tail-hedging]] for instrument selection.

## Implementation

**Step 1 — Trend-Following Core (75–80% allocation)**

Deploy a systematic trend-following strategy on crypto perpetuals:

- **Markets:** BTC/USDT perp, ETH/USDT perp as the core. SOL, BNB, and up to 4–5 liquid alts as satellite — but apply correlation caps aggressively (most alts are ~0.8+ correlated to BTC in risk-off moves).
- **Signal:** Dual moving average crossover — 50-day and 200-day EMA. Go long when short MA > long MA; short when below. A faster signal (20/50-day) for a sub-allocation can catch quicker trend-starts.
- **Position sizing:** ATR-based N-unit sizing (see [[turtle-trading]]): risk 0.5–1% of portfolio per market per unit based on 20-day ATR. Equalizes risk across BTC's and altcoins' very different volatility profiles.
- **Funding cost overlay:** holding long perps through positive funding and short perps through negative funding is the dominant ongoing P&L leak. Net expected funding against the strategy; in strongly positive funding environments, the long trend-following leg pays significant daily carry.
- **Correlation caps:** treat correlated alt perps as a single BTC-beta unit for the purpose of the correlation limits.

**Step 2 — Tail Risk Layer (15–20% allocation)**

Deploy two Deribit-based structures *(the crypto equivalent of the equity SPX puts + VIX calls layer)*:

*Deep OTM BTC/ETH Put Wings (10–15% of total):*
- Buy puts 20–35% OTM, 45–90 DTE, USDC-margined (linear). At DVOL percentile < 40, buy put wings (cheap protection when the crowd is paying up for calls).
- Spend approximately 0.2–0.4% of total portfolio per month on put premium.
- These wings are nearly worthless most of the time. In a cascade (BTC −25%+, DVOL 50 → 110), they can pay 6–15× their cost.
- Roll quarterly or when DTE drops below 14: sell and re-initiate at the next 45–90 DTE strike.

*Long Straddle Sleeve (5%) — the "crypto VIX call":*
- Buy 45-day ATM BTC/ETH straddles when DVOL percentile < 40 and term structure is in contango.
- This captures DVOL-spike exposure *regardless of direction* — the straddle pays on both up-spike (melt-up gamma) and down-spike (crash). This is what a VIX call would do in equity markets.
- Monetize fast into any DVOL spike (> 2× cost → begin scaling out); crypto vol reverts within days.

**Step 3 — Monthly Rebalancing**

On the first day of each month (or on a major expiry):
1. Mark all positions to market.
2. Rebalance trend-following perp positions based on updated signals; adjust N-unit sizes for updated ATR.
3. Roll expiring Deribit puts/straddles before DTE < 14.
4. Sweep realized trend-following profits above target allocation into the tail-hedge replenishment budget.
5. If a tail hedge paid off in a cascade, monetize into the spike and reload into the trend-following short side once signals confirm the new downtrend.

**Step 4 — Crisis Execution**

When a cascade hits:
- Tail hedges pay off immediately (within hours for deep OTM puts in a crash; the straddle's long gamma pays from the first sigma move).
- Take partial profits on puts and straddles (sell 50–70%) — do not hold for maximum payout, as crypto vol reverts within days or even hours (2025-10-10 example).
- Trend-following signals will start flipping short within days to weeks.
- Use tail-hedge profits to reload stablecoin and fund new short perp entries as the trend confirms.
- The cascade: tail hedges buy time and capital while trend-following catches up.

## Example Trade

**$1,000,000 crypto portfolio:**

- **$750,000 in crypto trend-following:** BTC/ETH/SOL perps on Binance + Hyperliquid, 50/200-day MA crossover, 0.75% risk per market per unit via 20-day ATR. Current positions (illustrative): long BTC (200-day MA = $62k, spot = $68k), long ETH.
- **$125,000 in Deribit OTM puts:** Buy 10× BTC $50,000 puts (25% OTM if BTC at $68k), 90 DTE, USDC-margined, at ~$1,800 each = $18,000 cost per quarter. Stagger across two expiries. Remaining budget reserved for rolling and DVOL-percentile-gated adds.
- **$50,000 in Deribit long straddles:** Buy 2× BTC 45-day ATM straddles at ~$8,500 each = $17,000 total. Roll monthly.
- **$75,000 stablecoin reserve (USDC):** Collateral and rebalancing buffer; earns on-chain yield while waiting.

**Annual cost of tail hedge layer:** approximately $150,000–200,000 (2–3% of portfolio). In a trending year, the trend-following core targets 15–30% return, making the combination roughly self-funding.

**In a 2025-10-10-style flash cascade:** BTC drops 12% in 60 seconds, ~$19B liquidated. The ATM straddles explode (DVOL 50 → 130); the OTM puts gain significant delta as spot approaches the strike. Monetize 60% of both positions into the spike (vol reverts within hours). The trend component transitions to short as the event resolves into a new downtrend, catching the continuation. Combined: the cascade loss is offset by tail-hedge monetization; the trend component captures the subsequent downtrend.

## When It Excels

- **Sustained bear markets** — this is what the combination is built for. Both components profit during extended declines (trend-following goes short; tail hedges pay on the initial shock). Crypto bear markets (2022, lasting 11 months) are ideal trend-following conditions.
- **Flash crashes and cascades** — the tail hedge (Deribit puts/straddles) captures the sudden-onset 10%+ moves that a trend signal is too slow to respond to. In a 2025-10-10-style event, the tail hedge pays within minutes.
- **As a portfolio diversifier** — this combination has extremely low (often negative) correlation to buy-and-hold crypto, making it a natural complement to a core spot BTC/ETH holding.
- **For traders running a core directional crypto book** — the trend component captures bull and bear macro phases; the tail hedge insures against the sudden shocks that can wipe a leveraged long book.

## When It Fails

- **Low-volatility, sideways range-bound markets** (crypto in 2023-Q1 or the mid-2024 consolidation). Trend-following signals whipsaw with small losses, and Deribit put wings bleed premium month after month. The combined drag can be 5–10% in a single calm year.
- **V-shaped recoveries** — the 2020 COVID crash in crypto saw BTC drop 50% and recover in weeks. Trend-following signals may flip short just before the reversal, giving back gains. The tail hedge profits on the down move but the trend component loses on the whipsaw.
- **Persistent positive funding / melt-up regimes** — in a strongly positive-funding bull, trend longs pay funding carry, reducing net returns, while put wings bleed with no cascade payoff.
- **Altcoin correlation collapse** — if the trend component is diversified across alts and BTC goes flat while alts diverge, the correlation caps bind and reduce the trend signal quality.
- **Deribit wing cost above budget** — if DVOL is structurally elevated (post-crash regime break), OTM put wings become very expensive and the tail hedge bleed exceeds trend income.

## Capacity limits

The trend component scales to the perp market's capacity — BTC perps alone have $5B+ open interest; the trend-following style can absorb $500M+ before material impact. The tail-hedge component scales with Deribit's OTM wing depth: clean fills to $5–25M vega-notional on BTC, above which the Paradigm/greeks.live RFQ network is needed. Practical total capacity for the combined strategy: $50–500M, with the constraint on the tail side.

## What kills this strategy

1. **Trend-following component in a perpetual chop regime** — crypto 2023-H1 and similar range-bound periods produce many whipsaw losses and no trend income to offset the tail-hedge bleed; the combination turns net-negative carry.
2. **Tail-hedge monetization failure** — failing to sell the Deribit puts/straddles into the cascade DVOL spike. Crypto vol reverts within hours to days; a hedger who waits watches a 10× mark revert to 1×.
3. **Over-sizing the trend component into a leveraged-long regime** — if the trend signal is long and perp funding is strongly positive, the combination bleeds from two directions (tail bleed + funding bleed) without a compensating trend trend.
4. **Deribit single-venue concentration** — the tail hedge is on Deribit; a Deribit outage or insolvency during a cascade is an un-hedgeable risk.
5. **Correlation collapse in crypto alts** — the "diversified" trend book behaves like a single BTC-beta bet in risk-off; the correlation caps must be enforced strictly.
6. **Budget creep on the tail hedge** — letting the bleed exceed 4% of NAV/year turns the combination into a negative-carry portfolio.

## Kill criteria (numeric)

*(From frontmatter — duplicated here for reference)*
- Trend component rolling 12-month Sharpe < 0.3 (choppy regime)
- Tail hedge annual cost exceeds 4% of NAV without cascade payoff in 18 months (re-spec)
- Combined drawdown > 25% — reduce both components to half size
- DVOL structurally above 90th percentile for > 60 days (new-regime bear; stop adding put wings at peak cost)

## Real-World Usage

**Crypto context:** several crypto funds have run explicit trend + tail combinations. The 2022 bear market demonstrated both components working: perp short positions (via trend signals) generated alpha in the 11-month decline; BTC/ETH OTM puts fired during the LUNA crash (May 2022) and FTX insolvency (November 2022) — exactly the "sudden onset" moments the tail hedge is designed for.

**[[universa-investments|Universa Investments]]** ([[mark-spitznagel|Mark Spitznagel]], advised by [[nassim-taleb|Nassim Taleb]]) reportedly returned over 4,000% in March 2020 *(equity markets; cited as the methodological ancestor of the tail-hedge discipline)*. Universa's pure tail hedge is difficult to hold through the years of bleed; the trend component is the income source that makes it sustainable.

**Man AHL, Winton, and major CTAs** run diversified trend-following strategies that form the core of this combination in TradFi *(equity/multi-asset; cited as historical context)*. The crypto-native equivalent is a BTC/ETH perp-based systematic trend system with similar signal architecture.

**The "Dragon Portfolio"** concept (Artemis Capital, Chris Cole) advocates combining trend following + tail risk hedging + long-vol + growth assets across 100 years of data *(equity/commodity construct; the crypto adaptation uses perps and Deribit options in place of equity futures and SPX/VIX structures)*.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d` — OHLCV for MA crossover signals and ATR sizing
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — funding overlay: net against trend-following expectancy
- `GET /api/v1/volatility/regime` — vol regime: DVOL percentile context for tail-hedge entry timing
- `GET /api/v1/market-intelligence/liquidations` — cascade early warning for tail-hedge monetization timing
- `GET /api/v1/quant/market` — HMM regime probabilities; is the market in a sustained trend or chop?

**Historical:**
- `GET /api/v1/backtesting/klines` (REST bars start 2026-05-09; older 1h/4h/1d bars are in the `klines_deep` archive) — OHLCV history for MA crossover backtesting
- `GET /api/v1/backtesting/funding` — historical funding to net against trend expectancy
- `GET /api/v1/backtesting/liquidations` — historical cascade data to backtest tail-hedge monetization timing

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/volatility/regime"
```

Auth: `X-API-Key` header. DVOL and the Deribit IV surface come from Deribit / [[greeks-live]], not CryptoDataAPI. Full catalog: [[cryptodataapi-market-data]], [[cryptodataapi-derivatives]], [[cryptodataapi-regimes]].

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [liquidations](https://cryptodataapi.com/liquidations) · [short-term regimes](https://cryptodataapi.com/market-regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run both legs end-to-end:

- **Signal** — daily klines run the MA-crossover trend engine and ATR sizing
- **Hedge timing** — `GET /api/v1/volatility/regime` (`compressed` = cheap wings) and `GET /api/v1/market-intelligence/liquidations` (cascade early-warning) time tail-hedge entry and monetization
- **Regime gate** — `GET /api/v1/quant/market` HMM probabilities separate sustained trend from chop before the trend leg deploys
- **Backtest** — `GET /api/v1/backtesting/klines` (Binance spot 1h/4h/1d back to 2017-08 only in the `klines_deep` archive, while the REST route starts 2026-05-09) for the trend leg, `GET /api/v1/backtesting/funding` (Hyperliquid hourly since 2023-05) for carry drag, and `GET /api/v1/backtesting/liquidations` (since 2026-03-30) for hedge-monetization triggers
- **Tips** — the hedge leg is priced on Deribit, not CDA; run the monetization decision off CDA cascade data but verify option marks before selling wings into a spike

## Related

- [[trend-following]] — the core trend discipline
- [[tail-risk-hedging]] — the systematic put-overlay discipline
- [[tail-hedging]] — the convex-hedging mechanics
- [[vix-calls]] — the crypto long-vol overlay (Deribit straddles, put wings; the analog to equity VIX calls)
- [[dvol]] — the crypto fear gauge (not tradeable directly; used to time tail entries)
- [[deribit]] — venue for the tail-hedge options
- [[funding-rate]] — the trend component's ongoing carry cost/credit
- [[perpetual-futures]] — the dominant crypto trend instrument
- [[crisis-alpha]] — the property the combination exhibits in bear markets
- [[cryptodataapi]] — data layer for signals, regime, and liquidations

**See also:** [[turtle-trading]] (full trend system with crypto adaptations), [[convexity]], [[antifragility]], [[fat-tails]], [[drawdown]]
