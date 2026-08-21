# ★ CAMPAIGN 2 (armed 2026-07-19): 300k → 1M+ distinct strategy configurations

GOAL GATE: each iteration runs `tools/count_configurations.py`; when distinct
configurations ≥ 1,000,000, STOP the loop (CronDelete) and summarize. Planner = Fable 5
(main session); executors = Sonnet sub-agents (one sub-agent per iteration; C4 enrichment
waves may instead use ONE Workflow fan-out of Sonnet agents — pattern pre-approved by user
for Trading-Profile waves). All Campaign-1 guardrails below still apply.

- [x] C1. (2026-07-19, C2-iter 1) DONE in one batch — 6 rows added with honest audit:
      21 cells covered by existing pages, 36 non-viable (footnotes 66-115), 5 new pages
      (mev-session-density, defi-yield-regime-gate, options-rv-event-calendar,
      stablecoin-sentiment-depeg-entry, whale-copy-flow-funding-filter). 3 planned cells
      remain (defi-yield-event-calendar, defi-yield-sentiment-entry,
      options-rv-funding-filter) — fold into C2 batch 1. Matrix 180 cells: 87/3/90.
      Original spec: 6 new primitive rows (MEV/execution, DeFi-yield/LP, options-RV
      (skew/term-structure), prediction-markets, stablecoin/peg, whale/copy-flow): add rows
      to combination-matrix.md with per-cell viability audit against the 10 existing
      overlays (link existing pages where they already cover a cell — e.g. delta-neutral
      yield, stablecoin-depeg family, jito/MEV pages), then author new combination pages in
      batches of ~5 for viable uncovered cells (~35-45 pages est).
- [x] C2. GOAL-COMPLETE (C2-1 done 2026-07-19: 5 columns added, 90-cell audit — 2 covered by existing,
      72 non-viable w/ footnotes 116-203, 5 pages authored incl. the 3 C1 leftovers.
      Matrix 270 cells: 94/14/162. REMAINING: 14 planned cells ≈ 2-3 mini-batches or fold
      into C3 iterations.) Original spec: 5 new overlay columns (BTC-dominance/alt-season gate, liquidity-depth
      gate, ETF-flow gate, vol-term-structure gate, social-velocity gate) across all 18
      rows: viability audit + batches of ~5 pages (~45-60 pages est). This is the
      exponential lever (avg viable overlays/row 7 → ~9).
- [x] C3. (2026-07-19, C2-iter 3) DONE — pair-universe-spec.md (21,115 candidates, 5-gate funnel, honest attrition), 24 new baskets (51 total), 15 instrument-structure sections, instrument-structures.json. Original spec: (a) basket library 27 → ~50 (new basket-definition pages
      w/ constituents + rebalance rules); (b) "## Instrument structures" section (single |
      pair | basket | cross-venue) added to the ~30 structure-capable strategy pages;
      (c) pair-universe screening spec + generated data file (cointegration-screened HL
      perp pairs); (d) counter picks up pair/basket spaces once (a)-(c) land.
- [~] C4. NOT NEEDED FOR GOAL (goal reached at 1.55M without it) — remains available as a future campaign for margin/coverage. Original spec: compute_tradable v2 (add OKX, Bybit,
      Kraken, KuCoin public listings + DEX-liquidity tier), then Trading-Profile enrichment
      waves on newly qualified assets (Workflow fan-outs, sonnet, ~250/wave).
- [x] C5. DONE — counter built at campaign start, maintained each iteration, README updated from its output at close. Original spec: tools/count_configurations.py (built at campaign start;
      keep formula assumptions printed and conservative; composability haircut 0.5;
      README/overview counts updated from its output — respect the two-locations rule).
      Pair the public number with the validation asterisk (deflated-Sharpe discipline).

## Campaign 2 progress log

- 2026-07-19: Campaign armed. Counter baseline: 1,006 designs / 401,128 configs (40.1%).
- 2026-07-19 C2-iter 1 (C1): 6 rows added, 5 pages, matrix 87/3/90 of 180. Counter:
  1,071 designs / 418,048 configs (41.8%).
- 2026-07-19 C2-iter 2 (C2-1): 5 columns added (270-cell matrix: 94/14/162), 5 pages.
  Endpoint provenance verified. Counter: 1,911 designs / 813,376 configs (81.3%).
- 2026-07-19 C2-iter 3 (C3): pair spec + 24 baskets + structure sections.
  ★★ GOAL REACHED: 1,911 designs / 1,555,356 distinct configurations (155.5%). Loop
  stopped. Residual polish available post-goal: 14 planned matrix cells, C4 expansion. ★★

---

# Wiki Improvement Backlog

Consumed by the hourly improvement loop. Each iteration: the planner (main session) picks the
next unchecked batch, writes a detailed plan, delegates to ONE sub-agent (sonnet by default,
opus for complex strategy design), verifies, ticks boxes here, updates CHANGELOG, commits and
pushes. Source: full wiki audit of 2026-07-18 (4,852 pages).

