# 丝印旅行海报 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/silkscreen-poster/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`f1c86a9f0cbe735de9fb1421d33ab44465122158e6c45a4786c98852ea9952b1`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

A poster being **printed on camera**. Every colour is an opaque ink laid by its own pull; later ink covers earlier ink completely. No halftone, no fluorescent ink, no line work: a shape's edge is where one flat ink stops. **Gradients are forbidden**: skies and haze are **stepped bands** (a flat colour, thinning stripes, the next colour).

What makes it read as silkscreen and not as flat vector art:
- **Registration**: every layer offset 1–3 px at 1080p; a knocked-out shape leaves a crescent of bare paper.
- **Overprint edge**: a faint multiply ghost ~2 u off under each ink, leaving a darker sliver where ink laps over ink.
- **Ink thickness**: a light rim top-left, a dark rim bottom-right, fills only; fresh ink has a wet sheen that fades within a second.
- **Paper**: cream stock with fibres; mottle and pinholes in paper colour, visible only on ink.

Not risograph (translucent fluorescent overprint with halftone grain), not ukiyo-e (key-block line work with bokashi), not woodcut (carved line), not low-poly (3D facets). This style is opaque, line-free, flat and banded.

## 2. Materials & rendering

- **One `Path2D` per ink layer**, filled in the current transform's units; knock-outs are holes in the path. Any shape can be printed.
- **Pull reveal**: a ragged squeegee front as a clip (a ~30 u drag tail); blade, bead and a sliver of handle ride on it.
- **Ink bead**: a round tube with lit half, dark underside, rolling glints and viscous strands; a split fountain puts several colours in one bead.
- **Screen**: a hinged frame with mesh, emulsion and tape; its shadow is a ring (even-odd), never a full rectangle.
- **Shapes**: ridges with a jagged lit facet, pines as one outline of drooping tiers, water as a flat body with glint bars. Hard edges everywhere.
- **Poster templates**: a portrait sheet (1000×1500 u: paper border, art area, a dark **info band** at the foot holding a name, a number, a rule and a row of stats; columns sized by content), or a **full-bleed print** (16:9, art to every edge, the name printed into the sky, a dark info panel such as a ticket stub printed last). In a full-bleed film the camera stays inside the print.
- **Texture budget**: fine paper tile, mottle multiply ~55 %, pinholes ~75 %, light encode grain. More reads as risograph.

## 3. Colour logic

- **One palette per poster, ≤ 6 inks**, assigned by role: light sky, deep sky / bands, far, mid, near (darkest; also the info band), and **one bright accent** (sun, route, highlights, key number). An optional lit-face ink.
- **Values step from far (light) to near (dark)**; depth is value, never blur.
- **The accent is rare**: the sun or light source, the one route or product, the most important number.
- **Paper is a colour**: an unprinted area is the brightest thing on the sheet (water, snow, a beam of light).
- **A series = one template, a new palette per item** (time of day, season, colourway, neighbourhood). Re-inking the same geometry in another palette is a statement.
- **Text inks are chosen by contrast** against the ink underneath (WCAG), never by a fixed key; a night palette must not swallow a header.
- Examples (sky1 → near, accent): dawn `#F6CD98 #EE9A73 #9A7FA8 #3E7079 #1E3B3F #FBE6B4`; harbour noon `#E8F0F2 #7FB3C8 #D9C7A3 #2F6E8E #173247 #E8553D`; winter `#EEF1F4 #B8C9D9 #8B9BB0 #4A5D78 #1F2A3C #F2B134`.

## 4. Type & subtitles

- **Condensed display** for names and values (e.g. Big Shoulders Display, League Gothic), auto-fit; a geometric sans for letter-spaced labels (e.g. Outfit 600).
- Headers are **printed into the sky**, tracked out; the info band is printed last.
- **The poster text is the subtitle.** No narration is needed; if there is a voice, subtitles are a printed strip (a band pull), never a floating caption.
- **Reading rule**: each text stays ≥ chars/12 + 1 s (min 1.5 s) after its **last** item lands, and ≥ max(1.8 s, speech + 0.6 s) with a voice. Compute it from the content, round up to the beat.
- On a wall shot, labels stay ≥ ~18 px and values ≥ ~30 px at 1080p; close-ups on a band keep the whole band in frame with ≥ 5 % side margins.

## 6. Camera grammar

A vocabulary, not a route. Opening and ending come from the topic.

| Move | Expresses | Can serve |
|---|---|---|
| Truck with the squeegee, slight roll, frame edge in view | the act of printing; colour arriving | a hook; a split-fountain sky |
| Locked top-down full sheet | layers stacking into a picture | watching a poster build; a comparison |
| Fast pull-back as the screen lifts | the reveal of a finished layer | a scene complete; a title |
| Push + tilt to the info band | reading | facts; a date; a price |
| Truck through a foreground silhouette (tree, lamp post, sail) in screen space | passing into the next poster | poster-to-poster transitions |
| Crane through loose planes (multi-plane parallax) | depth, a journey inside the print | a route; a climb; a street |
| Slow lateral dolly along a row of prints | a set, a range | a series wall; colourways |
| Push into the mesh until the weave shows | the craft, the grain of the medium | an intimate beat; a detail |
| Log-zoom pull-back to the wall or window | the poster in the world | a final lockup (hold ≥ 3 s) |

Close-ups on a portrait sheet keep its edge in frame (a full-bleed print has no edge to show); a squeegee across a close-up is tilted with the handle hidden, so it doesn't split the frame. Layers change by squeegee, posters through foreground silhouettes, a diagonal sweep that prints the next poster behind the blade, or a table move. No dissolves, no bare cuts.

## 9. Pitfalls of the medium

- Stroke edge effects draw internal lines on unioned paths → fills only (fill, then fill shifted inside a clip).
- A full-rectangle screen shadow muddies the print → ring shadow.
- Cool shadow facets next to water read as water → shadows in the near ink.
- Jagged ink beads read as paper edges → a round bead.
- Parallax alone reads as "the mountains are moving" → paper gaps and thickness while loose, snapped to zero with a sound.
- Silhouette wipes hold a dark blank → centre on the switch so full cover lasts ~1 frame.
- Very wide banners are slivers in 16:9 → about 4:1.
- Random coloured dots on the table read as confetti → a real workbench (planks, grain, muted stains, tape).
- Too many items at honest reading times overrun the length → print items side by side in the same pulls, or let secondary ones be read on the final wall.

