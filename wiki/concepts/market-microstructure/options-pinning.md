---
title: "Options Pinning"
type: concept
created: 2026-05-07
updated: 2026-06-11
status: good
tags: [options, market-microstructure, derivatives, behavioral-finance]
aliases: ["Options Pinning", "Strike Pinning", "Pin Effect", "Max Pain Effect", "Pinning"]
related: ["[[index-options]]", "[[spx-options]]", "[[spy-options]]", "[[pin-risk]]", "[[max-pain]]", "[[dealer-gamma-hedging]]", "[[market-makers]]", "[[am-vs-pm-settlement]]", "[[soq-settlement]]", "[[zero-dte-options]]", "[[gap-risk]]", "[[liquidity-evaporation]]", "[[gamma-explosion]]", "[[volmageddon]]", "[[gamestop-saga]]", "[[options-portfolio-construction]]", "[[options-risk-budgeting]]", "[[variance-risk-premium]]"]
domain: [market-microstructure, options, behavioral-finance]
prerequisites: ["[[options-greeks]]", "[[dealer-gamma-hedging]]"]
difficulty: intermediate
---

**Options pinning** (also "strike pinning") is the empirical phenomenon that the closing prices of optionable underlyings cluster at strike prices on options expiration days — far more often than the underlying's normal return distribution would predict. The effect is distinct from [[pin-risk|pin risk]], which is the position-level uncertainty a trader holding a near-the-money short option faces post-close; pinning is the *spot phenomenon* that creates the conditions for pin risk. The mechanism is dealer gamma hedging: when market makers are net long gamma at high-open-interest strikes (because the public is net short), their delta-rebalancing flow creates a mean-reverting force toward the dominant strike in the final hours of the trading session. Pinning was first documented academically by Ni, Pearson, and Poteshman (2005) for individual stocks and by Golez and Jackwerth (2012) for index futures; it has weakened materially since the 2022 explosion of [[zero-dte-options|0DTE options]] flows redistributed gamma across the strike grid.

## Overview

The textbook model of expiration is symmetric: an underlying ends "wherever it ends," strikes are arbitrary reference points, and the closing price has no special relationship to the strike grid. Reality is asymmetric. On expiration days for liquid optionable equities and indices, the closing price clusters at integer-multiple strikes (for stocks priced under $50) or $5 / $10 multiples (for higher-priced names) at materially elevated frequency relative to non-expiration days. The clustering disappears (or sharply attenuates) the trading day after expiration.

Two related but distinct concepts often get conflated:

| Concept | Meaning | Page |
|---|---|---|
| **Options pinning** | Empirical clustering of underlying prices at strikes on expiration | this page |
| **[[pin-risk\|Pin risk]]** | Position-level uncertainty when an underlying closes near a short option's strike | [[pin-risk]] |
| **[[max-pain\|Max pain]]** | The strike at which the most options expire worthless across the open-interest distribution | [[max-pain]] |

The pinning phenomenon is real, measurable, and has been replicated across multiple decades and asset classes. The "max pain" theory is a heuristic claim about *where* pinning aims; the empirical pinning effect is the underlying clustering whether or not max pain happens to be the focal strike.

## Mechanism / How It Works

### Dealer gamma hedging and the restoring force

The standard explanation is the **dealer-gamma-hedging mechanism** (see [[dealer-gamma-hedging]]):

1. **Public is net short premium near expiration.** Retail and many institutional flows tend to be **short** the near-the-money expiring options at high-OI strikes, particularly on expiration day itself. Covered calls, cash-secured puts, weekly income strategies, and short strangles all contribute.
2. **[[market-makers|Market makers]] are net long gamma** at those strikes by construction — they took the other side of the public's selling.
3. **A long-gamma position is delta-hedged by buying low and selling high.** As spot rises toward the strike, the dealer's call delta increases, and they sell stock to neutralize. As spot falls back toward the strike from above, delta decreases, and they buy stock. The same applies on the put side, mirrored.
4. **Aggregate dealer flow becomes mean-reverting toward the high-OI strike.** Across all dealers and all clients, the hedging flow generates buy pressure when spot is below the strike and sell pressure when spot is above — a literal restoring force toward the strike.
5. **The force grows as expiration approaches.** Gamma scales as 1/√(T) for at-the-money options, so the closer to expiration and the closer to the strike, the larger the per-share hedging flow per unit of spot move. By the final hour, hedging flow can dominate the underlying's order book.

The mechanism predicts pinning should be strongest:

