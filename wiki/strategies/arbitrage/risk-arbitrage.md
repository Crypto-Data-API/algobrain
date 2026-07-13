---
title: "Risk Arbitrage"
type: strategy
created: 2026-04-24
updated: 2026-06-20
status: excellent
tags: [arbitrage, event-driven, stocks]
aliases: ["Risk Arb", "Event Arbitrage", "Deal Arbitrage"]
related: ["[[arbitrage-overview]]", "[[merger-arbitrage]]", "[[event-driven-trading]]", "[[convertible-arbitrage]]", "[[edge-taxonomy]]"]
strategy_type: fundamental
timeframe: position
markets: [stocks]
complexity: advanced
backtest_status: untested
edge_source: [risk-bearing, analytical, structural]
edge_mechanism: "Long-only holders dump deal-completion risk at a discount after announcement; the arbitrageur is paid the deal spread to warehouse break risk it can handicap better than the marginal seller."
data_required: [ohlcv-daily, fundamentals-pit, ma-deal-terms, options-chain]
min_capital_usd: 250000
capacity_usd: 1000000000
crowding_risk: high
expected_sharpe: 0.8
expected_max_drawdown: 0.15
breakeven_cost_bps: 50
decay_evidence: "Mitchell & Pulvino (2001) document ~4% annual excess returns on passive deal portfolios; dedicated-arb spreads have compressed to ~4-7% annualized in the multi-strat era vs. 10-15% in the 1980s-90s."
---

# Risk Arbitrage

Risk arbitrage (also "deal arbitrage" or "event arbitrage") is the family of event-driven strategies that exploit mispricings created by announced or anticipated corporate actions -- mergers, tender offers, SPAC de-SPACs, rights issues, spin-offs, and capital-structure events. Unlike [[cross-exchange-arbitrage]] or [[triangular-arbitrage]], profits are not locked in at execution: the spread only collapses if the underlying deal or event closes on expected terms, so the arbitrageur is compensated for bearing *deal-break risk*.

This is the arbitrage of discretion. A classical pure-arb trade collapses in milliseconds once identified; a risk-arb trade lives for weeks or months and can gap against you 20-40% in a single session if the deal breaks. The edge is informational and analytical (legal, regulatory, and financing knowledge) plus structural (balance-sheet capacity to hold through vote dates, regulatory reviews, and financing contingencies).

## Edge source

Per the [[edge-taxonomy]], risk arb draws on three of the five edge categories:

- **Risk-bearing** (primary): the deal spread is fundamentally an insurance premium. The arbitrageur is paid to absorb deal-completion risk that the seller (usually a long-only holder who wants certainty now) wants to offload.
- **Analytical**: the best arb desks model regulatory risk ([[hsr-review]], [[cfius]], EU [[ec-merger-regulation]]), financing risk (for cash deals), and vote risk better than the marginal participant. The passive premium is small; selection is where excess return lives.
- **Structural**: prime-broker access, stock-borrow for hedging stock deals, and the labor capacity to read merger agreements and Delaware case law gate out most participants. Index-rebalancing flow (targets removed from indexes on close) creates predictable forced selling that arbs absorb.

## Why this edge exists

- **Structural sellers**: long-only holders (pensions, mutual funds) often sell immediately on deal announcement to lock in gains -- they don't want deal-break risk at the margin, and their mandates rarely reward holding for the last 3% of a $100 deal. They knowingly "lose" the spread in exchange for certainty; this is risk transfer, not stupidity, which is why the premium persists.
- **Index rebalancing**: the target is removed from indexes on close; passive funds must sell, creating predictable flow that someone must warehouse.
- **Capacity for complexity**: analyzing antitrust, CFIUS, financing, and proxy risk is labor-intensive and gates out retail and most generalist institutions.
- **Funding moats**: [[convertible-arbitrage]] and [[capital-structure-arbitrage]] require prime-broker relationships, leverage, and stock-borrow that most cannot access.

The other side of the trade is therefore: (1) holders paying for certainty, (2) index funds forced to trade on known dates, and (3) occasionally other arbs forced to liquidate in a crowded unwind.

## Relationship to merger arbitrage

