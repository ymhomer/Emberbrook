# 0.4 — Mobile world, bridge navigation and travel

## Report and correction

The previous bridge corridor extended down to the painted front rail rather than staying on the deck. Its right endpoint also stopped short of the dirt road at the image edge. Navigation now lives in `src/navigation.js`, shared by rules, renderer and tests. The bridge deck, west landing, east landing and far-right road are authored separately; the visible path beside the inn is included. A foreground rail layer preserves depth without making water walkable. Save normalization now retains valid far-east positions instead of clamping them back onto the bridge.

Use `scripts/render-navigation.py` with the existing Pillow environment to review map overlays in artifacts/. Green is authored ground; red is excluded scenery; gold rings are portal triggers. This review view is offline development tooling, not part of the player interface. Illustrated terrain still needs authored validation when a map changes.

## Mobile layout and view

- A compact character/health strip and collapsed quest chip replace the tall panels. The minimap is tappable; keyboard hints, large region title and footer are hidden on small screens.
- The camera uses a wider, height-aware default view. Zoom out, reset and zoom in controls remain available.
- Joystick and action controls sit above the bottom dock with safe-area spacing. High-DPI rendering and landscape resizing are retained.

## Travel

Walking into the southern village gate, east road portal, unlocked mine entrance, woodland return gate or dungeon exit triggers travel. The screen fades to dark before changing the world, then fades back in. Movement and pointer input are blocked during the swap. Arrivals are outside destination trigger circles and have a brief cooldown, preventing immediate return loops. The mine still requires a forged blade. The atlas walks to triggers without requiring another confirmation dialog.

## Living world

- A small masked water texture layer warps river/pond pixels and adds moving surface highlights. Water masks exclude the bridge and land; the original map is preserved underneath. Canvas and WebGL use the same authored mask assets.
- Timber, ore and herbs use a short tool/progress animation. Resources are awarded after completion; repeated interaction during the action cannot award duplicates.
- Bram, Mira and Elian use original detailed four-direction NPC sprites and matching conversation portraits. Talk to characters by approaching and interacting, clicking them, or selecting their speech marker in the atlas. Conversations offer valley guidance and relevant forge, inn or ranger services.

## Verification and limitations

Core tests cover bridge/right-road connectivity, blocked river/rail, inn-side path, portal triggers, safe arrivals and east-road save roundtrips, alongside existing gameplay rules. Full browser checks cover both quest loops after automatic travel and timed gathering. Focused high-DPI mobile checks cover compact HUD, zoom, changing water pixels, manual bridge crossing with darkened swap, gather reward count, NPC dialogue, mine locking and landscape layout. Physical phone testing remains an acceptance step.

Rollback: local commit 06223535450aaf76fb894a9b845dce06c97acd3b and artifacts/backups/before-v04.zip. Previous published commit: f17445912bf323ab8ddc4c03587fe5319faf06a1.

### Additional integration findings

Browser QA found and corrected overlapping atlas NPC/building targets; NPC destinations are now separate controls below the map. Timed-gather tests wait for completion before checking inventory. Local file origins can taint a derived canvas in WebGL: normal direct-file play uses Canvas, WebGL QA uses a test-only file-origin flag, and an unavailable water upload falls back to the original painting rather than blocking game startup. Fishing's timing window was relaxed slightly for touch input.
