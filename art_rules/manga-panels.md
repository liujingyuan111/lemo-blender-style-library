# 黑白漫画分格 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/manga-panels/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`5c53e55bce2df67d6c9cea3f12f559e4b92216b325be6581852ddf35dc0c0da8`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、10、11。

---

## 1. Essence, and what it is not

Three things make it read as a printed manga page and not as an illustration:
- **Only ink and paper.** Every grey is a pattern of black dots or lines (screentone), never a continuous grey or a gradient.
- **The panel is the unit of time.** A new panel inking in *is* the cut; panels open in reading order (right → left, top → bottom) on the beat.
- **Lettering is drawn, not typed.** Sound effects are big, rotated, outlined and boiling; narration lives in boxes, speech in balloons.

One spot colour (by default a vermilion; a user's brand colour can take its place) is allowed for one subject only; everything else is black and white. The subject comes from the film's topic: a product, a character's one item, a symbol of the story. Not an American comic (no CMYK process dots, no colour plates, no left-to-right page), not a pencil sketch (lines are inked, crisp, tapered), not a greyscale photo filter (no smooth greys anywhere).

## 2. Materials & rendering

- **Paper** `#F3F0E8` (warm, never pure white), **ink** `#121212`. A 512 px grey-noise grain multiplied at 10 % over every frame.
- **Ink line**: G-pen look — crisp lines that taper at both ends, thick contours, thin interior detail, solid spot blacks in hair and deep shadow, fine parallel hatching for form. Generated art is drawn this way (see §9) and only re-printed by code, never re-drawn.
- **Screentone from generated art** (`tools/prep.py`): detail areas (high local variance: lines, hatching) are hard-thresholded; flat areas (low variance) become a 45° AM dot screen (cell 6–9 px at display size, coverage capped at 62 %, above 84 % solid black). Scale every image to the size it will be **shown** before screening, and make a small, coarse-celled copy (cell 4, ~640 px wide) for anything shown small; otherwise the dots blur into grey. Real black stays solid.
- **Code tone**: dot gradients (`tone(key, w, h, fn, cell)`, coverage as a function of panel u, v) and line tone (`lineTone`, parallel lines whose width follows coverage), cached per key. Use dot gradients for sky, depth and emotion backgrounds; line tone for speed, shadow and the book spine.
- **Panel border**: 7 px solid ink with mitred corners at 1080p, gutters 18–40 px, at least one edge slanted 1–6° on most panels (shōnen energy). A dashed border means an *empty* panel, still to be filled.
- **白フチ (paper rim)**: a figure or product that breaks out of its panel gets a 12 px paper outline plus a 3 px ink outline (`halo()`, pre-composited once from the keyed image's silhouette).
- **Spot colour** `#F03C1E` is printed flat with ink dots on top for its shadows (the red area of the source image keyed by red dominance). The colour is written in two places, `ACC` in `demo/kit.js` (what the code draws) and `ACC` in `demo/tools/prep.py` (what the drawings are printed with): change both together.

## 3. Colour logic

| Name | Value | Use |
|---|---|---|
| PAPER | `#F3F0E8` | page, gutters, rims, white-out light |
| INK | `#121212` | line, solid black, every dot |
| ACC | `#F03C1E` (default) | the one spot colour; swap for the user's brand colour if they have one, keep it saturated and alone |

- The spot colour belongs to one subject and the graphics that speak for it (for example: a product's shell and the tags that point at it, a character's scarf, the key object of the story, a brand underline). Characters, backgrounds, lettering and effect lines stay black and white, or the page turns into a colour comic.
- Light is drawn by **removing** tone (white-out wedges, white stars with an ink edge), never by adding grey.
- Impact frames invert paper and ink for 2 frames.

## 4. Type & lettering

- **Sound effects** (katakana, Dela Gothic One): per letter — 1.6–1.9× → 1× slam with overshoot, 0.03–0.09 s stagger, ±10° random rotation, small offsets, three layers (wide ink stroke ×0.34, paper stroke ×0.27, ink fill), boiling ±1.5 px at 12 fps. Small kana (ッ ャ) at 0.62× and dropped. Dela's 「カ」 reads as 「太」 at small sizes: use another word (ドンッ rather than カンッ for a hit).
- **Narration boxes** (Noto Serif SC 900, vertical, right column first, a space starts a new column): paper box, 5 px ink border, offset solid ink shadow, characters ink in one after another. Inner voice, scene-setting, verse lyrics.
- **Hand-lettered shouts** (Noto Sans SC 900, 110–190 px): the same slam engine as the sound effects, horizontal or vertical. Choruses, slogans, anything shouted.
- **Speech balloons** (Noto Serif SC 900, vertical): ellipse with a tail toward the speaker's mouth; full-width comma becomes the vertical form.
- **Small Latin lines** (Barlow Condensed 800, slanted; 600 for the smallest): one English line under a Chinese title, brand line or colophon.
- **A film in a language written in rows** (English, for example): narration boxes and speech balloons are set in horizontal lines, in a heavy serif of that script; shouts in a heavy sans. Boxes, borders, shadows, strokes, the slam and the timings stay as above, and so do the katakana sound effects.
- All Chinese and Japanese fonts are subset to the glyphs used (`tools/fonts.sh`); load every weight before the first frame.

## 6. Camera grammar

A vocabulary, not a route. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Pan along the reading direction across a page wider than the frame | following, chasing | a run; a queue; a process |
| Push into a point inside a panel (an eye, a keyhole), then cut on an impact frame | entering the next thought | a decision; a flashback; a zoom into detail |
| Glide through the gutters from panel to panel, one beat each | a series, a collection | a day in photos; steps of a recipe; a team roster |
| Pull back from one panel to the whole page | the moment becomes part of a story | an ending; a reveal of scale |
| Static frame while the panels change around it | the grid itself is the action | bursts, comparisons, countdowns |
| Slow push on a single big panel with emotional tone | feeling, a held breath | a smile; a memory; a result |
| A panel splitting along a slanted gutter | a page giving way to the next | a chapter break; a change of place |

No page-turn transitions. The one legitimate page turn is a flip book, where turning pages *is* the animation.

## 10. Consistency checks

- Fix each character's silhouette-defining features (hair shape, the jacket, a bag) and repeat them in every prompt.
- Look at every generated image at the size it will be shown, screened: the prop must keep the same parts in the same places (for headphones, say: the logo on the left cup, the hinge at the same height on both sides, the cable on the right).
- The spot colour may appear only on the prop's one material; reject an image where it leaks onto clothes or the background.

## 11. Pitfalls of the medium

- Grey creeping in (alpha over tone, smooth gradients, a toned image drawn semi-transparent) → every grey must be dots or lines; fade by wiping, not by alpha.
- Dots turning into mush when an image is shown small → screen at display size; keep a coarse small copy.
- Spot colour spreading to clothes, lettering or effects → one subject only.
- Lettering inner counters filling with ink → paper stroke ≥ 0.27 × size, ink stroke only slightly wider (0.34).
- Sound effects and lyrics fighting for the same corner → plan lettering positions per shot; lyrics never cover the face.
- Text inside the camera transform getting blurry or cut off on a push → set readable lines in screen space.
- A panel holding still for more than a beat → add an in-panel action (boil, slide, sweat, sparkle) or a new panel.
- Page-turn transitions → don't; push into a point, split along a gutter, or cut on an impact frame.