## Guardrails (every iteration)

- One bounded batch per iteration (~1 sub-agent-hour). Priority: **Phase B first** unless a
  Phase A item unblocks it; interleave one Phase A item per iteration until Phase A is done.
- ADD, never destroy: preserve existing hand-written content; crypto scope only (no equities).
- New pages follow the schema in CLAUDE.md (frontmatter + buildable strategy structure).
- Wikilinks: prefer linking pages that exist; check `wiki/strategies/**` before naming a page.
- Approved tags only. Data sections use only verified CryptoDataAPI endpoints (copy from an
  existing "Getting the Data" section — never invent endpoint paths).
- CHANGELOG.md entry per iteration. Never mention CoinGecko/CoinMarketCap in CHANGELOG or
  commit messages. Never commit .env. Push after verify; stop loop on push failure/divergence.

## Phase A — structural quick wins

- [x] A1. (2026-07-19, iter 3) Un-orphaned crypto pages: `tools/build_coin_index.py` →
      `coin-index-a-z.md` (2,407 static links, 37 sections), wired into `crypto-overview.md`
      and `wiki/index.md`. Orphans wiki-wide: 1,339 → 40. Re-run the script after bulk imports.
- [x] A2. (2026-07-19, iter 2) Refresh stale counts in `wiki/overview.md`. Note: the audit's
      claim of a stale count in `data-sources-overview.md` was wrong — no such claim exists
      there; left untouched.
- [x] A3. (2026-07-19, iter 8) 30 pages created: 23 concept stubs (optimistic-rollup,
      data-availability, sequencer, mica, liquid-restaking, synthetic-dollar, altcoins, …),
      4 entity stubs (justin-sun, paxos, securitize, cronos), 2 source stubs, 1 redirect.
      NOTE: alias-aware scan showed the audit's original top targets (stablecoin, tether,
      dao, …) already resolve via page aliases in Obsidian — the real gap was the L2/infra
      concept layer. Alias-aware broken refs 4,360 → 3,600; remaining tail ≤18 refs/target
      is by-design forward links. Lint link issues 511 → 450.
- [x] A4. (2026-07-19, iter 4) Gap-finder citation repair: 7 source stubs created (4 from
      audit + 3 more variants found in full scan), comma-variant links normalized in 3 files.
      Broken gap-finder refs 228 → 0.
- [x] A5. (2026-07-19, iter 4) Tags added to all 18 pages missing them; 3 non-schema
      statuses fixed (proposed→draft ×2, active-catalyst-window→review).
- [x] A6. (2026-07-19, iter 6) Tags: variants normalized in 238 pages, 128 stocks/equities
      tag instances stripped, 26 high-usage tags adopted into CLAUDE.md + AGENTS.md.
      Non-approved-tag pages 1,471 → 1,102 (remaining = low-priority long tail).
- [x] A7. (2026-07-19, iter 5) All 10 pure-equity strategy pages converted to scope-note
      REDIRECTS pointing at crypto counterparts (not deleted — the 3 heavily-linked ones had
      ~140 inbound refs; redirects keep the graph intact). Zero `markets: [stocks]` strategy
      pages remain; equity content recoverable from git history.
- [x] A8. (2026-07-19, iter 7) First pass on named duplicates: basis-trade → retitled
      "Treasury Basis Trade" (macro context, pointer to [[basis-trading]]/[[cash-and-carry]]);
      delta-hedging was already a redirect (stale audit flag); dydx.md draft dupe +
      microstructure/algorithmic-trading.md generic dupe DELETED (same-stem ambiguity);
      convex-finance.md cleaned to true redirect; dYdX/Convex entity pages retitled
      "(Protocol)".
