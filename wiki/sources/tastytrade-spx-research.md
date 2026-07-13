---
title: "Tastytrade SPX Research"
type: source
created: 2026-05-07
updated: 2026-06-12
status: good
tags: [options, sp500, indicators, derivatives, volatility, backtesting, education]
aliases: ["Tastytrade SPX Research", "Tastylive SPX Studies", "Tastytrade SPX Mechanics"]
related: ["[[tastytrade]]", "[[tastytrade-mechanics]]", "[[tom-sosnoff]]", "[[spx-options]]", "[[index-options]]", "[[short-strangle]]", "[[iron-condor]]", "[[managing-winners]]", "[[implied-volatility-rank]]", "[[volatility-risk-premium]]", "[[volatility-skew]]", "[[zero-dte-options]]", "[[theta-targeting]]", "[[options-premium-selling]]", "[[itpm-options-portfolio-management]]"]
source_type: video
source_url: "https://www.tastylive.com/shows/market-measures"
source_author: "Tastylive / Tastytrade Research"
source_date: 2024-01-01
source_file: "n/a — published research from a regulated education business; cross-referenced rather than archived as raw"
confidence: medium
claims_count: 12
---

This page is a synthesised summary of **tastytrade's published SPX-options research** — the body of empirical work produced by tastylive (the educational arm of [[tastytrade|tastytrade]], founded by [[tom-sosnoff|Tom Sosnoff]]) since roughly 2013. It covers their canonical findings on [[short-strangle|short strangles]], [[iron-condor|iron condors]], and [[zero-dte-options|0DTE]] strategies on [[spx-options|SPX]], all derived from systematic backtests presented on the *Market Measures* show, the *Options Jive* show, and various tastylive YouTube and blog publications. This is **not** a single primary source but a compilation; individual claims are tagged with confidence levels.

## Core Doctrine

The "Tastytrade Mechanics" doctrine (also covered in [[tastytrade-mechanics]]) is the rule-set tastylive consistently advocates across its programming:

- **Sell premium when IV rank is elevated** (IVR > 30, ideally > 50)
- **Use index options for tax efficiency and liquidity** (SPX preferred over SPY for taxable accounts)
- **Target 45 DTE at entry** for the optimal trade-off of premium collected vs gamma risk
- **Take profit at 50% of max profit** (the "[[managing-winners]]" rule)
- **Set max loss at 2x credit received** for naked short premium
- **Keep position size small** — 1-3% buying power reduction per trade

The research backing each of these rules is the focus of this page.

## Key Empirical Claims

### Claim 1: 45 DTE is the optimal entry tenor for SPX strangles [HIGH]

Multiple tastytrade studies (cited across *Market Measures* episodes 2014-2022) compared 30-, 45-, and 60-day SPX strangles on a backtest from 2005 onward. The 45 DTE entry consistently produced:

- Higher Sharpe than 30 DTE (gamma risk too high at 30 DTE, theta extraction too compressed)
- Higher Sharpe than 60 DTE (vega exposure too large, capital deployed too long per trade)
- Faster cycling than longer tenors → more compounding opportunities per year

The 45 DTE rule is the most thoroughly tested element of the tastytrade doctrine and is where their published Sharpe figures (1.2-1.5 in calm regimes) come from.

### Claim 2: 50% profit-take maximises Sharpe vs hold-to-expiration [HIGH]

The "[[managing-winners]]" doctrine — close strangles when 50% of max profit has been captured rather than holding to expiration — is supported by tastytrade backtests showing:

- ~10-20% improvement in win rate (from ~70% hold-to-expiry to ~85-90% with 50% profit-take)
- Faster cycle time → more trades per year
- Lower variance of returns
- Slight reduction in average trade P&L (you give up the last 50% of premium) but improved Sharpe overall

This finding is widely accepted and has been replicated in academic and third-party backtests with similar conclusions.

### Claim 3: 16-delta strangles outperform 30-delta on Sharpe [MEDIUM]

Tastytrade has published several studies comparing strangle entry deltas:

