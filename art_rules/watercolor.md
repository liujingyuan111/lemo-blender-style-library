# 水彩笔刷 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/watercolor/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`662d57568408a7c82ef8f64980ca85798b8bb239df3dc3a6715283d7f4555ef0`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

- **One sheet of warm, fibrous paper** under everything; it is also the eraser (paper-coloured mist washes things away).
- **Everything is individual brush strokes**: a variable-width ribbon at partial opacity plus a few thin **bristle tracks** that break into dashes (flying white). Strokes overlap and darken where they cross, like transparent pigment. No vector outlines; a darker edge stroke along a form is the only "line".
- **Things paint themselves in**, stroke by stroke, structure before detail (trunk → branches → leaves; outline wash → shadow → accent).
- **An annotation layer** in a hand the painter would write with: labels with pen leader lines, a small measured value, a quiet title.
- Tone: calm, curious, precise. Numbers are real; the palette can carry data.

Not ink wash (colour, not ink tones; no calligraphic brush-as-gesture), not impasto (no thick paint, no knife), not a children's picture book (no crayon, no cute outlines), not vector illustration with a watercolour texture laid on top.

## 2. Materials & rendering

- **Paper**: a pre-generated image (warm base, three octaves of smooth noise ±3.5 %, a few thousand short curved fibres, fine grain, light vignette), drawn first every frame.
- **Stroke** (`engine.js` `mk`/`drawS`): a ribbon whose width follows a profile (`brush`, `leaf`, `even`, `tip`, `trunk`) with ~±22 % value-noise roughness, filled as a thin wash (≈ 0.55–0.6 body opacity when bristles are present), plus 3–9 bristle tracks at 30–85 % opacity, each with a random dash pattern and a random early end: that is the flying white. A stroke can be painted up to any fraction of its length (a moving brush tip).
- **Wash**: the same polygon painted in 3 passes with jittered vertices at a third of the opacity each, so edges darken where passes disagree (a pooled watercolour edge).
- **Depth by layers**: several parallax layers of washes and painted objects; farther = smaller, lighter, less saturated; paper-coloured mist bands between layers.
- **Cache finished objects as sprites**; draw stroke by stroke only what is being painted or transformed.
- **Everything is a pure function of `t`**; any stroke made inside `render(t)` is built under a fixed seed.

## 3. Colour logic

- **Paper is the white.** Never paint pure white; light is unpainted paper.
- **Transparent layering**: darker = more passes, not a darker pigment on top. Keep 3–5 hues per scene plus ink.
- **Ink** (a warm near-black and a lighter brown) for lines, text, edges and stems only.
- **Colour may carry the data or the mood**: blend sky, ground and background by position or time so the palette itself changes with the subject. Map ramps quantised into 4–6 bands read as paint, continuous ramps read as software.
- **One accent** (a vermilion, a rain blue) reserved for one element that recurs: a stamp, a marker, a key object.
- Examples: arid-to-wet — red ochre → sage → straw → blue-grey → deep green; a harbour at dawn — `#f3e2c8` sky, `#9fb4c4` water, `#5f7486` hulls, accent `#c8442a` buoys; a vegetable garden — `#e8e0c0` soil light, `#8ea860` leaves, `#4e6e3c` shade, accent `#d9632e` pumpkins.

## 4. Type & subtitles

- An elegant serif (e.g. Cormorant Garamond) for titles and subtitles, a handwriting face (e.g. Caveat) for notes, a small mono (e.g. IBM Plex Mono, wide tracking) for measured labels, Noto Serif SC for Chinese (subset to the characters used).
- Hand notes are drawn twice over a paper-coloured halo, revealed left to right like writing, with a pen leader line that grows to its specimen.
- **Subtitles** sit on the paper, not in a box: centred at the bottom, serif italic ~36 px (2 balanced lines max), a second-language line beneath at ~2/3 size, ink at ~78 % over a paper-coloured halo. Hold ≥ max(1.8 s, speech + 0.6 s).
- Numbers are spelled out in the TTS text and written as digits on screen.

## 6. Camera grammar

A vocabulary, not a route. The picture is one painted sheet; cutting is rare. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Long lateral dolly over a continuous world | a gradient; a journey; cause and consequence | a transect; a route; a timeline |
| Vertical tilt along one object | scale; measurement | a tall tree; a building; a depth |
| Locked sheet, things painted in | study; attention | a specimen plate; a recipe; a diagram |
| Slow push into a detail | the observer leaning in | a seed; an insect; a hand-written note |
| Pull-back to a map or diagram | the whole re-framed | where it all happened; a system |
| Mist wash to blank paper | chapter end; time passing | a season; forgetting; a new place |
| Page turn / new sheet slides over | a new entry in the journal | a new day; a new species; a new case |
| Change in time on a locked view | growth; decay; history | a season cycle; before/after; deep time |

Framing: generous paper margins; one hero subject per view with its note; labels never cover the subject. Transitions: brush-edge wipes, mist, a page turn, or a continuous camera move; no hard video cuts, no dissolves between unrelated pictures.

## 9. Pitfalls of the medium

- Offscreen wash strips too short flatten tall shapes into flat tops and expose seams on tilts → size strips well beyond the frame.
- A translucent wash that ends at its canvas edge shows a hard seam under other layers → extend below the frame and fade to paper with a gradient.
- Classic scripts share one global scope: touching a `const` before its declaration in async init leaves `READY` false and every screenshot times out → build everything inside the init; read `[pageerror]` lines.
- The stroke builder consumes the global RNG: any stroke created in `render(t)` must be wrapped in `withSeed` or parallel workers disagree.
- Thousands of strokes per frame are too slow → sprite cache.
- Beat-locked animation must be re-derived when the music edit changes.
- New CJK subtitle characters fall back to another font until the subset is rebuilt.

