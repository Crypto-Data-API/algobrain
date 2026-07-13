---
title: "Telegraph Impact on Arbitrage"
type: concept
created: 2026-04-24
updated: 2026-06-11
status: good
tags: [history, arbitrage, market-microstructure, latency]
aliases: ["Transatlantic Cable Arbitrage", "Telegraph and Markets"]
domain: [market-microstructure, history, arbitrage]
prerequisites: ["[[arbitrage]]", "[[market-microstructure]]"]
difficulty: intermediate
related: ["[[gold-point-arbitrage]]", "[[specie-flow-arbitrage]]", "[[bill-broking-arbitrage]]", "[[mint-parity-arbitrage]]", "[[rothschild-family]]", "[[baring-brothers]]", "[[shipping-certificate-arbitrage]]", "[[grain-futures-basis-arbitrage]]", "[[historical-cable-arbitrage]]", "[[covered-interest-arbitrage]]", "[[latency-arbitrage]]", "[[hft]]", "[[liverpool-cotton-exchange]]", "[[chicago-board-of-trade]]", "[[colocation]]"]
---

# Telegraph Impact on Arbitrage

The 19th-century telegraph — culminating in the 1866 transatlantic cable — is the clearest historical case study of communication technology compressing geographic arbitrage spreads. Within roughly a decade of the first permanent cable, New York-London FX spreads fell from ~1% to under 0.1%, cotton and grain basis trades lost much of their edge, and the economics of international merchant banking shifted permanently. The pattern — new communication technology collapses geographic arb, traders migrate to a faster layer — recurs through microwave networks, [[colocation]], and modern [[latency-arbitrage]].

## Pre-Telegraph Market Structure

Before the telegraph, cross-market prices were linked only through the physical movement of information:

- **Sailing packet ships** carried newspapers, price lists, and private letters across the Atlantic in **12-14 days** under favorable winds; 18-30 days against the wind. The Black Ball Line (founded 1818) operated the first scheduled New York-Liverpool packet service.
- **Signal towers and semaphore chains** (e.g. Paris-Lille optical telegraph, 1794) moved short messages ~200 miles in 10 minutes during daylight under clear skies — but capacity was tiny.
- **Carrier pigeons** gave the [[rothschild-family]] a reputed information edge ahead of public dispatches.

The result was that London and New York often quoted the same asset (e.g. US Treasury bonds, cotton, sterling) at prices 0.5%-3% apart, with the spread closing only after the next packet arrived. Merchants who financed cross-Atlantic trade effectively held 12-30 day information-risk positions.

## Timeline of Telegraph Development

| Year | Event | Significance |
|---|---|---|
| 1844 | Morse sends "What hath God wrought" Washington-Baltimore | First commercial electric telegraph in US |
| 1846 | AP (Associated Press) founded to pool telegraph newswire costs | Wire-service model of financial news begins |
| 1851 | Dover-Calais submarine cable | First successful cross-water cable |
| 1858 | First transatlantic cable (Field expedition) | Worked 3 weeks, then failed |
| 1861 | Western Union completes first transcontinental US telegraph | San Francisco-New York |
| **1866** | **Permanent transatlantic cable (Cyrus Field, SS Great Eastern)** | **Core event: NY and London quote in same day** |
| 1870 | London-Bombay cable | Integrates Indian markets |
| 1871 | London-Hong Kong-Shanghai | Integrates East Asian markets |
| 1872 | Completion of global cable network | Australia connected; truly worldwide |
| 1884 | Chicago Board of Trade connects pit to telegraph | Grain futures become a global price |
| 1890s | Stock tickers (Edison, 1869 onward) saturate broker offices | Intra-city latency drops to seconds |

## Cost of Cable Traffic

Early cable rates were punishing and themselves shaped what could be arbitraged:

- **1866** — ~$10 per word, New York to London. A 10-word price update cost $100 (~$1,900 in 2020 dollars).
- **1868** — $5/word
- **1870s** — $1-2/word
- **1880s** — $0.25/word

At 1866 prices only highest-margin traffic justified the wire — gold shipments, large bond trades, government dispatches. By the 1880s routine commercial price quotations were economic, which enabled continuous arbitrage.

## Quantified Spread Compression

The most-studied cases:

