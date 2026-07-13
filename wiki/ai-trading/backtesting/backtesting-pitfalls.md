---
title: "Backtesting Pitfalls"
type: concept
created: 2026-04-06
updated: 2026-06-21
status: excellent
tags: [ai-trading, backtesting, methodology, risk-management]
related:
  - "[[walk-forward-optimization]]"
  - "[[monte-carlo-backtesting]]"
  - "[[monte-carlo-permutation-test]]"
  - "[[backtrader-framework]]"
  - "[[vectorbt]]"
  - "[[bot-risks-and-pitfalls]]"
  - "[[book-advances-in-financial-ml]]"
  - "[[book-quantitative-trading-ernest-chan]]"
  - "[[book-building-winning-algo-trading-systems]]"
  - "[[crypto-perp-backtesting-pitfalls]]"
  - "[[auto-deleveraging]]"
  - "[[liquidation-cascade-modeling]]"
  - "[[point-in-time-data]]"
  - "[[funding-rate]]"
  - "[[2025-10-crypto-liquidation-cascade]]"
  - "[[deflated-sharpe-ratio]]"
  - "[[minimum-track-record-length]]"
  - "[[data-snooping-and-p-hacking]]"
  - "[[overfitting]]"
  - "[[intrabar-fill-modeling]]"
  - "[[slippage-modeling]]"
  - "[[backtesting]]"
---

# Backtesting Pitfalls

Why most backtests are wrong. The gap between backtest performance and live performance is the central challenge in quantitative trading. Understanding these pitfalls is the difference between deploying a profitable strategy and deploying an illusion.

---

## Overview

A backtest simulates how a strategy would have performed on historical data. Done correctly, it provides valuable evidence about a strategy's edge. Done incorrectly -- which is the default -- it produces dangerously misleading results that look profitable on paper but lose money in live markets. **If your backtest looks too good to be true, it is.**

Pitfalls fall into three broad families, and a credible validation process must address all three:

| Family | What goes wrong | Primary defences |
|---|---|---|
| **Information leakage** | The backtest "knows" the future (look-ahead, survivorship, revised data) | Point-in-time data ([[point-in-time-data]]), strict timestamping, [[intrabar-fill-modeling]] |
| **Cost & execution realism** | Frictionless fills (no slippage, fees, impact, funding) | [[slippage-modeling]], commission models, depth-aware fills, market-impact models |
| **Statistical illusion** | Noise mistaken for edge (overfitting, data snooping, too-short samples) | [[walk-forward-optimization]], [[monte-carlo-permutation-test]], [[deflated-sharpe-ratio]], [[minimum-track-record-length]] |

---

## The 10 Deadly Sins

The ten sins below map onto those three families — the first six are mostly leakage and statistical illusion; sins 3, 4, 7, 8, 9 are cost and execution realism.

| # | Sin | Family | One-line fix |
|---|---|---|---|
| 1 | Look-ahead bias | Leakage | Every input timestamped before the decision |
| 2 | Survivorship bias | Leakage | Point-in-time universe incl. delisted assets |
| 3 | No slippage | Cost | Depth-aware [[slippage-modeling\|slippage]] model |
| 4 | No commissions/fees | Cost | Always charge realistic fees |
| 5 | Overfitting | Statistical | [[walk-forward-optimization]]; low param count |
| 6 | Data snooping | Statistical | [[deflated-sharpe-ratio]]; one-shot holdout |
| 7 | Ignoring market impact | Cost | Impact ∝ size / ADV |
| 8 | Wrong position sizing | Cost | Size to real capital & book depth |
| 9 | No funding costs | Cost | Charge borrow/[[funding-rate\|funding]]/margin |
| 10 | Cherry-picked periods | Statistical | Test across regimes incl. bear/crash |


### 1. Look-Ahead Bias

Using information that would not have been available at the time of the trading decision. Examples: using the daily close price to make a decision at the open, incorporating earnings data before the release date, using future-adjusted data, or — at intraday resolution — filling an order at a price that the bar only reached *after* the signal (see [[intrabar-fill-modeling]]). **Detection**: Check that every data point used in signal generation has a timestamp before the trade entry; enforce the "signal-on-close, fill-on-next-open" rule.

