---
title: "External Strategy Sources"
type: concept
created: 2026-09-28
updated: 2026-09-28
status: draft
tags: [strategy-development, methodology, backtesting, free, validation, crypto]
aliases: ["Strategy Idea Sources", "Free Strategy Sources", "Strategy Idea Funnel", "Where to Find Trading Strategies"]
domain: [strategy-development, backtesting]
prerequisites: ["[[edge-taxonomy]]", "[[hypothesis-to-backtest-workflow]]"]
difficulty: intermediate
related: ["[[crypto-idea-generation]]", "[[hypothesis-to-backtest-workflow]]", "[[tradingview-platform]]", "[[pine-script]]", "[[quantconnect]]", "[[quantpedia]]", "[[stonehill-forex]]", "[[nnfx-method]]", "[[repainting]]", "[[overfitting-detection]]", "[[transaction-cost-modeling]]", "[[alpha-decay]]", "[[crypto-forward-testing]]", "[[cryptodataapi-backtesting]]", "[[cryptodataapi-strategy-library]]"]
---

# External Strategy Sources

Four free public libraries between them publish thousands of ready-made trading strategies. They are **[[tradingview-platform|TradingView]] Community Scripts**, **[[stonehill-forex|Stonehill Forex]]** (home of the [[nnfx-method|NNFX method]]), the **[[quantconnect|QuantConnect]] Strategy Library** and **[[quantpedia|Quantpedia]]**. This page treats them as the *input end* of the research pipeline. They supply candidate ideas cheaply, but nearly everything published there fails once fees, full history and out-of-sample testing are applied. The value is in the **funnel**: a fixed, repeatable process that kills most candidates quickly and sends the survivors into [[hypothesis-to-backtest-workflow]].

This complements [[crypto-idea-generation]], which *derives* ideas from crypto market structure. External sources are the other half: *borrowed* ideas, which need extra suspicion because someone chose to publish them.

## The Four Sources

