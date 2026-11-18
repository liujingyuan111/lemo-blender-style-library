# 体育战术板 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/telestrator/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`7289027728dc5e1b6d095b7c7bc7806790bb579934c81682265c0c1b4897a3d0`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、4、5、7、12。

---

## 1. Essence, and what it is not

1. **Watch it, then take it apart.** Every piece of action is seen moving before it is explained. A freeze always follows play; the explanation never comes first.
2. **One freeze, one finding.** Each freeze says one thing (the ball wasn't cleared; nobody stepped out; he struck it from outside the box) with one label and at most two groups of lines. The same few seconds of footage are reused, each pass going one layer deeper.
3. **Drawn on the real picture.** Rings sit under feet, arrows follow the ball's real path, the box line is traced over the real line. Nothing floats in an abstract diagram until the film deliberately flattens the pitch.
4. **Data counted from the footage.** Times come from frame counts (a stopwatch that runs on source frames), distances from the pitch markings (a perspective transform). What the footage can't measure (ball speed, sprint distance) is not stated.
5. **Studio energy.** Bright marker lines, a white flash and a punch on every freeze, the music stopping with the picture.

Not **Visual Investigation** (that is restrained, synchronised multi-camera evidence where the timeline is the protagonist; this is a pundit's show with packaging and enthusiasm). Not a **highlight reel** (no montage of goals to music; each clip is analysed). Not **Data Storytelling** or an infographic: charts are not the film; the top-down board appears once, as a summary, and is reached by flattening the real picture.

## 2. Frame and layout (1920×1080)

- **Full-frame footage** most of the time. The packaging lives in the corners:
  - **Corner bug**, top right (x 1452–1880, y 38–110): show name on a yellow block + a mode line in the mode's colour — LIVE (red dot) / ANALYSIS (yellow) / REPLAY (cyan). It is in every footage frame from frame 1, because it sits over the broadcaster's logo.
  - **Score bar**, bottom right (x 1392–1880, y 926–996): HOME n – n AWAY + minute. The away number flips on the frame the ball crosses the line (a 0.5 s roll with a yellow flash). It sits over the broadcaster's URL.
  - **Source clock**, top left (x 40–370, y 38–90), on every analysis shot: `❚❚ 04.20s F106` — source seconds and frame number; ▶ ½ in slow motion, ◀◀ in a rewind. Hidden in live play.
- **Labels** (black card, coloured left bar, Chinese line + small spaced English line) sit in empty grass or crowd, never over the action they describe.
- **Subtitle bar** bottom, centred at x 880 (its right edge stays left of the score bar), y 938–1044.
- **Split screen**: two 960×1080 vertical windows, each a 960-px-wide slice of a 1920 frame at 1:1 (no extra scaling), a 6 px yellow divider between them, a camera label at each window's top left (A MAIN CAMERA / B HIGH REVERSE). The slices are chosen so the broadcaster's logo and URL fall outside them.
- **Board pages** (shot map, data card): dark board `#0C1411` with a faint 60 px grid; left column text, right side drawing. No headers, no centred title-and-bullets.

## 4. Colour identity (the one rule that matters)

| Role | Colour |
|---|---|
| The team/player we follow, the ball, main marker lines | `#FFD400` fluorescent yellow |
| Opponents (rings, block arrows, link lines) | `#3FD8FF` cyan |
| Space (a patch nobody covers) | `#FF3B30` red, fill 0.34–0.38 + dashed edge |
| Pitch lines traced, neutral marks, stamps | `#F4F1E8` chalk |
| Show board | `#0C1411` ink green-black |
| Label / bug background | `rgba(8,12,14,0.9)`; opaque `#080C0E` where it covers a logo |

One colour, one identity, throughout the film: a label's left bar takes the colour of what it names. Change the hues if the show needs to, never the three roles.

## 5. Type

- Labels: Noto Sans SC 900, 40 px (30 px for a name), English line Barlow Condensed 600, 21 px, letter-spacing 2 px, in the role colour.
- Packaging numbers (score, minute, stopwatch, big data): Barlow Condensed 800 Italic.
- Clock / frame numbers: IBM Plex Mono 500, 24 px.
- Board pages: title Noto Sans SC 900 60–64 px, rows Noto Sans SC 700 34–42 px with a grey note under each, numbers Barlow Condensed 800 Italic 64–150 px in yellow; text appears left to right with a clip reveal.
- **No handwriting fonts** anywhere: printed type on a dark card belongs to the same packaging; handwriting reads as a school notebook.
- Subtitles: Chinese line (Noto Sans SC 500, 38 px) above an English line (Barlow Condensed 600, 32 px), black bar 0.64 with a 4 px yellow edge; one line per language, never wrapped — shorten the line instead of shrinking it.
- All fonts OFL from Google Fonts, subset to the characters used (`demo/tools/fonts.py`).

## 7. Grade and image quality

- Footage: `hqdn3d=1.2:1.2:2.5:2.5` → lanczos to 1920×1080 (modern footage at most 1.5×) → `unsharp=5:5:0.55` → `eq=saturation=0.9:contrast=1.04:gamma=0.97` + slightly cool shadows; one grade for every clip; film grain 2 added once at the master (`mux.sh`).
- Broadcaster logos and URLs are covered by the packaging (bug and score bar placed exactly over them, present from frame 1), or kept outside split-screen windows — never by cropping past 1.5×.
- Prefer a broadcaster's native resolution over an "AI-upscaled" stream.

## 12. Pitfalls

- **Wrong tracking points** are the biggest risk: reading coordinates off a scaled contact sheet is easily 20–50 px off. Read them on full-resolution crops with a pixel ruler, then check with `?dbg=1`.
- **Overlays not under the punch transform** slide off the players during a freeze.
- **Balls vanish**: long shots are a few pixels with motion blur; colour tracking loses them; frames where the ball is invisible are interpolated and the number says "≈".
- **Numbers the footage can't support** (ball speed, distance run) are not written. Distances only from a homography fitted to visible markings, each shot in its own frame (the camera zooms and pans between shots).
- **Packaging late by one frame** shows the logo: bugs never fade in over footage.
- **Split-screen windows sliding in** reveal what's outside them (a logo, a URL): clip each window to its slice in source coordinates, not only to the screen half.
- **Score state must match the moment**: before the 67th-minute goal it is 3–2, not 3–3.
- **Names in TTS**: spell them phonetically for the voice ("Zayits", "Saduk") and keep the real spelling in subtitles; record the ASR result for proper names in `lines.json` (`asr`).
- **Freeze labels echo the subtitle** and live only ~1 s; anything the viewer must read (scores, board rows, the data card) gets ≥ 2.5 s and goes into `TEXTS`.

