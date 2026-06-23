# Candle Counter

**Pine version:** v5 · **Type:** indicator · **Overlay:** yes

Counts runs of consecutive same-coloured candles and, on the last bar, prints a
table showing — for every observed run length — how many times that streak was
followed by a green vs. a red candle, expressed as a probability. Useful for
mean-reversion / exhaustion ideas ("after N greens in a row, what usually
happens next?"). Optionally numbers each candle in the current run and fires an
alert when a streak of a chosen length and colour forms.

## Inputs
| Input | Default | Description |
|---|---|---|
| Select Price | Candles | Regular candles or Heikin Ashi for colour determination. |
| Display Data | All Data | Show stats for all history or only the active run. |
| Candle Counter | true | Draw the running count above/below each candle. |
| Alert Candles in Row | 5 | Streak length that triggers the alert. |
| Alert colour | Green | Which colour streak the alert reacts to. |
| Table location / size | top-right / normal | Placement of the stats table. |

## Outputs / signals
- On-chart stats table: count of green/red runs per length and the historical
  probability the next candle is green or red.
- Alert: "N Green/Red Candles in Row on \<symbol\> [\<tf\>]".

## Notes
- Probabilities are descriptive statistics over the loaded history, not a forecast.
