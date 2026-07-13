---
title: "USD/JPY"
type: market
created: 2026-05-07
updated: 2026-06-21
status: excellent
tags: [forex, options, volatility, derivatives, japan]
aliases: ["USDJPY", "Dollar Yen", "Gopher", "USD/JPY"]
related: ["[[forex]]", "[[us-dollar]]", "[[bank-of-japan]]", "[[federal-reserve]]", "[[implied-volatility]]", "[[carry-trade]]", "[[yen-carry-trade]]", "[[options-concentration-risk]]", "[[eurusd]]", "[[vix-august-2024-spike]]", "[[interest-rates]]"]
---

USD/JPY is the second-most actively traded currency pair globally, expressing the price of the US dollar in Japanese yen. It is economically central because Japan is the world's largest net foreign creditor (~$3T+ in net international investment position) and because the JPY's status as the world's primary low-yield funding currency makes USD/JPY the **single highest-information cross in global macro** -- the pair where carry-trade leverage, safe-haven flows, and BOJ policy reflexivity all collide. From an options trading angle, USD/JPY is the FX pair most prone to sharp vol spikes, which is exactly what makes its options market both expensive in calm regimes and indispensable as a tail hedge.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Average daily turnover (spot + outrights + swaps) | ~$1.25T (BIS Triennial Survey 2022) |
| Share of total FX volume | ~13-14% |
| DXY index weight | 13.6% (second-largest after EUR) |
| Typical 1M ATM implied vol (calm regime) | 6-9% annualized |
| Typical 1M ATM implied vol (stress regime) | 12-25%+ annualized |
| Pip value (1 lot, 100,000 USD) | ~700 JPY (~$5 at USDJPY=140) |
| Quoted to | 3 decimal places (fractional pips on the 4th) |
| Settlement | T+2 |
| Primary listed options venue | [[cme-group|CME]] JPY/FX options on futures |
| Primary OTC venue | Interbank dealers; Tokyo and London centers most active |
| Retail proxy ETF | [[fxy-etf|FXY]] (Invesco CurrencyShares Japanese Yen Trust) |

The pair is conventionally quoted as **USD base / JPY quote** -- a quote of 145.20 means one dollar buys 145.20 yen. A higher number means a stronger dollar / weaker yen; a lower number means a stronger yen / weaker dollar.

## Instrument and Contract Specifications

USD/JPY exposure is accessible across the full FX instrument stack. The specifications below are structural conventions (not live prices) and let a trader size and compare instruments:

| Instrument | Venue | Contract / unit | Notional (indicative) | Tick / pip | Notes |
|------------|-------|-----------------|-----------------------|------------|-------|
| Spot FX | Interbank / ECN | 100,000 USD (standard lot) | 100,000 USD | 1 pip = 0.01 JPY | Settles [[t-plus-2|T+2]]; mini (10k) and micro (1k) lots for retail |
| JPY futures (6J) | [[cme-group|CME]] | 12,500,000 JPY | ~$85,000 at 147 | 0.0000005 USD/JPY = $6.25 | Quoted as **USD per JPY** -- inverse of spot |
| Micro JPY futures (MJY) | [[cme-group|CME]] | 1,250,000 JPY | ~$8,500 | 0.000001 = $1.25 | 1/10 the standard contract |
| Listed options on 6J | [[cme-group|CME]] | On the 6J future | -- | -- | American-style; inverse payoff convention |
| FXY ETF + options | NYSE Arca | [[fxy-etf|FXY]] shares | Retail-scale | $0.01 | Equity-account yen exposure; long FXY = long yen = short USD/JPY |
| OTC vanilla / exotic options | Interbank | Custom notional | Negotiated | -- | Deepest options book; risk reversals/butterflies quoted directly |
| NDF / forwards | Interbank | Custom | Negotiated | -- | Outright forwards price the [[interest-rate-differential|rate differential]] (forward points) |

**Forward points and the carry mechanic.** Because Japanese rates have historically sat far below US rates, USD/JPY trades at a **forward discount** -- the forward price is below spot. A trader who is long spot USD/JPY earns this differential as positive carry (the forward points roll in their favor), which is the mechanical engine of the [[carry-trade]]. When the [[interest-rate-differential|US-Japan rate spread]] compresses (Fed cuts, BOJ hikes), the carry shrinks and the incentive to hold the position weakens -- the trigger for unwinds.

