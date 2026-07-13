---
title: "0DTE Impact on SPX"
type: concept
created: 2026-05-07
updated: 2026-06-11
status: good
tags: [options, market-microstructure, sp500, indicators, derivatives, dealer-gamma-hedging]
aliases: ["0DTE Market Impact", "0DTE on SPX", "Same-Day SPX Options Impact", "0DTE Microstructure"]
related: ["[[zero-dte-options]]", "[[dealer-gamma-hedging]]", "[[gamma-squeeze]]", "[[volatility-surface]]", "[[max-pain]]", "[[options-pinning]]", "[[realized-volatility]]", "[[implied-volatility]]", "[[volatility-risk-premium]]", "[[high-frequency-trading]]", "[[market-makers]]", "[[volmageddon]]"]
domain: [market-microstructure, options, derivatives]
prerequisites: ["[[zero-dte-options]]", "[[options-greeks]]", "[[dealer-gamma-hedging]]"]
difficulty: advanced
---

The rapid expansion of **0DTE (zero days to expiration)** SPX options trading from 2022 onward has materially changed the microstructure of the S&P 500 options market and, by knock-on effect, the intraday dynamics of SPX itself. By mid-2024, 0DTE volume reached **roughly 50% of total SPX options daily volume** and on some days exceeded that — a structural shift unprecedented in the 40-year history of US listed options. This page summarises the empirical findings from JPMorgan, Goldman Sachs, the CBOE Research team, and academic studies on what 0DTE has done to realised volatility, intraday price patterns, dealer hedging flows, and risk in the underlying index.

## Background: How 0DTE Volume Became Dominant

Before 2022, SPX had three or four expiries per week (Mon/Wed/Fri standard, plus EOM). In April 2022 the [[cboe|CBOE]] expanded SPX options to **five-day-a-week expirations** (M/T/W/Th/F), creating a same-day expiry every trading day. This regulatory and product-listing change is what made the explosion of 0DTE volume possible.

Volume statistics (sourced from CBOE Research and OCC):

| Year | 0DTE share of SPX options daily volume | SPX 0DTE notional / day (approx.) |
|---|---|---|
| 2020 | ~5% (Friday only, mostly weeklies) | $5-10B |
| 2022 (post-listing) | ~25% | $30-60B |
| 2023 | ~40% | $80-150B |
| 2024 | ~50% | $200-400B |

For comparison, total SPX options daily *notional* turnover has been routinely $400-800 billion in 2024-2025 — a substantial fraction of which is now expiring within hours of being traded.

The growth in 0DTE has been driven by:
- Five-day-a-week expirations (the structural enabler)
- Retail platform marketing (Robinhood, tastytrade, IBKR introduced low-friction 0DTE access)
- Institutional adoption — systematic short-vol funds, market-makers, and CTAs began running explicit 0DTE strategies
- Tax efficiency (Section 1256 60/40 treatment applies to all SPX options regardless of holding period)
- Capital efficiency (a 0DTE position requires a fraction of the buying-power-reduction of a longer-dated equivalent)

## Empirical Effects on SPX Intraday Microstructure

### Realised Volatility

Multiple studies (Goldman Sachs, Morgan Stanley, Cboe Research) have examined whether 0DTE expansion has *increased* realised intraday vol. The consensus by 2024:

- **Headline finding**: realised volatility on the *daily* close-to-close timeframe has not measurably increased and may have slightly *decreased*. The structural short-vol flow from systematic premium-sellers absorbing 0DTE call and put writing has dampened daily moves.
- **Intraday finding**: realised vol on *very-short-horizon* timeframes (5-minute, 30-minute) has materially increased, particularly in the final two hours of the trading day when 0DTE gamma exposures are largest.
- **Tail-risk finding**: contingent on a shock entering the market, the *response* of intraday vol is more violent than pre-2022 because dealer gamma is much larger and accumulates much faster.

### The "0DTE Pin" Phenomenon

Traditional [[options-pinning|options pinning]] occurs at monthly OPEX and reflects the gravitational pull of large open interest at round-number strikes as dealers hedge into the close. The 0DTE expansion has produced a daily analog:

