---
title: Mean Reversion
type: strategy
created: 2026-04-06
updated: 2026-07-19
status: excellent
tags:
  - quantitative
  - mean-reversion
  - crypto
  - swing-trading
aliases:
  - mean-reversion-strategy
  - reversion-to-mean
  - short-term reversal
related: ["[[rsi-mean-reversion]]", "[[bollinger-band-reversion]]", "[[pairs-trading]]", "[[momentum]]", "[[statistical-arbitrage]]", "[[liquidation-cascade-fade]]", "[[funding-rate-arbitrage]]"]
strategy_type: quantitative
timeframe: swing
markets: [crypto]
complexity: intermediate
backtest_status: untested
edge_source: [behavioral, risk-bearing]
edge_mechanism: "Leveraged, forced, and narrative-chasing crypto flow overshoots fair value when it demands immediate liquidity into thin 24/7 books; the reversion trader is paid to absorb that flow and hold until price snaps back to a short-window mean."
data_required: [ohlcv-1h, ohlcv-daily, funding-rates, liquidations, volatility-regime]
min_capital_usd: 2000
capacity_usd: 15000000
crowding_risk: medium
expected_sharpe: 0.5
expected_max_drawdown: 0.35
breakeven_cost_bps: 25
decay_evidence: "Short-horizon reversal in liquid crypto (BTC/ETH majors) has weakened as CEX market-making tightened spreads post-2021 and perp-DEX liquidity deepened; the residual edge has migrated to alt perps and to liquidation-driven overshoots (see [[liquidation-cascade-fade]]). Crypto reverts on short horizons but trends violently on medium ones, so the reversion window is narrow and regime-dependent."
kill_criteria: |
  - rolling 12-month net Sharpe < 0
  - drawdown > 30% of allocated capital
  - hit rate < 48% over trailing 200 trades
  - rolling 30-day Hurst exponent of the traded universe > 0.55 for 6 consecutive weeks
  - median realized round-trip cost > 25 bps for a full month
---

# Mean Reversion

A systematic strategy that bets crypto prices return to a short-window average after an outsized deviation. The signal is usually a z-score, [[rsi]](2), or a [[bollinger-band-reversion|Bollinger band]] touch on 1h–1d bars; the trade is a fade of the overshoot back toward the mean. Mean reversion is one of the two great families of systematic trading (the other being [[trend-following]]/[[momentum]]) and underpins [[pairs-trading]], [[statistical-arbitrage]], and most crypto market-making. In crypto it is far noisier and more reflexive than in equities — the same 24/7 leverage that produces clean overshoots also produces violent trends that punish an ill-timed fade.

## Edge source

Per the [[edge-taxonomy]], crypto mean reversion draws primarily on two edge categories:

- **Behavioral** — crypto participants systematically overreact to listings, unlocks, liquidation headlines, and social-media narratives, extrapolating a 15-minute move into a thesis. The equity literature (De Bondt & Thaler 1985 on long-horizon overreaction; Lehmann 1990 and Jegadeesh 1990 on short-term reversal) documents the same behavior in a slower market; crypto is that effect on 10x leverage and no closing bell.
- **Risk-bearing (liquidity provision)** — a large fraction of short-horizon reversion profit is compensation for absorbing forced order flow. When a leveraged long book is liquidated, the exchange engine market-sells non-economic supply into a thinning book; the reversion trader collects the concession and carries inventory risk until the patient bid returns. This is the mild, higher-timeframe cousin of [[liquidation-cascade-fade]].

The trade does **not** rely on informational or analytical edge — everyone can compute a z-score. The edge is in having the discipline and risk control to be the counterparty to panic in a market that trends hard enough to bankrupt an undisciplined fader.

## Why this edge exists

Crypto prices oscillate around short-window means because the marginal price-setter during a dislocation is rarely a valuation-driven buyer. Who is on the other side, and why do they keep paying?

- **Forced and leveraged flow** — perp liquidations, margin calls, and stop cascades generate price-insensitive selling (or buying). These participants are not stupid; they are paying for immediacy, and the need for immediacy never disappears while perps offer 20–100x leverage on a single click. See [[liquidation]] and [[funding-rate]].
- **Narrative-chasing retail** who buy after a coin 3x's and panic-sell after it halves, manufacturing the overshoot that reverts.
- **Thin 24/7 books and weekend liquidity gaps** — market makers widen or pull during high realized volatility, and depth is thinnest during Asian-hours weekends. A dislocation can stay dislocated for hours because natural liquidity is absent, not because the move is informationally justified.

