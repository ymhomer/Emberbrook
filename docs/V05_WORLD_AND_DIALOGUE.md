# 0.5 — Directional world, animated NPCs and character conversations

## Travel graph

```text
                Village  ←→  Willowmere Woods
                   ↕          (west entrance)
             Sunleaf Meadow
             (north entrance)

Village mine ↔ underground Hollow
```

The village east bridge now enters the **western** woodland trail. Returning west arrives on the village's **eastern** road. The southern village gate has its own region, Sunleaf Meadow: arrival is on the meadow's northern trail, and the northern return enters the village from the south. Paired portal IDs, opposite edge names and region grid coordinates are validated together. Both former village exits no longer share a target/spawn.

The forest painting was edited to visibly include the west entry. Its old southern trail is now a scenic lookout rather than a misleading return portal. The meadow is an original separate map with herbs and a picnic recovery spot. Existing forest saves keep their progress and location, with the atlas showing the new west return.

## Portal readability

Portals now combine three continuously rendered layers: rotating ground runes, an upright three-phase glowing curtain, and rising/orbiting motes. Woodland, meadow and Hollow use different light colors. Darkened region transitions, safe spawns, cooldown and mine equipment requirements remain in place. Reduced-motion preference freezes portal movement.

## NPC motion

Each of Bram, Mira and Elian now has sixteen authored animation frames: four front idle/gesture/blink poses and four frames for each left, right and rear walking direction. The runtime uses animation clips rather than flipping a single directional still. Frame tests sample actual runtime changes.

## Dialogue

Character conversations use large original transparent standees, a parchment text panel at the bottom, speaker nameplate, and a separate choice stack over the game scene. The layout draws composition from the supplied reference while retaining Emberbrook's palette and character style. Text reveals progressively; tapping it completes the current line. Continue advances the conversation. Story, forge, inn and ranger actions remain available. Opening a shop restores the standard panel layout and closing a dialogue cancels its text timer.

Portrait, landscape, desktop, keyboard closing, normal-modal restoration, real animation frames and both reciprocal travel pairs are browser-tested. Existing chapter, fishing, provision, save and touch flows remain regression targets. Physical phone acceptance is still required.

## Art / rollback

Original assets were generated with the built-in imagegen tool; runtime paths, prompts and master hashes are recorded in V05_ART_SOURCES.json. Full-size masters remain local; only optimized runtime assets are published.

Rollback baseline: local commit 98ee76268f4ac7d2ae9b9f83f373f04be899bf95 and artifacts/backups/before-v05.zip. Previous published commit: 326c1e2adf2997d5a2aca0d9301fad9457895d74.
