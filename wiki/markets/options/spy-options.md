---
title: "SPY Options"
type: market
created: 2026-05-06
updated: 2026-06-19
status: excellent
tags: [options, derivatives, etf, sp500, stocks]
aliases: ["SPY", "SPDR S&P 500 ETF Options"]
domain: [derivatives, options]
difficulty: intermediate
related: ["[[index-options]]", "[[options]]", "[[spx-options]]", "[[xsp-options]]", "[[ndx-options]]", "[[rut-options]]", "[[section-1256-contracts]]", "[[cash-vs-physical-settlement]]", "[[american-vs-european-options]]", "[[assignment-and-exercise]]", "[[ex-dividend-date]]", "[[weekly-options]]", "[[0dte-trading]]", "[[vix]]", "[[options-portfolio-construction]]"]
---

SPY options are American-style, physically-settled options on the **SPDR S&P 500 ETF Trust** (ticker SPY), the largest and most liquid US equity ETF. They are the ETF counterpart to the cash-settled [[index-options]] on the same benchmark — most directly to [[spx-options|SPX]] — and the contrast between the two products is the central theme of this page. The contract multiplier is $100 (delivering 100 shares of SPY on assignment), so the notional per contract is approximately one-tenth that of a comparable [[spx-options|SPX]] option. SPY options are taxed as standard equity options (not [[section-1256-contracts|Section 1256]]) and quote in pennies on most strikes thanks to the SEC's Penny Pilot Program, which makes them particularly attractive for retail-sized accounts, IRA strategies, and any tactic that benefits from tight quoting.

## Overview

SPY tracks the S&P 500 Index but, because it is a fund holding actual securities, behaves differently from the SPX index in three important ways:

1. **It pays distributions** — typically quarterly (March, June, September, December). On ex-dividend dates the ETF price drops by the distribution amount, which creates [[ex-dividend-date|ex-dividend]] risk for short call holders (see Dividend Risk below).
2. **It can be borrowed and shorted** — SPY shares are deliverable on option exercise, which means physical delivery and pin-risk dynamics matter.
3. **Options are American-style** — exercise can happen on any business day before expiration, so sellers face early-assignment risk (see [[assignment-and-exercise]]).

SPY options trade across multiple exchanges in a national market system. Daily volume routinely tops several million contracts, and SPY weeklies and 0DTE expirations make up a large share of total US options volume.

## Specifications

| Spec | Value |
|---|---|
| Underlying | SPDR S&P 500 ETF (SPY) — 100 shares deliverable |
| Multiplier | $100 (= 100 shares per contract) |
| Exercise style | American |
| Settlement | Physical (delivery of 100 shares on exercise/assignment) |
| Strike intervals | $1 (broadly), $0.50 near-the-money on some weeklies |
| Tick size | $0.01 (Penny Pilot) on most strikes; $0.05 above $3 on some |
| Trading hours | 9:30am–4:00pm ET (with limited extended-hours options trading) |
| Listing | Multiple US options exchanges (CBOE, NYSE Amex, ISE, BOX, etc.) |
| Tax treatment | Standard equity option (short/long-term based on holding period) |
| Expirations | Monthly (3rd Friday), weekly (Mon/Wed/Fri at minimum), and daily 0DTE |

## Tax Treatment (Standard Equity)

SPY is structured as a Unit Investment Trust holding S&P 500 stocks; therefore SPY options are taxed as standard equity options, **not** Section 1256:

- **Holding-period sensitive** — gains held >1 year are long-term; <1 year are short-term (top federal rate ~37% vs ~20% long-term + 3.8% NIIT).
- **Wash-sale rules apply** — losses can be disallowed if substantially identical positions are reopened within 30 days (see [[wash-sale-rules-options]]).
- **No mark-to-market** — open positions are not deemed-closed on Dec 31, so positions can carry across years without forced taxable events.
- **No 60/40 blend** — the same trade in [[spx-options|SPX]] would be taxed at a meaningfully lower blended rate for short-term traders.

