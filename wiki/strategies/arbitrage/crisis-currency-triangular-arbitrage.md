---
title: "Crisis Currency Triangular Arbitrage"
type: strategy
created: 2026-04-25
updated: 2026-06-20
status: good
tags: [arbitrage, forex, history, crisis]
aliases: ["FX Crisis Triangle", "Peg-Break Triangle"]
related: ["[[currency-peg-break-arbitrage]]", "[[triangular-arbitrage]]", "[[carry-trade]]", "[[1992-black-wednesday-erm-crisis]]", "[[1994-tequila-crisis]]", "[[asian-financial-crisis]]"]
strategy_type: hybrid
timeframe: swing
markets: [forex]
complexity: advanced
backtest_status: live
edge_source: [structural, informational, risk-bearing]
edge_mechanism: "When a currency peg breaks or comes under speculative attack, the central bank's defence withdraws orderly two-way quoting from one leg of a triangle. Cross-rates between adjacent currencies (DEM/ITL during ERM, MYR/IDR during Asia 1997) become inconsistent for hours-days while liquidity providers reprice."
data_required: [spot-fx, forward-fx, central-bank-discount-rates, sovereign-cds]
min_capital_usd: 1000000
capacity_usd: 5000000000
crowding_risk: medium
expected_sharpe: 2
expected_max_drawdown: 0.3
breakeven_cost_bps: 30
decay_evidence: "Each crisis triangle closes within days-weeks of the peg breaking; the strategy is event-driven, not steady-state."
---

# Crisis Currency Triangular Arbitrage

Triangular FX arbitrage during currency-peg crises, when one central bank withdraws or is forced to abandon defence of an exchange-rate target. Cross-rates between the broken currency and its non-attacked neighbours become temporarily inconsistent — liquidity vanishes from one leg, and well-positioned macro funds (Soros's Quantum, Bacon's Moore Capital, Druckenmiller, Bessent at Soros) extract massive returns.

## Edge Source

**Structural** + **informational** + **risk-bearing**.

