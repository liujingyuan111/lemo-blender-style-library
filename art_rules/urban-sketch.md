# 钢笔淡彩 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/urban-sketch/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`2baf1a19f31b06e55d66d62e4c3449c7a2686c689190976f3e3d0cbdce2faa9a`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

Reportage drawing, made on location in a few minutes. Two layers that stay visibly separate:

1. **Ink.** One thin, near-constant line (a 0.3–0.5 mm fineliner) in dark sepia. It wobbles slightly, overshoots corners by a few pixels, breaks mid-stroke, and suggests rather than describes: a few window marks instead of a grid, scalloped fragments instead of a whole tree outline.
2. **Wash.** Transparent watercolour glazed on top, **misregistered** by 1–3 px from the line, sometimes spilling past it, leaving paper white for highlights and figures (reserves). Dried edges are darker (pigment pools at the rim), and pigment granulates into the paper tooth.

**The page is part of the image**: warm cream cold-press paper with large-scale mottling and fine tooth. Nothing is painted edge to edge; the painting frays into leaf-sized dabs and white holes, leaving margins for handwriting.

Not Watercolor Brush (no line-free wet-in-wet painting, no painterly edges without ink), not Whiteboard (no marker, no explainer diagrams), not Chinese Ink Wash (no brush calligraphy, no monochrome ink tones). Line and wash, both, always.

## 2. Materials & rendering

- **Paper**: two octaves of fbm mottling (a few %), a tooth tile multiplied over everything, figures included.
- **Ink**: ~96 % coverage; world line width thinner far, thicker near (e.g. 1.3–3.4 px); wobble ~1 px; overshoot 3–8 px; a third to half of long strokes get one small gap. Strokes are baked with their **draw time per pixel**, so the shader plays back stroke order.
- **Wash**: 2–3 rough-edged layers, multiply, alpha ~0.4–0.65, offset from the line by about one line width, a dried edge at 30–40 %; granulation = pigment × (0.82 + 0.36 · fbm).
- **Colour arrival field**: every pixel has a time at which colour reaches it. The wash is revealed through it with a ragged wet front (darkened band just behind the front) and noisy edges. Figures bloom from a point with a noisy circular clip.
- **Foliage**: pale base wash, then light and shadow masses, then small leaf dabs coloured by light direction, holes at the rim, scalloped ink only on the outline.
- **Sky**: a few big soft washes at low alpha, fading upward; clouds are reserves with a tinted belly.
- **Buildings**: local colour; shadow side mixed ~45 % with a cool violet-grey; distant blocks mixed ~50 % with a haze colour.
- **Figures**: a 3D skeleton in orthographic projection; torso from cross-sections; limbs as organic tapered tubes; hair and head as one mass; face left blank (one nose tick in profile); shadow side mixed with violet.
- **Page edge**: a noisy boundary, a white-dab band inside, a coloured-dab spray outside.
- Deterministic: same seed, same marks.

## 3. Colour logic

- **Ink is one colour** (dark sepia or warm black); it never changes.
- **Wash is local colour, lightly**: few pigments, mixed on the page; shadows are the local colour mixed toward one shared cool violet; distance mixes toward one haze.
- **Paper white is the brightest value**; it is reserved, never painted.
- **Colour can be withheld**: a page may be ink-only with colour as an event (one tinted object, colour arriving with a cause).
- Example palettes: park in summer (lawn `#c3c96f`, leaves `#7fa04a`, sky `#9fbcd6`, limestone `#d8c6a0`); harbour morning (sea `#7fa6b8`, hulls `#c9573f`, rope `#c8a86b`, sky `#bcd0dc`); winter market (roofs `#8b93a6`, lights `#e2b04a`, awnings `#b8483e`, snow = paper).

## 4. Type & subtitles

- **All text is handwriting on the page**, written on left to right with pen sound, and moves with the camera: a corner note (e.g. Reenie Beanie: day, time, weather, place), titles and colophon in a casual hand (e.g. Caveat 500–600), left-aligned in the blank margin.
- **Subtitles**, if there is a voice: handwritten lines in the page margin or a caption strip written into the lower margin, never a generic overlay box. Hold ≥ max(1.8 s, speech + 0.6 s).
- The style works well without any voice.

## 6. Camera grammar

A 2D camera over a large page (e.g. 5120 × 2880). Designed moves use cubic easing; follow shots use a critically damped spring on a lead-ahead target, so the camera lags like a hand-held follow. A vocabulary, not a route. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Push-in | attention; a detail observed | a face; a sign; a small event |
| Lateral follow on a spring | travel, pursuit | an object carried; a walker; a vehicle |
| Crane up | a new level, a view opening | a skyline; a tree; a balcony |
| Whip-tilt with slight roll | sudden change of direction | a fall; a gust; a surprise |
| Punch-in with a short shake | impact | a catch; a collision; a door slam |
| Pull back to the whole page | scale; the sketch as an object | a summary; a place in full |
| Tilt into the margin | from picture to words | notes; a date; a title |
| Slow pan across a line-only area | the world before colour | a quiet start; memory |
| Hold while the pen draws | the act of noticing | a subject being drawn |
| Page turn to a new spread | another time or place | a travel diary; a sequence of days |

Framing: subjects ≥ ⅓ of frame height at story beats; a small key object gets a faint paper halo (reserve) so it reads over busy foliage. Transitions: camera travel on the page, page turns, or colour arriving; no dissolves.

## 9. Pitfalls of the medium

- **Straight edges in the colour field** from clipping by a bounding box → clip by the actual noisy distance.
- **Rectangular masks around complex silhouettes** leave notches → mask with the real stepped silhouette.
- **Characters losing colour** when they move into unpainted areas → sample arrival once (or tie it to the event), never at the current position.
- **Static ink can't be occluded by later washes** → erase far ink inside nearer shapes before drawing; use carrot people for far crowds.
- **IK feet pinned while blending poses** splay the legs → blend foot targets toward under-hip.
- **Front-facing heads go bald** → draw the hair mass, then knock the face out of it.
- **Big canvases in headless Chrome**: pack ink and time into RGBA byte textures yourself and upload the arrival field as a filterable float texture (`R16F`).
- **Painting edge to edge** kills the sketchbook feel → leave margins and fray the edge.

