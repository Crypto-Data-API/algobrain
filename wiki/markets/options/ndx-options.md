---
title: "NDX Options"
type: market
created: 2026-05-07
updated: 2026-06-19
status: excellent
tags: [options, derivatives, nasdaq, indicators, stocks]
aliases: ["NDX Options", "Nasdaq-100 Options"]
domain: [derivatives, options, equity-indices]
difficulty: intermediate
related: ["[[index-options]]", "[[options]]", "[[spx-options]]", "[[spy-options]]", "[[xsp-options]]", "[[rut-options]]", "[[vix]]", "[[vix-options]]", "[[qqq-options]]", "[[nasdaq-100]]", "[[section-1256-contracts]]", "[[am-vs-pm-settlement]]", "[[soq-settlement]]", "[[cash-vs-physical-settlement]]", "[[american-vs-european-options]]", "[[options-greeks]]", "[[implied-volatility]]", "[[volatility-skew]]", "[[dispersion-trading]]", "[[short-strangle]]", "[[iron-condor]]"]
---

NDX options are Cboe-listed, cash-settled, European-style index options on the [[nasdaq-100|Nasdaq-100 Index]] — the 100 largest non-financial companies listed on Nasdaq, dominated by mega-cap technology names. They carry a $100 contract multiplier, qualify as [[section-1256-contracts|Section 1256 contracts]] for US tax purposes, and are the canonical institutional vehicle for expressing concentrated tech-sector exposure or hedging a tech-heavy book without reverting to single-name options or to the more diversified [[spx-options|SPX]].

## Overview

The Nasdaq-100 trades at a higher index level than SPX and is materially more concentrated: the top 10 names regularly account for 50%+ of the index weight, all of them in technology, communications, and consumer-discretionary sectors. NDX options inherit this concentration in their realized vol and skew profiles — NDX implied vol is typically 2-4 vol points higher than SPX, and the skew is steeper on the put side, reflecting the perception that a tech-led drawdown carries higher tail risk than a broad-market one.

NDX options exist alongside [[qqq-options|QQQ options]] (on the Invesco QQQ ETF) in the same way [[spx-options|SPX]] exists alongside [[spy-options|SPY]]:

- **NDX**: index, cash-settled, European-style, Section 1256 — the institutional product.
- **QQQ**: ETF, physical-settled, American-style, standard equity tax — the retail-friendly product with penny ticks and ~1/40 the notional.

For a tech-concentrated portfolio at meaningful size, NDX is the default. For sub-$100K accounts, QQQ is more accessible.

## Contract Mechanics

| Spec | Value |
|---|---|
| Underlying | Nasdaq-100 Index (NDX) |
| Multiplier | $100 |
| Exercise style | European |
| Settlement | Cash |
| Strike intervals | $25 standard; $5 increments common on weeklies near-the-money |
| Tick size | $0.05 below $3.00 premium; $0.10 above |
| Trading hours | 9:30 am – 4:15 pm ET regular session; Cboe Global Trading Hours session for NDX is more limited than SPX |
| Symbols | NDX (AM-settled monthlies), NDXP and NDXW (PM-settled weeklies/dailies) |
| Tax treatment | [[section-1256-contracts|Section 1256]] (60/40) |
| Listed | Cboe Options Exchange (exclusive Cboe license) |

At an NDX index level of 17,500, a single contract represents roughly **$1.75 million of notional** — the largest per-contract notional of any major US-listed index option, and one of the practical reasons NDX volume sits well below SPX. Position sizing on NDX requires real care: a 1% adverse move is $17,500 per contract.

## Settlement

Two settlement regimes coexist, mirroring the SPX/SPXW split:

- **AM settlement (NDX monthlies)** — settles to the **Special Opening Quotation (SOQ)** of the Nasdaq-100 on the third Friday, calculated from the opening prints of all 100 component stocks. Final trading occurs the prior afternoon, so AM-settled monthly NDX positions face overnight gap risk between Thursday close and Friday SOQ. With 50%+ of index weight in fewer than 10 names, an opening gap in any of the megacaps (AAPL, MSFT, NVDA, AMZN, META, GOOGL, TSLA) translates directly into SOQ slippage.
- **PM settlement (NDXP and NDXW weeklies and dailies)** — settles to the official 4:00 pm ET closing print of the Nasdaq-100. Trading on the expiration day continues until 4:00 pm.

