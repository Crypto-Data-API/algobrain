---
title: "Half-Life of Mean Reversion"
type: concept
created: 2026-07-20
updated: 2026-07-20
status: draft
tags: [quantitative, mean-reversion, statistics, backtesting, crypto, risk-management]
aliases: ["Half-Life", "Mean Reversion Half-Life", "OU Half-Life", "Reversion Speed", "Lambda Half-Life"]
related: ["[[ornstein-uhlenbeck]]", "[[hurst-exponent]]", "[[stationarity]]", "[[augmented-dickey-fuller]]", "[[mean-reversion]]", "[[stretch-revert]]", "[[time-stop]]", "[[z-score]]", "[[pairs-trading]]", "[[statistical-arbitrage]]", "[[cointegration]]", "[[autocorrelation]]", "[[random-walk]]", "[[crypto-short-history-statistical-power]]", "[[overfitting]]", "[[standard-deviation]]", "[[bollinger-bands]]", "[[position-sizing]]", "[[stop-loss]]", "[[funding-aware-position-sizing]]", "[[regime-detection]]", "[[least-squares-moving-average]]", "[[theil-sen-regression]]", "[[cryptodataapi-hyperliquid]]", "[[cryptodataapi-mcp]]"]
domain: [quantitative]
prerequisites: ["[[mean-reversion]]", "[[stationarity]]", "[[autocorrelation]]"]
difficulty: advanced
---

# Half-Life of Mean Reversion

The half-life of mean reversion is the expected time for a series to close **half** the gap between its current value and its long-run mean. It converts an abstract statement — "this series reverts" — into a number with units of bars or days, and that number is directly operational: it is how long a reversion trade should reasonably be given to work, and therefore how a [[time-stop]] gets sized.

Where the [[hurst-exponent]] answers *whether* a series reverts, the half-life answers *how fast*. The two are complementary and neither substitutes for the other: an H of 0.35 with a half-life of 400 bars describes a series that reverts reliably and far too slowly to trade against funding costs.

## The Ornstein-Uhlenbeck framing

The half-life is defined within a model, and that model is the **Ornstein-Uhlenbeck process** (see [[ornstein-uhlenbeck]]) — the canonical continuous-time mean-reverting process:

$$dy_t = \lambda\,(\mu - y_t)\,dt + \sigma\,dW_t$$

- **μ** — the long-run mean the process is pulled toward
- **λ** — the **speed of mean reversion**; larger λ means a stronger pull
- **σ dW** — the random shock term that keeps knocking it away

The deterministic part says the expected change is proportional to the distance from μ. Solving for the expected path from a displacement gives exponential decay toward μ with rate λ, and the time to close half the gap is the standard exponential half-life:

$$t_{1/2} = \frac{\ln 2}{\lambda} \approx \frac{0.693}{\lambda}$$

In the discrete regression form below, the fitted coefficient is negative, so the expression is conventionally written:

$$t_{1/2} = -\frac{\ln 2}{\lambda}, \qquad \lambda < 0$$

Both are the same statement — the sign convention depends on whether λ is defined as the pull coefficient or as the regression slope. **Getting this sign wrong produces a negative half-life**, which is the most common implementation error and, usefully, an obvious one: a negative or infinite half-life is the estimator telling you the series is not reverting, not that the arithmetic slipped.

## Estimation

The practical estimator is a single OLS regression of the change on the lagged level:

$$\Delta y_t = \lambda\,y_{t-1} + c + \varepsilon_t$$

This is precisely the [[augmented-dickey-fuller|Dickey-Fuller]] regression without the augmenting lag terms, which is why the ADF test and the half-life come out of the same fit. Take the slope coefficient and convert:

