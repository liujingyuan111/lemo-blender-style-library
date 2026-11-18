# 黑板粉笔 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/chalkboard/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`7f89f1a4694805e6bc767050007a6b44f2b7ab2474b0e3244032d3a0269b3e1c`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

- **A clean, freshly wiped board.** One even deep ink green with its own fine grain and very slow mottling. No history on the slate: no old swirls, no ghost lessons, no floating dust, no bokeh.
- **Writing that grows like a hand writes.** Strokes appear along their centre line in the correct stroke order, with pressure: pressed starts and corners, points that lift, 捺 feet that spread, hooks flicked off.
- **Three chalks at most.** White for structure, one accent chalk for the single part the lesson tracks, one pale chalk for a second hand (a pupil, a visitor).
- **A real object in a real room.** Wooden frame, a tray with sticks of chalk, painted tian-zi grids, sliding panels, a wall and a clock around it.
- **Few words, large letters.** The board holds keywords; the explanation is spoken.

Not Whiteboard Explainer: that style is a bright glossy board, coloured markers, floating marker props and magnets, ghost marks of old lessons, and a camera travelling across a knowledge map of many regions to explain how something works. Chalkboard is a dark matte slate with nothing floating in front of it, kept clean, one question per board, the camera facing it flat; it advances by writing a claim, wiping it and rewriting in place, and it lives in a classroom (panels that slide, grids painted on, a tray, a wall). Not a slide either: nothing is typeset, nothing fades in.

## 2. Materials & rendering

- Canvas 2D for everything visible; WebGL2 only for the post pass (camera motion blur, a light vignette, grade, dither).
- Each stroke is baked once into a board-space coverage sprite (coverage, arc length, lateral position). A partial stroke reveals pixels up to the current arc length with a round leading edge; the board's grain decides which grains take the chalk (deposit with a 2×2 supersample and a faint powder halo).
- Chalk edges are firm; loose powder only at the lift-off of a stroke (two to five grains). Never sugar the board.
- Writing strokes carry a width profile per stroke type (start bump, corner bumps, taper for 撇 / 提, foot for 捺, quick lift for hooks) and a pressure profile (heavier at both ends, lighter in the middle). Straight strokes bow slightly; horizontals rise 2–3° to the right; 横, 竖 and 折 enter with a short pressed tick from the upper left.
- Board, panels, frame, tray, clock and wall are baked once in world units; the slate grain is a periodic tile drawn in world space (soft-light) only when the camera is close.
- Erasing is a blurred destination-out band along one smooth path on a layer that holds only the strokes being wiped; it leaves a very thin, even haze. One wipe per film is plenty.
- A wet streak (a board just wiped with a damp cloth) is a soft mask with a wide blur at its drying edge, fading at top and bottom, that darkens the slate slightly; never a hard rim.
- Light: a gentle multiply falloff away from the windows and at most a faint warm window patch. Light never draws shapes across the writing in close shots.

## 3. Colour logic

- Ground: deep ink green slate, wood frame, warm white wall and a coloured dado if the room is seen.
- White chalk carries every structure: characters, lines, labels, arrows.
- The accent chalk (example: orange) is reserved for the one component the lesson tracks; it never decorates and never draws arrows or underlines that are not that component.
- A pale second chalk (example: yellow) marks another person's handwriting.
- No rainbow, no gradients in chalk, no glow. Painted grids are dull and thin so the chalk always wins.

## 4. Type & subtitles

- Chinese is hand-authored stroke data (centre lines + stroke type per stroke) drawn by the chalk engine, never a font's outline. Every character the topic needs is added to the data and checked against an OFL kai font behind it before shooting (how: §10, *New characters*).
- English on the board is a single-line OFL handwriting font (EMS family) drawn by the same engine; symbols missing from the font (arrows, plus) are drawn as strokes.
- On the board: keywords only, one line of Chinese, the next line English, a size smaller.
- Sizes at 1080p: big characters 300–450 px; labels ≥ 55 px CJK and ≥ 30 px Latin cap height; small writing gets heavier chalk so no stroke is thinner than 3 px.
- Reading time: every block stays fully in frame ≥ CJK ÷ 4.5 + other ÷ 15 + 1.5 s, counted from the frame it is wholly visible (readcheck). A block is fully written before it is read.

### Voice and subtitles

- When the style tells a story it is narrated: one calm teacher's voice in short spoken sentences, said as the matching chalk appears; what the voice names is being written or shown at that moment.
- A quiet subtitle plate sits above the bottom safe area: the spoken line in Chinese and a free English translation, one line each, a plain kai face (an OFL subset) on a soft dark plate, in and out with the voice. Long lines are split at sentence ends into several cues.
- Nothing the viewer must read on the board sits behind the plate; frames held for the board's words are composed above it.
- Pauses between voice lines are short (0.25–0.4 s); one longer hold (about 1.5 s) is kept for the verdict. Board action (a panel sliding, a wipe) runs under the voice instead of waiting for it.

## 6. Camera grammar

The camera always faces the board flat on (no perspective tilt).

| Move | What it expresses | Can serve |
|---|---|---|
| Close shot on the writing | attention on how a character or line is built | a component; a step of a proof; a spelling |
| Slow lateral pan along a line | time or sequence | a timeline; a derivation; a list of cases |
| Pull back to a fixed medium frame | the whole question at once | a comparison; a claim and its counter-claim |
| Same frame later | judgement | a correction; a before / after |
| Locked frame while a panel slides | a page turned in the room's own way | a new chapter; a hidden board |
| Whip with motion blur (≤ 0.5 s) | a jump to another part of the wall | a change of board |
| Cut on a line crossing a seam | a connection | cause and effect; the same part in two places |
| Wide shot of the whole wall | summary | the map of what was learnt |

The room is part of the style: at least once the frame opens wide enough to read board, frame, tray and wall as a classroom (where, and what else the room holds, is the film's choice). Close shots may show only slate and frame.

Rules: the subject is never smaller than a third of the frame in close shots; text blocks are never cut by the frame edge while they are read; no empty board for more than half a second. Transitions are hard cuts, a sliding panel or a line across a seam; no dissolves or page flips.

## 9. Pitfalls of the medium

- Dirty boards (old swirls, ghosts, floating dust) read as "messy", not "real". Keep the slate clean and let the grain carry the realism.
- Equal-width polylines look like a plotter and make characters misread. Use stroke-type width and pressure profiles.
- Character data that is structurally wrong is caught at once by native readers: check every character against a reference before shooting.
- Small writing at 1080p disappears with the same chalk width as large writing; give small text heavier chalk.
- Text written while the camera moves away fails reading time; hold the frame or keep the block in view.
- Accent colour spread over arrows and decorations stops meaning anything.
- A soft halo at the chalk's front reads as glow. The demo's `drawFront` (`props.js`) puts a faint radial gradient under its grains: in your copy, drop the gradient and keep the grains.
- A wet streak with a hard edge looks like a cut-out.
- Board-speak in the voice ("A plus B", component names with no meaning) is not understood: every component is said with what it means the first time it appears.

