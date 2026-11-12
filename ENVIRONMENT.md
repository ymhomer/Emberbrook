# Emberbrook environment

2026-11-11: Development project isolated under development/emberbrook.

- Node v24.22.1 / npm 11.19.1, existing host tools.
- Phaser 3.90.0 and Playwright 1.56.1 pinned in package-lock.json; project-local node_modules, install scripts disabled.
- AI map generation used imagegen; Pillow from the existing shared photo-retouch tool environment processed WebP maps and original sprite assets. No other application's dependencies were changed.
- Browser: official Playwright Chromium Headless Shell 141.0.7390.37, build 1194, project-local artifacts/browsers. Ubuntu 24.04 fallback selected for Ubuntu 26.04 compatibility and actually launched.
- Missing browser/font libraries were downloaded with apt-get download from configured Ubuntu official repositories, extracted under artifacts/browser-libs, never installed system-wide. Library package list and hashes retained with local validation artifacts.
- Fontconfig uses artifacts/fontconfig.xml and a project-local font cache, scoped to the test process. No global environment changes.
- Browser verification uses file:// and an approved command outside the restricted command sandbox because browser startup system calls are blocked inside it. No HTTP server, open port, global installation, service change or production deployment.
- Web-deliverable assets are self-contained. Font subsets are embedded into CSS for reliable local-file opening and are also retained with their OFL licenses.
- Current QA evidence: docs/BROWSER_VALIDATION.json and artifacts/*.png. Do not infer remote GitHub Pages publication from local checks.

2026-11-11 v0.2: reused the existing isolated runtime and pinned dependencies. Updated the local font subset for atlas labels. Published hosting target: https://ymhomer.github.io/Emberbrook/. No host service changes.

2026-11-11 v0.3: original woodland and traveler art generated with built-in imagegen; runtime assets prepared with existing Pillow tools. No new dependencies installed. Reused project-local Chromium for complete gameplay and high-DPI mobile checks.

2026-11-12 v0.4: reused pinned Phaser/Playwright and existing Pillow tools. Original NPC sheet generated through built-in imagegen; derived sprite, water-mask and bridge-foreground assets stay in the project. No new dependencies, global settings or services. Local-file pixel comparison uses a test-only browser file-access flag; normal play does not require it.

2026-11-12 v0.5: reused existing dependencies and isolated browser/Pillow runtime. Built-in imagegen produced original NPC animation sheets, large dialogue standees, a west-entry woodland edit and a north-entry meadow. Optimized standees use alpha WebP. Project writes ran through scoped permission escalation because this turn started read-only; no host settings or services changed.
