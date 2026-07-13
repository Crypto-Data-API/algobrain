---
title: "Melvin Capital"
type: entity
created: 2026-04-06
updated: 2026-05-07
status: good
tags: [hedge-funds, short-selling, history, stocks, options, risk-management, derivatives]
entity_type: fund
founded: 2014
headquarters: "New York, USA"
related: ["[[gamestop-short-squeeze]]", "[[short-selling]]", "[[short-interest]]", "[[float]]", "[[gamma-squeeze]]", "[[options-concentration-risk]]", "[[risk-of-ruin]]", "[[citadel]]", "[[robinhood]]", "[[reddit]]", "[[r-wallstreetbets]]", "[[point72]]", "[[sac-capital]]", "[[gabe-plotkin]]"]
---

Melvin Capital Management was a long/short equity [[hedge-funds|hedge fund]] founded by Gabe Plotkin in 2014, named after his late grandfather, that became the most prominent casualty of the January 2021 [[gamestop-short-squeeze]]. The fund's destruction is the canonical modern case study for [[options-concentration-risk]], crowded short positioning in low-[[float]] names, and reflexivity between options flow and underlying price — and the lessons it teaches are now standard reference material for any options or short-biased trader.

## Founding and Pre-GME History

Plotkin spent roughly a decade as a portfolio manager at Steve Cohen's [[sac-capital|SAC Capital]] (later [[point72]]), running a consumer-discretionary book that was widely regarded as one of the best on the platform. He launched Melvin in late 2014 with approximately $1 billion in seed capital — including a substantial allocation from Cohen — and the fund's initial mandate was tightly aligned with his SAC pedigree: long/short equity, bottom-up fundamental, concentrated in consumer and retail names where Plotkin's edge was deepest.

Returns in the first years were exceptional. Melvin reportedly compounded at over 30% net annually through 2020, ending that year up roughly 50% on the back of the COVID-era consumer rotation. By the end of 2020 the fund managed approximately $12.5 billion in assets and was viewed as one of the top performing hedge funds on the Street. Plotkin had a reputation as a disciplined risk manager — which made the magnitude of the GME blow-up the following month all the more striking.

## The GameStop Short — Why It Was Crowded

Melvin held a large short position in GameStop (GME) as part of a broader bet on secular decline in brick-and-mortar retail. By late 2020 the position was no longer unique: GME was the most heavily shorted name in the Russell 3000 by [[short-interest]] as a percentage of [[float]], with reported short interest exceeding **140% of the public float** — meaning more shares had been borrowed and sold short than actually existed in tradable form, a situation enabled by the mechanics of [[securities-lending]] and [[rehypothecation]].

Several structural risk factors were stacked on the same trade:

- **Crowding.** Numerous funds held the same short on similar fundamental theses; unwinds would have to compete for the same shares.
- **Low float.** GME's tradable share base was small, so any forced buying produced disproportionate price impact.
- **Borrow cost regime.** As demand to short the name persisted, the [[stock-borrow|cost to borrow]] rose into the high double digits annualized — a leading indicator that the trade was already saturated.
- **Concentration relative to fund size.** While Melvin disclosed the position only via [[13f|13F]] put-option holdings rather than direct short equity, the GME short was reportedly one of the fund's largest exposures by gross risk.

## The Squeeze — Mechanics

The January 2021 squeeze was not a pure equity short squeeze. It was an *options-flow-driven* event in which the [[gamma-squeeze]] dynamic acted as the accelerant on top of the underlying short cover. The mechanism (see also [[gamestop-short-squeeze]] for full timeline):

1. **Retail call buying on [[reddit|r/WallStreetBets]].** Thousands of retail traders coordinated on [[r-wallstreetbets|r/WallStreetBets]] to buy short-dated, out-of-the-money GME [[call|calls]]. This was concentrated, simultaneous, and concentrated in strikes the dealers were not naturally long.
2. **Dealer [[delta-hedging]].** The market makers who sold those calls had to buy GME shares to hedge their negative delta. As the stock rose, the delta of the calls increased, forcing the dealers to buy *more* shares — the [[gamma-squeeze]] feedback loop.
3. **Forced short cover.** As GME rallied, short sellers (Melvin among them) faced rising mark-to-market losses and rising borrow costs. Their margin lenders forced them to cover. Cover buying = more upward pressure.
4. **Reflexivity.** The position itself became part of the catalyst. The story of Melvin's losses — leaked into the press — drew more retail attention and more call buying. The squeeze fed itself.

The critical point for options traders: the [[gamma-squeeze]] amplified the equity move by an order of magnitude relative to what the underlying short interest alone could have produced. Dealer hedging is mechanical — they have no choice — and that mechanical buying is what turns a normal short squeeze into a parabolic move.

## The Losses — Concrete Numbers

