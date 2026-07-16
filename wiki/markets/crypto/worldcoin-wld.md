---
title: "Worldcoin (World Network)"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, hyperliquid, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, altcoins, ethereum]
aliases: ["WLD", "World", "World Network", "Worldcoin"]
entity_type: protocol
founded: 2019
website: "https://world.org/"
related: ["[[artificial-intelligence]]", "[[crypto-markets]]", "[[decentralized-ai]]", "[[ethereum]]", "[[hyperliquid]]", "[[layer-2]]", "[[narrative-trading]]", "[[openai]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[proof-of-humanity]]", "[[token-unlock-supply-event]]", "[[token-unlocks]]"]
headquarters: "Decentralized"
---

# Worldcoin (World Network)

**Worldcoin** — rebranded **World Network** in October 2024 — is the Sam Altman-co-founded ([[openai|OpenAI]] CEO) biometric identity project built by Tools for Humanity: iris-scanning "Orb" devices issue privacy-preserving World IDs as proof-of-humanness, with the WLD token distributed as grants to verified users. For traders, WLD is the purest listed proxy for the **AI-identity narrative** and one of the most news-reflexive large alts — it moves on Sam Altman/OpenAI headlines, US expansion milestones, biometric-privacy regulatory actions, and a heavy token-unlock schedule (only ~⅓ of the 10B supply circulates).

---

## Market Data

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

Backdrop: the [[crypto-fear-and-greed-index|Fear & Greed Index]] reads **22 (extreme fear)** in an **established bear market**. WLD is the most volatile name in this set: **+26.08% over 7 days** (a sharp news-driven bounce off its May ATL) yet **-7.31% on the day** — a classic high-beta AI-narrative whipsaw. Note the **acute dilution flag**: only ~3.41B of a 10B max supply circulates, so **FDV ($6.02B) is ~3x market cap ($2.06B)** — among the heaviest unlock overhangs of any large-cap token.