## Macro Drivers

USD/JPY is fundamentally a **rate-differential and balance-of-payments story**, with a powerful **safe-haven overlay** on top.

1. **Rate differentials.** This is the dominant single driver. Japan ran zero or negative policy rates from 2016 through early 2024, while the US Fed funds rate climbed from 0% to 5.25-5.50% in 2022-2023. The ten-year UST-JGB spread blew out to ~400bp+ at peak, dragging USD/JPY from 115 in early 2022 to over 160 by mid-2024. The mechanical relationship: when the US-Japan rate spread widens, holding dollars (or dollar bonds) versus yen earns a large positive carry, drawing capital out of yen and into dollars.
2. **Bank of Japan policy.** [[bank-of-japan|BOJ]] has been the most distinctive central bank in the developed world, holding negative rates until March 2024, capping JGB yields with [[yield-curve-control|yield-curve control]], and intervening in FX markets directly. BOJ rate decisions and YCC tweaks produce 200-500 pip moves on announcement.
3. **Safe-haven flows.** JPY strengthens in global risk-off events because Japanese institutional investors hold massive offshore portfolios that get repatriated under stress. The pattern: SPX falls sharply -> JPY rallies versus USD -> USD/JPY drops 2-5%. This is structural and persistent.
4. **MoF intervention.** Japan's Ministry of Finance (the legal decision-maker; the [[bank-of-japan|BOJ]] acts as its agent in the market) has intervened directly to defend the yen multiple times since 2022, notably September 2022 (USDJPY ~146), October 2022 (~152), and April-May 2024 (~160). Intervention size has run $20-60B per episode, producing immediate 3-7 yen reversals followed by partial fade. The escalation ladder is predictable: officials first deploy **verbal intervention** ("watching with a high sense of urgency"), then **rate-checking** (calling dealers for quotes -- a near-certain warning), and only then **physical intervention**.

| Episode | Approx. USD/JPY level | Indicative size | Immediate effect |
|---------|----------------------|-----------------|------------------|
| Sep 2022 | ~146 | ~$20B | First yen-buying intervention since 1998 |
| Oct 2022 | ~152 (then ~150) | ~$37B | Sharp multi-yen reversals |
| Apr-May 2024 | ~160 (then ~152) | ~$60B+ | Largest monthly intervention on record at the time |

(Figures are the publicly reported approximations cited above; treat as indicative, not live.)
5. **Balance of payments.** Japan's traditional current-account surplus (driven by export earnings and net interest receipts on its $3T+ net foreign asset position) has narrowed since 2022 due to higher energy import costs and shifting trade patterns. A weaker BoP is a structural drag on the yen.

## Volatility Regimes

USD/JPY is structurally a **higher-vol pair than EUR/USD** and exhibits a sharply asymmetric distribution: long stretches of moderate vol punctuated by violent shocks.

| Regime | 1M Realized Vol (annualized) | Notes |
|--------|------------------------------|-------|
| Deep calm (e.g. mid-2018, parts of 2019, early 2025) | 5-7% | Rare and short-lived |
| Normal | 7-10% | Modal regime |
| Elevated (BoJ pivot, MoF intervention, Fed pivot) | 10-15% | Common during 2022-2024 cycle |
| Stress (carry unwind, financial crisis) | 18-30%+ | Rare but extreme |

The pair's defining feature is that it can *transition* from a 7% calm regime to 25%+ stress regime in a matter of hours when a positioning unwind hits. This is what happened on **August 5, 2024** -- see [[vix-august-2024-spike]].

**Regime shifters** worth flagging on the calendar:

- **BoJ policy decisions** (eight per year, with quarterly Outlook Reports). Higher idiosyncratic vol than ECB or Fed days for this pair.
- **FOMC decisions** -- material because of the rate-differential channel.
- **US CPI / NFP** -- transmits through the rate-differential channel.
- **MoF intervention windows.** When USD/JPY trades through psychological levels (150, 152, 155, 160), MoF officials begin verbal intervention, then physical intervention. Implied vol tends to spike *before* and *during* the intervention window.
- **Risk-off shocks.** [[vix-august-2024-spike|August 2024]] is the canonical recent example. [[gfc|2008]], [[swiss-franc-floor-removal|January 2015]], and the 2016 Brexit night also produced multi-yen yen rallies in hours.
- **Quarterly Tankan and BoJ Outlook Reports.**

