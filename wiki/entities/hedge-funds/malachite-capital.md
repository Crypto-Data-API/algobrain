---
title: "Malachite Capital Management"
type: entity
created: 2026-05-07
updated: 2026-06-10
status: good
tags: [company, options, volatility, history, derivatives]
aliases: ["Malachite Capital", "Malachite", "Malachite Capital Management LP"]
entity_type: fund
founded: 2013
headquarters: "New York, New York, USA"
website: ""
related: ["[[covid-crash]]", "[[short-volatility-strategies]]", "[[long-vol-vs-short-vol]]", "[[ljm-preservation-and-growth]]", "[[catalyst-hedged-futures]]", "[[xiv-velocity-shares]]", "[[volmageddon]]", "[[variance-risk-premium]]", "[[short-strangle]]", "[[options-premium-selling]]", "[[universa-investments]]", "[[gap-risk]]", "[[failure-modes]]", "[[liquidity-crisis]]"]
---

Malachite Capital Management was a New York boutique hedge fund founded in 2013 that ran a structured short-volatility book on global equity indices. After roughly seven years of strong reported returns the firm imploded in mid-March 2020 during the [[covid-crash|COVID crash]], announcing a wind-down on March 17, 2020 — within days of the worst of the vol shock. Together with [[ljm-preservation-and-growth|LJM]] in 2018 and the broader [[xiv-velocity-shares|XIV]] cohort, Malachite is now cited as one of the canonical short-vol blow-up case studies of the modern era.

## Overview

Malachite was founded in 2013 by **Joe Aiken** and **Jacob Weinig**, who came off Goldman Sachs's equity-derivatives desk (Institutional Investor described them as VP-level salespeople on that desk before launching the fund). The firm built an institutional client base by running a structured short-volatility strategy whose track record through 2018-2019 looked exceptional: high-single-digit to low-double-digit annualized returns with reported volatility low enough to produce headline [[sharpe-ratio]]s well above 1. The fund oversaw about **$600 million** at its peak going into 2020 (Bloomberg, March 2020), with leveraged exposure reported upward of **$1.5 billion** in counterparty bets.

The fund survived the [[volmageddon|February 2018 vol shock]] (during which [[ljm-preservation-and-growth|LJM]] and [[xiv-velocity-shares|XIV]] died) and continued to grow. Allocators reportedly saw this survival as evidence that Malachite was the "smart" version of the short-vol trade -- a reading the COVID crash decisively refuted.

## Strategy / Mechanics

Public reporting and SEC filings indicate Malachite's strategy was structurally a short-vol portfolio, with several features that differentiated it from a naive [[short-strangle]] book:

- **Cross-asset short-vol**: The firm was reported to sell volatility on multiple equity indices globally (S&P 500, Euro Stoxx, Nikkei) rather than concentrating in SPX, with the intent of diversifying short-vol exposure.
- **Structured vehicles**: Some of the exposure reportedly came through structured products and dispersion trades rather than only listed options. Dispersion (long single-stock vol, short index vol) is a short-correlation trade that often correlates with short-vol exposure when correlations spike.
- **Tail wings**: Malachite reportedly bought some tail protection against the wings of its short positions, which is what allowed it to survive February 2018 with manageable losses. The protection, however, was sized to a smaller stress than what materialized in March 2020.
- **Income source**: The structural [[variance-risk-premium]] across multiple regional indices, plus [[correlation-risk-premium|correlation risk premia]] in dispersion books.

The book was **net short premium, net short vega, net short gamma** -- the textbook short-vol profile of [[long-vol-vs-short-vol]].

## Track Record

- **2013-2017**: Reported strong, low-vol returns through the long post-GFC bull market. The exact regime in which short-vol books are designed to print money.
- **February 2018 ([[volmageddon|Volmageddon]])**: Malachite reportedly absorbed losses but survived, distinguishing itself from LJM and the short-VIX-ETN cohort. This survival was used in subsequent marketing.
- **2018-2019**: Continued growth, AUM rose to several hundred million.
- **March 2020**: Catastrophic loss. By all public reports the fund was effectively wiped out within a few trading days as vol of vol exploded, correlations went to one across global equities, and dispersion books gapped against the short-index-vol leg. After margin calls from counterparties including BNP Paribas, Malachite announced on **March 17, 2020** that it was dissolving its funds, citing "extreme adverse market conditions."

## Blow-Up: March 2020

The [[covid-crash|COVID crash]] of February-March 2020 was a different kind of shock from Volmageddon:

- **Volmageddon (Feb 2018)** was a single-day VIX-of-VIX shock concentrated in U.S. short-VIX-futures vehicles. A book with cross-asset diversification and modest tail protection could absorb it.
- **COVID (Feb-March 2020)** was a multi-week, multi-asset, [[liquidity-crisis|liquidity-crisis]] vol regime in which:
  - SPX implied vol exceeded 80, multi-year highs.
  - Euro Stoxx and Nikkei vols rose simultaneously, eliminating the diversification benefit of the cross-regional short.
  - **Correlations spiked to ~1** across single names within indices, which is the worst possible regime for dispersion books -- the long-single-name-vol leg lagged the short-index-vol leg's losses.
  - Liquidity in OTM index options collapsed; bid-ask spreads in stressed wings widened many multiples.

