---
title: "Fees and Friction"
type: concept
created: 2026-05-07
updated: 2026-06-20
status: excellent
tags: [risk-management, market-microstructure, behavioral-finance, regulation, slippage]
aliases: ["Fees and Friction", "Trading Costs", "Transaction Costs", "Cost Stack", "Friction Stack", "Cost Drag"]
domain: [risk-management, market-microstructure]
prerequisites: ["[[bid-ask-spreads]]", "[[slippage]]"]
difficulty: beginner
related:
  - "[[bid-ask-spreads]]"
  - "[[slippage]]"
  - "[[market-microstructure]]"
  - "[[robinhood]]"
  - "[[portfolio-margin]]"
  - "[[tax-efficiency]]"
  - "[[capital-gains]]"
  - "[[fees-and-friction]]"
  - "[[professional-vs-retail-mindset]]"
  - "[[capital-preservation]]"
  - "[[market-makers]]"
  - "[[options-portfolio-construction]]"
  - "[[democratization-of-markets]]"
  - "[[finra]]"
  - "[[esma]]"
  - "[[sec]]"
---

Fees and friction is the umbrella term for the structural drag — commissions, bid-ask spreads, financing costs, slippage, payment-for-order-flow, taxes, currency conversion, account-minimum traps, behavioural friction — that compounds against active retail accounts and explains a material share of the 70-90% retail loss statistic documented in the [[esma|ESMA]]/[[finra|FINRA]] retail-broker disclosures. The proposition is that *active trading is structurally biased against the retail trader* not because retail traders are stupid, and not primarily because they lack information, but because the cost stack between their P&L and the market price is materially thicker than the equivalent stack for an institutional desk — and that the difference compounds, often invisibly, into negative real returns even before any behavioural error is layered on top. Closing the friction gap is a prerequisite for active retail trading to have a reasonable expectancy at all.

## Why Friction Matters Disproportionately

A trader with a 1.0 Sharpe ratio gross of costs has a roughly 16% expected return at 16% volatility. Strip out 200 bps of annual cost drag (commissions + slippage + spreads + financing) and the expected return drops to 14% — Sharpe falls to ~0.88. Strip out 500 bps and Sharpe falls to ~0.69. The drag is *larger* than most traders' realised excess return.

The compounding consequence over a decade: $100K compounded at 14% net for 10 years = $371K. The same $100K compounded at 9% net for 10 years (with 500 bps friction stripped) = $237K. The friction, not the gross alpha, is the dominant determinant of realised wealth. This is why professional frameworks treat cost as a *first-pass filter* on every strategy — strategies that look attractive gross of costs are rejected at the design stage if their breakeven cost exceeds what the trader can plausibly execute.

The retail bias is to treat friction as *small* because individual costs look small in isolation. A $0.65 per contract commission. A 2-cent bid-ask. 0.05% PFOF rebate. 0.1% conversion fee. Each is small; their *aggregate annualised drag* is rarely modelled, and almost never modelled correctly.

## The Cost Stack: Layer by Layer

### 1. Commissions

The most visible layer and the one retail focuses on most. The 2019-2020 zero-commission migration ([[robinhood|Robinhood]], Schwab, Fidelity, Interactive Brokers Lite) reduced equity commissions to zero for retail US stock trading. Options commissions remain non-zero almost everywhere:

- **Equity options retail**: $0.50-$0.65 per contract is typical (Robinhood, IBKR Pro, tastytrade); $0 to $1.00 elsewhere. Multiply by 2 for round-trip; multiply by spread legs (4 for an iron condor) for multi-leg structures.
- **Futures**: $0.85-$2.50 per contract per side at retail brokers; ~$0.10-$0.50 at institutional prime.
- **Crypto**: 0.05-0.50% per side at retail spot; 0.02-0.05% at institutional or maker-rebate venues. Retail platforms often layer a hidden spread on top.
- **CFDs / spread-bet**: nominally commission-free; the spread is the commission.

A trader running 100 four-leg options spreads per year at $0.65 per contract per leg pays 100 × 8 × $0.65 = $520. On a $50K account that is ~1% in commissions alone. On a $500K account it is 0.1%. Commissions therefore disproportionately tax small accounts.

### 2. Bid-Ask Spreads

