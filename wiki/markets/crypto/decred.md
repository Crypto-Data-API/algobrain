---
title: "Decred"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [altcoins, crypto, regulation, defi]
aliases: ["DCR", "Decred (DCR)"]
entity_type: protocol
founded: 2016
headquarters: "Decentralized"
website: "https://decred.org/"
related: ["[[binance]]", "[[bitcoin]]", "[[crypto-markets]]", "[[crypto-narratives-overview]]", "[[kraken]]", "[[event-driven-trading]]", "[[dca-strategy]]"]
---

# Decred

**Decred** (ticker **DCR**, its own Layer-1 [[blockchain]]) is a hybrid proof-of-work / proof-of-stake cryptocurrency launched in February 2016 that pioneered formal on-chain governance: stakeholders vote on consensus changes and direct a self-funded on-chain treasury via the **Politeia** proposal system. For traders it is one of the oldest "governance coin" plays still live — a fixed-supply (21M cap, mirroring [[bitcoin]]) asset whose price has historically reacted sharply to governance and treasury events rather than product launches.

---

## Market Data

| Metric | Value |
|---|---|
| **Market Cap Rank** | #178 |
| **Market Cap** | ~$201.3M |
| **Current Price** | $11.52 |
| **24h Volume** | ~$0.50M |
| **24h Change** | -0.12% |
| **7d Change** | -3.64% |
| **Circulating / Max Supply** | 17.47M / 21.00M DCR |
| **All-Time High** | $247.35 (2021-04-17) — **-95.35%** |
| **All-Time Low** | $0.43154 (2016-12-26) — **+2567%** |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

