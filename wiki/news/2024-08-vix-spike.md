---
title: "August 2024 VIX Spike"
type: news
created: 2026-05-05
updated: 2026-06-17
status: good
tags: [history, volatility, options, vix, risk-management, news]
aliases: ["August 5 2024", "VIX 65 Spike", "Aug 2024 Vol Shock"]
related: ["[[vix]]", "[[2024-08-yen-carry-unwind]]", "[[volatility]]", "[[vix-august-2024-spike]]", "[[long-vol-vs-short-vol]]"]
event_date: 2024-08-05
markets_affected: [stocks, options, fx]
impact: high
verified: true
sources_count: 0
---

# August 2024 VIX Spike

On the morning of **August 5, 2024**, the CBOE Volatility Index ([[vix|VIX]]) printed an intraday high of roughly **65** — its third-highest level on record, behind only the 2008 [[2008-global-financial-crisis|Global Financial Crisis]] and the March 2020 [[covid-crash|COVID crash]]. The spike was the equity-options expression of a global cross-asset deleveraging triggered by the unwinding of the Japanese-yen [[carry-trade]] (see [[2024-08-yen-carry-unwind]]). What made the episode distinctive was its speed: the VIX collapsed almost as fast as it rose, falling back toward the high-20s within days and into the mid-teens within weeks, making it one of the sharpest and shortest [[volatility]] shocks in modern market history.

## What Happened

A confluence of catalysts hit a heavily one-sided, short-volatility market over a single weekend:

| Date | Event |
|------|-------|
| **Jul 31, 2024** | [[bank-of-japan|Bank of Japan]] raised its policy rate to ~0.25% and signaled further hikes, strengthening the [[japanese-yen|yen]] |
| **Aug 1, 2024** | Weak US ISM manufacturing; markets begin pricing growth fears |
| **Aug 2, 2024** | Soft July US payrolls (114K vs ~175K expected; unemployment 4.3%) triggered the "Sahm Rule" recession signal; S&P 500 fell, VIX closed ~23 |
| **Aug 5, 2024** | Nikkei 225 fell **-12.4%** (worst session since Black Monday 1987); S&P 500 opened sharply lower; VIX printed ~**65** intraday before settling near **38** |
| **Aug 6–9, 2024** | Rapid recovery; equities retraced most losses; VIX fell back toward the 20s |

By mid-to-late August the S&P 500 had fully recovered its losses and went on to new highs, making the drawdown one of the shortest "V-shaped" panics on record.

## The Stale-Quote Microstructure

The ~65 print is widely regarded as partly a measurement artifact rather than a clean read on tradable risk. The VIX is computed from a strip of S&P 500 (SPX) option bid/ask quotes. In the first minutes of the August 5 US cash open, many SPX option quotes were **stale or extremely wide** — market makers had pulled liquidity amid the overnight Nikkei collapse and gapping futures. With sparse two-sided markets, the VIX formula mechanically produced an inflated value.

The dispersion was telling: **VIX futures and the VIX cash index diverged sharply** — front-month VIX futures traded around the high-30s/low-40s while the cash index spiked to ~65. Futures, priced on forward-looking dealer positioning rather than stale option quotes, never confirmed the 65 print. This gap between cash and futures is a recurring signature of liquidity-driven (as opposed to fundamentals-driven) volatility spikes.

## Why It Was So Violent and So Brief

- **Short-gamma dealer positioning**: Dealers were short gamma into the selloff, forcing them to sell futures as the market fell — mechanically amplifying the move down, then buy back as it recovered.
- **0-DTE and short-vol crowding**: A multi-year boom in short-volatility strategies — short strangles, short VIX-futures ETPs, [[volatility-risk-premium|vol-premium]] harvesters, and zero-days-to-expiry option selling — meant the market entered the shock heavily short vol. Forced unwinds of these positions accelerated the spike.
- **Carry funding shock**: The yen-funded [[carry-trade]] is a global leverage tap. When [[japanese-yen|JPY]] surged, margin calls cascaded across asset classes, forcing simultaneous liquidation of equities, FX, and crypto (see [[2024-08-yen-carry-unwind]]).
- **No fundamental break**: Unlike 2008 or 2020, there was no solvency crisis or economic stop. Once forced selling exhausted and the BoJ walked back its hawkishness (Aug 7), positioning normalized and volatility collapsed.

## Winners and Losers

| Side | Outcome |
|------|---------|
| **Short-vol / short-strangle sellers** | Severe losses; some short-VIX-ETP and short-strangle books took catastrophic single-day hits |
| **0-DTE premium sellers** | Whipsawed by the gap-down then snap-back |
| **Long-vol / tail-hedge funds** | Funds holding VIX call spreads and out-of-the-money puts (e.g., tail-risk specialists like Universa) profited on the spike |
| **Dispersion / relative-value desks** | Mixed, depending on gamma positioning |

## Trading Lessons

1. **A VIX print is not a fillable price.** During liquidity vacuums, the cash index can decouple from where volatility actually trades. Cross-check with VIX futures and SPX option mids before assuming a level is real.
2. **Short-vol carry is short a Lehman-shaped tail.** Months of small gains can be erased in one session; sizing must assume a multi-sigma gap.
3. **Cross-asset funding linkages dominate in deleveraging.** An FX/rates event (BoJ) became an equity-vol event because the same leveraged books spanned both.
4. **Speed cuts both ways.** The same forced-flow mechanics that produced the spike produced the recovery — making it as dangerous to chase the panic as it was to be short vol into it.

## Related

- [[vix]] — the index that spiked
- [[2024-08-yen-carry-unwind]] — the FX/funding trigger
- [[volatility]] — the broader concept
- [[vix-august-2024-spike]] — canonical event record with extended microstructure detail
- [[long-vol-vs-short-vol]] — the asymmetry this event illustrates
- [[bank-of-japan]] · [[japanese-yen]] · [[carry-trade]]

## Sources

- General market knowledge; no specific wiki source ingested yet.