- On expiration day itself, especially in the final hour.
- At strikes with the largest open interest.
- For underlyings where market makers are clearly net long gamma (i.e., when the public has been net selling expiring premium).
- For underlyings with large optionable volume relative to the underlying's stock volume (so dealer hedging is a meaningful fraction of total flow).

It also predicts pinning should *weaken* when:

- Dealers are net short gamma (e.g., during certain gamma squeezes when public flow has flipped to net long), at which point hedging is mean-amplifying rather than mean-reverting.
- Open interest is spread across many strikes rather than concentrated.
- The underlying's stock volume dwarfs option volume, drowning out the hedging signal.

### Why "max pain" is an imperfect proxy

The max-pain theory says the underlying drifts toward the strike that minimizes total payoff to long option holders (i.e., maximizes worthless expirations). This is *correlated* with where dealer gamma is concentrated — because public-short, dealer-long positions cluster at strikes that ultimately expire worthless when the underlying pins — but the correlation isn't perfect. A high-OI strike where market makers happen to be *short* gamma (e.g., dealers wrote calls into a retail squeeze) won't pin even if max-pain math says it should. Max pain is a useful first-order proxy; the true mechanism is the gamma sign at the strike, not the OI count alone.

### Distinction from gamma squeezes

A **gamma squeeze** is the opposite phenomenon: when dealers are net *short* gamma at a strike, hedging amplifies moves rather than dampening them. As spot rises toward and through a high-OI strike where dealers are short gamma (because public is long calls), dealers buy more and more stock to delta-hedge, accelerating the move. Gamma squeezes are anti-pinning: they push spot *through* strikes, not toward them. The 2021 GME and AMC episodes showed both phases: pinning at certain expirations early in the squeeze, gamma squeeze acceleration on the high-volume call-buying days.

## Empirical Evidence / Examples

### Ni, Pearson, and Poteshman (2005) — the foundational study

The canonical academic reference: Ni, S. X., Pearson, N. D., and Poteshman, A. M. (2005), *Stock Price Clustering on Option Expiration Dates*, *Journal of Financial Economics* 78(1): 49-87. Findings:

- **On monthly expiration Fridays, optionable US stocks closed at integer-multiple strikes ($5 multiples) about 16-17% of the time, vs. roughly 14% for non-expiration days** — a small but highly statistically significant excess.
- The pinning effect was **larger for stocks with greater open interest** in expiring options, and absent for non-optionable stocks (used as a control).
- The effect was **stronger when retail and proprietary trader flows pointed in directions consistent with the dealer-gamma mechanism** (i.e., when dealers were inferred to be net long gamma at the dominant strike).
- The authors estimated that **dealer hedging alone** could explain a significant fraction of the observed clustering, with non-hedging-related explanations (manipulation, sentiment) contributing the remainder.

This paper essentially established options pinning as a real, structural, non-anomalous market microstructure feature.

### Golez and Jackwerth (2012) — extension to index futures

Golez, B. and Jackwerth, J. C. (2012), *Pinning in the S&P 500 Futures*, *Journal of Financial Economics* 106(3): 566-585. Found:

- The S&P 500 e-mini futures contract pinned to round-number strikes on monthly OPEX Fridays, even though SPX-options settlement is on the cash index, not on the futures.
- The mechanism appeared to be cross-product hedging: dealers running SPX-options books hedged their delta with SPX e-mini futures, producing the same gamma-hedging restoring force in the futures market that Ni-Pearson-Poteshman documented in cash equity markets.
- The effect was strongest in the final hour of trading on Thursdays (the SPX monthly options stop trading Thursday afternoon for AM SOQ settlement — see [[soq-settlement]]).

### AAPL — the textbook pinner

[[apple|Apple]] has been the textbook example of an individual-stock pinning case for over a decade. In the post-2015 sample of monthly expirations:

- AAPL closed within $0.50 of a $5-multiple strike on more than 60% of monthly expirations.
- The unconditional probability for that interval, given AAPL's typical daily range, would be closer to 35-40%.
- The clustering was concentrated at strikes with the largest weekly + monthly OI, consistent with the Ni-Pearson-Poteshman mechanism.

### NFLX historically (2010s) and other retail-favorite single names

Netflix, during its 2012-2017 period as a retail-favorite, showed pronounced pinning to $5 strikes on monthly expirations. As 0DTE and weekly OI grew across the option chain, the pinning effect weakened — consistent with the prediction that gamma diffusion weakens pinning.

### GME during the 2021 meme-stock period (a complicated case)

[[gamestop-saga|GameStop]] in early 2021 showed both pinning and anti-pinning depending on the week:

- On expirations where retail had been net *short* expiring premium (early in the squeeze), classical pinning appeared at high-OI strikes.
- On the weeks of the most aggressive call buying (mid-late January 2021), dealers became net *short* gamma and the pinning mechanism inverted — gamma squeezes accelerated moves through strikes rather than pinning to them.
- The famous January 22, 2021 close at $65.01 (a $65-strike close) is sometimes cited as a pinning event, but the mechanism was unusual: it reflected end-of-day exhaustion after multi-hundred-percent intraday moves more than classical dealer hedging.

### TSLA — variable pinning

[[tesla|Tesla]] has shown pronounced pinning in some periods and weak pinning in others. Practitioner studies suggest the variation tracks the gamma sign in dealer books: when retail is net short premium TSLA pins, when retail piles into long calls (e.g., into earnings or ahead of major product announcements) pinning weakens or inverts.

### The 0DTE-induced weakening (2022 onward)

The single most important development for pinning since the original literature: **the rise of 0DTE options** has redistributed open interest across the strike grid in ways that reduce the concentration that pinning requires. Empirical observations:

- SPX monthly OPEX Fridays show **less prominent pinning** in the 2022-2025 sample than in the 2010-2018 sample, controlling for OI and volatility.
- The dispersion of dealer gamma across many strikes (because 0DTE flows hit dozens of strikes daily) means no single strike has the dominant restoring force it once did.
- Practitioner write-ups (SqueezeMetrics, Spotgamma, Goldman options desk research) have noted the "death of pinning" as a 0DTE side-effect.
- The effect persists in single-name stocks (AAPL, MSFT) where 0DTE doesn't yet dominate, but is materially weaker on indices and ETFs.

This is consistent with the dealer-gamma mechanism: more strikes with material gamma → less concentrated restoring force → weaker pinning.

### Cumulative effect on monthly OPEX Fridays

A common practitioner pattern: SPX monthly OPEX Fridays show a "drift to the largest dealer-gamma strike" in the final hour, with intraday volatility compressing as the strike is approached. The classic "OPEX dump-and-pump" — where SPX fades into the close near the dominant strike — has been observed many times historically. As 0DTE has grown, this pattern has weakened but not vanished.

## Implications for Risk

### For short-premium income books

Pinning is *favorable* for traders who are short an at-the-money option at the pinning strike — the underlying is dragged toward the strike by dealer hedging, increasing the probability of expiring worthless. Many [[options-portfolio-construction|premium-selling]] curricula explicitly cite the pinning bias as a tailwind for income strategies (see [[variance-risk-premium]] for the broader edge).

But the favorable pinning is paired with [[pin-risk|pin risk]]: a position pinned at the strike is in the *worst* state at expiration if it's a physically-settled American option (assignment uncertainty). The income trader's resolution: **trade [[index-options|cash-settled index options]]** to capture the pinning tailwind without the pin-risk operational cost.

### For long premium / tail-risk books

Pinning is *unfavorable* for long-premium positions at high-OI strikes. A long ITM call held into expiration can see its profit dragged back toward zero as dealer hedging pulls spot toward the strike. The mitigation: **close long premium positions before the final hour of expiration day**, especially for short-dated options.

### For 0DTE strategies

0DTE strategies operate in the regime where pinning historically has been strongest — but where the rise of 0DTE itself has weakened the effect. Modern 0DTE traders should not rely on classical pinning patterns to bail out delta-exposure on positions held into the close. The intraday gamma profile is more diffuse than the monthly OPEX literature suggests.

### Interaction with [[soq-settlement|SOQ settlement]]

For AM-settled monthly SPX, the *settlement* value is set by Friday morning's component opens, not by the Thursday-afternoon close where dealer-gamma hedging would otherwise pin. This means SPX monthlies' *settlement* is **not** subject to classical pinning, even if the cash SPX mark on Thursday afternoon was being pinned by hedging flow. The PM-settled SPXW weeklies, by contrast, settle to the Friday 4:00 pm close — and are subject to whatever pinning dynamics are operative in the final hour.

### Position management discipline

The institutional rule: **don't let position management depend on pinning happening**. If a position requires pinning to come out profitable, treat the pinning thesis as a separate bet from the original trade. The empirical effect is real but small in magnitude (~2-4 percentage points of clustering excess in the original studies); a position underwater by a few percent that needs pinning to save it is one with negative expected value, not a "wait for pinning" trade.

### Risk of *anti-pinning* (gamma squeezes)

