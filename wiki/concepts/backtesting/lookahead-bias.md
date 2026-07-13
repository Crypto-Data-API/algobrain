---
title: "Lookahead Bias"
type: concept
created: 2026-04-10
updated: 2026-07-13
status: excellent
tags: [backtesting, bias, methodology, validation]
aliases: ["Look-Ahead Bias", "Look Ahead Bias", "Future Leakage", "Information Leakage"]
domain: [backtesting]
difficulty: intermediate
related: ["[[backtesting-overview]]", "[[backtesting]]", "[[survivorship-bias]]", "[[selection-bias-research]]", "[[data-snooping-and-p-hacking]]", "[[purged-kfold-cv]]", "[[overfitting-detection]]", "[[data-sources-overview]]", "[[point-in-time-data]]", "[[walk-forward-analysis]]", "[[pybroker]]", "[[cryptodataapi]]"]
---

# Lookahead Bias

The use of information in a backtest that was not actually available at the decision time. The most insidious source of false-positive backtest results, because it can produce dramatic edge from data that has been corrupted in subtle ways. A single bar of leakage can turn a Sharpe of 0 into a Sharpe of 3.

## The Core Problem

A trading strategy must use only information that exists *strictly before* the trade decision. If the strategy at time t uses any data point that wasn't yet known at time t, the backtest is testing a model that could not have been built in real time. The result is meaningless.

This sounds obvious. In practice, lookahead leaks into research in dozens of subtle ways, most of which look completely innocuous until you spot them.

### Lookahead vs. its cousins

Lookahead bias is one member of a family of backtest-corrupting biases. It is worth fixing the boundaries precisely, because the defenses differ:

| Bias | What leaks | Direction in time | Primary defense |
|------|-----------|-------------------|-----------------|
| **Lookahead bias** | A specific *future data point* used in a past decision | Future → past | [[point-in-time-data\|Point-in-time data]], explicit bar offsets |
| [[survivorship-bias\|Survivorship bias]] | The *universe* excludes failed/delisted names | Selection on outcome | Point-in-time membership history |
| [[selection-bias-research\|Selection bias]] | The *strategy* was chosen after seeing results | Researcher → backtest | Held-out data, pre-registration |
| [[data-snooping-and-p-hacking\|Data snooping / p-hacking]] | Many trials, only the winner reported | Multiple-testing | [[deflated-sharpe-ratio\|Deflated Sharpe]], trial accounting |
| Sample-period bias | The window flatters the strategy | Window choice | Multiple windows, regime stratification |

Lookahead is the most mechanical of these — it is a property of the *code and data plumbing*, not of researcher judgment — which is why it is both the most preventable and the most embarrassingly common.

## The Common Sources

### 1. Restated / Revised Fundamentals

You download Compustat or Yahoo Finance fundamentals for AAPL going back to 2010. The numbers you get are the *current* version of those numbers — including any restatements, accounting adjustments, or reclassifications applied after the fact.

In real time on March 15, 2014, you would have seen the Q4 2013 numbers as originally reported. If they were later restated, the version in your dataset is the restated version, which reflects information that was not yet known on March 15, 2014.

**Defense:** Use point-in-time fundamental data. Vendors that provide this: Compustat Point-in-Time, S&P Capital IQ Point-in-Time, FactSet, Refinitiv. Free sources almost never provide it.

### 2. Filing Date vs. Period End Date

A company's fiscal Q4 might end December 31 but the 10-K isn't filed until March. If you align your fundamental data by *period end date*, you're assuming the market knew the December 31 numbers on December 31 — which it didn't. The market only knew them at the filing date in March.

**Defense:** Align by filing date, not period end date. For datasets that only have period end, add a conservative lag (45-90 days for annuals, 30-60 days for quarterlies).

### 3. Same-Bar Decision and Execution

A strategy that "buys at today's close when today's close is above the 20-day moving average" has a subtle issue: the 20-day MA includes today's close, which is the same bar you're trading on. By the time today's close is observable, the day is over and you can't trade.

**Defense:** Either compute the signal on bar t-1 and trade on bar t, or compute the signal on bar t and trade on the open of bar t+1. Be explicit in code about which bar's data is used for the signal and which for execution.

### 4. Macro Data Revisions

GDP, CPI, employment, industrial production — almost every macroeconomic series is revised after first release. The version in FRED today is the *latest* revision, which differs from what was actually reported on the original release date.

CPI revisions can change inflation prints by 20-50 basis points. Employment numbers get revised by 50-100k jobs. A strategy that trades macro releases using the *revised* number is using information that didn't exist at the time of trade.

**Defense:** Use the ALFRED database (Archival FRED), which provides vintage data — the value of each series as it was originally reported on each release date. Or use the BEA / BLS first-print archives directly.

### 5. Index Constituent Lookahead

Backtesting a long-only S&P 500 strategy using "the current S&P 500" as the universe is biased: any company that was in the S&P 500 historically but isn't today is excluded, and any company in the S&P 500 today but wasn't historically is included where it shouldn't be.

