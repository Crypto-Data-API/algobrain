---
title: "Dollar Carry Trade"
type: strategy
created: 2026-09-28
updated: 2026-09-28
status: draft
tags: [forex, macro, interest-rates, position-trading, quantitative, monetary-policy]
aliases: ["USD carry timing", "Dollar carry", "Lustig-Roussanov-Verdelhan dollar trade", "Quantpedia #0129"]
strategy_type: quantitative
timeframe: position
markets: [forex]
complexity: intermediate
backtest_status: untested
edge_source: [risk-bearing]
edge_mechanism: "When US short rates sit above the average developed-market rate (measured by the basket's forward discount), investors are paid to hold USD against the basket; when they sit below, they are paid to be short USD. The premium compensates US-specific and global risk that is countercyclical — it is highest precisely when US growth weakens and rates fall — and the counterparty is the USD hedger/borrower who pays for dollar funding or dollar protection."
data_required: [fx-forwards-monthly, interest-rates]
min_capital_usd: 50000
capacity_usd: 1000000000
crowding_risk: medium
expected_sharpe: 0.35  # prior only; source Sharpe 0.66 (1983-2009)
expected_max_drawdown: 0.30
breakeven_cost_bps: 100
decay_evidence: "Lustig, Roussanov & Verdelhan sample ends 2009; the 2009-2015 ZIRP era compressed forward discounts to near zero, weakening the signal. No post-2009 evidence harvested."
kill_criteria: |
  - rolling 5-year net Sharpe < 0
  - drawdown > 30%
  - average forward discount within ±25 bps of US T-bill for 12 months (no signal)
related: ["[[quantpedia]]", "[[quantpedia-strategy-encyclopedia]]", "[[carry-trade]]", "[[carry-anomaly]]", "[[currency-value-ppp]]", "[[currency-momentum]]", "[[dxy]]", "[[us-dollar]]", "[[yen-carry-trade]]", "[[covered-interest-arbitrage]]"]
---

# Dollar Carry Trade

A single-signal FX timing strategy: go long the US dollar against an equal-weight basket of ten developed currencies when the 3-month US Treasury rate exceeds the basket's average forward discount, and short the dollar when it is below; rebalance monthly. Unlike the cross-sectional [[carry-trade]], this trades only the dollar factor. Harvested from [[quantpedia|Quantpedia]] #0129, summarising Lustig, Roussanov & Verdelhan, "Countercyclical Currency Risk Premia" (Source: [[quantpedia-strategy-encyclopedia]]).

## Edge Source

**Risk-bearing** ([[edge-taxonomy]]). The dollar risk premium compensates for US-specific and global risk that peaks in US downturns — when rates fall and the forward discount turns against the dollar (Source: [[quantpedia-strategy-encyclopedia]]).

## Why This Edge Exists

Under [[covered-interest-arbitrage|covered interest parity]], the basket's average forward discount equals the average rate gap vs the US. Uncovered interest parity says the spot rate should move to offset it; empirically it does not, so the rate gap is (partly) earned. LRV find the average forward discount and US industrial-production growth forecast up to 25% of dollar return variation. The counterparty is whoever needs USD funding or protection and pays the carry.

## Null Hypothesis

If uncovered interest parity held, the expected return of long-USD when US rates are higher would be zero (the dollar would depreciate by the rate gap) and the strategy would lose forward-point spreads and roll costs of a few bps per month.

## Rules

- **Basket:** EUR, AUD, CAD, DKK, JPY, NZD, NOK, SEK, CHF, GBP, equal-weight.
- **Signal:** average 1-month forward discount of the basket vs the 3-month US T-bill.
- **Position:** T-bill > average forward discount → long USD / short basket; otherwise short USD / long basket.
- **Rebalance:** monthly, via 1-month forwards.
- **Sizing:** fixed notional, or volatility-targeted to ~8% annualised.

## Implementation Pseudocode

```python
# Dollar carry — illustrative only
basket = ["EUR","AUD","CAD","DKK","JPY","NZD","NOK","SEK","CHF","GBP"]
for month_end in calendar:
    fwd_disc = mean(forward_discount_1m(c) for c in basket)   # annualised
    usd_long = tbill_3m() > fwd_disc
    sign = +1 if usd_long else -1
    set_forwards({c: -sign / len(basket) for c in basket})    # short basket if USD long
```

