# 霓虹灯管 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/neon-tubes/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`86b5d2d9157b4e9e1cbc8e49d0e244f45e02619226a7cf228d14e513c93c8ea3`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

- **Glass, not lines.** A lit tube reads as a cylinder: a saturated gas column in the bore, a thin glass wall, a highlight along the top, a halo that spills onto whatever is behind. An unlit tube is still visible as clear glass or milky white (phosphor coated).
- **Real gas colours.** Clear glass + neon = red-orange; clear glass + argon and a drop of mercury = blue. Every other colour is a phosphor coating (milky when off).
- **Built objects.** Tubes stand off painted boards on supports with tie wires; strokes are joined by black-painted double-backs; every tube ends in a blacked-out electrode; a transformer box sits nearby.
- **Light does the work.** Signs are the only strong light. They tint brick, tile and plaster, catch the rain and double in wet asphalt and puddles.
- **Figures are tubes too.** A character is one outline tube per pose plus a few thin tubes (eye, whiskers, tail). It never morphs: it switches.

Not a vector glow line on black (no bore, no board, no wet street); not LED "neon flex" (uniform, no electrodes); not Sci-fi Hologram HUD (screen light); not a cartoon drawn in glowing strokes (no in-betweens, no squash).

## 2. Materials & rendering

- **Tube = centreline polyline in metres** (`lib.js tubeFromStrokes`): corners filleted with a radius of about one tube diameter, strokes joined by painted double-backs, painted sleeves and an electrode cap at each end (a broken end has neither). Diameters 1.0–1.9 cm; ties every 22 cm.
- **Cross-section profile layer**: each tube is stroked into a canvas as concentric bands of the cylinder height `h = sqrt(1 - r²)` with a material code (clear, coated, black paint, metal). The shader takes the normal from a Sobel gradient of that profile: gas column inside 70–85 % of the radius, glass rim, Fresnel edge, specular streak, refraction of what is behind.
- **Emission layer** at half resolution, blurred into a pyramid, used twice: as light on surfaces (lobes sized in metres, 2 cm to 3 m) and as bloom on screen. Bricks and tiles get relief toward the light.
- **Characters from silhouettes.** Build each pose from a small rig (haunch, body, chest, neck, head, muzzle, ears, two-segment legs) as a smooth union of signed-distance shapes; take the outer contour with marching squares, smooth it and open it at one point for the electrodes (usually under the body). Eyes, whiskers and tail are separate thin tubes. One pose = one tube; a pose library of 30–40 covers a short film.
- **Hanzi from the font's skeleton.** Lay each character on a 10 × 10 grid over the skeleton of a sans-serif CJK font (Noto Sans SC): horizontals level, verticals plumb, strokes joined into as few bent tubes as the shape allows, double-backs routed behind lit strokes, never across the open face of the character. Check every glyph overlaid on the font before use.
- **The street is procedural and anchored to the world**: brick, mosaic tile, plaster, shopfronts with dim interiors, roller shutters, AC units, drainpipes, cables; a dark alley is a near-black slot between buildings.
- **Wet street**: paving, kerb, asphalt with aggregate glints; puddles grow with wetness. The reflection mirrors the facade about the wall base: sharp in puddles, smeared on wet asphalt, rippled by rain rings and single drops. Keep two screen heights of facade above the frame in the layers so a low camera can mirror signs far above it.
- **Screen space only**: camera motion blur, a slight chromatic fringe, a filmic curve that pushes cores toward white, vignette, dither, grain.

## 3. Colour logic

- The ground is dark and neutral (night facade, wet asphalt); hue comes only from tubes and the light they cast.
- Gas colours follow the physics above. Give each sign its own hue so the street reads as a sequence.
- **Characters own their hues**: a hero hue for the protagonist and a contrasting one for whoever it meets (cool against warm reads best); no sign in the same shot uses either. A character keeps its hue wherever it goes.
- Values: tube core > halo > lit wall > unlit wall > sky. Nothing painted may be brighter than a lit tube.
- Boards are deep, desaturated versions of their tube colour (navy, oxblood, aubergine, bottle green).
- A failing tube turns pale lavender-white before it dies; a dying character dims step by step toward a dull red or grey.

Example (our demo, an example only): protagonist turquoise `#1ff2d9` with pink eyes `#ff3d9e`, second character `#ff2a08`, argon blue `#3d75ff`, boards `#0a1626` `#2a0b0d` `#1a0a24`.

## 4. Type & subtitles

- **Words are tubes.** Every word the viewer reads is bent glass on a sign: hanzi as above (5–14 strokes in 1–7 tubes), Latin capitals monoline at 15–20 % of the hanzi height, Chinese on one line, English beneath.
- **Printed type only where the world has paint or paper**: a stencil on a roller shutter, a tag, a clock face. Use open fonts lit by the scene's light.
- **Readable at 1080p**: hanzi tubes ≥ 60 px tall, Latin ≥ 18 px; hold ≥ CJK ÷ 4.5 + Latin ÷ 15 + 1.5 s from the moment the sign settles after its strike. A flickering or chasing sign does not count as readable.
- No subtitle bar. Names of places come from the signs, time from a clock; a story told in this style is best told without voice.

## 6. Camera grammar

| Move | What it expresses | Can serve |
|---|---|---|
| Macro on cold glass or an eye, pulling back | the object is real glass; the moment it strikes | an opening; a character waking |
| Whip pan along the facade | distance, desire, "over there" | a character seeing its goal |
| Lateral truck with a hanging sign in front | a street, a route, a sequence | a journey; a list of places |
| Locked medium | cause and effect, reading time | a mistake; a verdict; a revival |
| Slow push on one figure | attention, guilt, decision | a reaction |
| Crane down to puddle level (eye 0.3 m) | the city doubled, urgency | a chase; rain; a mood change |
| Rise from the reflection to the sign | the real thing behind the image | arrival; a reveal |
| Pull back and rise to the whole street | everything at once | a chorus; closing time |
| Tilt down into a still puddle | what remains | an ending |

- Signs face the camera straight on (lens shift: verticals stay vertical). For a macro, set the eye height to the subject's height so the tubes' stand-off adds no parallax.
- Screen direction is story: one way out, the other way home. Keep it.
- Cuts land on beats. Match cuts work on shapes of the same size: a round clock to a round eye, a tube on one sign to the same tube on another.

## 9. Pitfalls of the medium

- **Flat glowing strokes** look like vector art: always render the cross-section and the board behind.
- **Wrong gas colours** (a green clear tube, a blue neon): only neon and argon-mercury may be clear.
- **Hand-guessed hanzi**: strokes in the wrong place, double-backs crossing the character, one tube per stroke with caps everywhere. Lay them over the font.
- **Tweened or morphing figures** break the medium; so do bright, long afterglows that multiply a character.
- **Macro bloom**: very close to a lit figure the halo floods the frame; pull back a little or keep most of it unlit.
- **Low cameras need off-screen content**: a mirror at puddle level shows signs far above the frame; keep them in the layers or frame higher.
- **A small figure in a wide shot** (≈ 100 px) reads as a streak; use wides for the street's answer, mediums for the character.
- **Readable text vs flashing**: let a sign settle before it chases.