The largest single friction layer for most retail trading, and the most underestimated. The bid-ask spread is the difference between the price at which a market-maker will buy and the price at which they will sell — a round-trip pays the spread once.

- **Liquid US large-cap equities**: 1-2 bps in calm regimes
- **Liquid front-month index options (SPX, SPY, QQQ)**: 5-15 bps of underlying notional per round-trip
- **Single-name liquid options (NVDA, AAPL, TSLA front-month, near-the-money)**: 10-30 bps
- **Single-name far-OTM options or back-month**: 100-500+ bps round-trip
- **Small-cap and illiquid options**: occasionally 1000+ bps (10%+ of premium per round-trip)
- **Crypto altcoins on retail venues**: 50-200 bps
- **CFDs on minor pairs and exotics**: 100-300 bps

The spread is typically the *largest single cost* of an active options strategy. A trader buying a $1.00 single-name option with a $0.95 / $1.05 quote pays 10% in spread before the position even moves. A trader paid the bid on the way out gives back another 10%. In a year of active trading, this can amount to 20-50% of premium spent on spreads alone. See [[bid-ask-spreads]].

### 3. Slippage

The difference between the *expected* execution price and the *realised* execution price, beyond the quoted spread. Slippage shows up most aggressively when:

- **Market orders are used** instead of limit orders. A market order in fast-moving markets routinely fills 10-50 bps worse than the displayed quote.
- **Large size relative to displayed depth**. A 100-contract order on an option showing 10×10 displayed liquidity will move through multiple price levels.
- **Around news or open/close**. The spread widens, displayed depth thins, and realised slippage compounds.
- **Stops are placed in liquid hours and triggered in illiquid ones** (gaps, halts, overnight). The realised execution can be far from the trigger price.

The professional answer is *limit orders, patient working, and avoiding low-liquidity windows*; the retail default is market orders during the most liquid (and most-watched, most-news-driven) windows, which produces worst-case slippage.

### 4. Financing and Margin Interest

Levered positions cost interest. The typical 2024-2026 rate stack:

- **Reg-T margin debit**: 8-13% APR at retail brokers (Robinhood Gold ~8%, Schwab ~12%, IBKR Pro ~6.5% at high tiers)
- **[[portfolio-margin]] debit**: 5-7% APR at IBKR Pro, similar at top-tier retail
- **Institutional prime brokerage**: SOFR + 25-100 bps (~5-6% in 2026)
- **Crypto perps funding**: 8-30% annualised in calm regimes, 100%+ in squeezes
- **CFD overnight financing**: typically SOFR + 250-350 bps for long; sometimes a credit on shorts

A trader who runs $100K of margin debit at 12% pays $12K per year — 12% of the levered book — just to maintain the leverage. The same exposure at 6% IBKR Pro Portfolio Margin pays $6K. The difference is meaningful enough that the *broker choice* changes which strategies are economic.

### 5. Slippage on Halts, Gaps, and Off-Hours

A subtle but important layer. Stop-loss orders provide an *intended* maximum loss; the *realised* loss when the stop triggers in a gap or halt can be materially worse. Single-stock examples:

- Earnings gaps routinely move 5-15% overnight; a 5% trailing stop set at the close fills at the open the next day at the gap-down price, not the stop level.
- Halted names re-open at a print, often after a multi-cent or multi-percent move.
- Crypto markets trade 24/7; the 4am ET liquidity vacuum is when stop-runs are cheap.

The realised distribution of stop-out prices is typically 1.5-3× wider than the intended distribution. Models that assume stop-fills at the stop level overstate the realised cost discipline.

### 6. Payment-for-Order-Flow (PFOF)

The most opaque retail-specific layer. PFOF is the practice of retail brokers selling order flow to wholesale market-makers (Citadel Securities, Virtu, Susquehanna, others) who then execute the trades, typically by internalising against their own inventory or by routing to exchanges. The wholesaler pays the broker a per-share or per-contract rebate.

The mechanism is legal in the US but banned in the UK, Canada, and (since 2025) in the EU. The empirical evidence on whether it *materially worsens* retail execution quality is mixed but the regulatory direction is clear: the SEC's Best Execution disclosures (Rule 605/606) consistently show that PFOF venues fill marketable retail orders at *price-improvement* levels — i.e., better than the displayed national best bid/offer (NBBO) — but the price improvement on retail-marketable flow is itself a function of the wholesaler's information advantage about the flow's directional bias. A retail buy order is statistically more likely to be a noise trade than an informed one, and the wholesaler's improvement reflects that. Retail traders do not see the institutional BBO they could have hit at a tier-1 prime brokerage.