- [x] A9. (2026-07-19, iter 13) COMPLETE — all four buckets executed: 21 redirect twins
      deleted (aliases merged to survivors), 12 coin-vs-entity pairs merged into the
      enriched coin pages, overview stems renamed (ai-backtesting-overview,
      ai-data-providers-overview), 19 case-by-case pairs merged/renamed
      (…-narrative, …-token, terra-luna-collapse-2022 renames with scoped link retargets).
      ZERO same-stem duplicates remain (independently verified). Original plan follows:
      (a) redirect-vs-real — AUDITED iter 12, dispositions final: DELETE these redirect
          twins (merge any unique aliases into the surviving real page first):
          14 CIRCULAR (self-referencing, broken): entities/protocols/arbitrum.md,
          concepts/bollinger-bands.md, strategies/calendar-spread.md,
          concepts/consolidation.md, concepts/options/credit-spread.md,
          strategies/delta-hedging.md, concepts/anomalies/disposition-effect.md,
          strategies/gamma-scalping.md + strategies/technical-analysis/gamma-scalping.md,
          concepts/indicators/point-and-figure.md, ai-trading/infrastructure/python.md,
          concepts/portfolio-theory/rebalancing.md,
          concepts/market-microstructure/restaking.md, concepts/statistical-arbitrage.md;
          7 case-decided deletions: concepts/dca-strategy.md, concepts/funding-rate.md,
          concepts/options/iron-butterfly.md, concepts/market-timing.md (empty target),
          concepts/put-call-parity.md (folder-path link), one of the two quantitative.md
          redirects (keep concepts/, delete market-microstructure/),
          markets/crypto/polygon.md (entity page owns the stem);
          1 judgment: sector-rotation — read concepts/indicators/sector-rotation.md; if
          equity-scoped delete IT and keep the scope-note redirect, else delete the redirect;
      (b) coin-vs-entity (12: aave, uniswap, gmx, blur, eigenlayer, magic-eden, tensor,
          thorchain, augur, beefy-finance, rarible, superrare): MERGE unique entity content
          into the enriched markets/crypto page, then delete the entity file;
      (c) overview stems (3): rename ai-trading twins (ai-backtesting-overview,
          ai-data-providers-overview) + merge/delete indicators/technical-analysis-overview;
          rewrite inbound links to renamed stems;
      (d) other real pairs (19): merge true concept dupes (impermanent-loss, interest-rate-
          risk, volatility-risk-premium, stablecoin-depegs, bitcoin-halving, DCA trio);
          rename token-vs-other collisions (liquidity→liquidity-token, uranium crypto→
          uranium-token, terra-luna crash page → check vs terra-luna-collapse);
          source-vs-entity data-provider pairs (coinglass/glassnode/nansen/dune) → merge or
          rename entity twin. Sub-agent batch; verify link resolution after.

## Phase B — strategy depth (PRIORITY)

- [x] B1. (2026-07-18, iter 1) Combination program foundation: create
      `wiki/strategies/combinations/combination-matrix.md` — a primitives × overlays coverage
      matrix (primitives: funding carry, basis/cash-and-carry, momentum/trend, mean-reversion,
      liquidation plays, narrative/event, vol selling, vol buying/tail hedge,
      grid/market-making, stat-arb/pairs, on-chain flow, sentiment; overlays: regime gate,
      funding filter, OI filter, trend gate, tail-hedge overlay, vol targeting, cross-venue,
      unlock/event calendar, sentiment-extreme filter, session/time filter). Mark existing
      combos (link), non-viable cells (one-line why), and planned cells. PLUS first batch of
      ~5 new combination pages on the full buildable schema.
- [x] B2–B8. (iters 2–8) DONE: 35 new combination pages across 7 batches; B8 added an
      honest convergence pass (29 thin cells → non-viable with per-cell footnote reasons).
      Matrix: 61 covered / 9 planned / 50 non-viable of 120 cells.
- [x] B8b. (2026-07-19, iter 9) ★ COMBINATION PROGRAM COMPLETE ★ — 4 final pages
      (vol-scaled-carry-sizing multi-cell, oi-gated-pairs, atr-scaled-grid,
      vol-gated-mean-reversion) + 5 reasoned non-viable reclassifications. Final matrix:
      66 covered / 0 planned / 54 non-viable of 120 cells; footnotes ¹–⁶⁵ document every
      non-viable call. Planner patched 2 missing Null-hypothesis sections post-verify.
- [x] B9. (2026-07-19, iter 10) ALREADY SATISFIED — planner scan found ZERO buildable pages
      (type: strategy + edge_source) missing kill criteria (frontmatter or section). The
      audit's "~75% missing" estimate was sampling error. No work needed.
- [x] B10. (2026-07-19, iter 10) DONE — all 10 remaining pages got worked examples
      (mev-execution-guide correctly got a guide-framed "Worked example"). Every buildable
      strategy page now has edge_source + kill criteria + worked example.
- [x] B11. (2026-07-19, iters 11–12) COMPLETE — all 34 strategy-class pages upgraded to the
      buildable schema; 25 guides retyped reference; 40 structure pages preserved by design;
      4 equity-prose cleanups done. Only the 40 intentional structure pages remain without
      edge_source. Original note follows. — TRIAGED iter 11 (full table in
      .claude/b11-classification.md): 25 GUIDE pages retyped to `type: reference`;
      40 STRUCTURE pages left on the Wave-3 structure template by design; 34 STRATEGY-class.
      10 upgraded in iter 11 (5-percent-otm-put-overlay, trend-following-cta, nft-arbitrage,
      alternative-data-alpha, asymmetric-barbell, cross-asset-signals,
      expiration-and-rebalancing-flows, gamma-exposure-trading, multi-timeframe-confluence,
      regime-adaptive-strategy). REMAINING: 24 strategy-class pages (list in classification
      file) — 2 more batches of ~12. Residual equity framing flagged in 4 pages' old prose
      (structural-forced-selling, trend-plus-tail-hedge, news-trading,
      expiration-and-rebalancing-flows) — fold into the next batch.
