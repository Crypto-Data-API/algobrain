---
title: "October 2025 Crypto Liquidation Cascade & ADL Crisis"
type: news
created: 2026-05-05
updated: 2026-06-21
status: excellent
tags: [crypto, history, risk-management, derivatives, liquidity, leverage]
aliases: ["Oct 2025 crypto crash", "October 10-11 2025 crash", "2025 ADL crisis", "$20B liquidation cascade"]
related: ["[[auto-deleveraging]]", "[[liquidation-cascade-modeling]]", "[[liquidation-risk]]", "[[funding-rate]]", "[[funding-rate-arbitrage]]", "[[crypto-perp-backtesting-pitfalls]]", "[[hyperliquid]]", "[[binance]]", "[[bybit]]", "[[okx]]", "[[insurance-fund]]", "[[crypto-flash-crashes]]", "[[basis-trading]]"]
event_date: 2025-10-10
markets_affected: [crypto]
impact: high
verified: true
sources_count: 4
---

On **October 10-11, 2025**, crypto perpetual-futures markets suffered the largest 24-hour forced-liquidation event in their history: roughly **$20 billion in liquidations** across Binance, Bybit, OKX, and Hyperliquid, accompanied by the **first systemic Auto-Deleveraging (ADL) crisis** in which profitable hedges and "neutral" basis-trade legs were force-closed by venues to keep insurance funds solvent. The event reshaped how professionals model liquidation tail risk, broke the assumption that ADL is a tail-of-tail event, and triggered a multi-month compression of perp funding rates as basis-trade desks de-risked.

## Timeline

| Time (UTC) | Event |
|------------|-------|
| Oct 10 ~14:00 | Macro risk-off begins; BTC slides from ~$118k toward $112k on heavy spot ETF outflows; perps OI elevated near record highs |
| Oct 10 ~17:30 | First wave of long liquidations on Binance; ~$2.5B liquidated in 90 minutes; mark price diverges from index on thin venues |
| Oct 10 ~19:00 | BTC prints ~$104k low on Hyperliquid; ETH down 18% intraday; alt liquidations cascade as cross-margin collateral marked down |
| Oct 10 ~21:00 | Bybit and OKX insurance funds begin absorbing socialised losses; ADL queues activate on multiple venues |
| Oct 11 ~00:00–04:00 | ADL waves force-close profitable shorts and basis-arb hedge legs across Binance, Bybit, OKX, Hyperliquid; market makers see "neutral" books re-opened to directional risk |
| Oct 11 ~06:00 | Funding rates print extreme negative on perps as MMs withdraw quotes and longs are squeezed both ways |
| Oct 11 ~12:00 | Liquidation total exceeds $20B by CoinGlass aggregation; second-largest single-asset wipe (ETH) at ~$5.5B |
| Oct 11–14 | Funding rates compress sharply; basis collapses as desks unwind cash-and-carry; OI down ~35% from pre-event peak |

## Pre-Event State (the loaded spring)

The severity of the cascade was a function of *initial conditions*, not the size of the macro shock. Going into October 10, the perp ecosystem sat at multiple simultaneous extremes:

| State variable | Value entering Oct 10 | Historical percentile |
|----------------|-----------------------|-----------------------|
| Aggregate perp open interest | ~$95B | ~99th |
| Median retail leverage | 8-12x | ~95th |
| Median institutional leverage | 3-5x | elevated |
| Funding rate (BTC, annualised) | ~6% (down from ~11% in Q1) | crowded carry |
| Basis-arb / cash-and-carry book share | heavy | record |
| Insurance-fund coverage (Bybit, OKX) | thinning vs OI growth | below-comfort |

The combination — record OI, high leverage, and a crowded short-perp/long-spot basis population — meant the market was a *coiled spring*: a modest directional impulse could trigger forced selling, and the people who would normally absorb it (basis desks, market makers) were themselves long the instruments that would be force-closed. This is the precondition pattern Arnold-style [[counterparty-stress-arbitrage]] looks for, and the macro analog of the [[terra-luna|Terra reflexive doom-loop]] in a different asset class.

## What Happened

A macro risk-off impulse on October 10 met a perp ecosystem with **record open interest (~$95B aggregate)**, elevated **leverage (median 8-12x retail, 3-5x institutional)**, and a heavy population of cash-and-carry / basis-arb books that were short perps against spot ETF or spot exchange longs. The first ~$2-3B of long liquidations forced mark prices below index on the thinnest venues (notably Hyperliquid and OKX), which:

