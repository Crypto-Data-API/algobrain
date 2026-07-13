---
title: "VIX Options"
type: market
created: 2026-05-07
updated: 2026-06-19
status: excellent
tags: [options, derivatives, volatility, indicators, sp500]
aliases: ["VIX Options"]
domain: [derivatives, options, volatility]
difficulty: advanced
related: ["[[index-options]]", "[[spx-options]]", "[[spy-options]]", "[[xsp-options]]", "[[ndx-options]]", "[[rut-options]]", "[[vix]]", "[[vix-futures]]", "[[vix-calls]]", "[[vix-term-structure]]", "[[contango]]", "[[backwardation]]", "[[long-vol-vs-short-vol]]", "[[tail-hedging]]", "[[volatility-of-volatility]]", "[[vvix]]", "[[section-1256-contracts]]", "[[soq-settlement]]", "[[am-vs-pm-settlement]]", "[[american-vs-european-options]]", "[[cash-vs-physical-settlement]]", "[[implied-volatility]]", "[[volatility-skew]]", "[[variance-risk-premium]]", "[[xiv-blowup-feb-2018]]"]
---

VIX options are Cboe-listed, cash-settled, European-style options on the **Cboe Volatility Index (VIX)** — the headline measure of S&P 500 30-day implied volatility. They carry a $100 contract multiplier, qualify as [[section-1256-contracts|Section 1256 contracts]], settle on Wednesdays (matching VIX futures expiry), and have a single critical structural quirk that separates them from every other index option: they are **priced off VIX futures, not spot VIX**, because the spot VIX index cannot be hedged or replicated directly. This single fact creates the "VIX call term-structure trap" that has cost retail and institutional traders alike enormous sums chasing apparent tail-hedge bargains that fail to deliver as expected.

## Overview

The VIX is computed from a strip of out-of-the-money [[spx-options|SPX]] options, encoding a 30-day forward-looking estimate of S&P 500 implied volatility. It is a calculation, not a tradable instrument — there is no VIX share to buy or borrow. To create options on VIX, Cboe instead pegs VIX options settlement to a **futures-style construction** that references the [[vix-futures|VIX futures]] curve.

Three properties together define VIX options' character:

1. **Cash-settled, European-style** — like other [[index-options]], no physical delivery, no early assignment.
2. **Wednesday expiry** — VIX futures and options expire on Wednesdays (specifically 30 days before the third Friday of the following month for monthly expirations), aligning with the 30-day SPX-options reference window that VIX itself measures.
3. **Settled to the VRO (Special Opening Quotation)** — the VIX equivalent of an SOQ, computed from opening SPX option prices on the morning of expiration. Final settlement is published with ticker **VRO**.

VIX options trade actively in front-month and second-month expirations, with daily volume typically running **400,000-800,000 contracts**. Open interest concentrates heavily in **OTM calls**, which institutional and retail tail-hedgers buy as portfolio insurance.

## Contract Mechanics

| Spec | Value |
|---|---|
| Underlying | Cboe Volatility Index (VIX) — but priced off VIX futures, see below |
| Multiplier | $100 |
| Exercise style | European |
| Settlement | Cash |
| Strike intervals | $0.50 near-the-money; $1 / $2.50 / $5 further out |
| Tick size | $0.05 below $3.00 premium; $0.10 above |
| Expiry day | Wednesday (30 days before the 3rd Friday of the following calendar month for monthlies; intervening Wednesdays for weeklies) |
| Settlement value | VRO — Special Opening Quotation derived from SPX options opening prices on expiration Wednesday at 9:30 am ET |
| Symbol | VIX |
| Tax treatment | [[section-1256-contracts|Section 1256]] (60/40) |
| Listed | Cboe Options Exchange (exclusive) |

At a VIX level of 15, a single VIX option contract has roughly **$1,500 of notional** in index-level terms — far smaller than other index options' notionals — but the leverage on tail moves is enormous: a VIX call struck at 25 can multiply 10-50x in a vol-spike event.

## Settlement

