---
title: "Sonic"
type: entity
created: 2026-04-09
updated: 2026-06-21
status: excellent
tags: [crypto, defi]
aliases: ["S", "Fantom", "FTM"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://soniclabs.com"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[layer-1]]", "[[fantom]]", "[[proof-of-stake]]", "[[hyperliquid]]", "[[fear-and-greed-index]]"]
---

# Sonic

**Sonic** (ticker **S**) is a high-throughput, EVM-compatible [[layer-1]] blockchain, marketed as the highest-performing EVM L1 with up to 400,000 TPS and sub-second finality. Sonic is the rebrand and successor of **[[fantom|Fantom]] (FTM)**; FTM holders migrated 1:1 to the S token as the network relaunched under the Sonic Labs banner.

Its headline mechanism is **Fee Monetization (FeeM)**, which rewards developers with up to 90% of the fees their applications generate — adapting the Web2 ad-revenue model to a decentralized framework so builders profit directly from app traffic. The **Sonic Gateway** provides a native, fail-safe bridge to [[ethereum|Ethereum]] for liquidity access.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | S |
| **Current Price** | $0.0284923 |
| **Market Cap** | $107,878,736 (~$107.9M) |
| **Market Cap Rank** | #258 |
| **24h Volume** | $29,759,836 (~$29.8M) |
| **24h Change** | -10.22% |
| **7d Change** | -8.26% |
| **Fully Diluted Valuation** | ~$110.7M |
| **All-Time High** | $1.029 (2025-01-04) — now ~-97.2% |
| **All-Time Low** | $0.02766021 (2026-06-20) — now ~+2.7% |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

S is down sharply on the 24h horizon (-10%) and on the week, trading roughly 97% below its January 2025 all-time high, and made a fresh all-time low on 2026-06-20, the day before this snapshot. Notably, 24h turnover of ~$29.8M is large relative to a ~$108M cap (a ~0.28 volume/mcap ratio), so S remains heavily traded despite the de-rating. The weakness aligns with an extreme-fear market backdrop (crypto [[fear-and-greed-index|Fear & Greed Index]] 23, an "Established Bear Market" regime as of 2026-06-21).

---

## Technology & Consensus

Sonic is a standalone [[layer-1]], not an [[ethereum|Ethereum]] rollup, but it is fully EVM-equivalent so Solidity contracts and standard tooling port directly. Its design centers on raw performance and a developer-revenue model:

- **Consensus:** a leaderless, asynchronous Byzantine-Fault-Tolerant [[proof-of-stake]] design (the evolution of Fantom's Lachesis aBFT DAG consensus), targeting **sub-second finality** and headline throughput up to ~400,000 TPS in benchmarks.
- **SonicVM / SonicDB:** a re-engineered execution client and database layer claimed to cut storage requirements and speed up state access versus the legacy Fantom client.
- **Fee Monetization (FeeM):** the signature mechanism — apps can register to receive up to **90% of the gas fees** they generate, turning network usage into direct builder revenue. This is the main carrot used to recruit developers.
- **Sonic Gateway:** a native, "fail-safe" bridge to Ethereum designed so user funds can be recovered even if the bridge operators fail to act, addressing a major historical L1/bridge risk.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~3.78B S |
| **Total Supply** | ~3.89B S |
| **Max Supply** | Uncapped (inflationary) |
| **Fully Diluted Valuation** | ~$110.7M |
| **Market Cap / FDV** | ~0.97 |

S is the native gas, staking, and governance token of the Sonic L1, inherited from the **[[fantom|Fantom]] (FTM)** 1:1 migration. A market-cap/FDV ratio near **0.97** means almost the entire supply is already circulating — there is little near-term unlock overhang, which is favorable relative to many newer L1s. However, Sonic's max supply is uncapped: the protocol issues ongoing emissions for validator staking rewards and ecosystem/airdrop incentive programs, so **inflation rather than cliff unlocks is the primary dilution vector**. Because S originates from an established, widely distributed FTM base, supply concentration is lower than for freshly launched peers like [[berachain-bera|BERA]].

---

## Market Structure & Derivatives

### Spot venues (centralized)

| Exchange | Pair |
|---|---|
| Binance | S/USDT |
| Kraken | S/USD |
| Bitget | S/USDT |
| KuCoin | S/USDT |
| Crypto.com Exchange | S/USD |

### Derivatives

| Venue | Instrument | Type |
|---|---|---|
| [[hyperliquid|Hyperliquid]] | S-PERP | Perpetual |
| Binance Futures / Bybit / OKX | S perps | Perpetual (CEX) |

S enjoys deep centralized liquidity via Binance and is available as a perpetual on [[hyperliquid|Hyperliquid]] (and major CEX derivatives venues) for leveraged exposure with on-chain [[funding-rate|funding]] and open-interest. On-chain, native DEXs within the Sonic ecosystem (Shadow, Beets/BeethovenX, etc.) provide spot liquidity for S and ecosystem tokens. The relatively high spot turnover suggests reasonable depth for retail-to-mid size, though a sub-$110M cap still implies slippage on large clips.

---

## Use Case, Narrative & Category

Sonic sits in the **high-throughput EVM L1 / DeFi infrastructure** category. CoinGecko tags include Smart Contract Platform, Layer 1 (L1), Galaxy Digital Portfolio, and Sonic Ecosystem.

The investment narrative rests on three pillars: (1) raw performance (400k TPS, sub-second finality) as a home for high-frequency DeFi; (2) the **FeeM** developer-incentive flywheel intended to attract builders by sharing fee revenue; and (3) continuity from the established [[fantom|Fantom]] ecosystem and brand, including a pre-existing DeFi user base and developer community. Sonic competes directly with other performance-focused L1s and L2s for DeFi total value locked (TVL) and active builders.

---

## Valuation Framing (qualitative)

With MC/FDV ~0.97, Sonic's market cap and FDV are nearly equal — the market is already pricing essentially the full current supply, so future *dilution* is driven by ongoing emissions, not unlock cliffs. That removes one common overhang versus newer L1 peers, but it shifts the valuation question onto **organic demand**: does FeeM and the Fantom legacy translate into sustained TVL and fee revenue large enough to absorb staking emissions? Trading ~97% off ATH and on fresh lows, the market is pricing skepticism. A re-rating would likely track measurable TVL/fee recovery and developer retention rather than benchmark TPS claims. This is framing, not a price target.

---

## Peer Comparison

| Token | Symbol | Category | Mkt Cap | Rank | MC/FDV | Notes |
|---|---|---|---|---|---|---|
| **Sonic** | S | High-TPS EVM L1 | ~$107.9M | #258 | ~0.97 | Ex-[[fantom\|Fantom]] rebrand; FeeM |
| [[berachain-bera\|Berachain]] | BERA | DeFi-native L1 (PoL) | ~$63.5M | #381 | ~0.51 | Tri-token; heavier dilution |
| [[ontology\|Ontology]] | ONT | DID / trust L1 | ~$45.8M | #487 | ~1.00 | Dual-token ONT/ONG |
| [[nano\|Nano]] | XNO | Feeless payments L1 | ~$48.7M | #464 | ~1.00 | Fixed supply, no smart contracts |

*(Comparison figures from the same 2026-06-21 snapshot.)* Among these, Sonic has the largest market cap and the most favorable dilution profile (MC/FDV ~0.97) of the genuinely emissions-bearing L1s.

---

## Notable History

- **Fantom → Sonic rebrand:** Sonic is the relaunch of [[fantom|Fantom]], with FTM migrating 1:1 to the S token; this carries over an existing developer community and DeFi history.
- **All-time high:** $1.029 on 2025-01-04, near the relaunch hype peak.
- **All-time low:** $0.02766021 on 2026-06-20 — a fresh cycle low set the day before this snapshot, consistent with the broader bear market.
- The token's ~97% drawdown from ATH reflects both the cycle-wide de-rating of L1 tokens and S's high beta.

---

## Risks

- **Inflation/emissions:** uncapped supply with ongoing staking and incentive emissions creates structural sell pressure even without large unlock cliffs.
- **L1 competition:** the high-TPS niche is crowded; capturing durable DeFi TVL and developer mindshare against rivals (and against L2s) is far from guaranteed.
- **Incentive sustainability:** FeeM and airdrop-style incentives can attract mercenary capital that leaves when rewards taper.
- **Bear-market beta:** with [[fear-and-greed-index|Fear & Greed]] at 23 (extreme fear) and an established bear-market regime, and S at fresh lows, small-cap L1s carry elevated downside and liquidity risk.
- **Volatility / liquidity:** ~$108M market cap makes S a small-cap, high-volatility asset prone to sharp moves and slippage despite active turnover.

---

## Related

- [[crypto-markets]]
- [[fantom]] — the predecessor network (FTM → S migration)
- [[ethereum]] — bridged liquidity via Sonic Gateway
- [[layer-1]]
- [[proof-of-stake]] — aBFT consensus family
- [[hyperliquid]] — venue for S perpetuals
- [[fear-and-greed-index]] — macro sentiment gauge
- [[berachain-bera]], [[ontology]], [[nano]] — L1 peers

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data snapshot 2026-06-21 (cryptodataapi.com / CoinGecko; `raw/data/crypto-loop/coingecko-markets.json`).
- General market knowledge; no specific wiki source ingested yet.
