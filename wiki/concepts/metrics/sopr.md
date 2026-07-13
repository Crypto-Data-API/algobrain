---
title: "Spent Output Profit Ratio (SOPR)"
type: concept
created: 2026-06-24
updated: 2026-06-24
status: draft
tags: [crypto, bitcoin, indicators, valuation, market-microstructure, behavioral-finance]
aliases: ["SOPR", "Spent Output Profit Ratio", "aSOPR", "Adjusted SOPR", "spent-output-profit-ratio"]
domain: [market-microstructure]
prerequisites: ["[[on-chain-analysis]]", "[[realized-price]]"]
difficulty: intermediate
related: ["[[mvrv]]", "[[mvrv-z-score]]", "[[nupl]]", "[[realized-price]]", "[[on-chain-analysis]]", "[[market-capitalization]]", "[[bitcoin]]", "[[market-cycle]]", "[[hodl-waves]]", "[[exchange-netflow]]", "[[glassnode]]", "[[cryptoquant]]", "[[behavioral-finance]]"]
---

The **Spent Output Profit Ratio (SOPR)** is an [[on-chain-analysis|on-chain]] metric that measures whether coins being spent (moved) on-chain are, on average, changing hands at a **profit or a loss** relative to the price they were last acquired. For each spent output it compares the price at the moment of spending to the price when that coin last moved; aggregated across all spends in a period, SOPR above 1 means the market is realising gains, and below 1 means it is realising losses. It is one of the most-watched [[behavioral-finance|behavioural]] on-chain gauges for [[bitcoin]], popularised on [[glassnode]] and [[cryptoquant]].

## How It Is Computed

```
SOPR (per spent output) = price sold / price paid
                        = USD value when the output is spent / USD value when it was created

SOPR (aggregate) = Σ (USD value spent) / Σ (USD value at creation)   over all spends in the window
```

- **> 1.0** → spent coins are, on aggregate, sold for more than they were acquired — **profit-taking**.
- **= 1.0** → coins are spent at break-even — the market's aggregate realised cost basis.
- **< 1.0** → coins are sold below cost — **loss-realisation / capitulation**.

Where [[realized-price]] measures the cost basis of the *entire* supply, SOPR measures the profit/loss only on the coins that *actually moved* — making it a flow-of-realised-P/L metric rather than a stock-of-unrealised-P/L metric like [[mvrv]] or [[nupl]].

### Key Variants

- **aSOPR (Adjusted SOPR)**: excludes outputs with a lifespan shorter than ~1 hour, filtering out coins that move and return almost immediately (internal transfers, change outputs, exchange shuffling) that would otherwise add noise near 1.0.
- **STH-SOPR / LTH-SOPR**: restricts the calculation to **Short-Term Holders** (coins younger than ~155 days) or **Long-Term Holders** (older), separating the profit-taking behaviour of recent speculators from seasoned holders.

## Interpretation / How Traders Use It

SOPR is read as a real-time gauge of crowd profit-taking versus capitulation across a [[market-cycle]]:

- In **bull markets**, SOPR tends to stay above 1 (holders sell into strength at a profit). A pullback toward 1.0 that *holds* — the so-called **"SOPR reset to 1"** — is read as support: holders refuse to sell at a loss, dips get bought, and the uptrend resumes. A decisive break and sustained close *below* 1 warns the bull structure is weakening.
- In **bear markets**, SOPR tends to stay below 1 (forced/loss selling). A rally back to 1.0 that *fails* is read as resistance: holders who are finally at break-even sell to "get out even," capping the bounce.
- **Deep dips below 1** signal capitulation — heavy loss realisation that has *historically* clustered near cycle lows. **Sustained high readings** signal aggressive profit-taking that can precede local tops.

Because SOPR is a *flow* signal it often turns *before* slower stock metrics, so traders use it to confirm whether the paper profit/loss implied by [[mvrv]] and [[nupl]] is actually being realised, and pair it with [[exchange-netflow]] (are profit-takers sending coins to exchanges?) and [[hodl-waves]] (which age cohort is spending).

## Illustrative Example

During an established [[bitcoin]] uptrend, price dips and aSOPR falls toward 1.0. It touches roughly 1.0 and bounces — a "SOPR reset": holders declined to spend coins at a loss, the level acted as support, and price resumes higher. Months later, in a downtrend, aSOPR repeatedly fails to reclaim 1.0 from below — every relief rally is sold by holders trying to exit near break-even — and the metric finally plunges well under 1.0 as long-term holders capitulate, a loss-realisation flush that historically coincides with bottoming conditions.

## Limitations and Pitfalls

- **Noise near 1.0**: raw SOPR is heavily distorted by internal transfers and change outputs; the adjusted variant **aSOPR** is preferred for cleaner signals. Always check which version a chart shows.
- **Leading but whippy**: as a flow metric SOPR can flip above/below 1 frequently in choppy markets, producing false "reset" signals. It is most reliable when read on smoothed (e.g. moving-average) series and in conjunction with trend context.
- **Entity/exchange adjustments**: custodial reshuffles can register as "spends" at a profit or loss that do not reflect genuine economic selling; entity-adjusted feeds help, but the label layer is provider-produced and revised over time (see [[on-chain-analysis#Leading vs Lagging, and Data Caveats]]).
- **Lost/dormant supply**: coins that never move never contribute to SOPR, so it only describes the *active* float, not the silent majority of long-dormant supply.
- **Cohort matters**: aggregate SOPR can mask divergence — STH-SOPR and LTH-SOPR may point in opposite directions (e.g. new buyers panicking while old holders accumulate). Reading the blended figure alone can mislead.
- **Best for UTXO chains**: cleanest on [[bitcoin]]; account-based chains require approximating the "price paid," adding noise.

## Related

- [[realized-price]] — Supply-wide cost basis; SOPR is its per-spend, flow analogue
- [[mvrv]] — Stock of unrealized profit/loss that SOPR confirms is being realised
- [[nupl]] — Percentage-based unrealized P/L companion
- [[mvrv-z-score]] — Standardised cycle-extreme valuation gauge
- [[on-chain-analysis]] — Parent mechanics page
- [[market-cycle]] — The cycle the "SOPR reset to 1" idea is read against
- [[hodl-waves]] — Which age cohort is spending
- [[exchange-netflow]] — Whether profit-takers are sending coins to exchanges
- [[behavioral-finance]] — The profit-taking/capitulation psychology SOPR captures
- [[glassnode]], [[cryptoquant]] — Providers that popularised the metric

## Sources

General market knowledge; no specific wiki source ingested yet.