```python
import numpy as np

def half_life(y):
    """Half-life of mean reversion in bars, via the OU discretisation.

    y : level series (a spread, a residual, or price minus baseline)
        NOT returns — the regression is of the change on the LEVEL.
    """
    y = np.asarray(y, dtype=float)
    dy = np.diff(y)                       # Δy_t
    lag = y[:-1]                          # y_{t-1}

    X = np.column_stack([lag, np.ones(len(lag))])
    lam, _c = np.linalg.lstsq(X, dy, rcond=None)[0]

    if lam >= 0:
        return np.inf                     # no reversion detected; do not trade it
    return -np.log(2) / lam               # bars
```

Three implementation notes that matter more than they look:

- **Regress the change on the level, not on returns.** A regression of returns on lagged returns is an [[autocorrelation]] test, a different quantity. The OU estimator needs the level.
- **The units are the bar interval.** A half-life of 6 on 15m bars is 90 minutes. Reporting "half-life 6" without the interval is meaningless, and mixing intervals between a backtest and a live implementation is a real reproducibility hazard.
- **Apply it to a stationary object.** Raw crypto prices are not mean-reverting in level, so a half-life computed on BTC's price is measuring nothing. Apply it to a spread, a cointegrating residual, or — as in [[stretch-revert]] — price minus an adaptive baseline, which is the residual the [[z-score]] is built on.

## Interpretation

The half-life is an **expected** time under the fitted model, not a guarantee or a deadline. Interpretive anchors:

| Half-life | Reading | Trading implication |
|---|---|---|
| Very short (1–3 bars) | Reversion is nearly instantaneous | Likely [[bid-ask-spread\|bid-ask bounce]] or microstructure noise, not tradable displacement — the "edge" is the spread |
| Short (4–20 bars) | Fast, tradable reversion | The [[stretch-revert]] target zone; short exposure, low funding drag |
| Medium (20–100 bars) | Slow reversion | Tradable but costs compound; funding and opportunity cost start dominating |
| Long (> 100 bars) | Weak pull | Statistically real, economically marginal — the trade will not clear its costs |
| Infinite / negative λ | No reversion | The series has a unit root; it is a [[random-walk]] and there is nothing to fade |

The decay is exponential, so the full-gap timeline follows directly: two half-lives close ~75% of the gap, three close ~87.5%, four close ~94%. A position targeting full reversion to the baseline is implicitly a **3–4 half-life trade**, not a one-half-life trade — a distinction that changes the exposure budget by a factor of three or four and is routinely overlooked when translating half-life into a holding period.

## The operational use: sizing a time stop

This is the reason the half-life earns a page rather than a footnote.

> A position whose half-life is 6 bars has no business being held 60.

A [[time-stop]] caps how long a trade is given to work. Without a principled input it is set by feel — "give it an hour" — which is a free parameter fitted to whatever the backtest liked. The half-life supplies the input:

- **A reasonable time stop is a small multiple of the half-life**, typically 2–4×, depending on whether the exit target is a partial or full reversion to the mean.
- **Below ~1×** the stop fires before the modelled reversion has had time to occur; the strategy systematically scratches trades that were working. This looks in the results like a low win rate and is misdiagnosed as a bad signal.
- **Beyond ~4×** the stop stops binding. If reversion has not occurred in four half-lives the model has been rejected by the data, and holding longer is holding a position whose thesis has already failed — while paying funding for the privilege ([[funding-aware-position-sizing]]).

The half-life also disciplines the entry, not just the exit. A signal firing on a series with a 200-bar half-life on a strategy that holds for 12 bars is structurally mismatched: the model says the reversion will not have happened yet when the position closes. That mismatch is invisible in a backtest that only reports P/L, and it is a common reason a "working" reversion strategy turns out to be capturing something other than reversion.

Beyond stops, the half-life feeds:

- **Turnover and cost budgeting** — expected trades per period follows from the reversion timescale, and multiplying by round-trip cost gives the cost hurdle the edge must clear.
- **[[position-sizing]]** — a longer half-life means longer exposure to the shock term, so more variance accumulates before the target; risk per trade should scale accordingly.
- **Timeframe selection** — the half-life measured at 15m and at 1h will differ, and the frequency where reversion is fastest relative to costs is the one to trade.

