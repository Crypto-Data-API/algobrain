---
title: "Weekly Options"
type: concept
created: 2026-05-06
updated: 2026-06-11
status: good
tags: [options, derivatives, weekly]
aliases: ["Weeklys", "Weeklies", "SPXW", "Weekly Options"]
domain: [derivatives, options]
difficulty: intermediate
related: ["[[0dte-trading]]", "[[gamma-scalping]]", "[[section-1256-contracts]]", "[[options-portfolio-construction]]"]
---

**Weekly options** ("Weeklys") are option contracts that expire within a week of listing rather than following the traditional monthly third-Friday cycle. The Cboe introduced them in 2005 as a small experiment on a handful of products; today they cover essentially every trading day on SPX and most liquid equity underliers, and weekly volume — including same-day [[0dte-trading|0DTE]] expirations — exceeds traditional monthly volume on the index complex. Weeklies have a fundamentally different Greeks profile from monthlies: faster theta decay, sharper gamma near expiration, and less vega — which makes them powerful tools for event-driven trading and dangerous tools for un-managed short positions.

## Overview

The original options market settled on monthly third-Friday expirations as the standard cycle going back to the 1973 listing of the first listed equity options. Weeklies were an additive innovation: rather than wait for the next monthly, traders can now target almost any specific day for entry and exit.

Cboe rolled them out gradually:

- **2005** — first listing of "Weeklys" on a small set of products.
- **2010s** — broad expansion to hundreds of equity, ETF, and index underliers.
- **November 2022** — Cboe completes daily SPX expirations by adding Tuesday and Thursday SPXW listings (Monday/Wednesday/Friday were already daily). This turns SPX into a continuous-expiration market: every business day of the week now has at least one expiration.
- **2023+** — weekly and daily options exceed traditional monthly volume on SPX; 0DTE trading becomes a major share of total options activity.

Most equity options remain Friday-only weekly listings. The index complex (SPX, NDX, RUT, XSP) has the broadest daily coverage.

## Cycle Mechanics

- **Symbol convention** — SPX weeklies trade under the symbol **SPXW** (PM-settled), distinct from traditional monthly **SPX** (AM-settled).
- **Listing horizon** — weeklies are typically listed 1–6 weeks before expiration; new listings appear continuously as old ones expire.
- **Strike density** — comparable to or denser than monthly chains at the front, especially in the last week of life.
- **Expiration day** — most equity weeklies expire Friday; SPX expires every business day; some products have Wed and/or Mon weeklies.

## Weekly vs Monthly (theta/gamma comparison)

The differences in Greeks structure are not just quantitative — they change strategy design.

**Theta (time decay):**

- Theta is non-linear and accelerates as expiration approaches. A weekly option spends its entire life inside that acceleration zone, so a same-strike weekly typically loses time value much faster per day than a monthly with the same delta.
- For premium sellers, this means weeklies offer higher daily theta yield per unit of premium collected — but the position must be actively managed because everything else accelerates too.

**Gamma:**

- Gamma rises sharply in the final days. A weekly's gamma late in its life can be 5–10x its theoretical equivalent at the same delta on a 30-day option.
- Sharp gamma means small moves in the underlying create outsized P&L swings — both ways. Short gamma positions in the last day or two of a weekly can suffer catastrophic losses on a single intraday move.

**Vega:**

- Vega declines as expiration approaches. Weeklies have low vega, which means [[implied-volatility]] changes contribute less to their P&L than for monthlies. They are a closer-to-pure bet on realized price movement (and time).

**Practical implication:** weeklies trade time and price; monthlies trade time, price, and vol. Strategy choice should reflect which exposure the trader actually wants.

## Settlement Differences (SPXW PM vs SPX AM)

For S&P 500 options specifically, weeklies and monthlies settle differently:

- **SPX traditional monthlies (3rd Friday)** — **AM-settled** to the Special Opening Quotation (SOQ), calculated from opening prints of all 500 components on Friday morning. Final trading occurs Thursday afternoon.
- **SPXW weeklies** (including 0DTE) — **PM-settled** to the 4:00pm ET closing print of the SPX index. Trading on the expiration day continues until 4:00pm.

Spreads that mix AM- and PM-settled contracts (e.g., a calendar that buys a monthly and sells a weekly at the same strike) carry overnight gap risk because the two legs settle to different reference values. See am-vs-pm-settlement for full mechanics.

## Tax Status

For tax purposes, weekly options take the status of their underlying:

- **SPX/NDX/RUT/XSP weeklies** — qualify as [[section-1256-contracts|Section 1256]] contracts; 60/40 tax treatment applies regardless of how short the holding period is. A 2-minute SPXW scalp still gets the 60/40 blend.
- **SPY/QQQ/IWM weeklies** — taxed as standard equity options; no Section 1256 treatment.
- **Single-stock weeklies** — taxed as standard equity options.

This is one of the key reasons active short-term SPX traders use SPXW rather than SPY weeklies despite SPY's penny pricing.

## ITPM Use Cases

ITPM-style portfolios use weeklies in several specific scenarios:

- **Precise event timing** — selling a weekly straddle into earnings or a specific data release captures the IV crush or realized move with no exposure beyond the event window. See earnings-options-strategies.
- **Faster premium decay** — overlay strategies that systematically sell short-dated premium against a longer-dated position (e.g., diagonal calendars, double diagonals) extract theta faster on the short leg using weeklies.
- **Defined-risk earnings** — buying a weekly butterfly or iron condor for a known event provides a fixed-cost bet with no overnight assignment risk on cash-settled SPX/XSP variants.
- **Tactical gamma scalping** — long-gamma weekly positions in a known catalyst window, where the trader actively delta-hedges and harvests realized vol > implied vol. See [[gamma-scalping]].
- **Hedge layering** — buying weekly OTM puts as cheap, short-duration tail protection that rolls each week, allowing the portfolio to dynamically size hedge cost based on regime.

## Risks

- **Gamma blowups** — short weekly positions can lose multiples of the premium collected on a single sharp underlying move; the worst single-day P&L losses in retail and pro options trading typically come from short gamma in the last 1–2 days of a weekly.
- **Liquidity at non-standard strikes** — strikes outside the most heavily-traded ranges can have very wide bid/ask spreads in the final hours.
- **Pin risk** for physically-settled (e.g., SPY weekly) — when the underlying closes near a strike at 4:00pm Friday, sellers do not know if they will be assigned.
- **AM vs PM mismatch** — already noted; a SPX/SPXW calendar built without awareness of settlement type can produce surprise overnight P&L.
- **Theta-style overcrowding** — daily and weekly premium-selling strategies have become consensus retail trades, which can erode the [[volatility-risk-premium]] specifically at the very front of the term structure.

## Related

- [[0dte-trading]] — same-day weekly extreme
- [[section-1256-contracts]]
- [[gamma-scalping]]
- [[implied-volatility]]
- [[volatility-risk-premium]]
- [[options-position-sizing]]
- [[options-portfolio-construction]]

## Sources

- Cboe Weeklys product history and listing schedules
- Cboe SPXW specifications (Tuesday/Thursday additions, Nov 2022)
- OCC settlement and exercise rules
