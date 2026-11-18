# 笔式绘图仪 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/pen-plotter/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`6b4b45210d953e8ddee6741e7866b5cc7ad0a7fc37926b8cb7554f7209345412`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

- **Every mark is a stroke.** Nothing appears that a pen could not have drawn: no fills, no gradients, no type set as a font. Tone is hatching; weight is a wider nib or the same stroke traced twice; letters are single-line strokes or traced outlines.
- **The machine is in the shot.** Gantry, carriage, pen holder and pen rack are physical objects with weight; the pen is where the line ends.
- **Machine time is honest.** Pens move at plotter speed with acceleration and braking, drop and lift, and go to the rack to change. Time is saved by editing and by the camera, never by a pen that flies.
- **Information design made by hand.** The sheet is a real document (a map, a chart, a comparison, a number), drawn in plotting order, so the order of drawing is the order of the argument.
- **Few inks, each with a job**, on cream paper under one warm lamp.

Not Blueprint (no white-on-blue, no CAD chrome), not Data Storytelling (no screen-space charts that grow by tweening), not Whiteboard Explainer or One-line Drawing (no hand, no marker; the line is mechanical, not gestural), not Engineering Briefing Board (the sheet is being made, not presented).

## 2. Materials & rendering

- **Strokes are data.** Every mark is a polyline in sheet millimetres, in plotting order, tagged with its pen. A program turns the list into machine time: pen-up travel, drop, ink, lift, pen changes. One function gives the pen's position and how much ink is down at any machine time.
- **Kinematics**: trapezoidal velocity per move. Reference values: pen-down ≈ 60–125 mm/s, pen-up ≈ 200–300 mm/s, acceleration ≈ 1000–2500 mm/s²; drop and lift ≈ 0.07–0.1 s; a pen change ≈ 2–4 s (travel to the rack, lower, release, move one stall, lower, grip, raise).
- **Paper**: a canvas texture of the whole sheet (≈ 10 px/mm) plus high-resolution patches (20–40 px/mm) only where the camera is close; ink drawn with multiply blending, round caps; a slightly wetter dot where a pen lands; paper grain and a few fibres as a bump map. Going back in time redraws from scratch; going forward draws incrementally; the stroke under the pen is drawn partially.
- **Ink**: semi-opaque, never pure black; light inks (grey) at 0.6–0.75 opacity; strokes traced twice read darker, as on paper.
- **Machine**: rails, a moving beam, carriage, Z holder with a gripper, drag chain, a rack of capped stalls; metals with roughness 0.15–0.35, matte plastics, clearcoat pen barrels colour-coded to their ink. Cast shadows from one lamp are part of the look.
- **Lettering**: a single-line font (one stroke per subpath) for Latin and figures; CJK as the outline of a hairline-weight font drawn with a pen wider than the stroke, so it reads as single-line; display titles as outlines filled with fine hatching.
- **Screen space only for the end card**; everything else is on the sheet or in the room.
- **Post** (reference): supersampling, depth of field from a physical aperture, light ambient occlusion, a warm vignette, a little bloom on metal.

## 3. Colour logic

- Neutral ground: cream paper (≈ #F1ECDF) under a warm lamp; the room falls to near-black with one cool counter-light (a window).
- One ink per job, three to four inks at most: a dark ink for the frame and text, a terrain or data ink, a light ink for tone and grids, and **one accent reserved for the finding** (the path, the answer, the circle around the result).
- The accent appears late and on purpose; it never fills an area except by hatching.
- Pen barrels carry their ink colour, so a pen change reads at a glance.

Example (our demo): black #16161C, sepia #763C1A, grey #686662 (70 %), red #CC221A.

## 4. Type & subtitles

- **Roles**: single-line sans for figures and Latin labels (2.5–10 mm on the sheet; 40–50 mm for a hero number); hairline CJK labels 3–5 mm; a hatched serif for the sheet title. All OFL, subset to the characters used; letters are baked into stroke data, the page loads no font.
- **Labels live on the sheet**: next to what they name, one language per line (Chinese line, then English line, then the value), never in screen space.
- **Weight by retracing**: titles and key values drawn two or three times with a 0.2–0.3 mm offset.
- **Legibility**: anything to be read must reach ≥ 30 px cap height at 1080p when the camera holds on it; small legend text may stay unread.
- Hold readable text ≥ CJK characters ÷ 4.5 + other characters ÷ 15 + 1.5 s, measured from when its last stroke is drawn.

## 6. Camera grammar

| Move | What it expresses | Can serve |
|---|---|---|
| Macro on the nib, paper fibre in focus | the act of drawing; precision | a first line; a last stroke; a value being written |
| Overhead pull-back during jump-cut time-lapse | a whole emerging from strokes | a map filling in; a chart building; a pattern spreading |
| Low angle across the paper | the sheet as landscape | relief; depth; a reveal of scale |
| Long lens following the pen | travel, a path, sequence | a route; a timeline; a process step by step |
| Locked three-quarter on a panel, slight creep | reading, judging | a comparison; a verdict; a legend |
| Insert at the pen rack | a change of subject or voice | a new layer; a new data series; the answer's colour |
| Pull-back from the sheet to the desk and room | context, the work done | an ending; a reveal of the whole document |

Keep the carriage from covering what must be read: frame from the side the beam is not on, or wait until the pen has left. Cuts happen on beats or on a pen drop. No crossfades, no page turns, no screen-space titles.

## 9. Pitfalls of the medium

- **Flying pens.** Speeding the plot to fit the film reads as animation. Keep real speed and jump between stretches; a full sheet can take an hour of machine time.
- **The carriage hides the work.** It sits above the line being drawn; frame from the open side, hold until it leaves, or show the result from a different shot.
- **Beam shadows.** One lamp casts the beam's shadow as a hard bar; place the lamp on the camera's side of the beam for reading shots.
- **Thin lines vanish in wide shots** (mipmapping). Use darker inks, retrace key lines, keep wide shots for shapes, close shots for text.
- **Fat lines in 3D.** World-unit line widths grow huge near the lens; use screen-space widths for lifted strokes.
- **Fonts that are fills.** Outline fonts drawn as outlines look like stencils; use single-line fonts, or hairline weights narrower than the pen.
- **Made-up data on a "real" map.** If a sheet looks like a survey, its data must be real (DEM, published figures) and its sources in FACTS/SOURCES; mark approximations on the sheet.
- **Partial redraw cost.** Big canvases must be drawn incrementally and reset only when time runs backward.