See [[am-vs-pm-settlement]] for the broader regime and [[soq-settlement]] for the SOQ calculation. The "Thursday-night gap" risk on NDX AM monthlies is structurally larger than on SPX precisely because of the heavier index concentration.

## Liquidity & Spreads

NDX is the second-most-liquid US index option after SPX, but the gap is large:

- **Volume** — typically **40,000-80,000 contracts/day**, vs SPX's 2-4 million. NDX activity has grown materially since 2022 with the introduction of NDXP daily expirations.
- **Bid/ask** — **$0.10-$0.50 wide** on near-the-money strikes; **$1+ wide** on far-OTM wings. Penny-equivalent (after the $100 multiplier) is rare on NDX outside the most liquid front-month strikes.
- **Strike density** — $25 standard intervals are coarse compared to SPX's $5 grid; some $5-increment strikes near-the-money on weeklies improve granularity but the deep wings remain sparse.
- **Quote sizes** — typically 10-50 contracts at the inside near-the-money; market-makers compete but nothing like the depth on SPX.
- **Far-OTM liquidity** — meaningfully thinner than SPX, especially in stress. Hedge unwinds on NDX wings can carry 50-100 bps of slippage on a normal day, more in vol spikes.

For traders accustomed to SPX execution, the practical adjustment on NDX is: work limits aggressively, never use market orders on wings, and be aware that quote sizes and depth are an order of magnitude smaller.

## Greeks and Volatility-Surface Behavior

NDX options share the [[options-greeks|Greeks]] framework of all cash-settled [[index-options]] — clean delta with no early-exercise distortion, theta-driven decay, vega exposure to the tech-vol surface — but the index's concentration gives the surface a distinctive character:

- **Delta** — clean European/cash-settled delta. Because the top names dominate, NDX delta is in practice heavily exposed to a handful of megacaps (AAPL, MSFT, NVDA, AMZN, META, GOOGL, TSLA); a single-name shock translates almost directly into NDX delta moves.
- **Gamma** — NDX's coarser $25 strike grid and thinner depth mean dealer-gamma effects are less smoothly distributed than SPX, but the introduction of NDXP daily expirations since 2022 has built a short-dated gamma profile of its own. See [[gamma-exposure]].
- **Theta** — the decay engine for NDX [[options-premium-selling|premium selling]], which empirically harvests a slightly larger [[variance-risk-premium]] than SPX because of higher realized vol.
- **Vega** — NDX is the listed vehicle for broad tech-vol exposure; its implied-vol analog to [[vix|VIX]] is **VXN** (Nasdaq-100 volatility index), which typically runs above VIX.

### The NDX volatility surface

- **Elevated absolute vol** — NDX implied vol is typically 2-4 vol points higher than SPX (as noted above), reflecting the index's tech concentration and higher realized vol.
- **Steeper put [[volatility-skew|skew]]** — the market prices a tech-led drawdown as carrying higher tail risk than a broad-market one, so NDX downside puts are richer in vol-point terms than SPX's. Hedging NDX is structurally more expensive in IV terms even after notional adjustment.
- **Earnings-cluster term-structure bumps** — when 5-7 megacaps report within a single window (common in late-January and late-July), the NDX surface develops a local vol bump around that expiry, which calendars and diagonals can isolate.
- **Volatility-of-volatility** — VXN itself moves; the second-moment behavior of the tech-vol surface is more violent than the broad market's.

## Term Structure

NDX implied vol carries the same broad shape as SPX — upward-sloping in calm regimes, inverting in stress — but with two NDX-specific features:

| Regime / event | Term-structure effect | Structure response |
|---|---|---|
| Calm | Upward-sloping (near vol < far vol) | Sell near-dated theta; calendars to be long vega |
| Stress / tech selloff | Inverts faster and harder than SPX | Near-dated premium very rich; tail hedges expensive |
| Megacap earnings cluster | Local kink around the earnings-window expiry | Calendars/diagonals isolate the event bump |

Because every NDX expiry references the same Nasdaq-100 index, NDX calendars are **pure same-underlying time spreads** (like [[spx-options|SPX]], unlike [[vix-options|VIX]] calendars). The coarser $25 strike grid, however, makes precise calendar/diagonal construction harder than on SPX. See [[calendar-spread]] and [[implied-volatility]].

## Common Spread Structures

