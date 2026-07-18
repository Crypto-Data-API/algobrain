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
- [ ] A3. Broken-link round 2 (~1,200 refs): stubs/redirects for top targets —
      stablecoin(→stablecoins), depeg, tether(→tether-limited), tokenization,
      optimistic-rollup, decentralized-finance(→defi), binance-coin(→bnb),
      zero-knowledge-proof(→zero-knowledge-proofs), dao, altcoins, gaming-tokens,
      delegated-proof-of-stake, data-availability, crypto-market-regimes, justin-sun (entity
      stub), and next ~10 by frequency. Unlink `nvidia` (out of scope).
- [x] A4. (2026-07-19, iter 4) Gap-finder citation repair: 7 source stubs created (4 from
      audit + 3 more variants found in full scan), comma-variant links normalized in 3 files.
      Broken gap-finder refs 228 → 0.
- [x] A5. (2026-07-19, iter 4) Tags added to all 18 pages missing them; 3 non-schema
      statuses fixed (proposed→draft ×2, active-catalyst-window→review).
- [ ] A6. Tags: normalize variants (stablecoin→stablecoins, perpetuals→perpetual-futures, …);
      review the `stocks` tag on 132 pages (scope smell — retag or rescope); adopt genuinely
      useful new tags (macro, security, solana, real-world-assets, execution, exploits,
      trading-bots, strategy-development, hedging, anomalies, narrative-impact) into the
      approved list in BOTH CLAUDE.md and AGENTS.md.
- [ ] A7. Remove 10 pure-equity strategy pages: value-averaging, fundamental-analysis/
      sector-rotation, fundamental-analysis/event-driven-trading, combinations/
      momentum-value-combination, combinations/fundamental-technical-fusion,
      algorithmic/factor-investing (or crypto-rewrite), quantitative/calendar-effects,
      arbitrage/prime-broker-cascade-trading, arbitrage/block-trade-flipping-arbitrage,
      leveraged-etf-rebalancing. Fix inbound links to them.
- [ ] A8. Duplicates: basis-trade → redirect to basis-trading (keep a Treasury-basis note);
      resolve delta-hedging vs delta-hedged-options; review duplicate titles (Algorithmic
      Trading ×4, DCA ×3, Convex Finance ×3, dYdX ×3, Backtesting ×3, Beefy ×2) — merge or
      cross-link coin-page vs entity-page pairs.

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
- [ ] B2–B8 (B2 ✓ iter 2; B3 ✓ iter 3; B4 ✓ iter 4; 54 planned cells remain). Combination batches: ~5 new combination pages each, chosen from the matrix's
      highest-value unfilled cells; update matrix each time. Continue until every viable cell
      is filled or explicitly marked non-viable ("all possible combinations").
- [ ] B9. Kill-criteria completion: add `kill_criteria` frontmatter + "## Kill criteria"
      section to buildable strategy pages missing them (~80–120 pages, batches of ~25).
- [ ] B10. Example-trade completion: add "## Example trade" with concrete round-trip numbers
      (marked illustrative) to buildable pages missing one (~160 pages, batches of ~25).
- [ ] B11. Essay→buildable upgrades: upgrade ~100 essay-style strategy pages (no edge_source)
      to the full schema, batches of ~10, worst-first (technical-analysis/, combinations/).
- [ ] B12. Expand ~15 true stub concepts (ai-agents, depin, gamefi, liquidations, layer-1,
      mev, zk-rollup, etc.) from stub to real pages (200+ words, examples, links).

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