The combined effect is large: bankrupt companies are removed from the universe (a form of [[survivorship-bias]]) and high-performing recent additions are added retroactively (a form of lookahead).

**Defense:** Use a point-in-time index membership history. CRSP and Compustat both provide this. The universe at each date should be the actual constituents on that date.

### 6. Forward-Filled Data

A common backtest trick: forward-fill missing values in a feature so the model always has something. This is innocuous *if* the missing data was missing in real time too. It is lookahead if the data was filled in after the fact.

Worse: some data providers forward-fill in their delivered data, then patch in actual values later. If you cache the data once and then re-pull it, the new pull may have different (less-leaky) values than the old one.

**Defense:** Track data vintages. Always know whether your features are "as observed at the time" or "as known today."

### 7. Tomorrow's Open in Today's Strategy

Easy bug: indexing past the end of an array. A sloppy line of code that grabs `prices[i+1]` when computing the signal at bar `i` makes the strategy clairvoyant. Any backtest where the result is suspiciously good — Sharpe > 3, win rate > 80% — should be checked for off-by-one errors.

**Defense:** Run the strategy on shuffled data; if it still produces positive results, you have a leak.

### 8. Survivorship-Adjusted Volatility / Beta Estimates

Beta of a stock relative to "the market" is usually computed using market index data. If the market index itself is survivorship-biased (e.g., the current S&P 500), then your historical betas inherit the bias.

**Defense:** Use a survivorship-free benchmark or an index whose composition is point-in-time accurate.

### 9. Fundamental Data with Implicit Lookback

Some derived fundamental fields (e.g., trailing twelve month earnings) require multiple periods to compute. If you only have one period of recent data, the earlier periods may be filled in from a later vintage. The "TTM EPS" field at time t may secretly include restated data for the four trailing quarters.

**Defense:** Compute derived fields yourself from primary data, using point-in-time vintage for each component.

### 10. Earnings Estimates "As Of"

Analyst estimate datasets (IBES, Refinitiv) often timestamp estimates by the date they were *added to the database*, not the date they were *publicly knowable*. The lag can be days to weeks.

**Defense:** Use vendors that explicitly tag estimate timestamps with broker release date.

## Source Taxonomy at a Glance

The ten sources above cluster into three mechanisms. Knowing the mechanism tells you where to look:

| Mechanism | Sources | Tell-tale symptom | Canonical fix |
|-----------|---------|-------------------|---------------|
| **Data revised after the fact** | Restated fundamentals, macro revisions, forward-fill, TTM lookback, IBES "as of" | Re-pulling the dataset changes historical values | Vintage / [[point-in-time-data\|point-in-time]] data; track data vintages |
| **Timestamp / alignment error** | Filing-date vs period-end, same-bar execution, tomorrow's-open bug | Suspiciously high Sharpe; result collapses on a 1-bar shift | Align by *availability* date; explicit signal/execution bar offsets |
| **Universe / benchmark leakage** | Index constituent lookahead, survivorship-adjusted beta | Edge concentrated in names that later became famous | Point-in-time index membership; survivorship-free benchmark |

The single most valuable habit is to attach an **as-of timestamp** to every data point and assert, at the line of consumption, that `as_of < decision_time`. Frameworks that enforce this structurally — e.g., [[pybroker]]'s temporal windowing and [[purged-kfold-cv|purged, embargoed CV]] — remove an entire class of these bugs by construction. See [[event-driven-backtesting]] for why event-driven engines are less leak-prone than naive vectorized ones.

## A Diagnostic Test

If you suspect lookahead, run this test:

