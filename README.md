# Metabolic Marathon (CHEM 3B metabolism)

Study game for CHEM 3B Chapters 13–15 (carbohydrate metabolism, energy production, lipid and protein metabolism).
Live at https://itsdrdan.github.io/metabolism/ once this repo is published with GitHub Pages (branch `main`, root).

- `index.html` — the whole game (no build step). Loads the brand kit (`games/brand/itsdrdan.css`, `icons.js`, `embed.js`), `games/track.js`
  for anonymous stats, and the Exam Practice module from the textbook repo (`textbook/js/fbx.js`, `textbook/css/widget-base.css`,
  questions from `textbook/bank/metabolism.json`).
- `meta.json` — study hub card (copy the game into the hub's catalog the usual way). `logo.svg` — badge used in the hero.
- Modes: Pathway Order, Count the Coenzymes, Name the Reaction, Fuel Fates, Enzymes & Vitamins, Exam Practice.
  `?mode=count` (or order, rxn, fates, enz, exam) opens a mode directly; `?course=3B` is accepted and ignored (3B-only game).
- Conventions: 2.5 ATP per NADH, 1.5 per FADH2, 10 ATP per acetyl CoA, 32 ATP per glucose, activation of a fatty acid costs 2 ATP;
  citrate synthase is classed as a transferase (CHEM 3B convention).

Game design and chemistry by ItsDrDan. Code written with AI assistance (Claude) and checked by the author. CC BY-NC-SA 4.0.