## Indicators / Data Used

- 1-month FX forward points for the basket; 3-month US T-bill.
- Context: [[dxy]], [[us-dollar]], [[monetary-policy]] cycle.

## Example Trade

Illustrative: in a Fed hiking cycle the T-bill is 5.3% and the basket's average forward discount implies 3.5%. Signal: long USD vs the basket. The position earns roughly the 1.8% rate gap annualised plus or minus spot moves. When the Fed cuts below peers, the signal flips to short USD.

## Performance Characteristics

- **Source claim (1983-2009, pre-cost):** 5.6% annual return, 8.5% volatility, Sharpe 0.66, max drawdown −31.7% (Source: [[quantpedia-strategy-encyclopedia]]).
- **Cost overlay:** one monthly forward roll on 10 majors — a few bps; costs are negligible relative to the premium. Decay and regime (ZIRP) are the real risks.
- Sign flips are infrequent; the strategy is effectively a slow-moving USD regime call.

## Capacity Limits

Effectively unbounded at wiki scale — G10 forwards.

## What Kills This Strategy

- **Zero-rate regimes** — forward discounts collapse to noise.
- **Dollar-funding crises** (2008, March 2020) — USD spikes regardless of rate differential; short-USD positions are hurt precisely when risk is highest.
- **Policy convergence** among central banks. See [[failure-modes]].

## Kill Criteria

- Rolling 5-year net Sharpe < 0.
- Drawdown > 30%.
- Signal magnitude < 25 bps for 12 months.

## Advantages

- One transparent, economically motivated signal.
- Very cheap to run; high capacity.
- Dollar regime output is directly useful as a crypto macro overlay.

## Disadvantages

- Modest Sharpe; long flat or losing stretches.
- Exposed to dollar-funding squeezes.
- Old sample; post-2009 evidence not harvested.

## Crypto relevance

The strategy's output — "is the market being paid to be long or short USD?" — is a compact dollar-regime flag. Dollar strength and tightening USD funding have historically coincided with crypto drawdowns, and USD-rate carry sets the opportunity cost for stablecoin holders (see [[stablecoin-yield]] and [[risk-on-risk-off-framework]]). Perp [[funding-rate]] carry is the crypto-native analogue of FX carry.

## Variant / External Source: QuantConnect

[[quantconnect|QuantConnect]]'s Strategy Library has a simpler open-code relative, "Forex Carry Trade". It goes long the highest-rate currency and short the lowest-rate one, rebalancing monthly. That is a cross-sectional carry trade, not this page's dollar-level signal, so it works as a contrast, not a replication. It also uses LEAN's default Forex model, which charges no fees, so its results are gross of spreads. See also [[carry-trade]] and [[fx-skewness-risk-premia]] (Source: [[quantconnect-strategy-library]]).

## Sources

- (Source: [[quantpedia-strategy-encyclopedia]]) — Quantpedia #0129; primary paper Lustig, Roussanov & Verdelhan, "Countercyclical Currency Risk Premia".

## Getting the Data (CryptoDataAPI)

CryptoDataAPI does not serve FX forwards. `GET /api/v1/sentiment/macro` gives current EUR/USD and yields for a live dollar backdrop; forward points and T-bill history must come from a macro data vendor. See [[cryptodataapi-sentiment]].

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/sentiment/macro"
```

### AI agent workflow

- **Dollar backdrop** — sample `GET /api/v1/sentiment/macro` daily and log yield/EUR-USD changes alongside the monthly dollar-carry signal computed from external forward data
- **Crypto overlay** — when the signal is long-USD and yields are rising, reduce crypto beta; confirm with `GET /api/v1/regimes/current`
- **Carry comparison** — compare USD T-bill carry against perp carry from `GET /api/v1/derivatives/funding-rates?coin=BTC` to judge whether basis trades beat cash
- Run via [[cryptodataapi-mcp]]

## Related

- [[carry-trade]] · [[carry-anomaly]] · [[currency-value-ppp]] · [[currency-momentum]] · [[yen-carry-trade]] · [[dxy]] · [[quantpedia]]
