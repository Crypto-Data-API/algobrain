---
title: "SPAC Arbitrage"
type: strategy
created: 2026-04-24
updated: 2026-06-21
status: excellent
tags: [arbitrage, event-driven, stocks, options]
aliases: ["SPAC Trust Arb", "Pre-Deal SPAC Trade", "SPAC Mafia Strategy"]
strategy_type: hybrid
timeframe: position
markets: [stocks, options]
complexity: intermediate
backtest_status: untested
edge_source: [structural, risk-bearing]
edge_mechanism: "SPAC shares have a contractual right to redeem at trust value (typically $10 + accrued interest) at the shareholder vote. Buying shares below trust gives a guaranteed floor -- effectively a zero-coupon Treasury with a free call option (warrants and deal upside). Institutional 'SPAC Mafia' funds mass-redeemed in the 2020-22 bubble and crash."
data_required: [spac-prices, trust-value-per-share, warrant-prices, redemption-deadline, sponsor-disclosures]
min_capital_usd: 500000
capacity_usd: 10000000000
crowding_risk: high
expected_sharpe: 1.5
expected_max_drawdown: 0.10
breakeven_cost_bps: 15
related: ["[[merger-arbitrage]]", "[[ipo-arbitrage]]", "[[tender-offer-arbitrage]]", "[[warrant-arbitrage]]", "[[reg-s]]", "[[pipe-financing]]", "[[chamath-palihapitiya]]", "[[corporate-action-arbitrage]]", "[[arbitrage]]", "[[edge-taxonomy]]", "[[failure-modes]]"]
---

# SPAC Arbitrage

SPAC Arbitrage exploits the structural feature that a **Special Purpose Acquisition Company (SPAC)** holds investor proceeds in a trust typically earning Treasury-bill yields and must return those proceeds to any shareholder who redeems before a business combination. A common trade is to buy SPAC shares below trust value (often $10-$10.30 per share in the 2020-22 era, $10.50+ in the 2023-25 post-reform era due to accrued interest), intend to redeem at the vote for trust value, and retain warrants and rights for free upside optionality. The strategy was nicknamed the **"SPAC Mafia"** for the small club of dedicated funds that systematically harvested this return. In the [[arbitrage]] / [[relative-value-arbitrage|relative-value]] taxonomy it is unusual: the convergence anchor is not a related instrument but a *contractual cash floor*, making the pre-deal trade closer to a synthetic short-Treasury-plus-call than to a classic two-leg [[convergence-arbitrage]]. It is a near-relative of [[merger-arbitrage]] only in its post-announcement phase.

## Anatomy of a SPAC Unit

The whole trade rests on the fact that the IPO **unit** is a bundle that can be decomposed, and the redeemable common share carries a contractual floor that the detachable warrant does not dilute.

| Component | What it is | Role in the trade |
|-----------|------------|-------------------|
| Common share (Class A) | Redeemable at trust value per share | The cash floor — the "bond" half |
| Trust | Segregated account in T-bills | Backs the redemption right |
| Warrant (1/2, 1/3, 1/4) | Right to buy at $11.50 strike | The free "call" — kept after redemption |
| Right (some structures) | Fraction of a share at de-SPAC | Minor extra optionality |
| Sponsor promote | ~20% founder shares for nominal cost | The dilution / misalignment source |

Units typically split into separately trading shares and warrants ~52 days after IPO. After the split, an arbitrageur can hold the share to redemption for the trust floor and **keep the warrant for free** — the source of the asymmetric payoff.

## The Sub-NAV Trade Math

The core return decomposition:

```
P&L  =  (trust_per_share − purchase_price)        # the sub-NAV / accretion capture
      + accrued_trust_interest_to_redemption       # T-bill yield while held
      + value_of_retained_warrant (≥ 0)            # free optionality
      + any_pre-deadline_deal-pop_gain (optional)  # sell the share rich on a deal rumor
```

Because the redemption right is contractual and the warrant payoff is bounded below by zero, the *downside* of the pre-deal trade is essentially the difference between purchase price and trust value (negative only if you overpay above trust). This is why the trade is described as **"a zero-coupon Treasury with a free call option"** — and why the dangerous deviation is paying a *premium* to trust (the 2020-21 bubble error).

## Edge Source

**Structural** and **risk-bearing**. Structural because SPAC trust proceeds are contractually held in a segregated account invested in short-term Treasuries, and every public shareholder has a non-waivable redemption right. Risk-bearing because the arbitrageur accepts time-value risk (trust deadline can extend), sponsor-dilution risk, and (minimally) trust-mismanagement risk in exchange for yield above T-bills.

## Why This Edge Exists

