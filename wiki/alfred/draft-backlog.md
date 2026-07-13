---
title: "Draft Backlog — Remaining Quality Sweeps"
type: index
created: 2026-06-11
updated: 2026-06-11
status: good
tags: [meta, methodology]
aliases: ["Draft TODO", "Quality Sweep Backlog"]
related: ["[[wiki-operations-log|log]]", "[[strategies-overview]]", "[[stockmarketapi-fundamentals-2026-05-10]]"]
---

# Draft Backlog — Remaining Quality Sweeps

Prioritized TODO for converting the remaining ~2,030 draft and ~325 stub pages to `good`. Snapshot taken 2026-06-11 after the strategy sweep (2026-06-10) and the two entity-enrichment waves brought the wiki to 2,341 good pages. Method that works: tiered batches, parallel agents, batched Perplexity `sonar` calls (1-2 per agent batch), honest bumps only.

## Priority 1 — Cheap wins

- [x] **52 `review` pages — ALL DONE** (2026-06-11, two sweeps): sweep 1 = indicators, behavioral finance, risk, regulators, AI cluster; sweep 2 = NFT-microstructure, Solana-ecosystem tokens, defi, bitcoin-etfs, commodities, small entities (dead protocols reframed as historical records). 52/52 passed; wiki now has zero review-status pages.
- [x] **24 strategy stubs** in `wiki/strategies/` — DONE 2026-06-11: 10 redirected to canonical pages (stat-arb→statistical-arbitrage, equity-long-short→long-short-equity, cta-strategies+managed-futures→trend-following-cta, spread/straddle/leaps variants), 14 built to full template or hub-page standard ([[triple-screen-system]], [[atr-position-sizing]], [[buy-and-hold]], [[stablecoin-yield]], [[dividend-investing]]…). Strategies section now stub-free: 375 good / 6 excellent / 5 deliberate drafts.
- [x] **Dedupe pass — DONE 2026-06-11**: 13 pairs merged into canonicals + redirects (boston-properties→bxp, investors-business-daily→ibd, convex/cvx/convex-finance three-way→convex, arbitrum protocol→crypto page, virtual-protocol→virtuals-protocol, etherfi→ether-fi, decentralized-exchange→decentralized-exchanges, avalanche-2→avalanche, ustbl→spiko-us-t-bills, reddit exchanges→companies). eutbl + news-corp/fox share classes kept as distinct. **Follow-up flagged:** the redirected `ustbl-tokenized-u-s-treasury-bill` was actually NexBridge USTBL (distinct product, same ticker) — facts preserved as a note on the Spiko page, but consider restoring it as its own page. Original list:
  - [ ] [[boston-properties]] → merge into [[bxp]] (bxp has the API Fundamentals section)
  - [ ] [[ibd]] ↔ [[investors-business-daily]] (keep investors-business-daily per naming conventions)
  - [ ] [[reddit]] duplicated in entities/companies and entities/exchanges
  - [ ] protocols/[[convex]] → redirect to [[cvx]]; reconcile with markets/crypto convex-finance
  - [ ] protocols/[[arbitrum]] ↔ markets/crypto arbitrum (entity page vs token page — pick canonical or split roles explicitly)
  - [ ] [[virtual-protocol]] ↔ [[virtuals-protocol]]
  - [ ] [[ether-fi]] ↔ [[etherfi]]
  - [ ] [[eutbl]] ↔ [[ustbl-tokenized-u-s-treasury-bill]] ↔ spiko fund page
  - [ ] news-corp ×3 and fox ×3 share-class pages — decide one-page-per-class vs canonical+redirects
  - [ ] [[decentralized-exchange]] ↔ [[decentralized-exchanges]] (concepts)
  - [ ] [[avalanche-2]] empty stub → redirect to [[avalanche]]
  - [ ] [[barrick-gold]] → rename to barrick-mining (company renamed; aliases already added)
- [ ] **Schema fixes:**
  - [x] [[lazarus-group]] `entity_type` fixed to `threat-actor` (2026-06-11; verified the field is tooling-written only, not read for dashboard categorization)
  - [x] **DONE 2026-06-12:** 18 off-topic/personal pages moved to `wiki/personal-projects/` (out of the trading namespace) — 10 VentureAI-Labs ventures + 8 off-topic/self-help stubs. See [[personal-projects-overview]]. MCP test artifact ([[2026-05-28-verify-mcp-test-1779960598]]) deleted. Stale bucket copies of old paths removed via `gcloud storage rm`.

