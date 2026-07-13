---
title: "ADR Arbitrage"
type: strategy
created: 2026-04-24
updated: 2026-06-21
status: excellent
tags: [arbitrage, stocks, forex, mean-reversion, quantitative]
aliases: ["American Depositary Receipt Arbitrage", "ADR-ORD Arbitrage", "Depositary Receipt Arbitrage"]
strategy_type: quantitative
timeframe: intraday
markets: [stocks, forex]
complexity: intermediate
backtest_status: untested
edge_source: [structural, latency]
edge_mechanism: "ADR prices in New York and the underlying ordinary shares in the home market represent claims on the same cash flows but trade in different time zones, currencies, and liquidity pools. Creation and redemption via the depositary bank enforce long-run parity, but intraday frictions, FX moves, and overnight news produce exploitable gaps."
data_required: [equity-prices-global, fx-rates-intraday, adr-ratio-table, depositary-fees, borrow-availability]
min_capital_usd: 500000
capacity_usd: 2000000000
crowding_risk: medium
expected_sharpe: 1.2
expected_max_drawdown: 0.15
breakeven_cost_bps: 25
related: ["[[etf-arbitrage]]", "[[dual-listed-company-arbitrage]]", "[[fx-arbitrage]]", "[[depositary-receipt]]", "[[cross-border-arbitrage]]", "[[arbitrage]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[index-arbitrage]]"]
---

# ADR Arbitrage

ADR Arbitrage trades the spread between an **American Depositary Receipt (ADR)** listed on NYSE/Nasdaq and the underlying **ordinary shares** ("ords") in the company's home market. An ADR represents a defined ratio of home-country shares (e.g., 1 Taiwan Semi ADR = 5 Taiwanese ords) held at a depositary bank (BNY Mellon, JPMorgan, Citi, Deutsche Bank). The depositary mechanism -- similar in spirit to [[etf-arbitrage|ETF creation/redemption]] -- enforces long-run price parity after FX and ratio, but intraday dislocations, time-zone lags, and retail ADR demand spikes produce tradable gaps. It is the cross-listing member of the broader [[arbitrage]] family and a close cousin of [[dual-listed-company-arbitrage]] (Royal Dutch/Shell, BHP/Billiton), differing in that the ADR is a *receipt* on home shares rather than a separately incorporated share class, which makes the convergence enforceable through physical creation/cancellation rather than only through eventual unification.

## ADR Program Types

The tradability of the convergence depends entirely on the **ADR program level**. Only fungible, sponsored programs permit the physical creation/cancellation that closes the arbitrage; unsponsored and restricted programs are effectively un-arbitrageable except via slow intraday mean-reversion.

| Level | Trades on | Fungible w/ ord? | Creation/cancellation | Arbitrageable? |
|-------|-----------|------------------|------------------------|----------------|
| **Level I** | OTC / pink sheets | Sometimes | Limited | Weakly (intraday RV only) |
| **Level II** | NYSE/Nasdaq (listed, no capital raise) | Yes | Yes | Yes — core universe |
| **Level III** | NYSE/Nasdaq (with public offering) | Yes | Yes | Yes — core universe |
| **Rule 144A / RADR** | QIB-only private market | No (restricted) | No | No |
| **GDR** | London/Lux (Global DR) | Varies | Varies | Sometimes (GDR-ord) |

The same parity math powers Global Depositary Receipts ([[depositary-receipt|GDRs]]) listed in London and Luxembourg; the trade structure is identical with a different time-zone overlap and currency leg.

## Edge Source

**Structural** and **latency**. Structural because depositary fees, FX conversion costs, foreign withholding taxes, and settlement cycles create real frictions; a retail New York buyer of Alibaba ADRs doesn't shop the Hong Kong listing at 3am ET. Latency because the home market and U.S. market overlap for only part of the day (varying by country), and news flow in one zone is not immediately reflected in the other.

## Why This Edge Exists

