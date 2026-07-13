---
title: "Rights Issue Arbitrage"
type: strategy
created: 2026-04-24
updated: 2026-06-21
status: excellent
tags: [arbitrage, stocks, event-driven, regulation]
aliases: ["Rights Offering Arbitrage", "Rights Arb", "Seasoned Equity Offering Arbitrage", "SEO Arb"]
strategy_type: hybrid
timeframe: swing
markets: [stocks]
complexity: advanced
backtest_status: naive-backtested
edge_source: [structural, behavioral]
edge_mechanism: "Rights issues are priced at a discount to spot and most shareholders are slow to act; arbitrageurs who buy the rights (or traded ex-rights shares) and hedge via short sales of the underlying capture the discount, in exchange for providing liquidity to retail holders who would otherwise let the rights lapse."
data_required: [corporate-actions-calendar, rights-prospectus, equity-borrow-rates, intraday-book]
min_capital_usd: 100000
capacity_usd: 250000000
crowding_risk: medium
expected_sharpe: 0.7
expected_max_drawdown: 0.08
breakeven_cost_bps: 40
decay_evidence: "Edge has compressed since 2008-2009 bank recap wave; modern rights issues are tighter but still exist in European and Asian markets."
related: ["[[arbitrage]]", "[[merger-arbitrage]]", "[[convertible-arbitrage]]", "[[ipo-arbitrage]]", "[[equity-capital-markets]]", "[[failure-modes]]", "[[edge-taxonomy]]", "[[dilution]]"]
---

# Rights Issue Arbitrage

A **rights issue** (or **rights offering**) is a form of seasoned equity offering in which an existing listed company issues new shares by granting existing shareholders the right to buy new shares at a discount to the current market price, in proportion to their existing holdings. Rights issues are the dominant form of equity raising in the UK, Europe, Hong Kong, and Australia (regulatory preference for pro-rata treatment), while US companies more commonly use secondary offerings or shelf placements. **Rights issue arbitrage** is an event-driven [[arbitrage]] strategy — a corporate-action cousin of [[merger-arbitrage]] and [[risk-arbitrage]] — that exploits the discount between the **ex-rights theoretical price** and the **cum-rights market price** during the short window when both the original shares and the rights trade simultaneously.

### Key terminology

| Term | Definition |
|------|------------|
| Subscription price | Discounted price at which a right-holder may buy a new share |
| Rights ratio | New shares offered per existing share (e.g., 11-for-18) |
| Record date | Holders on this date receive rights |
| Ex-rights date | Shares begin trading without the attached right (price drops by ~rights value) |
| TERP | Theoretical Ex-Rights Price — the post-issue fair price (see Null Hypothesis) |
| Nil-paid rights | The tradeable right itself, before the holder pays the subscription price |
| Rump / rump placement | Unsubscribed shares the underwriter places into the market |
| Claw-back | Provision returning institutionally-placed shares to retail right-holders who subscribe |

The strategy has roots in 19th-century London equity markets but became globally prominent during the **2008-2009 bank recapitalization wave**, when RBS, HBOS, Lloyds, UBS, Commerzbank, and others raised hundreds of billions via deeply-discounted rights issues. Notable: the **April 2008 RBS £12bn rights issue** was priced at 200p, a 46% discount to the 372p pre-announcement price; the **November 2009 Lloyds Banking Group £13.5bn rights issue** (post-HBOS acquisition, then the largest in UK history) was priced at 37p versus a market price around 90p -- arb desks that bought rights and shorted Lloyds captured enormous discounts but had to manage heavy dilution risk. In 2023-2024, European REITs and German automakers ran distressed rights issues with similar setups.

## Edge Source

**Structural** and **behavioral**. Structural: the rules of the offering create a mechanically defined discount that would be zero in a frictionless market but is persistently larger due to transaction costs, borrow availability, and retail inertia. Behavioral: 10-30% of retail shareholders let their rights lapse, selling them to professional arbitrageurs at below-fair-value prices; underwriters also dump unsubscribed shares into the market at the offering price. See [[edge-taxonomy]].

## Why This Edge Exists

