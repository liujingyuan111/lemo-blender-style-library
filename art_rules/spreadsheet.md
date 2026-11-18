# 表格动画 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/spreadsheet/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`63b4c656fe1c63e38ac769ace40d7bf4a35313285e5f426003faf64b35f73f77`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

What makes a frame read as this style in one glance:

1. **Cells are the pixels, and they are wide.** A cell at 100 % is about 2.9 : 1 (the demo uses 64 × 22 px). Every diagonal and curve becomes horizontal stair-steps.
2. **The picture is computed.** Every painted cell holds a small, faint value (1/0, a code letter, a colour-scale step) and the value chooses its fill. Close up it is a data table; far away it is an image.
3. **The software shell never leaves the frame**: title bar, toolbar, name box, formula bar, column letters, row numbers, sheet tabs, status bar. The shell never zooms; only the sheet does.
4. **The formula bar is the dialogue.** A beat starts with a formula typed letter by letter; Enter drops the result into a cell and the sheet reacts.
5. **One hero: the selected cell**: thick ink border, marching ants, a fill handle. It hops cell by cell and leads the eye.

Not a data-storytelling chart on paper (there is no paper, no pencil: the sheet is the medium), not a dashboard (one idea per beat, no widgets), not a screencast of real software (the shell is generic and drawn, every action is staged), not pixel art (cells are wide, carry values and sit in a live grid).

## 2. Materials & rendering

- **Canvas 2D, one world → screen function.** The sheet is a grid in world units (column widths × row height); the camera is a centre and a zoom. Everything that belongs to the sheet (fills, values, merged cells, reference boxes, the selection) goes through that function; the shell is drawn in screen space on top.
- **Variable column widths** are part of the model: a hidden column has width 0 and every x position is a prefix sum of widths, so opening or closing columns reflows the whole sheet and the camera rides along.
- **Grid lines**: white cells get light grey lines (≈ `#dad9d3`); painted cells get thin dark lines (≈ rgba(6,4,18,0.42)), as if "all borders" were applied.
- **Cell values** at 11 px × zoom; below about 6.5 px they are not drawn, so the far view becomes pure colour instead of grey noise.
- **A painted cell flashes white** for ~0.12 s when its rule fires. That flash is the style's only "light".
- **Merged cells are the layout**: labels, results, titles and the end card are merged ranges with a cell border, never floating text.
- Nothing outside what a sheet can make: no gradients, glows, shadows, blur, depth of field or translucent panels. Text has no outline or drop shadow.
- **The sheet cannot scroll above row 1 or left of column A**: clamp the camera, and compose around that edge.

## 3. Colour logic

- **The sheet is white; colour means a rule fired.** Every fill on a cell is a conditional format with a meaning the viewer can learn in one look (success / failure, a category, a scale step).
- **At most five working hues** plus the shell's warm greys: two for the main binary or categories, one for a second variable, one for the hero (the selected cell, a winning result), and ink. Office-style conditional-format colours (lime, red, indigo, amber, sky) read as "spreadsheet" at once.
- **A colour scale is a payoff, not wallpaper.** A banded scale (6–8 steps radiating from one cell, neighbouring bands alternating light and dark) can paint the empty background once the argument is made; until then the background stays white.
- Reference boxes take their colour from the formula: each referenced name in the formula bar and the box around its range share one hue.
- Example palette (the demo): lime `#b8f25a`, red `#e8382d`, indigo `#2a2f6c`, amber `#ffb21f`, ink `#17120a`, shell `#dcdbd5` / `#f1f0eb`.

## 4. Type & subtitles

- **One grotesque for the whole interface** (Inter, OFL) and a matching CJK sans (Noto Sans SC, OFL), self-hosted as subsets.
- Roles: cell values 11 px × zoom (texture), merged-cell labels 14–26 px × zoom, results 26–32 px × zoom (they pop 30 % on Enter), formula bar 26 px fixed (the line of the film), shell 12–13 px fixed. On-screen Chinese ≥ 34 px at the zoom it is read at.
- **Subtitles are a cell comment**: a pale yellow note with an ink border and a red corner triangle, docked at the lower left, one Chinese line over one English line, never wrapped. Frame the subject above it (the camera's centre sits about 48 px above the viewport's centre).
- Formulas use the real syntax of a spreadsheet (`=AVERAGE(range)`, `=COUNTIF(range, "L")`), names for ranges, and colour the referenced names.
- Hold every subtitle ≥ max(1.8 s, speech + 0.6 s); a result that a sentence depends on stays in frame until the sentence has used it.

## 6. Camera grammar

The camera is the sheet's zoom and scroll. The column header grows a little with zoom (26 → ~38 px), as real software does.

| Move | What it expresses | Can serve |
|---|---|---|
| Pull out from one cell | the part becomes the whole; data becomes a picture | a reveal of scale; "each cell is one…"; a summary |
| Push into a cell or range | this one number matters | a verdict; a definition; an outlier |
| Follow the selected cell | the eye is led step by step | a calculation path; a comparison A → B; a list |
| Whip to the headers | look at the structure, not the data | a clue (hidden columns, a sort, a filter) |
| Track along a row or column | reading a series | a timeline; a ranking; a sequence of groups |
| Follow cells that move | the data reorganises | a sort; a pivot; a filter; a merge |
| Locked wide frame | let the viewer compare | a paradox; before/after; any judgement |

Framing: a judged comparison is wholly in frame and held ≥ 2.5 s; at key moments the subject fills ≥ 1/3 of the viewport height; keep key text above the subtitle note. Transitions are made by the sheet (a hop, a zoom, a column opening, cells flying, a colour scale spreading, a merged cell expanding); no cross-fades, wipes or page turns.

## 9. Pitfalls of the medium

- **Grey mush when zoomed out**: values drawn at 3–5 px turn the picture to noise. Stop drawing values below ~6.5 px.
- **Text unreadable at the zoom it is shown**: size merged-cell text for the zoom of its shot; a number the voice uses must be ≥ 26 px on screen.
- **Wide-and-short compositions**: a sheet that is wider than tall forces a low zoom; add a meaningful row of cells (a count, a total) below, or crop to the part being discussed.
- **Selection box drawn over the value**: a thick border on a small cell hides its content; select merged ranges for results, single cells only when zoomed in.
- **Brand look-alike**: a green ribbon, a familiar grid font, a product name; keep the shell generic and drawn by hand.
- **Moving cells smearing**: interpolated sub-cell positions read as sliding stickers; snap to whole cells.
- **Too many formulas**: one formula per beat; a formula bar that changes every second is noise.

