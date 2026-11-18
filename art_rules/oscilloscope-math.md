# 示波器数学 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/oscilloscope-math/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`2b9b1ca78c1bebaf58b2673356170e6dfe84f8e0b322617b16f016f53af8f635`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

- **The maths is real.** Circles, curves, readouts, cursors and the formula come from one set of numbers: an epicycle chain is the actual Fourier series, a readout is the value at the drawn point, a measured distance is computed. Freeze any frame and it checks out.
- **Light, not ink.** Everything is emitted light: a sharp core, a soft bloom, a white-hot centre where the beam is fast or new. Nothing is filled with flat colour.
- **The screen is glass in front of a world.** HUD (formula, readouts, subtitles, credits) is fixed to the glass; the world (curves, circles, axis, graticule) moves behind it.
- **Text becomes geometry.** Titles are written by the beam, then their letters morph into the next shot's subject (a circle, an axis).

Not Sci-fi Hologram HUD (no fantasy chrome, no cyan-magenta palette), not Data Storytelling (no bars and pies on white), not Blueprint (no paper, no drafting), not ASCII/CRT Terminal (no raster, no scanlines, no character grid).

## 2. Materials & rendering

- **Vector beam on a phosphor screen.** Draw with constant-width lines in screen pixels (1.2–3.2 px), so a line stays a beam at any zoom. No scanlines (an analogue scope is a vector display).
- **Light channels.** Draw three layers of light (beam trace, graticule and text, white-hot cores) plus an optional second channel for measurements; a post pass gives each its phosphor colour and glow. Beam layers bloom strongly; text blooms faintly so it stays crisp.
- **Bloom**: several Gaussian blurs at 1/2 to 1/16 size added back; where light piles up it turns towards white, through a soft shoulder rather than clipping.
- **Afterglow is drawn, not accumulated.** Earlier instants of moving objects (8–10 ghosts a few milliseconds apart, fading by a power curve) and a short trail behind a moving point. Frame-to-frame decay strobes at 24 fps; do not use it for anything that moves fast.
- **A fast beam leaves less light.** Steep segments of a trace are drawn dimmer (about 55–60 % on a vertical edge); older parts of a scrolling trace fade with age.
- **Graticule**: dotted minor lines, a solid centre axis with 0.2-division ticks, refined in levels of 5 as the camera zooms (the finer level fades in).
- **The screen**: near-black with a faint green ambient falloff, a vignette, a little dither noise so the glow never bands in 8-bit video.
- Example (our demo): Manim (Cairo renderer) draws the channels into PNG frames; a numpy/OpenCV pass makes the phosphor.

## 3. Colour logic

- One phosphor family; colour means role, not decoration.
- Beam green for anything the signal draws; paler green for graticule and text; white-hot for the beam's newest point, joints and arms, and the flash of anything just created.
- **Amber = the second channel**: measurement cursors, measured values, markers of a finding. Never used for decoration, never for the signal itself.
- No other hues. Grey cards only for unfinished placeholders.
- Example (our demo): screen #010402, ambient #0B2412, beam #4DFF88, text #8DFFB0, hot core #E6FFEC, amber #FFB547.

## 4. Type & subtitles

- **Instrument voice**: a monospace (e.g. JetBrains Mono, OFL) for readouts, cursors, knob values, labels on objects, 19–30 px. Values are live (computed every frame); align the `=` signs in a column.
- **Formula**: TeX typography (MathJax SVG paths or LaTeX), top left, about 520–560 px wide; glyphs are lit one by one by the beam; the part that changes (an upper limit, a coefficient) flashes when it changes.
- **Titles**: a serif that matches TeX (e.g. STIX Two Text, OFL), 60–84 px, with the key word in italic; a Chinese line under it in a CJK serif (e.g. Noto Serif SC) ≥ 34 px. Written by the beam (outline traced, then filled, then a white-hot flash), never faded in.
- **Subtitles**: bottom left, fixed to the glass, a thin vertical light bar, Chinese serif 36 px over English STIX italic 29 px, one line each, a soft dark scrim behind them so a trace never runs through the words. Keep subjects and labels out of that corner.
- Holds: anything the viewer must read stays at least characters ÷ 15 (Latin) + characters ÷ 4.5 (CJK) + 1.5 s; a measured verdict holds ≥ 2.5 s.

## 6. Camera grammar

The camera lives in the world (centre and zoom); zoom is logarithmic, and the centre moves so the target stays put on screen while zooming (flying to a point). Line widths and HUD do not scale.

| Move | What it expresses | Can serve |
|---|---|---|
| Follow the beam's writing point | something being made | an opening; drawing a curve |
| Push onto a rotation, then ride a moving point | attention on a mechanism | one term, one phasor, one particle |
| Match cut between two curves of the same shape | "this is that" | a circle's arc to a wave crest; a trajectory to a graph |
| Pull back over a whole curve | the result | after a build-up; an ending |
| Dive into a detail (×10 and more), graticule refining, TIME/DIV shrinking | looking closely; the twist | an error, a crossing, a limit |
| Locked frame with cursors | measuring | a verdict |

Transitions come from the medium: letters morphing into the next subject; a title flying down and straightening into the axis; STOP followed by a dive; a CRT switch-off (the picture collapses to a line, then to a dot). No crossfades, no slide-like page changes.

## 9. Pitfalls of the medium

- **Numbers that don't match the picture.** Compute every readout from the drawn values; never type them.
- **Strobing afterglow.** Frame-accumulated decay at 24 fps leaves doubled curves; draw ghosts sub-frame.
- **Thin features vanish when sampled.** Sample curves at screen resolution and add dense samples around edges and spikes, or a 0.1 px spike disappears.
- **Crowded chains.** Small circles pile up at the tip; push in, or draw only the circles larger than about a pixel and limit ghosts to the first few.
- **Out of frame.** Size the chain so its full reach stays inside the graticule (a sum of radii can exceed the radius you expect).
- **Text in the glow.** Keep glow on beams, not on type; no outlines or drop shadows on text.
- **Readouts that flicker.** A value meant to be read is shown at a precision that holds still.
- **Facts.** Mathematical claims shown as numbers come with their source (FACTS.md).

