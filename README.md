# Three Agents, Two Mistakes — posit::conf(2026)

Quarto reveal.js talk: *Designing for LLM-Assisted Data Analysis.*

## Build

```bash
quarto render presentation.qmd     # → presentation.html
quarto preview presentation.qmd    # live-reload while editing
```

## Layout

- `presentation.qmd` — the deck (one section per agent, Lesson callouts, conclusion)
- `theme.scss` — Posit brand reveal.js theme (Open Sans / Source Code Pro, blue+gray+orange)
- `assets/logos/` — official Posit logos, SVG (white/reverse for dark slides, full-color/black for light)
- `assets/fonts/` — Open Sans + Source Code Pro

## Structure

1. Title + hook (the two questions from last year's Conf)
2. What a harness is / big-idea comparison table
3. **Agent 1 — Positron Assistant** → Lesson 1: features cost changeability
4. **Agent 2 — Databot** → Lesson 2: autonomy is only as good as access
5. **Agent 3 — Posit Assistant** → subtract tools · add skills · our own UX
6. Conclusion: the two lessons pull against each other → callback to the hook

Speaker notes live in `::: {.notes}` blocks (press `S` in the deck for the
speaker view).

## Editing notes

- Headlines are Light weight, sentence case. Eyebrows are the only place
  Source Code Pro / uppercase is used.
- On dark slides use the white/reverse logo, never the full-color one.
- No emoji (brand rule) — use the `.yes` / `.no` spans for check/cross marks.
