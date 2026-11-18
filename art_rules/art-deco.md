# 装饰艺术 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/art-deco/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`d73b30c0fa6d153487549d32d8c6c599733cf5e7576badec862a12da6d284761`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

A world built from **gold keylines on warm black**, filled with **airbrushed hard-edged volumes** (Cassandre, Lempicka), organised around **one vertical axis**. Ornament *is* the picture: sunbursts are backgrounds, stepped arches are frames, a dial is a progress bar, a bulb marquee is a reveal. Motion is **mechanical and symmetrical**: things unfold from the centre, doors split along the seam, lights switch on in counted order. Native register: glamour with a clock ticking (an event, a deadline, a launch).

Not a gold-foil slideshow (things move and have volume), not Art Nouveau (no whiplash curves, no flowers), not a flat vector poster (volumes are airbrushed and rimmed), not a 60s spy title (no silhouettes on flat colour).

## 2. Materials & rendering

- **Ground**: warm lacquer black, never neutral grey-black; a night sky may drift toward a deep emerald near the horizon.
- **Gold is a banded metal gradient** (dark – light – hot – light – dark); animate its `sheen` offset for a light sweep.
- **The signature stroke** (`gline`): a dark engraved underline ~1.6 px wider than the line, the gold gradient line, and a hairline highlight on top. Optional glow and a parallel twin (`double`). Nothing gets a black cartoon outline.
- **Volumes**: hard edge + airbrush (`airbrush`): a directional gradient from shade to light inside the shape, one consistent light direction (upper left by default), a thin gold rim on the lit side.
- **Motifs** (sunburst, stepped arch / ziggurat, fish-scale, chevrons, fan, four-point sparkle, speed lines, clock face, dial) are structural (a background, a frame, a transition), not stickers.
- **Perspective is real**: true one-point (mode-7 floors) and two-point perspective through a pinhole camera, so dolly, tilt and pan change perspective instead of scaling flats.
- **Characters are deco too**: about 7 heads tall, tapered streamline bodies, faceted lacquer planes (Lempicka), almond or arc eyes, a one-stroke nose, airbrush + gold rim. Give each lead one or two silhouette marks readable at a quarter of frame height.

## 3. Colour logic

- Three constants: **warm black ground, gold line and metal, ivory** for paper, gloves, light and type.
- **One saturated accent reserved for the protagonist** (or the one object the story follows). It is the only large saturated area, so the eye finds it in any wide shot. A cooler jewel tone may carry secondary surfaces, never competing in area.
- **The one-colour exception**: any single element can be drawn in its own colour through the same fill + keyline + glow (`color` option) while everything else stays gold.
- Always expand hex to six digits in code (three-digit hex breaks colour mixing).
- Examples of the triad (accent / jewel / metal): burgundy / emerald / gold; coral / sapphire / pale gold; jade / plum / rose gold. Our demo's actual values are in DEMO.md.

## 4. Type & subtitles

- **Type (OFL)**: Limelight (titles), Poiret One (numbers, sign skeletons, plaques), Josefin Sans (subtitles, labels), Italiana (numerals).
- **Titles are architecture**: a stepped gold title bar over an arch or sunburst, optional badge and wings; drawn on in gold, then a sheen sweep.
- **Subtitle card** (`subtitleCard`): a lacquer bar (~88 % black) with stepped ends like the title bar, double gold keyline, Josefin Sans SemiBold ~40–42 px ivory, an optional small speaker icon per voice. It **unfolds from the centre** like every other title, so titles, subtitles and transitions are one system. Hold ≥ max(1.8 s, speech + 0.6 s).
- Numbers carry plot without narration: dials, clock faces, floor medallions, badges.

## 6. Camera grammar

A vocabulary, not a route. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Symmetric split (two door leaves hinged at the edges; or a revolving-door wipe) | a threshold crossed | a new place; a new chapter; a reveal behind a façade |
| Leaves sliding shut over the live shot | a door closing on a moment | leaving; a decision made; the end of an era |
| Extreme low-angle Cassandre tilt | scale and aspiration | a goal far above; a tower, a rocket, a monument |
| Architectural section (pull out to a cutaway of the whole building) | progress through a structure | climbing, descending, a process in stages; a company's floors |
| Busby Berkeley overhead, mirrored and rotating | people become pattern | a team, a release, a celebration, a system of parts |
| Push-in on a dial, medallion or clock | the number is the plot | a deadline; a count; a milestone |
| Match-cut on shape (circle → circle, ray → ray) | two places, one rhyme | jumping between departments, cities, eras |
| Low oblique along a sign or marquee | light travelling letter by letter | a name revealed; a launch; a score being counted |
| Pull back from detail to skyline | where the moment sits in the world | aftermath; a city-wide effect; scale |

Framing: the centre axis is sacred; an asymmetric frame must resolve to it within the shot. At an emotional peak the protagonist fills ≥ ~1/3 of frame height (smaller, the face reads as a prop in the ornament). Transitions: splits, revolves, arch openings, shape matches; never a generic dissolve or slide.

## 9. Pitfalls of the medium

- Bulb signs from glyph skeletons break on curves (G, S, R): Zhang–Suen staircase pixels fool a neighbour-count junction test → use the **crossing number** and weld chain ends within ~14 px.
- A generic cartoon character looks pasted in → characters are deco (§2).
- Fish-scale reads as brickwork → lower half-circles row by row, each overlapping the previous row, plus an inner arc.
- Door leaves over a flat "interior" read as a blank frame → draw only the leaves, closing over the live shot.
- A gold point on pure black trips `blackdetect` → lift the background wedges and glow slightly.
- Period loudspeaker distortion is unintelligible under music → gentle drive; whisper-check every line on the final mix.

