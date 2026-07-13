---
title: "Raj Malhotra"
type: entity
created: 2026-04-07
updated: 2026-05-07
status: good
tags: [traders, person, itpm, options, volatility, vix, risk-management]
entity_type: person
aliases: ["Rajesh Malhotra"]
related: ["[[itpm]]", "[[anton-kreil]]", "[[options]]", "[[volatility]]", "[[vix]]", "[[vix-futures]]", "[[implied-volatility]]", "[[long-vol-vs-short-vol]]", "[[options-concentration-risk]]", "[[itpm-trading-philosophy]]", "[[bank-of-america]]", "[[nomura]]", "[[wharton]]"]
---

Raj Malhotra is a former managing director and head of institutional [[options]] trading at [[bank-of-america]], later head of US options at [[nomura]], and a senior trading mentor at the [[itpm|Institute of Trading and Portfolio Management]]. His career spanned three continents over roughly fifteen years on the sell side, and he is best known within the ITPM ecosystem for his "Trading the Big Swinging VIX" methodology and for the Trading Legends interview in which he explains why retail traders systematically misread [[volatility]] (Source: [[itpm-trading-legends-raj-malhotra]]).

## Background and Path to ITPM

Malhotra began trading in high school using Lotus 1-2-3 spreadsheets — pre-Excel, pre-online-broker, manually entering price data and computing positions on his own. He went to the [[wharton|Wharton School of Business]] at the University of Pennsylvania, graduating in 1998. After graduation he joined a [[bnp-paribas]]-owned hedge fund trading S&P 500 index options, moving to its New York office in 2000 (Source: [[itpm-trading-legends-raj-malhotra]]).

In 2002 [[bank-of-america]] hired him as head of index options. By 2006 he was head of all institutional options trading at the firm, and made managing director before the age of 30 — a progression he describes as "unheard of" on a sell-side options desk. He left BofA in 2009 after the Merrill Lynch merger (in which Bank of America Securities personnel were largely made redundant in favour of Merrill staff), and moved his entire team to [[nomura]] to help launch the bank's US presence. He retired from sell-side trading in 2012 after roughly three years at Nomura, and subsequently joined ITPM as a Senior Trading Mentor specializing in options and volatility (Source: [[itpm-trading-legends-raj-malhotra]]).

## "Trading the Big Swinging VIX" Methodology

Malhotra's premium ITPM presentation, *Trading the Big Swinging VIX*, is a vol-trader's framework rather than a directional retail recipe. Its central propositions, reconstructed from the Trading Legends interview and the surrounding ITPM curriculum:

- **VIX is a price, not a fear gauge.** It is the market's clearing price for 30-day [[implied-volatility]] on S&P 500 options. Like any price, it can be cheap or expensive relative to what it is forecasting — and that judgment cannot be made by looking at the level alone.
- **Trade the regime, not the level.** The methodology operates in two distinct regimes: vol expansion (after a shock, when [[vix]] is rising and term structure is in [[backwardation]]) and vol compression (post-shock mean reversion, when contango is steep and [[vix-futures]] are bleeding theta). Position structure differs sharply between the two.
- **Use [[vix-futures]] and term-structure shape, not spot VIX.** Spot VIX is not directly tradable. The trade is constructed on the futures curve, where [[contango-and-backwardation]] do most of the P&L work over time.
- **Avoid catalysts you do not have an edge on.** The methodology explicitly avoids selling vol into [[fomc-meetings|FOMC]] decisions, NFP, earnings season concentrations, or pre-known geopolitical events without an asymmetric structure — these are precisely where the realized vs. implied gap is most likely to close violently against a short-vol position.

The methodology is best understood as the [[long-vol-vs-short-vol]] decision applied to the index complex, with explicit rules for when to be on each side rather than a structural bias.

## Lessons from the Trading Legends Interview

The Trading Legends sit-down with [[anton-kreil]] in New York covers Malhotra's career and is unusually concrete about how a professional vol trader actually thinks. Lessons can be grouped into four buckets (Source: [[itpm-trading-legends-raj-malhotra]]):

### Volatility regime detection

- **"Low is not cheap. High is often cheap."** Malhotra's signature framing: when [[volatility]] is low, options are usually *expensive* relative to what is about to happen, because the market has already priced in calm. When vol is high, options are often *cheap* relative to the realized turbulence ahead. This is the inverse of how most retail traders think about option premium.
- **Vol has momentum, like stocks.** Buy vol when it is going up, sell vol when it is going down — same directional principle. Buying vol simply because the level looks "low" is one of the most expensive retail mistakes, because you bleed [[theta]] while the regime persists.
- **Cross-asset signal beats single-asset signal.** At Bank of America, weekly cross-product risk meetings with mortgages, structured credit, and rates desks gave the equity options desk early warning before the equity tape itself broke. The equity market is "almost the last one to see the cracks." For a retail trader, this argues for explicitly watching credit spreads, [[move-index|MOVE]], and FX vol alongside [[vix]].

