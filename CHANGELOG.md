# Changelog

## 0.1.0 — 2026-11-11

Initial art-focused single-player test build.

- Added two original illustrated maps: Emberbrook village and Ember Hollow shrine.
- Added an original animated pixel traveler, NPC variants, foreground occlusion and independent animated smoke, sparks, motes and water highlights.
- Added keyboard and click/tap movement, collision-aware A* routes, renewable gathering, crafting, lightweight combat, a chest, recovery and a complete relic quest with a one-time reward.
- Added character HUD, objective journal, satchel, destination map, forge dialog, dusk toggle, short synthesized action sounds, Traditional Chinese / English UI and mobile controls.
- Added versioned browser-local saves, save export/import and confirmed reset. Storage failure is visible.
- Bundled Phaser and OFL font subsets; all web assets use relative paths and need no CDN/account/backend.
- Added static build, GitHub Pages Actions workflow, source/playable packaging and local test documentation.

Validation: seven deterministic core checks and nineteen browser end-to-end checks passed. Browser flow tested using Canvas rendering; WebGL was additionally launched and visually checked. Desktop 1440×960, mobile 390×844, local-file loading, save restore/export/import and blocked storage were tested. A final art-only smoke test passed after NPC/foreground refinements; see docs/VALIDATION.json for exact scope. Direct local-file opening also passed without special file-access browser flags (Canvas, fonts, movement and save). No remote repository, Pages deployment or multiplayer service was created.

Rollback baseline: project-local initial scaffold commit 15c02f1. All work is isolated in this project; artifacts, downloaded browsers, libraries and caches are excluded from source delivery.
