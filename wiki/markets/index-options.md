---
title: "Index Options"
type: market
created: 2026-05-07
updated: 2026-06-19
status: excellent
tags: [options, derivatives, indicators, sp500, nasdaq, stocks]
aliases: ["Index Options", "Equity Index Options", "Cash-Settled Index Options", "Broad-Based Index Options"]
related: ["[[spx-options]]", "[[spy-options]]", "[[xsp-options]]", "[[ndx-options]]", "[[rut-options]]", "[[vix-options]]", "[[dax-options]]", "[[nikkei-options]]", "[[section-1256-contracts]]", "[[am-vs-pm-settlement]]", "[[cash-vs-physical-settlement]]", "[[american-vs-european-options]]", "[[weekly-options]]", "[[zero-dte-options]]", "[[vix]]", "[[volatility-skew]]", "[[options-premium-selling]]", "[[short-strangle]]", "[[iron-condor]]", "[[itpm-trade-construction-playbook]]", "[[options-portfolio-construction]]", "[[theta-targeting]]", "[[options-buying-power-reduction]]", "[[variance-risk-premium]]"]
domain: [derivatives, options, equity-indices]
difficulty: intermediate
---

**Index options** are options whose underlying is an equity index (S&P 500, Nasdaq-100, Russell 2000, VIX) rather than a single stock or ETF. The signature features that distinguish them from equity options are **cash settlement**, **European exercise** (no early assignment), and — for US-listed broad-based indices — **[[section-1256-contracts|Section 1256]] 60/40 tax treatment**. Because of these structural advantages, index options are the canonical vehicle for [[options-premium-selling|premium-selling]] portfolios, macro hedges, and [[itpm|ITPM]]-style volatility books, and they are the deepest, most liquid options market in the world: SPX alone trades 2-4 million contracts per day.

## Overview

Index options trade on the underlying *index level* (a number, not a security). At expiration, in-the-money options pay out their intrinsic value in **cash**, computed as `(strike − settlement value) × multiplier` for puts or `(settlement value − strike) × multiplier` for calls. No shares are delivered, no margin call follows from physical delivery, and no early-assignment risk exists.

The major US-listed index options:

| Product | Underlying | Multiplier | Notional at typical level |
|---|---|---|---|
| [[spx-options\|SPX]] | S&P 500 Index | $100 | ~$500,000 (SPX 5000) |
| [[xsp-options\|XSP]] | Mini-SPX (1/10 SPX) | $100 | ~$50,000 (XSP 500) |
| [[ndx-options\|NDX]] | Nasdaq-100 Index | $100 | ~$1,750,000 (NDX 17,500) |
| [[rut-options\|RUT]] | Russell 2000 Index | $100 | ~$200,000 (RUT 2000) |
| [[vix-options\|VIX]] | VIX Index | $100 | ~$1,500 (VIX 15) |

Internationally, the same model applies with regional adjustments:

| Product | Region | Notes |
|---|---|---|
| [[dax-options\|DAX options]] | Eurex (Germany) | EUR multiplier; cash-settled European-style |
| [[nikkei-options\|Nikkei 225 options]] | OSE/SGX | JPY multiplier; cash-settled |
| [[ftse-100-options]] | ICE | GBP multiplier; cash-settled |
| [[hsi-options\|Hang Seng options]] | HKEX | HKD multiplier; cash-settled |

Across geographies the story is the same: the index-options franchise is the focal point for institutional vol trading, with deep liquidity, tight spreads on near-the-money strikes, and a continuous range of expirations from same-day to 2+ years.

## Contract Mechanics

### Cash settlement

At expiration, the broker credits or debits cash equal to intrinsic value. There is no share delivery and no possibility of being "put" stock. For sellers, this eliminates the [[assignment-risk|assignment risk]] that creates timing problems on equity options near ex-dividend dates and on deep-ITM positions late in life. See [[cash-vs-physical-settlement]] for the full mechanical contrast with [[spy-options|SPY]] and equity options.

### European exercise

Index options are exclusively European-style — exercise occurs only at expiration, never before. This is a hard regulatory constraint of the OCC contract, not a broker policy. The implication is that **time value cannot be lost to early exercise**: a deep-ITM short option will never be assigned three weeks before expiry, freeing the seller to manage on their own schedule. See [[american-vs-european-options]].

