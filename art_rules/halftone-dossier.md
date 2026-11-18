# 网点档案 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/halftone-dossier/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`6a3eb7919f286515674f7d544ee4124881491723615ba15ac13abc304f57f85d`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

- **The whole film is paper.** A warm cream sheet with low-frequency mottling, fine grain, a vignette and a fold; dark scenes are printed on it too, never glowing.
- **Shading is never a gradient**: it is halftone dots whose size follows a density field. Two or three dot layers at different screen angles overprint (multiply); that is the "printed" feel.
- **Bureaucratic apparatus**: case numbers, file chips, numbered exhibits, height charts, name plates, stamps. Their seriousness is the frame; the subject can be grave or trivial.
- **Loud but readable**: one idea per 2–4 s card, one big headline, one visual gag or exhibit, one caption line.

Not Risograph (no grainy two-ink riso texture as the whole look, no zine collage), not Swiss motion (no grid-driven kinetic type on white), not Rhythm Game Show (no candy sets, no rhythm-game rounds). Dots, paper and stamps must be visible in every frame.

## 2. Materials & rendering

- **Paper layer** (canvas, multiply over everything, built once): an upscaled random tile for mottling, per-pixel noise with a slight warm bias, a radial vignette, a faint centre fold.
- **Grain layer** (per frame): a few hundred paper-coloured specks and fewer ink specks, reseeded every 2 frames: dust on the print, not film grain.
- **Halftone**: a rotated grid of circles drawn as one path; step 20–26 px; screen angle different per layer; radius = density × step × k with k 0.6–0.72 (around 0.7 dots merge into solid ink). Density fields: radial (halos, blooms, corner glows), edge (dots crowding the frame border), linear ramps ("lit from above"). The second layer is multiplied so inks overprint.
- **Halftone-filled numerals and shapes**: a flat fill overprinted with a darker halftone clipped to the glyph; giant numerals may bleed off the frame.
- **Line boil**: turbulence displacement (small, ~5 px) reseeded ~10×/s plus a fine ink-grain mask that eats a little of every fill. Characters and hand-drawn props only; **never** on text, halftone, HUD or captions.
- **Characters**: chunky shapes with a heavy ink outline (~7 px), flat fills, a lighter belly or face area, glossy eyes (ink ellipse + two highlights) that can squint, blink or close into a happy arc. One head rig shared by all body poses.
- **Stamps**: a double rounded rectangle and bold text through a coarse ink-grain + displacement filter so edges are rough and the ink mottled; ~93 % opacity, tilted ±10°.
- **Props**: starbursts, speech bubbles, confetti, radial rays, sticky notes, folders, clocks: all flat fill + ink outline.

## 3. Colour logic

- **A paper ground, one dark ink, and four or five flat spot inks.** The dark ink (navy, black-brown or deep green) carries every outline, body text and the caption bar, and is the fade-out colour.
- One ink is the **overprint shadow** colour (misregistration offsets, caption shadows); one is the **highlight** for keywords and numerals; one warm red is reserved for stamps and alarms.
- Flat inks only. No gradients, no transparency ramps; tone comes from dot size and overprint.
- **Night or "secret" scenes** switch to a dark ink ground with a lighter dot layer of the same family, still multiplied by the paper.
- Characters may own one or two local colours (fur, clothing) that appear nowhere else.
- Example palettes: cream / navy / cobalt / hot pink / yellow / red; manila / sepia-black / teal / mustard / vermilion; off-white / forest green / tomato / sky / ochre.

## 4. Type & subtitles

- **Headlines**: a black-weight serif (e.g. Noto Serif SC 900 for CJK; a black slab for Latin), 100–230 px, left-aligned near the margin, with a **misregistration shadow** (+8/+8 px in the overprint ink, multiplied).
- **Display / numerals**: a fat rounded display face (e.g. Bagel Fat One) for names, big numbers, times.
- **Interjections**: a playful hand face (e.g. ZCOOL KuaiLe), paper fill with a thick ink stroke and an offset shadow.
- **Data / HUD**: a heavy monospace (e.g. JetBrains Mono 800) for case numbers, dates, rulers, file names.
- **Captions and stamps**: a black-weight sans.
- **Cards are the subtitles.** A headline per beat, plus a **caption bar**: a dark-ink rounded pill with an overprint-ink offset shadow, paper-coloured text, the **keyword in the highlight ink**. It pops in after the headline and holds ≥ max(1.8 s, speech + 0.6 s). With narration, the caption bar carries the spoken line.
- **HUD**: case number and a chapter chip top-left, a status (REC dot, date) top-right; colours invert on dark scenes.
- Latin runs 2–3× longer than CJK: smaller headlines, 1–2-word stamps (GUILTY, CLOSED), a tighter per-character stagger.

## 6. Camera grammar

A 2D camera group over a flat, frontal page. A vocabulary, not a route. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Locked frontal with a small beat pulse (~0.6 %) | the page as a poster, grooving | a title; a list; an accusation |
| Slow push-in (1 → 1.05–1.08) | scrutiny, rising tension | a profile; a summary before a verdict |
| Shake with quadratic decay (5–26 px) | impact | a stamp; a crash; a landing |
| Flash frames (white overlay ≤ 0.95 → 0, capped at 0.5 for big hits) | being photographed, a revelation | a mugshot; a verdict; evidence found |
| Pan across a pinned board | connection between exhibits | a timeline; suspects; a chain of events |
| Snap zoom into a halftone detail until dots are huge | "look closer" | a fingerprint; a signature; a number |
| Page turn / folder slide | next file, next chapter | a second case; a flashback |
| Pull back to reveal the whole desk | the file is one among many | scale; "this happens every day" |

Compose like a printed page: headline top-left, subject right-centre, caption bar bottom-centre, HUD in the corners. Transitions: dot wipe or hard cut; no dissolves.

## 9. Pitfalls of the medium

- **Fonts not loaded before layout** → per-character positions computed with a fallback font, glyphs overlap. Preload every family against the whole page source and the built text; runtime strings must use only characters that appear in the file. Use `font-display: block`.
- **Boil on text or dots** turns them to mush → filter only characters and props.
- **Clip-path ids are global** → every clipped numeral needs a unique id.
- **Time-windowed scenes** → an element invisible before its cue needs explicit opacity 0 for `t < t0`.
- **A dot wipe short of full coverage** at the cut shows the hard switch; make the max radius cover the grid cell's diagonal.
- **A 100 % white flash** reads as a dropped frame → cap at ~0.5.
- **Dots too small** (< ~14 px step at 1080p) alias into moiré after encoding.
- **Too many inks** lose the print feel → at most five plus paper.