## Priority 2 — High-value content pools

- [x] **Concepts — DONE 2026-06-11** (~860 pages across 5 waves): the whole `wiki/concepts/` tree is now **1,003 good + 1 excellent**, only 8 deliberately-skipped off-topic pages left. Waves: indicators (190) + market-microstructure (210) + risk-management (83) + portfolio-theory (125) + the combined rest (362: root/metrics/options/anomalies/behavioral-finance/backtesting/market-regimes/tax). ~273 redirects collapsed duplicate stubs into canonicals.
  - [ ] **8 off-topic concept pages** still draft/stub — candidates for deletion or move out of the trading namespace: diesel-vehicles, freedom-as-asset, generative-art, wharton, and portfolio-theory/{mentoring, savings-rate, wealth-building, work-life-balance}
- [x] **markets/stocks + markets/commodities — DONE 2026-06-12** (now 37 + 35 good, 0 draft).
- [x] **data-sources — DONE 2026-06-12** (46 good; 1 left draft: moby-gg, unverifiable niche tool).
- [x] **artificial-intelligence (whole tree, 160 pages) — DONE 2026-06-12** (178 good, 0 draft).
- [x] **ai-trading (libraries/infra/backtesting, 43 pages) — DONE 2026-06-12** (124 good; 2 left draft: convex-trading, pivolio — unverifiable niche tools).
- [x] **crypto-narratives — DONE 2026-06-12** (20 good; 2 left as-is: narrative-signals.md + narratives-by-direction.md are AUTO-GENERATED machine files — do NOT hand-edit, they regenerate from JSON).
- [x] **history (crashes + notable trades, 50 pages) — DONE 2026-06-12** (59 good, 0 draft; consolidated the six 1987-crash variants, LTCM pair, volmageddon/nickel dupes into canonicals).
- **P2 content COMPLETE.**
- [x] **sources/ (52 summaries) — DONE 2026-06-12**: 51 bumped to good (claim extraction + confidence markers + source schema); 1 left stub ([[2026-05-28-verify-mcp-test-1779960598]] — an MCP test artifact, not a real source; candidate for deletion). sources/ now 141 good.
- **ALL ADDRESSABLE CONTENT COMPLETE.** Only deferred P3 pools (below) + the ~12 off-topic personal pages remain.

## Priority 3 — Long tail (deliberately deferred)

- [x] **markets/crypto long-tail — DATA-REFRESHED 2026-06-12** via new `tools/refresh_crypto_market_data.py` (CoinGecko top-1000 snapshot, no agents/Perplexity): 711 draft pages updated with current rank/market-cap/price + "refreshed" stamp; 162 flagged as fallen out of the top 1000 (stale-data note, no fabricated numbers); 171 good pages untouched. Pages stay `draft` (catalog entries) — this is data currency, not a quality bump. Re-run the script anytime to re-refresh. Remaining option if ever wanted: selectively bump coins that enter the top-150 or get Hyperliquid listings to good via an agent wave.
- [x] **news — DONE 2026-06-12** (62 pages: 54 built, 2 redirected to history canonicals; news/ now 90 good). 8 left draft with `verified: false` — forward-2026 events resting on single internal gap-finder sources that couldn't be externally corroborated (anthropic-blackstone-jv, anthropic-finance-agents-launch, citrini-tech-selloff, bls-900k-jobs-revision, meta-ai-layoffs, 2024-03-hyperliquid-cascade likely conflated) — bump if/when a primary source confirms.
- [ ] **entities/companies residue: 34 stubs/drafts** — redirects, personal pages (see schema fixes), and 2 review pages.

## Workflow recipe (proven 2026-06-10/11)

1. Tier the target pool: A = complete-needs-review, B = 1-3 sections missing, C = rebuild.
2. ~8-15 pages per agent; agents make 1-2 *batched* Perplexity sonar calls (never `sonar-deep-research`).
3. Honest bumps only — pages that fail verification stay draft with a recorded reason.
4. Per-wave: verify scan → `wiki/log.md` entry → commit → push → `gcloud storage rsync wiki gs://alfred-data-venture-472911/wiki --recursive` (or `/deploy`).
5. Resume-friendly: keep batch opts byte-identical so the workflow journal cache hits on rerun; model overrides only on failed batches.

## Related

- [[log]] — full operation history for the 2026-06-10/11 sweeps
- [[strategies-overview]]
- [[stockmarketapi-fundamentals-2026-05-10]] — fundamentals data source + coverage limits
