# 玻璃质感产品 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/glass-product/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`630fa80cde0930154ba64f15bce5c8ee0c8dcf48d921253f8c7e3194712c8fb5`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

A single hero object of **glass, metal and light** floating in an infinite black studio. Long strips *behind and beside* it turn clear glass into a thin white outline with rainbow edges; the internals show through as in a display case. Everything moves slowly and precisely; every cut, sweep and pulse lands on the beat.

The object is always **fictional**. Never reproduce a real product silhouette (a famous phone or headphone outline), a real brand name, logo, typeface or UI.

Not a white-cyclorama catalogue shot, not a wireframe HUD, not a keynote slide: material and light are the subject.

## 2. Materials & rendering

- **Studio = a strip-light scene, not an HDRI.** Photo-studio HDRIs contain windows and clutter that print as messy streaks on glass. Build a tiny black scene of emissive planes and bake it to PMREM **every frame** (`pmrem.fromScene(env, 0, 1, 1000)`, dispose the previous RT): tall side strips behind (silhouette), a wide far strip (horizon rim), a soft top box (volume for frosted glass and metal), a weak front card (off when concave glass faces camera), a top-front key only when parts must be read one by one, an accent card driven by the pulses, and **the sweep**: a tall strip on an arc *behind the camera* (azimuth = camera + π). Being real geometry, its highlight, refraction and dispersion move physically; never paint a 2D highlight.
- **Clear glass**: `MeshPhysicalMaterial`, transmission 1, roughness ≈ 0.015, IOR ≈ 1.5, thickness sets lensing (thicker = stronger), **dispersion on** (three r163+), near-neutral attenuation, `side: DoubleSide` so other glass sees its back faces.
- **Frosted glass**: transmission ~0.85, roughness ~0.4, milky tint, thick. On black it reads as dark grey plastic unless **something bright is behind or inside it**: an opaque emissive shape inside (blurred into a soft internal glow) and/or a bright gradient behind.
- **Metals** make transparency worth looking at: satin bands, chrome (roughness ≥ ~0.14), brushed surfaces via a roughness map, boards with gold traces. **Anything inside transmissive glass must be opaque** (only opaque objects reach the transmission buffer).
- **Light guides**: dark polished opaque acrylic, clearcoat, emissive **comet pulses** along a UV axis via `onBeforeCompile` (Gaussian head, exponential tail, white-hot core, hue drifting with age). Idle emission ≈ 0.
- **Background**: black with an optional dark-grey radial sweep that separates glass edges; the floor fades into it, **no horizon line**. **Floor**: black gloss, blurred mirror, radial fade, procedural caustics (lens ring with R/G/B radii offset, warped Voronoi filaments, rings spreading from events).
- **Post**: 2× supersampling; physical DoF (shallow macro, deep exploded views); bloom only above ~1.1; **Neutral tone mapping** (AgX washes accents to white); grain 0. Model in mm, near plane 1.

## 3. Colour logic

- The world is neutral: black, greys, the white of strip reflections, the metals' own tints.
- **One accent colour family, reserved for light** (emission, caustic rings, the dispersion line on UI), optionally drifting between two neighbouring hues with age or energy. Examples: ice blue → soft violet; amber → rose; green → cyan. Pick it from what the product does, never from a brand.
- Emitters that only illuminate (inside frosted glass) stay cool-white and dim.
- Dispersion rainbows are allowed only at thick glass edges and in the caustic, never as a gradient on surfaces or type.

## 4. Type & subtitles

- **Subtitles are a slab of frosted glass**: a centred rounded bar filled with the live frame blurred (`filter: blur() brightness()` on the WebGL canvas, `preserveDrawingBuffer: true`), a little cool white, a thin highlight stroke and an accent line on top. A licence-free grotesk (e.g. Inter Tight), light weight, ~36–44 px, near-white. Hold ≥ max(1.8 s, speech + 0.6 s).
- **Titles**: the same grotesk at an ultra-thin weight (200), very large (100–140 px) with very wide tracking, centred in the upper third; a diagonal glint sweeps across the letters in sync with the sweep light on the object. Small tracked caps (18–20 px) for kickers and credits.
- The product name and slogan are **title cards**, not subtitle lines.

## 6. Camera grammar

A vocabulary, not a route. Opening and ending come from the topic.

| Move | Expresses | Can serve |
|---|---|---|
| Sweep over a dark object, slow push | Contour before content | an unknown thing; a before-state |
| Slow high 3/4 orbit | The whole object in one move | a mechanism opening; variants |
| Macro, rack focus surface → part inside | Nothing to hide | an ingredient; a sensor |
| Side macro orbit | Material contrast | layers; a seam |
| Exploded view, axis ~40° to view, orbit | Technical beauty, suspension | architecture; a pause before a turn |
| Straight-on front, slight push | Declaration | a single number; a name |
| Top-down macro | A pattern at full size | channels; a circuit |
| Top-down on the floor | The effect leaving the object | range; spreading energy |
| Low orbit under the object | Monument, weight | durability; a flagship |
| Slow pull-back into negative space | Room for type | a claim; a question |

Framing: one hero, centred or on a strong diagonal, never cropped by the frame edge in a wide. Cut only on beats (bar lines where possible). Product films need **no spatial continuity** between shots: each shot is its own presentation stage, so hide or move anything that doesn't serve it. Transitions are cuts on the beat or a sweep passing through black; never dissolves or wipes.

## 9. Pitfalls of the medium

- A manually updated mirror uses last frame's camera → call `scene.updateMatrixWorld(); camera.updateMatrixWorld()` first; the transmission pre-pass re-renders it → no-op its `onBeforeRender`, update once per frame.
- A coloured emitter inside frosted glass tints the whole object; idle glow under a lens dome becomes a pale blob; AgX turns accents white; frosted glass on black is black; mirror chrome becomes a white disc → the rules in §2–§3.
- An exploded view seen perpendicular to its axis is edge-on lines → axis ~40° to camera.
- Pure profiles read as simple shapes (mushrooms, pot lids) → 3/4 views, lids upright behind.
- Bass peaks without headroom push loudnorm into dynamic mode → limit them in the mix.
- Concave glass facing camera prints the front card as a grey rectangle → card off.

