---
title: "2015 ETF Flash Crash"
type: news
created: 2026-04-13
updated: 2026-06-12
status: good
tags: [history, crashes, market-microstructure, stocks]
event_date: 2015-08-24
markets_affected: [stocks, etfs]
impact: high
aliases: ["August 24 2015 Flash Crash", "ETF Flash Crash", "Black Monday 2015"]
related: ["[[flash-crashes]]", "[[flash-crash-2010]]", "[[circuit-breakers]]", "[[high-frequency-trading]]", "[[liquidity]]", "[[market-maker]]", "[[algorithmic-trading]]"]
---

On August 24, 2015, US equity markets opened into chaos. The Dow Jones Industrial Average dropped 1,089 points within minutes of the opening bell — the largest intraday point decline in its history at that time. But the headline number masked something far more alarming: hundreds of [[etf-arbitrage|ETFs]] traded 20–35% below their net asset values for extended periods, exposing a fundamental flaw in how ETF pricing functions during extreme market stress. For traders, this was the day the "ETFs are always liquid" narrative shattered.

## What Happened

### The Setup

China had devalued the yuan on August 11, 2015, triggering a global selloff. On August 24 — dubbed "Black Monday" in China — the [[shanghai-composite|Shanghai Composite]] crashed 8.5% overnight. European markets were deep in the red. [[sp500|S&P 500]] futures hit limit-down before the US open, indicating a gap-down of roughly 5%.

The problem was not the magnitude of the decline. Markets can handle a 5% selloff. The problem was the *structure* of the open.

### The Cascade

At 9:30 AM ET, a flood of market sell orders — many from retail investors and stop-loss triggers — hit a market with almost no bids. [[market-maker|Market makers]] and [[high-frequency-trading|high-frequency traders]] who normally provide [[liquidity]] had pulled back or drastically widened their quotes, unwilling to make prices in a gap-down environment with no reliable reference price.

What followed was unprecedented:

- **1,278 trading halts** triggered across **471 individual stocks and ETFs** in the first 30 minutes of trading alone
- These were [[circuit-breakers|LULD (Limit Up-Limit Down)]] halts — the very mechanism implemented after the [[flash-crash-2010|2010 Flash Crash]] to prevent disorderly markets
- The LULD bands, calculated from recent prices, were immediately breached as stocks opened far below prior closes
- As individual stocks halted, ETFs that held those stocks could no longer be accurately priced

### The ETF Meltdown

The iShares Core S&P 500 ETF (**IVV**, approximately $65 billion in AUM) fell 26% at one point — roughly 20 percentage points below its actual fair value. The iShares Select Dividend ETF (**DVY**) cratered 35% to $48 per share while its underlying basket of holdings was only down approximately 2.7%. The Vanguard Consumer Staples ETF (**VDC**) — holding stable names like Procter & Gamble and Coca-Cola — dropped 32%.

These were not obscure, thinly-traded products. These were among the largest, most liquid ETFs in the world.

Recovery took roughly 30 minutes as [[etf-arbitrage|arbitrageurs]] cautiously re-engaged and the underlying stocks reopened from their halts. By the close, most ETFs had returned to within normal tracking ranges — but the damage to anyone who sold at the lows, or whose stop-losses triggered, was permanent.

## Why ETFs Broke

The 2015 crash exposed a structural vulnerability in the ETF ecosystem that most investors had never considered:

1. **ETF liquidity is borrowed, not intrinsic.** ETFs depend on a continuous arbitrage mechanism: [[market-maker|authorized participants (APs)]] buy the underlying stocks and exchange them for ETF shares (or vice versa), keeping the ETF price pinned to its [[nav|net asset value]]. When you trade an ETF at a tight spread, you are implicitly relying on this arbitrage functioning.

2. **LULD halts broke the arbitrage.** When individual stocks hit LULD bands and were halted, APs could not create or redeem ETF shares because they could not buy or sell the underlying basket. They also could not hedge their positions. Rational market makers do not quote prices they cannot hedge — so they stopped quoting.

