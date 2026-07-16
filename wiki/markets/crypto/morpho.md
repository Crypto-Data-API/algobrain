---
title: "Morpho"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, hyperliquid, perpetual-futures, funding-rate, open-interest, derivatives, altcoins]
aliases: ["MORPHO", "Morpho Blue", "Morpho Labs"]
entity_type: protocol
founded: 2021
headquarters: "Paris, France (Morpho Association)"
website: "https://morpho.org/"
related: ["[[aave]]", "[[ai-finance]]", "[[artificial-intelligence]]", "[[base]]", "[[coinbase]]", "[[compound-governance-token]]", "[[crypto-markets]]", "[[defai]]", "[[defi-narratives]]", "[[defi]]", "[[ethereum]]", "[[ml-defi-risk-models]]", "[[token-unlocks]]", "[[hyperliquid]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[pairs-trading]]", "[[token-unlock-supply-event]]"]
---

# Morpho

**Morpho** (MORPHO) is the second-largest DeFi lending protocol after [[aave|Aave]], built as minimal, immutable, isolated lending markets (Morpho Blue) with a curated-vault layer on top. It has become the default white-label lending backend for institutions — most visibly powering [[coinbase|Coinbase]]'s BTC-backed loans — with deposits growing from ~$5B to ~$13B during 2025. As of 2026-06-20 the MORPHO token sits at **rank #61, market cap $1.21B**.

---

## Market Data

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

Backdrop: the [[crypto-fear-and-greed-index|Fear & Greed Index]] reads **22 (extreme fear)** in an **established bear market**. MORPHO is down on both a 24h and 7-day basis, and its 24h volume ($9.1M) is thin relative to cap — a relatively illiquid governance token where flows can move price.