## Relationship to Hurst and stationarity

Three tests, one underlying property, three different failure modes — which is exactly why practitioners run all of them.

| Test | Question | Output |
|---|---|---|
| [[hurst-exponent]] | Does it revert? | H < 0.5 → anti-persistent |
| [[augmented-dickey-fuller\|ADF]] | Is there a unit root? | Rejecting the null → [[stationarity\|stationary]] |
| **Half-life** | How fast does it revert? | A number of bars |

A low H, a rejected ADF null, and a short half-life are three independent ways of saying "this series reverts". The vault's [[hurst-exponent]] page works a case where all three agree: H ≈ 0.39, ADF statistic −3.6, and an OU half-life of ~8 days, which then sets the holding horizon and stop.

They fail differently, which is the point of running all three. ADF has low power in short samples — it frequently fails to reject a unit root on a series that genuinely reverts. Hurst is sensitive to estimator settings, window, and lag range; the same series can look trending or reverting under different configurations. The half-life is a **point estimate with no confidence interval attached by default**, and it inherits the fragility of both. Agreement across three imperfect tests is worth much more than any one of them.

Mathematically, half-life and Hurst are related but not interchangeable. H is a scaling exponent describing long-range dependence across all timescales; the half-life is a single timescale parameter of a specific model. A series can be anti-persistent (H < 0.5) at short horizons and persistent at long ones, and a single half-life cannot represent that.

## Instability of the estimate

The half-life is a **quotient**, and quotients of noisy estimates are badly behaved.

`t½ = −ln(2)/λ` blows up as λ approaches zero. Near the boundary between "reverting" and "random walk" — which is where most tradable financial series actually sit — a small change in the estimated λ produces an enormous change in the half-life. An λ of −0.010 gives 69 bars; −0.005 gives 139 bars; −0.001 gives 693 bars. Those three λ values are statistically indistinguishable on a few hundred bars, and they imply wildly different holding periods.

Specific instabilities to expect:

- **Wide confidence intervals on short samples.** A half-life estimated on 200 bars can carry an interval spanning an order of magnitude. Bootstrap it before trusting it; the interval is usually more informative than the point estimate.
- **Regime dependence.** λ is not a constant of nature. A series with a 10-bar half-life in a range regime may have no reversion at all in a trend. Estimating over a window that spans a regime change averages incompatible dynamics into a number describing neither ([[regime-detection]]).
- **Sensitivity to window length.** Rolling half-life estimates are visibly noisy. The temptation to pick the window that produces the most convenient number is direct [[overfitting]].
- **Crypto's short history.** Even where the data is high-frequency, the number of *independent regime episodes* is small. High-frequency data gives many observations of few regimes, which inflates apparent statistical power without providing it — see [[crypto-short-history-statistical-power]].
- **Outliers.** The OLS fit has a 0% breakdown point, so a single bad print moves λ. The same robustness argument that motivates [[theil-sen-regression]] applies here.

