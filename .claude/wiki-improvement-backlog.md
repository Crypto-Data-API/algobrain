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
- [ ] A9. Same-stem collisions — CLASSIFIED (iter 9), dispositions per bucket:
      (a) redirect-vs-real (21 stems, incl. gamma-scalping ×3): delete the redirect twin
          after merging its aliases into the real page (check each redirect's target first —
          circular ones are broken anyway; sector-rotation's scope-note needs care since
          indicators/sector-rotation may itself be equity-scoped);
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
- [ ] B11. Essay→buildable upgrades — RE-SCOPED (iter 10): 99 type:strategy pages lack
      edge_source, BUT many are intentional companion guides (arbitrage-* meta pages) and
      options STRUCTURE pages that the 2026-07-14 waves deliberately kept on a structure
      template (see wiki/log.md Wave 3: "No buildable-alpha schema was bolted onto
      theory/structure pages"). Plan: TRIAGE batch first — classify all 99 into
      {companion-guide OK | structure-page OK | genuine strategy needing upgrade}, record
      the classification here, then upgrade only the genuine ones in batches of ~10.
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
