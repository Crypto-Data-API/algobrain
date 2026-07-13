---
title: "Hyperliquid Backtesting & Anti-Overfit Playbook"
type: concept
created: 2026-06-14
updated: 2026-06-14
status: excellent
tags: [backtesting, crypto, derivatives, methodology, leverage, risk-management]
aliases: ["Hyperliquid Backtesting", "Hyperliquid Anti-Overfit", "Backtesting Hyperliquid Perps"]
domain: [backtesting]
difficulty: advanced
prerequisites: ["[[crypto-perp-backtesting-pitfalls]]", "[[overfitting]]", "[[in-sample-vs-out-of-sample]]"]
related: ["[[crypto-perp-backtesting-pitfalls]]", "[[overfitting]]", "[[in-sample-vs-out-of-sample]]", "[[walk-forward-analysis]]", "[[purged-kfold-cv]]", "[[deflated-sharpe-ratio]]", "[[slippage-modeling]]", "[[liquidation-cascade-modeling]]", "[[intrabar-fill-modeling]]", "[[point-in-time-data]]", "[[lookahead-bias]]", "[[transaction-cost-modeling]]", "[[overfitting-detection]]", "[[hyperliquid]]", "[[hyperliquid-funding-rate-microstructure]]", "[[hyperliquid-liquidation-engine]]", "[[hyperliquid-perp-trading-map]]", "[[funding-rate]]", "[[funding-rate-arbitrage]]", "[[auto-deleveraging]]", "[[perpetual-futures]]", "[[2025-10-crypto-liquidation-cascade]]", "[[book-advances-in-financial-machine-learning]]"]
---

# Hyperliquid Backtesting & Anti-Overfit Playbook

Avoiding [[overfitting]] on [[hyperliquid|Hyperliquid]] perps is not just about train/test splits — it is about making the backtest *behave like Hyperliquid actually behaves*. A strategy that survives clean [[in-sample-vs-out-of-sample|out-of-sample]] data but assumes free fills, an unrealistic fee tier, or never-liquidating leverage is still overfit — to the simulator rather than to the price path. This page is the Hyperliquid-specific layer on top of the venue-generic [[crypto-perp-backtesting-pitfalls]]: hourly funding, rolling-volume fee tiers, order-book fills, USDC margining, and regime-aware holdouts. The unifying principle: **a robust Hyperliquid strategy should survive worse fills, worse fees, worse funding, different coins, and different market regimes.** If it only works under one perfect configuration, it is overfit.

## Why Hyperliquid is its own backtesting problem

