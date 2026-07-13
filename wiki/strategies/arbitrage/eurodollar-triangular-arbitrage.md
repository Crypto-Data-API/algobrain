---
title: "Eurodollar Triangular Arbitrage"
type: strategy
created: 2026-04-25
updated: 2026-06-10
status: good
tags: [arbitrage, forex, history, bonds]
aliases: ["Eurodollar Arb", "Offshore-Onshore Triangular", "Eurocurrency Triangular Arbitrage"]
related: ["[[covered-interest-arbitrage]]", "[[triangular-arbitrage]]", "[[carry-trade]]", "[[historical-cable-arbitrage]]"]
strategy_type: quantitative
timeframe: swing
markets: [forex, bonds]
complexity: advanced
backtest_status: retired
edge_source: [structural, informational]
edge_mechanism: "Reg Q ceilings on US onshore deposits + sterling area capital controls created persistent gaps between onshore and offshore USD rates; cross-currency triangles closed only slowly because participants needed branches in 3+ jurisdictions."
data_required: [london-eurodollar-rates, fed-funds, ny-spot-fx, london-spot-fx, central-bank-discount-rates]
min_capital_usd: 1000000
capacity_usd: 1000000000
crowding_risk: medium
expected_sharpe: 1.2
expected_max_drawdown: 0.05
breakeven_cost_bps: 8
decay_evidence: "Reg Q phase-out 1980-1986 + capital-account liberalisation collapsed the original edge; cross-currency basis (post-2008) reopened a related but smaller dislocation."
---

# Eurodollar Triangular Arbitrage

Triangular arbitrage exploiting the persistent gap between onshore US deposit rates (capped by Federal Reserve **Regulation Q** until phased out 1980-1986) and offshore eurodollar deposit rates in London, Zurich, and later Tokyo. Active 1957-1986; foundational to the rise of London as global money-market centre and to Sigmund Warburg's Eurobond invention (1963).

## Edge Source

**Structural** + **informational**. Reg Q capped onshore time-deposit rates at 5.25-5.5% during 1960s; offshore eurodollar deposits faced no cap. UK exchange controls (until 1979) and the Bretton Woods peg created a triangle: USD onshore rate, USD offshore (London) rate, and the GBP-USD forward — which had to satisfy [[covered-interest-arbitrage|covered interest parity]] but often did not.

## Why This Edge Exists

The eurodollar market grew from $1B in 1959 to $500B by 1980. Soviet banks (Moscow Narodny in London) deposited USD outside US jurisdiction. Bank of England encouraged London USD deposits. Until US banks established London branches at scale (mid-1960s), the rate gap was self-sustaining: US banks could not issue offshore deposits, and UK banks faced sterling controls.

When the gap opened, traders with branches in NY, London, and Zurich could lend USD onshore, borrow eurodollars in London, and hedge GBP exposure via forwards — capturing 50-150 bp. Triangular variant: NY-London-Zurich, where Swiss franc forwards were used as the third leg.

## Null Hypothesis

Under no-arbitrage conditions, the offshore-onshore USD gap would equal the cost of capital controls plus cross-currency hedge costs. Empirically (Frenkel-Levich 1977; McKinnon 1977), the gap exceeded these costs by 50-100 bp for years at a time.

## Rules

1. Quote onshore (Fed funds, NY 90-day CD), offshore (LIBOR), and forward FX to a precision of 1 bp.
2. Compute implied cross-rates and the triangle.
3. Open positions only when triangle exceeds 8 bp net of bid-ask, custody, and balance-sheet costs.
4. Hold to maturity (90 days standard) — no mid-term unwind unless cross-currency basis collapses.
5. Reverse the triangle if the gap inverts (rare, but happened during 1973 oil-shock dislocations).

## Implementation Pseudocode