## Options Market

USD/JPY options are the second-deepest FX options market after EUR/USD. They trade in three primary venues:

1. **OTC interbank** -- the deepest market. Tokyo and London are the active centers; New York provides 24-hour coverage. Standard tenors: 1W, 1M, 3M, 6M, 1Y, 2Y, with active trading in 5Y vol for structured-product hedges. Risk reversals and butterflies are quoted directly.
2. **[[cme-group|CME]] JPY/FX options on futures** (symbol: 6J options) -- listed, exchange-cleared. Note that CME quotes JPY futures as USD per JPY (inverse of the spot convention), which inverts the option payoff convention versus OTC.
3. **[[fxy-etf|FXY]] options** -- equity-listed options on the Yen Trust ETF. Lower notional, retail-accessible, useful for US-domiciled traders who want yen exposure inside an equity options account.

**Surface characteristics.** USD/JPY risk reversals exhibit a persistent **JPY-call (USD-put) skew** -- the market always pays more for downside-USD/JPY protection than upside, because the dominant tail in the pair is a sharp yen rally on a risk-off shock. Typical 1M 25-delta risk reversal: -0.5 to -1.5 vol points (yen-call premium). In stress regimes this can blow out to -3 to -5 vol points. This is the inverse of the equity-skew shape and reflects the genuinely different tail geometry of the pair.

Butterflies are also higher than EUR/USD's, reflecting the higher vol-of-vol embedded in the carry-unwind risk.

**Carry-vol nexus.** USD/JPY is *the* canonical carry-vol pair. The structural trade is: **long USD/JPY (earning the rate differential) + short USD/JPY downside vol (selling yen-call premium)**. This works in every calm regime and blows up in every stress regime -- a classic short-vol-plus-carry profile that is mathematically equivalent to selling earthquake insurance in a quake-prone zone. The [[yen-carry-trade]] page describes the macro version of this trade; the options version embeds it directly into a vol surface position.

For a serious trader, **buying** USD/JPY downside vol (long yen calls or USD/JPY puts) is one of the cleanest cross-asset tail hedges available. It is positively correlated with [[vix-futures|VIX]] spikes, with yen rallies, and with equity drawdowns simultaneously. The carry cost of holding it is the negative variance risk premium plus the time decay -- typically 1-2% per month on 1M ATM-equivalent positions in calm regimes.

## Concentration-Risk Angle

USD/JPY vol provides genuine diversification from equity vol *most of the time*, but with an important and subtle correlation regime that traders must understand.

**The USD/JPY-equity correlation story:**

- **Carry-on regimes** (calm tape, low VIX, dollar uptrend). USD/JPY rises as carry trades accumulate, often **positively correlated with SPX** (both up together). USD/JPY 1M vol stays compressed, equity vol stays compressed. The pair acts like a *risk-on* asset.
- **Carry-unwind regimes** (vol spike, equity drawdown, JPY rally). USD/JPY collapses as carry positions liquidate; equities fall; USD/JPY 1M vol explodes; equity vol explodes. The pair acts like a *risk-off* shock asset, and **the correlation between USD/JPY and SPX flips negative** during these episodes.

This regime-switching correlation has profound implications for [[options-concentration-risk|options concentration risk]] in a multi-asset book:

1. In calm regimes, short USD/JPY vol and short SPX vol are *partially* correlated (both earn carry, both decay), so they don't diversify much.
2. In stress regimes, **the FX leg can blow up faster and harder than the equity leg**, because JPY repatriation flows are concentrated and reflexive, and because BOJ/MoF policy uncertainty amplifies the move.
3. Long USD/JPY downside vol is therefore one of the best-defined tail hedges available: it pays in essentially every scenario where equity vol pays, often by larger multiples on a vega-normalized basis.

**The August 2024 yen-carry unwind is the canonical recent example.** See [[vix-august-2024-spike]] for the full sequence. Compressed summary: USDJPY ran from ~162 in mid-July 2024 to ~141.7 intraday on August 5, a ~13% move in three weeks, with most of the violent leg compressed into 12 hours. SPX fell -8.5% peak-to-trough over the same window. Spot VIX printed near 65 intraday. **Retail short-strangle accounts on equities lost 40-90% of equity** -- not because they had explicit USDJPY exposure, but because the JPY-funded carry positioning unwound through equity markets via dealer short-gamma feedback. The lesson: a pure equity short-vol book *was implicitly short USD/JPY downside vol* via the global carry network, even if the trader never traded a yen option in their life.

