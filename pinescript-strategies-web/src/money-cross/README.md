# Money Cross

**Pine version:** legacy (no `//@version`) · **Type:** indicator · **Overlay:** no

A WaveTrend-style momentum oscillator. It builds an average price (`hlc3`),
derives a channel index, smooths it into the WaveTrend line `wt1`, and compares
it against its own SMA `wt2`. Crossovers of `wt1`/`wt2`, especially in the
overbought/oversold zones, are used as momentum-reversal signals.

## Inputs
| Input | Default | Description |
|---|---|---|
| Channel Length | 10 | Length of the channel EMA. |
| Average Length | 21 | Smoothing length of the WaveTrend line. |
| Over Bought Level 1 / 2 | 60 / 53 | Upper bands. |
| Over Sold Level 1 / 2 | -60 / -53 | Lower bands. |

## Outputs / signals
- `wt1` (green) and `wt2` (red) lines, their difference as an area, and circle
  markers on every cross. Bars are coloured on cross events.

## Notes
- This is the classic public WaveTrend logic (popularised on TradingView by
  **LazyBear**). Credit the original author before republishing.
- No version tag means it compiles as legacy Pine v1; migrating to v6 is on the roadmap.