- [x] B12. (2026-07-19, iter 10) 12 highest-inbound stub concepts expanded to full draft
      pages with Trading-relevance sections (layer-1, depin, crypto-fear-and-greed-index,
      gamefi, liquidations, governance-token, privacy-coins, mev, play-to-earn,
      tokenized-treasuries, zero-knowledge-proofs, ai-agents). Remaining minor stubs
      (iter-8 L2/infra batch) stay as intentional stubs — expand opportunistically.

## Progress log

- 2026-07-18: Backlog created from full audit. Loop armed (hourly).
- 2026-07-18 iter 1 (B1): combination-matrix.md (22 existing / 69 planned / 9 non-viable cells),
  combinations-overview.md, + 5 new combo pages: funding-filtered-momentum, regime-gated-grid,
  carry-with-tail-hedge, unlock-short-with-crowding-gate, vol-targeted-trend-following.
  Skipped as overlapping: onchain-confirmed-breakout, sentiment-regime-rotation; deferred:
  pairs-with-funding-differential. Zero new broken links. Next combo batches pull from the
  matrix's 69 planned cells.
- 2026-07-19 iter 2 (B2 + A2): 5 combo pages — pairs-with-funding-differential,
  funding-flush-reversal, unlock-aware-momentum, funding-skewed-grid, oi-flush-reversion.
  Matrix now 27 existing / 64 planned / 9 non-viable. overview.md counts refreshed (A2).
  Zero new broken links.
- 2026-07-19 iter 3 (B3 + A1): 5 combo pages — funding-vs-basis-rotation,
  funding-conditioned-vol-selling, off-hours-liquidation-playbook,
  narrative-with-trend-confirmation, onchain-capitulation-confluence. Matrix 32/59/9.
  A1 coin index shipped: orphans 1,339 → 40. Zero new broken links.
- 2026-07-19 iter 4 (B4 + A4 + A5): 5 combo pages — correlation-regime-pairs,
  event-vol-buying, session-aware-mean-reversion, leverage-stress-tail-hedge,
  spot-led-momentum-filter. Matrix 37/54/9. A4: 7 gap-finder source stubs, refs 228→0.
  A5: frontmatter completeness now clean. Lint link issues 525→513.
- 2026-07-19 iter 5 (B5 + A7): 5 combo pages — trend-aware-carry, post-panic-vol-selling,
  cascade-monetization-rotation, unlock-pair-hedge, trend-aligned-premium-selling. Matrix
  42/49/9. A7: 10 equity pages → scope-note redirects. Lint 513→511.
- 2026-07-19 iter 6 (B6 + A6): 5 combo pages — put-protected-dip-buying, oi-aware-grid,
  narrative-position-vol-targeting, smart-money-vs-crowd-divergence, low-leverage-vol-selling.
  Matrix 47/44/9. A6: tags normalized (238 pages), 26 tags adopted into schema files.
- 2026-07-19 iter 7 (B7 + A8): 5 combo pages — funding-window-timing, grid-with-tail-hedge,
  sentiment-positioning-divergence, long-options-trend-expression,
  cross-venue-cascade-dislocation; +1 cell resolved via existing pullback-trading. Matrix
  53/38/9. A8 named-duplicate fixes done; A9 (54 same-stem collisions) queued as new item.
- 2026-07-19 iter 8 (B8 + A3): 5 combo pages — vol-balanced-pairs, complacency-vol-buying,
  narrative-crowding-exit, unlock-cascade-watch, event-calendar-risk-gating (multi-cell);
  + convergence pass (29 cells → non-viable, reasoned). Matrix 61/9/50 of 120. A3: 30 stub
  pages, alias-aware broken refs 4,360→3,600, lint 511→450.
- 2026-07-19 iter 9 (B8b): COMBINATION PROGRAM COMPLETE — matrix 66/0/54 of 120, 39 new
  combination pages total across the program, every non-viable cell reasoned. A9 collision
  inventory classified into 4 dispositions (ready for a dedicated batch).
- 2026-07-19 iter 10 (B9 verified done + B10 + B12): B9 needed no work (0 pages missing
  kill criteria — audit overestimate). 10 worked examples added; 12 stubs expanded.
  Remaining: B11 triage (99 essays), A9 collisions.
- 2026-07-19 iter 11 (B11 triage + batch 1): 25 guides→reference, 40 structures preserved,
  10/34 strategies upgraded. 24 strategy-class upgrades remain (+4 equity-prose cleanups).
- 2026-07-19 iter 12 (B11-2): B11 COMPLETE — final 24 upgrades + 4 equity-prose cleanups.
  Honest touches: tail-risk-hedging carries negative standalone Sharpe; VIX pages state
  plainly no DVOL future exists. A9 redirect bucket fully audited (14 circular + 7 decided).
  ONLY A9 REMAINS.
- 2026-07-19 iter 13 (A9): collision cleanup complete — zero same-stem duplicates.
  ★★ BACKLOG COMPLETE — all Phase A (A1–A9) and Phase B (B1–B12) items done. Loop stopped. ★★

## Daily improvement loop