[[merger-arbitrage]] is the flagship and largest sub-strategy of the risk-arb family; the terms are often used interchangeably, but the relationship is one of subset-to-superset:

| | [[merger-arbitrage]] | Risk arbitrage (this page) |
|---|---|---|
| Scope | Announced M&A only (cash and stock deals) | All event-driven corporate actions — mergers, tenders, SPACs, rights issues, spin-offs, appraisal, distressed |
| Core trade | Long target, short acquirer (stock deal) | Same mechanics applied across the full event taxonomy |
| Edge | Deal-spread capture for break risk | Same risk-bearing premium generalized to every binary corporate event |
| Typical book | Pure merger book | Diversified across M&A + capital-structure + legal/regulatory events |

In practice a dedicated merger-arb desk *is* a risk-arb desk that has chosen to concentrate on the deepest, most diversifiable sub-pool (M&A). Everything in the [[merger-arbitrage]] page on deal spread, exchange-ratio hedging, and break risk applies here verbatim; this page situates it inside the broader [[event-driven-trading]] and [[relative-value-arbitrage]] universe. See also [[arbitrage]] and [[limits-to-arbitrage]] for why these spreads do not get fully competed away.

## Anatomy of the deal spread

The deal spread is the gap between the offer consideration and the target's current price. It is decomposed and traded as follows.

| Component | Definition | Drives |
|---|---|---|
| **Offer value** | Per-share consideration (cash $/share, or `exchange_ratio × acquirer_price` for stock) | The ceiling the target converges to on close |
| **Gross spread** | `offer_value − target_price` | Headline profit if the deal closes on time and on terms |
| **Annualized spread** | `(gross_spread / target_price) × (365 / days_to_close)` | The carry rate used to compare deals on a like-for-like basis |
| **Undisturbed price** | Pre-announcement trading price | The floor the target reverts to on a break — the basis for the **downside gap** |
| **Downside gap** | `target_price − undisturbed_price` | The loss-given-break; the number positions must be **sized off**, not the spread |
| **Implied P(close)** | Solved from the EV equation given spread and gap | The market's consensus break probability — your handicap is the bet against it |

The market's *implied completion probability* falls straight out of setting expected value to zero:

```
implied_p_close = (downside_gap + carry) / (gross_spread + downside_gap)
```

If the arbitrageur's handicapped `P(close)` exceeds this implied value, the spread is cheap (overcompensating for break risk); if below, it is rich (do not enter). The entire analytical edge is the difference between handicapped and implied completion probability.

## Completion probability — what moves the handicap

Handicapping `P(close)` is the core analytical task. The dominant inputs, roughly in order of historical importance:

| Factor | Raises P(close) | Lowers P(close) |
|---|---|---|
| **Antitrust** ([[hsr-review]], [[cfius]], EU [[ec-merger-regulation]], China SAMR) | Friendly strategic, low overlap, early termination granted | Second request, Phase II, horizontal overlap, active enforcement regime |
| **Financing** | All-cash from balance sheet; committed financing | Financing contingency, fragile LBO debt markets, ratings risk |
| **Shareholder vote** | Board + large holders supportive; ISS/Glass Lewis "for" | Activist opposition, low premium, competing bid uncertainty |
| **MAC clause** | Narrow, deal-specific carve-outs | Broad material-adverse-change language the acquirer can invoke |
| **Acquirer track record** | Serial acquirer, clean close history | History of renegotiation or walking |
| **Outside date / timing** | Generous outside date with extensions | Tight date with hard drop-dead and no extension |

Proxy advisors (ISS, Glass Lewis) and the **options skew** on the target are the two best real-time consensus checks: the put market independently prices break risk, and a divergence between your handicap and the put-implied probability is a signal to re-examine the thesis (see [[volatility-arbitrage]] and [[options-chain]] for the mechanics).

## Downside on a break — the asymmetry that defines the strategy

Risk arb is structurally a **short-volatility / short-put** profile: many small gains punctuated by occasional large losses. On a break, the target does not merely give back the spread — it falls to (or below) its undisturbed price, because (1) the takeover premium evaporates, (2) the now-overhang of arb sellers all exit at once, and (3) the break itself often signals deteriorated fundamentals or a regulatory verdict that re-rates the standalone business lower.