### AM vs PM settlement

A subtle but consequential split exists between two settlement regimes:

- **AM settlement** (traditional monthly SPX, NDX, RUT) — the contract settles to the **Special Opening Quotation (SOQ)** of the index on expiration Friday morning. The SOQ is computed from the *opening prints* of every component stock, which open at staggered times and can produce an SOQ that materially differs from Thursday's close. **Final trading occurs the prior afternoon** — there is no Friday trading on AM-settled contracts.
- **PM settlement** (SPXW weeklies and 0DTE, RUTW, NDXW, XSP) — settles to the **4:00 pm ET closing print** of the index. Trading continues until 4:00 pm.

The AM/PM distinction creates real risk:

1. Calendar spreads that pair AM-settled monthlies with PM-settled weeklies are mismatched at expiration; the long leg may settle hours after the short leg.
2. Overnight news between Thursday close and Friday SOQ can move AM settlement materially, creating "Thursday-night gap risk" not present in PM-settled products.
3. The SOQ is occasionally dramatically different from the Thursday close — the most famous case is **August 24, 2015**, when SPX's SOQ printed ~5% below the prior close due to staggered component openings during the flash-crash morning, settling AM puts deep in the money and crystallizing losses on positions that looked safe at Thursday's close.

See [[am-vs-pm-settlement]] for case studies and [[soq-settlement]] for the calculation methodology.

### Exercise-and-settlement workflow

The end-of-life mechanics differ sharply from equity options and are worth stating explicitly:

1. **No "do-not-exercise" decisions** — because settlement is automatic and cash-only, there is no exercise election to file, no risk of forgetting to exercise an ITM option, and no possibility of being assigned stock you didn't want. Every option that finishes ITM is settled in cash automatically by the OCC.
2. **The settlement value, not the last trade, determines payout** — an SPX call struck at 5000 pays `(SOQ − 5000) × $100` on an AM-settled monthly, where the SOQ may differ from where SPX last printed. A position that looks 5 points ITM on Thursday's close can settle flat or ITM by a different amount on Friday's SOQ.
3. **OTM options expire worthless with no residual obligation** — there is no pin risk in the equity sense (no uncertainty about share delivery), but there *is* settlement-value uncertainty on AM-settled contracts.

This clean cash workflow is the core operational reason institutions favor index options over equity-option chains for portfolio-scale structures. See [[assignment-and-exercise]] and [[pin-risk]] for the contrasting equity-option case.

### Strike intervals and tick sizes

| Product | Standard strikes | Near-the-money | Tick |
|---|---|---|---|
| SPX | $5 | $1 (some weeklies) | $0.05 below $3 / $0.10 above |
| NDX | $25 | $5 (weeklies) | $0.05 / $0.10 |
| RUT | $5 | $5 | $0.05 / $0.10 |
| XSP | $1 | $0.50 (weeklies) | $0.05 |
| VIX | $0.50 | $0.50 | $0.05 |

The tick floors above the penny-pricing of [[spy-options|SPY]] mean that bid/ask spreads on small-premium options are wider in dollar terms — see "Liquidity & Spreads" below.

### Expiry calendar

US index options now have **daily expirations** on SPX (M/T/W/Th/F since 2022), making same-day [[zero-dte-options|0DTE]] strategies possible. NDX, RUT, and XSP have multi-day-per-week expirations as of 2024+. International indices generally have weekly + monthly expirations.

## Tax Treatment

US-listed broad-based index options are **[[section-1256-contracts|Section 1256 contracts]]** under the Internal Revenue Code, which means:

- **60/40 split** — every realized gain or loss is treated as 60% long-term capital gain/loss and 40% short-term, regardless of holding period. A 10-second SPX scalp gets the same 60/40 treatment as a 9-month LEAPS roll.
- **Mark-to-market at year-end** — open positions on December 31 are deemed closed at fair market value on that date, with the resulting gain/loss reported on Form 6781. This eliminates holding-period tracking across years but creates a phantom taxable event on positions still open.
- **Loss carryback** — Section 1256 losses can be carried back **up to 3 years** against prior Section 1256 gains only.
- **No wash-sale rules** in the standard equity §1091 form — though anti-abuse and dealer rules can apply.