Rights issues are deliberately priced at a significant discount to ensure subscription success -- underwriters (investment banks guaranteeing the offering) need retail confidence and political margin for error. The discount creates an arbitrage if you can:

1. Buy rights in the secondary market at below-fair value (because rights-trading markets are less liquid than shares)
2. Subscribe for new shares at the offering price
3. Short the underlying to hedge directional exposure
4. Unwind when new shares are delivered

The counterparty is typically a retail investor who does not understand rights mechanics and sells rights at a panic discount, or an index fund forced to sell rights it cannot use because of mandate restrictions, or the underwriter placing unsubscribed rump shares. See [[behavioral-finance]].

### Who is on the other side, and why they keep losing

| Counterparty | Why they sell rights cheap |
|--------------|----------------------------|
| Retail holder | Does not understand TERP math; lets rights lapse or panic-sells the nil-paid right |
| Index / passive fund | Mandate forbids holding/exercising nil-paid rights; mechanical sale into the rights market |
| Cash-constrained holder | Cannot fund the subscription; must sell the right rather than dilute |
| Underwriter (rump) | Contractually places unsubscribed shares; willing to clear at the offering price |

This is a [[limits-to-arbitrage]] case in miniature: the TERP gap would be zero in a frictionless market, but borrow scarcity, illiquid nil-paid rights markets, the ~2-week capital lock, and short-sale bans during crises keep professional capital from fully arbitraging it away.

## Null Hypothesis

Under frictionless-market assumptions, the cum-rights price of a share equals the weighted average of the ex-rights price and the rights value: **P_cum = P_ex + N * R**, where N is rights per share and R is the rights price. The Theoretical Ex-Rights Price (TERP) is fully determined. In practice, the share typically trades **above** its theoretical ex-rights value by 1-5% during the rights period, because shorting in size is hard and the rights market is illiquid. The null outcome is that this premium converges exactly to zero at the subscription deadline, yielding zero profit after costs.

## Rules

### Entry

1. **Screen for rights issues** with discount > 15% and offering size > 15% of pre-issue market cap (otherwise economics are too small).
2. **Read the prospectus** for subscription deadlines, record date, rights ratio, settlement date, and any withdrawal rights.
3. **Check borrow availability**: the strategy requires shorting the underlying during the rights period. If borrow is unavailable or rate is punitive (>10%), the trade is dead. Banks during 2008 were frequently impossible to borrow.
4. **Open the trade two ways**:
   - **Long rights / short shares**: buy rights in the secondary market, short an equivalent number of new shares at market price
   - **Long ex-rights shares (bought cheap) / short cum-rights shares**: exploit the price distortion during the rights window
5. **Hedge ratio** = number of new shares issuable per old share (e.g., a 3-for-4 rights issue means 0.75 new shares per old share; short 0.75 old shares per right purchased)
6. **Size** by capital available to fund rights subscription, with margin buffer for adverse stock moves during the ~2-week period

### Exit

1. **New shares delivered**: receive new shares via subscription, deliver them to close the short
2. **Unwind rights in the rights market** before subscription deadline if the arb spread collapses
3. **Underwriter rump placement**: if underwriter dumps unsubscribed rump at a discount, opportunistically buy and cover short at better price

### Position Sizing

Capital-intensive: a £10M position requires £10M of subscription capital plus margin on the short side. Size no larger than you can fund and no larger than 10% of daily average volume in the underlying (for short execution).

## Implementation Pseudocode

```python
def rights_arb_opportunity(company):
    prospectus = company.rights_prospectus
    sub_price = prospectus.subscription_price
    ratio = prospectus.new_per_old
    spot = company.intraday_price
    rights_price_mkt = company.rights_mid_market

    terp = (spot + ratio * sub_price) / (1 + ratio)
    theoretical_rights = spot - terp

    # arb if market rights price is below theoretical
    if rights_price_mkt < theoretical_rights - fees - borrow_cost:
        return {
            "action": "buy_rights_short_stock",
            "rights_to_buy": size,
            "stock_to_short": size * ratio,
            "subscription_capital": size * sub_price,
            "expected_pnl_per_right": theoretical_rights - rights_price_mkt
        }
    return None

def execute(trade):
    assert borrow_available(trade.underlying, size=trade.stock_to_short)
    buy_rights(trade.rights_to_buy)
    short_shares(trade.stock_to_short)
    subscribe_new_shares(trade.subscription_capital)
    # wait for new-share delivery (typically T+2 to T+5 post-deadline)
    deliver_new_shares_against_short()
```

