# 白模投影 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/white-model/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`d285018ffffd5eac5c015550d3f5ffe32bc6b6222c9e37d9a1adfe8a03d929fb`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

- **The model is real geometry of a real place**: building footprints and heights from open data (§2), extruded at a stated scale (1:1000, 1:2000…). Nothing on the model is invented or "representative", and no generated image ever stands in for the place.
- **The model is white; data is light.** Colour is never painted into the material: it is projected, so it brightens surfaces that face the projector, fades on walls turned away, stops at the edge of the throw and reaches a little onto the plinth.
- **Layers arrive one at a time**, each with its own gesture of light (a wash, a pop-on, a rising level, a moving sun), and each answers the question the last one raised.
- **A physical room**: house lights, a projector that strikes and switches, a plinth, darkness around it. Lights out is where the data starts; lights up is where it ends.
- **Every number on screen is computed from the same buildings** that are on the table.

Not Isometric Infographic (no diorama or icons), not Low-poly Island (no invented terrain), not Sci-fi Hologram HUD (no wireframes; light lands on matter), not Satellite Briefing (no imagery), not a laser-scan or point-cloud film (no scan lines; light is projected, not measured).

## 2. Materials & rendering

- **Model**: matte white (≈ #F3F3F1, roughness ≈ 0.9), crisp edges; water a darker satin inlay in the base plate; bridges low white slabs; a thin base plate on a dark satin plinth.
- **Light model**: house light = one soft key + a neutral studio environment + AO on close shots. Projection = a term added to the lit surface in the shader: `colour × (0.42 + 0.58 · max(N·toProjector, 0)) × throw mask`, scaled by albedo, reduced on water. Never a texture on the mesh.
- **Building data is the material.** First look for the place's own open 3D or footprint-with-height data: 3DBAG (Netherlands, CC BY 4.0), PLATEAU (Japan, CC BY 4.0-compatible), city open-data portals (footprints with heights or floors, zoning, plans). Fine: CC0, public domain, CC BY (credited in CREDITS and on screen). OpenStreetMap and Overture (ODbL), CC BY-SA and "no known restrictions" are not CC0: name the terms to the user and ask first. For their own site, ask the user for their data (plan, city model, survey heights).
- **Layers depend on what exists.** Construction years per building are a Dutch luxury (BAG); elsewhere they are often missing. Substitute what the data does hold and the medium can still project: heights or floor counts, footprint area, zoning or plan status, a boundary, sun and shadow (always computable). Never invent a year layer.
- **A layer is state, not a picture**: per-building attributes (year, height, rank, flags) live in vertex data; the shader decides each frame what colour the projector gives them.
- **The sun is a real directional light** with shadow maps, computed from the place's latitude and a real date and time (NOAA/Meeus solar position). The projector can trace what the sun does (a shadow footprint) but never fakes a shadow.
- **Post**: physical depth of field (stronger on close shots), bloom only above the projection highlights, vignette, light grain in ffmpeg. GTAO only on close shots: on wide grazing views it bands.
- **Screen space only for the 2D layer**: readouts, pins, measured lines and subtitles go through the camera's world → screen function so they stay pinned to the model.
- **Keep a FACTS.md in the project folder** (claim, source URL, quoted wording, or the measurement method) and deliver it with the film; every number on screen is computed by a script from the same data as the model.

## 3. Colour logic

- Neutral ground: white model, dark room (near black), dark plinth. Projector black level is a cool near-black on the plate.
- **One hue family per layer**, chosen for the data: a single categorical accent for "the old/the exception" (e.g. warm amber), a sequential ramp for continuous data (blue → cyan → white for time, violet → magenta → peach for height).
- **A colour may return** only with the same meaning (the "before" colour reused later marks the same set of buildings).
- The sun is warm, its shade is a projected deep blue; data colours are put away when the sun arrives.
- Never colour the model in the house light; never use more than two layer palettes on screen at once.

## 4. Type & subtitles

- **Roles**: a light grotesk for the figure (Inter Tight 200, 120–140 px), a sans for labels in the film's language (Noto Sans SC 300/500, 20–36 px), a monospace for instruments, years and coordinates (IBM Plex Mono, 18–22 px). OFL, self-hosted, CJK subset.
- **Readout in the left third**, one per layer: index + layer name, one figure, one label, one source line, a legend bar.
- **Pins**: a hairline from a roof or a ground point up to a tag on a dark plate (title 26 px + one sub line 20 px).
- **Identity label** top-left, quiet: place, scale, data sources.
- **Subtitles** centred at the bottom on a soft dark gradient, no box, measured with the real fonts; if the film is bilingual, the film's language on top, each language on a single line, split into two cues rather than wrap.
- Nothing below 18 px at 1080p. Hold subtitles ≥ max(1.8 s, speech + 0.6 s); labels ≥ characters ÷ 4.5 + 1.5 s (CJK), letters ÷ 15 + 1.5 s (Latin).

## 6. Camera grammar

| Move | What it expresses | Can serve |
|---|---|---|
| Macro glide at rooftop height, shallow focus | the model is a real object | an opening; a detail that matters |
| Crane up and back | the whole pattern only seen from above | revealing a hole, a cluster, an edge |
| Slow orbit with a rise | the city as a whole, layers accumulating | growth over time; comparisons across the model |
| Boom down to a low angle against black | height, skyline | tall buildings, heights, a single tower |
| Side-on track along a line | a measured distance on the model | a shadow, a corridor, a route, a view line |
| Pull back as the house lights return | the data stops; the object remains | an ending; a reset between topics |

At key moments the subject fills a third of the frame height; readouts left third, subtitles bottom centre, pins never over the readout. Transitions are light changes on one take (lights out, a layer replacing another, the projector going dark), not cuts, fades or wipes.

## 9. Pitfalls of the medium

- **Wall normals** wound the wrong way show inside faces (walls look hollow): derive the outward normal from ring orientation. **Shared walls** between parts z-fight: skip the overlap below the lower neighbour.
- **Warm HDRIs turn the white model beige**: use a neutral studio environment.
- **GTAO on wide grazing views** produces wedge-shaped dark bands; keep it on close shots only.
- **A low sun lights facades, not roofs**: shoot from the sunlit side or side-on. **Narrow shadows vanish** among all the others: trace the one that matters (fill + edge) and measure it.
- **Hairline scan lines read as laser scanning**: give every projection front a wide soft edge or switch buildings individually.
- **Floating labels**: anchor pins on the tallest part of a building, not on its footprint centroid.
- **Numbers from mixed sources** (official height vs measured roof): say which on screen ("roof", "measured").