| Metric | Value |
|---|---|
| **Price** | $1.87 |
| **Market Cap** | $1,210,239,306 |
| **Market Cap Rank** | #61 |
| **24h Volume** | $9,111,613 |
| **24h Change** | -4.01% |
| **7d Change** | -6.78% |
| **24h Range** | $1.87 – $1.95 |
| **Circulating Supply** | 646,813,973 MORPHO |
| **Total Supply** | 1,000,000,000 MORPHO |
| **Max Supply** | 1,000,000,000 MORPHO |
| **Fully Diluted Valuation** | $1,871,077,863 |
| **Market Cap / FDV** | ~0.65 |
| **All-Time High** | $4.17 (2025-01-17) — **-55.07%** from ATH |
| **All-Time Low** | $0.713151 (2024-11-25) — **+162.74%** from ATL |

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | MORPHO |
| **Market Cap Rank** | #61 (2026-06-20) |
| **Market Cap** | $1.21B (2026-06-20) |
| **Sector** | DeFi lending (isolated markets + curated vaults), #2 by TVL behind [[aave|Aave]] |
| **Supply mechanics** | 1B max supply; ~65% circulating (MC/FDV ≈ 0.65) — meaningful unlock overhang remains |
| **Categories** | DeFi, Lending/Borrowing, Ethereum / [[base\|Base]] / Arbitrum Ecosystems, Coinbase Ventures & Pantera Portfolios |
| **Website** | [https://morpho.org/](https://morpho.org/) |

---

## Overview

Morpho is an open, efficient, and resilient platform that allows anyone to earn yield and borrow assets. Lenders earn via Morpho Vaults — noncustodial, simple-to-use lending vaults that optimize yields for depositors — while borrowers borrow directly from Morpho Markets. Developers and businesses can create markets, curate vaults, and build applications on its flexible, permissionless infrastructure.

Design pillars: trustless (immutable contracts, governance-minimized operations), efficient (higher collateralization factors via isolated markets, improved rates, low gas), and flexible (permissionless market creation and risk management). This "lending as infrastructure" design is why exchanges and fintechs embed Morpho rather than building their own credit engines.

## Major News & Events (2025–2026)

- **2025-01 — Coinbase BTC-backed loans**: Coinbase launched bitcoin-collateralized USDC loans powered by Morpho on [[base|Base]]. By April 2026 the integration held **$1.6B+ in collateral** with **>$2.17B cumulative USDC originations**, including a UK expansion in early 2026.
- **2025-06 — Morpho V2**: intent-based, market-driven pricing — fixed-rate, fixed-term loans with bespoke collateral (portfolios, RWAs) — moving DeFi lending toward institutional credit markets. **Vaults V2** followed (Sept 2025) with compliance-friendly curated vaults.
- **2025 — Structure cleanup**: Morpho Labs folded under the nonprofit **Morpho Association**, aligning the company with token holders (single-asset model).
- **2025 — Growth**: deposits grew ~$5B → ~$13B over 2025; TVL crossed ~$7B in May 2026 (~$10B+ counting all deposits, source-dependent), second only to Aave. Partner integrations include Crypto.com, Société Générale's stablecoin, Apollo/securitized credit funds and Bitwise.
- **2026-06-09 — $175M raise**: Paradigm and a16z invested $175M into Morpho (reported by The Crypto Times) — a major late-stage institutional endorsement.

---

## Protocol & Technology

Morpho is a [[defi|DeFi]] lending stack built in two layers: a minimal, immutable base protocol and a curated risk layer on top. This separation is the core design insight — it pushes risk management out of the core contract and into a competitive market of curators.

### Morpho Blue — isolated lending markets
The base layer is a single, immutable, governance-minimized contract. Anyone can permissionlessly create a **lending market** defined by five parameters: collateral asset, loan asset, oracle, liquidation LTV (LLTV), and interest-rate model. Each market is **isolated** — a bad-debt event in one market cannot contaminate another, unlike the shared-pool model of [[aave|Aave]] and [[compound-governance-token|Compound]] where every asset shares one risk surface. Because the core is tiny and immutable, it is cheap (low gas), auditable, and supports higher collateralization factors than monolithic pools.

Contrast with the original Morpho Optimizer (its first product, 2021–2023), which sat *on top of* Aave/Compound and peer-to-peer-matched lenders and borrowers to capture the spread, falling back to the underlying pool when unmatched. Morpho Blue replaced that with a standalone primitive.

### Morpho Vaults (MetaMorpho) — the curated layer
Most lenders don't want to pick individual isolated markets. **Vaults** are noncustodial ERC-4626 vaults run by **curators** (risk experts, DAOs, institutions) who allocate depositor funds across multiple Morpho Blue markets according to a published risk policy. Depositors get a single yield-bearing position; curators earn a fee for managing risk. This is the layer institutions and fintechs plug into — they (or a trusted curator) define the risk box, and depositors get optimized yield.

### Morpho V2 — intent-based, fixed-rate/fixed-term
Launched June 2025, **V2** introduces market-driven pricing via **intents**: borrowers and lenders express what they want (rate, term, collateral — including portfolios and RWAs) and the protocol matches them, enabling **fixed-rate, fixed-term** loans. This moves Morpho from variable-rate money markets toward institutional credit markets. **Vaults V2** (Sept 2025) added compliance-friendly, more configurable curated vaults.

### Why institutions embed Morpho ("lending as infrastructure")
Because the core is immutable and risk is externalized to curators, exchanges and fintechs can white-label Morpho as their credit backend rather than building one. The flagship example is [[coinbase|Coinbase]]'s BTC-backed USDC loans (powered by Morpho on [[base|Base]]) — Coinbase owns the front-end and UX; Morpho is the on-chain credit engine. This is the "DeFi mullet": fintech in front, DeFi in back.

### MORPHO token & governance
MORPHO is the governance token of the **Morpho DAO**, which oversees the protocol, the curator framework, incentive emissions and the treasury. Following the 2025 reorganization, **Morpho Labs folded under the nonprofit Morpho Association** to align the company with token holders under a single-asset model. The token does not directly capture lending interest (that flows to lenders and curators); value-accrual debate centers on potential future fee switches and governance rights.

---

## Tokenomics & Supply

> *Authoritative figures are in the [[morpho#Market Data\|Market Data]] block (2026-06-20).*

| Metric | Value (2026-06-20) |
|---|---|
| **Circulating Supply** | 646,813,973 MORPHO |
| **Total Supply** | 1,000,000,000 MORPHO |
| **Max Supply** | 1,000,000,000 MORPHO |
| **Fully Diluted Valuation** | $1,871,077,863 |
| **Market Cap / FDV Ratio** | ~0.65 |

**Emissions & unlocks.** MORPHO has a fixed 1B max supply. Circulating has risen from ~552M (April 2026) to ~647M (June 2026) — roughly **+95M in ~10 weeks**, i.e. ongoing emission/unlock pressure as investor (Coinbase Ventures, Pantera, Paradigm/a16z), team and DAO allocations vest and as governance/usage incentives are distributed. With MC/FDV ≈ 0.65, ~35% of supply (~353M MORPHO) is still to enter circulation — a persistent structural overhang ([[token-unlocks]] behavior). The June 2026 $175M Paradigm/a16z raise expands the long-term insider supply that will eventually unlock. Net: MORPHO is a token where supply growth is a recurring headwind that strong fundamentals (deposits, integrations) must outrun.

---

## Price History

> *Authoritative current figures are in the [[morpho#Market Data\|Market Data]] block (2026-06-20). Table below is long-horizon reference.*

| Metric | Value |
|---|---|
| **All-Time High** | $4.17 (2025-01-17) — -55.07% |
| **All-Time Low** | $0.713151 (2024-11-25) — +162.74% |
| **24h Change (2026-06-20)** | -4.01% |
| **7d Change (2026-06-20)** | -6.78% |

---

## Platform & Chain Information

**Native Chain:** Ethereum (deployed on Base, Arbitrum, Katana and others)

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x58d97b57bb95320f9a05dc918aef65434969c2b2` |
| Katana | `0x1e5efca3d0db2c6d5c67a4491845c43253eb9e4e` |
| Base | `0xbaa5cc21fd487b8fcc2f632f3f4e8d37262a0842` |
| Arbitrum One | `0x40bd670a58238e6e230c430bbb5ce6ec0d40df48` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair |
|---|---|
| Binance | MORPHO/USDT |
| Kraken | MORPHO/USD |
| Bitget | MORPHO/USDT |
| KuCoin | MORPHO/USDT |
| Crypto.com Exchange | MORPHO/USD |

### Decentralized Exchanges / Perps

| Exchange | Pair | Type |
|---|---|---|
| [[hyperliquid|Hyperliquid]] | MORPHO-PERP | Perpetual |
| Uniswap V3 (Ethereum) | MORPHO/WETH | Spot |

---

## Trading Relevance

- **Narrative basket**: blue-chip DeFi lending / "DeFi mullet" (fintech front-end, DeFi back-end) — the institutional-DeFi trade alongside [[aave|AAVE]]. See [[defi-narratives]].
- **Fundamental tape**: track deposits/TVL (DefiLlama), Coinbase loan-book growth, and vault curator flows; MORPHO re-rates on integration announcements (Coinbase, Crypto.com, SocGen) and raises (June 2026 Paradigm/a16z $175M).
- **Supply risk**: MC/FDV ≈ 0.55 — unlocks from investor/DAO allocations are a persistent overhang ([[token-unlocks]] basket behavior).
- **Venues**: Binance spot, MORPHO-PERP on [[hyperliquid]]; relative-value trades vs AAVE are the natural pair (Morpho growing faster, Aave larger and fee-switch-enabled).
- **Risks**: smart-contract/curator risk in isolated vaults (several curated-vault blowups across DeFi in 2025 raised scrutiny of the curator model), rate compression in a falling-yield regime.

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://morpho.org/](https://morpho.org/) |
| **Twitter** | [@Morpho](https://twitter.com/Morpho) |
| **GitHub** | [https://github.com/morpho-org](https://github.com/morpho-org) |
| **Whitepaper** | [Morpho Blue whitepaper](https://github.com/morpho-org/morpho-blue/blob/main/morpho-blue-whitepaper.pdf) |

---

## Trading Characteristics

> *Current figures: see [[morpho#Market Data\|Market Data]] (2026-06-20).*

| Characteristic | Detail (2026-06-20) |
|---|---|
| **24h Volume** | $9.11M |
| **Market Cap Rank** | #61 |
| **Volume / MCAP turnover** | ~0.75% (thin/illiquid for its cap) |
| **24h Range** | $1.87 – $1.95 |

---

## Ecosystem & Use Cases

- **White-label credit backend** — [[coinbase|Coinbase]] BTC-backed USDC loans (on [[base|Base]]), Crypto.com, Société Générale's stablecoin, and other fintechs use Morpho as their on-chain lending engine.
- **Curated yield vaults** — risk firms (Gauntlet, Steakhouse, Block Analitica, Re7 and others) run MetaMorpho vaults; depositors pick a curator's risk box and earn optimized lending yield.
- **Permissionless markets** — anyone can spin up an isolated market for a new collateral/loan pair (incl. RWAs, LSTs, long-tail assets) without governance approval.
- **Institutional credit (V2)** — fixed-rate, fixed-term loans against portfolios and tokenized real-world assets; partners include Apollo/securitized credit funds and Bitwise.
- **Leverage & looping** — borrowers loop collateral (e.g. ETH/LST recursive borrowing) for leveraged yield.
- **Deployments** — Ethereum, [[base|Base]] (largest by activity via Coinbase), Arbitrum, Katana and other chains.

---

## Market Structure & Derivatives

- **Spot venues**: Binance (MORPHO/USDT, price leader), Kraken, Bitget, KuCoin, Crypto.com. On-chain, MORPHO/WETH on [[uniswap|Uniswap]] v3.
- **Perps & funding**: MORPHO-PERP on [[hyperliquid|Hyperliquid]] and select CEX perp desks; OI and funding are modest given the token's relatively thin float and liquidity.
- **Liquidity caveat**: ~$9.1M 24h volume on a ~$1.2B cap is a ~0.75% turnover — low for a top-65 token. Slippage on size is real; treat MORPHO as a lower-liquidity governance token, not a deep-book major.
- **Fundamental tape (more important than price tape)**: deposits/TVL on DefiLlama, Coinbase loan-book originations, and vault curator flows drive re-rating more than order-book microstructure.

---

## Valuation Framework

MORPHO does not directly capture lending interest (that accrues to lenders/curators), so valuation leans on usage and optionality rather than current cash flows:

- **Deposits / TVL** — the headline fundamental; Morpho's TVL (~$7B+ on DefiLlama, ~$10B+ counting all deposits, source-dependent) is #2 behind [[aave|Aave]]. Track TVL trajectory and market share.
- **Loan originations** — Coinbase BTC-loan cumulative originations (>$2.17B by April 2026) and active collateral (>$1.6B) proxy real demand.
- **Protocol revenue / fee-switch optionality** — curator fees and any future DAO fee switch are the path to direct token value accrual; currently latent, a key bull/bear fault line.
- **MC/FDV ~0.65** — discount the implied valuation for the ~35% of supply still to unlock.
- **Relative multiple vs Aave** — compare MC/TVL (or FDV/TVL) of MORPHO vs [[aave|AAVE]]; Morpho grows faster, Aave is larger and already fee-switch-enabled — the spread is the relative-value trade.

---

## Trading Playbook

- **Institutional-DeFi / "DeFi mullet" basket** — MORPHO is a blue-chip lending play alongside [[aave|AAVE]]; rotate on integration and RWA-credit catalysts. See [[defi-narratives]].
- **Integration / raise catalysts** — MORPHO re-rates on partner announcements (Coinbase, Crypto.com, SocGen) and raises (June 2026 Paradigm/a16z $175M). Position around the fundamental tape, not the price tape.
- **Morpho vs Aave pair** — the natural relative-value trade: long MORPHO (faster growth) / short AAVE (larger, fee-switch live), or the reverse if you favor realized cash flow over growth optionality.
- **Unlock-aware sizing** — with ~+95M MORPHO added to float in ~10 weeks and ~35% still locked, fade strength into known unlock windows; supply growth is a structural headwind ([[token-unlocks]]).
- **Liquidity discipline** — thin 24h volume means use limit orders and scale; avoid market orders in size, especially in the current extreme-fear tape.
- **Risk in extreme fear** — Fear & Greed = 22; MORPHO is down on the week, so prefer accumulation on fundamental strength over momentum chasing.

---

## History

| Date | Event |
|---|---|
| 2021 | Morpho founded (Paris); Morpho Optimizer launches atop Aave/Compound (P2P matching) |
| 2023 | Token raise (a16z, Variant); Morpho Blue design begins |
| 2024-01 | **Morpho Blue** (isolated immutable markets) launches |
| 2024-11 | MORPHO token transferable; ATL $0.713 |
| 2025-01 | Coinbase BTC-backed loans go live on Morpho; ATH $4.17 |
| 2025-06 | **Morpho V2** (intent-based, fixed-rate/fixed-term) |
| 2025-09 | **Vaults V2** (compliance-friendly curated vaults) |
| 2025 | Morpho Labs folds under nonprofit Morpho Association; deposits ~$5B → ~$13B |
| 2026-06-09 | Paradigm + a16z invest $175M |
| 2026-06-20 | MORPHO $1.87, #61, in an extreme-fear / established-bear-market tape |

---

## Competitive Positioning

| Protocol | Model | Edge vs Morpho | Morpho's Edge |
|---|---|---|---|
| [[aave\|Aave]] | Shared-pool money market; #1 by TVL | Largest TVL, deepest liquidity, GHO stablecoin, fee switch live, brand | Isolated markets (better risk segmentation), higher capital efficiency, white-label embeddability, faster growth |
| [[compound-governance-token\|Compound]] | Original shared-pool money market | First mover, battle-tested, simple | Far more flexible (permissionless markets), curated vaults, better rates |
| Spark (Sky) | Sky-aligned lending | Deep DAI/USDS liquidity, SKY backing | Neutral/curator-driven, broader collateral, isolated risk |
| Euler v2 | Modular isolated lending | Similar modular thesis, vault connectors | Larger TVL, Coinbase/institutional distribution |
| Fluid (Instadapp) | Smart-collateral lending/DEX hybrid | Capital efficiency via combined lending+DEX | Bigger integration footprint, curator ecosystem |

Morpho's moat is the **immutable core + curated-vault model** plus **institutional distribution** (Coinbase, fintechs). The trade-off versus [[aave|Aave]]: Aave is larger and already returns value to token holders via its fee switch, while Morpho is the faster-growing, more-embeddable challenger whose token value accrual is still largely optionality.

---

## Risks

- **Curator / vault risk** — risk is externalized to curators; several curated-vault blowups across DeFi in 2025 showed depositors can absorb losses from a curator's bad allocation or oracle choice. Vault quality is uneven — depositors must vet curators.
- **Oracle / market-config risk** — permissionless markets can be created with weak oracles or aggressive LLTVs; isolated design contains the damage but a single bad market can still wipe its depositors.
- **Supply overhang** — ~35% of MORPHO still to unlock; rapid float growth (~+95M in 10 weeks to June 2026) pressures price ([[token-unlocks]]).
- **No direct fee capture (yet)** — MORPHO value accrual is governance + optionality; if a fee switch never materializes, the bull case weakens.
- **Concentration / dependence** — heavy reliance on the Coinbase integration for headline growth; a Coinbase pivot would dent the narrative.
- **Rate compression** — in a falling-yield regime, lending spreads compress, shrinking both curator economics and the growth story.
- **Liquidity** — thin token liquidity amplifies drawdowns in stress (relevant in the current extreme-fear tape).

---

## See Also / Related

- [[aave]] — the #1 lending protocol and natural pair trade
- [[compound-governance-token]] — original money-market peer
- [[coinbase]] — flagship integration partner
- [[ethereum]], [[base]] — deployment chains
- [[defi]], [[defi-narratives]] — sector context
- [[token-unlocks]] — supply-overhang dynamics
- [[hyperliquid]] — perp venue
- [[uniswap]] — on-chain spot venue
- [[ml-defi-risk-models]], [[defai]] — risk-modeling crossover topics

---

## Sources

- Market data 2026-06-20: cryptodataapi.com / CoinGecko markets snapshot (`raw/data/crypto-loop/coingecko-markets.json`)
- (Source: [[coingecko-top-1000-2026-04-09]]) — April 2026 market snapshot
- Morpho blog, "Morpho 2026" — https://morpho.org/blog/morpho-2026/
- DefiLlama Morpho dashboard — https://defillama.com/protocol/morpho
- The Crypto Times, "Why Paradigm and a16z Just Poured $175M Into Morpho" (2026-06-09) — https://www.cryptotimes.io/2026/06/09/why-paradigm-and-a16z-just-poured-175m-into-morpho/
- AInvest, "Morpho Vaults V2" coverage; Eco, "Morpho Protocol Explained 2026"
- Web verification (WebSearch + Perplexity), 2026-06-10

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 654.68M MORPHO |
| **Total Supply** | 1.00B MORPHO |
| **Max Supply** | 1.00B MORPHO |
| **Fully Diluted Valuation** | $2.10B |
| **Market Cap / FDV Ratio** | 0.65 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Trading Profile

### Venues & liquidity
MORPHO trades on **both** major derivatives venues: [[hyperliquid|Hyperliquid]] lists **MORPHO-PERP** (on-chain USD-margined perp, leverage up to ~40–50x), and Binance offers **MORPHO/USDT spot plus a USD-margined perpetual**. This gives a genuine two-venue market rather than a single-venue long-tail listing — CEX depth (Binance) and on-chain depth (Hyperliquid HLP book) coexist, so the two funding/mark prices can be arbitraged against each other. That said, MORPHO is a mid-cap governance token with modest turnover for its rank, so effective liquidity is thinner than a major: size positions to the book, prefer limit/scaled entries over market orders, and expect real slippage on large clips. The dual-venue structure improves execution optionality (route to whichever venue is deeper/cheaper at the moment) and enables cross-venue basis and funding trades.

### Applicable strategies
- [[hl-vs-cex-funding-divergence]] — MORPHO runs on both Hyperliquid and Binance perps, so the on-chain vs CEX funding spread is directly tradeable when the two venues diverge.
- [[funding-rate-arbitrage]] — long spot (Binance) / short perp (or vice versa) to harvest funding when the MORPHO perp trades persistently rich or cheap to spot.
- [[cash-and-carry]] — Binance MORPHO/USDT spot plus a perp short lets you lock the basis and collect carry on a genuine two-venue token.
- [[pairs-trading]] — MORPHO vs [[aave|AAVE]] is the natural DeFi-lending relative-value pair (faster-growing challenger vs larger incumbent), both liquid enough to trade the spread.
- [[liquidation-cascade-fade]] — thin float plus up-to-~50x leverage on MORPHO-PERP makes stop-runs and liquidation flushes sharp and often overshoot, giving mean-reversion entries.
- [[token-unlock-supply-event]] — with ~35% of supply still to enter circulation and ongoing emissions, unlock/emission windows are recurring, position-able supply events.

### Volatility & regime character
MORPHO is a **DeFi / lending-infrastructure altcoin** — a high-beta, mid-cap governance token rather than a large-cap major or memecoin. It trades with the broad DeFi-narrative basket (alongside [[aave|AAVE]] and other lending names) and carries elevated beta to BTC/ETH: it tends to amplify moves in the majors on both sides, with idiosyncratic re-rating driven by fundamental catalysts (deposits/TVL growth, Coinbase loan-book, institutional integrations and raises) more than by the price tape alone. Expect high-beta drawdowns in risk-off regimes and narrative-led rallies when institutional-DeFi is in favor.

### Risk flags
- **Liquidity / venue concentration** — modest turnover for a top-60 token; slippage and gap risk in stress, and much of the depth concentrates on Binance + Hyperliquid.
- **Token unlocks / emissions** — ~35% of supply still to unlock plus ongoing emissions ([[token-unlocks]]) are a persistent supply headwind that can cap rallies.
- **Narrative dependence** — price re-rates on integration/raise catalysts and DeFi-sentiment; heavy reliance on the Coinbase integration for headline growth.
- **Perp funding dislocations** — with up-to-~50x leverage and two venues, funding can spike and the Hyperliquid vs CEX marks can dislocate during volatility, forcing crowded positioning to unwind.
- **Protocol / curator risk** — smart-contract and curated-vault risk in the underlying protocol can feed back into token sentiment.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/summary?coin=MORPHO` — all-in-one perp data (mark, funding, OI)
- `GET /api/v1/hyperliquid/prices` — all mid prices
- `GET /api/v1/hyperliquid/l2-book?coin=MORPHO` — L2 order-book depth
- `GET /api/v1/hyperliquid/open-interest` — all-asset open interest

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=MORPHO&interval=1h&limit=1000` — OHLCV candles
- `GET /api/v1/hyperliquid/funding-rates?coin=MORPHO&limit=100` — funding history
- `GET /api/v1/daily/hyperliquid` — daily bulk snapshot of ~230 HL perps

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/summary?coin=MORPHO"
```

Auth: `X-API-Key` header. Endpoint catalog: [[cryptodataapi-hyperliquid]]. See also [[cryptodataapi]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---
