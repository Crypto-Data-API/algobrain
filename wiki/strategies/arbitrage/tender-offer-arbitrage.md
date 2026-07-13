---
title: "Tender Offer Arbitrage"
type: strategy
created: 2026-04-24
updated: 2026-06-21
status: excellent
tags: [arbitrage, event-driven, stocks]
aliases: ["Tender Arb", "Proration Arbitrage", "Odd-Lot Arbitrage", "Dutch Auction Arb"]
strategy_type: hybrid
timeframe: swing
markets: [stocks]
complexity: intermediate
backtest_status: untested
edge_source: [structural, analytical]
edge_mechanism: "Tender offers create a temporary price gap between the current market price and the offered tender price. Proration in oversubscribed tenders and odd-lot exemptions produce structurally asymmetric payouts that favor small allocators over institutional shareholders."
data_required: [tender-offer-filings, shareholder-registries, odd-lot-provisions, proration-history, deal-terms]
min_capital_usd: 100000
capacity_usd: 500000000
crowding_risk: medium
expected_sharpe: 1.4
expected_max_drawdown: 0.12
breakeven_cost_bps: 20
related: ["[[merger-arbitrage]]", "[[spac-arbitrage]]", "[[odd-lot-arbitrage]]", "[[dutch-auction]]", "[[going-private]]", "[[buffett]]", "[[corporate-action-arbitrage]]", "[[proration]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[arbitrage]]"]
---

# Tender Offer Arbitrage

Tender Offer Arbitrage trades the gap between the market price of a stock and the price offered in a **tender offer** -- a public bid by an acquirer, issuer, or third party to buy a specified quantity of shares at a stated price during a stated window (typically 20-40 business days, minimum 20 business days under SEC [[regulation-14e]]). It is a specialized branch of [[risk-arbitrage]] and a close sibling of [[merger-arbitrage]]; the distinguishing feature is the *deterministic legal machinery* (proration, withdrawal rights, odd-lot exemptions, best-price rule) that replaces some of the open-ended deal uncertainty of a one-step merger. Strategies include classic risk-arb on hostile / friendly tenders, specialized plays on **Dutch auction** self-tenders, **odd-lot arbitrage** exploiting proration exemptions for holders of <100 shares, and **going-private** management buyouts. [[warren-buffett|Warren Buffett]] famously made some of his earliest professional returns running odd-lot tender arbitrage in the 1950s-60s.

### Tender offer taxonomy

| Variant | Who bids | Mechanism | Where the edge sits |
|---------|----------|-----------|---------------------|
| Cash third-party tender | Acquirer | Fixed cash price for control (often >50%) | Deal-close probability, financing risk |
| Partial / two-step tender | Acquirer | Buy X% via tender, squeeze-out remainder via back-end merger | Proration + back-end (stub) valuation |
| Issuer self-tender (fixed price) | The company | Buy back its own shares at a stated price | Participation rate, signaling, stub support |
| Dutch auction self-tender | The company | Range quoted; clears at lowest price filling the size | Forecasting the clearing price |
| Odd-lot tender | Acquirer/issuer | Holders of <100 shares exempt from proration | Near-100% acceptance vs prorated institutions |
| Exchange offer | Acquirer | Stock/securities instead of (or with) cash | Valuing the offered paper |

## Edge Source

**Structural** and **analytical**. Structural: tender rules include deterministic features (20-day minimum window, proration, odd-lot exemptions, withdrawal rights, "best-price rule") that create measurable asymmetries. Analytical: estimating deal-close probability, proration ratio, and post-tender stub value requires judgement and specialized legal / regulatory knowledge.

## Why This Edge Exists

- **Legally defined payout structure.** SEC Rule 14d-4 and 14e-1 prescribe tender mechanics, making outcomes more predictable than open-market M&A.
- **Proration.** When more shares are tendered than the acquirer wants, the offer is oversubscribed and shares are bought pro-rata. Institutional shareholders are fully prorated; retail odd-lot holders (<100 shares) are typically exempt and fully accepted. An arbitrageur who assembles many odd lots captures 100% acceptance.
- **Short tender window.** With 20 business days minimum, the arbitrageur's IRR can be very high on modest spread. A 1% spread over 4 weeks = 13%+ annualized.
- **Sophistication gap.** Many retail holders and mutual funds don't tender at all (failing to take up the offer), leaving more spread for those who do.
- **Post-tender stub risk.** For partial tenders, the non-tendered stub shares may trade at a discount. Forecasting stub value is a source of edge.
- **Who is on the other side?** Retail holders who don't act; mutual funds with tender-constrained policies; short-sellers providing liquidity.