```
for tenor in [30d, 90d, 180d]:
    onshore_usd = fed_cd_rate(tenor)
    offshore_usd = libor(tenor)
    spot_gbpusd = ny_spot()
    fwd_gbpusd = london_fwd(tenor)
    cip_implied = (1 + offshore_usd*tenor/360) * fwd_gbpusd / spot_gbpusd
    if cip_implied < (1 + onshore_usd*tenor/360) - threshold:
        borrow_eurodollar(london, tenor)
        sell_usd_buy_gbp_spot()
        buy_usd_sell_gbp_forward(tenor)
        invest_gbp_uk_money_market(tenor)
```

## Indicators / Data Used

- London eurodollar interbank deposit rates (LIBOR-style reference pricing dates to the 1969 Zombanakis syndicated loans; the BBA formalized LIBOR only in 1986).
- US Fed funds and CD rates.
- London-NY spot FX (post-Bretton Woods, March 1973).
- 30/90/180-day forward FX premia.
- Reg Q ceiling levels.

## Example Trade

**Q3 1969: Fed-funds spike, eurodollar gap closes — but slowly.**

Fed-funds rate hit 9% (Reg Q ceiling 5.25%, so onshore CD outflows). Eurodollar 90-day at 9.6%. Bid-ask ~10 bp each leg.

Trade: borrow $10M in London at 9.6%, swap GBP via 90-day forward, invest GBP in the UK money market (local-authority deposits) at 8.5% with implied USD return 9.7% via CIP. Net spread ~10 bp annualized ≈ $2,500 on $10M per 90-day leg. In the wider-gap episodes documented for 1965-1973 (30-100 bp), the same structure earned $7.5-25K per $10M per quarter; scaled across a $1B balance-sheet allocation and rolled quarterly across tenors and currency triangles, low-single-digit $millions per year per house.

## Performance Characteristics

McKinnon (1977) and Aliber (1973) document persistent gaps of 30-100 bp throughout 1965-1973, narrowing to 10-30 bp by 1978, sub-5 bp by 1985 as Reg Q phased out. Aggregate industry profits at the peak (1973-1976) plausibly ran into the hundreds of millions of dollars per year across the 8-12 banks with full triangle infrastructure (Citibank, Chase, Morgan, Warburg, Schroder, Crédit Suisse, UBS, Mitsubishi) — a rough estimate, since no consolidated P&L was ever published.

## Capacity Limits

Eurodollar market grew from $1B (1959) to $500B (1980). Individual bank limits set by balance-sheet, not by market depth — capacity per house ~$1-10B at peak.

## What Kills This Strategy

- Reg Q phase-out (Depository Institutions Deregulation Act 1980; complete 1986).
- UK exchange-control abolition (October 1979).
- Standardized interbank reference rates (LIBOR-style pricing from 1969, BBA LIBOR from 1986) increased transparency and compressed dealer spreads.
- Currency volatility post-Bretton Woods (March 1973) introduced FX risk that compressed margins.
- Modern echo: post-2008 cross-currency basis blow-out is structurally similar but from regulatory capital costs not Reg Q.

## Kill Criteria

- Triangle inconsistency below 5 bp net.
- Cross-currency basis inverts and persists.

## Advantages

- Persistent edge for 20+ years.
- Highly scalable for major-bank balance sheets.
- Self-hedged FX exposure.

## Disadvantages

- Required global branch infrastructure.
- Regulatory regime changes destroy the edge overnight.
- Counterparty risk (Herstatt 1974).

## Sources

- Catherine R. Schenk, *The Origins of the Eurodollar Market in London: 1955-1963* (Explorations in Economic History, 1998).
- Robert Z. Aliber, *The Interest Rate Parity Theorem: A Reinterpretation* (1973).
- Jacob Frenkel & Richard Levich, *Transaction Costs and Interest Arbitrage* (JPE, 1977).
- Ronald McKinnon, *The Eurocurrency Market* (1977).
- Niall Ferguson, *High Financier* (Warburg biography, 2010).

## Related

[[covered-interest-arbitrage]] · [[triangular-arbitrage]] · [[carry-trade]] · [[historical-cable-arbitrage]] · [[gold-standard-mechanics]] · [[bill-broking-arbitrage]]
