# 油画厚涂 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/impasto/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`38a0dcb2808c2ff03ef721c1319b9145438b4074ed37ab7a09dcf20b7268e062`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

A moving oil painting made of knife strokes. Each stroke is a real object: a slanted plane of paint with a ridge where the blade pressed, a lip where it lifted off, broken streaks where the paint ran out, two colours dragged into each other. The world is **repainted from its strokes every frame**, but static paint never moves: only things that move in the story move. Light rakes across a height field, so the paint has body.

The look is clear and graphic (readable like a children's book at thumbnail size) but has the tactile surface of impasto at 100 % crop.

Not a Van Gogh swirl filter (strokes boiling everywhere), not a brush texture over flat vector art, not watercolour (paint is opaque), not a "painterly" photo filter (strokes are designed, not sampled from noise).

## 2. Materials & rendering

- **Value first.** Design each set as a flat, value-planned illustration (3 values minimum), then convert it to strokes. If the reference doesn't read at 480 px wide, no brushwork will save it.
- **Stroke sizes by importance and depth.** Coarse to fine: large planes in sky and walls, a few px only at edges and faces (per shape: `maxR`, `detail`, `dir`).
- **Strokes never cross shape groups**, so silhouettes stay crisp. Lost edges are opt-in (put two shapes in the same `group`).
- **Thin underpainting** (the reference itself, blurred ~1.5 px) under the strokes, so the canvas never peeks through as outlines.
- **Knife stroke**: longer than wide (≈ 1.7–3.1 × radius long, 0.95–1.45 × radius wide), slanted ends, small angle and value jitter (≈ ±13°, ±6 %). Solid objects that must read as silhouettes (figures, props) get little or no ragged run-out.
- **Light** rakes over a height field; wet or glossy surfaces get slightly more specular.
- **Reflections** (wet ground, glass, water) are **explicit stacks of short horizontal knife dabs** under each light source, broken and fading; never a painted rectangle.
- Render supersampled (2×). **No film grain**: grain plus compression eats the knife edges.

## 3. Colour logic

- Planes of mixed, slightly broken colour; each stroke may drag a second colour (`c2`) into the first. No gradients made by blending pixels: gradients are made by stroke-to-stroke steps.
- Warm light against cool shadow is the default temperature structure; the brightest, purest chroma is reserved for the story's subject (a prop, a crowd, a light source), not the background.
- **Colour can be an event.** Every stroke can hold a grey and a colour version; a monochrome world with one coloured exception, or a world re-laid from grey to colour, is native to the medium. The grey version is the luminance of the same strokes, slightly cool, with a small colour residue.
- Examples of palettes that fit: an after-rain sunset (cobalt → peach → gold sky, ochre facades, full-chroma props); a harvest field (straw yellow, burnt sienna earth, one viridian tractor); a night kitchen (umber shadows, sodium-lamp orange, one cold blue window). Choose from the topic.

## 4. Type & subtitles

- Titles are **laid in with the knife** (a stroke-by-stroke `appear` sweep of about a second) and can be taken off by the world (washed by rain, scraped, painted over). They move with the world.
- Small text (credits, data, captions) stays crisp DOM text over the painting: knife strokes can't carry small letters.
- A serif display face (e.g. Cormorant, OFL). Subtitles, if there is a voice: plain serif, ≤ 2 lines, in a calm plane; hold ≥ max(1.8 s, speech + 0.6 s).

## 6. Camera grammar

A vocabulary, not a route. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Slow truck + push on a wide | a world observed; patience | a place; a routine; a crowd |
| Push-in through a silence | inner pressure | a doubt; a decision; giving up |
| Tilt-up from the ground or a reflection | discovery from below | a small character entering; a first sight |
| Pull-back from a close-up | reaction; the world answering | consequence; a reveal of who is watching |
| Rotating crane-out, overhead | pattern emerging from many | choreography; traffic; a gathering |
| Same wide, repeated | before/after | change of colour, season or time |
| Locked frame, light moves | time and weather as the actor | a day passing; a storm arriving |
| Macro slide along the paint surface | the matter itself | a texture; a crafted object; a map |
| Whip-pan into a new painted plate | energy, a jump | a list; montage; travel |

Framing: keep the camera **inside the painted plate** (`half = W/2/zoom`), or the canvas shows. The subject gets the hard edges and the smallest strokes; everything else stays in big calm planes. Transitions: paint-over sweeps and scrapes, hard cuts on beats; no dissolves (two layers of knife ridges turn to mud).

## 9. Pitfalls of the medium

- Confined strokes shrink near edges and leave canvas-coloured outlines → add the underpainting texture.
- Draw order in the reference matters: painting the ground after the buildings covers their feet.
- Plain rectangles read as posts or blocks → give silhouettes taper, a lit edge, and one or two defining dabs (shoulder, hair, handle).
- Proportions carry the object's identity at this stroke size: a prop drawn too wide reads as a different thing. Check silhouettes at thumbnail size.
- Film grain or heavy compression destroys the knife edges → no grain, supersample, high bitrate.
- Strokes that are re-seeded every frame boil → fixed seeds per stroke.
- Engine-level WebGL traps (reserved words, VAO binding) are listed in DEMO.md build notes.