### Tender mechanics that create asymmetry

| Rule | Source | Effect on the arb |
|------|--------|-------------------|
| 20-business-day minimum window | SEC Rule 14e-1 | Caps the holding period → high IRR on small spreads |
| Withdrawal rights | Rule 14d-7 | Holder can pull shares until expiration → optionality, can re-tender at competing bid |
| Proration | Rule 14d-8 | Oversubscribed offers buy pro-rata → institutional acceptance <100% |
| Odd-lot exemption | Offer document (discretionary) | <100-share holders accepted in full → near-100% acceptance |
| Best-price rule | Rule 14d-10 | All tendering holders get the highest price paid → no side deals |
| "Subject-to" conditions | Offer document | Minimum-tender, financing, regulatory, MAC conditions → deal-break risk |

## Null Hypothesis

In a frictionless market, stock price jumps instantly to tender price minus risk-adjusted discount for deal failure. Proration is neutral because everyone is treated equally. A random-no-edge world shows tender spreads = pure deal-failure probability × (price − pre-deal price), with zero excess return to informed participation.

## Rules

**Classic partial / cash tender.**
1. Tender announced at $P_tender vs current market $P_market, with a specified percentage to be bought (e.g. 40% of float).
2. Enter long at $P_market if `(P_tender − P_market) / P_market × (365 / days) > hurdle_rate + deal_risk_premium`.
3. Forecast **expected proration ratio**: based on float, institutional vs retail holding, and historical tender response rates for similar deals.
4. Expected payoff = proration × P_tender + (1 − proration) × estimated_stub.

**Odd-lot arbitrage variant.**
1. Identify tender offers that exempt odd-lot holders (shareholders of < 100 shares).
2. Open multiple small accounts or use family/friends as holders (legally -- each must be a beneficial owner).
3. Purchase < 100 shares per account and tender in each. 100% acceptance vs ~30-60% for institutional.

**Dutch auction self-tender.**
1. Issuer announces a price range (e.g. $45-$50) and will buy the minimum number of shares needed at the lowest clearing price.
2. Analyze likely clearing price from order flow and past patterns.
3. Tender at the expected clearing price to maximize acceptance probability while capturing spread.

**Exit.** Shares accepted for tender settle in cash at tender close. Any unaccepted shares held for stub value, typically sold on the open market post-close.

## Implementation Pseudocode

```python
for tender in active_tenders:
    P_t = tender.offer_price
    P_m = market_price(tender.ticker)
    days = (tender.expiration - today).days
    shares_sought = tender.pct_of_float * float(tender.ticker)
    institutional_holding = inst_holdings(tender.ticker)
    proration_est = min(1.0, shares_sought / estimated_tender_response(tender))
    stub_est = model_stub_value(tender)
    expected_payoff = proration_est * P_t + (1 - proration_est) * stub_est
    spread = (expected_payoff - P_m) / P_m
    irr = spread * 365 / days
    deal_risk = legal_regulatory_risk_score(tender)
    if irr > 0.10 + deal_risk:
        buy(tender.ticker, size=capital_per_position)
        submit_tender_instruction(tender, shares=position_size)
    # For odd-lot exemption:
    if tender.has_odd_lot_exemption:
        for subaccount in sub_accounts:
            buy_at_most_99_shares(tender.ticker, subaccount)
            tender_in_each(subaccount)
```

## Indicators / Data Used

- Tender offer statements on Schedule TO (SEC EDGAR)
- Shareholder composition (13F filings, 13G, 13D)
- Historical proration rates for similar tenders
- Stub value estimation (DCF, trading comps for remaining business)
- Regulatory / antitrust timeline
- Odd-lot exemption language in offer document

## Worked Example

