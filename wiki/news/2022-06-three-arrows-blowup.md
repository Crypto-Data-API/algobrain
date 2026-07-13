---
title: "Three Arrows Capital Blowup (June 2022)"
type: news
created: 2026-04-26
updated: 2026-06-12
status: good
tags: [crypto, history, hedge-funds, three-arrows, leverage, defi]
aliases: ["3AC Collapse", "Three Arrows Liquidation", "Su Zhu Kyle Davies", "3AC June 2022"]
event_date: 2022-06-15
markets_affected: [crypto, defi]
impact: high
verified: true
sources_count: 5
related: ["[[liquidation-cascade-arbitrage]]", "[[gbtc-discount-arbitrage]]", "[[2022-06-steth-depeg]]", "[[2022-05-terra-luna-depeg-arb]]"]
---

# Three Arrows Capital Blowup (June 2022)

In **mid-June 2022**, Three Arrows Capital (3AC) — the Singapore-based hedge fund founded by Su Zhu and Kyle Davies, peak AUM $10B+ — collapsed under cascading margin calls triggered by the Terra/Luna implosion (May 2022) and the stETH depeg (June 13). The fund's failure crystallized the GBTC discount, drove BTC from $30k to $17k in 10 days, and ultimately resulted in losses to creditors estimated at **$3-4B**. For arbitrageurs positioned correctly, 3AC's forced liquidations created the best block-trade and basis-arbitrage opportunities of the entire 2022 crypto bear market.

## Background

3AC was founded by **Su Zhu and Kyle Davies** (Andover/Columbia classmates) in 2012, initially as an FX arbitrage shop. Pivoted to crypto ~2017; became a dominant force by 2020-2021. Strategies included:

- **GBTC premium arb** (2017-2021) — buy BTC, lock up via in-kind creation in Grayscale Trust, unlock 6 months later, sell at premium. See [[gbtc-discount-arbitrage]].
- **stETH-ETH basis** — long stETH (no withdrawal mechanism pre-Shapella), funded by leveraged ETH.
- **DeFi yield farming** with leverage on top.
- **OTC lending** at very high rates from Genesis, BlockFi, Voyager, Celsius — borrowed billions to fund leveraged positions.

By Q1 2022, 3AC had:
- Estimated $10B AUM at peak.
- Massive long stETH (later depegged).
- Massive long Luna/UST (collapsed May 2022).
- $300M+ lockup in GBTC (now at -25% discount and worsening).
- $200M+ in Avalanche/Axie Infinity tokens (down 80%+).
- $1B+ in unsecured borrowings from CeFi lenders.

## The Cascade

**May 2022 — Terra/Luna collapse:**
- 3AC reportedly held $200-560M Luna at peak (varies by source).
- All wiped to zero May 9-12, 2022.
- See [[2022-05-terra-luna-depeg-arb]].

**June 7, 2022 — Voyager Digital warning:**
- Voyager loaned 3AC $670M (15,250 BTC + 350M USDC).
- Voyager publicly disclosed concerns about 3AC repayment ability.

**June 13, 2022 — stETH depeg:**
- stETH/ETH from 0.9995 to 0.9346 (-6.5%) on June 13.
- 3AC held large leveraged stETH; mark-to-market hit on stETH PLUS the ETH borrowed against it.
- Forced selling of stETH on Curve 3pool further depressed prices in cascade.
- See [[2022-06-steth-depeg]].

**June 15, 2022 — Margin calls:**
- 3AC failed margin calls at multiple lenders simultaneously.
- BlockFi liquidated 3AC's pledged collateral.
- Genesis began liquidating.

**June 17-22, 2022 — Public unraveling:**
- Su Zhu deleted social media; Davies went silent.
- 3AC failed to respond to lender calls.
- BTC dropped from $30k to $17.6k June 18 — partially driven by 3AC's forced liquidations.

**July 1, 2022 — Bankruptcy:**
- 3AC files for Chapter 15 bankruptcy in BVI.
- $3.5B owed to 27 creditors disclosed.
- Davies and Zhu reportedly fled to Bali / Dubai.

## Triangular Arbitrage Opportunities

Six distinct trade setups emerged:

**Trade 1: Block-trade buyers absorb 3AC liquidations.** Genesis, BlockFi, Voyager, Celsius liquidated 3AC's pledged collateral via OTC blocks at 5-15% discounts. Buyers (Cumberland, B2C2, Jump, GSR) absorbed at $19-22k BTC and held; recovered to $30k+ by August. Conservative estimate: $200-500M extracted across the multi-week unwind.

**Trade 2: stETH-ETH convergence trade.** Long stETH at 0.935 ETH on June 13; hold to Shapella (Apr 2023); convergence to ~1.000 ETH = +7% return over 10 months risk-free. Specialist DeFi funds (Wave Financial, Galaxy, Pantera) extracted hundreds of millions.

**Trade 3: GBTC discount widening short.** Short GBTC vs long spot BTC; the discount widened from -19% to -49% over 2022. Specialist arbs profited from the widening; forced unwind eventually compressed it post-ETF-conversion January 2024.

