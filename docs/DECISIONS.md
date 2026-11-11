# Implementation decisions

- Single-player, local-state prototype; GitHub Pages is the target, with no backend or multiplayer service.
- Phaser 3.90.0 is pinned and bundled locally. A buildless browser runtime with classic scripts keeps the playable archive easy to open; the small build script copies assets and embeds font data. No CDN dependencies.
- Hosted builds automatically select WebGL where available; direct file opening selects Canvas; `?renderer=canvas` offers a compatible Canvas renderer. Both rendered successfully in local QA; the full interaction suite uses Canvas on the software-rendered test host.
- Two original illustrated maps with separately rendered actors, markers, collisions, foreground occlusion and animated environmental effects. The foreground mask drops unused transparent RGB data losslessly.
- Gameplay rules live in core.js, independent of Phaser, with deterministic tests. A* is intentionally small and grid-based; collisions are hand-authored for the authored map artwork.
- LocalStorage saves after significant actions, every five seconds and when the page is hidden. Import/export provides an explicit device-transfer route. No claim of cloud persistence or trusted server economy.
- Traditional Chinese and English share the same runtime state and UI. Fonts are self-hosted OFL subsets and embedded by the build for local-file compatibility.
- Browser QA uses a project-local official browser and extracted official Ubuntu libraries. No system packages or services were installed, and no network listener was started.