The following are real, documented deals used to *illustrate the mechanics*. Dollar figures are historical deal terms, not backtested strategy returns.

**Warren Buffett's early odd-lot tenders (1950s-1960s).** Buffett, in his partnership letters and the Snowball biography, describes systematic odd-lot tender arbitrage as a staple of his early practice. Because tender offers in the 1950s-60s frequently had odd-lot provisions allowing holders of less than 100 shares to avoid proration, Buffett would spread small purchases across many accounts and tender each separately, capturing the full spread with near-100% acceptance. Annualized returns on the small capital dedicated to these "workout" positions were very high — figures in the 30%+ range are commonly cited from the partnership-letter era, though Buffett reported workouts in aggregate rather than odd-lot tenders separately.

**[[rjr-nabisco]] 1988.** In the iconic contest for RJR Nabisco, KKR's winning bid was ~$109 per share in cash and securities (November 1988). Risk-arbitrage desks earned what was at the time one of the largest single-deal arbitrage profits on record: the stock traded in the high-$80s to ~$90 during the bidding war — a wide spread to the $109 headline value — reflecting financing risk and uncertainty over the value of the PIK-preferred and convertible securities component.

**Coca-Cola Consolidated Dutch auction (2024).** COKE (the bottler, not KO) launched a modified Dutch auction self-tender for up to $2.0 bn of its shares at a range of $850-$925. Dutch auction self-tenders like this require arbitrageurs to forecast the clearing price from holder composition and tender-response patterns: tender too low and you give up spread; tender above the clearing price and you get zero acceptance.

**Herbalife modified Dutch auction (2014).** A modified Dutch auction tender offer for HLF shares in 2014, associated with [[carl-icahn|Carl Icahn]]'s position in the stock, covered up to ~11 million shares at a range of $55-$63, with the final price set at the lowest level clearing the offer. Arbitrageurs had to weigh [[bill-ackman|Ackman]]'s public short campaign as a factor that could depress the clearing price or the post-tender stub.

**Dell going-private 2013.** Michael Dell and Silver Lake's $24.4 bn take-private was structured as a **one-step merger requiring a shareholder vote**, not a tender offer — a useful contrast case for tender arbitrageurs. The deal price was raised from $13.65 to $13.75 plus a $0.13 special dividend (~$13.88 total consideration) after Icahn mounted an opposition campaign; spreads widened sharply during the proxy fight and patient arbitrageurs earned a final-leg return of several percent once the revised record date and Icahn's retreat cleared the path to the September 2013 vote. (The Delaware appraisal litigation later found fair value of $17.62, a separate post-close story.)

## Performance Characteristics

These are *risk/return characteristics of the deal structure and of published risk-arbitrage benchmarks*, not a backtest of this page's rules. The dominant feature is negative skew: many small wins, occasional large losses on deal breaks.

- **Typical deal spread**: 50-300 bps depending on deal risk and tender duration.
- **Annualized IRR on deployed capital**: high relative to the gross spread because the window is short — a 1% spread captured over a 4-week (20-business-day) tender annualizes to ~13%+ *before costs and deal-break losses*.
- **Published risk-arb benchmark Sharpe**: Mitchell & Pulvino (2001) characterize the risk/return of risk arbitrage as resembling a written index put — positive returns most of the time, sharp losses in market declines. Tender arb inherits this profile.
- **Hit rate**: the large majority of announced tenders close, but proration ratios vary widely (30-100%), so realized return is path-dependent on participation.

### Cost stack (what the gross spread must survive)

| Cost component | Magnitude | Notes |
|----------------|-----------|-------|
| Equity bid-ask | 2-10 bps | Worse for thin / small-cap targets |
| Commission per tender instruction | flat fee per account | Dominates the odd-lot variant (many accounts) |
| Stub liquidation slippage | variable | Selling the un-tendered residual post-close |
| Legal / regulatory analysis | fixed overhead | Per-deal labor, not bps |
| Deal-break tail loss | 20-40% per position | The figure that determines true expectancy |

The first four are modest; the fifth dominates expectancy. A program that captures 1-2% per deal on a high close-rate can still be net-negative if its break rate creeps up, because each break erases the gains from many successful deals.

## Capacity Limits

