---
title: "Strategy Inc. (MicroStrategy)"
type: entity
created: 2026-04-13
updated: 2026-06-19
status: excellent
tags: [company, options, derivatives, crypto, bitcoin]
entity_type: company
founded: 1989
headquarters: "Tysons Corner, Virginia, USA"
website: "https://www.strategy.com"
aliases: ["MSTR", "Strategy Inc. (MicroStrategy)", "MicroStrategy", "Strategy Inc."]
ticker: "MSTR"
exchange: "NASDAQ"
sector: "Bitcoin Treasury"
industry: "Bitcoin Treasury"
sp500: false
options_liquidity_tier: "Tier 1 - Ultra Liquid"
options_volume: "Extremely High"
related: ["[[bitcoin]]", "[[crypto-trading]]", "[[gamma-scalping]]", "[[gamma-squeeze]]", "[[implied-volatility]]", "[[options]]", "[[options-greeks]]", "[[short-squeeze]]", "[[volatility]]"]
---

Strategy Inc., formerly MicroStrategy (NASDAQ: MSTR), is a business intelligence software company founded in 1989 by Michael Saylor and headquartered in Tysons Corner, Virginia. Beginning in August 2020, the company adopted a [[bitcoin]] treasury strategy and has since become the largest corporate holder of bitcoin in the world — **~845,000 BTC as of June 2026** — funded through repeated equity and convertible-debt issuance. MSTR effectively trades as a leveraged [[bitcoin]] proxy, with extreme implied [[volatility]] and one of the most actively traded options chains in the entire US equity market.

## Business Overview

Strategy has two faces. The legacy business is enterprise **business-intelligence and analytics software** (now AI-augmented), a small, roughly flat-to-declining revenue line (~$450-500M annually) that is largely irrelevant to the share price. The dominant identity is a **bitcoin treasury vehicle**: the company raises capital via at-the-market equity sales, convertible notes, and preferred stock, then converts the proceeds into bitcoin. Management tracks bespoke metrics such as "BTC Yield" (bitcoin per share accretion) and frames the equity as a way for capital-markets investors to gain leveraged, securitized bitcoin exposure. Because the float trades at a premium to the net asset value of its bitcoin (the "mNAV" premium), Strategy can issue stock above NAV and buy more BTC accretively — a flywheel that works while the premium and BTC price hold, and reverses violently when they don't.

## Business Segments

| Segment | What it is | Role in the story |
|---|---|---|
| **Bitcoin treasury** | The accumulated [[bitcoin]] balance and the capital-markets machine (ATM equity, convertibles, preferreds) that funds it | The thesis — essentially the entire equity value |
| **Enterprise analytics software** | Legacy [[business-intelligence]] / BI platform, now AI-augmented; recurring + cloud subscription mix | A small, slow-growing cash-generative business that anchors the corporate shell but is a rounding error vs. the BTC stack |

The software business matters for two narrow reasons: it provides operating cash flow and a legitimate operating company "wrapper" that keeps Strategy classified as an operating company (not an investment company), and it occasionally supplies a modest non-BTC catalyst. For price-formation purposes, however, **the analytics segment is noise and bitcoin is signal**.

## The mNAV Premium Flywheel (and its reverse)

The defining mechanic of MSTR is the **multiple-to-net-asset-value (mNAV) premium** — the gap between the company's market capitalization and the spot value of its [[bitcoin]] holdings (net of debt):

- **Forward flywheel:** when MSTR trades *above* the value of its BTC per share, management issues equity at that premium and uses the cash to buy more bitcoin. Each issuance is **accretive to BTC-per-share** ("BTC Yield"), which justifies the premium, which enables more issuance — a self-reinforcing loop that works while BTC rises and the premium holds.
- **Reverse flywheel:** when the premium collapses (BTC falls, sentiment sours, or dilution fatigue sets in), issuing equity becomes dilutive rather than accretive, the funding engine stalls, and the equity can fall *more* than bitcoin because both the BTC price and the premium-to-NAV contract at once. This double-compression is the core structural risk.
- **Convertible & preferred layer:** the convertibles add embedded optionality (conversion above strike) and the preferreds (STRK/STRF-style perpetuals) add a fixed-charge layer ahead of common equity — broadening the capital base but introducing senior claims and refinancing/coverage considerations in a deep BTC drawdown.

## Competitive Positioning / Peers

MSTR sits at the apex of the listed "bitcoin-equity" complex. It offers the largest, most liquid, securitized, leveraged BTC exposure available in size.