1. Triggered **margin calls on cross-margin alt positions** held by retail and prop desks, cascading into alt liquidations
2. Accelerated **mark-price divergence** between venues, breaking inter-exchange triangulation that market makers rely on
3. Caused MMs to **widen quotes or pull**, removing the absorbing liquidity that normally damps cascades
4. Drained **insurance funds** on Bybit and OKX faster than expected as bankrupt-account losses outpaced fund inflows from liquidation fees
5. Forced venues to invoke **Auto-Deleveraging** to maintain platform solvency once insurance funds approached depletion

## Liquidation Breakdown

**Aggregate:** ~$20B across all major venues over the 24-hour window (CoinGlass), eclipsing the previous single-day record from May 2021 (~$10B).

By venue (approximate, sourced from CoinGlass and venue post-mortems):

| Venue | Liquidations | Insurance fund drawdown | ADL invoked |
|-------|--------------|-------------------------|-------------|
| Binance | ~$8.5B | partial (well-capitalised) | limited, contained |
| Bybit | ~$5.0B | ~60-70% | yes, multiple waves |
| OKX | ~$3.5B | ~50% | yes |
| Hyperliquid | ~$1.8B | HLP vault drawdown ~$50M | yes (aggressive) |
| Others (dYdX, Lighter, Phemex) | ~$1.2B | varies | partial |

By asset (estimate):

- **BTC perps:** ~$7.5B (37%)
- **ETH perps:** ~$5.5B (27%)
- **SOL perps:** ~$2.0B (10%)
- **Alts (broad):** ~$5.0B (25%)
- **Other (memes, RWA-perps):** ~$0.5B

Long-side liquidations were ~85% of the total — the cascade was a one-way long-squeeze. Short books that survived initial leg saw their gains *clawed back* through ADL.

## The ADL Crisis

[[auto-deleveraging]] is the mechanism by which a derivatives venue, after exhausting its [[insurance-fund]], force-closes the most-profitable / highest-leverage opposing positions to absorb bankrupt-account losses. Until October 2025 it had been treated as a rare tail-of-tail mechanism. The October cascade made it a **first-order risk** for perpetual strategies.

What broke:

- **Basis-trade desks** running short perp / long spot saw the perp leg force-closed at the worst possible mark, leaving them naked long spot at the bottom of the move. Multiple sub-$500M funds reported 20-40% drawdowns on books that were nominally market-neutral.
- **Funding-rate arbitrage** strategies (long one venue / short another to harvest funding spread) saw the profitable leg ADL'd while the unprofitable leg remained, instantly converting a low-vol carry book into directional crypto-beta.
- **Delta-neutral options market makers** using perps to hedge gamma had hedge legs closed under them, blowing up a class of strategy that had never previously seen ADL exposure.
- **Hyperliquid's HLP vault** — the on-chain liquidity backstop — drew down ~$50M and itself became an ADL counterparty, validating the warnings that on-chain perp venues with shallower insurance funds carry higher ADL probability per dollar of OI.

The ADL waves moved in **multiple discrete pulses** over ~6 hours, not a single event, because each pulse re-balanced insurance-fund solvency only briefly before fresh bankrupt accounts arrived. Several venues subsequently disclosed that **>40% of profitable counter-side accounts touched ADL at least once** during the cascade.

## Funding-Rate Aftermath

Going into October 10, perp funding had been compressing through 2025 (~11% annualised average in Q1 down to ~6% by September) as basis-arb desks crowded the carry. Post-cascade:

- Funding **spiked deeply negative** on October 11 (-150% to -300% annualised on multiple BTC venues for several hourly intervals) as longs were squeezed and MMs pulled, then mean-reverted toward zero by October 13
- ETH perp funding hit -400% annualised hourly on Hyperliquid at the lowest point — one of the deepest single-hour negative prints in the venue's history
- By mid-November funding was running **~3-4% annualised** — below short-dated Treasuries — and stayed compressed through year-end
- Basis-arb capacity shrank materially as funds re-priced ADL risk into expected returns; the strategy, formerly a near-risk-free carry, started being underwritten with explicit ADL-tail haircuts (5-15% of notional per year)
- New entrants to funding-rate arbitrage essentially halted through Q4 2025; aggregate perp OI across the four major venues recovered only to ~$70B by year-end versus the pre-event ~$95B peak

The compression matters for backtesting because it represents a structural break: any historical-funding-rate replay that does not segment pre-October-2025 from post-October-2025 will systematically over-state expected carry returns by 2-4x.

## Comparison to Prior Liquidation Events

October 2025 was not the first crypto liquidation cascade, but it was the first to break the *neutral-book* assumption at scale via [[auto-deleveraging]]. Prior major events were one-directional liquidation waves; the October cascade added a second mechanism (ADL) that reached profitable, hedged positions.

