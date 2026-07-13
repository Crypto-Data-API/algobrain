---
title: "Class Action Arbitrage"
type: strategy
created: 2026-04-26
updated: 2026-06-21
status: excellent
tags: [arbitrage, stocks, regulation, event-driven]
aliases: ["Securities Litigation Arbitrage", "Class Action Settlement Trading", "Litigation Finance Arb"]
related: ["[[risk-arbitrage]]", "[[bankruptcy-claim-arbitrage]]", "[[appraisal-rights-arbitrage]]", "[[regulatory-approval-arbitrage]]"]
strategy_type: fundamental
timeframe: position
markets: [stocks]
complexity: advanced
backtest_status: live
edge_source: [analytical, informational, structural]
edge_mechanism: "Securities class action settlements take 2-7 years from filing to final distribution. The probability and quantum of recovery is hard to model; patient capital with legal expertise can buy claims at deep discounts in the secondary claim-trading market and capture the recovery delta."
data_required: [securities-class-action-clearinghouse, court-pacer-feeds, settlement-filings, claim-administrator-data]
min_capital_usd: 5000000
capacity_usd: 1000000000
crowding_risk: low
expected_sharpe: 0.8
expected_max_drawdown: 0.25
breakeven_cost_bps: 1500
decay_evidence: "Strategy stable since 1995 PSLRA reform; opportunity flow correlates with market drawdowns and fraud cycles. Average annual securities class action filings: 200-450."
---

# Class Action Arbitrage

The strategy of buying claims in active or settled securities class actions at discounts to expected recovery, then collecting the distribution. Practitioners include specialist firms (Battea, Goal Group, Financial Recovery Technologies, ISS Securities Class Action Services) and a few hedge funds (typically as a sub-allocation in distressed or event-driven portfolios). Distinct from active class-action plaintiffs' law firms — the arb does not litigate; it absorbs the timing and quantum risk of claim resolution. It is the securities-litigation member of the broader [[arbitrage]] family and sits adjacent to [[distressed-debt-arbitrage]] and [[bankruptcy-claim-arbitrage]] in the claim-trading complex; the shared trait is converting a slow, illiquid, hard-to-value legal entitlement into a tradeable instrument.

## Litigation Lifecycle and the Risk Profile at Each Stage

The discount a buyer can command — and the risk they assume — depends entirely on *which stage* the case is in. Quantum (how much) and timing (when) risk fall sharply as the case matures; price rises to match.

| Stage | Years from filing | Quantum risk | Timing risk | Typical claim price |
|-------|-------------------|--------------|-------------|---------------------|
| Filed, pre-MTD | 0-1.5 | Very high (case may be dismissed) | Very high | Deepest discount / often un-traded |
| Survived motion-to-dismiss | 1-2 | High | High | Deep discount |
| Class certified | 2-3 | Medium | High | Moderate discount |
| Settlement reached, pending approval | 3-5 | Low | Medium | Modest discount |
| Settlement approved, pre-distribution | 4-6 | Low (pro-ration only) | Low | Smallest discount |
| Distribution | 4-7 | Resolved | Resolved | Par |

The cleanest version of the trade is the **post-settlement, pre-distribution** purchase: quantum risk is essentially gone, only pro-ration uncertainty (the participation rate) and timing remain — which is why specialist IRRs on *settled* claims are both lower-variance and easier to reconcile with the discount than the high-variance pre-settlement trade.

## Edge Source

**Analytical** + **informational** + **structural**.

- **Analytical:** Estimating recovery requires modeling court-approved damages methodology (event-study price impact, plan-of-allocation tiers, claim-eligibility rules).
- **Informational:** Specialist firms with access to claim-administrator data forecast distribution timing and pro-ration.
- **Structural:** Most institutional holders don't track their class-action claims actively; many fail to file, leaving "unclaimed" residuals that re-distribute.

## Why This Edge Exists

