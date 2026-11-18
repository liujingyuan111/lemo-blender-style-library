# 金箔彩绘 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/gilded-illumination/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`515c5d01d9892fc629abf521aef4796862320fb072422bc72da27f5cf6b17252`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

- **Flat pigment, firm line.** Every shape is one flat colour, a darker band just inside the outline, a **firm ink outline** (never hairline: at least ~2.5 px on screen in a wide shot, thicker in close-ups) and white-lead strokes on the edges that face the light. No gradients that model form, no soft shading.
- **Gold is a material, not a colour.** Gold leaf is laid in squares: you can see the leaf blocks, their seams and overlaps, a little red bole where the leaf broke, punched dots. It lies dark and warm until a light crosses it; then the squares flash one by one (each one tilted a little differently) while the pigment beside it stays matte. That contrast is the style's signature. Anything yellow on screen is either real leaf with that texture or a pale pigment that cannot be mistaken for it; never a flat yellow standing in for gold.
- **White lead in strokes and dots.** Besides the edge strokes, white lead is laid as dots: triads on foliage and rock, a row of pearls along a hem, a band of pearls on a vermilion ring. They are what makes a flat shape read as painted, not as a vector illustration.
- **The picture is the place.** The camera lives inside one painted world. Text, when there is any, lives inside the picture too: a speech scroll, a plaque in the border, an inscription.
- **The world is painted too.** Mountains, trees, buildings, figures, water and sky use the same palette and the same outline-and-highlight rule. Nothing switches to photographic or 3D-shaded rendering.
- **Night is deep ultramarine.** The dark of the picture is the blue ground sinking toward a deep lapis, never black and never grey. When light returns, the sky stays a deep blue: the world gets brighter because its gold lights up, not because the blue turns pale or the whole frame is lifted.
- **Medieval pictorial logic.** Mountains are clusters of stepped, leaning spires; skies are blue grounds with gold stars and scalloped clouds; distance is shown by size, overlap and paler pigment, not by atmosphere.

Not Stained Glass (no lead cames, no transmitted light), not Art Deco (no streamlined geometry, no metallic gradients as decoration), not Ukiyo-e (no woodblock bleed, no bokashi), not Paper-cut Lightbox, not a fantasy game map, not a flat vector illustration with yellow circles.

## 2. Materials & rendering

- **Pigment shapes**: `fill` + `rimShade` (the same path stroked inside its own clip in a darker tone) + ink `stroke` + white-lead `hiLine` + white-lead dots. This recipe is the whole look; keep line widths tied to the camera so they never thin out to a hairline in wide shots.
- **Gold leaf**: a tileable texture laid in leaf squares (each square its own tone, a thin dark seam with a bright overlap ridge, a few cracks, specks of red bole), filled through a pattern into any path, then a burnish, a speck layer, an inner rim and an ink outline. Punched decoration is rows of tiny dark dots with a light fleck. Raised (gesso) gold gets a small cast shadow.
- **Light only on gold**: every gold path is also written into a screen-space mask; light from the picture's own sources is added only inside that mask, per leaf square (each square has its own tilt, so the light moves across the squares unevenly), with star-shaped flashes where it is brightest. Pigment never receives specular light.
- **Lit gold stays gold**: light pulls the leaf toward a warm gold with a cap on each colour channel (ours stops at 82% of the way), so the brightest leaf still shows its squares and seams and never burns to white or flat yellow. A soft bloom, if any, belongs only to the most strongly lit leaf and stays small; never a wash over the frame.
- **Ground pigment (ultramarine and friends)**: a granular pattern (coarse grains, not noise) mapped between a dark and a light tone of the hue.
- *Reference:* vellum (procedural sheet with grain and stains) is kept for the parts that are written on: speech scrolls and the end plaque.
- *Reference:* static and live layers: anything that does not move can be pre-rendered under the camera; anything that grows, flashes or is lit is vector, every frame (ours draws everything every frame at ~50 ms).
- **Light comes from inside the picture**: a lamp, the sun, a band of light crossing the painting. Night is the pigments sinking toward blue; lit gold rises above it.
- *Reference:* infinite zoom: textures that must survive a big push (the leaf in a macro shot) are generated again at higher resolution for that region and cross-faded by log zoom.

## 3. Colour logic

- The ground is ultramarine (sky) or gold (gold-ground panels and frames). Everything else is a short list of medieval pigments: lapis/ultramarine blue, vermilion, verdigris green, rose, azure, lilac-grey, white lead, iron-gall brown ink, gold, rarely silver. Ochre only in small, clearly matte places (hair, a roof), never on large areas next to gold.
- Each pigment comes in three values only: body, darker rim, white-lead highlight.
- Blue and gold are the pair the eye goes to; keep the biggest blue field and the brightest gold for the moment that matters. Vermilion is for the hero, frames and marks of importance.
- *Reference palette:* ultramarine `#22379a`, vermilion `#c8321f`, verdigris `#3f8f7a`, rose `#d97a8a`, ink `#2a1a10`, gold leaf (texture, mid tone `#c99a3e`); vellum `#efe2c4` only for scrolls and the plaque.
- Brightness is carried by gold, not by the whole frame: from the darkest night to the brightest ending, the average brightness of the picture moves little; what changes is how much gold is lit and how brightly.
- Never: neon, pastel gradients, photographic skies, flat yellow used as gold, black outlines thicker than the shapes they hold, a pale or washed-out sky after the light returns, a global brightness or saturation boost to show "day".

