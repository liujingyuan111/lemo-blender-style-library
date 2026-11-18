# 视觉调查 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/visual-investigation/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`8f4bab46692ba0a24e0c416b96ef3045aa107dc63e171e5164a43d7bb0324337`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

1. **Sources meet at one moment.** The payoff of every section is two or more independent sources (a frame, a photo, a testimony, a report line, a sound) pointing at the same place or the same second. Cut points are sync points.
2. **One clock, read in the picture.** Time is carried by large readouts that belong to the layout: the timestamp on each telegram card, a playhead with its clock on the data chart, a `T+xx.x` stopwatch over the decisive seconds, a frozen "32 s". The scale changes with the story (hours → minutes → seconds → days) at section cuts. A permanent timeline band under every shot is **optional and usually wrong**: it eats the bottom of the frame, adds a layer of small labels and goes empty once the story leaves the clock.
3. **One finding per layout.** Each section says one thing; a heading is part of the layout, never a page header.
4. **Uncertainty is drawn, not apologised for.** `≈`, *inferred*, *schematic*, dashed boxes. Known and unknown are separate columns. A source that does not cover a stretch simply is not on screen yet (it lights up late in its column); never an empty "no footage" box, which reads as a broken render.
5. **Restraint.** Real disasters and real people: no slow motion of the catastrophe, no music that tells you to feel; fire only inside evidence frames; casualties as counted dots and numbers.

Not **Satellite Briefing** (no orbital imagery, no zoom from space). Not **Archive Light Table** (no paper on glass, loupes or hands: documents are flat evidence frames). Not **Halftone Dossier** (no print texture, stamps or collage). Not a newsreel package (no channel bug, ticker or anchor voice). Not a keynote: no centred title slides, no page turns.

## 2. Materials & rendering

- **Three kinds of source at least**: moving image (newsreel, CCTV, phone video, launch camera), documents (testimony, memo, telegram/teletype, report page), photographs. Add sound (original commentary, radio, recordings), data (weather, telemetry, counts) and maps whenever they exist.
- **Documents**: a scanned page is shown as a strip or a page, never re-drawn; only the decisive line is highlighted (red, `multiply`, α ≈ 0.6, wiped left to right). Text that exists only as a transcription (a report, radiograms) is re-typeset by code and labelled as a transcription.
- **Archival picture pipeline** (pre-1950 film, max ≈ 2.5×): deinterlace (`bwdif=0`) → crop borders → deblock (`hqdn3d=2:2:3:3`) → lanczos upscale → light unsharp (`5:5:0.5`) → greyscale; one grain for everything. Modern footage: ≤ 1.5×. Never colourised or "restored" copies.
- **One grade** (canvas `ctx.filter`): footage and photos `grayscale(1) contrast(1.22) brightness(0.94)`; paper `grayscale(1) contrast(1.05) brightness(0.86)` (white pages pressed to light grey); maps greyscale, inverted, `brightness(.62)` so they read as dark line drawings.
- **One grain**: six 256² Gaussian tiles rotated per frame, `overlay`, α 0.22 on footage/photos, 0.10 on paper. Grain only on sources, never on type or lines (`mux.sh … 0`).
- **Drawn evidence** (plan, side schematic, charts, dot matrix) is thin line work on the panel colour, marked *schematic* when it is not measured.
- Remove channel bugs, watermarks and the source's own title cards; never generate an image to stand in for a historical one.

## 3. Colour logic

| Use | Value |
|---|---|
| Ground | `#0B0C0E` |
| Panels | `#141619` |
| Hairlines, frames | `#2E3238` |
| Text | `#ECEAE4` |
| Secondary text | `#8B9097` |
| Ticks, *uncertain* | `#4A4F57` |
| **The one accent: here / now / match** | `#FF4A2E` |
| Paper cards (typeset telegrams) | `#E4E0D4` with ink `#1D1D1B` |

Sources are greyscale; red is the only colour and it only ever points: circles, the chart playhead, sync lines, highlights, ✓ badges (a drawn tick in a red box, no words), the zone everything converges on, the *unresolved* column, a strike-through on a wrong claim.

## 4. Type & subtitles

