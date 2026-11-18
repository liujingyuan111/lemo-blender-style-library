# 2.5D 像素 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/hd-2d/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`f83bb4ee11739d4367bfce5371ba4110d5b6a5033b18aa5cc5fa37f82ceda323`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

A **3D miniature set** of boxes and cylinders wrapped in **pixel-art textures**, populated by **flat 2D pixel sprites that receive light and cast shadows**, seen from a **high, far camera** through a **tilt-shift band** so the world reads as a tabletop model. **Light is the subject**: practicals throw sprite shadows across the floor; shafts, fog, dust or rain hang in the air; strong bloom, heavy vignette. On top, a small **RPG UI**: chapter card, framed dialogue box with typewriter text, serif subtitles.

The key contrast: characters stay **flat, low-res and stepped** while camera, light, particles and focus move smoothly every frame.

Not a voxel game (no cubic characters), not a flat 2D pixel RPG (the set is real 3D with real light), not a tilt-shift photo of a real miniature (textures are pixels, not materials).

## 2. Materials & rendering

- **Constant texel density**: surfaces drawn per pixel on small canvases, `NearestFilter`, world-space UVs at one density (e.g. 24 px/m); sprites on a similar scale (a character ~30–60 px tall).
- **Colour from ramps**: 3–6 swatches picked by brightness through a narrow 4×4 Bayer dither. Sprites get a 1 px *selout* outline (neighbour colour darkened toward the ink).
- **Boxes and cylinders** for buildings, floors, rock; **billboards** (instanced) for foliage, distant props, ridges. Windows are emissive pixel panes; fire is a pixel atlas stepping at ~10 fps; water a shader with quantized ripples and light columns toward the camera.
- **Light rig per set**: one dim shadow-casting key, a hemisphere fill, **practical point lights** with shadows (lamps, fires, windows, screens), and a **front fill** ~2 m before the hero (a billboard lit from behind stays black). An additive glow sprite on every source gives bloom something to grab.
- **Post chain, at render time**: supersampled render → physical DOF with tilt-shift in the same signed circle of confusion (above the band = far, below = near; far never bleeds over a sharp foreground) → bloom → vignette/grade → filmic tone map. No film grain.

## 3. Colour logic

- **Two temperatures**: one large ambient key (cold, or pale, or dusty) against small warm or saturated practicals. The practicals carry the story; the ambient carries the mood.
- The darkest value is a warm ink, never pure black; the brightest is the light source itself, bloomed.
- Each set owns one fog colour and one light key, so a cut to a new place reads instantly.
- The hero wears the one saturated costume colour that no set uses, so the tiny sprite is findable in a wide.
- UI is one metal (gold, silver, copper) plus one paper white over a dark translucent plate.
- Examples: night canal town (blue fog, amber windows); autumn market at dusk (violet sky, pink paper lanterns); snowy mine at noon (grey-white daylight, green mineral glow).

## 4. Type & subtitles

- An inscriptional capital serif (Cinzel, wide tracking) for chapter labels and titles; an old-style serif (Cormorant, Cormorant Garamond italic) for subtitles, dialogue, taglines. All OFL.
- **Narration subtitles**: italic serif ~46–54 px, centred low on a soft dark gradient band, one line per voice clip, in ~0.35 s before the voice.
- **On-screen speech gets a dialogue box**, not a subtitle: dark plate, thin metal border, corner ornaments, name plate on its top edge, text **typed over ~90 % of the voice**, blinking caret, soft chime on entry.
- Chapter cards and a title card belong to the grammar. Hold ≥ max(1.8 s, speech + 0.6 s). Export the `.srt` from the data that drives the overlay.

## 6. Camera grammar

A vocabulary, not a route. Opening and ending come from the topic. Always look **down** on the world (never at eye level); every path is a monotone spline of a few keys, no overshoot; focus is recomputed every frame from camera to the subject.

| Move | Expresses | Can serve |
|---|---|---|
| Very high, very far, slow push; band on one tiny subject | Preciousness, a whole place as a map | where we are; scale; a landmark |
| Medium-high 3/4, near-static drift | Two figures on one stage | a conversation; a handover; a choice |
| Lateral tracking, camera leading slightly, foreground passing blurred | A path through a world | travel; a process with steps; a commute |
| Dive low and close while a figure kneels or stops | The toy world suddenly personal | exhaustion; care; a secret |
| Rising pull-back, focus handed from figure to object | The act spreads outward | consequence; a system switching on |
| Orbit half-way round a building or prop | An object seen from all sides | a workshop; a machine; a monument |
| Top-down, straight overhead, tilt band as a strip | A board game, a plan | routes; a schedule; a queue |
| Rack focus between two depths in a locked frame | Attention changing hands | a memory; someone watching; before/after |
| Return to an earlier framing, changed | The rhyme shows what changed | aftermath; growth; a season later |

Framing: characters ~1/12–1/8 of frame height; the sharp band follows the subject's projected height (clamped ~.2–.8 of screen); with no character, use a fixed band height per shot. Transitions: short fades to black or cuts between sets; no wipes, no 3D spins.

## 9. Pitfalls of the medium

- **Checkerboard everywhere** → the dither band is too wide (≈ .22 on sprites, ≈ .45 on textures).
- **A light burns out the sprite that holds it** → move the light ~0.45 m toward the camera; cap sprite lighting in the shader (`min(outgoingLight, diffuse * 1.35 + emissive)`).
- **Lights behind a billboard don't light it** (front normal only) → always the front fill.
- **Cylinder beams facing the camera give NaN** that bloom spreads into black blocks → billboard beam cards that fade toward the lens, glow sprite takes over.
- **Dark scenes unreadable** → lift environment mid-tones ~×2–2.5 outside the one beat that must go dark.
- **Distant glows hidden by fog** → `depthTest = false`, higher `renderOrder`.
- **Tilt-shift with no character to track** → fixed band height per shot. **Tilt as a separate blur pass** breaks occlusion → fold it into the DOF's signed CoC.
- **Node render scripts may not exit** after `done` (server keep-alive) → `process.exit(0)`; the file is complete once `done` prints.

