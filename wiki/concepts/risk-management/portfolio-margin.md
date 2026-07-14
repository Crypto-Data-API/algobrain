---
title: "Portfolio Margin"
type: concept
created: 2026-05-05
updated: 2026-06-20
status: excellent
tags: [options, risk-management, regulation]
aliases: ["PM Account", "Portfolio Margin Account", "Risk-Based Margin"]
related: ["[[options-portfolio-construction]]", "[[options-risk-budgeting]]", "[[options-position-sizing]]", "[[options-stress-testing]]"]
domain: [risk-management, regulation]
prerequisites: ["[[options-greeks]]", "[[options-position-sizing]]"]
difficulty: advanced
---

Portfolio margin (PM) is a risk-based [[margin|margining]] methodology that calculates account-wide margin requirements by stress-testing the entire book under a set of hypothetical underlying and [[volatility]] shocks, then charging the worst-case loss as the margin requirement. For traders running hedged options books — iron condors, ratio spreads, calendars, dispersion trades — PM typically requires 3-7x less capital than the strategy-based Reg T system, which sums per-trade margin requirements without recognizing offsetting positions. PM is not "free leverage" — it is a more accurate risk model (conceptually a single-day, broker-defined [[value-at-risk|VaR]] computed from a [[options-stress-testing|scenario grid]]) that exposes traders to non-linear margin expansion during volatility shocks, and the same hedged book that "fits" comfortably at normal vol can blow through the margin requirement when the [[vix]] doubles overnight.

## Margin Regimes at a Glance

Three margining regimes dominate U.S. retail and professional accounts. The distinction is *what each one recognizes* — the more of the book's internal hedging a methodology sees, the lower the requirement on a genuinely hedged book.

| Dimension | Reg T (strategy-based) | Portfolio Margin / TIMS (risk-based) | SPAN (risk-based, futures) |
|-----------|------------------------|--------------------------------------|----------------------------|
| **Methodology** | Fixed per-strategy lookup formulas | Full-book revaluation across a price × IV scenario grid | Scanning-risk array of ~16 price/vol scenarios per product group |
| **Operated / defined by** | Federal Reserve (Reg T) + FINRA Rule 4210 | OCC's **TIMS** engine, passed through by brokers | CME Group's **SPAN** (Standard Portfolio Analysis of Risk) |
| **Asset scope** | Equities + equity options | Equities, ETFs, equity/index options | Futures + futures options (cross-margined product groups) |
| **Recognizes hedges?** | Within a single strategy only (e.g. one vertical) | Yes — across the entire account at the clearing level | Yes — within a product group + inter-commodity spread credits |
| **Recognizes [[options-concentration-risk\|concentration]]?** | No (blind to it) | Yes — penalizes single-name concentration via add-ons | Yes — via concentration / liquidity charges |
| **Capital efficiency on a hedged book** | Low (3-7x more capital) | High | High |
| **Min. account equity** | None beyond Reg T basics | $125k FINRA minimum (broker overlays apply) | Set per product / broker |
| **Who uses it** | Default retail accounts | Active options books long/short books | Futures traders, vol-on-futures (ES, /VX) books |

PM (via TIMS) and SPAN are siblings — both replace fixed formulas with worst-case scenario revaluation. The practical difference is jurisdiction: TIMS governs the equity/options world (OCC), SPAN governs the futures world (CME). Brokers like [[thinkorswim|Schwab/thinkorswim]] run both and stitch them together so a portfolio spanning ES futures and SPX options is margined coherently. See [[span-margin]] for the futures-side detail.

## Reg T vs Portfolio Margin

The U.S. options margin system has two parallel regimes:

### Reg T (Strategy-Based Margin)

Regulation T is the default margin framework for retail brokerage accounts, originally designed in 1934 for cash equity margin and later extended to options through a strategy-by-strategy lookup table. Each position type has a fixed margin formula:

