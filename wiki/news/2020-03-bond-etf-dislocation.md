---
title: "March 2020 Bond ETF Dislocation"
type: news
created: 2026-04-07
updated: 2026-04-07
status: good
tags: [news, arbitrage, bonds, etf, crashes]
event_date: 2020-03-12
markets_affected: [bonds, stocks]
impact: high
verified: true
sources_count: 1
related:
  - "[[etf-arbitrage]]"
  - "[[2008-global-financial-crisis]]"
  - "[[federal-reserve]]"
---

# March 2020 Bond ETF Dislocation

During the COVID-19 market crash, the foundational arbitrage mechanism that keeps [[etf-arbitrage|ETF prices aligned with their NAV]] shattered in the corporate bond market. Major bond ETFs like [[lqd]] (investment-grade) and [[hyg]] (high-yield) traded at historically unprecedented discounts to their net asset values -- exposing a structural fragility that had been debated for years.

## What Happened

In the second and third weeks of March 2020, as the pandemic triggered a global flight to cash, corporate bond ETFs decoupled from their underlying holdings. On **March 12**, LQD traded over **90,000 times** on public exchanges while its top underlying corporate bonds traded only **37 times each**. By **March 19**, LQD traded at a **5.7% discount to NAV** -- the widest gap in the fund's history.

HYG, the high-yield bond ETF, experienced even more extreme dislocations. The ETF was functioning as a real-time price discovery vehicle for a market where the underlying assets had essentially stopped trading.

## Why the Arb Broke

Under normal conditions, [[etf-arbitrage|Authorized Participants (APs)]] keep ETF prices anchored to NAV through creation/redemption. When an ETF trades below NAV, APs buy ETF shares cheaply, redeem them for the underlying basket, and sell the bonds at NAV -- pocketing the spread. This mechanism typically keeps discounts to fractions of a percent.

In March 2020, this broke for several reasons:

- **Underlying illiquidity**: Corporate bonds trade OTC, and dealers pulled back dramatically. Many bonds simply had no executable bid.
- **AP balance sheet constraints**: Banks acting as APs faced their own capital pressures and reduced risk-taking.
- **Redemption risk**: APs could not be confident they could sell redeemed bonds at the stated NAV.
- **Correlation of stress**: Every fixed-income market was dislocating simultaneously, eliminating hedging options.

The result was the **largest ETF arbitrage failure in history**. Bond ETFs were doing real-time [[price-discovery]] that the underlying cash bond market could not.

## Timeline

| Date | Event |
|------|-------|
| March 9 | Oil price war triggers broad selloff; bond ETF discounts widen to ~1% |
| March 12 | LQD trades 90,000+ times; underlying bonds trade ~37 times each |
| March 16 | Fed emergency rate cut to zero; discounts persist |
| March 19 | LQD discount hits 5.7% -- historic extreme |
| March 23 | [[federal-reserve|Fed]] announces corporate bond and ETF purchase facilities |
| March 24 | LQD discount flips to a **premium** overnight |

## Market Impact

The dislocation raised fundamental questions about bond ETFs as vehicles for providing [[liquidity]] in assets that are inherently illiquid. The gap between ETF trading volume and underlying bond trading volume revealed that ETFs had become the **de facto price discovery mechanism** for corporate credit.

When the Fed announced it would buy corporate bonds and ETFs directly on March 23, the discount collapsed instantly. LQD went from a 5% discount to a premium in a single session -- proving the dislocation was about market structure failure, not fundamental credit concerns.

## Resolution

The [[federal-reserve|Federal Reserve]]'s intervention was unprecedented. The Secondary Market Corporate Credit Facility (SMCCF) ultimately purchased $8.7 billion in corporate bond ETFs. The mere announcement was enough to restore the arbitrage mechanism -- APs re-engaged once they knew a backstop buyer existed.

## Trading Lessons

- **Limits to arbitrage are real**: Even the most fundamental arb mechanism -- ETF creation/redemption -- can break under sufficient stress. See also [[2022-05-terra-luna-depeg-arb]] for another arb mechanism failure.
- **When mechanisms fail, they fail fast**: The discount went from normal to historic in days, not weeks.
- **Liquidity is a state, not a trait**: Bond ETFs appeared liquid until the moment the underlying market froze. [[liquidity]] can vanish precisely when you need it most.
- **Policy intervention resets arbs**: The Fed's announcement instantly restored the mechanism, showing that [[arbitrage]] depends on structural conditions, not just prices.
- **ETFs as price discovery tools**: During the dislocation, the ETF price was arguably the "correct" price -- it reflected real-time supply and demand while NAV was stale. This reframed the debate about whether the ETF or the NAV was "wrong."

The March 2020 bond ETF dislocation remains the clearest real-world demonstration of [[arbitrage]] limits in traditional finance. For similar dynamics in crypto markets, see the [[2017-2021-kimchi-premium|Kimchi Premium]], where structural barriers prevented arbitrage for years.
