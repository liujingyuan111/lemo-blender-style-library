# 复古版画拼贴 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/vintage-collage/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`9ae3f52c26a6d5e21315a9a73b82694bd29ea04f47c1c60482583eb5bebe0a6f`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

- **Real printed matter, cut by hand.** Every figure is a cut-out of a real public-domain print (an engraving, a stamp, a news photo, a line drawing), with a slightly rough white paper margin around it. Nothing is drawn in a vector or 3D way to look printed.
- **Flat torn colour behind it.** Large torn sheets of a few flat colours (teal sky, ochre disc, mustard sun, cream strips, paper clouds) make the space; their edges show a white fibre fringe.
- **It is paper on a table.** Every piece has a thickness (a 1–1.5 px cut edge), a shadow from a top-left light that grows softer and further as the piece lifts, and a paper back that shows when it turns over. The table is old paper, visible at the edges.
- **Cut-out motion.** Pieces slide in, overshoot and settle, drop and bounce, swing on a pin, turn over, get cut and scatter, stepped on twos. Nothing scales or rotates smoothly like software.
- **Our own addition: the data engraving.** Charts are engraved, not plotted: parallel lines whose width follows the value (the copperplate swelling line), cross-hatching at the peaks, a thin ochre wash, double-rule axes, torn breaks for broken scales.

Not Halftone Dossier (that one is a case file of documents; here the printed matter is cut free and performs), not Woodcut Print or Copperplate Engraving (we never re-engrave the whole frame; engravings arrive as found pieces), not Paper Pop-up Book (no 3D folds or depth stages), not a scrapbook slideshow (pieces move as puppets, the camera moves over a table).

## 2. Materials & rendering

- **Cut-outs**: a scan, a hand-traced or computed mask, the scan's grey turned into ink amount on a cream card, a white margin dilated around the mask with a slightly torn edge. Line art with a transparent ground gets its silhouette by closing and filling holes. Hand-colour (brass, mustard) only inside the cut, never as a gradient.
- **Separated plates**: a two-colour print (a poster, a label) is split into its ink plates by hue and re-inked in the palette; each plate can then be printed, shifted or turned on its own. Upscale before tightening the ink edge so lines stay crisp.
- **Torn colour papers**: flat colour with a faint mottle, the edge displaced by fractal noise, a thin white fibre fringe outside it.
- **Old paper**: a mottled cream base with fibres and faint foxing, lighter than a raw scan; it can be tiled with mirrored copies, so the table extends without seams.
- **Halftone**: any photograph enters as a 45° dot-screen news clipping on newsprint, torn edges, a typed caption.
- **Paper physics in the composite**: under each piece a cut-edge copy in a darker paper colour, offset down-right; two pre-blurred shadows mixed by height; the back side is paper colour with about 10 % of the mirrored ink showing through.
- **Bake, then move**: the heavy work (masks, separations, tearing, textures, engraving, halftone, typed slips) is baked once into sprites; the page only moves sprites. Grain is added in the mux, not drawn.

## 3. Colour logic

- A restrained palette of six: old paper, cream card, warm black ink, ochre red, teal, mustard. Large areas are paper and flat colour; heavy black is limited to engraved lines, small slips and silhouettes.
- A printed subject keeps its own inks, re-inked once into two tones close to the palette (for a two-colour poster: its red and its black), and only the subject uses them.
- One colour carries meaning per film beyond decoration (ochre for the data wash and one key figure, mustard for the slip that names it); flat colour papers are scenery.
- Example (our demo): paper #ECDFC2, card #F6EEDB, ink #221C17, ochre #C65F3A, teal #2F7F7A, mustard #E1AB3B; subject inks #C8463F and #2F5D8C; cut edge #B49D78, paper back #E9DFC8.

## 4. Type & subtitles

- All type is printed on its own slip of paper and placed like any other piece: no type floats on the frame, no outlines or drop shadows on letters, only the slip's shadow.
- Faces with a period feel, all OFL: an old-style serif (e.g. IM FELL English roman, italic and small caps) for titles and labels; a typewriter (e.g. Courier Prime) for slips, receipts and data; a CJK serif (e.g. Noto Serif SC, subset) for Chinese.
- **Ransom letters** for a hero word or number: one slip per character, rotating fonts, papers and inks, slapped in one per eighth note. Old-style serifs have old-style figures (1 like I, 0 like o): digits come from a lining face.
- **Typewriter slips** type out letter by letter on a blank slip (monospace advance), with a key sound per letter.
- On screen: Chinese ≥ 34 px, English labels ≥ 24 px, data numbers large enough to read at the widest framing they appear in.
- **Subtitles** (when there is a voice): two slips stacked at the bottom left, a black newsprint slip with the Chinese line (about 40 px) over a cream typewriter slip with the English line (about 30 px) typing out. One line per language, split long lines into two cues. Keep that corner (about 1100 × 180 px) free of anything the viewer must see.
- Comparisons and verdicts: every compared item fully in frame and held ≥ 2.5 s.

## 6. Camera grammar

A rostrum camera over a paper table: 2D only, but it can push, pull, pan, rise and tilt across a table much larger than the frame.

- Wide establishing on the assembled collage; follow a moving piece; push to read a detail; pull back for scale.
- **Through a shape**: push into a hole in the paper (an oval frame, a window, an empty album slot) and the next scene is already inside it.
- **Whip pan** sideways along the table, a paper seam between the two scenes.
- **Match cuts** on the same piece at a new size; match on action (a piece leaves the top of frame, enters the next shot from below).
- **Rise** along a growing data engraving, then pull back so the whole comparison is in frame.
- Keep the view on the paper: zoom ≥ 1 on a single-sheet table, or tile the table for wide pulls.

## 9. Pitfalls of the medium

- A cut-out without a margin or shadow reads as a digital sticker; one with a fat, even margin reads as a sticker too. Keep the margin thin and slightly torn.
- Shadows from different light directions, or shadows that do not change with height, flatten the table.
- Smooth scaling, fades and easing curves that never overshoot read as software, not paper.
- Too many pieces: one subject per frame, about twenty flying pieces at most, leave the bottom-left free for subtitles.
- Upscaled scans go soft and blotchy: separate and tighten the ink, use the largest public-domain scan, and keep cut-outs at or below their source size where possible.
- Old-style serif figures in numbers, letters with outlines or glows, system fonts.
- Copyrighted or "no known restrictions" images: only public domain and CC0 prints, each one in the credits.