DCR has **faded hard from the early-2026 governance rally**: from ~$29–32 (≈$563M cap) at the March 2026 Politeia-vote peak, to $20.57 (#119) at the April snapshot, to **$11.52 (~$201M cap, #178) by 2026-06-20** — a textbook governance-catalyst pump-and-fade now ~95% below the 2021 ATH. Daily volume is thin (~$0.5M), so the **"Established Bear Market"** ([[crypto-fear-and-greed-index|Fear & Greed]] = 23) regime weighs heavily on this low-liquidity name. See [[market-regime]].

---

## Technology / Protocol

Decred aims to build a community-directed digital currency whose security, adaptability, and sustainability make it a long-term store of value, governed as a decentralized autonomous organization.

Key structural features:

- **DCRDEX / Bison Wallet** — a native, non-custodial decentralized exchange for peer-to-peer **cross-chain atomic swaps** with no trading fees or KYC. Bison Wallet (the DCRDEX frontend expanded into a full multi-coin wallet) reached **1.0 in January 2026**.
- **StakeShuffle** — optional CoinShuffle++ privacy mixing at the wallet level.
- **Self-funded development** — a share of every block reward funds the on-chain treasury, which holds **>867,000 DCR** as of early 2026, removing dependence on external grants/VCs.

---

## PoW/PoS Hybrid Consensus & Governance

Decred's defining feature is its **hybrid consensus** and the on-chain governance it enables:

- **Hybrid PoW + PoS** — PoW miners (Blake-256, ASIC-mined) produce blocks, but **PoS ticket holders must vote to validate them**. A block is only confirmed once enough staked tickets approve it, so a 51% attack would require dominating *both* hash power and staked supply — far costlier than on pure-PoW chains.
- **Ticket voting** — holders lock DCR to buy **tickets**, which are randomly called to vote on (a) block validity and (b) governance proposals; ticket holders earn staking rewards.
- **Politeia** — the formal proposal-and-voting platform. Consensus changes (**DCPs**) require stakeholder supermajorities; treasury spending is also stakeholder-directed.
- **On-chain treasury** — funded from block rewards, deployed only by stakeholder vote — a genuinely self-governing DAO treasury.

This is the original "money + governance" design: holders are simultaneously the security backstop (via PoS tickets) and the electorate (via Politeia).

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | 17.47M DCR |
| **Total Supply** | 17.47M DCR |
| **Max Supply** | 21.00M DCR |
| **Fully Diluted Valuation** | ~$201.3M |
| **Market Cap / FDV Ratio** | ~0.83 |

DCR is **hard-capped at 21M**, mirroring [[bitcoin]]. ~17.47M (≈83%) is in circulation, with the remainder emitted via a smoothly declining block-reward schedule split across PoW miners, PoS voters, and the treasury. **Dilution flag:** the ~17% un-emitted supply releases gradually over many years (low, predictable inflation), so there is no unlock-cliff risk — but the slow emission plus a treasury that can sell DCR are mild structural sources of supply. MC/FDV ≈ 0.83 reflects coins not yet mined rather than locked insider allocations.

---

## Market Structure & Liquidity

- **Where it trades** — spot on [[binance|Binance]] (DCR/USDT), [[kraken|Kraken]] (DCR/USD), and KuCoin (DCR/USDT); natively on **DCRDEX** (peer-to-peer atomic swaps, no fees). **No major perp listing.**
- **Liquidity** — **thin** (~$0.5M daily volume against a ~$201M cap). Low float + no deep derivatives market means slippage is high; size accordingly. Thin liquidity amplifies both governance pumps and the subsequent fades (as the March→June 2026 round-trip showed).
- **Catalysts** — Politeia treasury proposals and DCP consensus votes drive most of DCR's volatility; the Jan 2026 DCP-0013 vote produced a ~75% weekly move. Watch treasury-spending decisions and DCRDEX volume growth.

### Exchange Listings

| Venue | Pair | Type |
|---|---|---|
| Binance | DCR/USDT | Spot (CEX) |
| Kraken | DCR/USD | Spot (CEX) |
| KuCoin | DCR/USDT | Spot (CEX) |
| DCRDEX (native) | Cross-chain pairs | Atomic swaps, no fees |

---

## Narrative & Category

DCR sits in the **"OG governance / sound-money alt"** basket: a fixed-supply, self-governing PoW/PoS chain with privacy tooling. It trades with the long-tail PoW/privacy cohort rather than with [[defi]] or AI baskets, and its catalysts are **endogenous governance events** (Politeia votes, treasury decisions) more than market-wide narratives. Categories: Layer 1, Privacy (StakeShuffle), On-chain Governance, Made in USA.

---

## Valuation Framing (qualitative)

DCR is best framed as a **governance + sound-money asset**, not a cash-flow protocol. Useful lenses: (1) **treasury value vs market cap** — a >867k DCR treasury (~$10M at $11.52, and a meaningful fraction of the ~$201M cap) provides a quasi-"book value" floor and self-funding runway; (2) **staking participation** (ticket pool size / % of supply locked) as a security and conviction gauge; (3) **DCRDEX volume** as the closest thing to product traction; (4) **governance optionality** — Politeia votes have repeatedly produced 50–75% short-term moves, so DCR carries embedded event-volatility. The bear read is that, fundamentally, DCR has limited usage outside governance and store-of-value framing, hence the deep drawdown.

---

## Peer Comparison

| Token | Category | Mkt Cap (rank) | Notes |
|---|---|---|---|
| **Decred (DCR)** | L1 / governance / privacy | ~$201.3M (#178) | Hybrid PoW+PoS, Politeia DAO, 21M cap |
| [[bitcoin\|Bitcoin (BTC)]] | L1 / store of value | huge | Shared 21M cap, pure PoW, no on-chain gov |
| Tezos (XTZ) | L1 / on-chain governance | mid-cap | Pure PoS, self-amending governance |
| Dash (DASH) | L1 / privacy / governance | small-cap | Masternode governance + treasury |
| Zcash (ZEC) | L1 / privacy | mid-cap | zk-SNARK privacy, pure PoW |

> *Peer market caps are category context; only DCR is from the 2026-06-20 snapshot.*

---

## Risks

- **Low liquidity** — ~$0.5M daily volume means high slippage and exaggerated pump/fade swings; hard to exit size.
- **Governance-event dependence** — price moves are driven by Politeia/DCP votes; between catalysts DCR drifts with the bear tape.
- **Drawdown depth** — **-95% from the 2021 ATH** ($247.35); a structurally weak long-tail name.
- **Narrative obsolescence** — "on-chain governance" is now common; Decred's first-mover edge has eroded versus newer L1s.
- **Treasury / emission supply** — slow block emission plus a treasury that can sell DCR are mild ongoing supply sources.
- **Established Bear Market backdrop** — Fear & Greed 23 / risk-off macro is especially punishing for thin, low-cap alts.

> *This page is informational, not investment advice. Figures are point-in-time snapshots and change continuously.*

---

## Major News & Events (2025–2026)

- **January 2026 — DCP-0013 approved with ~99.98% support** — stakeholders voted to cap monthly treasury spending at **4% of the treasury balance**, a fiscal-discipline rule for deploying the ~867k DCR war chest. The vote was a direct catalyst: DCR rallied ~75% in a week to ~$29–32 and a ~$563M cap by March 2026.
- **January 2026 — Bison Wallet 1.0** shipped, consolidating DCRDEX trading, multi-coin wallet, and cross-chain atomic swaps in one client.
- **Feb–Apr 2026** — DCR retraced ~30% into the April snapshot ($20.57, #119).
- **Apr–Jun 2026** — the fade continued; DCR fell to **$11.52 (~$201M, #178)** by 2026-06-20 — the full governance-catalyst pump-and-fade, a pattern worth noting for future Politeia votes.

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 768 |
| **GitHub Forks** | 315 |
| **Commits (4 weeks)** | 7 |
| **Pull Requests Merged** | 2,891 |
| **Contributors** | 72 |
| **Repo** | [decred/dcrd](https://github.com/decred/dcrd) |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://decred.org/](https://decred.org/) |
| **Twitter** | [@decredproject](https://twitter.com/decredproject) |
| **Reddit** | [r/decred](https://www.reddit.com/r/decred) |
| **Telegram** | [Decred](https://t.me/Decred) (~3,868 members) |
| **Discord** | [https://discord.gg/dXSmwvYury](https://discord.gg/dXSmwvYury) |

---

## Related

- [[bitcoin]] — shares the 21M hard cap and store-of-value framing
- [[crypto-markets]]
- [[crypto-narratives-overview]]
- [[binance]], [[kraken]]
- [[cex]] vs DCRDEX self-custodied trading
- [[market-regime]], [[crypto-fear-and-greed-index]]

---

## Sources

- CoinGecko market data snapshot, 2026-04-09 (CoinGecko top-1000 ingest)
- Market data 2026-06-20 from `raw/data/crypto-loop/coingecko-markets.json` (cryptodataapi.com / CoinGecko); macro backdrop from `raw/data/crypto-loop/_digest.md`.
- CoinJournal, "Decred (DCR) price soars amid treasury spending cap approval" — https://coinjournal.net/news/decred-dcr-price-soars-amid-treasury-spending-cap-approval/
- Decred treasury data — https://dcrdata.decred.org/treasury
- Decred docs — https://docs.decred.org/
- Verified via Perplexity (sonar) + web search, 2026-06-10: DCP-0013 4% treasury cap approved Jan 2026 (~99.98% support), treasury >867k DCR, Bison Wallet 1.0 Jan 2026

## Trading Profile

### Venues & liquidity

DCR is tradable on **Binance SPOT only** — there is **no liquid perpetual venue**, so leverage and short access are limited and this is a **spot-primary asset**. Perp funding/basis/liquidation strategies do **not** apply. Execution must run through spot order books, so directional exposure is effectively long-only (or requires borrowing, which is scarce for a #145-rank name). With ~$0.5M–$5M daily volume against a ~$200M cap, book depth is thin: market orders slip and large clips must be worked patiently (TWAP/VWAP-style scaling, limit ladders). Size positions small relative to typical liquidity, budget for wide spreads around governance catalysts, and prefer spot accumulation over any margin construction.

### Applicable strategies

- [[event-driven-trading]] — DCR's biggest moves are endogenous Politeia/DCP governance and treasury events (DCP-0013 drove a ~75% weekly move), the definitive catalyst-trade setup.
- [[dca-strategy]] — spot-only, hard-capped (21M) sound-money asset with deep drawdowns; averaging in suits accumulation without needing leverage or shorting.
- [[buy-and-hold]] — fixed-supply, self-funded-treasury governance coin fits a long-horizon store-of-value thesis for conviction holders.
- [[breakout-and-retest]] — thin liquidity produces sharp governance-driven range breaks; entering on the retest filters the frequent fade after the pump.
- [[volatility-targeting]] — event-clustered volatility (calm drift punctuated by 50–75% governance spikes) argues for scaling exposure to realized vol rather than a fixed notional.
- [[atr-trailing-stop]] — low-float pump-and-fade behavior makes a volatility-scaled trailing stop useful for locking gains as governance rallies exhaust.

### Volatility & regime character

Small-cap (~#145), low-float L1 with **high idiosyncratic, event-driven volatility** rather than steady beta. Between catalysts DCR drifts with the broad crypto tape and carries meaningful **BTC correlation** (shared 21M-cap / sound-money framing), but around Politeia votes it decouples with reflexive, low-liquidity spikes and fades. It trades in the OG PoW/privacy/governance cohort — not with [[defi]] or AI baskets — and behaves like a thin long-tail alt in risk-off regimes (amplified downside when Fear & Greed is low).

### Risk flags

- **Venue/liquidity concentration** — Binance-spot primary, thin (~$0.5M–$5M) daily volume; high slippage, hard to exit size, no perp hedge.
- **Narrative dependence** — price is hostage to endogenous governance/treasury events; between catalysts it bleeds with the bear tape, and "on-chain governance" is no longer a differentiated narrative.
- **Emission/treasury supply** — slow block emission (~17% un-emitted) plus a treasury that can sell DCR are mild ongoing supply sources (no unlock cliff, but persistent).
- **Regulatory** — privacy tooling (StakeShuffle) can attract exchange-delisting/regulatory scrutiny for privacy-adjacent assets.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] Binance-spot endpoints (auth via `X-API-Key`). No perp/funding endpoints apply — no liquid perp venue.

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=DCRUSDT` — current price
- `GET /api/v1/market-data/ticker/24hr?symbol=DCRUSDT` — 24h ticker stats (volume, range, change)

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=DCRUSDT&interval=1d&limit=1000` — OHLCV klines
- `GET /api/v1/market-data/volume-history?days=90` — daily volume + buy ratio
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=DCRUSDT&interval=1d&limit=1000"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]

---