| Company | Overlap with MSTR | Contrast |
|---|---|---|
| Spot [[bitcoin]] ETFs (e.g. IBIT) | Direct BTC price exposure | No leverage, no mNAV premium, no issuance flywheel — a "clean" 1x proxy |
| [[mara]] (MARA) | Large corporate BTC holder + miner | Earns/produces BTC via mining; operational + energy exposure |
| [[riot-platforms]] (RIOT) | Miner with BTC treasury | Mining-cost and power-contract sensitivity |
| [[core-scientific]] (CORZ) | Miner pivoting to HPC/AI hosting | Increasingly an AI-datacenter story, not a pure BTC proxy |
| [[cleanspark]] (CLSK) | Pure-play bitcoin miner | Operational beta to BTC + efficiency, not a treasury-premium model |
| [[iren]] (IREN) | Miner + AI/HPC compute | Diversifying away from pure BTC |
| GameStop (GME) | Adopted a [[bitcoin]] treasury (2025) | BTC is a small slice of a cash pile, not the whole thesis; a far milder NAV-premium dynamic |

The critical distinction versus miners is **mechanism**: miners *produce* bitcoin and carry energy/operational risk, whereas Strategy *buys* bitcoin with capital-markets proceeds and carries premium/dilution/refinancing risk. Versus spot ETFs, MSTR adds leverage and the premium — more upside in BTC bull phases, more downside in bear phases.

## Bull vs Bear Case

**Bull case**
- Largest, most liquid, securitized leveraged [[bitcoin]] exposure — accessible in tax-advantaged and options-enabled accounts that cannot hold spot BTC.
- Accretive issuance flywheel grows BTC-per-share when the premium holds.
- First-mover brand, index inclusion tailwinds, and a deep, sophisticated capital-markets apparatus (multiple convertible/preferred instruments).
- Optionality: a structural bid for BTC that has, at times, moved the underlying.

**Bear case**
- Double-leverage to sentiment: equity can fall more than BTC when the mNAV premium compresses alongside a BTC drawdown (the reverse flywheel).
- Persistent dilution; the BTC-per-share metric can still rise while *per-common-share* outcomes lag in stress.
- Senior claims from converts/preferreds sit ahead of common; refinancing and fixed-charge coverage matter in a prolonged bear market.
- The premium itself is reflexive and can evaporate quickly; there is no fundamental floor below the net BTC value, and the premium can briefly go negative.
- Single-asset concentration: the entire thesis rises and falls with one volatile asset.

## Valuation Framework (qualitative — the NAV-premium model)

Conventional multiples (P/E, EV/EBITDA) are meaningless for MSTR because GAAP earnings swing wildly with fair-value [[bitcoin]] accounting and the software segment is immaterial. The market values MSTR through a **net-asset-value-premium framework**:

1. **Net BTC asset value (the base):** spot [[bitcoin]] price × BTC held, less net debt and preferred claims. This is the tangible anchor.
2. **The mNAV premium (the variable):** the market routinely pays a *multiple* of net BTC value. That premium is a function of (a) expected future accretive issuance, (b) the convenience/leverage/optionality of the wrapper, and (c) sentiment toward BTC and toward Saylor's strategy.
3. **The implied leverage:** debt and preferreds amplify both directions; MSTR typically moves **1.5-2.5x the daily move of [[bitcoin]]**.

The single most important question for an MSTR investor is therefore *not* "what are earnings" but **"is the premium to net BTC value justified and sustainable, and is incremental issuance accretive at the current premium?"** When the premium is high, the flywheel funds accretion; when it compresses toward (or below) 1.0x NAV, the model stalls and downside accelerates.

## Capital Return & Allocation Policy

- **No common dividend.** All capital is directed toward [[bitcoin]] accumulation; the stated target has publicly approached ~1 million BTC.
- **Issuance, not return:** the capital policy is the inverse of a typical buyback/dividend story — Strategy is a serial *issuer* (ATM equity, convertibles, preferreds) by design, recycling proceeds into BTC.
- **Preferred dividends:** the perpetual preferred instruments (STRK/STRF-style) carry their own coupons, a fixed charge that ranks ahead of common — a genuine cash obligation independent of BTC's price.
- **No bitcoin sales policy:** management frames the BTC as a permanent treasury reserve ("never selling"), reinforcing the one-way, accumulate-only allocation stance.

## Financials (as of June 2026, approximate)

> Not covered by the stockmarketapi fundamentals feed; figures below are approximate, from research.

- **Bitcoin holdings**: ~845,256 BTC (as of 7 June 2026), aggregate cost ~$63.97 billion, average cost ~$75,680/BTC.
- **Software revenue**: roughly $450-500 million per year, secondary to the treasury thesis.
- **Capital structure**: financed via ATM equity, multiple convertible-note tranches, and preferred equity (e.g. STRK/STRF-style perpetuals); GAAP results swing wildly with fair-value bitcoin accounting (now mark-to-market under updated rules).
- **Stated target**: management has publicly aimed toward accumulating ~1 million BTC.

