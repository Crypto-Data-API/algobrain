---
title: "Triple-Barrier Labeling"
type: concept
created: 2026-07-14
updated: 2026-07-14
status: good
tags: [ai-trading, machine-learning, backtesting, volatility]
aliases: ["Triple-Barrier Method", "Triple Barrier Labeling", "Triple-Barrier", "TBM"]
domain: [machine-learning, ai-trading]
prerequisites: ["[[volatility]]", "[[average-true-range]]"]
difficulty: advanced
related: ["[[meta-labeling]]", "[[ml-crypto-price-prediction]]", "[[ml-trading-pipeline]]", "[[purged-kfold-cv]]", "[[feature-engineering-crypto]]", "[[liquidation]]", "[[volatility]]", "[[book-advances-in-financial-ml]]"]
---

# Triple-Barrier Labeling

**Triple-barrier labeling** is the labeling method from Marcos López de Prado's *Advances in Financial Machine Learning* (Chapter 3) for turning a price series into supervised-learning targets that respect *how a trade would actually play out*. Instead of asking "what is the return N bars from now?" (fixed-horizon labeling), it sets three barriers around each entry — an upper **profit-take** barrier, a lower **stop-loss** barrier, and a vertical **time** barrier — and labels the observation by *which barrier the price touches first* (Source: [[book-advances-in-financial-ml]]).