| Position | Reg T Margin Requirement |
|----------|--------------------------|
| Long stock | 50% of position value (initial), 25% (maintenance) |
| Short call (uncovered) | 20% of underlying value + premium − OTM amount |
| Short put (uncovered) | 20% of underlying value + premium − OTM amount |
| Vertical spread (long + short) | Width of spread − net credit |
| Iron condor | Width of one wing (the larger one) |
| Long option | 100% of premium |

The core feature of Reg T is that **margin is computed per-strategy, not per-portfolio**. Two short puts on uncorrelated stocks cost twice the margin of one. A short put hedged by a long put 50 strikes lower (a wide credit spread) costs the spread width minus credit, regardless of how the rest of the portfolio is positioned.

Reg T is conservative for naked positions, punitive for complex spreads, and almost completely blind to portfolio-level offsets. A market-neutral book of long calls on one ticker and long puts on another receives no offset benefit even though the trades hedge each other.

### Portfolio Margin (Risk-Based)

Portfolio margin replaces the strategy-based lookup with a scenario-based simulation:

1. Take the entire account — every stock, every option, every futures position
2. Apply a set of shocks: typically ±15% to single-name underlyings, ±6-8% to broad indices, with intermediate steps
3. At each shock level, also shock implied volatility up and down
4. Recompute the theoretical P&L of the entire book at each shock combination
5. The **worst-case P&L across all scenarios** is the portfolio margin requirement

Critically, this captures portfolio-level offsets: a short call hedged by a long call at a higher strike loses bounded money even in the up-shock scenario, so the PM requirement reflects that bounded loss, not the gross short-call exposure. This is why PM is so capital-efficient for hedged structures — see [[options-portfolio-construction]] for how this changes structure design.

The PM methodology was approved by FINRA in 2007 (after years of being available only to broker-dealers and hedge funds) and is now offered by most major U.S. brokers to qualifying retail accounts.

## How PM Requirements Are Calculated

The standard methodology used by U.S. brokers is the **TIMS** (Theoretical Intermarket Margin System) framework operated by the Options Clearing Corporation (OCC), which calculates a margin requirement at the clearing level and brokers pass through (with their own buffers) to customer accounts.

### TIMS vs SPAN — the two scenario engines

PM rests on one of two scanning-risk engines, depending on the asset class:

- **TIMS (OCC)** — governs equities, ETFs, and equity/index options. TIMS groups every position by underlying into a "class group" (all options + stock on one name) and then into "product groups" (correlated underlyings, e.g. an index and its components, which earn partial offset credits). For each class group it revalues the positions across a grid of equally-spaced price points spanning the down-shock floor to the up-shock ceiling, with an implied-[[volatility]] shock applied at each point. The **largest loss across the grid** is that class group's requirement; product-group offsets then reduce the sum.
- **SPAN (CME)** — the futures-world equivalent. SPAN scans a fixed **risk array of ~16 scenarios** per product: combinations of the price moving up/down by fractions of a "price scan range," IV moving up/down by a "volatility scan range," plus two extreme-move scenarios covering only a fraction (typically ~35%) of an outsized gap. SPAN then adds an **inter-month (calendar) spread charge**, grants **inter-commodity spread credits** for correlated products, and applies a **short-option minimum** floor so deep-OTM shorts are never charged zero. The requirement is the worst array loss, netted across the portfolio.

Both engines share the same philosophy — *don't sum formulas, revalue the book under shocks and charge the worst case* — which is why a book that is genuinely hedged is cheap under either, and a concentrated directional book is expensive under both.

### How a PM Requirement Is Computed — Step by Step

For an equity/options account under TIMS, the requirement is built like this:

1. **Group positions by underlying** into class groups (all stock + options on a single name) and correlated underlyings into product groups.
2. **Define the shock range** for each underlying from its TIMS class (see grid below) — ±6-8% for broad indices, ±15% for liquid single names, wider for illiquids and vol products.
3. **Build the scenario grid**: ~10 equally-spaced price points across that range, each crossed with an IV-up / IV-unchanged / IV-down shock.
4. **Revalue every position** at each grid node using a theoretical pricing model ([[options-pricing-models|Black-Scholes]] or binomial), producing a full profit/loss surface per class group.
5. **Take the worst-case loss** for each class group — the single grid node with the largest aggregate loss.
6. **Apply product-group offset credits** where correlated underlyings hedge each other (e.g. index vs components).
7. **Add concentration and minimum charges**: single-name concentration add-ons, short-option minimums, and illiquidity haircuts.
8. **Layer the broker's house buffer** on top of the OCC/clearing number — this is why the same position can show different margin at IBKR vs tastytrade.

