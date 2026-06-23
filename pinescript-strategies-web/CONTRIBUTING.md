# Contributing

Thanks for improving this collection. A few conventions keep it consistent.

## Adding a new script

1. Create a folder under `src/` using a lowercase, hyphenated name, e.g. `src/my-new-tool/`.
2. Put the script in it as `my_new_tool.pine` (lowercase, underscores).
3. Add a `README.md` in that folder using the template below.
4. Update the table in the root [README](README.md).
5. Add an entry to [CHANGELOG.md](CHANGELOG.md) under `[Unreleased]`.

## Per-script README template

```markdown
# <Script name>

**Pine version:** v_  ·  **Type:** indicator  ·  **Overlay:** yes/no

One-paragraph description of what it does and when it is useful.

## Inputs
| Input | Default | Description |
|---|---|---|
| ... | ... | ... |

## Outputs / signals
- ...

## Notes
- Known limitations, attribution to original author if adapted, etc.
```

## Style

- Target **Pine v6** for new scripts where possible.
- Keep `indent_size = 4` (enforced by `.editorconfig`).
- Use descriptive input titles and `group=` / `tooltip=` so the settings dialog is self-documenting.
- LF line endings (enforced by `.gitattributes`).

## Local check

Run the lightweight validator before committing:

```bash
python3 scripts/check_pine.py
```

It verifies each `.pine` file declares a Pine version, has balanced brackets, and ends with a newline. The same check runs in CI on every push and pull request.

## Attribution

If a script is adapted from another author (TradingView community, etc.), credit them in that script's README. Do not present third-party work as original.