The edge persists because providing this liquidity is genuinely unpleasant: crypto's fat tails mean the occasional dislocation that *doesn't* revert (a depeg, a hack, a regime break) can wipe a quarter of small wins. That tail deters enough capital to keep a residual premium — but the premium is smaller and more regime-dependent than the equity literature implies.

### Variants across timeframe and instrument

| Variant | Horizon | Signal | Capacity | Notes |
|---------|---------|--------|----------|-------|
| Micro reversal (market-making) | seconds–minutes | Micro z-score vs mid | Low | Latency-sensitive; a different (latency-edge) business |
| [[liquidation-cascade-fade]] | minutes–hours | Liquidation spike + CVD exhaustion | Low (~$2M/event) | The sharpest, most reflexive reversion setup |
| Short-term single-name (this page) | hours–days | 1h/1d z-score, [[rsi]](2) | Medium ($5–15M) | Canonical implementation; alts revert cleaner than BTC |
| Funding-extreme fade | hours–days | Perp funding z-score | Medium | Extreme positive funding = crowded longs due to unwind |
| [[bollinger-band-reversion]] | hours–days | BB touch + ranging filter | Medium | Volatility-adaptive bands |
| Cross-sectional reversal | days | Rank past-week alt losers vs winners | Medium | Long-short, BTC-beta-neutralized; Lehmann-style |

