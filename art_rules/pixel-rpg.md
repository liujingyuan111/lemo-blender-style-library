# 16-bit 像素 RPG · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/pixel-rpg/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`6624481152a77960b54bc3c0d2f2f9de6af15d4e95294525ef8e3635fe479fe5`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

- **320×180 native pixels**, scaled ×6 nearest-neighbour to 1080p; everything, text included, lives in the framebuffer.
- **A limited, indexed palette**; gradients are **ordered dither**, never blends.
- **Sprites** around 20–34 px tall animating in a handful of frames; faces act in **portraits**.
- **Story told the way a game tells it**: dialog boxes with portraits, menus, status bars, battle messages, save files, item fanfares.
- It takes the game's systems seriously as a language for feeling.

Not 2.5D Pixel Art (no depth of field, bloom or real-time light), not CRT nostalgia (no scanlines, no grain), not a parody.

## 2. Materials & rendering

- **Indexed framebuffer** (`Uint8Array` of palette indices) presented through a **lookup table** (index → RGB), so a whole palette can change in one frame. Camera moves are **integer pixels**; each parallax layer rounds its own offset.
- **Master palette** of ~32 colours (a free palette such as ENDESGA-32), plus **protected duplicates** of a few indices that no palette effect touches.
- **Colour-depth tables** computed from the master palette: identity (16-bit), nearest of ~15 NES-like colours (8-bit; it needs a dark green and a dark brown), 4 fixed luminance thresholds (4-colour, drawn natively at 160×90 and doubled), a faded set (`lum^0.8` → ~7 blue-greys), and intermediate subsets for step-by-step collapse. Map by luminance, never by rank.
- **Light is index stepping**: `LIGHT[]` / `DARK[]` tables move each index one step along its ramp; glows are Bayer-thresholded rings. Firelight in a low-colour era uses a warm remap (greens → browns → rust), not generic brightening.
- **Dither**: 4×4 Bayer for gradients and glows; light shafts as a flat 50 % checker with a 25 % edge.
- **Sprites from a rig**: capsule limbs with 3-tone shading from an upper-left light, a per-part inner line in the material's darkest tone, a global 1-px ink outline, plus hand-placed ASCII heads. One rig gives every pose; lower eras drop the highlight tone. Give the hero a **silhouette mark** (a garment tail, a hat, a hairstyle).
- **Portraits** 32×32, 3/4 view, base face + eye/brow and mouth overlays; they carry facial acting (the sprite face has one eye pixel).
- **Props** can be flat-shaded 3D shapes quantised to a few protected indices (e.g. a rotating crystal at 8 frames per 90°).

## 3. Colour logic

- **Palette = feeling.** Colour depth, fades and swaps are story tools; change the whole palette by table, never by alpha.
- **Colour depth can stand for time**: older = fewer colours, lower resolution.
- **Protected indices**: a few colours exempt from every effect become the thread through the film and allow match cuts between eras. Use one or two; more and they stop meaning anything.
- **Warm hues survive reductions**: keep orange, pink and plum in reduced subsets, or the first step turns a scene solid red.
- Example uses of protected colours: a red kite across a childhood; a gold coin in a grey economy; the green of one plant in a faded city.

## 4. Type & subtitles

- **The dialog box is the subtitle**, drawn in the framebuffer at the bottom quarter: a layered rounded border (ink / white / silver), a dithered dark-blue fill, a 32×32 portrait on the left, an **original** variable-width pixel font (cap ~7 px) with a 1-px shadow. It types with the voice (~38–40 chars/s; slower in older eras), ▼ blinks when done.
- **Skins follow the era** (light box for 4-colour, black box with white frame for 8-bit, blue for 16-bit).
- Battle and system messages go in a thin top window. Every box stays ≥ max(1.8 s, speech + 0.6 s); the next box cuts the previous one. Export the `.srt` from the same subtitle array.
- Titles in the pixel font at 2×, 8-neighbour ink outline, row-by-row gradient, Bayer-dissolved in and out.

## 6. Camera grammar

A vocabulary, not a route. Game cameras are simple and legible. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Side-scroll with parallax layers | journey; loneliness; progress | a commute; a quest; a timeline |
| Locked frame with UI on one third | a choice; a system speaking | a menu decision; a stats reveal |
| Battle side view (enemy / party / windows) | conflict as a system | an exam; a negotiation; an illness |
| Top-down overworld pan | the whole world; where things are | a city; a map of a company; a trip |
| Integer-pixel tilt up something tall | awe; scale | a tower; a door; a mountain |
| Hold while the palette changes | loss or change without motion | grief; a memory fading; nightfall |
| Back view at a threshold | resolve; the unknown ahead | a first day; a launch; a departure |
| Zoom by mosaic into a thumbnail | entering a memory or a file | a flashback; a save slot; a photo |

Framing: characters stay above the dialog box (floor line above its top edge); menus leave the action visible.

## 9. Pitfalls of the medium

- Rank-based palette mapping crushes a scene to black → map by luminance with a gamma.
- Reduced subsets without warm hues turn a sunset solid red → keep warm hues.
- An 8-bit set without dark green or brown turns night grass blue; generic brightening near fire turns grass neon → warm remap.
- Post-quantising a full-colour scene to 4 shades is mud → draw low eras natively with known indices at half resolution.
- Pixel hair as a smooth dome reads as a helmet; single-pixel alternation reads as noise → 2–3 big spikes. Pale clothing reads as skin. Held props cross the face in side view → back hand.
- A dark plank door reads as a jail → panels, bevels, studs.
- Negative modulo indexes `undefined` → `((n % m) + m) % m`.
- The dialog box covers the bottom quarter → keep the floor line above it.
- Match cuts on protected colours need both screen positions computed.

