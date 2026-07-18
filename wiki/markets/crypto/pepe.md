---
title: "PEPE"
type: entity
created: 2026-04-06
updated: 2026-07-16
status: excellent
tags: [crypto, ethereum, memecoins, speculation, hyperliquid, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, altcoins]
entity_type: protocol
aliases: ["PEPE", "PEPE-token", "pepe-coin"]
related: ["[[bitcoin]]", "[[crypto-markets]]", "[[decentralized-exchanges]]", "[[ethereum]]", "[[fartcoin]]", "[[hyperliquid]]", "[[solana]]", "[[uniswap]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[crowded-long-funding-fade]]", "[[long-liquidation-cascade]]"]
headquarters: "Decentralized"
website: "https://www.pepe.vip/"
---

# PEPE

**PEPE** (ticker: PEPE) is an ERC-20 meme coin on [[ethereum]] inspired by the Pepe the Frog internet meme. Stealth-launched in April 2023, it rapidly became one of the **top meme coins by market capitalization**, reaching a multi-billion dollar valuation and earning listings on major centralized exchanges. PEPE is a pure speculation and community-driven token with no protocol, utility, or revenue.

---

## Market Data

| Metric | Value |
|---|---|
| **Market Cap Rank** | #62 |
| **Market Cap** | $1.19B |
| **Current Price** | $0.00000284 |
| **Fully Diluted Valuation** | $1.19B (MC/FDV = 1.00) |
| **24h Volume** | $119.6M |
| **Volume / Market Cap** | ~10% (high turnover) |
| **24h Change** | +1.63% |
| **7d Change** | +0.17% |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

Context: in an **extreme fear** market (Fear & Greed = 23) inside an **Established Bear Market** regime as of 2026-06-20, PEPE is roughly flat — marginally up — over both 24h (+1.6%) and 7d (+0.2%), holding rank #62. Meme coins are typically among the first cohort dumped in risk-off conditions, so PEPE's flat-to-firm tape signals subdued — but not collapsing — speculative appetite. Notably, turnover is high: ~$119.6M of 24h volume against a ~$1.19B cap is a **volume/market-cap ratio near 10%**, far above most large caps and an order of magnitude above thin "float-game" tokens like [[memecore|MemeCore]]. PEPE remains genuinely, actively traded even in extreme fear, and is a useful real-time gauge of meme/risk sentiment across [[crypto-markets]].

---

## Key Facts

| Feature | Detail |
|---|---|
| **Chain** | [[ethereum]] (ERC-20), bridged to Avalanche, BNB Chain, Arbitrum |
| **Launch** | Stealth-launched 2023-04-14 |
| **Supply** | 420.69 trillion tokens (meme-inspired number), fully circulating |
| **Utility** | None -- pure meme/community token |
| **Token type** | [[meme-coin]] (no protocol, no revenue, no governance) |
| **CEX Listings** | [[binance]], [[coinbase]], Kraken, Upbit, Bitget, KuCoin, and others |
| **Market Cap** | ~$1.19B (2026-06-20); multi-billion at peaks |
| **Market Cap Rank** | #62 (2026-06-20) |
| **Contract status** | Renounced / immutable, zero transfer tax, LP locked |

---

## Protocol / Technology

There is, strictly, **no protocol** behind PEPE — and that is the entire point. PEPE is a standard ERC-20 [[meme-coin]] deployed on [[ethereum]], with bridged representations on Avalanche, BNB Chain and Arbitrum One (see contract addresses below). It runs no chain, validates nothing, settles nothing, and produces no fees or revenue. The token contract was **renounced** (no admin keys, immutable code), carries a **zero transfer tax**, and its primary liquidity pool on [[uniswap]] is reported to be **locked**. These three properties — renounced, no tax, locked LP — are the standard "clean memecoin" checklist that distinguishes PEPE from honeypot/rug contracts that retain mint authority or sell taxes.

This is the opposite of a utility token. A protocol token such as [[quant-network|QNT]] or [[ondo-finance|ONDO]] accrues value (in theory) from network usage, gateway licenses, or product fees; PEPE accrues nothing. Its only "technology" is the social layer: a fixed supply, a famous internet meme, and a community. As a result PEPE is best understood as a **pure attention / reflexivity asset** — a bearer claim on collective meme mindshare with no cash-flow floor underneath it. It exists alongside other zero-utility memes such as [[dogecoin]], [[shiba-inu]] and [[fartcoin]], and stands in deliberate contrast to "meme-infrastructure" L1 plays like [[memecore|MemeCore]] that bolt a chain onto the meme narrative.