Securities class actions filed under SEC Rule 10b-5 typically take:
- 1-2 years to motion-to-dismiss ruling.
- 2-3 years to class certification.
- 3-5 years to settlement or trial.
- 4-7 years to final distribution.

Holders who suffered damages often:
1. **Don't file claims** (~30-40% of eligible institutional shares fail to file).
2. **File but sell the underlying** before distribution.
3. **Want immediate liquidity** rather than wait years for distribution.

Claim-trading specialists buy these eligible-but-unfiled or pending claims at 30-60% discounts to expected recovery, then file/collect.

Counterparty: institutional holders disposing of legacy claims; corporate spin-out parents; bankruptcy estates monetizing residual claims.

## Variants

| Variant | Description | Timeline |
|---------|-------------|----------|
| **Pre-settlement claim purchase** | Buy class-member rights before settlement is reached | 3-7 years |
| **Post-settlement claim purchase** | Buy filed-claim entitlements between settlement and distribution | 6-24 months |
| **Opt-out trading** | Buy stake in plaintiffs who opt out of class to litigate individually | 2-5 years |
| **Distressed-debtor opt-out** | Bankruptcy estate sells class-action claim to distressed fund | 1-3 years |

## Null Hypothesis

In an efficient market, claims would clear at expected recovery discounted at a rate commensurate with timing and quantum risk — a buyer would earn only that risk-adjusted rate, not excess IRR. Under the null, the 30-70% observed discounts would be exactly fair compensation for duration, pro-ration uncertainty, and default risk of the settlement fund, and a naive buyer of random claims would earn Treasury-plus-a-little. Empirically, specialist buyers earn 10-15% IRR with low loss rates on *settled* claims (where quantum risk is largely resolved), which is hard to reconcile with the null; the discounts persist due to (1) information asymmetry on recovery quantum, (2) legal complexity of claim assignment, (3) low natural buyer base.

## Rules

1. Source: monitor securities class-action filings (Stanford Securities Class Action Clearinghouse).
2. Screen for: large classes (>$50M expected damages), deep-pocket defendant, clear damages methodology.
3. Model expected recovery using event-study + comparable-case settlement multipliers.
4. Source claim assignments from institutional holders or via secondary claim brokers.
5. Acquire claims at target discount to model recovery; cap any single case at ~5% of fund NAV (settlement-fund and pro-ration risk is case-correlated).
6. File claims with administrator on time.
7. Collect distribution; reinvest.

## Implementation Pseudocode

```python
universe = scac_filings(min_expected_damages=50e6)   # Stanford Clearinghouse feed
for case in universe:
    damages   = event_study_damages(case)            # price-impact model per court methodology
    multiple  = settlement_multiplier(comparable_cases(case))  # Cornerstone/NERA priors
    p_recover = stage_model(case)   # survived motion-to-dismiss? class certified? settled?
    fair_value = damages * multiple * p_recover * time_discount(est_years_to_distribution(case))

    for offer in secondary_claim_market(case):       # brokers, institutional disposals
        if offer.ask < (1 - target_margin) * fair_value:
            buy_claim(offer, max_size=0.05 * fund_nav)
            calendar.add(offer.claim_bar_date)       # missing the filing deadline = total loss

on settlement_approved(case):
    refresh(plan_of_allocation, est_participation_rate)  # pro-ration drives final cents/share
on distribution(case):
    collect_and_reconcile(case)
    update_settlement_multiplier_priors(case)
```

## Indicators / Data Used

- Stanford Securities Class Action Clearinghouse.
- Cornerstone Research annual securities class action reports.
- NERA Economic Consulting damages reports.
- PACER docket feeds.
- Claim-administrator (Garden City Group, Epiq, Strategic Claims Services) participation rates.

## Example Trades

