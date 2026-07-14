---
title: "Ornstein-Uhlenbeck Process"
type: strategy
created: 2026-04-06
updated: 2026-07-14
status: good
tags: [ornstein-uhlenbeck, mean-reversion, stochastic-process, half-life, statistical-arbitrage, quantitative, pairs-trading, crypto]
aliases: ["OU Process Trading", "Mean-Reverting Stochastic Process", "OU Model"]
strategy_type: quantitative
timeframe: swing
markets: [crypto]
complexity: advanced
backtest_status: untested
edge_source: [analytical, behavioral, risk-bearing]
edge_mechanism: "The OU process turns a mean-reverting crypto spread into three tradeable parameters (speed, mean, volatility); the edge is modeling the reversion correctly and being paid to provide liquidity against the flow that pushed the spread away from equilibrium."
data_required: [ohlcv-1h, ohlcv-daily, funding-rates, cointegration-window]
min_capital_usd: 5000
capacity_usd: 20000000
crowding_risk: high
expected_sharpe: 0.6
expected_max_drawdown: 0.20
breakeven_cost_bps: 30
decay_evidence: "OU is a modeling layer over [[pairs-trading]]/[[statistical-arbitrage]] and inherits their decay: crypto spreads have unstable parameters (theta, mu drift as BTC-dominance rotates), and the Gaussian OU assumption badly understates the fat-tailed jumps (unlocks, depegs, cascades) that break the very relationships it models."
kill_criteria: |
  - strategy-level drawdown > 20% from high-water mark
  - rolling 12-month net Sharpe < 0
  - realized half-life > 2x modeled half-life over a 40-trade sample
  - AR(1) coefficient b >= 1 on re-fit (spread no longer stationary) for tracked spreads
  - median realized round-trip cost > 30 bps for a full month
related: ["[[pairs-trading]]", "[[statistical-arbitrage]]", "[[kalman-filter-trading]]", "[[mean-reversion]]", "[[bollinger-band-reversion]]", "[[cointegration]]", "[[augmented-dickey-fuller]]", "[[book-algorithmic-trading-ernest-chan]]", "[[book-pairs-trading-vidyamurthy]]", "[[cryptodataapi]]"]
---

# Ornstein-Uhlenbeck Process

The Ornstein-Uhlenbeck (OU) process is a continuous-time stochastic model of mean-reverting dynamics — a price or spread pulled toward a long-run equilibrium with random fluctuations around it. It is the mathematical engine of [[statistical-arbitrage]] and [[pairs-trading]]: it turns a mean-reverting crypto spread into three tradeable parameters and, critically, a **half-life** that tells you how long a trade should take to play out. As a standalone "strategy" it is the disciplined, parameter-driven way to run spread reversion — replacing arbitrary z-score thresholds with entry/exit and holding-period expectations derived from the fitted process.

Named after Leonard Ornstein and George Uhlenbeck (1930, particle-velocity physics; Source: [[book-pairs-trading-vidyamurthy]]), the OU process has three parameters that directly drive trading decisions:

- **theta (mean-reversion speed):** how fast the spread reverts. Higher theta = faster reversion = shorter holds.
- **mu (long-run mean):** the equilibrium the spread is attracted to.
- **sigma (volatility):** the intensity of random fluctuation. Higher sigma = wider deviations = larger potential profit and loss.

The **half-life** — the time for a deviation to decay by half — is **t_half = ln(2) / theta** (Source: [[book-algorithmic-trading-ernest-chan]]). This is the single most important practical output: a 5-day half-life implies a trade closes in roughly 5–15 days; a 60-day half-life ties up capital far too long and gets eaten by perp funding carry.

## Edge source

Per [[edge-taxonomy]], OU-based reversion is primarily **analytical**, secondarily **behavioral / risk-bearing** — it inherits its edge from [[statistical-arbitrage]]:

- **Analytical** — the edge is fitting the reversion correctly: estimating theta/mu/sigma on a genuinely cointegrated crypto spread, sizing by the stationary distribution, and setting a time stop at a multiple of the fitted half-life. Most participants eyeball a z-score; the OU trader quantifies reversion speed and holding period.
- **Behavioral / risk-bearing** — the spread is displaced by the same crypto flow that drives all relative-value trades (listings, unlocks, single-coin liquidations); the OU trader supplies liquidity against it and is paid the reversion.

## Why this edge exists

