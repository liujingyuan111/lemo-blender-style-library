# 彩铅科普插画 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/colored-pencil/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`71d1970d26da38a4d6b0cbf4ce1f8ddd6462bece4f62107d7a2aa5ddb678c31d`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

- **The whole frame is one pencil drawing.** Sky, ground, soil, what lives in it and type are all pencil on the same paper; there is no "3D scene with a drawing in it". The sky is a loose blue wash with the clouds left as paper.
- **The cutaway is the signature composition.** Above the ground line, landscape; below it, the cut face of the soil, where the hidden things live (stones, burrows, seeds, pipes).
- **It is a real 3D world.** The camera can crane, push and truck through it, and things at different depths move at different speeds (multiplane parallax: the cut face slides over the far landscape).
- **Drawing is an event.** Every surface has a moment it is drawn; after that its four pencil layers arrive one after another, stroke by stroke.
- **Restraint.** One idea per shot, one visual focus, few labels. A science plate earns its clarity by leaving things out.

Not Watercolor (no washes, blooms or wet edges: every tone is built from strokes), not Urban Sketch (no ink line plus wash; the line is graphite and coloured pencil), not Crayon Picture Book (fine, controlled hatching, not waxy scribbles), not Isometric People Scene (perspective camera, a real cut face, depth).

## 2. Materials & rendering

- **Paper**: warm off-white with a tooth (fine grain, laid fibres, soft cockling). Pencil only lands on the raised tooth, which is where the colored-pencil grain comes from. The base mottling of blank paper is fixed to the screen.
- **Four pencil layers**, in this order, over every surface:
  1. **L0, side of the lead**: a soft broad fill in the local colour, tooth-limited.
  2. **L1, local colour hatching**: patches of short parallel strokes, each patch slightly re-angled; strokes follow the object (along stems, cables, trunks and blades; around stones and leaf clumps; a fixed diagonal for soil).
  3. **L2, cool cross-hatching**: in the shadows only, a darker and cooler version of the local colour, at another angle.
  4. **L3, accents**: deepest darks in sepia or indigo, a third angle.
- **Contour**: a graphite line from breaks in object id, depth and normal; the nearer surface owns the line; distant lines fade (aerial perspective).
- **Labels**: cream paper tags with a pencilled edge; the writing is graphite, written along the glyph skeletons stroke by stroke (never wiped on). Overlay marks share the paper tooth.
- **Pipeline (reference)**: three.js renders G-buffers (albedo + id, light + depth + normal, hatch direction, anchor coordinates + reveal time) at 2× and a post shader redraws them as pencil, then a 2× box downsample. See `demo/main.js`.

## 3. Colour logic

| Role | Colour |
|---|---|
| Paper (every blank area) | `#F8F4EA` |
| Grass and foliage | `#8DAA45` / `#5E8A3A` |
| Sky pencil | `#B3D4E6` |
| Soil: litter / topsoil / subsoil / weathered | `#4D3018` / `#66402A` / `#BD763B` / `#B38C5C` |
| Main buried structure (light) | `#DCB990` |
| Fine lines, highlights (white pencil) | `#FCFAF0` |
| Contour and writing (sepia graphite) | `#33241C` |

- Warm, restrained, paper-led. Bedrock is blue-grey, never large areas of black.
- **Accents carry meaning**, at most three in a film, each always meaning the same thing (say amber for warmth, cobalt for groundwater, red for one burrowing animal).
- **White pencil over dark** is how fine lines, highlights and anything delicate read on soil.

## 4. Type & subtitles

- One OFL handwriting face with a pencil feel (the demo uses LXGW WenKai, whose Latin comes from Klee One). English leads; one short Chinese line may follow.
- Labels in capitals on paper tags, at most one per shot; the Chinese at about 1.05× the English size, slightly lighter. A short pencil leader with a pale paper halo under it so it never reads as another line of the drawing.
- Titles are written in pencil on the sky, stroke by stroke, with a hand-drawn underline.
- Subtitles (when spoken): a cream paper slip, bottom left; Chinese over English, each one line; wiped on quickly (they are read, not drawn). Keep the subject out of that corner.

## 6. Camera grammar

- **Sink**: a vertical crane from the landscape into the cut face; the soil rises over the far view.
- **The magnifier**: a pencil circle drawn around a detail; inside it, the magnified view is drawn from blank paper outward from the centre; the circle grows to fill the frame. The reverse (the circle shrinking to a point in a wider view, then erased) returns. This is how the style changes scale, and it re-anchors the strokes at the new scale.
- **Focus is how fully something is drawn.** No optical blur: the subject gets all four layers and a firm line; what is behind keeps one light wash and a faint line. A focus pull moves "fully drawn" from one thing to another.
- **Inside the magnifier, draw only what the shot is about**; illustrators leave things out.
- **Follow**: a truck alongside a moving particle, which sits left of centre with space ahead.
- The orientation stays fixed inside a shot group; to turn, change scale or cut through a magnifier.

## 9. Pitfalls of the medium

- Hatching fixed to the screen while things slide under it ("through glass"), or re-randomised every frame (the whole screen flickers).
- Rotating the camera inside a shot group: the anchored strokes stretch. Turn by changing scale or cutting.
- Square noise cells as soil grit; grains must be round.
- Blank paper left "waiting" for more than about a second, with no drawing front moving: it reads as a bug.
- Growing tips that start as white sticks on dark soil: grow them already coloured.
- Too many labels, rulers and arrows: the plate turns into a worksheet. One label per shot.
- 3D-render tells: translucency, glow, bloom, depth-of-field blur, drop shadows on type.
- Lines thinner than about 1.5 px in a wide shot shimmer: thicken them for wide views, keep the finest for close-ups.

