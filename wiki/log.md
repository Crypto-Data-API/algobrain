---
title: "Wiki Operations Log"
type: index
created: 2026-07-13
updated: 2026-09-09
status: good
tags: [meta, log]
---

Chronological, append-only record of all wiki operations. Newest entries at the top.

## 2026-09-09 — Build: expanded 5 DePIN/infra concept stubs; skipped 2 deliberately-thin bios

**Scope:** ranked the wiki's remaining `status: stub` pages by inbound-link count as
usual, but found the top 2 (mark-jurik, arnaud-legoux, 6 refs each) are **not** content
gaps — both are already thorough, well-sourced pages deliberately kept at `stub` status
because their subjects (Jurik Moving Average and Arnaud Legoux Moving Average's
creators) have genuinely thin, unverifiable public records, and the pages themselves
say so explicitly ("Status is stub and should stay there"). Expanding either would mean
fabricating biographical detail the pages correctly refuse to assert. Skipped both and
moved to the next tier: 5 DePIN/crypto-infrastructure concepts (5-6 refs each), all
genuinely thin one-paragraph stubs this time.

- **[[decentralized-identity]]** — DID/verifiable-credential/soulbound-token primitives,
  a three-way proof-of-personhood comparison (biometric/social-graph/credential-
  aggregation), the privacy-surveillance tension (Worldcoin's ZK-unlinkability claim
  flagged as a live debate, not a settled guarantee), and identity-gated airdrops as the
  trading-relevant mechanism. Cross-checked against [[worldcoin-wld]] and
  [[ethereum-name-service]] without contradicting either.
- **[[decentralized-compute]]** — the two-sided marketplace mechanism, token-incentive
  bootstrapping and mercenary-capital risk (using Akash's own Q1 2026 lease-count-up/
  revenue-down disclosure as a concrete illustration), Render's and Akash's burn-and-mint
  mechanisms, and the AI-compute-shortage demand thesis — sitting inside, not
  duplicating, the general [[depin]] page.
