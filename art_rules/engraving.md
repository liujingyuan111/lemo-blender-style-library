# 铜版画 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/engraving/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`0c6816b8b47163d158ae0ea668feecf53dcbef9d1310e27b9e797d9b9e7aac0d`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

An **intaglio print**: the line is ink held in a groove a burin cut into copper. Three rules:

1. **Tone is made of lines, never of fills.** Light is bare paper; half-tone is one family of parallel lines; shadow a second family crossing it; the deepest dark a third, lozenge-making family. No grey fill anywhere in the ink.
2. **Every line swells and tapers.** The burin enters fine, bites deeper mid-run and lifts out to a point. Lines thicken where the form turns from the light and vanish where it faces it; contours are cut in several runs and thin where runs hand over. A uniform-width line reads as a pen or vector drawing — never.
3. **Colour comes afterwards, by hand**: transparent watercolour laid flat region by region over the finished black print, spilling past the lines, pooling at its edges, ink always on top. A film may stay monochrome long; colour arriving is an event.

Not a woodcut (black block, white gouges — `woodcut`), not a pen sketch (loose broken lines — `urban-sketch`), not an engineering drawing (`blueprint`), not a sepia filter.

## 2. Materials & rendering

- **The sheet is the world**: 1920×1080 world units of laid paper (cream, ~`#f1e8d2`) with world-space texture (fibres, laid lines, sparse foxing) that zooms with the camera; a pressed, bevelled **plate mark** and a ruled border (rule + hairline) frame it.
- **Ink** is one warm near-black (~`#1c1510`). Width ratios: outlines heaviest (swelling ×0.45–1.35), first hatching from a hair (~0.18 px) to ~2 px, crossing ~0.8×, third family ~0.6×, hair and stipple finest. Spacing is **relative to the figure** (~1/180 of its height, a little wider per later family) so small figures never go grey.
- **Swell law** for every hatch line: width × (0.2 + 0.8·sin(πu)^0.7), tapered over its first and last ~22 %. Families switch on by tone thresholds (~0.14, ~0.5, ~0.75 on a 0–1 tone).
- **One light direction** for the whole film (upper left by convention); heavier outlines away from it; tone fields come from the shape (pillow lighting, analytic spheres and cylinders), never from texture. **Occlusion** is geometric: lines stop at the shapes in front.
- **Roundels**: double-ruled circle, ruled-machine ground with a white halo round the subject, content authored at a large radius and scaled in. **Leaders**: hairlines from a dot on the part to the rim, routed with clearance, a small italic figure number at the root.
- **Hand colouring** multiplies over paper and under ink: a few px of spill, slight misregister, tide-line at the wet edge, low-frequency density lift, occasional backruns, granulation; each region blooms from where the brush touched.
- **Copper** (when shown): polished warm metal, polishing hairlines, a soft reflected window; grooves = dark trough + bright burr toward the light. The **burin** (lozenge steel shaft, bevelled face, mushroom handle) is held low and turned ≤ 15° off the line so the fresh groove shows; **swarf** is a narrowing ribbon curling ahead of the point, one edge lit.

## 3. Colour logic

- The print is two values, paper and ink; all tone is line density.
- Colour is **transparent wash only**, in muted earth and mineral pigments, one stronger pigment at most. Never opaque, never on lettering, rules or paper outside the figure.
- Reserve it: the whole subject at one moment, or only the part that matters — or none.
- Example wash sets: an amber insect with blue-grey wings; a map with a sea-green coastal band on buff land; one madder-rose organ on an otherwise black anatomy plate.

## 4. Type & subtitles

- Lettering belongs to the plate: **roman capitals** (Bodoni Moda; title ~44–56 px, wide tracking; labels ~15–19 px), **italics** for scientific names (~20–24 px), **script** (Pinyon Script) for notes, fixed size, balanced over two lines, never shrunk.
- Roman letters are **cut glyph by glyph**; script is **written** in one left-to-right stroke. Nothing fades in.
- Subtitles: script on a deckled paper slip, bottom centre, ≤ 2 lines, never over a label. Hold ≥ max(1.8 s, speech + 0.6 s). An engraved note stays in frame chars ÷ 12 + 1 s from when it starts writing.

## 6. Camera grammar

The camera is a **loupe over a sheet**. A vocabulary, not a route. Opening and ending come from the topic.

| Move | Expresses | Can serve |
|---|---|---|
| Loupe following the burin tip | One point of attention; making | a first mark; a signature |
| Log-zoom pull-out | The line was part of something larger | scale reveal; context |
| Push to a part, ride with its roundel | Where → what, in one take | an invisible detail; a mechanism |
| Tilt/pan along the sheet at reading zoom | Labels in order | a parts list; a coastline |
| Pull back while something flies | Everything placed in relation | acceleration; summary |
| Locked frame, or a ≤ 2 % breathing push | The plate as document | reading time; colour moving |
| Raking view across the copper | The groove as depth | the cost of craft |
| Cut from mirrored copper to true proof | Reversal | a hidden truth; before/after |

Framing: subject inside the plate mark, labels and roundels in the margins; order details so push-ins never crop a note early. Transitions from printmaking only (proof pulled, tissue guard laid over, region burnished out and re-cut, new sheet on the bed); no dissolves or wipes.

## 9. Pitfalls of the medium

- Uniform width reads as pen → swell hatches, pinch contours between runs (`hatch({swell})`, `outline({run, pinch})`), keep wMin hair-fine.
- Overlaps without occlusion → pass occluders as `excl` (subtracted ring by ring; even-odd would cancel overlaps).
- Outline-only parts beside a hatched body → hatch along each part's axis, a dark at every joint.
- Burin along the cut hides the groove; big skew looks like poking → ≤ 15°. Regular swarf helix reads as a spring → vary winding, twist, light one edge.
- Reflections over grooves wash them out → copper light first. Roundels authored small freeze sub-pixel → author large, scale in. Leaders hugging the subject read as crossing it → clearance.
- A long early stroke never draws → the ink's early exit must look ahead by the longest stroke.
- A push-in cropping a fresh note breaks the reading rule → put consecutive details on one side.
- Scientific names: TTS may manage, ASR won't → give the checker a plain spelling.