Per-deal capacity is limited by the tender's target size -- a $500 mm tender with expected 50% proration caps one arbitrageur at ~$50-100 mm without moving market. Strategy-level capacity across all active tenders: $500 mm - $2 bn for a dedicated fund. Odd-lot variant is *micro-capacity* -- tens of thousands of dollars per account, but can scale across many accounts (legal / ethical / tax limits apply).

| Variant | Per-deal capacity | Binding constraint |
|---------|-------------------|--------------------|
| Large cash/partial tender | $50-100 mm | Target size × proration |
| Dutch auction self-tender | $10-100 mm | Clearing-price uncertainty |
| Odd-lot program | tens of $k per account | Beneficial-ownership / per-account limits |
| Dedicated fund (all active tenders) | $500 mm - $2 bn | Deal flow, not impact |

## What Kills This Strategy

- **Deal break.** Financing falls through, antitrust block, board change of heart. Stock collapses to pre-deal level producing 20-40% loss per position.
- **Proration miscalculation.** If retail response is much higher than expected, institutional proration drops and stub value gap widens.
- **Legal structure changes.** SEC eliminating odd-lot exemptions (proposed but not adopted) would end the odd-lot variant.
- **Post-tender stub collapse.** For partial tenders, the un-tendered stub can trade far below expected; stubs have historically traded 20-30% below intrinsic after large successful tenders.
- **Litigation delays.** Class-action suits by aggrieved shareholders can extend deal timelines, crushing IRR.
- **Regulatory investigation.** Hart-Scott-Rodino second requests, CFIUS review, or foreign regulator delays (especially China MOFCOM post-2014).
- See [[failure-modes]].

## Kill Criteria

- Deal break rate over trailing 12 months > 15%.
- Average deal duration > 150% of initial estimate.
- Drawdown > 10% from high-water mark.
- Regulatory announcement eliminating odd-lot exemptions or best-price rule.

## Advantages

- Short, defined holding periods produce high IRRs on deployed capital.
- Legal structure provides clear outcome framework.
- Odd-lot variant offers near-arbitrage returns for retail-scale capital.
- Uncorrelated with broad equity market direction.
- Clear audit trail and documentation via SEC filings.

## Disadvantages

- Binary risk per deal: 2-5% gain vs. 20-40% loss on break.
- Labor-intensive legal and regulatory analysis per deal.
- Odd-lot strategy has scale limits and operational complexity (multiple accounts).
- Stub valuation is subjective and often disappointing in practice.
- Competition from dedicated risk-arb desks compresses spreads on large deals.

## Sources

- Schwert, G.W. (2000). "Hostility in Takeovers: In the Eyes of the Beholder?" *Journal of Finance*.
- Jindra, J. and Walkling, R. (2004). "Speculation Spreads and the Market Pricing of Proposed Acquisitions." *Journal of Corporate Finance*.
- Mitchell, M. and Pulvino, T. (2001). "Characteristics of Risk and Return in Risk Arbitrage." *Journal of Finance*.
- Buffett Partnership Letters (1957-1969).
- Alice Schroeder, *The Snowball: Warren Buffett and the Business of Life* (2008).
- SEC Regulation 14D and 14E.
- Verified via Perplexity (sonar), 2026-06-10: KKR's RJR Nabisco winning bid ~$109/share cash + securities with stock trading high-$80s-$90 during the contest (confirmed); Dell 2013 was a one-step merger raised $13.65 → $13.75 + $0.13 special dividend (confirmed); HLF 2014 modified Dutch auction ~11M shares at $55-$63 (confirmed); a claimed 2008 Coca-Cola (KO) Dutch auction could NOT be verified and was replaced with Coca-Cola Consolidated's 2024 $2.0bn tender at $850-$925.

## Related

- [[merger-arbitrage]]
- [[risk-arbitrage]]
- [[spac-arbitrage]]
- [[odd-lot-arbitrage]]
- [[dutch-auction]]
- [[going-private]]
- [[buffett]]
- [[corporate-action-arbitrage]]
- [[buyback-arbitrage]]
- [[proration]]
- [[limits-to-arbitrage]]
- [[edge-taxonomy]]
- [[failure-modes]]
- [[arbitrage]]