### 2. Survivorship Bias

Testing only on assets that still exist today. Stocks that went bankrupt, crypto tokens that went to zero, and ETFs that were delisted are excluded, biasing results upward (Source: [[book-quantitative-trading-ernest-chan]]). **Fix**: Use point-in-time datasets that include delisted securities.

### 3. Not Accounting for [[slippage]]

Assuming perfect fills at the exact price you want. In reality, market orders experience slippage, especially in thin markets. **Fix**: Add realistic slippage models. [[backtrader-framework|Backtrader]] and [[quantconnect|QuantConnect]] support configurable slippage.

### 4. Ignoring Commissions and Fees

A strategy that trades frequently can be profitable pre-fees and unprofitable post-fees. Crypto exchange fees (0.1% maker/taker) compound quickly on high-frequency strategies. **Fix**: Always include commissions in backtest configuration.

### 5. Overfitting to Historical Data

Optimizing too many parameters on too little data until the strategy perfectly fits the past but has no predictive power (Source: [[book-building-winning-algo-trading-systems]]). A strategy with 20 optimized parameters and 100 trades is almost certainly overfit. **Fix**: Use [[walk-forward-optimization]] and keep parameter count low relative to trade count.

### 6. Data Snooping (Multiple Testing)

Testing hundreds of strategy variations and selecting the one that worked best. With enough attempts, random noise will produce seemingly profitable results (Source: [[book-advances-in-financial-ml]]). This is [[data-snooping-and-p-hacking|data snooping]], and it is the failure mode the [[deflated-sharpe-ratio]] was built to catch — it discounts the selected strategy's Sharpe by the number of trials run. **Fix**: Adjust for multiple comparisons (Bonferroni correction), report a [[deflated-sharpe-ratio]] that folds in the trial count, or use a holdout test set that is only evaluated once.

### 7. Ignoring Market Impact

Large orders move the market. A backtest that assumes unlimited [[liquidity]] at the quoted price will overstate returns for any meaningful position size. **Fix**: Estimate market impact as a function of order size relative to average volume.

### 8. Wrong Position Sizing

Backtesting with unrealistic leverage, full portfolio allocation to single trades, or position sizes that would be impossible given actual [[liquidity]]. **Fix**: Size positions based on realistic capital, risk limits, and available order book depth.

### 9. Not Accounting for Funding Costs

Ignoring borrowing costs for short positions, [[margin]] interest, and crypto [[funding-rate|funding rates]] for perpetual futures. These costs accumulate and can turn a profitable strategy negative. **Fix**: Include financing costs in the backtest model.

### 10. Cherry-Picking Time Periods

Showing a strategy that "works" on 2020-2021 (crypto bull market) without testing on 2022 (bear market). Any momentum strategy looks great in a bull market. **Fix**: Test across multiple market regimes including bear markets, crashes, and range-bound periods.

---

## Red Flags and Validation

A backtest is suspect if: Sharpe > 3.0, win rate > 70% with large wins, no losing months, results collapse when fees are added, or results are parameter-sensitive. Before trusting results, verify: commissions/slippage included, survivorship-bias-free data, [[walk-forward-optimization]] used, multiple regimes tested, [[monte-carlo-backtesting|Monte Carlo]] confirms robustness, and paper trading validates.

### Red-flag reference table

| Red flag | What it usually signals | Diagnostic |
|---|---|---|
| Sharpe > 3 on daily data | Look-ahead, overfit, or unmodelled cost | Re-run with realistic fills; check [[minimum-track-record-length]] |
| Win rate > 70% with fat wins | Survivorship or stop-first ambiguity | Bracket fills; PiT data |
| No losing months | Smoothed / stale marks, or curve-fit | Inspect monthly return distribution |
| Edge vanishes when fees added | Cost-realism failure | Charge full fees + [[slippage-modeling\|slippage]] |
| Result swings with tiny param changes | Overfitting | [[walk-forward-optimization]]; reduce parameters |
| Best of many tried variants | Data snooping | [[deflated-sharpe-ratio]]; one-shot holdout |
| Short, flattering track record | Sample below significance | [[minimum-track-record-length]] |

