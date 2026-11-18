# 视觉笔记 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/sketchnote/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`c1d8538cf0c8f2124fe3aa8597924f3f1fc4b63a5a90c2e436fdea633f400906`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

- **The frame is the page.** Warm white dot-grid paper fills the screen; there is no desk, no notebook edge, no hand and no pen prop.
- **Everything is drawn in front of you**, at the speed of a pen: outlines first, then the marker, then the words. Nothing fades in, nothing slides in.
- **Three tools only**: one black fineliner, one grey marker (three strengths), one yellow marker.
- **Hand lettering is the typography**: titles on banners, keywords in a bold hand, notes in a thin hand, all written stroke by stroke.
- **The page is planned as a poster.** Every note has its place in the final page; the film is the page being made.

Not Whiteboard Explainer (no hand, no wipe, a page that is kept, not erased; tone and volume from marker, not a bare marker line), not Urban Sketch · Pen & Wash (no watercolour, no perspective scene), not Chalkboard, not Data Storytelling (charts are hand-drawn notes on the page, not a chart engine), not a keynote (no slides, header bars or page turns).

## 2. Materials & rendering

- **Paper**: a flat warm white with a faint grain texture anchored to the page, and a dot grid (26 px pitch, 1.3 px dots) drawn in world space so it scales with the camera.
- **Fineliner**: points resampled every 3 px and offset along the normal by three layered sines (a slow wobble, a medium one, a fine tremor); drawn twice, the second pass thinner (≈ 0.6×), lighter (≈ 0.5 alpha) and wobblier; line weight varies in short segments; closed shapes start at a random point and overshoot their start a little.
- **Marker**: clipped to a jittered outline, laid as a row of slightly bowed, semi-transparent broad strokes at one angle, composited with `multiply`, so overlaps darken into streaks; a thin line of pooled ink along the clip edge. Markers are laid stroke by stroke in their angle's order.
- **Shadow and volume**: the shape minus itself shifted (even-odd), filled with grey marker. Drop shadows always fall the same way (down-right, ≈ 9–10 px for boxes); crescent shading on the side away from the light.
- **Paper fill**: a shape that sits on top of others (a banner, a box, a jar label) is first filled with the paper colour, so the lines under it disappear.
- **Letters written stroke by stroke**: each glyph of the real font is thinned to its centre line, ordered like a pen (start at the top-left free end, keep the smoothest direction, lift and jump to the nearest free end), and revealed by a thick mask stroked along that path. Never wipe text in from left to right.
- **Determinism and boil**: every element has a fixed seed; random numbers are consumed the same way at every progress, so a half-drawn stroke and the finished stroke are the same stroke. Only the fineliner's wobble phase boils: a new drawing every 2 frames, a cycle of 3, a shift of 0.35–0.7 rad (≈ 1–2 px). Marker fills never boil.
- **Everything is anchored to the page** (world space) and seen through one world → screen camera. Only subtitles live in screen space.

## 3. Colour logic

- **Ground**: warm white paper; dots in a light warm grey. No dark backgrounds, no large black areas.
- **Ink**: one near-black for lines and words; a warm dark grey for secondary notes.
- **Grey marker**: the only way to give volume, shadow and fill; three strengths (light for volume, middle for shadows and banner tails, dark for folds and small dark parts).
- **One yellow**: reserved for the one thread the story follows (say, one raindrop on its way to the sea) and for two structural parts, the numbered banners and the fat arrows. Everything else stays black and grey. A darker yellow only for sparks and the closing loop.
- All colour is laid as translucent marker in `multiply`, never as opaque flat fill.

Example (our demo): paper #FBFAF6, ink #1E1E22, notes #5B5852, grey rgba(100,100,110,.16) / rgba(80,80,92,.28) / rgba(52,52,64,.45), yellow rgba(255,205,40,.80), dark yellow #F5AA00.

## 4. Type & subtitles

- **Hand lettering only**, licence-free and self-hosted: a bold casual hand for titles, banners and keywords (e.g. Kalam Bold, 34–84 px), a thin upright hand for notes (e.g. Patrick Hand, 26–32 px), a hand-written Chinese face for Chinese (e.g. ZCOOL KuaiLe, subset to the characters used). Avoid regular kai or sans faces: next to hand lettering they read as system fonts.
- **Hierarchy is part of the page**: title on a banner with a yellow swash; keywords bold; notes thin and grey; numbers that matter get a yellow swash or a loop. At most four sizes on a page.
- **Each letter has a little tilt and bob** (fixed seed), never perfectly aligned.
- **Micro notes** (≈ 3 px on the page) may live inside an icon, readable only when the camera dives in; on the full page they read as texture.
- **Subtitles** belong to the notebook: a paper slip at the bottom of the frame, a strip of grey washi tape on its corner, one line of Chinese (hand-written face, ≥ 40 px) over one line of English (the note hand, ≈ 31 px), never wrapped. A soft 0.2 s fade and a 6 px rise. Hold ≥ max(1.8 s, speech + 0.6 s). Frame every shot so the subject sits above the slip.
- Text written on the page is timed to the words of the voice-over.

## 6. Camera grammar

A camera over a flat page: one world → screen function, zoom in log space, centre moving in step with 1/zoom on big zoom changes.

| Move | What it expresses | Can serve |
|---|---|---|
| Ride the pen (centre trails the pen tip slightly) | being there while it is made | a long outline; a path; a diagram growing |
| Slow push while words are written | attention, reading time | a definition; a key number |
| Pan along the page between blocks | the next idea follows from this one | a sequence; cause and effect |
| Whip across empty dots (quintic ease) | a jump in thought, a question | a question; a change of topic |
| Dive (10–15×) into an icon | the detail inside the thing | a mechanism; a hidden part; a micro note |
| Shape match cut (one round shape to another of the same screen size) | this becomes that | a transformation; one thing carried elsewhere |
| Pull back to the whole page | the parts add up | a summary; a scale reveal |

- Pens may draw off-screen only when the shot shows other drawn work; a frame should always contain something readable.
- Framing: a block being explained fills about half to two thirds of the frame height; the subject stays above the subtitle slip.
- Transitions are camera moves over the same page. No cuts to other pages, no fades, no page turns.

## 9. Pitfalls of the medium

- **Flicker**: random numbers drawn per frame make every line jump. Seed every element; let only the wobble phase boil, and only a little.
- **Text that appears at once**: a wipe or a fade reads as a slide. Write along glyph skeletons.
- **Yellow everywhere**: when the accent decorates, it stops meaning. Keep it on one thread plus banners and arrows.
- **Overcrowded page**: if the poster looks like a page of handwriting, the film will too. Leave dot-grid air between blocks.
- **Heavy black and dirty shadows**: big black fills and inconsistent shadow directions break the paper feel. Grey marker for mass, one shadow direction.
- **Small text in the final frame**: plan the poster first; no note below ≈ 26 px at the final zoom.
- **Empty frames during camera moves**: a pan that lands on paper before the pen arrives. Start the words before the move, or keep finished work in frame.
- **Thick lines when diving**: line widths and wobble are in page units; inside a dive, draw micro notes with proportionally thinner lines and smaller wobble.
- **System-looking Chinese**: regular kai or sans faces next to hand lettering read as fallback fonts.

