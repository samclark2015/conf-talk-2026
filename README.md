# Three Agents, Two Mistakes

A talk from posit::conf(2026): *Designing for LLM-Assisted Data Analysis.*

The talk walks through three AI coding/data-analysis agents Posit has
shipped — Positron Assistant, Databot, and Posit Assistant — and the design
lessons learned (and re-learned) along the way:

- **Lesson 1:** every feature you add costs you changeability.
- **Lesson 2:** an agent's autonomy is only as good as what it can access.

## Viewing the slides

The deck is built with [Quarto](https://quarto.org) reveal.js. Open
[`index.html`](index.html) in a browser, or render it yourself:

```bash
quarto render index.qmd     # → index.html
quarto preview index.qmd    # live-reload while editing
```

## What's in this repo

- [`index.qmd`](index.qmd) — the talk itself
- [`theme.scss`](theme.scss) — Posit brand reveal.js theme
- [`assets/`](assets/) — logos, fonts, and other slide assets

## Author

Sam Clark · Posit, PBC