The practical consequence is the single most important sizing rule in the strategy:

> **Size off the downside gap, not the spread.** A $3 spread looks like a small position until you note the $20 gap-down on a break. Risking 1-2% of NAV on the *break scenario* — not on the spread — is what keeps a single broken deal from erasing a year of carry.

This is why [[merger-arbitrage]] and risk arb are best understood as insurance underwriting: you collect thin premiums (spreads) and occasionally pay large claims (breaks). See [[limits-to-arbitrage]] for why the risk-bearing premium persists rather than being arbitraged to zero.

## Null hypothesis

If spreads exactly priced break risk, a no-skill arbitrageur buying *every* announced definitive deal would earn approximately the risk-free rate plus a small disaster-insurance premium, with the return profile of a short out-of-the-money index put: many small gains, occasional 20-40% single-name gaps, and market beta that spikes in crashes. This is close to what Mitchell & Pulvino (2001) actually found for passive deal portfolios (~4% annual excess return pre-cost, nonlinear downside beta). The null is *not* zero -- it is "you are an insurance writer earning a thin premium with severe negative skew." Any claimed edge above that must come from deal selection: demonstrably better handicapping of break probability than the consensus implied by the spread.

## Rules

**Universe**: announced deals with a signed definitive agreement (not rumors, not LOIs). Sub-strategies extend to tenders, SPACs, rights issues, spin-offs -- see Taxonomy below.

**Entry**:
1. Compute the deal spread and the downside gap (current price minus undisturbed pre-announcement price).
2. Handicap P(close) from: regulatory exposure (HSR second request, CFIUS, EU Phase II), financing contingencies, vote math, MAC-clause strength, acquirer track record.
3. Enter only when expected value is positive at your handicapped probability AND annualized spread exceeds a hurdle (e.g., Fed funds + 300 bps).
4. Cash deal: long target only. Stock deal: long target, short acquirer at the exchange ratio to isolate the spread.

**Exit**:
- Deal closes: tender shares / receive consideration.
- Terms amended: re-run EV; exit if hurdle no longer met.
- Thesis break (lawsuit to block, financing wobble, MAC assertion): exit or cut before the binary resolution unless the repriced spread overcompensates.

**Position sizing**: size off the *downside gap*, not the spread -- e.g., risk no more than 1-2% of NAV per deal on a break scenario, which typically caps positions at 3-8% of NAV. Hold 10-30 deals; cap aggregate exposure to any single regulatory theme (e.g., all deals pending Chinese SAMR approval) at ~15% of NAV.

## Implementation pseudocode

```python
for deal in announced_definitive_deals:
    p_close   = handicap(deal)        # regulatory, financing, vote, MAC analysis
    spread    = deal.offer_value - deal.target_price
    downside  = deal.target_price - deal.undisturbed_price   # gap if break
    carry     = financing_cost(deal) + borrow_cost(deal)     # borrow only if stock deal
    ev        = p_close * spread - (1 - p_close) * downside - carry
    ann       = (ev / deal.target_price) * (365 / est_days_to_close(deal))

    if ev > 0 and ann > hurdle_rate:
        size = min(max_position_pct * nav,
                   per_deal_risk_budget / downside)           # size off the gap
        buy(deal.target, size)
        if deal.is_stock_deal:
            short(deal.acquirer, size * deal.exchange_ratio)

# monitor daily: regulatory milestones, proxy dates, financing news
# exit on close, on terms amendment below hurdle, or on thesis break
```

## Indicators / data used

- Deal terms: offer price, exchange ratio, termination fee, outside date, MAC clause (merger agreement, 8-K filings).
- Undisturbed price and current spread; implied break probability `= (spread vs. downside gap)` solved from the EV equation.
- Regulatory calendar: HSR waiting periods and second requests, CFIUS review windows, EU Phase I/II, sector regulators (FDA, FCC, NRC).
- Proxy/vote data and advisor recommendations (ISS, Glass Lewis move spreads).
- Options skew on the target -- the put market prices break risk and is a consensus check.
- Stock-borrow availability and cost on the acquirer (stock deals).

