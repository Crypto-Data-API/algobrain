---
title: "Dutch Auction Tender Arbitrage"
type: strategy
created: 2026-04-26
updated: 2026-06-21
status: excellent
tags: [arbitrage, stocks, event-driven]
aliases: ["Dutch Tender Arb", "Modified Dutch Auction Arbitrage", "Self-Tender Arb"]
related: ["[[tender-offer-arbitrage]]", "[[risk-arbitrage]]", "[[corporate-action-arbitrage]]", "[[buyback-arbitrage]]"]
strategy_type: hybrid
timeframe: swing
markets: [stocks]
complexity: intermediate
backtest_status: live
edge_source: [structural, analytical, risk-bearing]
edge_mechanism: "In a modified-Dutch-auction self-tender (issuer buyback), shareholders submit price-quantity offers within a stated range. Pro-ration risk and clearing-price uncertainty create a discount between current market price and the auction's likely clearing price; arbs price this gap and tender at marginal-acceptance prices."
data_required: [tender-offer-documents, holder-concentration, historical-tender-clearing-data, options-skew]
min_capital_usd: 500000
capacity_usd: 500000000
crowding_risk: low
expected_sharpe: 1.5
expected_max_drawdown: 0.05
breakeven_cost_bps: 80
decay_evidence: "Strategy stable since 1990s — Dutch-tender mechanics unchanged. Annual flow concentrated around $200-500B in announced buybacks globally."
---

# Dutch Auction Tender Arbitrage

Trading the pricing dynamics of **modified Dutch auction tender offers** — a buyback structure where the issuing company invites shareholders to tender shares at any price within a stated range (e.g. $42-$47), then determines the lowest single price at which the desired share count is achieved. All accepted shares clear at that single price; tendered shares above the clearing price are rejected. First used by Todd Shipyards in 1981, the structure has since been used by hundreds of mid- and large-cap issuers (Herbalife, Designer Brands, WEX, Wix.com) for concentrated capital return, and occasionally by activists' targets to fend off takeovers. Note that the largest mega-cap repurchasers (Apple, JPMorgan, IBM) generally use open-market repurchases and accelerated share repurchases (ASRs), not Dutch tenders.

This is an [[event-driven]] / [[corporate-action-arbitrage]] strategy in the same family as [[tender-offer-arbitrage]], [[risk-arbitrage]], [[buyback-arbitrage]], and the supply-side mirror [[secondary-offering-arbitrage]]. Where a secondary forces *new supply* into the market at a discount, a Dutch tender *removes supply* at a single clearing price — the arb captures the gap between the depressed market price during the tender window and the expected clearing price.

> **The core mechanic in one line.** During the 4–6 week tender window the stock trades at a discount to the price the issuer is likely to pay (because completion and pro-ration are uncertain); the arb buys at that discount, tenders at a price near the bottom of the range to guarantee acceptance, and collects the clearing price. The edge is the discount; the risk is pro-ration (you sell fewer shares than expected and keep an unwanted residual at market) and the deal being repriced or pulled.

## Edge Source

**Structural** + **analytical** + **risk-bearing** (see [[edge-taxonomy]]).

- **Structural:** Tender mechanics force a single clearing price; submitters who guess wrong (too high or too low) get rejected or get full pro-ration.
- **Analytical:** Probabilistic clearing-price estimation requires understanding of holder concentration, expected tender participation, and pro-ration logic.
- **Risk-bearing:** The 4-6 week tender window includes mark-to-market path risk.

| Edge dimension | Present? | Mechanism |
|---|---|---|
| Structural | Primary | Single-clearing-price auction + completion uncertainty depress the stock below expected pay price |
| Analytical | Primary | Modeling clearing price from holder concentration, free float, and participation is the core skill |
| Risk-bearing | Primary | 4–6 week mark-to-market path risk + pro-ration residual risk |
| Informational | Secondary | 13F holder concentration and prior-tender behavior inform participation estimates |
| Behavioral | Weak | Counterparty includes index funds and passive holders who under-tender or mis-price the option |
| Latency | No | Multi-week swing horizon; speed is not the edge |

## Why This Edge Exists