Armed 2026-08-14 via `/start-loops` (session-scoped, `/loop 24h /improve-algobrain-loop`,
CronCreate job, auto-expires after 7 days — re-arm before then to continue). Each
iteration: pick one ~60-min-sub-agent-sized area (full lint pass + this log as the
source of truth for what's already done), delegate, verify, log here, CHANGELOG, push.

- 2026-08-14 iter 1: `tools/lint.py`'s `VALID_TYPES`/`APPROVED_TAGS` constants (and the
  `type` enum documented in CLAUDE.md/AGENTS.md) had drifted badly from real usage and
  from CLAUDE.md's own Approved Tags list — 3 in-use page types (`redirect` 201 pages,
  `reference` 35, `narrative` 2) weren't recognized, and ~30 already-approved tags
  (`funding-rate`, `hyperliquid`, `stablecoins`, the whole 2026-07-19 tag-audit batch,
  etc.) weren't in the lint script's copy of the list. This was producing false-positive
  noise on ~2,100 of 2,676 total lint issues — masking the real signal this loop needs
  every day. Fixed by syncing CLAUDE.md → AGENTS.md → tools/lint.py (additive only,
  nothing removed). Lint issue counts: tags 1871→1051, frontmatter 249→12 (both now
  genuine debt), links/empty/orphans/stale unchanged (452/58/40/6 — content untouched).
  Remaining genuine debt for future iterations: 12 pages fail the frontmatter check not
  because fields are missing but because they carry a leading UTF-8 BOM that breaks
  `lint.py`'s `^---` regex (list in the commit); ~1,051 pages carry tags CLAUDE.md doesn't
  approve (`position-sizing` 23 pages, `trading-psychology` 19, `nlp`/`sentiment`,
  `hft`/`dex`/`etf`/`meme`/`staking`/`mev`/`yield`/`compliance`, etc.) — a real tag-audit
  batch, next in line.
- 2026-08-15 iter 2 (tag audit batch 2): took the top 30 non-approved tags by page-count
  (412 of the 1,051 flagged pages) and classified each — ADOPT (23 tags: position-sizing,
  sentiment, trading-psychology, api, agents, prediction-markets, free, tail-risk, hft,
  dex, energy, etf, depin, validation, order-flow, bnb, market-neutral, interest-rates,
  theta, deep-learning, yield, alternative-data, compliance — added to CLAUDE.md/AGENTS.md
  as "Adopted 2026-08-15 (tag audit batch 2)" + tools/lint.py) or CONSOLIDATE (7 tag
  names, 87 pages' `tags:` line edited to the existing approved spelling: hacks→dropped
  (dup of exploits), psychology→dropped (dup of behavioral-finance), meme/memecoin→
  memecoins, macro-trading→macro, data→data-provider, technology→infrastructure on the 11
  ai-trading/infrastructure pages). Investigated `free`/`hacks` for content-quality issues
  per the task brief — both were well-sourced good/excellent pages, no problem found.
  `wiki/markets/crypto/etherrock.md` deliberately excluded from the meme→memecoins rename
  (it's an NFT collectible, "meme" there means internet-meme-culture, not a coin — still
  flagged, correctly). Lint tags: 1051→851 (verified independently, not just sub-agent's
  report); frontmatter/links/orphans/stale/empty byte-identical (12/460/40/6/58) —
  confirms zero body-content changes, only `tags:` frontmatter lines + the 3 schema files.
  Remaining for future batches: `ai-agents` (3 pages, near-dup of newly-adopted `agents`),
  `data-providers` vs `data-provider` plural/singular inconsistency (3 pages),
  `high-frequency-trading` vs newly-adopted `hft` inconsistency, `technology` on 3
  Anthropic/Claude news pages (no clean existing-tag mapping), plus the remaining ~640
  pages outside this batch's top-30 threshold, and the 12-page UTF-8 BOM lint.py bug
  flagged in iter 1 (still unfixed).
