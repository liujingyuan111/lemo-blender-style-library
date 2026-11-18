# 马克笔白纸速写 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/marker-paper/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`26b384c99eeef6a9f119afeea237dc0916782f6b959f525d099c6891ebfe0458`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

- **The frame is the sheet.** A warm matte white paper fills the screen; no desk, no pad edge, no props, no hand, no pen.
- **One bullet-tip marker line.** Thick (6–10 px at full frame), near-constant width, a slightly denser touch-down, a slight lift at the end, corners overshot because each side is a separate stroke.
- **Three inks with fixed meanings.** Black builds everything; blue marks the givens; red marks the unknown and, later, the answer. Red is always the last stroke on a sheet.
- **One question per sheet**, written top-left in hand lettering as it is asked, the page number circled top-right.
- **Ink behaves like ink.** Same-colour crossings, corners and arrowheads over shafts are visibly darker; a stroke never darkens itself; nothing bleeds outside a stroke.

Not Whiteboard Explainer: that is a glossy board with ghost marks, floating markers and magnets, and a camera travelling over one big knowledge map. Not Chalkboard: dark slate, chalk grain, wipe-and-rewrite. Not a sketchnote: no dot grid, no fineliner, no grey or yellow marker fills, no page-wide poster to pull back to. Here: white matte paper, one thick marker, red/blue semantics, one sheet per step, changed by a push through a drawn shape or a peel.

## 2. Materials & rendering

- Canvas 2D. Each stroke is a filled ribbon (bullet nib, width ≈ constant, ±3 % noise, a 0.86→1 ramp over the first 3 widths, a 10 % lift over the last 2) built from a resampled, Chaikin-smoothed polyline with a slow arm wobble and a little finger tremor along the normal.
- **Drawn up to a length**: a stroke in progress is cut at its head with a round cap; a letter in progress is revealed by a fat mask along its glyph's centre line (stroke order from a thinned skeleton), so letters keep the real font's outlines.
- **Ink density, not alpha**: every stroke or letter adds one unit to its colour's density layer (`lighter`). Compose per pixel by transmittance: one unit = the palette colour at its opacity; n units = that transmittance to the power 1 + 0.6 (n − 1). Touch-down and sharp corners (found on the un-wobbled path, so they never flicker) add 0.3 of a unit inside the stroke.
- **Paper**: warm white, sub-2-level grain, faint cloudy formation, a few hundred 1-px fibres, one lamp's falloff of about 3 levels from top-left. Baked once per sheet, drawn through the camera.
- The camera moves over the paper by drawing strokes and letters *through* the camera transform: pushed in, lines get thicker and stay crisp, like a lens closer to the sheet. Never scale a rendered bitmap.
- No vignette, no film grain, no scan dirt, no glow, no drop shadows. The only shadow in the style is the peel's (≤ 0.16 opacity, narrow).

## 3. Colour logic

- Ground: warm white paper. Ink: black for structure (≈ 90 % of the ink on any sheet).
- **Blue = given, red = wanted.** The meaning is fixed for the whole film: the same quantity keeps its colour in the drawing and in the algebra. Where the topic has a hot/cold axis, red/blue may also carry it, in the same direction.
- Each sheet: blue and red each ≤ 10 % of the ink; one red focus per sheet (it may be a group: arrow + label + circle).
- Red never decorates and never draws structure. Grey, yellow and fills do not exist; a red bar is a thick red stroke.
- Example palette: paper `#FAF9F5`, black `#1B1C20` (opacity .97), red `#E23B2E` (.9), blue `#2456D6` (.9), peel shade `#463F33` ≤ .16.

## 4. Type & subtitles

- Latin: Kalam (OFL) — Bold for questions, labels, answers; Regular for small notes. Chinese: LXGW Marker Gothic 霞鹜漫黑 (OFL), one short line under an English question.
- Sizes at full frame: question 92–112 px; answer 100–120 px; labels 40–60 px; notes 30–40 px; Chinese on the sheet ≥ 34 px. Each glyph gets a fixed tiny tilt, baseline and size drift (±1.3°, ±1.7 %, ±2 %); no stroke, outline, shadow or double print.
- Letters are written, not faded: questions ≈ 12 characters/s, labels 8–10/s. Written letters never boil.
- Algebra is written in the drawing's colours, piece by piece (`v = d ÷ t`): the colour tells the viewer which line in the picture each term is.
- **Subtitles** sit on a torn slip of the same paper laid over the bottom of the frame (straight top and bottom, torn ends, 96 % opaque, 1-px hairline, no shadow): Chinese 38 px over English 31 px at 78 % ink, one line each, never wrapped. The slip is screen space and does not move with the camera. Keep sheet content above y ≈ 940 while a slip is up. Hold ≥ max(1.8 s, speech + 0.6 s).

## 6. Camera grammar

Top-down on the paper; the camera only moves over the sheet. Never tilt, never show past the paper's edge, never show a desk.

| Move | What it expresses | Can serve |
|---|---|---|
| follow the pen | the line being made is the subject | a long arc; a row of algebra; a timeline being drawn |
| lean in (≤ 2×) | this is the part that matters | the red answer; a given being labelled; a final rule |
| pull back | the whole picture, or a comparison read at once | a scale reveal; a summary sheet; holding a verdict |
| push through a drawn shape | "look closer" as a transition | a right angle; a small circle on a map; a decimal point |
| peel | a new question | the turn of an argument; a new case |

- Framing rules: a text is either wholly in frame or wholly out, never cut; when leaning in, choose a zoom that pushes the title out completely or keeps it whole. Comparisons are fully in frame and held ≥ 2.5 s.
- Transitions are only the push-through match cut and the peel. No fades, no wipes, no slides, no page-flip graphics.

## 9. Pitfalls of the medium

- **Flicker in letters.** Never re-randomise letters per frame; lay them out once, fixed seeds, no boil.
- **Dirty paper.** Shadows under text, vignettes and scan grime read as "unclean". Only the peel casts a shadow.
- **Red everywhere.** Two red foci on one sheet kill the semantics; demote one to black.
- **Text cut by the frame edge** when leaning in: pick the zoom from the text boxes (wholly in or wholly out).
- **Corners that pop.** Detect corner ink on the un-wobbled path; otherwise the boil switches pools on and off.
- **Zooming a bitmap.** Strokes must be redrawn through the camera, or a push-in looks blurred.
- **Algebra on a slide.** Centred, typeset, faded-in equations break the hand; write them left to right in the drawing's colours.
- **A page of everything.** One question per sheet; a new step is a new sheet.

