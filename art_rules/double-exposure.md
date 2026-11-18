# 双重曝光 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/double-exposure/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`dd8c7e6167f3323621dfbba2f286286be38c0bde58f3620a4beb91ff0243c52f`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

- **Animal silhouette × landscape.** The subject is a clean, recognisable animal profile (a horse, a fox, an owl in flight, a hare, a turtle); its fill is a real landscape or townscape photograph that belongs to it (its meadow, its marsh, the farm it grew up on, the island it returns to). The pairing is the meaning; the outline is never filled with a flat colour or a texture.
- **Two speeds.** Whenever the camera or the animal moves, the photograph inside the silhouette moves more slowly than the outline (or follows the body, never the frame). That parallax is what makes the medium move on screen.
- **The animal is alive.** It breathes, shifts its weight, lifts its head, beats its wings, swims. Its body deforms the way the real animal's body does, and the photograph inside bends with it. A rigid card sliding across the frame is the opposite of this style.
- **Monochrome photographs, warm lamps.** Licence-clean photographs (the user's own, or CC0 / public-domain files from Wikimedia Commons; check the licence on each file page) printed in black and white with a faint cool shadow / warm highlight split; the only saturated colour is the warm light of lamps, windows and city lights inside the windows.
- **Two images become one.** The medium's strongest moment is register: the place inside and the place outside slide into alignment and become a single photograph.

Not Vintage Collage (no paper cut-outs, no mixed print processes), not Ukiyo-e or Paper-cut (no flat graphic fills: the fill is always a photograph), not Shadow Puppetry (the silhouette is a window, not a lit cut-out), not a keynote (no header bars, no centred title cards, no slide transitions).

## 2. Materials & rendering

- **Silhouette masks** come from public-domain or CC0 vector silhouettes (PhyloPic is a good source for animals, but many of its images are CC BY or non-commercial: keep only those marked CC0 or Public Domain Mark), rasterised once in the page into a mask texture with three channels: R = sharp alpha (the fill), G = a blur of 2–3 % of the shape's height, B = a signed distance field where a shape needs it. G darkens the inner rim (inside × 0.4–0.6 at the edge) and makes a faint outer halo; without both the shape reads as a sticker.
- **Fills** are photographs sampled in a layer that moves with the camera at a lower depth factor than the outline (e.g. 0.6–0.85 of the outline's motion), so the inside drifts more slowly. Place the most legible band of the photograph (a ridge, a skyline, a row of lit windows) across the body, and lift the photograph's sky towards white, the way a second exposure prints into a dark shape.
- **The first exposure** (outside) is built in code from simple things: a high-key dusk sky, mist, cloud layers, the sea from below with light shafts and silt, a moonlit sea. Keep it simpler and lighter than the fill, or the two images mush.
- **Bodies deform along their own axis.** An animal's mask is sampled through a displacement field defined along its body axis (head to tail, spine line), and the photograph inside is sampled through the same field, so the place bends with the body. Cross-sections stay perpendicular to the bent spine (invert the mapping iteratively), never a shear of the whole image.
- **Swimming follows real locomotion.** When the subject swims, a fish is carangiform: the head barely moves, a wave travels from head to tail with an amplitude growing roughly with the square of the distance along the body, the tail fin lags in phase; seen from the side, the sideways sway shows mostly as foreshortening of the rear body and tail (the fin narrows as it turns away, widens as it turns back), plus a small bend of the spine so the travelling wave reads. A marine mammal (a dolphin, a whale) moves its body and flukes up and down, slowly. Forward speed surges twice per tail-beat cycle (glide and push), never a constant slide. Integrate the beat phase over time, so a change of rhythm never jumps.
- **Between two silhouettes, superimpose; never interpolate the shape.** When one animal becomes another, the second whole silhouette fades in at the same place and size while the first fades out, both drawn complete, the overlap and the two photographs blended with *screen*. A morph of the outlines (distance-field interpolation) makes an averaged, shapeless "loaf" in the middle; every frame must show a whole animal, the other whole animal, or both laid over each other.
- **Lamps** are procedural: a warm glow plus a small hot core, anchored to points in the fill photograph's own coordinates, lit one by one. They exist only inside the windows (and, after register, on the shore they belong to).
- **Post**: soft S-curve, the faintest cool shadow / warm highlight split, vignette, fine grain. Dissolves between scenes blend with *screen*, never a plain crossfade.

## 3. Colour logic

- Neutral ground: black-and-white photographs and code-drawn greys, from near-black forest to paper-white sky. Sky and water are the lightest areas outside; the fill sits darker than the outside so the silhouette holds.
- One warm hue, reserved for light inside a window: lamps, lit windows, a city at night, its reflection on the water. No orange skies, no golden-hour grading, no coloured animals.
- The warm light can grow over a film (one lamp, then a forest of them, then a whole city) to carry the arc.
- Titles may take a pale warm white; nothing else is tinted.
- Example (our demo): lamp glow rgb(255,161,82) around a pale core rgb(255,219,158); title rgb(245,230,204).

## 4. Type & subtitles

- Very little type. Subtitles are quiet: a serif (e.g. Noto Serif SC 600 for Chinese, Newsreader italic for English; both OFL), Chinese about 36 px over English about 28 px, one line each, on a barely visible soft shadow; no box, no outline.
- Subtitles sit in the empty part of the outside world (sky, water, snow), never across the silhouette's fill; move them per cue (bottom left, bottom right) when the animal occupies a corner.
- Titles and credits are developed like a print: they appear blurred and sharpen, baked into the image so they take the grade, vignette and grain. A vertical Chinese title works well beside a wide horizon.
- Reading time: every cue holds ≥ max(1.8 s, speech + 0.6 s); title and credit pass `readcheck.mjs`.

## 6. Camera grammar

| Move | What it expresses | Can serve |
|---|---|---|
| Tracking with the animal, the fill slower than the outline | the window and the place sliding apart | a journey; a migration; memory against the present |
| Push into the silhouette until its edge leaves the frame | entering the place it carries | a change of chapter; a hand-over to the next subject |
| Pull back from inside to reveal the outline | "this place was inside an animal" | a reveal; a change of narrator |
| Whip upwards with motion blur | a sudden change of altitude or scene | from ground to sky; a cry, a leap |
| Push and return during a gesture (a wing beat, a turn) | weight and scale | a climax inside one shot |
| Crossing a surface (waterline, cloud layer) in one move | one continuous world | a breach; a dive; a landing |
| Locked frame, only the inner layer and the light moving | waiting for alignment | register; an arrival; an ending |

Framing: the silhouette fills at least a third of the frame height whenever its fill must be read, and at least part of the outline stays in frame even when the fill covers the screen. A new shot of an animal starts with the whole animal readable, never a fragment that could be mistaken for a render error. Allowed transitions: screen-blend double-exposure dissolve, push through the window, pull-out reveal, whip, a continuous camera move across a surface, a silhouette-to-silhouette superimposition. No wipes, page turns, slides or white flashes.

## 9. Pitfalls of the medium

- **Mush.** Two busy photographs overlaid read as grey noise. Fix: one side simple (sky, water, mist), the other detailed; outside lighter than inside; rim darkening and halo.
- **Sticker silhouettes.** A hard-edged shape sliding at constant speed reads as a cut-out on a background. Fix: rim and halo, a slower fill, and a body that deforms with its locomotion.
- **Shear instead of swimming.** Offsetting the mask's sampling with a sine makes the whole body shear left and right while the photograph stays fixed. Fix: a displacement field along the body axis, sections perpendicular to the spine, the fill sampled through the same field.
- **The averaged loaf.** Interpolating two outlines gives an in-between shape that is neither animal. Fix: superimpose the two whole silhouettes (§2).
- **Features in the wrong place.** A bright window in the photograph landing on an eye, a gill or a fin reads as a light bulb or as something poking through the outline. Fix: move the photograph so the lit band crosses the middle of the body, darken thin parts (fins, tail, head) through the blurred mask, add a faint dark eye.
- **Unreadable fills.** The photograph's sky becomes a flat grey band inside the body. Fix: place the strongest band across the body; lift the sky.
- **Misaligned "same place".** Two different photographs never register. Fix: one photograph used twice, inside and outside, with two grades or keyed differently (lit buildings for the shore, a broken reflection for the water).
- **Mirrored tiling seams** when a photograph fills a long shape. Fix: scale the photograph to the shape, keep any seam outside the frame.
- **Colour creep.** Any warm sky or tinted water dilutes the lamps. Fix: keep every non-lamp element neutral.

