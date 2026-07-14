---
title: "Information Coefficient"
type: concept
created: 2026-07-14
updated: 2026-07-14
status: good
tags: [portfolio-theory, quantitative, machine-learning, crypto]
aliases: ["IC", "Information Coefficient", "Rank IC", "Rank-IC"]
domain: [portfolio-theory, quantitative]
prerequisites: ["[[alpha-model]]", "[[correlation]]"]
difficulty: advanced
related: ["[[alpha-model]]", "[[information-ratio]]", "[[alpha-decay]]", "[[signal-orthogonalization]]", "[[feature-engineering-crypto]]", "[[feature-selection-trading]]", "[[crypto-signal-library]]", "[[sharpe-ratio]]", "[[multi-factor-portfolio]]"]
---

The **Information Coefficient (IC)** is the correlation between a forecast (a signal, factor score, or model output) and the realized forward return it was meant to predict. It is the single most useful number for triaging a raw crypto feature *before* you build a strategy around it: it says, in one figure, whether the signal has any predictive skill at all. An IC of 0 is no skill; small positive ICs, applied across many independent bets, compound into real risk-adjusted return via the [[alpha-model|Fundamental Law of Active Management]].

## Definition

For each period `t`, you have a cross-section of signal scores `s_i,t` (across assets `i`) and the subsequently realized returns `r_i,t+h` over horizon `h`. The IC at `t` is the correlation across the cross-section:

- **Pearson IC** — `corr(s_i,t, r_i,t+h)` using raw values. Sensitive to outliers, which crypto has in abundance (a single memecoin +400% day distorts it).
- **Rank IC (Spearman)** — `corr(rank(s_i,t), rank(r_i,t+h))`. Uses ranks, so it is robust to fat tails and only rewards getting the *ordering* right. **Rank-IC is the default in crypto** because of the extreme return distribution.

The **IC time series** is the sequence of per-period ICs. Its **mean** is the signal's average skill; its **standard deviation** measures how consistent that skill is. The ratio of the two is the **Information Ratio of the signal** (the "IC-IR"): `mean(IC) / std(IC)` — closely related to the portfolio [[information-ratio]].

### Typical magnitudes
- **IC ≈ 0**: no skill; a coin-flip forecast.
- **IC 0.02-0.05**: a normal, durable single factor. This is *good*, not weak — the Law of Active Management turns it into Sharpe via breadth.
- **IC 0.05-0.10**: a strong standalone signal.
- **IC > 0.15 in a backtest**: treat as a red flag for look-ahead, [[feature-engineering-crypto|survivorship]], or overfitting until proven otherwise — real crypto features rarely sustain this out-of-sample (speculative threshold; calibrate to your universe and horizon).

## IC → Breadth → Sharpe (the Fundamental Law)

Grinold's **Fundamental Law of Active Management** links the quality of forecasts to the achievable risk-adjusted return:

`IR ≈ IC × √Breadth`

where **IR** is the portfolio [[information-ratio]] (the benchmark-relative [[sharpe-ratio|Sharpe]]) and **Breadth** is the number of *independent* bets per year. The message: a weak signal deployed broadly beats a strong signal deployed narrowly.

**Crypto worked example.** A cross-sectional funding-carry signal over ~150 liquid perps, rebalanced every 8h with a rank-IC of **0.03**, makes on the order of `150 names × (365×3 settlements)` bets — but they are far from independent, so effective breadth is much smaller. Suppose effective breadth ≈ **500 independent bets/year**. Then `IR ≈ 0.03 × √500 ≈ 0.67`. Push effective breadth to 2,000 (more assets, less correlated timing) and `IR ≈ 0.03 × √2000 ≈ 1.34`. The lever is *independent* breadth — which is exactly why [[signal-orthogonalization]] (removing shared BTC-beta so bets are actually independent) matters so much in crypto (numbers illustrative; effective breadth is the hard-to-estimate term).

The crucial trap: **breadth counts *independent* bets.** If all 150 perps are really one BTC-beta trade in disguise, effective breadth collapses toward 1 and the IR is an illusion. Crypto's pervasive [[signal-orthogonalization|BTC-beta contamination]] is the main reason nominal breadth overstates true breadth.

## IC decay and half-life

A signal's IC is not constant across the forecast horizon — it **decays**. Measuring IC at multiple horizons (`h` = 1h, 4h, 1d, 3d, 7d, 30d) traces the **IC decay curve**:
- **Fast-decaying signals** (order-book imbalance, taker flow, short-horizon funding): IC peaks at minutes-to-hours and is ~0 by a day. High Sharpe potential but turnover- and cost-heavy.
- **Slow-decaying signals** (MVRV/dormancy, whale accumulation, dry-powder): IC builds over days-to-weeks. Lower turnover, cheaper to trade.
- **IC half-life** — the horizon at which IC falls to half its peak. It sets the natural rebalance frequency: rebalancing much faster than the half-life just pays costs; much slower leaves alpha on the table.

Separately, IC **decays over calendar time** as a signal crowds — this is [[alpha-decay]]. Plotting rolling 90d mean-IC of a live signal is the primary early-warning that an edge is dying.