| Infrastructure | Why |
|-----------|-----|
| [[prime-broker]] relationship | Stock borrow for shorting acquirer / hedging convert |
| Deal-tracking data (Dealogic, Bloomberg M&A) | Spread, probability, and timing analytics |
| Legal expertise on-call | Merger agreements, MAC clauses, Delaware case law |
| Regulatory modeling | HSR, CFIUS, EU, FDA, FCC, NRC review probabilities |
| Financing-market read | LBO debt markets, syndicated loan health |
| Proxy advisor monitoring | ISS, Glass Lewis recommendations move spreads |

## Example trade

**Stylized mechanics**: Company A agrees to acquire Company B at $100/share cash; B trades at $97 post-announcement. The $3 gap is the **deal spread**:

```
annualized_return = (deal_spread / target_price) * (365 / days_to_close)
```

A $3 spread on $97 closing in 90 days = ~12.5% annualized. If the deal breaks, the target typically falls back to its *undisturbed* pre-announcement price (sometimes lower) -- a $15-30 gap down. Expected value:

```
EV = P(close) * deal_spread - P(break) * downside_gap - financing_costs - borrow_cost (if shorting acquirer)
```

**Real case -- Microsoft/Activision**: Microsoft agreed in January 2022 to acquire Activision Blizzard for $95.00/share cash. Because the FTC sued to block (December 2022) and the UK CMA initially blocked (April 2023, later accepting a restructured deal), ATVI spent much of 2022 trading in the mid-$70s -- a 20%+ gross spread, enormous by historical standards. An arb buying at ~$76 in mid-2022 who correctly handicapped the regulatory endgame collected $95 at the October 2023 close: ~25% gross over ~15 months (~19% annualized) for bearing real, highly publicized break risk. Arbs who sized the same trade off the spread instead of the ~$20 downside gap to the undisturbed price were carrying far more break risk than they thought.

## Performance characteristics

- **Academic baseline**: Mitchell & Pulvino (2001, *Journal of Finance*), on 4,750 deals 1963-1998, find passive risk-arb portfolios earn ~4% annual excess return before transaction costs, with returns resembling writing uncovered index puts -- near-zero beta in flat/rising markets, materially positive beta in sharp declines.
- **Modern era**: dedicated merger-arb annualized returns have compressed to ~4-7% (vs. 10-15% in the 1980s-90s) as multi-strat pods crowded the trade. Historical Sharpe for diversified books is roughly 0.7-1.0, flattered by smooth marks between event dates.
- **Cost overlay**: commissions and spread-crossing on entry/exit plus acquirer borrow (stock deals) typically cost 20-50 bps per deal round trip; on a 200-400 bps gross spread this is material, which is why `breakeven_cost_bps: 50` -- deals with gross spreads under ~1% are uneconomic for most books after costs and carry.
- **Skew**: hit rates of 85-95% deal completion with single-break losses of 5-15x the per-deal spread. The return distribution is the strategy; do not annualize a good quarter.

## Capacity limits

Risk arb is one of the higher-capacity arbitrage families -- industry-wide dedicated capital is in the tens of billions -- but per-deal capacity binds: in a $2B-market-cap target, the arb community collectively ends up holding a large share of the float, and a single fund moving >$50-100M into one mid-cap spread moves the spread against itself. A diversified single-manager book runs $1-5B before it is forced into only the largest deals (where spreads are tightest and crowding worst). Frontmatter `capacity_usd` is set at $1B as a conservative single-book figure. At small size ($250K-$10M) capacity is a non-issue; the constraint is analytical labor, not market impact.

## What kills this strategy