- Heavy accumulation of 0DTE positions at 25- or 50-point strike intervals creates *intraday* magnetic levels.
- The pull is strongest in the final 60-90 minutes when [[gamma]] for ATM 0DTE options goes hyperbolic.
- This appears as the "0DTE pin" — SPX gravitating toward the strike with the largest net gamma exposure for the day.
- Distinct from monthly OPEX pinning in two ways: (1) it happens *every day*, and (2) the open interest is much smaller than monthly accumulations, so the pinning is weaker but more frequent.

The 0DTE pin is observable but unreliable as a trading signal — it is overwhelmed by any meaningful directional flow, and the gamma magnetism is far smaller than it appears in dealer-positioning charts.

### Intraday Gamma-Hedging Flows

Dealers (market-makers selling 0DTE options) carry massive gamma exposure that explodes near the close as 0DTE options approach expiration. Empirical findings:

- **Late-session amplification** — JPMorgan's Marko Kolanovic and others have documented that the final 90 minutes of the SPX trading day has seen a measurable increase in realised intraday vol post-2022, attributed to the dynamic rehedging of 0DTE dealer positions.
- **Asymmetric risks** — a small intraday move can transition large 0DTE blocks from OTM to ITM, forcing dealers to dump or buy underlying SPX futures aggressively to maintain delta neutrality. This "gamma flip" effect is much sharper than for monthly options.
- **Self-stabilising in calm regimes** — when dealers are *short* gamma (typical for retail-dominated 0DTE flow), a small move triggers buying that *opposes* the move, dampening intraday trends.
- **Self-destabilising in shocks** — when dealers are *long* gamma (rarer, but happens in heavy institutional flow), the same logic reverses and dealers' rehedging *amplifies* directional moves.

The full mechanics are covered in [[dealer-gamma-hedging]]; the 0DTE-specific point is that gamma exposures are now far higher *as a fraction of liquidity* at the close than they were pre-2022.

### Dealer Balance Sheets

Cboe Research and primary-dealer reports through 2024:

- 0DTE has *not* materially increased the aggregate gross risk on dealer balance sheets in the way critics initially feared, because the positions expire same-day and turn over rapidly.
- However, *intraday peak risk* — the gross gamma exposure at, say, 3pm on an active 0DTE day — has grown substantially.
- The risk is therefore an **intraday-management** problem rather than an overnight-balance-sheet problem; dealers manage by aggressive delta-rehedging and by widening spreads on the 0DTE quote during stressed periods.

### Implied vs Realized Volatility (VRP)

The 0DTE expansion has compressed the [[volatility-risk-premium|VRP]] at very-short-dated tenors:

- 0DTE implied vol is now systematically *closer* to realised intraday vol than it was pre-2022 — competition among 0DTE option sellers (retail, hedge funds, market-makers) has tightened the premium.
- The 30-day, 60-day, and 90-day VRP appears largely unchanged.
- Implication: 0DTE-only short-vol strategies have lower expected returns than 30-day short-vol strategies on a risk-adjusted basis as of 2024-2025.

## Conflicting Evidence and Open Questions

Not all the academic and practitioner work agrees:

- **Goldman Sachs 2023 research** initially suggested 0DTE was meaningfully amplifying intraday vol; **Goldman 2024 follow-up** softened this conclusion, attributing earlier findings to confounding factors (the 2022 macro vol regime).
- **Marko Kolanovic (JPMorgan)** has been the most prominent voice warning that 0DTE could amplify a future shock event in a "Volmageddon-style" cascade. Critics argue Kolanovic over-weights the scenarios visible in his book and that aggregate dealer gamma remains manageable.
- **Cboe Research** consistently finds modest intraday vol increases, no aggregate balance-sheet stress, and stable bid-ask spreads — broadly the "0DTE is fine" position.
- **Academic literature** (multiple working papers 2023-2024) has found mixed evidence; some studies find 0DTE creates a measurable "smile-tail" distortion in the IV surface, others find no effect after controlling for the macro vol regime.

