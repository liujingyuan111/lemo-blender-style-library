# 流场风线 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/flow-field/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`4605fa6f3093dee6177f483d1ec5c7cea0cb7aa3aff9f7e1857f5dbb277993e9`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

- **Every line is a streamline of a real field.** Thousands of long, thin, continuous lines that never cross; their pattern *is* the information (a vortex, a jet, a sink, a wake).
- **Two layers of ink:** a fine engraved base line, and short tapered strokes that run along it, faster where the field is stronger. Motion comes from the strokes and the field changing, not from the lines jittering.
- **Warm paper, blue-black ink, one warm ramp** for magnitude. The paper is the screen; the world under the lines is printed (a chart, a landscape, a sky), not photographed.
- **The field meets things:** coasts, relief, objects and text push the lines aside. Where lines bend is where the story is.
- **Measured, then printed:** readings, legends and verdicts are printed on the world or pinned to it with a leader.

Not a particle effect (no glowing dots, no additive light, no bloom), not Data Storytelling (no axes floating on blank paper as the main picture), not Satellite Briefing (no photographs), not a weather app (no rainbow ramp, no neon on black), not a keynote (no slides, header bars, chapter numbers).

## 2. Materials & rendering

- **Field first.** Write the field as a function `field(x, y, t)` from data or a published model (wind from a best track and a parametric vortex, currents from a grid, flow round an obstacle from a potential). Never place vortices by eye. Land, relief and objects act on the field (slowing, turning, deflecting the up-slope component), not on the drawing.
- **Streamline engine (time-varying fields):** seeds are fixed points of a jittered grid *in world units*, one grid per level of detail (spacing halves each level); every line is integrated for a fixed number of RK2 steps of fixed length in both directions, with the step shrinking only near calm points. No collision tests, no early stops: each line is a continuous function of the field.
- **Level of detail:** a level's weight is 1 − |log₂(on-screen seed spacing / target)|; two neighbouring levels always sum to one, so density stays constant through any zoom. Seed spacing ≈ 36 px at 1080p and a half-length of 4 spacings give lines ~6 px apart on average.
- **Static fields** may instead use evenly spaced streamlines (Jobard–Lefer) computed once and frozen; moving obstacles then deform the frozen lines continuously (r → √(r² + k²) in the obstacle's frame).
- **Strokes:** a phase along each line's time of flight (∫ ds / f(|v|), f compressive, e.g. v^0.6) compared with one global flow clock Φ(t); a comet profile, bright head, fading tail. Lines fade at both ends (sin^0.8 taper) and inside calm cores (an eye clears by fading, not by cutting).
- **Batching:** quantise alpha (1/40) and width (1/6 px) into buckets per colour; draw runs as polylines, round joins. Thousands of lines and tens of thousands of strokes render in well under a second.
- **The printed world:** in perspective, a WebGL pass intersects each pixel's ray with the ground plane and prints paper, depth tint, land wash with hill shading and world-anchored hatching (LOD-blended octaves so it never crawls); vector layers (coast as a double line, dotted depth contours, relief contours, graticule) are projected per frame. Paper fibre and vignette are screen-space overlays.
- **Haze:** toward the horizon the ground fades into paper; the camera never shows a hard horizon line.

## 3. Colour logic

- Neutral ground: warm paper (around #ECE0C4 to #E9D3A6), land a slightly darker umber wash, water a faint cool grey.
- Ink: blue-black (around #262C38) for calm, for coastlines and for text.
- **One magnitude ramp**, ink → slate → umber → ochre → orange → vermilion, stepped at thresholds that mean something (wind grades, speed limits, safety levels). The same ramp prints the legend, so the lines are their own key.
- Vermilion is reserved for the extreme band and for the single verdict or event on screen.
- Never rainbow, never glow, never coloured paper. Land and sea are tints, not colours.

Example (our demo): grade ramp #262C38, #2C3A4A, #3E525C, #705C3A, #9E6828, #C46C26, #C83A24 on paper #ECE0C4.

## 4. Type & subtitles

- **Roles:** a CJK serif for names and headings (e.g. Noto Serif SC, 600–700); a book serif with a true italic for English and water names (e.g. Newsreader); a monospace for readings, dates and units (e.g. IBM Plex Mono Medium). All OFL, self-hosted, CJK subset to the characters used.
- **Text lives in the world:** names of seas and regions are printed on the ground plane (italic, letter-spaced); places are pinned with a small ring and a label; readings sit at the end of a leader from the thing measured; legends, curves and the title block are printed cartouches (paper fill, double rule).
- Bilingual: one language per line, Chinese above English. Chinese printed on screen is at least 34 px at 1080p, Latin at least 20 px; printed text is sized in world units for the shot where it is read. A crowded table loses a column before its type shrinks.
- **Subtitles** (when there is narration) are printed at the foot of the chart on a soft paper wash, an elliptical fade rather than a box, no outline or shadow: Chinese (CJK serif 600, ~38 px) over English (book italic, ~29 px), centred. Compose every shot so cartouches, readings and labels end above ~900 px and the wash never covers the subject.
- Hold every readable block ≥ CJK ÷ 4.5 + other ÷ 15 + 1.5 s after it is fully in frame. A rolling reading is not reported for reading until it lands.
- Keep printed text off the strongest part of the field, or give it a paper halo.

## 6. Camera grammar

| Move | What it expresses | Can serve |
|---|---|---|
| High oblique push over a calm field | scale, the quiet before | an opening; a season; a baseline |
| Orbit round a centre while descending | something organising itself | a vortex forming; a crowd gathering; a whirlpool |
| Pull-up to the whole map, north up | the path, the context | a track; a route; a spread |
| Near-nadir lock with creep | reading, judging | a legend; a comparison; a threshold |
| Dive to a grazing pass over the surface | force, contact | a landfall; a breach; a current hitting a pier |
| Top-down follow of the moving feature | travel, squeeze | a strait; a pass; a bottleneck |
| Long pull-back with a hold | aftermath, the whole story | an ending; a summary; a record |

Tilt up to ~66° with haze; at low angles lines may lift off the ground slightly (a few km in world units) to give parallax. Transitions are camera moves only: blended shot functions, no cuts to black, no dissolves between places, no page turns.

## 9. Pitfalls of the medium

- **Flicker** comes from anything discrete that changes with t: collision-terminated streamlines recomputed per frame, seeds in screen space, a level switched on or off, a step count that changes, a seed culled when it crosses the near plane. Fix: world-fixed seeds, fixed step counts, weights and fades only, conservative culling (cull by where the line can reach, clamp the LOD measure near the camera).
- **Piling at sinks:** convergent fields bunch lines into black knots. Shrink the step with the speed, fade lines in calm cores, keep line length moderate.
- **Shimmer:** 1-px lines under a fast rotating camera alias. Keep rotations slow (under ~20°/s), widths ≥ 1 px, and strokes shorter than they move.
- **Fake fields:** vortices placed by hand read as decoration. Derive the field; document the model, its parameters and what is approximated (terrain, friction) next to the film.
- **Perspective text:** plane-printed text at grazing angles is unreadable; print it for top-down shots and pin labels on low ones.
- **Rainbow ramps and glow** turn the engraving into a weather app. One warm ramp, flat ink.
- **Horizon:** a low camera shows the end of the world; haze it into paper and cap the footprint there.
- **Text over the strongest lines** gets lost; place it beside the feature with a leader, or give it a paper halo.
- **Maps of China follow the national standard map:** the South China Sea islands (Dongsha, Xisha, Zhongsha with Huangyan Dao, Nansha) are drawn and named with their standard Chinese names (pinyin in English: Xisha Islands, not Paracel), the dashed line is printed in the chart's own ink whenever its waters are in frame, the Diaoyu Islands are drawn, Taiwan carries the same land treatment as the mainland and no country name, and land boundaries are left out unless their course is certain. Island marks are symbols scaled up to stay legible; positions come from published base points or open gazetteers, cited next to the film.
- **A view that shows the South China Sea but not its southern part carries a 南海诸岛 inset**, as published maps of China do: a small cartouche in the chart's paper, ink and type, the whole sea from about 2°N to 23°N with the dashed line, the four island groups and Zengmu Ansha. Place it over empty sea or land away from the subject, the other cartouches and the subtitles. Names never sit on the dashed line or a coastline: move the label, not the line.
- **Wide shots hide what matters under cartouches:** a legend or curve placed over open water may cover islands; place it where the chart is truly empty.