- **Regulatory regime shifts**: 2021-2024 FTC/DOJ under Lina Khan blocked / challenged more deals ([[kroger-albertsons]], announced 2022 and ultimately blocked; Microsoft-Activision challenged 2022-23) widening spreads then whipsawing arbs.
- **Financing markets close**: cash deals with financing contingencies (2008 [[credit-crisis]]) see mass deal breaks; numerous 2007-08 LBOs (Harman, SLM/Sallie Mae, Clear Channel) saw spreads blow out as debt markets froze.
- **Crowding**: spreads compress below fair risk premium because too many multi-strat pods chase the same deals; in a stress event the crowd unwinds together and spreads gap wider on every deal simultaneously (correlation goes to 1 -- the [[ltcm-collapse-1998]] lesson).
- **Black-swan deal breaks**: [[allergan-pfizer]] broken 2016 by Treasury inversion rules (15%+ one-day gap); [[qualcomm-nxp]] broken 2018 when China's MOFCOM withheld approval; [[att-tmobile]] broken 2011 by DOJ suit.
- **Compliance failure**: the historical record below shows the strategy's proximity to material non-public information has repeatedly destroyed practitioners.

See [[failure-modes]] for the general taxonomy.

### Famous blow-ups and lessons

- **Boesky 1986-87** -- [[ivan-boesky]] settled with the SEC in November 1986 for $100M ($50M disgorgement + $50M penalty), pleaded guilty, and was sentenced to 3 years in prison (served about 2). He informed on Michael Milken ([[drexel-burnham]]). Catalyst for the modern compliance regime.
- **Long-Term Capital 1998** -- [[ltcm-collapse-1998]] included a large merger-arb book; correlation with everything else in the fund killed them.
- **2007-2008 financing break** -- numerous LBOs (Harman, SLM, Clear Channel) saw spreads blow out as debt markets froze.
- **Valeant-Allergan 2014** -- [[bill-ackman]]'s co-bidder structure raised insider-trading questions; litigation settled 2017 for $290M.
- **Pfizer-Allergan 2016** -- Treasury changed inversion rules mid-deal; 15%+ one-day gap.
- **Archegos 2021** ([[archegos-blowup-2021]]) -- not risk arb per se, but the convertible-arb / cap-structure unwind through [[total-return-swap]] structures rippled through prime-broker books that warehouse risk-arb trades.

## Kill criteria

- Single deal break costing > 5% of NAV → halve gross exposure pending process review (sizing discipline failed).
- ≥ 3 deal breaks in any rolling 12 months where realized break frequency exceeds 2x the modeled probability → stop new positions; the handicapping model is broken.
- Rolling 24-month net return < T-bills + 100 bps → the book is not being paid for the skew; derisk or retire.
- Median annualized gross spread across the investable universe < Fed funds + 150 bps → stand down until spreads normalize (crowding has eaten the premium).
- Aggregate exposure to a single regulatory theme breaching the 15% NAV cap → forced trim regardless of conviction.

## Advantages

- Returns driven by deal outcomes, not market direction -- low beta in normal conditions.
- High base-rate of success (85-95% of definitive deals close) gives smooth carry between events.
- Analytical edge is durable: legal/regulatory handicapping does not decay the way signal-based edges do.
- Scales across a deep, constantly refreshing deal calendar; diversifiable across sectors and jurisdictions.
- Spread widens (opportunity improves) exactly when forced sellers appear -- the strategy is paid more in dislocations, if you have dry powder.

## Disadvantages

- Severe negative skew: short-put profile; a single break can erase a year of spread income.
- Hidden market beta that appears precisely in crashes (1998, 2008, March 2020), when financing breaks and deal flow stops simultaneously.
- Labor- and expertise-intensive; the edge is in legal and regulatory judgment that cannot be fully systematized.
- Crowded: multi-strat pods have compressed spreads to historically thin levels; returns ~4-7% annualized vs. 10-15% historically.
- Proximity to MNPI creates career-ending compliance risk (the entire Boesky era).
- Capital-inefficient at small scale: proper diversification needs 10+ concurrent deals.

## Historical context

Risk arb as a distinct discipline was institutionalized on Wall Street in the mid-20th century (Gus Levy at [[goldman-sachs]], Guy Wyser-Pratte at Bache) but became notorious in the 1980s LBO boom.