- **30-delta strangles**: higher gross premium, higher win rate per trade, but bigger losses in tail events; Sharpe ~0.8-1.0 net of costs
- **16-delta strangles**: lower gross premium, but the wider strikes are touched less often, producing lower variance and higher Sharpe of ~1.2-1.5 in calm regimes
- **10-delta strangles**: even lower variance but premium too small to compensate for capital tied up; Sharpe drops back to ~0.7-0.9

The 16-delta sweet spot is widely cited. **Caveat**: this is a Sharpe optimisation. On *raw return* the 30-delta wins because higher premium dominates in calm years, and the 16-delta's outperformance comes mostly from avoiding the worst losses in tail years. Investors with stronger drawdown tolerance can rationally choose 30-delta despite the Sharpe deficit.

### Claim 4: IV rank > 30 is a meaningful entry filter [HIGH]

Studies show that selling SPX strangles when IV rank exceeds 30 produces materially better risk-adjusted returns than indiscriminate entry. The mechanism: IV rank is a noisy proxy for the [[volatility-risk-premium|VRP]] — when realised vol has been low and IV is at the higher end of its 52-week range, IV is overpricing forward realised vol on average. Without the IV rank filter, the strategy ends up selling at structurally low premiums and getting tagged in normal moves.

The threshold of 30 is somewhat arbitrary; thresholds of 40 or 50 produce slightly better Sharpe but fewer trades. The trade-off is degrees-of-freedom (more trades = more diversification across regimes) vs entry quality.

### Claim 5: Iron condors underperform strangles on undefined Sharpe [MEDIUM]

When tastytrade compares strangles to iron condors (the same strangle with protective wings):

- Iron condors have lower max loss per trade
- Iron condors have lower Sharpe than strangles in calm regimes (the wings cost more than the tail-risk reduction is worth in a benign environment)
- Iron condors have *better* risk-adjusted returns in stress regimes (the wings actually fire)

The implication: traders without portfolio margin and without the capacity to absorb full strangle losses should use iron condors despite the Sharpe deficit; traders with portfolio margin and book-level hedges can use strangles. This nuance is sometimes lost in the simpler "sell strangles" presentation.

### Claim 6: Reality during shocks contradicts the calm-regime Sharpe [HIGH]

The most important caveat — and one tastytrade has acknowledged in subsequent research — is that the published Sharpe figures of 1.2-1.5 are *conditional on calm regimes*. In stress events:

- 2018 Volmageddon (February 5): SPX strangle programs took 6-12 months of premium back in a single day
- March 2020 COVID crash: similar magnitude losses for many systematic strangle programs
- 2022 bear market: chronic drag on strangle programs from elevated realised vol

The realised long-run Sharpe of mechanical SPX strangle programs across 2010-2024 is closer to 0.6-0.9 once tail events are included — substantially below the calm-regime figure. This is a well-known criticism of the tastytrade approach and the central reason ITPM-style methodology insists on a long-vol overlay (see [[itpm-options-portfolio-management]]).

### Claim 7: 0DTE strategies require different rules [MEDIUM]

Post-2022 tastytrade has produced extensive 0DTE-specific research:

- The 50% profit-take rule does *not* transfer well to 0DTE — gamma too high, time too short for the rule to fire reliably
- 0DTE iron condors have higher win rate but smaller trade R/R
- 0DTE works best with intraday entry (e.g., 10am-noon) and intraday exit
- IV-rank filters are less useful for 0DTE because intraday IV is not the same construct as 30-day IV rank

See [[zero-dte-options]] and [[0dte-impact-on-spx]] for the broader market-microstructure context.

### Claim 8: Strangles outperform straddles on Sharpe [HIGH]

A simple but important finding: at-the-money straddles capture more theta but expose to gamma at the strike, while 16-delta strangles trade some theta for materially less gamma. Strangles win on Sharpe, straddles win on raw return, and the gap widens in choppy markets. See [[straddle-vs-strangle]] for the full comparison.

### Claim 9: Section 1256 tax efficiency makes SPX dominant for taxable accounts [HIGH]

Cross-referencing with [[section-1256-contracts]]: SPX options receive 60/40 tax treatment regardless of holding period. For an active SPX strangle program in the top US tax bracket, the after-tax Sharpe is materially higher than the equivalent SPY strangle program (which is taxed as standard short-term capital gains at much higher marginal rates).

### Claim 10: Diversification across expirations is essential [HIGH]

