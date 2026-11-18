# 扁平尺度漫游 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/flat-space-explainer/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`a56b7e17f818efd1fe9ab3edcbd2f6b7a5c1bce8dcedd896e817089ac12c2b58`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

- **Flat and opaque**: every object is a solid colour plus at most one shade step. No gradients, blur, transparency, outlines or drop shadows.
- **Glow is two hard rings**: anything bright sits on two concentric solid discs one and two steps lighter than the night ground, like a screen print.
- **True scale inside each frame, a readout for the camera**: things in one frame are drawn to one scale; a corner ribbon (a log track with a few stop icons) and a field-of-view number come from the same camera.
- **A guide with a lens for an eye**: a round, friendly character whose single eye is a zoom lens. Where it looks, the camera goes; its signature is a dotted sight line fired from the lens to a "next stop" ring.
- **Next-stop ring**: a sun-yellow circle, a dashed outer ring, a leader and a two-line label mark the point the camera dives into.

Not Isometric Infographic (no isometric projection, no dioramas), not Data Storytelling (no charts on paper), not a 3D soft-body render (no rim light, bloom or depth of field), not Sci-fi Hologram HUD (no glowing wireframes), not a keynote (no header bars, centred stacks or page turns).

## 2. Materials & rendering

- **SVG, rebuilt every frame** from a pure function of time; every random draw from a fixed seed. Nothing is carried from the previous frame.
- **One shade step**: draw the whole shape in the shade colour, then the base colour on a copy shifted toward the light (upper left) and clipped to the shape; what is left is a crescent at the lower right. Land, clouds and anything on a sphere follow the sphere's terminator (`twoTone`).
- **Forms**: circles, ellipses, rounded rectangles and smooth closed curves (Catmull-Rom). Thin lines are round-capped and 2.5–4 px.
- **Stars**: three colours of dots (mist, cream, sun) and a few four-point sparkles. Dots never flicker; sparkles may breathe slowly (±16 %, ~0.3 Hz, each on its own phase).
- **Grain**: none in video (a static grain sits on moving shapes; a moving grain makes flat fields shimmer). A 5 % static grain is allowed on still frames only.
- **One camera, screen = (p − C)·z + S0**, with parallax layers taking a fraction of the zoom (stars ~0.18, far objects ~0.4, the subject ~0.75, the guide 1.0). Everything that follows a subject (sight line ends, rings, labels) goes through that function. Zooms interpolate in log space.

## 3. Colour logic

- Ground: a deep night blue; its two lighter steps are reserved for glow rings and dim shapes.
- Five hues, each with one shade step: a blue (oceans, arms, nuclei, glass), a mint (land, living cells, one orbit), a coral (bacteria, blood, the guide's cheeks, one orbit), a sun yellow (the guide's body, every "pointer": dots, rings, tape, progress, sign-off) and a cream (titles, clouds, satellites, the lens ring). A muted lavender "mist" for secondary text.
- Sun yellow means *look here*. It is never a background.
- No pure black, pure white or grey.
- A scene may change its ground once for a reason (a daylight sky in the blue) and come back.

Example (our demo): night #1D2052 with rings #252A63, #30367C; blue #4D7CFE / #3A5FD9; mint #3FD8AE / #22B38C; coral #FF6B5E / #E14B45; sun #FFC84A / #F2A12F; cream #FFF4E2 / #F0DCC0; mist #9298D4.

## 4. Type & subtitles

- **Roles**: a geometric sans (e.g. Jost, OFL): titles 96–132 px weight 700 with tight tracking; labels 26–34 px weight 600; small caps tags 16–18 px weight 600 with letter-spacing 3 in mist or sun. One short Chinese line where needed in a CJK sans (e.g. Noto Sans SC Bold, subset), ≥ 34 px.
- **Two ways in**: big words rise from below their own baseline through a clip (spring, small overshoot); labels wipe left to right. Exits run the same moves backwards. No fades.
- **Labels**: a small-caps tag above, one cream line below, attached by a 2.5 px leader. One label or one big number per screen; comparisons go in the voice, the screen gives a name and a number.
- **Subtitles** sit bottom left: one Chinese line (36 px, cream) over one English line (26 px, mist), a 5 px sun bar at the left, rising in over 0.16 s. On a light ground they sit on an opaque night plate. Never wrapped; a long sentence becomes two cues. Hold ≥ max(1.8 s, speech + 0.6 s).
- The corner instrument (field-of-view label, number, ribbon) and the subtitle band are kept clear of subjects.

## 6. Camera grammar

| Move | What it expresses | Can serve |
|---|---|---|
| Log-space dolly through a shape (ring, lens, iris) | going down a level of scale | every change of scale; a chapter turn |
| Pull back from an extreme close-up | revealing who and where | a cold open; a "this is the real size" moment |
| Slow push with a 2–5 % creep | attention, reading time | a measurement; a label being read |
| Tracking with a moving thing while pulling out | travel, duration | light crossing space; a journey with a clock |
| Frame within frame (a magnifier inset) | a detail too small for the scale | an orbit's height; a cell's part |
| Shape match (a small dot becomes the next subject) | the same thing at two scales | a planet dot to a planet; a cell icon to a cell |
| Fly-through layers (clouds, skin) | crossing a boundary | atmosphere; skin; a wall; water |

Subject at least a third of the frame height at key moments; titles and labels in the free third; subtitles bottom left, instrument bottom right. Transitions are made from the medium (rings, lenses, concentric layers, a covering cloud bank); no crossfades, no hard cuts inside a zoom.

## 9. Pitfalls of the medium

- **Readable scale**: things too small to see at true scale become markers (a dot with a ring); say so with a label. Never enlarge a true-scale thing to fit the composition: change the level instead.
- **The guide's size**: viewers read it as information. State once that it is drawn larger than life, show its true size once, and say when it shrinks along.
- **A flat face**: covering the lower half of a lens eye with a colour block reads as sleepy or hurt; bend the iris instead.
- **Light grounds**: cream text and cream skin collide; put subtitles and the corner instrument on an opaque night plate there.
- **Overshoot of a pull-back** reveals the edge of the star field: lay stars beyond the frame.
- **Shimmer**: small dots moving sub-pixel are fine; random per-frame twinkle is not.
- **Hands and props** drawn as plain capsules read as extra fingers: draw curled fingers, a thumb and a knuckle line.

