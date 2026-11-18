# 60s 间谍片头 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/spy-titles/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`ea6e9e9073af43ef0bb860e368f60b16ec32a91668386115a142907d92cb1f75`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

- **Flat, opaque inks on paper**: four colours, no gradients.
- **Hand-cut edges** on every shape; pieces layered with cut gaps and small paper shadows.
- **Abstraction down to silhouettes**: figures in profile, all acting in outline and timing.
- **Typography is the picture's structure**: credits are architecture, props, vehicles.
- **Music cuts the picture**: brass stabs are edit points.
- A title sequence is a story in itself: one goal, a few locations, one reveal.

Not flat vector motion graphics (the edges are cut, the paper is physical), not a halftone print style (no dots), not a Swiss grid (diagonals, jaunty type, playful), not a spy parody with gadgets and gun barrels.

## 2. Materials & rendering

- **Scissor-cut edges**: every polygon resampled every ~9–10 px and displaced along its normal by low-frequency noise (amp ~1.2–2.2 px, larger for bigger shapes) plus a rare 1–2 px notch. **Cut the edge once in the piece's local space and cache it**, so a moving cutout keeps the same edge, exactly like real cutout animation (screen-space edges crawl).
- **Paper layering**: separate pieces are separated by a ~2.4 px cut gap in the ground colour and cast a small paper shadow (offset a few px, blur ~5, alpha ~0.3). Whole figures get the gap as an outline, so a black figure reads in front of a black letter.
- **Paper texture**: one full-frame texture multiplied on top (mottling + faint fibres), a sparse "ink void" speckle on dark ink, faint squeegee streaks; film grain in the mux (~6).
- **Silhouette figures**: tall stylised adults (~7 heads), identity by hat, coat cut, shoes and **one colour accent** that doubles as a motion indicator (a tie or scarf streaming back when running). Pieces **merge into one outline** inside the figure, with only thin slits at shoulder, elbow, hip and knee. Hands are sharp wedges; no faces except an eye slit in close-ups.
- **The object of the chase** sits on a black backing (an ink keyline) so it reads on any ground; it is the brightest thing in frame.
- **Type**: a condensed OFL display face (e.g. League Gothic) for credits, glyph outlines extracted (opentype.js) and **re-cut** per letter (edge noise, ±0.8° rotation, ±1.5 px baseline jitter). A title in custom geometric cut glyphs (straight cuts + arcs, uneven weights, staggered baselines), never a real title's lettering.

## 3. Colour logic

- **Four inks**: ink black, paper cream, one hot colour, one warm secondary. Darker "shadow paper" variants of those inks only for depth.
- **One dominant ground colour per scene**, changing with the location; figures and type in the other inks.
- The hot colour is reserved for one accent on the hero and for danger; the secondary marks the object of the chase.
- Background props go in a darker version of the ground, never in black, or they read as letters.
- Examples: black `#1b1714` / cream `#efe4c9` / red `#d23a22` / mustard `#e2a52a`; ink `#161a22` / bone `#ece6d6` / teal `#1f8a8a` / orange `#f07a28`; black / pale pink `#f3d6cc` / cobalt `#2a46b8` / lemon `#f0d23a`.

## 4. Type & subtitles

- **Credits live in the set**, never in the subtitle band: one line per location, fully readable at some moment. Credits are fictional roles only, never real people's names.
- **Subtitles** on a narrow paper strip (scissor-cut ends, slightly tilted) bottom-left, a small glyph from the film as bullet, a geometric OFL sans (e.g. League Spartan 600, ~44 px). Light strip on dark scenes, dark strip on light scenes; slides in from the left in ~0.18 s. Hold ≥ max(1.8 s, speech + 0.6 s).
- Hold each credit long enough to read alongside a subtitle.

## 6. Camera grammar

A vocabulary, not a route. Graphic, flat, decisive. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Wide on a full credit line, then truck in | reading, then action | any location built from type |
| Lateral tracking, one screen direction | pursuit; momentum | a chase; a race; a delivery |
| Hard cut on a brass stab | punch; a new location | montage; a reveal; a gag |
| Graphic match cut (same shape, same position) | rhyme; acceleration | wheel → coin → pupil → moon |
| Locked single shape on a flat ground | mystery; an icon | a cold open; a clue; a logo |
| Silhouette against a giant circle | the hero moment | a catch; a triumph; a stand-off |
| Diagonal split into a grid | fragmentation; many at once | a split screen; a conspiracy; a team |
| Vertical pan down a column of type | descent; a list | a building; a roster; a countdown |
| Push into a letter until it fills frame | a letter becomes a place | a door; a tunnel; a window |

Framing: strong diagonals (~30°), big flat grounds, figures small against type. Match cuts keep circle centres and sizes identical across the cut. No dissolves.

## 9. Pitfalls of the medium

- Every internal piece outlined with a gap looks like a mannequin diagram → merge pieces in an offscreen layer, cut only joint slits (`destination-out`), outline the whole figure.
- A `clear()` that resets the transform silently kills the camera.
- A figure fully hidden behind a letter reads as "nobody there" → let hat, nose and accent stick out. A stiff streamer reads as a tongue → multi-segment ribbon with a travelling sine.
- A credit only ever seen partially is uncomfortable → always open wide on the full line.
- Black background props read as letters → darker ground colour.
- An object in the same ink as its ground vanishes → black backing.
- Circular props dropped into a word cover neighbouring letters → lay the word out around a gap.
- Match cuts fail if circle centres move across the cut.
- Flat inks + grain make huge files at low CRF → a higher CRF looks the same.

