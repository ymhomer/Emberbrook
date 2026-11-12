# Changelog

## 0.5.0 — Directional world and character conversations

- Replaced faint travel circles with three-layer, three-phase upright portal effects.
- Added 16-frame animation sheets for each NPC, including idle gestures/blinks and walking clips.
- Rebuilt conversations around original large standees, a bottom parchment text box, speaker nameplate, progressive text and separate choices. Added mobile/landscape layouts while preserving shop/inn/ranger services.
- Split the old duplicate exits: east village bridge ↔ west woodland trail; south village gate ↔ north Sunleaf Meadow trail. Added the corresponding painted west entry and a separate meadow map with gathering/rest spots.
- Added reciprocal edge/grid, distinct destination, real frame, dialogue and return-route regressions. Save format remains version 1.

## 0.4.0 — Mobile world and living village

- Centralized navigation geometry, aligned the bridge deck/landings, opened the east dirt road and inn-side path, and preserved valid far-east save positions.
- Added movement-triggered region portals with a darkened world swap, input guard, safe arrivals, cooldown and existing mine lock.
- Reworked mobile HUD into compact status/quest/minimap controls; added a wider default camera, zoom controls and safe-area spacing.
- Added masked animated water, timed gathering tool/progress effects, detailed directional NPC sprites, portraits and conversations with forge/inn/ranger services.
- Expanded core, full-flow and focused mobile regression coverage. Existing saves remain compatible.

## 0.3.0 — Willowmere and detailed traveler

- Replaced broad collision allowances with traced ground surfaces, blocked the reported forge-side fence/rock gap, moved inaccessible deposits, and added safe migration for saved positions. Corrected southern gate navigation and overhead sign occlusion.
- Added an original detailed sixteen-frame 128×160 traveler, matching portrait and up to 2× device-pixel rendering.
- Added Willowmere Woods: original illustrated third map, timing-based fishing, replenishing herbs, repeatable ranger deliveries, healing draughts, campfire rest and a one-time shrine restoration reward.
- Extended the atlas, journal, satchel and Traditional Chinese/English labels. Existing local saves keep first-chapter progress and initialize woodland fields safely.
- Validation: 14 core checks plus original chapter/woodland browser flow; focused mobile validation recorded separately.

## 0.2.0 — Touch controls and navigation

- Added an analog touch joystick with deadzone, pointer capture, release/cancel/blur handling, and independent action buttons.
- Replaced coarse four-way navigation with eight-way A*, continuous segment checks and safe route smoothing. Foot-radius collision and substepped manual movement prevent corner cutting and tunnelling; river crossing is limited to the bridge.
- Forge errors and crafting success now appear inside the shop dialog. Successful crafting updates the recipe without closing the shop. Other dialog notifications use the same accessible inline notice.
- Replaced destination button lists with an illustrated atlas, selectable landmark pins, current location, route preview and explicit walk confirmation. Dungeon maps show dungeon destinations; map selection never teleports between regions.
- Corrected world marker hit areas. Existing version-1 local saves remain compatible.


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