The output is the account's PM requirement; subtracting it from equity gives buying power. Because step 4 is a full revaluation, the requirement *moves continuously* as spot, IV, and time change — unlike a Reg T number that only changes when you trade.

### Standard Shock Grid

The TIMS shock grid defines 10 equally-spaced underlying price scenarios from the down-shock floor to the up-shock ceiling:

| Underlying Type | Price Shock Range | Volatility Shock |
|-----------------|-------------------|------------------|
| Broad-based index (SPX, NDX, RUT) | ±6% (sometimes ±8%) | ±10% IV |
| ETFs on broad indices (SPY, QQQ, IWM) | ±10% | ±10% IV |
| Single-name equities (high cap) | ±15% | ±10% IV |
| Single-name equities (low cap, illiquid) | ±20-30% | ±10% IV |
| Volatility products (VIX, VXX, UVXY) | ±20% (asymmetric, more upside) | ±15% IV |
| Concentrated single-stock positions | up to ±30-40% | ±15% IV |

The volatility shock is applied at each price point, so the actual scenario grid is roughly 10 (price) × 3 (vol up, unchanged, down) = 30 scenarios per underlying. The worst loss across all scenarios sets the requirement.

### Worked Example

Consider a market-neutral SPX iron condor at $5,000 with $100-wide wings:
- Short 4900 put / Long 4800 put (put wing)
- Short 5100 call / Long 5200 call (call wing)
- Net credit: $4.00 per contract

**Under Reg T**: Margin = $100 wing width − $4 credit = $96 per contract = $9,600 per contract notional
**Under PM**: SPX broad-index shock is ±6%. At $5,000, that's ±$300 = scenario range $4,700 to $5,300. The condor's max loss within this shocked range is approximately the wing width ($96), but the *worst* shocked scenario depends on how quickly the wing breaches and the vol shock applied. Often, PM yields $40-60 per contract — a 30-50% reduction.

For a *delta-hedged* short straddle, the PM benefit is much more dramatic — Reg T treats the short straddle as two naked shorts requiring full naked margin, while PM recognizes the delta hedge and the limited move size, often charging only 10-20% of the Reg T number.

### Why PM Is Conservative for Concentrated Positions

PM rewards diversification and hedging, but punishes concentration:
- A book with 80% of its risk in one ticker still pays full single-name shock margin on that ticker
- Broker-imposed concentration add-ons can push single-name margin above the TIMS floor
- Illiquid stocks may be assigned wider price shocks (up to ±30%) at broker discretion

## Eligibility

Portfolio margin is regulated by [[finra]] under FINRA Rule 4210, which sets minimum standards. Brokers can (and do) impose additional requirements.

### FINRA Minimums

- **Minimum equity**: $125,000 (must be maintained; falling below triggers conversion back to Reg T)
- **Options approval**: Highest level (typically Level 4 — naked options trading approval)
- **Knowledge requirement**: The customer must demonstrate familiarity with risk-based margining (broker-administered questionnaire or signed acknowledgment)
- **Account type**: Cannot be an IRA in most cases; some brokers offer "limited PM" for IRAs with restrictions
- **Pattern day trader**: PM accounts are exempt from the $25k PDT rule and the 4-day-trades-in-5-business-days restriction

### Broker-Specific Requirements

Most brokers exceed FINRA minimums:

| Broker | Minimum Equity | Notes |
|--------|----------------|-------|
| interactive-brokers | $110,000 (lower than FINRA min for some accounts) | TIMS-based; tightest spreads on requirements |
| tastytrade | $250,000 (some accounts $125k) | "SPAN-style" methodology branded as Portfolio Margin |
| Charles Schwab / [[thinkorswim]] | $125,000 | Inherits TD Ameritrade's PM platform post-merger |
| Tradier | $125,000 | Available for active options accounts |
| E*TRADE | $250,000 | Higher minimum than most |
| Fidelity | Not offered to retail | Available institutionally only |

The actual requirement to *qualify* often differs from the requirement to *maintain* — falling below maintenance triggers a margin call and potential conversion back to Reg T.

## Broker Implementations

### Interactive Brokers

IBKR uses the OCC's TIMS methodology directly with minimal broker overlay. Their PM implementation is widely considered the most aggressive (i.e., lowest margin requirements) among retail brokers, particularly for delta-hedged and dispersion books. Key features:

- Real-time PM calculation in [[trader-workstation|TWS]] — every order shows margin impact before submission
- Stress test view: simulate ±10%, ±20%, ±30% shocks on any underlying and see resulting margin
- Risk Navigator tool: detailed scenario analysis across the entire book
- "What-if" portfolio: clone the live account and test trades hypothetically
- House margin requirements: IBKR overlays additional requirements for very concentrated positions, illiquid names, and during market stress

IBKR is the most popular choice for hedged long/short equity books because the PM methodology accurately reflects the risk of long/short pair trades with options overlays.

### Charles Schwab / thinkorswim

After acquiring TD Ameritrade in 2020, Schwab inherited the [[thinkorswim]] platform and TDA's PM implementation. Schwab uses TIMS for equity options and [[span-margin|SPAN]] for futures and futures options, providing a unified PM view across both. Notable features:

- Beta-weighted analysis showing total portfolio risk in SPY-equivalent terms
- "Worst-case scenario" view showing margin requirement at each shock level
- Integrated futures + options margin (SPAN cross-margining for portfolios spanning both)
- Schwab maintains a higher house buffer than IBKR, particularly during volatility spikes

### TastyTrade

TastyTrade markets its PM offering aggressively to its premium-selling retail base. The methodology is TIMS-based but with TastyTrade-specific overlays:

- Optimized for [[short-strangle|short strangles]], [[iron-condor|iron condors]], and other premium-selling strategies that retail tastytrade customers favor
- "BPR" (Buying Power Reduction) display showing real-time margin consumption
- Built-in strategy templates that compute PM impact before execution
- Margin requirements tend to be slightly higher than IBKR for equivalent positions, reflecting tastytrade's more conservative house buffers

### Tradier

Tradier offers PM through its brokerage layer at the FINRA minimum $125k threshold. Used primarily by API-driven retail traders and small fund operators who need PM-grade capital efficiency without IBKR's complexity.

## Why Professional-Scale Traders Use PM

Professional discretionary traders running long/short equity books typically run 20-40 simultaneous positions, with options overlays for risk management. Reg T margin makes this almost impossible at retail scale:

- Each pair trade (long stock + short stock, or long call + short call across two tickers) requires full naked margin on the short side under Reg T
- A 30-position book of small Greek exposures can require 5-8x more capital under Reg T than the actual portfolio risk warrants
- Hedge structures (calendar spreads, ratio spreads, butterflies) get no offset recognition under Reg T

PM converts the margin requirement from "sum of individual position requirements" to "actual risk of the combined book," which is exactly the framing professional traders already think in. A trader using [[options-position-sizing]] and [[options-risk-budgeting]] frameworks is implicitly computing portfolio Greek exposures — PM just charges margin against those exposures directly.

### Capital Efficiency Examples

| Structure | Reg T Margin | PM Margin | Reduction |
|-----------|--------------|-----------|-----------|
| Iron condor on SPX, $50 wings | $4,600 | $1,200-2,000 | 55-75% |
| Calendar spread, ATM SPX | $0 (debit) | $0-500 | Similar |
| Ratio spread (1×2) on SPY | Full naked margin on extra short | Net of hedge | 60-80% |
| Long stock + protective put | 50% of stock value | ~10-20% of stock value | 60-80% |
| Short strangle, delta-hedged | Full naked × 2 | Single shocked move | 70-85% |
| Long/short pair (stocks + options) | Full margin both sides | Net beta exposure | 50-70% |

