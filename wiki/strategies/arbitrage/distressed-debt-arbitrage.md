---
title: "Distressed Debt Arbitrage"
type: strategy
created: 2026-04-26
updated: 2026-06-21
status: excellent
tags: [arbitrage, bonds, fundamental-analysis, event-driven]
aliases: ["Distressed Securities", "Bankruptcy Trading", "Workout Arbitrage", "Vulture Investing"]
related: ["[[bankruptcy-claim-arbitrage]]", "[[risk-arbitrage]]", "[[capital-structure-arbitrage]]", "[[cds-bond-basis-arbitrage]]"]
strategy_type: fundamental
timeframe: position
markets: [bonds, equities]
complexity: advanced
backtest_status: live
edge_source: [analytical, structural, risk-bearing]
edge_mechanism: "Distressed bonds and loans trade at deep discounts (often 20-50¢ on the dollar) because regulated holders (insurance, mutual funds, prime-brokerage clients) cannot or will not hold below-investment-grade or defaulted paper. Specialized funds buy at distressed levels, work through restructuring/Chapter 11, and recover par or near-par over 1-3 years."
data_required: [bond-pricing-feeds, edgar-bankruptcy-filings, court-docket-feeds, indenture-trustee-reports]
min_capital_usd: 50000000
capacity_usd: 5000000000
crowding_risk: medium
expected_sharpe: 1
expected_max_drawdown: 0.4
breakeven_cost_bps: 1500
decay_evidence: "Distressed cycles roughly 7-10 years (post-recession peaks: 2002, 2009, 2020, 2024). Strategy alive across cycles; entry timing critical."
---

# Distressed Debt Arbitrage

The strategy of buying senior debt of distressed or bankrupt issuers at deep discounts, then realizing recovery value through Chapter 11 reorganization, out-of-court restructuring, or asset liquidation. Distinct from passive [[bankruptcy-claim-arbitrage]] (which trades general unsecured claims at discount) — distressed-debt arb actively engages in process: filing 2019 statements, voting on plans, joining ad hoc creditor committees, sometimes leading the restructuring. The dominant strategy at Oaktree, Centerbridge, Apollo (early), Elliott, Avenue Capital, and Davidson Kempner. It is the capital-structure / bankruptcy member of the broader [[arbitrage]] and [[relative-value-arbitrage|relative-value]] families, and overlaps directly with [[capital-structure-arbitrage]] (the cross-instrument version of the same issuer view) and [[risk-arbitrage|risk arbitrage]] (when the catalyst is a court-driven event rather than a merger).

## The Absolute-Priority Waterfall

Every recovery estimate is an exercise in allocating enterprise value (EV) down a strict priority ladder. The discount a buyer captures depends on *where in this ladder* the bought security sits relative to where EV runs out — the **fulcrum security** is the tranche that EV stops at, and therefore the one most likely to convert to the post-emergence equity.

| Priority | Claim class | Typical recovery posture |
|----------|-------------|--------------------------|
| 1 | DIP financing (super-priority) | Near-100%, paid in cash on emergence |
| 2 | Secured / first-lien debt | High; often money-good if collateral covers |
| 3 | Second-lien debt | Variable; frequently the fulcrum |
| 4 | Senior unsecured bonds | Often the fulcrum; converts to equity |
| 5 | Subordinated / mezzanine | Low; out-of-the-money unless EV is large |
| 6 | Trade / general unsecured claims | Low and lumpy; see [[bankruptcy-claim-arbitrage]] |
| 7 | Preferred equity | Usually wiped |
| 8 | Common equity | Almost always wiped in Chapter 11 |

The art is identifying the fulcrum *before* the market consensus does, buying it cheap, and then influencing the plan so the conversion price favors your tranche. This is what separates distressed-debt arb from passive claim trading.

## Edge Source

**Analytical** + **structural** + **risk-bearing**.

- **Analytical:** Recovery analysis is intensive — capital-structure modeling, fraudulent-conveyance review, intercreditor priority, valuation of operating businesses.
- **Structural:** Most institutional holders (insurance companies, IG bond funds, prime-brokerage clients) cannot hold defaulted or sub-investment-grade paper. Forced sellers create persistent discount.
- **Risk-bearing:** Workouts take 12-36 months. Capital is locked up.

## Why This Edge Exists

Capital-structure rules of engagement:
1. **Insurance regulatory capital:** NAIC RBC charges spike for sub-investment-grade and defaulted bonds. Insurers sell.
2. **Fund mandates:** IG bond funds, target-date funds, money-market substitutes cannot hold high-yield distressed.
3. **Prime-brokerage haircuts:** Margin requirements on distressed bonds become prohibitive.
4. **Time:** Most institutional investors don't have the patience for 18-month workouts.
5. **Complexity:** Indenture analysis, intercreditor agreements, and bankruptcy-court process require specialist expertise.

