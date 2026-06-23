# DigitalTrend Insight

**Pine version:** v4 (deprecated) · **Type:** indicator · **Overlay:** yes

A multi-tool overlay that combines several discretionary aids into one script:
buy/sell signal markers, "void" lines, optional support/resistance lines, an
8/200 EMA pair, Fibonacci retracements, signal bar colouring and an on-chart
dashboard.

## Inputs (selected)
| Input | Default | Description |
|---|---|---|
| Void Lines | true | Draw void lines. |
| Dashboard | true | Show the on-chart dashboard. |
| Signal Bars | true | Colour bars on signals. |
| Support & Resistance | false | Plot S/R lines. |
| EMA (8, 200) | false | Plot the EMA pair. |
| Buy & Sell Signals | true | Show entry markers. |
| Fibonacci Retracement | false | Draw fib levels. |
| Dashboard Distance | 13 | Dashboard offset. |

## Outputs / signals
- Buy/sell markers, optional S/R, EMAs, fibs, void lines and a dashboard panel.

## Notes
- Written for Pine **v4**; migrate to v6 to keep it future-proof (roadmap).
- It bundles many independent features — turn off what you don't use to keep the chart readable.