### Statistical validation stack

A clean P&L curve is necessary but not sufficient. Before trusting an apparent edge, run it up the validation stack — each rung answers a question the rung below cannot:

1. **[[minimum-track-record-length]]** — is the sample even long enough for the Sharpe to be meaningful? If not, stop here.
2. **[[monte-carlo-permutation-test]]** — could this result arise by chance under a distribution-free null? Shuffle the signal/returns and rebuild the null.
3. **[[deflated-sharpe-ratio]]** — after accounting for how many variants were tried, is the *selected* result still significant?
4. **[[walk-forward-optimization]]** — does the edge persist out-of-sample as parameters are re-fit through time?
5. **Paper / pilot trading** — does it survive live microstructure, latency, and slippage that no backtest fully captures?

A strategy that clears all five is hard to dismiss as luck or [[overfitting]]; one that clears only the backtest P&L has merely been spot-checked.

---

## Crypto Perpetual-Futures Specific Pitfalls

The 10 deadly sins above apply to every market. Crypto [[perpetual-futures|perps]] add a second tier of failure modes that the October 10-11 2025 liquidation cascade and the April 2026 Aave/KelpDAO incident both made expensive. The deep-dive lives at [[crypto-perp-backtesting-pitfalls]]; the headline traps are summarised here.

### A. Auto-deleveraging not modeled

When an exchange's insurance fund cannot absorb a bankrupt position, the loss is socialised through [[auto-deleveraging|ADL]] — profitable positions on the *opposite* side are force-closed, in priority order, until the book balances. Standard backtests assume liquidations only affect the position being liquidated. During the [[2025-10-crypto-liquidation-cascade|October 10-11, 2025 cascade]] (~$20B liquidations) ADL broke nominally delta-neutral basis and funding-arb trades that had passed every conventional stress test. **Fix**: in any perp backtest, model an ADL probability as a function of (a) realised mark-to-fair divergence, (b) insurance-fund balance proxy, and (c) cross-position correlation. Drop the most-profitable hedge leg with that probability and recompute drawdowns.

### B. Funding-rate regime shifts

[[funding-rate|Funding rates]] are not stationary. The basis-trade APY ran near 19% through 2024, then compressed to under 4% by mid-2025 as crowding intensified and the post-cascade ADL regime made the trade riskier. A backtest that splices pre-2025 funding history into a forward simulation will systematically overstate expected return. **Fix**: regime-condition the backtest — fit funding-rate dynamics on the post-October-2025 window separately, or use [[market-regime-detection-ml|regime detection]] to switch parameters.

### C. Liquidation cascade modeling

Cascades are the dominant tail risk for leveraged crypto strategies and they are not Gaussian. A single $1.5B+ cascade can execute in minutes, with mark prices wicking 5-15% beyond what a quoted spread implies. Static slippage models miss this entirely. **Fix**: see [[liquidation-cascade-modeling]] for the dependency-aware approach (own-position-size driven price impact + exogenous cascade Poisson process calibrated to [[coinglass]] historical liquidation distributions).

### D. Slippage in crypto: depth-aware, not fixed

A 0.1% fixed slippage assumption is an artefact of equity-market backtesting tools. In crypto perps, realistic slippage on a 100x leveraged $1M order during a stressed regime can be 1-3% one-way; in a flash crash, market orders can fill 5-10% from last. Different methodologies (fixed %, VWAP, tick-by-tick replay, depth-walked) produce results that diverge by an order of magnitude. **Fix**: walk the historical L2 book where available (see [[coinglass]], Kaiko); otherwise calibrate to an Almgren-Chriss-style impact model with crypto-specific parameters and stress the volatile-regime case separately.

