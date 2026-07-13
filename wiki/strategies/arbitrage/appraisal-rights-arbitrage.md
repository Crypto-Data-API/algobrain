---
title: "Appraisal Rights Arbitrage"
type: strategy
created: 2026-04-26
updated: 2026-06-21
status: excellent
tags: [arbitrage, stocks, event-driven, regulation]
aliases: ["Appraisal Arb", "Dissenters' Rights Arb", "DGCL 262 Trading"]
related: ["[[merger-arbitrage]]", "[[risk-arbitrage]]", "[[hostile-takeover-arbitrage]]"]
strategy_type: fundamental
timeframe: position
markets: [stocks]
complexity: advanced
backtest_status: live
edge_source: [analytical, structural, risk-bearing]
edge_mechanism: "Delaware General Corporation Law §262 grants dissenting shareholders the right to demand judicial appraisal of their shares' fair value rather than accept the merger consideration. Specialist firms (Merion, Houlihan-side, etc.) buy shares of merger targets they believe were sold at below-fair value, dissent, and litigate for higher payouts plus statutory interest."
data_required: [merger-agreement-documents, fair-value-models, delaware-court-precedents, statutory-interest-rates]
min_capital_usd: 5000000
capacity_usd: 2000000000
crowding_risk: low
expected_sharpe: 0.8
expected_max_drawdown: 0.3
breakeven_cost_bps: 800
decay_evidence: "Court rulings have alternated friendly and hostile to appraisal arbs. *Dell* (2017) and *DFC Global* (2017) raised the bar for above-deal-price awards; appraisal claims peaked 2014-2015 then declined."
---

# Appraisal Rights Arbitrage