These reductions enable strategies that are simply uneconomic under Reg T — particularly dispersion trades, [[volatility-arbitrage|vol arbitrage]], and [[delta-neutral]] options books.

## The Hidden Risks

PM is often described as a benefit, but the *actual* feature is a more accurate risk model — and accurate risk models can punish you when conditions change. The key risks:

### Apparent Free Leverage

A trader who uses PM to deploy 5x more contracts than they would under Reg T has not gained risk-free capital — they've gained leverage proportional to the margin reduction. The book is *more* exposed to a tail event that breaches the shock grid, not less. Many PM accounts blew up in March 2020 and August 2024 because traders sized positions to PM buying power without stress-testing beyond the standard shock grid.

### Non-Linear Margin Expansion

PM requirements expand non-linearly during vol spikes:

- Higher IV → wider shock-grid prices (some brokers widen shocks dynamically)
- Higher IV → larger absolute P&L swings within the standard grid
- Concentration adjustments kick in as positions move further in/out of the money
- Broker-imposed house buffers tighten during stress

The August 2024 [[vix]] spike (VIX from 15 to 65 in two trading days) is the canonical recent example. Traders running short-vol books that were comfortably margined at VIX 15 saw margin requirements double or triple in 48 hours, forcing liquidations into a vol-bid market. Many positions that would have been profitable held to expiration were closed at the worst possible price because the trader couldn't post additional margin in time.

### Forced Liquidation Below $100k

If account equity drops below $100,000, brokers are required to convert the account back to Reg T — and immediately reapply Reg T margin requirements to all existing positions. This often produces a cascade:

1. Account equity drops to $99k due to losses
2. Account auto-converts to Reg T
3. All positions revalued at Reg T (much higher) requirements
4. Account is now in massive Reg T deficit
5. Broker liquidates positions at market

This conversion mechanism is more dangerous than a typical margin call because it changes the *rules* mid-stress. Traders should maintain a buffer significantly above $100k — most professionals run with 30-50% buffer minimum.

### Single-Name Concentration Limits

Most brokers cap PM benefits when a single ticker exceeds a threshold (often 25-30% of total portfolio risk). Above the cap, the position is margined as if it were standalone, eroding the PM benefit. Traders building [[concentrated-positions]] often discover this only when their margin requirement jumps unexpectedly after a position appreciates.

### Broker Discretion

Brokers retain the right to impose additional house margin at any time, particularly:
- Before known volatility events ([[fomc]] meetings, earnings, elections)
- During market stress
- For positions in illiquid or volatile underlyings
- For positions held into expiration with [[pin-risk|pin risk]]

These adjustments can happen mid-day with little notice.

## Margin Call Mechanics

When a PM account falls below requirements, the cure mechanics are:

### Same-Day Cure

For mild deficits (typically <5% of equity), brokers issue a same-day margin call requiring resolution by market close. The trader can:
- Deposit cash
- Close losing positions
- Add hedges to reduce stress-test losses

### Next-Day Cure

For larger deficits, brokers may extend to T+1 — but interest accrues immediately, and the broker retains the right to liquidate without notice if the deficit grows.

### Forced Liquidation (Sellout)

If the deficit isn't cured, the broker liquidates positions at its discretion. Critically, the broker chooses *which* positions to close — often the most liquid ones, even if they're profitable, to raise cash quickly. A trader's carefully constructed hedged book can be unwound asymmetrically, leaving residual unhedged exposure that gets liquidated next.

### Equity Below $100k Trigger

As noted above, falling below $100k equity converts the account to Reg T immediately. Brokers vary in how aggressively they enforce this — some apply a buffer (e.g., $90k floor), others convert at exactly $100k. Read the broker's PM agreement carefully.

## PM and Tail Events

The fundamental fragility of PM is that the shock grid is a *finite* representation of risk. A book that survives all standard shocks can still fail outside the grid:

### Examples of Grid-Breaching Events

