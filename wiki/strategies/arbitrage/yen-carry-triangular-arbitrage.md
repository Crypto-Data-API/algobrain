---
title: "Yen Carry Triangular Arbitrage"
type: strategy
created: 2026-04-25
updated: 2026-06-21
status: excellent
tags: [arbitrage, forex, position-trading]
aliases: ["JPY Carry Triangle", "Yen-Dollar-AUD Triangle", "Mrs. Watanabe Trade"]
related: ["[[carry-trade]]", "[[covered-interest-arbitrage]]", "[[triangular-arbitrage]]", "[[crisis-currency-triangular-arbitrage]]"]
strategy_type: hybrid
timeframe: position
markets: [forex, bonds]
complexity: intermediate
backtest_status: live
edge_source: [structural, risk-bearing]
edge_mechanism: "Persistent Japanese real-rate gap (zero/negative for 25+ years vs ~3-5% in higher-yield economies) keeps the JPY-USD-AUD/NZD/MXN/TRY triangle open. CIP holds in theory; cross-currency basis violates it post-2008 by 20-80 bp."
data_required: [jpy-spot, jpy-forwards, target-currency-rates, cross-currency-basis, fx-implied-vol]
min_capital_usd: 1000
capacity_usd: 1000000000000
crowding_risk: high
expected_sharpe: 0.4
expected_max_drawdown: 0.4
breakeven_cost_bps: 12
decay_evidence: "Crowding-driven crashes: Aug 16 2007, Oct 24 2008, Aug 5 2024 Japan crash (Nikkei -12%, JPY +5%). Returns persist between crashes due to real-rate gap."
---

# Yen Carry Triangular Arbitrage

The largest persistent FX carry trade in history: borrow Japanese yen at near-zero rates, swap into a high-yield currency (USD, AUD, NZD, MXN, TRY, BRL, ZAR), invest in that currency's money market or bonds, hedge the FX leg via forwards. The "triangle" makes explicit the three legs — JPY interest cost, target-currency yield, and FX hedge — and isolates the cross-currency basis as the residual profit/loss after CIP. It combines two well-studied strategies: the [[carry-trade]] (earn the rate differential) and [[triangular-arbitrage]] / [[covered-interest-arbitrage]] (close the loop across three prices and isolate the CIP residual). See also [[crisis-currency-triangular-arbitrage]] for the stress-regime variant.

> **The hedged/unhedged distinction is the whole point.** Run *unhedged*, this is a directional FX bet whose return is a risk premium for bearing crash risk — the "Mrs. Watanabe" trade. Run *fully forward-hedged*, [[covered-interest-arbitrage|CIP]] gives back almost the entire rate gap and the only true arbitrage residual left is the **cross-currency basis** (~20–80 bp post-2008). Most real books sit between the two with partial hedge ratios. Conflating the two is the single biggest analytical error in this trade: the headline "5% carry" is mostly unhedged FX risk premium, not arbitrage.

Estimated outstanding notional $1-4 trillion across institutional and retail (Mrs. Watanabe in Japan, Toshin investment trusts).

