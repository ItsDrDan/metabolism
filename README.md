# Metabolic Marathon (CHEM 3B metabolism)

Study game for CHEM 3B Chapters 13–15 (carbohydrate metabolism, energy production, lipid and protein metabolism).
Live at https://itsdrdan.github.io/metabolism/

- `index.html`: the whole game (no build step). Loads the brand kit (`games/brand/itsdrdan.css`, `icons.js`, `embed.js`), `games/track.js`
  for anonymous stats (with named slips), and the Final Boss module from the textbook repo (`textbook/js/fbx.js`, `textbook/css/widget-base.css`,
  questions from `textbook/bank/metabolism.json`).
- Layout matches Sig Fig Sleuth: pick one or more of 5 groups (Pathways, ATP Accounting, Reactions & Coenzymes, Fuel Fates & Health, Rosa’s Case Files), then
  turn topic chips on or off. Exam Prep Check = 10 mixed questions and a study plan. Final Boss Questions = the shared exam bank.
- Art: see `ASSETS.md`. Until the WebP files exist, brand-kit badges and a drawn mitochondrion stand in.
- Rosa’s Case Files follow the textbook’s patient (Rosa’s Story, Parts 13–15 in Chapters 13–15) plus her medicines; topics `rosa13`, `rosa14`, `rosa15`, `rosarx`. This group appears only when the game is opened from the textbook: a LibreTexts referrer, a `?topic=rosa…` link or `?src=book` (remembered for the browser tab). On the study hub, Canvas or a direct visit it is hidden, and Every Mile asks for four groups.
- Links: `?topic=rxn,coenz` opens topics directly. Old links still work: `?mode=order|count|rxn|fates|enz|exam`. `?course=3B` is ignored (3B only).
- Conventions (Dr. Dan's Ch 22–24 slides): 2.5 ATP per NADH, 1.5 per FADH2, 10 per acetyl CoA, 32 per glucose, fatty acid activation costs 2 ATP,
  one less FADH2 per C=C. Students are not expected to memorize every intermediate, so pathway questions focus on start/end, location,
  reaction types and reading diagrams; full glycolysis and citric acid cycle orders are marked "Challenge".
- `tools/build_game.py` builds other CHEM 3B games from the **v1** engine (git history before the v2 rebuild); it does not work on this v2 file.

Game design and chemistry by ItsDrDan. Code written with AI assistance (Claude) and checked by the author. CC BY-NC-SA 4.0.