The settlement-day mechanic is essentially: at 9:30 am ET on expiration Wednesday, Cboe runs a **Special Opening Quotation auction** in SPX options that expire 30 days later (matching VIX's forward window). The mid-prices of those SPX options are fed into the VIX formula to produce the **VRO** — the final settlement value.

This creates two practical subtleties:

1. **Settlement uses opening SPX option prices** that may differ from the SPX option mid-prices in the seconds before the bell. Sophisticated traders attempt to influence the SOQ auction; results occasionally diverge from intuitive expectation.
2. **VRO can differ materially from spot VIX** at the moment of settlement, because spot VIX uses near- and next-term SPX options on a continuously updated basis while VRO uses a fixed strip auctioned at the open.

The VRO is published shortly after the open and is the value used to settle every open VIX options position, both calls and puts.

See [[soq-settlement]] for the general SOQ methodology and [[am-vs-pm-settlement]] for the regime context.

## The VIX Call Term-Structure Trap

The single most important thing to understand about VIX options:

> **VIX options are priced off VIX futures, not spot VIX.**

Spot VIX is a calculation derived from a continuously-updated SPX options strip. It cannot be replicated by holding a basket of securities, so it cannot be hedged. A market-maker who sells you a VIX call cannot delta-hedge by buying spot VIX. The only hedgeable instrument is the **VIX future** that expires the same day as the option.

Therefore: a VIX call expiring in, say, 60 days is priced relative to the **60-day VIX future**, not the spot VIX index.

The consequences are dramatic:

### 1. Long VIX calls underperform spot VIX in normal regimes

The VIX futures curve is in **[[contango]]** roughly 80% of the time — far-month futures trade above spot VIX, anticipating mean reversion. A 60-day VIX future at, say, 18 with spot VIX at 15 means a VIX call struck at 18 is "at-the-money" relative to the future even though it is "OTM" relative to spot. As the future rolls down toward spot through time, that call decays not just from theta but from **negative roll yield** on its underlying.

### 2. The "tail hedge" gap

A retail trader looking at VIX = 14 and buying VIX 25 calls "for tail protection" is effectively buying calls struck **above** the futures curve in many regimes, paying a premium that reflects the curve's positive forward expectation, not just spot VIX's distance to 25. When a moderate vol spike sends VIX to 25 but the future settles only at 22 because the market expects fast mean-reversion, **the VIX call pays out far less than spot-VIX-mathematics would suggest**.

This has been demonstrated empirically across virtually every vol spike of the last 20 years: VIX call P&L on small-to-medium vol shocks is consistently disappointing relative to the spot VIX move. Only very large, persistent spikes (March 2020, October 2008) generate the tail-hedge payoffs that match retail intuition.

### 3. The XIV / volmageddon analog

The flip side: short VIX exposure via [[vix-futures]] or VIX call sales benefits enormously from contango decay in normal regimes. This is why short-vol products like XIV produced 30%+ annualized returns from 2012-2017 — until the [[xiv-blowup-feb-2018|February 2018 vol spike]] erased XIV in a single day. The same term-structure asymmetry that makes long VIX calls underperform makes short VIX exposure dangerous: the regimes in which short-vol breaks are exactly the regimes where the futures curve flips to [[backwardation]] and the trade explodes.

### 4. Implication for hedging

Practitioners who use VIX options for portfolio hedging must size positions based on **futures-implied moves**, not spot-VIX-implied moves, and must understand that "VIX 18 to 28" in spot terms may be only "future 22 to 26" in futures terms — meaning a call struck at 25 may pay far less than a naive Black-Scholes-on-spot calculation predicts. Many institutional desks use VIX call **spreads** rather than naked calls, both to reduce premium cost and because the spread payoff structure is more robust to term-structure dynamics.

See [[vix-calls]], [[vix-term-structure]], [[contango]], [[backwardation]].

## Greeks and Vol-Surface Behavior

VIX options' Greeks behave unlike any equity-index option, precisely because the underlying is a [[vix-futures|VIX future]] rather than a tradable spot:

- **Delta is futures-delta, not spot-delta** — a VIX option's delta measures sensitivity to its *reference future*, not to spot VIX. A market-maker delta-hedges with the VX future expiring on the same Wednesday, never with spot. This is why the [[#The VIX Call Term-Structure Trap|term-structure trap]] exists: a call can have high delta to its future yet pay out modestly relative to a spot-VIX move.
- **Gamma and theta** behave conventionally with respect to the future, but the *effective* decay a long-call holder experiences combines option theta with the [[roll-yield|negative roll yield]] of the underlying future drifting down the [[contango]] curve toward spot. The two bleeds compound, which is why long VIX calls held through quiet periods decay faster than option theta alone would predict.
- **Vega is vol-of-vol exposure** — the implied vol *of* VIX options is [[vvix|VVIX]], the volatility-of-volatility index. A long VIX option is implicitly long VVIX; a sharp VVIX move can reprice VIX option premiums substantially even with VIX itself unchanged. This is a second-order risk that catches traders who think of VIX options as simple direct vol bets.

### The inverted (call-up) skew

The VIX option surface is the mirror image of the SPX surface:

- **SPX**: puts richer than calls (downside-crash demand) — a negative [[volatility-skew|skew]].
- **VIX**: calls richer than puts — a *positive*, "up-side" skew. Demand for VIX calls (tail hedges) is one-directional and persistent, and vol-of-vol is itself asymmetric: VIX spikes up violently and grinds down slowly, so upside VIX-call IV is structurally bid.

This inversion means traders accustomed to selling rich SPX puts must invert their intuition on VIX: it is the *calls* that carry the persistent richness, and short-VIX-call overlays are the VIX-side analog of short-SPX-put overlays — with the same open-ended tail risk demonstrated by [[xiv-blowup-feb-2018|Volmageddon]].

### Surface dynamics across regimes

In calm regimes the VIX future curve is in steep [[contango]] and the VIX option surface is relatively flat and cheap in absolute premium. In stress the curve flips to [[backwardation]], VVIX spikes, and the entire VIX option surface lifts and steepens on the call side simultaneously — meaning the cost of *adding* VIX-call protection rises exactly when it is most wanted. This is the structural reason tail hedges must be bought in calm, not in crisis. See [[vix-term-structure]] and [[tail-hedging]].

## Term Structure

VIX options inherit the [[vix-term-structure|VIX futures term structure]] because each expiry is priced off its own reference future:

| Regime | Curve shape | Effect on VIX options |
|---|---|---|
| Steep [[contango]] (~80% of days) | Far futures > near futures > spot | Long calls bleed roll-down; short-vol overlays earn carry |
| Mild contango | Gentle upward slope | Baseline; modest roll cost on long calls |
| Flat | Curve compressed | Transition zone; vol about to break |
| [[backwardation]] | Near futures > far futures > spot | Crisis; long calls finally pay convexly, short-vol blows up |

Because each VIX option references the future expiring on its own Wednesday, a **VIX calendar spread is not a pure-time spread** — the near and far legs reference *different underlying futures* that can move independently. This makes VIX calendars and diagonals genuinely term-structure trades (a view on the slope of the VX curve), not the same-underlying time decay trades that SPX calendars represent. See [[calendar-spread]] and [[vix-futures]].

## Common Spread Structures

| Structure | Construction | View | Why VIX-specific |
|---|---|---|---|
| Long VIX call | Buy OTM call | Long tail / vol spike | Subject to term-structure trap; underperforms spot intuition |
| VIX call spread | Buy lower call, sell higher call | Cheaper tail hedge | Caps cost; more robust to curve dynamics than naked call |
| VIX call ladder / 1x2 | Buy one call, sell two further-OTM | Convex but capped tail | Reduces premium bleed in calm regimes |
| VIX put / put spread | Long downside | Bet on vol mean-reversion | Profits from contango grind-down |
| VIX calendar | Sell near future's option, buy far | Curve-slope view | Legs reference different futures — true term-structure trade |
| Short VIX call (overlay) | Sell OTM call | Carry / short vol | Open-ended risk; the Volmageddon-style blow-up exposure |

Institutional desks overwhelmingly prefer **call spreads over naked calls** for tail hedging, both to cut the continuous premium bleed and because the spread's payoff is less distorted by the futures-vs-spot gap. See [[tail-hedging]] and [[vix-calls]].

## Liquidity & Spreads

- **Volume** — typically **400,000-800,000 contracts/day**, third-most-liquid US index option (behind SPX and SPY); concentrated in **front-month and second-month** expirations and in OTM calls.
- **Bid/ask** — **$0.05-$0.10** wide on near-the-money front-month strikes; **$0.20-$1+** on back-month and far-OTM strikes.
- **Open interest** — heavily skewed toward OTM calls, which dwarf put open interest by typically 5-10x. This reflects the dominant use case (tail hedging) and produces a permanent positive convexity in dealer positioning.
- **Strike density** — $0.50 increments below 20, $1 above, with $2.50 / $5 in the deep wings.
- **Skew** — VIX call skew is **inverted** vs SPX: calls are more expensive than puts in implied-vol terms because vol-of-vol asymmetry favors upside spikes. See [[vvix]] and [[volatility-of-volatility]].
- **VRO settlement liquidity** — the SPX option auction underpinning VRO is typically smooth, but it has occasionally produced surprising prints when SPX opening liquidity is thin (e.g., overnight gap mornings).

## Use Cases

### Tail hedging

The flagship use case. Long VIX calls (or call spreads) on a long-equity portfolio aim to monetize a sharp risk-off episode. In moderate vol spikes the term-structure trap eats most of the expected payoff; in large persistent spikes (March 2020, August 2024 unwind) the calls pay off in multiples. The trade-off — paying continuous premium for the chance of a large payout in genuine tail events — is exactly the tail-hedge proposition.

### Volatility direction expression

Pure directional vol views — "I think VIX will rise (or fall) over the next 30-60 days" — are most cleanly expressed via VIX options, because [[vix-futures|VIX futures]] alone embed roll yield that can swamp the directional view in low-vol regimes. Options' nonlinear payoff structure separates the directional view from the term-structure carry.

### Vol-of-vol expression

The implied volatility *of VIX options themselves* is the [[vvix|VVIX]] index — the second-moment view on volatility. VIX options structures (calendars, butterflies) are the way to express a vol-of-vol view directly, used by sophisticated tail-risk and dispersion books.

### Long/short vol overlays

Persistent overlays that are long downside VIX puts (collecting decay when vol stays high) or short upside VIX calls (collecting decay in normal regimes) generate the [[variance-risk-premium]] premium-selling on the vol-product side rather than the equity-options side. Drawdowns on short-VIX positions can be dramatic — the 2018 volmageddon episode is the canonical case.

### Calendar and term-structure trades

Selling front-month VIX vol against buying back-month VIX vol — or vice versa — expresses views on the curve's contango/backwardation dynamics. These are operationally subtle because of the underlying-future change between expiries.

## Risks / Quirks

- **Term-structure trap on long calls** — long VIX calls underperform spot-VIX-based intuition in normal regimes; large positions sized on spot-VIX assumptions can disappoint badly.
- **Wednesday expiry, not Friday** — operationally distinct from every other major index option; spread structures that mix VIX with SPX have date-mismatched legs.
- **VRO settlement risk** — the VRO can deviate from intuitive expectation when SPX opening auction is unusual (overnight gaps, low liquidity at the bell).
- **Inverted skew vs SPX** — VIX call IV > VIX put IV, opposite the equity-options skew structure traders are used to.
- **Vol-of-vol risk** — VIX options' own pricing is highly sensitive to changes in VVIX; a vol-of-vol regime shift can move VIX option premiums substantially even with VIX itself unchanged.
- **Roll cost on overlays** — persistent long-VIX overlays bleed contango-driven decay across rolls in normal regimes.
- **Short-vol blowup risk** — short VIX option positions face open-ended upside risk; the XIV episode of February 2018 (single-day -90%+) is the canonical disaster.
- **Liquidity concentrations** — back-month strikes can be very thin; large positions there require patience and limit-order discipline.

## Tax Treatment

VIX options qualify as **broad-based stock index options** under IRC §1256, despite the underlying being a volatility calculation rather than an equity index. This grants [[section-1256-contracts|Section 1256]] treatment:

- **60/40 blended** — every realized gain or loss is split 60% long-term / 40% short-term regardless of holding period.
- **Mark-to-market on December 31** — open positions deemed-closed at year-end FMV, reported on Form 6781.
- **3-year loss carryback** against prior Section 1256 gains.
- **No standard §1091 wash-sale concerns** in the equity sense.

The Section 1256 treatment is materially more favorable than the standard equity-options treatment that applies to ETF-based vol products like UVXY or SVXY — another structural reason institutional vol books prefer VIX options to ETF wrappers.

See [[section-1256-contracts]].

## How Traders Use VIX Options — Playbook

| Goal | Typical structure | Notes |
|---|---|---|
| Cheap insurance against a crash | OTM VIX call **spread**, rolled monthly | Cheaper than naked calls; accept that moderate spikes pay little |
| Express "vol will rise into a catalyst" | Front/second-month call or call spread | Cleaner than futures, which embed roll yield |
| Harvest contango carry | Short OTM call overlay (small, defined) | The XIV trade in disguise — open-ended risk |
| Bet on mean-reversion after a spike | Put or put spread bought in backwardation | Profits as curve normalizes back to contango |
| Trade the curve slope | VIX calendar (different reference futures) | A genuine term-structure trade, not pure theta |
| Trade vol-of-vol | Butterfly / calendar structures | Implicit [[vvix\|VVIX]] exposure |

Disciplined practitioners follow three rules drawn from the structural quirks above: (1) **size on futures-implied moves, not spot-VIX moves**; (2) **buy protection in calm, when contango makes it cheapest, not in crisis**; (3) **prefer defined-risk spreads to naked positions** because the futures-vs-spot gap and VVIX sensitivity make naked VIX options behave unpredictably.

## Historical Context

VIX options launched on the Cboe in **2006**, two years after [[vix-futures|VIX futures]] (2004) — the futures came first precisely because options need a hedgeable underlying, and spot VIX is not tradable. The product's defining historical episodes are the same ones that define the listed-vol complex:

- **2008 GFC** — VIX spiked toward record highs; long VIX calls and futures paid off in multiples, validating the tail-hedge thesis for the products that survived.
- **August 2015 China-devaluation flash crash** — a sharp but short vol spike; a textbook case where short-dated long VIX calls underperformed spot-VIX intuition because the futures curve never fully repriced.
- **[[xiv-blowup-feb-2018|February 2018 (Volmageddon)]]** — the seminal short-vol disaster: the [[xiv-blowup-feb-2018|XIV note was terminated]] after a single overnight session, and short-VIX positions (including short VIX-call overlays) suffered open-ended losses. The episode is the permanent reference point for VIX-option short-side risk. See [[volmageddon]].
- **March 2020 (COVID)** — VIX reached its highest-ever spot print; long VIX calls and futures returned multiples for hedgers who held them, the rare "tail event large and persistent enough to overcome the term-structure trap."
- **August 2024 yen-carry-unwind** — the largest single-session percentage move in VIX history; another reminder that short-vol crowding migrates but never disappears. See [[vix-august-2024-spike]].

These episodes share one lesson: VIX options reward convex *long-tail* positioning held patiently and punish *short-tail* carry positioning sized for the calm regime that will not last.

## Related-Product Comparison

| Vehicle | Wrapper | Tax | Tail-hedge quality | Carry quality |
|---|---|---|---|---|
| **VIX options** | Listed option | [[section-1256-contracts\|§1256]] (60/40) | Best convexity (calls); curve-aware | Defined-risk short overlays possible |
| [[vix-futures\|VIX futures]] | Listed future | §1256 | Linear, not convex; bleeds on long side | Cleanest short-carry expression |
| [[vxx\|VXX]] / [[uvxy\|UVXY]] | ETN/ETF (long) | Equity | Linear bleed; poor long-run hedge | n/a |
| [[svxy\|SVXY]] | ETF (-0.5x short) | Equity | n/a | De-levered post-2018; capped carry |

VIX options are the **only listed vehicle that delivers genuine convexity** on the long side — futures and long ETPs bleed linearly, while options' nonlinear payoff is what tail-hedgers actually want. This convexity, plus §1256 tax treatment, is why institutional tail-risk books center on VIX options (and call spreads) rather than VIX-futures-linked ETPs. See [[vix-futures]], [[tail-hedging]], and [[long-vol-vs-short-vol]].

## Related

- [[index-options]] — overview of the franchise
- [[vix]] — the underlying index
- [[volatility]] — the asset class VIX options trade
- [[vix-futures]] — the actual instrument VIX options reference
- [[vix-calls]] — deep dive on long-VIX-call mechanics and historical performance
- [[vix-term-structure]], [[contango]], [[backwardation]] — curve dynamics
- [[vvix]], [[volatility-of-volatility]] — second-moment view
- [[long-vol-vs-short-vol]] — the strategic split
- [[tail-hedging]] — the dominant use case
- [[xiv-blowup-feb-2018]] — short-vol disaster case study
- [[spx-options]] — VIX is calculated from SPX option prices
- [[section-1256-contracts]] — tax framework
- [[soq-settlement]] — VRO methodology
- [[american-vs-european-options]], [[cash-vs-physical-settlement]]
- [[implied-volatility]], [[volatility-skew]]
- [[variance-risk-premium]] — the structural premium short-vol harvests
- [[options-greeks]] — Greeks vocabulary (delta is futures-delta here)
- [[roll-yield]] — the curve drift that compounds with theta on long calls
- [[calendar-spread]] — VIX calendars are true term-structure trades
- [[volmageddon]], [[vix-august-2024-spike]] — short-vol blow-up episodes
- [[vxx]], [[uvxy]], [[svxy]] — VIX-linked ETP alternatives
- [[long-vol-vs-short-vol]] — the strategic split

## Sources

- Cboe VIX Options product specifications (cboe.com/tradable_products/vix/vix_options) — multiplier, expiry, settlement.
- Cboe VIX White Paper — VIX index calculation methodology.
- Cboe VRO Special Opening Quotation methodology documentation.
- IRC Section 1256 — broad-based index option qualification (including volatility indices).
- Cboe VIX Futures product specifications — futures-curve mechanics underpinning options pricing.
- [[xiv-blowup-feb-2018]] — empirical short-vol disaster reference.
