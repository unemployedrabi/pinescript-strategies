# EMA Rainbow

**Pine version:** v2 (deprecated) · **Type:** indicator · **Overlay:** no

Plots eight exponential moving averages of `close` with periods 20, 25, 30, 35,
40, 45, 50 and 55 in a warm colour gradient. When the bands fan out and align in
order the trend is strong; when they compress and interleave the market is
ranging or about to turn.

## Inputs
None — periods and colours are fixed in the source.

## Outputs / signals
- Eight EMA lines (periods 20–55).

## Notes
- Written for Pine **v2**, which TradingView no longer allows for new scripts.
  Migrating to v6 (and exposing the periods/colours as inputs) is on the roadmap.
- Despite plotting moving averages, the script declares `overlay=false`; change
  to `overlay=true` if you want them drawn on the price chart.