The order-of-magnitude estimates ([[robinhood|Robinhood]] disclosures, SEC analyses):

- **Equities**: 5-30 bps of PFOF rebate per share to the broker, of which 10-50% is shared back as price improvement. Net retail loss vs. institutional execution: ~5-15 bps per round-trip.
- **Options**: substantially higher — $0.30-$0.80 per contract in PFOF rebates is typical. Options PFOF is the primary revenue source for many retail brokers.

The [[robinhood|Robinhood]] case study is the most-discussed: PFOF revenues are 60-80% of the company's net revenue, and the SEC fined the firm $65M in 2020 for understating execution quality (settled without admission). PFOF is not necessarily worse than the alternative for any individual order, but it creates a structural conflict of interest between the broker and the user, and the cumulative friction over a year of active retail trading is non-zero. See the [[robinhood]] page for the corporate case study.

### 7. Taxes

Often the largest single friction layer for profitable active retail traders, and the one most often ignored at the strategy-design stage.

- **Short-term capital gains** (held < 12 months in the US) are taxed as ordinary income. A 24-37% federal marginal rate, plus state (up to 13.3% in California, 10.9% in NY), plus 3.8% NIIT on investment income above thresholds. A high-income retail trader in a high-tax state pays ~50% on short-term gains.
- **Long-term capital gains** (held > 12 months) are taxed at 0/15/20% federal, much lower in aggregate.
- **Section 1256 contracts** (US futures, broad-based index options like SPX, XSP) are taxed 60% long-term / 40% short-term regardless of holding period — a structural advantage for index-options traders over single-stock-options traders.
- **Wash sale rules** disallow loss recognition if a substantially identical security is purchased within 30 days. Active traders inadvertently violate wash sale rules constantly, deferring losses and accelerating gains.
- **Partial-year losses cannot offset prior gains** in the same year if the gains were realised earlier and tax was already paid (in jurisdictions with quarterly estimated payments).

The professional response is to *plan for tax* at the strategy level: hold-period bias, year-end harvesting, instrument selection (1256 vs equity options), entity structure for size accounts (LLC, S-corp). Retail accounts that ignore tax often discover at year-end that nominal gains have produced a much smaller after-tax balance than expected.

### 8. Currency Conversion

Often invisible. Common retail traps:

- **FX conversion on US-stock trades through non-US brokers**: 0.5-2% spread per conversion, paid on every deposit, withdrawal, and dividend.
- **Multi-currency accounts at retail brokers** (eToro, Revolut, etc.) often charge spreads in the 50-100 bps range on conversion versus the interbank rate.
- **CFD financing on cross-currency positions** has a hidden FX leg.
- **Crypto on-ramp/off-ramp spreads** (USD ↔ stablecoin or USD ↔ BTC at retail venues) can be 100-300 bps versus the institutional venue.

A trader who converts $10K USD → EUR → equity, then back, pays 100-200 bps on each conversion — 4-8% of capital just on FX, before any trading P&L. Institutional accounts use IBKR's IDEAL FX or direct prime broker conversion at interbank rates; retail accounts often pay 50-100× more.

### 9. Account-Minimum Traps

Account-level rules and minimums that *force* friction-heavy structures on small accounts:

- **Pattern Day Trader rule**: US retail accounts under $25K are limited to 3 day trades per 5 trading days. Above $25K the rule is lifted but Reg-T margin still applies.
- **[[portfolio-margin]] minimum**: $125K initially, $100K maintenance at most US brokers. Below this, traders are stuck with strategy-based margin, which makes hedged options books prohibitively expensive.
- **Futures minimums** vary by broker; meaningful margin headroom requires $25-50K minimum in practice.
- **Inactivity fees** at some brokers ($10-20/month) for accounts below thresholds.
- **Dividend withholding** at non-resident-broker combinations (typically 30% US withholding on dividends paid to non-US accounts unless treaty rates apply).

