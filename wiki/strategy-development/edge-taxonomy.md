---
title: "Edge Taxonomy"
type: concept
created: 2026-04-10
updated: 2026-04-13
status: excellent
tags: [strategy-development, edge, alpha, market-microstructure, behavioral-finance, risk-premia]
aliases: ["Sources of Edge", "Where Alpha Comes From", "Six Sources of Edge"]
domain: [strategy-development]
difficulty: intermediate
related: ["[[strategy-development-overview]]", "[[research-checklist]]", "[[failure-modes]]", "[[anomalies-overview]]", "[[reflexivity]]", "[[volatility-risk-premium]]", "[[carry-anomaly]]", "[[when-to-retire-a-strategy]]", "[[strategy-correlation-matrix]]"]
---

# Edge Taxonomy

A trading strategy without an articulated source of edge is, with very high probability, an overfit backtest. Every strategy you build should map to at least one of the six categories below. If you cannot answer "why does this work, and who is on the other side of my trade?" — stop and do not deploy capital.

The first five categories describe *alpha* — returns from exploiting an inefficiency. The sixth — risk-bearing — describes *risk premia* — returns earned as compensation for holding risks that others refuse to bear. Both are legitimate sources of strategy returns, but they differ in mechanism, persistence, and failure mode. Understanding which type you are harvesting determines how you size, hedge, and retire the strategy.

## The Six Categories

### 1. Structural Edge

Returns from being on the right side of a forced flow. Someone *has to* trade, regardless of price, and you provide the liquidity (or front-run the flow).

Examples:
- **Index rebalancing** — when a stock is added to the S&P 500, index funds *must* buy it. See [[index-arbitrage]].
- **ETF creation/redemption** — authorized participants forced to deliver baskets. See [[etf-arbitrage]].
- **Margin liquidations** — leveraged longs forced out at predictable price levels. See [[liquidation]], [[stop-hunting-and-liquidity-sweeps]].
- **Quarter-end rebalancing** — pension funds forced to sell winners and buy losers to maintain target weights. See [[expiration-and-rebalancing-flows]].
- **Convertible bond issuance** — convert arb desks forced to short the underlying. See [[convertible-arbitrage]].
- **Dividend capture / ex-div mechanics** — see [[dividend-capture]], [[dividend-arbitrage]].

**Who is on the other side?** A non-discretionary participant: a passive fund, a broker hedging client flow, a leveraged trader getting margin-called. They lose by design; you collect the premium for warehousing risk or providing liquidity.

**Why it persists:** the forced participant cannot stop trading even when the trade is bad for them. Mandate beats P&L.

**How it dies:** the mandate changes (e.g., S&P removes the cliff effect of additions) or the forced flow becomes too predictable and gets fully arbitraged.

### 2. Behavioral Edge

Returns from systematic human cognitive biases. Market participants overreact, anchor, herd, and avoid losses irrationally — and these biases produce price patterns that mean-revert or extend predictably.

Examples:
- **Post-earnings drift** — investors underreact to earnings surprises; price drifts in the direction of the surprise for 60+ days. See [[earnings-momentum]], [[post-earnings-announcement-drift]].
- **Momentum** — winners keep winning because investors anchor to old prices and underreact to new information. See [[momentum-anomaly]].
- **Lottery preference / low-vol anomaly** — investors overpay for high-volatility "lottery ticket" stocks, leaving low-vol stocks underpriced. See [[low-volatility-anomaly]].
- **Disposition effect** — traders sell winners too early and ride losers too long, creating persistent mean-reversion in losers. See [[prospect-theory]].
- **Narrative-driven crashes** — fear cascades produce overshoots. See [[contrarian-extremes]], [[reflexivity]].

**Who is on the other side?** Retail and emotional institutional traders. Behavioral edges work because human psychology is stable and slow to change.

**Why it persists:** biases are wired in. Even traders who *know* about loss aversion still feel it. Knowledge is not enough to overcome reflex.

**How it dies:** when the bias becomes so well-known that *systematic* traders crowd it out faster than retail can supply it. Momentum and value have both decayed in this way over the past two decades.

### 3. Informational Edge

Returns from having or processing information faster or more completely than the rest of the market.

Examples:
- **Alternative data** — satellite imagery of parking lots, credit card transactions, web scraping of job postings, app download counts. See [[alternative-data-alpha]], [[alternative-data]].
- **Expert networks** — paying domain experts for ground-truth before it shows up in financial reports.
- **Faster news parsing** — NLP on SEC filings, earnings calls, central bank statements, social media.
- **Order flow / footprint analysis** — reading the tape to infer institutional positioning. See [[footprint-charts]], [[order-flow-scalping]], [[tape-reading]].
- **On-chain analytics** — wallet tracking, exchange flows, whale movements. See [[smart-money-orderflow-combo]].

**Who is on the other side?** Slower or less-informed participants. Often retail; sometimes institutions that haven't invested in the data infrastructure.

