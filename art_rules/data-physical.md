# 数据实物化 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/data-physical/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`18c3c76d1ddb3d8616c7cd571433853885e8bd65146ab0b4ee2222e4475c6116`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

- **The unit is an object.** One plate, block or coin equals one stated quantity, and the rule is said on screen once ("1 plate = 10 GW"). A heavier material marks every tenth unit, so the stack is its own ruler.
- **Scale is exact.** Heights, counts and areas are computed from the data; rounding is one unit at most and written in the facts. Two series compared on the same base use the same unit.
- **Studio light, real matter.** Metal reflects an HDRI, wood shows grain, acrylic transmits; nothing glows, nothing is outlined, no fake UI.
- **Growth is assembly.** Data increases by pieces being placed, one after another, with weight and sound; it never scales or morphs.
- **The pull-back.** At least once the chart is revealed as a made thing: a dial, a table piece, a landscape of stacks.
- **Every number has a source on screen**: real published statistics (or the user's own figures), credited in frame.

Not Isometric Infographic (no icons, no flat colour coding), not Glass Product Render (the object is data), not Data Storytelling (no paper chart or inked axes), not Dark Tech Keynote (no black stage or neon), not Brick Toy (no toy proportions, no characters).

## 2. Materials & rendering

- **Pieces**: thin boxes or cylinders instanced in the thousands, each with a few-millimetre random offset and yaw, a ±7 % value change and a hairline gap: that is what makes a stack read as stacked, not as a bar.
- **Material per series**, chosen so two series separate in one glance at thumbnail size: brushed metal against tinted acrylic, pale wood against dark stone, copper coins against paper. A third material (e.g. brass) only for the ruler pieces, shared by every series.
- **Base**: a real-texture slab (wood veneer, stone) with inlaid marks: a tick ring, the series' paths, the labels of categories or years, cut into the surface at the base's own scale, lit with the scene.
- **Rendering**: PBR (transmission for acrylic), an HDRI at low intensity for reflections only, a warm key at 20–35° with long soft shadows, one or two cool rims so metal and acrylic separate from wood at distance; GTAO, physical depth of field, 2× supersampling, a light vignette.
- **Screen space only for type**: readings, verdicts, the source line, subtitles, the title card. Every reading is pinned to its object through the same world → screen function as the camera.
- **Post**: grain light (the background is pale), no lens flares, no chromatic aberration.

## 3. Colour logic

- The set is warm and neutral: a seamless greige sweep, the base in a natural material, the series in material colours (silver, pale teal, brass, oak). Material, not paint, separates series.
- **One accent** (e.g. signal orange) for the reading or verdict that matters on this screen; nothing else is accent-coloured.
- Ink is near-black at two strengths (value, then labels at ~60 %).
- No rainbow series palettes, no colour ramps on the objects, no dark mode.

Example (our demo): sweep #C4BEB4, walnut base, aluminium #C8CCD1 (metal), acrylic #9FD3D6 with teal attenuation, brass #D2B07A, ink #1C1D20, accent #D4521C.

## 4. Type & subtitles

- **Roles**: a light grotesk for numbers (e.g. Inter 200–300; the hero reading 130–170 px, a stack reading 46–56 px); a sans for labels and verdicts in the film's language (e.g. Noto Sans SC 500, 24–46 px); a monospace for units, years and source lines (20–24 px); a serif only for the title. OFL, self-hosted, CJK subset.
- **A reading** = a dot on the object, a 1.4 px leader, a small swatch of the series' material, the category line, then the value and unit, on a translucent paper plate (~84 %). Two readings of one pair stack in one column, larger value on top.
- **The source line** (dataset, publisher, year, licence, e.g. "数据：IRENA (2026)，经 Our World in Data 整理 · CC BY 4.0") is in frame with the data, small (20–22 px, ink at ~60 %) in a corner away from the subtitles, at least from the first reading to the summary, and on the title card.
- **A verdict** sits in the upper-left third on its own plate in the accent colour, underlined by a growing rule; it appears only after the readings it judges have been still for ≥ 2.5 s.
- **Subtitles**: bottom-left, a 2 px ink rule and a paper plate fading right; if the film is bilingual, the film's language on top; each line one line only, measured with the real font (`nowrap`), split into two cues rather than wrapped. Hold ≥ max(1.8 s, speech + 0.6 s).
- Labels hold ≥ CJK characters ÷ 4.5 + 1.5 s / letters ÷ 15 + 1.5 s; a counter reports its landing value; nothing below 20 px.

## 6. Camera grammar

| Move | What it expresses | Can serve |
|---|---|---|
| Macro dolly along a stack's edge, rack focus | the unit is real and countable | the rule "1 piece = X"; a single record |
| Low lateral track along the series | time passing; growth | a decade; a ranking; a sequence of sites |
| Locked three-quarter frame on two subjects | comparison | before/after; A against B; a crossover |
| Crane with the rising top | accumulation | one year's increase; a target being reached |
| Pull-back to near top view | the whole as an object | a summary; a ratio; an ending |
| Slow orbit around the base | the installation as sculpture | a title; a breath |

The subject fills at least a third of the frame height at key moments; readings live in empty background, never over the subtitle strip; comparisons keep both subjects completely in frame. Transitions are camera moves inside one set (one continuous take where possible); no cuts to a chart, no wipes, no page turns.

## 9. Pitfalls of the medium

- Two materials too alike (bright aluminium vs clear acrylic) read as one series: give one a tint or a finish change, and check at thumbnail size.
- Long shadows and warm reflections turn metal brown at distance: add a cool rim light and keep the base darker than the pieces.
- Thin pieces moiré at 2–3 px per layer: random per-piece value and offset, 2× supersampling.
- A reading pinned to a moving object can leave the frame: clamp it to a safe box.
- Counters that roll by time instead of by landed pieces lie; tie them to the object count.
- Rounding to whole pieces can invert close values; when two values are within one unit, say so on screen or choose a finer unit.
- Transmission streaks at low angles: acrylic roughness ≥ 0.2, tinted attenuation.