The structural consequence: small accounts pay disproportionately high friction. A $10K account running active options costs 5-10% of capital per year on commissions alone; the same activity at $500K is 0.2-0.5%. The friction is regressive, which is why a professional-style options framework is realistically only deployable above ~$125-200K of equity.

### 10. Behavioural Friction

The least-discussed but often largest layer. Behavioural patterns systematically *worsen* the realised distribution of trades versus the planned one:

- **Averaging down**: doubles the loss in the worst-case path. See [[loss-aversion]] and [[disposition-effect]].
- **Exiting winners too early**: cuts the right tail of the distribution. The planned 3:1 trade becomes a 1.5:1 realised trade.
- **Holding losers past the stop**: extends the left tail.
- **Chasing news**: produces high-friction entries at the worst spreads and slippage.
- **Revenge trading**: produces oversized positions in the lowest-conviction setups.

The friction is not measured on the trade ticket but on the *realised P&L distribution versus the strategy's theoretical distribution*. For active retail traders this gap is typically 200-500 bps annualised on top of the explicit cost stack. Closing the gap is the central programme of [[professional-vs-retail-mindset|the professional discipline]].

## Per-Asset-Class Cost Sketch

| Asset class | Typical retail round-trip cost | Typical institutional round-trip cost |
|---|---|---|
| US large-cap equity (liquid) | 2-5 bps (spread + slippage) | 1-2 bps |
| US small-cap equity | 10-30 bps | 5-15 bps |
| Liquid index options (SPX/SPY/QQQ) | 5-20 bps notional | 2-5 bps notional |
| Single-name front-month options | 15-50 bps notional | 5-15 bps notional |
| Single-name far-OTM/back-month | 100-500+ bps premium | 30-100 bps |
| US Treasury futures | 1-3 bps | 0.5-1 bps |
| FX major pairs | 5-20 bps (retail), 1-3 bps (ECN) | 0.1-1 bp |
| Crypto majors (BTC/ETH) liquid venue | 5-15 bps | 2-5 bps |
| Crypto altcoins retail venue | 50-200 bps | 10-50 bps |
| CFDs majors | 50-100 bps | n/a (institutional uses futures/spot) |

The retail/institutional gap is consistently 2-5× and frequently 10× or more for the lower-liquidity instruments. Across an actively traded book, the aggregate annualised drag for a typical retail account is 200-500 bps; for a typical institutional desk it is 30-100 bps. The difference, 200-400 bps annually, is *larger than the gross alpha of most strategies*, which is why the retail/institutional performance gap is structural and not a function of intelligence.

## Worked Example: Stacking the Full Friction Cost

*The numbers below are illustrative and hypothetical, not real broker quotes or real returns.*

Consider a hypothetical $100,000 retail account running an active single-name options strategy: 150 round-trips per year, each a 2-leg vertical spread on a mid-liquidity single name, average premium $400 per spread, average 6-week holding period, profitable enough to realise $20,000 of short-term gains in the year.

| Friction layer | Per-round-trip cost | Annual total | % of account |
|----------------|--------------------|--------------|--------------|
| Commissions (4 contract-legs × $0.65) | $2.60 | $390 | 0.39% |
| Bid-ask spread (~25 bps of $400 premium, ×2 legs, round-trip) | ~$50 | $7,500 | 7.5% |
| Slippage (market-order habit, ~10 bps) | ~$8 | $1,200 | 1.2% |
| PFOF gap vs direct routing (~$0.50/contract net) | ~$2 | $300 | 0.3% |
| Short-term tax on $20K gains (~35% blended) | — | $7,000 | 7.0% |
| Behavioural drag (early exits, averaging down) | — | ~$3,000 | ~3.0% |
| **Total friction** | | **~$19,390** | **~19.4%** |