All variants share the same economics — being paid to provide immediacy — but trade off **capacity against per-trade edge** and **cost sensitivity** (see [[#Performance characteristics]] and [[#Capacity limits]]).

## Null hypothesis

If crypto prices followed a random walk (Hurst exponent ≈ 0.5, no serial correlation), buying after drops and selling after rips would produce zero expected gross return and a *negative* net return equal to round-trip costs times turnover. Concretely: a 1h/1d z-score reversal system running ~300% annual turnover per side at 25 bps round-trip would bleed roughly 7–8% per year under the null. Any backtest must beat this cost drag with statistical significance — and must also beat a "short volatility" benchmark, since naive reversion P&L in crypto is highly correlated with simply selling [[volatility]] into a market that periodically detonates.

The crypto-specific null is stricter than the equity one because crypto's Hurst exponent spends long stretches *above* 0.5 (persistent trending) during bull impulses and capitulations. A reversion edge that only shows up in a range-bound sample is not an edge — it is a regime bet that must be gated by [[regime-detection]].

## Rules

A representative single-name crypto z-score implementation on 1h bars (liquid perps or spot):

**Universe and filters**
- Liquid coins only: top ~30 by perp open interest and CEX spot volume (BTC, ETH, SOL, and liquid L1/L2/major alts). Illiquid alt books produce larger overshoots but un-exitable slippage.
- Exclude coins with a scheduled catalyst inside the holding window — token unlock, mainnet/upgrade date, exchange-listing event, or known macro print (FOMC, CPI). Catalyst-driven moves revert far less reliably. Cross-check the CDA event calendar (see [[#Getting the Data (CryptoDataAPI)]]).
- Confirm the series is currently mean-reverting (rolling Hurst < 0.5, ADF stationary on the last N bars) and that [[volatility]]/[[regime-detection]] does not flag a `vol_shock` or `strong_trend` state.

**Entry**
- Compute z = (price − N-bar SMA) / N-bar standard deviation, N = 20 bars on the chosen timeframe (20h or 20d).
- Buy when z ≤ −2.0; short when z ≥ +2.0. In crypto, prefer the **long** side in a BTC uptrend and be far more cautious shorting strength (crypto squeezes are vicious).
- Confirmation filters: 2-period [[rsi]] < 10 for longs (> 90 for shorts); price on the correct side of the 200-bar SMA (trade reversion with the higher-timeframe trend); perp **funding not extreme against you** (do not buy a dip while funding is deeply negative and still falling — that is an ongoing liquidation, not exhaustion).

**Exit**
- Take profit when z crosses back through 0 (price returns to the 20-bar mean).
- Time stop: exit after ~10 bars-of-the-timeframe (e.g., 10 days on daily, 10 hours on hourly). If it has not reverted, the dislocation is probably informational (hack, depeg, delisting).
- Hard stop: exit if price moves a further 1.5σ against entry, or on any liquidation-cascade acceleration against the position.

**Position sizing**
- Risk a fixed fraction (0.5% of equity) per position to the hard stop; cap any single coin at 5% of the book; run 8–20 concurrent positions for breadth.
- Scale gross exposure down by 50% when the [[volatility]] regime is `expanding`/`vol_shock` or realized BTC vol exceeds ~2× its 90-day median — reversion failure clusters in high-vol regimes.
- Prefer 1–2x notional; leverage on a negative-skew fader is how a good month becomes a blown account.

## Implementation pseudocode

```python
# crypto short-term z-score reversion — 1h or 1d bars
for coin in liquid_universe:                       # top-30 by OI + spot volume
    if has_catalyst_within(coin, bars=10):         # unlock / listing / macro print
        continue
    if vol_regime(coin) in ("vol_shock", "strong_trend_bull", "strong_trend_bear"):
        continue                                   # regime gate — CDA /volatility/regime, /quant/market
    sma   = mean(close[coin][-20:])
    sigma = std(close[coin][-20:])
    z     = (close[coin][-1] - sma) / sigma
    fund  = funding_8h[coin]                        # CDA /derivatives/funding-rates

    pos = positions.get(coin)
    if pos is None:
        long_ok  = z <= -2 and close[coin][-1] > sma200(coin) and fund > -0.0005
        short_ok = z >= +2 and close[coin][-1] < sma200(coin) and fund <  0.0005
        if long_ok:
            buy(coin, size=risk_budget(0.005, stop_dist=1.5 * sigma))
        elif short_ok:                              # used sparingly; crypto squeezes hard
            sell_short(coin, size=risk_budget(0.005, stop_dist=1.5 * sigma))
    else:
        crossed_mean = (pos.side == LONG and z >= 0) or (pos.side == SHORT and z <= 0)
        stopped      = pos.adverse_move() > 1.5 * pos.entry_sigma
        expired      = pos.bars_held >= 10
        if crossed_mean or stopped or expired:
            close_position(coin)

if realized_vol(BTC, 20) > 2 * median(realized_vol(BTC, 20), lookback=2160):  # 90d of 1h
    scale_gross_exposure(0.5)
```

## Indicators / data used

- **Z-score** — the primary signal; standard deviations of price from a 20-bar SMA.
- **[[rsi]](2)** — short-lookback RSI for oversold/overbought confirmation; see [[rsi-mean-reversion]].
- **[[bollinger-bands]]** — volatility-adaptive band touch; see [[bollinger-band-reversion]].
- **[[funding-rate]]** — extreme perp funding flags a crowded book; deeply negative-and-falling funding is a *do-not-catch-the-knife* filter. See [[funding-rate-arbitrage]].
- **[[liquidation]] feed** — a liquidation spike into the position is the difference between exhaustion and an ongoing cascade.
- **[[volatility]] / [[regime-detection]]** — the on/off switch; reversion is gated to non-trending, non-shock regimes.
- **Stationarity diagnostics** — clean OHLCV plus a catalyst calendar.

### Identifying mean-reverting crypto series

Not everything reverts, and crypto's reversion is unstable across regimes. The three core diagnostics:

| Test | What it measures | Mean-reverting signal | Crypto caveat |
|------|------------------|------------------------|--------|
| Augmented Dickey-Fuller (ADF) | Presence of a unit root | p-value < 0.05 (reject unit root) | Flips out-of-sample fast; re-test weekly, not monthly |
| Hurst exponent (H) | Long-memory / persistence | H < 0.5 | Crypto spends long stretches at H > 0.5 during impulses |
| Half-life ([[ornstein-uhlenbeck]] fit) | Speed of reversion | Short half-life (≈ holding period) | Assumes constant mean; unlocks/hacks permanently shift it |

A robust workflow runs all three and trades only series that pass on multiple measures, then re-tests **frequently** because crypto mean-reversion is aggressively regime-dependent — the same coin flips from H < 0.5 to H > 0.5 the moment BTC breaks range (the primary kill mechanism in [[#What kills this strategy]]).

## Example trade

SOL trades at $150 with a 20-hour SMA of $158 and 20-hour σ of $4. A cross-market risk-off wobble and a cluster of perp long-liquidations flush SOL down 5% in two hours on no SOL-specific news; z = (150 − 158)/4 = −2.0, 2-period RSI is 7, price remains above its 200-hour SMA, and 8h funding is +0.01% (not a bear cascade). The trader buys $3,000 notional, risking 0.5% of a $60k book to a stop at $144 (1.5σ below entry). Over the next six hours the forced selling exhausts and SOL drifts back to $157 as z crosses zero. Exit at $157: +4.7% on the position, ~+1.7R, holding period 6 hours. Round-trip cost on a liquid perp: ~12 bps taker + ~4 bps slippage ≈ 16 bps — comfortably inside the move.

## Performance characteristics

Realistic, cost-corrected expectations for a careful crypto implementation (not a backtest of this exact spec):

- **Gross edge per trade is small**: liquid-coin 1h/1d reversion signals earn ~30–120 bps gross per round trip with 52–62% win rates. Edge is harvested through frequency and breadth, not big winners.
- **Cost sensitivity is the defining feature, and crypto costs are higher than equities**. At 300–500% annualized turnover per side, every 10 bps of round-trip cost removes ~3–5 points of annual return. See the overlay below.
- **Realistic net expectation**: net Sharpe ~0.3–0.7 (frontmatter assumes 0.5) with negative skew — many small wins punctuated by sharp losses when a "dip" is a depeg, hack, or the first leg of a bear trend.
- **Drawdowns cluster in crypto crises**: reversion books were run over on 2022-05 (LUNA), 2022-11 (FTX), 2024-08-05 (yen carry unwind), and 2025-10-10, when "oversold" kept getting more oversold. Expect peak drawdowns around 25–35% of allocated capital (frontmatter assumes 35%).

**Cost overlay (crypto, per round trip):**

| Component | Magnitude | Note |
|---|---|---|
| Taker fee (perp, both legs of round trip) | ~8–11 bps | Binance 5 bps, Bybit 5.5 bps, Hyperliquid ~4.5 bps taker; maker quoting cuts this |
| Spot alternative (both legs) | ~10–20 bps | CEX spot taker 5–10 bps/side; wider than perps |
| Slippage | 2–5 bps majors, 10–40 bps alts | Thin books at the exact moment you fade |
| Funding carry during hold | ±1–3 bps/day | A cost or a credit depending on side and regime |
| **All-in round trip** | **~15–35 bps** | vs ~30–120 bps gross edge — costs eat 20–50% |

The arithmetic is unforgiving: the reversion edge only survives with maker-biased execution, liquid coins, and tight regime gating. Naive taker execution on alt spot destroys it.

## Capacity limits

Short-horizon reversion *is* liquidity provision — the bigger you trade, the more you become the impatient flow you are fading. On the top-30 liquid crypto perp/spot universe, holding 8–20 positions for hours-to-days, market impact begins to dominate somewhere in the **$5–15M** range (frontmatter assumes $15M); participation above ~1–2% of a coin's rolling volume during the entry window measurably erodes the per-trade edge. BTC/ETH majors offer more capacity but weaker per-trade edge; alt perps offer sharper overshoots but brutally low absorbable size. Scaling beyond this means diversifying across many smaller, thinner alt events — trading capacity for microstructure risk.

## Mean reversion vs momentum

Mean reversion and [[momentum]]/[[trend-following]] are near-opposites, which is precisely why they diversify each other — and in crypto, momentum is the *stronger* base-rate family, so reversion must be gated:

| Dimension | Mean reversion | Momentum / trend |
|-----------|----------------|------------------|
| Bets that | Overshoots snap back | Trends persist |
| Best regime | Range-bound, choppy | Persistent, directional (crypto's default in impulses) |
| Hurst exponent of edge | H < 0.5 | H > 0.5 |
| Return skew | **Negative** (small wins, sharp losses) | **Positive** (small losses, big wins) |
| Implicit vol exposure | Short volatility | Long volatility / convexity |
| Worst environment | Trending breakouts, liquidation cascades against you | Whippy, mean-reverting chop |
| Holding period | Short (hours–days) | Longer (days–weeks) |

Because the two profiles are mirror images on skew and vol exposure, sizing each by [[market-regime]] (via the rolling Hurst exponent or the CDA quant-market HMM; see [[regime-detection]]) smooths the equity curve far more than either alone. Regime detection is the practical key to running both.

## What kills this strategy

The most likely failure modes (see [[failure-modes]]):

1. **Regime change** — the market shifts from range to trend and every fade loses. Crypto does this faster and more violently than equities; the rolling Hurst drifting above 0.5 is the statistical fingerprint. This is the dominant risk.
2. **Reflexive liquidation cascades** — a fade entered before CVD exhaustion gets run over by the next liquidation leg (2022-05, 2024-08-05, 2025-10-10). The line between "mild higher-TF reversion" and "catching a cascade" is thin.
3. **Informational dislocations** — fading a move actually justified by a hack, depeg, exploit, or delisting. Catalyst filters reduce but never eliminate this; in crypto the tail event is often a total loss on the coin.
4. **Crowding / deleveraging spirals** — when many reversion and stat-arb books hold similar inventory, one forced unwind moves prices against everyone (the crypto analogue of the August 2007 equity quant quake).
5. **Cost creep** — spread widening on alts, adverse funding, or slippage growth quietly pushing per-trade cost above the ~25 bps breakeven.
6. **Short-vol blowup** — unhedged reversion is implicitly short volatility; a crypto vol regime shift produces correlated losses across the whole book at once.

## Kill criteria

- Rolling 12-month net Sharpe < 0.
- Drawdown > 30% of allocated capital.
- Hit rate < 48% over the trailing 200 trades (vs ~52–62% design expectation).
- Rolling 30-day Hurst exponent of the traded universe > 0.55 for 6 consecutive weeks (the universe has stopped mean-reverting).
- Median realized round-trip cost > 25 bps for a full month.

See [[when-to-retire-a-strategy]].

## Instrument Structures

Mean reversion deploys across three structure types depending on the signal and target:

| Structure | Role in this strategy |
|-----------|----------------------|
| **Single-asset** | The primary deployment. Fade an individual token's overshooting move — long after a sharp decline or short after a sharp rally — holding for a reversion to the short-window mean. Simple entry/exit logic, one leg, no hedge. |
| **Pair** | The market-neutral extension: when the single-asset move is suspected to be sector-wide (e.g., all L1s sold off together), express the reversion as a pair — long the most oversold asset in the sector, short the least oversold — to strip out the shared beta and isolate the idiosyncratic reversion. This is the [[pairs-trading]] overlap. |
| **Basket** | Used as a sector-level filter or entry gate: if the sector basket has mean-reverted (returned to its short-window mean) but individual tokens within it have not, the basket-level signal identifies laggards still to catch up — a within-basket relative reversion. |
| Cross-venue | Not deployed in standard mean reversion. Cross-venue reversion (same token, different venues) is [[cross-exchange-arbitrage]] territory. |

The mechanics differ between structures: single-asset reversion uses raw z-score of returns vs. a 5–20 day window; pair reversion uses the spread z-score and cointegration (see [[pairs-trading]]); basket reversion computes the average z-score across sector constituents to identify over/under-sold sectors rather than single names.

## Advantages

- High trade frequency gives statistical significance quickly — you learn fast whether the edge is real in the current regime.
- Positive expectancy in flat/choppy crypto markets where trend strategies bleed; a natural diversifier to [[momentum]] and [[trend-following]] books.
- Short holding periods limit exposure per position; 24/7 markets mean no overnight gaps (though weekends are thin).
- Conceptually simple, cheap data (OHLCV + funding + a catalyst calendar), and grounded in both behavioral and liquidity-provision economics.

## Disadvantages

- Negatively skewed: steady small gains punctuated by sharp losses when reversion fails; "picking up nickels in front of a steamroller," and in crypto the steamroller is levered.
- Extremely sensitive to transaction costs and slippage — crypto spreads and alt slippage are wider than equities, and an edge that exists on paper often vanishes at taker cost.
- Implicitly short volatility and crowding-exposed; losses correlate with market stress exactly when liquidity is worst.
- Crypto trends harder than equities, so the reversion window is narrow and the regime gate is doing most of the work — get the regime wrong and the strategy inverts.

## Sources

- De Bondt, W. & Thaler, R. (1985). "Does the Stock Market Overreact?" *Journal of Finance*. (Behavioral overreaction — the mechanism crypto exhibits on leverage.)
- Lehmann, B. (1990). "Fads, Martingales, and Market Efficiency." *Quarterly Journal of Economics*. (Short-term reversal.)
- Jegadeesh, N. (1990). "Evidence of Predictable Behavior of Security Returns." *Journal of Finance*.
- Lo, A. & MacKinlay, A.C. (1990). "When Are Contrarian Profits Due to Stock Market Overreaction?" *Review of Financial Studies*.
- Chan, E. (2013). *Algorithmic Trading: Winning Strategies and Their Rationale* — ADF/Hurst/half-life testing methodology, directly applicable to crypto spreads.
- Crypto microstructure context: this wiki's [[liquidation-cascade-fade]] and [[funding-rate-arbitrage]] pages for the reflexive-flow mechanics that dominate crypto reversion.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1h&limit=1000` — OHLCV for z-score / SMA / σ computation
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — perp funding, the crowded-book filter
- `GET /api/v1/market-intelligence/liquidations` — liquidation spikes (do-not-catch-the-knife guard)
- `GET /api/v1/volatility/regime` — per-asset vol regime (compressed / expanding / vol_shock / mean_reverting)
- `GET /api/v1/quant/market` — HMM regime probabilities, the on/off gate

**Historical data:**
- `GET /api/v1/backtesting/klines` — full OHLCV archive for backtesting the reversion signal
- `GET /api/v1/backtesting/funding` — funding history for the crowded-book filter
- `GET /api/v1/quant/history` — point-in-time regime probabilities for a leak-free backtest

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=1h&limit=1000"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-data]].

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [liquidations](https://cryptodataapi.com/liquidations) · [short-term regimes](https://cryptodataapi.com/market-regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this strategy end-to-end:

- **Signal** — z-scores from `GET /api/v1/market-data/klines?interval=1h` per coin, with `GET /api/v1/derivatives/funding-rates` as the crowded-book filter and `GET /api/v1/market-intelligence/liquidations` as the do-not-catch-the-knife guard
- **Regime gate** — `GET /api/v1/quant/market` + `GET /api/v1/volatility/regime`: trade only outside `strong_trend_*`/`vol_shock` states — the Hurst/regime gate is doing most of this strategy's work
- **Catalyst filter** — `GET /api/v1/event/calendar` to exclude coins with an unlock, listing, or macro print inside the holding window (catalyst moves revert far less reliably)
- **Backtest** — `GET /api/v1/backtesting/klines` (Binance spot 1h/1d back to 2017-08) with `GET /api/v1/quant/history` point-in-time regime probabilities (Pro Plus) so the regime gate is applied leak-free; `GET /api/v1/backtesting/funding` (HL hourly since 2023-05) for the carry term
- **Tips** — batch per-coin sizing via `GET /api/v1/quant/coins/risk` instead of looping symbols; respect `insufficient_history` flags before computing 20-bar σ on new listings

## Related

- [[rsi-mean-reversion]]
- [[bollinger-band-reversion]]
- [[pairs-trading]]
- [[momentum]]
- [[statistical-arbitrage]]
- [[liquidation-cascade-fade]] — the sharpest, most reflexive reversion setup
- [[funding-rate-arbitrage]] — funding as a crowding signal
- [[bollinger-bands]]
- [[rsi]]
- [[contrarian-extremes]] — a reversion variant trading sentiment and positioning extremes
- [[trend-following]] — the opposite systematic family; natural diversifier
- [[market-regime]] — regime detection determines when reversion vs trend is favored
- [[regime-detection]] — the Hurst/vol filters that switch the strategy on and off
- [[volatility]] — reversion is implicitly short vol; vol regime drives drawdowns
- [[ornstein-uhlenbeck]] — the model behind half-life estimation
- [[cointegration]] — the basis for spread reversion in [[pairs-trading]]
- [[edge-taxonomy]]
- [[failure-modes]]
- [[when-to-retire-a-strategy]]