---

## Market Phenomenon

PEPE's rise illustrated several key dynamics of crypto meme coin trading:

- **Early price discovery on [[uniswap|Uniswap]]** before centralized exchange listings, rewarding [[on-chain-analysis|on-chain]] watchers
- **Massive retail FOMO cycles** driven by social media (Twitter/X, Telegram, Reddit)
- **Extreme volatility** -- 100%+ rallies and 50%+ crashes within days
- **Reflexive momentum** -- price rises attract attention, which attracts buyers, which drives further price rises, until the cycle reverses

---

## Trading Relevance

- PEPE trades as a **sentiment indicator** for meme coin appetite and speculative excess in [[crypto-markets]]
- It demonstrated that meme coins can achieve sustained market caps and exchange listings, not just flash-in-the-pan pumps
- PEPE's [[perpetual-futures|perp]] markets on [[hyperliquid]] and centralized exchanges exhibit elevated funding rates during mania phases
- Meme coins like PEPE are frequently used in funding rate [[arbitrage]] strategies
- Early PEPE buyers who monitored [[uniswap]] launches profited enormously, reinforcing the value of [[on-chain-analysis]] for meme coin trading
- Risk management is critical -- most meme coin positions should be sized as speculative bets, not core holdings

---

## Tokenomics & Supply

| Metric | Value (2026-06-20 snapshot) |
|---|---|
| **Circulating Supply** | 420.69T PEPE |
| **Total Supply** | 420.69T PEPE |
| **Max Supply** | 420.69T PEPE |
| **Fully Diluted Valuation** | $1.19B |
| **Market Cap / FDV Ratio** | 1.00 |

PEPE's supply schedule is the simplest possible: a one-time mint of **420,690,000,000,000 tokens** (the "420.69T" meme number), all in circulation. There are **no future unlocks, no team vesting cliffs, and no emissions** — `circulating = total = max`, so **MC/FDV = 1.00**. This is a genuine structural positive relative to low-float, high-FDV listings: there is no hidden supply waiting to dilute holders, unlike [[ondo-finance|ONDO]] (MC/FDV ≈ 0.49) or insider-controlled meme-L1 [[memecore|MemeCore]] (MC/FDV ≈ 0.24). What you see on the order book is the whole supply.

**On burns — important and honest:** PEPE has **no protocol-level burn mechanism**. Its supply is fixed and fully circulating; the contract is renounced and cannot mint or programmatically burn. Any "burn" you may see referenced is a **community/charity send to a dead address**, not a tokenomic feature, and has negligible effect on the float. Do not model PEPE as a deflationary asset — it is flat-supply by design, and price is driven entirely by demand for that fixed float.

---

## Ecosystem & Use Cases

PEPE has **no ecosystem and no use case beyond speculation and community**. There is no staking, no lending market native to the token, no DeFi protocol, no governance, and no fee-sharing. Its functional role in [[crypto-markets]] is twofold:

1. **A speculative bearer asset** — a liquid way to express a bullish (or, via [[perpetual-futures|perps]], bearish) view on meme/risk appetite.
2. **A sentiment gauge** — because PEPE is one of the largest, most liquid pure memes, its tape is read across the market as a real-time barometer of speculative excess. A ripping PEPE is a classic risk-on tell; a bleeding PEPE often precedes broader altcoin de-risking.

The only "product" the project itself describes is community-building (token-gated groups, newsletters) — see the project's own framing in the Overview section below.

---

## Market Structure & Derivatives

**Spot.** PEPE's price was first discovered on [[uniswap]] (V2/V3) before any centralized listing, rewarding [[on-chain-analysis|on-chain]] watchers who tracked the pool. It now trades on every major CEX — [[binance]], [[coinbase]], Kraken, Upbit, Bitget, KuCoin, Crypto.com — across USDT/USD/KRW/TRY pairs. At ~$119.6M of 24h volume against a ~$1.19B cap (2026-06-20), turnover is **~10% of market cap per day**, very high for a top-100 asset and a sign of genuine, continuous two-sided flow rather than a thin float.

