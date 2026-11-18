# 胶片直刻 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/scratch-film/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`79be9b3664338fb2f7f1877acaff9ec7a7ec0946fda096bc1c3e96bf9a64ec86`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

These define the style; keep all of them.

- **Black is the ground, light is a cut.** The frame is warm black emulsion. Everything bright is a scratch (one cream colour); everything coloured is transparent dye laid in or beside the cuts. A bright area is dense hatching, never a flat fill.
- **The line boils.** Each drawing is redrawn with a new hand tremble at 15 drawings a second: several near-parallel passes per line, uneven width, skips, chipped edges, an overshoot tail. Even a held frame moves.
- **The whole frame is the drawing.** Sea, sky, a room, a map: the world itself is scratched and dyed, edge to edge. The style is not a strip of film shown inside a scene.
- **The cut is visible.** Marks appear behind a hot point (a white core, a glow, chips flying): the act of making is part of the picture.

Not a chalkboard or whiteboard explainer (no flat board, no clean vector strokes), not Ink Wash (no wet tonal washes, no paper), not ASCII / CRT (no raster, no character cells), not a neon sign (no tubes), not a collage (no photographs). Film props are not the subject: perforations, frame lines, film strips, projectors and countdown leaders appear only if a story is about film itself, never as decoration.

## 2. Materials & rendering

Reference: how our engine does it (`demo/js/base.js`); another stack is fine if the marks read the same.

- **Layers.** One 2D canvas per frame: a mottled emulsion plate (warm and cool blotches, a rotating set of four), the scene's marks in painter's order, then the light pass: two blurred additive copies for halation (about 9 px and 28 px at 1080p), dust specks and short curls, a corner falloff, a one-drawing flicker, a weave of about 1 px, grain added at mastering. No long vertical hairlines (they read as film damage).
- **The needle line** (`scratch`): a Catmull-Rom path resampled in screen space, 2–3 passes offset by the tremble, width varying along the stroke, about 1 % skips, small triangular chips on heavy lines, a thin overshoot tail. Width follows the picture's scale; the tremble is in screen pixels (about 0.7 × width, capped at 5 px), so a close-up and a wide shot both look hand-cut.
- **Dye** (`dye`): 4–8 thin translucent bristles along a path, tapered at both ends: reflections, rays, wakes.
- **Fills** (`hatch`): back-and-forth zigzag hatching that overshoots the outline, two passes at different angles. Large light (a sky, a glow from above) is several sparse hatch layers stacked into a gradient, or drawn on its own layer and faded with a gradient mask; never stepped bands (they read as film frames).
- **Text as cuts.** Words are rendered once as images with thin skips through them and cut in left to right behind the hot point; they tremble by less than a pixel and are never re-lettered per drawing.
- **Depth.** Depth of field is a blurred copy masked by a disc around the subject; background creatures can be drawn on their own layer and blurred. Keep blur ≤ 5 px on bright hatching or it melts into a flat fill.

## 3. Colour logic

- Ground: warm black `#050403` with brown and blue mottles; never grey.
- Light: one cream `#FFF4DC` for every cut. Strong light (a sun, a glow from above, the hot point) is the same cream, denser.
- Dye: a few transparent colours laid by hand, alpha 0.5–0.9, always with cream lines on top. **One dye, one kind of thing, for the whole film.** Our demo: teal `#1FB39A` the hero, blue `#2F86FF` living light, red `#FF3220` danger, yellow `#FFC81C` sun and moon, green `#46D65A` small food.
- Values: black dominates (≥ 50 % of most frames); the brightest point is a fresh cut or a light source.

## 4. Type & subtitles

- Words belong to the drawing: a depth figure beside a scratched ruler, a title cut into the dark. No boxes, no outlines, no drop shadows.
- Faces (all OFL): a heavy geometric sans filled with diagonal cuts for titles (Jost 800), a sturdy mono for numbers (IBM Plex Mono SemiBold), a marker-like Chinese face (LXGW Marker Gothic). These are references; any face with the same roles works.
- Subtitles sit low left, Chinese above English, cream on the black ground, revealed left to right in about 0.3 s. Cap height ≥ 30 px for anything the viewer must read.

## 6. Camera grammar

| Move | What it expresses | Can serve |
|---|---|---|
| a mark cut live, the camera still | something being made | a first line, a title, a signature, a correction |
| one continuous log-scale pull from one mark to a whole place | scale; "all of this from that" | a reveal, a system, a crowd |
| a descent or climb past a scratched ruler | distance, depth, time | a journey, a countdown, a timeline |
| tracking alongside, specks streaming in parallax | travel, effort | a climb, a chase, a commute |
| from below into hatched light, the subject a black silhouette | exposure, being seen | danger, a reveal, a spotlight |
| split screen, two views on one beat | cause and effect | action and its result, plan and outcome |

- Keep the subject ≥ 1/3 of the frame; never hold a frame that is mostly empty black for more than a second without a mark being made.
- Transitions happen inside the medium: a cut line that becomes a divider, a push into a point of light, a pull to a wide shot. No wipes, no page turns, no white flashes.

## 9. Pitfalls of the medium

- Flat bright areas look digital: always hatch; stack sparse layers for gradients.
- Large light drawn as segments or bands reads as film frames: fade it with a mask instead.
- Tremble scaled with zoom shakes macros and blurs wide shots: tremble in screen pixels, width from the picture.
- Boiling text becomes unreadable: tremble ≤ 1 px on text, never re-letter a word per drawing.
- Too many full characters overlapping on screen turn into noise: fewer, smaller, placed by hand around the hero.
- Particles positioned by speed × absolute time jump whenever the speed changes: offset them by the camera's displacement instead.
- A crowd of glowing points generated in boxes shows the box edges: use soft (Gaussian) distributions per level of detail.