For active premium-sellers, the standard-equity treatment is the single biggest practical disadvantage of SPY versus SPX or [[xsp-options|XSP]].

## Settlement & Exercise

- **Physical delivery** — exercising one long SPY call delivers 100 SPY shares (debited at strike); a long ITM put delivers a short position of 100 shares at the strike (or closes an existing long).
- **Auto-exercise** — by OCC rules, options that finish $0.01 or more in-the-money at expiration are automatically exercised unless a "do-not-exercise" instruction is filed.
- **Pin risk** — when SPY closes very near a strike at expiration, sellers cannot know with certainty whether they will be assigned, creating overnight directional exposure (see [[pin-risk]]).
- **Early exercise** — almost always uneconomic except just before ex-dividend dates on deep ITM calls (see Dividend Risk).

For full mechanics see [[cash-vs-physical-settlement]] and [[assignment-and-exercise]].

## Liquidity Profile

- **Volume** — among the highest of any US-listed option, often the single most active product in the country on busy days.
- **Quote tightness** — penny-wide bid/ask on most ATM strikes; the deepest options market in the world by quoted depth at the inside.
- **Strike granularity** — $1 increments mean traders can target almost any underlying level precisely.
- **Multi-exchange** — quotes sourced from a dozen exchanges create natural arbitrage that compresses spreads.
- **Off-hours** — SPY tracks futures-implied levels via the after-hours ETF market; SPX, by contrast, has its own extended Globex session.

## Greeks and Volatility-Surface Behavior

SPY options track the same S&P 500 benchmark as [[spx-options|SPX]], so their volatility surface is nearly identical in *shape* — but the wrapper introduces distinctive Greek behaviors:

- **Delta** — SPY delta is distorted near ex-dividend by the [[ex-dividend-date|distribution]] embedded in the forward price; deep-ITM call deltas approach 1.00 but carry the early-exercise risk that index options never face. Practitioners often size SPY positions in *share-equivalent* delta because physical delivery is real.
- **Gamma** — SPY's penny ticks and $1 strikes make for an extremely fine gamma grid; the deepest single options book in the US means dealer gamma in SPY is part of the same broad-market [[gamma-exposure|GEX]] picture as SPX, just at ~1/10 the notional per contract.
- **Theta** — identical decay dynamics to SPX in percentage terms; the [[variance-risk-premium]] is harvested the same way, but every gain is taxed at the higher equity rate (see Tax Treatment).
- **Vega** — SPY and SPX implied vol move together (both reference the same [[vix|VIX]]-measured surface). A vega-hedged book can mix SPY and SPX legs, though the tax and settlement mismatch must be managed.

### The volatility surface

SPY exhibits the same characteristic broad-index surface as SPX:

- **Steep negative [[volatility-skew|skew]]** — puts richer than equidistant calls, the persistent crash-protection premium that has defined index options since 1987.
- **Term structure** — upward-sloping (near vol below far vol) in calm regimes, inverting in stress, traded via [[weekly-options|weekly]]/monthly [[calendar-spread|calendars]].
- **Dividend kink** — unlike a pure index, SPY's surface and put-call parity embed discrete quarterly distributions, which is what creates the [[ex-dividend-date|ex-dividend]] early-exercise dynamic on short calls.

The practical upshot: SPY's penny-tick surface lets traders capture skew and calendar edges in increments too fine for SPX's $0.05/$0.10 tick — at the cost of equity (non-§1256) taxation and assignment management.

## Common Spread Structures

SPY's penny ticks and $1 strikes make defined-risk multi-leg structures especially clean:

| Structure | Construction | View | SPY-specific note |
|---|---|---|---|
| [[covered-call\|Covered call]] | Long 100 SPY + short call | Income on shares | Monetizes physical delivery rather than avoiding it |
| [[cash-secured-put\|Cash-secured put]] | Short put, cash reserved | Acquire SPY at a discount | Assignment is by design |
| [[wheel-strategy\|Wheel]] | CSP → assigned → covered call → repeat | Continuous income | The retail SPY workhorse |
| Put credit spread | Short higher put, long lower put | Mildly bullish / short vol | Penny ticks capture edge SPX erodes |
| [[iron-condor\|Iron condor]] | Short strangle + protective wings | Range-bound, defined risk | $1 strikes allow precise wing placement |
| [[put-spread\|Put spread]] (long) | Long higher put, short lower | Cheap tail hedge | Penny pricing keeps roll cost low |
| Calendar / diagonal | Sell near, buy far | Term-structure / vega | Beware dividend timing on the legs |