The OU model is only tradeable because crypto spreads *are* pushed away from equilibrium by non-fundamental flow and *do* revert when that flow exhausts. Who is on the other side, and why do they pay? The momentum chaser buying the leg that pumped, the forced seller dumping the leg that unlocked, and the discretionary trader pricing each coin on its own story rather than relative to its statistical twin. The OU parameters simply formalize the reversion: theta measures how fast the flow-driven displacement decays, mu is the equilibrium the fundamentals enforce, and sigma is the noise the liquidity provider is paid to warehouse. The edge persists in attenuated form because the reversion is genuinely uncertain — in crypto, mu itself can jump when a relationship breaks structurally (an unlock permanently reprices a token, a depeg permanently kills a peg), which is exactly the tail the Gaussian OU model cannot see.

## Null hypothesis

If the spread is a random walk rather than an OU process, the AR(1) fit gives b ≥ 1 (no reversion), theta ≤ 0, and the "half-life" is undefined or enormous. Under the null, entries at the stationary ±2σ are followed by divergence as often as convergence and P&L equals the negative of fees plus funding carry. The null is directly testable: the AR(1) coefficient b should not be significantly below 1, the [[augmented-dickey-fuller]] test should fail to reject a unit root, and a fit on **shuffled** spread data should yield theta ≈ 0. A real edge requires a stable, significantly-mean-reverting fit (b < 1, ADF p < 0.05) whose half-life is short enough (days to a few weeks) to beat crypto's funding and cost drag — and that survives out-of-sample re-fitting.

## How it works

The OU process is described by the SDE:

**dX_t = theta · (mu − X_t) · dt + sigma · dW_t**

In discrete time it becomes an AR(1) regression:

**X_t = a + b · X_(t−1) + epsilon_t**

where **theta = −ln(b) / dt**, **mu = a / (1 − b)**, and **sigma** is derived from the residual standard deviation adjusted for theta. Estimation procedure:

1. Compute the spread between two cointegrated crypto assets (from the [[pairs-trading]] setup).
2. OLS-regress X_t on X_(t−1) to get a and b.
3. Verify b < 1 (mean-reverting; b ≥ 1 means non-stationary — do not trade).
4. Extract theta, mu, sigma; compute half-life = ln(2) / theta.
5. Validate with the [[augmented-dickey-fuller]] test.

The stationary distribution of the spread is Normal(mu, sigma² / (2·theta)), which defines the expected range and the z-score thresholds for entry and exit.

## Rules

### Pair / spread selection
1. For each cointegrated candidate spread, fit the OU parameters.
2. **Reject half-life > 20 days** (too slow — funding carry eats it) or **< ~4 hours** (too fast — microstructure noise, uncapturable after cost).
3. Ideal range: **1–15 days** for swing spreads; a few hours for intraday spreads on liquid majors.
4. Rank candidates by sigma / theta (higher = more profitable reversion amplitude per unit time).

