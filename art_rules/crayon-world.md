# 蜡笔立体世界 · 原文美术章节

来源：Crayon World 3D by 2nd1st, in Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/crayon-world/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`50c5b5319fabd7189cf725524092b3c69af334ae7f92052f10da2581356030b0`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

- **A real 3D place, drawn.** The world is modelled in simple primitives and seen through a perspective camera; the 3D render never reaches the screen. Each frame its shapes are traced and drawn again in crayon: outlines, scribbled hatching, colour that spills past the line.
- **The paper never moves.** The sheet is the screen: tooth, emboss and vignette stay put while the world turns behind them. Depth comes from overlap, size and parallax, never from shading gradients or fog.
- **12 drawings a second.** The camera moves smoothly, but the drawing is replaced 12 times a second, so motion has the faint stepping of hand animation.
- **Hatching sticks to things.** A roof keeps its scribble as the camera passes it.
- **A camera that is someone.** First person is native: the viewer looks through someone's eyes, and where they look is the shot.

Not **Crayon Picture Book**: that style is a flat page drawn while you watch, the camera moving over the paper, a watercolour wash, narration printed as the book's words. Here the camera moves *inside* a world, the page is only the surface it is drawn on, and there is no wash. Not a toon shader or cel look (no flat fills, no smooth lines, no lighting ramps), not a low-poly render with a paper overlay.

## 2. Materials & rendering

- **Two passes per frame.** (1) An invisible half-resolution render: region id (R), light (G), depth. (2) Marching squares trace each region into smoothed rings; crayon strokes are drawn from them into Canvas2D pressure layers (RGB = colour, A = pressure), and a WebGL2 compositor lets wax stick only to the paper's tooth.
- **A region is a drawing recipe**, not a material: crayon colour, pressure, hatching angle, row gap and width, overshoot, outline width (0 = none), layer group, and whether its dark side gets a second, denser pass.
- **Outlines** follow each region's ring but are never drawn along the frame edge (that would box the picture in). One dark outline colour for everything.
- **Hatching** is a child's scribble: bowed, leaning rows, uneven spacing, a skipped row now and then, long rows broken into overlapping strokes; a lighter cross-hatch on big areas. Every row and random value is counted from an anchor projected from the object, so it is coloured the same way in every drawing.
- **Occlusion like a child.** Layer groups (background, characters, foreground) are composited in order; before each group its silhouette is knocked out of what lies behind it, so the paper stays clean behind a figure.
- **Faces and tiny things are drawn in 2D**: eyes and mouths placed by projecting points of the 3D head; anything too small to trace (a far bird) becomes a 2D doodle at its projected position.
- **A child's vocabulary**: squashed spheres for crowns and hills, boxes, a prism for a gable roof; people with big round heads and tube limbs, props bigger than real.

## 3. Colour logic

- **A box of about a dozen crayons.** One dark outline colour (indigo, plum or dark brown), never black. Value comes from pressure and a dark-side pass, not from more hues.
- The sky is a light-pressure cross-hatch so the paper shows through; the ground is lighter than the things standing on it.
- White things are not coloured: the paper is their colour, with an outline only (clouds, a white wall, a gravestone).
- One colour may belong to the story (the flowers someone planted, a red scarf) and is used nowhere else at that strength.
- Example box (a village in summer): indigo line, sky, white, grass, olive, lemon, caramel, earth, brick, rose, cream, plum.

## 4. Type & subtitles

- Words are **printed on the page**: a handwriting face in the outline colour, written in a character at a time, sitting on blank paper. Never a speech bubble, a box or a plate.
- Blank paper is made: leave part of the picture uncoloured (only a strip of sky) and put the words there, clear of what the eye follows. Thin the colour out just before the words arrive; blank paper held empty reads as a mistake.
- Bilingual: the Chinese line, then the English line a size smaller underneath, written in after it. Example faces (OFL): Long Cang for Chinese at 110–140 px, Patrick Hand for Latin at 50–64 px.
- A wordless film is native; a narrated one prints its lines the same way, at the bottom of the frame, on a paper patch the scene leaves free.
- Reading time: every block stays fully in frame ≥ max(1.8 s, CJK ÷ 4.5 + other ÷ 15 + 1.5 s) (readcheck).

## 6. Camera grammar

| Move | What it expresses | Can serve |
|---|---|---|
| First person, gaze leads | We are someone; what they look at is what matters | a memory; a visit; a stranger arriving |
| Gaze follows a moving person with a lag | Watching, not tracking | longing; shyness; a child watching a parent |
| A low skim over a surface (wheat, water, roofs) | Speed and freedom | a journey; a return home; a chase |
| Rising over a place | Leaving, or seeing it whole | a farewell; a map of a life; an ending |
| Riding something that sways (a flower, a boat, a branch) | Being small and alive in the wind | waking; waiting; a rest |
| Hard cut to another person's eyes | The other side of the same moment | a reveal of who the camera was; a reply |
| Narrow field of view, held | Staring at one thing | recognition; grief; a decision |

Framing: keep the subject of a held shot at least 1/4 of frame height; keep paper free where words will go. Transitions are cuts or camera moves; never a dissolve, never a 3D-looking whip with motion blur.

## 9. Pitfalls of the medium

- The camera passes inside a solid (a hill, a roof) → clamp its height above the terrain and check flight paths against every big shape.
- A pop where two camera phases meet (waking, take-off, landing) → derive each phase's position from the same rest pose; ease clearances in instead of clamping them on.
- Smoothing a look-at point near the camera whips the view → smooth the direction.
- State carried between frames breaks parallel rendering → recompute smoothed values from the shot's start each frame.
- Hatching recomputed per drawing reads as heavy boil → anchor rows to the object.
- Two-pose flapping or stepping can poke through a nearby object on the extreme pose → limit the pose while the object is close.
- Things that shrink below a few analysis pixels flicker or vanish → draw them as 2D doodles below a size threshold.
- Region ids live in one 8-bit channel → at most 255 recipes per film.
- Uncoloured outlines (clouds) left floating on blank paper look unfinished → hide them where the colour has been taken away.

