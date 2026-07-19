---
title: "Volatility Regime Switching"
type: concept
created: 2026-05-07
updated: 2026-07-19
status: excellent
tags: [volatility, indicators, quantitative, regime, backtesting]
aliases: ["Regime-Switching Models", "Markov-Switching Volatility", "Vol Regime Switching"]
related: ["[[volatility-regime]]", "[[volatility-regime-classification]]", "[[volatility-term-structure]]", "[[market-regime]]", "[[market-regime-detection-ml]]", "[[hidden-markov-model]]", "[[garch]]", "[[backtesting]]", "[[lookahead-bias]]", "[[overfitting]]", "[[implied-volatility]]", "[[realized-volatility]]", "[[variance-risk-premium]]", "[[volmageddon]]", "[[covid-crash]]", "[[vix-august-2024-spike]]", "[[cryptodataapi]]"]
domain: [quantitative, volatility]
prerequisites: ["[[volatility-regime]]", "[[garch]]"]
difficulty: advanced
---

**Volatility regime switching** is the empirical pattern — and the family of econometric models that capture it — in which the parameters of the return-generating process change discretely between a small number of latent states. The dominant tools are Hidden Markov Models (HMM) and Markov-switching GARCH following Hamilton (1989), supplemented by structural-break tests (CUSUM, Bai-Perron) and threshold autoregressive models. For a trader, the critical insight is not the math but the consequence: a backtest that fits a single set of parameters across multiple regimes is, by construction, fitting an average that no regime actually inhabits — and is therefore fragile to the next regime transition.

## Overview

Real-world volatility does not evolve as a single smooth process. It moves in clusters with characteristic levels, then transitions — sometimes gradually, often violently — to a different cluster with different characteristic levels. The pattern shows up in:

- **Equity index vol** — long calm regimes punctuated by short crisis regimes (see [[volatility-regime]] for examples).
- **Currency vol** — pegged-then-broken regimes (Asia 1997, Swiss franc 2015, GBP/USD 2016).
- **Rate vol** — the [[move-index|MOVE index]] shows decade-scale regimes tied to monetary policy.
- **Crypto vol** — even more pronounced clustering with sharper transitions.

Modeling this pattern requires letting the data say *which regime is active*, because the regime is a latent state. The toolkit is the **regime-switching** family of models. The lineage runs:

- ARCH (Engle 1982) and GARCH (Bollerslev 1986) — single-regime conditional heteroskedasticity.
- Hamilton (1989, *Econometrica*) — Markov-switching autoregression for business cycles.
- Gray (1996), Klaassen (2002) — Markov-switching GARCH.
- Bai-Perron (1998, 2003) — multiple structural breaks at unknown dates.
- Hidden Markov Models — the broader latent-state framework, applicable far beyond volatility.

## Definition / Formal Description

### Hidden Markov Model

The discrete-state HMM treats the return process as a mixture conditioned on a latent regime indicator `s_t`:

```
r_t | s_t = k  ~  N(μ_k, σ_k²)            (emission)
P(s_t = j | s_{t-1} = i) = A_{ij}          (transition)
```

The transition matrix `A` encodes regime persistence — diagonal elements close to 1.0 mean regimes are sticky. For SPX daily returns, a fitted two-state HMM typically yields:

```
A ≈ [[0.985, 0.015],     # low-vol → low-vol or → high-vol
     [0.05,  0.95 ]]     # high-vol → low-vol or → high-vol
σ_low ≈ 0.6%/day  (~9.5% annualized)
σ_high ≈ 1.8%/day (~28% annualized)
```

Implied half-lives: low-vol ≈ 46 days; high-vol ≈ 14 days. The asymmetry — the calm regime is roughly three times stickier — is the structural reason short-vol *appears* profitable in casual backtesting.

Inference proceeds via:

- **Forward-backward algorithm** — smoothed probability `P(s_t = k | r_{1:T})` for each date.
- **Viterbi algorithm** — the most likely *path* of regimes.
- **EM (Baum-Welch)** — maximum-likelihood estimation of `A`, `μ_k`, `σ_k`.

### Markov-switching GARCH

Hamilton-style switching combined with GARCH dynamics:

```
σ_t² | s_t = k  =  ω_k + α_k r_{t-1}² + β_k σ_{t-1}²
```

Each regime has its own GARCH parameters. Fits better than a single-regime GARCH on long samples but introduces a *path-dependence* problem (the GARCH state at time `t` depends on the entire history of regimes), which Klaassen (2002) addresses via integration over the regime path.