For an active premium-seller in the top US federal bracket, the 60/40 blended rate is roughly **26.8% federal** vs **~37% short-term** on equity options — a structural after-tax edge of ~10 percentage points that compounds substantially over a portfolio's life. Two identical strategies, one on SPX and one on SPY, deliver materially different after-tax Sharpe.

What qualifies as a "broad-based index" is defined in IRC §1256(g)(6) and IRS guidance: SPX, NDX, RUT, XSP, VIX all qualify. ETF options on SPY, QQQ, IWM **do not** qualify (they are equity options on ETFs, taxed as standard short-term/long-term capital gains). This is the single largest practical reason serious short-premium portfolios trade SPX rather than SPY despite SPY's better intraday liquidity and penny tick.

International index options have their own jurisdiction-specific tax treatment with no analogous 60/40 framework.

See [[section-1256-contracts]] for full mechanics and [[wash-sale-rules-options]] for edge cases.

## Liquidity & Spreads

US index options are the deepest options market in the world:

- **SPX**: 2-4 million contracts/day. 0DTE alone is over 40% of total SPX volume as of 2024-2025.
- **NDX**: ~50,000 contracts/day — meaningfully thinner than SPX, with wider spreads on far-OTM strikes.
- **RUT**: ~25,000 contracts/day — thinnest of the major US indices.
- **XSP**: ~30,000 contracts/day — growing as a small-account proxy for SPX.
- **VIX options**: ~600,000 contracts/day, concentrated in front-month and short-dated.

Spread characteristics:

- **Near-the-money**: $0.05-$0.10 wide on SPX/NDX/RUT — penny-equivalent given the $100 multiplier.
- **Far-OTM wings**: spreads can widen to $1+ during stress, creating significant slippage on hedge unwinds at exactly the moments hedges are needed. See [[liquidity-evaporation]].
- **0DTE near-the-money**: extremely tight, often penny-wide, with quote sizes of hundreds of contracts.
- **Back-month (180+ DTE) strikes**: wider spreads, especially on RUT and NDX.

Quote sizes are typically large at the inside on near-the-money strikes (50-500 contracts on SPX), and market-makers compete via the [[clob|CLOB]] auction mechanics. Execution quality on liquid strikes is excellent; on far-OTM tails it can be punishing in stress.

The 5-cent tick floor below $3 on SPX (vs penny pricing on SPY) creates an effective spread that is **wider in basis points** than SPY at small-premium strikes — a consideration for high-frequency or scalping strategies that compete on cents-per-contract.

## Greeks and Volatility-Surface Behavior

Index options share the full [[options-greeks|Greeks]] vocabulary with single-name options, but several behaviors are distinctive to broad indices and matter for how positions are managed:

- **Delta** — index options have no dividend-driven early-exercise distortion, so delta behaves cleanly along the Black-Scholes-Merton curve. Practitioners often size positions in *delta-equivalent index points* rather than contracts so that SPX, NDX, and RUT books can be aggregated to one net exposure.
- **Gamma** — short-dated index options ([[weekly-options|weeklies]], [[zero-dte-options|0DTE]]) carry enormous gamma per dollar of premium. Dealer net gamma positioning in SPX has become a tracked market-structure variable ([[gamma-exposure|GEX]]): when dealers are net long gamma they dampen intraday moves by trading against them, and when net short they amplify moves — a feedback loop that intensified with the 0DTE boom. See [[gamma-exposure]] and [[0dte-impact-on-spx]].
- **Theta** — the time-decay engine that makes [[options-premium-selling|premium selling]] work. Theta accelerates non-linearly into expiry, which is why short-dated [[theta-targeting|theta-targeted]] books harvest the bulk of decay in the final days of an option's life.
- **Vega** — index options are the primary listed instrument for taking [[implied-volatility|implied-vol]] exposure on the broad market. A long calendar is long vega; a short strangle is short vega. The [[variance-risk-premium]] is, in vega terms, the structural overpricing of index implied vol relative to subsequent realized vol.

### The index volatility surface

Index options exhibit a characteristic three-dimensional surface — implied vol as a function of both strike and expiry:

- **Steep negative skew (the "smirk")** — index puts trade at materially higher implied vol than equidistant calls. This [[volatility-skew|skew]] is far steeper for broad indices than for single names because index crashes are correlated, demand for crash protection (long puts) is persistent and one-directional, and there is no offsetting upside-call demand of equivalent size. The skew is one of the most stable features of the index surface and is itself a tradable object via risk reversals and put-spread-collar structures.
- **Term structure of implied vol** — in calm regimes the surface is upward-sloping in time (near-dated vol below long-dated vol), reflecting mean-reversion expectations; in stress it inverts (near-dated vol spikes above long-dated). This term structure is the equity-option analog of the [[vix-term-structure|VIX futures curve]] and is traded via [[calendar-spread|calendars]] and diagonals.
- **Volatility-of-volatility** — the index surface itself moves; its second-moment behavior is captured by [[vvix|VVIX]] and is what makes vega hedging of long-dated index books non-trivial.

Understanding the surface — not just at-the-money vol — is what separates a structural index-options book from naive directional trading. See [[volatility-skew]], [[implied-volatility]], and [[book-option-volatility-and-pricing|Natenberg]].

## Common Spread Structures

Index options are almost always traded as multi-leg structures rather than naked single legs. The canonical families:

| Structure | Construction | View expressed | Risk profile |
|---|---|---|---|
| [[short-strangle\|Short strangle]] | Sell OTM put + sell OTM call (e.g. 16-delta each) | Range-bound / short vol | Undefined risk both sides; collects [[variance-risk-premium\|VRP]] |
| [[iron-condor\|Iron condor]] | Short strangle + protective long wings | Range-bound, defined risk | Capped loss; lower credit than strangle |
| [[short-straddle\|Short straddle]] | Sell ATM put + sell ATM call | Strong short-vol, pinning bet | Highest theta, highest gamma risk |
| Put credit spread | Sell higher-strike put, buy lower-strike put | Mildly bullish / short vol | Defined risk; popular 0DTE structure |
| [[calendar-spread\|Calendar / time spread]] | Sell near-dated, buy same-strike far-dated | Long vega, exploits term structure | Long vol, profits if IV rises |
| [[ratio-calendar-spread\|Ratio calendar]] | Asymmetric near/far quantities | Term-structure + skew view | Complex; ITPM staple |
| Put-spread collar / overlay | Long put spread financed by short call | Tail hedge for long book | Net cheap downside protection |
| Risk reversal | Long call + short put (or reverse) | Directional + skew trade | Trades the skew directly |
| Butterfly | Body short, wings long | Pin-the-strike, low-cost lottery | Defined risk, peaked payoff |

The defined-risk variants (condors, credit spreads, butterflies) dominate retail and 0DTE flow because they cap the [[notional-shock|notional shock]] of a single index contract; undefined-risk strangles and straddles dominate institutional [[options-premium-selling|premium-selling]] books where [[options-buying-power-reduction|portfolio margin]] makes them capital-efficient. See [[itpm-trade-construction-playbook]] for the institutional construction methodology.

## Use Cases

### Premium-selling and short-vol portfolios

Index options are the canonical vehicle for [[options-premium-selling|short-premium]] strategies because:

- **No assignment risk** simplifies management; there are no early-exercise surprises.
- **No dividend risk** — index options on cash-settled indices are not affected by component dividends in the same way as equity options on individual dividend-payers (SPX has a continuous dividend yield baked into the futures basis, but no discrete equity-option-style ex-div assignment risk).
- **Section 1256 tax treatment** materially improves after-tax returns for active strategies.
- **Liquidity** allows sizing a [[theta-targeting|theta-targeted]] book without fighting bid/ask on entry and exit.
- **Portfolio-margin efficiency** ([[options-buying-power-reduction|BPR]]) is best for broad-based indices; the ±6% portfolio-margin grid for SPX is more lenient than the ±15% grid for single-name stocks.

Canonical premium-selling structures on indices: 16-delta [[short-strangle|strangles]], [[iron-condor|iron condors]], 30-delta put credit spreads, [[ratio-calendar-spread|ratio calendar spreads]]. See [[itpm-trade-construction-playbook]].

### Macro hedging

Long index puts are the standard hedge for diversified equity portfolios:

- **One trade hedges the whole book** — a $1M long-equity portfolio can be approximately hedged with ~20 SPX puts (at $50K notional each).
- **Cash-settled** so the hedge pays out in dollars at exactly the moment they're needed; no need to liquidate the long book to monetize the hedge.
- **No dividend leakage** vs hedging with short SPY shares.
- **Tax-efficient** under §1256.

The [[5-percent-otm-put-overlay]] is a common macro-hedge template using SPX or XSP.

### Volatility expression

[[vix-options|VIX options]] are options on implied volatility itself, providing direct exposure to second-moment events rather than spot direction. Used by tail-risk funds, pension overlays, and dispersion traders. See [[vix-options]] for the unique mechanics (futures-based settlement, complex term structure).

### Index-vs-component dispersion

Selling [[variance-swap|variance]] on the index against buying variance on components captures the **dispersion premium** — the gap between implied correlation and realized correlation. Institutional vol desks run dispersion books continuously; the index options are the short leg. See [[dispersion-trading]].

### Income overlays

Buy-write programs on index options ([[bxm-index|CBOE BXM]]) and put-write programs ([[put-index|CBOE PUT]]) are productized index-options income strategies. Track records exist back to the 1980s with documented Sharpe in the 0.5-0.7 range — modest but genuine, and tax-efficient.

## Risks

- **Notional shock per contract** — an SPX contract is $500K of notional at $100 multiplier on a 5000-level index. A 1% adverse move is $5,000 per contract. Sizing errors are unforgiving.
- **AM-settle gap risk** — overnight news between Thursday close and Friday SOQ can move settlement materially. The August 2015 SPX flash-crash morning is the canonical case.
- **Liquidity collapse on stress days** — bid/ask spreads on far OTM wings widen sharply during volatility spikes, exactly when hedges need to be monetized. Far-OTM puts traded $5+ wide on March 12, 2020.
- **VIX-options peculiarities** — VIX options settle to the VRO (a special opening calculation), not to spot VIX. See [[vix-options]] for the gap between expectations and reality.
- **Pricing tick floors** — the $0.05 / $0.10 tick on SPX limits arbitrage opportunities at the smallest price increments and creates wider effective spreads vs SPY.
- **Section 1256 mark-to-market** — open positions on December 31 generate phantom taxable events even without closing, complicating year-end planning for long-dated structures.
- **Settlement-induced pinning and slippage** — large open interest at popular strikes can produce significant pinning behavior, particularly on monthly OPEX Fridays. See [[max-pain]] and [[options-pinning]].
- **0DTE volume distortion** — the explosion of same-day expiry volume in 2022-2025 has changed intraday gamma and dealer positioning dynamics in ways still being studied. See [[0dte-impact-on-spx]].

## Historical Context

The index-options franchise has been reshaped by a handful of structural episodes that every serious user should know:

- **1983 — CBOE launches OEX (S&P 100) options**, the first cash-settled, broad-based index options and the template for the entire category. SPX followed in 1987.
- **October 19, 1987 (Black Monday)** — the first stress test of listed index options. Portfolio-insurance hedging (a synthetic-put strategy executed in index futures rather than options) is widely cited as an amplifier of the crash, and the episode permanently entrenched the steep index put [[volatility-skew|skew]] that persists to this day: demand for crash protection never normalized after 1987. See [[1987-crash]] and [[volatility-skew]].
- **1993 — the VIX is introduced**, later (2003) recast on the SPX-options-strip methodology, turning index-option implied vol itself into a tracked, ultimately tradable object. See [[vix]] and [[vix-options]].
- **August 24, 2015 — the SOQ flash-crash morning**, when staggered component openings produced an SPX Special Opening Quotation roughly 5% below the prior close, settling AM puts far deeper ITM than Thursday's close implied. The canonical cautionary tale for AM-settlement gap risk. See [[am-vs-pm-settlement]].
- **February 5, 2018 (Volmageddon)** — though centered on [[vix-futures|VIX-futures]] products, it reset the entire listed-vol complex's appreciation of short-vol crowding and tail convexity. See [[xiv-blowup-feb-2018]] and [[volmageddon]].
- **2022–2025 — the 0DTE era** — daily SPX expirations (and later NDX/RUT/XSP dailies) drove same-day options to over 40% of SPX volume, transforming intraday dealer-gamma dynamics and creating an entirely new short-dated retail and systematic flow. See [[zero-dte-options]] and [[0dte-impact-on-spx]].

