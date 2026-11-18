# 平板速写讲解 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/ipad-sketch/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`4a0e371e38f3660227e48886f3479ae060a310186a9ae2a35b8263da028c5d0f`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

- **One canvas.** Every frame is a region of one page. The page fills up as the film goes and is seen whole at least once; nothing exists off the page (no device bezel, no app toolbar, no hand).
- **Line first, colour second.** Objects are drawn in graphite (white inside), then coloured as a separate pass. Colour sits *under* the pencil and is visibly shifted off it (offset 5–12 canvas units, down-right), with a ragged edge.
- **Still drawing.** Some evidence that the drawing is in progress always stays: light construction lines left in, a block coloured half way, one object with its line only.
- **The canvas moves, the marks don't.** Finished lines never boil or jitter; the camera is two fingers on the glass (pan, pinch, rotate a few degrees).
- **A stylus, no hand.** The only real object in the frame is a clean stylus that rides the mark being made and lifts between marks.

Not the sketchnote (dotted paper, ink fineliner that boils, grey marker + one yellow, a pen you never see). Not a whiteboard explainer (white board, black marker, hand). Not urban sketch pen-and-wash (watercolour washes that bleed). Not a vector flat explainer (no pencil grain, no off-register).

## 2. Materials & rendering

- **Paper:** cream canvas with a fixed paper grain (fine value noise plus a slow mottle), anchored to the canvas so it pans, zooms and turns with it. A light screen-space corner falloff only.
- **Pencil:** a stamped-dot brush along a Catmull-Rom spline, one stamp every ~0.5 canvas units; pressure = taper in and out × slow noise, driving both width and density; a small low-frequency wobble along the normal. Within one stroke take the max coverage (no self-darkening).
- **Grain threshold:** at composite, pencil opacity = clamp((coverage · 0.9 − grain · 0.85 + 0.32) · 2.1). Light pressure is eaten by the paper tooth: broken, grainy edges. Lettering goes through the same threshold, so words look pencilled too.
- **Colour blocks:** the object outline, translated off the line and displaced along its normal by noise (ragged edge), filled flat and blended *multiply* under the pencil. Highlights, seams and inner layers are holes cut out of the block (the paper shows through). Objects in front cut the blocks behind them.
- **Colouring path:** a block is revealed along a back-and-forth (boustrophedon) path across its shape, so a half-coloured block ends in visible strokes. A block can stop at any fraction.
- **Re-registering:** to change an object's colour, erase what the new block covers (slightly wider, so no old fringe peeks out) and colour again; the line stays.
- **Layers, in order:** paper → colour blocks → light construction pencil (≈55% opacity) → graphite → coral accent pencil.
- Draw the canvas into buffers at ≥ 2× its unit size so a 2.5× push-in still shows clean grain; the camera scales the buffer, the grain is never generated in screen space.

## 3. Colour logic

- Neutral ground: a warm cream paper; graphite (warm dark brown-grey, never pure black) for every line and word.
- **System colours (every film):** a light graphite for construction lines, one coral for the "explaining" marks (arrows, underlines, burst ticks, the one number that matters), one mustard for the highlight block under the key word of a title.
- **Subject colours (per film):** soft, warm, chalky versions of the subject's real colours; each gets a darker variant of the same hue for a second, smaller shadow block (≈40% multiply). Four to eight subject hues in a film.
- Colour is information: when a thing changes (ripens, dries, cooks, ages) change its block, not its line. A swatch strip that records each state is the style's way to chart.
- Example: paper #F3EADB, graphite #43362E, light #A8998A, coral #DC6A4C, mustard #F1C04F.

## 4. Type & subtitles

- **Lettering on the page** is handwriting written stroke by stroke along each glyph's skeleton, then put through the pencil threshold. A casual marker-hand Latin (e.g. Caveat Bold for titles, Medium for notes) and a pen-hand Chinese (e.g. Long Cang) for one short line; all OFL.
- Roles: a title (≈100 canvas px) with a mustard block under one word and a coral underline; chapter capsules (circled number + word on an offset block) when a film has chapters; notes 32–50 px with a short pencil leader to what they name. Chinese on the page ≥ 34 px on screen.
- Notes are placed in the empty space next to their object, never centred stacks, never a header bar.
- **Subtitles** live outside the canvas, as a small paper chip: a light cream rounded strip over a darker paper block offset down-right (the colour-block grammar), Chinese on top in a readable text face (e.g. LXGW WenKai, 40 px), English below in the handwriting face (40 px), left aligned, one line each. The chip wipes in left to right like a colour block (≈0.2 s), the words fade in after; bottom left by default, bottom right when the subject sits there. Hold ≥ max(1.8 s, speech + 0.6 s).

## 6. Camera grammar

The camera is the canvas under two fingers. Every move is a gesture: quick start, settles with momentum (≈0.7–0.9 s); between gestures the canvas drifts very slowly; it usually sits 1–4° off level and comes back to 0° for the whole page.

| Move | What it expresses | Can serve |
|---|---|---|
| Extreme push on a line (2.5×) | the material: grain, pressure, a line being made | a hook; a detail that needs attention; the first stroke |
| Pinch out | "now see what it was" | a reveal; changing scale; closing a section |
| Two-finger turn | the artist settling into the next drawing | a new section; a long curve being drawn |
| Pan / tilt along the page | moving to the next idea on the same sheet | a sequence; a journey; cause → effect |
| Follow the stylus | being led | a branch, a road, a timeline drawn in one stroke |
| Match cut between a small and a magnified copy of a drawing | zooming in without leaving the page | a close look at a process; data inside an object |
| Punch-in (≈0.15 s) and settle | an event | a crack, a click, a threshold |
| Whole page | the answer | an ending; a summary; a map of everything said |

Framing: the subject fills ≥ 1/3 of the frame height at key moments; leave the bottom 160 px for subtitles. Transitions are made from the medium (a gesture, a colour flood, a match cut); no fades, no wipes, no hard cuts except a match cut.

## 9. Pitfalls of the medium

- **Boiling lines** turn it into a sketchnote: keep finished marks still.
- **Colour on top of the line** looks like a sticker: composite colour under the pencil, always multiply.
- **Perfect fills** look vector: keep the offset, the ragged edge and an occasional unfinished block.
- **Grain in screen space** crawls during camera moves: generate it in canvas space, at the buffer resolution, and let the camera scale it.
- **Stylus parked over the subject or a note:** park it in empty paper, or take it off frame.
- **Too many objects on one page:** a page for a 50 s film holds about six drawings and a dozen short notes; plan the whole page before drawing the first line, and leave the final title's space empty until the end.
- **A drawing that is too small to read when the page is whole:** size objects for the final pull-back, then push in for detail.
- **Thin flat transitions** (a fade between areas of the same page) break the canvas illusion: move the canvas instead.

