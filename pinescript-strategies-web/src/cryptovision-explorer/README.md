# CryptoVision Explorer

**Pine version:** v5 · **Type:** indicator · **Overlay:** yes

A forward price-projection tool. It samples the distribution of historical
returns and runs a Monte-Carlo / geometric-Brownian-motion style simulation to
draw an **expected move** and a **deviation range** ahead of the current bar.
Drift can be modelled with linear regression or a volatility-degraded average,
and returns can be computed as percent change or log returns.

## Inputs (selected)
| Input | Default | Description |
|---|---|---|
| Derivative Source | Candle | `Candle` = close−open, `Move` = close−close[1]. |
| Outcome Smoothing | 1.75 | Smooths the outcome distribution (0 = off). |
| Drift Style | Standard | `Linear Regression`, `Standard`, or `None`. |
| Returns Style | Log Returns | `Percent` or `Log Returns`. |
| Side of Chart | Right | Which side the projection is drawn on. |
| Move Visualization | Both | `Expected`, `Deviation Range`, `Both`, `None`. |
| Bullish / Bearish colours | — | Projection colouring. |

## Outputs / signals
- Projected expected-move path and a shaded deviation range.

## Notes
- A probabilistic visualisation, not a guarantee; wide ranges reflect high
  realised volatility. Tune `Outcome Smoothing` and drift to your timeframe.
