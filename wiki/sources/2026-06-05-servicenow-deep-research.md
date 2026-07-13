---
title: "Deep Research — ServiceNow (NOW) Fundamentals & Investment Analysis"
type: source
created: 2026-06-05
updated: 2026-06-05
status: good
tags: [meta, source, stocks, ai-trading, fundamental-analysis]
source_type: data
source_url: "n/a — deep-research workflow aggregating 20 sources (primary SEC filings + secondary)"
source_author: "Claude deep-research harness (5-angle fan-out, 3-vote adversarial verification)"
source_date: 2026-06-05
confidence: high
claims_count: 24
related:
  - "[[servicenow]]"
  - "[[alfred-fundamental-analysis]]"
  - "[[salesforce]]"
---

#meta

Deep-research run dated 2026-06-05 on ServiceNow (NYSE: NOW), scoped to feed [[alfred-fundamental-analysis|Fred's fundamental-analysis bars]]. Refreshes the [[servicenow]] entity page, whose prior fundamentals snapshot (2026-05-09, `stockmarketapi`) lacked debt-to-equity, quick ratio, interest coverage, and dividend data, and predated the 5-for-1 split.

## Method

`deep-research` workflow: 5 search angles → 20 sources fetched → 75 claims extracted → top 25 verified via 3-vote adversarial verification (2/3 refutes to kill). **24 confirmed 3-0, 1 refuted.** 102 agent calls. Most financial figures confirmed verbatim against **primary SEC filings** (FY2025 10-K, ARS, Q4 8-K, Q1 FY2026 8-K) — high confidence.

## Underlying sources

| Quality | Sources |
|---|---|
| **Primary** | FY2025 10-K (`now-20251231.htm`), FY2025 Annual Report (`now2025ars.pdf`), Q4/FY2025 8-K (`erq4fy25.htm`), Q1 FY2026 8-K (`erq1fy26.htm`), ServiceNow newsroom press release |
| **Secondary** | stockanalysis.com (balance sheet, statistics), io-fund, Benzinga (BofA NOW vs CRM), MarketBeat (analyst forecast), The Register (ITSM battle) |
| **Blog/unreliable** | businesswire, macrotrends, gurufocus, fullratio (filtered, 0 claims) |

## Key verified claims (all 3-0 unless noted)

| Claim | Confidence | Basis |
|---|---|---|
| FY2025 revenue $13,278M (+20.9%), 97% subscription | HIGH | 10-K / ARS / 8-K / PR |
| Gross margin 77.5%, GAAP op margin 13.7% (non-GAAP 31%), net margin 13.2% | HIGH | Primary |
| GAAP diluted EPS $1.67 (vs $1.37 FY2024, +22%); non-GAAP $3.51 | HIGH | Primary; split-adjusted |
| FCF $4,636M (35% margin, non-GAAP); op cash flow $5,444M (41%) | HIGH | ARS / PR |
| Total assets $26,038M; equity $12,964M; cash $3,726M | HIGH | 10-K |
| LT debt $1,491M; total debt incl. leases ~$2,403M; D/E ~0.12–0.19 | HIGH | 10-K + stockanalysis |
| Current assets $10,471M / current liabilities $10,443M → current ratio ~1.00 | HIGH | 10-K |
| Interest expense $23M → interest coverage ~79x; interest income $451M (net-interest-positive) | HIGH | 10-K |
| ROE 13.5% (period-end) / ~15.5% (average); ROA 6.7% | HIGH | Computed from primary |
| RPO $28.2B (+26.5%); cRPO $12.85B (+25%); renewal rate 98% | HIGH | 10-K / PR |
| Q1 FY2026: revenue $3,770M (+22%), FCF margin 44%, GAAP EPS $0.45 | HIGH | Q1 8-K + transcript |
| Now Assist >$1M-ACV customers +130% YoY; 2026 incremental-AI target raised 50% to $1.5B | HIGH | Q1 8-K / transcript |
| Price $119.36, mkt cap $123.1B, EV $117.6B (Jun 4 2026, post 5-for-1 split Dec 17 2025) | MEDIUM | stockanalysis (secondary, drifts) |
| **No dividend**; capital return via buybacks ($5B additional auth. Jan 2026) | HIGH | PR |

## Refuted (excluded)

- **Q4-2025 standalone FCF of $2,032M / 57% margin** — refuted 0-3. The verified figure is the FY2025 FCF of $4,636M / 35%.

## Follow-up run (2026-06-05) — open questions closed

A second `deep-research` run (5 angles → 20 sources → 25 verified, **23 confirmed / 2 refuted**, 102 agents) targeted the four gaps below. Results:

| Gap | Finding | Confidence |
|---|---|---|
| **Valuation multiples** | Jun 4 2026: forward P/E ~27.5x, trailing P/E ~71x, EV/Sales ~8.4x, EV/EBITDA ~40.7x, PEG ~1.11, P/FCF ~26.6x (stockanalysis.com) | MEDIUM (secondary, drifts) |
| **Net revenue retention** | **NOT disclosed.** Only metric is ACV-based renewal rate **97% Q1 FY2026** (98% FY2025), 6th straight qtr 97–98%, incl. Moveworks. CFO: NRR "not trending significantly differently" | HIGH (primary 10-Q) |
| **Recognized AI revenue** | **$0 disclosed.** No AI revenue/segment line. Only ACV: Now Assist ACV ~$750M entering Q1 2026 (from ~$600M end-2025); >$1M-ACV customers +130% YoY; $1.5B is a forward ACV *commit* target, not revenue | HIGH (primary) |
| **Guidance & analysts** | FY2026 subscription guide raised to $15,735–15,775M (+22–22.5% rep / +20.5–21% cc); non-GAAP op margin 31.5% (cut from 32.0% for Armis), FCF margin 35% (cut from 36%); Q1 beat high end. Bernstein PT $236 (from $226), Outperform, ~May 6. Analyst Day 2030 targets: ~$30B subscription, Rule of 40 >60, ~30% of ACV from AI | HIGH (guide, primary) / MEDIUM (analyst) |

**Refuted in follow-up:** "Now Assist surpassed $100M ACV / $1.5B *pure AI revenue*" (0-3 — conflates ACV with revenue); a "~19.5–20% growth / 36% FCF" guidance variant (1-2 — superseded by the raised guide).

## Third run (2026-06-05) — benchmarks, analyst panel, moat (page → `good`)

A third `deep-research` run (5 angles → 20 sources → 25 verified, **21 confirmed / 4 refuted**, 102 agents) closed the last three gaps:

| Gap | Finding | Confidence |
|---|---|---|
| **Peer/index benchmarks** | S&P 500 fwd P/E **20.9x** (FactSet, May 1) → NOW ~27.5x = ~31% premium. Public-SaaS median EV/Rev **~3.4–3.6x** (Aventis) → NOW ~8.4x = ~2.5x median. Adobe peer: fwd P/E 10.7x / EV/Sales 4.3x (AI-fear compression). SaaS median fell 5.1x→3.4x through early 2026 | HIGH (index primary) / HIGH (SaaS secondary) |
| **Analyst consensus** | ~48 analysts; "Strong Buy" (stockanalysis) ↔ "Moderate Buy" (MarketBeat, 37 B/5 H/1 S). Avg target **~$141.86** (median ~$137.50) → ~16–19% upside. Range **$85 (KeyBanc) → $236 (Bernstein)**. Spring cuts: JPM $195→$145, MS $210→$180, Goldman $188→$163, BTIG $200→$185, Stifel $180→$135 (US federal spend) | HIGH |
| **Competitive moat** | ~40% ITSM share (IDC), 8,600 ITSM customers, ~6x next two (BMC Helix, Atlassian). MSFT = **coopetition** (AI Control Tower ↔ Foundry/Copilot Studio, Nov 2025). Salesforce Agentforce = system-of-action vs CRM battleground; BofA "growth engine for NOW, risk for CRM" | HIGH (ITSM/MSFT primary) / MEDIUM (positioning) |

**Refuted in third run:** stale pre-split Benzinga panel ($328 avg / $1,300 high, 0-3); a Bernstein "Market Perform" mislabel (0-3); a multiples.vc EV/NTM figure (0-3); a Yahoo "43 Buy" breakdown (1-2).

### Residual minor gaps (acknowledged on-page; do not block `good`)

1. Exact mid-2026 multiples for **CRM / WDAY / MSFT / PANW / SNOW** individually (only Adobe confirmed at peer level).
2. The **BofA NOW-vs-CRM thesis** is referenced secondhand; the primary BofA note/target did not verify.
3. **Hard win/loss / seat-share-shift data** vs Agentforce & Copilot — moat case rests on share/renewal + stated strategy, not measured displacement.

## Caveats

- **5-for-1 split effective Dec 17, 2025** — all per-share figures (EPS, BVPS, price) are split-adjusted; pre-split comparisons must be normalized.
- **GAAP vs non-GAAP gap is large** (op margin 13.7% vs 31%), driven mainly by **stock-based compensation**. Fred's bars run on GAAP report figures; a reader must decide which basis to underwrite. This is the central analytical tension for NOW.
- ROE/ROA computed on period-end balances as stated; average-equity ROE ~15.5%.
- The **$1.5B "2026 AI target" is forward-looking incremental ACV, not recognized GAAP revenue** — do not treat as reported.
- Market data is a Jun 4 2026 point-in-time snapshot from one secondary source; drifts across vendors/days.
- **Not investment advice.** The wiki documents NOW's fundamentals and Fred-framework fit; position-taking is downstream.

## Pages this contributed to

- [[servicenow]] — refreshed Fundamentals (FY2025 reported), added D/E / quick ratio / interest coverage / dividend, Q1 FY2026 momentum, AI monetization, valuation, and recomputed Fred-framework view.