- Touches the **upper** barrier first → label **+1** (a winning long / the move went the trade's way)
- Touches the **lower** barrier first → label **−1** (a loss / adverse move)
- Touches neither before the **vertical** barrier expires → label **0** (or the sign of the return at expiry)

This makes the label **path-dependent**: it encodes the sequence of prices, not just the endpoints — exactly what a real position with a stop and a target experiences.

## Why Fixed-Horizon Labels Fail in Crypto

The naïve alternative labels each bar by its return over a fixed horizon (e.g. sign of the 24h-forward return). This has two fatal problems, both amplified in crypto:

1. **It ignores the path.** A position that rockets to +8% then closes the window at −1% is labeled a *loss*, even though any sane stop/target would have booked the +8%. Conversely, a trade that plunges −20% (liquidating the account) before recovering to close +2% is labeled a *win* — a label no leveraged trader could ever have realized.
2. **It uses a constant threshold across wildly different volatility.** A ±3% move is noise for a memecoin and a major event for BTC. Fixed-horizon labels blur high- and low-vol regimes together.

Crypto makes both failures acute: 24/7 trading, frequent double-digit intraday swings, deep wicks, and **[[liquidation|liquidation cascades]]** that touch a stop barrier in seconds during a [[long-liquidation-cascade|cascade]]. A close-to-close label is blind to the liquidation that would have ended the trade. Triple-barrier labeling captures it because the lower barrier is checked against the intrabar *path* (typically the bar's low/high), not just the close.

## Setting Barrier Widths From Volatility

Barriers scale with volatility so that "profit" and "loss" mean the same statistical thing across assets and regimes (Source: [[book-advances-in-financial-ml]], §3.3). Two common width estimators:

- **Realized / EWMA volatility.** De Prado's reference implementation estimates a daily volatility `σ` from an exponentially-weighted standard deviation of returns, then sets barriers at multiples of `σ`.
- **[[average-true-range|ATR]].** ATR(14) on the trading timeframe is a practical, wick-aware width for crypto because it incorporates gaps and full-range moves.

The barriers can be asymmetric via profit-take and stop-loss multipliers `[pt, sl]`:

```
upper_barrier = entry_price * (1 + pt * σ)     # profit-take
lower_barrier = entry_price * (1 - sl * σ)     # stop-loss
vertical_barrier = entry_time + horizon        # e.g. 24 bars
```

A symmetric `[pt, sl] = [1, 1]` gives a balanced 50/50-ish label mix; a trend-following bias might use `[2, 1]` (let winners run, cut losers fast). In crypto, practitioners often widen the stop relative to the target to avoid being wicked out by noise, or tighten it when leverage and liquidation risk are high.

## Worked Example: BTC on 1h Bars

Entry long on BTC at **$60,000**. Estimate volatility from recent 1h returns: `σ ≈ 1.2%` per bar, and use a 24-bar (one-day) horizon with `[pt, sl] = [2, 1.5]`:

```
upper_barrier    = 60000 * (1 + 2   * 0.012)  = 61,440   (+2.4%)
lower_barrier    = 60000 * (1 - 1.5 * 0.012)  = 58,920   (-1.8%)
vertical_barrier = entry + 24 hours
```

Then walk the next 24 bars:
- If any bar's **high ≥ 61,440** before a bar's **low ≤ 58,920** → label **+1**.
- If any bar's **low ≤ 58,920** first → label **−1**.
- If neither is touched within 24 bars → label **0** (or `sign(P_expiry − 60000)`).

Because the check uses each bar's high and low, a −1.8% wick during an hourly candle correctly triggers the stop label even if that candle closes green — the path-dependence crypto demands.

## Meta-Labeling Connection

Triple-barrier labels are the natural training target for [[meta-labeling]]. Run a primary side model, apply the triple-barrier method *on the side the primary chose*, and the +1/0 outcome (hit profit target vs. not) becomes the binary meta-label the secondary filter learns. The two techniques are designed to be used together (Source: [[book-advances-in-financial-ml]], §3.6).

## Sample Weights and Label Concurrency

Triple-barrier labels overlap: a label opened at bar `t` and one at `t+1` can both resolve over a shared future window, so they share return information and are **not independent**. This concurrency inflates any standard cross-validation score and biases bagged models. Two fixes from de Prado, both essential downstream:

- **Uniqueness/concurrency weights** — down-weight observations whose resolution windows overlap many others.
- **[[purged-kfold-cv|Purged, embargoed cross-validation]]** — drop training observations whose label windows overlap the test set, plus an embargo buffer.

Never validate triple-barrier-labeled data with a random-shuffle split; the overlap guarantees leakage. See [[purged-kfold-cv]].

## Pitfalls

- **Label imbalance.** Asymmetric barriers or a strong trend skew the +1/−1/0 mix; use class weights and inspect the distribution before training.
- **Vertical-barrier-only labels.** If the horizon is too short relative to barrier width, most observations expire as 0 and the model learns little. Widen the horizon or narrow the barriers.
- **Hindsight barrier tuning.** Choosing `[pt, sl]` and horizon to maximize backtest returns is a form of [[overfitting-detection|overfitting]]. Set widths from volatility a priori, not by grid-searching P&L.
- **Wick data quality.** Path-dependent labels rely on accurate high/low. Thin-liquidity venues print unreliable wicks; source OHLCV from deep venues (Binance, Hyperliquid) and cross-check.
- **Funding and fees.** For perps, the profit target should clear expected [[funding-rate|funding]] and fees over the holding window, or "wins" evaporate net of costs.

## Getting the Data (CryptoDataAPI)

Triple-barrier labeling needs high-resolution OHLCV (for the path) and volatility estimates (for the widths); liquidation data helps validate stop realism.

**Live / recent data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1h&limit=1000` — Binance spot OHLCV path
- `GET /api/v1/hyperliquid/candles?coin=BTC&interval=1h&limit=1000` — Hyperliquid perp OHLCV
- `GET /api/v1/volatility/regime` — per-asset volatility regime (compressed/expanding/vol_shock) to condition barrier widths

**Historical data (for building the label set):**
- `GET /api/v1/backtesting/klines` — full OHLCV archive (Parquet since 2020) for path resolution
- `GET /api/v1/backtesting/liquidations` — historical liquidations to sanity-check stop-barrier touches
- `GET /api/v1/market-data/btc-price-history?days=730` — long BTC series with 200D MA

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=1h&limit=1000"
```

Auth: `X-API-Key` header. Endpoint catalogs: [[cryptodataapi-market-data]], [[cryptodataapi-backtesting]].

## Related

- [[meta-labeling]] — consumes triple-barrier outcomes as its target
- [[ml-crypto-price-prediction]] — the pipeline stage this sits in
- [[ml-trading-pipeline]] — general ML trading workflow
- [[purged-kfold-cv]] — required validation for overlapping labels
- [[feature-engineering-crypto]] — features paired with these labels
- [[average-true-range]] — a practical barrier-width estimator
- [[liquidation]] — why path-dependence matters in crypto
- [[volatility]] — barrier widths scale with it

## Sources

- [[book-advances-in-financial-ml]] — López de Prado, M. (2018). *Advances in Financial Machine Learning*, John Wiley & Sons. Chapter 3 ("Labeling"), §3.2–3.6 (triple-barrier method, dynamic thresholds, meta-labeling).
