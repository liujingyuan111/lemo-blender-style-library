# 工程简报板 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/briefing-board/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`44669da808da4ed37e2a4a0f6e5d2b23008775a3c4870add04641d714e9f323d`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

1. **A physical board in a room**: enamel, window falloff, a sliding reflection, ghosts of earlier work, frame and tray.
2. **Real things on it**: cut-out photographs of the real objects, a few millimetres off the board, shadowed by one window, parallaxing. They are evidence: never a generated image presented as a real object.
3. **Ink that means something**: graphite for names and rules, blue for water and measurement, red only for the decision; rejected ideas erased to ghosts.
4. **One continuous wall**: no pages; the camera travels along lines, projections and leaders.
5. **The whole wall, once**: every shot is a crop of the final briefing, seen whole only in the last pull-back, as a poster.

Not **Whiteboard Explainer** (a hand drawing line art on a flat page): the board is a filmed object, subjects are photographs. Not **Data Storytelling**: comparisons are dimension lines in real units beside real objects. Not a keynote: no headers, centred bullets, page turns.

## 2. Materials & rendering

- **Board (z 0)**: procedural enamel, wiped ghost strokes, smudges, a window falloff, a sliding diagonal reflection; the frame shadows a warm grey wall.
- **Ink (multiply)**: flat colour at about 90 %, lighter core, round caps, a wet-tip glint on the stroke being drawn. Lettering: a marker font revealed glyph by glyph with seeded tilt and baseline jitter. Erasing leaves a blurred ghost (about 7 %).
- **Prints (z ≈ 6–14)**: photographs cut out at full resolution (a matting model, or a hand polygon / mask), clean edges, one shared grade (lower saturation, a touch warmer, lifted blacks). Thin structure (cables, wires, masts, railings) is measured in the photo and redrawn as clean lines in one colour. Shadow = blurred silhouette along one light vector, softer the higher the object. **No frame upsamples a photo**: ≥ 1 source px per screen px at its largest, measured; cap the zoom or find a bigger source.
- **Secondary layer** (only where the camera never goes before the end): the photos as pinned prints, a source card, sums on sticky notes, a small sketch. Texture and proof for the final wall, lighter than the main line.
- **Props (z ≈ 8–26)**: magnetic tags, magnets, a steel ruler, printed cards, a pitted stamp impression; the tray (z 70) nearest the lens.
- **Camera**: parallax by height, sub-frame motion blur (180° shutter), light grain. Only subtitles are screen-space.

## 3. Colour logic

- Ground: the enamel and its light falloff; the wall around is neutral warm grey.
- Ink: graphite = names, rules, facts; blue = water and measurement (dimensions, projection lines, measured numbers); red = the decision (a rejection, the key word of a verdict, the one mark to notice); grey for drafting only (extension lines, hatching).
- Red is rare: two or three red marks per frame at most, never on a red object. Full colour belongs to the photographs; props stay neutral; a red magnet is a verdict.

## 4. Type & subtitles

- **Marker lettering**: a single-weight marker face covering every script the film uses (ours: LXGW Marker Gothic, OFL, subset — re-run when words change). Content 100–160 board px; a verdict 230–400.
- **Printed labels** (tags, cards, stamps): a sturdy sans; credit lines in a monospace. A tag holds one to three words.
- **Subtitles**: a frosted acrylic strip at the bottom centre with a blue marker tick. If the film is bilingual, the film's language sits on top. **One line per language**: `nowrap`, measured in the page against a 1,500 px safe width; a long line becomes two cues. Key content stays above the strip (bottom 15 %).
- **Reading time**: subtitles ≥ max(1.8 s, speech + 0.6 s); board text stays fully in frame for CJK ÷ 4.5 + other ÷ 15 + 1.5 s from when it appears. In the final wall, text meant to be read is ≥ 20 px on screen.

## 6. Camera grammar

| Move | What it expresses | Can serve |
|---|---|---|
| Ride a line (with the pen or a dimension) | measuring; "how far does it go?" | lengths compared; a route; a timeline |
| Tilt along projection lines | the same quantity in another view | plan → elevation; a total → its parts |
| Slow push-in, slight Dutch tilt | tension, an approaching problem | a collision; a deadline; an overrun |
| Pull back and sideways | stepping back to state a rule | a constraint; a turn in the argument |
| Whip with the line, overshoot, settle | a result that exceeds | a record; an outlier |
| Rise along a leader line | from evidence to verdict | a conclusion; a recommendation |
| Staircase framing (each new item with the previous result) | comparison in sequence | rankings; tests; options |
| Judgement frame: the whole item, the limit and the verdict, held ≥ 2.5 s | a test the viewer can check | pass / fail against a threshold; a budget against a cap |
| Long pull-back to the whole wall | scale; everything at once | the end of an argument; a summary |

Framing: off-centre, cropped, close. The first frame holds a readable subject; the first strong action hits within 0.5 s. Items tested against a limit each get a judgement frame (wider each time if they grow); the verdict lands after the camera settles. Before the reveal: ≤ about 60 % of the board's width, never both side edges, never the reveal's zone. Transitions are moves; no cuts, fades or zoom-to-fit.

## 9. Pitfalls of the medium

- **Text glimpsed in passing** fails the reading time. Fix: words where the camera rests; frame each new item with the last result.
- **Only close-ups.** The viewer never sees the whole object against the limit. Fix: detail → judgement frame → hold → verdict → move on.
- **Photos that don't belong together.** Fix: one grade, one light vector, one viewpoint family.
- **Thin parts lost or stair-stepped** by the matte. Fix: key them against the clean background, redraw clean lines at the measured positions.
- **Upsampled photos** go soft in close-ups. Fix: full-resolution cuts, large sources, a per-frame check.
- **Lettering in photos** (signs, names, logos). Fix: paint out, cut, or choose another photo.
- **The wall seen too early** spends the ending; **a sparse or tiny final wall** wastes it. Fix: measure every frame's visible share; size the hierarchy for the poster; a quiet secondary layer, no empty middle.