| Structure | Construction | View | NDX-specific note |
|---|---|---|---|
| [[short-strangle\|Short strangle]] | Sell OTM put + OTM call | Range-bound / short tech vol | Larger VRP than SPX; wider spreads, bigger notional |
| [[iron-condor\|Iron condor]] | Short strangle + protective wings | Range-bound, defined risk | $25 grid limits wing precision vs SPX |
| Long NDX call / call spread | Buy upside | Directional tech bull view | Captures AAPL/MSFT/NVDA upside without picking a winner |
| Long NDX put / put spread | Buy downside | Hedge a tech-heavy book | One trade hedges sector concentration |
| Earnings-cluster straddle | Long ATM straddle into cluster | Bet on cumulative earnings vol | Replaces legging into 5+ single-name straddles |
| SPX-vs-NDX [[dispersion-trading\|dispersion]] | Sell NDX vol, buy SPX vol (or reverse) | Tech-vs-broad-market vol view | The canonical index-pair dispersion trade |

The recurring NDX caution: every structure carries **larger per-contract notional (~$1.75M), wider bid/ask, and thinner wings** than the SPX equivalent, so operational P&L is noisier. See [[itpm-trade-construction-playbook]].

## Typical Strategies / Use Cases

### Tech-concentrated risk expression

NDX options are the cleanest single-instrument way to express a directional or volatility view on US mega-cap tech as a complex. A long NDX call position captures upside across AAPL/MSFT/NVDA/AMZN simultaneously without needing to pick the winner; a long NDX put captures the entire sector's drawdown without single-name idiosyncratic risk.

### Tech vs broad-market dispersion

The **SPX-vs-NDX dispersion trade** sells NDX vol against buying SPX vol (or vice versa), expressing a view on whether tech concentration will lead or lag the broader market in vol terms. With Nasdaq-100 names representing ~50% of SPX weight, the two indices co-move heavily but not perfectly — the residual is the dispersion. See [[dispersion-trading]].

### Hedging a long-tech book

For long-short funds with a tech-heavy long book, NDX puts hedge sector concentration without requiring the trader to leg out individual names. The Section 1256 treatment improves after-tax hedge cost vs equivalent QQQ hedges.

### Premium selling on tech vol

NDX [[short-strangle|strangles]] and [[iron-condor|iron condors]] capture the tech-sector [[variance-risk-premium]], which empirically runs slightly larger than SPX's because of higher realized vol and steeper skew. The trade-off: wider bid/ask, larger per-contract notional, and thinner wings make the operational P&L noisier than the equivalent SPX strategy.

### Earnings-cluster hedges

When 5-7 of the top NDX names report earnings within a single window (a common occurrence in the late-January and late-July quarters), NDX implied vol embeds the cumulative earnings-event risk. Traders express views on the cluster via NDX straddles or condors rather than legging into 5+ single-name structures.

## Risks / Quirks

- **Concentration risk** — NDX is not a "diversified" index in the SPX sense. The top 10 weights drive the bulk of moves; an NVDA-specific shock can move NDX 1-2% in a single session.
- **AM-settle gap on monthlies** — overnight news on a megacap (an after-hours guidance cut, a regulatory headline) can move the NDX SOQ materially relative to Thursday close.
- **Higher per-contract notional** — at $1.75M+ per contract, sizing errors are amplified vs SPX (~$500K) and vs XSP/SPY (~$50K).
- **Wider effective spreads** — particularly on wings, eroding edge on tactical and scalping strategies.
- **Steeper skew** — long-tail puts are expensive in vol-point terms; the cost of hedging NDX is structurally higher than hedging SPX in IV terms even after notional adjustment.
- **Dividend-yield drift** — NDX has a lower aggregate dividend yield than SPX, which affects the put-call parity calculation and the cost-of-carry term in pricing models.
- **Single-name event risk** — earnings, M&A, regulatory news, or a single CEO headline (Musk, etc.) can jolt NDX in ways the SPX won't see.

## Tax Treatment

NDX options are **broad-based stock index options** under IRC §1256, qualifying for [[section-1256-contracts|Section 1256]] treatment:

- **60/40 blended** — every realized gain or loss is split 60% long-term / 40% short-term regardless of holding period.
- **Mark-to-market on December 31** — open positions are deemed-closed at year-end FMV, with results reported on Form 6781.
- **3-year loss carryback** against prior Section 1256 gains.
- **No standard §1091 wash-sale concerns** in the equity sense.