| Era | Figures | Vehicle | Outcome |
|-----|---------|---------|---------|
| 1980s LBO boom | [[ivan-boesky]], Marty Siegel, Dennis Levine | Ivan F. Boesky & Co. | Boesky settled with SEC Nov 1986 ($100M: $50M disgorgement + $50M penalty); pleaded guilty; sentenced to 3 years for [[insider-trading]]. Informed on Michael Milken ([[drexel-burnham]]) |
| 1980s-90s mainstream | Goldman Arbitrage Desk (Robert Rubin, Robert Freeman), Bear Stearns, [[bear-wagner]] | Prop desks | Rubin later Treasury Secretary; Freeman pled guilty 1989 to mail fraud tied to arb trades |
| 2000s boutiques | [[john-paulson]] (Paulson & Co. pre-"Big Short"), Richard Perry (Perry Capital), [[farallon-capital]] | Event-driven hedge funds | Paulson built Paulson & Co. primarily on merger arb 1994-2006 before the [[big-short-2008]] subprime trade |
| Modern | [[millennium-management]], [[citadel]], [[balyasny]], Davidson Kempner, HBK, Pentwater, Sachem Head, Kellner | Multi-strat pods and dedicated event funds | Compressed spreads; annualized returns ~4-7% vs. historical 10-15% |

The Boesky era is the cautionary tale: "risk arb" became a euphemism for insider-trading operations where the arbitrageur paid for advance knowledge of deals. Modern risk arb is heavily regulated, with Rule 10b5-1 plans, information-barrier requirements, and compliance oversight that did not exist in the 1980s.

## Taxonomy

The risk-arb family organized by the type of corporate event being traded.

### Merger & Acquisition Arbitrage

| Strategy | Description | Typical Spread | Key Risk |
|----------|-------------|----------------|----------|
| [[merger-arbitrage]] | Long target, (short acquirer for stock deals); profit on deal close | 1-8% gross; 4-15% annualized | Deal break, timing extension |
| [[tender-offer-arbitrage]] | Tender shares to acquirer at fixed price; arb the pre-tender spread | 0.5-3% | Pro-ration, withdrawal, MAC clause |
| [[hostile-takeover-arbitrage]] | Trade bid / counter-bid dynamics in contested deals | Variable; 5-20% potential | Bid failure, poison-pill deployment |
| [[stub-trading]] | Trade the "stub" equity value after partial acquisitions | Variable | Liquidity collapse |

### Equity Capital Event Arbitrage

| Strategy | Description | Typical Spread | Key Risk |
|----------|-------------|----------------|----------|
| [[spac-arbitrage]] | Buy SPAC units near trust value; redeem at NAV if no deal, participate if good | Trust-NAV discount + warrant optionality | Opportunity cost, warrant decay |
| [[rights-issue-arbitrage]] | Trade nil-paid rights vs. underlying during rights offer window | 2-10% per event | Underwriter pricing, short-squeeze on nil-paids |
| [[corporate-action-arbitrage]] | Spin-offs, splits, special dividends, share consolidations | Highly variable | Forced-index selling, inclusion/exclusion flows |
| [[secondary-offering-arbitrage]] | Short into announced secondaries, cover at deal price | 2-5% | Deal pull, cornered borrow |
| [[dutch-auction-tender-arbitrage]] | Participate in Dutch-auction buybacks at edge of clearing range | 1-3% | Pro-ration, clearing uncertainty |

### Capital Structure & Credit Arbitrage

| Strategy | Description | Typical Spread | Key Risk |
|----------|-------------|----------------|----------|
| [[convertible-arbitrage]] | Long convertible bond, short underlying equity; isolate vol + credit | 4-10% annual | Vol collapse, credit blow-up (e.g., [[archegos-blowup-2021]] tangential), financing shutoff |
| [[capital-structure-arbitrage]] | Long one layer (bonds, pref), short another (equity, CDS); bet on structural mispricing | Variable | Model risk, correlation break |
| [[distressed-debt-arbitrage]] | Buy distressed bonds / loans; recover via restructuring or Chapter 11 | 10-30% annualized targets | Process risk, plan confirmation |
| [[cds-bond-basis-arbitrage]] | Trade the gap between cash bond spreads and CDS spreads | 20-100bp | Basis widening (2008 taught this lesson) |

### Legal & Regulatory Event Arbitrage