- **Time-zone non-overlap.** European ADRs overlap NY for ~2 hours (9:30-11:30 ET); Asian ADRs have zero overlap with NY. Overnight news is priced in U.S. ADR trading before the home market reopens, and the home market's open often produces a catch-up move.
- **FX spread and funding.** Creation requires buying ords, wiring foreign currency, and delivering to the depositary -- typically a T+2 to T+5 process. FX moves during that window are arbitrage risk.
- **Depositary fees.** The depositary bank charges $0.01-$0.05 per ADR per year (often called "pass-through fees") plus creation/cancellation fees of $0.05 per ADR. These are the minimum friction cost.
- **Retail-driven mispricings.** Names like [[alibaba]] (BABA), [[taiwan-semiconductor]] (TSM), [[petrobras]] (PBR), [[tencent]] (pink-sheet ADR), and [[nio]] attract heavy retail flow in the U.S., regularly pushing ADR prices 30-100 bps rich to ord-implied fair value.
- **Who is on the other side?** Retail ADR buyers paying a premium; cross-border rebalancing flows; sovereign wealth funds buying ords in the home market without caring about ADR pricing.

## The Parity Identity

The no-arbitrage relationship that anchors every trade:

```
ADR_fair (USD) = Ord_price (local) × ADR_ratio × FX (USD per local) − depositary_pass_through
```

where `ADR_ratio` = home shares per ADR (TSM = 5, BABA = 1, SHEL = 1, HSBC = 5). The realized deviation is `dev_bps = (ADR_market − ADR_fair) / ADR_fair × 10000`. The three error terms that make `ADR_fair` only *approximately* knowable in real time are: (1) a **stale ord print** when the home market is closed, (2) **FX latency** between the quoted spot and the rate the desk can actually transact, and (3) **dividend timing** (ex-date misalignment between ADR and ord). Each is a distinct source of basis risk and a distinct reason a naive `dev_bps` signal misfires.

## Null Hypothesis

With zero fees, instantaneous FX, and 24-hour overlap, ADR price = ordinary price × ratio × FX. Arbitrage profits would be zero net of transaction costs. Observed persistent premiums or discounts of 20-100 bps reflect real frictions, not free money. The sharper version of the null: a measured ADR-ord deviation is **fair compensation for FX gap risk plus the carry cost of warehousing an offsetting cross-border position to settlement**; under that null, a desk that mechanically trades every >40 bps gap earns the bid-ask round-trip and the FX hedge cost back and nets ~zero. Rejecting the null requires showing the convergence happens *faster and more reliably* than the FX/settlement risk implies — which is true for liquid Level II/III names with same-day overlap and false for closed-market Asian names where the "deviation" is mostly un-priced overnight information. See [[limits-to-arbitrage]].

## Rules

**Entry.**
1. Build a universe of Level II and Level III ADRs (fungible with ord, creation/cancellation allowed). Common: TSM, BABA, PBR, VALE, SHEL, AZN, NVS, UL, HSBC, BHP, BP, TM, SNY.
2. Compute fair ADR = ord_price × ratio × FX − depositary_fee − estimated_tax_drag.
3. Enter when deviation > 2x historical noise and > 40 bps absolute.

**Creation arb (ADR rich).**
- Short ADR in NY.
- Buy ords in home market.
- Deliver ords to depositary, receive new ADRs, deliver to cover short (T+2 to T+5).
- Hedge FX with forwards matching settlement date.

**Cancellation arb (ADR cheap).**
- Buy ADR in NY.
- Short ords in home market (subject to borrow).
- Instruct depositary to cancel ADR, receive ords, deliver to cover short.

**Intraday mean-reversion variant (no creation).** For names where creation is costly, simply trade the spread intraday without actually creating/cancelling -- carry overnight risk but avoid settlement complexity.

**Position sizing.** Size each leg to be FX- and ratio-neutral, then cap by the *thinner* of the two ADV pools. A practical rule: notional per name ≤ 5-10% of min(ADR_ADV, ord_ADV) so the exit (creation delivery or intraday cover) does not move either market. The FX forward is sized to the local-currency value of the ord leg and dated to the depositary settlement date, not to the trade date. Hold gross deviation-weighted: bigger deviations get bigger size, but cap single-name risk because capital-control tail risk is per-country, not diversifiable within a country.

| Trade type | Sizing anchor | Typical hold | Primary risk warehoused |
|------------|---------------|--------------|--------------------------|
| Intraday RV (no creation) | min(ADR_ADV, ord_ADV) | minutes-hours | overnight gap if held |
| Creation arb (ADR rich) | depositary processing throughput | T+2 to T+5 | FX move to settlement |
| Cancellation arb (ADR cheap) | ord borrow availability | T+2 to T+5 | borrow recall, FX move |