### Structural break tests

When the question is *"did the regime change at a specific date?"*, structural-break tests are appropriate:

- **CUSUM (cumulative sum) test** — Brown, Durbin, Page. Tracks the cumulative sum of standardized residuals; large deviations indicate a parameter change. Variants include CUSUM-of-squares for variance breaks.
- **Bai-Perron (1998, 2003)** — tests for *multiple* breaks at *unknown* dates simultaneously. Standard in macro econometrics; useful for identifying historical regime change-points without imposing them ex ante.
- **Quandt-Andrews / sup-Wald test** — tests whether a single break occurred somewhere in a window.

### Threshold autoregressive models

Tong (1978) — TAR / SETAR (self-exciting threshold autoregressive) models trigger regime change when an observed state variable crosses a threshold. Useful when the regime trigger is observable (e.g., VIX crossing a level) rather than latent.

### Choosing Among the Models

| Model | Regime is | Output | Strength | Weakness |
|-------|-----------|--------|----------|----------|
| **Two-state HMM** | Latent | Regime probability per date | Interpretable, sample-efficient | Gaussian/Markov assumptions violated by fat tails |
| **Markov-switching GARCH** | Latent | Regime-conditional variance | Captures within-regime clustering | Path-dependence makes online estimation expensive |
| **CUSUM / Bai-Perron** | A dated break | Change-point(s) | Pinpoints *when* a break occurred | Says nothing about which regime is active going forward |
| **TAR / SETAR** | Observable threshold | Rule-based switch | Transparent, no latent estimation | Requires you to know the trigger variable a priori |

