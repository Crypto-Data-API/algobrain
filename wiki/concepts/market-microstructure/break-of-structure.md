---
title: "Break of Structure"
type: concept
created: 2026-04-10
updated: 2026-06-11
status: good
tags: [technical-analysis, market-microstructure, breakout]
aliases: ["BOS", "change of character", "ChoCH", "market structure shift", "MSS", "break-of-structure"]
domain: [market-microstructure, technical-analysis]
prerequisites: ["[[market-structure]]", "[[smart-money-concepts]]"]
difficulty: intermediate
related: ["[[smart-money-concepts]]", "[[order-blocks]]", "[[liquidity-sweeps]]", "[[fair-value-gaps]]", "[[market-structure]]", "[[trend]]"]
---

Break of structure (BOS) is the event where price breaks a previous swing high or swing low, confirming the continuation or reversal of the prevailing [[market-structure]]. In [[smart-money-concepts]] trading, BOS and its counterpart -- change of character (ChoCH) -- are the primary tools for establishing directional bias and identifying when institutional participants have shifted their positioning.

## Break of Structure (BOS)

A BOS occurs when price continues the existing trend by breaking the most recent significant swing point:

- **Bullish BOS**: price breaks above a previous swing high in an uptrend, confirming that buyers remain in control and the sequence of higher highs and higher lows is intact
- **Bearish BOS**: price breaks below a previous swing low in a downtrend, confirming that sellers remain dominant and the sequence of lower highs and lower lows continues

BOS is a continuation signal. It tells the trader that the current trend is valid and that setups aligned with the trend direction (buying pullbacks to [[order-blocks]] in an uptrend, selling rallies into bearish OBs in a downtrend) remain high-probability.

## Change of Character (ChoCH)

A change of character occurs when price breaks structure in the **opposite** direction of the prevailing trend, signaling a potential reversal:

- **Bullish ChoCH**: in a downtrend (lower highs, lower lows), price breaks above the most recent lower high. This is the first sign that sellers have lost control and buyers may be taking over
- **Bearish ChoCH**: in an uptrend (higher highs, higher lows), price breaks below the most recent higher low. This signals that the bullish trend may be ending

ChoCH is a reversal signal, but not a guarantee. It represents the first structural evidence that the trend may have changed. Traders typically wait for a confirmed BOS in the new direction (a new higher high after a bullish ChoCH, or a new lower low after a bearish ChoCH) before committing with full conviction.

The term **market structure shift (MSS)** is used interchangeably with ChoCH in many [[smart-money-concepts|SMC]] communities, though some practitioners distinguish MSS as a ChoCH that occurs after a [[liquidity-sweeps|liquidity sweep]], adding confluence to the reversal signal.

## Internal vs. External Structure

SMC methodology distinguishes between two layers of market structure:

**External structure** (also called swing structure) refers to the major swing highs and swing lows visible on the trader's primary timeframe. These are the significant turning points that define the overall trend. External BOS and ChoCH carry the most weight for directional bias.

**Internal structure** (also called sub-structure or fractal structure) refers to the smaller swing points that form within the moves between external structure points. For example, within a bullish leg from one external swing low to the next external swing high, price will make multiple internal higher highs and higher lows. Internal structure is used for entry timing -- a trader might wait for an internal ChoCH at an [[order-blocks|order block]] to time a precise entry within the broader external trend.

Understanding the interplay between internal and external structure is critical. A bearish internal ChoCH within a bullish external trend is not a signal to short -- it is a pullback that may provide a buying opportunity. Only when external structure breaks does the macro bias change.

## Using BOS and ChoCH in Trading

The practical application follows a top-down sequence:

1. **Establish bias on the higher timeframe** (daily or 4H): identify the external trend via BOS. If the daily shows bullish BOS (higher highs being made), the bias is long
2. **Wait for a pullback**: on the execution timeframe (15m or 1H), price should retrace into a discount zone, ideally into an [[order-blocks|order block]] or [[fair-value-gaps|fair value gap]]
3. **Look for internal ChoCH as entry trigger**: when price reaches the zone of interest, watch for the lower-timeframe structure to shift from bearish (the pullback) to bullish (an internal bullish ChoCH). This confirms that the pullback is over and the next bullish leg is beginning
4. **Enter after ChoCH confirmation**: place the entry near the internal ChoCH level with a stop below the [[order-blocks|order block]] or the recent [[liquidity-sweeps|liquidity sweep]] low
5. **Target**: the next external swing high or [[liquidity-sweeps|buy-side liquidity]] pool

## Common Mistakes

- **Confusing internal and external breaks**: an internal BOS does not carry the same weight as an external BOS. Traders who treat every small swing break as a trend change will be whipsawed repeatedly
- **Trading ChoCH in isolation**: a ChoCH without supporting confluence ([[liquidity-sweeps|liquidity sweep]], [[order-blocks|order block]], [[fair-value-gaps|FVG]]) has a lower probability of leading to a sustained reversal
- **Ignoring the higher timeframe**: a bearish ChoCH on the 5-minute chart means little if the 4H and daily are in a strong bullish trend. Always align with the higher timeframe structure

## Sources

- [[smart-money-concepts]] — the broader SMC framework page within this wiki, which synthesises the ICT/SMC methodology that defines BOS and ChoCH
- Inner Circle Trader (ICT) and the wider SMC trading community — origin of the BOS/ChoCH/MSS terminology and the internal-vs-external structure distinction (concept is community-developed; no single canonical academic source)

## Related

- [[smart-money-concepts]] -- the methodology that uses BOS and ChoCH as foundational tools
- [[market-structure]] -- the broader concept of trend structure that BOS and ChoCH define
- [[order-blocks]] -- the zones where entries are taken after BOS/ChoCH confirms direction
- [[fair-value-gaps]] -- imbalances created during the impulsive moves that produce BOS
- [[liquidity-sweeps]] -- sweeps that often precede ChoCH at reversal points
- [[trend]] -- the macro concept that BOS confirms and ChoCH challenges
