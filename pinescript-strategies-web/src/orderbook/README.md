# OrderBook

**Pine version:** v5 · **Type:** indicator · **Overlay:** yes

Approximates a volume profile / "orderbook" by bucketing traded volume into
fixed-height price levels and drawing each level as a horizontal box whose width
and colour scale with the volume accumulated there. Optionally extends the
point-of-control (highest-volume level) across the chart and draws a grid/table.

## Inputs
| Input | Default | Description |
|---|---|---|
| Source | close | Price used to assign volume to a level. |
| Rows | 10 | Levels drawn above and below current price. |
| Width | 0.5 | Multiplier on the first candle's range → bucket height. |
| POC | false | Extend the highest-volume level to the left. |
| Table / Left / Grid | false / 5 / false | Optional framing and gridlines. |

## Outputs / signals
- Horizontal volume boxes (red below / green above / grey at price) with volume labels.

## Notes
- It is a single-pass approximation built from candle volume, not true L2 depth.
- `max_boxes_count`/`max_lines_count` are capped at 500; very high `Rows` on long
  histories can hit those limits.