## Implementation Pseudocode

```python
for adr in universe:
    ord_px = home_market_price(adr.ord_ticker)  # may be stale if closed
    fx = spot_fx(adr.home_ccy)
    fair = ord_px * adr.ratio * fx - adr.depo_fee_bps / 10000 * price(adr)
    dev_bps = (price(adr) - fair) / fair * 10000
    if dev_bps > 40 and is_home_market_open(adr):
        short_adr(adr, notional=N)
        buy_ord(adr.ord_ticker, notional=N / (adr.ratio * fx))
        fx_forward(adr.home_ccy, notional=N, days=settlement_days(adr))
        submit_creation_instruction(adr, shares=N/price(adr), depositary=adr.depositary)
    elif dev_bps < -40 and can_borrow_ord(adr.ord_ticker):
        buy_adr(adr, notional=N)
        short_ord(adr.ord_ticker, notional=N / (adr.ratio * fx))
        submit_cancellation_instruction(adr, shares=N/price(adr))
```

## Indicators / Data Used

- Real-time ADR prices (U.S. exchanges)
- Real-time / last-close ordinary prices (home exchange)
- Intraday FX rates and forwards
- ADR ratio table (from depositary bank fact sheets)
- Depositary fee schedule
- Foreign dividend withholding rates (IRS Form 1042-S)
- Home-country short-sale rules and borrow availability

## Example Trade

**Latin American ADR gaps, 1994-1998.** Brazilian, Mexican, and Argentine ADRs frequently diverged 1-3% from ordinary-implied fair value during the Asia (1997) and Russia (1998) crises because U.S. emerging-market ETFs (before they existed in current form) and retail flows cleared at different speeds than home market. Arbitrage desks at Bear Stearns, Lehman, and Banco Santander are anecdotally reported to have earned **$50-200 mm annual P&L** running Latin ADR books in this era (trade-press lore; no audited figures exist).

**Petrobras (PBR), October 2014.** During the pre-election political volatility in Brazil, the Petrobras ADRs in NY frequently traded 50-150 bps cheap to the Sao Paulo listings because U.S. hedge funds sold ADRs aggressively on political news while Brazilian retail bought ords. (Note the line mapping: PBR tracks the PETR3 common shares; PBR.A tracks the PETR4 preferreds.) Cancellation-arb traders bought the ADR, shorted the corresponding local line via [[bm&fbovespa]] borrow, and earned the convergence.

**Alibaba (BABA), 2014-2021 Hong Kong dual-listing.** Before BABA's November 2019 Hong Kong listing (9988.HK), ADR was the only access to BABA. Post-listing, the two prices converged closely but still diverged 30-80 bps intraday. Quants at [[citadel]], [[hudson-river-trading]], and [[jump-trading]] run high-frequency ADR-ord convergence books.

**Taiwan Semi (TSM)**. TSM ADR / 2330.TW is one of the most-traded ADR pairs in the world. ADR ratio = 5:1, meaning 1 ADR = 5 Taiwanese shares. Because Taiwan's market closes at 01:30 ET and U.S. market opens at 09:30 ET, TSM ADR trades based entirely on overnight news flow for 8+ hours. The 9:30 ET open frequently gaps 1-2% from Taipei's close, and the Taipei open the following night catches up.

## Performance Characteristics

> Note: the Sharpe and win-rate ranges below are illustrative practitioner expectations and order-of-magnitude desk lore, **not** results of a backtest run in this wiki. There is no audited track record attached to this page; treat all figures as qualitative.

- **Intraday mean-reversion**: Sharpe 1.0-1.8 for high-frequency variants; realized P&L per name small but scales across ~50 ADRs.
- **Creation/cancellation arb**: lower Sharpe 0.8-1.2 but much larger capacity per trade.
- **Typical P&L per creation trade**: 10-40 bps net of fees and FX.
- **Win rate**: 65-75% when deviation > 2 sigma.

The trade is a classic **negative-skew carry**: many small wins as deviations converge, punctuated by rare large losses when a convergence does not happen (capital controls, FX crisis). The full round-trip cost stack is what determines whether a 40 bps signal is tradable at all:

| Cost component | Typical range | Notes |
|----------------|---------------|-------|
| ADR bid-ask | 2-10 bps | tighter on TSM/BABA, wider on small ADRs |
| Ord bid-ask | 5-20 bps | depends on home-market liquidity |
| FX spot + forward | 1-5 bps | wider in EM currencies, blows out in crisis |
| Depositary pass-through | 2-10 bps | $0.01-$0.05/ADR annual + $0.05 create/cancel |
| Ord borrow (cancellation arb) | 10-50 bps | infeasible where shorting is banned |
| Foreign withholding drag | varies | dividend periods only; reclaim is slow |
| **Round-trip total** | **~15-60 bps** | breakeven_cost_bps ≈ 25 in frontmatter |

This is why the entry threshold (>40 bps and >2x noise) sits *above* the cost floor: the edge is only what survives the stack.

## Capacity Limits

Per-name capacity is bounded by ADR and ord ADV: large names (TSM, BABA) can absorb $100-500 mm/day; smaller ADRs only $5-20 mm. Strategy-level capacity across ~100 ADRs: $1-3 bn for a dedicated fund. Beyond that, impact on FX forwards and depositary processing becomes limiting.

## What Kills This Strategy

- **Capital controls.** If the home country imposes controls (e.g. Russia post-Feb 2022, Venezuela, Argentina at various times), ords become un-deliverable. Russian ADR arbitrage blew up in March 2022 when depositary banks suspended creation/cancellation and U.S. sanctions froze ord holdings.
- **Depositary suspension.** Banks sometimes suspend creation or cancellation for operational or regulatory reasons, trapping positions. China-listing ADRs saw several suspensions in 2020-2022 under Holding Foreign Companies Accountable Act fears.
- **FX gaps and crisis devaluations.** Brazilian real in 1999, Argentine peso in 2001, Turkish lira 2018, Russian ruble 2022 all produced overnight moves that exceeded the arbitrage spread by orders of magnitude.
- **Borrow squeezes on ordinary shares.** Some foreign markets have limited or no shorting (Taiwan, parts of India). Cancellation arb is often infeasible.
- **Dividend withholding disputes** (e.g. U.S.-Dutch treaty changes affecting ASML ADR / ord arb).
- See [[failure-modes]].

## Kill Criteria

- Home-country capital controls announced or rumored.
- Depositary bank issues suspension notice.
- Drawdown > 10% in a single ADR.
- Aggregate drawdown > 15%.
- FX vol exceeds historical 99th percentile.

## Advantages

- Persistent, measurable edge anchored in published parity math.
- Scalable across many names and regions.
- Clear exit (creation or cancellation delivery) in normal markets.
- Low correlation to traditional equity long/short strategies.

## Disadvantages

- Event risk from capital controls and sanctions can wipe out years of gains.
- Operational complexity (multiple brokers, FX desks, depositary relationships, global custody).
- Time-zone coverage requires 24-hour operation.
- Dividend withholding and foreign tax reclaim processes are slow and imperfect.

## Sources

- Gagnon, L. and Karolyi, G.A. (2010). "Multi-Market Trading and Arbitrage." *Journal of Financial Economics* — measures persistent ADR-ord price deviations and links them to short-sale and holding constraints.
- Auguste, S., Dominguez, K., Kamil, H., Tesar, L. (2006). "Cross-Border Trading as a Mechanism for Implicit Capital Flight." *Journal of Monetary Economics* (Argentine ADR study) — documents the capital-control failure mode directly.
- BNY Mellon Depositary Receipts Market Review (annual).
- Citi Global Depositary Receipts Services fact sheets.
- Performance and cost figures above are general market knowledge and practitioner lore; no audited backtest source is ingested in this wiki for them.

## Related

- [[etf-arbitrage]]
- [[dual-listed-company-arbitrage]]
- [[fx-arbitrage]]
- [[depositary-receipt]]
- [[cross-border-arbitrage]]
- [[index-arbitrage]]
- [[relative-value-arbitrage]] — the RV hub this trade belongs to
- [[convergence-arbitrage]]
- [[limits-to-arbitrage]]
- [[merger-arbitrage]]
- [[risk-arbitrage]]
- [[edge-taxonomy]]
- [[failure-modes]]
- [[arbitrage]]