When the dealer gamma flips negative at a strike — typically because public flow has shifted from net-short to net-long expiring options, as in retail-driven squeezes — the same hedging flow that previously pinned now amplifies. Risk-budgeted books (see [[options-risk-budgeting]]) need to monitor the **net dealer gamma at strike** indicator (provided by SqueezeMetrics, Spotgamma, and similar dealers) rather than just open interest, since OI alone doesn't reveal which side dealers are on.

## Common Mistakes / Pitfalls

1. **Confusing pinning with pin risk.** Pinning is the empirical clustering of spot at strikes; pin risk is the position-level uncertainty of post-close exercise. They are related but distinct. See [[pin-risk]].
2. **Treating max pain as a forecast.** The "max pain strike" is a heuristic for where pinning aims. It works *on average* and *over many expirations*, not as a same-day price target. A single-week max-pain trade is not an edge.
3. **Assuming pinning works on illiquid names.** The pinning mechanism requires meaningful dealer gamma, which requires meaningful options open interest. On illiquid optionables (low-volume single names), the mechanism is too weak to detect.
4. **Ignoring the dealer-gamma sign.** Pinning works when dealers are net long gamma at the strike. When the gamma flips negative, the same OI causes the opposite effect (gamma squeeze). Check the gamma sign before betting on pinning.
5. **Underestimating 0DTE-induced gamma diffusion.** The classical pinning literature was based on a market structure where monthly expirations dominated and gamma was concentrated. 2022+ markets have continuous expirations and diffuse gamma. The effect is materially weaker than older studies suggest.
6. **Confusing single-name pinning patterns with index pinning.** AAPL pinning and SPX pinning have similar mechanisms but different magnitudes and distortion sources. Monthly OPEX patterns on individual stocks generalize less well to indices in the post-0DTE era.
7. **Letting pinning bias position-sizing.** "I'm short the put at $200, AAPL has been pinning to $200 for years" is not a sizing argument — the pinning effect is small relative to the underlying's daily move distribution. Size for the underlying's vol, not for the pinning prior.
8. **Forgetting that pinning is an *intraday* effect that resets overnight.** Friday's pinning to a strike doesn't constrain Monday's open. Positions held over the weekend are exposed to whatever overnight news produces, regardless of where Friday closed.

## Related

- [[pin-risk]] — position-level uncertainty (distinct concept)
- [[max-pain]] — the open-interest-weighted strike heuristic
- [[dealer-gamma-hedging]] — the mechanism that drives pinning
- [[market-makers]] — the agents whose hedging produces the effect
- [[index-options]], [[spx-options]], [[spy-options]] — products where pinning is observed
- [[am-vs-pm-settlement]] — AM-settled monthlies aren't pinned at settlement; PM-settled are
- [[soq-settlement]] — settlement mechanism that bypasses Friday-afternoon pinning
- [[zero-dte-options]] — 0DTE flow has weakened classical pinning
- [[gamma-explosion]] — the gamma side of expiration risk
- [[gap-risk]] — overnight gap risk that resets pinning patterns
- [[liquidity-evaporation]] — liquidity-collapse mechanism that can break pinning
- [[gamestop-saga]] — case study of pinning vs anti-pinning regimes
- [[volmageddon]] — case study of dealer-hedging cascade (anti-pinning case)
- [[options-portfolio-construction]] — portfolio handling of pinning bias
- [[options-risk-budgeting]] — gamma-aware position sizing
- [[variance-risk-premium]] — broader edge captured by short-premium books

## Sources

- Ni, S. X., Pearson, N. D., and Poteshman, A. M. (2005). *Stock Price Clustering on Option Expiration Dates*. *Journal of Financial Economics*, 78(1): 49-87. The foundational empirical study.
- Golez, B. and Jackwerth, J. C. (2012). *Pinning in the S&P 500 Futures*. *Journal of Financial Economics*, 106(3): 566-585. Index-futures extension.
- Pearson, N. D., Poteshman, A. M., and White, J. (2007). *Does Option Trading Have a Pervasive Impact on Underlying Stock Prices?* University of Illinois working paper.
- Ben-David, I., Franzoni, F., and Moussawi, R. (2018). *Do ETFs Increase Volatility?* *Journal of Finance*. Related microstructure work on ETF arbitrage and basket hedging.
- SqueezeMetrics, Spotgamma, Goldman Sachs equity-derivatives research notes — practitioner observations on dealer gamma exposure (DGE / GEX) and the post-2022 weakening of pinning.
- Cboe research notes on 0DTE option volume and the dispersion of dealer gamma.
- [[itpm-options-portfolio-management]] — institutional treatment of pinning bias as a tailwind for short-premium books.
- [[tastytrade-spx-research]] — empirical studies on SPX expiration-day return distributions, including pinning measurements.
