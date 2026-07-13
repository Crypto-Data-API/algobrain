---
title: "Basel III"
type: concept
created: 2026-07-02
updated: 2026-07-02
status: good
tags: [risk-management, regulation, bonds]
aliases: ["Basel III", "basel-iii", "Basel 3", "Basel Accords"]
related: ["[[credit-risk]]", "[[leverage]]", "[[risk-management]]", "[[systemic-risk]]", "[[liquidity-risk]]", "[[stress-test]]", "[[too-big-to-fail]]", "[[bank-run]]", "[[global-financial-crisis]]", "[[bonds]]", "[[regulation]]"]
domain: [risk-management]
prerequisites: ["[[credit-risk]]", "[[leverage]]"]
difficulty: advanced
---

**Basel III** is the international regulatory framework for bank **capital**, **leverage**, and **liquidity** developed by the Basel Committee on Banking Supervision (BCBS), which sits at the Bank for International Settlements (BIS) in Basel, Switzerland. Agreed in the aftermath of the 2007–2009 [[global-financial-crisis|global financial crisis]], it strengthened and extended the earlier Basel I (1988) and Basel II (2004) accords by requiring banks to hold more, and higher-quality, capital against their risks; capping their overall [[leverage]]; and — for the first time in a global standard — imposing minimum **liquidity** requirements so a bank can survive a funding run without collapsing. Basel standards are not law in themselves; they are recommendations that member jurisdictions (the US, EU, UK, Japan and others) transpose into their own binding rules.

## Overview

The crisis exposed two fatal weaknesses in how banks were regulated. First, many banks were **thinly capitalised** in real terms: their headline capital ratios looked adequate, but much of the "capital" was low-quality (hybrid instruments, deferred tax assets, goodwill) that absorbed no losses when trouble came, and their [[leverage]] — total assets relative to genuine equity — was enormous. Second, several failed not because they ran out of capital but because they ran out of **cash**: they had funded long-dated, illiquid assets with very short-term wholesale borrowing that evaporated overnight (a wholesale [[bank-run]]). Basel III attacks both problems at once, and adds a **macroprudential** layer aimed at the [[systemic-risk|system as a whole]] rather than just each bank in isolation.

Basel III is built on three reinforcing pillars, in the tradition of Basel II:

- **Pillar 1 — minimum requirements.** Quantitative floors for capital, leverage, and liquidity (the ratios described below).
- **Pillar 2 — supervisory review.** Bank-specific add-ons set by regulators through supervisory judgement and [[stress-test|stress testing]], covering risks Pillar 1 does not fully capture.
- **Pillar 3 — market discipline.** Standardised public disclosure so investors and counterparties can compare banks' risk and capital positions.

## Capital requirements

The core of Basel III is the requirement to hold **regulatory capital** — loss-absorbing equity and equity-like instruments — against **risk-weighted assets (RWA)**. RWA is the denominator that scales an asset by how risky it is: cash and government bonds carry very low or zero risk weights, while unsecured corporate or retail loans carry much higher ones (see [[credit-risk]] for the standardised and internal-ratings-based approaches that produce these weights, alongside charges for market risk and operational risk). Capital ratios are therefore expressed as *capital ÷ RWA*.

Capital is stratified by loss-absorbing quality:

- **Common Equity Tier 1 (CET1)** — the highest-quality, most loss-absorbing capital: common shares and retained earnings, net of regulatory deductions. This is the number analysts and regulators watch most closely.
- **Additional Tier 1 (AT1)** — perpetual instruments that absorb losses on a going-concern basis, most notably contingent-convertible bonds ("CoCos") that convert to equity or write down when CET1 falls through a trigger. CET1 + AT1 = **Tier 1 capital**.
- **Tier 2** — "gone-concern" capital such as subordinated term debt that absorbs losses only in wind-down. Tier 1 + Tier 2 = **Total capital**.

### The Pillar-1 minimum ratios

Basel III sets the following minimum ratios of capital to RWA (these are the standard, widely-published headline minimums):

- **CET1 ≥ 4.5%** of RWA
- **Tier 1 ≥ 6%** of RWA
- **Total capital ≥ 8%** of RWA (unchanged in headline terms from Basel I/II, but backed by far stricter definitions of what counts)

### Buffers on top of the minimums

