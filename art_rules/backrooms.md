# 后室录像带 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/backrooms/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`2a3697a1ce37d0fbae3281220ae6154eeb9789233f1fae472d55ac169ba26fb4`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

- **One first-person camcorder recording** (1990s VHS, 4:3), handheld, continuous.
- **An empty, familiar-but-wrong interior** that repeats: an office, a hotel floor, a school, a mall, a parking level, a hospital wing. Humming fluorescent light, no people.
- **Dread from emptiness, repetition, bureaucratic rules, and the camera's own machinery failing at the wrong moment.** Nothing chases anyone. A chill on the back of the neck, not a jump.
- **The medium is the storyteller**: focus, exposure, tape damage and the on-screen display carry the plot.

Not a horror film (no monster close-ups, no gore, no jump scares, no score stings), not an ASCII/CRT terminal piece (the artefacts are tape and lens, not phosphor and scanlines), not a ruin (clean is part of the style).

## 2. Materials & rendering

- **Frame**: 4:3 pillarboxed in 1920×1080. Render 3D at low resolution (e.g. 720×540) and let the VHS pass upscale; low resolution hides CG cleanliness.
- **Space**: axis-aligned partitions on a grid with random gaps and stubs, pillars, a drop ceiling of tiles with recessed light panels at regular intervals. A hand-authored route through procedurally filled space, so every doorway shows more emptiness.
- **Lighting = thousands of lights, no shadows**: store every panel's colour and intensity in a float texture; each fragment sums the nearest panels (emitter cosine × Lambert / (d² + ε)) plus a bounce term. No occlusion: this light is flat. Per-light variation (a few % warm/cool/green), a few % dead, a few % flickering. Ambient occlusion darkens seams.
- **Fog follows local light**: fog colour × (local light / average). Where lights are dead the haze is dark, so a silhouette there reads as a *hole in the light*. Background = fog × ~0.15, so corridors dissolve into darkness, never a bright wall.
- **Restrained decay**: tide-marks at the foot of some walls, a discoloured band under the ceiling, rare peeling seams, a few yellowed or missing tiles, dead insects in diffusers. Percentages in single digits.
- **Printed matter**: office laser-print on yellowed paper, condensed sans headers, form numbers and revisions, numbered rules, a polite closing line from "Management". Pinned or taped.
- **VHS camcorder pass** (not a CRT): small line jitter (≤ 0.25 px low-frequency wobble), a head-switching band, tracking tears on demand, barrel + vignette on the image but **not** the OSD, luma blur + edge ringing, chroma smeared right, light smear, drifting white balance, AGC noise in darks, dropouts, lifted blacks, soft clip. Noise at tape rate (30 fps). No scanlines, no RGB mask.
- **OSD**: a hand-made bitmap font with a black outline: REC dot, battery, time and date. A camcorder title generator uses the same font, larger.

## 3. Colour logic

- **One dominant sickly hue** from the location's materials (mustard wallpaper, institutional green, hospital blue, beige laminate), with a darker trim and a mottled floor of the same family; ceiling and light panels near-white and slightly warm.
- **Exactly one saturated colour**: a signal such as a red alarm lamp, a green emergency sign, an amber warning light. It is the only thing that blooms (drive its emissive high enough to cross the bloom threshold).
- White balance drifts; colour is never graded clean.
- Example material palettes: wallpaper `#d5bd66`, trim `#4d3d26`, carpet `#8c763c`; pool tile `#9fc7c0`, grout `#e6ece6`, water `#5e8f96`; school corridor `#b9c49a`, lockers `#6f7f66`, linoleum `#a89a7d`.

## 4. Type & subtitles

- **Closed captions (CEA-608 style)**: a monospace (e.g. IBM Plex Mono 600) ~42 px, white on a solid black box per row, ≤ 32 characters, centred inside the 4:3 frame above the OSD. Untouched by tape noise (the TV decodes them). Hold ≥ max(1.8 s, speech + 0.6 s).
- **Speaker marks**: `[PA]` for announcements, italics for the operator, SDH descriptions in brackets (`[LIGHTS FLICKER]`, `[TAPE NOISE]`, `[SILENCE]`).
- **Rules on notices are not captioned**: they are the picture. Readable at 1080p, ≥ 3–4 s uncovered. For close-ups **lower the camera so the lens is parallel to the page**; pitching down at a vertical sheet shears words into fake italics.
- The **title** is camcorder title-generator text over the first shot.

## 6. Camera grammar

A vocabulary, not a route. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Walking POV down a corridor | routine, the endless | establishing the space; time passing |
| Slow pan off a detail to the space | scale; the space goes on | a reveal; a first look |
| Glance down at the feet | obedience, avoidance | obeying a rule; not looking |
| Crouch and hold on printed text | reading; bureaucracy | a rule; a contradiction |
| Zoom + focus hunt into the distance | seeing / not seeing | a presence; a doubt |
| Identical framing after a tear, only the OSD changed | time removed | a jump; a loss |
| Turn a corner, hold still | a threshold | an exit; a choice |
| Slow push-in with no sound | the pull of something | a door; a sign |
| Backing away while filming | retreat, fear | leaving a room; a rule broken |
| Camera set down on a surface, static, recording alone | abandonment | the operator gone; a long wait |
| Whip toward a sound, then nothing | expectation denied | a noise with no source |

Framing: text readable and uncovered; any presence small, far, and in a region of dead lights. Transitions: tape events only.

## 9. Pitfalls of the medium

- **A fully bright scene reads as a hospital corridor** → partitions with gaps; far areas fall dark.
- **Lights leak through walls** (no occlusion) → a dead zone needs every light within ~±5 m dead, and the space behind it dim.
- **Background shows as a bright rectangle** at a corridor's end → background = fog × ~0.15.
- **Uniform fog lifts silhouettes to grey** → fog follows local light.
- **Line wobble skews text; pitching down italicises it** → ≤ 0.25 px wobble; lower the camera.
- **Primitive-built figures read as toys**, primitive legs as tubes → organic silhouettes; show only shoe toes.
- **Pure red never blooms** at low emissive (low luminance) → drive it far higher.
- **Normalising a filtered signal by its pre-filter peak** blows up a bus → normalise the processed signal.
- **Heavy PA reverb destroys intelligibility** → ASR-check processed lines and the full mix.
- **Billboards stamp dark rectangles** in AO → exclude them.
- **Time-compressing a finished timeline** → keyframes in original time mapped through one warp function, including hard-coded times elsewhere.