**Trade 4: Funding rate cascade arbitrage.** Perp funding rates on BTC/ETH spiked extremely negative (-0.10%/8h, -110% APR) during the June panic. Long perps + short futures captured 50-100% APR for 1-2 weeks.

**Trade 5: Unsecured lender short-thesis.** BlockFi (-$80B AUM gone), Voyager, Celsius all collapsed within months of 3AC's failure. Specialists who shorted these names' equity (or bet against their CEX tokens) made multi-x returns.

**Trade 6: Distressed claim arbitrage.** 3AC creditor claims traded on secondary OTC at 10-20¢ in late 2022; some Genesis claims reportedly recovered 50-70¢ via the 2024 settlement. See [[bankruptcy-claim-arbitrage]].

## Winners

**Distressed-block-trade buyers** — Cumberland, B2C2, Jump, GSR collectively extracted $400-800M from absorbing 3AC's forced selling.

**stETH convergence funds** — Wave, Galaxy Digital, Pantera Capital reported large recovery on the 2022-2023 stETH trade.

**GBTC discount arbs** — Funds including Bracebridge, Strategic Capital extracted significant profits as the discount eventually closed January 2024.

**Tail-risk hedgers** — Funds like Capstone, Ambrus Group, etc. that ran long-gamma DeFi-tail-risk books extracted significant alpha.

**Singapore Monetary Authority** — Reputational win for tighter post-3AC oversight that other regulators emulated.

## Losers

**3AC creditors:**
| Creditor | Approximate Exposure |
|----------|----------------------|
| Genesis Global Trading | $2.36B |
| Voyager Digital | $670M |
| Celsius | $1B+ (estimated) |
| BlockFi | $80M+ |
| Sam Trabucco / Alameda | undisclosed (FTX collapsed Nov 2022 partly due to similar leverage; some via 3AC) |
| Various crypto lenders | $300M+ combined |

**Total creditor losses estimated at $3-4B.**

**Voyager Digital** — Bankrupt July 5, 2022 (3 weeks after 3AC).

**BlockFi** — Bankrupt November 2022 (5 months after 3AC).

**Celsius** — Bankrupt July 13, 2022 (29 days after 3AC).

**Genesis (DCG subsidiary)** — Massive losses; eventually filed bankruptcy January 2023; DCG's parent Grayscale survived but with severe stress.

**Su Zhu** — Arrested in Singapore September 2023 on trustee contempt charges; sentenced to 4 months prison.

## Aftermath

- **July 2022:** Multiple CeFi lenders fail in cascading collapses.
- **November 2022:** FTX collapse — partially traceable to similar leverage cascade.
- **December 2022:** GBTC discount peaks at -49%.
- **January 2023:** Genesis files for bankruptcy.
- **June 2023:** SEC charges Genesis, Gemini Earn for unregistered securities.
- **September 2023:** Su Zhu arrested in Singapore.
- **January 2024:** GBTC converts to spot BTC ETF; discount closes.
- **2024-2025:** Estate liquidations continue; secondary claim trading active.

## Lessons for Crypto Traders

1. **Multi-venue concentration without aggregate visibility = systemic failure pattern.** Same lesson as Archegos 2021; 3AC borrowed from many lenders, none saw the full book.
2. **CeFi unsecured lending was systemic risk.** Genesis, BlockFi, Voyager, Celsius all extended billions on Su Zhu/Davies' name and reputation alone — collateral was minimal or nonexistent.
3. **Leverage on illiquid collateral is the crash vector.** GBTC, stETH (pre-Shapella), Luna, Avalanche tokens — all illiquid in stress. 3AC borrowed cash against them.
4. **Forced-seller cascades create the year's best entry prices.** BTC bottom $17.6k June 18, 2022; recovered to $32k within 60 days.
5. **Distressed claim trading is recurring.** Mt. Gox (2014→2024), Lehman (2008→2014), Madoff (2008→2024), 3AC/Celsius/FTX (2022→ongoing) — patient capital extracts the recovery delta.
6. **Convergence trades pay off given patience.** stETH at 0.935 to 1.000 took 10 months; stETH funders earned ~7% with structured downside.

## Sources

- Three Arrows Capital, *Chapter 15 BVI Bankruptcy Filing* (July 1, 2022).
- *Voyager Digital Form 10-K* and bankruptcy filings.
- Singapore Monetary Authority enforcement notices on 3AC.
- *Bloomberg Crypto*, *The Block*, *CoinDesk* contemporaneous June-August 2022 coverage.
- Su Zhu Twitter/X archive (largely deleted June 2022).

## Related

[[liquidation-cascade-arbitrage]] · [[gbtc-discount-arbitrage]] · [[2022-06-steth-depeg]] · [[2022-05-terra-luna-depeg-arb]] · [[2021-2022-gbtc-discount]] · [[bankruptcy-claim-arbitrage]] · [[block-trade-flipping-arbitrage]] · [[archegos-blowup-2021]]
