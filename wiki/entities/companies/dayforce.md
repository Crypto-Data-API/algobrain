---
title: "Dayforce"
type: entity
created: 2026-04-13
updated: 2026-06-19
status: excellent
tags: [company, sp500, stocks]
entity_type: company
aliases: ["DAY", "Dayforce Inc.", "Ceridian"]
website: "https://www.dayforce.com"
headquarters: "Minneapolis, Minnesota, USA"
ticker: "DAY (delisted 2026-02-04)"
exchange: "NYSE (delisted)"
sector: "Industrials"
sp500: false
related: ["[[industrials]]", "[[s-and-p-500]]", "[[automatic-data-processing]]"]
fundamentals_updated: 2026-06-10
fundamentals_period_end: 2024-12-31
fundamentals_source: stockmarketapi
debt_to_equity: 0.47
ebitda_margin_5y_avg: 0.1033
roe_5y_avg: -0.0081
roa_5y_avg: -0.0023
data_completeness_pct: 100
fred_profile: "Value with concerns"
---

Dayforce (formerly Ceridian HCM) was a human capital management (HCM) software company — payroll, workforce management and HR on the Dayforce platform — that traded on NYSE/TSX as DAY until **Thoma Bravo completed a $12.3B take-private at $70.00/share cash on 2026-02-04**. DAY no longer trades; the page is retained as a historical record and merger-arbitrage case study.

## Take-Private by Thoma Bravo (2025–2026)

