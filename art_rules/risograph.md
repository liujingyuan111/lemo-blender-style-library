# 孔版印刷 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/risograph/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`c3d85c91a81b0afde091d964482749482adc66c12730afe124708f7b18b331a6`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

A risograph prints **one colour at a time**: each colour is its own stencil ("plate") with its own drum of translucent ink. That one fact makes the look:

- **A tiny palette**: 2–3 spot inks on warm off-white paper.
- **Overprint mixing**: inks multiply, so two inks make a third colour and all three approach black; a tint of one ink over a solid of another gives the brightest mixes.
- **Misregistration**: every plate lands a few pixels off; edges show slivers of paper or a coloured halo.
- **Halftone dots** for mid-tones, each plate on its own screen angle; **imperfect ink**: pinholes in solids, streaks along the feed direction, blotchy density.
- **Flat shapes, no outlines**: forms are colour fields and silhouettes.

Not flat vector art with a noise overlay (every colour comes from the plates), not CMYK pop-art halftone (no process colours, no keyline), not screen-print posters (riso ink is translucent and grainy, not opaque). **Never** show the RISO brand, logo or machine trade dress; ink names are colour references only.

## 2. Materials & rendering

**Pipeline.** Draw each frame into **one RGB canvas where each channel is one plate's density** (R = ink 1, G = ink 2, B = ink 3; 0 = none, 1 = solid). `source-over` gives true **knockouts**; `globalCompositeOperation = 'lighter'` adds ink only to the channels you set: a true **overprint**. A WebGL2 shader "prints" it:

- per plate: offset in px + tiny rotation → misregistration;
- halftone: cosine spot function on a rotated grid, period ~6–8 px at 1080p, anti-aliased threshold; densities ≥ ~0.9 print solid; screen angles ≥ 15° apart;
- grain on the dot threshold, pinholes in solids, density varying with a feed-direction streak and a slow blot noise;
- composite `paper × Π mix(1, ink_i, coverage_i)`, with faint paper fibre;
- dots anchored to the **paper** (screen), not to objects: a pan slides the image under a fixed screen, as if each frame were printed anew;
- a per-plate **gate** and a **roller sweep** (moving edge, slightly heavier ink band) let a plate arrive mid-shot.

**Composition rules.**
- Every area uses **at most two plates, at most one of them as a tint**. Three halftones on top of each other = mud.
- Big flat shapes, lots of solid paper and solid ink; halftone in a few stepped bands (e.g. 20 / 40 / 60 / 100 %) for skies, shadows, distance.
- Characters get a **paper-white knockout halo** (4–5 px): stamp their layer in a ring with `filter: brightness(0)` (zero ink = paper), then draw them. Plates misregister around it, so it picks up coloured fringes like a real trap.
- One horizon, one big flat field or disc, one small figure; the figure's head against the flattest colour in the frame.
- Design for the **one-plate version**: every main colour contains some of the first plate, so a one-ink frame still reads as a complete silhouette. A deliberate exception stays blank paper until its plate arrives: a reveal.

## 3. Colour logic

- **2–3 spot inks, never more**, plus paper; every other colour is an overprint or a tint. No gradients except stepped halftone.
- Pick inks whose pairs mix into useful colours; at least one must carry a silhouette alone.
- Paper is warm off-white (around `#F4EEE2`), never pure white; paper white is a colour too (knockouts, highlights, subtitles).
- Light neutral surfaces (skin): a light tint of the palest ink. Dots of a saturated ink on skin look like a rash.
- Save the full overprint (every plate, densest mixes) for the moment that earns it.
- Example ink sets: Blue `#0078BF` + Yellow `#FFE800` + Fluorescent Pink `#FF48B0`; Teal `#00838A` + Fluorescent Orange `#FF7477`; Federal Blue `#3D5588` + Red `#FF665E` + Sunflower `#FFB511`.

## 4. Type & subtitles

- **Type is printed**: titles and subtitles live on one plate, so they misregister and grain with it. A title can be printed on two plates with a visible offset: the riso double-hit.
- Fonts (OFL): heavy grotesque for titles (e.g. Bricolage Grotesque 800), geometric sans for captions (e.g. Jost 500–700). Preload every weight before `READY`.
- Subtitles: a **paper-white knockout strip** (zero ink, small radius) with text on one plate, ~40–46 px; its edges catch misregistration fringes. Hold ≥ max(1.8 s, speech + 0.6 s).
- Prints don't fade: titles arrive with a roller wipe or on a beat and leave on a cut.

## 6. Camera grammar

A vocabulary, not a route. Opening and ending come from the topic.

| Move | Expresses | Can serve |
|---|---|---|
| Wide lateral tracking, small figure, empty sky | Travel, routine, room | a commute; a process line; a title |
| Static wide, the subject crosses the frame | Comedy of scale | a gag; an arrival; a crowd |
| Locked composition: horizon, disc, figure | Stillness, awe | a decision; a reveal; the film's one pause |
| Ground-level low angle, big foreground shapes | Energy, abundance | a burst; a harvest; a launch |
| Medium two-shot held for a look | Reaction | a joke landing; a deal; a disagreement |
| Straight top-down, long shadows | Pattern, a map | a schedule; a floor plan; a game board |
| Push into a halftone field until dots are shapes | Entering the print | a close look at data; a memory; a cell |
| Pull back to reveal the paper | It was one sheet | a series; an archive; a summing-up |
| Match cut on a flat shape | Continuity through form | a time jump; cause and effect; before/after |

Framing: lots of paper and solid ink, text on empty sky or a knockout strip. Transitions: overprint growths, roller sweeps, shape match cuts, hard cuts on beats. Never a cross-dissolve, never a soft digital wipe.

## 9. Pitfalls of the medium

- Three halftoned plates in one area = mud → two plates, one tint.
- `fract(p*vec2(233.34,851.73))` draws vertical stripes across solids at 1080p → a well-mixed hash (`fract(vec3(p.xyx)*.1031)` family).
- Per-frame registration jitter and sheet streaks flicker and blow up file size → fixed offsets per shot, kicks on accents, sheet noise at cuts, partial boil.
- JPEG screenshots (4:2:0) smear saturated dots → PNG frames into a lossless yuv444 intermediate, encoded once with `-tune grain`; check at 100 % and 50 % for moiré.
- The halo layer must copy the canvas transform, or zoomed shots draw the subject at the wrong scale.
- Additive `over()` inside a transparent layer loses its meaning → overprint on the plate canvas.
- A main colour without the first plate floats loose in one-ink frames → build palette recipes up from the one-ink silhouette.
- `evenodd` fills of arches fill solid → trace the inner edge in the opposite direction.