**Petrobras securities class action (2014-2018)** — Operação Lava Jato corruption scandal. ~$3B settlement. Claims for institutional holders traded at 30-50¢ on the dollar in 2017; final distribution paid 65-85¢ equivalent. Specialist firms like Battea netted 30-40% IRR.

**Wells Fargo cross-selling fraud (2016-2020)** — $480M federal class action settlement. Claim trading active 2018-2020 at 50-65¢; final recovery 75-85¢.

**Volkswagen "Dieselgate" (2015-2019)** — Multiple jurisdictions; complex multi-class structure. Claim discounts varied 40-70%.

**Theranos investor litigation (2018-2022)** — Limited recovery (Theranos insolvent); claim discounts very deep (5-15¢) — high-variance trade.

**FTX customer claims (2022-ongoing)** — Not strictly securities class action, but adjacent claim-trading market. See [[bankruptcy-claim-arbitrage]].

## Performance Characteristics

Specialist claim-trading firms report 10-15% annualized IRR over multi-year horizons. Sharpe 0.8-1.2 due to long lock-ups and lumpy distributions. Hedge fund sub-allocations achieve similar returns with smaller capacity.

> The IRR/Sharpe ranges above are practitioner-reported industry figures, not a backtest run in this wiki. Settled-claim trades are lower-variance than pre-settlement trades; the blended numbers above hide that dispersion. Treat as qualitative.

**Cost and friction overlay.** The headline "buy at 40¢, collect 80¢" arithmetic is gross of the frictions that drive the high `breakeven_cost_bps` (≈1500):

| Friction | Effect |
|----------|--------|
| Legal due diligence | Each claim assignment requires counsel review of standing/eligibility |
| Bar-date / filing risk | Missing the claim filing deadline = total loss on that claim |
| Pro-ration uncertainty | Final cents/share depends on participation rate, unknown until distribution |
| Settlement-fund / counterparty risk | Defendant insolvency can shrink or void the recovery |
| Duration / carry | 3-7 year lock-up; IRR sensitive to timing slippage |
| Case correlation | A fraud-cycle or tort-reform shock hits the whole book at once |

Because settlement-fund and pro-ration risk are **case-correlated**, single-case exposure is capped (~5% of NAV) — diversification within a vintage is the primary risk control.

## Capacity Limits

Industry-wide secondary claim trading volume ~$1-3B annually. Largest specialist (Battea) processes ~$500M+ annual claim volume.

## What Kills This Strategy

- Tort reform reduces class-action volume.
- Defendant insolvencies reduce recovery quanta.
- Claim-trading-market commoditization compresses discounts.
- Lower fraud-cycle activity in steady-state markets.

## Kill Criteria

- Average claim discount narrows below 25% to expected recovery.
- 36 months of negative IRR.

## Advantages

- Decoupled from beta and macro.
- Long-duration capital deployment with predictable cash flows.
- Specialist moat (legal/process expertise).

## Disadvantages

- Long lock-up periods (3-7 years).
- Distribution timing uncertainty.
- Specialist legal infrastructure required.

## Sources

- *Securities Class Action Clearinghouse* (Stanford Law).
- Cornerstone Research, *Securities Class Action Filings* (annual).
- NERA Economic Consulting, *Recent Trends in Securities Class Action Litigation* (annual).
- Black, Cheffins, Klausner, *Outside Director Liability* (Stanford 2006).
- Battea / FRT / Goal Group practitioner publications.
- Performance, IRR, and discount figures above are general market knowledge and practitioner-reported ranges; no audited backtest source is ingested in this wiki for them.

## Related

[[risk-arbitrage]] · [[bankruptcy-claim-arbitrage]] · [[appraisal-rights-arbitrage]] · [[regulatory-approval-arbitrage]] · [[distressed-debt-arbitrage]] · [[arbitrage]] · [[relative-value-arbitrage]] · [[limits-to-arbitrage]] · [[edge-taxonomy]] · [[failure-modes]] · [[when-to-retire-a-strategy]]
