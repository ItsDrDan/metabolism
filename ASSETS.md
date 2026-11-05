# Metabolic Marathon: art

**Status (Nov 4, 2026):** all 23 images are in (logo, 5 Mito moods, 6 menu badges, 11 achievements), plus the study hub card `games/assets/games/metabolism.webp`. `cat-fates.webp` was trimmed with a round mask to remove white corners.

**23 images total: 1 logo + 5 mascot moods + 6 menu badges + 11 achievement badges.**

The pathway diagrams (citric acid cycle, glycolysis, β-oxidation, urea cycle, electron transport chain, the cell with parts A–D) are drawn by the game's code because their labels have to be exact. Don't make those.

Use the brand prompt from itsdrdan.github.io/games/brand and change only the Subject line. Glossy cartoon style, transparent background, no text except the letters or symbols listed.

## 1 game logo

| File | Size | Subject |
|---|---|---|
| `assets/logo-256.webp` in this repo, plus `assets/games/metabolism.webp` in the games repo (study hub card) | 1024 × 1024 source, cut to 256 × 256 for the game | **Mito**, a cute peach-orange mitochondrion (bean shape with wavy orange cristae lines showing through), mid-stride running a race: little arms pumping, sneakers, a red sweatband and a race bib that reads "ATP". A tiny lightning bolt trails behind. Name: Metabolic Marathon. |

## 5 mascot moods (same character as the logo)

Make them on one sheet so Mito looks the same in all five. Each is cut to **320 × 320 transparent WebP** and saved in `assets/mascot/`.

| File | Mood | Subject |
|---|---|---|
| `mito-idle.webp` | idle | Mito jogging in place, relaxed smile |
| `mito-thinking.webp` | thinking | Mito standing still, one hand on chin, looking up, a small "?" above |
| `mito-correct.webp` | correct | Mito grinning with a thumbs up, small sparkles |
| `mito-oops.webp` | oops | Mito sheepish, scratching head, one sweat drop, wobbly smile |
| `mito-victory.webp` | victory | Mito bursting through a finish-line ribbon, arms up, gold medal on |

## 6 menu badges

Each is cut to **256 × 256 transparent WebP** and saved in `assets/`.

| File | Used for | Subject |
|---|---|---|
| `cat-pathways.webp` | Pathways | A winding trail map with three stops (a hexagon sugar, a circle-arrow cycle, a lightning bolt) connected by a dotted path |
| `cat-atp.webp` | ATP Accounting | A cartoon cash register or tally counter whose screen glows "ATP", small coins labeled NADH and FADH₂ |
| `cat-reactions.webp` | Reactions & Coenzymes | Two molecules passing a glowing "H" between them, a curved arrow, an NAD⁺ token |
| `cat-fates.webp` | Fuel Fates & Health | A dinner plate, a running shoe and a heart monitor line in one round badge |
| `prep.webp` | Exam Prep Check | A finish-line flag with a clipboard checklist |
| `boss.webp` | Final Boss Questions | A gold trophy with a tiny crown and a lightning bolt |

## 11 achievement badges

Each is cut to **256 × 256 transparent WebP** and saved in `assets/`.

| File | Achievement | Subject |
|---|---|---|
| `ach-start.webp` | Starting Line | A starting block on a track with a small "GO" flag |
| `ach-streak5.webp` | Second Wind | A sneaker with 5 small green checks trailing behind like a wind gust |
| `ach-streak10.webp` | Runner's High | A sneaker on fire with a "10" on its side |
| `ach-pathfinder.webp` | Pathfinder | A compass whose needle is a curved metabolic arrow |
| `ach-atp.webp` | ATP Accountant | A calculator with a glowing ATP battery on its screen |
| `ach-fat.webp` | Fat Burner | A cartoon fat droplet with a little flame turning into ATP sparks |
| `ach-redox.webp` | LEO & GER | A cartoon lion (LEO) and a smiling "GER" speech bubble trading an electron |
| `ach-fuel.webp` | Fuel Fixer | A fuel gauge pointing to full, with a glucose hexagon on the dial |
| `ach-every-mile.webp` | Every Mile | A road sign with four checked mile markers |
| `ach-finish.webp` | Finish Line | A gold medal on a ribbon with a mitochondrion stamped on it |
| `ach-boss.webp` | Boss Fight | A crowned round-bottom flask (the Final Boss logo) knocked out with stars |

## Where the images go

- `metabolism/assets/logo-256.webp` (top bar, page header)
- `metabolism/assets/mascot/mito-<idle|thinking|correct|oops|victory>.webp` (5 files)
- `metabolism/assets/cat-pathways.webp` … `metabolism/assets/ach-boss.webp` (17 files)
- `games/assets/games/metabolism.webp` (the study hub card; that file lives in the games repo)


## Added for Rosa’s Case Files (Nov 2026)

| File | Subject |
|---|---|
| `assets/cat-rosa.webp` | A manila case folder with a paper clip, a glucose meter peeking out, and Mito’s small face on the tab |
| `assets/ach-rosa.webp` | A case folder stamped with a gold check mark ("Case Closed") |

Done (Nov 2026): both files are in `assets/`.