| Strategy | Description | Typical Spread | Key Risk |
|----------|-------------|----------------|----------|
| [[appraisal-rights-arbitrage]] | Dissent from mergers, demand judicial appraisal; bet court grants above deal price | Court discretion; 0-50% | Delaware statute interpretation, interest accrual |
| [[regulatory-approval-arbitrage]] | Trade the probability distribution of antitrust / FDA / FCC approvals | Variable | Political risk, review extension |
| [[class-action-arbitrage]] | Trade around securities litigation outcomes | Event-specific | Settlement discount |

### Risk / Return / Capital Comparison

| Strategy | Risk Level | Expected Return | Capital Required | Time Horizon | Complexity |
|----------|-----------|-----------------|------------------|--------------|------------|
| [[merger-arbitrage]] (friendly strategic) | Low-Med | 4-8% annualized | High | Weeks-months | Medium |
| [[merger-arbitrage]] (sponsor LBO) | Medium | 6-12% annualized | High | Months | Medium-High |
| [[tender-offer-arbitrage]] | Low | 2-4% per event | Medium | Days-weeks | Low |
| [[spac-arbitrage]] (pre-deal) | Very Low | ~T-bill rate + warrant upside | Medium | Months-years | Low |
| [[rights-issue-arbitrage]] | Medium | 3-8% per event | Medium-High | Days-weeks | High |
| [[convertible-arbitrage]] | Medium | 6-12% annualized | Very High | Weeks-months | High |
| [[capital-structure-arbitrage]] | Medium-High | 8-15% annualized | Very High | Weeks-months | Very High |
| [[corporate-action-arbitrage]] | Low-Med | Event-specific | Medium | Hours-weeks | Medium |
| [[appraisal-rights-arbitrage]] | Medium | 5-20% annualized | Medium | Months-years | Very High |

## Sources

- Mitchell, M. & Pulvino, T., "Characteristics of Risk and Return in Risk Arbitrage," *Journal of Finance* 56(6), 2001 -- the canonical academic study (passive deal portfolios ≈ short index puts, ~4% annual excess pre-cost).
- Baker, M. & Savasoglu, S., "Limited Arbitrage in Mergers and Acquisitions," *Journal of Financial Economics* 64, 2002.
- Wyser-Pratte, G., *Risk Arbitrage* (Wiley, reissued 2009) -- practitioner classic.
- Stewart, J. B., *Den of Thieves* (1991) -- definitive account of the Boesky/Milken era.
- Boesky settlement and sentencing details verified via Perplexity (sonar), 2026-06-10: SEC settlement Nov 1986, $100M ($50M disgorgement + $50M penalty), 3-year prison sentence. Citations: sechistorical.org (1987 sentencing memorandum), en.wikipedia.org/wiki/Ivan_Boesky, sec.gov/news/speech/1986/112086cox.pdf.

## Related

- [[arbitrage]] -- the umbrella concept and its risk spectrum
- [[arbitrage-overview]] -- parent index
- [[event-driven-trading]] -- broader event category
- [[relative-value-arbitrage]] -- adjacent RV family (basis, capital-structure, convertible)
- [[merger-arbitrage]] -- flagship risk-arb strategy
- [[convertible-arbitrage]] -- capital-structure cousin
- [[limits-to-arbitrage]] -- why deal spreads persist instead of going to zero
- [[ivan-boesky]] -- historical figure
- [[john-paulson]] -- modern risk-arb success
- [[ltcm-collapse-1998]] -- risk-arb inside a multi-strat blow-up
- [[archegos-blowup-2021]] -- prime-broker / TRS exposure lessons
- [[edge-taxonomy]] -- where risk arb fits in the edge framework
- [[failure-modes]] -- general failure taxonomy
- [[arbitrage-backtesting-guide]] -- how to test event-driven spreads honestly
- [[arbitrage-parameter-cheatsheet]] -- concrete merger-arb entry thresholds

## Pages

```dataview
TABLE status, updated
FROM "wiki/strategies/arbitrage"
WHERE contains(tags, "event-driven") OR contains(file.name, "merger") OR contains(file.name, "spac") OR contains(file.name, "convertible") OR contains(file.name, "rights") OR contains(file.name, "tender") OR contains(file.name, "corporate-action")
SORT updated DESC
```