## Indicators / Data Used

- Rights issue prospectus (subscription price, ratio, deadlines)
- Rights trading volume and mid-price vs TERP-implied value
- Equity borrow rate and availability on the underlying
- Short interest trend during rights period (crowding indicator)
- Underwriter identity and reputation (higher-quality underwriters often have tighter rump placements)
- [[dilution]] math: new share count, pro-forma EPS, pro-forma book value

## Example Trade

### RBS £12bn Rights Issue, April-June 2008

- **Announcement (22 Apr 2008)**: RBS announces 11-for-18 rights issue at 200p per share, raising £12bn. Pre-announcement price: 372p. Discount: 46%.
- **TERP**: (18 * 372 + 11 * 200) / 29 = **307p**. Theoretical rights value per old share = 372 - 307 = 65p (or 307 - 200 = 107p per new share).
- **Arb setup**: on 1 May 2008, rights traded in London at 102p per new share versus theoretical 107p -- a 5p per new share discount. RBS shares traded at 308p vs 307p TERP, close to theoretical.
- **Trade**: buy 1.1M rights at 102p (£1.122M subscription intent), short 1.1M new shares-equivalent at 308p. Subscribe for 1.1M new shares at 200p -- total capital tied up £1.122M + £2.2M = £3.322M.
- **Delivery (6 Jun 2008)**: new shares delivered at ex-rights date. Close short against new shares.
- **P&L calculation**: rights bought at 102p, intrinsic value at delivery ~107p -> £55,000 gross on the rights leg; short-side P&L roughly flat as stock moved in line with TERP.
- **Net**: roughly £45,000 after £10,000 of fees and financing, on £3.3M of capital, over 5 weeks -- about **1.4% gross / 14% annualized** on this single trade.
- **Cautionary note**: RBS subsequently collapsed to around 10p in January 2009; arbs who failed to close the short and retained unhedged long exposure were wiped out. This is **not** a buy-and-hold thesis.

### Lloyds Banking Group 2009

Even larger mispricings appeared in the November 2009 Lloyds Banking Group £13.5bn rights issue (1.34 new shares per existing share at 37p), with rights trading at meaningful discounts to TERP for days as the banking sector repriced violently. Quants with disciplined delta-hedging extracted low-double-digit returns; those unhedged lost catastrophically.

## Performance Characteristics

> **Data disclaimer:** The ranges below are *qualitative practitioner estimates* describing the historical character of the strategy, not a controlled backtest. No specific return series is claimed. Event cadence is lumpy and regime-dependent, so any annualized figure is conditional on opportunities being available.

- **Hit rate**: 75-85% of identified opportunities deliver positive P&L; losses come from adverse stock moves during holding period or borrow recalls.
- **Return per trade**: 50-200 bps on capital deployed, held 2-6 weeks.
- **Annualized**: 8-20% when opportunities are available; long dry spells between events.
- **Sharpe**: 0.6-1.0 net of costs over multi-year horizons.
- **Best conditions**: forced recapitalization periods (2008-2009 banks; 2020 COVID-distressed sectors), deeply-discounted offerings, new retail ownership bases that misprice rights.
- **Worst conditions**: quiet primary-issuance regimes; narrow-discount offerings; hard-to-borrow underlyings.

### Cost overlay (per trade)

| Cost / friction | Typical drag | Notes |
|-----------------|--------------|-------|
| Borrow rate on the short leg | 0.5–10%/yr (annualized over ~3-wk hold) | >8% kills the trade; 2008 banks were often impossible to borrow |
| Subscription capital opportunity cost | Funding rate × ~3 weeks | Capital-intensive: must fund full subscription |
| Bid/ask on illiquid nil-paid rights | 50–200 bps | The rights market is thinner than the share market |
| Commissions / settlement | 5–20 bps | Two legs plus subscription |
| Adverse-move margin buffer | Carry on idle margin | Needed against the ~2-week directional gap risk |

