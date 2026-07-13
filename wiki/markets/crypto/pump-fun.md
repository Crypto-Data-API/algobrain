---
title: "Pump.fun"
type: entity
created: 2026-04-09
updated: 2026-07-13
status: excellent
tags: [crypto, defi]
aliases: ["PUMP", "pumpdotfun"]
entity_type: protocol
founded: 2024
headquarters: "Decentralized"
website: "https://pump.fun"
related: ["[[crypto-markets]]", "[[solana]]", "[[pumpswap]]", "[[letsbonk]]", "[[bonk]]", "[[memecoin-mania]]", "[[hyperliquid]]", "[[pump-fun-bonding-curve-sniping]]", "[[cryptodataapi]]"]
---

# Pump.fun

**Pump.fun** (PUMP) is the dominant [[solana|Solana]] memecoin launchpad — the bonding-curve factory behind the 2024–2025 memecoin supercycle — and PUMP is its token, launched via one of the largest ICOs in crypto history (July 2025, ~$600M raised at $0.004). The platform monetizes token-creation and trading fees (plus its own AMM, [[pumpswap|PumpSwap]]) and routes a share of revenue into PUMP buybacks and burns, making PUMP effectively a cash-flow claim on Solana [[meme-coin|memecoin]] activity. As of 2026-06-20 it sits at **rank #107**, ~$476M market cap.

---

## Market Data

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

| Metric | Value |
|---|---|
| **Price** | $0.00137261 |
| **Market Cap** | $475,666,412 (~$476M) |
| **Market Cap Rank** | #107 |
| **Fully Diluted Valuation** | $1,176,308,812 (~$1.18B) |
| **MC / FDV** | **0.40** (≈60% of max supply not yet circulating) |
| **24h Volume** | $33,245,147 (~$33.2M) |
| **24h Change** | -1.42% |
| **7d Change** | -10.99% |
| **24h Range** | $0.00135507 — $0.00139619 |
| **Circulating Supply** | 346.55B PUMP |
| **Total Supply** | 857.01B PUMP |
| **Max Supply** | 1.00T PUMP |
| **All-Time High** | $0.00881908 (2025-09-14) — **-84.44%** from ATH |
| **All-Time Low** | $0.00131641 (2026-06-06) — **+4.27%** from ATL |

> **Dilution alert.** FDV (~$1.18B) is **~2.5x** the circulating market cap (~$476M) — MC/FDV ≈ 0.40 means **~60% of max supply is not yet circulating** (max 1T vs ~347B circulating). Even after the April 2026 mega-burn, future emissions remain a meaningful overhang and must be weighed against the buyback/burn demand sink.