- **[[decentralized-storage]]** — contrasts Filecoin's renewable PoRep/PoSt contract
  model, Arweave's pay-once endowment model, and Walrus's newer erasure-coded ("Red
  Stuff") design, with an explicit hedge that Walrus's mechanism is less battle-tested
  than the other two's multi-year track record.
- **[[trusted-execution-environment]]** — SGX/SEV/TrustZone mechanics, the three crypto
  use cases (confidential compute, oracle attestation, MEV/encrypted-mempool
  infrastructure via Flashbots' SUAVE), and an honest, named exploit history (Foreshadow
  2018, Plundervolt 2019, the broader MDS side-channel family) — explicitly flagged as
  illustrative and non-exhaustive rather than a complete list.
- **[[move-language]]** — the resource-type-system design (no-copy, no-implicit-discard)
  contrasted with Solidity's mapping-based accounting, the Aptos-vs-Sui dialect
  divergence (account-centric/Block-STM vs. object-centric/Mysticeti), and an honest
  limit: Move's resource safety did not prevent the May 2025 Cetus exploit on Sui
  ($223M) because that was application-level math (a u256 overflow), not a language
  flaw.

All 5 moved `stub` → `good` with full `domain`/`prerequisites`/`difficulty` frontmatter.
None received a `Getting the Data (CryptoDataAPI)` section for a real reason in each
case (checked, not skipped by default): these are infrastructure/mechanism concepts, not
tradeable-signal topics, and CryptoDataAPI has no identity/DePIN-usage/TEE/language-level
endpoints — where a related token already has its own verified endpoint section (WLD,
ENS, RENDER, IO, FIL, AR), the page links there instead of duplicating it.

**Verified independently, not on trust:** checked all 30 distinct wikilink targets
referenced across the 5 pages against the wiki filesystem — zero forward links, 100%
resolve, including less-common ones (`civic`, `gitcoin`, `humanity`, `bittensor`,
`iexec-rlc`, `oasis-network`, `movement`). `git status`/`git diff --stat` confirmed only
the 5 target pages were touched — `mark-jurik.md` and `arnaud-legoux.md` correctly left
alone. Re-ran lint: 974 → 970 (empty 42 → 38; links/tags/orphans/stale unchanged at
234/659/31/8 — no regressions). 8 non-source stub pages remain (12 minus the 5 done
here minus the 2 correctly-excluded bios still counted as "stub" but not real Build
candidates using this method).

## 2026-09-08 — Sync: CryptoDataAPI 2026-09-07 release (x402 three-rail payments, hl-liquidations)

**Scope:** absorbed the 2026-09-07 upstream API release (already pre-marked `material` in `.claude/cryptodataapi-changelog-state.json`) — a significant expansion of x402 agent payments plus one brand-new backtesting endpoint. All endpoints and response fields verified against the live OpenAPI JSON (`https://cryptodataapi.com/api`) and live curl tests (a throwaway free key was minted for verification purposes) before writing.

- **[[cryptodataapi-mcp]]** — expanded the existing single-flow x402 section (`agent-subscribe` + `plan:"monthly"`) into three documented rails, keeping the original curl example intact:
  1. **Pay per time** — `agent-subscribe` and the parallel `subscribe` endpoint now take 6 plan values beyond the original `monthly`/`annual` (`pass_1h`, `pass_1d`, `pass_7d` → Pro; `pass_1h_plus`, `pass_1d_plus`, `pass_7d_plus` → Pro Plus), confirmed against the live `AgentSubscribeRequest`/`SubscribeRequest` schemas.
  2. **Pay per request** — 6 endpoints (`quant/whales`, `quant/market`, `regimes/current`, `market-intelligence/liquidations`, `event/calendar`, `market-intelligence/etf/{asset}/flows`) now 402 instead of 401 when keyless; documented the live-verified 402 body (`accepts[]`, `resource`, `extensions.bazaar`, `price_usd`, `route_id`, `grants_tier`, `alternatives`) from a real unauthenticated `GET /quant/whales` call.
  3. **Pay per resource** — new `GET /backtesting/archives/purchase`; live-verified the 404-before-quote guarantee on a missing object and the 402 quote shape on a real one.
  - Added `GET /api/v1/pricing` as the price-lookup endpoint for all three rails.
  - Hedged one brief-supplied field (`seconds_remaining` on the subscribe success response) as reported-but-unconfirmed, since that response is untyped (`schema: {}`) in the published OpenAPI spec and could not be produced without an actual USDC payment.
- **[[cryptodataapi-backtesting]]** — added `/backtesting/hl-liquidations` (new, Pro tier since 2026-09-07 — the per-event Hyperliquid liquidation tape, ~30-day hot window) and `/backtesting/archives/purchase` (pay-per-resource, cross-referenced to `cryptodataapi-mcp`'s payment detail rather than duplicated) to the endpoint table, with prose distinguishing `hl-liquidations` (Hyperliquid per-event fills) from the existing `liquidations` (cross-exchange summary).
- **[[cryptodataapi]]** — small addition to the Access section's error-envelope paragraph: the `403`/`429` `upgrade` object gained `passes`, `pay_per_request`, and `pricing_api` fields (live-confirmed on both a triggered `403` and a triggered `429`).

**Verification note:** every endpoint and field cited was checked against the live OpenAPI JSON's `paths`/`components.schemas`, plus direct curl tests (some requiring a throwaway free key) for the 402/403/404/429 response bodies — nothing in this batch was taken on the brief's word alone.

## 2026-09-07 — Fix: un-orphaned 8 substantive zero-inbound-link pages

**Scope:** the wiki's 39 lint-flagged "orphan" pages split into two very different
buckets on inspection — 13 are `type: redirect` stubs, correctly orphaned by design
(nothing should link to a redirect alias), and 26 are real, substantive content pages
(mostly `status: good`/`excellent`) that genuinely have zero inbound wikilinks despite
solid content — undiscoverable via the wiki's link graph. Picked the 8 highest-value
ones and found genuine (not forced) conceptual connections to link them from, adding
real inline-prose wikilinks rather than padding `## Related` lists alone:

- **[[put-call-ratio]]** — linked from [[deribit]] ("Put/call ratios, skew, and OI
  changes on Deribit serve as leading sentiment indicators") and
  [[sentiment-analysis]] (a section literally titled "Put/Call Ratio" that had never
  linked the actual page).
- **[[margin-debt]]** — linked from [[market-bubbles]] and [[deleveraging]] ("high
  aggregate leverage (measured by margin debt...)").
- **[[pensions]]** — linked from [[2022-09-uk-mini-budget-crisis]] (two prose
  mentions of UK pension-fund LDI strategies) and a new row added to
  [[deleveraging]]'s Historical Episodes table for the 2022 UK Gilt/LDI crisis as a
  cross-asset forced-selling case study.
- **[[casey-rodarmor]]** — linked from [[bitcoin-ordinals]] ("created by developer
  Casey Rodarmor") and [[bitcoin-runes-brc20-arbitrage]] ("Casey Rodarmor's Runes
  protocol activated at halving block 840,000").
- **[[zagabond]]** — linked from [[azuki]] ("Azuki's pseudonymous founder Zagabond
  published a blog post...") — a genuine gap, since Azuki's page never linked its own
  founder.
- **[[metakovan]]** — linked from [[beeple]] ("Buyer: MetaKovan (Vignesh
  Sundaresan)") — same gap pattern: Beeple's page named MetaKovan five times without
  ever linking him.
- **[[sophisticated-investor]]** — linked from [[securitize]] (the exact unlinked
  "Reg D for U.S. accredited/qualified investors" phrase) and [[real-world-assets]]
  ("most institutional products remain permissioned to accredited/qualified
  investors"). Checked [[paxos]] and [[tokenization]] too — neither mentions
  accredited/qualified investors, so correctly left unlinked there.
- **[[cfd-trading]]** — linked from [[asic]] and [[esma]] (both regulators'
  CFD-restriction actions) — the originally-suggested [[perpetual-futures]] link
  didn't pan out (that page never mentions CFDs at all), so the regulator pages were
  the genuine natural fit instead.

13 files touched, all small (2-8 line diffs) — this is a link-addition pass, not a
content rewrite. Verified independently: re-grepped for inbound links on all 8 targets
myself (not just trusting the sub-agent's report) — all 8 now show 1-2 genuine inbound
links; spot-read the `deleveraging.md` and `securitize.md` diffs directly and confirmed
minimal, well-integrated, contextually correct insertions. Re-ran lint: orphans 39 → 31
(exactly the 8 fixed), everything else unchanged (links 234/tags 659/empty 42/stale 8)
— no regressions, no side effects on unrelated pages. 18 non-redirect orphans remain
(26 minus the 8 done here) for a future Fix iteration.

## 2026-09-06 — Build: expanded 5 more thin stub pages (bitcoin mining, Paxos, Securitize, DPoS, Justin Sun)

**Scope:** second stub-expansion batch, same method as 2026-09-05's — ranked the wiki's
remaining `status: stub` pages by inbound-wikilink count and expanded the top 5
(6-7 refs each) from a one-paragraph lead to a full page.

- **[[bitcoin-mining]]** (7 inbound refs) — PoW security mechanism, hashrate/difficulty-
  adjustment mechanics (2,016-block retarget), miner revenue (subsidy + fees), mining
  economics (ASIC/energy costs, hash price/breakeven), a full miner-capitulation-dynamics
  section cross-checked against [[miner-capitulation-bottom]] to avoid contradicting its
  small-sample/ETF-era-dampening caveats, and public-miner coverage (MARA, Hut 8, Core
  Scientific, Bitdeer). `Getting the Data` cites `/on-chain/miners/reserves`,
  `/on-chain/miners/hash-ribbon`, `/on-chain/dormancy/btc`, `/on-chain/score`. Fixed a
  stale link along the way: the stub's `[[halving]]` target is only a redirect stub —
  repointed to the real, richly-developed `[[bitcoin-halving]]` page.
- **[[paxos]]** (6 inbound refs) — NYDFS trust-charter regulatory model, full stablecoin-
  issuance history (USDP/BUSD/PYUSD/Global Dollar), the February 2023 BUSD wind-down as a
  regulatory case study, and its tokenization/settlement business. Cross-linked to
  [[mica]] and [[stablecoin-regulation]] (both recently built) as the wiki's clearest
  regulated-issuer example. No `Getting the Data` section — Paxos itself isn't a priced
  token; USDP/PYUSD carry their own endpoints on their own pages.
- **[[securitize]]** (6 inbound refs) — the SEC-registered-transfer-agent/broker-dealer
  regulatory model (not an unregistered token issuer), its flagship tokenized-RWA
  products (BlackRock BUIDL, STAC, ACRED, a VanEck fund), and why they trade as
  effectively-zero-secondary-volume sector barometers rather than directional
  instruments. Cross-linked to the existing [[tokenization]] page's off-chain custody/SPV
  model. No `Getting the Data` section — no CryptoDataAPI price endpoint is meaningful for
  permissioned, whitelist-only securities.
- **[[delegated-proof-of-stake]]** (6 inbound refs) — DPoS mechanism, tradeoffs vs. plain
  PoS, the EOS vote-buying/cartel critique, and canonical examples (TRON, EOS, Hive/Steem,
  ARK, GXChain). **Reconciled a real cross-page tension**: the stub previously implied
  "early BNB Chain" was a DPoS chain; [[bnb-chain]] (built two iterations ago) documents
  its actual consensus as Proof of Staked Authority, an explicit PoA/DPoS hybrid — added a
  dedicated section correcting this and keeping the two pages consistent rather than
  contradictory.
- **[[justin-sun]]** (6 inbound refs) — TRON founding (Aug 28, 2017 genesis), the 2020
  Steemit acquisition and Hive fork, HTX advisory role, USDD/TRON DAO Reserve history, the
  March 2023 SEC civil complaint (stayed Feb 2025, reported dismissed with prejudice March
  6, 2026 per aggregator tracking on [[bittorrent]] — explicitly flagged as reported, not
  independently confirmed), and the 2025-2026 World Liberty Financial wallet-freeze
  dispute. Deliberately omitted an unverifiable Poloniex-hack-response claim rather than
  guessing. **Caught and fixed a frontmatter error before shipping**: the sub-agent had
  used `founded: 1990` for Sun's birth year and an empty `website: ""` — checked 4 other
  `entity_type: person` pages on this wiki and confirmed neither field is used that way
  for a person (birth year belongs in prose, which the lead paragraph already had;
  `website` is omitted rather than left empty) — removed both fields.

All 5 pages moved `status: stub` → `good` with full frontmatter. Verified independently:
re-pulled the live OpenAPI spec and confirmed all 4 cited `/on-chain/*` endpoints exist
exactly as claimed; checked all 27 distinct new wikilink targets across the 5 pages
against the wiki filesystem (mara, hut-8, core-scientific, bitdeer-technologies,
on-chain-analysis, paxos-standard, pyusd, binance-usd, global-dollar,
2023-02-busd-wind-down, blackrock-usd-institutional-digital-liquidity-fund,
securitize-tokenized-aaa-clo-fund, apollo-diversified-credit-securitize-fund,
vaneck-treasury-fund, blackrock, tron, usdd, htx-dao, bittorrent,
world-liberty-financial, sun-token, apenft, hive, steem, consensus-mechanism,
proof-of-stake, ark, gxchain) — zero forward links, 100% resolve. `git status`/`git diff
--stat` confirmed only the 5 target pages were touched. Re-ran lint: 987 → 982 (empty
47 → 42, exactly matching the 5 pages expanded from near-empty; links/tags/orphans/stale
unchanged at 234/659/39/8 — no regressions). 21 stub pages remain (16 non-source minus
the 5 done here, plus 10 gap-finder source stubs not in scope for this method).

## 2026-09-05 — Build: expanded 5 thin stub concept pages (lending, emissions, MiCA, synthetic dollar, crypto market regimes)

**Scope:** all 5 pages carried only a one-paragraph lead, a bare `## Related` list, and
minimal frontmatter (missing `domain`/`prerequisites`/`difficulty`), despite genuine
inbound demand (7-11 wikilinks each from existing pages). Selected by inbound-link count
among the wiki's 31 `status: stub` pages.

- **[[lending]]** (11 inbound refs) — DeFi money markets (Aave/Morpho/Compound
  utilization-curve interest rates, health-factor liquidations, flash loans) vs. CeFi
  lending desks, with the Terra/LUNA → 3AC → Voyager/Celsius/Genesis → FTX → BlockFi 2022
  contagion as the canonical CeFi-lending failure case study, plus how lending rates feed
  borrow-to-short, leveraged yield farming, and cash-and-carry. `Getting the Data` cites
  `/derivatives/funding-rates` and `/derivatives/summary` as the genuinely relevant
  surface — explicitly notes CryptoDataAPI does not carry on-chain DeFi protocol lending
  rates (Aave/Compound/Morpho APYs) rather than inventing an endpoint for them.
- **[[emissions]]** (11 inbound refs) — emission schedule types (Bitcoin-halving-style
  fixed/decaying, fixed/non-decaying, inflation-targeted, liquidity-mining), holder
  dilution mechanics, and an explicit "Emissions vs. Unlocks" section built directly on
  [[cryptodataapi-supply]]'s documented cliff-calendar-vs-emissions-feed distinction. No
  `Getting the Data` section — correctly identified that no genuine CryptoDataAPI
  endpoint covers continuous emissions (the supply/unlocks endpoint explicitly excludes
  them by design).
- **[[mica]]** — EU CASP licensing/passporting, the EMT/ART stablecoin reserve rules
  (pointing to the already-thorough [[stablecoin-regulation]] rather than duplicating its
  table), the phased 2024-2026 rollout, and MiCA's role as a Geopolitical/Policy Shock
  catalyst. `Getting the Data` cites `/policy/headlines`, `/policy/regime`,
  `/policy/regime/score` — framed honestly as the general policy-headline surface, not
  MiCA-specific.
- **[[synthetic-dollar]]** (8 inbound refs) — the delta-neutral basis-trade mechanism
  (long staked collateral + short equal-notional perp), funding-flip/venue-custody/
  synthetic-specific-depeg risks, and a 4-way comparison table against fiat-backed/
  crypto-overcollateralized/algorithmic stablecoin designs, kept consistent with
  [[ethena-usde]]'s existing supply-trajectory and depeg-history figures. `Getting the
  Data` cites `/sentiment/stablecoins` (+ `/remote-history`) and `/derivatives/
  funding-rates` as the two live inputs that determine hedge health.
- **[[crypto-market-regimes]]** (7 inbound refs) — rewritten as the accessible bridging
  page it was always meant to be rather than a duplicate of the much deeper
  [[crypto-market-regime-taxonomy]] and [[regime-strategy-playbook]] pages it links to:
  why regime-gating matters, the four beginner-level axes (risk-on/off, trending/ranging,
  vol, alt-season/BTC-dominance), and a high-level, non-duplicative pointer to the
  CryptoDataAPI regime engine.

All 5 pages moved `status: stub` → `good` with full `domain`/`prerequisites`/`difficulty`
frontmatter and approved tags. Verified every endpoint cited against a fresh live OpenAPI
pull (`/derivatives/funding-rates`, `/derivatives/summary`, `/policy/headlines`,
`/policy/regime`, `/policy/regime/score`, `/sentiment/stablecoins` + `/remote-history` —
all confirmed present) and every wikilink added across all 5 pages against the wiki
filesystem — zero forward links, all resolve to real pages. Re-ran lint: 991 → 987 issues
(empty-page count 51 → 47, consistent with genuine content added to previously
near-empty pages; links/tags/orphans/stale unchanged at 234/659/39/8 — no regressions).

## 2026-09-04 — Fix: finish the CryptoDataAPI broken-path sweep (borrow-interest, grayscale, hyperliquid mark-price/funding-rates, volatility/realized, blockchain/exchange-flows, archives-index, mvrv, stablecoin-flows, dex/tokens)

**Scope:** completes the sweep iter14 (2026-09-03) deferred. Rebuilt the broken-path list from
scratch — did not trust the old iter9/iter14 counts — by pulling a fresh `curl
https://cryptodataapi.com/api` OpenAPI spec, normalizing every real path, and grepping all of
`wiki/` for `/api/v1/...` citations, matching concrete param substitutions against the wildcard
form. Found 13 distinct broken strings after the previous fixes; 6 were false positives
(regex truncation on `<PLACEHOLDER>` curl examples for `dex/security/{chain}/{address}` and
`nfts/collections/{slug}`; deliberate `/api/v1/backtesting/*` and `/api/v1/dex/*` wildcard
prose; Santiment's `/api/v1/social_volume`, explicitly labeled non-CryptoDataAPI) — leaving
**11 real broken paths, ~47 citations** to fix.

- **`/market-intelligence/borrow-interest` and `/market-intelligence/grayscale/{holdings,premium}`**
  (12 citations, 6 files) — confirmed **retired with no replacement** (absent from the live
  spec; no changelog rename entry, no `borrow`/`grayscale`/`margin`-rate hits anywhere in the
  spec text). Per the deprecation rule: struck through on [[cryptodataapi-market-intelligence]]'s
  endpoint table with a dated warning callout, and struck through inline on every citing
  strategy page ([[crypto-signal-library]], [[box-spread]], [[staking-yield-arbitrage]],
  [[cash-and-carry]]) rather than deleted — each now points at perp funding as the
  leverage-cost proxy instead. Content preserved, not removed.
- **`/derivatives/hyperliquid/funding-rates` → `/hyperliquid/funding-rates`** (7 citations,
  2 files: [[funding-window-timing]], [[cross-venue-cascade-dislocation]]) — plain path swap.
- **`/derivatives/hyperliquid/mark-price` → `/hyperliquid/summary?coin=BTC`** (`mark_price`
  field) (4 citations, [[cross-venue-cascade-dislocation]]) — the invented path had no real
  analog; `/hyperliquid/summary` is the real endpoint carrying a genuine `mark_price` field.
- **`/volatility/realized?coin=BTC&days=30` → `/volatility/index`** (`majors[].realized_30`
  + pre-computed `vrp` = implied − realized) (5 citations, [[options-rv-event-calendar]],
  [[defi-yield-regime-gate]]) — better than the invented endpoint would have been: VRP is
  already computed server-side. Historical variant on defi-yield-regime-gate pointed at
  `/volatility/regime/BTC`'s 60d Pro-Plus `history[]` (`rv_cc_30`) instead. Also fixed the
  same file's `/volatility/correlation?assets=BTC,SPX` (no such endpoint exists) to state
  plainly it must be computed from klines — the wiki's own "(if available)" hedge was right
  to be suspicious.
- **`/blockchain/exchange-flows` → `/on-chain/exchange-flows/spike-alerts`** (multi-asset
  case) or `/on-chain/exchange-flows/{symbol}` (per-symbol case) (3 citations,
  [[news-trading]], [[structural-forced-selling]]) — also added the EVM-chain+Solana-only
  coverage caveat (no native BTC) to structural-forced-selling's per-symbol citation, the same
  class of coverage gap iter14 found on whale-score.
- **`/backtesting/archives-index` → `/backtesting/archives/index`** (2 citations,
  [[cryptodataapi-backtesting]], concepts/indicators/backtesting) — path had an extra
  flattening; real route nests `index` under `archives/`.
- **`/on-chain/mvrv` → `/on-chain/dormancy/btc`** (1 citation, [[alternative-data-alpha]];
  the [[log]] mention is historical) — flagged by iter14, fixed this pass. Verified fields:
  `metrics.mvrv` (raw ratio) + `mvrv_signal.zone` (categorical: capitulation → accumulation →
  neutral → elevated → euphoria). Noted the endpoint is **BTC-only**, not a general
  per-altcoin MVRV route as the old citation implied.
- **event-vol-buying "No CryptoDataAPI endpoint for event calendar" → `/event/calendar`**
  (flagged stale by iter14, fixed this pass) — the claim predated the endpoint's addition;
  corrected to cite it with its real filters (`type`, `symbol`, `bias`, `min_magnitude`,
  `window_days`) and fixed an adjacent `?days=30` param-name bug to `?window_days=30` in the
  same file.
- **`/sentiment/stablecoin-flows` → `/sentiment/stablecoins`** (1 citation,
  [[stablecoin-sentiment-depeg-entry]]) — real endpoint returns market cap + 14d/90d flow
  fields (`inflow_14d_billions`, `inflow_90d_billions`).
- **`/dex/tokens` → `/coins/{symbol}` (market cap) + `/dex/token/{chain}/{address}` (DEX
  liquidity, once a contract address is known)** (1 citation, [[narrative-position-vol-targeting]])
  — the invented plural route doesn't exist; the real singular route needs chain+address, not
  a bare symbol.
- **Verified:** re-grepped `wiki/` for every fixed path string — zero remaining *live*
  citations. All post-fix hits are either deliberate deprecation/correction annotations
  (struck-through table rows, "retired"/"corrected from the invented X" inline notes — exactly
  the ADD-never-destroy documentation this fix requires) or the 6 pre-existing false positives
  above, unchanged.
- **Not touched (bounded scope):** the `?days=30` vs `window_days` param-name mismatch on
  `/event/calendar` recurs across ~15 other pages; only the one page already being edited for
  the stale-claim fix got the param corrected. A dedicated params-only pass would be needed to
  clear the rest.
- **Files touched (17):** all bump `updated: 2026-09-04`. [[cryptodataapi-market-intelligence]],
  [[cryptodataapi-backtesting]], [[crypto-signal-library]], [[box-spread]],
  [[staking-yield-arbitrage]], [[cash-and-carry]], [[funding-window-timing]],
  [[cross-venue-cascade-dislocation]], [[options-rv-event-calendar]],
  [[defi-yield-regime-gate]], [[news-trading]], [[structural-forced-selling]],
  [[alternative-data-alpha]], [[event-vol-buying]], [[stablecoin-sentiment-depeg-entry]],
  [[narrative-position-vol-targeting]], concepts/indicators/backtesting.

## 2026-09-03 — Fix: 4 confirmed-broken CryptoDataAPI paths (fear-greed-index, whale-score, volatility/dvol, dvol-history)

**Scope:** iter9/iter10 flagged 24 distinct invented/renamed endpoint paths cited across the
wiki (166 citations); this iteration fixed the 4 highest-citation ones (~119 citations,
~45 pages), independently re-verified against a fresh pull of the live OpenAPI spec
(`curl https://cryptodataapi.com/api`) plus the current `/api/v1/changelog` feed (no
relevant entries — the rename predates the 10-release retention window, confirmed by hand
against the spec instead). The other ~20 broken paths
(`/derivatives/hyperliquid/funding-rates`, `/market-intelligence/borrow-interest`,
`/market-intelligence/grayscale/*`, and a long tail) are **explicitly deferred** to a
future Fix iteration — not touched.

- **`/sentiment/fear-greed-index` → `/sentiment/fear-greed`** (8 citations, 3 files: narrative-
  position-vol-targeting, post-panic-vol-selling, put-protected-dip-buying). Straight path
  swap — `FearGreedResponse{value, classification, sources, individual_values}` matches the
  wiki's existing field claims exactly, no drift.
- **`/on-chain/whale-score/{symbol}` (incl. concrete `/BTC` forms) →
  `/on-chain/whales/accumulation-score/{symbol}`** (39 citations, 27 files) — but
  verification surfaced three problems beyond the path rename that a blind swap would have
  hidden: (1) the **entire** `/on-chain/whales*` family, including the "renamed" endpoint,
  is currently "Coming soon" (temporarily disabled) per the live spec — not just the
  top-holder pair the wiki already knew about; (2) it is scoped to **ERC-20 tokens only
  (USDT/USDC/WBTC/WETH)** — it does not accept native BTC, which most citing pages assume;
  (3) the real response (`WhaleAccumulationScoreResponse`) is a categorical verdict —
  `signal: "accumulating"|"neutral"|"distributing"|"unknown"` plus `counts`,
  `tracked_tokens`, `symbol`, `deltas` (per-window `available`/`delta`/`pct_change`), and
  `reason` — **not** the continuous 0-100 score several strategy pages build numeric Gate
  thresholds on ("≥ 60", "≥ 65"). Fixed the path everywhere;
  rewrote the disabled-endpoint caveats on [[cryptodataapi-on-chain]] (table + warning box +
  historical-data section, now naming both accumulation-score routes and the confirmed
  signal enum), [[whale-copy-flow-funding-filter]], [[smart-money-vs-crowd-divergence]],
  [[alternative-data-alpha]], [[crypto-signal-library]], [[whale-onchain-flows]], and
  [[whale-alert]]. Did **not** rewrite the numeric Gate-threshold logic itself (unverified
  exactly how "≥ 60/100" maps onto the real 4-way signal) — flagged inline on both strategy
  pages as unresolved pending the endpoint's re-enable.
- **`/volatility/dvol` (17 citations) and `/market-intelligence/dvol-history` (55 citations,
  11 files) → `/volatility/implied`** — **deviates from the iter9 backlog note**, which
  proposed `/volatility/index` / `/volatility/index/history` for these. Schema-level
  verification showed why that would have been a second, quieter bug: `/volatility/index`'s
  `majors[]` and `/volatility/index/history`'s points carry only realized vol
  (`cvi_realized_30`/`cvi_realized_7`) — **no DVOL/implied-vol field at all** — while every
  citing page is explicitly about Deribit-implied vol (DVOL) for options/IV gates. The genuine
  match is `/volatility/implied`: `items[]` of `symbol`, `dvol`, `dvol_change_24h`,
  `realized_30`, `vrp`, `history[]`, `term_structure[]` (BTC-only Free, +ETH Pro/Pro Plus;
  `history`/`term_structure` Pro Plus only) — a real per-date DVOL series the index-history
  route cannot provide. Also dropped invented `?coin=BTC`/`?coin=ETH`/`&historical=true`
  query params (not real parameters on any of these routes — one call's `items[]` already
  covers both symbols) and merged the resulting duplicate BTC/ETH bullets. Documented the
  whole CVI/DVOL family (new to this wiki) as a subsection of [[cryptodataapi-regimes]]'s
  existing "Volatility Regime" section, since no dedicated `cryptodataapi-volatility` hub page
  exists yet (two pages had a pre-existing forward-link to that name; left as-is rather than
  building a new hub page, which is Build- not Fix-scope) — added `[[cryptodataapi-regimes]]`
  to the "Full endpoint catalog" line on the 10 of 14 pages that lacked it.
- **Noticed but out of scope, not touched:** [[alternative-data-alpha]] also cites
  `/api/v1/on-chain/mvrv`, which is not a real path either (the live route is
  `/on-chain/dormancy/btc`) — part of the deferred ~20; [[event-vol-buying]] states "No
  CryptoDataAPI endpoint for event calendar," which is stale (`/api/v1/event/calendar` exists
  and is documented on [[cryptodataapi-regimes]]) — a staleness bug, not a broken-path bug,
  left for a future pass.
- **Verified:** re-grepped `wiki/` for all 4 original broken strings post-fix — zero
  remaining citations (the only hits are the deliberate historical record in this log and two
  "path history" callouts on the hub pages explaining the old→new rename for context).
- **Files touched (45):** all bump `updated: 2026-09-03`. [[cryptodataapi-on-chain]],
  [[cryptodataapi-regimes]] (new CVI/DVOL section), [[crypto-signal-library]],
  [[whale-onchain-flows]], [[whale-alert]], [[alternative-data-alpha]],
  [[whale-copy-flow-funding-filter]], [[smart-money-vs-crowd-divergence]], plus 23 further
  whale-score spoke pages (concept/metrics pages, ML-model pages, on-chain strategy pages)
  and 3 fear-greed-index pages fixed as plain path swaps; and 14 DVOL-family strategy
  combination pages (event-calendar-risk-gating, complacency-vol-buying, cascade-
  monetization-rotation, trend-aligned-premium-selling, low-leverage-vol-selling, long-
  options-trend-expression, leverage-stress-tail-hedge, grid-with-tail-hedge, put-protected-
  dip-buying, post-panic-vol-selling, event-vol-buying, stablecoin-sentiment-depeg-entry,
  options-rv-event-calendar, defi-yield-regime-gate).

## 2026-09-03 — Sync: new /exchanges venue directory; Build: AsterDEX, Lighter, BNB Chain entity pages

**Scope:** Bounded iteration combining a small Sync batch (one new CryptoDataAPI release,
2026-08-23) with a Build batch (three high-inbound-link entity-page gaps). The new
`/api/v1/exchanges` and `/api/v1/exchanges/{slug}` endpoints were verified against the raw
OpenAPI JSON (`curl https://cryptodataapi.com/api`, parsed with Python) and live curl
responses — confirming `{slug}` is a path parameter, the current 7-slug set (hyperliquid,
binance, bybit, okx, robinhood, asterdex, lighter), and the exact `ExchangeInfo`/
`ExchangeSpecs` field shapes — before any page cited them.

- **Created** [[cryptodataapi-exchanges]] — new category page for the public (no API key)
  venue-directory endpoints: `slug`, `kind` (CEX/DEX/Broker), `specs`
  (instruments/coins/max_leverage/kyc/custody/fiat_onramp), and the referral
  `signup_url`/`signup_incentive`/`referral_code`/`is_referral_link`/`disclosure` fields,
  with the disclosure-surfacing rule spelled out. Registered on [[cryptodataapi]]'s category
  map and `related:`; cross-linked from [[exchanges-overview]]'s Start Here list.
- **Created** [[asterdex]] — entity page for the AsterDEX perp DEX (46 inbound links across
  16 files; the highest-priority gap). Covers the December 2024 APX Finance/Astherus merger,
  March 2025 "Aster" rebrand, YZi Labs/CZ backing, hidden-order and yield-collateral
  mechanics, and a fee-schedule table hedged against third-party-tracker disagreement.
  `founded` frontmatter uses the 2025 rebrand year; the page documents all three candidate
  "founding" dates (merger, rebrand, CryptoDataAPI's own "2024") rather than asserting one.
  [[aster-2]] (an existing redirect stub) now resolves correctly.
- **Created** [[lighter]] — entity page for the zk-rollup perp DEX (14 inbound links).
  Covers the 2022 company founding, January 2025 private beta, the Season 1/2 points
  program, the December 2025 LIT TGE (1B supply, ~25% to points holders), and the
  Circle-subsidized zero-fee retail model — flagged as an unverified permanent structure.
  Cross-checked against [[edgex]] and [[dydx-chain]]'s existing treatment of comparable
  zk/L2 perp-DEX peers so as not to contradict prior claims.
- **Created** [[bnb-chain]] — entity page for the BNB Chain protocol (10 inbound links,
  twice-queued in prior iterations), distinct from the [[bnb]] token page. Covers the
  September 2020 Binance Smart Chain launch, the February 15, 2022 rename to BNB Chain,
  PoSA consensus (~21-validator Cabinet), EVM compatibility, PancakeSwap/Venus as the
  dominant DeFi primitives, and the October 2022 bridge exploit — without duplicating
  [[bnb]]'s existing "BNB Chain Ecosystem" section; links back to it for token/tokenomics.
- **Marked seen** in `.claude/cryptodataapi-changelog-state.json`: release `2026-08-23`
  (disposition: material).

**Verification:** `python tools/lint.py --check links --json` only reports files with **>5**
broken wikilinks, so it undercounts the fix here (most of the 46+14+10 inbound references
to these three targets sit in files with just 1-2 broken links each, invisible to this
per-file threshold in either run). Within that reported set, the aggregate count still
dropped from 2,501 to 2,491 broken wikilinks (234 files both before and after — same file
set, lower counts per file), with `wiki/log.md` and `wiki/markets/crypto/lista.md` each
losing their `bnb-chain` entries specifically. A full occurrence count (not just the
>5-threshold report) would show a larger drop across the ~30 files that reference
[[asterdex]], [[lighter]], or [[bnb-chain]].

## 2026-09-02 — Absorbed 4 CryptoDataAPI releases: supply/float, unlocks, volume scanner, sr/ret_90d fields, error envelope (Sync)

**Scope:** Bounded ~60-minute Sync batch reconciling the 4 CryptoDataAPI releases left
unprocessed by prior iterations (2026-08-17, 2026-08-19, 2026-08-25, 2026-08-26 — flagged
as deferred in iter11's log entry and confirmed still outstanding by
`tools/check_api_changelog.py`). Every endpoint path, param, and response field below was
verified against the live OpenAPI schema (`curl https://cryptodataapi.com/api`, parsed with
Python) and, for the new error envelope, against live `401`/`403`/`429` responses pulled
with a freshly-minted free API key — not taken on the changelog's prose alone.

- **Created** [[cryptodataapi-supply]] — new category page for `/api/v1/supply/float`
  (circulating float, `dilution_overhang`, `next_unlock`, the `unlock_coverage:
  not_tracked` "not the same as no unlock" caveat) and `/api/v1/supply/unlocks` (dedicated
  cliff-calendar view — tokens/USD/`pct_of_float`, cliffs only, DefiLlama coverage bound).
  Registered on [[cryptodataapi]]'s category map and `related:`.
- **Updated** [[token-unlocks]] — `Getting the Data` section now lists `/supply/unlocks`
  and `/supply/float` alongside the existing `/event/calendar` reference, explaining
  `/supply/unlocks` is the new first-class view of the same unlock data
  `/event/calendar?type=unlock` already carried. Added [[cryptodataapi-supply]] to
  `Related` and frontmatter.
- **Updated** [[cryptodataapi-regimes]] — documented the new `mint` event type on
  `/event/calendar`/`/event/regime*` (`delta_usd`, `pct_of_supply`, `long`/`short` bias,
  observed-not-scheduled) in the Event Regime section, and added `ret_90d` to the Meme
  Regime section's metrics list (null under 91d history, not part of the lifecycle
  classifier).
- **Updated** [[cryptodataapi-indicators]] — documented the new `sr` (support/resistance)
  field on `/indicators/technical[/{symbol}]`: up to 3 levels/side, `{price, strength,
  dist_pct}`, swing-pivot clustering within 1.5%, empty `[]` as a real "no clean level"
  read. Added a trading-applications bullet linking the existing [[support-and-resistance]]
  concept page.
- **Updated** [[cryptodataapi-hyperliquid]] — added `/volume/scanner` and
  `/volume/scanner/{symbol}` to the endpoint table (`volume_24h`, `avg_volume_30d`/
  `median_volume_30d`, `multiplier`/`multiplier_median`, activity `band` enum, `kBONK`/
  `kPEPE`/`kSHIB` alias handling); documented `/hyperliquid/summary`'s 3 new additive
  fields (`avg_volume_30d`, `volume_multiplier`, `volume_band`); added a relative-volume
  screening trading-applications bullet.
- **Updated** [[cryptodataapi]] — Access section now documents the shared
  `{"detail":{"error","message",...}}` JSON envelope now returned on every `401`/`403`/
  `429` across `/api/*`, including `403`'s `required_tier`/`pricing_url` (confirmed live)
  and `429`'s `scope` field (confirmed live) plus CDA's documented `Retry-After`/
  `X-RateLimit-*` headers. Per explicit instruction, left the existing GEX-is-Pro-tier note
  on [[cryptodataapi-regimes]] untouched — this release only fixed an inconsistent error
  *message*, not access.
- **Live-verification note:** a rapid 15-request burst against a fresh free key reproduced
  the `403` envelope exactly (`required_tier`, `pricing_url`) but the `429` response from
  that burst carried only `error`/`message`/`scope`/`pricing_url` — no `Retry-After` header,
  no `X-RateLimit-*` headers, no `limit`/`window`/`tier`/`retry_after` body fields that
  CryptoDataAPI's own rate-limit blog post documents. Most likely explanation: a rapid
  same-second burst trips Cloudflare edge-level protection before the origin app's richer
  per-tier limiter runs. Wiki text notes the header/field set as CDA's documented behavior
  rather than asserting personal reproduction of every field, since the discrepancy could
  not be resolved within the batch's time budget.
- **Verified independently:** all live OpenAPI schema pulls (`SupplyFloatRow`,
  `SupplyUnlockItem`, `NextUnlock`, `EventCatalystModel`, `VolumeScannerItem`,
  `VolumeScannerDetailResponse`, `HLSummaryResponse`, `TechnicalRegimeItem`,
  `SupportResistanceModel`, `SRLevelModel`, `MemeMetricsModel`) matched every field named in
  the task brief exactly — no invented paths or fields. Marked material in the changelog
  state file: 2026-08-17, 2026-08-19, 2026-08-25, 2026-08-26.

## 2026-08-26 — Documented the News & Catalyst Detection endpoint family (daily loop iter 11, Sync)

**Scope:** Sync-track iteration. `tools/check_api_changelog.py` found 6 unprocessed
CryptoDataAPI releases (2026-08-17 through 2026-08-25) — more than one bounded batch
could responsibly cover. Picked the highest-leverage, self-contained cluster: the
2026-08-18 and 2026-08-21 releases, which together are entirely about one coherent
signal family (news-derived catalyst detection plus a closely-related forced-liquidation
tripwire) with zero prior wiki coverage, and left the other 4 releases genuinely
unprocessed rather than stretching the batch.

- **Created** [[cryptodataapi-news]] — new data-source category page covering
  `/news/pulse`, `/news/market-moving`, `/news/coin/{symbol}`, `/news/sources`, and
  `/backtesting/news-events`. Documents the filtered-tape nature (~15-40 of 300-500 daily
  stories qualify, no raw-feed endpoint at any tier), `match_mode`/`confidence` tiers
  (the Hyperliquid perp universe has many ordinary-English-word tickers), the
  `corroboration` cross-source signal, the 2026-08-21 nine-category policy-taxonomy
  expansion (added after a 2026-08-20 BTC move liquidating ~$3B of shorts on zero recorded
  catalyst events, root-caused to a missing legislation/executive-action/sovereign-buyer
  taxonomy), and the hard 2026-08-18 no-backfill start date.
- **Updated** [[cryptodataapi-market-intelligence]] — added `/market-intelligence/
  squeeze-alerts` to its endpoint table plus a caveat on the `direction` naming convention
  (named after the side being liquidated), shared venue-coverage gap, and
  `suppressed_by`/`include_quiet`.
- **Registered** the new category on [[cryptodataapi]]'s category map + `related:`, and
  added a reverse link from [[cryptodataapi-sentiment]].
- **Extended** [[news-trading]] with a `Getting the Data` + `AI agent workflow` update
  (it previously cited zero `/news/*` endpoints despite its name) and made a small, scoped
  addition to [[crypto-policy-shock-trading]] (a `/news/market-moving` corroboration
  signal, plus a caveat that a 2026-08-21 sign-error fix on `/policy/headlines` — which
  had scored constructive "banking"/"banks" headlines as maximum-severity bans — improved
  that page's existing signal's reliability).
- **Sub-agent self-correction:** the task brief named `event-driven-trading.md` as an
  edit target; the sub-agent found it was actually an out-of-scope equity redirect stub
  (removed 2026-07-19 per CLAUDE.md's scope rules), left it untouched, and substituted the
  real crypto strategy page ([[news-trading]]) instead of silently complying with a
  contradicted premise.
- **Verified independently:** all 9 added wikilinks resolve to real files; `tools/lint.py`
  re-run shows links/tags/orphans/stale/empty/frontmatter byte-identical to iter10
  (234/659/39/6/51/0) — zero regressions. Marked material in the changelog state file:
  2026-08-18, 2026-08-21. Left unprocessed (deferred, not "noted"): 2026-08-25
  (`ret_90d`/`sr` additive fields), 2026-08-23 (`/exchanges` venue directory), 2026-08-19
  (`/supply/float` + `/supply/unlocks`, pairs naturally with [[token-unlocks]] next),
  2026-08-17 (`/volume/scanner` family, needs its own category page).

## 2026-08-25 — Created 3 missing concept pages: DAO, Tokenization, Tokenomics (daily loop iter 10, Build)

**Scope:** Daily improvement loop, Build track. Balance check (last 3 Fix/Build-classified
entries: iter6 Build, iter7 Fix, iter8 Fix) required Build; iter9 (Sync, below) sits
outside the Fix/Build balance rule per its own design. iter8 had queued `[[depeg]]`,
`[[dao]]`, `[[tokenization]]`, `[[tokenomics]]` as genuine missing-page gaps — re-verified
all four before acting and found `[[depeg]]` was misclassified:
`wiki/concepts/risk-management/depeg-risk.md` already covers it comprehensively and even
lists "depeg" as a frontmatter alias, but `tools/lint.py` doesn't resolve frontmatter
aliases when checking wikilinks, so it still reads as broken. Left `depeg.md` uncreated to
avoid duplicating `depeg-risk.md`; queued the real fix (rewrite the 43 pages' `[[depeg]]`
links to `[[depeg-risk|depeg]]`) as a Fix-track item for a future iteration instead. The
other three were confirmed genuine: no page exists under any filename or alias for any of
them, and each was already anticipated by an existing page — `[[governance-token]]` lists
`[[dao]]` as a frontmatter prerequisite, `[[real-world-assets]]` links `[[tokenization]]`,
`[[emissions]]` links `[[tokenomics]]`.

- **Pages created (all `type: concept`, `status: draft`):** [[dao]] (1,741 words —
  proposal lifecycle, voting mechanisms incl. token-weighted/delegation/vote-escrow/
  quadratic/dTAO's market-based alternative, treasury custody models, legal wrappers
  incl. Wyoming DAO LLC 2021 and CFTC v. Ooki DAO 2022-2023, notable examples incl. The
  DAO 2016 hack and the ETH/ETC fork it caused, failure modes incl. the 2022 Beanstalk
  flash-loan governance attack), [[tokenization]] (1,269 words — the general
  mint/custody/redemption mechanism one level above [[real-world-assets]]'s TradFi-
  specific treatment, custody-model spectrum from fully on-chain to wrapped to off-chain
  SPV), [[tokenomics]] (1,434 words — supply design, distribution/vesting, value-accrual
  mechanisms, sinks-vs-faucets incentive design incl. the 2020 DeFi Summer liquidity-
  mining/mercenary-capital case study, failure modes incl. hyperinflationary emissions and
  unlock overhangs).
- **Differentiation deliberately preserved:** [[dao]] covers the organizational/governance
  structure and defers to the pre-existing [[governance-token]] for the token instrument
  itself; [[tokenization]] covers the general mechanism and defers to [[real-world-assets]]
  for TradFi-specific depth; [[tokenomics]] is the umbrella concept and defers to the
  pre-existing [[emissions]]/[[token-unlock-supply-event]]/[[staking]] stubs for their
  specific sub-topics rather than re-explaining them.
- **No `Getting the Data (CryptoDataAPI)` section** on any of the three — all are
  structural/conceptual topics with no direct market-data endpoint, matching the
  2026-08-20 precedent of omitting rather than forcing a weak fit.
- **Verified independently:** every wikilink target across all three pages (30 distinct
  targets) checked against the real file tree — zero broken links introduced. Fresh
  `tools/lint.py` run: links 240→234 (partial resolution — `check_wikilinks` only flags
  pages with >5 broken links total, so some of the ~35 references now resolve without the
  source page dropping below threshold), tags/orphans/stale/empty/frontmatter unchanged
  (659/39/6/51/0) — confirms only additive, schema-clean changes. `[[bnb-chain]]` remains
  queued from iter8 as a further genuine Build gap (10 inbound refs, the BNB Layer-1 chain
  distinct from the token page).
## 2026-08-25 — New category page: News & Catalysts (daily loop iter 10, Sync)

**Scope:** Second Sync-track iteration, working the backlog deferred from iter 9 (no new
upstream releases since). Absorbed the two interdependent releases that introduce the
`/news/*` endpoint family and the policy-catalyst taxonomy layered on top of it.

- Pages created:
  - [[cryptodataapi-news]] — the 17th CryptoDataAPI category page, covering
    `/news/pulse` (per-coin `news_pressure` / `news_tilt` features, cross-sectionally
    ranked and joinable onto price), `/news/market-moving` (the filtered catalyst tape),
    `/news/coin/{symbol}`, `/news/sources` (feed health and funnel counts), and
    `/backtesting/news-events` (the archived tape with measured `ret_15m` / `ret_1h` /
    `ret_4h` response labels). Documents the nine policy `category` values added
    2026-08-21 — `legislation`, `executive_signal`, `rulemaking`, `restrictive_policy`,
    `sovereign_bid`, `strategic_reserve`, `pro_crypto_eo`, `macro_liquidity`,
    `macro_tightening` — all of which resolve to `symbol: "MARKET"`. States plainly that
    the archive holds qualified events only and that its history begins 2026-08-18 and
    cannot be backfilled.
- Pages updated:
  - [[cryptodataapi]] — category map row, `related:`, and the endpoint count raised from
    "190+" to "200+" (the spec now lists 204).
  - [[cryptodataapi-market-intelligence]] — added `/market-intelligence/squeeze-alerts`,
    the forced-liquidation cascade tripwire, including the reading that matters most:
    `direction` names the side being *liquidated*, so `short_squeeze` is upward pressure,
    and `oi_state` separates a move consuming its own fuel from fresh positioning.
  - [[cryptodataapi-backtesting]] — added `/backtesting/news-events` with its no-backfill
    constraint.
  - [[cryptodataapi-regimes]] — recorded the `/policy/headlines` sign-error fix: the `ban`
    rule was unbounded on the right, so any headline containing "banking", "banks" or
    "banner" scored as a maximum-severity regulatory ban, skewing `headline_tilt` and
    `regulatory_pressure` negative. whitehouse.gov joined the policy feed set.
  - [[cryptodataapi-sentiment]], [[news-and-sentiment-sources]] — cross-registered.
- Every endpoint path was verified against the live OpenAPI spec before writing, and a
  wiki-wide sweep confirmed this batch introduced no unresolvable endpoint references.

## 2026-08-24 — API changelog sync: tier limits, ETF/liquidation endpoints, gex breaking change (daily loop iter 9, Sync)

**Scope:** First Sync-track iteration. Reconciled the wiki against the data layer's
release feed, which had never been checked before today. Of the 10 retained releases,
processed the 5 that change facts the wiki already documented; deferred the 5 that
introduce entirely new endpoint families needing their own category pages.

- Pages updated:
  - [[cryptodataapi]] — every row of the plans/rate-limits table was wrong. Free is
    1,000/day + 10/min (was 50/day + 5/min); Pro Plus is 50,000/day + 120/min (the page
    claimed "Unlimited" + 60/min). Added the email-verification mechanic (an unverified
    free key sits on a smaller starter allowance; confirming unlocks the full free tier
    plus a 24-hour Pro trial), `POST /api/v1/auth/resend-verify`, and the effective-limits
    fields on `GET /api/v1/auth/keys/me`.
  - [[cryptodataapi-market-intelligence]] — `/etf/{asset}/flows` supports BTC/ETH/SOL only
    (XRP now returns 400, not 503; SOL was restored 2026-08-22). `/etf/btc/aum` reframed
    from "total AUM" to the reconstructed estimate it is, with its real field names
    (`aum_usd_from_flows`, `btc_held_from_flows`) and the GBTC-seed understatement.
    Added the OKX/Bybit/Hyperliquid venue-coverage caveat to `/liquidations/by-exchange`.
  - [[cryptodataapi-regimes]] — `/quant/gex` is Pro tier, not Pro Plus. Documented the
    2026-06-27 breaking change (a single-symbol query now returns the bulk envelope
    narrowed to one coin, not a bare per-coin object) plus `regime.confidence`, the
    capped/nullable `gamma_flip`, and per-coin `distribution_context`.
  - [[cryptodataapi-backtesting]] — corrected a pre-existing error: `/backtesting/snapshots`
    is the data endpoint (requires `data_type` and `start`), and `/backtesting/snapshots/types`
    is the discovery route. The page had the two backwards and listed a `/snapshots/{type}`
    path that does not exist in the API.
  - [[spot-etf-flows]], [[gamma-explosion]], [[gamma-exposure-trading]],
    [[feature-engineering-crypto]] — corrected the same endpoint and tier claims.
- Every path written was verified against the live OpenAPI spec (204 paths) before the
  edit, per CLAUDE.md's never-invent-an-endpoint rule.
- **Known gap, queued:** a wiki-wide sweep against the spec found 24 distinct endpoint
  paths cited that do not exist, across 166 citations — most notably
  `/market-intelligence/dvol-history` (55 citations) and `/on-chain/whale-score/{symbol}`
  (39 citations, since renamed to `/on-chain/whales/accumulation-score/{symbol}`). These
  predate this iteration and are scheduled for a dedicated Fix batch.

## 2026-08-24 — Tooling: CryptoDataAPI changelog reconciliation added to the improvement loop

**Scope:** Loop/tooling change, not a content batch. The daily improvement loop now
reconciles the upstream API release feed before choosing a track, so endpoint
documentation across the wiki can no longer drift silently.

- Added `tools/check_api_changelog.py` — watches the public, key-free
  `GET /api/v1/changelog` feed and reports releases the wiki has not absorbed, with state
  in `.claude/cryptodataapi-changelog-state.json`.
- Pages updated: [[cryptodataapi]] — the Docs line now names the machine-readable
  changelog endpoint and its 10-release retention limit.
- No content pages were re-synced in this operation. The first Sync-track iteration of the
  loop will triage the 10 currently-unprocessed releases (2026-06-27 through 2026-08-23,
  two of them breaking); known drift already visible includes the Pro Plus per-minute rate
  limit and the free-tier limits on [[cryptodataapi]].

## 2026-08-22 — Wikilink rename-mismatch batch (daily loop iter 8, Fix)

**Scope:** Daily improvement loop, Fix track. Wrote a standalone tally script (reusing
`tools/lint.py`'s own wikilink-extraction logic) to find broken-link targets referenced
from many pages at once — `lint.py`'s own report only shows pages with >5 broken links
and truncates each list to 5 targets, hiding cross-wiki patterns. Found 1,226 distinct
broken targets; sampled usage context on the top ones to separate real rename-mismatches
from genuine missing-concept gaps.

- **Fixed 5 rename-mismatches, 60 files, 150 link-target changes:**
  [[memecoins]]→[[meme-coins]] (8 files), [[btc-bitcoin]]→[[bitcoin]] (10 files, `|BTC`
  alias preserved), [[nvidia]]→[[nvidia-ai]] (16 files, `|Nvidia` alias added where
  missing), [[rwa]]→[[real-world-assets]] (9 files — all were redundant duplicates
  alongside an existing real-world-assets link, so deleted rather than renamed),
  [[tether]]→[[usdt]] or [[tether-limited]] by context (17 files, 72 refs — split roughly
  50 token/market-context refs to `usdt` and 22 issuer/company/regulatory-context refs to
  `tether-limited`, read individually rather than blind-replaced).
- **Ruled out** [[bnb-chain]] (10 pages) as a rename-mismatch after checking usage — it
  genuinely means the BNB Layer-1 chain itself, distinct from [[bnb]] the token/market
  page (which even links to `[[bnb-chain]]` separately). A real missing-page gap, not a
  typo.
- **Queued for Build (iter9+):** [[depeg]] (43 pages/135 refs — very high leverage; `depeg`
  was adopted as an approved tag in iter7 but has no page at all), [[dao]] (9 pages),
  [[tokenization]] (15 pages), [[tokenomics]] (10 pages), [[bnb-chain]] (10 pages).
- **Verified independently:** re-ran `tools/lint.py` before and after — `[links]` 247→240;
  `[tags]`/`[orphans]`/`[stale]`/`[empty]` byte-identical (659/39/6/51). Spot-read the
  rwa-dedup and tether-split diffs directly.

## 2026-08-21 — Tag audit batch 3 (daily loop iter 7, Fix)

**Scope:** Daily improvement loop, Fix track. Fresh lint run showed 852 pages carrying
non-approved tags (flat since iter 3) — by far the largest lint category, versus 247
broken links, 51 empty pages, 39 orphans, 6 stale. Continued the tag audit begun in batch 2 (2026-08-15).

- **Adopted 42 new tags** into CLAUDE.md/AGENTS.md's Approved Tags list and
  `tools/lint.py` (additive, "Adopted 2026-08-21 (tag audit batch 3)"): DeFi/crypto
  infrastructure vocabulary the approved list had never picked up (staking, lending,
  restaking, yield-farming, smart-contracts, mev, oracle, amm, cross-chain, layer-2,
  governance, launchpad, depeg), AI/ML sub-domains (ai, nlp, llm), options vocabulary
  (premium-selling, defined-risk, income, greeks, gamma), quant/strategy-methodology
  terms (factor-investing, alpha-edge, informational-edge, performance, diversification,
  portfolio-construction, contrarian, price-action, grid-trading, calendar-effects),
  macro/commodities (fixed-income, monetary-policy, vix, crisis, industrial-metals,
  agricultural, payments), and standalone themes (institutional, digital-art,
  short-selling, open-source).
- **Consolidated 7 near-duplicate tags** across 50 pages: artificial-intelligence→ai,
  regime→market-regime, api-trading→api, on-chain-analytics→on-chain,
  comparison→comparisons, liquidation→liquidations, course→courses. Zero duplicate-tag
  lines introduced (verified).
- **Skipped:** research, banking, economics — too generic or ambiguous to classify
  mechanically; left for a future batch with more editorial judgment.
- **Verified independently:** re-ran `tools/lint.py` before and after (not just the
  sub-agent's report) — `[tags]` 852→659; `[links]`/`[orphans]`/`[stale]`/`[empty]`
  byte-identical (247/39/6/51), confirming zero content regressions. Spot-read 2
  consolidated pages and 1 adopt-only page for correct, isolated `tags:` line edits.
- **Note:** the local wiki MCP server showed "Connected" via `claude mcp list` but its
  tools were unreachable from this session (same gap as iter 6, survived a re-registration
  attempt). Worked via `tools/lint.py` run directly with the repo's venv Python instead of
  `wiki_lint` — a fully adequate substitute, now the preferred fallback.

797 distinct non-approved tags remain (mostly long-tail 1-3-occurrence ones) for future
batches.

## 2026-08-20 — Expanded 6 more concept stubs (daily loop iter 6, Build)

**Scope:** Daily improvement loop, Build track (second Build iteration, continuing from
2026-08-19). Of the 37 `status: stub` pages remaining after iter 5, 21 were genuine
concept-page candidates. Ranked all 21 by inbound wikilink count and picked the 6
highest, verifying each was still a genuine ~200-430 char placeholder before committing.

- **Pages updated (all `type: concept`, stub → draft):** [[altcoins]] (33 inbound links,
  916 words — asset-class definition, BTC-dominance rotation mechanics, alt-season
  breadth), [[gaming-tokens]] (33 inbound links, 1,045 words — token-taxonomy angle
  deliberately distinct from the already-substantive [[gamefi]]/[[play-to-earn]] pages:
  governance vs. reward vs. chain-native vs. interop tokens), [[data-availability]]
  (30 inbound links, 1,022 words — DAS/erasure coding, EIP-4844 blobs, Celestia, EigenDA,
  validiums), [[modular-blockchains]] (28 inbound links, 977 words — the 4-function
  execution/settlement/consensus/DA split vs. Solana's monolithic design), [[sequencer]]
  (28 inbound links, 996 words — centralization risk, MEV chokepoint, based/shared
  sequencing decentralization paths), [[consensus-mechanism]] (28 inbound links, 1,095
  words — PoW/PoS/DPoS/BFT/PoA taxonomy, the Merge as reference case).
- **Getting the Data (CryptoDataAPI) added** to [[altcoins]] (`/market-health/altcoin-breadth`,
  `/coins/top`) and [[gaming-tokens]] (`/coins/category-groups`) — the other 4 are
  infrastructure/mechanism concepts with no direct data-mapped endpoint, matching the
  2026-08-19 precedent of omitting the section rather than forcing a weak fit.
- **Rejected after inspection:** [[crypto-market-regimes]] (28 inbound links, would have
  ranked in the top 6) — dropped because the topic is already exhaustively covered by the
  existing `status: good` [[crypto-market-regime-taxonomy]] page (which even carries
  "Crypto Market Regimes" as an alias) plus a 14-page `market-regimes/` subdirectory;
  fully expanding the stub would have duplicated that content rather than adding to it.
  [[consensus-mechanism]] was promoted from the tier below to fill the 6th slot.
- **Verified:** every wikilink added across all 6 pages resolves to a real existing page
  (checked via Glob/Grep before adding, not just assumed); one near-miss caught and fixed
  — `[[memecoins]]` does not exist as a file (only `[[meme-coins]]`/`[[meme-coin]]`
  redirect stubs do, themselves pointing at the same missing target — a pre-existing
  wiki-wide gap left untouched); only CLAUDE.md-approved tags used.

## 2026-08-19 — Expanded 7 L2/infrastructure stubs, left over from the 2026-07-19 A3 batch

**Scope:** Daily improvement loop, Build track (first Build iteration after 4 straight Fix
iterations rebalanced the loop). The 2026-07-19 A3 batch created a wave of concept stubs
to resolve broken links and explicitly deferred expanding them ("stay as intentional
stubs — expand opportunistically"). Nobody had. Picked the 7 highest-inbound-demand
survivors of that batch and brought them to full concept pages at the quality bar of the
existing [[depin]]/[[liquidations]]/[[governance-token]] pages (mechanism, concrete
named examples with real dates/figures, AlgoBrain trading-relevance links, honest
unsourced-knowledge disclosure — `status: draft`, not `good`, matching that precedent).

- **Pages updated (all `type: concept`, stub → draft):** [[cross-chain]] (863 words — the
  general taxonomy of why/how assets move between chains), [[centralized-exchange]] (874
  words — CEX business model and custody risk, FTX/Mt. Gox as case studies),
  [[zk-rollup]] (943 words — sequencer→prover→verifier architecture, zkEVM Type 1-4),
  [[exchange-tokens]] (917 words — explicitly differentiated from [[governance-token]];
  BNB/OKB/KCS/BGB, FTT as the cautionary tale), [[cross-chain-bridge]] (1,154 words —
  lock-mint/burn-mint/liquidity-network mechanisms plus Ronin $625M, Wormhole $325M,
  Nomad $190M, Multichain $130M+, cross-referenced against the deeper existing
  [[cross-chain-bridges]] comparison page rather than duplicating it), [[interoperability]]
  (911 words — IBC/LayerZero/Wormhole messaging-standard philosophy, explicit
  "related but distinct" note vs. the other two), [[optimistic-rollup]] (930 words —
  fraud-proof/challenge-window mechanics, mirrored against [[zk-rollup]]).
- **Verified:** every wikilink added across all 7 pages resolves to a real existing page
  (spot-checked ~20, zero fabricated targets); only CLAUDE.md-approved tags used; full
  lint pass after the change shows zero regressions (tags 852, links 247, orphans 39,
  stale 6 all unchanged; empty pages 58→55 as three former near-empty stubs crossed the
  content threshold).
- **Not done:** no "Getting the Data (CryptoDataAPI)" sections — these are
  infrastructure/mechanism concepts, not data-mapped instruments, and no genuinely
  applicable documented endpoint exists for them.

## 2026-07-20 — Stretch Revert cluster: inbound links, findings feedback, lifecycle records

**Scope:** The 33-page cluster was a self-referential island — 35 pages linked to [[stretch-revert]] but only **one** ([[moving-averages]]) pre-dated the build-out. Everything else was written the same day. Fixed that, fed the estimator findings back up to the family page, and filed the missing lifecycle records.

- **Inbound links added** from pre-existing hubs: [[mean-reversion]] (z-score bullet rewritten to link [[z-score]]/[[median-absolute-deviation]], plus Related), [[bollinger-band-reversion]] (Related), [[quantitative-overview]] (Mean Reversion & StatArb list). These pages now surface the family in their backlink panes and in `wiki_search` reversion queries.
- **[[stretch-revert]] updated** — the page was written *before* its 32 supporting pages existed and did not reflect what they found. Added a "Findings from the estimator build-out" subsection under What kills this strategy (6 structural defects + the missing-robust-quadratic gap + the folklore-parameters note), plus corrections to Entry (z-thresholds are ranking devices, not probabilities), Stops (full reversion is a 3-4 half-life trade, so a one-half-life stop scratches winners), and Disadvantages.
- **[[regime-matrix]]** — row added. Rated stricter than [[mean-reversion]] on High Vol and Risk-Off (❌ vs ➖): the family runs 3-5x leverage, so an unreverting move is a liquidation rather than a stop-out.
- **[[live-journal]]** — added to the Currently ON table and a full backfill entry. Recorded explicitly that **this family was deployed before it was journaled**; the entry backfills the record and is not a deploy event. Deploy dates and sizing policy per member are unknown and noted as such.
- **Pages created:** [[2026-07-20-hyperliquid-trader-stretch-revert-dashboard]] (`type: source`, `confidence: medium`) — the dashboard snapshot now has a source page, so the live figures cite something. 9 claims extracted with confidence markers; win rate independently recomputed from the per-member rows (77.5%, consistent with the reported 77%). Carries a "What the snapshot does NOT establish" section, because the headline figures invite the opposite reading. [[stretch-revert]] Sources section now uses a real `(Source: [[...]])` reference.

**Also:** `.obsidian/graph.default.json` + `tools/restore_obsidian_config.ps1` added — Obsidian rewrites `graph.json` from memory and was silently reverting the entities palette to teal. Script restores `colorGroups` only, leaving view state intact; `-Check` mode reports drift; warns if Obsidian is running (it was, PID 3208). Wired to a `SessionStart` hook in `.claude/settings.json`. Script is ASCII-only by necessity — Windows PowerShell 5.1 reads UTF-8-without-BOM as ANSI, which corrupted em-dashes and broke parsing on the first attempt.

## 2026-07-20 — Created: 19 supporting pages (Stretch Revert cluster completion)

**Scope:** Closed the load-bearing gaps and wrote the people behind the estimators. 19 pages, ~3,900 lines, four parallel agents. Selected from the Obsidian graph's unresolved nodes; the five nodes named for the user's own proprietary strategy groups were **deliberately not written** (see below).

**Concepts — load-bearing (5):** [[z-score]], [[adaptive-moving-averages]], [[half-life-of-mean-reversion]], [[time-stop]], [[weighted-moving-average]]
**Concepts — supporting (5):** [[fractal-dimension]], [[linear-regression]], [[median-absolute-deviation]], [[chande-momentum-oscillator]], [[macd-v]]
**Entities — indicator authors (6, `wiki/entities/traders/`):** [[john-ehlers]], [[perry-kaufman]], [[alan-hull]], [[patrick-mulloy]], [[arnaud-legoux]] (stub), [[mark-jurik]] (stub)
**Entities — mathematicians (3):** [[rudolf-kalman]], [[henri-theil]], [[pranab-sen]]

- Pages updated: [[triple-exponential-moving-average]] — Mulloy citation corrected, see contradiction below.
- **Verified:** all 19 — no non-whitelisted CryptoDataAPI endpoints; no `.md`/folder paths in wikilinks; the single `(Source: [[...]])` reference used ([[2026-04-20-comprehensive-guide-technical-trading-indicators]]) exists. `statistics` tag restored to the three mathematician pages (agent had misread the approved list, missing the 2026-07-19 audit adoptions on CLAUDE.md line 303).

**Substantive findings:**

- **[[z-score]] — the family's core quantity is self-masking.** An outlier inflates the σ it is measured against: a 10-unit outlier reads z ≈ 7.0, not 10. Measured stretch is understated, and the understatement grows with the size of the dislocation — worst precisely in the liquidation flushes [[stretch-revert]] exists to fade.
- **[[median-absolute-deviation]] — the other half of the robustness problem.** [[theil-sen-regression]] gives a robust *location* (numerator); nothing in the family gives a robust *scale* (denominator). Recorded as a design observation, explicitly **not** a claim that swapping MAD in would have improved live results.
- **[[half-life-of-mean-reversion]] — time-stop sizing correction.** Full reversion is a 3–4 half-life trade, so a stop set at one half-life scratches most winners. Estimate is badly identified on short samples: λ = −0.010/−0.005/−0.001 → 69/139/**693** bars.
- **[[john-ehlers]] — estimator clustering.** Ehlers is behind four of the fourteen baselines (FRAMA, Laguerre, SuperSmoother, ZLEMA w/ Ric Way). A shared weakness in the DSP framing is not diversified away by running four of his filters in parallel — this weakens the family's defence-in-depth argument.
- **[[perry-kaufman]]** — KAMA's Efficiency Ratio and the [[hurst-exponent]] regime gate are not independent tests of the same thing.
- **[[macd-v]]** — verified: `[(EMA12 − EMA26)/ATR(26)] × 100`, Alex Spiroglou, **both** the Charles H. Dow Award and the NAAIM Founders Award in 2022; developed 2015. Zone-boundary conventions differ between renderings and are flagged unresolved. Page states it documents the published indicator, **not** the user's undocumented "MACD-V Group".

**Contradiction handled — [[triple-exponential-moving-average]] TEMA attribution.**
> **Claim A** (encyclopedic sources, confidence: MEDIUM): TEMA and DEMA both introduced in "Smoothing Data With Faster Moving Averages", *TASC* V.12:1, Jan 1994, pp. 11–19.
> **Claim B** (publisher listings + secondary sources, confidence: MEDIUM): a second article, "Smoothing Data With Less Lag", *TASC* V.12:2, Feb 1994, pp. 72–80, also covers TEMA/DEMA; some sources credit it with TEMA specifically.
> **Resolution**: Unresolved. Both articles exist and are now cited on the page; neither has been read. The page previously asserted January flatly — corrected to state the ambiguity.

**Biography — what could not be verified (omitted or hedged on-page, not asserted):** Ehlers' Raytheon employment, "private trader since 1976" and the 1978 MESA anecdote (mesasoftware.com and cmtassociation.org both return 403; no PhD claimed — sources say "doctoral work"); Kaufman's 1995 *Smarter Trading* year for KAMA, and "founder" vs "co-founder" of the *Journal of Futures Markets*; all of Hull's biography (self-description only); **all** of Mulloy's biography (no record exists); all of Legoux's (no primary source at all — co-creator's name appears three different ways across sources); Jurik's dates and background (jurikres.com serves an invalid TLS cert, nothing fetched live). [[rudolf-kalman]]: emigration date, PhD-vs-DSc. [[henri-theil]]: Florida appointment year, 1950 journal identity. [[pranab-sen]]: a Padma Shri and honorary DSc appeared in a single uncorroborated fetch and were **omitted**.

- **Apollo claim corrected on [[rudolf-kalman]]**: Kálmán did not work on Apollo. Stanley F. Schmidt at NASA Ames, after a visit from Kálmán, developed the extended/Schmidt–Kalman adaptation, and a version of that went into the Apollo onboard navigation computer.
- **No pages for Ric Way or Dimitrios Kouzis-Loukas** — public record too thin; both named in prose on [[john-ehlers]] and [[arnaud-legoux]].
- **Not written, deliberately:** [[bar-break-group]], [[ride-group]], [[clock-group]], [[burst-and-pulse-group]], [[whale-traders-lab]] — these name the user's own proprietary strategy families. Nothing is known about them beyond the names in a dashboard "See also" list; writing them would be invention. They need dashboard content supplied, as [[stretch-revert]] was.
- Pronouns: all nine entity pages use they/them, no source read stated pronouns.

## 2026-07-20 — Created: 13 baseline-estimator indicator pages (Stretch Revert build-out)

**Scope:** Closed the estimator gap opened by [[stretch-revert]]. Of its 14 baselines only [[kalman-filter-trading]] had a page; the other 13 are now written (2,616 lines total) in `wiki/concepts/indicators/`. Written by four parallel agents grouped so siblings cohere, each given the verified endpoint whitelist rather than left to derive paths.

- **Weighted / lag-cancelling:** [[alma]], [[hull-moving-average]], [[triple-exponential-moving-average]], [[zero-lag-exponential-moving-average]]
- **Adaptive:** [[frama]], [[vidya]], [[kama]]
- **Signal-processing filters:** [[laguerre-filter]], [[supersmoother-filter]], [[jurik-moving-average]]
- **Regression:** [[least-squares-moving-average]], [[theil-sen-regression]], [[quadratic-regression]]
- Pages updated: [[moving-averages]] — the 9-line "Adaptive and Advanced MAs" section (HMA/DEMA/TEMA/KAMA only) rebuilt as a four-group taxonomy linking all 13, preserving the original prose; [[log]], [[index]] pending prior entry.
- All `type: concept`, `status: draft`, each with `## Use as a mean-reversion baseline` tying it to [[stretch-revert]], plus `## Getting the Data (CryptoDataAPI)` + `### AI agent workflow`.
- **Verified:** 13/13 on required sections; every endpoint on the verified whitelist (no inventions); no `.md`/folder paths in wikilinks; no fabricated `(Source: [[...]])` refs — primary literature cited by author/year only (Mulloy 1994; Hull 2005; Legoux & Kouzis-Loukas 2009; Ehlers 2004/2005/2013; Chande 1992; Kaufman 1995; Theil 1950; Sen 1968; Runge 1901).

**Substantive findings recorded on the pages (not just documentation):**

- **[[zero-lag-exponential-moving-average|ZLEMA]] has a structural bias against the family.** Its de-lag correction assumes linear trend, so under acceleration it errs *in the trend direction* — the residual points toward fading a strengthening move. Acceleration is the signature of a liquidation cascade, i.e. the family's home condition. `zlema_stretch_revert` is on the prod bot.
- **Adaptive baselines suppress the signal they measure.** [[frama]]/[[vidya]]/[[kama]] speed up during fast moves, shrinking measured stretch exactly when it matters — and the z-score's rolling σ shrinks with it. Severity graded FRAMA (moderate) < stdev-VIDYA (acute) < KAMA (worst: a flush is by definition a maximum-efficiency-ratio event).
- **[[jurik-moving-average|JMA]] is unauditable.** Proprietary, never disclosed; circulating community ports disagree with each other. Page carries no formula and a `## Reproducibility problem` section: the [[deflated-sharpe-ratio]] for that member cannot be computed correctly because the vendor's own search count is unknowable.
- **[[theil-sen-regression|Theil-Sen]]:** robustness fixes *measurement* failure, not *position* failure — relevant to that member's 80% WR on negative P/L.
- **Gap surfaced:** no robust *quadratic* estimator exists in the family. [[quadratic-regression]] is *more* leverage-sensitive than [[least-squares-moving-average|LSMA]] (edge-of-window outliers distort curvature disproportionately) and nothing covers it.
- **Default parameters are folklore.** ALMA 0.85/6, HMA 9/16/55, TEMA/ZLEMA periods — no derivation found for any; each page labels them convention, not derived optima. ALMA, HMA and ZLEMA have no peer-reviewed publication at all.

**Still open:** new forward links created and unresolved — [[adaptive-moving-averages]], [[john-ehlers]], [[perry-kaufman]], [[z-score]], [[time-stop]], [[half-life-of-mean-reversion]], [[fractal-dimension]], [[chande-momentum-oscillator]], [[linear-regression]], [[median-absolute-deviation]], [[outliers]], [[bias-variance-tradeoff]], [[curve-fitting]]. No source-summary page for the dashboard snapshot; no [[live-journal]] entry; no [[regime-matrix]] row.

## 2026-07-20 — Created: Stretch Revert strategy family

**Scope:** New family page for the Stretch Revert group (14 baseline estimators, one mean-reversion thesis) running on the Hyperliquid prod bot. The vault had no coverage — "stretch" appeared ~20 times but always meaning *stretched funding rates*, never price-deviation-from-baseline.

- Pages created: [[stretch-revert]] (`type: strategy`, `status: draft`, `backtest_status: live`) in `wiki/strategies/quantitative/`. Full 16-section strategy schema per CLAUDE.md, incl. edge source, null hypothesis, pseudocode, capacity, kill criteria, and a `## Getting the Data (CryptoDataAPI)` + `### AI agent workflow` block using only verified endpoints (hyperliquid candles/l2-book, derivatives funding/OI, backtesting klines, quant regimes history).
- Pages updated: [[index]] (Strategies section).
- Live figures recorded from a Hyperliquid Trader dashboard snapshot (2026-07-20 11:23:51 AEST): 53 fills, +$50.08, 77% trade-weighted WR. Recorded **with explicit caveats** rather than as evidence of edge — 10 of 14 members have zero trades, `frama` is 94% of family P/L, and `theilsen` shows 80% WR on negative P/L (payoff asymmetry). Page argues the 14-variant design is a multiple-comparisons problem requiring [[deflated-sharpe-ratio]] deflation before promotion.
- **Known gap — 13 new red links, deliberate.** Only [[kalman-filter-trading]] of the 14 estimators has a page. [[alma]], [[frama]], [[vidya]], [[kama]], [[hull-moving-average]], [[triple-exponential-moving-average]], [[zero-lag-exponential-moving-average]], [[jurik-moving-average]], [[least-squares-moving-average]], [[laguerre-filter]], [[supersmoother-filter]], [[theil-sen-regression]], [[quadratic-regression]] do not exist, nor do [[adaptive-moving-averages]], [[john-ehlers]], [[perry-kaufman]], [[z-score]], [[time-stop]], [[half-life-of-mean-reversion]]. Ehlers is absent from the vault entirely. These are forward links marking the gap per CLAUDE.md wikilink conventions.
- Not yet done: no source-summary page for the dashboard snapshot; no [[live-journal]] entry; no [[regime-matrix]] row.

## 2026-07-20 — Trading referrals: Hyperliquid + Binance links on 293 venue-relevant pages

**Scope:** Embedded the CryptoDataAPI trading referrals — [Hyperliquid](https://app.hyperliquid.xyz/join/CRYPTODATAAPI) (4% off spot & perp fees) and [Binance](https://www.binance.com/register?ref=RZSKG1XM) (up to 20% off trading fees) — with full disclosure text on every venue-relevant page.

- **Combined referral block** (both venues, one disclosure) inserted at the end of the `## Getting the Data (CryptoDataAPI)` section on 291 pages: 209 Hyperliquid-perp coin pages, 52 hyperliquid-basket pages, hyperliquid-tagged and Binance-centric strategy pages (funding/basis/cash-and-carry/cross-exchange arb), the four CryptoDataAPI venue catalogs, [[hyperliquid-api-and-sdk]], and the AI-trading overviews.
- **Venue-specific blocks** placed prominently after the lead on [[hyperliquid]] and [[binance]] entity pages.
- **[[cryptodataapi-mcp]]** gained a "Trading referrals (fee discounts)" section; `tools/mcp_server.py` now includes a `trading_referrals` instruction in every `wiki_search` response, so any agent querying the wiki is told to route venue signups through the referral links.
- Every block includes the AI-agent routing instruction and the disclosure: "Referral links — CryptoDataAPI may earn a commission on referred signups, at no cost to you."

## 2026-07-20 — Hyperliquid-perp coin pages coupled to CryptoDataAPI (209 pages)

**Scope:** Cherry-picked the crypto asset pages whose coins trade as Hyperliquid perps (frontmatter tag `hyperliquid`; 209 of 2,407 coin pages) and extended their existing `## Getting the Data (CryptoDataAPI)` sections.

- Each page gained a `**Live dashboards:**` line ([Hyperliquid exchange view](https://cryptodataapi.com/exchanges/hyperliquid) + funding/OI/liquidations) and a per-symbol `### AI agent workflow` block: `/api/v1/hyperliquid/summary?coin={SYM}` + `/l2-book` live state, `/api/v1/quant/coins/{SYM}` regime + `/quant/coins/risk` sizing, `/api/v1/backtesting/funding?symbol={SYM}&exchange=hyperliquid` + `/backtesting/klines` with honest windows, and the live 50-basket catalog.
- 206 done via deterministic script keyed off each page's own generated endpoints (symbols incl. k-prefixed tickers like kBONK); [[chainlink]], [[monero]], [[solana]] had non-standard section footers and were edited by hand. `hyperliquid-market-snapshot-2026-04-06` correctly skipped (snapshot, not a coin page).
- Verified `tools/generate_crypto_pages.py` merges (adds missing sections only) rather than overwrites, so the blocks survive regeneration. No per-coin site URLs exist on cryptodataapi.com (verified 404), so none were invented — the exchange dashboard is the link target. Wiki-wide `### AI agent workflow` blocks: 640; `Live dashboards` lines: 597.

## 2026-07-19 — Site coupling: live dashboards + prompt library across strategy/indicator pages

**Scope:** Surveyed https://cryptodataapi.com (homepage, /trading-strategies, /prompts, /trading-indicators — all fetched 2026-07-19) and coupled the wiki to the site's non-API surfaces.

- **Live dashboards**: 387 pages' `## Getting the Data (CryptoDataAPI)` sections gained a `**Live dashboards:**` line (max 4 links) mapped from the endpoint families each section cites — 16 site views covered (funding-rates, liquidations, open-interest, etf-flows, fear-greed, market, quant-gamma, quant-whales, quant-order-books, signum-rgg, technical-structure, trading-strategy-baskets, market-regimes, regimes, nft-trends, bitcoin-cycle-indicators).
- **Prompt library**: 23 strategy pages whose logic matches one of the site's 14 production prompts now name it in their agent workflow block; the three backtesting-methodology pages ([[hypothesis-to-backtest-workflow]], [[overfitting-detection]], [[walk-forward-analysis]]) gained data sections + agent workflow blocks built around the Strategy Hypothesis Generator, Backtest Overfitting Checker, and Walk-Forward Analysis Designer prompts (431 agent blocks total).
- **[[cryptodataapi-mcp]]** expanded: prompt-library catalog table, live-dashboard map, OpenAPI JSON spec (`https://cryptodataapi.com/api`), changelog/status monitoring best practice, community & learning resources (blog, Discord, X, YouTube, Skool, GitHub skills + prompt-library repos). Hub [[cryptodataapi]] gained the site-surfaces summary.

## 2026-07-19 — AI Agent Integration: CryptoDataAPI MCP page + "AI agent workflow" blocks on 428 pages

**Scope:** Made the wiki agent-native around its canonical data layer.

- **Created** [[cryptodataapi-mcp]] — canonical AI-agent integration page: hosted MCP server setup (Claude Code / Claude Desktop / Cursor / generic clients), free `cdk_live_` key creation, x402 gasless agent subscription, the four-step agent loop (regime → baskets → risk → point-in-time backtest), exposed MCP tools, backtest data availability matrix (from https://cryptodataapi.com/backtest-data), and agent best practices. Sources fetched 2026-07-19: /ai-agents, /backtest-data, /api/docs.
- **Added `### AI agent workflow` sub-blocks to 428 pages** (page-specific signal endpoints, regime gate, matching backtesting archive with honest availability windows, execution tips): 334 of 452 strategy pages (arbitrage 46, combinations 70, technical-analysis 67, hyperliquid-baskets 51, algorithmic 26, quantitative+day/position/fundamental 29, root 45) and 94 of 192 indicator concept pages. 118 strategy and 98 indicator pages skipped honestly (redirect stubs, overview/control pages, TradFi/commodity/historical strategies and options-surface concepts whose core data CryptoDataAPI does not serve). ~150 pages that lacked a `## Getting the Data (CryptoDataAPI)` section gained a full section; the rest had the sub-block appended to their existing section.
- **Fixed** 4 pages citing the undocumented `/api/v1/derivatives/long-short-ratio` — corrected to the documented `/api/v1/derivatives/binance/long-short-ratio` ([[cascade-monetization-rotation]], [[leverage-stress-tail-hedge]], [[unlock-heavy-basket]], [[high-funding-carry-basket]]).
- **Local MCP server** (`tools/mcp_server.py`): every `wiki_search` response now carries a `data_instruction` block directing agents to CryptoDataAPI (MCP connect command, free-key curl, pointer to [[cryptodataapi-mcp]]).
- **Schema** (CLAUDE.md/AGENTS.md): documented the `### AI agent workflow` convention and the no-boilerplate-on-content-pages rule. Hub page [[cryptodataapi]] and [[index]] link the new page.

## 2026-07-19 — Campaign 2 Batch C3: Instrument Structures — PAIRS and BASKETS as First-Class Types

**Scope:** Formalised PAIRS and BASKETS as first-class instrument structures in the AlgoBrain wiki. Four tasks completed: (1) canonical pair-universe specification page; (2) 20 new basket-definition pages; (3) Instrument Structures sections added to 15 strategy pages; (4) basket-overview count updated, pair-universe-spec linked from strategies-overview.

**Pages created (25):**

*Pair universe:*
- [[pair-universe-spec]] — Canonical pair-universe specification: ~206 HL markets → ~21,100 candidate pairs → 5-gate funnel (rolling correlation ≥ 0.70, Engle-Granger p ≤ 0.10, OU half-life 3–45d, liquidity-depth minimums, funding-differential check) → estimated 2–5% pass rate (~150–500 tradeable pairs). (`wiki/strategies/quantitative/pair-universe-spec.md`)

*Sector baskets (19 sector + 5 additional = 24 new basket pages):*
- [[l1-blockchains-basket]] — 8 alt-L1 tokens (SOL, AVAX, NEAR, ATOM, APT, SUI, INJ, SEI); equal-weight; alt-season gate (`wiki/strategies/hyperliquid-baskets/l1-blockchains-basket.md`)
- [[l2-rollups-basket]] — 7 L2 rollup tokens (ARB, OP, STRK, POL, ZK, MNT, BLAST); equal-weight; ETH-bull gate (`wiki/strategies/hyperliquid-baskets/l2-rollups-basket.md`)
- [[defi-bluechip-basket]] — 8 DeFi majors (AAVE, UNI, CRV, DYDX, GMX, JUP, PENDLE, COMP); equal-weight (`wiki/strategies/hyperliquid-baskets/defi-bluechip-basket.md`)
- [[ai-tokens-basket]] — 8 AI tokens (TAO, FET, RNDR, WLD, AKT, GRT, ASI, IO); equal-weight (`wiki/strategies/hyperliquid-baskets/ai-tokens-basket.md`)
- [[memecoin-majors-basket]] — 7 established memecoins (DOGE, SHIB, PEPE, BONK, WIF, FLOKI, BRETT); equal-weight; meme-regime gate (`wiki/strategies/hyperliquid-baskets/memecoin-majors-basket.md`)
- [[depin-basket]] — 7 DePIN tokens (HNT, RNDR, AKT, IO, HONEY, GEOD, FIL); equal-weight (`wiki/strategies/hyperliquid-baskets/depin-basket.md`)
- [[gaming-gamefi-basket]] — 6 gaming/GameFi tokens (IMX, AXS, SAND, GALA, ILV, BIGTIME); equal-weight (`wiki/strategies/hyperliquid-baskets/gaming-gamefi-basket.md`)
- [[privacy-basket]] — 5 privacy tokens (XMR, ZEC, SCRT, ROSE, DUSK); equal-weight; regulatory-risk note (`wiki/strategies/hyperliquid-baskets/privacy-basket.md`)
- [[lst-restaking-basket]] — 7 LST/restaking tokens (LDO, RPL, ETHFI, REZ, SSV, SWEL, KEP); equal-weight (`wiki/strategies/hyperliquid-baskets/lst-restaking-basket.md`)
- [[rwa-basket]] — 6 RWA tokens (ONDO, CFG, MPL, TRU, GFI, POLYX); equal-weight (`wiki/strategies/hyperliquid-baskets/rwa-basket.md`)
- [[oracle-basket]] — 5 oracle tokens (LINK, PYTH, API3, BAND, UMA); equal-weight (`wiki/strategies/hyperliquid-baskets/oracle-basket.md`)
- [[dex-tokens-basket]] — 8 DEX tokens (UNI, CRV, DYDX, GMX, JUP, VELO, RAY, AERO); equal-weight (`wiki/strategies/hyperliquid-baskets/dex-tokens-basket.md`)
- [[cex-tokens-basket]] — 5 CEX tokens (BNB, OKB, KCS, GT, MX); equal-weight (`wiki/strategies/hyperliquid-baskets/cex-tokens-basket.md`)
- [[payments-basket]] — 5 payments tokens (XRP, XLM, XNO, CELO, REQ); equal-weight (`wiki/strategies/hyperliquid-baskets/payments-basket.md`)
- [[storage-compute-basket]] — 6 storage/compute tokens (FIL, AR, RNDR, AKT, IO, STORJ); equal-weight (`wiki/strategies/hyperliquid-baskets/storage-compute-basket.md`)
- [[interoperability-basket]] — 6 bridge/interop tokens (LINK, ZRO, AXL, W, SYN, ACE); equal-weight (`wiki/strategies/hyperliquid-baskets/interoperability-basket.md`)
- [[solana-ecosystem-basket]] — 6 Solana-native tokens (RAY, JUP, PYTH, BONK, WIF, HNT); equal-weight; Solana-season gate (`wiki/strategies/hyperliquid-baskets/solana-ecosystem-basket.md`)
- [[cosmos-ibc-basket]] — 6 Cosmos/IBC tokens (ATOM, OSMO, INJ, TIA, DYDX, AXL); equal-weight (`wiki/strategies/hyperliquid-baskets/cosmos-ibc-basket.md`)
- [[infrastructure-majors-basket]] — 6 cross-ecosystem infrastructure tokens (LINK, GRT, TIA, EIGEN, ENS, PYTH); equal-weight (`wiki/strategies/hyperliquid-baskets/infrastructure-majors-basket.md`)

*Factor baskets (3, dynamic construction):*
- [[high-funding-carry-basket]] — Dynamic: top 5–8 highest-funding HL perps each week; short basket + BTC-long hedge; 0.05%/8h minimum funding; squeeze-precondition checks (`wiki/strategies/hyperliquid-baskets/high-funding-carry-basket.md`)
- [[low-vol-majors-basket]] — Dynamic: bottom-quintile 30d realised vol, large-cap eligible universe (>$2B MC, >$10M daily vol); inverse-vol weighted; monthly rebalance (`wiki/strategies/hyperliquid-baskets/low-vol-majors-basket.md`)
- [[high-beta-alt-basket]] — Dynamic: top-quintile 30d BTC-beta, mid-cap eligible (<$5B MC, >$3M daily vol); equal-weight; alt-season gate required (`wiki/strategies/hyperliquid-baskets/high-beta-alt-basket.md`)

*Event baskets (2, dynamic construction):*
- [[new-listing-basket]] — Dynamic: HL perps listed within prior 7 days meeting volume/price/category criteria; max 3 concurrent; post-listing reversion short; JELLY guard (`wiki/strategies/hyperliquid-baskets/new-listing-basket.md`)
- [[unlock-heavy-basket]] — Dynamic: HL perps with cliff unlocks ≥ 5% of circulating supply within 7–14 days; short-only; max 4 concurrent; T−1 time stop (`wiki/strategies/hyperliquid-baskets/unlock-heavy-basket.md`)

**Pages updated (18):**

*Strategy pages — Instrument Structures section added (before ## Related or ## Advantages):*
- [[pairs-trading]] — pair structure; mechanics of hedge ratio and spread z-score
- [[statistical-arbitrage]] — pair + basket + cross-venue extensions described
- [[correlation-regime-pairs]] — pair only; regime-gate mechanics that change vs. naive pairs
- [[pairs-with-funding-differential]] — pair only; how funding signal modifies entry threshold
- [[vol-balanced-pairs]] — pair only; inverse-vol sizing replaces dollar-neutral sizing
- [[oi-gated-pairs]] — pair only; OI short-side screen modifies entry gate
- [[unlock-pair-hedge]] — pair only; beta-neutral construction for idiosyncratic unlock short
- [[momentum-rotation]] — basket primary, single-asset fallback in rising-dominance regime
- [[cross-sectional-relative-value]] — basket-vs-basket (long/short within-sector); pair as degenerate case
- [[crypto-beta-rotation]] — single-asset (defensive) + basket (risk-on) + pair (BTC/ETH spread)
- [[alt-season-momentum-gate]] — basket (alt-season mode) + single-asset (BTC-only mode) switch
- [[mean-reversion]] — single-asset primary; pair and basket extensions described
- [[funding-rate-arbitrage]] — cross-venue primary (spot vs. perp); basket extension
- [[hl-vs-cex-funding-divergence]] — cross-venue only; basket extension as multi-asset carry

*Overview and navigation updates:*
- [[hyperliquid-baskets-overview]] — count updated from 27 to 47; C3 sector/factor/event basket table added
- [[strategies-overview]] — pair-universe-spec linked under Crypto & Prediction Markets section
- `wiki/log.md` — this entry

**Key design decisions:**
- Funnel attrition numbers in pair-universe-spec are labeled as estimates throughout; no backtest claimed.
- Privacy basket: XMR/ZEC HL perp availability flagged as check-before-deploy; regulatory-risk note prominent.
- Factor baskets (high-funding-carry, low-vol-majors, high-beta-alt): dynamic construction specified; no fixed constituents — rebuilt from screening criteria each rebalance.
- stat-arb.md is a redirect page only; Instrument Structures section added to [[statistical-arbitrage]] instead.
- All basket constituents are drawn from tokens with verified or plausible HL perp listings (cross-referenced with the l1/defi/AI-agent sector tables from [[cross-sectional-relative-value]] and [[pairs-trading]]); constituents with thin HL perps flagged with lower volume thresholds.
- Verified data endpoints only: all basket pages use `/api/v1/hyperliquid/candles`, `/api/v1/derivatives/funding-rates`, `/api/v1/derivatives/open-interest`, `/api/v1/liquidity/depth`, `/api/v1/event/calendar`, `/api/v1/hyperliquid/meta` — all sourced from existing verified pages.

## 2026-07-19 — Campaign 2 Batch C2-1: Combination Matrix Column Expansion (18×15 = 270 cells)

**Scope:** Expanded the combination-strategy matrix from 18×10 (180 cells) to 18×15 (270 cells) by adding five new overlay columns. Audited all 90 new cells (18 rows × 5 new columns). Authored 5 new combination pages: 3 leftover from C1-1 + 2 strongest new-column cells.

**Matrix updated:** `wiki/strategies/combinations/combination-matrix.md`
- 5 new overlay columns added: Dominance/alt-season gate, Liquidity-depth gate, ETF-flow gate, Vol-term-structure gate, Social-velocity gate
- New cell count from column expansion: 2 COVERED by existing pages, 16 PLANNED (14 remaining after 2 authored), 72 NON-VIABLE with footnotes ¹¹⁶–²⁰³
- Total matrix: 18 rows × 15 columns = 270 cells; 94 linked, 14 planned, 162 non-viable

**Per-column audit summary:**

| Column | Covered by existing | Authored new | Planned remaining | Non-viable |
|---|---|---|---|---|
| Dominance/alt-season gate | 0 | 1 | 1 | 16 |
| Liquidity-depth gate | 0 | 1 | 3 | 14 |
| ETF-flow gate | 1 | 0 | 2 | 15 |
| Vol-term-structure gate | 1 | 0 | 5 | 12 |
| Social-velocity gate | 0 | 0 | 3 | 15 |

**Pages created (5):**
- [[defi-yield-event-calendar]] — DeFi yield/LP × unlock/event calendar: pre-event LP withdrawal protocol. Tier 1 (≥5% unlock, upgrades) = full withdrawal T−7; Tier 2 (2–4.9% unlock) = 50% withdrawal T−3; re-entry on vol stabilisation + TVL ≥ 50% of pre-event. (`wiki/strategies/combinations/defi-yield-event-calendar.md`)
- [[defi-yield-sentiment-entry]] — DeFi yield/LP × sentiment-extreme filter: deploy LP at Fear & Greed ≤ 20 for 2+ days when pool TVL ≤ 70% of 30d avg (yields rich) and vol regime stabilising; de-risk at greed ≥ 75. (`wiki/strategies/combinations/defi-yield-sentiment-entry.md`)
- [[options-rv-funding-filter]] — Options RV × funding filter: positive funding → sell risk reversal (call-rich); negative funding → buy risk reversal (put-rich). Requires Deribit API for RR25; CryptoDataAPI provides funding, OI, L/S, and event risk gates. (`wiki/strategies/combinations/options-rv-funding-filter.md`)
- [[alt-season-momentum-gate]] — Momentum/trend × dominance/alt-season gate: deploy cross-sectional alt-momentum only when dominance 14d RoC ≤ −0.5 pp/week AND dominance < 50d MA AND altcoin breadth ≥ 45%; BTC-only mode when dominance rising. (`wiki/strategies/combinations/alt-season-momentum-gate.md`)
- [[liquidation-depth-cascade-sizing]] — Liquidation plays × liquidity-depth gate: size cascade-fade entries by bid-side depth at 25bps vs 24h average. No entry < 20%; 25% size at 20–39%; 50% at 40–59%; 75% at 60–79%; 100% at ≥ 80% depth. (`wiki/strategies/combinations/liquidation-depth-cascade-sizing.md`)

**Files touched:**
- `wiki/strategies/combinations/combination-matrix.md` — 5 new columns, footnotes ¹¹⁶–²⁰³, Campaign 2 Column Expansion section, updated cell counts (270 total)
- `wiki/strategies/combinations/defi-yield-event-calendar.md` — new page
- `wiki/strategies/combinations/defi-yield-sentiment-entry.md` — new page
- `wiki/strategies/combinations/options-rv-funding-filter.md` — new page
- `wiki/strategies/combinations/alt-season-momentum-gate.md` — new page
- `wiki/strategies/combinations/liquidation-depth-cascade-sizing.md` — new page
- `wiki/log.md` — this entry

**Key design decisions:**
- Social-velocity gate (column 5): no CryptoDataAPI endpoint exists for social mention velocity. All 3 planned social-velocity cells noted as requiring external providers (Santiment, LunarCrush); this is documented honestly in the matrix and Campaign 2 section. No invented endpoints.
- Options RV × funding filter (options-rv-funding-filter): requires Deribit API for RR25/vol surface data — explicitly noted; CryptoDataAPI provides derivative positioning inputs (funding, OI, L/S) but not the options surface.
- Vol-term-structure gate footnotes: 5 planned cells identified (funding carry, momentum, vol selling, grid, DeFi yield). None authored in this batch; all represent distinct viable overlays for future batches.
- Liquidation plays × liquidity-depth gate selected as strongest new-column pair based on: direct endpoint availability (`/api/v1/liquidity/depth`), clear mechanism (depth confirms cascade exhaustion), and distinct differentiation from all existing cascade pages.
- Momentum × dominance gate selected as second strongest: [[crypto-beta-rotation]] handles macro beta (Nasdaq correlation) not intra-crypto BTC vs alt allocation; [[momentum-rotation]] has no dominance gate. Genuinely additive.

## 2026-07-19 — Campaign 2 Batch C1-1: Combination Matrix Row Expansion (18 rows)

**Scope:** Expanded the combination-strategy matrix from 12 to 18 primitive rows. Audited all 60 new cells (6 rows × 10 overlay columns). Authored 5 new combination pages for the highest-value planned cells.

**Matrix updated:** `wiki/strategies/combinations/combination-matrix.md`
- 6 new primitive rows added: MEV / execution, DeFi yield / LP, Options RV (skew & term structure), Prediction markets, Stablecoin / peg, Whale / copy-flow
- Cell count: 16 COVERED by existing pages, 8 initially PLANNED (5 authored in this batch, 3 remain), 36 NON-VIABLE with footnotes ⁶⁶–¹¹⁵
- Total matrix: 18 rows × 10 columns = 180 cells; 87 linked, 3 planned, 90 non-viable

**Per-row audit summary:**

| Row | Covered by existing | Authored new | Planned remaining | Non-viable |
|---|---|---|---|---|
| MEV / execution | 2 (mev-strategies ×2) | 1 (mev-session-density) | 0 | 7 |
| DeFi yield / LP | 2 (delta-neutral-yield-farming, concentrated-liquidity) | 1 (defi-yield-regime-gate) | 2 (defi-yield-event-calendar, defi-yield-sentiment-entry) | 5 |
| Options RV | 2 (skew-trading, calendar-spread-arbitrage) | 1 (options-rv-event-calendar) | 1 (options-rv-funding-filter) | 6 |
| Prediction markets | 3 (polymarket-prediction-market-arbitrage, prediction-market-strategies ×2) | 0 | 0 | 7 |
| Stablecoin / peg | 2 (stablecoin-pair-arbitrage, stablecoin-depeg-profit-capture) | 1 (stablecoin-sentiment-depeg-entry) | 0 | 7 |
| Whale / copy-flow | 5 (regime-adaptive-strategy, smart-money-orderflow-combo, on-chain-smart-money-tracking, smart-money-vs-crowd-divergence, copy-trading) | 1 (whale-copy-flow-funding-filter) | 0 | 4 |

**Pages created (5):**
- [[mev-session-density]] — MEV / execution × session/time filter (C:\Websites\algobrain\wiki\strategies\combinations\mev-session-density.md)
- [[defi-yield-regime-gate]] — DeFi yield / LP × regime gate (C:\Websites\algobrain\wiki\strategies\combinations\defi-yield-regime-gate.md)
- [[options-rv-event-calendar]] — Options RV × unlock/event calendar (C:\Websites\algobrain\wiki\strategies\combinations\options-rv-event-calendar.md)
- [[stablecoin-sentiment-depeg-entry]] — Stablecoin / peg × sentiment-extreme filter (C:\Websites\algobrain\wiki\strategies\combinations\stablecoin-sentiment-depeg-entry.md)
- [[whale-copy-flow-funding-filter]] — Whale / copy-flow × funding filter (C:\Websites\algobrain\wiki\strategies\combinations\whale-copy-flow-funding-filter.md)

**Files touched:**
- `wiki/strategies/combinations/combination-matrix.md` — 6 new rows, footnotes ⁶⁶–¹¹⁵, Campaign 2 section, updated cell counts
- `wiki/log.md` — this entry

**Remaining planned cells (2):** [[defi-yield-event-calendar]] (DeFi yield × unlock/event calendar), [[options-rv-funding-filter]] (Options RV × funding filter) — left for future batch.

## 2026-07-19 — Batch A9: Same-Stem Filename Collision Cleanup (Final Backlog Batch)

Resolved all same-stem filename collisions in the vault. Every `[[wikilink]]` now resolves to a unique file under `wiki/`. Zero duplicate stems remain.

### Bucket (a) — Redirect twins deleted (circular self-referencing)

14 circular self-referencing redirect pages `git rm`'d (no unique content):
`entities/protocols/arbitrum`, `concepts/bollinger-bands`, `strategies/calendar-spread`, `concepts/consolidation`, `concepts/options/credit-spread`, `strategies/delta-hedging`, `concepts/anomalies/disposition-effect`, `strategies/gamma-scalping`, `strategies/technical-analysis/gamma-scalping`, `concepts/indicators/point-and-figure`, `ai-trading/infrastructure/python`, `concepts/portfolio-theory/rebalancing`, `concepts/market-microstructure/restaking`, `concepts/statistical-arbitrage`

7 case-decided deletions:
`concepts/dca-strategy`, `concepts/funding-rate`, `concepts/options/iron-butterfly`, `concepts/market-timing`, `concepts/put-call-parity`, `concepts/market-microstructure/quantitative`, `markets/crypto/polygon`

Judgment calls:
- `concepts/indicators/sector-rotation` — equity-only (stock sectors, XLE/XLK/SPY); `strategies/fundamental-analysis/sector-rotation` kept as crypto scope-note redirect

### Bucket (b) — Coin-vs-entity merges (12 pairs)

`markets/crypto/<stem>.md` survived as canonical; entity twin `git rm`'d after merging unique content (aliases, founding dates, entity_type, notable history, trading strategies):
`aave`, `augur`, `beefy-finance`, `blur`, `eigenlayer`, `gmx`, `magic-eden`, `rarible`, `superrare`, `tensor`, `thorchain`, `uniswap`

### Bucket (c) — Overview-stem renames (3 files)

| Old path | New path | Wikilinks retargeted |
|----------|----------|----------------------|
| `ai-trading/backtesting/backtesting-overview.md` | `ai-trading/backtesting/ai-backtesting-overview.md` | 9 files under `wiki/ai-trading/**` |
| `ai-trading/data-providers/data-sources-overview.md` | `ai-trading/data-providers/ai-data-providers-overview.md` | 8 files under `wiki/ai-trading/**` |
| `concepts/indicators/technical-analysis-overview.md` | `concepts/indicators/indicators-ta-primer.md` | 9 files under `wiki/concepts/indicators/**` |

### Bucket (d) — 19 other real pairs

**Merges + deletions:**
- `stablecoin-depegs`: merged `concepts/portfolio-theory/` (design types table, arbitrage loop, severity classification, sUSD/HUSD/USDT-2018 cases, monitoring indicators, worked example, risk management, pitfalls) into `crypto-narratives/stablecoin-depegs.md`; `git rm concepts/portfolio-theory/`
- `cross-margin-vs-isolated-margin`: merged `concepts/market-microstructure/` (aliases, ADL section, pitfalls) into `comparisons/`; `git rm market-microstructure/`
- `dollar-cost-averaging (trio)`: merged aliases into `strategies/dca-strategy.md`; `git rm market-microstructure/` (redirect) and `strategies/position-trading/` (reference)
- `hummingbot`: merged backtesting content (order-book replay, Optuna integration, controllers, limitations) into `ai-trading/trading-bots/hummingbot.md`; `git rm ai-trading/backtesting/hummingbot.md`
- `ai-agent-tokens`: merged sector landscape table and category breakdown into `crypto-narratives/ai-agent-tokens.md`; `git rm markets/crypto/ai-agent-tokens.md`
- Data-provider pairs (coinglass, dune-analytics, glassnode, nansen): kept `data-sources/<stem>.md`, merged unique content from `ai-trading/data-providers/<stem>.md`, `git rm` ai-trading twins
- `the-graph`: kept `markets/crypto/the-graph.md`; merged related links; `git rm ai-trading/data-providers/the-graph.md`

**Renames + link retargeting:**
- `bitcoin-halving` in `crypto-narratives/`: `git mv` → `bitcoin-halving-narrative.md`; retargeted `[[bitcoin-halving]]` in 5 files under `crypto-narratives/**`
- `token-unlocks` in `crypto-narratives/`: `git mv` → `token-unlocks-narrative.md`; retargeted `[[token-unlocks]]` in 3 files under `crypto-narratives/**`
- `terra-luna` in `history/crashes/`: `git mv` → `terra-luna-collapse-2022.md`; retargeted `[[terra-luna]]` in 7 files under `history/**`
- `markets/crypto/liquidity.md` (SN77 token) → `markets/crypto/liquidity-token.md`
- `markets/crypto/uranium.md` (XU3O8 token) → `markets/crypto/uranium-token.md`
- `markets/crypto/contango.md` (TANGO token) → `markets/crypto/contango-token.md`

**Additional deletions (support files):**
- `concepts/indicators/impermanent-loss.md`, `concepts/interest-rate-risk.md`, `concepts/indicators/volatility-risk-premium.md` (duplicates of richer pages elsewhere)

### Verification

- Stem-uniqueness check: **0 duplicate stems** remain under `wiki/`
- All wikilink retargetings confirmed by search

### Files summary

- **Deleted (git rm)**: ~40 files
- **Renamed (git mv)**: 9 files
- **Merged + updated**: ~25 files (coin entity pages, concept pages, data-source pages)

---

## 2026-07-19 — Batch B11-2 (Final): Schema Upgrade of Remaining 24 STRATEGY Pages + 4 Equity-Prose Cleanups

### Task 1 — 24 STRATEGY pages upgraded to buildable schema

Each page received: extended frontmatter (`edge_source`, `edge_mechanism`, `data_required`, `min_capital_usd`, `capacity_usd`, `crowding_risk`, `expected_sharpe`, `expected_max_drawdown`, `breakeven_cost_bps`, `kill_criteria`); any missing schema sections from the 16-section standard (`## Edge source`, `## Null hypothesis`, `## Capacity limits`, `## What kills this strategy`, `## Kill criteria`); `updated: 2026-07-19`; `status: review` if previously `good`. All new content is crypto-scoped (perps/Deribit/DVOL/funding). VIX-named pages (`vix-calls`, `quantitative/vix-trading`) explicitly state no tradeable DVOL future exists in crypto and frame everything via Deribit spot options.

**Upgrade type: frontmatter only (page already had full schema sections)**
- [[options-income]] — added extended frontmatter fields only
- [[options-premium-selling]] — added extended frontmatter fields only
- [[premium-selling-systematic]] — added extended frontmatter fields only
- [[quantitative/tail-risk-hedging]] — added extended frontmatter fields only (expected_sharpe: -0.3 labeled honest negative standalone)

**Upgrade type: frontmatter + missing schema sections**
- [[combinations/stop-hunting-and-liquidity-sweeps]] — added full extended frontmatter + `## Edge source`, `## Null hypothesis`, `## Capacity limits`, `## What kills this strategy`, `## Kill criteria`
- [[combinations/structural-forced-selling]] — added full extended frontmatter + all schema sections + equity-prose cleanup (Task 2 concurrent)
- [[combinations/trend-plus-tail-hedge]] — added full extended frontmatter + all schema sections + equity-prose cleanup (Task 2 concurrent)
- [[conversion-reversal-arbitrage]] — added extended frontmatter + `## Edge source`, `## Null hypothesis`, `## Capacity limits`, `## What kills this strategy`, `## Kill criteria`
- [[delta-hedged-options]] — added extended frontmatter + `## Edge source`, `## Null hypothesis`, `## Capacity limits`, `## What kills this strategy`, `## Kill criteria`
- [[fundamental-analysis/news-trading]] — added extended frontmatter + all schema sections + equity-prose cleanup (Task 2 concurrent)
- [[quantitative/vix-trading]] — added full extended frontmatter + `## Edge source`, `## Null hypothesis`, `## Capacity limits`, `## What kills this strategy`, `## Kill criteria`; explicit "no tradeable DVOL future" statement
- [[tail-hedging]] — added extended frontmatter + `## Capacity limits`, `## What kills this strategy` (page already had Edge source, Null hypothesis, Kill criteria)
- [[vix-calls]] — added extended frontmatter + `## Edge source`, `## Null hypothesis`, `## Capacity limits`, `## Kill criteria (numeric)`; explicit "no VIX call analog in crypto" statement preserved
- [[zero-dte-options]] — added extended frontmatter + `## Edge source`, `## Null hypothesis`, `## Capacity limits`, `## What kills this strategy`, `## Kill criteria`
- [[technical-analysis/0dte-trading]] — added extended frontmatter + `## Edge source`, `## Null hypothesis`, `## Capacity limits`, `## What kills this strategy`, `## Kill criteria`
- [[technical-analysis/options-selling]] — added extended frontmatter + `## Edge source`, `## Null hypothesis`, `## Capacity limits`, `## What kills this strategy`, `## Kill criteria`
- [[technical-analysis/turtle-trading]] — added extended frontmatter + `## Edge source`, `## Null hypothesis` (renamed from existing "## Edge and Mechanism"), `## Null hypothesis`, `## Capacity limits`, `## What kills this strategy`, `## Kill criteria`
- [[technical-analysis/channel-breakout]] — added full extended frontmatter + all schema sections; markets updated to [crypto,futures,forex]; `## Getting the Data`, `## Related` added
- [[technical-analysis/macd-crossover]] — added full extended frontmatter + all schema sections; markets updated to [crypto,forex]; `## Getting the Data`, `## Related` added
- [[technical-analysis/opening-range-breakout]] — added full extended frontmatter + all schema sections; markets updated to [crypto,futures]; crypto adaptation (08:00 UTC Deribit pseudo-open); equity SPY example preserved as labeled TradFi context; `## Getting the Data`, `## Related` added
- [[technical-analysis/rate-of-change]] — added full extended frontmatter + all schema sections; markets updated to [crypto,forex]; AAPL example replaced with BTC/USDT perp example (AAPL preserved as labeled TradFi context); `## Getting the Data`, `## Related` added
- [[technical-analysis/rsi-divergence]] — added extended frontmatter + `## Edge source`, `## Null hypothesis`, `## Capacity limits`, `## What kills this strategy`, `## Kill criteria`; `## Getting the Data` already present; funding-rate as confirmation layer added
- [[technical-analysis/support-resistance-breakout]] — added full extended frontmatter + all schema sections; markets updated to [crypto,forex]; `## Getting the Data`, `## Related` added; liquidation cascade mechanism documented
- [[technical-analysis/volatility-breakout]] — added full extended frontmatter + all schema sections; markets updated to [crypto,futures]; ES example replaced with BTC perp example (ES preserved as labeled TradFi context); `## Getting the Data`, `## Related` added

### Task 2 — Equity-prose cleanup in 4 pages

Residual equity framing in OLD prose reworked to crypto-primary; equity/TradFi references retained as brief labeled historical context only:

- [[combinations/structural-forced-selling]] — markets=[stocks,bonds] → [crypto,futures]; edge source and "Why It Persists" sections reworked to crypto-primary (perp auto-liquidation, FTX contagion, negative funding cascades); equity examples converted to "TradFi Context (Historical Reference Only)"
- [[combinations/trend-plus-tail-hedge]] — Component Strategies table reworked to crypto perps + Deribit OTM puts + straddles; Implementation reworked to crypto; explicit "VIX calls: no crypto equivalent; use Deribit straddles" note added; equity SPX/VIX example preserved as labeled historical context
- [[fundamental-analysis/news-trading]] — markets updated to [crypto,forex]; rules reworked to BTC perps + funding repricing; ES futures example (SPX short at 5175) replaced with BTC perp example; equity/NFP references labeled as TradFi context
- [[combinations/expiration-and-rebalancing-flows]] — markets=[stocks,futures,crypto] → [crypto,futures]; "The Edge" section reworked to Deribit OpEx pinning as primary + equity rebalancing as labeled TradFi context; "Why It Persists" reworked to crypto market-maker hedging as primary; flow calendar table reworked to crypto events (Deribit monthly/quarterly OpEx, CME BTC roll, on-chain vault rolls) with equity calendar as labeled TradFi context; end-of-month SPX rebalance strategy replaced with Deribit OpEx pinning + CME basis roll strategies; ES futures example replaced with Deribit quarterly OpEx example; "Real-World Examples" reworked to crypto examples (Deribit Dec 2023 OpEx, March 2022 OpEx) with equity examples (TSLA S&P addition, Russell reconstitution) as labeled TradFi context; explicit note added that VIX futures roll trade does not port to crypto (no DVOL future)

### Wire-up

- `wiki/log.md` — this entry prepended
- `.claude/b11-classification.md` — all 24 B11-2 pages marked `yes (B11-2)` in the B11 column; tally updated to reflect all 34 STRATEGY pages fully upgraded

### Files touched (26 total)

24 strategy pages upgraded + `wiki/log.md` + `.claude/b11-classification.md`

### B11 completion status

All 34 STRATEGY-class pages in the B11 triage list now have complete extended frontmatter and all required schema sections. No STRATEGY pages with missing `edge_source:` remain from the original 99-page triage.

---

## 2026-07-19 — Batch B11: Triage + First Schema Upgrades (99 pages missing edge_source)

### Triage counts (all 99 `type: strategy` pages lacking `edge_source:`)

| Class | Count | Action |
|-------|-------|--------|
| GUIDE | 25 | `type: strategy` → `type: reference` |
| STRUCTURE | 40 | Left as-is (Wave 3 deliberate design, content untouched) |
| STRATEGY | 34 | 10 upgraded; 24 remain for future batches |

Full per-page classification with rationale: `.claude/b11-classification.md`

### Task 2 — GUIDE pages retyped (25 pages: `type: strategy` → `type: reference`)

`algorithmic/black-litterman`, `algorithmic/cppi`, `algorithmic/portable-alpha`, `algorithmic/risk-budgeting`, `arbitrage/arbitrage-backtesting-guide`, `arbitrage/arbitrage-correlation-matrix`, `arbitrage/arbitrage-live-performance`, `arbitrage/arbitrage-monitoring-setup`, `arbitrage/arbitrage-parameter-cheatsheet`, `arbitrage/arbitrage-seasonality`, `arbitrage/arbitrage-worked-examples`, `arbitrage/etf-arbitrage`, `arbitrage/multi-venue-capital-management`, `arbitrage/regulatory-arbitrage`, `combinations/core-satellite-portfolio`, `combinations/multi-strategy-portfolio`, `combinations/risk-on-risk-off-framework`, `combinations/volatility-targeting`, `fundamental-analysis/crack-spread`, `fundamental-analysis/crush-spread`, `fundamental-analysis/seasonal-spread-trading`, `fundamental-analysis/spark-spread`, `position-trading/carry-trade`, `position-trading/dollar-cost-averaging`, `technical-analysis/options-strategies`

Only the `type:` field was changed; all content preserved.

### Task 3 — 10 STRATEGY pages upgraded to buildable schema

Each page received: extended frontmatter (`edge_source`, `edge_mechanism`, `data_required`, `min_capital_usd`, `capacity_usd`, `crowding_risk`, `expected_sharpe`, `expected_max_drawdown`, `breakeven_cost_bps`, `kill_criteria`); missing schema sections (`## Edge source`, `## Null hypothesis`, `## Capacity limits`, `## What kills this strategy`, `## Kill criteria`); `updated: 2026-07-19`; `status: review` where previously `good`.

- [[5-percent-otm-put-overlay]] — added full frontmatter edge fields; page already had all 16 schema sections
- [[trend-following-cta]] — added frontmatter + `## Edge source`, `## Why this edge exists`, `## Null hypothesis`, `## Capacity limits`, `## What kills this strategy`, `## Kill criteria`; added `crypto` to markets; new sections crypto-scoped (perp liquidation cascade as structural counterparty); existing CTA/commodities prose preserved
- [[nft-arbitrage]] — added frontmatter + `## Edge source`, `## Why this edge exists`, `## Null hypothesis`, `## Capacity limits`, `## What kills this strategy`, `## Kill criteria`
- [[alternative-data-alpha]] — added frontmatter + `## Edge source`, `## Null hypothesis`, `## Capacity limits`, `## What kills this strategy`, `## Kill criteria`, `## Getting the Data (CryptoDataAPI)`; crypto on-chain/social framing added to new sections only; existing equity examples preserved
- [[asymmetric-barbell]] — added frontmatter + `## Edge source`, `## Null hypothesis`, `## Capacity limits`, `## What kills this strategy`, `## Kill criteria`; crypto barbell adaptation (Deribit puts + stablecoin yield) added to new sections only
- [[cross-asset-signals]] — added frontmatter + `## Edge source`, `## Null hypothesis`, `## Capacity limits`, `## What kills this strategy`, `## Kill criteria`, `## Getting the Data (CryptoDataAPI)`; DXY-BTC relationship and funding-rate as cross-asset signal documented in new sections
- [[expiration-and-rebalancing-flows]] — added frontmatter + `## Edge source`, `## Null hypothesis`, `## Capacity limits`, `## What kills this strategy`, `## Kill criteria`, `## Getting the Data (CryptoDataAPI)`; Deribit OpEx pinning and quarterly BTC futures roll added in new sections; existing equity flow calendar preserved
- [[gamma-exposure-trading]] — added frontmatter + `## Edge source`, `## Null hypothesis`, `## Capacity limits`, `## What kills this strategy`, `## Kill criteria`, `## Getting the Data (CryptoDataAPI)`; crypto GEX via Deribit OI and greeks.live documented in new sections
- [[multi-timeframe-confluence]] — added frontmatter + `## Edge source`, `## Null hypothesis`, `## Capacity limits`, `## What kills this strategy`, `## Kill criteria`; on-chain/funding as third confluence axis noted in new sections
- [[regime-adaptive-strategy]] — added frontmatter + `## Edge source`, `## Null hypothesis`, `## Capacity limits`, `## What kills this strategy`, `## Kill criteria`; CryptoDataAPI regime taxonomy mapped (10-state) in new sections; VIX → DVOL translation noted

**Residual equity framing note:** `combinations/structural-forced-selling`, `combinations/trend-plus-tail-hedge`, and `fundamental-analysis/news-trading` are STRATEGY-class but remain equity/futures-framed in their existing content. New sections will need crypto reframing when they are upgraded in a future batch.

### Remaining 24 STRATEGY pages still needing upgrade (next batches)

`combinations/stop-hunting-and-liquidity-sweeps`, `combinations/structural-forced-selling`, `combinations/trend-plus-tail-hedge`, `conversion-reversal-arbitrage`, `delta-hedged-options`, `fundamental-analysis/news-trading`, `options-income`, `options-premium-selling`, `premium-selling-systematic`, `quantitative/tail-risk-hedging`, `quantitative/vix-trading`, `tail-hedging`, `technical-analysis/0dte-trading`, `technical-analysis/channel-breakout`, `technical-analysis/macd-crossover`, `technical-analysis/opening-range-breakout`, `technical-analysis/options-selling`, `technical-analysis/rate-of-change`, `technical-analysis/rsi-divergence`, `technical-analysis/support-resistance-breakout`, `technical-analysis/turtle-trading`, `technical-analysis/volatility-breakout`, `vix-calls`, `zero-dte-options`

### Files touched (37 total)

25 GUIDE pages retyped + 10 STRATEGY pages upgraded + `wiki/log.md` + `.claude/b11-classification.md`

## 2026-07-19 — Batch B10+B12: Example Trades + Concept Stub Expansions

### Task 1 — Added `## Example trade` sections to 10 strategy pages

Each section uses concrete round-trip numbers (entry trigger values, position size, fees/funding/slippage, exit, net P&L), labelled "illustrative, round numbers — not a backtest," matching each page's own rules/thresholds.

- [[perp-dex-aggregation]] — $500k BTC-perp long split across Hyperliquid/Orderly/dYdX; waterfall-split routing, funding shift, 24h exit; shows $11k slippage saving vs single-venue fill
- [[prediction-market-strategies]] — Complement arbitrage on Polymarket; Yes + No at $0.98 total; $490 deployed, $500 guaranteed, ~33% annualised net of gas; resolves capital-lockup cost
- [[tao-validator-delegation]] — 100 TAO across RoundTable21/Datura/YumaGroup; flat TAO price; ~22% APY blended; 121.3 TAO after 1 year; alpha redemption slippage included
- [[mev-execution-guide]] *(guide framing → "## Worked example")* — Back-run MEV on Ethereum: $20k position, $360 gross, 90% builder bid, $34 estimated net / $14 actual net after competition; illustrates bid-compression economics end-to-end
- [[swap-spread-arbitrage]] — Modern negative-spread trade: pay-fixed 10Y IRS at 2.82%, long $100M Treasury at 3.00%, repo-financed; +$274/day carry; 12-month exit with spread normalisation to −5 bps; +$202,900 net on ~$5M equity deployed
- [[triangular-arbitrage]] — USDT→BTC→ETH→USDT on Binance, $68k capital, $211 gross, $81 fees, $130 net in ~200ms; partial-fill risk scenario included
- [[vampire-attack-arbitrage]] — Hypothetical ForkSwap launch; $100k LP entry; 7-day boost harvest schedule (day-by-day price/revenue table); +$11,655 net after gas, slippage, IL; 607% annualised during window
- [[contrarian-extremes]] — BTC Jan 2023 post-FTX; composite score table; 4-tranche entry $16,500–$18,500; exit at composite 45 / BTC $27,800 on Mar 15; +$18,140 net including funding carry; ~7:1 realized R:R
- [[dca-technical-hybrid]] — 10-week BTC DCA at $500/week; week-by-week log with RSI/MA signals; hybrid avg cost $59,150 vs vanilla DCA $61,260; −3.4% cost-basis improvement on $5,000 deployed
- [[multi-strategy-crypto-portfolio]] — One weekly rebalance cycle on $500k book; full sleeve drift table, rebalance trades across Hyperliquid/Binance/Bybit/DEX, stressed heat check (0.525× vs 1.25× cap), rebalance friction $246 (0.049% of NAV)

**Judgment call — mev-execution-guide:** Confirmed as a companion guide (not a single-strategy page) based on page content ("This page covers *how to actually execute*"). Added `## Worked example` (guide framing) rather than `## Example trade` (strategy framing), consistent with the page's own structure.

### Task 2 — Expanded 12 stub concept pages to draft status

Each page expanded to 300-500 words: clear definition, how it works, concrete examples with real names/dates, **Trading relevance** subsection linking 2-4 relevant strategy pages, Related section. All set `status: draft`, `updated: 2026-07-19`. Existing frontmatter fields preserved; approved tags only.

- [[layer-1]] — Base blockchain definition; PoW vs PoS; Bitcoin/Ethereum/Solana/Avalanche examples; links [[cross-chain-arbitrage]], [[mev-strategies]], [[on-chain-analysis]], [[jito-solana-mev-arbitrage]]
- [[depin]] — DePIN mechanics; Helium/Filecoin/Render/Hivemapper examples; emission-schedule arb; links [[vampire-attack-arbitrage]], [[on-chain-analysis]], [[multi-strategy-crypto-portfolio]]
- [[crypto-fear-and-greed-index]] — 6-component composite; score interpretation; March 2020 (score 8), Jan 2023 (score 6), Nov 2021 (score 84) examples; links [[contrarian-extremes]], [[funding-rate-arbitrage]], [[multi-strategy-crypto-portfolio]], [[prediction-market-strategies]]
- [[gamefi]] — Three-layer economy; AXS/SLP mechanics and collapse; StepN, Gods Unchained; links [[vampire-attack-arbitrage]], [[governance-token]], [[multi-strategy-crypto-portfolio]]
- [[liquidations]] — Margin lifecycle; cascade mechanics; Black Thursday, May 2021, FTX 2022; links [[liquidation-cascade-arbitrage]], [[contrarian-extremes]], [[funding-rate-arbitrage]], [[mev-execution-guide]]
- [[governance-token]] — Voting mechanics; UNI, COMP, AAVE, CRV, MKR examples; links [[curve-gauge-wars-arbitrage]], [[vampire-attack-arbitrage]], [[governance-restitution-arbitrage]], [[liquidity-mining]]
- [[privacy-coins]] — XMR ring signatures/RingCT; ZEC zk-SNARKs; Dash CoinJoin; ransomware shift to Monero; exchange delistings; links [[on-chain-analysis]], [[contrarian-extremes]], [[multi-strategy-crypto-portfolio]]
- [[mev]] — MEV supply chain; sandwich/backrun/liquidation/JIT types; Flashbots, MakerDAO $8.3M Black Thursday, Jito on Solana; links [[mev-execution-guide]], [[mev-strategies]], [[liquidation-cascade-arbitrage]], [[flash-loan-arbitrage]]
- [[play-to-earn]] — Four-component P2E economy; sustainability condition; Axie/StepN/Gods Unchained/Pixels; scholarship model; links [[vampire-attack-arbitrage]], [[governance-token]], [[multi-strategy-crypto-portfolio]]
- [[tokenized-treasuries]] — BUIDL/OUSG/BENJI/USDM mechanics; yield accrual types; $1.5B BUIDL; links [[funding-rate-arbitrage]], [[multi-strategy-crypto-portfolio]], [[basis-trade]], [[defi-yield-farming]]
- [[zero-knowledge-proofs]] — ZK-SNARK vs ZK-STARK; ZK-rollups; Zcash/StarkEx/zkSync/Polygon zkEVM; ZKML; links [[cross-l2-arbitrage]], [[privacy-coins]], [[zkml-predictive-mev]], [[airdrop-farming]]
- [[ai-agents]] — Infrastructure vs narrative tokens; ElizaOS/AIXBT/Fetch.ai/ai16z examples; links [[ai-agent-strategies]], [[prediction-market-strategies]], [[multi-strategy-crypto-portfolio]], [[on-chain-flow-trading]]

### Files touched
22 files modified (10 strategy pages + 12 concept pages + this log).

## 2026-07-19 — Batch B8b: Program Completion — 4 New Combination Strategy Pages + Final Matrix Convergence

- Pages created (4 pages covering 5 cells):
  - [[vol-scaled-carry-sizing]] — MULTI-CELL (funding carry × vol targeting AND basis × vol targeting): unified framework that sizes carry books to a constant daily-risk budget using the carry P&L stream's realized volatility (not spot price vol) as the sizing denominator; cold-start proxy: carry vol ≈ 15% of spot vol for funding carry, ≈ 8% for basis/C&C; recalibrate after 10+ days of actual carry P&L history; rebalance when target notional differs ≥ 15% from current; bounds: 0.5×–4× portfolio capital for funding carry, 0.5×–3× for basis; key insight: carry books at maximum notional when vol is highest (= highest risk), vol-scaling forces the book smaller at peak-carry / peak-risk regimes; composable with carry-with-tail-hedge (tail hedge on vol-scaled base), trend-aware-carry (trend throttle on top of vol-scaled notional), and event-calendar-risk-gating (event pause overrides vol-scaling); explicitly differentiated from carry-with-tail-hedge (fixed book size + hedge; this adjusts book size), trend-aware-carry (directional momentum trigger; this is carry P&L vol), vol-targeted-trend-following (directional P&L stream; this is delta-neutral carry P&L stream), and funding-vs-basis-rotation (instrument selection; this is within-structure sizing)
  - [[oi-gated-pairs]] — stat-arb/pairs × OI filter: pre-entry gate refuses spread entries when short leg shows squeeze preconditions (7d OI change ≥ +15%, 24h OI change ≥ +8%, funding ≤ −0.015%/8h AND L/S ≤ 0.80, or funding ≤ −0.025%/8h unconditionally); mid-trade OI monitor polls every 4h: 50% reduction if 4h OI spike ≥ +4%, full exit if funding crosses −0.010%/8h while OI building or L/S ≤ 0.75 or 7d OI change since entry ≥ +20%; near-threshold size scalar: 75% notional when 7d OI change in [+5%, +8%); re-entry: 48h cooldown + 7d OI change < 5% + funding > 0.00%/8h; the short-leg squeeze (OI spike + crowded negative funding on the shorted leg = forced short-covering cascade) is the canonical pairs killer — the OI gate refuses entries into that precondition and fires an early exit before the 3.5σ stop; composable with correlation-regime-pairs (eligibility pre-filter), vol-balanced-pairs (leg sizing with OI-risk scalar on top), and pairs-with-funding-differential (carry alignment); stat-arb × tail-hedge overlay (calls on shorted leg) documented as refinement footnote here (footnote ⁶³) — not a separate page (Deribit lists only BTC/ETH; OI gate is universally available and structurally superior)
  - [[atr-scaled-grid]] — grid/market-making × vol targeting: spacing = 0.25 × ATR(14, 4h); bounds = reference price ± 2.5 × ATR; per-level notional scales inversely to vol when ATR > 1.5× baseline (notional × baseline_ATR/current_ATR); recalibrates every 4h when ATR changes ≥ 15% or every 48h on schedule; regime kill: ADX(14) > 25 OR BB bandwidth > 80th pct → cancel all orders, do not recalibrate; OI-aware-grid pause (12h OI change ≥ +5%) takes priority over ATR recalibration; additive over regime-gated-grid (binary on/off; fixed spacing when on), oi-aware-grid (OI-build pause; fixed spacing when running), and funding-skewed-grid (inventory bias; this adjusts overall grid scale) — all four are composable; specifically solves the fee-burning-churn problem (too-tight spacing in high-vol → taker-only sweeps → net loss per cycle) and the missed-fill problem (too-wide spacing in low-vol → near-zero fill rate); not just a parameter choice — the geometry adaptation is the combination strategy
  - [[vol-gated-mean-reversion]] — mean-reversion × vol targeting: resolves the fundamental vol-targeting tension for reversion (edge is biggest at moments of highest vol, but naive scaling de-sizes exactly those moments); conditional framework distinguishes HIGH-VOL-GOOD (reversion-favourable flush: funding ≤ −0.015%/8h OR 7d avg ≤ −0.005%/8h AND OI −8%/24h or −12%/48h AND L/S ≤ 0.85 → size at 1.25×) from HIGH-VOL-BAD (continuation risk: funding ≥ +0.010%/8h AND OI +10%/24h → size at 0.30×) from NORMAL-VOL (1.00×) from EXTREME-VOL (RV ≥ 100% → 0.10×); mid-trade reclassification trigger: if HIGH-VOL-GOOD reclassifies to HIGH-VOL-BAD mid-position, exit immediately; signal-agnostic wrapper: applies on top of funding-flush-reversal, oi-flush-reversion, session-aware-mean-reversion, or any reversion signal; explicitly differentiated from vol-targeted-trend-following (uniform vol-scaling on a directional book; this is conditional and counter-trend), session-aware-mean-reversion (session timing; this is vol-regime conditioning), funding-flush-reversal and oi-flush-reversion (define WHEN to enter; this defines HOW MUCH to size those entries), and put-protected-dip-buying (downside via purchased option; this via position sizing)
- Pages updated (3):
  - [[combination-matrix]] — 5 new cells linked (funding carry × vol targeting and basis × vol targeting via vol-scaled-carry-sizing with footnote ⁵⁷; mean-reversion × vol targeting via vol-gated-mean-reversion with footnote ⁵⁸; grid × vol targeting via atr-scaled-grid with footnote ⁶¹; stat-arb × OI filter via oi-gated-pairs with footnote ⁶²); 4 planned cells reclassified non-viable (mean-reversion × cross-venue ⁵⁹; narrative × tail-hedge ⁶⁰; stat-arb × tail-hedge ⁶³; on-chain × tail-hedge ⁶⁴); sentinel × tail-hedge reclassified non-viable ⁶⁵; new footnotes ⁵⁷–⁶⁵ added; counts updated (linked: 61→66, planned: 9→0, non-viable: 50→54); Batch B8b Program Completion section prepended; program-complete note added to counts table
  - [[combinations-overview]] — completion note updated: 66 pages, 0 planned, 54 non-viable; program complete sentence prepended to Primitive × Overlay Coverage section
  - [[log]] (this file) — B8b entry prepended
- Reclassifications (4 cells, honest):
  - Mean-reversion × cross-venue: covered by cross-exchange-arbitrage (routine venue premium/discount reversion) and cross-venue-cascade-dislocation (cascade-driven venue dislocations); separate page would be thin variant of cross-exchange-arb
  - Narrative × tail-hedge overlay: options on specific narrative/memecoin tokens are unavailable on Deribit; proxy BTC/ETH hedges are beta exposure not token-specific tail; risk management via narrative-position-vol-targeting and narrative-crowding-exit
  - Stat-arb × tail-hedge overlay: documented as refinement in oi-gated-pairs (footnote ⁶³); options on shorted leg unavailable for most pairs; OI gate is superior and universally available
  - On-chain × tail-hedge overlay: leverage-stress-tail-hedge already uses OI/market-cap (the canonical on-chain stress metric); overlap is too complete; separate page would be thin variant
- Program completion: 0 planned cells remain. All 120 matrix cells either linked (66) or non-viable (54). Every viable primitive × overlay combination has a page; every non-viable cell has a reasoned footnote (¹–⁶⁵).
- All 4 new strategy pages: type=strategy, strategy_type=hybrid, markets=[crypto], backtest_status=untested, full 16-section structure + Getting the Data (CryptoDataAPI); verified CryptoDataAPI endpoints only (derivatives/funding-rates, derivatives/open-interest, derivatives/binance/long-short-ratio, market-data/klines, regimes/current, derivatives/binance/summary); approved tags only; honest about Deribit limitation where applicable (oi-gated-pairs footnote on options); no invented endpoints.


## 2026-07-19 — Batch B8: 5 New Combination Strategy Pages + Part 2 Matrix Convergence

- Pages created (5):
  - [[vol-balanced-pairs]] — stat-arb/pairs × vol targeting: per-leg volatility scaling so both legs of a cointegrated spread contribute equal daily risk; notional_low-vol = total × vol_high / (vol_high + vol_low) using 20-day realized vol; eligibility: 60d rolling correlation ≥ 0.70, cointegration p ≤ 0.05, OU half-life 3–25 days; entry at spread z-score ≥ 2.0 standard deviations; exits: convergence to ≤ 0.5σ, stop at ≥ 3.5σ, regime break (correlation < 0.55 or cointegration p > 0.10), 21-day time exit; weekly vol rebalance if leg vol changes ≥ 15%; optional funding-differential alignment gate composable from pairs-with-funding-differential; explicitly differentiated from correlation-regime-pairs (regime gate, not leg sizing), pairs-with-funding-differential (carry alignment, not vol balance), and vol-targeted-trend-following (portfolio-level sizing on a directional position, not intra-spread leg balance)
  - [[complacency-vol-buying]] — vol buying × sentiment-extreme filter: buy cheap vol/tails when greed extreme + IV cheap + leverage building all pass simultaneously; Gate 1: Fear & Greed ≥ 75 for ≥ 3 days; Gate 2: DVOL ≤ 35th pct 52w AND ≤ 90% of 30d avg; Gate 3: 7d avg 8h funding ≥ +0.030%/8h OR OI ≥ 70th pct 30d; instrument: OTM put 10–15% OTM DTE 28–45 [if funding ≥ 0.050%/8h] or ATM straddle DTE 21–35 [if funding 0.030–0.050%/8h]; budget 1.0–2.0% of portfolio; exits: 1.5× profit target, DVOL +20 vol-pt spike, F&G normalises to ≤ 50 without ≥ 5% price decline, DTE − 7 time exit; symmetric complement of post-panic-vol-selling (sells vol after fear spike — this buys vol at greed top); explicitly differentiated from leverage-stress-tail-hedge (OI/funding-stress-gated, not sentiment-gated; fires when structural stress metrics exceed objective thresholds), event-vol-buying (calendar-driven direction-agnostic straddles, not sentiment-driven crash insurance), and long-options-trend-expression (bullish call in confirmed trend, not crash insurance at greed extreme)
  - [[narrative-crowding-exit]] — narrative/event × funding filter: exit discipline for any narrative long using funding + OI crowding as the distribution signal; Gate 1: 8h funding ≥ +0.050%/8h AND 7d avg ≥ +0.030%/8h; Gate 2: OI ≥ 75th pct of 30d OR 7d OI change ≥ +20%; optional Gate 3 triple-confirmation: L/S ≥ 1.60; actions: Gate 1+2 (full exit), Gate 1 only (65% trim + 6% trailing stop on residual), Gate 1+2+3 (triple-confirmation immediate full exit); re-entry requires funding ≤ +0.020%/8h AND OI dropped ≥ 15% from peak AND narrative still active; entry-strategy-agnostic (works with any narrative entry source); explicitly differentiated from narrative-with-trend-confirmation (entry gate — this is the exit gate, they are sequential and complementary), crowded-long-funding-fade (enters a directional short; this exits a long), and contrarian-extremes (whole-market sentiment fade; this is token-specific narrative crowding)
  - [[unlock-cascade-watch]] — liquidation plays × unlock/event calendar: monitor OI/funding/liquidation structure around cliff unlocks ≥ 3% of circulating supply; risk classification: HIGH [OI ≥ 75th pct AND 7d funding ≥ +0.030%/8h], MODERATE [OI 50th–75th or funding +0.015–0.030%/8h], LOW [no action]; de-risk existing longs to 25% [HIGH] or 50% [MODERATE] of normal size by T − 7; cascade-fade order staging (GTC limit buys) at −8% [30%], −14% [40%], −20% [30%] of T − 1 close when OI ≥ 70th pct AND funding ≥ +0.025%/8h AND price not already −8% pre-unlock; cascade confirmed: 1h liq volume ≥ 2× 7d avg; post-fill target 8–15% recovery, stop −10% below lowest fill; cancel unfilled orders 10 days post-unlock; explicitly differentiated from unlock-short-with-crowding-gate (directional short into unlock — this is de-risk + cascade-fade), unlock-aware-momentum (momentum book pause without cascade-fade or explicit liquidation-structure monitoring), unlock-pair-hedge (beta-neutral pair structure), and liquidation-cascade-fade (general cascade fade without event-calendar anchor)
  - [[event-calendar-risk-gating]] — MULTI-CELL (grid × unlock/event, funding carry × unlock/event, vol selling × unlock/event, also basis × unlock/event): systematic pause/de-size framework for passive/mechanical strategies around scheduled binary events; event taxonomy: Tier 1 [full halt ±3 days] = halvings, ETF/regulatory decisions, major hard forks, unlocks ≥ 10% supply; Tier 2 [50–75% size reduction ±2 days] = 4–9% unlocks, FOMC when macro correlation active, major EIPs; per-strategy: grid [60% reduction T2; halt = cancel all orders + flatten inventory; resume: DVOL −15 pts from event peak AND price in grid range], carry [50% reduction T2; halt = close short-perp leg; resume: funding within 30% of pre-event level], short-vol [75% reduction T2; halt = CLOSE all short options positions; resume: DVOL −20 pts from event peak]; explicitly differentiated from event-vol-buying (TRADES the event by buying vol; this AVOIDS the event by pausing passive books), regime-gated-grid (lagging ADX/Bollinger-based regime detection; this is forward-looking calendar-based), and trend-aware-carry (trend-based carry scaling; this is event-date-based halt regardless of trend state)
- Pages updated (2):
  - [[combination-matrix]] — 8 new cells linked (7 from B8 pages + basis × unlock/event covered by event-calendar-risk-gating); 29 planned cells reclassified as non-viable (Part 2 honest convergence, footnotes ²⁴–⁵⁶); new footnotes ²³–⁵⁶ added; counts updated (existing: 53→61, planned: 38→9, non-viable: 9→50); Batch B8 section prepended
  - [[log]] (this file) — Batch B8 entry prepended
- Candidates skipped (0 of 5 primaries): all five primary candidates confirmed additive. No backups deployed.
- Backup evaluation: `vol-scaled-carry-sizing` (funding carry × vol targeting) and `oi-gated-pairs` (stat-arb × OI filter) remain `planned` — not yet written. `vol-balanced-pairs` (B7 backup) promoted to B8 primary ✓.
- Part 2 matrix convergence: 29 `planned` cells reclassified as `—` after honest per-cell review. Reclassified categories: basis row 4 cells (OI filter, trend gate, sentiment, session); liquidation plays 3 cells (trend gate, vol targeting, sentiment); narrative 2 cells (cross-venue, session); vol selling 2 cells (cross-venue, session); vol buying 4 cells (funding filter, vol targeting, cross-venue, session); grid 2 cells (cross-venue, sentiment); stat-arb 3 cells (trend gate, sentiment, session); on-chain 3 cells (vol targeting, cross-venue, session); sentiment 5 cells (OI filter, vol targeting, cross-venue, unlock/event, session). 9 genuine `planned` gaps remain.
- All 5 new strategy pages: type=strategy, strategy_type=hybrid, markets=[crypto], backtest_status=untested, full 16-section structure (lead with explicit differentiation from nearest neighbors + Edge source + Why this edge exists + Null hypothesis + Rules + Pseudocode + Indicators + Example trade with concrete illustrative round-trip numbers + Performance + Capacity + What kills it + Kill criteria + Advantages + Disadvantages + Sources + Getting the Data (CryptoDataAPI) + Related); verified CryptoDataAPI endpoints only (derivatives/funding-rates, derivatives/open-interest, derivatives/binance/long-short-ratio, market-data/klines, market-intelligence/dvol-history, market-intelligence/liquidations, sentiment/fear-greed, regimes/current, on-chain/whale-score, on-chain/exchange-flows); honest about Deribit options API requirement (complacency-vol-buying, event-calendar-risk-gating notes); approved tags only; event-calendar-risk-gating honest that token unlock calendar data is NOT in CryptoDataAPI.


## 2026-07-19 — Batch B7: 5 New Combination Strategy Pages

- Pages created (5):
  - [[funding-window-timing]] — funding carry × session/time filter: peri-settlement timing overlay; enters 40–50 min before 8h CEX funding settlements (00:00/08:00/16:00 UTC) or 10–15 min before Hyperliquid hourly settlements when |funding| ≥ 0.015%/8h, OI ≥ 60th percentile of trailing 30d, and no cascade in progress (1h liq volume < 2× 7d avg); captures pre-settlement repositioning drift from large participants positioning on the receiving side of the payment; exits 5–15 min post-settlement; stop at 0.8% adverse; HL hourly variant (0.5% of portfolio, 10–15 min window) is a smaller, more frequent, less-crowded complement; explicitly differentiated from hl-vs-cex-funding-divergence (rate spread not settlement timing), funding-skewed-grid (continuous centre adjustment), funding-rate-harvest (multi-period carry not peri-settlement scalp), and session-overlap-momentum (geographic session, not funding timestamp)
  - [[grid-with-tail-hedge]] — grid/market-making × tail-hedge overlay: OTM put budgeted from grid income; budget = min(20% of trailing 14d net grid P&L, 0.8% of grid notional); buy 10–15% OTM put, DTE 21–35, only when DVOL ≤ 70th pct 52w; grid halts on ADX > 25 or 12h OI change > +3% (mirrors oi-aware-grid runtime check); put payoff provides partial offset in gap-through-the-ladder event; stop at 22% combined drawdown; income-financing pattern adapted from carry-with-tail-hedge; explicitly differentiated from regime-gated-grid, oi-aware-grid, funding-skewed-grid (gate WHEN/HOW the grid runs — this caps the loss WHEN those gates fail or fire late)
  - [[sentiment-positioning-divergence]] — sentiment × funding filter: "talk vs money"; two setups: (1) washout long (all three gates): Fear & Greed ≤ 20 for ≥ 2 days AND funding ≤ −0.005%/8h AND L/S ≤ 0.90 AND at least one higher low on daily — longs have been flushed, shorts paying carry, stated panic coincides with actual washout; 3% of portfolio, 1.5× leverage, stop = new 10d low, exit when F&G ≥ 45 AND funding ≥ +0.01%/8h; (2) incomplete-cap avoidance/short (Fear & Greed ≤ 20 AND funding ≥ +0.010%/8h AND L/S ≥ 1.10): stated panic but longs still paying — do NOT enter long; explicitly differentiated from contrarian-extremes (sentiment alone), crowded-short-funding-fade (positioning alone), funding-flush-reversal (single-signal funding extreme), and smart-money-vs-crowd-divergence (on-chain vs positioning, not stated sentiment vs positioning)
  - [[long-options-trend-expression]] — vol buying/tail hedge × trend gate: express confirmed trends via long calls or call spreads on Deribit instead of futures when IV is cheap; trend gate (uptrend): daily close ≥ 12% above EMA50 + 4h RSI ≥ 58 in ≥ 3/5 bars + 7d avg funding ≥ 0.015%/8h; IV-cheap gate: DVOL ≤ 90% of 30d avg OR 20d RV ≥ DVOL + 5 vol pts OR DVOL ≤ 40th pct 52w; instrument: 10–15% OTM call or call spread, DTE 35–55, DTE-time-exit at DTE-7; budget 2% of portfolio; eliminates stop-wicking failure mode (option cannot be stopped out by spike vs trend); profit exit at 2× premium; explicitly differentiated from trend-following-cta (futures + stop), vol-targeted-trend-following (size scaling not instrument switch), event-vol-buying (calendar-driven straddle), and trend-aligned-premium-selling (sells options when IV elevated — structural complement: sell when rich, buy when cheap)
  - [[cross-venue-cascade-dislocation]] — liquidation plays × cross-venue: HL-Binance BTC perp price spread ≥ 0.5% during cascade (1h liq volume ≥ 3× 7d avg); enter long HL (dislocated) + short Binance (reference), equal notional 2.5% per leg; exit on spread ≤ 0.1% (reconvergence) or 15-min time limit; stop if spread widens to ≥ 1.5%; emergency close if one leg fills but other doesn't within 30s; edge: HL HLP vault architecture creates mechanical price dislocation vs Binance mark-price system during concentrated liquidation; explicitly differentiated from liquidation-cascade-arbitrage (DeFi MEV on-chain bonus — entirely different mechanism), hl-vs-cex-funding-divergence (steady-state funding spread not cascade price gap), and cross-exchange-arbitrage (continuous normal-market arb not event-triggered)
- Pages updated (2):
  - [[combination-matrix]] — 5 new cells linked: funding carry × session/time ([[funding-window-timing]] with footnote ¹⁷), liquidation plays × cross-venue ([[cross-venue-cascade-dislocation]] with footnote ¹⁸), vol buying × trend gate ([[long-options-trend-expression]] with footnote ¹⁹), grid × tail-hedge ([[grid-with-tail-hedge]] with footnote ²⁰), sentiment × funding filter ([[sentiment-positioning-divergence]] with footnote ²¹); 1 backup cell resolved: mean-reversion × trend gate → [[pullback-trading]] ²² (higher-timeframe-reversion-gate backup confirmed already covered); counts updated (existing: 47→53, planned: 44→38); footnotes ¹⁷–²² added; Batch B7 section prepended
  - [[log]] (this file) — Batch B7 entry prepended
- Candidates skipped (0 of 5 primaries): all five primaries confirmed additive. No backups deployed.
- Backup evaluation: `higher-timeframe-reversion-gate` (mean-reversion × trend gate backup) confirmed covered by [[pullback-trading]] and [[trend-pullback-rally-fade]] — both document HTF-trend-gated mean-reversion entries. Matrix cell updated to reference [[pullback-trading]]. `vol-balanced-pairs` (stat-arb × vol targeting) remains planned.
- All 5 new strategy pages: type=strategy, strategy_type=hybrid, markets=[crypto], backtest_status=untested, full 16-section structure (lead with explicit differentiation from nearest neighbors + Edge source + Why this edge exists + Null hypothesis + Rules + Pseudocode + Indicators + Example trade with concrete illustrative round-trip numbers + Performance + Capacity + What kills it + Kill criteria + Advantages + Disadvantages + Sources + Getting the Data (CryptoDataAPI) + Related); verified CryptoDataAPI endpoints only (funding-rates, hyperliquid/funding-rates, open-interest, liquidations, long-short-ratio, fear-greed, dvol-history, klines, binance/summary, mark-price, regimes/current); honest about Deribit options API requirement (grid-with-tail-hedge, long-options-trend-expression); approved tags only.


## 2026-07-19 — Batch B6: 5 New Combination Strategy Pages

- Pages created (5):
  - [[put-protected-dip-buying]] — mean-reversion × tail-hedge overlay: post-capitulation dip-buy (spot or perp long) entered simultaneously with a 15–20% OTM protective put on Deribit; the put converts the infinite-downside stop into a contractual floor that cannot gap through; entry trigger is any of three capitulation methods (funding-flush [funding < −0.02%/8h for 24h], OI-flush [OI −15% from 5d peak], or on-chain+sentiment [whale spike + Fear & Greed ≤ 20]); put capped at 2.5% of notional; max loss = floor width + put premium; explicitly differentiated from leverage-stress-tail-hedge (pre-crash put accumulation without simultaneous long) and cascade-monetization-rotation (lifecycle rotation structure)
  - [[oi-aware-grid]] — grid/market-making × OI filter: grid paused when 12h OI change ≥ +5% OR 24h change ≥ +8% (rapid OI accumulation signals directional leverage entering = breakout fuel); grid resumes after OI stabilises below +3%/12h for 6 consecutive hours (minimum 12h pause); leading-indicator gate that fires 4–24 hours before the breakout vs regime-gated-grid's lagging ADX/ATR indicators; also gated on flat funding [−0.03%, +0.05%/8h] and ADX ≤ 25 for normal run conditions
  - [[narrative-position-vol-targeting]] — narrative/event × vol targeting: each narrative/memecoin position sized to a fixed 1%-of-portfolio daily-vol risk budget (notional = budget / daily_vol); 5% single-position cap; 25% portfolio notional heat cap and 2.5% aggregate daily-vol cap across concurrent narrative positions; vol-targeted stop = 2.5× daily risk budget below entry; explicitly differentiated from vol-targeted-trend-following (large-cap BTC/ETH trend book) — this page targets the high-vol-dispersion narrative sub-book (RV range 80%–500%+ annualised)
  - [[smart-money-vs-crowd-divergence]] — on-chain flow × funding filter: long entry requiring all five simultaneous gates: whale score ≥ 65 (accumulating); 24h exchange outflow top-quartile OR 7d net outflow; funding ≤ 0.00%/8h; long/short ≤ 0.95; at least one higher low on daily (no consecutive lower lows); exit when funding ≥ +0.02% AND L/S ≥ 1.05, or whale score drops below 50 for 2 days; explicitly differentiated from smart-money-orderflow-combo (order-flow second leg, intraday) and crowded-short-funding-fade (positioning alone, no on-chain gate)
  - [[low-leverage-vol-selling]] — vol selling × OI filter: sell BTC strangle (25d put + 15d call) ONLY when OI/MC ≤ 2.0% (no leverage) AND funding flat [−0.01%, +0.02%/8h] AND long/short balanced [0.90–1.20] AND DVOL ≥ 45th percentile AND IV−RV ≥ 5 vol pts; live OI/MC monitoring — exit if OI/MC rises above 2.8% while position open (leverage rebuilding); structural inverse of leverage-stress-tail-hedge; fourth distinct vol-selling entry regime: leverage-ABSENCE gate
- Pages updated (2):
  - [[combination-matrix]] — 5 new cells linked: mean-reversion × tail-hedge overlay ([[put-protected-dip-buying]] with footnote ¹⁴), grid × OI filter ([[oi-aware-grid]]), narrative × vol targeting ([[narrative-position-vol-targeting]]), vol selling × OI filter ([[low-leverage-vol-selling]] with footnote ¹⁵), on-chain flow × funding filter ([[smart-money-vs-crowd-divergence]] with footnote ¹⁶); counts updated (existing: 42→47, planned: 49→44); footnotes ¹⁴–¹⁶ added; Batch B6 section prepended
  - [[log]] (this file) — Batch B6 entry prepended
- Candidates skipped (0 of 5 primaries): all five primary candidates confirmed additive. No backups used.
- Vol-selling differentiation note: [[low-leverage-vol-selling]] (vol selling × OI filter) is explicitly differentiated in its lead from all three prior vol-selling combos: funding-conditioned-vol-selling (HIGH funding), post-panic-vol-selling (post-event fear extreme), and trend-aligned-premium-selling (trend-selected wing). The four vol-selling combos now cover four distinct entry regimes: leverage-absent, leverage-crowded-long, post-crash-fear, and trend-selected.
- All 5 new strategy pages: type=strategy, strategy_type=hybrid, markets=[crypto], backtest_status=untested, full 16-section structure (lead with explicit differentiation from nearest neighbors + Edge source + Why this edge exists + Null hypothesis + Rules + Pseudocode + Indicators + Example trade with concrete illustrative round-trip numbers + Performance + Capacity + What kills it + Kill criteria + Advantages + Disadvantages + Sources + Getting the Data (CryptoDataAPI) + Related), verified CryptoDataAPI endpoints only (open-interest, funding-rates, long-short-ratio, whale-score, exchange-flows, dvol-history, klines, liquidations, sentiment, regimes/current), honest about Deribit options API requirement (put-protected-dip-buying and low-leverage-vol-selling), approved tags only.


## 2026-07-19 — Batch B5: 5 New Combination Strategy Pages

- Pages created (5):
  - [[trend-aware-carry]] — funding carry × trend gate: carry book (short perp / long spot) that scales to 60% then 30% deployment when a strong uptrend is confirmed (BTC ≥ 15% above SMA20, 4h RSI ≥ 70, 7d funding ≥ 0.05%/8h); reduces exposure to funding-flush and basis-blowout risk without paying option-premium costs; re-enters in tranches over 3 days after trend normalises; explicitly differentiated from carry-with-tail-hedge (permanent hedge overlay, not a sizing throttle)
  - [[post-panic-vol-selling]] — vol selling × sentiment-extreme filter: enter short-vol (sell 25-delta BTC put) only after a panic spike when all five stabilisation gates pass simultaneously (Fear & Greed ≤ 20 for 2 days; DVOL ≥ 85th percentile AND +20 vol-pt spike from 5d ago; 24h RV rolling over from ≥ 80 vol-pt peak; 12h liquidation volume < 1.5× 7d avg; no new 7-day low in last 4h candle); harvests the fear-premium mean-reversion post-stabilisation; explicitly differentiated from funding-conditioned-vol-selling (fires on pre-crash bullish crowding, not post-crash fear)
  - [[cascade-monetization-rotation]] — liquidation plays × tail-hedge overlay: two-leg lifecycle strategy: accumulate 10-delta OTM puts during stress build-up using leverage-stress-tail-hedge entry rules; monetise when cascade fires (≥12% price drop OR DVOL +25pts with $500M+ 6h liquidations); rotate 60% of gross payoff into cascade-fade perp long within 4 hours when CVD is flattening, liquidation decelerating, and price ≥ 10% below pre-cascade level; the combination is the capital rotation (fade capital comes from tail-hedge payoff, not additional committed capital)
  - [[unlock-pair-hedge]] — stat-arb/pairs × unlock/event calendar: beta-hedged long-short pair expressing token cliff unlock shorts (≥ 3% of circulating supply) as short-unlocking-token perp / long-sector-peer perp at hedge ratio = 1/beta; strips BTC/sector beta to isolate idiosyncratic supply-shock component; enter 6 days before unlock, exit 10 days post-unlock; explicitly differentiated from unlock-short-with-crowding-gate (outright directional short with crowding filter — not beta-neutral)
  - [[trend-aligned-premium-selling]] — vol selling × trend gate: sell puts in confirmed uptrends (price ≥ 10% above SMA20, 4h RSI ≥ 60, funding ≥ 0.02%/8h), sell calls in confirmed downtrends (≥ 8% below SMA20, RSI ≤ 45, funding ≤ 0); trend selects which wing to sell rather than whether to sell; DVOL ≥ 50th percentile also required; explicitly differentiated from funding-conditioned-vol-selling (funding crowding trigger in any regime direction) and post-panic-vol-selling (post-crash fear trigger)
- Pages updated (2):
  - [[combination-matrix]] — 5 new cells linked: funding carry × trend gate ([[trend-aware-carry]]), vol selling × sentiment-extreme filter ([[post-panic-vol-selling]]), liquidation plays × tail-hedge overlay ([[cascade-monetization-rotation]] with footnote ¹³), stat-arb/pairs × unlock/event calendar ([[unlock-pair-hedge]]), vol selling × trend gate ([[trend-aligned-premium-selling]]); counts updated (existing: 37→42, planned: 54→49); footnote ¹³ added; Batch B5 section prepended
  - [[log]] (this file) — Batch B5 entry prepended
- Candidates skipped (0 of 5 primaries): all five primary candidates confirmed additive. No backups used.
- Vol-selling differentiation: [[post-panic-vol-selling]] (vol selling × sentiment-extreme) and [[trend-aligned-premium-selling]] (vol selling × trend gate) are in distinct cells; their leads explicitly differentiate from each other and from [[funding-conditioned-vol-selling]].
- All 5 new strategy pages: type=strategy, strategy_type=hybrid, markets=[crypto], backtest_status=untested, full 16-section structure (lead with explicit differentiation from nearest neighbors + Edge source + Why this edge exists + Null hypothesis + Rules + Pseudocode + Indicators + Example trade with concrete illustrative round-trip numbers + Performance + Capacity + What kills it + Kill criteria + Advantages + Disadvantages + Sources + Getting the Data (CryptoDataAPI) + Related), verified CryptoDataAPI endpoints only (klines, funding-rates, open-interest, dvol-history, liquidations, long-short-ratio, fear-greed-index, regimes/current), honest about Deribit options API requirement (consistent with all B3-B4 vol pages), approved tags only.


## 2026-07-19 — Batch B4: 5 New Combination Strategy Pages

- Pages created (5):
  - [[correlation-regime-pairs]] — stat-arb/pairs × regime gate: pairs/stat-arb book operated only while the pair's cointegrating relationship is demonstrably active (rolling 30d correlation ≥ 0.70, ADF cointegration p ≤ 0.10, OU half-life 3–45 days); flatten immediately on correlation breakdown below 0.60 rather than averaging into a structurally broken spread; composable with pairs-with-funding-differential's funding-differential gate as a second layer
  - [[event-vol-buying]] — vol buying × unlock/event calendar: buy ATM straddles or OTM strangles on Deribit ahead of scheduled binary-outcome catalysts (Bitcoin halvings, SEC ETF decision deadlines, major Ethereum hard forks, significant token unlocks, regulatory votes) when ATM IV on the catalyst expiry is within 10% of its 30-day trailing DVOL average (event not yet priced); exit on +20 vol-point IV expansion or within 48h post-event; the long-side event counterpart to funding-conditioned-vol-selling
  - [[session-aware-mean-reversion]] — mean-reversion × session/time filter: RSI/VWAP/Bollinger-band mean-reversion with session-conditional parameter table (peak / Asia-overnight / weekend / session-transition); lower RSI threshold and lower VWAP deviation required in thin sessions; session-open transition windows (+0.2× size bonus); explicitly NOT a cascade strategy (that is off-hours-liquidation-playbook); the routine daily drift-and-revert that occurs without liquidation spikes
  - [[leverage-stress-tail-hedge]] — vol buying/tail hedge × OI filter: standalone OTM put accumulation strategy (no carrier book) triggered when all three leverage-stress gates are simultaneously elevated (BTC OI/market-cap ≥ 3.0%, 7d-average 8h funding ≥ 0.04%, long/short ratio ≥ 1.8); exit on crash payoff (≥12% price drop), DVOL expansion (+25 vol points), or stress deactivation; differentiated from carry-with-tail-hedge (hedge secondary to a carry book) and convex-tail-hedge-arbitrage (vol-cheapness triggered)
  - [[spot-led-momentum-filter]] — momentum × cross-venue: momentum entries conditioned on three simultaneous cross-venue flow-origin signals (Coinbase premium ≥ 0.05% sustained ≥ 2 of 3 hours; 8h funding ≤ 0.03%; spot volume ≥ 1.2× 7d avg AND OI 3d growth ≤ 15%); spot-led moves reflect real capital inflow; perp-led moves are leverage that mean-reverts; differentiated from funding-filtered-momentum which gates on funding LEVEL, not flow ORIGIN
- Pages updated (2):
  - [[combination-matrix]] — 5 new cells linked (stat-arb × regime gate, vol buying × event calendar, mean-reversion × session filter, vol buying × OI filter, momentum × cross-venue); session-aware-mean-reversion also placed in momentum × session filter cell (footnote ¹² added); counts updated (existing: 32→37, planned: 59→54); footnote ¹² added; Batch B4 section prepended
  - [[log]] (this file) — Batch B4 entry prepended
- Candidates skipped (0 of 5 primaries): all five primary candidates confirmed additive. spot-led-momentum-filter assessed against funding-filtered-momentum and confirmed distinct (flow origin vs funding level). No backups used.
- All 5 new strategy pages: type=strategy, strategy_type=hybrid, markets=[crypto], backtest_status=untested, full 16-section structure (lead with explicit differentiation from nearest neighbors + Edge source + Why this edge exists + Null hypothesis + Rules + Pseudocode + Indicators + Example trade with concrete illustrative round-trip numbers + Performance + Capacity + What kills it + Kill criteria + Advantages + Disadvantages + Sources + Getting the Data (CryptoDataAPI) + Related), honest about Deribit options API requirement (consistent with funding-conditioned-vol-selling), verified CryptoDataAPI endpoints only (coinbase-premium, funding-rates, open-interest, dvol-history, klines, liquidations, long-short-ratio, regimes/current), approved tags only.


## 2026-07-19 — Batch B3: 5 New Combination Strategy Pages

- Pages created (5):
  - [[funding-vs-basis-rotation]] — basis/cash-and-carry × funding filter: allocation-layer strategy that switches the carry book between perp-funding carry (long spot, short perp) and dated-futures basis carry (long spot, short quarterly) depending on which annualised yield is higher net of costs; hysteresis prevents churn; always market-neutral and always earning the fatter of the two available carry streams
  - [[funding-conditioned-vol-selling]] — vol selling × funding filter: sell BTC/ETH options on Deribit only when perp funding is elevated (≥ 0.03%/8h confirming a leveraged-retail crowd driving IV richness) AND DVOL percentile is in the 40th–90th range AND IV−RV > 5 vol points; funding adds information beyond the DVOL-percentile gate by identifying *why* the surface is rich (leverage-crowd demand vs. genuine macro uncertainty); call-wing tilt when funding ≥ 0.05%/8h
  - [[off-hours-liquidation-playbook]] — liquidation plays × session/time filter: session-conditional extension of the cascade-fade strategy; applies different entry thresholds, minimum cascade sizes, position-size multipliers, target reversion ranges, and slippage budgets depending on session window (US/EU peak, Asia/overnight, weekend); off-hours cascades travel further per dollar of forced flow in thin books — the session layer concentrates risk where the reversion edge is amplified
  - [[narrative-with-trend-confirmation]] — narrative/event × trend gate: enter narrative/theme trades only after price structure confirms (20-day channel high breakout or higher-low above 50-day SMA), avoiding the pioneer-penalty regime where a correct narrative precedes the capital flow by weeks; dual-exit discipline (narrative decay OR trend break, whichever fires first) prevents sitting through secondary distribution
  - [[onchain-capitulation-confluence]] — on-chain flow × sentiment-extreme filter: bottom-fishing entry for BTC that requires BOTH an on-chain capitulation signal (exchange-inflow top-decile spike, SOPR ≤ 0.97 for 5+ days, or MVRV-Z ≤ 0) AND Fear & Greed ≤ 20 for 2+ consecutive days; the dual-signal confluence addresses the two failure modes of single-signal bottom fishing — fear without on-chain selling (correction, not bottom) and on-chain selling without sentiment extreme (distribution, not capitulation)
- Pages updated (2):
  - [[combination-matrix]] — 5 new cells linked (basis × funding filter, vol selling × funding filter, liquidation plays × session filter, narrative × trend gate, on-chain flow × sentiment filter); counts updated (existing: 27→32, planned: 64→59); footnote ¹¹ added; Batch B3 section prepended
  - [[log]] (this file) — Batch B3 entry prepended
- Candidates skipped (0 of 5 primaries): all five primary candidates confirmed additive. The two backup candidates (correlation-regime-pairs, session-aware-mean-reversion) were not needed.
- All 5 new strategy pages: type=strategy, strategy_type=hybrid, markets=[crypto], backtest_status=untested, full 16-section structure (lead with explicit differentiation from nearest neighbors + Edge source + Why this edge exists + Null hypothesis + Rules + Pseudocode + Indicators + Example trade with concrete round-trip numbers + Performance + Capacity + What kills it + Kill criteria + Advantages + Disadvantages + Sources + Getting the Data (CryptoDataAPI) + Related), verified CryptoDataAPI endpoints only (no invented paths), honest about DVOL/SOPR gaps requiring external sources, kill criteria with numeric triggers, approved tags only.


## 2026-07-19 — Batch B2: 5 New Combination Strategy Pages

- Pages created (5):
  - [[pairs-with-funding-differential]] — stat-arb/pairs × funding filter: perp-expressed pairs where the funding differential between legs agrees with the spread z-score direction; earns both mean-reversion of the spread and structural carry for being on the non-crowded leg
  - [[funding-flush-reversal]] — mean-reversion × funding filter: dip-buy only after funding has sustained below −0.02%/8h for 24h+, confirming leveraged-long deleveraging is complete and shorts are now the crowded, carry-paying party
  - [[unlock-aware-momentum]] — momentum × unlock/event calendar: momentum book that freezes new longs 5 days before and closes all longs 2 days before cliff unlock events, re-entering after supply digestion with post-unlock momentum re-confirmation
  - [[funding-skewed-grid]] — grid/market-making × funding filter: perp grid whose inventory allocation is biased toward the funding-receiver side (earn both spread and carry simultaneously); skew rebalances when funding direction flips
  - [[oi-flush-reversion]] — mean-reversion × OI filter: dip-buy only after OI has declined ≥ 15% from its 5-day peak, confirming leveraged deleveraging is substantially complete before entering the mean-reversion long
- Pages updated (2):
  - [[combination-matrix]] — 5 new cells linked (mean-reversion × funding filter, mean-reversion × OI filter, momentum × unlock/event calendar, grid × funding filter, stat-arb × funding filter); cell counts updated (existing: 22→27, planned: 69→64); Batch B2 section added
  - [[log]] (this file) — Batch B2 entry prepended
- Candidates skipped (0 of 5 primaries): all five primary candidates were confirmed additive (no existing page covered the same combination × primitive pair)
- All 5 new strategy pages: type=strategy, strategy_type=hybrid, markets=[crypto], backtest_status=untested, full 16-section structure (lead + Edge source + Why this edge + Null hypothesis + Rules + Pseudocode + Indicators + Example trade + Performance + Capacity + What kills it + Kill criteria + Advantages + Disadvantages + Sources + Getting the Data + Related), CryptoDataAPI endpoints verified against B1 exemplars, kill criteria with numeric triggers, differentiation sentences in lead paragraphs, approved tags only.


## 2026-07-18 — Batch B1: Combination Matrix + 5 New Combination Strategy Pages

- Pages created (7):
  - [[combination-matrix]] — primitive × overlay coverage matrix (22 existing, 69 planned, 9 non-viable cells)
  - [[combinations-overview]] — category overview with Dataview table and combination families
  - [[funding-filtered-momentum]] — momentum entries gated by non-consensus (flat/negative) funding
  - [[regime-gated-grid]] — grid trading activated only inside confirmed low-vol range regimes
  - [[carry-with-tail-hedge]] — funding carry book with budgeted OTM put overlay financed from carry income
  - [[unlock-short-with-crowding-gate]] — token unlock supply-event short filtered for non-crowded entry conditions
  - [[vol-targeted-trend-following]] — crypto-native trend following with volatility-targeted position sizing
- Pages updated (1):
  - [[strategies-overview]] — added [[combination-matrix]] link alongside [[combinations-overview]] in the Subcategories list
- Candidates skipped (3 of 8 assessed):
  - `onchain-confirmed-breakout` — high overlap with [[on-chain-flow-trading]] and [[smart-money-orderflow-combo]]; noted in matrix
  - `sentiment-regime-rotation` — high overlap with [[contrarian-extremes]], [[crypto-beta-rotation]], [[regime-adaptive-strategy]]; noted in matrix
  - `pairs-with-funding-differential` — partial overlap with [[pairs-trading]] and [[hl-vs-cex-funding-divergence]]; deferred to next batch
- All 5 new strategy pages: type=strategy, strategy_type=hybrid, markets=[crypto], backtest_status=untested, full 16-section structure, CryptoDataAPI data section with verified endpoints only, kill criteria, wikilinks to primitives and neighbors.


## 2026-07-16 12:47 — Batch Import: Top 2376 Cryptocurrencies (CoinGecko)

- Source: [[coingecko-top-1000-2026-07-16]]
- Type: data (API batch import)
- Pages created (1339): [[united-stables]], [[spiko-amundi-overnight-swap-fund-eur]], [[pudgy-penguins]], [[peanut-2-2]], [[coco-2]], [[spark-usdc]], [[tradable-apac-diversified-finance-provider-sstn]], [[lido-earn-eth]], [[safo]], [[tradable-latam-fintech-sstn]], [[alpha-bulgaria-warrants]], [[genius-3]], [[tradable-na-third-party-online-merchant-sstn]], [[manadia]], [[tradable-latam-middle-market-lender-sstl]], [[tradable-latam-middle-market-lender-sstl]], [[nexus-4]], [[saturn-dollar]], [[tradable-singapore-fintech-ssl]], [[cash-cat]] ... and 1319 more
- Pages merged (1037): [[bitcoin]], [[ethereum]], [[usdt]], [[bnb]], [[usdc]], [[xrp]], [[solana]], [[tron]], [[figure-heloc]], [[hype]] ... and 1027 more
- Data points per coin: 20 (metadata, market data, tokenomics, social, developer, exchange listings)
- Confidence: HIGH (official CoinGecko API data)

## 2026-07-14 — Second-tier options/quant/charting crypto re-scope (Wave 4)

Re-scoped ~56 more crypto-relevant pages from equity framing to crypto (9 parallel Opus agents), finishing the technique/structure upgrade the user requested. Options spreads & structures (bull/bear verticals, credit/calendar/ratio spreads, straddles/strangles, 0DTE, cash-secured puts, long-call/put, put-call parity) → crypto structure theory on Deribit. Vol strategies (premium-selling, long/short-vol, tail hedges, and the VIX pages reframed to DVOL — honestly flagging crypto has no tradeable VIX-future/ETP analog). Crypto-applicable quant (mean-reversion, pairs, stat-arb, Ornstein-Uhlenbeck, Kalman, Bollinger-reversion, regime-detection) rebuilt to the buildable schema (all `untested`, Sharpes revised down for crypto). Price-action methods (gap/pullback/London-breakout = strategies; ICT/SMC/triple-screen = concept frameworks). Duplicate stubs redirected (vertical-spreads, iron-condors, calendar-spread root, cash-secured-put, delta-hedging/gamma-scalping strategy copies). Created [[dvol]] (Deribit Volatility Index) for 16 inbound links; stripped stray equity tags from ~60 already-crypto pages; redirected iron-fly→iron-butterfly.

Deliberately LEFT as intentional cross-asset reference (not gaps): the historical/TradFi arbitrage encyclopedia (gold-point, medieval bills, treasury/currency/commodity-basis arbs) and TradFi portfolio theory (Black-Litterman, CPPI, factor-investing) — already-thorough theory pages that are cross-asset by design.

## 2026-07-14 — Technique & options-structure theory upgrade (Wave 3)

Upgraded ~58 charting-technique and options-structure pages from thin/equity-framed essays into comprehensive, crypto-scoped theory pages (9 parallel agents). Charting theories (Elliott wave, Fibonacci, Gann, harmonic patterns, Ichimoku, Heikin-Ashi, Renko, point-and-figure, Darvas, Supertrend, Parabolic SAR, supply-demand, breakout, Donchian, volatility-arb) re-typed `strategy`→`concept` with full method coverage. Options structures (iron-condor family, straddles/strangles, spreads, covered/protective/wheel) rewritten to a structure template (construction, payoff, greeks, adjustments, crypto specifics) and re-scoped from `[stocks]`/SPY to crypto/Deribit. Options-theory concepts (Black-Scholes, delta/vega hedging, IV-crush, moneyness, selection frameworks) given crypto grounding. No buildable-alpha schema was bolted onto theory/structure pages. Several duplicate stubs redirected (long-straddle, covered-calls, collar-strategy, protective-puts, concepts/options iron-butterfly + gamma-scalping). All endpoints verified; zero new dangling links.

## 2026-07-14 — Depth-parity rewrites (Wave 2)

Rewrote 24 crypto-native strategy essays from descriptive prose into the buildable strategy schema (full frontmatter + 16-section structure + realistic cost overlays + `## Getting the Data (CryptoDataAPI)`), matching the funding-rate-arbitrage gold standard. Buildable strategy pages rose 215 → 251. Scope drift (equity/commodity tags) removed from latency-arbitrage, calendar-spread-arbitrage, cash-and-carry.

- algorithmic: [[basis-trading]], [[restaking-strategies]], [[points-farming]], [[airdrop-farming]], [[liquidity-sniping]], [[synthetic-asset-trading]], [[intent-based-trading]], [[nft-trading]]
- combinations: [[delta-neutral-yield-farming]], [[crypto-yield-stack]], [[smart-money-orderflow-combo]]
- quantitative: [[sentiment-trading]], [[momentum-rotation]], [[skew-trading]], [[garch-volatility]]
- day-trading: [[order-flow-scalping]], [[scalping]], [[vwap-trading]]
- arbitrage: [[cross-exchange-arbitrage]], [[flash-loan-arbitrage]], [[latency-arbitrage]], [[staking-yield-arbitrage]], [[calendar-spread-arbitrage]], [[cash-and-carry]]
- also created concept pages [[coinbase-premium]] and [[participation-rate]] (filled inbound forward-links).

## 2026-07-14 — Strategy-creation gap-fill (Wave 1)

Filled the value-bearing gaps from the 2026-07-14 strategy-creation gap analysis (see [[coverage-gaps]]): 34 new pages + 5 essay→buildable rewrites + crypto sections on 6 existing pages, authored by 7 parallel agents. Adds the front-of-funnel methodology (idea generation, feature/signal engineering, ML labeling), crypto-specific backtest validation, missing archetypes (on-chain market-making, LVR, crypto options), execution/sizing, and live-ops runbooks. All new/rewritten pages carry the buildable schema and `## Getting the Data (CryptoDataAPI)` sections using only verified endpoints. Sub-clusters below.

### Crypto options, ETF-flow, cycle-timing & beta-rotation strategy cluster

Authored five new crypto strategy pages, each on the full buildable strategy schema (complete frontmatter + 16-section structure + realistic fees/funding/slippage/borrow cost overlay, never a naive backtest), with a `## Getting the Data (CryptoDataAPI)` section using only verified endpoints.

- Pages created:
  - [[crypto-options-volatility-selling]] — selling BTC/ETH vol on Deribit; DVOL-percentile regime gating, inverse vs linear (USDC) settlement, perp-driven skew, no §1256 shelter, strangles/iron-condors sized by DVOL, delta-hedge cadence, vol-shock kill switches (2020-03/LUNA/FTX/2025-10-10) (strategies/quantitative)
  - [[crypto-options-dispersion]] — index (BTC/ETH-major) vs single-name implied-vol dispersion; correlation mean-reversion; Deribit/venue constraints on alt-option liquidity (strategies/quantitative)
  - [[etf-flow-directional]] — trade spot BTC/ETH ETF NET FLOW directionally (flow-momentum, z-score sizing, flow-reversal exit); explicitly distinguished from the [[etf-arbitrage|NAV arb]] (strategies)
  - [[bitcoin-halving-cycle-timing]] — cycle top/bottom timing via [[mvrv]]/[[mvrv-z-score]]/[[nupl]]/[[realized-price]] bands + months-since-halving overlay; accumulation vs distribution zones; long-horizon sizing (strategies/position-trading)
  - [[crypto-beta-rotation]] — crypto-beta vs DXY/Nasdaq risk-on/off regime rotation; de-beta/hedge when [[crypto-macro-correlation-regime|correlation regime]] + DXY trend flip risk-off (strategies/quantitative)
- Endpoints used (all verified): market-intelligence (options/max-pain, etf/{asset}/flows, etf/btc/aum, coinbase-premium, exchange-balance, btc/cycle-indicators, fear-greed-history, liquidations), volatility/regime(+score,+/{symbol}), quant/gex + quant/market, on-chain (dormancy/btc, score, miners/hash-ribbon, whale-score, exchange-flows), regimes/current, policy/regime, liquidity/regime, sentiment/macro, derivatives/funding-rates, market-data/klines + btc-price-history, backtesting/klines. DVOL/IV surface sourced from [[deribit]]/[[greeks-live]] (noted as non-CDA).

### AMM LP economics & market-making cluster

Authored one new concept page and one new strategy page, and rewrote three existing essay-style strategy pages to the full buildable strategy schema (16 sections + strategy frontmatter).

- Pages created:
  - [[loss-versus-rebalancing]] — the LVR framework: LP vs the arbitrageur, LVR vs impermanent loss (path-dependence), markout as the empirical estimator, why LVR is the dominant modern lens on AMM LP profitability, the "hedging removes IL variance but not LVR" insight, CL implications, and LVR-mitigation AMM designs (am-AMM, CoW/FM-AMM, Diamond, dynamic fees, v4 hooks). Populates the near-empty concepts/defi folder. (concepts/defi)
  - [[hyperliquid-market-making]] — be-the-maker on the Hyperliquid on-chain CLOB: two-sided quoting, Avellaneda-Stoikov inventory skew (parameterized with concrete BTC numbers), maker rebates/fee tiers, adverse-selection/markout management, hourly funding exposure of inventory, HLP competitive context, toxic-flow & inventory-blowout kill criteria. Native counterpart to the perps corpus. (strategies/quantitative)
- Pages rewritten (same filenames, restructured to buildable schema):
  - [[concentrated-liquidity]] — Uniswap v3/v4 CL LP as buildable strategy: vol-sized tick-range selection, rebalance triggers, fee-APR vs IL/LVR math, LVR-aware delta-hedge overlay (`delta = x(p)`), links [[loss-versus-rebalancing]], kill criteria. (strategies/algorithmic)
  - [[jit-liquidity]] — mempool-triggered single-block LP spec: uninformed-flow filter, flash-loaned atomic mint→swap→burn bundle, economics gate (fee > gas + tip + single-swap LVR), JIT-resistance decay. (strategies/algorithmic)
  - [[market-making-strategy]] — re-scoped from stocks/forex to crypto CEX (Binance/Bybit); parameterized Avellaneda-Stoikov, thin-alt adverse-selection caveats, VIP/MM-program fee reality, 8h funding on inventory; complement to [[hyperliquid-market-making]]. (strategies/day-trading)
- All pages carry `## Getting the Data (CryptoDataAPI)` sections using only verified endpoints (volatility/regime, market-data & backtesting klines, hyperliquid l2-book/funding/candles, liquidity/depth, derivatives funding/OI, dex trending/token). HL fee schedule and LVR magnitudes verified against Hyperliquid docs and Milionis et al. (2022, arXiv:2208.06046).

### Live-ops infrastructure & buildable-strategy rewrites

Authored four infrastructure concept pages, one data-source page, and rewrote two algorithmic strategy essays to the buildable strategy schema (full frontmatter + 16-section structure + realistic cost overlay).

- Pages created:
  - [[paper-to-live-promotion]] — backtest→testnet→canary→scale promotion ladder with go/no-go gates and canary sizing (concept, `wiki/ai-trading/infrastructure/`)
  - [[bot-kill-switch-design]] — kill-switch/circuit-breaker design: trigger taxonomy, global-flatten vs per-strategy halt, auto vs manual, reduce-only unwind, distinguished from exchange circuit breakers (concept)
  - [[position-reconciliation]] — internal state vs exchange truth; partial fills, funding/fees, WebSocket gaps, restart recovery; reconciliation loop (concept)
  - [[exchange-api-key-security]] — permission scoping, withdrawal-disabled keys, IP allowlists, sub-accounts, HSM/Ed25519 secrets, rotation/revocation drills (concept)
  - [[proof-of-reserves]] — CEX PoR as counterparty-health monitoring signal; Merkle/zk-SNARK PoR, post-FTX context, no-liabilities gap, live-risk wiring (source)
- Pages rewritten (same filenames, buildable strategy schema):
  - [[mev-strategies]] — sandwich/backrun/JIT/DEX-arb each as a spec with infra (Flashbots/Jito, private mempools, priority fees) and gas/competition cost overlay
  - [[defi-yield-farming]] — APR decomposition (fees/emissions/incentives), IL/LVR, delta-hedge overlay, SC-risk-adjusted sizing, rotation and kill rules
- Getting the Data (CryptoDataAPI) sections added where data-mapped (verified endpoints only): backtesting/market-health, security/health, derivatives funding, dex + security, on-chain exchange-flows/reserves.

### Crypto execution & sizing cluster

Authored five new concept pages and one strategy page on crypto execution, perp sizing, and portfolio-level risk aggregation, and extended one existing page.

- Pages created:
  - [[cross-venue-execution-crypto]] — routing a directional order across Binance/Bybit/OKX/Hyperliquid by book depth, fee tier, and funding; depth-proportional allocation; explicitly not arbitrage (concepts/market-microstructure)
  - [[thin-market-execution]] — executing in illiquid alt books: child-order sizing to depth, participation-rate caps, self-impact avoidance, iceberg/TWAP, when not to trade (concepts/market-microstructure)
  - [[funding-aware-position-sizing]] — funding-adjusted Kelly for perps; carry-adjusted drift `μ_eff = μ ∓ φ`; sizing funding-positive vs funding-negative positions (concepts/risk-management)
  - [[liquidation-price-aware-sizing]] — sizing so liquidation sits beyond a 3σ / named-wick stress move; `L ≤ 1/(S+m+β)`; isolated vs cross; buffer & add-margin rules (concepts/risk-management)
  - [[crypto-portfolio-heat]] — aggregate BTC-beta exposure across nominally-different alt longs that converge to ~1.0 in a crash; beta-weighted heat budgeting (concepts/portfolio-theory)
  - [[multi-strategy-crypto-portfolio]] — perp-carry + momentum + on-chain + memecoin sleeves in one book; all-correlated-in-crisis, per-venue caps, stablecoin base, regime-based allocation; full buildable schema (strategies/combinations)
- Pages updated:
  - [[smart-order-routing]] — added "Crypto-Venue Routing" section linking [[cross-venue-execution-crypto]] and [[thin-market-execution]]; kept existing equities/SOR content (no de-scope)
- All new pages carry `## Getting the Data (CryptoDataAPI)` sections using only verified endpoints (liquidity/depth, derivatives & hyperliquid funding, volatility regime, market-data/backtesting klines, on-chain, dex, regimes).

### Crypto backtesting & idea-generation cluster

Authored six new pages and extended two existing ones, filling gaps in the strategy-development and backtesting sections.

- Pages created:
  - [[crypto-idea-generation]] — generative, inversion-based process for mining new crypto strategy hypotheses (strategy-development)
  - [[crypto-data-quality]] — GIGO checklist for crypto backtest data corruption (concepts/backtesting)
  - [[regime-conditional-validation]] — per-regime Sharpe attribution and regime-stratified holdouts across the 14 crypto regimes (concepts/backtesting)
  - [[crypto-short-history-statistical-power]] — tiny effective N, wide Sharpe CIs, MinTRL vs available history (concepts/backtesting)
  - [[crypto-forward-testing]] — testnet vs live-info shadow, champion-challenger, perp-metric reconciliation (concepts/backtesting)
  - [[probability-of-backtest-overfitting]] — PBO via CSCV, crypto framing; resolves an existing red link (concepts/backtesting)
- Pages updated:
  - [[wash-trading]] — added "Backtesting Data-Quality Impact" section (venues to distrust, signal corruption, detection heuristics)
  - [[cryptodataapi-backtesting]] — added "From Archive to Validated Strategy" subsection (survivorship-universe construction + CPCV/DSR/PBO handoff)
- All new pages carry `## Getting the Data (CryptoDataAPI)` sections using only verified endpoints (backtesting archive, quant point-in-time regime history, derivatives/on-chain/hyperliquid feeds).

## 2026-07-13 — Vault created

Vault scoped to crypto-trading ("AlgoBrain"). Removed stock-market entities, stock news, personal/persona pages, and off-scope equity content; retained crypto, blockchain, DeFi, trading, algorithms, markets, macro context, and general AI knowledge. Added CryptoDataAPI data-source documentation and per-page "Getting the Data (CryptoDataAPI)" sections.