**Perpetual futures.** PEPE is one of the most actively traded meme [[perpetual-futures|perps]] in the market, with deep books on [[hyperliquid]] (PEPE-PERP) and every major CEX perp venue (Binance, Bybit, OKX). The derivatives layer is where most of PEPE's reflexivity plays out, and it must be traded with clear eyes:

- **Funding rates** swing hard. During mania phases, crowded longs push **funding strongly positive** (longs pay shorts), and perp price trades at a premium to spot. In washouts, funding can flip **negative** as shorts pile in. Funding is therefore both a sentiment thermometer and a carry cost.
- **Open interest** balloons on rallies as retail adds leverage, then collapses in liquidation cascades.
- **Leverage and liquidations.** Retail commonly runs 10x–50x on PEPE perps. Because the asset can move 20–50% in a session, **long-liquidation cascades** are routine: a sharp dip triggers stop-outs, forced selling drives price lower, triggering more liquidations — a reflexive downdraft amplified by leverage. The reverse (short squeezes) happens on upside breakouts.
- **Funding-rate [[arbitrage]] / basis trades.** Sophisticated participants run cash-and-carry (long spot / short perp) to harvest positive funding, or fade extreme funding back toward neutral. PEPE's elevated and volatile funding makes it a frequent vehicle for these strategies — but basis can gap violently when the underlying moves.

The honest summary: PEPE perps are a high-octane, retail-heavy arena where leverage manufactures both the upside spikes and the down-cascades. Position sizing and stops matter more than direction.

---

## Valuation Framework (Qualitative)

PEPE has **zero fundamental value** by any conventional measure — no cash flows, no fees, no users-of-a-product, no terminal book value. There is no discounted-cash-flow, no price-to-fees, and no protocol-revenue multiple to anchor a price. What "valuation" exists is purely relative and behavioural:

- **Attention / mindshare share** — PEPE's price is a function of how much of the finite pool of meme-coin attention it commands versus rivals ([[dogecoin]], [[shiba-inu]], [[bonk]], the latest Solana memes).
- **Reflexivity** — rising price *is* the fundamental: it attracts attention, which attracts buyers, which raises price, until the loop reverses.
- **Beta to risk appetite** — PEPE is high-beta to [[bitcoin]] and [[solana]]/altcoin risk-on/risk-off swings; it leads on the way up and on the way down.
- **Relative-cap heuristics** — traders sometimes anchor to "PEPE vs DOGE/SHIB market cap" as a crude ceiling, but this is narrative, not value.

The only honest floor is **zero**: with no cash-flow support, PEPE can revert toward zero if attention permanently rotates away. As of 2026-06-20 it sits ~90% below its December 2024 ATH, a reminder of how far attention-driven assets retrace.

---

## Trading Playbook

- **Momentum / reflexivity longs (risk-on only):** PEPE is a trend vehicle, not a value buy. The high-probability setups are breakouts with confirming volume and rising open interest *while the broader tape is risk-on* — not bottom-fishing in an [[established-bear-market|Established Bear Market]].
- **Funding-rate fades:** when perp funding goes extreme (very positive), fade crowded longs into spot; when funding capitulates negative on a washout, look for short-squeeze snapbacks.
- **Sentiment-indicator read:** use PEPE's tape and funding as a meme/risk barometer for the whole book, even if you don't trade PEPE itself.
- **On-chain launch / flow monitoring:** for the meme cohort broadly, watching [[uniswap]] launches and large [[on-chain-analysis|on-chain]] wallet moves remains the earliest edge.
- **Strict risk sizing:** treat any PEPE position as a speculative bet, not a core holding; assume it can halve overnight and size so a total loss is survivable. Hard stops are mandatory given liquidation dynamics.

---

## History

| Date | Event |
|---|---|
| **2023-04-14** | Stealth launch on [[ethereum]] (Uniswap), zero pre-sale, zero tax, LP locked, contract renounced |
| **2023 (mid)** | First mania wave; rapid CEX listings ([[binance]], others); multi-billion cap reached within weeks |
| **2024-12-09** | All-time high $0.00002803 |
| **2025–2026** | Long drawdown alongside the broader altcoin/meme bear; ~-90% from ATH |
| **2026-06-20** | ~$0.00000284, rank #62, ~$1.19B cap, in an Established Bear Market / extreme-fear regime |