| Event | Approx liquidations (24h) | Primary driver | ADL a factor? | Distinct lesson |
|-------|---------------------------|----------------|---------------|-----------------|
| Mar 2020 "COVID crash" | ~$1.6B (BitMEX-led) | Spot collapse, exchange overload | No | Venue outages amplify cascades |
| May 2021 leverage flush | ~$10B | Leveraged long unwind | Minimal | First $10B-scale single-day wipe |
| [[terra-luna\|May 2022 Terra/LUNA]] | spot-driven, ~$40B value destroyed | Algorithmic-stablecoin death spiral | N/A (spot/contagion) | Reflexive mechanisms become doom loops |
| Nov 2022 FTX collapse | multi-day | Exchange insolvency, contagion | N/A | Counterparty/custody risk |
| **Oct 2025 ADL crisis** | **~$20B** | Leveraged long flush + ADL | **Yes — systemic** | "Neutral" books are not ADL-proof |

The October event most resembles the **forced-unwind** structure that John Arnold exploited against [[amaranth-advisors|Amaranth]] in 2006 — a participant whose position is large relative to depth is forced to transact at the worst moment, and the survivors are on the other side. See [[john-arnold]] and [[counterparty-stress-arbitrage]]. The crypto-specific twist is that ADL makes *the venue itself* the forced unwinder of the winning side.

## Key Terms

| Term | Meaning in this event |
|------|------------------------|
| [[auto-deleveraging\|ADL]] | Venue force-closes profitable/high-leverage opposing positions once the insurance fund is exhausted |
| [[insurance-fund]] | Venue-held buffer that absorbs bankrupt-account losses before ADL triggers |
| [[funding-rate]] | Periodic payment between perp longs and shorts that tethers perp to spot |
| [[basis-trading\|Basis / cash-and-carry]] | Long spot, short perp (or futures) to harvest funding/basis — the book class hit hardest |
| Mark vs index divergence | Gap between a venue's mark price and the composite index; reached 200-400bp at peak |
| HLP vault | Hyperliquid's on-chain liquidity provider vault; itself became an ADL counterparty |

## Affected Market Participants

- **Centralised market makers** (Wintermute, Auros, GSR, others): reported MTM hits on basis books; several rotated capital toward options market making where ADL is not a mechanism. Quote-pulling during the worst hour of the cascade was a deliberate risk-management choice, not an outage.
- **Crypto-native funds running cash-and-carry / funding arb** (multiple sub-$1B funds): drawdowns of 15-40% on nominally neutral books; at least three reportedly wound down in the following weeks. Several published post-mortems explicitly citing ADL as the unmodelled-risk that broke their books.
- **Retail leveraged longs**: the bulk of the $20B in liquidations; CoinGlass attributed ~70% to retail-sized accounts (<$50k notional). The retail-side wipe contributed materially to OI shrinkage and to subsequent funding compression.
- **DeFi vaults providing perp liquidity** (Hyperliquid HLP, GMX GLP, dYdX equivalents): real losses, not just MTM, as bankrupt accounts socialised. HLP depositors saw negative day on October 11; GLP saw smaller drawdown given GMX's lower OI exposure relative to AUM.
- **Spot ETF basis-trade desks** (TradFi entities running long ETF / short CME or short perp): CME leg held without issue (CME did not invoke any equivalent of ADL); perp leg ADL'd; partial losses on the perp side of the structure. This validated CME-vs-perp leg selection for the basis-trade post-event — TradFi capacity flowed back toward CME futures and away from offshore perps.
- **Stablecoin-collateral lenders on Aave/Morpho/Spark**: indirect exposure via crypto-collateralised loans where the borrower's perp account was ADL'd and they could not service the loan. A small wave of liquidations on lending protocols followed October 11, though without reaching systemic-stress thresholds.

## Lessons for Backtesting

This event is the **canonical case study** for [[crypto-perp-backtesting-pitfalls]], specifically:

1. **ADL must be modelled.** Backtests that assume liquidations only affect losing positions are dangerously optimistic. A realistic ADL model assigns probability proportional to (a) insurance-fund coverage ratio, (b) position rank in venue's profit-and-leverage queue, and (c) cross-venue cascade correlation. Pre-October-2025 backtests of cash-and-carry strategies showed Sharpe ratios of 4-8 net of costs; post-event re-estimation with explicit ADL-tail modelling cut realistic Sharpe to 1.5-2.5.

