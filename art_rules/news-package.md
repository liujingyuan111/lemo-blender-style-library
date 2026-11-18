# 电视新闻包装 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/news-package/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`d763b356442dd0d7373fe409fa9108ec6a3c2901ec5534522af6b08b0915b72f`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、4、5、6、11。

---

## 1. Essence, and what it is not

1. **One package system, used consistently.** Every graphic is built from the same few parts: a brand plate (parallelogram), a tab in the accent colour, a paper strap, ink cards with an accent top edge, mono datelines, stamps. Viewers read the system before they read the words.
2. **The bulletin's order.** Sting → rundown ("today we have four stories") → item → item → … → back to the rundown, ticked off → sign-off. Each item opens with its category on the strap's tab and its date on the first graphic.
3. **One fact per screen.** A full-frame graphic states one thing: the price, the break, the two stocks, the place, the two letters, the quote, the verdict.
4. **The strap holds the headline.** One lower-third strap is on screen from the first story to the recap and changes its words with a vertical flip; the picture above it is free for the graphic.
5. **Clean panel.** No crawl, no burned-in subtitles; subtitles ship as a separate `.srt`. The frame is the graphic, the strap, the bug and a source line.

Not **Caption News** (that is captions-first social video: huge slammed captions are the lead, no rundown, no strap; here type is small and orderly and the graphics lead). Not **Data Storytelling** (one chart per beat, never a dashboard; the chart is an insert in a bulletin). Not a keynote: no centred title-and-bullets, no page turns. Not a studio show: no virtual set, no anchor, no fly-throughs — the package is flat graphics over ink.

## 2. Frame and layout (1920×1080)

| Zone | Position | Content |
|---|---|---|
| Content | x 96–1824, y 56–840 | the full-frame graphic; when a strap is up, nothing important below y 840 |
| Lower-third strap | tab x 96 y 856, 48 high; strap x 96 y 904, 1250×104, + 120 px ink end block | category tab (accent, ink text, Chinese + English), headline in Chinese 50 px + one English line 27 px |
| Source line | right-aligned at x 1836, y 950 / 978 | `SOURCE: …` mono 13 px + Chinese 16 px, 75 % opacity; English ≤ 36 characters or it slides under the strap's end block |
| Channel bug | top right, plate centre (1739, 86), 0.327 of the sting plate | the plate plus `AI NEWS` |
| Corner tag | top left x 96 y 56, 330×64 | `ILLUSTRATION / 示意 · AI 生成画面` on generated plates, `SCHEMATIC / 示意图` on schematic charts; flips in and out 0.2 s |

Content layers sit lower than a subtitled layout would put them (a 60–110 px downward shift) so the bottom strap does not leave an empty band above it. When you remove subtitles and the crawl, re-lay the page; never leave the space they used.

## 4. Colour

| Role | Value | Use |
|---|---|---|
| ink | `#121417` | backgrounds, panels, strap end block |
| ink2 / ink3 | `#1B1E23` / `#22262C` | cards, land on maps |
| accent (lemon) | `#F2CF1D` (light `#F8DE4A`, dark `#D8B30C`) | plate, tabs, band wipe, bars, stamps, the line that breaks |
| gold | `#D4B064` | thresholds, datelines, source lines, light fins, badges |
| paper | `#F4F1E8` | strap, documents, the chart line |
| breaking | `#FE6B3D` | only for BREAKING and LIVE. A weekly round-up has neither, so it never appears |

Structure to keep when you change the brand: one accent + one gold-like secondary + paper + ink, and a reserved alarm colour. Ink text on the accent; on paper, English secondary lines in a dark olive (`#6E5A1E`) because gold is too weak there.

## 5. Type

- Chinese: Noto Sans SC 900 (headlines, strap) / 700 (labels).
- Latin: Barlow Condensed 800 (numbers, names, the plate), 600 (secondary lines, quotes), 600 italic (the end-card English title).
- Mono: IBM Plex Mono 500 for datelines, sources, axis labels, all caps with 1–4 px tracking.
- All OFL, subset from Google Fonts by `demo/tools/fonts.sh` (the character list is read from `main.js`; delete `fonts/*.woff2` after a text change). No handwriting faces in this style.
- Every label is bilingual on one line each (Chinese first, English smaller); never wrap.

## 6. Picture layer and grade

- When there is no footage, the picture layer is data graphics drawn in code plus, at most, a few **illustrative plates** (generated or stock), each tagged `ILLUSTRATION` for as long as it is on screen. They set a mood (a server room behind a model launch, a wafer behind chip stocks); they never stand in for the event, the place or the people.
- One grade for every plate: greyscale → auto black/white points (0.5 / 99.6 percentile) → γ 1.05 → 35 % S-curve → black 8, white 232 → duotone `#0E1013` → `#ECE7D8` (`tools/prep.py: grade()`), plus a left-dark ink gradient for type, a 50–55 % vignette and 7 % overlay grain cycling through six tiles. Graphics and the package are never grained.
- Real footage, if you have it, takes the same grade path; modern footage ≤ 1.5× scale, archive ≤ 2.5× after deblocking; crop out station logos.

## 11. Pitfalls

- **Package left behind.** If the strap, source line or tags are drawn once on top of everything, a wipe changes the picture under yesterday's headline and the strap catches up 0.3–0.5 s later. Draw them per picture, inside the wipe's clip.
- **Leftover layout.** Removing subtitles or a crawl without moving the content down leaves a dead band above the strap.
- **Masked type peeking in.** A push-in title clipped by a mask shows its top edge before it moves if the travel distance doesn't clear the mask; start it fully below and don't draw at progress 0.
- **Words stronger than the source.** "Request for information" is not "investigation" or "penalty"; write "no fine, no case opened" or "for the first time" only if a source says so — and check the institution's own pages, which can contradict a report ("first requests" may have gone out months earlier).
- **Thresholds depend on the reference.** "Bear market" = −20 % from *which* high? Name the reference on the axis; from a different peak the claim can be false.
- **Attribute what only a report says.** When the official source does not name the companies, the graphic carries "据… 报道 / reported by …" and so does the voice.
- **A schematic posing as data.** Rolling counters on a close price flash values that never existed; set the close with a mask push instead. Don't label axes the data doesn't support.
- **Source lines under the strap.** Right-aligned mono 13 px: ≤ 36 characters.
- **Stamps over key words.** A stamp hit can mask the voice ("fines"); take the brass off the stamp and low-pass its clack.
- **Gold on paper** has too little contrast: use ink or dark olive.
- **Generated plates** carry stray corner marks: crop them in `prep.py`.
- **Short preview text.** Rundown rows are previews of the stories; `readcheck` flags them as short in the opening — they return in the recap and as straps, so accept the flag or leave them out of `TEXTS`.
- **Names in synthetic speech.** Spell brand names, model numbers and abbreviations the way they should sound in the TTS text (a respelling, a number written as a word, an abbreviation without dots) while the strap and subtitles keep the real spelling; when speech-to-text mishears an unusual name, put the expected transcript in the line's `asr` field instead of rewriting the line.