| Source | What you get | Format | Main biases | Best use for crypto |
|---|---|---|---|---|
| [[tradingview-platform\|TradingView Community Scripts]] | 100k+ user-published indicators and strategies | [[pine-script\|Pine Script]], often open source (MPL-2.0) | [[repainting]], zero-commission strategy-tester defaults, curve-fit inputs, popularity ≠ edge | Indicator building blocks; quick visual prototypes on crypto pairs |
| [[stonehill-forex\|Stonehill Forex]] | NNFX framework plus free MT4 indicator library with role-by-role test results | Methodology plus MQL4 indicators | Forex-pair universe, daily-close only, author-run tests | A disciplined *system template* (ATR risk, baseline, confirmation, volume, exit) to slot indicators into |
| [[quantconnect\|QuantConnect Strategy Library]] | Research write-ups with full LEAN (Python/C#) code | Runnable algorithms | Stale backtest windows, survivorship in default universes, optimistic fee models, mostly equities | Code you can port directly onto CryptoDataAPI archive data; FX, futures and crypto entries |
| [[quantpedia\|Quantpedia]] | Encyclopedia of academic anomalies as plain-language rules with the source paper | Text descriptions (premium adds backtests and code) | Pre-cost in-sample returns, post-publication [[alpha-decay\|decay]], heavily equity | Hypotheses *with a named mechanism and a paper*; cryptocurrency, FX, commodity and futures categories |

The sources differ in *where they sit* in the pipeline. Quantpedia supplies a mechanism, which is Stage 1 of [[hypothesis-to-backtest-workflow]]. TradingView and QuantConnect supply code, which is Stage 3. Stonehill supplies a *testing protocol and system skeleton* that applies across all the ideas.

## The Funnel

```
 FIND ──► RESTATE ──► TRANSLATE ──► COST-ON FULL BACKTEST ──► OVERFIT CHECKS ──► FORWARD TEST ──► LIVE
 (source)  (hypothesis)  (Python on       (fees+funding+slippage,     (PBO, DSR, walk-       (paper,       (live-journal)
                          CDA archive)     2020→today, all regimes)    forward, params)        4-12 wks)
  ~100%        ~50%          ~40%                  ~10%                       ~3%                 ~1%
```

The survival percentages are rough attrition targets. They are not measurements: a funnel that passes far more than this is probably not testing hard enough (see [[data-snooping-and-p-hacking]]).

1. **Find.** Pull candidates from a source. Record the source URL, author and publication date. For TradingView, prefer open-source scripts, because you cannot vet a protected script.
2. **Restate as a hypothesis.** Write one sentence: *who is on the other side and why they keep losing* (see [[edge-taxonomy]]). An indicator crossover with no nameable counterparty is a pattern, not an edge. Mark it as `analytical` at best and treat it with extra suspicion.
3. **Translate.** Port the logic to your own backtester and run it on CryptoDataAPI archive data, not on the platform's own tester. Porting forces every rule to be explicit and exposes [[repainting]] or [[lookahead-bias]] hidden in the original. LLMs do this translation well (Pine → Python, LEAN → pandas, prose → rules). Check the output line by line against the original.
4. **Cost-on, full-history backtest.** Include realistic fees, slippage and perp funding ([[transaction-cost-modeling]], [[crypto-perp-backtesting-pitfalls]]). Test on the *full* archive (2020→present at minimum, so it covers the 2021 mania, the 2022 bear, and the 2024-25 ETF regime) and on a survivorship-free universe. A strategy that only works on the pair and window its author showcased is dead at this step.
5. **Overfitting checks.** Count every variant you tried. Report the [[probability-of-backtest-overfitting]] and [[deflated-sharpe-ratio]], run [[walk-forward-analysis]], and check that performance is stable when parameters move ±20%. See [[overfitting-detection]].
6. **Forward test.** Paper trade or run a tiny live pilot for 4-12 weeks, with kill criteria set in advance ([[crypto-forward-testing]], [[when-to-retire-a-strategy]]).
7. **Promote.** Write a full strategy page (`backtest_status` stepping up from `untested` → `cost-corrected` → `paper-traded`) and log it in [[live-journal]].

## Source-Specific Red Flags

- **TradingView:** a strategy that uses `request.security()` on a higher timeframe without `lookahead=barmerge.lookahead_off` or bar-offsetting; `calc_on_every_tick` / intrabar fills; strategy-tester commission left at 0; fewer than ~100 trades; a showcase chart on one hand-picked pair; very high "likes" with no published performance.
- **Stonehill / NNFX:** indicator rankings come from forex majors on daily bars. Crypto's volatility, 24/7 sessions and BTC-beta correlation mean every indicator's *role result* has to be re-tested, not inherited (see [[nnfx-method]]).
- **QuantConnect:** backtest windows often end years ago. Check whether the write-up's universe was selected with hindsight, and whether the fee model matches your venue.
- **Quantpedia:** returns are the source paper's in-sample, pre-cost figures. Published anomalies lose a large share of their return after publication (see [[alpha-decay]]). Equity-only entries are out of scope for this wiki unless they are re-derived for a crypto cross-section.

## Worked Example (Process Only)

A Quantpedia-style "short-term reversal in cryptocurrencies" entry states a mechanism (overreaction by retail flow), a universe (liquid coins) and a rule (buy last week's losers, short the winners). Restated, the counterparty is momentum-chasing retail flow that overshoots, and the edge is `behavioral`. Translated, it becomes weekly cross-sectional ranks on `/api/v1/backtesting/klines`, using a point-in-time top-N universe from `/api/v1/backtesting/daily-snapshots/{date}`. The cost-on test adds taker fees on both legs and perp funding on the shorts. The overfit check tests lookback windows of 3, 5, 7 and 14 days and reports the whole grid, not the best cell. Only then does it earn a strategy page. This example illustrates the funnel. It is not a tested result.

## Getting the Data (CryptoDataAPI)

Every funnel step after "Find" runs on the [[cryptodataapi-backtesting|CryptoDataAPI backtesting archive]] rather than on the source platform's own data or tester:

- **Duplicate check first:** this wiki's own catalogue is queryable via `GET /api/v1/strategies` (317 strategies, 22 groups) and `GET /api/v1/algobrain/search?q=...&type=strategy` ([[cryptodataapi-strategy-library]]). Search it before harvesting a candidate so the funnel doesn't re-derive a strategy the wiki already has. The hosted index lags the repo, so also grep `wiki/strategies/` locally.
- **Historical OHLCV:** `GET /api/v1/backtesting/klines`, for the full-history, cost-on re-test of any ported script
- **Perp carry:** `GET /api/v1/backtesting/funding`, needed to cost any strategy that holds perps across funding windows
- **Point-in-time universe:** `GET /api/v1/backtesting/daily-snapshots/{date}` plus `GET /api/v1/backtesting/symbols`, for survivorship-free cross-sectional tests (the Quantpedia and QuantConnect universes)
- **Bulk research:** `GET /api/v1/backtesting/archives` → `/archives/download`, for Parquet datasets since 2020

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/backtesting/klines?symbol=BTCUSDT&interval=1d"
```

### AI agent workflow

- **Port, then re-test:** have the agent translate the source's Pine or LEAN code to Python, then pull `/api/v1/backtesting/klines` via [[cryptodataapi-mcp]] and re-run it with fees on. Never trust the source platform's equity curve.
- **Universe discipline:** build cross-sectional universes from dated `/api/v1/backtesting/daily-snapshots/{date}`, not from today's top-N, so the port doesn't inherit survivorship bias.
- **Funding in the cost stack:** join `/api/v1/backtesting/funding` onto any perp holding period before reporting a Sharpe.
- **Regime split:** report results separately for the 2021, 2022 and 2024-25 regimes. If an edge only shows up in one, flag it before forward testing.

## Sources

- (Source: [[quantpedia-strategy-encyclopedia]])
- (Source: [[quantconnect-strategy-library]])
- (Source: [[tradingview-community-scripts]])
- (Source: [[stonehill-forex-nnfx]])

## Related

- [[crypto-idea-generation]]: deriving ideas from crypto structure (the complement to borrowed ideas)
- [[hypothesis-to-backtest-workflow]]: where funnel survivors go next
- [[nnfx-method]]: the system template from Stonehill
- [[tradingview-platform]], [[pine-script]], [[quantconnect]], [[quantpedia]], [[stonehill-forex]]
- [[overfitting-detection]], [[data-snooping-and-p-hacking]], [[repainting]], [[alpha-decay]]
- [[crypto-forward-testing]], [[live-journal]]