The discount is the price specialist funds extract for absorbing all five frictions. Counterparty: forced-seller institutionals, retail bondholders, panicked secondary buyers.

## Variants

| Variant | Description | Holding Period |
|---------|-------------|----------------|
| **Loan-to-own** | Buy senior debt with intent to convert to controlling equity in restructuring | 12-36 months |
| **Fulcrum security** | Buy the most-likely-to-receive-equity tranche in the cap structure | 12-24 months |
| **Trade claims** | Buy general unsecured claims for liquidation/distribution; see [[bankruptcy-claim-arbitrage]] | 6-36 months |
| **Section 363 sale** | Bid for assets in bankruptcy auction; fund the bid via senior secured | 3-12 months |
| **DIP financing** | Provide debtor-in-possession loan with high yield + super-priority + warrants | 3-12 months |
| **Activist distressed** | Lead the negotiation as ad hoc creditor committee chair | 18-36 months |

## Null Hypothesis

If distressed pricing were efficient, recovery-adjusted yields would equal Treasury + small premium. Empirically, distressed bonds at 30-40¢ recovering to 70-80¢ over 18 months equate to 50-100% IRR — far above any realistic risk-free benchmark.

## Rules

1. **Universe screening:** scan for bonds trading <60¢ on the dollar with default within 24 months.
2. **Capital structure mapping:** rank tranches by priority and collateral.
3. **Recovery modeling:** estimate enterprise value, allocate by waterfall.
4. **Catalyst identification:** restructuring negotiation, court process, sale.
5. **Position sizing:** typically 1-3% of fund per name; scale up to a *blocking position* (>1/3 of a class, the threshold to veto a plan under §1126(c)) when the goal is loan-to-own control. Single-name cap 5-10% of fund NAV because process risk is idiosyncratic and lumpy.
6. **Active engagement:** join ad hoc committee, file objections to motions, lead negotiation when warranted.
7. **Exit:** plan effective date, equity distribution, or secondary sale post-emergence.

**Entry / exit / sizing at a glance.**

| Decision | Trigger |
|----------|---------|
| Enter | Price < ~70% of modeled recovery mid AND security is senior or fulcrum |
| Upsize to blocking | Position approaches 1/3 of class; control thesis intact |
| Exit early | Price reaches recovery mid before emergence (let someone else bear process risk) |
| Exit at emergence | Plan effective date; take cash/equity distribution or sell post-emergence equity |
| Cut / stop | Liquidation floor breached, fraud/MAC discovered, or priority thesis defeated in court |

## Implementation Pseudocode

```python
on weekly_screen:
    universe = bonds(price < 0.60, est_default_prob_24m > 0.5)   # TRACE + ratings + CDS-implied
    for issuer in universe:
        structure = map_capital_structure(issuer)    # liens, guarantees, intercreditor, maturity wall
        ev_range  = value_enterprise(issuer)         # going-concern multiples + liquidation floor
        for tranche in structure:
            recovery = waterfall(ev_range, tranche)  # allocate EV by priority/collateral
            if tranche.price < 0.70 * recovery.mid and is_senior_or_fulcrum(tranche, ev_range):
                buy(tranche, size=min(0.03 * fund_nav, blocking_stake_cost(tranche)))
                if position_pct_of_class(tranche) > 1/3:     # blocking position in the class
                    join_or_form_ad_hoc_committee(issuer)

on docket_event(issuer):                             # PACER feed: plan, DIP motion, 363 bid, valuation fight
    recovery = update_waterfall(issuer, event)
    if price(position) >= recovery.mid or event is plan_effective_date:
        exit_via_distribution_or_secondary(position)
```

## Indicators / Data Used

- TRACE bond pricing data.
- PACER court docket feeds.
- 2019 statement filings (creditor identity disclosure).
- Indenture trustee reports.
- Bloomberg DDIS / Reorg Research / Debtwire.
- Restructuring law firm activity (Kirkland, Weil, Akin).

## Example Trades

**Lehman Brothers (2008-2022)** — Senior unsecured bonds traded as low as 8¢ in 2008-2009. The 2011 plan estimated ~21¢ recovery for LBHI senior unsecured; cumulative distributions ultimately over-delivered, reaching roughly 40-45¢ for LBHI general unsecured creditors through the final distributions. Funds that bought at 9-12¢ made 70-130% gross against the plan estimate alone, with the later distributions pushing multiples toward 3-4x. Paulson & Co., Centerbridge, Elliott major participants.