## 2025-2026 Developments

- Continued aggressive accumulation through 2025 into 2026, crossing **800,000+ BTC** (818,334 reported late April 2026) and reaching **~845,000 BTC by early June 2026**; aggregate bitcoin value hit record levels (~$63B+).
- Funding via successive equity ATM programs and new preferred-stock instruments designed to widen the capital base without diluting the BTC-per-share metric as fast as common-only issuance would.
- The mNAV premium, dilution pace, and bitcoin price remain the three swing variables; sharp BTC drawdowns compress the premium and amplify equity downside (and vice versa on rallies).

## Options Trading Profile

**Liquidity Tier:** Tier 1 - Ultra Liquid
**Avg Daily Options Volume:** Extremely High

Leveraged BTC exposure; extreme IV; widely used for Bitcoin proxy options at all strikes

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | NASDAQ: MSTR |
| **Sector** | Bitcoin Treasury |
| **Options Tier** | Tier 1 - Ultra Liquid |
| **Options Volume** | Extremely High |

## Trading & Options Playbook

**Index / ETF membership**
- A nasdaq-listed large-cap; has been added to major large-cap indices, which created mechanical buy-flow on inclusion and makes MSTR a meaningful component of technology-tilted and Nasdaq-tracking ETFs.
- Functions as the de facto "bitcoin equity" in many index and thematic baskets; inclusion/exclusion events are themselves catalysts because of the leveraged-BTC profile they add to a fund.

**Volatility behavior**
- Among the highest [[implied-volatility]] of any liquid US large-cap, driven by the 1.5-2.5x leverage to [[bitcoin]] plus the reflexive mNAV premium.
- IV expands sharply around BTC price swings, capital-raise announcements, and weekly purchase disclosures; the options surface is rich and actively arbitraged against spot BTC and BTC-ETF vol.

**Leveraged bitcoin proxy**
- MSTR typically moves **1.5-2.5x the daily move of [[bitcoin]]** given balance-sheet leverage and the mNAV premium; it is the highest-beta liquid bitcoin equity available in size, and the premium can add or subtract beyond the raw BTC beta.

**Catalysts calendar (event-driven)**
- Bitcoin spot price (the dominant driver, continuously).
- Weekly BTC-purchase disclosures (8-K filings) and BTC-Yield updates.
- New capital raises — ATM equity, convertible tranches, preferred issuance.
- Index inclusion/exclusion events.
- Changes to bitcoin fair-value accounting or tax treatment (e.g. corporate AMT considerations on unrealized gains).

**Options use**
- Extreme IV makes MSTR a favorite for [[gamma-scalping]], [[gamma-squeeze]] setups, covered calls written against BTC exposure, put-protection on leveraged BTC longs, and volatility-surface / dispersion trades against spot BTC.
- Correlated names for spreads and pairs: bitcoin miners and treasury proxies — [[mara]], [[riot-platforms]], [[core-scientific]], [[cleanspark]], [[iren]] — plus spot bitcoin ETFs and GME's smaller BTC sleeve.

## Risks

- **BTC drawdown** — the first-order risk; everything else amplifies it.
- **mNAV premium collapse** — the reverse flywheel; a premium-to-NAV reversal can drive equity losses well beyond the underlying bitcoin move, and the premium can briefly fall below 1.0x.
- **Dilution overhang** — continuous issuance caps per-common-share upside and can fatigue the bid.
- **Refinancing / conversion dynamics** — convertibles and preferreds introduce senior claims, fixed charges, and refinancing risk in a sustained bear market.
- **Concentration & key-person risk** — a single-asset thesis tied closely to Michael Saylor's strategy and continued capital-markets access.

## Related

- [[bitcoin]]
- [[crypto-trading]]
- [[gamma-scalping]]
- [[gamma-squeeze]]
- [[implied-volatility]]
- [[options]]
- [[options-greeks]]
- [[short-squeeze]]
- [[volatility]]
- [[mara]]
- [[riot-platforms]]
- [[core-scientific]]
- [[iren]]
- [[cleanspark]]

## Sources

- (Source: stockmarketapi-options-stocks-2026-04-13)
- Strategy bitcoin holdings tracker (bitcointreasuries.net): https://bitcointreasuries.net/public-companies/strategy
- Strategy bitcoin purchases (Bitbo treasuries): https://bitbo.io/treasuries/microstrategy
- Strategy 8-K bitcoin purchase disclosures (SEC): https://www.sec.gov/Archives/edgar/data/0001050446/000119312526249768/mstr-20260530.htm
- Verified via WebSearch, 2026-06-10
