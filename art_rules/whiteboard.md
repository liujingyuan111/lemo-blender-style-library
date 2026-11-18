# 白板讲解 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/whiteboard/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`19f66326257bcafb8aca18af3e209d1fee31d9e23902ce1708bbb606cbf4b718`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

- **One physical whiteboard.** Everything the viewer learns is drawn in dry-erase marker in front of them, in real handwriting order.
- **The board is a map**: each idea lives in its own region; the camera travels between regions, often led by the pen. Distance on the board = distance in the argument.
- **Real marker, not animated text**: ink pools where the nib lands, dry streaks and speckle, strokes overshoot and don't quite close, ghosts of old lessons remain, a glossy sheen drifts slower than the board, and **every stroke makes a sound**.
- **No hands.** Markers float with a real cast shadow that grows when they lift, park outside the frame between phrases and fly back in. Magnets and the eraser move on their own. Never draw a hand, an arm or a cursor.

Not Blueprint (no blue sheet, no drafting conventions), not Crayon Picture Book (no wax texture, no children's story), not a kinetic-type explainer (text is handwritten stroke by stroke, never animated as blocks).

## 2. Materials & rendering

- **Board**: a warm white gradient, a faint scuff and micro-scratch tile, a few dozen **ghost marks** (old words, circles, arrows) at 5–10 % in grey or pale blue, and a soft diagonal **window sheen** (white, 10–16 %) moving at ~0.35× the camera: this one detail sells "glossy".
- **Ink**: alpha ~0.94, composited with **multiply** so overlaps darken like real marker. Width 6–11 px for drawing, ~13 % of cap height for lettering.
- **Stroke character**: resampled every ~0.6 × width; low-frequency hand wobble along the normal (a few px, long wavelength) plus a finer tremor; chisel-tip width modulated by direction; a pressure ramp at the start and a small taper at the end; circles start at an angle and **overlap past closure**; rectangles are four strokes with small corner overshoot; a darker pooled dot *inside* the start of long strokes.
- **Dry-marker texture**: a speckle-and-streak tile subtracted from the ink layer (destination-out), locked to board space, faded out when the camera is wide.
- **Lettering**: a single-line (single-stroke) font written in stroke order, each glyph with small rotation, baseline and scale jitter. Missing symbols (μ ≈ → × − ✓ ² ° ±) are hand-defined.
- **Props**: dry-erase markers (white barrel, colour band and cap in the ink colour, felt nib), a felt eraser, magnets (glossy, with specular highlight and soft cast shadow). Frame, tray and wall appear only if the camera ever goes past the board edge.

## 3. Colour logic

- **Three marker colours at most**, each with a meaning held for the whole film: one dark ink for things and structure, one for signals / measurement / process, one accent for the thing that matters (one accent per region).
- **Monochrome variant**: everything in the dark ink, one element in the accent (the "only colour").
- Ghost marks and board stay neutral; the accent never appears on props except its own marker cap and the hero magnet.
- Example sets: black `#23262c` / blue `#2a5cb3` / orange `#d97757`; black / green `#2e8b57` / red `#c8363a`; navy `#1f2a44` / teal `#1f8a8a` / purple `#7a4fb3`.

## 4. Type & subtitles

- **Handwriting only**: a single-line hand (e.g. EMS Tech, OFL) for all board text; titles large (~120–200 px cap height), labels 30–70 px.
- **Title and end card are written on the board** in the same hand.
- **Burned subtitles**: an off-white rounded label (~90 %), a handwriting-like face (e.g. Architects Daughter ~44 px), dark text, a short accent-colour marker dash. Split at clauses, ≤ 44 characters per line, bottom ~12 % of the frame kept free for them in every shot. Hold ≥ max(1.8 s, speech + 0.6 s).
- **Writing finishes on the word**: a term appears exactly when the narrator says it.
- A label is fully in or fully out of every shot it appears in.

## 6. Camera grammar

A 2D camera over a large board (e.g. 8000 × 4500): position, zoom interpolated in 1/z so pushes feel like dollies, a little roll. A vocabulary, not a route. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Pull back from a tiny drawing | scale | a surprising size; context |
| Ride the line the pen is drawing | one idea leads to the next | a transition; a process; a path |
| Hold still | read now | an equation; a definition; a list |
| Whip to a new region | a new idea after a pause | a twist; a "but" |
| Return to an earlier region | a callback, for free | reusing a result; a comparison |
| Split view of two regions (zoomed out enough for both) | two things at once | a duet; before/after |
| Slow push into one symbol | this term is the point | a unit; a variable; a name |
| Track along a long diagram | sequence, time | a timeline; a pipeline; a journey |
| Pull back past the board edge to the wall | the whole lesson as one picture | a summary; a scale jump |

Motion blur: when the camera moves more than ~14 px per frame, render and average sub-frames (≤ 4 px apart). No cuts on the board; if a cut is needed, it is a whip.

## 9. Pitfalls of the medium

- **One pen, too many jobs** drifts later and later → give each drawing a deadline window and let overlapping jobs go to another pen.
- **Minimum stroke duration × many dashes** makes a dashed line take seconds → dashes need their own floor.
- **A pooled-ink dot bigger than the stroke start** leaves halos on every letter → keep it inside.
- **Punctuation vanishes** (a font period is a 1 px stroke) → render sub-width strokes as dots.
- **Labels half-cut by a push-in** look sloppy.
- **Motion blur with few sub-frames** strobes text.
- **Eraser paths** crossing labels you want to keep.
- **Voice and phoneme set mismatch** (a British voice with US phonemes) mispronounces → match the language code to the voice; ASR-check.