**General Motors (2009)** — Old GM bonds traded ~10¢ at filing. Unsecured creditors received 10% of new GM common equity plus two warrant tranches (struck at $10 and $18.33) via the Motors Liquidation GUC Trust — worth roughly 10-15¢ on ~$32B of allowed claims as GM stock rallied post-IPO. Well below par, but a positive trade for buyers at distressed lows, and the warrant package gave significant convexity to the post-IPO rally.

**Hertz (2020)** — COVID bankruptcy. Bonds traded at 30-40¢; ultimately recovered par+ as used-car prices rallied 2021. Specialty funds (Knighthead, Certares) led equity rights offering and made 5-10x.

**Caesars Entertainment (2015-2017)** — Complex multi-OpCo bankruptcy. Bondholders pushed back against private-equity sponsor (Apollo, TPG) extraction; recovery negotiated up over 2 years.

**Frontier Communications (2020)** — Bonds 30-50¢; converted to equity in 2021. Equity rallied; recovery 70-90¢ equivalent.

**WeWork (2023-2024)** — Complex multi-class bondholder situation. Distressed funds (King Street, Brigade) led the restructuring.

## Performance Characteristics

Top distressed funds report 12-20% annualized over multi-decade horizons (Oaktree's distressed funds: 15-22% net IRR through 2020). Sharpe 0.7-1.2 due to lumpy returns and 18-36 month lock-ups. Highly cyclical — distressed yields compress in QE-fueled years (2014-2019, 2021), wide in recessions (2002, 2009, 2020, 2024).

> The IRR figures above are publicly cited industry ranges/manager disclosures, not a backtest produced in this wiki. They are coarse, multi-decade, and survivorship-biased (failed distressed funds do not report). Treat as qualitative.

**Cost and friction overlay.** The gross "buy at 30¢, recover at 70¢" arithmetic is gross of substantial frictions that the high `breakeven_cost_bps` (≈1500) reflects:

| Friction | Effect |
|----------|--------|
| Distressed bid-ask | Wide — often 200-1000+ bps on illiquid names |
| Legal / advisory fees | Restructuring counsel, financial advisors, committee costs |
| Time value | 12-36 month lock-up; IRR ≠ MOIC; carry cost of idle dry powder |
| Process failure | Plan rejected, valuation fight lost, priority recharacterized |
| Cyclical timing | Buying too early (2008 had a second leg down) destroys IRR |

The strategy is **deeply negative-skew across the cycle**: outsized vintages (2009, 2020 entries) carry the multi-decade average, while mid-cycle deployment at compressed yields earns little and ties up capital.

## Capacity Limits

Industry-wide distressed AUM ~$300-500B. Per-fund $5-20B sweet spot. Single-name positions typically capped at 5-10% of fund.

## What Kills This Strategy

- QE/zero-rate environments compress default rates.
- Capital glut from PE/credit flows narrows distressed yields.
- Aggressive fraudulent-conveyance and equitable-subordination case law shifts (against creditors).
- Sponsor-friendly jurisdictions (Texas, Delaware) entrench sponsor control.

## Kill Criteria

- Distressed default rate <2% for 24 consecutive months.
- Average buy yields below 12% on the universe.

## Advantages

- High-Sharpe, decoupled from beta.
- Asymmetric upside (par recovery vs. distress entry).
- Specialist moat via legal/process expertise.

## Disadvantages

- Long capital lock-up.
- Headline risk (distressed names often have business or fraud issues).
- Lumpy returns; large drawdowns possible if process goes wrong.

## Sources

- Edward Altman, *Corporate Bankruptcy: Predicting Financial Distress* (1968+).
- Stuart Gilson, *Creating Value Through Corporate Restructuring* (2010).
- Howard Marks (Oaktree) memos on distressed cycles.
- Reorg Research, Debtwire — primary trade press.
- *American Bankruptcy Law Journal* — academic.
- NY Fed Liberty Street Economics, *Creditor Recovery in Lehman's Bankruptcy* (2019).
- Verified via Perplexity (sonar), 2026-06-10 — Lehman recovery figures (2011 plan ~21%; LBHI GUC cumulative ~45% by the 16th distribution): libertystreeteconomics.newyorkfed.org/2019/01/creditor-recovery-in-lehmans-bankruptcy/, hugheshubbard.com Lehman final-payout notice.

## Related

[[bankruptcy-claim-arbitrage]] · [[risk-arbitrage]] · [[capital-structure-arbitrage]] · [[cds-bond-basis-arbitrage]] · [[convertible-arbitrage]] · [[archegos-blowup-2021]] · [[arbitrage]] · [[relative-value-arbitrage]] · [[class-action-arbitrage]] · [[limits-to-arbitrage]] · [[edge-taxonomy]] · [[failure-modes]] · [[when-to-retire-a-strategy]]