- **NY-London FX (sterling-dollar)** — pre-cable spreads of 60-100 bps around [[mint-parity]] compressed to 10-20 bps by the mid-1870s and to sub-10 bps by 1900. The remaining band matched the gold points almost exactly — see [[gold-point-arbitrage]].
- **Liverpool-New York cotton** — pre-1866 price differentials could persist for weeks; post-cable they closed within a trading session. The [[liverpool-cotton-exchange]] and [[new-york-cotton-exchange]] effectively became one market with a shipping-cost basis.
- **US Treasury gold bonds** — London-New York yields converged to within 5-15 bps. The arbitrage channel was not just information but funding — London merchant banks could lend against bonds collateralized by NY, with daily mark-to-market via cable.
- **Chicago grain (wheat, corn) vs East Coast / Liverpool** — after 1866 cable plus transcontinental US telegraph, Chicago pit prices became the global reference for grain — see [[grain-futures-basis-arbitrage]].

Peter Garbade and William Silber's influential 1978 paper (Journal of Finance) showed that the transatlantic cable compressed NY-London security price differentials by roughly 90% within a decade — the single cleanest natural experiment in the economics of market-information technology.

## Winners and Losers

**Winners:**

- Firms with **capital, credit lines, and representation in both cities** could execute the arbitrage: [[rothschild-family]], [[baring-brothers]], Brown Brothers, J.P. Morgan's predecessors.
- Exchanges with fast internal infrastructure — NYSE, [[liverpool-cotton-exchange]], [[chicago-board-of-trade]].
- Newswire services (Reuters, founded 1851; AP; Dow Jones, 1882).

**Losers:**

- Provincial brokers whose edge was purely geographic.
- Sailing packet operators (displaced as information carriers; freight-only after 1870).
- Merchant banks that failed to invest in cable access — notably contributing to the [[overend-gurney]] collapse in 1866, whose discount-rate arbitrage model depended on informational asymmetry that was evaporating.

## The Death of Geographic Arb as a Repeating Pattern

The telegraph is the archetype of a pattern that repeats every time communications infrastructure improves:

| Era | Technology | Arb compressed |
|---|---|---|
| 1840s-1900 | Telegraph, transatlantic cable | Cross-continental prices (FX, bonds, commodities) |
| 1920s | Teleprinter, trans-Pacific cable | Asia-Americas FX and commodities |
| 1960s-1980s | Bloomberg terminal (1982), electronic brokers | Intra-day bond and FX quotes globalize |
| 1990s | ECNs (Island, Instinet), Reuters Matching | Spread compression on equities and FX |
| 2000s | Decimalization, NYSE hybrid | Spreads collapse from 1/16 to 1 cent and below |
| 2007+ | [[colocation]] at exchange data centers | Latency arb moves to microseconds |
| 2010+ | Microwave NY-Chicago (McKay Brothers) | Latency beats fiber by ~3 ms, price of ms-latency paid |
| 2020+ | Hollow-core fiber, low-earth-orbit satellite | Fractional-microsecond wins |

The lesson for traders: **any [[latency-arbitrage]] edge decays monotonically as the cost of communication drops**. The remaining edge always lives at the frontier of the technology — shipping certificates in 1840, cable arbitrage in 1870, HFT colocation today. See [[latency-arbitrage]], [[hft]], and the [[edge-taxonomy]] treatment of latency edges.

## Trading Implications

1. **Geographic arbitrage always compresses** — budget for edge decay as a function of communication cost.
2. **Mechanism matters** — an informational edge dies when the information becomes public; a structural edge (capital, creditworthiness, venue access) can survive longer.
3. **New technology creates a fresh geographic arb for a limited window** — the firms that industrialized in that window (Rothschilds in cable, Renaissance/Citadel in HFT) captured the bulk of the profit.
4. **The frontier has moved from geography to physics** — today's "geographic arb" is fiber-vs-microwave-vs-laser between NY4, CH1, LD4, and TY3 data centers. The economic structure is identical to 1866.

## Related

- [[gold-point-arbitrage]]
- [[specie-flow-arbitrage]]
- [[bill-broking-arbitrage]]
- [[mint-parity-arbitrage]]
- [[rothschild-family]]
- [[baring-brothers]]
- [[shipping-certificate-arbitrage]]
- [[grain-futures-basis-arbitrage]]
- [[historical-cable-arbitrage]]
- [[covered-interest-arbitrage]]
- [[latency-arbitrage]]
- [[hft]]
- [[colocation]]
- [[liverpool-cotton-exchange]]
- [[chicago-board-of-trade]]

## Sources

- Kenneth Garbade and William Silber, "Technology, Communication and the Performance of Financial Markets: 1840-1975" (Journal of Finance, 1978) — the canonical quantitative study of cable arbitrage.
- Standage, *The Victorian Internet* (1998) — popular history of the telegraph as information network.
- Hoag, "The Atlantic Telegraph Cable and Capital Market Information Flows" (Journal of Economic History, 2006).
- No raw sources ingested yet.