For a deliberately constructed multi-asset short-premium book, a 10-20% USD/JPY-vol allocation alongside equity vol gives meaningful diversification *and* makes the implicit exposure explicit so it can be sized and hedged. A long USD/JPY downside vol overlay (e.g., a 1M 25-delta yen call) sized at 2-5% of vega budget is a high-payoff tail hedge.

## Liquidity

USD/JPY is liquid 24/5, with the deepest windows being the Tokyo morning (0000-0300 UTC) and the London-New York overlap (1300-1700 UTC). Spot bid-ask spreads run 0.5-1 pip on top-of-book in calm tape (where 1 pip = 0.01 yen), widening dramatically to 5-20 pips in MoF intervention windows or carry-unwind sessions. CME futures (6J) spreads are typically 1-2 ticks. FXY options spreads on liquid strikes are typically 0.02-0.10 USD wide.

The pair's overnight liquidity is materially worse than EUR/USD's, particularly during the Sunday-Monday session boundary -- which is exactly when carry unwinds tend to ignite (as on August 5, 2024). Stop-loss orders placed in the Tokyo opening window can fill several yen worse than the screen price during stress events.

## Session Behaviour

Unlike [[eurusd]], USD/JPY is genuinely a 24-hour pair with meaningful flow in every session, because Japanese institutional activity anchors the Asia window:

- **Tokyo session (~0000-0800 UTC).** The deepest yen window. The 0855 Tokyo-time *Gotobi* fixing (the 5th/10th-of-the-month corporate fixing) and exporter/importer hedging flows shape the morning. This is also where MoF intervention and verbal warnings most often appear.
- **London session (~0700-1600 UTC).** European desks add directional flow; macro positioning and cross-JPY (EUR/JPY, GBP/JPY) flows transmit into USD/JPY.
- **London-New York overlap (~1300-1700 UTC).** The most liquid window. US data (CPI, NFP) and the FOMC calendar drive the rate-differential channel here.
- **Sunday-Monday boundary.** The thinnest, most dangerous window — carry unwinds historically ignite here (e.g. the night before August 5, 2024) when liquidity is minimal and gaps are largest.

## How It's Traded

USD/JPY is accessed through the same instrument stack as other majors, with a few JPY-specific quirks:

- **Spot FX.** Interbank spot settling [[t-plus-2|T+2]]. Retail access via brokers; institutions via ECNs with Tokyo and London as the active centers. Standard lot is 100,000 USD.
- **Pip mechanics.** Because JPY is quoted to 2-3 decimals, a *pip* is 0.01 yen (the 2nd decimal), and a fractional pip is the 3rd decimal. On a standard 100,000-USD lot, one pip is worth ~1,000 JPY (~$7 at USDJPY=140). Note the pip definition differs from four-decimal pairs like EUR/USD.
- **Futures.** [[cme-group|CME]] JPY futures (symbol 6J, plus the micro contract) are quoted as **USD per JPY** — the inverse of the spot convention — which flips the option and directional payoff convention versus OTC. Traders must account for this inversion.
- **Options.** OTC interbank options, [[cme-group|CME]] listed options on 6J futures, and [[fxy-etf|FXY]] equity-listed options — covered in the Options Market section above. Long USD/JPY downside vol (yen calls) is a premier cross-asset tail hedge.
- **Carry and forwards.** USD/JPY is *the* canonical [[carry-trade|carry]] funding pair: borrow low-yield yen, hold high-yield dollars. The [[yen-carry-trade]] page covers the macro version; the [[interest-rate-differential|rate differential]] is the engine and the source of carry-unwind risk.

## Crosses and Related Spreads

USD/JPY rarely trades in isolation; it sits at the center of a web of yen crosses and rate-differential spreads that traders use to express more precise views:

| Pair / spread | What it isolates | Trading note |
|---------------|------------------|--------------|
| EUR/JPY | Euro-yen carry and risk sentiment | Highest-beta yen cross; amplifies USD/JPY moves in risk-off |
| GBP/JPY ("the Dragon") | High-vol carry cross | Notoriously violent; favored by carry and momentum traders |
| AUD/JPY | The purest **risk-on/risk-off barometer** | Long-time proxy for global carry appetite; AUD is a high-yielder, JPY the funder |
| 10y UST-JGB yield spread | The rate-differential engine | Cleanest leading indicator for USD/JPY direction (see Macro Drivers) |
| USD/JPY vs [[us-dollar\|DXY]] | Idiosyncratic yen vs broad dollar | Decompose how much of a move is "yen" vs "dollar" |
| FX vol spread (USD/JPY vol minus [[eurusd]] vol) | The yen vol premium | USD/JPY structurally carries a richer vol surface than EUR/USD |

A key structural relationship: because the yen funds carry trades against many high-yielders simultaneously, a USD/JPY carry unwind is rarely contained to USD/JPY -- it propagates through **every** yen cross at once (the [[yen-carry-trade]] is a multi-currency network, not a single pair). This is what makes the crosses move in lockstep during stress and what amplified the [[vix-august-2024-spike|August 2024 unwind]].

## Correlations and Cross-Asset Relationships

USD/JPY's correlations are regime-dependent, which is the single most important thing for a trader to internalize:

- **Regime-switching correlation with [[sp500|SPX]].** Positive in carry-on regimes (both rise together), sharply negative in carry-unwind regimes (yen rallies as equities fall). See the Concentration-Risk Angle above.
- **Positive with the [[us-dollar|DXY]] (USD-base).** A broad dollar rally lifts USD/JPY, the opposite sign to [[eurusd]].
- **Tracks the UST-JGB yield spread.** The 10y UST-JGB differential is the cleanest leading indicator; when it widens, USD/JPY tends to rise.
- **Inverse to [[gold]] and to the [[vix-futures|VIX]] in stress.** When VIX spikes and gold bids in a risk-off, the yen rallies and USD/JPY falls.
- **Cross-JPY transmission.** EUR/JPY and GBP/JPY flows feed into USD/JPY; a sharp move in a cross-JPY pair often pulls USD/JPY with it.

## Risks for Traders

- **Carry-unwind / gap risk.** The defining risk. USD/JPY can drop several yen in hours when leveraged carry positions liquidate, often in thin Sunday-Monday liquidity. Stops slip badly. See [[vix-august-2024-spike]] and [[yen-carry-trade]].
- **Intervention risk.** Japan's Ministry of Finance intervenes directly to defend the yen — episodes in 2022 and 2024 produced immediate 3-7 yen reversals on $20-60B of buying. Being short yen into a stretched, above-150 level carries asymmetric intervention risk; implied vol spikes before and during these windows.
- **BOJ policy reflexivity.** [[bank-of-japan|BOJ]] rate decisions and [[yield-curve-control|YCC]] tweaks produce 200-500 pip moves on announcement and can re-rate the entire carry trade.
- **Asymmetric tail (short-vol trap).** The structural long-USD/JPY-plus-short-downside-vol trade earns steadily then loses catastrophically — mathematically equivalent to selling earthquake insurance. Position with explicit tail awareness.
- **Leverage risk.** As with all FX, high retail leverage magnifies the percentage P&L of even modest spot moves. See [[risk-management]] and [[leverage]].

## Related

- [[forex]] -- parent market
- [[us-dollar]] -- the base currency
- [[bank-of-japan]] -- monetary authority for the yen
- [[federal-reserve]] -- monetary authority for the dollar
- [[eurusd]] -- the other major FX vol pair, lower-vol counterpart
- [[options-concentration-risk]] -- where FX vol fits in a multi-asset book
- [[carry-trade]] -- broader strategy class
- [[yen-carry-trade]] -- the specific JPY-funded version
- [[vix-august-2024-spike]] -- canonical recent unwind episode
- [[implied-volatility]] -- foundational concept
- [[fxy-etf]] -- retail equity-options proxy
- [[cme-group]] -- listed-options venue
- [[interest-rates]] -- the dominant macro driver
- [[yield-curve-control]] -- BOJ-specific policy framework

## Sources

- BIS Triennial Central Bank Survey 2022 -- daily FX turnover and pair rankings.
- BoJ Outlook Reports and policy statements 2022-2024 -- the YCC and rate-pivot context.
- Japan Ministry of Finance public statements on FX intervention 2022-2024.
- [[vix-august-2024-spike]] -- the wiki's case study of the most recent JPY-funded carry unwind and its transmission to equity vol.
- [[options-concentration-risk]] -- the framework for placing FX vol in a multi-asset book.
