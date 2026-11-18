# 纸雕灯影 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/paper-lantern/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`e8be26d64f33229859e284a33d77969f9a4468b7bf1b478ca8fa924c7dd9f27d`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

Every shot is made of **one physical object**: a shallow box (a cavity about 0.56 × 0.33 m, 0.16 m deep) holding parallel sheets of cut paper. Two framings are both valid, and a film may use either or both: **box framing** (the lamp's edge or frame is in the picture) and **full-bleed** (the lens is inside the box and the paper scenery fills the screen). The stack, the backlight and the shadows are the same in both. Everything on screen is one of three things:

1. **A paper layer**: a flat cut sheet, one flat colour, fibre grain, a thin warm **rim of light on its top edge** and a **dark band on its bottom edge**. Back layers lighter and cooler, the front almost black: that value ladder *is* the depth.
2. **Light through paper**: a warm, cloudy translucency (pulp mottling), strongest near the light source. Windows, lanterns, trails of light are **holes / emissive windows** that burn and bloom.
3. **Shadows**: a top spot casts **soft shadows** from every layer onto the layers behind. This sells "real paper in a real box"; never turn it off.

The film may step out of the box into the **real world** (the lit lamp on a table, spill light on nearby objects) to say "this is an object someone keeps"; whether, where and how often is a choice of the film.

Not flat paper-cut animation (here: depth, backlight, cast shadows), not shadow puppetry (no single screen, no rods), not a 3D diorama (every element is a flat sheet parallel to the box front).

## 2. Materials & rendering

- **Units in metres, y up.** Layers from z ≈ −0.14 (sky) to 0 (front); camera at z ≈ 0.2–0.56, fov ~26°. In box framing, sheets are **never larger than the cavity**. In full-bleed shots that travel, a layer may be a long strip that scrolls past, and the sky panel moves with the camera so its edge never shows.
- **A layer** is a Canvas2D drawing in metre space mapped to a plane; cut-outs are `destination-out` holes. Finish on every sheet: fibre grain (`source-atop`), a warm top rim and a dark bottom shade, each shifted a few px.
- **Backlight shader**: `emissive += albedo × lightCol × trans × lit × falloff × (base + cloud)`, with a Gaussian falloff around a per-shot light point and a tiled pulp-mottle texture. `trans` per layer goes from ~.9 (far) to ~.05 (front).
- **Emissive windows**: a second canvas (white = light) gated by a 0→1 "switch on" uniform; bloom makes them burn. Titles, lights and curtains in front neither cast nor receive shadows.
- **Lens**: shallow depth of field, bloom, a gentle vignette; supersample 2× so cut edges stay crisp.
- **Real-world set** (when used): wood frame, black lining, a dark room, an area light as the box's spill onto real objects.

## 3. Colour logic

- **Back layers bright and translucent, front layers dark and opaque.** Each layer is one flat colour; the ladder of values from back to front is the depth. Never break it (a pale front layer flattens the box).
- **One temperature per stack**, chosen by the scene (cool night, warm interior, violet or green elsewhere). Changing ladder is how the film says "another place".
- **Light is warm** (amber to gold) against the stack, and it is the only saturated element besides one accent.
- **One accent colour** (a seal red, or a single object's colour) marks what the story is about. A second accent only when the story has two sides (one each).
- Examples of ladders: night village — `#0a1330` sky → `#6a86c2` far → `#3f5a92` mid → `#0e1532` front, windows `#ffb862`; desert caravan — `#f0c890` dusk sky → `#c07850` dunes → `#6a3020` → `#1e0e08`, fires `#ffd080`; winter forest — `#dfe6ee` → `#9aaec4` → `#4a6078` → `#101820`, one red scarf.

## 4. Type & subtitles

- **Text in the picture is paper**: titles, letters, poems and captions are cut strips inside the box, revealed by growing from an anchor edge (scale the texture repeat with the mesh so glyphs aren't squashed), with an optional small seal.
- Chinese: an OFL brush font (e.g. Ma Shan Zheng) for titles, a running script for handwriting, Noto Serif SC for subtitles. Latin: an OFL serif (e.g. Cormorant) at similar weight.
- **Subtitles** are quiet and burned in: warm off-white serif, soft shadow, fading in just before the line. Where they sit depends on the framing:
  - **box framing**: under the box, on the dark of the room (serif 500, ~40 px CJK / ~38 px Latin, ~74 px from the bottom);
  - **full-bleed**: on the darkest band at the bottom of the scene (the front layer), ~64 px from the bottom, never over a figure, a lit window or a light. A faint dark band behind the text is allowed when something lit has to sit there.
  - A bilingual cue is one CJK line (~40 px) over one Latin line (~42 px). No wrapping: a line longer than ~21 CJK / ~42 Latin characters becomes two cues, split at the comma nearest the middle.
- **Words that appear as paper are not subtitled**: never show the same words twice.
- Hold ≥ max(1.8 s, speech + 0.6 s).

## 6. Camera grammar

A vocabulary, not a route. The lens is small and the box is shallow: moves are short. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Slow dolly in, nearly frontal | intimacy; being drawn into a place | a memory; a detail that matters; a lit window |
| Slow dolly out | context; loneliness; scale | a figure alone; before/after; the whole place at once |
| Rack focus between layers | attention moving in depth | two people near and far; a clue behind; now and then |
| Lateral travel with depth parallax | journey; time passing | a road trip; a process in stages; a timeline |
| Top-down layer stack | a made thing seen as a craftsman sees it | a recipe; a letter; a map; a product being assembled |
| Pull out of / push into the box | the frame as object; "this is a story told" | a keepsake; a framing device; returning to the present |
| Locked frame with only light changing | waiting; the passage of a day or a night | a vigil; seasons; a city going to sleep |
| Tilt up/down the stack | climbing; falling; sky vs ground | a mountain; a well; hope and weight |
| Near-plane occluder wipe | a curtain between scenes | chapter changes; dreams; a secret revealed |
| Travelling alongside | speed; being carried along (near layers rush past, far layers drift) | a journey by train or boat; a delivery; a migration |

Framing: the story layer in focus, foreground and far layers soft; box edges fully out of frame inside, clearly in frame outside, never half. Transitions: dissolves (0.5–1.2 s), an iris, light off/on, a near-plane curtain whose halves meet exactly. No whip pans, no digital zooms.

## 9. Pitfalls of the medium

- `destination-out` cut-outs need an **opaque fillStyle** before punching, or the hole is half-cut (`world.js` `cut(x, fn)` does it).
- Soft shadows bleed and halo: layers that must not take part need **both** `shadow: false` and `recv: false`.
- A transparent radial-gradient texture shows a square edge as an additive glow → use an analytic shader falloff (`burst()`).
- A near-plane curtain whose halves don't meet at their **front edges** leaves a slit of the old shot.
- Sheets larger than the cavity poke through the frame in outside shots.
- **Grade state must not carry over** between shots: every grade key a shot omits must fall back to a default each frame, or renders depend on which frame a worker started on (visible pops at worker boundaries).
- **Light over paper text**: a lamp's glow or a headlight flare over a name board or a card washes the letters out. Keep every lit point clear of text.
- **Subtitles over a lit window** lose their contrast: frame so the bottom band is dark, or put the faint band behind them.
- Headless Chrome must run with GPU flags; SwiftShader is ~6× slower.