The specialist strategy of buying shares of public-company merger targets, dissenting from the merger, and petitioning Delaware Chancery Court (or another state's analog) for **judicial appraisal** of "fair value" — which can exceed the merger consideration. The pioneering practitioners were specialist funds such as [[merion-capital|Merion Capital]], Magnetar Capital, and Verition Partners in the 2010s; the strategy compressed substantially after the 2017 Delaware Supreme Court rulings in *Dell* and *DFC Global*. It is a niche, litigation-heavy corner of [[event-driven]] [[arbitrage]] — adjacent to [[merger-arbitrage]] and [[risk-arbitrage]] but distinct in that the payoff is decided by a judge applying a statutory "fair value" standard rather than by deal completion. The strategy is a textbook case of a [[limits-to-arbitrage|limit to arbitrage]]: the right exists for every dissenter, but the multi-year lock-up, litigation cost, and binary court outcome keep all but specialist capital out.

At a glance:

| Attribute | Value |
|---|---|
| Style | [[event-driven]] single-name, litigation-driven |
| Legal anchor | Delaware General Corporation Law (DGCL) §262 |
| Typical horizon | 18-36 months (entry to award) |
| Counterparty | Acquirer / sponsor (cash defendant in the appraisal action) |
| Capital lock-up | Full position illiquid until ruling/settlement |
| Regime | Far more attractive pre-2017 (*Dell*/*DFC Global* compressed it) |
| Edge sources | [[edge-taxonomy\|Analytical + structural + risk-bearing]] |

## Edge Source

**Analytical** + **structural** + **risk-bearing** (see [[edge-taxonomy]]).

| Edge | Where it comes from | Who pays it |
|---|---|---|
| **Analytical** | Fair-value modeling under Delaware case law — DCF vs market price vs deal-process bias. Reconciling a defensible "fair value" the court will accept. | Acquirers who underpriced a flawed-process deal |
| **Structural** | DGCL §262 grants the right, but only specialist plaintiffs exercise it. The de minimis floor and continuous-holding rule exclude most holders. | The 85-98% of shares that simply take the cash |
| **Risk-bearing** | 18-36 month process; capital lock-up; statutory interest accrues but at a sub-market rate post-2016. The arb warehouses litigation and timing risk. | The market, which discounts illiquid, binary-outcome claims |

## Why This Edge Exists

When a public company merges (cash deal), shareholders can:
1. Vote yes and receive merger consideration.
2. Vote no but receive merger consideration anyway (majority controls).
3. Dissent, refuse the consideration, file for appraisal.

Option 3 is the appraisal-arb path. The arb's hypothesis: the deal price was depressed by a flawed sales process — controlled deal, conflicted board, insufficient market test, sponsor-led recapitalization disguised as arms-length sale, take-private at trough valuation. If Chancery agrees, fair value > deal price; the arb captures the delta plus statutory interest.

Pre-2016: statutory interest of 5% above the Federal Reserve discount rate (compounded quarterly) accrued from merger close to court ruling — a meaningful return even on a tie verdict.

Post-August-2016 amendments: the interest *rate* was unchanged, but the surviving company gained the right to **prepay** the merger consideration to dissenters, stopping interest accrual on the prepaid amount. This killed the "interest-only" carry trade; the strategy now requires actual upside on fair value. The 2016 amendments also added a de minimis exception (appraisal unavailable unless dissenting shares exceed $1M in value or 1% of outstanding shares, for listed companies).

Counterparty: sponsor / acquirer (the cash defendant in the appraisal proceeding).

### Statutory mechanics and timeline (DGCL §262)

Perfecting appraisal rights is procedurally unforgiving — a single missed step forfeits the claim entirely, which is itself part of the [[limits-to-arbitrage|limit to arbitrage]] that keeps the field thin.

| Step | Requirement | Failure mode |
|---|---|---|
| Record date | Hold shares of record continuously through the effective date | Beneficial-only holders must perfect via the record holder |
| Written demand | File a written demand for appraisal **before** the shareholder vote | Late or defective demand → rights forfeited |
| Do not vote yes | Must not vote in favor of the merger | Voting yes waives appraisal |
| Effective date | Merger closes; dissenters do not receive consideration unless prepaid | Acquirer may **prepay** to truncate interest (post-2016) |
| Petition | File petition in Chancery within 120 days of close | Missed window → claim dies |
| Discovery / trial | Valuation discovery; expert DCF battle | Court-discretion variance |
| Award | Judge sets "fair value" + statutory interest | May be **below** deal price (*Aruba*, *SWS*) |

### Statutory interest regime

| Period | Interest treatment | Effect on strategy |
|---|---|---|
| Pre-Aug 2016 | 5% over Fed discount rate, compounded quarterly, accruing from close to ruling | Supported an "interest-only" carry trade — positive even on a tie |
| Post-Aug 2016 | Same rate, but acquirer may **prepay** the consideration to stop interest on the prepaid amount; de minimis exception added ($1M / 1% floor for listed cos.) | Carry trade killed; strategy now needs real upside on fair value |

## Null Hypothesis

In an efficient sale process, deal price = fair value, and appraisal nets zero before legal costs and illiquidity — i.e., the strategy under the null is a multi-year lock-up that returns deal price plus (post-2016, prepayment-truncated) statutory interest minus litigation expense: negative expected value. Empirically the null was rejected pre-2017: academic studies (Korsmo & Myers 2015; Jiang, Li & Thomas) found Chancery awarded above deal price in a majority of litigated cases, with substantial but right-skewed premiums. *Dell* and *DFC Global* (2017) shifted the court toward deal price as the presumptive fair-value benchmark in clean-process deals, pushing average premiums toward zero — i.e., the post-2017 regime moved much closer to the null, and below-deal awards (*Aruba* $19.10 vs $24.67; *SWS* $6.65 vs $6.92) made dissenting in clean deals actively negative-EV.

## Rules

1. **Deal screen:** identify cash mergers with potentially flawed process — single-bidder, sponsor-led, controlling-shareholder buyout, take-private at trough.
2. **Process review:** assess board independence, special committee adequacy, market check thoroughness.
3. **Fair value model:** DCF + comparable transactions + comparable companies; reconcile to deal price.
4. **Acquire shares:** buy in open market post-record date (per DGCL must hold continuously through merger).
5. **Dissent:** file demand for appraisal in time per statutory deadline.
6. **Litigate:** join consolidated appraisal action; participate in valuation discovery.
7. **Settle or trial:** typical 18-36 month timeline.

**Position sizing:** per-deal exposure capped by the de minimis floor on one side ($1M+ / 1%+ of shares) and by total dissent capacity on the other (historically 2-15% of float dissents); fund-level concentration limits of 10-20% per deal given binary court outcomes and multi-year illiquidity.

## Implementation Pseudocode

```python
for deal in cash_merger_pipeline():                     # announced definitive cash mergers
    process = score_process(deal.proxy_DEF14A)          # single-bidder? MBO/controller? special-committee quality? market check?
    fv = fair_value_model(deal)                         # DCF + comps + precedent transactions, reconciled to deal price
    upside = fv / deal.price - 1

    # Post-Dell/DFC: only flawed-process deals are worth litigating
    if process.flawed and upside > 0.20 and dissent_value(deal) > max(1_000_000, 0.01 * deal.shares_out):
        shares = buy(deal.ticker, size=min(per_deal_cap, dissent_capacity(deal)))
        # Perfect appraisal rights under DGCL 262:
        do_not_vote_yes(shares)
        hold_continuously_through(deal.close_date)
        file_written_demand(before=deal.statutory_deadline)

        outcome = litigate_or_settle(horizon_months=(18, 36))
        interest = statutory_interest(rate=fed_discount_rate + 0.05,
                                      compounding="quarterly",
                                      truncated_by=company_prepayment)   # post-2016 right
        pnl = outcome.award_per_share * shares + interest - cost_basis - legal_costs
```

## Indicators / Data Used

- Merger proxy (DEF 14A): special-committee report, fairness opinion, process narrative.
- 13D / Schedule TO history.
- Delaware Chancery prior opinions on similar deals.
- Federal Reserve discount rate (statutory interest base).
- Deal-flow desks at corporate-law firms.

## Example Trades

**Dell Inc. (2013-2017)** — Michael Dell-led $13.65 take-private (plus $0.13 special dividend). Dissenters argued $17+ fair value. Chancery (VC Laster, 2016) awarded ~$17.62 (~28% above deal). The Delaware Supreme Court reversed in December 2017, signaling deal price is presumptively strong evidence of fair value where the sale process is robust. On remand the remaining petitioners settled or were dismissed — receiving roughly merger consideration plus interest, **not** the $17.62 award. The reversal discouraged future challenges to clean-process deals.

**Aruba Networks / HP (2015 deal)** — $24.67 deal price; Chancery awarded $17.13 fair value (unaffected market price — below deal price). On appeal, the Delaware Supreme Court (*Verition v. Aruba*, 2019) set fair value at $19.10 (deal price minus synergies) — still below deal price. Dissenters lost.

**SWS Group / Hilltop Holdings (2014 deal)** — Chancery (2017) awarded fair value **below** the merger consideration: $6.65 vs ~$6.92 (~4% below). Another "negative" appraisal — dissenters lost.

**Verition Partners cases (multiple, 2013-2019)** — Active appraisal-arb fund (Dell, Aruba); mixed-to-negative results post-Dell.

**Ramtron / Cypress Semiconductor (2012 hostile deal)** — Chancery awarded $3.37 fair value vs the $3.10 deal price — ~9% above deal; one of the dissenter wins.

Summary of the worked outcomes above:

| Case | Deal price | Court fair value | Outcome for dissenter |
|---|---|---|---|
| Dell (2013) | $13.65 + $0.13 | Chancery $17.62; reversed on appeal | Net ≈ deal price + interest (loss vs award) |
| Aruba / HP (2015) | $24.67 | $19.10 (Supreme Court) | Below deal — loss |
| SWS / Hilltop (2014) | ~$6.92 | $6.65 | ~4% below — loss |
| Ramtron / Cypress (2012) | $3.10 | $3.37 | ~9% above — win |

The split outcomes are the whole point: a single below-deal ruling on a clean-process deal swamps several modest wins, which is why post-*Dell* practitioners screen ruthlessly for process flaws.

## Performance Characteristics

> **Data disclaimer:** the ranges below are practitioner/era estimates and academic case-study findings, not a reproducible backtest. Appraisal outcomes are binary and judge-dependent; no audited track record of dedicated appraisal-arb returns is published here. Treat all figures as illustrative orders of magnitude.

The cost structure is unusually heavy for an equity strategy and dominates expected value:

| Cost / drag | Magnitude | Note |
|---|---|---|
| Litigation expense | High fixed + per-deal | Expert valuation, counsel, discovery; the `breakeven_cost_bps: 800` in frontmatter reflects this drag |
| Capital lock-up | 18-36 months | No interim liquidity; opportunity cost |
| Statutory interest (post-2016) | Sub-market, prepay-truncated | No longer a reliable carry |
| Court-discretion variance | Binary | Can be negative even on a "good" thesis |

Era estimates (illustrative, not audited):

- **Pre-2017 (Dell-era):** practitioners cited roughly 12-25% annualized on dedicated appraisal-arb capital, with a high but right-skewed dispersion. The interest regime alone provided a floor.
- **Post-2017:** roughly 6-10% annualized at best, with meaningfully reduced capacity. Surviving practitioners focus on controlled-deal scenarios with conflicted boards (controller squeeze-outs, sponsor-led recapitalizations) where deal price is *not* presumptively fair value.

## Capacity Limits

Per-deal capacity bound by the appraisal-eligible share count (typically 2-15% of float dissent). Strategy-level capacity ~$1-3B globally.

## What Kills This Strategy

- *Dell* / *DFC Global* + their progeny narrowed the gap.
- 2016 statute amendment reduced interest-only carry trade.
- Sponsors offer pre-deal "appraisal protection" structures.
- Reduced LBO / take-private deal flow in compressed-multiple environments.

## Kill Criteria

- Average post-2017 awards below deal price for 36 months running.
- New Delaware case law explicitly capping appraisal at deal price.

## Advantages

| Advantage | Why it matters |
|---|---|
| Niche; few competitors | Low [[crowding-risk\|crowding]]; the procedural and capital barriers deter generalists |
| Decoupled from market beta | Payoff depends on a court ruling, not market direction — diversifies an [[arbitrage]] book |
| Asymmetric upside on conflicted-process deals | Controller squeeze-outs and sponsor-led recaps can deliver large premiums to fair value |
| Statutory interest floor (legacy) | Pre-2016 provided downside cushion even on a tie verdict |

## Disadvantages

| Disadvantage | Why it matters |
|---|---|
| Long capital lock-up | 18-36 months illiquid per deal; severe opportunity cost |
| Court-discretion variance | Outcome is binary and judge-dependent; can be below deal price |
| Specialist legal expertise required | Needs Delaware litigation counsel and credible valuation experts |
| Post-2017 regime shift | *Dell*/*DFC Global* made clean-process deals negative-EV to challenge |
| Procedural fragility | One missed §262 step forfeits the entire claim |

## Sources

- DGCL §262 (statute).
- *Dell Inc. v. Magnetar Global Event Driven Master Fund Ltd.*, Del. Supreme Court (2017).
- *DFC Global Corp. v. Muirfield Value Partners*, Del. Supreme Court (2017).
- Subramanian, *Deal Price as Fair Value: A Theory* (2018).
- Korsmo & Myers, *Appraisal Arbitrage and the Future of Public Company M&A* (2015).
- Jiang, Li & Thomas, *Appraisal: Shareholder Remedy or Litigation Arbitrage?* (J. Law & Econ.).
- Verified via Perplexity (sonar), 2026-06-10 — Dell remand settlements, SWS award ($6.65 below deal), Ramtron award ($3.37 vs $3.10), 2016 prepayment amendment, Aruba Supreme Court $19.10. Citations include seyfarth.com, potteranderson.com, morrisjames.com, courts.delaware.gov.

## Related

[[merger-arbitrage]] · [[risk-arbitrage]] · [[relative-value-arbitrage]] · [[hostile-takeover-arbitrage]] · [[corporate-action-arbitrage]] · [[tender-offer-arbitrage]] · [[regulatory-approval-arbitrage]] · [[event-driven]] · [[limits-to-arbitrage]] · [[arbitrage]] · [[edge-taxonomy]] · [[failure-modes]]