The "rolling 45 DTE" approach implicitly creates expiration diversification — at any point the book has positions at varying DTE. Concentrating on a single expiration (e.g., always entering on the first of the month for the next-month expiry) creates expiration-cliff risk that can wipe out years of gains. The mechanical 45 DTE approach with weekly entries naturally addresses this.

### Claim 11: Position sizing is the dominant determinant of long-run survival [HIGH]

Tastytrade research repeatedly emphasises that strategy selection (strangle vs condor, 16-delta vs 30-delta) matters less than position sizing. A 16-delta strangle program sized at 5% BPR per trade fails in 2018; the same program sized at 1% BPR per trade survives. This is the most consistent message across the tastytrade education library and is broadly aligned with ITPM's emphasis on capital preservation.

### Claim 12: Realized volatility is what matters; implied is just the entry price [MEDIUM]

A more philosophical claim consistent across tastytrade content: traders should monitor realised vol behaviour over the life of trades, not just the implied vol at entry. A strangle entered at high IV is in trouble if realised vol spikes; the IV rank entry filter doesn't help once the trade is on. Active management based on realised path is what tastytrade emphasises.

## Tastytrade Research vs Reality

The published Sharpe figures (1.2-1.5) come from periods that were *predominantly* calm, with brief shock events. Three caveats are widely accepted in the academic and practitioner community:

1. **Survivorship in the tasty backtests** — backtests have implicitly survived through the worst regimes; real-time deployment exposes the trader to "the next" regime, which may be worse.
2. **Position-sizing assumptions** — backtests often use simplified position sizing that real-world margin calls and broker risk-rules would interfere with.
3. **Cost assumptions** — slippage on the wings of strangles in stress events is much worse than backtests model.

These are not critiques of tastytrade specifically; they apply to any premium-selling backtest. The honest framing is that tastytrade's research is genuine and the 45 DTE / 50% profit-take cycle is a real and durable rule-set, but the achieved Sharpe in real-time over a multi-decade horizon is lower than the calm-regime backtest suggests, and the realised drawdown profile is fatter-tailed than the Sharpe figure implies.

## Confidence Summary

| Claim | Confidence |
|---|---|
| 45 DTE optimal entry | HIGH |
| 50% profit-take improves Sharpe | HIGH |
| 16-delta beats 30-delta on Sharpe | MEDIUM |
| IV rank > 30 is meaningful entry filter | HIGH |
| Iron condor underperforms strangle on Sharpe in calm | MEDIUM |
| Reality during shocks contradicts calm-Sharpe | HIGH |
| 0DTE requires different rules | MEDIUM |
| Strangles beat straddles on Sharpe | HIGH |
| Section 1256 dominance for SPX | HIGH |
| Expiration diversification matters | HIGH |
| Position sizing is dominant | HIGH |
| Realised vol matters, not just implied | MEDIUM |

## Related

- [[tastytrade-mechanics]] — the rule-set page with the doctrine spelled out
- [[tastytrade]] — the company and platform
- [[tom-sosnoff]] — founder and the doctrine's primary spokesperson
- [[short-strangle]], [[iron-condor]] — the canonical structures
- [[managing-winners]] — the 50% profit-take rule
- [[spx-options]], [[index-options]] — the preferred underlyings
- [[implied-volatility-rank]] — the entry filter
- [[volatility-risk-premium]] — the structural source of the income
- [[volatility-skew]] — affects strangle pricing
- [[zero-dte-options]], [[0dte-impact-on-spx]] — the modern variant
- [[itpm-options-portfolio-management]] — the contrasting institutional approach with explicit hedge layer
- [[long-vol-vs-short-vol]] — broader philosophical context

## Sources

- tastylive *Market Measures* show — multiple episodes 2013-2024 (tastylive.com).
- tastylive *Options Jive* show — multiple episodes on 0DTE and strangle research.
- tastytrade YouTube channel — video research library.
- tastytrade.com blog and education portal — written research summaries.
- *Mechanics* and *Best Practices* documents from tastytrade education.
- Sosnoff, Tom — multiple interview appearances discussing the underlying philosophy.
- Cross-referenced academic and third-party replication studies of the 45 DTE / 50% profit-take cycle.