- **January 2021: −53%.** Melvin lost approximately $6.8 billion in the single calendar month of January 2021, representing roughly 53% of its assets.
- **January 25, 2021: $2.75 billion emergency capital injection.** [[citadel]] (and its principals) plus [[point72]] injected $2.75 billion in fresh capital to keep Melvin solvent through the squeeze. The terms were widely reported as expensive — passive minority equity in the management company plus revenue share — and they did not include risk-managing decisions.
- **2021 full year: roughly −39%.** Even after a partial recovery in February and the rest of the year, Melvin finished 2021 down nearly 40% net.
- **2022: −21%** through the first four months as macro losses continued.
- **May 2022: fund closure announced.** Plotkin announced he would wind down the fund and return capital. He had attempted to launch a successor vehicle with reduced fees in early 2022, but withdrew the plan after investor backlash.

The fund went from $12.5 billion AUM and a top-tier reputation to closure in roughly 16 months.

## Lessons for Options and Short Traders

The Melvin episode is now a standard case study because it concentrates several distinct lessons that all materialized in the same trade:

### 1. Crowded shorts in low-float names are a tail-risk concentration

A short with [[short-interest]] >100% of [[float]] is not a normal short — it is a [[options-concentration-risk|stacked-risk]] position. Even if the fundamental thesis is correct, the path-dependent risk of a forced unwind can wipe the trade out before fundamentals matter. Borrow cost is the price tag the market is putting on that tail; ignore it at your peril.

### 2. Options flow can amplify equity moves through dealer hedging

A pure equity short ignores the [[gamma-squeeze]] dimension. Once retail or coordinated call-buying meets a low-float name with stretched short interest, dealer [[delta-hedging]] becomes the dominant marginal buyer, and price moves go non-linear. Any short trader holding through expiry weeks in heavily optioned names is implicitly short the dealer hedge.

### 3. Borrow cost is a leading indicator

When [[stock-borrow|borrow cost]] hits triple-digit annualized rates, the trade is structurally over even if the fundamental thesis is intact. The carry is now negative enough that a flat tape produces losses, and any squeeze immediately blows past stop levels. Melvin's GME borrow was reportedly running at extraordinary rates by late 2020.

### 4. Reflexivity — the position itself becomes part of the catalyst

When a fund's short is well-known and large enough to be tracked publicly (via 13Fs, leaked prime-broker chatter, or media reporting), the fund itself becomes the catalyst. Adversaries can target the position with the explicit intent of triggering a forced cover. This is a new microstructure regime; it did not exist at scale before social-media coordination.

### 5. Social-media-coordinated retail flow is a real microstructure regime

The [[r-wallstreetbets|r/WallStreetBets]] coordination is not a one-off. AMC, BBBY, KOSS, and a dozen subsequent names showed that coordinated retail option buying is a recurring market regime, not a quirk of January 2021. Risk frameworks built before 2020 systematically underweight this factor.

### 6. Fund-level [[risk-of-ruin]] from a single name

A 53% drawdown in one month from a single name on the short side violates virtually every traditional sizing rule. Melvin's risk system reportedly used [[var|VaR]] and stress-test frameworks that did not capture the gamma-amplified scenario. The lesson is structural: any sizing that does not stress-test for *non-linear* outcomes in concentrated short or short-vol positions is incomplete.

### 7. Emergency capital does not save a brand

The Citadel/Point72 capital kept Melvin solvent but did not restore investor confidence. Once a fund is publicly associated with a binary squeeze loss, redemptions follow regardless of the recovery path. The reputational damage is a separate, quasi-permanent loss event distinct from the trading loss.

## Connection to Wiki Concepts

- [[options-concentration-risk]] — Melvin's GME short is the textbook illustration of stacked-risk in a single name (short equity exposure + options-flow tail + borrow cost regime + reputation risk all on one ticker).
- [[risk-of-ruin]] — A 53% single-month drawdown from a single position is the modern reference point for what "ruin" looks like at an institutional scale.
- [[gamma-squeeze]] — The accelerant on the GME move; understanding this mechanism is the key takeaway for options traders.
- [[short-interest]] / [[float]] — When the ratio exceeds 100%, the structural setup for a forced unwind is mathematically present.
- [[reflexivity]] — Soros's concept applied to a fund's own visibility as a market catalyst.

## Trading Relevance

Melvin Capital is no longer an active fund, but the case is studied because it concentrates the modern options-flow / short-equity / social-coordination regime into a single, well-documented event. For options traders specifically, the lesson is that the *underlying* and the *option chain* are not separable risks in heavily-optioned names — they are coupled through dealer hedging, and any short or short-vol position must price the gamma feedback loop explicitly.

## Sources

- (Source: [[gamestop-short-squeeze]]) — Full event timeline, Robinhood restrictions, Congressional hearings
- (Source: [[gamma-squeeze]]) — Mechanics of the dealer-hedging feedback loop
- Public reporting on Melvin's January 2021 losses, Citadel/Point72 capital injection, and May 2022 closure announcement