| Metric | Value |
|---|---|
| **Price** | $0.601876 |
| **Market Cap** | $2,055,325,392 |
| **Market Cap Rank** | #43 |
| **24h Volume** | $444,737,643 |
| **24h Change** | -7.31% |
| **7d Change** | +26.08% |
| **24h Range** | $0.593864 – $0.649409 |
| **Circulating Supply** | 3,413,109,605 WLD |
| **Total Supply** | 10,000,000,000 WLD |
| **Max Supply** | 10,000,000,000 WLD |
| **Fully Diluted Valuation** | $6,021,855,815 |
| **Market Cap / FDV** | **~0.34 (heavy dilution overhang)** |
| **All-Time High** | $11.74 (2024-03-10) — **-94.87%** from ATH |
| **All-Time Low** | $0.230306 (2026-05-18) — **+161.55%** from ATL |

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | WLD |
| **Rank tier** | #43 (2026-06-20) |
| **Backers** | Tools for Humanity; a16z, Bain Capital Crypto, Coinbase Ventures, Multicoin, Blockchain Capital portfolios |
| **Supply mechanics** | 10B max supply; only ~34% circulating — persistent unlock/grant emission overhang (**MC/FDV ~0.34**) |
| **Chains** | Ethereum (native), World Chain (own OP-stack [[layer-2\|L2]]), Optimism |
| **Users** | ~33M World App users / ~15M Orb-verified reported around Sep 2025; ~25M users / ~12M Orb-verified per June 2026 estimates (sources vary — treat counts as approximate) |
| **Market data** | $2.06B cap at $0.602 (2026-06-20); ATL $0.230306 set 2026-05-18 |
| **Website** | [https://world.org/](https://world.org/) |

---

## Overview

The mission of the Worldcoin project is to build the world's largest identity and financial network as a public utility, giving ownership to everyone. A key component is foundational infrastructure for a world where AI plays an increasingly large role.

The system revolves around **World ID**, a privacy-preserving global identity network. World ID enables users to verify their humanness online while maintaining privacy through zero-knowledge proofs. Using World ID, individuals can prove they are a real, unique human to any integrated platform — web3 systems, social networks, governmental programs — enabling fair airdrops, sybil resistance, and potentially AI-funded UBI experiments.

To engage with the protocol, individuals download World App, then visit a physical imaging device called the **Orb** (operated by independent "Orb Operators") for iris verification; images are deleted on-device by default. Orb-verified World ID holders can claim recurring WLD grants. WLD is a utility token with governance properties; the network runs its own Ethereum L2, **World Chain**, in the Optimism Superchain.

---

## Protocol & Technology

Worldcoin/World is three coupled products: a **proof-of-personhood identity** (World ID), the **hardware** that issues it (the Orb), and an **app + L2 + token** that distribute and use it.

### World ID — privacy-preserving proof-of-humanness
World ID is a [[proof-of-humanity|proof-of-personhood]] credential. The goal: let a user prove to any service that they are **a unique, real human** (not a bot, not duplicated) **without revealing who they are**. This matters in an AI world where bots are indistinguishable from people online — sybil-resistant airdrops, fair voting, bot-free social, and potentially AI-funded UBI all need a humanness primitive.
- **Zero-knowledge proofs** — verification produces a ZK proof of "I am a unique verified human" without exposing the underlying biometric or linking actions across services (unlinkability).
- **Iris as the uniqueness key** — the iris is used because it is highly unique and stable, enabling global de-duplication (one human → one World ID).

### The Orb — biometric hardware
The **Orb** is a physical iris-scanning device operated by independent **Orb Operators**. A user visits an Orb, which captures an iris image, derives an **iris code**, and (by default) **deletes the image on-device** — only the cryptographic code/proof persists. This local-deletion design is the core privacy claim, but compelled collection of biometric data is exactly what has drawn regulators. Newer Orb hardware and **AMPC (anonymized multi-party computation)** upgrades aim to further decentralize and harden how iris data is stored/checked.

### World App, World Chain, and grants
- **World App** — the consumer wallet/super-app: holds World ID and WLD, hosts **Mini Apps**, and is the on-ramp to the ecosystem.
- **World Chain** — World's own **OP-stack [[layer-2|L2]]** in the Optimism Superchain, giving verified humans priority blockspace/gas allowances and hosting the WLD in-app economy.
- **WLD grants** — Orb-verified users can claim **recurring WLD grants** (the distribution mechanism and a key emission source). WLD is also gas/utility in the World ecosystem and carries governance properties.

### Backers & governance
Co-founded by **Sam Altman** ([[openai|OpenAI]] CEO), built by **Tools for Humanity**; backed by a16z, Bain Capital Crypto, Coinbase Ventures, Multicoin and Blockchain Capital. The OpenAI/Altman association is why WLD is the market's purest **AI-identity narrative** proxy.

---

## Major News & Events

- **Oct 2024** — Project rebrands from Worldcoin to **World Network**.
- **Jan–May 2025 — Regulatory friction.** The project has faced bans, suspensions or enforcement over biometric data collection in multiple jurisdictions (Spain and Portugal suspensions in 2024; Brazil's data authority ordered a halt to compensated iris scanning in January 2025; Indonesia suspended operations and a Kenyan court ordered biometric data deletion in May 2025).
- **May 1, 2025 — US launch.** World opened US operations in Atlanta, Austin, LA, Miami, Nashville and San Francisco (plus Razer stores), with a stated plan to deploy **7,500 Orbs across the US** — at the time roughly quadruple global deployment (BeInCrypto).
- **May 2025 — $135M raise.** World Assets sold $135M of WLD to **a16z and Bain Capital Crypto** to fund US/network expansion; WLD rallied on the news (FXStreet, 2025-05-21).
- **Sep 2025** — ~33M World App users, ~15M verified reported.
- **Apr–May 2026 — capitulation.** WLD ground to fresh lows amid alt-market weakness and continued unlock pressure, printing an **all-time low of $0.230306 on 2026-05-18** (~-98% from the March 2024 ATH of $11.74).
- **2026 — Recovery + roadmap.** Network activity hit 2026 highs and WLD rebounded sharply (**+26% in the week to 2026-06-20, to $0.602**, -7.3% on the day) on AI-narrative flow; 2026 roadmap includes World ID privacy/scalability upgrades (AMPC), Mini Apps / WLD in-app economy expansion, and World Chain throughput scaling.

---

## Trading Relevance

- **Narrative basket:** AI x crypto / digital-identity — WLD is the headline-beta vehicle for [[artificial-intelligence|AI]] news that touches crypto, especially anything involving Sam Altman or OpenAI product launches (historically: GPT/Sora releases pumped WLD).
- **Venues:** deep spot liquidity on Binance, Kraken, Upbit (KRW pairs drive Korean retail flow), Bitget, KuCoin, Crypto.com; **WLD-PERP on [[hyperliquid|Hyperliquid]]** and all major perp venues. **~$445M daily volume on 2026-06-20** — a very high ~21% turnover, reflecting the news-driven 7-day spike (one of the most actively traded names in the set).
- **Supply overhang:** MC/FDV ~0.34 — continuous unlocks to insiders/Tools for Humanity plus grant emissions make WLD a structurally heavy chart; short-the-rip on unlock schedules has been a recurring trade.
- **Catalysts:** US Orb-deployment milestones, regulatory bans/reinstatements (binary headline risk in both directions), OpenAI/Altman news, World Chain ecosystem metrics, exchange listing/delisting of WLD in restricted jurisdictions.
- **Risk:** extreme drawdown profile (-98% ATH-to-ATL); biometric-privacy enforcement is an ever-present tail risk.

---

## Tokenomics & Supply

> *Authoritative figures are in the [[worldcoin-wld#Market Data\|Market Data]] block (2026-06-20).*

| Metric | Value (2026-06-20) |
|---|---|
| **Circulating Supply** | 3,413,109,605 WLD |
| **Total Supply** | 10,000,000,000 WLD |
| **Max Supply** | 10,000,000,000 WLD |
| **Fully Diluted Valuation** | $6,021,855,815 |
| **Market Cap / FDV Ratio** | **~0.34 (heavy dilution overhang)** |

**Emissions, unlocks & dilution (the central risk).** WLD has a **10B max supply** and only ~3.41B circulates — **FDV is ~3x market cap**, one of the heaviest unlock overhangs among large-cap tokens. Two emission vectors run continuously: (1) **scheduled unlocks** of insider/Tools-for-Humanity and investor (a16z, Bain, Coinbase Ventures, Multicoin, Blockchain Capital) allocations, and (2) **WLD grants** to newly Orb-verified users (the user-acquisition subsidy). Both add sell pressure. The original allocation skewed heavily toward the team/investors/foundation with a long vesting tail. **Trading consequence**: WLD is a structurally heavy chart — "short-the-rip into unlock windows" has been a recurring trade, and rallies (like the +26% week to 2026-06-20) must absorb ongoing supply to persist. Circulating rose ~+150M WLD from the April snapshot (~3.26B) to June (~3.41B), evidence of the steady emission drip. See [[token-unlocks]].

---

## Price History

> *Authoritative current figures are in the [[worldcoin-wld#Market Data\|Market Data]] block (2026-06-20). Table below is long-horizon reference.*

| Metric | Value |
|---|---|
| **All-Time High** | $11.74 (2024-03-10) — -94.87% |
| **All-Time Low** | $0.230306 (2026-05-18) — +161.55% |
| **24h Change (2026-06-20)** | -7.31% |
| **7d Change (2026-06-20)** | +26.08% |

---

## Platform & Chain Information

**Native Chain:** Ethereum (plus World Chain L2 and Optimism)

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x163f8c2467924be0ae7b5347228cabf260318753` |
| World Chain | `0x2cfc85d8e48f8eab294be644d9e25c3030863003` |
| Optimistic Ethereum | `0xdc6ff44d5d932cbd77b52e5612ba0529dc6226f1` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair |
|---|---|
| Binance | WLD/USDT |
| Kraken | WLD/USD |
| Upbit | WLD/KRW |
| Bitget | WLD/USDT |
| KuCoin | WLD/USDT |
| Crypto.com Exchange | WLD/USD |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| [[hyperliquid|Hyperliquid]] | WLD-PERP | Perpetual |
| Uniswap V3 (Ethereum) | WLD/WETH | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://world.org/](https://world.org/) (formerly worldcoin.org) |
| **Twitter** | [@worldcoin](https://twitter.com/worldcoin) |
| **Telegram** | [worldcoin](https://t.me/worldcoin) (120,461 members, April 2026) |
| **Discord** | [https://discord.com/invite/worldnetwork](https://discord.com/invite/worldnetwork) |
| **Whitepaper** | [https://whitepaper.world.org/](https://whitepaper.world.org/) |

---

## Ecosystem & Use Cases

- **Proof-of-personhood** — World ID as a sybil-resistance / bot-filter primitive for airdrops, voting, social, and AI-era "human-only" gating. The flagship use case.
- **World App + Mini Apps** — consumer super-app hosting payments, the WLD economy, and third-party Mini Apps reachable by verified humans.
- **World Chain** — own OP-stack [[layer-2|L2]] giving verified humans priority blockspace; hosts the in-app economy.
- **Grants / quasi-UBI** — recurring WLD grants to verified users, the project's user-acquisition and "universal access" mechanism (and an emission source).
- **Identity-as-infrastructure** — integrations where platforms require unique-human verification (potentially incl. AI-service access controls, given the OpenAI tie).

---

## Market Structure & Derivatives

- **Spot venues**: deep books on Binance (price leader), [[kraken|Kraken]], Upbit (KRW — Korean retail is a major flow driver), Bitget, KuCoin, Crypto.com.
- **Perps & funding**: WLD-PERP on [[hyperliquid|Hyperliquid]], Binance, Bybit, OKX. WLD is a perennial high-OI perp because of its headline reflexivity; after a +26% week, **funding likely turned sharply positive (longs paying)** — crowded-long squeeze risk is elevated.
- **Liquidity & volatility**: ~$445M 24h volume on a ~$2.06B cap = **~21% turnover**, by far the highest in this set — WLD is a fast, news-driven, high-beta vehicle. The -7.3% day inside a +26% week shows how violently it whipsaws.
- **Korean premium**: Upbit KRW flow can drive temporary kimchi-premium dislocations; watch for cross-venue divergence.

---

## Valuation Framework

WLD has minimal fundamental cash flow; value it on **adoption, narrative, and net-of-dilution supply**:

- **Verified users / Orb deployments** — the core fundamental: World App users (~25–33M) and Orb-verified humans (~12–15M), plus Orb rollout pace (esp. the 7,500-Orb US plan). Verification growth is the demand proxy.
- **World ID integrations** — number/quality of platforms requiring World ID (the network-effect driver).
- **Net supply growth** — unlocks + grants minus any sinks; with FDV ~3x market cap, dilution is the dominant valuation variable. Always frame WLD on **FDV, not just market cap**.
- **Narrative beta** — WLD's price is heavily a function of AI/Altman/OpenAI headline flow rather than protocol revenue; it trades as the listed call option on "AI needs proof-of-humanity."
- **Regulatory discount** — biometric-privacy bans/reinstatements are binary repricing events; apply a regulatory risk discount.

There is no clean multiple — WLD is a narrative + adoption asset with a heavy supply discount.

---

## Trading Playbook

- **AI-identity headline beta** — WLD is the purest listed proxy for [[artificial-intelligence|AI]]-x-crypto and digital-identity news; it spikes on Sam Altman/[[openai|OpenAI]] product launches (historically GPT/Sora releases pumped WLD). Trade it as the headline vehicle.
- **Short-the-rip into unlocks** — the structural heavy chart (FDV ~3x cap) makes fading rallies into known unlock windows a recurring edge; the +26% week into a Fear & Greed of 22 is exactly the kind of move supply tends to cap.
- **Binary regulatory event trades** — biometric bans (Brazil, Indonesia, Kenya, EU actions) and reinstatements move WLD sharply in both directions; size for two-way binary risk.
- **US Orb-rollout milestones** — deployment progress (7,500-Orb US plan) and US-access news are bullish catalysts.
- **Crowded-long caution** — after a sharp rally, check perp funding/OI for squeeze risk before chasing.
- **Risk in extreme fear** — high turnover + dilution + extreme fear = whipsaw central; use defined risk and respect the -98% peak-to-trough history.

---

## History

| Date | Event |
|---|---|
| 2019–2021 | Worldcoin founded (Sam Altman, Alex Blania); Tools for Humanity builds the Orb |
| 2023-07 | Worldcoin mainnet + WLD token launch; global Orb verification rollout |
| 2024-03 | WLD all-time high $11.74 (AI-narrative peak) |
| 2024 | Spain & Portugal suspensions over biometric data |
| 2024-10 | Rebrand Worldcoin → **World Network**; World Chain L2 |
| 2025-01 | Brazil halts compensated iris scanning |
| 2025-05-01 | **US launch** (Atlanta, Austin, LA, Miami, Nashville, SF; Razer stores); 7,500-Orb US plan |
| 2025-05 | $135M raise from a16z + Bain Capital Crypto; Kenya court orders biometric data deletion |
| 2025-09 | ~33M World App users, ~15M Orb-verified |
| 2026-05-18 | WLD all-time low $0.230306 |
| 2026-06-20 | WLD $0.602, #43, +26% on the week, -7.3% on the day, in an extreme-fear market |

---

## Competitive Positioning

| Project | Approach to proof-of-personhood / identity | Edge vs World | World's Edge |
|---|---|---|---|
| Humanity Protocol | Palm-biometric PoP (no eye scan) | Less invasive biometric; privacy-friendlier perception | Scale (millions verified), Orb infrastructure, OpenAI/Altman backing |
| Civic | Identity verification (KYC-style) | Compliance/KYC focus | Anonymity-preserving uniqueness without doxxing |
| Gitcoin Passport | Aggregated web2/web3 sybil scoring | No hardware needed | Stronger uniqueness guarantee (one human = one ID) |
| BrightID | Social-graph PoP | No biometrics | Harder to game than social graphs |
| Idena | Proof-of-person via synchronized puzzles | Fully decentralized, no hardware | Far larger user base and distribution |

World's moat is **scale + hardware + the Altman/OpenAI association**: tens of millions verified, a global Orb network, and the strongest AI-identity narrative. Its handicaps are **biometric-privacy backlash/regulation**, the **invasiveness of iris scanning** vs softer competitors, and the **heavy token dilution**. The thesis is binary: if proof-of-humanity becomes essential infrastructure in an AI world, World is the leader; if biometrics are regulated out, the moat erodes.

---

## Risks

- **Dilution (primary)** — FDV ~3x market cap; relentless unlocks + grant emissions are a structural headwind. WLD must be analyzed on FDV. See [[token-unlocks]].
- **Biometric-privacy regulation** — bans/suspensions across jurisdictions (Spain, Portugal, Brazil, Indonesia, Kenya, EU scrutiny) are an ever-present binary tail risk; the entire model depends on legally collecting iris data.
- **Extreme drawdown profile** — -98% ATH-to-ATL; high beta and reflexivity mean violent moves in both directions.
- **Narrative dependence** — price tracks Altman/OpenAI headlines more than protocol fundamentals; sentiment can reverse fast.
- **Centralization** — Tools for Humanity and insiders hold large allocations and control Orb manufacturing/rollout; "decentralized" claims are aspirational.
- **Adoption risk** — if World ID integrations and verified-user growth stall, the demand side cannot absorb emissions.
- **Crowded-long squeeze** — after sharp rallies (e.g. +26% week to 2026-06-20), positive funding/high OI raise squeeze risk.

---

## Related

- [[proof-of-humanity]] — the concept WLD operationalizes
- [[openai]] / [[artificial-intelligence]] / [[decentralized-ai]] — the correlated narrative
- [[ethereum]] — settlement layer; World Chain is an OP-stack L2
- [[layer-2]] — World Chain context
- [[token-unlocks]] — the dominant supply-overhang dynamic
- [[hyperliquid]] — WLD-PERP venue
- [[narrative-trading]], [[crypto-markets]]

---

## Sources

- Market data 2026-06-20: cryptodataapi.com / CoinGecko markets snapshot (`raw/data/crypto-loop/coingecko-markets.json`)
- CoinGecko top-1000 snapshot, 2026-04-09 (Source: [[coingecko-top-1000-2026-04-09]])
- BeInCrypto: World expands "Proof of Human" network to US (2025-05-01 launch) — https://beincrypto.com/world-launch-in-us/
- FXStreet (2025-05-21): WLD rallies as Worldcoin Foundation raises $135M — https://www.fxstreet.com/cryptocurrencies/news/wld-rallies-as-worldcoin-foundation-raises-135-million-for-network-expansion-202505212113
- Wikipedia: World (blockchain) — https://en.wikipedia.org/wiki/World_(blockchain)
- Blockchainreporter (2026): Worldcoin network activity at 2026 highs, WLD above $0.408 — https://blockchainreporter.net/worldcoin-network-activity-explodes-to-2026-highs-as-wld-tops-0-408/
- World.org blog: What is Worldcoin (WLD) — https://world.org/blog/how-to/what-is-worldcoin-wld-and-how-to-use-it
- Verified via Perplexity sonar + web search, 2026-06-10.

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 3.54B WLD |
| **Total Supply** | 10.00B WLD |
| **Max Supply** | 10.00B WLD |
| **Fully Diluted Valuation** | $3.97B |
| **Market Cap / FDV Ratio** | 0.35 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $164.11M |
| **Market Cap Rank** | #57 |
| **24h Range** | $0.3945 — $0.4195 |
| **CoinGecko Sentiment** | 82% positive |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Trading Profile

**Venues & liquidity.** WLD is a deep, liquid **two-venue** name, tradable on **both Binance** (spot + USD-margined perp) **and [[hyperliquid|Hyperliquid]]** (WLD-PERP, up to ~40-50x leverage), on top of broad spot listings (Kraken, Upbit KRW, Bitget, KuCoin, Crypto.com). The dual centralized/on-chain perp footprint means execution can be sized meaningfully — Binance is the price leader with the deepest book, while Hyperliquid's on-chain order book supports high-leverage directional and funding trades. This availability across venues enables cross-market execution (spot-vs-perp, CEX-vs-DEX) and lets larger positions be worked without single-venue slippage, though WLD's news-reflexive spikes can thin depth abruptly during headline events.

**Applicable strategies.**
- [[narrative-trading]] — WLD is the market's purest listed proxy for the AI-identity narrative; it moves hardest on Sam Altman/OpenAI headlines and US Orb-rollout milestones.
- [[token-unlock-supply-event]] — a 10B max supply with only ~⅓ circulating (MC/FDV ~0.34) makes scheduled unlocks and grant emissions a recurring, tradable supply catalyst.
- [[crowded-long-funding-fade]] — after sharp AI-narrative rallies (e.g. the +26% week), positive funding and high perp OI set up crowded-long fades and squeeze risk.
- [[hl-vs-cex-funding-divergence]] — with liquid perps on both Hyperliquid and Binance, funding can diverge between venues, allowing rate-capture across the two books.
- [[liquidation-cascade-fade]] — WLD's high beta and reflexive whipsaws (a -7.3% day inside a +26% week) produce liquidation-driven overshoots to fade.
- [[event-driven-trading]] — binary biometric-privacy regulatory bans/reinstatements and exchange listing/delisting actions are discrete, repriceable catalysts.

**Volatility & regime character.** WLD is a **high-beta AI-narrative / digital-identity alt** — one of the most news-reflexive large caps, with extreme turnover (~21% on 2026-06-20) and a violent drawdown history (-98% ATH-to-ATL). It broadly carries high beta to BTC/ETH in risk-on/risk-off swings but decouples upward on idiosyncratic AI/Altman/OpenAI flow, making it a headline-driven vehicle rather than a clean market-beta trade. Regime is reflexive and momentum-prone on the way up, supply-capped and mean-reverting into unlock windows.

**Risk flags.**
- **Dilution / supply overhang** — FDV ~3x market cap; continuous insider unlocks + grant emissions are a structural headwind (analyze on FDV). See [[token-unlocks]].
- **Narrative dependence** — price tracks Altman/OpenAI headlines more than fundamentals; sentiment can reverse abruptly.
- **Regulatory tail risk** — biometric-privacy bans/suspensions (Spain, Portugal, Brazil, Indonesia, Kenya, EU scrutiny) are binary two-way events.
- **Perp funding dislocations** — high-OI reflexive perp; funding can swing sharply positive after rallies, elevating crowded-long squeeze risk.
- **Venue/flow concentration** — Upbit KRW (Korean retail) can drive kimchi-premium dislocations and cross-venue divergence.

---

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/summary?coin=WLD` — all-in-one perp data (mark, funding, OI)
- `GET /api/v1/hyperliquid/prices` — all mid prices
- `GET /api/v1/hyperliquid/l2-book?coin=WLD` — L2 order-book depth
- `GET /api/v1/hyperliquid/open-interest` — all-asset open interest

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=WLD&interval=1h&limit=1000` — OHLCV candles
- `GET /api/v1/hyperliquid/funding-rates?coin=WLD&limit=100` — funding history
- `GET /api/v1/daily/hyperliquid` — daily bulk snapshot of ~230 HL perps

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/summary?coin=WLD"
```

Auth: `X-API-Key` header. Endpoint catalog: [[cryptodataapi-hyperliquid]]. See also [[cryptodataapi]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---
