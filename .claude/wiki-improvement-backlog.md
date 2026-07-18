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

- [ ] A1. Un-orphan ~1,300 crypto coin pages: write `tools/build_coin_index.py` generating
      A–Z index pages (e.g. `wiki/markets/crypto/coin-index-a-z.md` + per-letter sections)
      wikilinking EVERY coin page; link the index from `crypto-overview.md` and `wiki/index.md`.
- [ ] A2. Refresh stale counts: `wiki/overview.md` (~3,500 → 4,852 pages; markets ~1,150 →
      2,467) and `wiki/data-sources/data-sources-overview.md` (same stale fork claim + date).
- [ ] A3. Broken-link round 2 (~1,200 refs): stubs/redirects for top targets —
      stablecoin(→stablecoins), depeg, tether(→tether-limited), tokenization,
      optimistic-rollup, decentralized-finance(→defi), binance-coin(→bnb),
      zero-knowledge-proof(→zero-knowledge-proofs), dao, altcoins, gaming-tokens,
      delegated-proof-of-stake, data-availability, crypto-market-regimes, justin-sun (entity
      stub), and next ~10 by frequency. Unlink `nvidia` (out of scope).
- [ ] A4. Repair 4 truncated `2026-04-22-gap-finder-…` source links (~206 refs): find real
      filenames in `wiki/sources/`, fix links by script (or add redirect pages).
- [ ] A5. Frontmatter: add tags to the 18 pages missing them; fix 3 non-schema statuses
      (`proposed` ×2, `active-catalyst-window` ×1 → nearest schema value, note in body).
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
- [ ] B2–B8. Combination batches 2–8: ~5 new combination pages each, chosen from the matrix's
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