### Entry
1. Stationary z-score: **z = (X_t − mu) / sqrt(sigma² / (2·theta))**.
2. **Long the spread** when z ≤ −1.5 to −2.0; **short the spread** when z ≥ +1.5 to +2.0.
3. Confirm neither leg has an imminent catalyst (unlock, listing, upgrade) that would shift mu — check the CDA event calendar (see [[#Getting the Data (CryptoDataAPI)]]).

### Exit
1. **Mean-reversion exit:** close when z returns to 0 (partial at ±0.5).
2. **Stop-loss:** close if |z| ≥ 3.5 (the model is breaking — a regime change or structural break is underway).
3. **Time stop:** if not reverted within **3–4 half-lives**, close and re-estimate (in crypto, re-fit weekly regardless).

### Position sizing
Size proportionally to |z| and inversely to sigma — larger deviations warrant larger positions (higher reversion probability), higher sigma warrants smaller (wider fluctuations). Risk ≤ 0.5–1% of equity per spread; keep gross leverage modest so a fat-tailed jump the Gaussian model didn't price cannot wipe the book.

## Implementation pseudocode

```python
# OU-parameterized crypto spread reversion
for spread in cointegrated_spreads:
    X = compute_spread(spread, lookback_days=90)          # P_A - beta * P_B
    a, b = ar1_regress(X)                                 # X_t = a + b*X_{t-1}
    if b >= 1:                                            # not mean-reverting
        retire(spread); continue
    theta     = -log(b) / dt                              # dt in days
    mu        = a / (1 - b)
    sigma     = resid_std(X) * sqrt(2*theta / (1 - b**2))
    half_life = log(2) / theta
    if not (1 <= half_life <= 20):                        # days
        retire(spread); continue

    stat_sd = sqrt(sigma**2 / (2*theta))
    z = (X[-1] - mu) / stat_sd

    if no_position(spread):
        if z <= -1.8: open(long_spread,  risk=0.005*equity)   # long A, short beta*B
        if z >= +1.8: open(short_spread, risk=0.005*equity)   # short A, long beta*B
    else:
        if abs(z) <= 0.3:                       close(spread)  # reverted
        elif abs(z) >= 3.5:                     close(spread)  # model breaking
        elif days_held(spread) > 3*half_life:   close(spread)  # time stop
```

Pair the OU fit with a [[kalman-filter-trading|Kalman filter]] to let theta/mu/sigma (and the hedge ratio) evolve in real time rather than re-fitting on a fixed window — important in crypto, where the parameters drift as BTC-dominance rotates.

## Indicators / data used

- **OU parameters** (theta, mu, sigma) and **half-life** from the AR(1) fit on the spread.
- **Stationary z-score** — the entry/exit signal, scaled by the model's own stationary standard deviation.
- **[[cointegration]] tests** (Engle-Granger, Johansen) and **[[augmented-dickey-fuller]]** — to qualify the spread before fitting OU.
- **[[kalman-filter-trading|Kalman filter]]** — to track drifting OU/hedge-ratio parameters online.
- **Perp [[funding-rate]]** on the short leg — the carry that determines whether a longer half-life is still worth trading.
- Clean 1h/1d OHLCV for both legs plus a catalyst calendar (unlocks/listings shift mu).

## Example trade

**Setup:** BTC/ETH spread, 4-hour bars, OU fit.
1. Spread = log(BTC) − 15.2·log(ETH) over 90 days of 4h data.
2. AR(1) yields b = 0.987, a = 0.013 → theta = −ln(0.987)/1 = 0.0131 per bar. Half-life = ln(2)/0.0131 = **53 bars ≈ 8.8 days**.
3. Long-run mean mu = 0.013 / (1 − 0.987) = 1.0; stationary std = 0.42.
4. Current spread = 0.12 → z = (0.12 − 1.0)/0.42 = **−2.1**. ETH is cheap relative to BTC.
5. **Enter:** long ETH-perp, short BTC-perp at the dynamic hedge ratio, sized for ~1% portfolio risk. Combined entry cost ~10 bps taker.
6. Over 7 days (≈40 bars ≈ 0.8 half-lives) the spread reverts to 0.85 (z = −0.36). **Exit** near equilibrium.
7. Gross P&L ≈ +$1,200 on a $50k spread (~+2.4%); ~+$1,150 net after four-fill fees and a small adverse BTC-short funding carry. Holding time tracked the OU-predicted half-life.

## Performance characteristics

OU-based reversion inherits the [[statistical-arbitrage]] profile: net Sharpe ~0.4–0.8 for a diversified crypto book (frontmatter assumes 0.6), many small wins with a negatively skewed tail. The OU discipline improves the *distribution* of a stat-arb book — a time stop at 3–4 half-lives cuts the "carry bleed" trades that a naive z-score system holds forever — but it does not create edge where the spread is not genuinely cointegrated.

**Cost overlay (crypto spread, per completed round trip = 4 fills):**

| Component | Magnitude | Note |
|---|---|---|
| Taker fees, both legs, entry + exit | ~16–22 bps | Four fills per completed trade |
| Slippage | ~4–20 bps | Wider on loose alt legs |
| Funding carry over the hold | ±(half-life × 1–4 bps/day) | The longer the half-life, the more this matters |
| Gross edge per converged trade | ~80–200 bps | Costs consume 20–40% |
| **Breakeven (frontmatter)** | **~30 bps** | Rejecting long-half-life spreads is a cost-control decision |

The half-life filter *is* a cost-control tool: a 40-day-half-life spread at 3 bps/day adverse funding bleeds ~120 bps before it reverts — more than the entire gross edge. This is why crypto OU trades cap half-life tightly.

## Capacity limits

Bounded by the thinner leg of each spread, exactly as in [[pairs-trading]]: liquid major spreads (ETH/BTC) absorb the most (low tens of millions) before entries move the spread; loose sector/alt spreads absorb far less. Frontmatter assumes **$20M** blended. Crowding is **high** — OU-parameterized reversion is the textbook quant approach, so the well-fit majors are traded by everyone and the edge is shared.

## What kills this strategy

- **Parameter drift (regime change).** theta, mu, and sigma are assumed constant but are not — in crypto they drift as BTC-dominance rotates, turning a fast-reverting spread into a slow bleed. The realized half-life exceeding the modeled one is the fingerprint.
- **Structural mu shift.** An unlock, delisting, migration, or depeg permanently moves the equilibrium; the OU model keeps generating "buy the cheap spread" signals into a spread that never comes back.
- **Fat-tailed jumps.** The Gaussian OU assumption badly understates crypto tail risk; a real move can be 5–10× the model's stationary σ (LUNA, stETH depeg, 2025-10-10). The z ≥ 3.5 stop is the crude defense.
- **Over-fit windows.** Too short a window gives unstable parameters; too long includes stale regimes. Half-life point estimates have wide confidence intervals (a "10-day" estimate can have a 95% CI of 5–25 days).
- **Cost creep.** Adverse funding on the short leg plus taker slippage pushing net edge below the ~30 bps breakeven.

## Kill criteria

- Strategy-level drawdown > 20% from high-water mark.
- Rolling 12-month net Sharpe < 0.
- Realized half-life > 2× modeled over a 40-trade sample (reversion regime changed).
- AR(1) coefficient b ≥ 1 on re-fit for tracked spreads (no longer stationary) → retire those spreads.
- Median realized round-trip cost > 30 bps for a full month.

See [[when-to-retire-a-strategy]].

## Advantages

- Provides **quantitative** estimates of reversion speed, equilibrium, and volatility — far more actionable than a bare stationarity test.
- The **half-life** directly sets holding-period expectations, the time stop, and (via funding carry) a hard cost filter.
- Mathematically rigorous: the continuous-time analog of AR(1), with well-understood properties.
- Enables **distribution-aware** entry/exit sizing rather than arbitrary z thresholds.
- Pairs naturally with [[kalman-filter-trading]] to track evolving parameters online.

## Disadvantages

- Assumes **constant parameters** — false in crypto; requires frequent re-estimation.
- The **Gaussian assumption** understates tail risk; real crypto spread moves blow well past the model's σ.
- Estimation is data-hungry and window-sensitive; half-life confidence intervals are wide.
- Says nothing about **why** a spread reverts — a structural mu shift (unlock, depeg) produces confident, losing signals.
- Only models **linear** reversion; threshold/asymmetric dynamics need richer models (Source: [[book-pairs-trading-vidyamurthy]]).

## Sources

- [[book-algorithmic-trading-ernest-chan]] — the primary practical reference for the OU process in trading: half-life estimation, Hurst analysis, and the cointegration/reversion-speed link, directly applicable to crypto spreads.
- [[book-pairs-trading-vidyamurthy]] — Vidyamurthy (2004): theoretical foundation for OU/spread modeling in pairs trading.
- Avellaneda, M. & Lee, J.-H. (2010). "Statistical Arbitrage in the US Equities Market." *Quantitative Finance* — OU-style residual reversion at portfolio scale (generalizes to crypto factor residuals).

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=4h&limit=1000` — OHLCV for spread construction and AR(1) fitting
- `GET /api/v1/hyperliquid/candles?coin=ETH&interval=4h&limit=1000` — alt-perp OHLCV for the second leg
- `GET /api/v1/derivatives/funding-rates?coin=ETH` — short-leg funding carry (the half-life cost filter)

**Historical data:**
- `GET /api/v1/backtesting/klines` — full OHLCV archive for OU fitting and half-life backtests
- `GET /api/v1/backtesting/funding` — funding history for the carry overlay
- `GET /api/v1/backtesting/symbols` — symbols with backtest-grade history

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=4h&limit=1000"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-data]].

## Related

- [[pairs-trading]] — the primary strategy built on OU-modeled spreads
- [[statistical-arbitrage]] — the broader framework where OU is the mean-reversion backbone
- [[kalman-filter-trading]] — dynamic estimation of OU parameters as they evolve
- [[mean-reversion]] — the market behavior the OU process formalizes
- [[cointegration]] — the property a spread must have before OU applies
- [[augmented-dickey-fuller]] — the stationarity test that qualifies a spread
- [[bollinger-band-reversion]] — a simplified, indicator-based approach to the same concept
- [[funding-rate-arbitrage]] — the carry mechanics that make half-life a cost filter
- [[edge-taxonomy]]
- [[failure-modes]]
- [[when-to-retire-a-strategy]]