The lesson is the *ordering*. Commissions — the layer retail obsesses over — are the smallest line at 0.39%. The [[bid-ask-spreads|spread]] (7.5%) and [[#7. Taxes|tax]] (7.0%) layers dwarf everything else, and the behavioural layer is nearly invisible on any ticket. A trader who switched to liquid index options (spread ~5 bps instead of 25), used [[#7. Taxes|Section 1256]] instruments for the 60/40 tax treatment, and replaced market orders with patient limits could plausibly cut the friction stack by more than half — without improving the strategy's gross edge at all. This is why [[capital-preservation]] treats friction reduction as the highest-return "trade" available to most retail accounts.

## How Professionals Minimise Each Layer

The professional response, layer by layer:

1. **Commissions**: tier negotiation with the broker, prime brokerage at scale, IBKR Pro / IBKR Lite for retail-equivalent costs.
2. **Spreads**: trade liquid instruments by default; use limit orders; work into positions across multiple time slots; avoid open/close and news windows for non-news-driven trades.
3. **Slippage**: limit orders, patient execution, awareness of displayed depth, avoidance of stops in low-liquidity hours.
4. **Financing**: portfolio margin (5-7% APR vs Reg-T 10-13%); securities lending revenue offsets; box-spread financing for SPX (3-4% APR for those with sophistication).
5. **Halt/gap slippage**: position size assuming the stop *won't* trigger cleanly; defined-risk options structures where the maximum loss is the premium; tail hedges sized for gap scenarios.
6. **PFOF**: use a non-PFOF broker (IBKR Pro routed direct, Tradestation Direct, Lightspeed) for size or sensitive flow; accept retail PFOF for low-friction strategies where the price improvement is comparable to the alternative.
7. **Taxes**: instrument selection (1256 contracts for index exposure), holding-period planning, year-end harvesting, entity structure at scale.
8. **Currency**: IBKR IDEAL FX conversion (at-interbank for $$ size); avoid multi-currency retail brokers for FX-heavy workflows.
9. **Account minimums**: capitalise the account properly before deploying the strategy. The framework is not deployable below ~$125-200K, full stop.
10. **Behavioural friction**: written process discipline, journal, peer accountability, drawdown circuit breakers — see [[professional-vs-retail-mindset]] and [[capital-preservation]].

The aggregate effect is to compress the 200-500 bps retail drag toward the 30-100 bps institutional band. This is not a small adjustment — it is often the difference between profitable and unprofitable active trading.

## Friction Layer Priority Map

Where to spend effort, ranked by typical magnitude for an active retail options trader. Optimising in this order yields the most basis points saved per unit of effort:

| Priority | Layer | Typical retail magnitude | Highest-leverage fix |
|----------|-------|--------------------------|----------------------|
| 1 | Taxes | Up to ~50% of short-term gains | Instrument selection (1256), holding-period planning, harvesting |
| 2 | Bid-ask spreads | 5-500+ bps per round-trip | Trade liquid instruments; limit orders; avoid far-OTM/back-month |
| 3 | Behavioural drag | 200-500 bps/yr | Written process, journal, [[derisking]] circuit breakers |
| 4 | Slippage | 10-50 bps in fast markets | Patient limits; avoid open/close and news windows |
| 5 | Financing | 6-13% APR on margin debit | [[portfolio-margin]]; box-spread financing for SPX |
| 6 | Gap/halt slippage | 1.5-3× wider than intended | Defined-risk structures; size for the gap |
| 7 | PFOF | ~5-15 bps equities; $0.30-0.80/contract options | Non-PFOF broker for size/sensitive flow |
| 8 | Currency conversion | 50-200 bps per conversion | Interbank FX (e.g., IBKR IDEAL); avoid spread-loaded brokers |
| 9 | Account-minimum traps | Regressive on small accounts | Capitalise properly; the framework needs ~$125-200K |
| 10 | Commissions | $0-$0.65/contract | Tier negotiation; lowest-cost broker |

The single most common mistake is inverting this list — agonising over commissions (priority 10) while ignoring taxes (priority 1) and spreads (priority 2), which together are often 30-50× larger.

## Cost Discipline as a Strategy Filter

The professional approach is to make cost the *first* filter on any strategy idea. The questions:

1. **What is the breakeven cost** in bps round-trip that the strategy can absorb and still be net-positive at the historical edge?
2. **What is the realistic execution cost** at the trader's actual broker, account size, and instrument liquidity?
3. **Is the realistic cost less than the breakeven cost by a meaningful margin** (typically 2-3×)?

Strategies that fail this filter — high-frequency mean-reversion on liquid futures at retail commissions, daily rebalanced index basket strategies at retail spreads, premium-selling on illiquid options chains — are rejected before the backtest is run. The discipline avoids the canonical retail trap of "the backtest looks great gross of costs."

## Common Misapplications

1. **Modelling friction as a flat percentage of notional.** Friction is heterogeneous: spreads scale with liquidity, commissions scale with structure complexity, slippage scales with order size and time-of-day, taxes scale with holding period. A flat 10 bps round-trip estimate can be wildly wrong in either direction.
2. **Ignoring the variance of friction.** The *average* cost matters, but so does the *worst-case* cost in stress regimes. Spreads triple in vol shocks; slippage explodes; halts produce gaps. A strategy whose expectancy is positive at the average cost can be negative at the stress-cost.
3. **Confusing zero commissions with zero friction.** [[robinhood|PFOF]] migration produced "free" commissions but materially worse fills on options. Total friction often *increased* for retail options traders during the zero-commission migration; the cost just moved to a less visible layer.
4. **Optimising the wrong layer.** A trader saving $0.50 per options contract on commissions while paying 30 bps on spreads is optimising the smaller layer. The right order of focus is spreads → slippage → financing → commissions → PFOF, roughly in proportion to typical magnitudes.
5. **Treating tax as someone else's problem.** Tax is the largest friction layer for many profitable active retail traders. Deferring tax modelling until April produces structural strategy-design errors.
6. **Believing the institutional band is unreachable.** With portfolio margin and a top-tier broker (IBKR Pro / Tradestation Direct / similar), retail traders can compress most of the gap. The remaining gap is access to direct exchange routing on size and cross-asset prime brokerage, which only matters above ~$1M account size.
7. **Believing all retail brokers are equivalent.** They are not. Robinhood's PFOF model, IBKR Pro's direct routing, eToro's spread-loaded model, and Schwab's pricing tiers produce materially different friction profiles. Broker choice is a strategy decision.

## Cost Discipline in the Professional Frame

Fees-and-friction is the structural-side companion to the [[professional-vs-retail-mindset|behavioural divergence]]. Retail underperformance has *both* causes — behavioural inversion and structural cost stack — and mindset work alone cannot close the gap without the structural fix, just as the structural fix alone cannot close the gap without the discipline. The complete operational layer ([[options-portfolio-construction]]) addresses both:

- **Portfolio margin requirement** — closes the financing layer
- **Liquid-underlyings preference** — closes the spread layer
- **Limit-order discipline** — closes the slippage layer
- **Turnover caps** — caps the cumulative cost drag
- **Instrument selection** (SPX/index over single-name where appropriate) — closes the tax layer
- **Hedging cost as a fixed expense** — pre-committed friction, not discretionary

The trader who runs the framework on a low-friction broker compresses the cost gap to institutional-comparable bands, which is the precondition for the framework's risk math to work as intended. Without the friction compression, the same framework runs at a different — and often negative — expected return.

## Related

- [[bid-ask-spreads]] — the largest single friction layer for most retail strategies
- [[slippage]] — execution-quality friction
- [[market-microstructure]] — the broader literature on how friction is generated
- [[robinhood]] — canonical retail-broker / PFOF case study
- [[portfolio-margin]] — the financing-cost reduction lever
- [[tax-efficiency]] — the tax-friction lever
- [[capital-gains]] / [[mortgages]] — broader personal-finance friction
- [[professional-vs-retail-mindset]] — behavioural-side companion to this page
- [[capital-preservation]] — the discipline that subsumes friction control
- [[market-makers]] — counterparties on the other side of the spread
- [[democratization-of-markets]] — the structural shift creating modern retail friction
- [[finra]] / [[esma]] / [[sec]] — regulators publishing the relevant disclosure data

## Sources

- ESMA CFD broker disclosure data 2018-2025 — empirical retail loss distributions
- SEC Rule 605/606 best-execution disclosures — PFOF and execution-quality data
- FINRA retail trading studies — US data on cost incidence
- [[robinhood|Robinhood]] S-1 and 10-K filings — PFOF revenue disclosure
- Robert Battalio, Shane Corwin, Robert Jennings, "Can Brokers Have It All? On the Relation Between Make-Take Fees and Limit Order Execution Quality" (*Journal of Finance*, 2016) — academic evidence on fee structures and execution quality
- Charles Schwab "Annual Cost Survey" — broker fee comparison
- Brad Barber et al., "Just How Much Do Individual Investors Lose by Trading?" (2009) — academic estimate of retail trading drag
