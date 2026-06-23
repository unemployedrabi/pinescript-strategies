# Pine Script Trading Strategies

A curated collection of **TradingView Pine Script** indicators and trading tools — momentum oscillators, volume/order-flow visualisation, price-projection models and pattern detection — organised as a clean, versioned, single-source-of-truth repository.

> [!NOTE]
> Every script in this repo is a TradingView `indicator` (study), not a backtestable `strategy()`. They are decision-support / visualisation tools meant to be layered onto a chart, not auto-traders. See [Roadmap](#roadmap) for the planned `strategy()` ports.

---

## Contents

| Script | Pine version | Type | Overlay | Summary |
|---|---|---|---|---|
| [Candle Counter](src/candle-counter) | v5 | Statistics | ✅ | Counts consecutive same-colour candles and builds a probability table for the next candle + alerts. |
| [EMA Rainbow](src/ema-rainbow) | v2 ⚠️ | Trend | ➖ | A "rainbow" of eight EMAs (20–55) for reading trend direction and momentum compression. |
| [Money Cross](src/money-cross) | legacy ⚠️ | Oscillator | ➖ | WaveTrend-style momentum oscillator with overbought/oversold bands and cross signals. |
| [OrderBook](src/orderbook) | v5 | Volume / order flow | ✅ | Volume-by-price "orderbook" rendered as horizontal boxes with optional POC. |
| [CryptoVision Explorer](src/cryptovision-explorer) | v5 | Probability model | ✅ | Monte-Carlo style forward price projection (drift + log returns) showing expected move and deviation range. |
| [DigitalTrend Insight](src/digitaltrend-insight) | v4 ⚠️ | Multi-tool | ✅ | Dashboard overlay: buy/sell signals, support/resistance, EMAs and Fibonacci retracements. |
| [AI Animal Predator](src/ai-animal-predator) | v5 | Pattern detection | ✅ | Harmonic-pattern detector (Gartley, Bat, Butterfly…) with pattern scoring and configurable targets. |

⚠️ = written for a deprecated Pine version (see [Pine versions](#pine-versions)).

---

## Repository layout

```
pinescript-strategies/
├── src/                     # one folder per script
│   ├── candle-counter/
│   │   ├── candle_counter.pine
│   │   └── README.md        # description, inputs, usage
│   └── ...
├── scripts/
│   └── check_pine.py        # lightweight static validation
├── .github/workflows/
│   └── pine-check.yml       # CI: runs the validation on every push/PR
├── CONTRIBUTING.md
├── CHANGELOG.md
└── LICENSE
```

Each script lives in its own folder with a dedicated `README.md` documenting its inputs, outputs and intended use.

---

## Usage

1. Open [TradingView](https://www.tradingview.com/) and any chart.
2. Open the **Pine Editor** (bottom panel).
3. Copy the contents of the desired `.pine` file and paste it in.
4. Click **Add to chart**.

Each script's folder README lists its configurable inputs.

---

## Pine versions

TradingView's current language version is **v6**. Three scripts here target older versions and TradingView no longer lets you *create* new scripts on them, although existing ones still run:

- **EMA Rainbow** → `//@version=2`
- **Money Cross** → no `//@version` tag (legacy v1)
- **DigitalTrend Insight** → `//@version=4`

Migrating these to v5/v6 is tracked in the [Roadmap](#roadmap). The [`@version` migration guides](https://www.tradingview.com/pine-script-docs/migration-guides/) are the reference for that work.

---

## Roadmap

- [ ] Migrate legacy scripts (EMA Rainbow, Money Cross, DigitalTrend Insight) to Pine v6.
- [ ] Add `strategy()` ports with entries/exits so signals can be backtested.
- [ ] Per-script screenshots in each folder README.
- [ ] Tag a `v1.0.0` release once migrations land.

---

## Attribution & licensing

Several of these scripts are adapted from the TradingView community (for example, the WaveTrend logic behind *Money Cross* is a well-known public indicator). Where a script derives from another author's work, please add proper credit in that script's folder README before publishing or republishing — it is both good practice and required by TradingView's House Rules.

This repository's structure, tooling and documentation are released under the [MIT License](LICENSE). Individual scripts may carry their own original authors' terms; treat each as such.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for naming conventions, the folder template and the local check command.