Public reporting in *Bloomberg*, *Wall Street Journal*, and *Institutional Investor* in March-April 2020 indicated Malachite told investors the funds had suffered losses sufficient to render the strategy non-viable, and that the firm would close positions and wind down. Institutional Investor's post-mortem ("How to Lose a Billion Dollars Without Really Trying") reported that the blow-up left losses roughly **twice the size of the ~$600M fund itself** — counterparties as well as investors absorbed the damage, which is why the episode also triggered investor-claims investigations against the consultant (Fund Evaluation Group) that had recommended the fund.

The wind-down was unusually fast -- positions closed, capital returned, firm dissolved -- in part because the structured nature of the book meant counterparties were unwilling to face Malachite at any size into the storm. This matches the pattern in [[ljm-preservation-and-growth|LJM]]'s wind-down two years earlier: when short-vol books fail, they fail in days, not quarters.

## Why It Matters / Lessons

1. **Surviving one shock is not evidence of robustness.** Malachite survived Volmageddon and was then destroyed by COVID. Each shock is a different distribution of vol, vol-of-vol, correlation, and liquidity. A book optimized to survive one vector can still be overwhelmed by another. See [[stress-testing]] and [[failure-modes]].
2. **Cross-asset and dispersion diversification of short vol is mostly illusory in true stress.** Index correlations across regions spiked together in March 2020. Single-stock correlations within indices spiked toward one. The "diversified" short-vol book turned out to be a single trade with multiple labels.
3. **Modest tail protection is not the same as a real long-vol overlay.** Malachite carried some wings, which helped in February 2018 but were dwarfed by the magnitude of the March 2020 move. Sizing a [[long-vol-overlay]] to median stresses rather than tail stresses leaves the book exposed where it matters most.
4. **Speed of failure favors counterparties, not investors.** The 4-7-day wind-down meant investors had no opportunity to redeem or reposition. Once the firm decided the strategy was non-viable, recovery for limited partners was determined by whatever remained after closing positions in the worst possible market.
5. **Survivorship bias in published track records is real.** Allocator due diligence in 2019 saw Malachite's "survived 2018" track record as a positive signal. In hindsight, that signal was specific to one type of shock. Backtests and live track records of short-vol books should be read with explicit attention to which historical shocks they cover and which they do not.

The Malachite case is now used alongside LJM in vol-strategy due diligence as a reminder that the [[ergodicity]] problem is not a theoretical concern -- it is the empirical reality of the short-vol space.

## Key People

- **Joe Aiken** -- Co-founder. Background in equity derivatives at major dealer banks before founding Malachite.
- **Jacob Weinig** -- Co-founder. Background in structured equity derivatives.
- Both founders departed the asset-management industry in the immediate aftermath of the wind-down; subsequent activities are not publicly documented in detail.

## Related

- [[covid-crash]] -- the event that ended the fund
- [[ljm-preservation-and-growth]] -- the prior canonical short-vol blow-up
- [[catalyst-hedged-futures]] -- another short-vol mutual-fund failure
- [[xiv-velocity-shares]] -- the most public Volmageddon casualty
- [[volmageddon]] -- the shock Malachite survived
- [[short-volatility-strategies]] -- the strategy archetype
- [[short-strangle]] -- the canonical structure
- [[long-vol-vs-short-vol]] -- comparison and synthesis page
- [[options-premium-selling]] -- the broader doctrine
- [[variance-risk-premium]] -- the premium being harvested
- [[universa-investments]] -- the structural opposite
- [[gap-risk]] -- the failure mechanism
- [[liquidity-crisis]] -- the secondary failure mechanism
- [[failure-modes]] -- failure-mode taxonomy

## Sources

- Malachite Capital Management Form ADV filings, 2014-2020 (SEC IARD).
- *Bloomberg*, "Ex-Goldman Duo's Fund to Shut After Volatility Bets Go Awry" (March 17, 2020): https://www.bloomberg.com/news/articles/2020-03-17/malachite-capital-to-wind-down-funds-amid-market-volatility
- *Institutional Investor*, "How to Lose a Billion Dollars Without Really Trying": https://www.institutionalinvestor.com/article/2bsx55uaovbhxkwutx2io/portfolio/how-to-lose-a-billion-dollars-without-really-trying
- *Institutional Investor*, "A Hedge Fund's Fatal Bet. And the Consulting Firm Tied Up in the Mess.": https://www.institutionalinvestor.com/article/2bswy6cn47m9ct8vbn4zk/corner-office/a-hedge-funds-fatal-bet-and-the-consulting-firm-tied-up-in-the-mess
- S&P Global Market Intelligence, "NY hedge fund Malachite Capital to shut; Fed launches emergency lending facility" (March 2020): https://www.spglobal.com/marketintelligence/en/news-insights/latest-news-headlines/ny-hedge-fund-malachite-capital-to-shut-fed-launches-emergency-lending-facility-57637218
- Sonn Law Group, Malachite Capital Partners LP investor-loss investigation: https://sonnlaw.com/investigations/malachite-capital-partners-lp-investment-losses/
- *Wall Street Journal* and *Financial Times*, post-March 2020 reviews of vol-strategy failures.
- Key facts (founded 2013 by Aiken and Weinig ex-Goldman; ~$600M AUM; ~$1.5B leveraged exposure; BNP Paribas margin calls; March 17, 2020 wind-down) verified via web search of the above sources, 2026-06-10.
- [[long-vol-vs-short-vol]] -- internal synthesis comparing Malachite-style books to long-vol overlays.
