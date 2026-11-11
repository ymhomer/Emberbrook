# Preview 0.2 controls and navigation

- Touch devices: drag the lower-left joystick. A small deadzone prevents drift; longer drags increase speed. Release, pointer cancellation, window blur, hidden tabs, and opening a dialog reset movement. The right-hand buttons interact and attack independently.
- Keyboard movement and joystick movement cancel a click-to-walk route. WASD and arrows remain available.
- Open the minimap, select a landmark, inspect the highlighted route, and choose **Walk there**. Opening the map pauses movement. The atlas uses the current region; it never switches regions by teleporting.
- The forge keeps material errors and successful crafting visible inside its dialog. The recipe refreshes immediately after crafting.
- Navigation checks the character's feet and the entire route segment. Buildings, crop plots, the entrance sign, and river banks are solid. The bridge is the river crossing.

## Verification scope

Automated checks cover core rules and route segments, the complete chapter, save roundtrips, forge notices, region-specific maps, and joystick pointer events in a 390×844 touch-enabled Chromium context. Screenshots are retained locally in artifacts/. Physical iOS/Android device behavior has not been verified; test simultaneous joystick and attack on the target phone during acceptance.

Existing version-1 saves remain compatible. A saved position inside a newly blocked prop returns to the safe spawn while keeping inventory and quest progress.
