# 等距信息图 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/iso-infographic/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`a3bf89913255043ff2c8616bff9be9f9536efe1eb7a3b98c755cb4189bd7dff1`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

- **Flat, true isometric.** No perspective, no outlines on solids; shapes are separated only by the three tones of each face. The projection never rotates or tilts.
- **Infographic furniture is part of the picture**: leader lines, label pins, dashed cut lines, hatched section faces, tracking rings, a legend, a route line all live in the world.
- **Numbers are built from icons** (Isotype), and they add up.
- **A diorama**: the system sits on a floating board or plinth with a visible cross-section at its edges, on a pale ground.

Not low-poly 3D (no perspective, no lighting beyond three face tones), not a flat 2D explainer (everything has isometric depth), not a blueprint (colour blocks, not line drawings on blue).

## 2. Materials & rendering

- **Projection**: axes at 30°. `sx = (x − y)·cos30°·k`, `sy = ((x + y)·½ − z)·k`; x runs down-right, y down-left, z up; painter depth = x + y + z. Everything is queued and depth-sorted, then flushed.
- **Three tones per face** chosen from its normal: top light, left (+y) mid, right (+x) dark. Derive tones from one base colour: mix toward warm white ~20 % for the top and toward a cool dark (e.g. `#231A2C`) ~22 % for the dark side, so shadows are slightly cool.
- **Ink lines** (2 px) only for infographic elements: leaders, pins, cut lines, rings, routes, labels.
- **The board**: floats on a pale background with a faint isometric dot lattice and a soft blurred shadow; its front faces show strata (soil, water column, floors, pipes) where the section meets the edge.
- **Composites** (a terraced hill with shrubs, a crane over a ship) are drawn as one ordered item or given a depth bias; generic painter sorting fails on them.
- **People**: minimal billboards (round head, tapered two-tone body, a thick arm stroke, a hat or hair shape for identity, no faces), stepping at 12 fps.
- **Close-ups** of hands or objects: flat faceted shapes in three tones, same logic as the blocks.
- **Level of detail by zoom**: skip small world detail at high zoom, fade tall objects in by zoom so a pull-out never sweeps a giant shape through the frame.

## 3. Colour logic

- **A pale neutral ground** (cream, paper grey or pale blue) and **5–7 flat hues**, each with its three tones; one ink colour.
- **Colour codes meaning**, the way a legend does: one hue per material or role (water is always the same blue, the subject always its hue). Never reuse a hue for two meanings.
- **The subject's hue is reserved**: when the story needs "this one", everything else desaturates toward warm grey and only the subject keeps its colour (focus + context).
- Stations that must be found in a wide shot get a pale plate with a dashed ink outline plus one accent hue.
- Examples: a recycling chain — bottle green, kraft brown, can silver-blue, compost umber, mustard on cream; a hospital — teal, coral, lavender, steel grey on pale grey; a data centre — electric blue, amber, graphite, mint on off-white.

## 4. Type & subtitles

- One geometric sans (e.g. Jost): titles 600 all caps with ~0.12 em tracking, numbers 400 large (~44 px), units at half size. All text has a ~7 px halo in the ground colour so it reads over any block.
- **Label pins**: dot (ink ring, pale fill) → vertical leader → horizontal rule → text. Pins point up or down, left or right, chosen per station so labels never cover the subject.
- **Titles** can be isometric type on a world plane, extruded as blocks.
- **The subtitle is a map label**: a pale card with a small radius and an ink border, a tiny iso cube as legend chip, sans ~42 px, bottom-centre; border draws first, text wipes in. Keep the bottom ~170 px clear for it. Hold ≥ max(1.8 s, speech + 0.6 s); lines never overlap titles or other lines.
- **An end frame can be the legend**: title, totals, the Isotype key, credits, "NOT TO SCALE".

## 6. Camera grammar

A vocabulary, not a route. The camera is a world centre plus a **log-interpolated zoom** k (px per unit); the projection never changes. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Follow along a route | process; cause → effect | a supply chain; a journey; a signal |
| Hold wide + circular inset | the system and the individual together | one worker in a factory; one cell in an organ |
| Push through nested cutaways | a fall into scale; finding one thing among millions | a needle in a haystack; inside a machine |
| Fast log pull-out | release; the big picture after a detail | scale reveal; a statistic made physical |
| Locked frame while things accumulate | a system filling up; overload | a queue; traffic; data growing |
| Lateral follow over emptiness | a breath; distance | an ocean; a wait; a quiet phase |
| Top-to-bottom tilt through strata | layers; depth; history | geology; a city's underground; a software stack |
| Switch boards (a second diorama) | before/after; here vs there | two cities; two eras; two designs |

Framing: the subject ≥ 1/3 of frame height at key moments; labels never cover it; the subtitle zone stays clear. One continuous take is one option; a cut to a new board or an inset is another.

## 9. Pitfalls of the medium

- Newell normals depend on vertex order: faces get culled as back faces → give every face an outward hint and flip the normal to match before culling.
- Painter sorting breaks on composites → draw them as one ordered item; add depth bias for overhangs.
- Semi-transparent moving solids look like ghosts → motion only, no alpha.
- A hull or wheel touching the wrong surface reads as an accident → leave visible clearance.
- World geometry behind a close-up becomes giant discs → skip detail above a zoom threshold, paint a flat backdrop behind hero layers.
- A pull-out through a tall object gives one ugly frame → fade tall objects in by zoom.
- Hidden jumps (a time or place change during a dive) must be drawn in screen space anchored on the tracked subject, so the frame doesn't reveal the jump.
- An object drawn with the wrong silhouette reads as something else (a white box with a red roof is a house) → give machines their tell-tale parts.

