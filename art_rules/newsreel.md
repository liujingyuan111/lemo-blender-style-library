# 1920s 新闻影片 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/newsreel/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`ec7cf8cef4efdc557c70f7743c5eb431d20e219e43a0a3dc2cbea1cfeea41e8d`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、10。

---

## 1. Essence, and what it is not

An edit style: the look is in **how real material is arranged, cut, captioned and carried by sound**, not in a drawing technique.
- **Archive in a projected gate**: 1.37:1 picture, full height, rounded corners, black outside; everything inside it shares one silver grade, gate weave, flicker, scratches and dust.
- **News objects** do the explaining: newspapers, magazine pages, books, telegrams, maps, records. They are filmed (spun, slammed, panned, turned, underlined), never typeset as slides.
- **A voice talks over everything**: short exclamations, half joking, never a lecture.
- **Music is a band, and it edits**: cuts land on the band's beats; the band stops dead to let a line land; a period record can take over the soundtrack.

Not `silent-film` (1920s Silent Film, in this library): that style is a drawn, inked comedy projected between velvet curtains, with intertitles instead of voices, a cinema pianist and no foley. Here nothing is drawn but the packaging; the footage and print are real; somebody always speaks; the soundtrack is brass, banjo and records; titles are news captions (place · date), not dialogue cards; there are no curtains and no theatre.
Not a documentary with a "vintage filter" either: no talking heads, no slow Ken Burns drifts, no modern lower-third bars.

## 2. Materials & rendering

- **Gate**: 1480 × 1080 inside 1920 × 1080 (1.37:1), corner radius 26 px, pure black outside. Nothing is ever drawn outside the gate.
- **Two layers**: the picture layer (footage, print, maps, cards) gets the film look; the type layer (place cards, labels, subtitles, the record inset) stays sharp and steady. Grease-pencil marks belong to the picture (they weave with it).
- **Base grade** for every source, before anything else (`tools/prep.py`, `grade()`): greyscale → percentile stretch (0.6 % → black, 99.6 % → white; print: 0.2–0.3 % / 99.0–99.7 % with the black lifted to 26–30, like newsprint) → mild S-curve `x + 0.18·(x−0.5)·(1−|2x−1|)` → output 14–238. **Moving footage uses one level set per clip** (sampled across all its frames), never per frame.
- **Projection look** (`filmLook()`, picture layer only): warm silver (`multiply #efe7d6`, `screen #17140f`), vignette 0.42 H → 0.95 H, flicker ±3.5 % per frame + 3 Hz drift, gate weave ±1.6 px / ±2.2 px (value noise), 0–3 vertical scratches that live for 9 frames, 0–4 one-frame dust specks. Grain is added at mux (`mux.sh … 24 7`), not in the page.
- **Archive film upscaling**: at most ~2.5×. NTSC transfers (720 × 480) are treated as 4:3, cropped to 1.37 and scaled 2.31× to 1480 × 1080: `hqdn3d=4:3:6:5` → `lanczos` → `unsharp=5:5:0.55` → base grade. Frames are exported at 24 fps as JPEG sequences and played by `floor((t − t0) · 24)`, so renders are deterministic.
- **Print**: newspapers, magazines and books at their scan resolution; crop pages to the relevant fold so unrelated (and sometimes ugly) old stories never come into view.
- **Code-drawn packaging only**: the ident (sunburst, two searchlights, wire globe), item title cards, maps, the end card. Never generate "archive" pictures.

## 3. Colour logic

- **Monochrome warm silver** for the picture; values do the work (check every shot as a thumbnail).
- Type is cream on near-black (`#f3eee4` / `#d6cfc0` on `rgba(12,11,10,.8)`), framed by a 2 px cream rule; marks are a slightly warm white grease pencil; underlines on printed pages are dark soft lead.
- Packaging silver: Art Deco gradient lettering `#fff → #d9d4ca | #9e978a → #efebe2` with a hard "metal" break at the middle and a black outline (0.12 em).
- No colour accents, no sepia wash on top of the silver, no colourised archive.