2. **Liquidation cascade correlation across venues.** Backtests built on single-venue tick data systematically miss the cross-venue feedback loop. Realistic stress models require synchronised order-book reconstruction (CoinGlass, Kaiko) across at minimum Binance + Bybit + OKX + Hyperliquid.

3. **"Neutral" is a backtest assumption, not a market reality.** Any strategy whose backtest returns a Sharpe above ~3 on a multi-year window must be re-tested under an explicit ADL-tail scenario; if the strategy degrades materially, the original Sharpe was an artefact of unmodelled mechanics.

4. **Insurance-fund balance is a state variable.** Funding-rate, basis, and liquidation models that ignore venue insurance-fund balance drift will undershoot tail loss. Live monitoring of insurance-fund coverage ratios should be part of any production perp strategy.

5. **OI / leverage state-space conditioning.** The cascade's severity correlated tightly with pre-event aggregate OI and median account leverage. Strategies must reduce sizing or hedge directional risk when these state variables exceed historical 90th-percentile thresholds.

## Lessons for Risk Management

- **Hard leverage caps**: many surviving funds had unilateral 3x effective leverage caps regardless of venue maximums — these books lost less and recovered faster
- **ADL queue monitoring**: live dashboards tracking position rank in venue ADL queues (rank by profit × leverage) should be standard for any perp-heavy book
- **Multi-venue diversification with correlation awareness**: spreading exposure across venues mitigates single-venue ADL but does *not* mitigate cross-venue cascade — diversification is necessary, not sufficient
- **Insurance-fund-conditional sizing**: cut perp exposure when target venue's insurance fund coverage falls below trigger thresholds (Bybit publishes this real-time; OKX publishes daily; Binance and Hyperliquid require off-chain inference)
- **Cash buffer for ADL re-establishment**: book design should assume the hedge leg can be force-closed at the worst possible price; capital reserved to re-establish the hedge from spot is now standard practice
- **OI / leverage state-space awareness**: monitor aggregate venue OI, median account leverage, and pre-event funding skew; reduce exposure when the combined signal exceeds historical 90th-percentile (October 10 printed in the 99th percentile across all three signals simultaneously)
- **Counterparty-side stress for DeFi vaults**: vaults like HLP and GLP are not "passive yield" — they are sellers of variance and absorbers of bankrupt-account losses. Treat allocation to such vaults as a directional crypto-beta + short-vol exposure, not as carry

## Why Backtests Missed This

Pre-October 2025, the typical retail and mid-tier institutional backtest of a perp strategy made the following implicit assumptions:

1. Liquidations are **independent** across positions on a venue
2. Liquidations are **independent** across venues
3. Insurance funds are **infinitely deep** for the purposes of strategy modelling
4. Profitable counter-side positions are **untouched** by the liquidation mechanism
5. Funding rates are **stationary** within regime, with no structural breaks
6. Mark price tracks index price within ~10bp under all conditions

October 10-11 invalidated all six assumptions simultaneously. Liquidations were perfectly correlated within and across venues (correlation ≈ 1 during the worst hour). Insurance funds depleted in hours, not days. Profitable counter-side positions absorbed losses via ADL. Funding regime broke. Mark-index divergence reached 200-400bp on multiple venues at peak stress.

The lesson for backtest construction: any one of these assumptions, *if it were correct*, makes the strategy look attractive. The combination of all six being correct is what made carry trades look like 4-8 Sharpe machines. The combination of all six being wrong simultaneously is what produced the October cascade.

## Sources

- CoinGlass aggregate liquidation data and per-venue post-mortems, October 2025
- BitMEX research, *State of Crypto Perps 2025* (covers pre-event conditions and immediate aftermath)
- CryptoSlate, "Bitcoin sees another flash crash leading to multi-billion cascade in crypto liquidations" (chronicled cascade in real time)
- Hyperliquid HLP post-cascade transparency report, October 2025
- Perplexity research summary, *Backtesting pitfalls in crypto perps* (2026-04-22): identifies October 10-11 2025 as watershed event for ADL modelling

## Related

- [[auto-deleveraging]] — mechanism explainer
- [[liquidation-cascade-modeling]] — how to model events like this
- [[liquidation-risk]] — broader risk category
- [[crypto-perp-backtesting-pitfalls]] — backtesting framework lessons
- [[funding-rate]], [[funding-rate-arbitrage]] — strategies affected
- [[basis-trading]] — strategy class hit hardest
- [[insurance-fund]] — what depleted across venues
- [[hyperliquid]], [[binance]], [[bybit]], [[okx]] — affected venues
- [[crypto-flash-crashes]] — sibling timeline of cascade events