PEPE proved that a pure meme with no roadmap could reach and *sustain* a multi-billion-dollar cap and tier-1 exchange listings — not merely a flash pump — which reshaped how the market treats the meme cohort.

---

## Competitive Positioning

PEPE competes for the same finite pool of speculative attention as the rest of the meme cohort. It is differentiated by being a **clean, fixed-supply, fully-circulating ERC-20 with no insider overhang** — a contrast to float-game tokens.

| Token | Chain | Supply / float | Fundamental value | Liquidity profile | Notes |
|---|---|---|---|---|---|
| **PEPE** | [[ethereum]] (+bridges) | 420.69T, fully circulating (MC/FDV 1.00) | None | Deep spot + very active perps; ~10% daily turnover | Cleanest large meme; sentiment bellwether |
| [[dogecoin]] (DOGE) | Own PoW chain | Inflationary (no cap) | None (payments meme) | Deepest meme liquidity, futures + ETF interest | The original; lowest-beta meme |
| [[shiba-inu]] (SHIB) | [[ethereum]] | ~589T, burns + Shibarium L2 | Minimal (ecosystem attempt) | Deep | Tries to add utility (Shibarium) |
| [[fartcoin]] | [[solana]] | Fixed | None | Active on Solana DEX/perps | Solana-meme-cycle representative |
| [[bonk]] / WIF | [[solana]] | Fixed | None | Active | Solana retail-meme beta |
| [[memecore|MemeCore]] (M) | Own L1 (+BNB) | ~13% of max circulating (MC/FDV ~0.24) | "Meme L1" claim | Thin (~0.2% daily turnover) | Float-game / insider-concentration concerns — opposite of PEPE's clean float |

The takeaway: among large memes, PEPE's tokenomics are unusually trustworthy (no hidden supply, real liquidity), even though its *fundamental* value is — like all of them — effectively zero. Its risk is attention rotation, not dilution.

---

## Risks

- **Zero fundamental value** — PEPE has no protocol, cash flow, or utility; price is driven entirely by attention and reflexive flows, so it can revert toward zero when momentum reverses.
- **Extreme volatility & drawdowns** — 100%+ rallies and 50%+ crashes within days are routine; PEPE sits well below its all-time high.
- **Sentiment / risk-off fragility** — meme coins are typically the first cohort dumped in risk-off regimes; the current **Established Bear Market** and extreme-fear backdrop (2026-06-20) is structurally unfavorable.
- **Perp / leverage risk** — PEPE perps on [[hyperliquid|Hyperliquid]] and CEXs show elevated funding during manias, setting up sharp long-liquidation cascades.
- **Concentration & rug-adjacent dynamics** — although liquidity is reportedly locked and the contract renounced, large-holder concentration and copycat tokens create manipulation and dilution-of-attention risk.
- **Attention rotation** — PEPE's only "moat" is mindshare; a shift of speculative attention to newer memes (or to a different chain's meme cycle, e.g. [[solana]]) can drain bids with no fundamental floor to catch the fall.
- **Liquidation reflexivity** — high retail leverage on [[perpetual-futures|perps]] means downside is self-reinforcing: dips trigger long liquidations that drive further dips. The same reflexivity that powers rallies amplifies crashes.
- **No deflationary support** — PEPE has no protocol burn; do not expect supply mechanics to backstop price (see Tokenomics & Supply).

---

## Trading Profile

### Venues & liquidity

PEPE trades on a **deep, liquid two-venue derivatives market**. On [[binance]] it is available as **spot plus a USD-margined perpetual**, and on [[hyperliquid]] as **PEPE-PERP with leverage up to ~40–50x**. Both books are deep and continuously two-sided — consistent with PEPE's ~10% daily turnover on a ~$1.19B cap — so slippage on standard clip sizes is low and execution is straightforward on either venue. The dual-venue setup is what makes PEPE tradable at scale: an on-chain-native memecoin gains CEX-grade depth on Binance while Hyperliquid supplies a transparent, on-chain perp with its own funding and order book. That parallel availability enables **cross-venue execution** (route the aggressive leg to whichever book is deeper), supports **larger position sizing** than a single-venue meme could bear, and — critically — creates a clean CEX-vs-DEX pair for basis and funding-divergence trades. Note that Hyperliquid quotes the perp as `kPEPE` (price scaled ×1000) for tick precision; size and PnL are unaffected but the mark must be de-scaled when comparing to Binance spot.