- **2025-08-21:** Dayforce entered a definitive agreement with Thoma Bravo (with a significant minority investment from Abu Dhabi's Mubadala) to go private at **$70.00 per share in cash**, ~$12.3B enterprise value — one of 2025's largest software LBOs.
- **2025-11-12:** stockholders approved the deal at the special meeting.
- **2026-02-04:** acquisition completed; common stock ceased trading and was delisted from the NYSE and Toronto Stock Exchange; Dayforce was removed from the [[s-and-p-500]] (it had only joined the index in 2024).
- **Trader takeaway:** a clean all-cash arb — the spread compressed steadily from announcement through the shareholder vote; the main risk priced was regulatory review of the Mubadala co-investment. Exposure to the HCM space now runs through [[automatic-data-processing]], Paychex, Paycom, Paylocity and [[workday]].

### Merger-arbitrage case study

DAY is a useful, recent template for a **definitive all-cash take-private** arb. The deal had the features arbs prefer:

- **All-cash, fixed price ($70.00):** no exchange ratio, no equity stub, no collar — the payoff is binary (deal closes at $70 vs deal breaks). Downside on a break would have been a re-rating to the standalone trading multiple of an unprofitable-on-GAAP SaaS name in a soft software tape.
- **Spread mechanics:** post-announcement the stock traded at a discount to $70 reflecting (a) time value of money to expected close and (b) deal-break probability. The annualized return on the spread is the arb's edge; it compressed as milestones de-risked the deal.
- **De-risking milestones:** definitive agreement signed (2025-08-21) → shareholder vote approved (2025-11-12) → regulatory clearance → close (2026-02-04). Each cleared milestone narrowed the spread.
- **The priced risk:** the **Mubadala (Abu Dhabi sovereign) co-investment** raised potential **CFIUS / foreign-investment review** scrutiny — the principal reason the spread did not collapse to near-zero immediately. Once clearances landed, the spread closed to the deal price.
- **Financing risk:** as a sponsor LBO (Thoma Bravo), there was theoretical debt-financing risk, but committed financing and a strong sponsor kept this minor.

This is a textbook example of why merger-arb is described as *picking up the last few percent in front of a binary event*: most of the time the deal closes and you earn the spread; occasionally it breaks and you take an outsized loss. See [[event-driven]] approaches for the broader playbook.

## Bull vs Bear Case (Historical, pre-deal)

**Bull case (why a sponsor wanted it):**
- High-recurring-revenue (~80%+) enterprise SaaS with sticky, mission-critical payroll workflows and high switching costs.
- Operating-leverage story: EBITDA margins were inflecting upward (see trend table), suggesting the platform had reached scale.
- Rate-driven float revenue provided a high-margin tailwind.
- Single-database architecture was a genuine product differentiator upmarket against modular rivals.

**Bear case (the discount the public market applied):**
- Persistent GAAP unprofitability and heavy stock-based compensation; net margin and ROE hovered near zero (see Fundamentals).
- A crowded HCM market with deep-pocketed incumbents ([[automatic-data-processing|ADP]], [[workday]]) and nimble mid-market rivals (Paycom, Paylocity).
- Float revenue would reverse as a headwind in a rate-cutting cycle.
- The take-private at $70 effectively settled the debate — a financial sponsor concluded the value was best realized away from public-market scrutiny.

## Valuation Framework (qualitative, Historical)

While listed, DAY was valued on **EV/revenue and EV/recurring-revenue** like other enterprise SaaS, with the multiple driven by: revenue growth rate, the cloud-recurring mix, net dollar retention, and the *path to durable GAAP profitability*. The float-revenue line added a rate-sensitive overlay that most pure-software names lack. The Thoma Bravo bid put a definitive private-market value on the franchise; the public multiple before the bid embedded the market's skepticism about margin durability.

## Risks (Historical)

- **Deal/regulatory risk (while pending):** the CFIUS angle from the Mubadala co-investment was the live risk during the arb window.
- **Competitive risk:** entrenched incumbents and well-funded mid-market challengers in HCM.
- **Profitability risk:** thin/zero GAAP margins and high stock-based comp left little cushion.
- **Rate sensitivity:** float revenue cut both ways with interest rates.
- **Post-close:** the equity no longer exists publicly; there is no listed-stock risk to manage — the page is a historical and merger-arb reference only.

## Business (Historical)

Ceridian, a decades-old payroll processor, was transformed after the 2012 acquisition of Dayforce (founded by David Ossip, who became CEO); it IPO'd in 2018 and renamed itself Dayforce Inc. in 2024. The pitch: a single real-time database for HR/payroll/workforce management with continuous pay calculation, competing against ADP, Workday, UKG and Paycom. At the time of the deal it served ~6.9k+ customers with recurring revenue around 80%+ of total and FY2024 revenue of ~$1.76B (see fundamentals below).

### Business Segments (Historical)

Dayforce's economics were classic enterprise SaaS layered on a payroll-processing legacy:

| Line | What it was | Trader note |
|---|---|---|
| **Dayforce recurring (cloud)** | Subscription HCM platform — payroll, benefits, time/attendance, talent, workforce management on one real-time database | The growth engine and the reason for the SaaS multiple; ~80%+ recurring revenue |
| **Float revenue** | Interest earned on client funds held briefly between payroll collection and disbursement | A rate-sensitive, high-margin kicker — rose with interest rates in 2023-2024, a structural feature shared with [[automatic-data-processing|ADP]] and Paychex |
| **Powerpay / legacy Ceridian** | Older, lower-growth payroll products being wound down or migrated | A declining drag the bull thesis assumed would shrink to irrelevance |
| **Professional services** | Implementation and configuration revenue (lower margin) | Lumpy; a leading indicator of future recurring revenue as new logos go live |

The key SaaS levers were **net dollar retention**, **new-logo bookings**, **per-employee-per-month (PEPM) pricing**, and the **cloud recurring revenue mix** — plus the rate-driven float kicker. Margin expansion (visible in the EBITDA trend below) was the central debate: bulls argued the platform had scale operating leverage; bears pointed to persistent GAAP unprofitability and heavy stock-based compensation.

### Competitive Positioning / Peers (Historical)

Dayforce sat in the crowded **human capital management (HCM)** software market, differentiating on a *single real-time database* and *continuous pay calculation* versus rivals that stitched together modules.

| Company | Relationship | Model |
|---|---|---|
| [[automatic-data-processing]] (ADP) | Largest incumbent | Scaled payroll + HCM; float-revenue beneficiary; the share-of-wallet target Dayforce attacked upmarket |
| Paychex | Incumbent | SMB-focused payroll/HCM; float-sensitive |
| [[workday]] | Enterprise rival | Cloud HCM + financials; competes for large-enterprise HR suites |
| Paycom | Mid-market rival | Single-database HCM; closest "modern stack" comp |
| Paylocity | Mid-market rival | Cloud HCM/payroll |
| UKG (private) | Direct rival | Workforce management + HCM (Ultimate + Kronos merger) |

Exposure to the HCM theme now runs through the listed names above, since DAY itself no longer trades.

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | NYSE: DAY (delisted 2026-02-04) |
| **Fate** | Acquired by Thoma Bravo for ~$12.3B ($70.00/share cash) |
| **Sector** | [[industrials|Industrials]] (GICS); functionally HCM software |
| **Headquarters** | Minneapolis, Minnesota |
| **CIK** | 0001725057 |


## Fundamentals

> **Note:** historical — final full fiscal year (FY2024) before the 2026-02-04 take-private. Retained for record.

*Source: [[stockmarketapi-fundamentals-2026-05-10]] · period end 2024-12-31 · primary sec_edgar · completeness 100% · pulled 2026-06-10*

### Snapshot

| Metric | Latest | 5y avg | Note |
|---|---|---|---|
| PE ratio | — | — | compare to sector / index avg |
| Gross margin | 46.1% | 40.9% | trend matters — rising = pricing power |
| Operating margin | 5.9% | 2.0% | — |
| EBITDA margin | 17.8% | 10.3% | >20% strong; >27% Fred's 'excellent' tier |
| Net margin | 1.0% | -1.8% | — |
| ROE | 0.7% | -0.8% | API uses book equity — high values reflect leverage / buybacks |
| ROA | 0.2% | -0.2% | Fred's bar: ≥5% |
| Debt-to-equity | 0.47x | — | Fred: <1.0 healthy, >2.0 leveraged (sector-adjusted) |
| Liabilities-to-equity | 2.58x | — | broader leverage |
| Current ratio | 1.13x | — | Fred: >2.0 (N/A for retail / staples / banks) |
| Quick ratio | — | — | Fred: >1.0 |
| Interest coverage | 2.6x | — | Fred: <1.5 dangerous, >3.0 comfortable |
| EPS (diluted) | 0.11 | — | — |
| Dividend per share | — | — | — |
| Dividend yield (API) | — | — | API definition — see source page; not directly = market yield |
| Dividend payout | — | — | — |

### 5-period trend

| Period | EBITDA margin | Operating margin | ROE | D/E |
|---|---|---|---|---|
| 2024-12-31 (FY) | 17.8% | 5.9% | 0.7% | 0.47x |
| 2023-12-31 (FY) | 17.5% | 8.8% | 2.3% | 0.50x |
| 2022-12-31 (FY) | 5.1% | -2.1% | -3.5% | 0.58x |
| 2021-12-31 (FY) | 4.1% | -3.5% | -3.4% | 0.50x |
| 2020-12-31 (FY) | 7.1% | 0.9% | -0.2% | 0.31x |

### Fred-framework view

**Profile:** *Value with concerns* — passes 1/7 of Fred's hurdles.

| Bar | Result | Value |
|---|---|---|
| ROA ≥5% | ✗ | -0.2% |
| ROE ≥15% | ✗ | -0.8% |
| Net margin ≥10% | ✗ | 1.0% |
| EBITDA margin ≥20% | ✗ | 10.3% |
| D/E ≤1.0 (Industrials bar) | ✓ | 0.47x |
| Current ratio ≥2 | ✗ | 1.13x |
| Interest coverage ≥3x | ✗ | 2.56x |

- **Suits:** deep-value portfolios that explicitly want to underwrite turnaround risk
- **Watch for:** permanent-impairment risk if multiple Fred bars stay broken across a cycle
- **Sector context:** Industrials — Fred's standard bars apply (D/E <1.0, current >2, interest coverage >3x).

## Related

- [[s-and-p-500]]
- [[industrials|Industrials]]
- [[automatic-data-processing]]
- [[allegion]]
- [[ametek]]
- [[a-o-smith]]
- [[axon-enterprise]]
- [[workday]]
- [[paycom]]

## Sources

- (Source: [[stockmarketapi-sp500-2026-04-13]])
- Thoma Bravo — completion of acquisition (2026-02-04): https://www.thomabravo.com/press-releases/thoma-bravo-completes-acquisition-of-dayforce
- Thoma Bravo — definitive agreement ($12.3B, $70/share, 2025-08-21): https://www.thomabravo.com/press-releases/dayforce-enters-into-us12.3-billion-definitive-agreement-with-thoma-bravo-to-become-a-private-company
- Completion press release (GlobeNewswire, 2026-02-04): https://www.globenewswire.com/news-release/2026/02/04/3232075/0/en/Thoma-Bravo-Completes-Acquisition-of-Dayforce.html
- Verified via Perplexity (sonar) and web search, 2026-06-10
