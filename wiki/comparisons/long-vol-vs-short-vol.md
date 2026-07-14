---
title: "Long Volatility vs Short Volatility"
type: comparison
created: 2026-05-05
updated: 2026-06-20
status: excellent
tags: [options, volatility, comparison, strategy-types]
aliases: ["Long Vol vs Short Vol", "Vol Buyer vs Vol Seller"]
related: ["[[variance-risk-premium]]", "[[volatility-regime-classification]]", "[[tail-risk-hedging]]", "[[options-premium-selling]]", "[[options-portfolio-construction]]", "[[vega-budgeting]]", "[[vix-august-2024-spike]]", "[[long-vol-overlay]]", "[[long-volatility-strategies]]", "[[short-volatility-strategies]]", "[[regime-matrix]]", "[[market-regime]]"]
subjects: ["[[long-volatility-strategies]]", "[[short-volatility-strategies]]"]
comparison_dimensions: [P&L profile, Sharpe, blow-up risk, regime fit, capital efficiency, psychology]
---

## Overview

Long [[volatility]] versus short volatility is the most fundamental book-bias choice an options portfolio manager makes, deeper than direction or tenor (the market's reference gauge for expected equity volatility is the [[vix|VIX]]). **Long vol** means owning [[options-greeks|gamma and vega]]: paying [[theta-decay|theta]] every day in exchange for convex payoff when realized vol expands or markets crash. **Short vol** means selling gamma and vega: collecting theta in calm regimes and absorbing tail risk when shocks arrive. The two profiles are mirror images: their P&Ls, Sharpe ratios, drawdown shapes, and psychological demands are opposites. The crucial nuance is that most professionally managed options books are not purely one or the other -- they run a [[variance-risk-premium|VRP]]-harvesting short-vol core with an explicit [[long-vol-overlay|long-vol overlay]] to cap the blow-up. Picking a side without understanding the synthesis is how retail blows up; understanding the synthesis is how [[universa-investments|Universa]], [[ljm-preservation-and-growth|LJM]] (in reverse), and the survivors of [[volmageddon|February 2018]] and [[vix-august-2024-spike|August 2024]] separate.

## Long Volatility Explained

A **long-vol** book is **net long options**. The trader buys puts, calls, straddles, strangles, [[vix-calls|VIX calls]], or [[variance-swaps|variance swaps]], and the position has:

- **Positive [[gamma]]** -- it gets longer as the market falls and shorter as it rises (or vice versa for calls), so realized moves create P&L regardless of direction.
- **Positive [[vega]]** -- it makes money when [[implied-volatility]] rises.
- **Negative [[theta]]** -- it bleeds premium every day the market is calm. This is the rent paid to own optionality.
- **Convex payoff** -- losses are bounded at the premium spent; gains are essentially uncapped.

The archetypal long-vol vehicles are:

- **[[universa-investments]]** -- [[mark-spitznagel]]'s tail-risk fund, advised by [[nassim-taleb]]. Buys deep OTM SPX puts continuously, accepts steady premium bleed, and reportedly returned over 4,000% in March 2020. See [[tail-risk-hedging]].
- **[[longtail-alpha]]** -- Vineer Bhansali's vol-buying fund. Combines OTM puts, VIX calls, and convexity trades.
- **[[saba-capital-tail-fund]]** -- Boaz Weinstein's credit-and-vol tail vehicle.
- **Retail tail hedgers** -- DIY versions buying SPY puts 3-6 months out, 10-20% OTM, sized at 1-3% of NAV per year.

The defining characteristic is that long-vol books **lose money most days** and **make a year of returns in a week** during a crash. This is the [[crisis-alpha]] profile.

## Short Volatility Explained

A **short-vol** book is **net short options**. The trader sells puts, calls, strangles, iron condors, [[covered-calls]], [[cash-secured-puts]], or shorts [[vix-futures]], and the position has:

- **Negative gamma** -- it gets shorter as the market falls and longer as it rises, accumulating losses on big moves in either direction.
- **Negative vega** -- it loses when implied vol rises.
- **Positive theta** -- it earns premium every day the market is calm. This is the income the strategy is built to harvest.
- **Concave payoff** -- gains are bounded at the credit collected; losses can be many multiples of the credit, or theoretically unbounded for naked calls.

The archetypal short-vol vehicles are:

- **tastytrade retail premium sellers** -- the doctrine of selling 16-30 delta strangles, taking profits at 50% of credit, and managing winners aggressively. See [[tom-sosnoff]] and [[tastytrade-mechanics]].
- **[[ljm-preservation-and-growth]]** -- a short-vol fund that lost ~80% in a single day on **February 5-6, 2018** ([[volmageddon]]) and was wound down. The textbook short-vol blow-up.
- **Risk-parity short-vol overlays** -- many large allocators run "income enhancement" sleeves selling SPX puts to monetize the [[variance-risk-premium]].
- **[[xiv-velocity-shares]]** and **SVXY** -- short-VIX-futures ETPs. XIV terminated on Feb 5, 2018 after losing 96% intraday.
- **Structured products** -- autocallables, reverse convertibles, and yield-enhancement notes are short-vol in disguise. The investor is paid a coupon for being short a put.

The defining characteristic is that short-vol books **make money most days** and **lose multiple years of P&L in a week** during a vol shock.

## Comparison Table

| Dimension | Long Volatility | Short Volatility |
|---|---|---|
| **Net options position** | Net long premium | Net short premium |
| **[[gamma]]** | Positive (benefits from realized moves) | Negative (penalized by realized moves) |
| **[[vega]]** | Positive (wins on IV expansion) | Negative (loses on IV expansion) |
| **[[theta]]** | Negative (bleeds premium daily) | Positive (collects premium daily) |
| **P&L skew** | Positive skew (many small losses, occasional huge wins) | Negative skew (many small wins, occasional huge losses) |
| **Expected return (gross)** | -1% to -3% per year (premium bleed) | +5% to +12% per year ([[variance-risk-premium]] capture) |
| **Hit rate** | Low (~10-30% of months profitable) | High (~70-90% of months profitable) |
| **Sharpe (in-sample, calm regimes)** | Negative (often -0.3 to -0.8) | High (often 1.5-3.0+) |
| **Sharpe (full cycle including shocks)** | Roughly flat to slightly positive when monetized well | 0.4-0.8 once tail events are included |
| **Max drawdown** | Bounded, slow bleed (5-15% over a calm year) | Catastrophic and fast (40-100% in days) |
| **Worst day** | -1% to -2% (just more theta bleed) | -20% to -100% (vol shock + gap) |
| **Regime fit** | Stressed / Crash regimes (see [[volatility-regime-classification]]) | Calm / Normal regimes |
| **Capital efficiency** | Capital-light always (premium = max loss) | Capital-efficient until shock; margin spikes 5-10x in stress |
| **Liquidity demands in stress** | Position becomes more liquid (puts trade easily) | Position becomes illiquid; bid-ask widens 10x |
| **Margin call risk** | None (paid upfront) | Severe (portfolio margin reprices instantly) |
| **Psychology** | Lonely losses; doubt during long calm | Dopamine cycle; sudden ruin |
| **Survivor bias in track records** | Few funds, long histories ([[universa-investments]]) | Many funds, short histories (survivors only) |
| **Typical archetype** | [[universa-investments]], [[longtail-alpha]] | tastytrade sellers, [[ljm-preservation-and-growth]] |

## Why Short Vol Is More Popular

Short vol dominates retail options activity and accounts for a large share of fund AUM despite its blow-up profile. Several structural and behavioral forces explain this:

1. **It looks great in calm regimes.** A naked short-vol book in 2013, 2017, or 2019 produced equity-like returns with bond-like volatility -- a 2.5+ Sharpe in-sample. Allocators see the track record before they see the tail.
2. **Sharpe is misleading for [[negative-skew|negatively skewed]] strategies.** Sharpe assumes [[gaussian-assumption|Gaussian returns]]; short vol violates this assumption catastrophically. A 2.0 Sharpe over five calm years tells you almost nothing about the sixth year's [[volmageddon|vol shock]]. See [[sharpe-ratio-pitfalls]] and [[deflated-sharpe-ratio]].
3. **Broker margin treats it favorably.** Under [[portfolio-margin]] and [[span-margin]], short-vol positions in calm markets carry low buying-power requirements -- often 10-15% of notional. This makes leverage easy and invisible until margin reprices in a shock.
4. **Theta is psychologically rewarding.** A trader sees daily P&L tick green almost every day. The [[dopamine-loop]] of frequent small wins is more reinforcing than the long, lonely bleed of long vol. See [[behavioral-finance]] and [[loss-aversion]].
5. **Education-industrial complex.** tastytrade, options-selling YouTube channels, and many retail brokers actively promote the short-vol playbook. Long-vol education is essentially limited to Spitznagel's books and a handful of academic papers.
6. **Survivorship bias in published track records.** The short-vol funds that blew up disappear from the data ([[ljm-preservation-and-growth]], [[malachite-capital]], [[catalyst-hedged-futures]]). The survivors look great, biasing perception of the strategy.

## Why Long Vol Is Institutionally Important

Long vol is unpopular and yet structurally essential for sophisticated allocators because it provides **convex offset to the equity book**:

1. **Equities are short vol in disguise.** A levered long equity portfolio is structurally similar to a short-put position on the global economy. Adding explicit short vol on top stacks the same risk twice.
2. **Convex hedges shrink the cost of high equity allocation.** [[mark-spitznagel]] argues in [[safe-haven-spitznagel|*Safe Haven*]] (2021) that an allocation of 3-5% of NAV to a Universa-style tail fund can offset 25-40% drawdowns in a 95-97% equity book -- producing a higher [[geometric-mean]] return than a 60/40 portfolio over multi-decade horizons. The math is **multiplicative survival**, not additive return.
3. **Crisis alpha funds rebalancing.** Long vol throws off cash exactly when equities are cheapest. The hedge funds the buy-the-dip leg, which is the [[barbell-portfolio|barbell]] alpha.
4. **It is uncrowded.** Because long vol is psychologically and career-risk hostile to most managers, the trade does not arbitrage away. The [[variance-risk-premium]] persists partly because nobody wants to be the buyer.

## The Blow-Up Asymmetry

The defining mathematical fact of vol books:

- **Short vol's worst day is a multi-year P&L.** [[xiv-velocity-shares|XIV]] lost 96% on Feb 5, 2018. [[ljm-preservation-and-growth]] lost ~80% in two days. Many short-strangle accounts lost 50-100% in [[vix-august-2024-spike|August 2024]] when VIX spiked from 16 to 65 intraday. The previous five years of theta were erased -- and exceeded -- in a single session.
- **Long vol's worst day is a 1-2% bleed.** A long-put or long-vix-call book grinds lower in calm regimes but cannot lose more than the premium paid. The worst case is a year of slow bleed, which is bounded.

Most short-vol funds have **1-2 catastrophic events per decade** that erase 5+ years of gains. Across the population:

- 1987 [[black-monday]] -- short-vol portfolios margin-called.
- 1998 [[long-term-capital-management|LTCM]] / Russia -- short-vol blew up across the credit complex.
- 2008 [[gfc|GFC]] -- structured product short-vol books erased decades of yield.
- 2018 [[volmageddon]] -- XIV terminated, LJM closed.
- 2020 [[covid-crash]] -- many short-strangle books gapped through wings.
- 2024 [[vix-august-2024-spike]] -- yen-carry unwind sparked the largest-ever VIX percentage spike.

The [[ergodicity]] argument: a strategy with a 5% annual risk of -80% has a **time-average** return that is far lower than its **ensemble-average** return. Backtests and Sharpe ratios reflect ensemble averages. The trader living through the strategy experiences the time average. See [[ole-peters]] and [[ergodicity-economics]].

## Capital Efficiency

A subtle and dangerous asymmetry sits in margin treatment.

**Short vol is capital-efficient in calm regimes.** Selling an SPX 16-delta strangle 45 DTE under [[portfolio-margin]] might require 10-15% of notional in buying power. A $250K account can run $1.5-2M of short strangles. Theta income looks enormous relative to the cash committed.

**Margin reprices instantly during a shock.** When VIX spikes from 15 to 50:

- Short-strangle margin requirements can rise **5-10x** in hours.
- The broker may force liquidation at the worst possible prices.
- Bid-ask spreads widen 5-20x; getting out costs another 5-20%.
- Net result: even if the trader had cash to meet calls, they cannot transact at sane prices. This is **liquidity-driven ruin**, not directional ruin.

**Long vol is capital-light always.** Premium paid is the maximum loss. There is no margin call, no forced liquidation, no [[gap-risk]]. The position **becomes more liquid** in stress -- everyone wants the puts you own. You can meet the family payroll, deploy capital into cheap equities, and act as a [[liquidity-provider]] exactly when others are being forced to sell. This optionality on the rest of the portfolio is itself worth multiples of the premium paid.

This asymmetry is invisible in calm-regime backtests and is the single most important reason real-money allocators run [[long-vol-overlay|long-vol overlays]] even when expected return is negative.

## The Synthesis: Short-Vol Core + Long-Vol Overlay

The institutional answer to "long vol or short vol?" is **both, in deliberate proportion**. The canonical construction looks like this:

- **Short-vol core (90-95% of vega budget).** Sell systematically priced premium where the [[variance-risk-premium]] is fattest -- index strangles, [[short-strangle]] sleeves, [[iron-condor]] sleeves, [[short-put-spread|put credit spreads]] in equities. The job of this book is to harvest the empirical 3-5% per year that implied vol prices over realized vol. See [[options-premium-selling]] and [[premium-selling-systematic]].
- **Long-vol overlay (5-10% of capital, or ~10% of the vega budget).** A continuous ladder of long puts and/or VIX calls structured to cap the worst-case scenario. Sized so that during a 30%+ equity drawdown the overlay generates enough P&L to keep the combined book inside acceptable drawdown limits. See [[long-vol-overlay]] and [[vega-budgeting]].
- **Net effect:**
  - In calm regimes: short-vol income is ~80-90% of standalone naked income (the overlay costs ~10-20% of premium).
  - In stress regimes: short-vol losses are largely offset by overlay gains. Net drawdowns are 10-15% rather than 50-100%.
  - **Sharpe over a full cycle** is typically **higher** than naked short vol once shocks are included, because the overlay fixes the negative-skew tail.
  - **Geometric returns** are dramatically higher because the strategy survives shocks and continues compounding.

This is the trade [[mark-spitznagel]] effectively offers institutional clients: keep your equity book, add a small allocation to a long-vol fund, and the combination dominates the unhedged equity book on any horizon longer than a single bull run.

## Worked Example

A trader has a $250,000 account. Three configurations:

### A) Pure short vol

- Sell **8 SPX 16-delta strangles**, 45 DTE.
- Per strangle: ~$5 credit on a $5K margin requirement = $4,000 credit, $40K margin.
- Daily theta: ~$80/day.
- Annualized expected return (calm regime): **+8% to +12%**.
- Worst-day risk: in [[vix-august-2024-spike|August 5, 2024]] this position would have lost ~40-60% of account in a single session.
- Max drawdown in shock: **40-100%** depending on whether wings are bought.
- Sharpe in calm year: **~2.5**.
- Sharpe over 7-year cycle including one shock: **~0.3 to 0.6**.

### B) Pure long vol

- Build a **6-month put ladder** on SPY: buy 1 SPY 480 put (~10% OTM) per month, $6 each x 100 shares = $600/month.
- Annual premium spend: $7,200 = 2.9% of NAV.
- Daily theta: ~-$20/day.
- Annualized expected return (calm regime): **-2% to -3%** (pure premium bleed).
- Best-day P&L: in a 2020-style 30% crash over 4 weeks, the ladder could be worth **+$30K-$60K** = **+12% to +24% of NAV** in a month.
- Max drawdown: capped at premium spent (~3% per year).
- Sharpe in calm year: **negative** (~-1.0).
- Sharpe over cycle: **slightly positive when crashes are monetized**.

### C) Blended (recommended professional configuration)

- **Short core:** 5 SPX 16-delta strangles -> ~$50/day theta, ~$25K margin.
- **Long overlay:** 1 SPY 6-month put ladder, $300/month spent.
- **Net daily theta:** ~$40-50/day.
- **Annualized expected return (calm regime):** **+5% to +7%**.
- **Worst-day risk:** in a 2024-style spike, the overlay catches ~30-50% of the strangle loss. Net account drawdown: **~10-15%** instead of 50%.
- **Max drawdown over cycle:** ~15%.
- **Sharpe in calm year:** ~1.6 (lower than naked short vol).
- **Sharpe over cycle:** **~1.0-1.4** -- the highest of the three because it survives shocks and continues compounding.

The blended book trades **gross income** for **path quality** and **survival**. Over a multi-cycle horizon (the only horizon that matters for compounding), it is empirically the dominant configuration.

## Regime Mapping

Reference [[volatility-regime-classification]] for the four-regime framework. How each book performs:

| Regime | Conditions | Long Vol | Short Vol | Blended |
|---|---|---|---|---|
| **Calm** (VIX <13, low realized) | Low vol, trending, suppressed RV | Worst (max bleed) | Best (max theta capture, low gamma loss) | Slightly underperforms short vol |
| **Normal** (VIX 13-20) | Median conditions | Mild bleed | Strong income | Solid income, slight overlay drag |
| **Stressed** (VIX 20-35) | Elevated but not panicked | Mild profit (vega and gamma kick in) | Marginal; gamma starts to bite | Stable; overlay starts paying |
| **Crisis** (VIX 35+) | Crashes, gap moves, [[volmageddon]] | Best (huge convex payoff) | Worst (catastrophic loss, possible ruin) | Acceptable; overlay offsets core |

Pure books are **regime-specialists**. Blended books are **regime-generalists**: they underperform their specialist counterpart inside the specialist's regime but dominate over a full cycle because they survive every regime.

The key empirical fact: the calendar weight of the four regimes over the last 30 years has been roughly 55% calm, 30% normal, 10% stressed, 5% crisis. A naked short-vol book underperforms a blended book despite the calendar tilt because the 5% crisis weight contributes ~80% of the lifetime drawdown.

## When to Pick a Side

**Pure long vol makes sense when:**

- You are a **dedicated tail fund** (Universa, LongTail) raising capital from allocators who want crisis alpha as a portfolio building block.
- You have a strongly bearish macro view and want a **bounded-cost expression** of it (better than short futures because limited loss).
- You hold **concentrated long-equity** elsewhere and need explicit insurance.
- You are studying or pilot-testing tail strategies and want to learn the bleed-and-monetize cycle. See [[tail-risk-hedging]].

**Pure short vol makes sense when:**

- You are running a small account in **a single calm regime** and accept the eventual blow-up as tuition.
- You are systematically **harvesting [[variance-risk-premium]]** in size with [[portfolio-margin]] and a clear understanding of the [[ergodicity]] problem (most fail this test).
- Note: nearly every fund that has run pure short vol at scale has eventually had a fund-ending event.

**Blended is the answer for almost everyone else** -- particularly anyone running real capital across multiple cycles. See [[options-portfolio-construction]].

## Quick-Reference Decision Table

| Your situation | Recommended posture | Why |
|---|---|---|
| Run a large long-equity book | **Short-vol core + long-vol overlay** | Equities are already short-vol; the overlay caps the stacked tail |
| Dedicated tail / crisis-alpha fund | **Pure long vol** | You are selling convexity-as-a-product to allocators |
| Strong bearish macro view, want bounded loss | **Pure long vol** (puts/VIX calls) | Limited-loss expression beats short futures |
| Small account, calm regime, accept eventual blow-up | **Pure short vol** (eyes open) | Tuition trade; size for ruin, not for income |
| Systematic VRP harvester at scale | **Short-vol core + overlay** (never naked) | The 5% crisis weight contributes ~80% of lifetime drawdown |
| Cannot articulate your long-vol leg | **Stop and reassess** | You are running naked short vol whether you know it or not |

## Mapping to the Strategy Regime Matrix

The long-vol / short-vol split is the single most important axis in the wiki's [[regime-matrix]], which classifies nearly every strategy as implicitly one or the other:

| Cluster | Vol posture | Regime where it thrives | Regime where it dies | Examples |
|---|---|---|---|---|
| [[short-volatility-strategies\|Short-vol-like]] | Sells convexity | Calm, range-bound, low-vol | Vol spikes, regime transitions | [[short-strangle]], [[iron-condor]], [[covered-calls]], carry, [[grid-trading]], most DeFi yield |
| [[long-volatility-strategies\|Long-vol-like]] | Buys convexity | High vol, crashes, regime shifts | Calm chop (theta/whipsaw bleed) | [[tail-risk-hedging]], long straddles, [[trend-following-cta]], breakout |

Two practical corollaries:

1. **Trend following is "long vol in disguise."** It pays theta-like costs in chop (whipsaws) and earns convex payoffs during volatile regime shifts — the same skew shape as an explicit long-vol book. This is why a [[trend-following-cta|CTA]] sleeve is a partial substitute for a tail hedge in a multi-strategy book (see [[regime-matrix#The Long-Vol / Short-Vol Master Axis]]).
2. **Carry and premium-selling share one fate.** [[carry-trade|FX carry]], crypto [[funding-rate-arbitrage|funding carry]], and equity-index premium selling all collect a small premium for absorbing tail risk and all blow up in the same risk-off transition. Holding several of them is *not* diversification — it is the same short-vol bet replicated. See [[market-regime]] and [[failure-modes]].

## Verdict

Long vol and short vol are not "two strategies"; they are the two sides of one risk premium ([[variance-risk-premium|VRP]]). The seller earns a steady premium for absorbing tail risk; the buyer pays that premium for convex protection. Picking a side dogmatically is a category error -- the right question is **how much of each, and at what relative sizing**.

Empirically, the highest-quality long-run options books (Universa, the survivor cohort of premium sellers, sophisticated risk-parity overlays) all run **short-vol cores with deliberate long-vol overlays**. The overlay reduces gross income but pays for itself many times over by ensuring the book is still trading after the next [[volmageddon|2018]]/[[covid-crash|2020]]/[[vix-august-2024-spike|2024]]. Short vol without an overlay is not a strategy; it is a leveraged bet that the next crash will not happen on your watch. Long vol without a short-vol core is a tail-hedge product, not a stand-alone strategy.

The practical rule: **if you cannot describe the long-vol leg of your book, you are running naked short vol -- whether you know it or not.**

## Related

- [[variance-risk-premium]] -- the underlying premium being arbitraged in both directions
- [[volatility-regime-classification]] -- the four-regime framework that determines book performance
- [[tail-risk-hedging]] -- detailed strategy page on the long-vol overlay
- [[options-premium-selling]] -- detailed strategy page on the short-vol core
- [[options-portfolio-construction]] -- how to size and combine the two
- [[vega-budgeting]] -- formal framework for allocating risk between core and overlay
- [[long-vol-overlay]] -- mechanics of attaching a long-vol sleeve to a short-vol book
- [[volmageddon]] -- the 2018 vol shock that ended XIV and LJM
- [[vix-august-2024-spike]] -- the 2024 yen-carry-unwind vol shock
- [[universa-investments]] -- the canonical long-vol fund
- [[ljm-preservation-and-growth]] -- the canonical short-vol blow-up
- [[mark-spitznagel]] -- author of *Safe Haven*
- [[nassim-taleb]] -- co-architect of the convex-hedge approach
- [[tom-sosnoff]] -- founder of tastytrade, popularizer of retail short-vol
- [[ergodicity]] -- why time-average and ensemble-average diverge for negative-skew strategies
- [[deflated-sharpe-ratio]] -- statistical correction for in-sample short-vol Sharpe
- [[short-strangle]] -- canonical short-vol structure
- [[iron-condor]] -- defined-risk short-vol structure
- [[long-volatility-strategies]] -- the full catalog of long-vol structures
- [[short-volatility-strategies]] -- the full catalog of short-vol structures
- [[regime-matrix]] -- the master strategy-regime map organized around this axis
- [[market-regime]] -- the conceptual frame for regime classification
- [[failure-modes]] -- how short-vol books fail in regime transitions

## Sources

- Spitznagel, Mark. *Safe Haven: Investing for Financial Storms* (2021) -- the canonical defense of long-vol overlays. Argues that a small allocation to convex hedges raises the geometric return of the combined portfolio.
- Spitznagel, Mark. *The Dao of Capital* (2013) -- earlier theoretical framing of "roundabout" investing and convex tail protection.
- Taleb, Nassim Nicholas. *Dynamic Hedging* (1997) and *The Black Swan* (2007) -- the intellectual origin of the long-vol case and the critique of Gaussian risk models.
- Bhansali, Vineer. *Tail Risk Hedging* (2014) -- practitioner treatment of tail-hedge construction.
- Carr, Peter and Wu, Liuren. "Variance Risk Premiums" (2009) -- canonical academic measurement of the VRP and its persistence.
- [[volmageddon|Feb 2018 vol shock]] -- direct historical evidence on short-vol blow-up dynamics.
- [[vix-august-2024-spike|Aug 5, 2024]] -- most recent example of yen-carry-unwind-driven vol shock and short-vol losses.
- Peters, Ole. "The ergodicity problem in economics" (2019, *Nature Physics*) -- the formal argument for why time-average matters more than expected return for compounding strategies.