### Applicable strategies

- [[crowded-long-funding-fade]] — during meme manias PEPE funding goes strongly positive as retail piles into longs; fade the crowd back toward neutral funding.
- [[crowded-short-funding-fade]] — on washouts funding flips negative as shorts crowd in; fade extreme negative funding for the snapback.
- [[long-liquidation-cascade]] — high retail leverage (10x–50x) makes reflexive long-liquidation downdrafts routine; trade the forced-selling leg.
- [[post-liquidation-rebound]] — PEPE's sharp cascades routinely overshoot, setting up mean-reverting bounces once the liquidation flush exhausts.
- [[hl-vs-cex-funding-divergence]] — with an active Binance perp and Hyperliquid PEPE-PERP, funding can diverge between the two venues; harvest the spread.
- [[cash-and-carry]] — Binance spot plus a short perp lets you harvest PEPE's chronically elevated positive funding as carry.

### Volatility & regime character

PEPE is a **high-beta, reflexive memecoin** — the archetype of an attention-driven bearer asset with zero cash-flow floor. It exhibits classic memecoin reflexivity: rising price attracts attention that attracts buyers, amplifying moves in both directions, with 100%+ rallies and 50%+ crashes within days. It is **high-beta to [[bitcoin]] and to [[solana]]/altcoin risk-on/risk-off swings**, and (being ERC-20) somewhat to [[ethereum]] — it typically leads on the way up and on the way down, making its tape and funding a real-time barometer of speculative excess across the meme cohort. Meme coins are usually the first cohort dumped in risk-off regimes, so PEPE de-risks early in fear-driven drawdowns.

### Risk flags

