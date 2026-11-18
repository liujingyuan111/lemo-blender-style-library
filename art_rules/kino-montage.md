# 构成主义蒙太奇 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/kino-montage/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`8c63deefda22d4677d286ddfffb243ce6385dfa7ab56fbc493705fe13908f204`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、12。

---

## 1. Essence, and what it is not

1. **Evidence, recut.** Every picture is real material (archive film, photographs, documents) about the actual subject. The film's argument comes from how they are cut and set, not from illustration.
2. **One printed sheet.** All material is converted to the same two-tone print (warm ink → paper); red is the only colour and is laid on top as a printed element.
3. **The beat is the editor.** Cuts, slams, wipes and counts sit on a 120 BPM grid (or the score's tempo); sections accelerate by halving shot length.
4. **Type is structure.** Words and numbers are beams: on a −18° band, as solid blocks, stacked vertically. Never floating captions.
5. **The collective over the individual.** Crowds, hands, machines and many small figures; a single face is never the protagonist.

Not **Data Storytelling** or a keynote: no centred headline with bullets, no slide transitions, no header bars; data appears as marked documents, counters and measured bars inside the composition. Not **Swiss Motion Graphics**: asymmetric, diagonal, no grid of white space, no thin rules as decoration. Not **Art Deco** or **60s Spy Titles**: no gold, no fine lines, no jazz. Not a museum slideshow: archive material is never shown "as is" in a neutral frame; it is cut, windowed, stacked and counted.

## 2. Materials & rendering

- **Four kinds of element only**: **bands** (red or ink, along the axis), **windows** (rectangles or parallelograms holding film or photographs), **cut-outs** (people scissored from photographs with a paper-white border), **type blocks**. Plus one paper-fibre texture over everything.
- **The print grade** (one function for film, photos and documents): luminance → percentile stretch (film: one pair of percentiles per clip, so it never pumps; 0.7 / 99.5; photos 0.8 / 99.4) → S-curve `x + s·(x−0.5)·(1−|2x−1|)·2`, s = 0.32 (documents 0.18, they keep their paper) → map to ink→paper: `rgb = INK + (PAPER − INK)·g`. Archive film keeps a ±2.5 % per-frame flicker inside its window (`hash(frame)`), photographs and documents do not.
- **Cut-outs**: a person-segmentation model (u2net_human_seg via onnxruntime) → threshold 0.5 → median filter → largest component → 7 px paper border dilated outside the mask. The border is the medium's own look and hides the model's edge errors. Group photos rarely segment cleanly: use them whole in windows.
- **Documents**: scans at full resolution, never retyped. They are marked: a red highlighter bar in `multiply` over the exact sentence, a hand-drawn red ellipse round a heading, a red circle on a map. Drawings on a document (a chart, a map) may be lifted off the page and reused, keyed from their paper (`alpha = (205 − luminance) / 90`).
- **Resolution ceiling**: archive film ≤ 2.5× its source pixels on screen, modern footage ≤ 1.5×, photos ≥ 1 source px per screen px where possible. Prepare clips with `hqdn3d → lanczos → light unsharp` before grading; add grain only in the mux. A 720-line film transfer can fill a 1,700 px window, not a full 1080p frame: frame it (a window, a split strip, an iris) instead of stretching it.
- **Paper fibre**: a fixed seeded noise canvas multiplied over the frame at α 0.5; film grain 4 added by `mux.sh`.

## 3. Colour logic

| Role | Value | Use |
|---|---|---|
| Red | `#D52B1E` | bands, wedges, blocks, the key number, marker bars, circles and leaders, the one winner in a comparison |
| Ink | `#141210` | type, beams under each floor, window borders, dark grounds |
| Paper | `#EDE4D0` | ground, reversed type, cut-out borders |

- Everything photographic is ink-on-paper; nothing else has colour. Red is never laid on red: a red block on a red ground becomes ink.
- Alternate grounds to make cuts land: paper scene → ink scene → paper. In an acceleration the background itself alternates red / ink per cut.

## 4. Type & subtitles

| Use | Face | Size (1080p) |
|---|---|---|
| Chinese display, slogans | Noto Sans SC 900 (subset) | 110–210 px; stacked vertically 170 px per character |
| Numbers, English display | Oswald 600–700 | numbers 230–440 px; English lines 30–62 px, letter-spacing 2–10 px, capitals |
| Source and footage tags | Space Mono Bold (CJK falls back to Noto) | 17–18 px on an ink or red tab, padding 6 |
| Subtitles | Noto Sans SC 700 40 px over Oswald 500 28 px | bottom left, ink bar at 90 %, a 10 px red tick |

- **Bilingual pairs**: Chinese block, then one English line in Oswald directly under it (or on the neighbouring band). Each language one line, measured.
- **Placement**: along the −18° axis on a band, or as an ink / red block; never centred on the frame, never a header. Numbers can be bigger than the words that explain them.
- **Tags**: every archive window carries its footage tag (`FILM · <TITLE> · <PLACE> <YEAR>`, `PHOTO · <AUTHOR> <YEAR>`), every fact a source tag (`来源 · <PUBLISHER> <YEAR>`). If the footage is not of the subject itself, the tag says what it really is.
- **Subtitles** stay bottom-left in a 960–1056 px strip; key type keeps above y 930 while narration runs. Subtitles hold ≥ max(1.8 s, speech + 0.6 s). On-screen text follows `readcheck.mjs` (CJK ÷ 4.5 + other ÷ 15 + 1.5 s, fully in frame); a comparison holds every item ≥ 2.5 s before its verdict.

## 12. Pitfalls of the medium

- **Upscaled archive film** turns to mush on a 1080p full frame: window it; split strips into panels; keep zooms inside the 2.5× ceiling.
- **Per-frame grading pumps**: one percentile pair per clip.
- **Type on a band running off frame**: place it from the band's centre line (point + normal), not by eye.
- **Red on red**: a red answer block on a red exposure ground disappears; switch it to ink.
- **A face as hero**: ordinary identifiable workers appear in groups, at work, in quick cuts; no slow motion or close-up protagonist.
- **Counters read as facts**: label only the end value and dated anchors; a caption beside a counter must match the number shown at every frame (stop the count on the caption's value while it is up).
- **A number without a unit**: every counter carries its unit in the same layout as elsewhere (小时 / 层 / 人 MEN).
- **Ink type over a window**: a line that runs past a photo's edge disappears into dark film; give it a paper tab or keep it clear of the window.
- **The verdict covering what was compared**: place it where no item is, after the hold.
- **Too many documents**: one marked sentence per document shot; a page with three highlights is a slide.
- **Short labels in an acceleration** fail reading time by design: keep text out of the 1/8-beat cuts; put the result in a held block after.
- **A hit at sample 0** overshoots in the AAC encode: fade the first 25 ms.