For production trading the consensus default is a **two-state HMM on daily returns plus a fast term-structure overlay** — it captures most of the practical value without the path-dependence cost of Markov-switching GARCH (see Implications for Strategy #4). The broader, multi-feature, multi-asset generalization of this approach is covered in [[market-regime-detection-ml]].

## Empirical Evidence / Examples

### Real-world transitions

**2017 calm → 2018 [[volmageddon|Volmageddon]] (Feb 5, 2018).** A two-state HMM fit on data through end-2017 puts the smoothed probability of the low-vol regime at > 0.99 throughout 2017. On Feb 5, 2018, the [[volmageddon|XIV blow-up day]], realized vol jumped 5σ relative to the low-vol regime parameters; the smoothed regime probability flipped to high-vol within 1–2 days. The transition was abrupt: a vol-of-vol event triggered by a crowded short-vol ETP cascade rather than a macro shock.

**2019 calm → 2020 [[covid-crash|COVID]] (Feb 24, 2020 onward).** Through January 2020, the same HMM signaled high regime confidence in low-vol. Realized vol began ticking up the week of Feb 24; by March 9 the regime smoother had fully transitioned to high-vol, and the smoothed probability of low-vol stayed near zero until June. This was a *macro-shock* transition, distinct in mechanism but identical in econometric signature.

**2024 calm → [[vix-august-2024-spike|August 5, 2024 spike]].** VIX averaged ~13 through summer 2024 with the regime-classifier confidently in low-vol. The Aug 5 spike (intraday VIX > 65) was triggered by the unwind of the JPY carry trade compounding with weak NFP — a *carry-trade-unwind* transition. The vol-regime signature in equity returns lasted only a few weeks before reverting; HMM smoothers actually had difficulty resolving it as a full regime change due to its rapid mean-reversion.

| Transition | Date | Trigger type | HMM regime-flip lag | Persistence |
|------------|------|--------------|---------------------|-------------|
| [[volmageddon\|Volmageddon]] | Feb 5, 2018 | Vol-of-vol / crowded short-vol ETP cascade | 1–2 days | Short, sharp |
| [[covid-crash\|COVID crash]] | Feb 24 – Mar 2020 | Macro shock | ~2 weeks (full by Mar 9) | Months (low-vol prob near zero until June) |
| [[vix-august-2024-spike\|Aug 2024 spike]] | Aug 5, 2024 | JPY carry-trade unwind + weak NFP | Hard to resolve (rapid mean-reversion) | Weeks only |

The lesson across all three: the *trigger* differed (vol-of-vol cascade, macro shock, FX unwind), but the *structural profile* — long calm regime, abrupt transition, asymmetric exit — repeats. Regime-switching models do not predict the trigger; they identify the structural pattern after the fact and provide the framework for sizing the bet that *some* trigger will eventually fire.

### How regime-switching affects backtests

The empirical importance of regime-switching for backtesting is hard to overstate:

1. **Single-regime parameter estimates are weighted averages.** A short-strangle backtest fit on 2010–2024 SPX data is implicitly fitting a model on a sample that is ~85% calm/normal regime and ~15% stressed/crisis. The resulting Sharpe is the weighted average; in any specific regime, the realized Sharpe will be either much higher or sharply negative.
2. **Out-of-sample failure is regime-dependent.** A strategy can pass walk-forward validation if every walk-forward fold contains the same regime mix. The *real* out-of-sample test is whether the strategy survives the regime that wasn't in the training data — which is, by definition, never available ex ante.
3. **Overfitting often manifests as regime-overfitting.** A backtest tuned to perform well on 2014–2019 SPX data is tuned to a calm-dominant sample. The *true* edge being measured is partly real (variance risk premium) and partly an artifact of the regime mix.
4. **Deflated Sharpe ratio.** López de Prado's [[deflated-sharpe-ratio|Deflated Sharpe Ratio]] formally penalizes the multiple-trials problem; when regime-switching is present, the *effective* number of independent observations is much smaller than the number of days because returns within a regime are highly correlated.

The honest fix is to backtest under *forced regime stratification* — e.g., compute Sharpe separately within each HMM-inferred regime, and require the strategy to make sense in all regimes (or to have an explicit regime-conditional sizing rule). See [[backtesting]] and [[overfitting]] for the broader hygiene practices.

## Implications for Strategy

1. **Use regime probability, not regime label, for sizing.** A binary "calm vs stressed" tag whipsaws on the boundary. A smoothed regime *probability* (output of forward-backward) lets size scale continuously — half the position when `P(stressed) = 0.5`, full position when `P(calm) = 0.95`.
2. **Match strategy to regime persistence.** Short-vol works because the calm regime is sticky (multi-month half-life). Long-vol convexity works because the stressed regime is short but extreme. Trying to "trade" the regime transition itself is the hardest variant — the transition window is short and the signal-to-noise low.
3. **Use [[volatility-term-structure|term-structure-based]] signals as fast complements to slow HMM signals.** The HMM smoother updates over weeks; the [[volatility-term-structure|VIX/VIX3M]] inversion updates intraday. Use both.
4. **Avoid Markov-switching GARCH for production trading unless you have the infrastructure for it.** The path-dependence problem makes online estimation expensive. A two-state HMM on daily returns plus a term-structure overlay captures most of the practical value.
5. **Do not over-fit the number of regimes.** Two- and three-state models are interpretable and stable. Five-state models tend to allocate states to noise. Information criteria (AIC, BIC) help but are themselves penalized by regime-switching's parameter explosion.

## Common Mistakes

1. **Trusting a one-shot HMM fit.** HMM likelihood surfaces are multi-modal; different starting seeds find different local maxima. Always fit from multiple random starts and pick the best likelihood.
2. **Confusing in-sample regime labels with out-of-sample regime forecasts.** The smoothed regime probability uses *future* data through the forward-backward algorithm. For real-time trading, use the *filtered* probability, which only uses data up to time `t`. Conditioning live trades on smoothed probabilities is a textbook [[lookahead-bias|look-ahead bias]] — the same filtered-vs-smoothed trap is detailed in [[market-regime-detection-ml#Filtered vs. Smoothed Probabilities (the live-trading trap)|the ML regime-detection page]].
3. **Ignoring transition matrix sampling error.** With ~15 regime transitions in 25 years of SPX data, the off-diagonal entries of `A` have wide confidence intervals. Treat them as point estimates with caution.
4. **Building strategies that work only at the regime boundary.** Backtests that look spectacular often turn out to be earning their P&L on the 2–3 regime transitions in the sample. Strip out those days and the edge disappears.
5. **Using regime models without a non-econometric sanity check.** When the model says *"low-vol regime"* but credit spreads are widening, breadth is collapsing, and term structure is flat, trust the cross-asset evidence over the single-asset model.
6. **Fitting Markov-switching GARCH and then using a single-regime simulator for risk.** The whole point of fitting the switching model is that risk is regime-conditional — use the switching model in the risk simulation too.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/regimes/current` — current long-horizon market regime (10-state taxonomy)
- `GET /api/v1/quant/market` — HMM regime probabilities, 4h/24h horizons (15-min refresh)
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite (0-100)
- `GET /api/v1/liquidity/regime/score` — liquidity fragility composite (0-100)

**Historical data:**
- `GET /api/v1/quant/timeline` — daily market regime labels, 2019-now
- `GET /api/v1/quant/regimes/history` — full 6-regime Parquet download (2020-yesterday)
- `GET /api/v1/quant/history` — point-in-time probability records for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/regimes/current"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-regimes]].

**Live dashboards:** [short-term regimes](https://cryptodataapi.com/market-regimes) · [long-term regimes](https://cryptodataapi.com/regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can work with this indicator directly:

- **Live state** — `GET /api/v1/quant/market` exposes filtered probabilities from a production 6-state HMM (15-min refresh) — the online `P(s_t | data through t)` this page requires for live trading; `GET /api/v1/quant/model` publishes model version and metrics for auditability
- **Compute** — fit your own MS-GARCH or K-state HMM on return series from `GET /api/v1/backtesting/klines` (Binance spot 1h/4h/1d back to 2017-08) and compare recovered states against the hosted engine's taxonomy from `GET /api/v1/quant/regimes`
- **Backtest** — `GET /api/v1/quant/history` gives point-in-time probability records and `GET /api/v1/quant/regimes/history` the full hourly Parquet archive since 2020 (Pro Plus) — enough transitions to test boundary-dependence of a strategy's P&L
- **Tip** — replay the mistake list here: strip regime-transition days out of a backtest built on these archives and confirm the edge survives before attributing it to regime-switching skill

## Related

- [[volatility-regime]] — the broader concept of which regime-switching is the modeling framework
- [[volatility-regime-classification]] — operational four-regime classification used at the trading desk
- [[market-regime]] — the foundational cross-asset regime concept
- [[market-regime-detection-ml]] — multi-feature ML generalization of this framework
- [[volatility-term-structure]] — fast complementary signal for transition detection
- [[hidden-markov-model]] — the latent-state framework underlying regime models
- [[garch]] — single-regime conditional heteroskedasticity, the building block
- [[backtesting]] — why regime-stratified evaluation matters
- [[lookahead-bias]] — filtered-vs-smoothed probability is a regime-specific instance
- [[overfitting]] — regime-overfitting as a specific failure mode
- [[deflated-sharpe-ratio]] — penalty for multiple-trials in regime-clustered samples
- [[implied-volatility]] / [[realized-volatility]] — the observable inputs to regime fitting
- [[variance-risk-premium]] — regime-dependent in magnitude
- [[volmageddon]] — Feb 2018 case study in calm-to-crisis transition
- [[covid-crash]] — Feb–March 2020 macro-shock transition
- [[vix-august-2024-spike]] — Aug 2024 carry-unwind transition
- [[theta-targeting]] — sizing should be regime-probability-weighted

## Sources

- Hamilton, J. (1989). *A New Approach to the Economic Analysis of Nonstationary Time Series and the Business Cycle*. Econometrica 57(2), 357–384. The seminal Markov-switching paper.
- Hamilton, J. (1994). *Time Series Analysis*. Princeton University Press. Chapter 22 covers regime-switching in textbook form.
- Engle, R. (1982). *Autoregressive Conditional Heteroscedasticity with Estimates of the Variance of United Kingdom Inflation*. Econometrica 50(4). The ARCH foundation.
- Bollerslev, T. (1986). *Generalized Autoregressive Conditional Heteroskedasticity*. Journal of Econometrics 31(3). GARCH.
- Gray, S. (1996). *Modeling the Conditional Distribution of Interest Rates as a Regime-Switching Process*. Journal of Financial Economics 42. Early Markov-switching GARCH application.
- Klaassen, F. (2002). *Improving GARCH Volatility Forecasts with Regime-Switching GARCH*. Empirical Economics 27. Path-dependence solution.
- Bai, J. and Perron, P. (1998, 2003). *Estimating and Testing Linear Models with Multiple Structural Changes*. Econometrica 66 / Journal of Applied Econometrics 18. Multiple-breakpoint methodology.
- Tong, H. (1978, 1990). *Threshold Models in Non-Linear Time Series Analysis*. Lecture Notes in Statistics / Oxford University Press. TAR/SETAR origin.
- López de Prado, M. (2018). *Advances in Financial Machine Learning*. Wiley. On regime-aware backtesting and the deflated Sharpe ratio.