- **Narrative / attention dependence** — PEPE's only "moat" is mindshare; a rotation of speculative attention to newer memes or another chain's cycle drains bids with no fundamental floor to catch the fall.
- **Perp funding dislocations** — funding swings hard positive in manias and negative in washouts; basis can gap violently when spot moves, so carry/basis trades carry real tail risk.
- **Liquidation reflexivity** — heavy retail leverage means downside is self-reinforcing; long-liquidation cascades amplify dips just as short squeezes amplify rallies.
- **Venue / execution nuance** — while the two-venue market is liquid, the Hyperliquid `kPEPE` ×1000 price scaling must be handled correctly in any cross-venue basis or funding-divergence calc to avoid mispriced legs.
- **No supply overhang, but no supply support** — supply is fixed and fully circulating (no unlocks or emissions), which removes dilution risk but also means there is no burn/deflation mechanic to backstop price.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/summary?coin=kPEPE` — all-in-one perp data (mark, funding, OI)
- `GET /api/v1/hyperliquid/prices` — all mid prices
- `GET /api/v1/hyperliquid/l2-book?coin=kPEPE` — L2 order-book depth
- `GET /api/v1/hyperliquid/open-interest` — all-asset open interest

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=kPEPE&interval=1h&limit=1000` — OHLCV candles
- `GET /api/v1/hyperliquid/funding-rates?coin=kPEPE&limit=100` — funding history
- `GET /api/v1/daily/hyperliquid` — daily bulk snapshot of ~230 HL perps

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/summary?coin=kPEPE"
```

Auth: `X-API-Key` header. Endpoint catalog: [[cryptodataapi-hyperliquid]]. See also [[cryptodataapi]].

## Related

- [[meme-coin]] -- the asset class PEPE belongs to
- [[ethereum]] -- PEPE's home chain
- [[uniswap]] -- where PEPE's price was first discovered
- [[hyperliquid]] -- venue for PEPE perpetual futures
- [[perpetual-futures]] -- the derivatives layer that drives PEPE's reflexivity
- [[arbitrage]] -- funding-rate / basis trades on PEPE perps
- [[on-chain-analysis]] -- the early edge for meme-coin entries
- [[dogecoin]], [[shiba-inu]], [[fartcoin]], [[bonk]] -- peer meme coins
- [[memecore|MemeCore]] -- meme-narrative L1 (float-game contrast)
- [[bitcoin]], [[solana]] -- risk-appetite drivers PEPE is high-beta to
- [[crypto-markets]] -- broader market context for meme coins
- [[decentralized-exchanges]] -- where meme coins first trade

## See Also

- [[fartcoin]] -- Another notable meme coin
- [[ethereum]] -- PEPE's home chain
- [[crypto-markets]] -- Broader market context for meme coins
- [[decentralized-exchanges]] -- Where meme coins first trade

## Overview

What is the project about?
Pepe is a community based meme token surround the iconic meme Pepe the frog. Pepe aims to leverage the power of such an iconic meme to become the most memeable memecoin in existence. 

What makes your project unique?
Pepe is here to make memecoins great again. Ushering in a new paradigm for memecoins, Pepe represents the memecoin in it's purest simplicity. With zero taxes, liquidity locked forever, and contract immutable, Pepe is for the people, forever. Pepe is about culture, rallying together a community to have fun and enjoy memes, fueled purely by memetic power. 

History of your project.
Pepe was stealth launched on Friday, April 14th, 2023. 

What’s next for your project?
Pepe will focus on developing a tight-knit community around the token and building resources to enrich the communities knowledge and success in crypto through a token gated group, newsletter, and more tools. 

What can your token be used for?
Pepe can be used to speculate on the power of memes, and does not pretend to be anything more.

---

## Tokenomics (Snapshot Table)

> *2026-06-20 snapshot. See **Tokenomics & Supply** above for the full discussion.*

| Metric | Value (2026-06-20 snapshot) |
|---|---|
| **Circulating Supply** | 420.69T PEPE |
| **Total Supply** | 420.69T PEPE |
| **Max Supply** | 420.69T PEPE |
| **Market Cap** | $1.19B |
| **Fully Diluted Valuation** | $1.19B |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value (2026-06-20 snapshot) |
|---|---|
| **Current Price** | $0.00000284 |
| **All-Time High** | $0.00002803 (2024-12-09) |
| **Current vs ATH** | -89.87% |
| **All-Time Low** | $0.000000055142 (2023-04-18) |
| **Current vs ATL** | +5049.17% |
| **24h Change** | +1.63% |
| **7d Change** | +0.17% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x6982508145454ce325ddbe47a25d4ec3d2311933` |
| Avalanche | `0xa659d083b677d6bffe1cb704e1473b896727be6d` |
| Binance Smart Chain | `0x25d887ce7a35172c62febfd67a1856f20faebb00` |
| Arbitrum One | `0x25d887ce7a35172c62febfd67a1856f20faebb00` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | PEPE/TRY | N/A |
| Kraken | PEPE/USD | N/A |
| Upbit | PEPE/KRW | N/A |
| Bitget | PEPE/USDT | N/A |
| KuCoin | PEPE/USDT | N/A |
| Crypto.com Exchange | PEPE/USDT | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V2 (Ethereum) | 0X6982508145454CE325DDBE47A25D4EC3D2311933/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |
| Uniswap V3 (Ethereum) | 0X6982508145454CE325DDBE47A25D4EC3D2311933/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |
| [[hyperliquid|Hyperliquid]] | PEPE-PERP | Perpetual |

PEPE's early price discovery happened on [[uniswap|Uniswap]] before CEX listings, rewarding [[on-chain-analysis|on-chain]] watchers; today its perp markets (Hyperliquid + CEXs) carry elevated funding during mania phases.

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.pepe.vip/](https://www.pepe.vip/) |
| **Twitter** | [@pepecoineth](https://twitter.com/pepecoineth) |

---

## Trading Characteristics

| Characteristic | Detail (2026-06-20 snapshot) |
|---|---|
| **24h Volume** | $119.6M |
| **Volume / Market Cap** | ~10% (high turnover) |
| **Market Cap Rank** | #62 |
| **Current Price** | $0.00000284 |
| **Backdrop** | Fear & Greed = 23 (extreme fear); Established Bear Market |
| **Last Updated** | 2026-06-20 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 420.69T PEPE |
| **Total Supply** | 420.69T PEPE |
| **Max Supply** | 420.69T PEPE |
| **Fully Diluted Valuation** | $1.15B |
| **Market Cap / FDV Ratio** | 1.00 |

---