## Using IC to triage a raw crypto feature (before building anything)

The discipline: compute IC *first*, build a strategy *only* if it clears the bar. A pre-build IC checklist:

1. **Point-in-time panel.** Assemble the feature and forward returns from a survivorship-free, point-in-time universe (see [[feature-engineering-crypto]]) — otherwise IC is inflated by dead tokens.
2. **Rank-IC, not Pearson.** Use Spearman to neutralize crypto's fat tails.
3. **Multiple horizons.** Compute the IC decay curve to find the half-life and thus the tradeable frequency.
4. **IC-IR and t-stat.** `mean(IC)/std(IC)` and a t-stat on the IC series test whether the skill is *consistent*, not one lucky quarter. A high mean IC with huge variance is fragile.
5. **Regime split.** Compute IC separately in bull/bear/chop ([[market-regime]]); a signal that only works in one regime needs a regime gate.
6. **Net-of-cost sanity.** A fast IC that dies after realistic fees + funding + slippage is not tradeable. Overlay a cost model before celebrating.
7. **Orthogonalized IC.** Recompute IC on the BTC-beta-residualized signal (see [[signal-orthogonalization]]); if the IC vanishes once beta is removed, the "signal" was just market direction.

Only signals that pass steps 1-7 graduate to [[feature-selection-trading|feature selection]] and [[alpha-model|alpha-model]] construction.

## Computing IC in practice

```python
# Cross-sectional rank-IC time series and its decay across horizons.
import pandas as pd

def rank_ic(signal, fwd_return):
    # signal, fwd_return: DataFrames indexed by time, columns = assets
    return signal.rank(axis=1).corrwith(fwd_return.rank(axis=1), axis=1)  # Spearman per timestamp

def ic_summary(ic):
    mean, sd = ic.mean(), ic.std()
    return {"mean_IC": mean, "IC_IR": mean / sd, "t_stat": mean / sd * (len(ic) ** 0.5)}

# Decay curve: recompute mean rank-IC at each horizon and find the half-life.
for h in [1, 4, 24, 72, 168, 720]:      # hours
    ic_h = rank_ic(signal_t, fwd_return_h[h])
    print(h, ic_summary(ic_h)["mean_IC"])
```

An illustrative decay curve for a funding-based signal (numbers indicative, not measured):

| Horizon | 1h | 4h | 1d | 3d | 7d | 30d |
|---|---|---|---|---|---|---|
| Mean rank-IC | 0.045 | 0.040 | 0.030 | 0.018 | 0.010 | 0.003 |

Peak IC ~0.045 at 1h; half-life near the 3d mark — so an 8h-to-daily rebalance captures most of the edge without over-trading.

## Common pitfalls

- **Look-ahead** — using the revised or same-bar data inflates IC; the classic phantom-alpha source.
- **Overlapping returns** — multi-day forward returns computed every hour are autocorrelated, so the naive IC t-stat is overstated; use non-overlapping samples or adjust degrees of freedom.
- **Confusing high IC with high Sharpe** — a high-IC, high-turnover, high-cost signal can be unprofitable; a low-IC, high-breadth, low-cost signal can be excellent.
- **Cross-sectional vs. time-series IC** — cross-sectional IC (rank assets at each time) and time-series IC (predict one asset's own next return) answer different questions; don't mix them.

## Getting the Data (CryptoDataAPI)

IC is computed on a signal series aligned to forward returns. Pull both from the archive for a point-in-time calculation, and the live endpoints to compute IC on fresh signals:

**Historical (to build the IC panel):**
- `GET /api/v1/backtesting/klines` — forward-return labels over each horizon
- `GET /api/v1/backtesting/funding` — funding-signal history
- `GET /api/v1/backtesting/daily-snapshots/{date}` — point-in-time signal values (survivorship-free)

**Live (to compute IC on current signals):**
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — funding signal
- `GET /api/v1/on-chain/dormancy/btc` — MVRV/dormancy signal
- `GET /api/v1/on-chain/whale-score/{symbol}` — whale-accumulation signal

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/backtesting/klines?symbol=BTCUSDT&interval=1d&limit=1000"
```

Auth: `X-API-Key` header. Category pages: [[cryptodataapi-backtesting]], [[cryptodataapi-derivatives]], [[cryptodataapi-on-chain]].

## Related

- [[alpha-model]] — where IC-weighted signals are combined
- [[information-ratio]] — the portfolio quantity IC feeds via the Fundamental Law
- [[alpha-decay]] — IC falling over calendar time as a signal crowds
- [[signal-orthogonalization]] — restoring *independent* breadth so IC × √breadth is real
- [[feature-engineering-crypto]] / [[feature-selection-trading]] — the pipeline IC triages
- [[crypto-signal-library]] — the menu of signals to screen with IC

## Sources

- Grinold, Richard, and Ronald Kahn. *Active Portfolio Management* (2000) — the Fundamental Law, IC, and the IC/breadth decomposition
- [[book-machine-learning-for-asset-managers]] — de Prado on IC estimation, overlapping-sample bias, and signal evaluation
- [[book-advances-in-financial-ml]] — purged/embargoed evaluation to avoid inflated IC
