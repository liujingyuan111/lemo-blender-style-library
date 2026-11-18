# 热成像 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/thermal-camera/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`b6af38ba920121ef8b764831514b7c917ed24beadcb86e7d8a63f54fa47f45ae`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

- **Temperature is the picture.** Every pixel is an apparent temperature mapped through one palette and one scale; brighter means warmer, always. Nothing is coloured for drama.
- **It looks like a sensor.** A coarse grid (320×240 or 640×480 class, cropped to 16:9) blown up to the frame, optical softness, temporal noise, column stripes, lens shading. Never a clean gradient.
- **Physics decides what glows.** Surfaces get temperatures from heat flow (indoor vs outdoor, thermal bridges, leaks, bodies, engines), then emissivity and reflection decide what the camera reads: glass and bare metal look cold because they mirror the sky.
- **The instruments are diegetic.** Colour scale with its range, spot meters, boxes with max/avg, isotherm, hot-spot tracker, time stamp: the camera's screen, not a slide.
- **Two eyes, one place.** The visible picture is the baseline; the thermal picture is the revelation. The switch between them is a native move.

Not Sci-fi Hologram HUD (no glowing wireframes, no invented sci-fi chrome), not Data Storytelling (no charts on paper), not a neon colour grade (no false colour without a scale), not Under the Microscope (no lab optics).

## 2. Materials & rendering

- **Two passes, one camera.** A picture pass (PBR, real lights, night or day) and a thermal pass in which every material writes °C into a float target. The composite chooses per pixel: picture, thermal, or a split.
- **Thermal materials**: a surface temperature model (steady-state wall: T_out + ΔT·U·R_se; bridges as bands; local sources as Gaussians; plumes as animated noise), then `apparent = ε(θ)·T + (1−ε(θ))·T_reflected`, with emissivity falling off at grazing angles and the reflected scene temperature from the view's mirror direction (cold overcast sky above, snow or ground below). Glass ε ≈ 0.84, paint/brick/skin 0.9–0.98, bare metal 0.1–0.3.
- **Sensor simulation** in screen space: render the thermal pass at ~3× the sensor grid, integrate with an optics blur into the sensor resolution, add temporal noise (~0.1 °C), fixed column/row patterns and corner shading, read the sensor back for all measurements, then upsample with bicubic and a mild detail enhancement. Optional edge overlay from the thermal depth buffer (never from the picture, which carries snow, rain or bokeh into the heat image).
- **Transparent heat** (exhaust, breath, steam) blends in temperature space: alpha-composite °C, not colour.
- **The picture pass must hold up on its own** (real light sources, believable materials); the thermal reveal is only as strong as the baseline.

## 3. Colour logic

- One palette per film (iron: black → indigo → purple → magenta → orange → yellow → white).
- The scale (level and span) is part of the story: wide span for overview, narrow span to reveal faint structure, the same scale when two images are compared. Out-of-range values clip to the palette ends.
- The isotherm owns one colour outside the palette (a saturated green) and means only "above the threshold".
- Overlay graphics are white with a dark halo; a single accent (pale green) is reserved for a verdict.
- The visible picture keeps natural colour; it is never tinted to match the heat.

Example (our demo): palette stops #000008 #120554 #4D0894 #991294 #DB3352 #FA7812 #FFBF21 #FFFADB; isotherm #2BD14A; verdict border #7DFFA0.

## 4. Type & subtitles

- **Roles**: a monospace for readings, scale ends, time stamp and measurement names (IBM Plex Mono, 22–40 px); a sans for labels (Noto Sans SC for Chinese 24–40 px, Inter for English 20–32 px). OFL, self-hosted, CJK subset to the characters used.
- **Labels belong to the camera or to the world**: a spot meter's value sits beside its crosshair; a label hangs on a leader line to the thing; the scale and the time stamp sit at the frame edges. No title bars, no centred captions.
- Bilingual labels are two lines, one language each. Numbers keep one decimal and flicker in the last digit at the meter's refresh rate; the value registered for reading time is the measured median.
- Nothing below 20 px at 1080p. Each label holds ≥ max(1.5 s, characters ÷ reading speed + 1.5 s) (CJK 4.5 chars/s, Latin 15 chars/s), measured from the moment it is fully on screen.

## 6. Camera grammar

| Move | What it expresses | Can serve |
|---|---|---|
| Scan line across a locked or slowly pushing frame | the invisible becomes visible | an opening; a reveal; a return to the ordinary picture |
| Fixed split with the camera trucking past | what the eye sees vs what the camera sees, side by side | hidden structure in walls, machines, bodies |
| Zoom / push onto one reading | inspection, suspicion | a defect; the hottest point; a single number |
| Crane or tilt over an edge | survey, extent | roofs, fields, an assembly line from above |
| Low push onto a living thing | warmth, life | an animal, a person's hands, a sleeping child (if people are allowed) |
| Locked twin frame (same scale) | judgement | before/after; this vs that; good vs faulty |

Framing rules: the subject that carries the reading sits away from the scale bar (right edge) and the time stamp (bottom left); readings never cover the hot spot they measure. Transitions: scan lines, splits, level/span changes, the shutter freeze of the detector; cuts on beats. No cross-dissolves between visible and thermal; no wipes that are not a sensor action.

## 9. Pitfalls of the medium

- **Glass is not transparent.** Infrared does not see through windows; lit rooms look no warmer. Never show interiors through glass in the thermal pass.
- **Reflections lie.** Shiny metal and glass show the sky's cold or a lamp's heat, not their own temperature. Measure on matte, high-emissivity surfaces, or say what is reflected.
- **Too clean reads as CG.** Without noise, optics blur and a coarse grid, the image looks like a gradient render. Simulate the sensor, then upsample.
- **Moiré from fine geometry** (railings, grilles, branches): supersample the thermal pass and blur before decimating to the sensor grid.
- **Numbers must match colours.** Read every value from the same temperature buffer that is coloured; register the measured median for reading time; keep the scale range visible whenever a value is shown.
- **Comparisons on different scales are meaningless.** Lock level and span before judging.
- **Trackers must not chatter.** The per-frame hottest pixel is noisy: two equally warm spots (two eyes, two bulbs) swap places from frame to frame and the marker jitters by whole sensor pixels. Find the hot point once from the buffer, pin the marker to that point on the object (in world or object coordinates) and let it ride the camera; only the reading refreshes.
- **Thin hot features vanish at distance.** A crack or a gap one sensor pixel wide reads cooler from far away; frame closer or use a box maximum.

