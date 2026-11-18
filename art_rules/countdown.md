# 实时倒计时分屏 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/countdown/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`867cca6e0c9bb0d6fb914cc4e9a2e295623ecd345fda9bd00bc362ff233f220f`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、9。

---

## 1. Essence, and what it is not

1. **Real time.** One continuous stretch of the event, never cut, never re-ordered, never sped up. Slow-motion sources are played back at real speed. The clock and the picture can be checked against each other at any frame.
2. **The clock is the lead.** It ticks every whole second (sound and a falling digit), it says who is in control, and it changes state at zero.
3. **Cells show the same second.** Every video cell is synced to the clock, or says plainly that it is not (§8, "sync badge").
4. **The layout is the edit.** Cuts are layout changes, and every layout change lands on a real spoken call or event in the native sound, not on the music.
5. **More cells, closer to zero; one picture at zero.** The number of cells is the tension curve.

Not a montage (time jumps), not a security wall (the layout never moves), not a flashback structure (real time cannot go back), not a slide deck (cells that don't follow events, text filling the cells, centred titles with page turns).

## 2. Materials & rendering

- **Three kinds of material at once**: video cameras of the same moment (2–8), documents (a fact sheet, a filing, a schedule: shown as paper, never retyped as a slide), and photographs (the people of the day). Our own type explains them; type printed in the material is only picture.
- **Data drawn by us**: checklists, bars, a flight or process profile, a second countdown to the next milestone. Every number comes from an official source (§10).
- **Cells**: hard rectangles on near-black `#06080A`, 24 px outer margin, 8–9 px gutters, 1 px border `rgba(222,232,238,.16)`, a light radial vignette (to 36 % black) on video cells. No rounded corners, no drop shadows, no 3D.
- **Camera chip** top-left of every cell: dark plate 84 %, a square dot (orange = synced video, grey = unsynced or still), code (`CAM 4`, `DOC`, `LIST`), Chinese name, small English name.
- **Burned-in text in the sources** (broadcast bugs, camera IDs, timers, tracker readouts) is cropped by a per-shot usable region, or blurred out (ffmpeg `delogo`) after it has been used for syncing. Never shown as if it were ours.
- **One grade for every source** (ffmpeg): `eq=contrast=1.07:saturation=0.9:gamma=0.97:brightness=-0.01,colorbalance=rs=-0.02:bs=0.03:rh=0.03:bh=-0.02`, then film grain 1 at the master (`mux.sh … 1`). Cool shadows, slightly warm highlights: control rooms and launch pads look like one film.
- **Resolution**: modern footage at most 1.5× its source pixels; for a punch-in, extract that stretch at a higher resolution from the 4K source instead of enlarging a 1080p frame. Documents at ≥ 1 source pixel per screen pixel.

## 3. Colour logic

| Role | Value |
|---|---|
| Ground | `#06080A`; panels `#0B0E11` |
| Main text | `#F2F5F7`; secondary `#7C878D` |
| Accent: the T− sign, synced dots, ticks done, event flags, the active control segment | `#FF5B1F` |
| Speaking light, "heard" tags | `#FF3B30` |
| Plates over full-screen footage | `rgba(6,8,10,.80)` |
| After zero, the clock block | ground `#FF5B1F`, text `#0A0B0C` (inverted) |

Orange means "now / synced / done". Grey means "pending / not synced". Nothing else is coloured; colour belongs to the footage.

## 4. Type & subtitles

- Clock digits: a condensed sans with fixed-width digit slots (ours: Barlow Condensed SemiBold, drawn digit by digit in equal slots so the clock never jitters); size up to 132 px, the T−/T+ sign at 0.85×, tenths at 0.41× in grey, a ten-segment sub-second bar under it.
- Chinese: a sturdy sans (ours: Noto Sans SC 500/700, subset). English text: a clean grotesque (Barlow). Labels, codes and English small print: a monospace (IBM Plex Mono). All OFL, in the project's `fonts/`.
- **The live transcript is the subtitle.** A fixed box (bottom right, or a cell in the grid): a speaking light and the speaker type (commentary / loop / narrator — the narrator, our own voice, is marked in orange so it is never mistaken for the event's audio), the English line appearing word by word at the spoken times (0.08 s fade per word, a block cursor), the Chinese line whole when its cue starts. **One line per language, never wrapped**: a long sentence becomes two cues; each cue ≥ max(1.8 s, speech + 0.6 s). Transcribe only what is said; mark doubtful words in `FACTS.md`.
- Reading time for everything else: CJK ÷ 4.5 + other ÷ 15 + 1.5 s from the moment it is complete (`readcheck.mjs`). A comparison (two bars, two numbers) stays fully on screen ≥ 2.5 s.

## 9. Pitfalls of the medium

- **Unsyncable footage** (an edited "rover" reel with no clock or event to align on). Never fake it: label the cell "same window · not frame-synced", keep it out of the countdown's key seconds or use it only where nothing it shows contradicts the time, and say so in `FACTS.md`. Look first for a source with a burned-in timer, a visible ignition / flash / whistle, or the same audio.
- **Measuring zero.** Never trust metadata. Combine two independent marks: a visible event (ignition flash, a broadcast countdown bug's flip) and the spoken word timing ("booster" at zero). Re-measure on the file you actually cut: `ffmpeg -ss … -c copy` starts on the previous keyframe.
- **Audio and picture of one file can disagree** (a switched feed whose audio lagged its video by ~1 s). Sync each camera on its picture.
- **Slow-motion sources**: measure the factor from two events with a known gap (e.g. engine start to booster ignition = 6.36 s) and re-time with `setpts=PTS/k`.
- **Burned-in text**: broadcast bugs, camera numbers, timers, tracker data. Define per-shot usable regions (they change when the source cuts) or `delogo` them; check every source cut with a frame-difference scan.
- **A static wide shot for ten seconds** reads as flat. Give every 1–2 seconds a new element (a cell, a tick on the list, a flag, a punch-in), not a fake camera move.
- **Spoilers in the subtitle**: a whole-sentence Chinese line reveals the end of a count early. Split counts into separate cues.
- **The clock jitters** if digits are proportional: draw them in fixed slots.
- **Hot peaks** from broadcast audio and the ignition hit miss the true-peak target: pre-limit the mix at about −4 dBFS after normalising to −14 LUFS.
- **Logos.** No agency insignia as a graphic; cut slates and bugs; the film says it is unofficial.

