# 火柴人讲解 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/stick-explainer/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`da45e2773336892fb75b77e5cdd805d0376a532e509418df0c33780b7e477490`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

- **The people are the diagram.** Each figure is a round head and single curved lines, all one weight (an "even hose" body). No faces, no hands, no props for heads. The figures act out the idea: who changed, who reacts, who is connected.
- **Bodies are continuous.** The head sits on the neck with no gap; limbs grow from one point on the torso; every limb is one smooth curve, never a polyline with a corner at the elbow or knee.
- **Hands join into one line.** Two held hands become one tangent-continuous curve between two shoulders. A row of people holding hands is a single line; a ring of people is a closed shape.
- **One accent, one meaning.** Ink figures on paper; the accent marks the one thing that matters on this screen (the source of a change, a path that connects, a number that crosses a limit).
- **Logic as motion.** Change travels: a pulse runs along the ground line or through joined arms, and each person reacts as it reaches them.

Not Whiteboard Explainer (no hand drawing the frame, no marker texture), not Pictogram Motion (figures are drawn lines, not filled ISO-style pictograms), not Data Storytelling (the people are the chart), not Mid-century Cartoon (no character design, no faces, no props).

## 2. Materials & rendering

- **Paper**: one flat warm off-white with a very fine matte grain (± 3 levels of value), drawn once and reused. No vignette, no fibres, no shadows.
- **Figures**: Canvas 2D strokes with round caps and joins. A skeleton (hip, curved spine, two-bone arms, IK legs, a head that rotates about the neck) drives quadratic curves: each limb runs from its root to its tip with the joint as control point (`k ≈ .8`: the curve bends towards the joint without passing through it). The head is a filled paper disc with an ink ring; an accented figure has a solid accent head.
- **Line weight**: one weight per figure (≈ 8 px for a figure 380 px tall). In a still scene, scale it with √(height/380), clamped 0.6–1.05; when the camera changes scale across orders of magnitude (fractal pull-backs, a whole globe), scale it in proportion to the figure so it reads the same on screen.
- **Joined hands**: both hands travel to a clasp point (between the two shoulders, 0.17 × height towards the feet when hanging, above the shoulders when lifted). Once clasped, the two control points are rotated onto one line through the clasp (tangent continuity), so the two arms draw as one hose. Each half keeps its owner's colour.
- **The accent run**: a stroke in the accent colour drawn along the joined arms' path up to a length that grows with time (round front, like liquid in a tube). Nodes on the ground line fill as it passes.
- **Rotation**: a figure can stand on a circle with its feet on the circle and its head outward. Joints are computed in the figure's own frame and mapped to the world, and "down" (where hands hang and elbows bend) follows the figure, so rings and globes use the same rig.
- **World and camera**: everything lives in world coordinates under one camera (centre and zoom, zoom interpolated in log space). Screen space is only for titles, the count column, sources and subtitles.

## 3. Colour logic

- Neutral ground: warm paper. Ink is for lines and type only, never large filled areas.
- **One accent** (a warm red-orange). It marks: the source of a change, the connected path, the person reached, the number that exceeds a threshold. Never decoration, never a second meaning in the same film.
- Supporting tones are greys from the paper: a muted grey for secondary type and sources, a light grey for ground lines, empty nodes and dropped objects, and at most one pale paper tone for a filled shape (a globe, a panel).
- No gradients, no transparency as a colour (fades are only for appearing and leaving).

Example (our demo): paper #F3F0EA, ink #24242C, mute #9C978C, tint #E2DDD2, accent #EB4A2A, globe fill #E9E4DA.

## 4. Type & subtitles

- **One geometric sans** for everything Latin (e.g. Jost, OFL): titles 600 at 84–92 px with tight tracking (−2), big numbers 600 at 44–150 px, small caps labels 500 at 20–22 px with +3 tracking. A CJK sans (e.g. Noto Sans SC, OFL, subset to the characters used) for Chinese, ≥ 34 px on screen.
- **Left-aligned**, flush to a 124 px margin; no header bars, no centred stacks. The one exception is type inside a closed shape (a ring, a globe), which centres in it.
- **Hierarchy**: one big statement or number, one line saying what it means, one small source line. A question can sit left and its answer right on the same baseline.
- **Arrival**: type slides up 12–22 px while fading in over ~0.4 s, staggered by line; it leaves by fading. Big numbers slide further.
- **Subtitles** belong to the page: bottom-left, a 4 px accent bar at the margin, one Chinese line (36 px, ink) over one English line (25 px, mute), no box. Keep every subject above y ≈ 920 so subtitles never cover it. Hold ≥ max(1.8 s, speech + 0.6 s); a verdict or comparison frame stays fully visible ≥ 2.5 s.

## 6. Camera grammar

| Move | What it expresses | Can serve |
|---|---|---|
| Locked frame | rules being set up; reading time | a question; a demonstration; a verdict |
| Pull back | one case becomes many | one chain → many chains; one person → a crowd |
| Push in + focus shift | singling one out | "now take just you"; the exception |
| Fractal pull back | growth by a constant factor | rings ×2.5, generations, compounding |
| Through a shape | a jump to another place or time | diving into a head, a node, a ring |
| Match transform | the same thing seen anew | a line bending into an arc, a row into a ring |
| Slow drift / push | holding attention on data | a count, a comparison |

Keep the subject in the upper 85 % of the frame; text columns sit beside the figures, never on them. Cut on a beat or move through something; no page turns, no wipes, no zoom-blur.

## 9. Pitfalls of the medium

- **Polyline limbs.** Straight segments with a rounded corner still read as broken sticks. Use one curve per limb, joint as control point.
- **Detached heads.** A head spring that translates the head lets it float off the neck. Let the lag only rotate the head about the neck.
- **Two arms touching.** Clasped hands drawn as two separate curves meeting at an angle look like a kink. Align the control points through the clasp.
- **Straight bars.** When joined hands pass the shoulder line, the arms go straight for a moment; keep that pass fast and rare.
- **Hands through bodies.** Spring overshoot makes curved arms wrap through the torso in poses that touch the body (hands on hips, folded arms). Avoid those poses or lock the hand.
- **Thin crowds.** Line weight on √ scale vanishes when the camera pulls far back. Switch to proportional weight for zooms.
- **Second accent.** A second highlight colour destroys the one-meaning rule. Use grey or size instead.
- **Slideware.** Header bars, centred stacked text and page flips turn it into a deck. Keep the margin, move the camera.
- **Too much per screen.** One idea per screen; a crowd is a texture, not a list of individuals.