3. **The cascade was self-reinforcing.** Stock halt → ETF can't be priced → ETF market maker pulls quote → ETF price collapses → ETF hits LULD → ETF halted → more uncertainty about fair value → more stocks affected. The circuit breakers designed to stabilize markets actually amplified the dislocation in ETFs.

4. **Market orders were the accelerant.** Retail investors placing market sell orders at the open received fills 20–30% below fair value because there were simply no bids at reasonable levels. The orders were filled at whatever price was available.

The core lesson: **ETF liquidity is a derivative feature, not a primary one.** It depends entirely on the arbitrage mechanism operating smoothly. When that mechanism breaks — and it will break during the moments you most need liquidity — ETF prices can detach violently from reality.

## Aftermath

The SEC conducted a comprehensive review of the August 24 events. Key outcomes and discussions included:

- **LULD recalibration** — regulators examined whether the halt bands were too narrow for the open, and whether the interaction between single-stock halts and ETF pricing needed specific rules
- **Opening auction procedures** — NYSE and other exchanges reviewed how they handle the transition from pre-market to regular trading during stress
- **Market maker obligations** — renewed debate over whether firms that profit from market-making in normal conditions should have affirmative obligations to provide liquidity during stress
- **ETF industry response** — fund sponsors became more cautious about marketing ETFs as inherently liquid instruments; disclosure language was updated to acknowledge structural risks

No sweeping regulatory changes were implemented specifically for ETFs, but the event permanently altered how sophisticated market participants think about ETF mechanics under stress.

## Lessons for Traders

1. **Never place market orders at the open during extreme stress.** Use limit orders. If you must sell, set your limit at a level you find acceptable — not "at any price." The traders who were destroyed on August 24 were overwhelmingly those with market orders and stop-loss market orders.

2. **Understand that ETF "liquidity" is conditional.** An ETF trading $2 billion per day in normal conditions can become effectively illiquid in seconds if the arbitrage mechanism fails. Do not confuse normal-times volume with crisis-times liquidity.

3. **Circuit breakers have second-order effects.** LULD halts in individual stocks can create pricing blackouts for ETFs, leading to dislocations far larger than the actual move in the underlying. This is a structural feature, not a bug that has been fixed.

4. **Dislocations create opportunity.** Traders who recognized the ETF/NAV gap on August 24 and bought aggressively during the panic were rewarded with 20–30% returns within 30 minutes. Understanding market structure lets you be a buyer when others are forced sellers.

5. **Stress-test your execution plan.** If your strategy involves selling ETFs during a crash, you need to account for the possibility that your exit price will be dramatically worse than the screen price.

## Related

- [[flash-crashes]] — overview of flash crash events
- [[flash-crash-2010]] — the original May 6, 2010 event that led to LULD implementation
- [[circuit-breakers]] — LULD bands and market-wide circuit breakers
- [[liquidity]] — the concept of market liquidity and its fragility
- [[market-maker]] — how market makers and authorized participants function
- [[high-frequency-trading]] — the role of HFT in modern market structure
- [[etf-arbitrage]] — the creation/redemption mechanism that keeps ETFs priced correctly
- [[algorithmic-trading]] — automated trading and its role in market stress events
- [[volmageddon]] — a later structural-product blow-up (inverse-VIX ETPs, Feb 2018)

## Sources

- SEC, *Research Note: Equity Market Volatility on August 24, 2015* (Division of Trading and Markets, December 2015) — the regulator's analysis of the LULD halt cascade and ETF/NAV dislocations; documents the ~1,278 halts across ~471 securities in the opening 30 minutes.
- BlackRock, *US Equity Market Structure: An Investor Perspective* (2015 white paper) — issuer analysis of why ETF arbitrage broke when underlying constituents were halted.
- Vanguard and *Wall Street Journal* / *Financial Times* coverage, 24-25 August 2015 — reporting on individual ETF dislocations (IVV ~-26%, DVY ~-35%, VDC ~-32%) and the subsequent recovery to NAV.