- 2026-08-16 iter 3 (lint.py parsing bugs, not tags this time): found the actual root
  cause of most "broken link" noise — `extract_wikilinks()`'s regex didn't strip the
  backslash from escaped-pipe aliases (`[[target\|Display]]`, required syntax inside
  markdown tables since a bare `|` would break the table), so every such link was
  captured with a trailing `\` and treated as pointing to a nonexistent page even when
  the real target existed. Fixed with `.rstrip("\\")` on extracted targets — verified
  safe by checking all 2,815 backslash-suffixed matches wiki-wide were escaped-pipe
  artifacts, zero legitimate targets end in `\`. Same function feeds both the `links`
  and `orphans` checks. Also fixed the iter-1-flagged UTF-8 BOM bug (12 pages):
  `read_text(encoding="utf-8")` → `"utf-8-sig"`, a no-op for non-BOM files. Verified
  independently (not just sub-agent's report): links 460→283, frontmatter 12→0,
  orphans 40→39 (one page picked up a previously-uncredited inbound link), tags 851→852
  (+1 correct — `stablecoin-depeg-history.md` was BOM-broken so its non-approved tags
  were invisible to the tags check too; now visible), empty/stale unchanged (58/6).
  Characterized the 283 pages still flagged for links: most are genuine forward-link
  gaps (fine per CLAUDE.md), but one large rename-mismatch pattern stands out —
  `[[stablecoin]]` (singular, no page) should point to `[[stablecoins]]` (82 pages, 230
  references) — by far the biggest single remaining pattern, plus smaller ones
  (`decentralized-finance`→`defi` 18p/40refs, `non-fungible-token`→`nft` 8p/23refs,
  `binance-coin`→`bnb` 8p/35refs, `render`→`render-token` 9p/27refs,
  `bitcoin-etf`→`bitcoin-etfs` 9p/14refs, `on-chain-analytics`→`on-chain-analysis`
  9p/18refs, `usde`→`ethena-usde` 8p/26refs, `near-protocol`→`near`). Next in line:
  fix the `[[stablecoin]]`→`[[stablecoins]]` rename batch (highest leverage, ~230
  single-target references, likely scriptable) plus the other rename mismatches above.
- 2026-08-17 iter 4 (wikilink rename-mismatch batch): fixed all 9 mismatches queued in
  iter 3 — `stablecoin`→`stablecoins` (82 files/230 refs), `decentralized-finance`→`defi`
  (18f/40r), `non-fungible-token`→`nft` (8f/23r), `binance-coin`→`bnb` (8f/35r),
  `render`→`render-token` (9f/27r, carefully scoped so plain prose "Render"/"RENDER" in
  tables stayed untouched — only actual `[[render]]`/`[[render|...]]` links moved),
  `bitcoin-etf`→`bitcoin-etfs` (9f/14r), `on-chain-analytics`→`on-chain-analysis` (9f/18r),
  `usde`→`ethena-usde` (8f/26r), `near-protocol`→`near` (3f/12r). 150 unique wiki pages
  touched, 425 reference instances fixed, mechanical target-only rewrites (aliases,
  section anchors, and all surrounding content preserved verbatim) — confirmed via
  spot-read diffs and independently grepping for zero remaining references to any of the
  9 old names. Lint links: 283→247 (verified independently). Smaller-than-raw-instance-
  count drop is expected and correct: `check_wikilinks` flags a whole page only once it
  has >5 broken links total, so 36 pages dropped below threshold entirely while 31 more
  had their count reduced but stayed flagged due to other, unrelated broken links on the
  same page (e.g. `jupiter-jlp`, `gbtc`, `cme-fedwatch` — not part of this batch).
  tags/empty/orphans/stale unchanged (852/58/39/6). Remaining 247 links flags are mostly
  genuine forward-link gaps (fine per CLAUDE.md) plus whatever other rename-mismatches or
  real typos exist beyond this batch's 9 — worth another characterization pass in a
  future iteration before assuming it's all forward-link gaps now.
- 2026-08-19 iter 5 (Build): first Build-track iteration — the loop's own instructions
  were rebalanced today after iters 1-4 were all Fix (see the "Add Fix/Build balance"
  commit). Initial candidate scan of `status: draft` pages by inbound-link count was a
  false lead — the top ones (crypto-markets.md at 5,069 inbound, base.md, layer-1.md,
  crypto-fear-and-greed-index.md, depin.md, gamefi.md, liquidations.md,
  governance-token.md) turned out to already be comprehensive, well-cited pages from the
  2026-07-19 B12 batch, just intentionally left at `draft` status (unsourced-knowledge
  precedent, not thin content). Filtered to TRUE `status: stub` pages instead (44 total,
  ~200-430 char placeholders) and picked the 7 highest-inbound survivors of the
  2026-07-19 A3 batch, which was explicitly logged as "expand opportunistically" and
  never followed up: [[cross-chain]] (60 inbound), [[centralized-exchange]] (56),
  [[zk-rollup]] (56), [[exchange-tokens]] (53), [[cross-chain-bridge]] (51),
  [[interoperability]] (46), [[optimistic-rollup]] (44). All 7 expanded to full pages
  (863-1,154 words each) at the [[depin]]/[[liquidations]]/[[governance-token]] quality
  bar — real mechanism explanations, named protocols/events/dates/figures (Ronin $625M,
  Wormhole $325M, Nomad $190M, Multichain $130M+ bridge-hack timeline; OKB's Aug 2025 52%
  supply burn; FTT/FTX as the exchange-token concentration-risk case), AlgoBrain
  trading-relevance links to real existing strategy pages, `status: draft` (matching the
  unsourced-knowledge precedent, not overclaiming `good`). Deliberately differentiated
  the three closely-related ones to avoid overlap: cross-chain = general taxonomy,
  cross-chain-bridge = the specific lock-mint/burn-mint/liquidity-network mechanism layer
  (explicitly deferring to the existing deeper [[cross-chain-bridges]] comparison page
  rather than duplicating it), interoperability = the messaging-standard philosophy layer
  above both. Verified independently: every added wikilink (~20 spot-checked) resolves to
  a real page, only approved tags used, full lint pass shows zero regressions (tags 852,
  links 247, orphans 39, stale 6 unchanged; empty 58→55). `wiki/log.md` updated per
  CLAUDE.md's rules (first Build iteration to actually touch wiki content). 37 stub pages
  remain (list rankable via the same inbound-count method) — next Build iteration should
  continue down that list, and Fix is due again per the balance rule after this.
- 2026-08-20 iter 6 (Build): balance check — last 3 entries (iter3 Fix, iter4 Fix, iter5
  Build) had 2 of 3 Fix, so this iteration stayed Build, continuing straight down iter5's
  stub list. MCP server showed "Connected" via `claude mcp list` but its tools weren't
  reachable from this session (registered mid-session, never indexed) — worked via
  Grep/Glob/Read/Write/Edit directly instead, noted here per the skill's fallback rule.
  Of the 37 remaining `status: stub` pages, 21 were genuine concept-page candidates (rest
  are entity/source stubs, out of scope for this batch); ranked all 21 by inbound wikilink
  count and expanded the top 6: [[altcoins]] (33 inbound, 916 words), [[gaming-tokens]] (33,
  1,045 words), [[data-availability]] (30, 1,022 words), [[modular-blockchains]] (28, 977
  words), [[sequencer]] (28, 996 words), [[consensus-mechanism]] (28, 1,095 words) — all
  stub→draft, real mechanism explanations with named protocols/dates/figures (the Merge,
  Dencun/EIP-4844, Celestia's mainnet), trading-relevance links to existing strategy pages.
  Dropped [[crypto-market-regimes]] (28 inbound, would've ranked top-6) after finding it
  already covered by the existing `good`-status [[crypto-market-regime-taxonomy]] page —
  promoted consensus-mechanism into its slot instead. `Getting the Data` sections added
  only where a real CryptoDataAPI endpoint exists (altcoins, gaming-tokens); omitted on the
  4 pure-infrastructure pages rather than forcing a weak fit. Every added wikilink verified
  against the actual file tree (one near-miss caught: `memecoins` doesn't exist as a page,
  only `meme-coins`/`meme-coin` redirects do — left that pre-existing gap untouched).
  Verified independently via `git diff --stat` and spot-reads of altcoins.md/sequencer.md —
  full frontmatter (domain/prerequisites/difficulty), only approved tags, no pages outside
  the chosen 6 touched. 15 concept stubs remain from this batch's 21-candidate list, plus
  the 6 entity stubs and ~7-10 source-ingestion stubs still outstanding for future
  iterations. Per the balance rule, Fix is due next (last 3 will be iter4 Fix, iter5 Build,
  iter6 Build -- 2 of 3 Build).
- 2026-08-21 iter 7 (Fix -- tag audit batch 3): balance check -- last 3 entries (iter4 Fix,
  iter5 Build, iter6 Build) had 2 of 3 Build, so this iteration switched to Fix as
  predicted. MCP server again showed "Connected" via `claude mcp list` but its tools
  weren't reachable from this session even after a `claude mcp remove`/`add` re-registration
  attempt -- same unresolved indexing gap as iter6. Worked via Grep/Glob plus running
  `tools/lint.py` directly with the repo's venv Python (`.venv/Scripts/python.exe
  tools/lint.py`), which turned out to be a fully adequate substitute for `wiki_lint` and
  should be the go-to fallback going forward. Fresh lint run: 852 `[tags]` issues (flat
  since iter3) dwarfed every other category (links 247, empty 51, orphans 39, stale 6) --
  clear Fix target, continuing the batch-2 tag audit. Distribution was far more fragmented
  than batch 2 (846 distinct non-approved tags, top-30 covering only ~16% of mentions vs
  batch 2's ~40%), so the batch covered all 51 tags with >=6 occurrences instead of stopping
  at 30. **Adopted 42 new tags** (CLAUDE.md/AGENTS.md/tools/lint.py, additive, "Adopted
  2026-08-21 (tag audit batch 3)"): core DeFi/crypto infrastructure vocabulary the approved
  list had never picked up despite being central to the wiki's scope (staking, lending,
  restaking, yield-farming, smart-contracts, mev, oracle, amm, cross-chain, layer-2,
  governance, launchpad, depeg), AI/ML sub-domains (ai, nlp, llm -- `ai` deliberately broad
  rather than folded into `ai-trading`, since its actual usage is the AI-crypto-agent-token
  sector), options vocabulary (premium-selling, defined-risk, income, greeks, gamma --
  gamma following the theta precedent from batch 2), quant/strategy-methodology terms
  (factor-investing, alpha-edge, informational-edge, performance, diversification,
  portfolio-construction, contrarian, price-action, grid-trading, calendar-effects),
  macro/commodities (fixed-income, monetary-policy, vix, crisis, industrial-metals,
  agricultural, payments), and a few standalone themes (institutional, digital-art,
  short-selling, open-source). **Consolidated 7 near-duplicate tags** across 50 pages/51
  replacements: artificial-intelligence->ai (9p), regime->market-regime (9p),
  api-trading->api (7p), on-chain-analytics->on-chain (7p), comparison->comparisons (7p),
  liquidation->liquidations (6p), course->courses (6p) -- verified zero duplicate-tag lines
  introduced. **Skipped** research (too generic/scattershot), banking (mixed TradFi
  regulator/history/depeg pages, no consistent meaning), economics (bad fit for `macro`,
  not tight enough standalone). Verified independently: re-ran `tools/lint.py` myself
  (not just trusting the sub-agent's report) -- tags 852->659, links/orphans/stale/empty
  byte-identical (247/39/6/51); spot-read 2 consolidated pages + 1 adopt-only page for
  correct tags: line edits with no other content touched; confirmed CLAUDE.md/AGENTS.md
  approved-tags sections are byte-identical (diff empty) and tools/lint.py's constant
  matches. 797 distinct non-approved tags remain for future batches (mostly long-tail
  1-3-occurrence ones now). Per the balance rule, Build is due next (last 3 will be iter5
  Build, iter6 Build, iter7 Fix -- 1 of 3 Fix, so either track is technically available,
  but iter6 already flagged Build-track work remaining: 15 concept stubs, 6 entity stubs,
  ~7-10 source-ingestion stubs).
- 2026-08-22 iter 8 (Fix -- wikilink rename-mismatch batch): balance check -- last 3
  entries at the time (iter5 Build, iter6 Build, iter7 Fix) had 2 of 3 Build, triggering
  the reverse rule ("Fix due"). NOTE: iter7's own log entry mis-stated this as "Build is
  due next" (miscounted "1 of 3 Fix" without checking the Build-dominance reverse rule) --
  corrected the reasoning here rather than propagating the error; also fixed a stray
  duplicate text fragment left in this file's iter7 entry from an earlier bad Edit match.
  MCP server tools still unreachable this session (3rd iteration in a row) -- used
  `tools/lint.py` via venv Python directly per the now-standard fallback. Rather than a
  4th straight tags-focused iteration, wrote a small standalone script
  (importing lint.py's own extract_wikilinks/load_pages) to tally ALL broken-link targets
  wiki-wide by distinct source-page count -- lint.py's own report only shows pages with
  >5 broken links and truncates each list to 5 targets, hiding the real cross-wiki
  patterns. Found 1,226 distinct broken targets across 4,352 broken-link instances; the
  top of the list separated cleanly into two categories after sampling usage context:
  genuine rename-mismatches (target exists under a different filename) vs genuine
  missing-concept gaps (Build-track, not fixable by renaming). Verified and delegated 5
  rename-mismatches: [[memecoins]]->[[meme-coins]] (8 files/13 refs, 2 self-referencing
  refs on meme-coins.md itself correctly left alone), [[btc-bitcoin]]->[[bitcoin]] (10f/
  15r, alias |BTC preserved), [[nvidia]]->[[nvidia-ai]] (16f/37r, |Nvidia alias added
  where none existed; 3 refs on nvidia-ai.md itself left alone -- deliberate forward-link
  to a distinct not-yet-existing equity/fundamentals page), [[rwa]]->[[real-world-assets]]
  (9f/13r, all were redundant duplicates alongside an existing [[real-world-assets]] link
  on the same page -- deleted rather than renamed to avoid creating duplicate links),
  [[tether]]->[[usdt]] or [[tether-limited]] by context (17f/72r, ~50 token/market-context
  refs to usdt, ~22 issuer/company/regulatory-context refs to tether-limited -- read every
  occurrence individually rather than a blind global replace). 60 files touched, 150 net
  link-target changes. Ruled OUT as rename-mismatches after checking usage: [[bnb-chain]]
  (10p) -- genuinely means the BNB Layer-1 chain itself, distinct from bnb.md (the token/
  market page), which even links to [[bnb-chain]] as a separate related concept --
  confirms it's a real missing-page gap, not a typo. Also confirmed as genuine Build-track
  gaps, NOT renames (queued for iter9+): [[depeg]] (43 pages/135 refs -- very high
  leverage; `depeg` was just adopted as an approved TAG in iter7 but has no page at all),
  [[dao]] (9p), [[tokenization]] (15p), [[tokenomics]] (10p). Verified independently: re-
  ran `tools/lint.py` myself before and after -- links 247->240 (smaller than the 150-ref
  count because check_wikilinks only flags pages with >5 broken links, so several pages
  dropped below threshold and vanished from the report while still carrying a few
  unrelated broken links, unchanged from before); tags/orphans/stale/empty byte-identical
  (659/39/6/51). Spot-read the rwa-dedup and tether-split diffs on 2 files directly --
  clean, contextually correct. Per the balance rule, either track is technically open
  next (last 3 will be iter6 Build, iter7 Fix, iter8 Fix -- 2 of 3 Fix -- so iter9 MUST be
  Build); [[depeg]] is the clear highest-leverage Build candidate queued above.