**Macro backdrop (2026-06-20):** Crypto Fear & Greed Index = **23 (Extreme Fear)**; *Established Bear Market*. PUMP is -11% on the week and trades just **+4.3% above its 2026-06-06 ATL** ($0.00131641) — i.e. hovering at all-time lows. The buyback/burn regime is now competing against memecoin-cycle decay and risk-off flows.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | PUMP |
| **Asset class** | Launchpad / exchange-token hybrid (Solana SPL) |
| **Market Cap Rank** | #107 (2026-06-20; #67 at 2026-04-09 snapshot) |
| **Market Cap** | ~$476M at $0.00137261 (2026-06-20); FDV ~$1.18B (MC/FDV ≈ 0.40) |
| **Token launch** | 2025-07 ICO at $0.004; ~$600M raised (reported) |
| **Supply mechanics** | 1T max; ~347B circulating, ~857B total after the April 2026 mega-burn; ongoing revenue-funded buybacks |
| **Categories** | Launchpad, DEX, SocialFi, AMM, Solana Ecosystem, Meme, Exchange-based Tokens |
| **Website** | [https://pump.fun](https://pump.fun) |

---

## Overview

Pump.fun launched in January 2024 and industrialized memecoin creation: anyone can deploy a token on a bonding curve for ~free; tokens that "bond" (complete the curve) graduate to AMM liquidity (originally [[raydium|Raydium]], later Pump.fun's own [[pumpswap|PumpSwap]]). At peak it generated more daily revenue than most L1s and has accounted for the majority of new token launches on Solana. The PUMP token added a value-capture layer on top: platform fees fund buybacks/burns and creator revenue-sharing programs ("Project Ascend"-style fee splits introduced August 2025).

## Major News & Events (2025–2026)

- **2025-07 — PUMP ICO**: ~$600M raised (reported; public sale sold out in minutes at $0.004), one of the largest token sales ever. Around the same time Pump.fun acquired wallet-tracker **Kolscan**.
- **2025-H2 — Launchpad wars**: [[letsbonk|LetsBonk]] (BONK ecosystem) briefly flipped Pump.fun in daily launches/graduations in July 2025; Pump.fun responded with fee cuts, creator revenue sharing, and aggressive PUMP buybacks. ATH $0.00882 on 2025-09-14.
- **2026-Q1 — Revenue machine**: ~**$124.7M app revenue in Q1 2026**, over 30% of all Solana application revenue (~$342M).
- **2026-04-28/29 — Mega-burn + policy shift**: one-time burn of **~$370M of PUMP (~36% of circulating supply)**; going forward **50% of net profits** committed to automated buybacks for the next year (down from 100%).
- **2026-05-21 — USDC bonding curves**: new launches can use USDC-quoted curves instead of SOL, insulating new tokens from SOL volatility.
- **2026-05-29 — Treasury flows**: cumulative SOL fee-revenue sales reached ~**$780M** (latest tranche 100,628 SOL ≈ $8.3M) — a persistent structural SOL sell-flow worth tracking.
- **2026 — GO bounty marketplace** launched; drew controversy (viral tattoo-bounty incident).

---

## Protocol & Project — Launchpad Mechanics, PUMP Token & Fee Buybacks

Pump.fun is an *infrastructure* play, not a memecoin — it is the factory, and PUMP is a cash-flow claim on the factory's output.

### Launchpad mechanics (bonding curves)

- Anyone can deploy a token for ~free. Each new token starts on a **bonding curve**: buyers purchase along a deterministic price curve, and the curve's reserves accumulate as the token rises.
- When a token's curve fills ("**bonds**"/"graduates"), it migrates to AMM liquidity — originally [[raydium|Raydium]], now Pump.fun's own AMM **[[pumpswap|PumpSwap]]**, capturing the trading-fee stream in-house.
- **2026-05-21 — USDC bonding curves**: new launches can use USDC-quoted curves instead of SOL, insulating new tokens from [[solana|SOL]] volatility and broadening the user base.
- This bonding-curve design is what industrialized memecoin issuance and made Pump.fun the majority of Solana token launches. (Strategy note: [[pump-fun-bonding-curve-sniping]].)

### The PUMP token & fee buybacks

- **Value capture** — platform fees (creation + trading + PumpSwap AMM fees) fund **buybacks and burns** of PUMP, plus creator revenue-sharing ("Project Ascend"-style fee splits, Aug 2025). PUMP therefore behaves like an **exchange/fee token**: its fundamental tape is platform revenue, buyback rate, and burn schedule.
- **2026 regime shift** — after the April 2026 mega-burn (~$370M of PUMP, ~36% of circulating supply), the policy moved from 100% of net profits → **50% of net profits committed to automated buybacks** for the following year. Less aggressive, but still a structural demand sink tied to revenue.
- **GO bounty marketplace** (2026) — a bounty product layered on top (drew controversy via a viral tattoo-bounty incident).

This is the key distinction from the memecoins in this comparison set: PUMP has a *real revenue stream* and an explicit value-capture mechanism, making it valuable to model like an exchange token rather than a pure attention asset.

---

## Tokenomics & Supply

| Metric | Value (2026-06-20) |
|---|---|
| **Circulating Supply** | 346.55B PUMP |
| **Total Supply** | 857.01B PUMP |
| **Max Supply** | 1.00T PUMP |
| **Fully Diluted Valuation** | $1,176.31M (~$1.18B) |
| **Market Cap / FDV Ratio** | **0.40** |

**Dilution profile — flag heavily.** Despite the April 2026 burn of ~36% of circulating supply, **MC/FDV ≈ 0.40 means ~60% of max supply (1T) is not yet in circulation** (circulating ~347B, total ~857B, max 1T). FDV (~$1.18B) is ~2.5x the float market cap (~$476M). The gap between *total* (857B) and *max* (1T) plus the locked allocations represents future emissions to team/ecosystem/investor pools. The crucial tension for PUMP holders: **buyback-and-burn demand vs ongoing emission supply.** The April 2026 burn improved the ratio (from ~0.59 in April) but did not eliminate the overhang — net token deflation depends on revenue staying high enough that buyback-burn outpaces emissions.

---

## Ecosystem & Use Cases

- **Token issuance** — the dominant Solana memecoin launchpad; bonding-curve creation + graduation pipeline.
- **[[pumpswap|PumpSwap]]** — Pump.fun's in-house AMM, capturing graduated-token trading fees.
- **Creator revenue-sharing** — fee splits to token creators (Project Ascend), aligning the supply side.
- **PUMP token** — fee-funded buyback/burn value capture; the liquid claim on platform revenue.
- **Kolscan** — acquired wallet-tracker (analytics for traders).
- **GO bounty marketplace** — bounty/task layer on the platform.
- **Tooling** — the bonding-curve API is the backbone for a large ecosystem of sniping bots, scanners, and trading front-ends.

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.00881908 (2025-09-14) |
| **Current vs ATH** | -84.44% |
| **All-Time Low** | $0.00131641 (2026-06-06) |
| **Current vs ATL** | +4.27% |
| **24h Change** | -1.42% |
| **7d Change** | -10.99% |

*Path: $0.00882 ATH (Sep 2025) → ATL $0.00157 (Apr 2026, since broken) → fresh ATL $0.00131641 (2026-06-06) → $0.00137 (2026-06-20), only ~4% above the low.*

---

## Market Structure & Derivatives

- **Spot venues** — deep liquidity on Binance (PUMP/USDT), Kraken, Upbit (PUMP/KRW), Bitget, KuCoin, Crypto.com; Orca/PumpSwap on Solana. ~$33.2M 24h volume (2026-06-20).
- **Perpetuals** — **PUMP-PERP on [[hyperliquid|Hyperliquid]]** and major CEX futures. As a fee-token with memecoin beta, PUMP's [[perpetual-futures|perp]] funding swings with both Solana-app-revenue sentiment and meme risk appetite; buyback/burn announcements can spike funding positive, while emission/cycle-decay fears drive it negative. Liquid enough for funding/basis trades.
- **Funding/basis trade** — trade it like an exchange token: long spot / short perp to harvest positive funding around buyback events; the perp also lets traders short the dilution thesis with depth.
- **SOL-flow linkage** — Pump.fun's own cumulative SOL fee-revenue selling (~$780M by May 2026) is a Solana-ecosystem headwind to monitor alongside PUMP's order book.

---

## Valuation Framework (qualitative)

Unlike the pure memecoins here, PUMP is best valued as a **revenue/fee token (exchange-token framework)**:

1. **Revenue** — the core input: platform fees (creation + trading + PumpSwap). Q1 2026 app revenue was ~$124.7M (>30% of all Solana app revenue). Rising revenue → larger buybacks → demand.
2. **Buyback/burn rate** — the explicit value-capture: 50% of net profits → automated buybacks (post-April-2026). Model the buyback as a recurring bid; compare it to emission supply.
3. **Net supply trajectory** — *the decisive question:* does buyback-burn outpace ongoing emissions? At MC/FDV 0.40, ~60% of supply is still to come; deflation is conditional on sustained high revenue.
4. **Launchpad market share** — Pump.fun vs [[letsbonk|LetsBonk]] vs Believe (see [[pump-fun-vs-letsbonk-vs-believe-vs-moonshot-vs-heaven]]); share = revenue = buyback power. Watch this as the leading indicator.
5. **Memecoin-cycle beta** — revenue is ultimately a derivative of memecoin speculation; in a bear market (current), issuance and fees fall, shrinking the buyback.

Net: "Solana memecoin-activity fee token with a real revenue stream and explicit buyback-burn, valued on revenue × buyback rate net of a large (~60%) emission overhang and cyclical memecoin-volume risk."

---

## Trading Playbook

- **Regime read** — Extreme Fear / Established Bear Market; PUMP is at all-time lows (+4% off ATL) with revenue under cyclical pressure. Trend is down; favor mean-reversion only with tight risk.
- **Fundamental tape** — track **weekly platform revenue, buyback rate, and burn announcements** as you would an exchange token's earnings; the April 2026 burn (+36% supply cut) and the shift to 50% profit buybacks are the key regime changes.
- **Launchpad-share signal** — Pump.fun vs LetsBonk vs Believe market share is the leading indicator for revenue → buyback power.
- **Dilution short** — the ~60% emission overhang (MC/FDV 0.40) is a structural short thesis when revenue/buyback weakens; PUMP-PERP depth supports it.
- **Catalyst trades** — buyback/burn announcements (demand) vs emission-unlock and SOL fee-selling headlines (supply) are two-sided, dated catalysts.
- **ATL watch** — $0.00131641 (2026-06-06) is the key level; a clean break opens fresh price discovery lower.

---

## Competitive Positioning — Launchpads & Fee-Token Peers

| Token / Platform | Role | MC/FDV | Differentiator | Key risk |
|---|---|---|---|---|
| **PUMP (Pump.fun)** | Solana launchpad + AMM fee token | ~0.40 | Dominant launchpad; real revenue + buyback/burn | ~60% emission overhang; cycle-dependent revenue |
| **[[letsbonk|LetsBonk]] / [[bonk|BONK]]** | Rival Solana launchpad (BONK ecosystem) | BONK ~1.00 | Revenue → BONK burn; briefly flipped Pump.fun (Jul 2025) | Launchpad share is volatile |
| **Believe** | Solana launchpad (creator tokens) | n/a | Creator-economy angle | Smaller share; unproven durability |
| **[[raydium|Raydium]] (RAY)** | Solana AMM (original graduation venue) | mature | Established DEX; broad liquidity | Disintermediated as Pump.fun moved to PumpSwap |
| **Exchange tokens (BNB-style)** | CEX fee tokens (reference frame) | varies | Diversified revenue, regulatory standing | Not memecoin-cycle-levered |

PUMP's edge is its launchpad dominance and genuine revenue/buyback value capture (unique among the memes in this set); its weaknesses are the large emission overhang (MC/FDV 0.40) and the fact that its revenue is a derivative of the volatile memecoin cycle.

---

## Risks

- **Emission/dilution overhang** — MC/FDV ≈ 0.40; ~60% of max supply still to emit. Buyback-burn must outpace emissions for net deflation, which is conditional on sustained high revenue.
- **Memecoin-cycle decay** — PUMP printed a fresh ATL (2026-06-06) and trades just above it; revenue (the fundamental) falls when memecoin speculation cools, shrinking the buyback bid.
- **Launchpad competition** — LetsBonk (Jul 2025) and Believe show share can be lost; lost share = lost revenue = weaker buybacks.
- **Self-inflicted SOL sell-flow** — Pump.fun's ~$780M cumulative SOL fee-revenue selling is a Solana-ecosystem headwind that can pressure the whole complex, PUMP included.
- **Regulatory attention** — memecoin-issuance infrastructure is a plausible regulatory target; controversy (e.g., the GO tattoo-bounty incident) adds reputational risk.
- **Buyback-policy risk** — the shift from 100% → 50% profit buybacks shows the policy is discretionary and can be cut further.

---

## Platform & Chain Information

**Native Chain:** Solana

| Chain | Address |
|---|---|
| Solana | `pumpCmXqMfrsAkQ5r49WcJnRayYRqmXz6ae8H7H9Dfn` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair |
|---|---|
| Binance | PUMP/USDT |
| Kraken | PUMP/USD |
| Upbit | PUMP/KRW |
| Bitget | PUMP/USDT |
| KuCoin | PUMP/USDT |
| Crypto.com Exchange | PUMP/USD |

### Decentralized Exchanges / Perps

| Exchange | Pair | Type |
|---|---|---|
| [[hyperliquid|Hyperliquid]] | PUMP-PERP | Perpetual |
| Orca / PumpSwap (Solana) | PUMP/SOL | Spot |

---

## Trading Relevance

- **Narrative basket**: [[memecoin-mania]] / Solana app-revenue beta. PUMP is the cleanest liquid proxy for Solana memecoin activity — it tends to lead/lag SOL with higher beta and reacts to launchpad market-share data (Pump.fun vs [[letsbonk]] vs Believe; see [[pump-fun-vs-letsbonk-vs-believe-vs-moonshot-vs-heaven]]).
- **Cash-flow angle**: trade it like an exchange token — weekly fee revenue, buyback rate, and burn announcements are the fundamental tape. The April 2026 burn (+ ~36% supply cut) and the shift to 50% profit buybacks are the key 2026 regime changes.
- **Venues**: deep spot on Binance/major CEXs (~$33.2M 24h volume, 2026-06-20), PUMP-PERP on [[hyperliquid]] for funding/basis trades.
- **Risks**: memecoin-cycle decay (ATL set 2026-04-02), launchpad competition, regulatory attention on memecoin infrastructure, and the platform's own ~$780M cumulative SOL selling as a Solana-ecosystem headwind.
- Related strategy note: [[pump-fun-bonding-curve-sniping]].

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://pump.fun](https://pump.fun) |
| **Twitter** | [@pumpdotfun](https://twitter.com/pumpdotfun) |

---

## Trading Characteristics

| Characteristic | 2026-06-20 | 2026-04-09 (prior) |
|---|---|---|
| **24h Volume** | $33.25M | $59.19M |
| **Market Cap Rank** | #107 | #67 |
| **Price** | $0.00137261 | (pre-burn pricing) |
| **24h Range** | $0.00135507 — $0.00139619 | — |

Rank fell from #67 to #107 and volume nearly halved April→June 2026 as memecoin-issuance activity (PUMP's revenue base) contracted in the Established Bear Market.

---

## See Also / Related

- [[solana]] — host chain and revenue ecosystem
- [[meme-coin]] — asset class
- [[pumpswap]] — Pump.fun's own AMM
- [[letsbonk]], [[bonk]] — main launchpad rival
- [[raydium]] — original graduation venue
- [[memecoin-mania]] — narrative context
- [[hyperliquid]] — perp venue
- [[perpetual-futures]] — derivatives context
- [[pudgy-penguins]], [[official-trump]], [[spx6900]] — meme peers
- [[pump-fun-vs-letsbonk-vs-believe-vs-moonshot-vs-heaven]] — launchpad comparison
- [[pump-fun-bonding-curve-sniping]] — related strategy

---

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/dex/trending` — trending DEX pools (Solana/Ethereum/Base/BSC/Arbitrum)
- `GET /api/v1/dex/new-pools` — newest launches, multi-chain
- `GET /api/v1/dex/security/{chain}/{address}` — token security report (rug/honeypot detection)
- `GET /api/v1/meme/regime/score` — market-wide meme-hype score + meme_season flag

**Historical data:**
- `GET /api/v1/meme/regime/{symbol}` — per-asset meme lifecycle + 60d history

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/dex/trending"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-dex]].

## Sources

- Market data snapshot 2026-06-20 (cryptodataapi.com / CoinGecko) — current Market Data block
- (Source: [[coingecko-top-1000-2026-04-09]]) — April 2026 market snapshot
- BanklessTimes, "Pump Fun Coin Price Jumps After $370M Token Burn" (2026-04-29) — https://www.banklesstimes.com/articles/2026/04/29/pump-fun-coin-price-jumps-after-370m-token-burn/
- CoinMarketCap Top Stories, "Pump.fun (PUMP) Surges on Buybacks, Revenue, Upgrades" (2026)
- CoinGecko PUMP page — https://www.coingecko.com/en/coins/pump-fun
- Web verification (WebSearch + Perplexity), 2026-06-10
