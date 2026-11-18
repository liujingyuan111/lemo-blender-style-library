# 80 年代赛璐璐动画 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/cel-anime-80s/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`1e16f5c6f90ebf09556ec94d37434400d309c978e00ee89e9d38dec476664eaf`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

Four layers, and the contrast between them is the look:
- **Background painting**: soft airbrushed gradients, glowing windows, wet reflections; painted once at load (colour + emissive pair), then only slid.
- **Cel** (characters, vehicles, props): flat fills, **hard-edged** shadow and highlight shapes, **coloured** outlines, never pure black; stepped at 12 or 8 fps.
- **Light**: backlit cel (透過光): signs, lamps, title letters glowing *through* the frame; flares, halation.
- **Playback**: videotape on a CRT: chroma bleed, scanlines, grille, phosphor glow, darkened corners, faint noise.

If a frame looks like modern digital anime, one layer is missing. Not moe anime (round eyes, giant irises, hatched blush), not vector clip-art (uniform black lines, gradients in shapes), not a film-print pastiche (no gate weave or scratches: this is tape).

## 2. Materials & rendering

**Cel rendering.** Fill, then a **hard** shadow crescent, then a **hard** highlight crescent, then the coloured outline. No gradients inside a cel shape (exception: one "harmony" painted still at a peak). Automatic shading: clip to the shape and fill `shape − shape shifted toward the light` with the shadow colour (even-odd); the same shifted away for the highlight and for a saturated neon **rim light** (2–4 px). Add hand-placed cast shadows. Outlines ~2–3 px at 1080p, scaled down (0.45–0.8×) in extreme close-ups. **Colour models per lighting** (色指定): define each character in daylight, derive other sets by multiplying lit / shadow / line separately, plus a backlit silhouette set with a warm rim.

**People the 80s way.** Construct the head (sphere + jaw): long egg-shaped face, soft-point chin, far eye foreshortened with a cheekbone turn in 3/4. **Almond** eyes near the vertical middle of the head, a thick upper lash line flicking outward, a tall oval layered iris, two highlights, long thin brows. Nose = a shadow plane + one stroke; one faint blush layer, never hatched. Hair in overlapping locks with sharp uneven tips over a wider dark under-layer, a continuous "angel ring" highlight with a zigzag lower edge. Lines: skin thin warm dark brown, hair dark purple; only hard props near-black. Emotion lives in brows, lid height, iris size, mouth corners and shoulders. Build and approve a **model sheet** first; draw every shot from the same head function.

**Backgrounds.** Painted once at load: sky gradients, airbrushed clouds with lit undersides, buildings or landscape with painted light sources, and always a matching **emissive plate** that slides with the colour plate. Wet ground = a flipped, blurred, streaked copy of the plate darkened with ripple bands. Generic sign words only, never brands. Moving plates get a light horizontal smear (~16 px) against strobing.

**Light and lens.** Bloom strongly from the emissive canvas, weakly from the colour canvas above ~0.9; tint the widest bloom red-orange (halation). Flares: star-burst, anamorphic streak, hexagonal ghosts through frame centre. Stamp every cel's silhouette in black onto the emissive canvas so glow never bleeds through it.

**Videotape + CRT, restrained and deterministic:** chroma bleed (sharp luma, horizontally blurred and slightly shifted chroma), fine scanlines anchored to output pixels whose gap shrinks on brights, a faint RGB grille, phosphor glow, darkened corners without curved borders, faint signal noise. Subtitles are composited inside the pass after grading. Two optional accents: a **power-on** (dot → line → picture) and **tracking noise** (a few frames of tearing, rolling band, vertical hop). Check moiré on a 720p downscale. Frame: full 16:9 as a theatrical feature (4:3 pillarbox is valid for an OVA feel).

## 3. Colour logic

- Painted plates carry gradients and atmosphere; cels are flat, few-colour, saturated. Each time of day gets its own colour model, never a filter over the frame.
- The protagonist has **one accent colour** that pops in every lighting set. Line colours are dark versions of their fill.
- Skin gets its own colour in every set; multiplying daylight skin by a tint turns faces pink under neon.
- Examples: night city (indigo, violet, neon magenta, cyan, window gold); seaside noon (cobalt, white cumulus, sand, coral); classroom dusk (amber, chalk green, brown wood, purple shadows).

## 4. Type & subtitles

- Subtitles live on the tape, composited inside the CRT pass: a semi-condensed sans (e.g. Barlow Semi Condensed 600, ~50–56 px), cream-yellow with a thick dark outline and soft shadow, ~96 px above the bottom; a second speaker may take a second colour and a small boxed tag. Hold ≥ max(1.8 s, speech + 0.6 s); a line yields to the next.
- Titles: heavy italic Latin in a **chrome gradient** (sky → white horizon line → violet → pink → gold), dark + neon outlines, optional katakana line (e.g. Dela Gothic One), glowing through the emissive layer, flickering on at 12 fps with a light sweep and a star glint.

## 6. Camera grammar

A vocabulary, not a route. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Multiplane crane over a tall plate | a world revealed layer by layer | arriving; descending into a place; rising above it |
| Side tracking, 3–4 parallax layers | steady momentum | a journey; a chase; progress |
| Rear view into a pseudo-3D canyon | speed, pressure ahead | a race; a tunnel; a countdown |
| Held bust with light bands | speed or tension without animation | a drive; waiting; a decision |
| Insert with bokeh and a sliding highlight | this object matters | a letter; a key; a ticket |
| Extreme close-up on eyes | resolve, recognition | a choice; a promise |
| Slow pan across a painted still | awe, a held breath | a peak; a memory; a landscape |
| Radial speed lines + one-beat freeze | the instant before impact | a leap; a collision; a goal |
| Truck-in through a window or screen | entering another world | a flashback; a broadcast; a dream |
| Locked two-shot with lip flaps | conversation | banter; a confession; an argument |
| An earlier composition repainted | what changed | after a storm; years later |

Cut on bars. Framing: cels readable against the painted plate; keep the lower ~120 px clear for subtitles. Transitions: cuts, white flashes, impact frames, tracking noise at a tape-related beat; no digital dissolves or wipes.

## 9. Pitfalls of the medium

- White cels bloom pink → bloom from the emissive canvas; weak, high-threshold bloom on colour.
- Neon bleeds through characters → silhouettes stamped into the emissive canvas.
- Black holes in highlights → clamp before S-curves.
- Thick rim light swallows thin shapes → 2–4 px offsets.
- Hair like tentacles, a face like a paper mask, moe eyes, uniform black lines → the drawing rules in §2.
- Pink faces under coloured light → skin gets its own colour per set; weaker light sweeps on faces.
- Front views are the hardest drawing → hide them behind a visor, a windscreen or backlight when you can.
- Pseudo-3D points behind the camera flip into the sky → clamp z to the near plane.
- Canvas silently falls back to a serif → `document.fonts.load` every weight before painting.
- CRT detail inflates files → noise in the shader, only `noise=c0s=2:allf=t` in ffmpeg, CRF ≈ 23; loudnorm in two passes with `linear=true`; don't let a limiter flatten the dynamics.