Hyperliquid is a **layer 1 blockchain** in its own right — not a smart contract on Solana or Ethereum — running a custom [[hyperliquid|HyperBFT]] consensus that targets 200,000+ transactions per second with roughly 0.07-second finality (Source: [Gate Learn — HyperBFT](https://www.gate.com/learn/course/l1-deep-dives-hyperliquid-hype/hyper-bft-consensus-mechanism)). The exchange's matching engine, margin engine, and liquidation logic are all on-chain protocol mechanics with **publicly specified formulas**, which is unusual: most CEX backtests have to guess at internal mechanics, whereas a faithful Hyperliquid simulator can replicate the venue almost exactly. The flip side is that there is no excuse for an unrealistic simulator — if a backtest ignores hourly funding, rolling-volume fee tiers, oracle-price liquidation, or the HLP/insurance/ADL waterfall, it is overfitting to a fiction. The 15 techniques below are organized to close that gap.

## 1. Strict chronological splits

Split history by time, never by shuffling trades — train to build the idea, validation to tune, a final out-of-sample block touched exactly once. A representative layout:

| Period               | Use                 |
| -------------------- | ------------------- |
| Jan 2024 – Dec 2024  | Research            |
| Jan 2025 – Sep 2025  | Parameter selection |
| Oct 2025 – May 2026  | Final holdout       |

Once you look at the final holdout, do not tune again. Shuffling rows (standard k-fold) leaks future information backwards in any time-series setting, which is why López de Prado's [[book-advances-in-financial-machine-learning|Advances in Financial Machine Learning]] argues for time-respecting splits and feature-importance-driven research over brute-force pattern searching (Source: [Shortform summary](https://www.shortform.com/summary/advances-in-financial-machine-learning-summary-marcos-lopez-de-prado)). See [[in-sample-vs-out-of-sample]] for the discipline.

## 2. Walk-forward testing

Use rolling train→validate→test windows rather than one big optimization. Each training window precedes its test window in time, the windows roll forward, and you track performance and parameter stability across *every* window rather than only the average (Source: [QuantInsti — Walk-Forward Optimization](https://blog.quantinsti.com/walk-forward-optimization-introduction/); [Blockchain Council](https://www.blockchain-council.org/cryptocurrency/backtesting-ai-crypto-trading-strategies-avoiding-overfitting-lookahead-bias-data-leakage/)). This is especially important on Hyperliquid because funding, liquidity, open interest, and volatility shift quickly — and the data spans known regime breaks (the **October 2025 ADL cascade** and the subsequent funding compression, see §16). A strategy whose optimal parameters jump between adjacent windows is regime-fragile even if the blended Sharpe looks fine. Recent crypto-specific walk-forward frameworks (e.g. regime-based Bitcoin backtesting and hypothesis-driven walk-forward validation) formalize exactly this rolling-evaluation discipline. See [[walk-forward-analysis]] and the regime-aware windowing note in [[crypto-perp-backtesting-pitfalls]].

## 3. Purge and embargo overlapping data

If a signal uses a multi-hour lookback and positions are held for hours, train and test windows overlap at the boundary, so a naive split lets information bleed across the seam. **Purging** removes training observations whose labels overlap in time with the test set, and an **embargo** adds a temporal buffer immediately after the test block so that serially-correlated information does not leak backwards into the next training fold (Source: [Purged cross-validation overview](https://en.wikipedia.org/wiki/Purged_cross-validation); [Towards AI — Combinatorial Purged CV](https://towardsai.net/p/l/the-combinatorial-purged-cross-validation-method)). This matters most for ML models, funding-rate strategies, momentum, and any strategy with forward-looking labels (e.g. "did price rise over the next 6 hours?"). The technique originates with López de Prado's [[book-advances-in-financial-machine-learning|Advances in Financial Machine Learning]]. See [[purged-kfold-cv]] and [[cross-validation]].

## 4. Test across assets, not only time

An edge that only works on one coin in one period is probably overfit. Test Hyperliquid perps in groups, because each behaves differently:

| Group               | Why it differs                        |
| ------------------- | ------------------------------------- |
| BTC / ETH           | Deep liquidity, tighter spreads       |
| Large alts          | More volatility, less depth           |
| Smaller perps       | More slippage and regime risk         |
| Newly listed assets | Launch-phase behavior can be abnormal |

A pooled cross-asset test (out-of-sample on coins never used in research) is one of the cheapest and strongest [[overfitting-detection|overfit checks]] available.

## 5. Model Hyperliquid funding correctly

Hyperliquid funding is paid **every hour** — far more frequent than the 8-hour cycle on most CEXes — and is added to or subtracted from the contract holder's balance at each funding interval (Source: [Hyperliquid Docs — Funding](https://hyperliquid.gitbook.io/hyperliquid-docs/trading/funding)). The mechanics that a faithful backtest must reproduce:

**Payment formula** (note: **oracle price, not mark price**):

```
Funding Payment = position_size × oracle_price × funding_rate
```

**Rate formula** — the 8-hour funding rate is computed as a premium plus a clamped interest-rate term, and the hourly charge is one-eighth of that 8-hour rate:

```
8h Funding Rate = Average Premium Index + clamp(interest_rate − Premium, −0.0005, 0.0005)
Hourly Rate     = (8h Funding Rate) / 8
```

- The **interest rate** is fixed at **0.01% per 8 hours** (≈ 11% APR, paid by the side keeping the perp pinned to spot).
- The **premium index is sampled every 5 seconds and averaged over the hour**.
- Hourly funding is **capped at 4% per hour** — a critical detail for stress scenarios, because funding can spike enormously in a squeeze.
- For HIP-3 (builder-deployed) perps the premium uses an impact-bid/impact-ask midpoint: `Premium = (0.5 × (impact_bid + impact_ask) / oracle_price) − 1`.

Backtest implications:

- Charge or credit funding **hourly**, not per 8-hour cycle. A position held across many intervals accrues funding far faster than a CEX-tuned model assumes — at the 4%/hour cap a held position could bleed ~96% of notional in a single brutal day, which a coarse 8-hour model would understate.
- Use only funding information that was **known at the time** — never use future realized funding as a signal (a classic [[lookahead-bias]]).
- **Funding debits reduce margin** and therefore affect the liquidation price (§11) — fold funding into the equity curve before evaluating survival, not after.
- Stress-test funding assumptions (see §12); carry-dependent edges such as [[funding-rate-arbitrage]] are fragile to the post-October-2025 compression (§16).

See [[hyperliquid-funding-rate-microstructure]] for the mechanism in depth.

## 6. Include realistic fees

Hyperliquid fees depend on **rolling 14-day volume**, assessed daily in UTC (Source: [Hyperliquid Docs — Fees](https://hyperliquid.gitbook.io/hyperliquid-docs/trading/fees)). Perps and spot have **separate schedules with 7 tiers each (tiers 0–6)**, and **taker fees consistently exceed maker fees**. Crucially for cross-product strategies, **spot volume counts double** toward tier progression:

```
Weighted 14d Volume = 14d_perps_volume + 2 × 14d_spot_volume
```

Do **not** backtest at the best possible fee tier unless you are sure you will actually qualify for it — and remember the tier is recomputed *daily*, so a quiet fortnight silently demotes you to worse fees. Use a conservative tier, then stress worse fees:

| Scenario        | Purpose                                   |
| --------------- | ----------------------------------------- |
| Normal fees     | Expected case                             |
| 1.5× fees       | Mild stress                               |
| 2× fees         | Robustness test                           |
| Taker-only fees | Tests whether maker-fill assumptions are real |

See [[transaction-cost-modeling]] for the general framework.

## 7. Backtest on order-book data, not only candles

Candle backtests overfit because they assume perfect fills at prices that may never have been tradable. Hyperliquid's `l2Book` info endpoint returns at most **20 levels per side**, each level structured as `px` (price), `sz` (size), `n` (number of orders) (Source: [Hyperliquid Docs — Info endpoint](https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/info-endpoint)). Historical L2 book snapshots are published roughly monthly in the official `hyperliquid-archive` S3 bucket in the format `s3://hyperliquid-archive/market_data/[date]/[hour]/[datatype]/[coin].lz4` (Source: [Hydromancer — Hyperliquid Historical Data](https://hydromancer.xyz/hyperliquid-historical-data)).

**Alternative L2 archives** (useful when the official bucket has gaps or you need finer resolution):

| Source | Resolution / format | Notes |
| ------ | ------------------- | ----- |
| Official `hyperliquid-archive` | ~monthly, LZ4 | Authoritative, gaps possible |
| Hydromancer Reservoir | 1-minute L2 snapshots | Free archive |
| SonarX public S3 | 20-level summaries every ~20 blocks, CC0 | Open license |
| 0xArchive | ~1.2s resolution L2 | Higher granularity |

(Source: [SonarX — Order Book Snapshots release](https://www.sonarx.com/blog/sonarx-releases-hyperliquid-order-book-snapshots); [Hydromancer](https://hydromancer.xyz/hyperliquid-historical-data).)

For a realistic perp backtest, simulate:

- bid/ask spread
- market-order slippage (walk the book level by level — see worked example below)
- partial fills
- queue position for limit orders
- latency between signal and order placement
- failed maker fills
- IOC / GTC / post-only order behavior

A worked slippage pattern: to fill a market buy of size `Q`, consume ask levels in order until cumulative `sz` ≥ `Q`, then the fill VWAP is `Σ(px_i × min(sz_i, remaining)) / Q`. The realized **slippage** is `(fill_VWAP − best_ask) / best_ask`. If `Q` exceeds the 20-level depth the simulator should either reject, partial-fill, or apply a punitive impact estimate rather than silently filling at the top of book. A strategy that only works with candle-close fills is usually overfit. See [[intrabar-fill-modeling]], [[slippage-modeling]], and [[execution-model-differences]].

## 8. No same-candle lookahead

A common bug: the signal uses the candle close, then enters at *that same* close. In reality you only know the close after the candle has closed (Source: [StratBase.ai — Look-Ahead Bias](https://stratbase.ai/en/blog/look-ahead-bias-hidden-killer)). Assume signal-at-close, then enter on the next trade, next candle open, or the next order-book snapshot after latency. The cost of getting this wrong is not academic: in crypto perpetuals the **gap between today's close and tomorrow's open can be 0.5–2%, which is often the entirety of a strategy's edge** (Source: [StratBase.ai](https://stratbase.ai/en/blog/look-ahead-bias-hidden-killer)). This single correction destroys many overfit strategies — which is exactly why it is useful. See [[lookahead-bias]] and [[point-in-time-data]].

## 9. Parameter stability tests

Do not accept a strategy because one parameter combination looks amazing. Robust strategies show a **plateau** of acceptable performance across parameter variations; overfit strategies exhibit sharp **cliffs**, where a small change causes a large performance drop (Source: [PickMyTrade — Stop Backtest Overfitting](https://blog.pickmytrade.trade/trading-strategy-validation-backtest-overfitting/)). You want a plateau, not a spike:

| Pattern   | Fast MA | Slow MA | Sharpe                |
| --------- | ------: | ------: | --------------------- |
| Bad sign  | 17      | 83      | 3.1                   |
| (fragile) | 18      | 83      | 0.4                   |
| (fragile) | 17      | 84      | −0.2                  |
| Good sign | 15–25   | 70–100  | Consistently positive |

A practical quantitative rule: perturb each parameter by **±10–20%** and require that **>70–80% of the neighbouring configurations remain profitable**. A *Parameter Stability Score* = (profitable neighbours) / (total neighbours tested); a lone lucky peak surrounded by losers scores near zero and is a fit to noise. See the heatmap discussion in [[overfitting-detection]] and [[curve-fitting]].

## 10. Penalize multiple testing

If you test 2,000 combinations, the best one often looks good by chance. Track *every* variation tried — indicators, timeframes, coins, stops, take-profits, leverage, funding filters, volatility filters, entry/exit rules — and adjust confidence downward. The [[deflated-sharpe-ratio|Deflated Sharpe Ratio]] (Bailey & López de Prado, *Journal of Portfolio Management*, 2014; SSRN 2460551) explicitly corrects for **two** sources of performance inflation: **selection bias under multiple testing**, and **non-normally distributed returns** (skew and fat tails) (Source: [SSRN 2460551](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2460551)). Both are endemic to crypto strategy research — crypto returns are sharply non-normal, and grid searches over many coins/parameters guarantee selection bias. Report the number of trials `N` alongside the Sharpe, and treat the deflated figure, not the raw figure, as the headline. See [[selection-bias-research]] and [[data-snooping-and-p-hacking]].

## 11. Simulate margin and liquidation rules

Hyperliquid perps use **USDC collateral** with **USDT-denominated linear contracts** — technically *quanto* contracts, since the oracle price is denominated in USDT but the collateral is USDC (Source: [Hyperliquid Docs — Contract Specifications](https://hyperliquid.gitbook.io/hyperliquid-docs/trading/contract-specifications)). They support **cross margin** (the default — maximal capital efficiency, collateral shared across positions) and **isolated margin** (collateral constrained to a single asset) at the wallet level (Source: [Hyperliquid Docs — Margining](https://hyperliquid.gitbook.io/hyperliquid-docs/trading/margining)).

Key formulas a backtest must reproduce:

```
Initial Margin Fraction = 1 / leverage_set_by_user
Maintenance Margin      = at most 0.5 × Initial Margin
Liquidation (cross)     = Account Value (incl. unrealized PnL) < Maintenance Margin × Total Open Notional
```

When account value (including unrealized PnL) falls below maintenance margin times total open notional, the position is liquidated (Source: [Hyperliquid Docs — Margining](https://hyperliquid.gitbook.io/hyperliquid-docs/trading/margining)). A backtest must model:

- cross vs isolated margin
- leverage caps
- maintenance margin (≤ half of initial margin)
- liquidation price (driven by **oracle** price, consistent with funding)
- funding debits reducing margin (link back to §5)
- the liquidation waterfall and forced deleveraging / [[auto-deleveraging|ADL]]
- margin shared across simultaneous positions (cross)

**The liquidation waterfall** (the order in which losses are absorbed):

1. The **HLP vault** takes over the position at a mark-based price.
2. If a shortfall remains, the **insurance fund** covers it.
3. If both are exhausted, **auto-deleveraging (ADL)** closes profitable counterparties' positions.

(Source: [eco.com — Hyperliquid Liquidations & Insurance Fund](https://eco.com/support/en/articles/15247705-hyperliquid-liquidations-explained-margin-calls-and-insurance-fund).) A strategy must not be allowed to "survive" a historical drawdown that would in reality have liquidated it — and, on the winning side, it must model the risk of being *ADL'd out* of a profitable position (§16). See [[hyperliquid-liquidation-engine]] and [[liquidation-cascade-modeling]].

## 12. Stress-test execution assumptions

Run every promising strategy through harsh assumptions and check it still clears:

| Stress test                   | What it catches           |
| ----------------------------- | ------------------------- |
| Double slippage               | Fragile scalping edge     |
| Taker-only execution          | Fake maker alpha          |
| 1–5 second latency            | Unrealistic signal timing |
| Half order-book depth         | Size sensitivity          |
| Worse funding (toward 4% cap) | Carry overfit             |
| Worse fees (worse tier)       | Fee-tier overfit          |
| No fills on some limit orders | Queue-position overfit    |
| ADL on the winning side       | Counterparty/protocol risk |

## 13. Separate entry logic from risk parameters

Overfitting thrives when you optimize entry, exit, stop, take-profit, leverage, sizing, and filters all at once — a bad entry can hide behind perfectly fitted exits. Instead **fix the risk rules first** (e.g. max 1–2× account leverage, fixed risk per trade, fixed max drawdown, conservative slippage), then test whether the entry signal adds value on top. This also keeps the multiple-testing count (§10) tractable.

## 14. Regime-based holdouts

Hyperliquid performance varies sharply by regime. Hold out and test each separately, classifying each bar using the **perpetuals asset-context endpoint**, which exposes mark price (`markPx`), oracle price (`oraclePx`), current funding (`funding`), open interest (`openInterest`), premium (`premium`), and day notional volume (`dayNtlVlm`) (Source: [Hyperliquid Docs — Perpetuals asset context](https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/info-endpoint/perpetuals)):

| Regime             | Tagging field(s)              | Question it answers                |
| ------------------ | ----------------------------- | ---------------------------------- |
| High funding       | `funding` above e.g. 90th pct | Does the strategy depend on carry? |
| Negative funding   | `funding` < 0                 | Does long/short behavior change?   |
| High open interest | `openInterest` above pct band | Does crowding hurt?                |
| Low liquidity      | `dayNtlVlm` below pct band    | Does slippage kill it?             |
| Trending market    | realized return / sign run    | Is there a momentum edge?          |
| Choppy market      | low realized trend, high vol  | Is there a mean-reversion edge?    |

Use *relative* (percentile) thresholds per coin rather than fixed absolute cutoffs, since funding and volume distributions differ enormously across BTC vs a small alt.

## 15. Keep an untouched "live shadow" test

Before trading real size, run the strategy live with no execution or tiny size, and compare reality to the backtest:

| Backtest expectation | Live shadow result |
| -------------------- | ------------------ |
| Fill rate            | Actual fill rate   |
| Slippage             | Actual slippage    |
| Funding cost         | Actual funding     |
| Turnover             | Actual turnover    |
| Drawdown             | Actual drawdown    |
| Signal frequency     | Actual frequency   |

Practical options: run against **Hyperliquid testnet** (real matching engine, no capital risk) to validate fill logic, or run a paper/shadow process against the live mainnet info endpoints with orders logged but not submitted, then reconcile logged intended fills against the actual book that materialized. A strategy that fails immediately in live shadow trading was probably overfit or had unrealistic execution assumptions.

## 16. The October 2025 ADL cascade — a regime break to respect

On **10 October 2025**, Hyperliquid experienced the largest liquidation event of any platform during that crash: roughly **$10.3 billion** in positions liquidated (versus ~$4.6B on Bybit and ~$2.4B on Binance), with about **35,000 ADL events affecting ~20,000 users in 12 minutes** (Source: [BTCC — ADL Controversy](https://www.btcc.com/en-US/square/NodeS4mur4i/1082737)). During the cascade the auto-deleveraging engine **closed roughly $2.1 billion of winning traders' PnL in those 12 minutes, with approximately $653 million representing overshoot** beyond what was strictly needed to cover losses (Source: academic analysis of the event, arXiv 2512.01112v2; see also [SSRN 6636998](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6636998)).

> Note: an early circulating figure put the autodeleveraged winning PnL at ~$705M; the figure cited here ($2.1B PnL closed, ~$653M overshoot) reflects the later quantitative reconstruction and supersedes it.

Why this matters for backtesting:

- **ADL is not symmetric risk you can ignore on the winning side.** Profitable, correctly-positioned traders had positions force-closed. A backtest that assumes a winning position is held to the modeled exit overstates returns during cascades. Model the probability of being ADL'd when you are deep in profit and the opposite side is being liquidated en masse.
- **"Positional blindness."** ADL closes *individual positions* without recognizing a trader's broader hedge. **Delta-neutral traders** (long on Hyperliquid, short elsewhere) had only the Hyperliquid leg force-closed, leaving them suddenly directional and unhedged (Source: [BTCC](https://www.btcc.com/en-US/square/NodeS4mur4i/1082737)). A backtest of a "market-neutral" Hyperliquid strategy that does not model single-leg ADL is overfitting to a hedge that the protocol can unilaterally break.
- **A regime boundary, not just an outlier.** Liquidity recovery after the cascade was two-regime, and **funding compressed** in the aftermath. Treat the pre- and post-October-2025 periods as distinct regimes in walk-forward windows (§2) and regime holdouts (§14); a carry edge fitted on the high-funding pre-event period may simply not exist afterward.

See [[2025-10-crypto-liquidation-cascade]], [[auto-deleveraging]], and [[liquidation-cascade-modeling]].

## Practical Hyperliquid anti-overfit checklist

Before trusting a backtest, require all of these to pass:

- [ ] Profitable after fees, funding (hourly), and slippage
- [ ] Still profitable with 1.5×–2× worse costs and worse fee tier
- [ ] Works out-of-sample, holdout touched exactly once
- [ ] Works across multiple walk-forward time windows (incl. the Oct 2025 break)
- [ ] Works across more than one asset (or has a clear reason not to)
- [ ] Parameter performance forms a plateau (>70–80% of ±10–20% perturbations profitable), not a spike
- [ ] No same-candle lookahead
- [ ] Funding charged hourly at `position_size × oracle_price × funding_rate`, capped at 4%/hour
- [ ] Margin and liquidation simulated against the oracle price; HLP→insurance→ADL waterfall modeled
- [ ] Limit orders include partial-fill and no-fill risk; market orders walk the 20-level book
- [ ] Winning positions model ADL risk; "neutral" strategies model single-leg ADL
- [ ] Deflated Sharpe reported with the number of trials `N`
- [ ] Results not driven by one trade, one day, or one coin
- [ ] Survives a live shadow / testnet reconciliation before real size

## Sources

- User briefing — 15 Hyperliquid-specific anti-overfit techniques with citations (raw: `raw/articles/2026-06-14-overfitting-backtesting-hyperliquid-techniques.md`)
- [Hyperliquid Docs — Funding](https://hyperliquid.gitbook.io/hyperliquid-docs/trading/funding) — hourly funding, `position_size × oracle_price × funding_rate`, premium sampled every 5s, 4%/hour cap, 8h-rate formula
- [Hyperliquid Docs — Fees](https://hyperliquid.gitbook.io/hyperliquid-docs/trading/fees) — rolling 14-day volume, 7 tiers, daily UTC assessment, spot volume double-counts, taker > maker
- [Hyperliquid Docs — Info endpoint](https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/info-endpoint) — `l2Book` (20 levels/side; `px`, `sz`, `n`)
- [Hyperliquid Docs — Perpetuals asset context](https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/info-endpoint/perpetuals) — `markPx`, `oraclePx`, `funding`, `openInterest`, `premium`, `dayNtlVlm` regime-tagging fields
- [Hyperliquid Docs — Contract specifications](https://hyperliquid.gitbook.io/hyperliquid-docs/trading/contract-specifications) — USDC collateral, USDT-denominated quanto contracts
- [Hyperliquid Docs — Margining](https://hyperliquid.gitbook.io/hyperliquid-docs/trading/margining) — cross/isolated margin, liquidation trigger formula
- [Hyperliquid Docs — Liquidations](https://hyperliquid.gitbook.io/hyperliquid-docs/trading/liquidations)
- [Hydromancer — Hyperliquid Historical Data](https://hydromancer.xyz/hyperliquid-historical-data) — `hyperliquid-archive` S3 path format; Reservoir 1-minute snapshots
- [SonarX — Order Book Snapshots release](https://www.sonarx.com/blog/sonarx-releases-hyperliquid-order-book-snapshots) — public S3, 20-level summaries every ~20 blocks
- [eco.com — Hyperliquid Liquidations Explained](https://eco.com/support/en/articles/15247705-hyperliquid-liquidations-explained-margin-calls-and-insurance-fund) — HLP → insurance fund → ADL waterfall
- [Gate Learn — HyperBFT Consensus](https://www.gate.com/learn/course/l1-deep-dives-hyperliquid-hype/hyper-bft-consensus-mechanism) — layer 1, 200k+ TPS, ~0.07s finality
- [BTCC — Hyperliquid ADL Controversy (Oct 2025)](https://www.btcc.com/en-US/square/NodeS4mur4i/1082737) — $10.3B liquidated, 35k ADL events, positional blindness
- [SSRN 6636998 — Two-Regime Liquidity Recovery After the Oct 10 2025 Cascade](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6636998)
- [Bailey & López de Prado — The Deflated Sharpe Ratio (SSRN 2460551, JPM 2014)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2460551)
- [López de Prado — Advances in Financial Machine Learning, Ch.1 (SSRN 3104847)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3104847)
- [Purged cross-validation overview](https://en.wikipedia.org/wiki/Purged_cross-validation) — purge + embargo
- [Towards AI — The Combinatorial Purged Cross-Validation Method](https://towardsai.net/p/l/the-combinatorial-purged-cross-validation-method)
- [QuantInsti — Walk-Forward Optimization](https://blog.quantinsti.com/walk-forward-optimization-introduction/)
- [Blockchain Council — Backtesting AI Crypto Trading Strategies](https://www.blockchain-council.org/cryptocurrency/backtesting-ai-crypto-trading-strategies-avoiding-overfitting-lookahead-bias-data-leakage/)
- [StratBase.ai — Look-Ahead Bias: The Hidden Backtest Killer](https://stratbase.ai/en/blog/look-ahead-bias-hidden-killer) — same-candle bias, 0.5–2% close-to-open gap
- [PickMyTrade — Trading Strategy Validation / Backtest Overfitting](https://blog.pickmytrade.trade/trading-strategy-validation-backtest-overfitting/) — plateau vs cliff
- [Medium (Dolejs) — Intrabar Accuracy Problem](https://medium.com/@kojott/why-your-trading-backtests-might-lying-to-you-the-intrabar-accuracy-problem-68f8b7decdb3) — checking SL/TP against candle high/low
- [Shortform — Advances in Financial Machine Learning summary](https://www.shortform.com/summary/advances-in-financial-machine-learning-summary-marcos-lopez-de-prado)

## Related

- [[crypto-perp-backtesting-pitfalls]] — the venue-generic umbrella catalogue this page specializes
- [[overfitting]] — the failure mode being defended against
- [[overfitting-detection]] — heatmaps, plateaus, and trial-counting in detail
- [[in-sample-vs-out-of-sample]] — chronological split vs walk-forward
- [[walk-forward-analysis]]
- [[purged-kfold-cv]]
- [[cross-validation]]
- [[deflated-sharpe-ratio]]
- [[lookahead-bias]]
- [[point-in-time-data]]
- [[slippage-modeling]]
- [[intrabar-fill-modeling]]
- [[execution-model-differences]]
- [[transaction-cost-modeling]]
- [[liquidation-cascade-modeling]]
- [[curve-fitting]]
- [[selection-bias-research]]
- [[data-snooping-and-p-hacking]]
- [[hyperliquid]]
- [[hyperliquid-funding-rate-microstructure]]
- [[hyperliquid-liquidation-engine]]
- [[hyperliquid-perp-trading-map]]
- [[funding-rate]]
- [[funding-rate-arbitrage]]
- [[auto-deleveraging]]
- [[perpetual-futures]]
- [[2025-10-crypto-liquidation-cascade]]
- [[book-advances-in-financial-machine-learning]]