| Event | Shock Beyond Grid |
|-------|-------------------|
| August 2024 VIX spike | IV moved 4-5x in 48 hours; PM grid assumes ±10% IV |
| Volmageddon (Feb 2018) | XIV/SVXY moved 90% in one day; grid assumed ±20% |
| March 2020 COVID crash | SPX moved -34% in 23 trading days; grid assumes ±6% per day |
| GameStop Jan 2021 | GME moved +1900% in 2 weeks; single-name grid assumes ±15% |
| Silicon Valley Bank Mar 2023 | SIVB moved -60% in 1 day before halt; standard ±15% |

In each case, traders running short-vol or short-correlation books at high PM utilization were forced to either post massive additional margin or be liquidated at the worst possible prices.

### Stress Testing Beyond the Grid

Professional PM users routinely run [[options-stress-testing]] scenarios well beyond the standard grid:

- ±25% single-name shock (vs. standard ±15%)
- ±15% broad-index shock (vs. standard ±6%)
- ±20-point IV shock (vs. standard ±10%)
- Combined shock + IV shock (the worst case is rarely "max move with no IV change")
- Liquidity shock: bid-ask widening of 5-10x

A book that survives these "beyond grid" shocks can be sized to PM buying power. A book that *only* survives the standard grid is one tail event from forced liquidation.

## Practical Guidance

### Sizing Rules of Thumb

Active PM users converge on a few common sizing principles:

1. **Keep PM utilization below 50% of buying power**. The remaining 50% absorbs margin expansion during vol spikes without triggering forced liquidation.

2. **Maintain a cash reserve of 20-30% of equity**. Cash earns interest at most brokers and provides immediate cure capacity for margin calls.

3. **Stress test at 2x the standard grid**. If the book can't survive a ±30% single-name shock or ±12% index shock, it's overleveraged regardless of what PM says.

4. **Cap single-name concentration at 15-20% of portfolio risk**. Beyond this, broker concentration adjustments and gap risk dominate.

5. **Distinguish intraday vs. overnight requirements**. Some brokers (notably IBKR) reduce margin requirements intraday and tighten them overnight. Positions sized to intraday limits can fail overnight checks.

6. **Avoid earnings/event concentration**. A book of short premium across 10 names with earnings in the same week is one bad earnings season from disaster — PM doesn't fully capture event risk.

7. **Watch the Greeks, not the BP**. PM utilization is a coarse measure. Net portfolio gamma, vega, and beta-weighted delta tell you more about actual risk exposure (see [[options-position-sizing]]).

### When to Avoid PM

PM is wrong for some accounts even when they qualify:

- **Single-strategy traders**: A trader running only outright stock or only long options gets minimal PM benefit; the complexity isn't worth it
- **Inactive traders**: PM's benefit is in capital efficiency for active hedged books; passive accounts gain little
- **Traders without stress-testing capability**: If you can't model the book under non-standard shocks, you can't safely use PM
- **Accounts near the $100k floor**: One bad day can trigger forced conversion; better to stay in Reg T until you have a comfortable buffer

### Tools and Workflow

Mature PM traders typically use:

- Broker stress test tools (IBKR Risk Navigator, thinkorswim Analyze tab)
- External risk systems (custom Python with [[options-pricing-models|Black-Scholes]] or [[binomial-trees]] revaluation across scenarios)
- [[options-greeks]] aggregation across the full book, beta-weighted to a benchmark
- Daily margin utilization tracking with alerts at 60%, 70%, 80% thresholds
- Pre-trade margin impact checks (every order shows margin delta before submission)

## Connection to Position Sizing & Stress Testing

PM is not a sizing methodology — it is a *constraint* that sits underneath one. The disciplined workflow keeps three numbers separate and treats the most conservative as binding:

1. **The risk-based size** — how big the position can be from a [[position-sizing]] standpoint (e.g. risk ≤1-2% of equity on the worst plausible move). This is the trader's own limit.
2. **The stress-test size** — what the position loses under [[options-stress-testing|beyond-grid scenarios]] (±25% single-name, ±15% index, ±20-pt IV, plus a liquidity haircut). This is the honest tail number.
3. **The PM requirement** — what the broker charges. This caps *contracts* but is a *floor on risk awareness*, not a measure of it.