Basel III's real tightening came less from the minimums than from a stack of **buffers** — all met with CET1 — that sit above them. Breaching a buffer does not close a bank, but it automatically **restricts distributions** (dividends, buybacks, and discretionary bonuses), which is precisely the lever that connects bank regulation to shareholder returns:

- **Capital conservation buffer — 2.5%** of RWA. A permanent CET1 buffer above the minimum; dipping into it triggers graduated caps on payouts. This lifts the *effective* CET1 requirement for most banks to **7%** (4.5% + 2.5%).
- **Countercyclical capital buffer (CCyB) — 0% to 2.5%.** A time-varying, jurisdiction-set CET1 add-on that regulators raise in credit booms (to build a cushion and lean against exuberant lending) and release in downturns. This is Basel III's key **macroprudential** tool.
- **G-SIB surcharge — typically 1% to 3.5%.** An extra CET1 requirement on **global systemically important banks**, scaled to a bank's size, interconnectedness, complexity, and cross-border activity — an explicit charge for the [[too-big-to-fail]] externality. (Many jurisdictions apply an analogous D-SIB surcharge to domestically important banks.)

### The leverage ratio

Because risk-weighting can be gamed or simply wrong — pre-crisis models assigned trivial weights to assets that later blew up — Basel III adds a **non-risk-weighted leverage ratio** as a backstop:

- **Leverage ratio = Tier 1 capital ÷ total exposure measure (on- and off-balance-sheet), with a minimum of 3%.**

Because the denominator ignores risk weights entirely, the leverage ratio catches a bank that has quietly loaded up on "low-risk" assets that RWA understates. G-SIBs face an additional **leverage-ratio buffer** on top of the 3% floor. The leverage ratio is deliberately simple and hard to arbitrage, and in practice it — rather than the risk-based ratio — is the binding constraint for some large, low-risk-weight balance sheets.

## Liquidity requirements

Basel III introduced two entirely new global liquidity standards to address the funding-run problem that capital rules alone cannot solve:

- **Liquidity Coverage Ratio (LCR) — ≥ 100%.** A bank must hold enough **high-quality liquid assets (HQLA)** — cash, central-bank reserves, and top-grade government [[bonds]] — to cover its **total net cash outflows over a 30-day** acute stress scenario. In formula terms, `LCR = HQLA ÷ net cash outflows over 30 days ≥ 100%`. The LCR is the short-term, survive-the-run standard.
- **Net Stable Funding Ratio (NSFR) — ≥ 100%.** Over a one-year horizon, a bank's **available stable funding** (equity and reliable, longer-term liabilities) must cover its **required stable funding** (the funding its assets need, weighted by how illiquid and long-dated they are): `NSFR = available stable funding ÷ required stable funding ≥ 100%`. The NSFR is the structural, don't-fund-long-assets-with-hot-money standard.

Together the LCR and NSFR force banks to reduce **maturity transformation** — the practice of borrowing short and lending long that makes banks profitable but fragile (see [[liquidity-risk]]).

## Basel III finalization ("Basel III Endgame")

The 2010 package was followed by a further set of reforms agreed by the BCBS in **December 2017**, formally the *finalisation* of Basel III but universally nicknamed the **"Basel III Endgame."** Its central purpose is to reduce unwarranted variability in RWA — the concern that two banks holding identical portfolios could report very different risk-weighted assets because their internal models differed. The main elements are:

- **Output floor — 72.5%.** A bank using its own internal models to compute RWA cannot report total RWA below 72.5% of what the **standardised approaches** would produce. This caps the capital saving a bank can extract from favourable internal modelling and puts a floor under model-driven optimism.
- **Constraints on internal models** — removing or restricting the internal-ratings-based approach for certain low-default portfolios (e.g. large corporates, banks) where models are unreliable, and revising the standardised approaches for credit, [[market-risk]], and operational risk to be more risk-sensitive.
- **Revised operational-risk and CVA frameworks** — a single standardised measurement approach for operational risk, and updated capital for credit-valuation-adjustment (counterparty) risk on derivatives.

### US implementation debate