Because the gross edge per trade is only 50–200 bps, costs are decisive: a hard-to-borrow name or a short-sale ban turns a positive-expectancy trade negative instantly.

## Capacity Limits

Capacity per rights issue is a function of offering size and rights-market liquidity. For a £10bn offering, arb desks can collectively absorb £1-2bn without impact; for a €200M mid-cap European rights issue, capacity is probably €10-30M. Industry-wide capacity is in the low-single-digit billions; beyond that, rights markets move and edge disappears.

## What Kills This Strategy

1. **Stock collapse during rights period**: if the stock falls below the subscription price (as RBS, HBOS, and many 2008 banks did later), rights become worthless and the short side profits but the net is zero at best, and the subscribed shares are immediately underwater.
2. **Borrow recall / squeeze**: prime broker calls back the short, forcing cover at a loss. Common in meme-stock era; was frequent for 2008 banks too.
3. **Withdrawal / restructuring of offering**: underwriters occasionally pull or re-price offerings mid-process, creating whipsaw.
4. **Underwriter rump dumping** below market: the price can overshoot to the downside when underwriters place unsubscribed shares, hurting long-rights positions if timed wrong.
5. **Regulatory change**: short-selling bans on European banks during 2008-2011 repeatedly froze the hedge leg. The UK FSA's September 2008 short-sale ban on financials (and the SEC's parallel US ban) eliminated the strategy overnight for affected names; ESMA coordinated later EU-wide bans in 2011-2012.
6. **Dilution modeling error**: if the actual new-share count differs from expected (e.g., due to overallotment, claw-back provisions), the hedge ratio is wrong.

See [[failure-modes]] for more.

## Kill Criteria

- Short-selling ban imposed on the target sector or stock
- Borrow rate > 8% annualized on the underlying during the rights period
- Stock price within 5% of subscription price (trade economics too thin)
- Three consecutive rights-issue arbs with losses exceeding average winning-trade P&L

## Advantages

- Clearly defined, calendar-based event with fixed end date
- Mechanically determined fair value (TERP) makes mispricing easy to measure
- Historically high hit rate with moderate capital requirements
- Provides useful liquidity to retail holders and underwriters
- Diversifies across sectors and geographies -- not correlated to typical trend/mean-rev factors

## Disadvantages

- Highly capital-intensive during the 2-4 week holding period
- Requires robust prime-broker relationships for borrow and for deal flow
- Short-sale bans during crises (2008, 2011, 2020) can wipe out the strategy entirely
- Deep knowledge of offering mechanics (rights ratio, fractional entitlements, overallotment) required
- Event cadence is unpredictable -- may be quiet for quarters, then three issues in a week
- Tail risk of issuer default during holding period (recall RBS's post-rights collapse to around 10p in January 2009)

## Sources

- Eckbo & Masulis (1992), *Adverse Selection and the Rights Offer Paradox*, Journal of Financial Economics — the canonical academic treatment of rights offerings
- RBS rights issue prospectus, April 2008 (11-for-18 at 200p, £12bn) and Lloyds Banking Group rights issue prospectus, November 2009 (1.34-for-1 at 37p, £13.5bn) — primary documents
- UK FSA short-selling ban statement on financial stocks, 18 September 2008
- Broader SEO literature: Ritter, Masulis, Cornett on seasoned equity offerings

## Related

- [[arbitrage]] -- parent concept
- [[merger-arbitrage]] -- related event-driven strategy
- [[risk-arbitrage]] -- the broader convergence-to-known-value family
- [[convertible-arbitrage]] -- related structured-offering arb
- [[ipo-arbitrage]] -- primary-market cousin
- [[equity-capital-markets]] -- market context
- [[dilution]] -- underlying corporate-finance concept
- [[limits-to-arbitrage]] -- why the TERP gap persists
- [[bankruptcy-claim-arbitrage]] -- adjacent event-driven distressed strategy
- [[edge-taxonomy]], [[failure-modes]] -- methodology
- [[rbs-2008-rights-issue]] -- historical case
- [[short-selling-ban-2008]] -- regulatory risk reference
