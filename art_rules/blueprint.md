# 工程蓝图 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/blueprint/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`de01fc7fcb38b17b58eb017c9cdbcb36b9242b029435a33587614c93088e1717`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

- **The whole film happens on one sheet of blueprint paper** lying on a dark drafting table. The camera moves over it like an eye reading a drawing.
- **White line work on uneven Prussian blue**: centre lines, outlines, hatching, dimension lines, leader lines with numbered balloons, a title block, a notes column.
- **A 2D line-drawing language**: orthographic and oblique/isometric projection are allowed, **3D rendering never**.
- **Rigorous convention carries the tone**: the drawing is dry and exact; the notes can carry wit, warmth or gravity.
- **The designed thing is the character.** A machine, object, building or plan acts through its parts; people appear only as a hand shadow with a pen, or a signature.

Not Hologram HUD (no glowing wireframe, no 3D orbit), not Whiteboard (no marker on white), not Copperplate Engraving (no burin tonal hatching as the whole look).

## 2. Materials & rendering

- **Sheet**: procedural cyanotype in a shader in *sheet coordinates*, crisp at any zoom: fbm between two Prussian blues, coating streaks, fibres, fold creases (bright edge, dark edge, whitening), bleached edges, specks. Around it: dark drafting cloth with a drop shadow.
- **Lines**: pale blue-white, slightly soft (mipmap bleed), a faint ink breakup driven by paper grain. Four weights (outline, detail, thin, hair; e.g. 3.2 / 2.0 / 1.25 / 0.9 sheet units). **Screen width = sheet width × zoom^0.65**, so close-ups don't turn into sausages and wides don't vanish.
- **Dash conventions**: centre line (long-short), hidden (short dashes), phantom / cutting plane (long-short-short), scaled with zoom so the pattern stays on the paper.
- **Occlusion by painter's order**: every solid is filled with "paper" before its outline is stroked. Oblique extrusion: stroke the outline at N depth steps at 2× width, then fill the same steps with paper; a clean silhouette survives.
- **Composite in buffers**: ink (white = exposed line); fx (shadow, wetness, stamp ink as channels); a subtitle overlay last. Shadows darken lines too: that is how a lifted object proves it has left the paper.
- **Hatching** (fine-line shading) for sections, soil, weights, at 45°, spacing 8–14 units.
- **Cyanotype and water**: a drop blooms deeper blue with a pale tide line; white lines inside the stain go soft; ink signatures bleed.
- **The one real thing** (optional, at most once): a drawing symbol that leaves the drawing language gets soft volume, one gradient across its whole shape, glow, and a shadow falling across the lines. It leaves a pale unexposed imprint where it was drawn.

## 3. Colour logic

- **Blue and white only.** The blue varies in value (coating, stains, folds); the white varies in weight and softness, never in hue.
- **One non-blue colour, used exactly once**: a rubber-stamp ink (red is classic; a green APPROVED or black VOID work too). It carries the verdict.
- The "real" object at the climax may carry light (white glow, soft value), not a new hue.
- Example blues: `#18336B` → `#2A58A6` with lines `#E7F0F9` and table `#0D1116`; a faded sun-bleached sheet `#3A6DA8` → `#5B8CC4`; a deep over-exposed sheet `#0F2350` → `#1D3F80`.

## 4. Type & subtitles

- **Hand lettering** for header, labels, notes and subtitles (e.g. Architects Daughter); a technical sans for title-block fields (e.g. B612); a script only for the signature (e.g. Allura). All OFL.
- **Text is written on left to right** with a glowing nib, like everything else.
- **Subtitles are drawing notes**: a light translucent box with double white rules, a "NOTE / n" cell, the text lettered on in ~0.35 s, a small leader tick. **Placed per shot in empty sky**, never fixed to the bottom (the bottom of a drawing is ground line, base and title block). Wrap at ~880 px. Hold ≥ max(1.8 s, speech + 0.6 s).
- Every subtitle is also lettered into the sheet's **GENERAL NOTES** column, so the final wide shows the whole voiceover as drawing notes.
- The **title is the sheet header**; the **title block** holds status and verdict fields.

## 6. Camera grammar

A vocabulary, not a route. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Whole sheet on the table | scale, the document as an object | establishing; a verdict; a series of sheets |
| Medium on a figure, subject ~80 % of height, sky on one side | the design being drawn | drafting; explaining a part |
| Track along a path of force (chain, pipe, wire, beam) | cause and effect | how it works; a sequence of operations |
| 2× close-up cut on a downbeat | the mechanism's heart | gears meshing; a valve; a joint |
| Locked-off, hold a beat | deliberation | a hand revising; a decision |
| Oblique depth factor 0 → 0.5 | the flat drawing "turns" and gains thickness | from plan to object; a reveal of depth |
| Section line sweeping across | inside vs outside | a cutaway; hidden structure |
| Lateral pan across Fig. 1 → Fig. 2 → Fig. 3 | versions, steps, time | revisions; stages of construction |
| Slow push-in, no voice | wonder | the one real thing |

Keep storytelling shots close; full-sheet wides are rare. Keep the main figure at least `960/zoom` from any sheet edge you will frame. Transitions: cuts on downbeats, or fig-number rewrites on the sheet; no dissolves.

## 9. Pitfalls of the medium

- **Main figure near the sheet edge** → wides show the desk. Keep margins or enlarge the sheet.
- **Upward explosions hit the header** → explode sideways and flatten long parts during the explode.
- **Subtitles on the ink buffer** vanish off-sheet and can't occlude lines → separate overlay, premultiplied alpha.
- **An object darkened by its own shadow** → zero the shadow channel only in its area.
- **Per-lobe shading on a blobby shape reads as grapes** → one gradient across the union; crescents from a union-minus-shifted mask; fill unions as one path (`nonzero`) or overlapping fills make bubbles.
- **A small payoff undersells the return** → the payoff object ~⅓ of frame height, centred, drawn stroke by stroke, subtitles off it.
- **Line weights not scaled with zoom** → sausages in close-ups, vanishing wides.

