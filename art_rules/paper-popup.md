# 纸片立体书 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/paper-popup/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`8e5c0ca430fd96b75c4d9c2af92a87c84d4d1af8cda64280a189c51279e1ee9b`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

Two worlds in one frame. **The real world** at human scale: a photoreal surface lit by an HDRI room, a few real objects, a macro lens (shallow focus, warm practical light, soft contact shadows). **The paper world**: a hardcover book in that room; when it opens, one board stands up as the **backdrop** and the lower page is the ground. Every set piece is a **flat cut-paper card** that lies on the page and **pops up** around its bottom edge. Characters are cut paper too: a few centimetres tall, flat, with a thick off-white border, a grey cardboard edge and grain.

What sells it is the **mismatch of scale and material**: flat, saturated, outlined paper cartoons under real light, casting cut-out-shaped shadows and going soft in real lens blur. Keep the paper graphic; let light and lens make it real.

Not a papercut silhouette film (no one-colour lace, no backlight), not a 3D cartoon (nothing modelled round), not claymation (paper hinges, folds, curls and slides; it never squishes).

## 2. Materials & rendering

- **Real units** (metres): page 0.3–0.5 m wide, actors 3–5 cm, near plane a few mm, so HDRI, shadows and depth of field behave like a real macro shot.
- **Cut-paper finish**: Canvas2D art with a dark ink outline; its silhouette dilated (drawn at many angles on several rings, recoloured `source-in`) into a grey cardboard edge offset slightly down (thickness) and a wide off-white border; a shared paper grain on top (`source-atop`).
- **Drawing**: one dark-brown ink (never black), thick outline + thinner detail line, round joins; shading = one hard **crescent** (fill with shade, refill shifted with base); wobbly shapes (low-harmonic noise), never perfect geometry; simple faces.
- **Pop-up pieces**: planes with art on the front and plain paper on the back (same alpha); `alphaTest` + `alphaToCoverage`; a custom depth material with the alpha map so **the shadow is the cut-out silhouette**. Anything "3D" is several flat cards (front/back layers, triangles hinged on a keel).
- **The book** is modelled: cloth cover with foil title (roughness/metalness map), page block with edge lines, a curling leaf.
- **Real world**: HDRI environment and softly blurred background, real wood or fabric, a few CC0 props. **Neutral tone mapping** (ACES shifts paper colours).
- **Depth of field by hand**: CoC = aperture × (1/focus − 1/z), spiral gather that keeps far samples off a sharp foreground (stock bokeh looks fake at this scale); then light bloom, vignette, warmth.

## 3. Colour logic

- Saturated children's-book colour, **never neon**; the real world stays natural and slightly warm so paper pops against it.
- **One dominant hue family per spread**, so a page turn is also a colour change; a few accents (a red, a yellow, a gold) recur across spreads to stitch the book together.
- Ink dark brown, border off-white, card backs plain paper.
- Unfinished or "outside the story" pages lose colour: graphite on cream. Night is a change of the paper art; the real lamp keeps its warmth.

Examples of spread families: green meadow under sky blue; pink-and-lilac market with mint accents; ochre desert with a turquoise oasis.

## 4. Type & subtitles

- Rounded OFL faces: a rounded sans for subtitles, bubbles, signs (e.g. Fredoka); a chunky display face for cover, banners, action words (e.g. Lilita One); a storybook serif for taglines (e.g. IM Fell English); a playful Chinese face (e.g. ZCOOL KuaiLe) with the Latin face in its stack.
- **Narration subtitles**: bottom centre, ~40 px, cream with a thick dark-brown outline and soft shadow, second language smaller below. Hold ≥ max(1.8 s, speech + 0.6 s).
- **Speech bubbles** live in the paper world: white card, ink outline, tail projected each frame to the speaker; pop in with overshoot, type on with blips.
- **Titles are paper objects**: a cardboard sign dropping on strings and swinging; the cover itself is the film title. Action words (italic display, gradient, double stroke, rays) sparingly, like a game rating.
- Subset Chinese fonts to the characters used; re-subset after every text change.

## 6. Camera grammar

One virtual macro camera keyed as position / target / fov / aperture / focus with monotone-cubic interpolation; a new key list = a hard cut. A vocabulary, not a route. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Eye-level macro track, shallow focus | being inside the story at the actors' size | a walk; a conversation; a chase |
| Pull up to a 3/4 view of the spread | the mechanism, the map | a page turn; a new setting; a plan |
| Descending dolly from human height | entering the book's scale | an arrival; zooming into one part of a system |
| Push-in on a face | feeling | a wish; a fear; a decision |
| Reverse shot from inside the book to the blurred room | the world beyond the page is huge | curiosity; an outside threat; a reader watching |
| Rack focus paper ↔ real object | paper and reality touch | cause and effect; a real product in a paper story |
| Top-down over the open spread | a board game, a diagram | a route; two sides of the gutter compared |
| Locked frame on a pull-tab | the trick is the event | before/after; a count |
| Rising crane leaving the book small | scale, distance | aftermath; a summary; time passing |

Actors in focus, room objects as soft foreground or background; keep near pop-ups out of the lens path. Transitions: page turns, a book closing and reopening, a hard cut on a paper sound; never a video dissolve inside the book.

## 9. Pitfalls of the medium

- `rotation.y` shows a card edge-on, then its blank back → `scale.x` flip. Negative scale also swaps front/back materials → draw mirrored props instead.
- A one-plane container hides its contents → back card + front card, contents between.
- Near-lens foreground pop-ups fill the frame with blur → move them or close the aperture.
- Rectangle shadows kill the illusion → alpha-mapped depth material on every card; tight shadow bias and a big shadow map against acne on thin cards.
- A turning page goes black facing away from lights → emissive map = colour map.
- ACES shifts paper colours → Neutral.
- Headless Chrome falls back to software WebGL → GPU ANGLE flags; ES modules need HTTP.
- Redrawing character canvases each frame → redraw only on pose change.
- Chinese subsets miss new characters and Latin glyphs → re-subset; Latin face in the stack.