## 4. Type & subtitles

| Use | Face (all OFL) | Spec |
|---|---|---|
| Ident, item cards, end title | Limelight | 104–118 px, silver gradient, black outline |
| Chinese display (ident, cards, end title) | Noto Serif SC 900 | 50–76 px, letter-spacing 10–26 px, `#ece7dc` |
| Place card, labels (English) | Oswald 600 | 26–34 px, letter-spacing 4–6 px, upper case "PLACE · DATE" |
| Place card, labels (Chinese) | Noto Sans SC 500–600 | 24–30 px |
| Subtitles | Noto Sans SC 600 40 px over Oswald 400 29 px | bottom of the gate (baselines H−82 / H−38), black stroke 8 / 6 px |

- **Place card** (the newsreel's segment title, instead of full-screen cards for every story): top left of the gate (gate x + 48, y 56), dark box with an inset 2 px cream frame, English "PLACE · DATE" over one Chinese line; it is pulled out left to right in 0.22 s and fades 0.15 s before it leaves. Hold ≥ CJK ÷ 4.5 + Latin ÷ 15 + 1.5 s from the moment it is complete (`readcheck.mjs`), so keep both lines short.
- **Item title card** (one per film at most, to turn to a new story): black, a double Art Deco frame drawn in 0.35 s with quarter-fan corners, Limelight line + Chinese line, slow push; ≥ 2.5 s.
- **Labels inside split screens**: one per panel, top centre, same box style, enter one beat apart.
- **Subtitle strip**: the subtitles sit on a dark strip across the bottom of the gate (180 px, transparent at the top edge, ≈ 93–96 % `#0a0908` below), on every shot, fading in 0.25 s before the first cue of a run and held through gaps under 1 s, so it never blinks; print and pale footage would otherwise swallow the letters (`subBand()`).
- **Subtitles**: Chinese line over English line, **one line per language, never wrapped** (`tools/subcheck.mjs` measures every cue in the page); a cue lasts max(1.8 s, spoken + 0.6 s) and ends 50 ms before the next. Print in shot is never re-typed as a caption: the announcer and subtitles carry its meaning, an underline points at it.

## 6. Camera on stills and archive

| Move | What it does | Typical use |
|---|---|---|
| Spin-and-slam | the paper arrives as news | a headline; a telegram; a poster |
| Slow push then punch-in on a beat | from the whole page to the one detail | a headline → a photo in it |
| Pan across a wide print | a crowd, a parade, a skyline | panoramas, group photos |
| Tilt to reveal | the landmark behind the subject | a building, a monument |
| Map push | from the country to one city, into the next story | travel, spread, campaigns |
| Grid deal | many related stills land one per beat | step-by-step, collections, "all of them" |
| Flip-book | a series of stills played on the beat becomes motion | dance steps, assembly stages, before/after |
| Freeze + jolt | stop the archive on the telling frame | the punchline, the evidence |
| Split / quad | two or four places at once, side by side | comparisons, "everybody's doing it" |

Archive footage is not reframed with fake camera moves bigger than ~6 % (it already has its own camera); stills always get a move with a purpose.

## 10. Pitfalls

- Catalogue descriptions matter: a picnic film can contain both old-time dances and the Charleston; use only the shots that match the claim.
- Archive transfers start and end with archive slates, "End of Recording" and white flashes; cut inside them. Remove watermarks and archive logos.
- Newspaper pages hold unrelated, sometimes offensive stories next to yours: crop to the fold you need.
- Per-frame auto-levels make footage pump; use one level set per clip.
- `destination-in` irises leave transparent corners that later turn grey under `screen` — paint black behind with `destination-over`.
- Captions that fade before they can be read fail `readcheck`; shorten the words, not the hold.
- A fast announcer outruns Chinese subtitles: 6–12 English words per line, ≤ 23 Chinese characters.
- TTS mispronounces names (Bessie → "Bestie"); rephrase until the speech check passes.
- Old sources are soft: never exceed ~2.5× upscale; prefer wider framings to crops.
- Grain belongs to the mux; don't add it in the page as well.