Implementation of the Endgame has been contentious, especially in the United States. A **2023 US proposal** to transpose the rules drew heavy pushback from banks, which argued the higher capital requirements would raise the cost and reduce the availability of lending (mortgages, small-business credit) without a commensurate stability benefit; consumer and market-structure groups pushed back the other way. Regulators subsequently signalled a **re-proposal with materially lower capital increases**, and timelines have slipped repeatedly. As of mid-2026 the final US calibration and start date remain unsettled, and the EU and UK have likewise phased in their versions on adjusted timetables. The unresolved question — how much capital is "enough" versus a drag on credit — is the live policy fault line in bank regulation.

## Why it matters to investors

Basel III is not just a compliance topic; it directly shapes the investment case for bank stocks and bank [[bonds]]:

- **It constrains leverage and therefore return on equity.** More required equity against the same assets mechanically lowers a bank's ROE (see roe), all else equal. Post-crisis bank ROEs are structurally below pre-crisis levels largely because [[leverage]] is capped. Valuation multiples (price-to-book) reflect this: a bank earning a return only modestly above its cost of equity will trade near or below book value.
- **It gates capital return.** A bank's capacity to pay dividends and fund buybacks is a function of its CET1 headroom above the buffer stack. In the US this is enforced through the Federal Reserve's annual **supervisory [[stress-test|stress tests]]** (the CCAR/DFAST exercises), which set a bank's **stress capital buffer** and effectively cap payouts. Buyback and dividend announcements from large banks are, in practice, reads on their post-stress-test capital position.
- **It affects lending capacity and credit supply.** Higher capital and liquidity requirements can make some activities (certain trading, long-dated or capital-intensive lending) less economic, shifting them either off bank balance sheets or into non-bank lenders ("shadow banks"). Investors track this as a driver of loan growth and net interest margin.
- **It underpins financial-sector stability.** For holders of bank equity and debt across the financials sector, stronger capital and liquidity buffers lower the probability of the sudden, wipe-out failures that characterised 2008 — though they cannot eliminate them, as later regional-bank failures showed when interest-rate and deposit-flight risks fell partly outside the framework's core focus.
- **It makes AT1/CoCo bonds a distinct risk class.** Contingent-convertible AT1 bonds absorb losses *before* a bank fails, so they can be written down or converted while the bank is still a going concern — a feature that surprised some holders in past bank resolutions and that must be priced separately from senior bank debt.

## Relationship to other frameworks

Basel III is the capital-and-liquidity core, but it interacts with adjacent post-crisis regimes: **resolution and TLAC/MREL** rules (total loss-absorbing capacity — how much bail-in-able debt a G-SIB must hold so it can fail without a taxpayer rescue), and jurisdiction-specific statutes such as the US **Dodd-Frank Act** that layer on stress testing, living wills, and prudential standards. Together these form the architecture built to make banks both harder to break ([[systemic-risk]] reduction) and safer to let fail.

## Related

- [[credit-risk]] — the standardised and internal-ratings-based approaches that produce credit RWA, the largest capital charge for most banks
- [[leverage]] — what the leverage ratio and capital minimums directly constrain
- [[liquidity-risk]] — the funding-run risk that the LCR and NSFR are designed to contain
- [[stress-test]] — supervisory stress testing (CCAR/DFAST), which sets buffers and gates capital return
- [[systemic-risk]], [[too-big-to-fail]] — the system-wide concerns behind the G-SIB surcharge and countercyclical buffer
- [[bank-run]] — the failure mode the liquidity standards address
- [[global-financial-crisis]] — the 2007–2009 crisis that prompted Basel III
- [[bonds]] — HQLA (government bonds) and the AT1/Tier 2 instruments that count as regulatory capital
- [[regulation]] — the broader regulatory context

## Sources

- Basel Committee on Banking Supervision (BCBS) / Bank for International Settlements (BIS) published standards — the *Basel III: A global regulatory framework for more resilient banks and banking systems* (2010, rev. 2011) capital text; the LCR (2013) and NSFR (2014) liquidity standards; the leverage-ratio framework; and *Basel III: Finalising post-crisis reforms* (December 2017), which introduced the 72.5% output floor. The minimum ratios cited (CET1 4.5%, Tier 1 6%, Total 8%, capital conservation buffer 2.5%, CCyB 0–2.5%, leverage ratio 3%, LCR/NSFR ≥ 100%) are the standard published Basel III minimums.
- General, widely-taught bank-regulation and risk-management knowledge (e.g. Hull, *Risk Management and Financial Institutions*), for the framing of capital tiers, RWA, maturity transformation, and the three-pillar structure.
