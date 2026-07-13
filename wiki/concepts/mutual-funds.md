---
title: "Mutual Funds"
type: concept
created: 2026-04-15
updated: 2026-06-11
status: good
tags: [portfolio-theory, valuation, stocks, education]
aliases: ["Mutual Fund", "Open-End Fund", "Open-End Investment Company", "Managed Fund"]
domain: [portfolio-theory, valuation]
prerequisites: ["[[nav]]", "[[diversification]]"]
difficulty: beginner
related: ["[[etf]]", "[[etfs]]", "[[index-fund]]", "[[nav]]", "[[passive-investing]]", "[[diversification]]", "[[hedge-fund]]", "[[expense-ratio]]", "[[dollar-cost-averaging]]"]
---

A **mutual fund** is a pooled investment vehicle that collects money from many investors and invests it in a portfolio of securities — stocks, bonds, money-market instruments, or a mix — managed by a professional portfolio manager. Investors buy and sell shares directly with the fund (not on an exchange) at the fund's [[nav|net asset value]], which is struck once per day after the market closes. Mutual funds are the dominant retail savings vehicle in most developed markets and a major structural force in equity flows.

## Overview

Mutual funds are "open-end" funds: the fund continuously issues new shares when investors buy in and redeems shares when investors sell, so the share count expands and contracts with demand. This is the key structural difference from a [[closed-end-fund|closed-end fund]] (fixed share count, trades at a premium/discount on an exchange) and from an [[etf]] (creation/redemption happens through authorized participants in large blocks, and retail trades intraday on-exchange).

Because all buys and sells transact at the same end-of-day [[nav]], there is no intraday price and no bid-ask spread for the investor — but also no ability to trade during the session or to use limit/stop orders.

### Types

| Type | Holdings | Typical use |
|---|---|---|
| Equity funds | Stocks (growth, value, sector, regional) | Long-term capital growth |
| Bond / fixed-income funds | Government and corporate debt | Income, lower volatility |
| Money-market funds | Short-term high-quality debt | Cash management, near-cash yield |
| Balanced / target-date funds | Mix of stocks and bonds | One-decision retirement saving |
| Index funds | Track a benchmark passively | Low-cost market exposure (see [[index-fund]]) |

### Active vs passive

Most assets historically sat in **actively managed** funds, where a manager picks securities aiming to beat a benchmark. The long-run evidence (e.g. the S&P SPIVA scorecards) shows the large majority of active equity managers underperform their benchmark over 10–15 years after fees — the central argument for low-cost [[index-fund|index funds]] and [[passive-investing|passive investing]].

## Cost structure

Costs are the single most reliable predictor of net returns:

- **Expense ratio** — annual management + operating cost as a percentage of assets (see [[expense-ratio]]). Active funds often charge 0.5–1.5%; index funds can be under 0.10%.
- **Load fees** — sales commissions charged on purchase (front-end load) or sale (back-end load). "No-load" funds avoid these.
- **12b-1 fees** (US) — distribution/marketing fees bundled into the expense ratio.
- **Trading costs and tax drag** — turnover inside the fund generates transaction costs and, in taxable accounts, capital-gains distributions the investor cannot control.

## Trading relevance

Mutual funds matter to traders less as instruments and more as **flow drivers and structural features**:

- **End-of-day flow.** Mutual fund inflows/outflows are processed at the close, contributing to the documented concentration of volume and price pressure in the closing auction (see [[market-on-close]] dynamics).
- **Forced selling.** Open-end funds must meet redemptions by selling holdings. In stress, redemption waves force selling regardless of price — a mechanism behind liquidity spirals (see [[liquidity]], [[fire-sale]]). The 2020 bond-fund stress and the broader [[2020-03-bond-etf-dislocation|March 2020 dislocation]] highlighted this fragility in less-liquid asset classes.
- **Window dressing.** Funds reporting holdings at quarter-end can buy winners and sell losers near the reporting date, a recurring calendar effect.
- **Closet indexing.** Many "active" funds hold portfolios close to their benchmark while charging active fees — a structural inefficiency value-aware allocators screen for.
- **ETF substitution.** For most retail exposures, [[etf|ETFs]] now offer the same or better diversification with intraday liquidity, lower cost, and (in the US) greater tax efficiency via in-kind redemption — the main reason mutual-fund market share has eroded.

## Mutual funds vs ETFs

| Dimension | Mutual fund | ETF |
|---|---|---|
| Pricing | Once daily at [[nav]] | Continuous intraday |
| Trading venue | Direct with fund | Exchange |
| Minimums | Often a dollar minimum | One share |
| Tax efficiency (US) | Lower (cap-gains distributions) | Higher (in-kind redemption) |
| Order types | None (NAV only) | Limit, stop, etc. |
| Intraday liquidity | No | Yes |

## Related

- [[etf]] — the intraday-traded, lower-cost alternative
- [[etfs]] — ETF overview
- [[index-fund]] — passive low-cost fund design
- [[nav]] — how mutual fund shares are priced
- [[passive-investing]] — the broader low-cost strategy
- [[diversification]] — the core benefit of pooling
- [[hedge-fund]] — the lightly-regulated, performance-fee counterpart
- [[expense-ratio]] — the dominant cost metric

## Sources

- U.S. Securities and Exchange Commission, *Investor Bulletin: Mutual Funds and ETFs — A Guide for Investors*
- Investment Company Institute (ICI), *Investment Company Fact Book* (annual)
- S&P Dow Jones Indices, *SPIVA U.S. Scorecard* (active vs passive performance)
- William F. Sharpe, "The Arithmetic of Active Management" (1991)