- Chinese headings and findings: Noto Sans SC 700 (30–124 px). Tags, timecodes and ticks: IBM Plex Mono 400/600. Quotes: Source Serif 4 Italic for the original wording, Noto Serif SC 500 for a translation underneath in the secondary colour (only when the subtitles don't already say it). All OFL, subset to the words on screen.
- **Few words per frame.** Each frame keeps only what this beat needs: the main readout or heading, the quoted original (the highlighted line), and one short source tag per piece of evidence. No eyebrow labels, no English twin under every Chinese label, no archive numbers, dates or "estimate / schematic / not to scale" footnotes unless the beat is about them, nothing the subtitle is saying at the same moment.
- **Source tag**: a 6×12 chip + `type · source` in mono, ≤ about 12 characters (`照片 · Pasquarella`, `FBI 电传 · 1937-05-08`), sitting just above its frame. Full credits go on the end card, not on the panels.
- **Lower third**: a red bar + place name (36 px bold) + one mono line (place code).
- **Subtitles** (bilingual films): at the bottom of the frame (Chinese baseline y ≈ 984, English y ≈ 1022): Chinese 34 px bold over English 23 px, centred, 10 px black shadow; **one line per language**, measured in the page against 1,500 px; a long sentence becomes two cues. Original sound gets subtitles too, marked `【原声】` / `[1937 newsreel]`.
- **Reading time**: every key text stays still and whole for CJK ÷ 4.5 + other ÷ 15 + 1.5 s (`readcheck.mjs`); verdict and comparison frames hold ≥ 2.5 s with every item fully in frame. Counters (timecode readouts, the stopwatch) and tick labels are exempt.

## 6. Shot & layout grammar

- 1920×1080, 60 px margins; content y 60–900, subtitles below it (y ≈ 950–1030). Layouts use the full height; no strip is reserved for a timeline. When a section has no subtitle, centre its content vertically.
- Panels are hard-edged rectangles with 1 px frames; footage panels keep the source's aspect.
- Typical layouts: **map → plan** (left) with a reference photo and a footage panel (right); **one big statement + one quote + one wide schematic**; **five-source board** (three evidence frames on top, sound and report below, schematic right, red links converging); **three-column sync grid** (report / photo / video under one stopwatch, each column lighting up when its source begins); **document strip + two-column verdict**; **claim card + fact-check card + dot matrix**; **evidence map** (plan, broken-axis mini timeline, schematic, thumbnails with links).
- Avoid centred layouts, page headers and slide-like page turns. Transitions are hard cuts on a 0.5 s grid, white flashes and the rewind; no dissolves.

## 9. Pitfalls

- **Inference passed off as fact.** Camera positions, photo times and offsets need `≈ / inferred / unlocated` on screen and in `FACTS.md`.
- **Early reports as facts.** The first-night memo and the period newsreel often disagree with the final report; use them as images or as claims to check, never as the source of a number.
- **Faking a multi-camera event.** With one licensable film, do not borrow clips of unclear origin; cross-check film + photos + documents + sound instead. The structure still holds.
- **Seams in "continuous" shots.** An exposure jump or splice breaks timing; time durations from the official record and state the alignment error.
- **Time zones and clocks.** Old reports may use standard time while the place ran on daylight time; pick one and state it once on screen (`18:25:00 EST` on the first readout).
- **Too much at once.** One layout, one finding; at most five sources on a board, and the subtitle never repeats the heading word for word.
- **Too many words on screen.** Keep only what this beat needs (main readout or heading, the highlighted original, one short tag per source). Eyebrows, English twins of every label, archive numbers, footnotes and translations the subtitle already gives turn the frame into noise.
- **Empty placeholder boxes for missing material.** A grey "no footage" or "waiting for photo" panel looks like a render error. Fill the slot with real material, change the layout, or let the source appear when it starts.
- **A strip reserved at the bottom** (timeline band, caption rail) leaves an empty band when it has nothing to show. Content runs to y ≈ 900; nothing lives in the subtitle area (y ≈ 950–1030).
- **Catastrophe as spectacle.** No slow motion of fire or impact, no full-screen flames, no sound effects on deaths.