The same after-tax math that favors SPX over SPY applies to NDX over [[qqq-options|QQQ]]: the 60/40 rate is roughly **26.8% federal** vs **~37% short-term**, so an active premium-seller's after-tax return on NDX is several percentage points higher per year than the equivalent QQQ strategy. The tax penalty for "trading down" to QQQ is the principal reason institutional tech-vol books stay in NDX despite QQQ's tighter quoting.

See [[section-1256-contracts]] for full mechanics.

## Historical Context

The Nasdaq-100 index was launched in **1985**, and NDX index options followed as part of the broad-based index-options franchise that began with OEX (1983) and SPX (1987). NDX's history as a trading vehicle is inseparable from the rise of the technology sector:

- **2000–2002 dot-com bust** — the defining tech-concentration stress for the index; the Nasdaq-100 fell far more than the S&P 500, permanently establishing NDX's reputation for higher tail risk and the steeper put [[volatility-skew|skew]] it still carries.
- **2010s megacap concentration** — the rise of the "FAANG"/megacap complex steadily concentrated NDX weight into a handful of names, so that the top 10 now regularly exceed 50% of index weight. This is the structural source of NDX's single-name event risk.
- **2022 — NDXP daily expirations** — Cboe extended short-dated and daily expirations to NDX (NDXP/NDXW), driving the volume growth noted above and building a 0DTE-style short-dated profile that mirrors the [[spx-options|SPX]] 0DTE boom. See [[zero-dte-options]].
- **2023–2024 AI-driven concentration** — the AI-led megacap rally (NVDA in particular) pushed concentration to record levels, making NDX increasingly a bet on a small cluster of names and amplifying the single-name event risk the page flags below.

## Related-Product Comparison

| Dimension | NDX | [[qqq-options\|QQQ]] |
|---|---|---|
| Underlying | Nasdaq-100 Index | Invesco QQQ ETF |
| Settlement | Cash | Physical (100 shares) |
| Exercise | European | American |
| Tax | [[section-1256-contracts\|§1256]] (60/40) | Standard equity |
| Notional / contract | ~$1.75M (NDX 17,500) | ~$45K |
| Tick | $0.05/$0.10 | $0.01 (penny) |
| Strikes | $25 (some $5 weeklies) | $1 broadly |
| Early-assignment risk | None | Yes (esp. ex-dividend) |
| Best for | Institutional tech-vol books, scale | Retail, IRAs, granular sizing |

The NDX/QQQ relationship is the tech analog of SPX/SPY: cash-settled NDX wins on tax and exercise; ETF-based QQQ wins on tick granularity and small-account accessibility. The decision turns on account size, tax status, and assignment tolerance. See [[spx-options]] and [[spy-options]] for the broad-market version of the same trade-off.

## Related

- [[index-options]] — overview of the index-options franchise
- [[options]] — options fundamentals
- [[spx-options]] — broad-market sibling, deeper liquidity
- [[xsp-options]] — mini-SPX with same Section 1256 treatment, smaller notional
- [[spy-options]] — physically-settled ETF cousin to SPX
- [[qqq-options]] — physically-settled ETF cousin to NDX
- [[rut-options]] — Russell 2000 small-cap sibling
- [[vix]] — the S&P 500 volatility index (NDX's analog is VXN)
- [[vix-options]] — options on volatility itself (referenced to SPX, not NDX)
- [[nasdaq-100]] — the underlying index
- [[section-1256-contracts]] — tax framework
- [[am-vs-pm-settlement]] — settlement regime split
- [[soq-settlement]] — SOQ calculation methodology
- [[cash-vs-physical-settlement]]
- [[american-vs-european-options]]
- [[volatility-skew]] — NDX skew is steeper than SPX
- [[dispersion-trading]] — SPX-vs-NDX is a canonical pair
- [[options-greeks]], [[implied-volatility]]
- [[short-strangle]], [[iron-condor]]
- [[calendar-spread]] — same-underlying term-structure trade
- [[gamma-exposure]] — dealer-gamma market structure
- [[variance-risk-premium]] — the premium tech-vol selling harvests
- [[zero-dte-options]] — NDXP daily expirations
- [[options-buying-power-reduction]] — portfolio-margin efficiency
- [[nasdaq]] — the exchange behind the index

## Sources

- Cboe NDX product specifications (cboe.com/tradable_products/sp_500/ndx_options) — multiplier, settlement, expirations.
- Cboe Special Opening Quotation methodology documentation.
- Nasdaq Inc. — Nasdaq-100 Index methodology and component weights.
- IRC Section 1256 — broad-based index option qualification.
- IRS Publication 550 — Section 1256 mechanics.
