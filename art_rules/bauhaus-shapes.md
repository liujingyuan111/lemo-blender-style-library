# 包豪斯几何 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/bauhaus-shapes/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`f501d8728bbcd8506cd77fc1109c6949432b36e89a6f3bf82b6ad2036d9e9a6e`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、8。

---

## 1. Essence, and what it is not

- **Shapes are amounts.** A disc that doubles doubles its *area* (radius × √2); a weight three times heavier is a square of three times the area; a share of a whole is a ring of that share of the area. If the numbers would make a shape unreadably small, change the framing, never the proportions.
- **Shapes have roles.** Circle = what grows or moves; square = what stays or weighs; triangle = slope, time, pivot. One shape keeps one meaning through a film.
- **Point → line → plane.** The protagonist starts as a dot, draws a line by moving (its path stays on screen), and becomes a plane (a field, a disc that runs out of frame). Use this progression as the spine of an explanation.
- **The grid is visible.** Construction lines draw first, shapes and letters land on them, then the lines retract. The grid does more each time it returns: a layout, a ruler, a tangent, a scale on a slope, the baseline of a formula.
- **Few words, large.** One key number, one short English line, at most one short Chinese line per scene.

Not Swiss Motion Graphics (there type is the material; here type is a label and the shapes carry the meaning), not Mid-century Cartoon (no characters, no faces), not Data Storytelling (no axes, ticks and legends as chrome: a ruler appears only when it measures something), not a slide deck (no headers, no centred stacks, no page turns).

## 2. Materials & rendering

- **Canvas 2D, flat fills, hard edges.** No gradients, shadows, glows, transparency between shapes, outlines on filled shapes or rounded rectangles.
- **Opaque ink on matte card.** One full-frame finish pass: fine paper tooth and fibre (about ±7 levels, a touch more in dark inks) and a very slow, barely visible ink-density drift inside colour fields. Edges stay sharp; no misregistration, no ageing, no halftone. The finish is static (it is the paper), the shapes move over it.
- **Lines**: one weight for paths (5 px), one for construction and leaders (2–3 px), butt caps. Lines only draw a path, a tangent, a leader or the grid; never a decorative frame.
- **Compass marks**: a small cross at the centre a circle was drawn from may stay visible; it is the Vorkurs construction layer, not decoration.
- **Cropping is tension**: big discs and slopes run out of frame. Anything being compared is fully in frame.

## 3. Colour logic

Six colours per palette, assigned by role, never by hue:

| Role | Use |
|---|---|
| paper | the ground, at least 40% of the frame; also type reversed on fields |
| protagonist | the dot, the smallest amount, the thing the story follows |
| field | the one large area (a slope, a total, a heavy block); at most one per frame |
| pivot | bases, pivots, middle amounts, the square that holds the title |
| secondary | swept areas, outer rings, a pale band |
| ink | type, paths and thin bars only; never a large area |

- No pure black, no dark ground. Ink is a deep blue-black used only for line and type.
- Reversed type on a field uses the paper colour, so protagonist and field must be dark enough to carry it.
- A palette swap changes nothing but these six values.
- Example palettes (our demo): **Klein** paper #F8F7F3, protagonist #0E9F7A, field #2138C8, pivot #F4E04D, secondary #D5DCEE, ink #161C3A; **Sorbet** paper #F5E8E1, protagonist #E9476B, field #3552E8, pivot #F6B12F, secondary #94D3BF, ink #1F3340.

## 4. Type & subtitles

- **Latin and numbers**: a geometric sans (e.g. Jost, OFL, variable). Key word or number 800 with tight tracking (−2 to −6); the light companion line 300 with wide tracking (+12 to +18); reading lines 500; small labels 600–700 caps with +3 to +6 tracking.
- **Chinese**: a sans (e.g. Noto Sans SC, OFL, subset to the characters used), 700, tracking +2 to +4, **≥ 34 px on screen** (after camera scale). One Chinese line per scene at most.
- **Type joins the shapes**: a letter can be a shape (the O of a word is the protagonist dot); a number sits on the line it measures or in the field it names.
- **How type arrives**: letters rise out of a slot on their baseline, one block at a time; labels slide out from under an edge (clipped by it); reading lines reveal left to right. Never fades, never typewriter.
- **Hierarchy**: the number is largest; its caption is small caps under it; the Chinese line sits under both.
- **Subtitles**: a paper-coloured block fixed to the screen's bottom-right corner, a protagonist-colour bar on its left edge, Chinese (sans 700, 36 px) over English (sans 500, 30 px), one line each. The block never moves with the camera; compose every scene so this corner stays free.
- **Holds**: a comparison is whole in frame and still for ≥ 2.5 s before it is read out; labels ≥ characters ÷ 4.5 + 1.5 s.

## 6. Camera grammar

- Build on a locked frame; push in slowly once a composition is complete.
- Move the whole group, not the camera, when the meaning changes: a slope swings flat about its corner and becomes a ruler.
- **Through a shape**: push into a colour band until it fills the frame, cut, pull out of the same colour in the next scene.
- **Whip**: a fast lateral move to a scene beside this one, long construction lines passing to carry the speed.
- **Grid match cut**: the pieces of a scene fall out of frame, its construction lines stay and re-form as the next scene's grid.
- Every scene uses a different entry; a whole film never sits on one fixed frame.

## 8. Pitfalls

- A dark ground or large dark areas: the style turns heavy; ink is for line and type only.
- More than one field per frame, more than six colours, any gradient or drop shadow.
- Proportions bent for looks: the areas must match the numbers, or the film says something false.
- Text crossing construction lines or tangents: move the label, or end the line where the label begins.
- Labels and the subtitle block in the same corner; anything sliding with the camera that should be fixed to the screen.
- Concrete objects (parts, screens, faces): the style explains relations; detail turns to mush.
- Two paths drawn over each other: when an old path stays as reference, set it in the secondary colour.