Because SPY is **American-style and physically settled**, every short-option leg must be screened for early-assignment and [[ex-dividend-date|ex-dividend]] risk — the single biggest operational difference from the otherwise-identical [[spx-options|SPX]] structures. See [[assignment-and-exercise]].

## SPY vs SPX Comparison

| Dimension | SPY | [[spx-options|SPX]] |
|---|---|---|
| Underlying | ETF (holds 500 stocks) | Index (no shares) |
| Notional per contract | ~$50,000 (at SPY 500) | ~$500,000 (at SPX 5000) |
| Exercise | American | European |
| Settlement | Physical (100 shares) | Cash |
| Tax | Standard equity | Section 1256 (60/40) |
| Tick size | $0.01 (penny pilot) | $0.05 / $0.10 |
| Strikes | $1 broadly | $5 broadly |
| Dividend risk | Yes (quarterly) | No |
| Early-assignment risk | Yes | No |
| Capital efficiency | 1x | ~10x |
| Best for | Smaller accounts, IRAs, granular sizing | Tax-sensitive active traders, scale |

**When to choose SPY:**

- IRA or tax-advantaged accounts where Section 1256's mark-to-market is irrelevant.
- Small accounts where SPX's $50K notional per contract is too coarse.
- Strategies that need penny-tick pricing (e.g., scalping cheap OTM weeklies).
- Traders who are comfortable managing assignment.

**When to choose SPX:**

- Active premium-selling where after-tax return matters.
- Large accounts where contract count would otherwise become operationally heavy.
- Strategies that benefit from European exercise (no early assignment).

## Dividend Risk

SPY pays a distribution roughly every quarter (typical ex-dates in mid-March, June, September, and December). On the ex-dividend date the ETF price drops by the distribution amount. The implication for short call holders:

- A deep ITM call held by a long counterparty becomes a candidate for **early exercise on the day before ex-dividend** if the remaining extrinsic value is less than the upcoming distribution. The long exercises to capture the dividend; the short call writer is assigned and effectively forfeits the dividend to the counterparty.
- This is the single most common cause of unexpected early assignment on SPY.
- **Pre-ex-dividend defense:** check short call positions for extrinsic value < expected dividend; if so, roll up/out or buy back ahead of the close.

See [[ex-dividend-date]] and [[dividend-adjustments]].

## ITPM Use Cases

While [[itpm|ITPM]] portfolios generally prefer [[spx-options|SPX]] for tax and assignment reasons, SPY has clear roles:

- **Smaller-account income strategies** — [[wheel-strategy]], [[covered-call|covered calls]], [[cash-secured-put|cash-secured puts]] on a granular share basis.
- **IRA-eligible exposure** — most retirement accounts permit defined-risk SPY options strategies; SPX is increasingly available but historically has been more restricted at retail brokers.
- **Tactical hedges where penny pricing matters** — short-dated OTM puts as cheap tail hedges; the tighter quoting on SPY can offset the lack of Section 1256 benefit on short hold periods.
- **Cross-product spreads** — pairing SPY with SPX or [[xsp-options|XSP]] for tax-loss harvesting that avoids wash-sale concerns (the products are not "substantially identical" for tax purposes per common practitioner reading, though confirmation with a tax professional is essential).
- **Pairs vs single-name equities** — natural hedge leg for [[long-short-equity]] books that hold individual stocks on the long side.

## Typical Strategies

SPY's penny ticks, $1 strikes, and physical settlement make it the retail workhorse:

- **Income on shares** — [[covered-call|covered calls]] and the [[wheel-strategy|wheel]] against a long SPY position, monetizing physical delivery rather than avoiding it.
- **Cash-secured puts** — [[cash-secured-put|CSPs]] to acquire SPY at a discount, accepting assignment by design.
- **Defined-risk spreads** — vertical [[put-spread|put spreads]] / [[call-spread|call spreads]] and [[iron-condor|iron condors]], where the $0.01 tick lets traders capture small edges that SPX's wider ticks erode.
- **Cheap tail hedges** — short-dated OTM puts; penny pricing keeps the cost of rolling protection low.
- **0DTE scalping** — same-day [[0dte-trading|0DTE]] directional and credit trades on the deepest single options book in the US.

Because SPY is American-style and physically settled, every short-option strategy must account for early-assignment and dividend risk — see the sections above.

## Risks

- **Early assignment** — particularly on short ITM calls before quarterly ex-dividend dates.
- **Pin risk at expiration** — physically-settled options near a strike at the close.
- **Tax drag for short-term traders** — every gain taxed at marginal rate without 60/40 benefit.
- **Wash-sale tracking** — losing trades reopened within 30 days are disallowed.
- **Liquidity is tight at ATM but thinner on far wings** — same caveat as any equity option.

## Historical Context

SPY launched in **1993** as the first US exchange-traded fund, and listed options on it followed shortly after — making SPY options one of the longest-running, most heavily traded options markets in the world. A few milestones shaped how the product is used today:

- **Penny Pilot Program** — the SEC's program (rolled out over 2007–2010) brought $0.01 quoting to the most liquid options, including SPY. This is the structural origin of SPY's defining edge over [[spx-options|SPX]]: penny-tight quoting that lets traders capture small edges SPX's $0.05/$0.10 tick erodes.
- **Weekly options** — the proliferation of [[weekly-options|weeklies]] (and later daily [[0dte-trading|0DTE]] expirations) turned SPY into a premier short-dated trading vehicle alongside SPX; SPY weeklies and 0DTE now account for a large share of total US options volume.
- **The 0DTE era (2022–2025)** — same-day expirations made SPY a core venue for retail and systematic intraday flow, sharing the broad-market dealer-gamma dynamics tracked via [[gamma-exposure|GEX]].
- **The enduring SPY-vs-SPX choice** — across these eras the fundamental trade-off has never changed: SPY wins on tick granularity and small-account/IRA accessibility; [[spx-options|SPX]] wins on §1256 tax treatment and European exercise. The choice is driven by account size, tax status, and tolerance for assignment.

## Related

- [[index-options]] — cash-settled index counterpart franchise
- [[options]] — options fundamentals
- [[spx-options]] — cash-settled, European-style index sibling
- [[xsp-options]] — mini-SPX with Section 1256 tax treatment
- [[ndx-options]] — Nasdaq-100 index options
- [[rut-options]] — Russell 2000 index options
- [[vix]] — implied volatility on the S&P 500
- [[section-1256-contracts]] — what SPY misses
- [[cash-vs-physical-settlement]]
- [[american-vs-european-options]]
- [[assignment-and-exercise]]
- [[ex-dividend-date]]
- [[weekly-options]]
- [[0dte-trading]]
- [[wheel-strategy]]
- [[covered-call]]
- [[cash-secured-put]]
- [[iron-condor]], [[put-spread]] — defined-risk structures
- [[options-greeks]] — Greeks vocabulary
- [[volatility-skew]] — the index put-skew SPY shares with SPX
- [[implied-volatility]], [[calendar-spread]] — surface and term-structure
- [[gamma-exposure]] — dealer-gamma market structure
- [[variance-risk-premium]] — the premium short-vol harvests
- [[pin-risk]] — physical-settlement expiry risk
- [[qqq-options]] — Nasdaq-100 ETF analog
- [[options-portfolio-construction]]

## Sources

- State Street SPDR S&P 500 ETF Trust prospectus
- OCC (Options Clearing Corporation) exercise and settlement rules
- SEC Penny Pilot Program documentation
- IRS Publication 550 (investment income, equity options)