- **Mandatory redemption right.** Under standard SPAC charter, every public shareholder can redeem at the business-combination vote for their pro-rata share of the trust, regardless of how they vote. This is a legally enforceable cash-equivalent.
- **Warrants and rights are detachable.** SPAC units IPO at $10 and typically contain 1 common share + fractional warrants (1/2, 1/3, or 1/4 warrant, strike $11.50). Once units split (~52 days after IPO), warrants trade separately. An arbitrageur can redeem shares at $10.10 and keep warrants that may be worth anywhere from $0.10 to $2.00+.
- **Retail demand for de-SPAC deal stocks** pushes target prices above $10 on deal announcement, producing capital-gains opportunity on the share before redemption deadline.
- **Forced-seller dynamics.** At deal vote, non-redeemer fund-manager constraints (mutual funds that cannot hold post-deal target) produce discounts to trust even when deal looks good.
- **Who is on the other side?** The sponsor (who gets the "promote" -- 20% of post-IPO equity for nominal investment, incentivizing them to overpay for any target); PIPE investors; and retail who sold shares pre-deadline.

## Null Hypothesis

In a friction-free market, SPAC share price = trust value per share throughout the SPAC's life. Warrants would price as pure options on the deal probability. Under this null, arbitrage earns only the T-bill yield on the trust. Any systematic excess return therefore reflects (a) structural pricing anomalies, (b) warrant mispricing, or (c) sponsor/PIPE frictions.

## Rules

**Entry.**
1. Screen all pre-deal SPACs daily. Compute `trust_per_share` from filings (initial $10 + accumulated interest).
2. Buy units or shares whenever market price < trust value − 15 bps (rare pre-2021 but common 2022-25).
3. Compute yield-to-redemption: `(trust_per_share − price) / price × 365 / days_to_deadline`. Target > 3-month T-bill + 100 bps.
4. Split units, sell or retain warrants based on valuation.

**Post-deal-announcement decision.**
- If target is strong and trading above trust: hold through close for upside.
- If target is weak or trading near trust: elect to **redeem** at vote; keep warrants for residual optionality.
- If deal rumored to fail: hold shares for trust return, short warrants if overpriced.

**Exit.** Redemption, deal close, or SPAC wind-up at deadline.

## Implementation Pseudocode

```python
for spac in universe:
    p = price(spac)
    trust = trust_per_share(spac)
    days = days_to_deadline(spac)
    ytr = (trust - p) / p * 365 / days  # yield to redemption
    tbill_yield = treasury_3m_yield()
    if ytr > tbill_yield + 0.01 and p < trust:
        buy(spac, size=capital_allocation)
        mark_for_redemption(spac, vote_date=deal_vote_date(spac))
    # At unit split: detach warrants
    if unit_has_split(spac) and warrant_value_fair(spac) > warrant_price(spac):
        keep_warrants(spac)
    else:
        sell_warrants(spac)
```

## Indicators / Data Used

- Trust per share (from quarterly 10-Q disclosure)
- Redemption deadline (from S-1 / charter + any extension vote)
- Warrant terms (strike, expiry, redemption provisions, cashless exercise)
- Sponsor promote and lockup
- PIPE and FPA (Forward Purchase Agreement) details
- Target sector (biotech SPACs, EV SPACs, fintech SPACs had wildly different outcomes)

## Example Trade

**The 2020-2021 SPAC bonanza.** In 2020, 248 SPACs IPO'd raising $83 bn. In 2021, 613 SPACs raised $162 bn. Many traded at material premiums to trust on deal-rumor speculation (Nikola, Lucid, DraftKings, SoFi, [[chamath-palihapitiya|Chamath Palihapitiya's]] IPOC/IPOD/IPOE/IPOF). The "SPAC Mafia" funds -- Glazer Capital, Magnetar, Polar Asset Management, Millennium, Davidson Kempner, and a few dozen others -- bought at or just above trust, waited for deal-rumor pops, sold pre-deadline, and redeemed any remaining shares. Reported IRRs in 2020-2021 were **10-20% annualized** for the core trust trade, with some vintage SPACs (CCIV/Lucid) producing one-time multi-bagger returns on warrants.

**The 2022-2023 collapse.** As rates rose and retail demand for de-SPAC targets evaporated, post-deal SPAC shares collapsed (average post-deal SPAC lost ~60% by end-2022). Pre-deal SPACs, however, *did not lose money* -- the trust structure protected the trade. In fact, with rising Treasury yields boosting trust accretion, 2022-2024 became a **golden era** for pure trust-arb funds, with risk-free-equivalent yields of 4-6% on SPAC trust plus warrant optionality. Many SPACs saw 90-95% redemption rates as arbitrageurs universally redeemed, leaving sponsors with tiny float to close deals.

**Chamath's IPOF wind-up (2022).** Social Capital Hedosophia VI (IPOF) failed to find a target; in late 2022 Chamath announced the wind-up of IPOD and IPOF, returning the ~$1.15 bn IPOF trust to shareholders at roughly $10.04 per share. Arbitrageurs who had entered at $9.95 earned the ~90 bps (0.9%) trust spread plus ~2 years of warrant optionality (warrants expired worthless).

**PIPE complications.** Deals often require [[pipe-financing|PIPE financing]] -- institutional private placements to bridge post-redemption gaps. If redemptions are 90%+ (increasingly common post-2022), the PIPE needs to fund nearly the entire deal, which can fall through, causing deal to fail and triggering trust wind-up.

## Performance Characteristics

