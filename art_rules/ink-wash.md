# 中国水墨 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/ink-wash/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`5d71598f0b9cf4034c6461956b0d8bd63bd33750b4045376044f0d956b01d645`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

An ink painting (水墨) painted and unrolled before you: black ink on warm rice paper in five tones, plus **one** red, the vermilion seal. No Western outlines: forms are made by **loaded brushstrokes** whose dark edge *is* the contour (没骨, "boneless" painting), by **wet washes** that bleed into the paper, and by **dry, fast strokes** where the paper shows through the bristle tracks (飞白, "flying white").

Most of the frame is **empty paper** (留白): water, sky, mist, silence. Things are *painted into existence*, not cut to.

Not watercolour (no colour washes), not vector art with a brush texture (no flat fills or closed outlines), not a calligraphy title sequence.

## 2. Materials & rendering

- **Paper** is procedural, in the compositor, never a texture file: warm rice paper (around `#F2ECDE`), cloud mottling, long fibres, pulp flecks, grain that fades when zoomed out (or it shimmers), a light vignette; anchored to the world.
- **Ink** is stroke opacity multiplied onto paper (never an overlay), in five tones (墨分五色):

| Tone | Opacity | Use |
|---|---|---|
| 焦 jiao (burnt) | ~.96 | calligraphy, the sharpest lines, moss dots |
| 浓 nong (thick) | ~.82 | contours, dark edge of loaded strokes |
| 重 zhong (heavy) | ~.60 | secondary lines, folds |
| 淡 dan (light) | ~.34 | mountain bodies, robe and body washes |
| 清 qing (clear) | ~.16 | far mountains, faces, mist |

- **Brushstroke model**: centreline × pressure profile × width noise, plus 4–60 **bristles** whose ink load drops along the stroke and breaks on long-scale noise. `dry` runs from a solid wet stroke to flying white (dry strokes are bristle tracks only).
- **Loaded stroke**: bristles darker on one side, so the stroke carries its own contour: this makes bodies, rocks and waves read as ink, not vectors.
- **Two layers**: the wet one bleeds in the compositor (noisy blur, **edge pigment accumulation**, granulation); the dry one only gets fibre jitter and paper tooth.
- **Masses**: soft polygons, jittered edges, a gradient; never flat fills.
- **Landscape**: mountains dissolve downward into mist bands, with 披麻皴 texture and 苔点 moss dots on near ranges only; rocks are outline → axe-cut texture → shadow wash → dots.
- **Water is blank paper**, moved by faint dry streaks and open ink rings. Solid water: Song-dynasty **parallel wave lines** (dense near the edge) or a pale body with a few huge loaded strokes along its face.
- **Figures are xieyi**: one pale body mass plus two loaded strokes, burnt-ink lines for limbs; features, if ever shown, in 3–5 strokes.
- **Calligraphy**: an OFL brush font is only a **skeleton**: trace centrelines in stroke order, pressure from glyph thickness, hidden-tip entry (藏锋), tapered exits.

## 3. Colour logic

- Ink only, from cool grey at low density to warm black at full density. No other hue in the world.
- **One vermilion** (around `#B02E22`), for the seal and at most one tiny accent in the story (an object the protagonist carries). The accent finds the protagonist in wide shots and can rhyme with the seal. Never a red wash, never red type.
- Values carry depth: far = pale and soft, near = dark and textured. If a frame gets busy, remove ink rather than add tone.

## 4. Type & subtitles

- Subtitles are **inscriptions (题跋)**: a classical italic serif (Cormorant Garamond italic), ink-coloured, no box, ≤ 2 lines, placed in each shot's empty paper. A small vermilion square marks the start of each line. They appear wet and dry in a fraction of a second. Hold ≥ max(1.8 s, speech + 0.6 s).
- Titles are written on the painting itself, in vertical columns in its empty space, with a vermilion 白文 seal drawn by code (lines knocked out of a slightly irregular red square, with ink-paste speckles). They move with the world.
- Screen-space overlays reset the camera transform.

## 6. Camera grammar

A vocabulary, not a route. Opening and ending come from the topic.

| Move | Expresses | Can serve |
|---|---|---|
| Locked frame on the paper | The page is the stage; things are painted in | a thing forming; a line being read; a still decision |
| Right-to-left pan (handscroll) | Time and distance as one painting | a journey; a history; a process |
| Vertical tilt (hanging scroll) | Height, stages stacked | seasons; a climb; generations |
| Lateral tracking, lead room, slow far parallax | Motion through a world | travel; a chase; a commute |
| High wide, a tiny figure in blank paper | Smallness, solitude | loneliness; nature's scale; one life among many |
| Low angle, dark mass towering, slow push-in with shake | Weight, threat | an obstacle; a storm; pressure |
| Hard cut to an extreme close-up | A break in the flow (the style's only hard cuts) | a decision; a shock; a memory |
| Push into an ink bloom or mist | Passing between states | memory; dream; a season turning |
| Pull back until a mark joins the whole | The part was inside something larger | a summing-up; irony of scale |
| Return to an earlier framing | The rhyme shows what changed | aftermath; growth; before/after |

Framing: 60–80 % empty paper; dark foreground may pass along the frame bottom. Transitions are ink blooms, pans along the scroll or mist; never a generic dissolve or a wipe.

## 9. Pitfalls of the medium

- Dry brush looks like dashed lines → breaks from long-scale noise and an ink load that drops along the stroke.
- Parallel semi-transparent strokes make bodies look like organ pipes → one base mass + two loaded strokes.
- Big side-brush strokes look like a hairbrush → a gradient mass + a few low-dryness strokes. Gradients in vertical bands leave seams → a cached per-pixel layer.
- A stroke body split between wet and dry layers loses density → full body in the dry layer plus a wet halo.
- Clipping calligraphy with the font outline notches the junctions → font as skeleton only.
- Uniform hatching inside a wave turns it into a wire mesh → loaded strokes along the face.