## Related-Product Comparison

| Product | Settlement | Exercise | Tax | Notional (typical) | Tick | Best for |
|---|---|---|---|---|---|---|
| [[spx-options\|SPX]] | Cash | European | §1256 | ~$500K | $0.05/$0.10 | Scale, tax-sensitive active books |
| [[xsp-options\|XSP]] | Cash | European | §1256 | ~$50K | $0.05 | §1256 benefit at small size |
| [[ndx-options\|NDX]] | Cash | European | §1256 | ~$1.75M | $0.05/$0.10 | Tech-concentrated exposure |
| [[rut-options\|RUT]] | Cash | European | §1256 | ~$200K | $0.05/$0.10 | Small-cap exposure |
| [[spy-options\|SPY]] | Physical | American | Equity | ~$50K | $0.01 | Small accounts, IRAs, penny ticks |
| [[qqq-options\|QQQ]] | Physical | American | Equity | ~$45K | $0.01 | Retail tech exposure |
| [[vix-options\|VIX]] | Cash (VRO) | European | §1256 | ~$1.5K | $0.05/$0.10 | Vol direction, tail hedging |

The recurring trade-off across the franchise: **cash-settled index products** (SPX/NDX/RUT/XSP) win on tax (§1256), exercise (no early assignment), and operational cleanliness; **ETF products** (SPY/QQQ/IWM) win on tick granularity, small-account accessibility, and IRA eligibility. The decision is almost always driven by account size, tax status, and whether early-assignment management is acceptable.

## Related

- [[spx-options]] — the canonical US index options product (deep page)
- [[spy-options]] — physically-settled American-style ETF cousin
- [[xsp-options]] — 1/10 size SPX with same Section 1256 treatment
- [[ndx-options]], [[rut-options]] — Nasdaq-100 and Russell 2000 index options
- [[vix-options]] — options on the volatility index itself
- [[section-1256-contracts]] — the tax framework
- [[am-vs-pm-settlement]] — settlement mechanics and case studies
- [[cash-vs-physical-settlement]] — settlement type contrast
- [[american-vs-european-options]] — exercise style distinction
- [[weekly-options]], [[zero-dte-options]] — short-dated index options
- [[vix]] — implied volatility on SPX, the headline measure
- [[volatility-skew]] — index options have steeper skew than single names
- [[options-premium-selling]] — the strategy class index options dominate
- [[short-strangle]], [[iron-condor]] — canonical structures
- [[options-buying-power-reduction]] — BPR efficiency on indices
- [[theta-targeting]] — sizing framework for index-options income books
- [[variance-risk-premium]] — the structural edge that makes index premium-selling work
- [[itpm-trade-construction-playbook]] — institutional methodology built around index options
- [[options-greeks]] — delta/gamma/theta/vega vocabulary
- [[gamma-exposure]] — dealer-gamma positioning that drives intraday SPX dynamics
- [[implied-volatility]] — the surface index options trade
- [[vix-term-structure]] — the volatility-curve analog for VIX products
- [[calendar-spread]], [[ratio-calendar-spread]] — term-structure structures
- [[0dte-impact-on-spx]] — market-structure effects of the 0DTE boom
- [[1987-crash]] — the event that entrenched index put skew
- [[qqq-options]], [[rut-options]], [[xsp-options]] — sibling index/ETF products

## Sources

- Cboe Global Markets — SPX, NDX, RUT, XSP, VIX product specifications (cboe.com).
- IRC Section 1256 — Internal Revenue Code provisions for broad-based index options.
- IRS Publication 550 — Investment Income and Expenses, Section 1256 mechanics.
- Cboe Special Opening Quotation methodology documentation.
- [[book-option-volatility-and-pricing]] — Natenberg on index-options pricing dynamics.
- [[itpm-options-portfolio-management]] — institutional treatment of index options as the core premium-selling vehicle.
- [[tastytrade-spx-research]] — empirical studies on SPX strangles, condors, and 0DTE strategies.
