---
title: "Fractional Differentiation"
type: concept
created: 2026-07-14
updated: 2026-07-14
status: good
tags: [ai-trading, machine-learning, quantitative, mean-reversion]
aliases: ["Fractional Differentiation", "Fractional Differencing", "Frac-Diff", "Fixed-Width Window Frac-Diff", "FFD"]
domain: [machine-learning, quantitative]
prerequisites: ["[[stationarity]]", "[[augmented-dickey-fuller]]"]
difficulty: advanced
related: ["[[stationarity]]", "[[augmented-dickey-fuller]]", "[[feature-engineering-crypto]]", "[[feature-engineering-finance]]", "[[ml-crypto-price-prediction]]", "[[autocorrelation]]", "[[book-advances-in-financial-ml]]"]
---

# Fractional Differentiation

**Fractional differentiation** is the technique from Marcos López de Prado's *Advances in Financial Machine Learning* (Chapter 5) for making a time series **stationary while preserving as much memory as possible**. It resolves the central dilemma of feature engineering for ML: models need [[stationarity|stationary]] inputs, but the usual way to get them — taking integer differences (returns) — throws away nearly all the *level* information (memory) that carries predictive signal. Fractional differentiation applies a *real-valued* differencing order `d ∈ [0, 1]` instead of the integer `d = 1`, finding the **minimum** differencing needed to pass a stationarity test while retaining maximal memory (Source: [[book-advances-in-financial-ml]]).

## The Stationarity–Memory Trade-off

Raw crypto prices are non-stationary: they wander with drift and unbounded variance (a unit root — see [[augmented-dickey-fuller]]). Feeding raw prices to a model breaks the stationarity assumption and produces spurious fits. The standard fix is `d = 1` differencing — log returns — which is stationary but **memoryless**: a return series is almost uncorrelated with the original price level (correlation near zero), so all long-run structure (where price sits relative to history) is erased.

The two endpoints of integer differencing are both bad for ML features:

| Order `d` | Series | Stationary? | Memory retained |
|---|---|---|---|
| `d = 0` | raw price | No (unit root) | 100% |
| `d = 1` | returns | Yes | ~0% |

Fractional differentiation fills the continuum between them — enough differencing to cross the stationarity threshold, and *no more* — keeping the series predictive.

## How It Works: The Binomial Weight Expansion

Differencing is the operator `(1 − B)^d`, where `B` is the backshift operator (`B·x_t = x_{t-1}`). For a non-integer `d`, expand it as a binomial series, producing an infinite sequence of weights applied to lagged values:

```
X̃_t = Σ_{k=0}^{∞} w_k · X_{t-k}

w_0 = 1
w_k = -w_{k-1} · (d - k + 1) / k
```

For `d = 1` the weights collapse to `w_0 = 1, w_1 = -1`, all others 0 — ordinary first differencing. For fractional `d`, the weights decay slowly and never vanish, which is precisely why memory is preserved: distant lags still contribute, unlike returns which use only the single previous value.

### Fixed-Width Window (FFD)

The infinite weight series is impractical and its window grows over time, causing non-stationary variance. De Prado's **fixed-width window fractional differentiation (FFD)** truncates the weights once they fall below a threshold `τ` (e.g. `1e-5`), giving a constant-width, driftless filter applied identically at every point. FFD is the production-ready form and the one implemented in `mlfinlab` and similar libraries (Source: [[book-advances-in-financial-ml]], §5.5).

## Choosing `d` by the ADF Test

The recipe: sweep `d` upward from 0 and pick the **smallest** `d` at which the series becomes stationary (Source: [[book-advances-in-financial-ml]], §5.6):

1. For `d` in `{0.0, 0.1, 0.2, …, 1.0}` (refine near the crossing), compute the FFD series.
2. Run the [[augmented-dickey-fuller|ADF test]] on each.
3. Find the minimum `d` whose ADF statistic falls below the 5% critical value (rejects the unit-root null).
4. Also record the correlation between the FFD series and the original — this quantifies retained memory.

Empirically, most financial price series cross into stationarity at a **low `d`, often ≈ 0.3–0.5**, well below 1. In de Prado's E-mini S&P study the series became stationary around `d ≈ 0.35` while retaining correlation above **0.99** with the original level — near-total memory at full stationarity (Source: [[book-advances-in-financial-ml]], Ch. 5). The exact value is series-specific; it must be estimated, not assumed.