The honest summary as of 2026: 0DTE has changed SPX microstructure measurably but *not* catastrophically, and a major test event (a Volmageddon-scale shock) has not yet occurred since the 2022 expansion. What happens to 0DTE microstructure in such an event remains the central open question.

## The Volmageddon Comparison

The February 2018 [[volmageddon|Volmageddon]] event — when the short-VIX ETP cascade caused VIX to double in a day and the underlying VIX-futures structure broke — is the canonical recent example of an exotic options/vol product creating a feedback loop that destabilised the broader market. The fear with 0DTE is structural similarity:

- A large enough shock could push 0DTE options across many strikes ITM simultaneously
- Dealer hedging of those positions would require enormous delta-rehedging in SPX futures or SPY shares within minutes
- The forced rehedging would amplify the original shock
- Liquidity could collapse on the 0DTE quote, creating exit-illiquidity for everyone holding 0DTE positions

Whether this scenario is realistic or catastrophist depends on (a) the *direction* of dealer gamma at the moment of shock, (b) the depth of the [[spx-futures|SPX futures]] book during the shock, and (c) circuit-breaker mechanics. Cboe and the SEC have studied it; no formal regulation has resulted as of 2026 but the SEC has made several requests for information from CBOE on the topic.

## Regulatory Concerns

Active areas of regulatory and exchange concern:

- **Suitability** — retail 0DTE access has expanded faster than retail options education. Some brokers now require explicit 0DTE-specific risk acknowledgments.
- **Clearing risk** — same-day expirations compress the clearing window. The OCC has tightened margin and clearing protocols for 0DTE.
- **Manipulation surveillance** — short-window manipulation schemes (e.g., late-day spoofing into 0DTE expiration) are easier to attempt and harder to detect because the tape is dense.
- **Market-wide stress testing** — regulators have requested that CBOE and primary dealers stress-test 0DTE-specific scenarios. Results are not public.

## Implications for Traders

- **Short-vol traders** — 0DTE-only premium-selling has tighter VRP than 30-day. The income strategies that work pre-2022 still work, but expected returns are slightly compressed at very short tenors.
- **Long-vol / hedge buyers** — 0DTE puts are surprisingly effective intraday hedges *if* the shock occurs during the trading day. Useless for overnight gap risk.
- **Macro / directional traders** — Be aware that the 0DTE pin can hold SPX in a tight range late in the day even when fundamentals would suggest a move; the move often comes the *next* day after the 0DTE expires.
- **Systematic strategies** — Backtests using pre-2022 SPX intraday data are now structurally non-stationary; the 0DTE regime is a different distribution. Walk-forward and regime-aware testing are essential.

## Related

- [[zero-dte-options]] — the parent strategy/product page
- [[dealer-gamma-hedging]] — the mechanism behind the intraday effects
- [[gamma-squeeze]] — extreme gamma-driven feedback (related but distinct)
- [[options-pinning]], [[max-pain]] — traditional pinning vs 0DTE pinning
- [[volatility-risk-premium]] — the structural quantity 0DTE compresses
- [[volmageddon]] — the canonical vol-product cascade event
- [[high-frequency-trading]], [[market-makers]] — the participants on the other side of 0DTE flow
- [[itpm-trade-construction-playbook]] — institutional treatment of 0DTE within a portfolio framework

## Sources

- CBOE Research — *0DTE Option Trading Data and Trends* series (multiple notes 2022-2024). Available at cboe.com/insights.
- OCC daily volume statistics — option clearing volumes by tenor.
- Kolanovic, Marko (JPMorgan) — *Global Markets Strategy* notes on 0DTE volume and dealer positioning, 2022-2024.
- Goldman Sachs Equity Derivatives Research — multiple notes on 0DTE flow and intraday vol, 2023-2024.
- Bloomberg, *0DTE Options: A Year After CBOE's Daily Expirations*, May 2023.
- Working paper: Beckmeyer, Branger, Hommel, *Same-Day Settled Options and the Intraday Volatility Surface*, 2023.
- Cboe and OCC joint white paper on 0DTE clearing and risk management, 2024.
- [[itpm-options-portfolio-management]] — institutional-grade portfolio treatment of 0DTE within a hedged book.
