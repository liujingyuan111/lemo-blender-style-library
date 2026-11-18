# 红色窗花剪纸 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/papercut-red/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`65e317d83335e0cb34696b643e31ad9e46fb0bb93fd748c2e21d74358aea61ec`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

Every visible thing is **a piece of paper that was cut with scissors** and laid flat on another sheet. There is no painting, no gradient shading, no outline stroke: detail, volume and expression come only from **what was cut away**. Red paper is the hero material; grounds are paper too (a light paper by day, a deep dyed paper by night). Characters are **jointed cut-outs** (head, torso, upper and lower limbs pinned at rivets) animated in hard 12 fps steps.

Not shadow puppetry: no light behind a screen, no translucent dyed hide, no rods. Here the paper is **front-lit and opaque**; backlight is a special event you save for the moment that needs it. Not flat vector art (no strokes, no gradients), not a silhouette film (every shape's interior is cut).

## 2. Materials & rendering

- **Paper grain:** a neutral-grey texture in `soft-light` inside each piece (dye mottling, fibres, specks), then the piece's alpha restored with `destination-in`, so holes stay holes.
- **Cut edge:** every silhouette is a polyline with a slight low-frequency wobble (hand-cut), a 1 px light rim upper-left and a dark rim lower-right (the cut face). Architecture and machines use straight segments + wobble, never smoothing.
- **Paper thickness:** each piece casts a tight soft shadow on the layer below; stacked folded paper shows 2–6 offset darker edges.
- **Figures: red block + yin lines.** Every figure piece gets an **inset contour** (a thin slit a few units inside the outline): the classic double outline, which also separates red-on-red overlaps (an arm over a coat).
- **Folk cutting vocabulary** (`demo/motifs.js`): sawtooth rows (fur, grass, tiles, fringe), serrated edges, crescents (scales, quilting), swirls (joints), clouds, rosettes, plum, coin, tapered slits.
- **No floating islands.** A closed ring cut would drop its centre out of real paper. Eyes are two crescents (upper and lower lid) that leave bridges, plus a pupil *hole*.
- Faces never morph: expressions are **swappable face pieces** (smile, surprise, fear, determined, asleep).
- **The rosette (团花)** is designed as one 45° wedge and mirrored 8× (D4); other folds give 2×, 4× or 6×. Alternate rings of *yang* cut (band cut away, red lines left) and *yin* cut (lines cut out of a red field). Fold seams leave faint crease lines: keep them, they are true to the craft.
- **Light:** front-lit scenes use the paper as is. Night: `frame × lightmap` + warm pools, then **emissive** backlit pieces (light × paper transmission via `multiply`; holes at full light), a two-level bloom and optional rays. Keep bloom low enough that the pattern stays legible at the centre.
- **Projected pattern:** a piece's hole mask, squashed onto the ground and added with `lighter`; on a character, masked by its layer alpha over a solid warm spot, so cut features still read as holes.

## 3. Colour logic

- **China red** (around `#d2201f`, range `#c8102e`–`#d7261e`) is the hero material. Depth and role are shown by **paper tones one step apart**, not by shading: near pieces one step brighter, far pieces one step darker, an antagonist or a heavy object one step deeper.
- **Ground and hero must be different paper families.** If background and hero are both red, the silhouettes stop popping. At night, all background layers are one dark dyed family and only the pieces that matter to the story are red; by day, a light paper ground with red and pale-red layers.
- **Gold foil** is an accent kept for one late moment (a sun, a title, a coin); never a second main colour.
- Examples of ground families: indigo night papers (far layers lighter blue, near darker); a warm rice-paper day with pale-red far hills; a jade-green or black paper for a story that isn't festive. Choose from the topic.

## 4. Type & subtitles

- **Subtitles are a paper strip in the world**, e.g. a red banner (横批) darker than the picture's reds so cream text holds, serrated edges, swallow-tail ends; a sturdy OFL serif (e.g. Fraunces SemiBold) around 44 px, low, with a paper shadow. It drops in on two 12 fps steps, like a couplet being pasted. Hold ≥ max(1.8 s, speech + 0.7 s); never overlap.
- **Titles** are cut-out letters (*yang*-cut, counters are real holes) popping in letter by letter on 12 fps steps, with sawtooth border strips and a seal cut by code.
- Small credits may be printed ink on paper.

## 6. Camera grammar

A vocabulary, not a route. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Extreme close-up tracking the scissor tip | making; attention to craft | a beginning of work; a precise act; a signature |
| Flat front view, locked | the cut-out as an emblem | a title; a statement; a family portrait |
| Slow pan across paper layers (parallax) | a world laid out | a village, a route, a timeline |
| Low wide, a shape standing up from the ground layer | scale, threat | a storm; a rival; a deadline arriving |
| Top-down tabletop | the craft as plot | folding, cutting, assembling, sorting |
| Push toward a lit piece, pull back to many | one act spreading | influence; a network lighting up |
| Page turn / sheet peel | time or place changing | day to night; before and after; chapters |
| Pull back to an object in a room | the film was a thing someone made | memory; a gift; a tradition |
| Rotation around a rosette's centre | order, repetition | a cycle; a team |

Framing: layers stay parallel to the screen; depth comes from parallax and paper tones, never from perspective. Transitions are paper actions (fold, page turn, peel, a sheet flying off, a cut through the frame); no dissolves.

## 9. Pitfalls of the medium

- **Red on red** reads as one blob → different ground family, near/far paper tones, inset contours for overlaps.
- **Darkening a layer through the light map** also darkens what covers it → tint the layer itself (multiply + restore alpha).
- **A flat cos-squashed flap reads as a sliding card**, not a fold → strips with fake perspective, darken as it stands up, show the back colour.
- **Cut reveal shows the uncut stack through the holes** → stack thickness inside the "uncut" mask only; the cut part gets its own offset copies.
- Scissors pointing backwards → the blade axis follows the direction of travel, the rivet a little behind the cutting point.
- Blank frames between shots → overlap outgoing and incoming paper actions.
- Engine traps (`put()` transforms, piece boxes, test pages) are in DEMO.md build notes.

