---
title: "LJM Preservation and Growth"
type: entity
created: 2026-05-07
updated: 2026-06-10
status: good
tags: [company, options, volatility, regulation, history]
aliases: ["LJM", "LJM Preservation & Growth Fund", "LJM Funds Management"]
entity_type: fund
founded: 2006
headquarters: "Chicago, Illinois, USA"
website: "https://www.ljmfunds.com"
related: ["[[volmageddon]]", "[[short-volatility-strategies]]", "[[long-vol-vs-short-vol]]", "[[xiv-velocity-shares]]", "[[malachite-capital]]", "[[catalyst-hedged-futures]]", "[[variance-risk-premium]]", "[[short-strangle]]", "[[options-premium-selling]]", "[[universa-investments]]", "[[vix]]", "[[gap-risk]]", "[[failure-modes]]"]
---

LJM Preservation and Growth was a Chicago-based options-selling fund run by Anthony Caine and Anish Parvataneni that became the textbook case of a short-volatility blow-up when it lost roughly 80% of its value over two trading days during the **February 5-6, 2018** [[volmageddon|Volmageddon]] vol shock. The fund had marketed itself for years as a low-correlation income strategy harvesting the [[variance-risk-premium]] by selling out-of-the-money S&P 500 index options; it was wound down within weeks of the shock and became the canonical short-vol cautionary tale repeated in every subsequent vol-strategy due diligence.

## Overview

