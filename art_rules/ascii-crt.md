# CRT 字符终端 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/ascii-crt/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`471f294a40b8ca050daeaaee329b94036174e5eda1e521c8406a579d711bb9b6`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

A single monochrome terminal screen: **P3 amber** (or P1 green) phosphor glowing on dark glass, curved at the edges, with scanlines. Every image, including title, landscape, face, room and subtitles, is made of **real glyphs placed on a character grid** and chosen by ink density. The film has one camera, the screen itself. It moves only by changing the **font size of the grid**: bigger characters push in, smaller characters pull out.

The mood is cold, patient and machine-calm: typed text, a blinking cursor as suspense, and one warm surprise.

**Never** fake it with an image plus an "ASCII filter". Characters must be drawn as characters on a grid. Not a hacker-movie green rain, not a pixel-art game (no sprites, no free pixels), not a sci-fi HUD (no vector lines, no free-floating panels).

## 2. Materials & rendering

- **Font**: one monospace bitmap-style font (VT323, OFL); cell 0.4 em × 0.8 em (1:2). A large prerendered glyph atlas with a stroke for beam spread, scaled with `drawImage`, keeps zooms continuous and sharp.
- **Grids**: column count per shot (title ~20, terminal 80, picture 200+); a push-in can go until one cell holds a sub-grid of its own.
- **Density ramp**: each glyph's measured ink coverage × dim / normal / bold → about 20 levels, near-duplicates dropped; a small ordered-plus-hash dither per cell; cells below a threshold stay blank. **Negative space makes ASCII art readable.**
- **Picture pipeline**: paint grayscale into an offscreen "negative" aligned exactly to the grid (several samples per cell; channels for phosphor, second colour, a flag), average per cell, pick a glyph. Interiors get local contrast (`m + 0.9·(m − mean)`) to keep outlines.
- **Recognisable subjects**: silhouettes, not noise (real coastline polygons, a face from a few planes); dark = sparse dim glyphs, bright = dense bold, shadow sides sparse `.` only; an angle with a clear silhouette.
- **Depth on a grid**: far = darker and sparser, near = brighter and denser; a thin bright rim separates planes.
- **CRT post** (WebGL, adapted from `core/post/crt.js`):
  - **Phosphor colour**: luminance maps along the phosphor's ramp (dim deep orange → amber → overexposed near-white for P3).
  - **Glow**: multi-level bloom plus a faint halo.
  - **Glass**: fine scanlines (narrower on bright areas), slight barrel curvature, rounded mask, warm near-black unlit glass, faint reflection, ~1 % flicker, fine noise. **No RGB grille: monochrome tubes have none.**
- **Afterglow**: text that disappears decays with τ ≈ 0.1 s, computed analytically so every frame is deterministic. Moving glyphs get one faint trail sample.

## 3. Colour logic

- **One phosphor** carries everything: amber, green or white, in its own brightness ramp. No second hue for decoration.
- **At most one soft second colour**, used for one thing only (the emotional object), switched on at a single moment, on a downbeat, and never taken back casually.
- Examples: amber screen with an ice blue-white for something far away; green screen with a warm pink for a living thing; white P4 screen with a pale gold for a memory.
- Brightness is the only other tool: dim / normal / bold and inverse video.

## 4. Type & subtitles

- **Subtitles are terminal output.** A reserved **LOG strip** at the bottom: a dim separator, an inverse-video tag, then a prompt and the line in uppercase at ~45 px. It is **typed word by word in sync with the voice** (whisper word timestamps) and holds ≥ max(1.8 s, speech + 0.6 s). It lives outside the zooming grid, like a status line, with the same scanlines and glow. When nobody speaks it can show system state (a progress bar, a waiting message).
- **On-screen text that the story shows** is picture, not subtitle; in the `.srt` it appears as `[SCREEN] …`.
- **Titles** are typed with key clicks, as a filename, a command or a header.

## 6. Camera grammar

The only camera is the grid scale, plus CRT power states and one possible shot outside the screen.

| Move | What it expresses | Can serve |
|---|---|---|
| Static 80-column terminal | Waiting, procedure, machine time | a countdown; a queue; a log being read |
| Push in (cells grow) | Attention, intimacy | one line of dialogue; a name; a decision typed |
| Pull out (cells shrink) | Context, scale | a title becoming line 1 of a list; one entry among thousands |
| Push into a single glyph | Hidden depth; what a symbol is made of | a letter made of messages; a pixel made of people |
| Scroll (the buffer moves) | Accumulation, time passing | years of records; a changelog; a feed |
| Clear screen / hard redraw | A cut; a new state | a reboot; a new chapter; a crash |
| Text becomes image (grid shrinks as glyphs fall) | Words turning into world | a letter becoming a face; data becoming a map |
| Power on / off, degauss | Birth, death, sleep, shock | a machine waking; an ending; a jolt |
| Pull back off the glass into a drawn room | The screen is an object in a world | who is reading; where the machine is |

Opening and ending come from the topic. Framing: text stays in the safe area inside the curvature; keep the LOG strip clear. Transitions happen on the screen (clear, redraw, scroll, power), never a crossfade between two screens.

## 9. Pitfalls of the medium

- **Inverse video**: `destination-out` only changes alpha, which the upload ignores → opaque black canvas, cut letters with a *black* atlas.
- **Negative not aligned to the grid** drifts across hundreds of columns → map with cell width / samples exactly.
- **Wrong cell centre**: cells are 2·cw tall, so the centre is `(j + .5)·2cw`, not `(j + 1)·cw`.
- **Every dark pixel becomes a character** (`-+-+` walls) → threshold, gamma ≈ 1.25, local contrast.
- **Noise-textured subjects read as textured blobs** → silhouettes, a dark sparse background, a dot-only shadow side.
- **Particles from letter centres stack into bars** → random points inside the glyph, small, faded in.
- **Stroked atlas glyphs close their counters** (`M`, `B`) → sample a thin fill-only glyph bitmap for masks.
- **Lazily built data never reaches the exporter** → build particle schedules and their sound events before `window.EV` is exported.
- **A power-on parameter at 0 still draws the centre dot** → exposure 0 before power-on, multiply the dot term by exposure.

