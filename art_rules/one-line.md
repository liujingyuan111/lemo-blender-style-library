# 一笔画 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/one-line/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`69d26cb06f48ab6b03c12a76c2390d0945cdaddc38bc109b7d5e292b9af1399b`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

- **One continuous line** on warm white paper. The pen never lifts: in code the whole film can literally be one point array, from the first touch of the nib to the last frame.
- **Everything is a line**: characters, places, objects, even time. No fills, no shading, no second line weight, no background art.
- **We watch the line being drawn**: the camera follows the nib with a little lag and anticipation.
- Besides ink there is only the paper and a soft **shadow of the pen** (the real world above the paper). One accent colour at most, used once.

Not a whiteboard explainer (no hand, no marker, no erasing, no text-heavy boards), not ink wash (no tones, no brush bloom as a look), not a line-art animation with cuts and many strokes.

## 2. Materials & rendering

- **Paper**: warm white (around `#F4EFE4`), procedural mottling (soft-light, large tile), long fibres that fade out when zoomed out (or they shimmer), a sparse paper-tooth speckle over the ink at close zoom, light vignette. All textures anchored to the paper; they move with the camera.
- **Ink** is a filled polygon around the path (not `ctx.stroke`), mixed with paper colour to an opaque tone per point.
  - Width = base width of the current "voice" of the line × pen pressure × fine noise (±8 %); pressure from speed: `0.66 + 0.8·exp(−v/300)` (fast = thin, slow = fat).
  - The line's character can change along the path (base width, alpha, tremble, dryness); blend over a short stretch at boundaries.
  - Ink bleed: the same polygon slightly wider, blurred on an offscreen layer, composited at ~20 %.
  - Pooling: extra round dots where speed drops low.
  - Tremble (perpendicular noise) and dry-brush gaps (long-scale noise + thin bristle strands) for age, fear or fatigue.
  - A stop leaves a teardrop-shaped blot: tip at the nib, belly sagging downward as it spreads, a dark tide line at the rim.
  - **A screen-space minimum width**: widths scale with zoom like a line under a macro lens, but clamp the zoom used for width during pull-backs so a wide view keeps its weight.
- **The pen is never drawn**: a soft blurred wedge of shadow from the nib and a tiny contact dot. Hands, if any, appear only as shadows, each hand composited as one flat layer.
- **Path design**: chapters written as SVG path strings, sampled by arc length, joined by tangent-continuous connectors; time assigned per point weighted by curvature.

## 3. Colour logic

- **Ink on paper.** A warm black (around `#1D1A17`) on warm white; nothing else fills the frame.
- **One accent at most, used once**, on a stretch of the line that means something; it returns to ink afterwards and stays visible in the final picture if the picture is revealed.
- Examples of an accent's job: red for love or danger; blue for water or cold; gold for money or a prize. Never a second accent.

## 4. Type & subtitles

- **Text is written, like the line**: a handwriting face (e.g. Caveat) for subtitles, ink at ~84 %, no box, centred near the bottom, **written on** left to right (~0.2 s + ~17 ms per character) behind a soft paper-coloured halo so passing lines never cross the letters; fade out ~0.45 s. Hold ≥ max(1.8 s, speech + 0.6 s).
- Titles in a monoline connected script (e.g. Sacramento: itself a one-line drawing), written on in empty paper away from the drawing, gone before the camera moves into them.

## 6. Camera grammar

A vocabulary, not a route. The camera is one continuous move: composition centre, zoom, a few degrees of roll, and a follow weight (0 = composed, 1 = locked to the nib); the follow point averages the nib over roughly −0.55…+0.4 s (lag and anticipation), with a soft clamp keeping the nib inside the central ~70 % of the frame. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Follow the nib (high follow weight) | travel; momentum; a thread of time | a journey; a process; a timeline |
| Composed frame, low follow weight | a scene that must read as a whole | a vignette; a joke; a diagram |
| Macro on the nib | intimacy; the act of making | a first touch; a signature; a detail |
| Hold with a slow push-in | weight; a stop | a loss; a doubt; a decision |
| Mirrored framing | rhyme across time | parent and child; before/after |
| Continuous pull-back | everything was one picture | a reveal; a map; a word |
| Lateral scroll with the line running ahead | a horizon; a graph; a race | a stock chart; a heartbeat; a road |
| Roll with the line | vertigo; play | a loop-the-loop; a fall; a dance |

No cuts. Transitions are morphs: the last stroke of one image is the first stroke of the next.

## 9. Pitfalls of the medium

- **Stray connectors ruin a reveal**: every extra line reads as a wrinkle, beard or mask. Fix the topology (where each chapter enters and leaves), not the drawing. Plan it like an Euler path: a closed motif is a circuit (you leave where you came in); retrace or reorder chapters.
- Each region of a final picture is drawn exactly once; connectors must fall on natural lines of that picture.
- **Test the reveal early and often**: render the whole path at once at final scale after every change.
- Lines drawn too close braid together once width is applied; keep a gap.
- A round blot reads as a mole → a sagging teardrop.
- Thin lines at wide zoom → clamp the width zoom.
- Translucent hand shadows double-darken where they overlap → one layer per hand.
- Titles collide with the drawing as the camera moves → check every frame of the title's window.
- Whisper mishears short lines → rephrase rather than fight it.