### E. Survivorship bias in the token universe

Crypto's failed-asset graveyard is large: Terra/LUNA, FTT, dozens of L1s, hundreds of memecoins. Exchange failures (FTX, Celsius, Voyager, Gemini Earn) also delisted entire token sets. A backtest run against today's CoinGecko top-100 silently excludes the losers. **Fix**: use a point-in-time token universe (CoinAPI, Glassnode, Kaiko all publish PiT lists) and explicitly include delisted tokens with their final price = 0 where appropriate. See also [[survivorship-bias]].

### F. Look-ahead bias from revised on-chain data

On-chain metrics depend on labels (entity tags, exchange clusters, smart-contract sets) that get backfilled as analysts learn more. A "today's snapshot" of 2022 exchange flows uses 2026 labelling — a subtle [[lookahead-bias]] vector unique to crypto. **Fix**: use [[point-in-time-data|PiT-versioned]] on-chain feeds (Glassnode is the reference vendor); never rebuild historical features against the live API.

### G. Single-venue assumption when liquidity is fragmented

Crypto liquidity is split across Binance, Bybit, OKX, [[hyperliquid]], dYdX, and others, with Hyperliquid alone reaching ~73% of decentralised perp share by H1 2025. A backtest run against one venue's order book systematically over-estimates fillability for any size strategy. **Fix**: aggregate L2/L3 books across venues (CCXT helps), or constrain backtest size to a fraction of the smallest plausible execution venue's depth.

### H. Stablecoin / collateral assumed always at par

USDT and USDC do not always trade at $1. UST went to zero, USDC depegged to ~$0.87 during the SVB weekend, and during the April 2026 Aave incident stablecoin pools hit 100% utilisation. A backtest that uses USDT as the unit of account and assumes 1.0 USDT/USD always collapses an entire risk dimension. **Fix**: model collateral price as a separate stochastic process; add depeg shocks to the Monte Carlo overlay.

### I. Oracle manipulation for DeFi-integrated strategies

Strategies that touch DeFi (Aave borrows, GMX positions, perp DEXes with TWAP oracles) are exposed to oracle-manipulation attack vectors. The April 2026 Aave/KelpDAO bridge exploit ($196M bad debt) and the recurring history of flash-loan oracle attacks demonstrate this is not a tail-of-tails event. **Fix**: identify every oracle dependency in the strategy graph and stress-test with adversarial price paths that respect the oracle's update mechanism (TWAP window, Chainlink heartbeat, etc.).

> For the full treatment — including framework-by-framework checklists for Backtrader / vectorbt / Zipline, calibration recipes, and the Glassnode/Coinglass/Kaiko data-vendor map — see the dedicated **[[crypto-perp-backtesting-pitfalls]]** page.

---

## Sources

- [[book-advances-in-financial-ml]] — data snooping, multiple testing bias, and the backtest overfitting problem in quantitative research
- [[book-quantitative-trading-ernest-chan]] — survivorship bias, transaction cost modeling, and practical backtesting pitfalls for independent quants
- [[book-building-winning-algo-trading-systems]] — overfitting detection via walk-forward testing and Monte Carlo validation

## See Also

- [[walk-forward-optimization]] -- The correct way to optimize parameters
- [[monte-carlo-backtesting]] -- Stress-testing strategy robustness
- [[monte-carlo-permutation-test]] -- Distribution-free significance test for an edge
- [[deflated-sharpe-ratio]] -- Correcting the Sharpe for the number of variants tried
- [[minimum-track-record-length]] -- Is the sample long enough to trust the Sharpe?
- [[data-snooping-and-p-hacking]] -- The multiple-testing trap behind most false edges
- [[intrabar-fill-modeling]] -- Intraday fill realism and the H-or-L ambiguity
- [[bot-risks-and-pitfalls]] -- What goes wrong after deployment
- [[backtrader-framework]] -- Framework with built-in slippage/commission models
- [[quantconnect]] -- Platform with institutional-grade simulation
- [[slippage]] -- The hidden cost most backtests ignore
