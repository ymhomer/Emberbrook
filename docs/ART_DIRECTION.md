# Art direction and assets

Original illustrated miniature fantasy environments, inspired by the user-supplied visual reference: warm tiled roofs, lush olive vegetation, turquoise water, amber forge light and a cooler crystal-lit shrine. Original pixel characters are a deliberate contrast to the painted map detail.

Generated map masters remain in local artifacts, not the source/release ZIP. Image generation produced new background artwork; the supplied reference itself is not redistributed. WebP delivery uses quality 94 for the village and 93 for the shrine. Foreground pixels are extracted from the village art to occlude actors walking behind buildings.

Character and NPC sprite atlases, portrait, resource sprites and favicon are authored procedurally by scripts/make-sprites.py using Pillow. The browser independently renders actors, paths, interactive markers, shadows, fire/smoke particles, water glints and combat effects. This is not a single flattened screenshot interface.

UI icons are inline SVG. UI text is live HTML or Phaser text; it is not baked into images. Noto Sans TC and Cormorant Garamond are self-hosted subsets with OFL licenses. Font sources and SHA256 values are in FONT_SOURCES.json. Phaser license accompanies its bundled runtime.