## 4. Type & subtitles

- *Reference:* titles and inscriptions in Uncial Antiqua (display capitals) or Grenze Gotisch (lowercase Gothic); explanatory words and subtitles in IM Fell English (roman and italic) for English and Noto Serif SC for Chinese, in brown ink, written on scrolls and plaques. One language per line.
- **Sizes**: text meant to be read ≥ 40 px at 1080p for titles, ≥ 32 px for English subtitles, ≥ 34 px for Chinese.
- **Reading time**: hold ≥ CJK ÷ 4.5 + other ÷ 15 + 1.5 s, and ≥ 1.8 s, from the first frame the block is complete. Text is revealed by a pen wipe, never typed letter by letter.
- **Subtitles are a speech scroll, fixed in one place**: a vellum banderole at the bottom centre of the frame (Chinese line, English line) that unrolls when a line is spoken. It is part of the style. It never moves sideways and never changes size: one width for the whole film (set by the longest line, shorter lines centred inside it), one height, one type size. Between two close lines the scroll stays open: the old words fade, then the new ones are pen-wiped on; two lines are never seen on top of each other.
- **Compose for the scroll**: the hero is kept out of the lower-centre band while a line is up (higher in frame, to one side, or the camera lowered), rather than moving the scroll.

## 6. Camera grammar

A virtual camera over a flat painted world (centre, log zoom, roll).

| Move | What it expresses | Can serve |
|---|---|---|
| exponential pull out of the leaf | from the material to the picture | an opening; a reveal of scale |
| push through a quatrefoil / foliate frame | entering the picture, changing chapter | a hero introduced in a roundel, then the world |
| follow along the path of a continuous narration | a journey, time passing | a climb, a pilgrimage, a delivery |
| foreground spire or cloud wiping across | an elided stretch of time without a cut | the middle of a long walk |
| locked frame while light rakes | revelation, value | the finished work, gold, a seal |
| a band of light sweeping the whole picture | the world changes | a sunrise, a verdict, a return |
| a ring of gold light spreading from a touch | ignition, a decision, a turning point | a key turning in a lock, a seal pressed |
| hard cuts on circles, centre to centre | match, repetition | a wheel to a halo, a coin to a seal |
| the big pull back to the whole painting | the story was one picture | endings: every scene seen at once |

Framing: the painted world fills the frame edge to edge; a patterned border can be the camera's frame and, at the end, grow into the whole painting's frame. Allowed transitions: continuous zoom, push through a frame, foreground wipes, match cuts on shapes, hard cuts on the beat. Forbidden: page-turn wipes, slide transitions, cross-dissolves between unrelated scenes.

## 9. Pitfalls of the medium

- **Shading creeps in.** Soft gradients make objects look plastic; model with the rim band and white-lead strokes only.
- **Flat-illustration drift.** Thin lines, no white dots, gold as plain yellow discs: the picture turns into a modern vector illustration. Keep the ink firm, add white-lead dots, show the leaf squares.
- **Gold everywhere, lit all the time.** If gold shines all the time, the light has nothing to reveal. Keep gold dark until its moment.
- **The white-out climax.** Pushing the lit leaf's brightness up (or adding a big glow) turns the brightest moment into a yellow-white blur and erases the leaf squares. Light the climax with more gold, not with more white: rings, squares lighting in turn, a capped gold tone.
- **Day by brightening.** Raising the whole frame's brightness or saturation, or turning the night sky light blue, to show that the light came back looks like a colour-correction slip and kills the deep ultramarine. The sky stays deep; the gold does the work.
- **Wandering subtitles.** A scroll that jumps between left, centre and right, or changes width with each line, reads as an error. Fix its place and size; move the camera or the hero instead.
- **Picket-fence mountains.** A row of spires of the same height reads as a fence. Group spires in clusters (one tall, smaller ones leaning off it), vary the gaps, and stack two or three ranges, paler and smaller behind.
- **Stacked-box mountains.** Rectangular ledges read as buildings; spires must lean and taper, with small stair-steps on both flanks.
- **The hero as a nun.** A hood over the face makes a small figure read as a nun or monk; keep the face and hair visible.
- **Blackletter legibility.** Grenze capitals are hard to read; set display capitals in Uncial and keep Gothic for lowercase words. Never set Chinese or long English in blackletter.
- **Fake Latin.** Use real public-domain Latin sentences or none.
- **Infinite zoom seams.** A single texture stretched over a big push turns to mush; regenerate the leaf at the zoomed region's resolution.
- **Render state.** Canvas state and cached patterns leak between frames; reset the context every frame and clear offscreen buffers.