The failure mode is letting (3) drive (1): "I have buying power for 100 contracts, so I'll trade 100." PM buying power is a single-day, finite-grid VaR; it systematically understates tail loss because the grid stops at ±15% / ±10 IV (see [[options-stress-testing#Why Greeks Alone Are Insufficient]]). The correct ordering is to size with [[position-sizing]] and stress, then confirm the result *also* fits inside PM — never the reverse.

Concretely, PM ties into the rest of the risk stack:

- **[[portfolio-greeks-aggregation]]** — PM is implicitly charging margin against the book's aggregate [[delta]], [[gamma]], and [[vega]]. A trader who already aggregates dollar-Greeks and beta-weighted delta is computing the same exposures the TIMS grid prices; the Greeks dashboard is the early-warning system for where the margin number is heading.
- **[[options-stress-testing]]** — the broker's scenario engine *is* a stress test, just a deliberately mild one. Running your own wider grid (and stressing the *margin* alongside P&L) tells you whether a vol spike will trigger forced liquidation before it happens.
- **[[options-concentration-risk]]** — PM's concentration add-ons mechanically penalize single-name clustering, but only above broker thresholds; a book can be dangerously concentrated *and* well inside PM. Concentration limits must be enforced independently.
- **[[theta-targeting]] / [[vega-budgeting]]** — a premium-selling book sized to a daily [[theta]] target will consume PM proportional to its short [[vega]]; in a vol spike both the income and the margin rise together, which is exactly when over-sized books fail.
- **[[trade-repair-and-rolling]]** — when PM expands in a stress event, *adding a hedge* (e.g. long wings, an index put) reduces the worst-case scenario loss and therefore *reduces the margin requirement* — often a faster cure than depositing cash. Rolling untested sides, by contrast, may collect credit but does little for the stressed grid number.

The one-line synthesis: **size to your own risk and stress numbers; use PM only as a hard ceiling and an early indicator of margin expansion, never as a sizing signal.**

## Related

- [[margin]] — the parent concept; PM is one of its risk-based variants
- [[risk-management]] — the broader discipline PM sits inside
- [[options-portfolio-construction]] — designing books that exploit PM efficiency
- [[options-risk-budgeting]] — allocating risk budget across PM-margined positions
- [[options-position-sizing]] — Greeks-based sizing within PM constraints
- [[position-sizing]] — the sizing discipline PM should constrain, not drive
- [[options-stress-testing]] — beyond-grid scenario analysis; the broker engine is a mild version
- [[portfolio-greeks-aggregation]] — the aggregate Greeks PM implicitly charges against
- [[value-at-risk]] — PM is conceptually a single-day, broker-defined VaR
- [[options-concentration-risk]] — concentration PM penalizes, but only above thresholds
- [[theta-targeting]] — premium-selling income that consumes PM via short vega
- [[vega-budgeting]] — the vega limit that maps directly to PM consumption
- [[trade-repair-and-rolling]] — adding hedges reduces stressed margin faster than cash
- [[span-margin]] — the futures-equivalent scanning-risk engine
- [[delta]], [[gamma]], [[vega]] — the exposures the TIMS grid prices
- [[volatility]] — the IV dimension of the shock grid
- [[thinkorswim]] — Schwab's PM-enabled platform
- [[options-greeks]] — the risk measures PM is implicitly charging against
- [[finra]] — regulator that sets PM minimums
- [[options-clearing-corporation]] — clearinghouse that runs the TIMS calculation
- [[vix]] — volatility events that stress PM accounts
- [[concentrated-positions]] — risk concentration that PM penalizes

## Sources

- FINRA Rule 4210(g) — portfolio margin requirements
- OCC TIMS methodology documentation — the underlying calculation engine
- Interactive Brokers Margin Requirements documentation
- TastyTrade Portfolio Margin disclosure