| Leg | Instrument | Sign of P&L |
|---|---|---|
| 1. Funding | Borrow JPY at TONA / OIS | Cost (small, near-zero historically) |
| 2. Investment | Buy target-currency T-bill / money market | Income (the rate gap's gross source) |
| 3. FX hedge | Sell target → JPY forward (or run unhedged) | Hedged: gives back ~the rate gap, leaves the basis. Unhedged: full FX P&L |
| Residual (hedged) | Cross-currency basis | The true arbitrage profit, ~20–80 bp |

## Edge Source

Two of the five categories in [[edge-taxonomy]]:

- **Structural** — Japan's policy rate sat at or below zero from 1999 to March 2024 while comparable economies cycled through 2-5%+ regimes; the rate gap is a policy artifact, not a market inefficiency that arbitrage can close. Post-2008 bank-regulation costs additionally keep the cross-currency basis (a CIP violation) persistently open at 20-80 bp.
- **Risk-bearing** — the unhedged carry return is compensation for bearing crash risk: the trade earns steadily and then loses 15-30% in days when risk-off events force synchronized unwinds (1998, 2007, 2008, 2015, 2024). Whoever holds the position through the tail is the insurer; the premium is the carry.

| Edge dimension | Present? | Mechanism |
|---|---|---|
| Structural | Primary | Decades-long policy rate gap (BoJ ≤ 0% 1999–2024) + post-2008 bank balance-sheet costs keeping the cross-currency basis open |
| Risk-bearing | Primary | Carry is compensation for bearing synchronized crash risk; the holder is selling disaster insurance |
| Analytical | Secondary | Hedge-ratio choice, basis pricing, and carry-to-risk timing add value |
| Informational | Weak | CFTC IMM / BIS positioning gives a read on crowding, not a price edge |
| Behavioral | Weak | Retail (Mrs. Watanabe) reliably over-supplies the unhedged side, chasing yield |
| Latency | No | Position horizon (1m–6m rolls); not a speed game |

## Why This Edge Exists

BoJ kept the policy rate near zero from 1999 to 2024. Yen-denominated savers in Japan (households + Government Pension Investment Fund + Norinchukin Bank etc.) need yield. Foreign borrowers want cheap funding. Banks intermediate, charging the cross-currency basis — a regulatory-capital-cost spread of 20-80 bp persistent post-2008.

CIP says: forward = spot × (1 + r_USD) / (1 + r_JPY). In practice forward prices are *cheaper* than CIP implies (USD trades at a forward premium narrower than rate differential), meaning the synthetic USD funding via JPY swap is cheaper than direct USD borrow. This is the cross-currency basis — the modern echo of [[eurodollar-triangular-arbitrage]].

## Null Hypothesis

Under perfect CIP, the three legs net to exactly zero. Empirically (Du-Tepper-Verdelhan 2018) the basis on USD/JPY 5y averaged -50 bp 2010-2018, peaking -100 bp in 2016 — a free 50-100 bp annual carry for those with balance-sheet to provide synthetic USD.

## Rules

1. Borrow JPY at TONA / OIS rate.
2. Spot-convert JPY → target (USD, AUD, MXN).
3. Invest in target-currency short-duration sovereign or money market.
4. Sell forward target → JPY at the forward rate.
5. Hold to forward expiry (1m, 3m, 6m), roll.
6. Tail-hedge via OTM JPY calls / EM currency puts.

### Position sizing
7. Cap leverage so a 1998/2008/2024-scale JPY spike (8-12% in days) cannot breach the 25% drawdown kill criterion — in practice ≤2.5x on the FX-hedged triangle, and materially less (≤1x) if the FX leg is run unhedged for the rate-gap carry.

### Exit
8. Unwind when the real-rate gap compresses below ~200 bp, when the basis falls below round-trip costs (~12 bp), or when tail-hedge cost exceeds expected carry for the tenor.

## Implementation Pseudocode

```python
funding_jpy = tona_rate(tenor)  # ~0.05-0.4%
target_yield = us_t_bill(tenor)  # ~5%
fx_spot = usdjpy_spot
fx_fwd = usdjpy_forward(tenor)
cip_implied_fwd = fx_spot * (1 + funding_jpy * tenor/360) / (1 + target_yield * tenor/360)
basis = (fx_fwd - cip_implied_fwd) / fx_spot

if basis > 12bp + tail_premium:
    borrow_jpy(notional)
    swap_to_usd(notional, fx_spot)
    invest_us_tbills(notional, tenor)
    sell_usd_buy_jpy_forward(tenor)
    # P&L = target_yield - funding_jpy - implied_fx_loss + basis
```

## Indicators / Data Used

- TONA / OIS yen funding curve.
- Cross-currency basis swap quotes.
- BIS triennial FX survey on carry-trade positioning.
- CFTC IMM positioning (JPY net short = carry-trade indicator).
- Vol-adjusted carry-to-risk ratio.

## Example Trade

**Late March 2024: late-cycle yen carry.**

Borrow ¥1B at TONA ~0.08% (just after the BoJ's 19 March 2024 exit from negative rates). Convert to ~$6.6M at USD/JPY ≈151. Buy 3-month T-bills yielding ~5.4%. Two variants:

- **Unhedged ("Mrs. Watanabe" version):** earn the full ~5.3% annualized rate gap — roughly $87,000 per quarter on the position — but carry the entire FX risk. This is the version that was destroyed four months later.
- **Fully forward-hedged (the true triangle):** under CIP the 3-month forward (~149) gives back essentially the whole rate gap; the residual profit is the **cross-currency basis**, ~30-50 bp annualized depending on Japanese bank balance-sheet pressure — small, but close to riskless for institutions with the balance sheet to run it at scale.

The popular "carry trade" P&L is therefore mostly *unhedged FX risk premium*, while the genuine arbitrage component is the basis. Most real books run somewhere in between (partial hedge ratios, tail options).

**July-August 2024 — the crash.** BoJ hiked to 0.25% on 31 July 2024; soft US payrolls on 2 August triggered a dovish Fed repricing. USD/JPY fell from ~153.5 to an intraday low near 141.7 on 5 August (~8% in under a week, from ~162 in early July). Unhedged retail positions were wiped out; institutional carry funds drew down 8-15% in 3 days; the Nikkei fell 12.4% on 5 August 2024 — its worst day since October 1987.

## Performance Characteristics

Long-sample academic estimates (Koijen, Moskowitz, Pedersen & Vrugt, *Carry*, JFE 2018) plus realized episodes through 2024:
- Mean carry-to-risk Sharpe ~0.3-0.6 net of costs.
- ~3-5 fat-tailed drawdowns of 15-30% per decade (1998 ruble; Aug 2007 quant crisis; Oct 2008 Lehman; Aug 2015 China devaluation; Aug 2024 BoJ hike).
- Long-run return 4-7% APR with 8-12% vol — Sharpe drops to 0.3-0.4 once tail crashes included.

> **Execution note.** Because the trade is a triangle, the order in which the three legs are put on matters — see [[execution-sequencing]]. Spot, the money-market investment, and the forward should be locked close to simultaneously so the basis you measured is the basis you capture; legging in slowly exposes the book to FX drift between legs. For the basis-harvesting (hedged) version this leg risk, not the rate gap, is the dominant short-horizon P&L driver.

> **Data disclaimer.** Sharpe and return ranges above blend academic estimates (Koijen et al. 2018; Du-Tepper-Verdelhan 2018) with realized episodes; they are not a wiki-verified backtest of a specific book. The crash magnitudes are observed market moves, not strategy-level P&L.

## Capacity Limits

Total outstanding ~$1-4T. Effectively limitless for institutional sizes; market-impact dominates only for daily flows >$10B.

## What Kills This Strategy

- **BoJ policy normalization:** the rate gap is the engine; hikes (started cautiously 2024) shrink it and can trigger the unwind.
- **Risk-off shocks:** correlations break the wrong way — the target currency falls *and* JPY rallies, so both legs lose simultaneously.
- **Cross-currency basis collapse:** would mechanically close the triangle but also compress the only true-arbitrage profit for the hedged version.
- **Crowding-driven cascade:** when positioning is extreme, an unwind becomes self-reinforcing (margin calls force more selling), producing the violent gaps the strategy is famous for.

| Crash | Date | Trigger | Approx. JPY/risk move |
|---|---|---|---|
| LTCM / ruble | Aug–Oct 1998 | Russia default, LTCM unwind | JPY spiked sharply vs USD in days |
| Quant crisis | 16 Aug 2007 | Cross-asset deleveraging | Carry pairs gapped, synchronized unwind |
| Lehman | 24 Oct 2008 | GFC risk-off | Carry currencies collapsed vs JPY |
| China devaluation | Aug 2015 | CNY devaluation shock | Carry unwind, JPY rally |
| BoJ-hike crash | 5 Aug 2024 | BoJ hike (31 Jul) + soft US payrolls | USD/JPY ~153.5 → ~141.7 (~8% in days); Nikkei −12.4% |

## Kill Criteria

- Real-rate gap < 200 bp (the engine is fading).
- Cumulative drawdown > 25% of allocated capital.
- Implied vol > 20% on USDJPY 1m (crowded-unwind warning).
- Cross-currency basis falls below round-trip costs (~12 bp) for the hedged book.
- CFTC IMM / BIS positioning at crowding extremes while carry-to-risk is poor → de-gross.

## Advantages

- 25+ years of persistent edge rooted in a durable policy rate gap.
- Immense capacity — institutional sizes face market impact only on daily flows > ~$10B.
- Multiple legs offer flexibility: currency choice, tenor, and hedge ratio can be tuned to the regime.
- The hedged version isolates a near-riskless basis carry for balance-sheet-rich institutions.

## Disadvantages

- Crashes are violent and synchronized across *all* carry pairs — diversification across target currencies fails exactly when needed.
- Crowded trade; Aug 2024 demonstrated ~7–8% one-day moves that wiped out unhedged retail.
- Highly correlated to the global risk-on regime — it is short volatility / short disaster insurance.
- Negative [[skewness]]: steady carry punctuated by rare, large losses; naive Sharpe overstates the edge.

## Sources

- Koijen, Moskowitz, Pedersen, Vrugt, *Carry* (Journal of Financial Economics 2018).
- Du, Tepper, Verdelhan, *Deviations from CIP* (JF 2018).
- BIS Quarterly Reviews on JPY positioning.
- Mallaby, *More Money Than God* (2010) — Druckenmiller and Tudor's role.

## Related

[[carry-trade]] · [[covered-interest-arbitrage]] · [[triangular-arbitrage]] · [[crisis-currency-triangular-arbitrage]] · [[eurodollar-triangular-arbitrage]] · [[funding-rate-arbitrage]] · [[multi-leg-arbitrage]] · [[execution-sequencing]] · [[skewness]] · [[edge-taxonomy]] · [[failure-modes]]
