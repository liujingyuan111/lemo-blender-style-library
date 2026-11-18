# 瑞士动态排版 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/swiss-motion/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`14ddeb6dc495e691a220497069a2ee4827d820f9ee7a3173de5846489ef41f57`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

- **Pure 2D graphic design animated on a grid**: flat paper, black type and bars, a very light grey and **one** saturated signal colour.
- **Every element snaps to the grid, every move lands on a beat, nothing bounces.**
- **Rigor with one exception**: the whole frame obeys a system, so the one element that doesn't becomes a character.
- **Extreme scale contrast**: a giant numeral next to tiny technical notes.

Not a keynote (no gradients, no glow, no device renders), not kinetic typography for a lyric video (words don't fly, spin or bounce), not data visualisation (bars have mass as graphic form, not as charted quantities, unless the grid gives them that meaning), not a Bauhaus pastiche of primary shapes.

## 2. Materials & rendering

- **Frame grid**: 1920×1080, 12 columns, ~96 px side margins, 24 px gutters, 24 px baseline. The frame can act as a **spread**: a left page (the programme: numeral, rule text, notes) and a right page (the artifact).
- **Artifact grid** derived from the content (Gerstner): what the columns and rows *mean* is a design decision. **Choose module sizes that give the elements mass**; too many thin columns make a layout look like a chart.
- **Surfaces**: page, paper, ink, signal colour, grid lines in two or three light greys (on page, while building, on paper). No gradients, no shadows, no particles, no grain (mux grain 0).
- **Bars and blocks** are flat rects; consecutive cells of one unit merge into one bar, overdrawn 1 px at seams (antialiasing shows hairlines, especially when rotated or scaled).
- **A secondary voice** can be light-grey elements under the black ones: depth without a second colour.
- **A 2D camera matrix** (centre, scale, rotation) for all moves.

## 3. Colour logic

- **Paper, ink, greys, and one signal colour.** Only one thing carries the signal colour; that makes it the protagonist. It is the only thing allowed to be inexact.
- Overprint is allowed: black type on the signal colour.
- The signal colour can be red, orange, ultramarine or green; choose it for the topic, then never add a second.
- Examples: `#EAE9E5` page, `#FFFFFF` paper, `#111111` ink, signal `#E30613`; or `#F2F0EA` / `#141414` / signal `#FF5A00`; or `#E9ECEF` / `#0B0B0B` / signal `#1F3FFF`.

## 4. Type & subtitles

- **One family for the whole film**, an OFL neo-grotesque (Archivo, Inter, Schibsted Grotesk, Instrument Sans…), several weights. Letter-spacing ~−2 % at ≥ 90 px. Headlines can be lowercase. Load every weight with `document.fonts.load` before drawing.
- **Flush left, ragged right**; everything on a grid line; big white space is part of the layout. Giant numerals are **optically** flush left (subtract the glyph's left bearing).
- **Subtitles are part of the layout**, not a bar at the bottom: each line sits at a column start in the current composition (a small grey lead-in + a large bold statement, or a caption like a museum label), each word clip-revealed on its whisper timestamp. Hold ≥ max(1.8 s, speech + 0.6 s); assert it in code.
- **Caption rows**: small (~19 px) medium-weight notes with a 1 px rule above; technical notes in a corner (module sizes, counts, a bar counter).

## 6. Camera grammar

A vocabulary, not a route. The camera moves only with the precise ease and only on beats. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Locked spread | cause (left) → effect (right) | a rule applied; a before/after; a comparison |
| Hard pan by one page or column | the next step in a system | a sequence; a catalogue; a timeline |
| Rotate 90° and stop | the same thing read another way | a poster as a score; a chart as a map |
| Pull out to a wall of artifacts | one programme, many outputs | a brand system; a product range; a series |
| Push into one module | detail; the unit of the system | a pixel; a letter; a single data point |
| Grid extends past the page | the system is bigger than the artifact | scale; ambition; a break from constraints |
| Split frame into equal cells | parallel cases | options; variants; team members |
| Vertical scroll through a column | reading; a list | a manifesto; a spec sheet; a timetable |

Framing: everything on the grid; the signal element may sit off-grid only when it is being the exception. Transitions are wipes, knife cuts, camera moves and re-flows; never dissolves.

## 9. Pitfalls of the medium

- Too many thin columns look like a chart → fewer, wider modules.
- A "better" composition that isn't obviously better → one strong diagonal with long/short rhythm, a larger signal element, bleeds, type over colour. Merely tilting is not enough.
- Rotating and labelling at once reads as noise → rotate, hold, then add labels.
- Merged bars show seams after rotation → overdraw 1 px.
- Elements that share the camera matrix leak into other shots → draw them only when on screen.
- Canvas `letterSpacing` affects `measureText` → measure after setting the font.
- Onsets that fall between frames flicker → put visual onsets on whole frames.
- Whisper splits or merges words and pads the first word → align by letters, clamp to 0.

