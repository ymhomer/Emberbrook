# 0.3 — Woodland expansion and navigation correction

## Report and cause

The reported character position beside Bram's forge was inside a fence/rock decoration that the previous rectangular collision list did not cover. A previously allowed empty area was not necessarily illustrated ground. Navigation now uses explicit ground polygons, subtracts buildings and scenery, and keeps foot-radius/segment checks for both manual movement and A* routes. Regression coordinates around (780,350), (800,365) and (820,400) are blocked. Gathering deposits formerly inside dense foliage were moved onto accessible ground.

The southern arch is an overhead object: its posts are solid, the opening is walkable, and a separate foreground layer draws the hanging sign over actors behind it. Every interaction point, including the woodland gate, has route-reachability coverage. A saved position inside a new blocker moves to nearby valid ground, preserving other save fields.

## Character quality

The new original illustrated traveler uses sixteen normalized 128×160 frames, replacing the 40×48 runtime sprite. The portrait matches the new character. Runtime rendering uses up to 2× device-pixel resolution; the map and character retain smooth artwork filtering. Existing low-resolution NPCs are retained for this preview.

## Willowmere loop

1. Use the atlas to walk to **Trail to Willowmere** at the southern village gate, then enter.
2. Gather moonleaf herbs beside the marked patches. Each patch replenishes in four seconds.
3. At the pier, cast a line, then reel in when the float enters the golden zone. A miss costs no materials. Successful catches award one fish and eight XP.
4. Deliver two fish and three herbs at the ranger cottage for 65 gold, 35 XP and one healing draught. Deliveries are repeatable; ingredients are consumed.
5. After a first delivery, restore the willow shrine for a one-time 100 gold and 60 XP reward.
6. Rest at the campfire, use a healing draught from Inventory (+50 HP, capped at 100), or return to the village. Draughts work in the original dungeon too.

All progress remains in the version-1 local-save slot; older saves initialize the added fields to zero. No account, backend, cloud save or multiplayer was added. First-chapter progress is retained.

## Evidence and limits

- Core tests cover navigation, reported obstacles, gate/woodland reachability, fishing timing, delivery costs/rewards, consumable healing, one-time shrine reward and old/new save normalization.
- Full browser tests cover the original chapter followed by the new woodland loop, shrine, return journey and save export/import.
- Additional mobile checks cover saved-position migration, detailed character loading, 2× rendering, actual emulated touch events, potion use and the woodland atlas.
- Physical phone/browser acceptance is still required. Decorative art and collision are hand-mapped, so report any remaining specific obstacle mismatch with its location.

Rollback: local commit adc9ec7 and artifacts/backups/before-v03.zip. Previous published commit: 597fa5f86da7ea3dfab1cae45ecbb9adcc8a19d2.