Mechanics:
1. Issuer announces tender for X shares at price range [P_low, P_high].
2. Shareholders submit "price tenders" (specific price within range) or "no price" tenders (accept any price within range).
3. At expiration: issuer aggregates tendered shares and finds the lowest price P* where Σ shares tendered at ≤ P* ≥ X shares.
4. All shares tendered at ≤ P* are bought at P* (single clearing price). If oversubscribed at P*, pro-ration applies.

The arbitrage: stock typically trades at a discount to the upper end of the range during the tender window (because the deal isn't certain to close). Arbs buy at the discount and tender at marginal-acceptance prices ($P_low+0.01 to be safe; or higher with bias on clearing).

Variants:

1. **Buy-and-tender** — buy in the open market, tender at low end of range, capture the spread.
2. **Pre-tender accumulation** — buy weeks before the tender announces, tender into the offer.
3. **Reject-the-deal short** — short into the announcement if you believe the deal pulls or terms widen.

## Null Hypothesis

In an efficient market, stock would trade at the expected clearing price discounted only by the tender-failure probability and the time value of money over the window. Empirically, stocks trade 2-5% below this fair value during the tender window — a small but persistent arb. Under the null, that 2–5% is *exactly* compensation for pro-ration risk (you tender 100 shares, get 60 bought, and are left holding 40 at a lower post-tender market price) plus completion risk, leaving zero excess return. The test is whether, across many tenders, the realized clearing price minus entry minus the cost of the pro-rated residual is reliably positive net of the few deals that get pulled or repriced.

## Rules

1. On tender announcement: read SC TO-I form, identify range, target shares, expiration.
2. Estimate clearing price: model holder concentration, free float, expected participation rate.
3. Buy stock at market discount to expected clearing.
4. Submit tender at $P_low + small buffer to ensure acceptance.
5. Hold any rejected shares (rare) for sale post-expiry.
6. If pro-rated: keep retained shares as residual position.

## Implementation Pseudocode

```python
on dutch_tender_announced(ticker, range_low, range_high, target_shares, expiration):
    holders = get_13f_holders(ticker)
    expected_participation = model_participation_rate(holders, range_high)
    expected_clearing = solve_clearing_price(target_shares, expected_participation, range_low, range_high)
    market_price = market.price(ticker)
    if expected_clearing - market_price > 80bp:
        size = target_shares * 0.001  # don't move the auction
        buy(ticker, size, market_price)
        on expiration - 2_days:
            tender(ticker, size, price=range_low + 0.01)
        on expiration:
            collect_proceeds()
```

## Indicators / Data Used

- SC TO-I tender offer documents (SEC EDGAR).
- 13F holder data (concentration analysis).
- Historical tender clearing prices (for similar issuers' prior tenders).
- Options skew within tender window.
- Tender depository reports (typically published in last 48 hours).

## Example Trades

**Todd Shipyards (1981)** — the first modified Dutch auction self-tender, the prototype studied in the academic literature (Bagwell 1992).

**Herbalife (2018)** — modified Dutch auction tender for roughly $600M with a stated price range around $98-$108; heavily covered because of the concurrent Icahn/Ackman saga. Typical arb pattern: stock traded inside the range during the window; tendering at the low end ensured acceptance.

**Designer Brands (2023)** — modified Dutch auction tender for up to $100M of Class A shares; representative of the mid-cap deals that dominate current flow.

**WEX Inc. (2025)** — modified Dutch auction tender for up to $750M at a $148-$170 range.

**Wix.com (2026)** — modified Dutch auction tender for up to $1.75B at an $80-$92 range; the stock traded toward the lower half of the range during the window, the classic discount that buy-and-tender arbs capture.

**Activist-defensive tenders (various)** — companies under activist pressure have used self-tenders to consolidate control or return cash defensively. Arbs are less keen on these — tenders are occasionally repriced or pulled mid-window.

## Performance Characteristics

Annualized 5-12% net of costs for dedicated tender arb desks (rare standalone strategy; usually a sub-allocation in multi-strat or risk-arb portfolio). Sharpe 1.5-2.5 in deal-rich years due to short windows and low directional risk; the conservative through-cycle expectation is ~1.5 because deal flow is lumpy and capital sits idle between tenders. Realistic cost overlay: 5-15 bps round-trip in liquid names, plus mark-to-market path risk over the 4-6 week window.

> **Data disclaimer.** These return/Sharpe figures are practitioner ranges, not a wiki-verified backtest. The academically grounded facts are the *structure and shareholder-heterogeneity effects* (Bagwell 1992; Comment & Jarrell 1991), not net strategy returns. Capital idleness between deals materially lowers realized through-cycle returns versus the in-deal figures.

| Characteristic | Profile |
|---|---|
| Holding period | 4–6 weeks per event, defined exit at expiry |
| Return shape | Steady small gains, occasional loss on pulled/repriced deals |
| Idle-capital drag | High — lumpy deal flow leaves capital uninvested between tenders |
| Directional exposure | Low; hedge-able with sector ETF |
| Main residual risk | Pro-ration stub + 4–6 week mark-to-market path |

## Capacity Limits

Per-event $5-100M depending on tender size and expected clearing differential. Annual flow ~$50-100B in Dutch-tender buybacks globally; only fraction is arb-able.

## What Kills This Strategy

- **Channel substitution:** issuers shift to open-market repurchases or accelerated share repurchases (ASRs), which have no single-clearing-price arb window — the dominant secular threat, as mega-caps already prefer ASRs.
- **Deal pulled or repriced:** rare but possible, especially in activist-defensive tenders, and it produces the strategy's worst path.
- **Crowding:** multi-strat pods piling into the same tender compress the discount.
- **Pro-ration on concentrated holders:** when a few large holders tender heavily, the arb's fill is small and the residual stub trades down post-expiry.

| Failure mode | Effect | Mitigation |
|---|---|---|
| Issuer uses ASR / open-market buyback instead | No arb window | Focus on the mid-cap names that still favor Dutch tenders |
| Tender pulled / repriced mid-window | Mark-to-market loss on the long | Avoid activist-defensive tenders; size for the tail |
| Heavy pro-ration | Small fill + unwanted residual stub | Model holder concentration; assume conservative participation |
| Crowding compresses discount | Edge → completion-risk premium only | Be selective; demand a discount above ~80 bp to costs |
| Mark-to-market path risk over 4–6 weeks | Drawdown before clearing | Optionally hedge with sector ETF; cap window exposure |

## Kill Criteria

- Average spread (entry discount to expected clearing) compression below 50 bp.
- Cumulative drawdown >5% of allocated capital.
- Two or more pulled/repriced deals in a rolling sample (terms-risk regime worsening).
- Dutch-tender deal flow falls to the point capital sits idle and the sleeve cannot meet its hurdle.

## Advantages

- Short holding period relative to most [[event-driven]] trades (4–6 weeks, defined exit).
- Highly predictable, rules-based mechanics (single clearing price, published depository reports).
- Low directional exposure; hedge-able with a sector ETF.
- Stable since the 1990s — the mechanics have not changed, so the playbook generalizes across decades.

## Disadvantages

- Limited per-event size; the strategy is deal-flow gated and capital sits idle between tenders.
- Pro-ration risk with concentrated holder bases leaves an unwanted residual stub.
- Niche strategy; rarely a standalone book — usually a sub-allocation in [[risk-arbitrage]] / multi-strat.
- Multi-week mark-to-market path risk before the clearing price is realized.

## Sources

- SEC Rule 13e-4 (issuer tender offers).
- Wachtell Lipton, *Buyback Considerations* memos.
- Bagwell, L. S., "Dutch Auction Repurchases: An Analysis of Shareholder Heterogeneity" (*Journal of Finance*, 1992).
- Comment, R. & Jarrell, G., "The Relative Signalling Power of Dutch-Auction and Fixed-Price Self-Tender Offers and Open-Market Share Repurchases" (*Journal of Finance*, 1991).
- Example tenders verified via Perplexity (sonar), 2026-06-10 — including Herbalife 2018, Designer Brands 2023, WEX 2025 ($148-$170, $750M), Wix.com 2026 ($80-$92, $1.75B). Citations: ir.wexinc.com, prnewswire.com (Designer Brands), wix.com press room / globenewswire.com.

## Related

[[tender-offer-arbitrage]] · [[risk-arbitrage]] · [[corporate-action-arbitrage]] · [[buyback-arbitrage]] · [[merger-arbitrage]] · [[secondary-offering-arbitrage]] · [[event-driven]] · [[multi-leg-arbitrage]] · [[edge-taxonomy]] · [[failure-modes]]