1. Take your backtest
2. Shift all input features forward by one bar (so today's signal is computed from yesterday's features and yesterday's features only)
3. Re-run

If the strategy's Sharpe drops sharply (more than ~30%), you had lookahead. The shifted version is the honest version.

A more aggressive test: shift features forward by 5 bars. Real strategies should degrade smoothly with longer shifts (because their signal is real but stale). Lookahead-based strategies often collapse to near-zero immediately because the lookahead is concentrated at the boundary.

## Detecting Lookahead in Code

Code-level red flags to grep for:

- `shift(-1)` — almost always wrong; shift forward, not backward
- `iloc[i+1]` or `loc[date+1]` — same thing
- `fillna(method='bfill')` — backfill is lookahead by definition
- `expanding().mean()` followed by use at the same index — fine
- `expanding().mean()` followed by use at an earlier index — lookahead
- `df.merge(..., how='left')` where the right-hand df is timestamped later than the join key — possible leakage

A code review checklist for any backtest: at every line where data is consumed by the model, ask "what is the latest timestamp on this data point, and is it strictly less than the decision time?"

## Why Lookahead Looks So Good

Lookahead bias is dangerous specifically because it produces *plausible-looking* results. A strategy with 5% lookahead might have:
- Sharpe 1.5 (looks good)
- 60% win rate (plausible)
- 15% max drawdown (reasonable)
- Smooth equity curve (suspicious only in retrospect)

Whereas a strategy with 100% lookahead has:
- Sharpe 8.0 (obviously fake)
- 95% win rate (impossible)
- 2% max drawdown (impossible)
- Straight-line equity curve (clearly broken)

The first kind is the more dangerous one because it doesn't trip your "this looks too good" alarm. It just looks like an OK strategy. You deploy it, it loses money, and you never know whether it died because of regime change or because you were trading on data that didn't exist.

## How Bad Is It in Practice?

In most quant research labs, the first attempt at any new dataset has lookahead bias somewhere. The second attempt usually still has it but in a subtler place. By the third or fourth careful pass, most leakage is removed but small amounts persist. The discipline is recognizing this is normal and budgeting time for the leak hunt.

A reasonable rule: any new strategy that achieves Sharpe > 2 in early development should be assumed to have lookahead bias until proven otherwise. The proof is the diagnostic test above.

## Worked Example (Qualitative): The Earnings-Surprise Trap

Consider a simple-sounding strategy: "buy a stock the day before it reports earnings if trailing-twelve-month EPS growth is accelerating, and the consensus estimate has been revised up in the last month."

Three lookahead leaks hide inside this one sentence:

1. **TTM EPS** (source #9). If the dataset's TTM field is built from a *current* vintage, the four trailing quarters may include restatements applied after the original earnings date. The "acceleration" the model sees was not visible the day before the report.
2. **"Consensus estimate revised up"** (source #10). If estimates are timestamped by *database-add* date rather than *broker-release* date, an upward revision that the database recorded on Monday may actually have been published the following Thursday — after the trade.
3. **The report itself** (source #3 / #7). If the alignment code accidentally keys the feature row to the *report* date rather than the *pre-report* date, the model is effectively reading the earnings result before trading on it. Win rates above 80% on this strategy almost always trace to this off-by-one.

The diagnostic: shift all features back one trading day and re-run. If the edge survives a one-day shift but dies at a five-day shift, the signal is real but stale (acceptable). If it dies immediately on the one-day shift, the P&L was living on the boundary — i.e., it was lookahead. This is exactly the smooth-vs-collapse degradation pattern described in [[walk-forward-analysis|walk-forward]] hygiene.

## Prevention Checklist

A practical pre-deployment checklist, ordered from cheapest to most thorough:

| # | Check | Catches |
|---|-------|---------|
| 1 | Grep for `shift(-1)`, `iloc[i+1]`, `bfill`, `fillna(method='bfill')` | Mechanical off-by-one and backfill |
| 2 | Assert every consumed feature has `as_of < decision_time` | Timestamp/alignment errors |
| 3 | One-bar feature shift; compare Sharpe | Boundary-concentrated leakage |
| 4 | Five-bar feature shift; check for smooth decay | Distinguishes stale-but-real from leaked |
| 5 | Re-pull the dataset; diff historical values | Silent data revision / forward-fill |
| 6 | Use point-in-time universe + fundamentals | Survivorship and restatement leakage |
| 7 | Run on shuffled (returns-randomized) data | Any residual clairvoyance |
| 8 | Cross-check Sharpe > 2 results against a second, independent code path | Implementation-specific bugs |

No single check is sufficient. The discipline is treating leak-hunting as a standing budget line in every research project, not a one-time gate.

## Sources

- [[book-advances-in-financial-machine-learning]] — López de Prado on the full taxonomy of leakage
- [[book-quantitative-trading-ernest-chan]] — Chan on practical lookahead detection
- [[book-evidence-based-technical-analysis]] — Aronson on data integrity for TA research

## Getting the Data (CryptoDataAPI)

**Historical archive:**
- `GET /api/v1/backtesting/klines` — OHLCV candle archive
- `GET /api/v1/backtesting/funding` — funding-rate archive
- `GET /api/v1/backtesting/liquidations` — liquidation records archive
- `GET /api/v1/backtesting/daily-snapshots/{date}` — point-in-time daily snapshot
- `GET /api/v1/backtesting/archives` — Parquet dataset archive (since 2020)

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/backtesting/symbols"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-backtesting]].

## Related

- [[backtesting-overview]] — parent overview of backtesting hygiene
- [[backtesting]] — the broader practice this bias corrupts
- [[survivorship-bias]] — sibling universe-selection bias
- [[selection-bias-research]] — researcher-side bias
- [[data-snooping-and-p-hacking]] — multiple-testing cousin
- [[overfitting-detection]] — detecting tuned-to-the-past results
- [[purged-kfold-cv]] — leak-free cross-validation
- [[point-in-time-data]] — the canonical defense against revised-data leakage
- [[walk-forward-analysis]] — validation framework where the shift-test lives
- [[pybroker]] — backtesting framework that prevents leakage structurally
- [[event-driven-backtesting]] — engine design that resists same-bar leakage
- [[hypothesis-to-backtest-workflow]] — where leak-hunting fits in the research loop