> The Sharpe and yield ranges below are practitioner expectations and published fund-disclosure ranges, not a backtest produced in this wiki. The "risk-free-equivalent" framing applies only to the pre-deal trust trade held to redemption; warrant and post-deal exposure is genuinely risky. Treat figures as qualitative.

- **Base trust yield (2020)**: T-bill + 0-50 bps when T-bills were near zero.
- **Post-2022**: T-bill (4-5%) + 50-150 bps of arb spread plus warrant optionality.
- **Historical Sharpe (dedicated SPAC funds 2015-2024)**: 1.5-2.5, nearly market-neutral.
- **Max drawdown**: typically <5% in the core trade (trust is effectively cash); warrant variance adds ~10-15% peak drawdown on diversified book.

The return is **positively skewed** in a way most arbitrage is not: the floor caps the downside near zero while the retained warrant gives a long-tail upside (CCIV/Lucid being the canonical multi-bagger). The cost stack is thin precisely because the core leg is a long-only cash-equivalent:

| Cost component | Typical range | Notes |
|----------------|---------------|-------|
| SPAC share bid-ask | 2-8 bps | tight; instruments are liquid and regulated |
| Custody / financing | ~5 bps | minimal — core leg is long-only |
| Borrow | ~0 | not needed for core trade |
| Operational | per-name | deadline/extension/redemption tracking across 100+ names |
| Opportunity cost | T-bill yield | the floor only earns the trust's T-bill rate if no warrant pops |

Net: the realized excess return over T-bills is small and crowds away in bubbles; the warrant optionality is what differentiates vintages.

## Capacity Limits

Enormous during bubbles -- $20+ bn of pre-deal SPAC trust outstanding during 2020-21. Today (post-2022) the universe shrunk to ~$10-15 bn but remains highly accessible. Per-SPAC capacity is constrained by IPO size ($100 mm - $1 bn typical); strategy-level capacity is $5-10 bn for a dedicated fund.

## What Kills This Strategy

- **Regulatory changes.** The SEC's January 2024 SPAC rules (adopted 2024-01-24, effective July 2024) tightened disclosure and aligned de-SPAC liability with traditional IPOs, cooling supply. More aggressive rules (making redemption conditional on voting) could break the trade.
- **Trust mismanagement.** Rare but possible: if trustee permits non-Treasury investments, the "guaranteed" floor is no longer guaranteed.
- **Sponsor fraud.** A handful of cases (e.g. Akazoo/Modern Media, Multiplan lawsuits) raised questions about sponsor conduct, though trust itself has always paid out.
- **Warrant redemption traps.** Some warrants can be called at $0.01 if shares trade above $18 for 20 of 30 days, wiping out warrant value if you don't exercise in time.
- **Deadline extension dilution.** Extension votes sometimes add founder shares or PIPE dilution reducing remaining economics.
- **Excess pre-deal premium.** Buying at $10.50 when trust is $10.10 -- losing money on share leg if deal fails. See [[failure-modes]].

## Kill Criteria

- Trust yield < T-bill yield (negative carry).
- Evidence of trustee deviation from Treasury investment mandate.
- Regulatory ban on redemption rights.
- Average pre-deadline SPAC price > trust + 3% (signals overheating; 2020-21 warning sign).

## Advantages

- Effectively risk-free floor from trust structure.
- Attractive yield vs. cash and Treasuries during normal regimes.
- Free optionality from warrants and post-announcement pops.
- Large capacity, high liquidity, regulated instruments.
- Works in rising-rate environments (rising trust interest).

## Disadvantages

- Returns are modest unless warrants hit; bubble-era multi-baggers are rare and cannot be underwritten.
- Operational complexity: tracking deadlines, extensions, redemption instructions across 100+ SPACs.
- Crowded strategy during bubbles -- returns compress.
- Warrant accounting and valuation is complex (especially post-2021 SEC clarification on warrant classification as liabilities).
- Sponsor incentives are badly aligned (promote payoff only if *any* deal closes), producing many bad deals.

## Sources

- Klausner, M., Ohlrogge, M., Ruan, E. (2022). "A Sober Look at SPACs." *Yale Journal on Regulation*.
- Gahng, M., Ritter, J., Zhang, D. (2023). "SPACs." *Review of Financial Studies*.
- SEC (2024). "SPAC Final Rules," Release No. 33-11265.
- Bloomberg, *Matt Levine's Money Stuff* archive on SPACs (2020-2023).
- [[glazer-capital]] investor letters (public excerpts).
- Sharpe, IRR, and spread figures above are general market knowledge and practitioner-reported ranges; no audited backtest source is ingested in this wiki for them.

## Related

- [[merger-arbitrage]]
- [[ipo-arbitrage]]
- [[tender-offer-arbitrage]]
- [[warrant-arbitrage]]
- [[pipe-financing]]
- [[chamath-palihapitiya]]
- [[corporate-action-arbitrage]]
- [[relative-value-arbitrage]]
- [[risk-arbitrage]]
- [[convergence-arbitrage]]
- [[limits-to-arbitrage]]
- [[edge-taxonomy]]
- [[failure-modes]]
- [[arbitrage]]
