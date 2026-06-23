# AI Animal Predator

**Pine version:** v5 · **Type:** indicator · **Overlay:** yes

A harmonic-pattern detector. It scans price for XABCD harmonic structures
(Gartley, Bat, Butterfly, Crab and related "animal" patterns), scores each
candidate by how closely it matches the ideal Fibonacci ratios, and draws the
pattern with configurable profit targets and invalidation levels. Bullish,
bearish and potential/incomplete patterns can be shown or hidden, and a minimum
score can be required.

## Inputs (selected)
| Input | Default | Description |
|---|---|---|
| Bullish / Bearish | true / true | Which directions to detect. |
| Potential/Incomplete | true | Show forming patterns. |
| Only high scoring | true | Hide patterns below the score threshold. |
| Lookback bars | off / 100 | Limit detection window. |
| Pattern types (Gartley…) | on | Toggle each pattern family. |
| Target 1 | .618 AD | Target level per pattern (many Fib options). |

## Outputs / signals
- Drawn harmonic patterns with score labels, targets and stop levels.

## Notes
- Pattern detection is sensitive to the pivot/lookback settings; expect more
  candidates on lower timeframes. Use the score filter to cut noise.
