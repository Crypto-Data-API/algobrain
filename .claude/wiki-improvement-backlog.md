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
- 2026-08-24 iter 9 (Sync -- first run of the new changelog-reconciliation step): the
  loop gained a Sync track this session, and its first run found the wiki badly out of
  date against the data layer. All 10 releases the feed retains were unprocessed (the
  watcher was seeded empty rather than baselined, deliberately, so nothing was skipped).
  MCP server tools unreachable again (4th iteration running) -- root cause finally found
  and fixed: `.venv` did not exist, so `tools/start_servers.ps1` had been failing its
  interpreter check every time. Created the venv, installed `tools/requirements.txt`, and
  started the server (it cannot register into an already-running session, so this
  iteration still used the Grep/OpenAPI fallback; future sessions get the real tools).
  **Triage:** split the 10 releases on a clean boundary -- "correct what the wiki already
  documents" (processed) vs "document what is new" (deferred). Processed 5 as material:
  2026-08-22 (breaking), 2026-08-20, 2026-07-10, 2026-07-06, 2026-06-27 (breaking).
  Deferred 5, all of which need entirely NEW `cryptodataapi-*` category pages and are a
  natural iter-10 batch: 2026-08-23 (`/exchanges` venue directory, public), 2026-08-21
  (news policy-catalyst categories + `/market-intelligence/squeeze-alerts`), 2026-08-19
  (`/supply/float`, `/supply/unlocks`), 2026-08-18 (the whole `/news/*` family -- pulse,
  market-moving, coin/{symbol}, sources, plus `/backtesting/news-events`), 2026-08-17
  (`/volume/scanner`). **Verified before delegating**, not after: pulled the live
  OpenAPI spec (204 paths) and confirmed every path in the brief; independently confirmed
  all three rate-limit rows from the changelog's own burst-ratio arithmetic
  (per_day/1440 vs per_minute gives Free 14x, Pro 4.3x, Pro Plus 1.7x pre-change ->
  Free 1,000/day+10/min, Pro 10,000/day+30/min, Pro Plus 50,000/day+120/min). Every row
  of the wiki's tier table was wrong, including "Unlimited" for a tier that caps at
  50,000/day. **Changed (8 files):** cryptodataapi.md (tier table + email-verification
  mechanic + `/auth/resend-verify` + effective-limits bullet), cryptodataapi-market-
  intelligence.md (ETF flows btc/eth/sol only -- XRP now 400 not 503; `/etf/btc/aum`
  reframed from "total AUM" to a reconstructed estimate with its real `_from_flows`
  field names; venue-coverage caveat on `/liquidations/by-exchange`), cryptodataapi-
  regimes.md (gex tier Pro not Pro+, breaking single-symbol envelope, `regime.confidence`,
  capped/nullable `gamma_flip`, `distribution_context`), spot-etf-flows.md, gamma-
  explosion.md, gamma-exposure-trading.md, cryptodataapi-backtesting.md, feature-
  engineering-crypto.md. **Caught in my own verification pass, not the sub-agent's:** it
  wrote `GET /api/v1/backtesting/snapshots/gamma_exposure` in 3 places -- an invented
  path. It flagged the uncertainty honestly in its report rather than asserting it, which
  is what let me catch it. The spec has no such route: `/backtesting/snapshots` IS the
  data endpoint (required `data_type` + `start` params) and `/backtesting/snapshots/types`
  is the discovery route. Corrected to the query form. That also exposed a PRE-EXISTING
  error on cryptodataapi-backtesting.md, which had the two routes documented backwards
  and listed a `/snapshots/{type}` path that has never existed -- fixed there and on
  feature-engineering-crypto.md. **Sub-agent correctly rejected one brief premise:**
  hyperliquid-market-making.md has no stale CryptoDataAPI rate-limit quote (my grep had
  matched on `10,000/day`, which is Pro's cap and unchanged) -- no edit made, correctly.
  **QUEUED FOR NEXT FIX ITERATION (high leverage, newly discovered):** wrote a template-
  aware sweep (scratchpad, reusable) matching every `/api/v1/...` path cited anywhere in
  the wiki against the live OpenAPI spec, treating `{param}` segments as wildcards so
  concrete values like `/BTC` match `/{symbol}`. Result: **24 distinct endpoint paths
  that do not exist, 166 citations.** Worst offenders with confirmed correct
  replacements: `/market-intelligence/dvol-history` (55 citations, 11 pages -- no dvol
  endpoint exists at all; the real series is `/volatility/index/history`),
  `/on-chain/whale-score/{symbol}` and `/on-chain/whale-score/BTC` (39 citations, 27
  pages -- renamed to `/on-chain/whales/accumulation-score/{symbol}`), `/volatility/dvol`
  (17x -> `/volatility/index`), `/sentiment/fear-greed-index` (8x -> `/sentiment/fear-
  greed`), `/derivatives/hyperliquid/funding-rates` (7x -> `/hyperliquid/funding-rates`),
  and `/market-intelligence/borrow-interest` (10x) plus `/market-intelligence/grayscale/*`
  which appear to have been retired outright with no replacement. This is a direct
  violation of CLAUDE.md's never-invent-an-endpoint rule sitting in the wiki at scale,
  and it is exactly what the new Sync step exists to surface. Per the balance rule, Sync
  does not create balance debt: the last 3 Fix/Build entries remain iter6 Build, iter7
  Fix, iter8 Fix, so iter 10 is still owed a **Build** -- but this endpoint sweep is a
  strong Fix candidate competing with it, and the deferred 5 releases are Sync work that
  outranks both.
- 2026-08-25 iter 10 (Sync -- news/catalyst family): no new upstream releases since iter 9
  (`api_version` still 2026-08-23), so this iteration worked the deferred backlog rather
  than fresh drift. Of the 5 releases left unprocessed, took the two that are
  interdependent and form one coherent unit: 2026-08-18 (the whole `/news/*` family) and
  2026-08-21 (the policy-catalyst taxonomy that adds `category` values to those same
  endpoints, plus `/market-intelligence/squeeze-alerts`). Doing 08-21 without 08-18 would
  have documented category values for endpoints the wiki did not describe at all. MCP
  tools still unavailable in-session (the server is running from iter 9's fix, PID 55260,
  but cannot register into a session that started before it existed) -- used the OpenAPI
  spec + Grep fallback. **Created** `wiki/data-sources/cryptodataapi-news.md`, the 17th
  `cryptodataapi-*` category page: 5 endpoints (`/news/pulse`, `/news/market-moving`,
  `/news/coin/{symbol}`, `/news/sources`, `/backtesting/news-events`), full tier gating
  per endpoint, the `news_pressure`/`news_tilt`/`headlines` feature semantics, the
  `match_mode`/`confidence` provenance model, the funnel-health fields, and the two hard
  constraints on the archive (qualified events only; history starts 2026-08-18 and cannot
  ever be backfilled because RSS serves only a recent window). **Registered** it in the
  hub category map + `related:`, and added reverse links on market-intelligence,
  backtesting, regimes, and sentiment, plus an entry on news-and-sentiment-sources.
  **Also absorbed:** `/market-intelligence/squeeze-alerts` onto the market-intelligence
  page (with the nuance that `direction` names the side being LIQUIDATED, so
  `short_squeeze` is upward pressure), `/backtesting/news-events` onto the backtesting
  page, and the `/policy/headlines` sign-error fix onto the regimes page (the `ban` rule
  was unbounded on the right, so "banking"/"banks"/"banner" scored as maximum-severity
  regulatory bans at `bias: -1.0`, skewing `headline_tilt` and `regulatory_pressure`
  negative). Bumped the hub's "190+ endpoints" to "200+" -- the spec now lists 204.
  **Verified independently, not taken on trust:** re-fetched the OpenAPI spec and
  confirmed all 5 new-page paths resolve; re-ran the iter-9 template-aware endpoint sweep
  and confirmed it stayed at exactly 24 bad paths / 166 citations, i.e. this batch
  introduced no invented endpoints (the specific failure mode from iter 9); confirmed all
  11 wikilinks on the new page resolve to real files (zero forward links) and all 8 tags
  are on the approved list; re-ran lint -- byte-identical at 995 issues
  (links 240 / tags 659 / orphans 39 / stale 6 / empty 51), so the new page is fully
  linked rather than an orphan. Sub-agent reported no paths written outside the brief,
  which the sweep corroborates. **Remaining deferred (3, all new families needing their
  own category pages):** 2026-08-23 (`/exchanges`, `/exchanges/{slug}` -- public venue
  directory carrying referral disclosure, which interacts with the README's existing
  referral-link section and wants care), 2026-08-19 (`/supply/float`, `/supply/unlocks`,
  plus a `mint` event type on `/event/calendar`), 2026-08-17 (`/volume/scanner`,
  `/volume/scanner/{symbol}`). Per the balance rule Sync creates no debt, so the standing
  position is unchanged: last 3 Fix/Build entries remain iter6 Build, iter7 Fix, iter8
  Fix, so a **Build** is still owed -- competing with the 24-bad-endpoint Fix sweep queued
  in iter 9, which remains the highest-leverage Fix available.
- 2026-08-25 iter 10 (Build): balance check confirmed iter10 owed a Build (iter6 Build,
  iter7 Fix, iter8 Fix -- 2 of 3 Fix; iter9 was Sync, which sits outside the Fix/Build
  balance rule per its own log entry above). Before acting on iter8's queued candidates
  ([[depeg]], [[dao]], [[tokenization]], [[tokenomics]]), re-verified each -- and caught
  an error in iter8's classification: `[[depeg]]` is NOT a missing page. It's already
  comprehensively covered by `wiki/concepts/risk-management/depeg-risk.md` (status good,
  916 words, named events incl. USDC/SVB and Terra/UST), which even lists "depeg" as a
  frontmatter alias -- but `tools/lint.py` doesn't resolve frontmatter aliases when
  checking wikilinks (confirmed: zero "alias" references in the script), so the 43
  pages/134 refs linking `[[depeg]]` still read as broken. Creating `depeg.md` would have
  duplicated `depeg-risk.md`'s content outright. Left it uncreated; queued the real fix
  (rewrite those 43 pages' `[[depeg]]` targets to `[[depeg-risk|depeg]]`, same pattern as
  the iter4/iter8 rename-mismatch batches) as a Fix-track item for a future iteration.
  The other three held up on inspection: no page exists for any of them under any
  filename or alias (checked via `find`), and each was already anticipated by an existing
  page's forward links -- [[governance-token]] lists `[[dao]]` as a frontmatter
  prerequisite, [[real-world-assets]] links `[[tokenization]]` in `related`, [[emissions]]
  links `[[tokenomics]]` in its Related section. Delegated authoring of all three to one
  sub-agent with explicit differentiation boundaries against the pre-existing adjacent
  pages. Created (all `type: concept`, `status: draft`, difficulty intermediate):
  [[dao]] (1,741 words -- proposal lifecycle, voting mechanisms incl. token-weighted/
  delegation/vote-escrow/quadratic/dTAO market-based, treasury custody incl. multisig vs.
  fully-on-chain, legal wrappers incl. Wyoming DAO LLC 2021 + CFTC v. Ooki DAO 2022-2023,
  notable examples incl. The DAO 2016 hack/ETH-ETC fork + Uniswap's Dec 2025 UNIfication
  fee-switch vote, failure modes incl. the 2022 Beanstalk $182M flash-loan governance
  attack -- defers to the pre-existing [[governance-token]] for the token instrument
  itself), [[tokenization]] (1,269 words -- general mint/custody/redemption mechanism one
  level above [[real-world-assets]]'s TradFi-specific treatment; custody-model spectrum
  fully-on-chain/wrapped/off-chain-SPV; explicitly covers native-crypto-value
  tokenization, not just RWA), [[tokenomics]] (1,434 words -- supply design, distribution/
  vesting cliffs, value-accrual mechanisms incl. Uniswap's 2025 buyback-and-burn,
  sinks-vs-faucets incentive design incl. the 2020 DeFi Summer liquidity-mining/mercenary-
  capital case study and Olympus's OHM collapse as a cautionary case, failure modes incl.
  hyperinflationary emissions and unlock overhangs -- umbrella page deferring to the
  pre-existing [[emissions]]/[[token-unlock-supply-event]]/[[staking]] stubs). No
  `Getting the Data` section on any of the three (structural/conceptual topics, no direct
  CryptoDataAPI endpoint -- matches iter6 precedent). Verified independently: all 30
  distinct wikilink targets across the three pages checked against the real file tree via
  `find`, zero broken links introduced; re-ran `tools/lint.py` myself -- links 240->234
  (partial resolution; `check_wikilinks` only flags pages with >5 broken links so some
  references now resolve without the source page dropping below threshold),
  tags/orphans/stale/empty/frontmatter byte-identical (659/39/6/51/0), confirming zero
  regressions. Per the balance rule, Fix is due next (last 3 Fix/Build entries will be
  iter7 Fix, iter8 Fix, iter10 Build -- 1 of 3 Fix, technically either track open, but two
  Fix candidates are already queued and ready: the `[[depeg]]`->`[[depeg-risk]]`
  rename-mismatch above, and iter9's higher-leverage 24-broken-endpoint-path sweep (166
  citations) which iter9 itself flagged as competing for the next Fix slot. `[[bnb-chain]]`
  (10 inbound refs) remains queued from iter8 as a further genuine Build gap if Build
  continues instead.
- 2026-08-26 iter 11 (Sync): `tools/check_api_changelog.py` found 6 unprocessed releases
  (2026-08-17 through 2026-08-25) -- more material content than one ~60-min batch could
  responsibly cover (a full new News/Catalyst family, a squeeze-alerts endpoint, a
  volume-scanner family, an exchange directory, supply/float+unlocks, and two additive
  fields). Per the Sync integration rules, picked the single highest-leverage, self-
  contained cluster and left the rest genuinely unprocessed rather than stretching the
  batch: the 2026-08-18 and 2026-08-21 releases are, together, entirely about ONE coherent
  signal family (news-derived catalyst detection + a closely-related forced-liquidation
  tripwire), already had zero wiki coverage, and tie directly into two existing strategy
  pages -- clean scope boundary, high real value (catalyst/event-driven signals are core
  AlgoBrain territory). MCP server tools still unreachable this session -- used
  `tools/lint.py`/`check_api_changelog.py` via venv Python directly, the now-standard
  fallback. **Delegated and verified:** created `wiki/data-sources/cryptodataapi-news.md`
  (new category page: `/news/pulse`, `/news/market-moving`, `/news/coin/{symbol}`,
  `/news/sources`, `/backtesting/news-events` -- filtered-tape caveat, match_mode/
  confidence tiers, corroboration, the 2026-08-21 nine-category policy-taxonomy expansion
  with its own origin story (a 2026-08-20 BTC 10% move + $3B of shorts liquidated on zero
  recorded catalyst events, root-caused to a missing legislation/executive-action/
  sovereign-buyer taxonomy), no-backfill-before-2026-08-18 hard start date); added
  `/market-intelligence/squeeze-alerts` to the existing `cryptodataapi-market-
  intelligence.md` endpoint table + a caveat paragraph (direction-naming convention,
  shared venue-coverage gap, `suppressed_by`/`include_quiet`); registered the new category
  on `cryptodataapi.md`'s category map + `related:`, and added a reverse link from
  `cryptodataapi-sentiment.md`; added a `Getting the Data` + `AI agent workflow` extension
  to `wiki/strategies/fundamental-analysis/news-trading.md` (previously cited zero
  `/news/*` endpoints despite its name) and a small, scoped addition to `crypto-policy-
  shock-trading.md` (the new `/news/market-moving` policy-category corroboration signal,
  plus a one-line caveat that a 2026-08-21 sign-error fix on `/policy/headlines` -- which
  had scored constructive "banking"/"banks" headlines as maximum-severity bans --
  improved that page's existing signal's reliability). **Sub-agent caught its own scope
  error**: the task brief named `event-driven-trading.md` as a target, but that page
  turned out to be an out-of-scope equity redirect stub (removed 2026-07-19 per CLAUDE.md
  scope rules) -- the sub-agent read the file, recognized the contradiction, left it
  untouched, and substituted the real crypto strategy page (`news-trading.md`) instead of
  silently complying with a premise the file itself disproved. Verification method: the
  sub-agent found WebFetch summaries of the live docs unreliable (inconsistent excerpts,
  one fabricated enum), so it downloaded the raw OpenAPI spec + docs HTML + public
  changelog JSON directly and parsed them for exact field/path text -- flagged one thing
  it could NOT verify (the pre-2026-08-21 crypto-native `category` enum is unpublished)
  and correctly omitted it rather than guessing. Verified independently: all 9 wikilinks
  added across the 5 touched files resolve to real files (checked via `find`); re-ran
  `tools/lint.py` myself -- links/tags/orphans/stale/empty/frontmatter byte-identical to
  iter10 (234/659/39/6/51/0), confirming zero regressions. **Marked material** in
  `.claude/cryptodataapi-changelog-state.json`: 2026-08-18, 2026-08-21. **Left
  unprocessed** (not noted -- genuinely deferred, not surfaceless): 2026-08-25 (`ret_90d`
  meme field, `sr` support/resistance field -- additive, low urgency), 2026-08-23
  (`/exchanges` venue directory -- ties well to the README's existing referral-link work,
  good next-Sync candidate), 2026-08-19 (`/supply/float` + `/supply/unlocks` as first-
  class endpoints -- natural pairing with the existing `token-unlocks.md` page; its
  unlock-coverage/entity-resolution fixes needed no wiki correction since no page cited
  the stale figures), 2026-08-17 (`/volume/scanner` family -- entirely undocumented,
  needs its own category page). Sync sits outside the Fix/Build balance rule -- last 3
  Fix/Build entries remain iter7 Fix, iter8 Fix, iter10 Build, so the next Fix/Build choice
  is still owed a **Fix** per the balance rule, competing candidates unchanged
  (`[[depeg]]`->`[[depeg-risk]]` rename, iter9's 24-broken-endpoint-path sweep).
- 2026-09-02 iter 12 (Sync): `tools/check_api_changelog.py` reported 8 unprocessed
  releases (2026-08-17 through 2026-08-28), including one **breaking** entry, and
  surfaced a real bug in the upstream feed itself: two distinct changelog entries (a
  breaking error-envelope change and an unrelated cache/security fix) both carry the
  identical version string `2026-08-26` — the feed's dedup key isn't unique. The state
  file can only hold one record per version, so both had to collapse into a single
  `2026-08-26` entry; noted here so a future iteration doesn't get confused if the report
  ever shows `2026-08-26` as unprocessed again after this. Triaged all 8: 4 marked
  **noted** (2026-08-28 onboarding/agent-UX polish, 2026-08-27 param bug-fixes, and the
  non-breaking half of 2026-08-26 — none had wiki-visible surface, no stale claims to
  fix); 4 marked **material** and absorbed this iteration (2026-08-17, 2026-08-19,
  2026-08-25, the breaking half of 2026-08-26); 1 left genuinely unprocessed
  (2026-08-23's new `/exchanges` venue directory — a real new category, deferred purely
  for batch size, good next-Sync candidate) plus one bullet of 2026-08-19 (the
  `/news/pulse` `headlines` field — belongs on `cryptodataapi-news.md`, not touched this
  batch). **Delegated and verified:** created `wiki/data-sources/cryptodataapi-supply.md`
  (new category page for `/supply/float` and `/supply/unlocks` — dilution overhang,
  `unlock_coverage: not_tracked` caveat, cliff-only calendar, DefiLlama coverage bound),
  registered on `cryptodataapi.md`'s category map + `related:`; updated `token-
  unlocks.md`'s `Getting the Data` section to cite the new dedicated supply endpoints
  alongside the existing `/event/calendar` reference; added the new `mint` event type
  (stablecoin mint/burn, `delta_usd`/`pct_of_supply`, observed-not-scheduled) and
  `ret_90d` (meme regime) to `cryptodataapi-regimes.md`; added the new `sr` (support/
  resistance) field to `cryptodataapi-indicators.md` with a trading-applications bullet
  linking the existing `[[support-and-resistance]]` concept page; added `/volume/scanner`
  + `/volume/scanner/{symbol}` and 3 new `/hyperliquid/summary` fields to `cryptodataapi-
  hyperliquid.md` with a relative-volume-screening bullet; added a one-paragraph note on
  the new consistent `401`/`403`/`429` JSON error envelope to `cryptodataapi.md`'s Access
  section. Explicitly left the existing GEX-is-Pro-tier note on `cryptodataapi-regimes.md`
  untouched — already correct from iter9, this release only fixed an inconsistent error
  *message*. Verification method: sub-agent downloaded the live OpenAPI spec
  (`curl https://cryptodataapi.com/api`, 397KB) and parsed every path/param/schema with
  Python rather than trusting changelog prose, and additionally minted a live free API key
  to curl real `401`/`403`/`429` responses confirming the exact error-envelope shape (one
  gap flagged honestly: a rapid-burst `429` test showed only `error`/`message`/`scope`,
  not the `Retry-After`/`X-RateLimit-*` headers CDA's own docs describe — likely Cloudflare
  edge-layer throttling short-circuiting the origin app on a same-second burst; wiki text
  attributes the richer set to CDA's docs, not to personal reproduction, and the gap is
  logged in `wiki/log.md` for future reconciliation). I independently re-verified all 4 new
  endpoint paths (`/supply/float`, `/supply/unlocks`, `/volume/scanner`, `/volume/scanner/
  {symbol}`) plus `SRLevelModel` against a fresh pull of the live OpenAPI spec myself
  rather than taking the sub-agent's word for it — all present. `git diff --stat`: 6 wiki
  files touched + 1 created, 134 insertions / 19 deletions, all wikilink targets confirmed
  to resolve (`[[support-and-resistance]]` exists at `wiki/concepts/indicators/`).
  Sync sits outside the Fix/Build balance rule — last 3 Fix/Build entries unchanged since
  iter11 (iter7 Fix, iter8 Fix, iter10 Build), so the next Fix/Build choice is still owed
  a **Build** per the balance rule (2 of the last 3 were Fix) — note this corrects iter11's
  entry, which mis-stated the owed track as Fix.
- 2026-09-03 iter 13 (Sync + Build, combined): `tools/check_api_changelog.py` reported
  exactly 1 unprocessed release (2026-08-23, the `/exchanges` venue directory deferred
  from iter12). Per the "small Sync batch ⇒ also do a Fix/Build pick" rule, and since the
  balance check owed a **Build** (last 3 Fix/Build entries: iter7 Fix, iter8 Fix, iter10
  Build — 2 of 3 Fix), combined both in one delegated batch. **Sync:** verified
  `GET /api/v1/exchanges` and `GET /api/v1/exchanges/{slug}` against the raw OpenAPI JSON
  and live curl responses (confirmed `{slug}` is a path param, not `?slug=`, correcting an
  assumption in the task brief) before writing anything; created
  `wiki/data-sources/cryptodataapi-exchanges.md` (new category page: `kind`/`specs`/
  referral fields, the disclosure-surfacing rule), registered on `cryptodataapi.md`'s
  category map + `related:`, cross-linked from `exchanges-overview.md`'s Start Here list.
  Marked `2026-08-23` material — `check_api_changelog.py` now reports zero unprocessed
  releases, wiki fully level with the upstream feed. **Build:** found 3 genuine
  high-inbound missing entity pages by direct grep (not just lint's truncated broken-link
  sample, which only lists the first ~5 targets per file): `[[asterdex]]` (46 refs across
  16 files — highest priority, a redirect stub `aster-2.md` and a full existing strategy
  map `asterdex-perp-trading-map.md` both already assumed it would exist), `[[lighter]]`
  (14 refs), `[[bnb-chain]]` (10 refs — queued twice before, in iter8 and iter9, never
  actioned). Created all three: `wiki/entities/exchanges/asterdex.md` (Dec 2024 APX
  Finance/Astherus merger, Mar 2025 "Aster" rebrand, hidden orders, USDF/asBNB yield
  collateral — 3 candidate "founding" dates all documented rather than one asserted),
  `wiki/entities/exchanges/lighter.md` (zk-rollup perp DEX, Jan 2025 beta, Dec 2025 LIT
  TGE), `wiki/entities/protocols/bnb-chain.md` (PoSA consensus, Feb 2022 BSC→BNB Chain
  rename, Oct 2022 bridge exploit — explicitly the protocol/chain layer, distinct from and
  linking back to the existing `bnb.md` token page rather than duplicating its "BNB Chain
  Ecosystem" section). Nicely paired with the Sync work: asterdex and lighter are 2 of the
  7 venues in the new `/exchanges` directory, and both new entity pages cite it in their
  `Getting the Data` sections. **Verified myself** rather than taking the sub-agent's word
  for it: re-pulled the live OpenAPI JSON and confirmed `/api/v1/exchanges`,
  `/api/v1/exchanges/{slug}`, `ExchangeListResponse`, `ExchangeDetailResponse`,
  `ExchangeSpecs` all present; confirmed every new wikilink target referenced from the 4
  new pages exists (`pancakeswap-token`, `venus`, `layer-1`, `bitcoin`, `edgex`,
  `dydx-chain`, `layer-2`); validated `.claude/cryptodataapi-changelog-state.json` as
  valid JSON with 14 unique version entries, no duplicates. `git status`/`git diff --stat`
  clean, no upstream divergence this time (unlike iter12). Fully hedged facts the
  sub-agent could not verify (AsterDEX's exact fee schedule and single founding date,
  Lighter's current fee/leverage figures, both venues' live TVL/OI) rather than asserting
  them. Lint: `tools/lint.py --check links --json` reports one entry per file with **>5**
  broken links, so the file-count (234) held steady while the underlying broken-link
  *instance* count dropped (~2,501 → ~2,491 per the sub-agent's more granular count) —
  consistent, not contradictory, since the files citing `bnb-chain`/`asterdex`/`lighter`
  each still have other unrelated broken links keeping them above the 5-link reporting
  threshold. Fix/Build balance now satisfied — this iteration's Build entry means the next
  Fix/Build choice starts a fresh 3-entry window (iter8 Fix, iter10 Build, iter13 Build:
  2 of 3 Build), so the next Fix/Build pick is owed a **Fix**.
- 2026-09-03 iter 14 (Fix): `tools/check_api_changelog.py` reported zero unprocessed
  releases (fully synced as of iter13) and no upstream git divergence, so this iteration
  was a clean Fix pick per the balance rule owed since iter13. Took the highest-leverage
  queued Fix candidate: iter9's template-aware sweep had found **24 distinct
  CryptoDataAPI endpoint paths cited in the wiki that do not exist** (166 citations),
  re-confirmed unchanged through iter10 and again by me this iteration before delegating.
  Scoped to the top 4 offenders (~119 of 166 citations, ~72%): `/market-intelligence/
  dvol-history` (55 cites), `/on-chain/whale-score/{symbol}` (39), `/volatility/dvol`
  (17), `/sentiment/fear-greed-index` (8). **The sub-agent caught something my brief got
  wrong**: I'd suggested `/volatility/index`(`/history`) as the DVOL replacement, but
  schema inspection showed that endpoint carries realized vol only (`cvi_realized_30`/
  `cvi_realized_7`) with no implied-vol field at all — the real match is
  `/volatility/implied` (`items[].{dvol, dvol_change_24h, realized_30, vrp, history[],
  term_structure[]}`), which every citing page (Deribit-implied-vol option gates)
  actually needs. It also found the whale-score replacement
  (`/on-chain/whales/accumulation-score/{symbol}`) is currently **disabled upstream**
  ("🚧 Coming soon"), scoped to **ERC-20 tokens only** (USDT/USDC/WBTC/WETH, not native
  BTC), and returns a categorical `signal` (`accumulating`/`neutral`/`distributing`/
  `unknown`) rather than the continuous 0-100 score several strategy pages built numeric
  Gate thresholds on — it fixed the path everywhere AND added honest inline caveats
  rather than silently swapping the path and leaving the numeric-threshold claims wrong.
  fear-greed-index → fear-greed was a clean path swap, fields matched. **44 wiki pages +
  CHANGELOG.md touched**, incl. two hub pages with real content additions: `cryptodataapi-
  on-chain.md` (rewrote the disabled-family warning box with the ERC-20 scope and real
  `signal` enum) and `cryptodataapi-regimes.md` (new subsection documenting `/volatility/
  index`, `/volatility/index/history`, and `/volatility/implied` for the first time —
  these were never previously documented anywhere in the wiki despite being cited, wrong,
  from 14 strategy pages). Full file list and the two Gate-1 strategy pages needing
  numeric-threshold recalibration (still flagged inline, not resolved) are in
  `wiki/log.md`'s 2026-09-03 Fix entry. **Verified independently, not on trust:**
  re-pulled the live OpenAPI spec and confirmed `/volatility/implied` and
  `WhaleAccumulationScoreResponse` match exactly what the sub-agent reported (including
  the disabled-status description text and ERC-20 scope), re-grepped all of `wiki/` for
  the 4 old broken path strings myself — zero remaining citations outside one deliberate
  historical-explanation mention on `cryptodataapi-on-chain.md`. Re-ran lint: byte-
  identical at 991 issues (links 234/tags 659/empty 51/orphans 39/stale 8) — this was a
  path/prose correction, not a link-topology change, so no shift expected or seen.
  **Flagged but explicitly not touched** (2 items the sub-agent found while grepping,
  outside this batch's 4-path scope): `alternative-data-alpha.md` also cites
  `/on-chain/mvrv` (not real; should be `/on-chain/dormancy/btc`), and
  `event-vol-buying.md` claims "No CryptoDataAPI endpoint for event calendar" which is
  now stale (`/event/calendar` exists) — both queued as small future Fix items alongside
  the ~20 remaining broken paths from the original sweep (`/derivatives/hyperliquid/
  funding-rates` 7x, `/market-intelligence/borrow-interest` 10x, `/market-intelligence/
  grayscale/*` — possibly retired outright, and a long tail of ~18 more paths / ~30
  citations) — deliberately deferred, not stretched into this batch. Fix/Build balance:
  this is a Fix entry, so the 3-entry window is now iter10 Build, iter13 Build, iter14
  Fix (1 of 3 Fix) — next Fix/Build pick has no balance constraint either way, judge on
  merits.
- 2026-09-04 iter 15 (Fix): `tools/check_api_changelog.py` reported one new release
  (2026-09-03, `why_subscribe` added to the `upgrade` object on 403s/429s) — marked
  **noted**, consistent with the parent `upgrade` object's own 2026-08-28 disposition
  (no wiki page documents the tier-403/429 upgrade-path shape in enough detail to need
  it). No upstream git divergence. With the balance rule unconstrained, chose to finish
  the endpoint-correctness sweep from iter14 rather than start something new — a known,
  well-scoped bug is higher-leverage than exploring fresh Build territory. Did **not**
  reuse iter9's stale citation counts: had the sub-agent rebuild the broken-path list
  from a fresh OpenAPI pull + full wiki grep first, since pages had changed since iter9.
  Found **11 real broken paths (~47 citations, 17 pages)**, closing out the sweep begun
  at iter9: `/market-intelligence/borrow-interest` and `/market-intelligence/grayscale/
  {holdings,premium}` (12 cites, 6 files) confirmed **retired with no replacement** —
  struck through with a dated warning on `cryptodataapi-market-intelligence.md`'s
  endpoint table and every citing page, pointing at perp funding as the leverage-cost
  fallback (ADD-never-destroy: struck through, not deleted); `/derivatives/hyperliquid/
  funding-rates` → `/hyperliquid/funding-rates` (7x); `/derivatives/hyperliquid/mark-
  price` → `/hyperliquid/summary`'s `mark_price` field (4x, an invented path with no
  real analog at that path); `/volatility/realized?coin=BTC&days=30` →
  `/volatility/index` (`majors[].realized_30`+`vrp` — the real endpoint already carries
  a pre-computed variance-risk-premium field the invented one never would have had);
  `/volatility/correlation` (no such endpoint, corrected to state it must be computed
  from klines); `/blockchain/exchange-flows` → `/on-chain/exchange-flows/{spike-alerts,
  {symbol}}` (3x, added an EVM+Solana-only coverage caveat); `/backtesting/archives-
  index` → `/backtesting/archives/index` (2x, a slash-vs-hyphen typo); `/on-chain/mvrv`
  → `/on-chain/dormancy/btc` (`metrics.mvrv`+`mvrv_signal.zone` — this was iter14's
  flagged-but-deferred item); `/sentiment/stablecoin-flows` → `/sentiment/stablecoins`
  (1x); `/dex/tokens` → `/coins/{symbol}` + `/dex/token/{chain}/{address}` (1x). Also
  fixed iter14's second flagged item: `event-vol-buying.md`'s stale "No CryptoDataAPI
  endpoint for event calendar" claim (predated `/event/calendar`'s addition) — and while
  fixing it, caught and fixed a pre-existing, unrelated `?days=30` vs `?window_days=30`
  param-name bug in the same page's AI-agent-workflow section. Correctly identified 6
  false positives and left them alone (curl `<PLACEHOLDER>` truncation artifacts,
  deliberate `/api/v1/backtesting/*` and `/api/v1/dex/*` wildcard-family prose, and one
  citation of Santiment's `/api/v1/social_volume` explicitly labeled non-CryptoDataAPI).
  **Verified independently, not on trust:** re-pulled the live OpenAPI spec and confirmed
  every one of the 11 old paths is genuinely absent and every replacement path exists;
  drilled into the actual response schemas (`HLSummaryResponse.mark_price`,
  `VolatilityIndexResponse.majors[]` → `MajorVolEntry.{realized_30,vrp}`,
  `DormancyResponse.metrics.mvrv` + `.mvrv_signal.zone`) and confirmed every field name
  the sub-agent cited actually exists at exactly that path — did not just trust the
  prose claims. Re-grepped `wiki/` for all 11 old path strings: zero remaining live
  citations. Re-ran lint: byte-identical at 991 issues (links 234/tags 659/empty
  51/orphans 39/stale 8) — a path/prose correction, no link-topology change, as expected.
  **Caught and fixed one sub-agent error before shipping**: its `CHANGELOG.md` edit had
  *overwritten* the existing "2026-09-03 — Fix 4 confirmed-broken..." heading with the
  new "2026-09-04" heading instead of inserting above it, silently merging two distinct
  dated entries' prose under one heading — a real violation of the ADD-never-destroy
  rule that would have lost the iter14 entry's own dateline. Restored the missing
  heading before committing. `wiki/log.md`'s edit did not have this bug (correctly
  prepended). **The endpoint-correctness sweep begun at iter9 is now fully closed** —
  24 of 24 flagged broken paths fixed across iter14+iter15 (166 of 166 citations
  addressed, either fixed or marked retired with no replacement). Also noticed (not
  investigated further, future Fix candidate): `cryptodataapi-market-intelligence.md`'s
  endpoint table has a pre-existing duplicate `squeeze-alerts` row (two entries, slightly
  different tier text) unrelated to this batch. Fix/Build balance: another Fix entry —
  window is now iter13 Build, iter14 Fix, iter15 Fix (2 of 3 Fix) — next Fix/Build pick
  is owed a **Build**.
- 2026-09-05 iter 16 (Build): `tools/check_api_changelog.py` reported one new release
  (2026-09-04, `upgrade` object + `Retry-After` extended to edge-authed endpoints'
  403s/429s) — marked **noted**, third release in this same consistency-fix family
  (2026-08-28, 2026-09-03) and same reasoning each time: no wiki page documents the
  tier-403/429 upgrade-path shape in enough detail to need it. No upstream git
  divergence. Balance rule owed a Build (iter14 Fix, iter15 Fix = 2 of last 3). Surveyed
  the wiki's 31 `status: stub` pages, counted inbound-wikilink demand for each via grep,
  and picked the top 5 by count: [[lending]] (11), [[emissions]] (11), [[mica]] (10),
  [[synthetic-dollar]] (8), [[crypto-market-regimes]] (7) — all genuinely thin (one
  paragraph + bare Related list, missing `domain`/`prerequisites`/`difficulty`
  frontmatter) despite the real demand. Expanded all 5 to full concept pages: DeFi vs.
  CeFi lending mechanics (with the 2022 CeFi contagion case study); emission-schedule
  taxonomy built explicitly on [[cryptodataapi-supply]]'s documented emissions-vs-cliff-
  unlock distinction (correctly added NO `Getting the Data` section since no genuine
  endpoint covers continuous emissions); MiCA's CASP-licensing/EMT-ART framework
  (pointing to the existing [[stablecoin-regulation]] table rather than duplicating it,
  citing `/policy/*` for the general regulatory-headline surface); the synthetic-dollar
  delta-neutral mechanism with a 4-way stablecoin-design comparison table, consistent
  with [[ethena-usde]]'s existing figures; and a rewrite of `crypto-market-regimes` as
  the accessible bridging page to the much deeper [[crypto-market-regime-taxonomy]] and
  [[regime-strategy-playbook]] rather than a duplicate of either. All 5 moved
  `stub` → `good`. **Verified independently, not on trust:** re-pulled the live OpenAPI
  spec and confirmed all 6 distinct endpoints cited across the batch
  (`/derivatives/funding-rates`, `/derivatives/summary`, `/policy/headlines`,
  `/policy/regime`, `/policy/regime/score`, `/sentiment/stablecoins` +
  `/remote-history`) exist exactly as claimed; checked every wikilink added across all 5
  pages (30+ distinct targets, including less-common ones like `[[compound]]`,
  `[[flash-loans]]`, `[[governance-token]]`, `[[basis-carry-regime]]`,
  `[[regime-adaptive-strategy]]`) against the wiki filesystem — zero forward links, 100%
  resolve. `git status`/`git diff --stat` confirmed only the 5 target concept pages were
  touched. Re-ran lint: 991 → 987 (empty 51 → 47, consistent with genuine content
  replacing near-empty stubs; links/tags/orphans/stale unchanged at 234/659/39/8 — no
  regressions). Fix/Build balance: this is a Build entry — window is now iter14 Fix,
  iter15 Fix, iter16 Build (1 of 3 Build) — next Fix/Build pick has no balance
  constraint either way. 26 stub pages remain (of the original 31) for a future Build
  iteration, ranked by inbound-link count if that signal still holds.
- 2026-09-06 iter 17 (Build): `tools/check_api_changelog.py` reported zero unprocessed
  releases (fully synced). No upstream git divergence to worry about from my own
  changes, but found and fast-forward-pulled a real upstream commit from the actual
  user (`463679f "Make MCP setup cross-platform"` — FastMCP 1.x → MCP SDK 2.x migration,
  new `tools/manage_mcp.py` cross-platform entry point, README/command-file updates)
  before starting; confirmed the MCP server still worked post-migration via a live
  `wiki_stats` call before proceeding. Balance rule had no constraint (iter15 Fix,
  iter16 Build = 1 of 3 Build). Considered a Fix pass on the 659-page non-approved-tags
  backlog first, but tallied actual tag frequencies and found it's now a long diffuse
  tail (max 10 uses for any single tag, versus the 20-30+ concentrated wins previous tag
  audits found) — lower leverage than continuing the stub-expansion method that worked
  cleanly last iteration, so stayed Build. Ranked the wiki's remaining 16 non-source
  `status: stub` pages by inbound-link count and took the next 5: `[[bitcoin-mining]]`
  (7), and a 4-way pick from an 8-way tie at 6 refs each — `[[paxos]]`, `[[securitize]]`,
  `[[delegated-proof-of-stake]]`, `[[justin-sun]]` — chosen for cross-linking synergy
  with recent work (MiCA/stablecoin-regulation, tokenization, BNB Chain's PoSA
  consensus). All 5 expanded to full pages with complete frontmatter, moved
  `stub` → `good`. Full per-page detail in `wiki/log.md`'s 2026-09-06 entry (same
  detail level as always, not duplicated here) — notably including a real cross-page
  consistency reconciliation (DPoS page vs. `bnb-chain.md`'s PoSA description) and one
  deliberately omitted unverifiable claim (a Justin Sun/Poloniex-hack-response detail no
  wiki source confirmed). **Caught and fixed a sub-agent error before shipping**:
  `justin-sun.md`'s frontmatter used `founded: 1990` for a birth year and an empty
  `website: ""` — checked 4 other `entity_type: person` pages on this wiki and confirmed
  neither convention is used for a person page here; removed both fields (the birth year
  was already in the lead paragraph, so no information was lost). **Verified
  independently, not on trust:** re-pulled the live OpenAPI spec and confirmed all 4
  `/on-chain/*` endpoints cited on `bitcoin-mining.md` exist exactly as claimed; checked
  all 27 distinct new wikilink targets across the 5 pages against the wiki filesystem —
  zero forward links, 100% resolve; `git status`/`git diff --stat` confirmed only the 5
  target pages were touched (plus the pre-existing, expected `changelog-state.json`
  `last_checked` bump from step 1's check). Re-ran lint: 987 → 982 (empty 47 → 42,
  exactly matching the 5 pages expanded; links/tags/orphans/stale unchanged at
  234/659/39/8 — no regressions). Fix/Build balance: another Build entry — window is now
  iter15 Fix, iter16 Build, iter17 Build (2 of 3 Build) — next Fix/Build pick is owed a
  **Fix**. 21 stub pages remain (11 non-source + 10 gap-finder source stubs, the latter
  not really candidates for this expansion method) for future iterations.