**Why it persists:** the data is expensive to source, clean, and process. Most participants will not pay the fixed cost.

**How it dies:** the data becomes commoditized, the cost drops, and everyone has it. Satellite parking-lot counts were a real edge in 2014; by 2020 they were priced in within hours.

### 4. Analytical Edge

Returns from having a better *model* of the same data everyone else has. The information is public; your interpretation is sharper.

Examples:
- **Better volatility surfaces** — superior options pricing models. See [[volatility-arbitrage]], [[dispersion-trading]].
- **Better correlation forecasting** — cleaner cointegration estimates for [[pairs-trading]] and [[statistical-arbitrage]].
- **Better regime detection** — knowing which model to use when. See [[regime-detection]], [[regime-adaptive-strategy]].
- **Better factor models** — proprietary risk decomposition that lets you isolate alpha from beta. See [[factor-investing]], [[long-short-equity]].
- **Better term-structure models** — for [[yield-curve-trading]], [[carry-trade]].

**Who is on the other side?** Participants using cruder models — usually because they're optimizing for simplicity, speed, or interpretability rather than accuracy.

**Why it persists:** model improvements require deep technical skill. Most participants are not quants, and most quants are doing the same thing as each other.

**How it dies:** the better model becomes standard (e.g., Black-Scholes was an edge in 1973, table stakes by 1985), or the underlying assumptions break (LTCM, see [[ltcm|LTCM's collapse]]).

### 5. Latency Edge

Returns from acting faster than other participants on the same opportunity.

Examples:
- **HFT market making** — quoting both sides faster than the next-fastest quoter. See [[market-making-strategy]].
- **Latency arbitrage** — exploiting price differences between venues before they sync. See [[latency-arbitrage]], [[cross-exchange-arbitrage]].
- **MEV** — reordering transactions in a blockchain mempool. See [[mev-strategies]], [[liquidity-sniping]].
- **News-driven** — reacting to a CPI print or central bank statement microseconds before slower participants.

**Who is on the other side?** Slower participants, or liquidity takers who don't know they're paying a microstructure tax.

**Why it persists:** the technology arms race is expensive and the winner-take-all dynamic means only a handful of firms can afford to compete at the top.

**How it dies:** new venue rules (speed bumps, batch auctions, IEX-style delays), or being out-spent by a faster competitor.

### 6. Risk-Bearing Edge

Returns from accepting risks that other market participants are unwilling or unable to hold. Unlike the other five categories — which exploit *inefficiencies* — risk-bearing earns a premium precisely *because* markets are working correctly: you are being compensated for providing a service (absorbing tail risk, supplying liquidity during stress, warehousing illiquid positions).

Examples:
- **Volatility risk premium (VRP)** — selling options or variance swaps to harvest the persistent gap between implied and realized volatility. Buyers overpay for protection because they value the *utility* of insurance, not just the expected payout. See [[volatility-risk-premium]], [[volatility-arbitrage]].
- **Carry** — going long high-yield assets and short low-yield assets across currencies, bonds, or funding rates. Returns compensate for crash risk and funding fragility. See [[carry-anomaly]], [[carry-trade]], [[funding-rate-arbitrage]].
- **Liquidity provision during stress** — buying assets when forced sellers dump them (fire sales, margin cascades, fund redemptions). You earn a premium for being the only buyer when liquidity disappears. See [[contrarian-extremes]], [[liquidation]].
- **Credit risk premium** — holding corporate bonds or selling CDS to earn spread over risk-free rates. You are paid for bearing default risk. See [[credit-spread]].
- **Insurance selling** — strategies that earn steady premiums but face occasional large losses (e.g., selling tail puts, writing earthquake reinsurance). See [[tail-risk]].

**Who is on the other side?** Risk-averse participants who would rather pay a premium than bear the risk themselves. This includes hedgers (portfolio managers buying puts), regulated institutions (banks required to hold high-quality assets), and anyone with a shorter time horizon or lower risk tolerance than you.

**Why it persists:** risk-bearing premiums are *not* anomalies — they are compensation for real economic risk. They persist because the demand for risk transfer is structural: as long as people need insurance, someone must supply it. Unlike alpha, risk premia do not decay from crowding (though the premium can compress).

**How it dies:** you blow up. Risk-bearing strategies fail not from edge decay but from *tail realization* — the event you were being paid to absorb actually happens. [[ltcm|LTCM's collapse]] is the canonical example: the convergence and carry trades were sound, but leverage turned a tail event into an existential loss. Risk-bearing edges also fail when the premium compresses below the level that compensates for the true tail risk (which happened to short-vol strategies before Feb 2018).

> **Key distinction:** the other five categories produce *alpha* — returns that should not exist if markets were perfectly efficient. Risk-bearing produces *premia* — returns that *should* exist because someone must be compensated for holding risk. This distinction matters for portfolio construction: alpha and premia are somewhat uncorrelated, so holding both improves your Sharpe ratio. It also matters for sizing: alpha strategies should be sized by conviction, risk-bearing strategies by how much tail loss you can survive.

## Combining Edges

The strongest strategies combine *multiple* edge categories. Examples:

- **Index reconstitution arbitrage** = structural (forced flows) + analytical (predicting which stocks will be added)
- **Earnings drift trading** = behavioral (underreaction) + informational (faster parsing of the call)
- **Pairs trading** = analytical (cointegration) + behavioral (mean-reversion in correlated names)
- **Funding rate arbitrage** = structural (perp mechanics) + latency (rate update timing)
- **Systematic carry + vol selling** = risk-bearing (premium harvesting) + analytical (better tail-risk models to size the position correctly)
- **Distressed debt** = risk-bearing (illiquidity premium) + informational (deep fundamental research on recovery values)
- **Fire-sale buying during liquidation cascades** = risk-bearing (liquidity provision) + structural (forced sellers)

A strategy that maps to two or more categories is more robust because both would have to fail simultaneously for the edge to die. Combining an alpha source with a risk premium is especially powerful: the alpha provides timing, and the premium provides baseline compensation even when the alpha signal is flat.

## Red Flags

Be very skeptical of any strategy where the answer to "why does this work?" is one of:

- **"The backtest is good"** — that's a result, not a cause. Backtests are biased estimators.
- **"Technical analysis says so"** — TA *describes* price patterns; it doesn't explain why they should persist. A pattern needs an underlying behavioral or structural cause to be tradeable.
- **"The market is inefficient"** — too vague. *How* is it inefficient, and *who* is making the inefficiency happen?
- **"AI/ML found it"** — a model trained on history will always find patterns. The question is whether they generalize.

If you can't identify which of the six categories your edge belongs to, you almost certainly don't have an edge.

## Edge Decay Patterns

Not all edges decay the same way. Understanding the decay mechanism helps you monitor for early signs of death.

| Category | Primary Decay Mechanism | Decay Speed | Early Warning Signs |
|----------|------------------------|-------------|---------------------|
| **Structural** | Mandate or market-structure change | Slow (years) | Rule changes announced; forced flow becomes predictable enough to fully arbitrage |
| **Behavioral** | Crowding by systematic traders | Medium (5-15 years) | Falling Sharpe, rising AUM in the factor, academic publication wave |
| **Informational** | Data commoditization | Fast (2-5 years) | Data vendors multiply; data cost drops; signal decays within days instead of weeks |
| **Analytical** | Model becomes standard practice | Medium-slow (5-20 years) | Open-source implementations; industry adoption; convergence of pricing across desks |
| **Latency** | Technology arms race | Very fast (months-years) | Competitor upgrades; venue rule changes (speed bumps, batch auctions) |
| **Risk-Bearing** | Premium compression or tail realization | Variable | VRP narrows to historical lows; crowding into short-vol; leverage creep in your own book |

The general pattern: **informational and latency edges decay fastest** because they depend on being first, and being first is a temporary advantage. **Structural and risk-bearing edges decay slowest** because they depend on institutional mandates and risk aversion, which change slowly. **Behavioral edges** sit in the middle — human biases are permanent, but systematic exploitation of them can crowd out the premium.

See [[failure-modes]] for what happens when edge decay goes undetected, and [[when-to-retire-a-strategy]] for the kill criteria.

## How to Use This Page

When reviewing or building any strategy in this wiki:

1. Open the strategy page
2. Identify which edge category (or categories) it belongs to
3. Add `edge_source: [behavioral, structural, informational, analytical, latency, risk-bearing]` to the frontmatter (one or more)
4. If you can't identify any category — flag the page as `status: review` and dig deeper

Over time, the wiki should have a clean Dataview query that lists every strategy by edge source, making it easy to diversify across edge types.

```dataview
TABLE edge_source AS "Edge Source", backtest_status AS "Status", expected_sharpe AS "Sharpe"
FROM "wiki/strategies"
WHERE edge_source
SORT edge_source ASC
```

## Sources

- [[book-quantitative-trading-ernest-chan]] — Chan on classifying edges before backtesting
- [[book-advances-in-financial-machine-learning]] — López de Prado on the difference between *finding* a pattern and *understanding* one
- [[book-active-portfolio-management]] — Grinold & Kahn on the fundamental law of active management (alpha = skill × breadth)
- Antti Ilmanen, *Expected Returns* (2011) — the definitive reference on risk premia vs. alpha, and why risk-bearing is a distinct return source

## Related

- [[strategy-development-overview]]
- [[research-checklist]]
- [[failure-modes]]
- [[anomalies-overview]]
- [[reflexivity]]
- [[volatility-risk-premium]] — canonical risk-bearing edge
- [[carry-anomaly]] — structural + risk-bearing
- [[strategy-correlation-matrix]] — strategies sharing an edge source tend to correlate
- [[when-to-retire-a-strategy]] — kill criteria when edges decay
- [[ltcm]] — the definitive risk-bearing blowup