## Applying It to Crypto Series

Fractional differentiation is valuable anywhere a persistent (long-memory) crypto series must become an ML feature without losing its level information:

- **Log price.** Frac-diff of BTC/ETH log price yields a stationary feature that still "knows" whether price is historically high or low — useful for models blending trend and mean-reversion.
- **On-chain series.** [[whale-score|Whale accumulation scores]], MVRV/dormancy, exchange **netflows**, and stablecoin reserves are highly persistent and trend for weeks. Differencing them to returns destroys the slow-moving accumulation signal that is the whole point; frac-diff keeps it while satisfying model assumptions.
- **Derivatives levels.** [[open-interest|Open-interest]] and [[funding-rate|funding]] *levels* (not just changes) carry regime information; a low-`d` transform stabilizes them for modeling.

### Worked Example: BTC Log Price

Take daily BTC log price over several years. Sweep `d`:

```
d = 0.0  → ADF stat  -0.6   (fail to reject — non-stationary),  corr = 1.00
d = 0.3  → ADF stat  -2.4   (fail to reject at 5%),             corr ≈ 0.997
d = 0.4  → ADF stat  -3.1   (reject at 5%)  ← minimum d,        corr ≈ 0.99
d = 1.0  → ADF stat  -30+   (strongly stationary),             corr ≈ 0.03
```

Here `d ≈ 0.4` is the first order to pass the ADF test, and it preserves ~0.99 correlation with the level — versus returns (`d = 1`) at ~0.03. The frac-diff feature is both admissible for the model *and* far more informative than returns. (Illustrative numbers; recompute on your own sample and window.)

## Pitfalls

- **Apply to already-stationary series and you gain nothing** — funding-rate *changes* or returns are already `d ≈ 1` candidates; frac-diff is for persistent *levels*.
- **The FFD threshold `τ` sets the window length.** Too aggressive a truncation drops memory; too loose lengthens the filter. Tune it alongside `d`.
- **Structural breaks still bite.** Frac-diff makes a series stationary in a statistical-test sense; a genuine regime break (a new crypto cycle, a market-structure shift) can still invalidate it. Re-estimate `d` on rolling windows.
- **Look-ahead in `d` selection.** Choosing `d` on the full sample leaks future information; select it in-sample within each [[purged-kfold-cv|CV]] fold or on a training prefix, walk-forward.
- **Multiple testing.** Sweeping `d` and windows across many series inflates the odds of a spurious "just stationary" pass; confirm with KPSS and out-of-sample.

## Getting the Data (CryptoDataAPI)

Fractional differentiation is applied to raw price and persistent on-chain/derivatives *level* series pulled from these endpoints.

**Price series:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=1000` — daily OHLCV to build a log-price series
- `GET /api/v1/market-data/btc-price-history?days=730` — long BTC history with 200D MA
- `GET /api/v1/backtesting/klines` — full OHLCV archive (Parquet since 2020) for long, stable estimation of `d`

**Persistent on-chain / derivatives level series:**
- `GET /api/v1/on-chain/whale-score/BTC` — whale accumulation score timeseries (long-memory)
- `GET /api/v1/on-chain/exchange-flows/BTC` — CEX inflow/outflow (netflow levels)
- `GET /api/v1/on-chain/dormancy/btc` — MVRV + supply-shock, zone classification
- `GET /api/v1/backtesting/funding` — funding-level archive

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=1000"
```

Auth: `X-API-Key` header. Endpoint catalogs: [[cryptodataapi-market-data]], [[cryptodataapi-on-chain]], [[cryptodataapi-backtesting]].

## Related

- [[stationarity]] — the property frac-diff achieves at minimum cost to memory
- [[augmented-dickey-fuller]] — the test that selects `d`
- [[feature-engineering-crypto]] — where frac-diff features are built
- [[feature-engineering-finance]] — general feature-engineering context
- [[ml-crypto-price-prediction]] — pipeline that consumes these features
- [[autocorrelation]] — the memory structure frac-diff preserves

## Sources

- [[book-advances-in-financial-ml]] — López de Prado, M. (2018). *Advances in Financial Machine Learning*, John Wiley & Sons. Chapter 5 ("Fractionally Differentiated Features"), §5.4–5.6 (binomial weights, fixed-width window, choosing d by ADF).