**Practical stance:** treat the half-life as an order-of-magnitude input, not a precision parameter. "This reverts in roughly ten bars, not a hundred" is a defensible statement that supports a time-stop decision. "The half-life is 11.4 bars, so the time stop is 34.2 bars" is false precision, and any strategy whose profitability depends on that third significant figure is fitted to noise.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/candles?coin=X&interval=15m&limit=500` — the closes the level series is built from; the half-life must be computed on a stationary object (spread or price-minus-baseline), never on raw price
- `GET /api/v1/derivatives/funding-rates?coin=X` — the cost side of the trade-off; a half-life is only tradable if the expected reversion outruns accumulated funding over the holding window
- `GET /api/v1/volatility/regime/{symbol}` — λ is regime-dependent, so a half-life is only interpretable alongside the volatility state it was estimated in

**Historical data:**
- `GET /api/v1/backtesting/klines` — long kline history for estimating the half-life over multiple regime episodes rather than one, and for bootstrapping a confidence interval
- `GET /api/v1/quant/regimes/history` — hourly HMM regime labels since 2020, so λ can be estimated separately per labelled regime instead of averaged across incompatible ones

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/candles?coin=ETH&interval=15m&limit=500"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-hyperliquid]].

**Live dashboards:** [market regimes](https://cryptodataapi.com/market-regimes) · [funding rates](https://cryptodataapi.com/funding-rates)

### AI agent workflow

An agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can turn a half-life estimate into a stop parameter without over-trusting it:

- **Estimate on the residual, not on price.** Compute the baseline first, then run the Δy-on-lagged-y regression on `price − baseline`. An agent that regresses raw BTC closes will return a large or infinite half-life and it will mean nothing.
- **Always return a bootstrap interval, never a point estimate.** Resample the window from `GET /api/v1/backtesting/klines` and report the range. If the interval spans an order of magnitude — which near λ ≈ 0 it usually does — say so, because that is the finding.
- **Estimate per regime.** Join against `GET /api/v1/quant/regimes/history` and fit λ separately inside range- and trend-labelled states. A single blended half-life describes neither and is the number most likely to be wrong when it matters.
- **Convert to a time stop explicitly, in bars and in wall-clock time.** Report "half-life ≈ 6 bars on 15m = 90 minutes, suggested [[time-stop]] 12–24 bars", so the interval and the exposure budget are stated in the same units the execution layer uses.
- **Cross-check the funding cost over that window.** Multiply the suggested holding period by the rate from `GET /api/v1/derivatives/funding-rates?coin=X`. If the expected reversion does not clear accumulated funding, the half-life is statistically real and economically untradable — a distinction worth reporting before, not after, deployment.

## Related

- [[ornstein-uhlenbeck]] — the process the half-life is a parameter of
- [[hurst-exponent]] — *whether* a series reverts, to this page's *how fast*
- [[augmented-dickey-fuller]] — same regression, different question; low power on short samples
- [[stationarity]] — the property the half-life presumes
- [[time-stop]] — the direct operational consumer of this estimate
- [[stretch-revert]] — the strategy family whose time stops this parameterises
- [[z-score]] — the residual the half-life should be estimated on
- [[mean-reversion]] — the trade
- [[pairs-trading]] · [[statistical-arbitrage]] · [[cointegration]] — where half-life screening is standard practice
- [[autocorrelation]] · [[random-walk]] — the null the estimator tests against
- [[least-squares-moving-average]] · [[theil-sen-regression]] — the OLS fragility and the robust alternative
- [[funding-aware-position-sizing]] — the cost that converts a long half-life into an untradable one
- [[position-sizing]] · [[stop-loss]] — the other risk parameters the horizon feeds
- [[regime-detection]] — λ is regime-dependent, not constant
- [[crypto-short-history-statistical-power]] · [[overfitting]] — why the point estimate should not be trusted to three figures

## Sources

- Uhlenbeck, G. E. and Ornstein, L. S. (1930). "On the Theory of the Brownian Motion," *Physical Review* 36 — the original process.
- Chan, Ernest P. (2013). *Algorithmic Trading: Winning Strategies and Their Rationale* — the standard practitioner treatment of the Δy-on-lagged-y half-life estimator, its link to the ADF regression, and its use in setting holding periods for mean-reverting spreads.
- Dickey, D. A. and Fuller, W. A. (1979). "Distribution of the Estimators for Autoregressive Time Series with a Unit Root," *Journal of the American Statistical Association* 74 — the regression the half-life estimator shares.
- The worked case (H ≈ 0.39, ADF −3.6, ~8-day half-life) is drawn from the vault's [[hurst-exponent]] page, which this page resolves a forward link from.
- The time-stop application follows the risk design recorded on [[stretch-revert]] (2026-07-20). No source-summary page exists for that family's live data.
- No vault source-summary page covers the half-life specifically; the analysis is derived from the method and from existing vault pages ([[hurst-exponent]], [[stationarity]], [[augmented-dickey-fuller]], [[crypto-short-history-statistical-power]]).