LJM Funds Management was founded in the early 2000s and built its track record by systematically selling [[short-strangle|short strangles]] and other premium-collecting structures on S&P 500 futures options. The flagship vehicle, LJM Preservation and Growth Fund (a registered '40 Act mutual fund offered to retail and advisory investors), targeted an "absolute return" profile -- modest, equity-like returns with low correlation to the S&P 500 -- by pocketing option premium in calm regimes. The fund also operated parallel hedge-fund-structured private vehicles for accredited investors.

For most of the 2009-2017 cycle the strategy delivered exactly what the marketing promised: steady, positive monthly returns with [[sharpe-ratio]]s well above 1.0 and headline drawdowns measured in single digits. Assets under management peaked above $800M across the LJM fund complex by late 2017, with the Preservation and Growth mutual fund alone holding several hundred million.

## Strategy / Mechanics

The book was a classic [[options-premium-selling|premium-selling]] short-vol portfolio:

- **Instrument**: S&P 500 (ES) futures options, primarily monthly expirations.
- **Structure**: Short strangles and short put spreads sold OTM, frequently 2-5% from spot, with delta and vega budgets sized to a target account-level risk.
- **Margin**: SPAN-margined futures options, which gave the fund significant notional leverage relative to deposited capital under [[span-margin]] in calm regimes.
- **Hedging**: Limited and discretionary. The fund did not run a continuous [[long-vol-overlay|long-vol overlay]]; tail protection was added opportunistically when volatility was deemed cheap.
- **Income source**: The structural [[variance-risk-premium]] -- the spread between implied and realized volatility on SPX options.

This is the same archetype critiqued in [[long-vol-vs-short-vol]]: a [[negative-skew]] book that prints money in calm regimes and accumulates [[gap-risk]] across the wings until a single shock prices in years of accumulated theta.

## Track Record

- **2009-2016**: Reported annualized returns in the high single digits to low teens with low single-digit volatility -- the exact profile that attracts allocators to short-vol strategies.
- **2017**: Strong year as realized vol stayed near record lows (the VIX spent much of 2017 below 11). The fund's marketing leaned heavily on the idea that a "preservation" mandate guaranteed conservative position sizing.
- **End of January 2018**: LJM Preservation and Growth had approximately $805M in assets across its mutual fund and related vehicles, per public Form N-Q filings and subsequent SEC filings. The CFTC's complaint put total LJM assets under management — commodity pools, the mutual fund, and managed accounts combined — at **over $1 billion** as of January 2018.

## Blow-Up: February 5-6, 2018

On Friday February 2, 2018 the S&P 500 fell 2.1% as bond yields climbed; LJM ended the week with significant short-vega and short-gamma exposure. On **Monday February 5, 2018**, the S&P 500 fell another 4.1%, the VIX more than doubled from ~17 to ~37 in a single session, and short-VIX-futures vehicles such as [[xiv-velocity-shares|XIV]] lost roughly 96% in after-hours trading. LJM's short SPX puts and strangles repriced violently:

- Reports filed after the event indicate the LJM Preservation and Growth mutual fund's NAV dropped from approximately $9.90 on Feb 2 to roughly $4.07 on Feb 6 -- a drawdown near **-56% in one trading day** at the mutual fund level, and approximately **-80%** when measured peak-to-trough across the Feb 2-Feb 6 window.
- Margin calls on the underlying ES options forced liquidation into a market with [[liquidity-crisis|disappearing liquidity]] and bid-ask spreads many multiples of normal.
- Subsequent SEC filings showed the fund had been carrying short-option positions whose [[stress-testing|stress-test loss profile]] had been understated to investors, particularly under VIX-doubling scenarios.

By the end of the week the fund had suspended new subscriptions; within weeks it announced a wind-down. The private LJM hedge-fund vehicles took similarly severe losses and were also closed.

## Regulatory Aftermath

The regulatory record (verified June 2026):

- **May 2021**: The [[sec|SEC]] and CFTC filed parallel civil complaints (CFTC complaint announced May 27, 2021) against **Anthony Caine, Anish Parvataneni, LJM Funds Management Ltd, and LJM Partners Ltd** for misleading investors about the fund's risk profile and risk-management practices. Per the CFTC, LJM falsely claimed worst-case daily losses were capped at roughly **20%** for the Preservation and Growth strategy (30% for Moderately Aggressive, 35-40% for Aggressive) when LJM's own internal historical scenarios showed potential losses **exceeding 40%**. Former chief risk officer **Arjuna Ariathurai** settled at filing ($150,000 penalty, $83,333 disgorgement plus interest).
- **July 1, 2025**: The U.S. District Court for the Northern District of Illinois entered consent orders resolving the case for a combined **~$6 million**: LJM and Caine jointly liable for **$4,624,271 in disgorgement**, Caine paying a **$500,000** civil penalty, and Parvataneni **$721,093 disgorgement plus a $200,000 penalty**. Caine received a **3-year** registration/advising ban and Parvataneni a **1-year** ban (not permanent industry bars, as sometimes reported).

The case is now used as a teaching example in compliance training for risk-disclosure obligations of '40 Act funds running short-vol mandates.

## Why It Matters / Lessons

LJM is cited in nearly every post-2018 piece of vol-fund due diligence for several reasons:

1. **The blow-up was a single-shock event, not a slow bleed.** Five-plus years of theta were erased in two trading sessions. This is the defining mathematical feature of [[negative-skew]] books -- the average month tells you nothing about the distribution of bad months.
2. **Marketing as "preservation" was incompatible with the strategy.** A continuously short-vega, short-gamma book cannot honestly be marketed as preservation-of-capital. The label was a [[behavioral-finance|behavioral red flag]] that predates the trade itself.
3. **'40 Act / mutual-fund wrapping does not neutralize tail risk.** Daily-liquid retail wrappers around short-vol books concentrate exit risk: redemptions force liquidation precisely when liquidity is worst.
4. **Stress tests must include vol-of-vol, not just vol.** Many of LJM's published risk numbers assumed VIX moves of 5-10 points; the actual February 2018 move was ~20 VIX points and roughly a 4-sigma vol-of-vol shock. The strategy's tail was modeled with the wrong distribution. See [[fat-tails]] and [[stress-testing]].
5. **The right comparison is portfolio-level survival, not headline Sharpe.** LJM's Sharpe through 2017 was excellent. Its Sharpe over a full cycle including February 2018 is undefined (the fund did not survive).

It is the canonical counter-example to [[universa-investments|Universa]]'s long-vol case: where Universa is structurally designed to lose small in calm regimes and win big in shocks, LJM was structurally designed to win small in calm regimes and lose enormously in shocks. Both designs are internally consistent; only one survives multiple cycles. See [[long-vol-vs-short-vol]] for the side-by-side.

## Key People

- **Anthony Caine** -- Founder and chairman of LJM Funds Management / LJM Partners. Subject to SEC/CFTC enforcement following the 2018 collapse: jointly liable with LJM for $4.6M disgorgement, $500K penalty, and a 3-year ban on managing or advising third-party money (consent order, July 2025).
- **Anish Parvataneni** -- Chief portfolio manager of the LJM Preservation and Growth Fund (ex-Citadel trader). Paid $721K disgorgement and a $200K penalty with a 1-year ban under the same consent orders.
- **Arjuna Ariathurai** -- Former chief risk officer; settled with the SEC/CFTC at the time of the May 2021 charges ($150K penalty plus disgorgement).

## Related

- [[volmageddon]] -- the February 2018 event that ended the fund
- [[xiv-velocity-shares]] -- the short-VIX ETN that terminated on the same day
- [[malachite-capital]] -- another short-vol fund that died in a different shock (March 2020)
- [[catalyst-hedged-futures]] -- a related short-call mutual-fund blow-up earlier in 2017
- [[short-volatility-strategies]] -- the strategy archetype
- [[short-strangle]] -- the canonical structure
- [[long-vol-vs-short-vol]] -- comparison and synthesis page
- [[options-premium-selling]] -- the broader doctrine
- [[variance-risk-premium]] -- the premium being harvested
- [[universa-investments]] -- the structural opposite
- [[gap-risk]] -- the mechanism that destroyed the fund
- [[failure-modes]] -- failure-mode taxonomy for trading strategies
- [[stress-testing]] -- what was insufficient at LJM
- [[negative-skew]] -- the return profile that masks tail risk

## Sources

- CFTC Press Release 8392-21, "CFTC Charges Chicago Commodity Pool Operators, Owner, and Former Chief Portfolio Manager with Fraud and Supervision Failures" (May 27, 2021) — https://www.cftc.gov/PressRoom/PressReleases/8392-21
- SEC Litigation Releases LR-25101 (2021 complaint) and LR-26338 (resolution) — https://www.sec.gov/litigation/litreleases/lr-25101
- CFTC Press Release 9092-25, "Federal Court Orders Chicago Commodity Pool Operators, Owner, Former Chief Portfolio Manager to Pay More Than $6M in Fraud Action" (July 2025) — https://www.cftc.gov/PressRoom/PressReleases/9092-25
- Crain's Chicago Business, "SEC fines LJM Partners execs over $1B collapse" (2025)
- LJM Preservation and Growth Fund Form N-Q and N-CSR filings (2017-2018), available via SEC EDGAR.
- *Wall Street Journal*, "Volatility Bet Spirals Into a Disaster for Some Funds" (February 2018).
- *Bloomberg*, coverage of the LJM wind-down (February-March 2018).
- *Financial Times*, post-Volmageddon analyses (February-March 2018).
- Verified via Perplexity (sonar) and web search, 2026-06-10.