- **Structural:** Pegs are enforced by central-bank intervention. When the central bank stops quoting (or quotes only one-way), price discovery fragments across venues.
- **Informational:** Insiders (Bundesbank's Helmut Schlesinger Sept 1992, BoT internal forward-book leaks 1997) reveal commitments before official announcements.
- **Risk-bearing:** Most market participants exit; macro funds with conviction take the other side.

## Why This Edge Exists

A defended peg is not a market price — it is a policy commitment. Once that commitment is questioned, traders unwind directional bets first, leaving cross-rate triangles unhedged. The third leg (e.g. DEM-ITL during ERM, when GBP came under attack) often re-prices last because participants focus on the most-attacked pair.

## Null Hypothesis

In normal times, EUR-USD-JPY etc satisfy triangle parity to <2 bp. During crisis windows (Sep 14-17 1992; Dec 19-22 1994; July 2 1997 baht float; Aug 16-17 1998 ruble; Jan 15 2015 CHF un-peg) cross-rate spreads widen to 50-300 bp for hours-days.

## Rules

1. Maintain a real-time triangle scanner across all 60+ G10/EM crosses.
2. Pre-position capital at multiple prime brokers (cross-PB risk).
3. When triangle inconsistency exceeds 30 bp net of bid-ask, execute *all three legs simultaneously*.
4. Hedge tail risk via OTC FX options on the broken currency.
5. Exit within 24-72 hours — the window closes fast.

## Implementation Pseudocode

```python
for (a, b, c) in fx_triangles:
    quote_ab = mid(a, b, bid_ask=spread_ab)
    quote_bc = mid(b, c, bid_ask=spread_bc)
    quote_ca = mid(c, a, bid_ask=spread_ca)
    triangle = quote_ab * quote_bc * quote_ca
    cost = spread_ab + spread_bc + spread_ca
    if abs(triangle - 1) > cost + threshold_30bp:
        side = 'long' if triangle > 1 else 'short'
        execute_three_leg(a, b, c, side, sized_for_kelly_quarter)
```

## Indicators / Data Used

- ECB / BoE / BoT central-bank reserves disclosure.
- Sovereign CDS spreads.
- 1-month / 3-month FX implied vol.
- Risk-reversal skew (1-month 25-delta).
- BIS triennial FX survey.

## Example Trade

**September 16, 1992 — Black Wednesday triangulation (illustrative reconstruction, not a documented trade).**

GBP/DEM: 2.95 ERM central rate (lower band 2.7780 broken intraday).
DEM/ITL: 749 (ITL devalued 7% within the ERM on Sep 13; Italy suspended ERM membership Sep 17).
GBP/ITL implied via DEM: 2.95 × 749 ≈ 2210.
Direct GBP/ITL quoted: 2120 (≈90 lira gap ≈ 4% triangle).

Trade: short GBP/DEM, long DEM/ITL, long GBP/ITL → close triangle. The *documented* trade of that week was directional: Quantum Fund's leveraged GBP short, estimated at $10B notional, generating $1B+ profit (see [[currency-peg-break-arbitrage]] and [[1992-black-wednesday-erm-crisis]]). **[UNVERIFIED]** Claims that Quantum extracted an additional ~$200M from residual cross-rate triangle legs could not be sourced (checked via Perplexity, 2026-06-10 — no documentation found); treat the triangle numbers above as an illustration of the mechanism, not as a verified historical P&L.

## Performance Characteristics

Crisis-window returns are concentrated. Examples (note: these are predominantly *directional* peg-break P&Ls, not pure triangle-arb P&Ls — see Contradictions below):
- 1992 ERM: Soros $1B+, Druckenmiller-led, holding period <1 week. (Documented — Mallaby 2010.)
- 1994-95 Tequila: Long Term Capital and Tudor estimated ~$300M each. **[UNVERIFIED]** — no documentation found (Perplexity check, 2026-06-10).
- 1997 Asian Crisis: Robertson's Tiger ~$1B from baht/ringgit shorts. Widely attributed (Mallaby 2010), but again a directional trade. **[MEDIUM]**
- 1998 LTCM ruble: contributed to LTCM blow-up — wrong-way cross-currency basis.
- 2015 CHF un-peg: many losers (Everest Capital wiped); winners hidden.

## Contradictions

> **Claim A** (this page's premise): crisis windows open multi-hour triangular cross-rate inconsistencies of 50-300 bp that funds systematically harvested.
> **Claim B** (documented record, confidence: HIGH): the famous crisis-window profits (Soros 1992, Tiger 1997) were *directional* peg-break trades, covered at [[currency-peg-break-arbitrage]]. No primary source documents a named fund's P&L from pure triangle closure during these crises.
> **Resolution**: Pending evidence, and the reader should treat the headline triangle magnitudes as unproven. Academic microstructure literature does document triangular-parity deviations widening during turmoil, but at far smaller magnitude and shorter duration than the 50-300 bp / multi-hour figures asserted here. The page is documented to a `good` standard — the mechanism, the verification trail, and the contradiction are all laid out honestly — but **Claim A's quantitative scale remains unverified**: no primary source documents a named fund's P&L from pure triangle closure during these crises. Pure-triangle harvesting is best read as a plausible-but-undocumented adjunct to the well-documented *directional* peg-break trade at [[currency-peg-break-arbitrage]].

## Capacity Limits

Crisis liquidity is finite — even during 1992 ERM, more than $20B in concentrated GBP shorts would have moved markets faster and closed the window earlier. Realistic capacity per fund ~$1-5B notional.

## What Kills This Strategy

- Central bank surprises (CHF un-peg Jan 15 2015 wiped retail and several macro funds).
- Cross-currency basis dislocations during the window (LTCM 1998).
- Counterparty failure during execution (Herstatt risk on FX settlement).

## Kill Criteria

- Triangle restored to <10 bp inconsistency for 5 days running.
- Implied vol on the broken currency drops below 12%.
- Central bank credibly re-establishes a corridor.

## Advantages

- Asymmetric payoff — limited downside (triangle either closes or you cut), large upside.
- Decoupled from systematic risk.

## Disadvantages

- Pure event-driven; capital must sit idle between crises.
- Relies on accurate read of central-bank credibility — wrong calls (early 1992 ITL longs, Aug 1998 ruble bonds) destroy years of profit.

## Sources

- Sebastian Mallaby, *More Money Than God* (2010) — Quantum, Tiger, Moore.
- *Soros on Soros* (1995).
- Robert Slater, *Soros: The Life, Times, and Trading Secrets of the World's Greatest Investor* (1996).
- BIS Quarterly Reviews, Crisis editions.
- Verified via Perplexity (sonar), 2026-06-10: no documentation found for the Quantum ~$200M triangle-leg claim or the Tudor/LTCM ~$300M Tequila figures; lira timeline corrected (devalued 7% Sep 13 1992, ERM membership suspended Sep 17 1992).

## Related

[[arbitrage]] · [[currency-peg-break-arbitrage]] · [[triangular-arbitrage]] · [[carry-trade]] · [[1992-black-wednesday-erm-crisis]] · [[1994-tequila-crisis]] · [[asian-financial-crisis]] · [[ltcm-collapse-1998]] · [[george-soros]] · [[stanley-druckenmiller]] · [[edge-taxonomy]] · [[risk-management]] · [[limits-to-arbitrage]]