### Preparation and idea generation

- **Worldview first, ticker last.** Start with a top-down read on what is changing in the world — what consumer behaviours, what apps, what supply chains — then identify the sectors that benefit, and only then drill into individual names. Use options to *express* that view with leverage and limited downside, not as standalone mispricing trades.
- **Look down the value chain for second-derivative beneficiaries.** If Apple says it will sell more iPhones, the obvious trade (long AAPL) is already in the price. The component, battery, and supplier names two steps down the value chain are where the asymmetric setups live.
- **Trade only what you understand.** Both Malhotra and his ITPM colleagues stress this: the universe of stocks is large enough that there is no reason to take positions in companies or sectors you cannot describe in plain language.

### Position sizing and risk

- **Use options to express stock views, not to chase mispricings.** Most listed options are reasonably efficiently priced; the edge is rarely in the option itself. The edge is in having the right stock view and using the option structure to get convex payoff with bounded downside.
- **Cross-asset awareness limits drawdown.** The 2006-2008 experience at BofA taught him that the desks that survived were the ones that had been listening to other asset classes. Single-asset traders blew up; cross-asset listeners de-risked early.

### Mistakes to avoid

- **Greed kills hedges.** First market lesson he ever observed: an executive's wife held ~200,000 shares at $220 and was offered a [[collar]] with a $150 [[put|put]] floor that locked in roughly $30 million. She let it expire waiting for the stock to retrace. The stock went to zero. The lesson is not "always hedge" — it is "do not unwind a hedge because you got greedy after it was already on."
- **Overtrading on catalysts is a tax.** Trading earnings, [[fomc-meetings|FOMC]] decisions, and other scheduled catalysts without a genuine edge means you are paying [[implied-volatility]] crush in exchange for a coin flip. The market has already priced the event.
- **Doing no research is the most expensive shortcut.** Most retail blow-ups trace to taking positions in names the trader cannot describe at the business-model level.

## Volatility as an Asset Class

A recurring theme in Malhotra's ITPM work is that professional [[volatility]] traders see options as exposure to a separate asset class, not as a leveraged proxy for the underlying:

- The professional asks "what is the [[implied-volatility|implied vol]] vs. [[realized-volatility|realized vol]] gap, and which side am I on?" before asking direction.
- Retail asks "is the option cheap?" by looking at the absolute premium or the absolute level of [[vix]] — both of which are nearly meaningless without the regime context.
- The asset-class framing means a vol portfolio has its own [[vega]], [[gamma]], and [[theta]] budgets, sized independently of equity directional risk. See [[vega-budgeting]] and [[options-portfolio-construction]] for the operational framework that ITPM teaches around this insight.

## Connection to ITPM Philosophy

Malhotra's vol-regime framing maps directly onto the broader [[itpm-trading-philosophy]]:

- **[[capital-preservation]] first.** Avoiding short-vol positions in low-vol regimes is the same instinct as Kreil's "do not sell premium when premium is cheap." Both are versions of refusing to take negatively convex bets at the wrong price.
- **[[asymmetric-risk-reward]].** Using options to express directional views with bounded downside is the structural payoff Kreil and Malhotra both insist on — a long [[call|call]] or [[put|put]] is the cleanest possible asymmetric structure.
- **80% fundamental / 20% technical.** Worldview-first idea generation is identical to the [[itpm-five-principles|five principles]] taught in the core program; Malhotra simply layers an options/vol overlay on top of the same fundamental view.

## Trading Relevance

Malhotra is the cleanest example in the ITPM ecosystem of a *sell-side options trader* perspective, complementary to [[anton-kreil]]'s buy-side directional view and [[chris-quill]]'s quantitative volatility lens. His relevance is highest for:

- Retail traders who already understand directional equity trading and want to add a [[long-vol-vs-short-vol]] overlay
- Traders evaluating [[vix-futures]] structures, [[vix-etps|VXX-style ETPs]], or term-structure trades
- Anyone whose [[options-concentration-risk|options book is concentrated]] in short premium and needs an explicit framework for when that bet is profile-appropriate

## Sources

- (Source: [[itpm-trading-legends-raj-malhotra]]) — Trading Legends interview with Anton Kreil covering career, financial-crisis experience, and volatility-regime framework
- (Source: [[itpm-education-methodology-overview]]) — Mentor profile context within the ITPM program structure
