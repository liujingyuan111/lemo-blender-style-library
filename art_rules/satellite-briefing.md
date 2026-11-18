# 卫星简报 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/satellite-briefing/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`659e1d33189f252cec629685c60fc9b495d1c6f6679c5c8791b37b1192a3147f`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

- **The ground is a photograph**: real, licence-clean, georeferenced satellite or aerial imagery of the actual place. Nothing on the ground is drawn, stylised or generated.
- **Two layers, two truths**: the imagery is what the satellite saw; the hairlines are what the analyst measured. Marks are thin, white, sparse, and sit on real coordinates.
- **The grade moves with the story**: orbit in true colour, the analysis layer in grey, colour back only where the story turns.
- **Scale is the camera**: one zoom from orbit to the ground built from nested plates, with an altitude readout and a scale bar from the same camera.
- **One finding per screen**, in the single accent colour.

Not Data Storytelling (a chart on paper), not Sci-fi Hologram HUD (no glowing wireframes or invented chrome), not Blueprint, not Isometric Infographic (real nadir or oblique views, no diorama), not a keynote (no slides, header bars or chapter numbers).

## 2. Materials & rendering

- **Plates**: georeferenced rasters with a lon/lat box, sampled in a shader where the camera ray hits the ground, nested by resolution (world → region → detail) with feathered edges so finer plates dissolve in as the camera descends.
- **Globe**: ray–sphere from a perspective camera, a thin atmosphere rim, limb shading at orbit only; compute |C|² − R² in double precision (float32 fails below a few tens of km).
- **Time**: dated plates share one grid. A soft scan front (a satellite pass, never a hairline) swaps them: north → south forward, south → north for a rewind. Growth can run outward from the old edge, ordered by a distance map.
- **The analyst's grade** (one uniform from colour to grey): luminance with local contrast and clarity, a shoulder so salt, snow and cloud stay below white, toned blue-black → cool silver up to ~65 % grey, a fifth of the chroma. White belongs to the marks.
- **Marks**: a 2D overlay through the same world → screen function: hairlines 1.2–2.6 px with a dark halo, dashes for history and claims, brackets, ticks, leader lines. Lines draw on; outlines print behind the scan.
- **Screen space only for instruments** (altitude, scale bar, imagery credit) and the transcript strip. Everything else is anchored to the ground.
- **The claim layer** is a printed map drawn in the shader from a distance field of the old outline: paper grain a few pixels wide at any zoom, halftone ink, coast and waterlines, graticule, the serif name.
- **Post**: light grain in ffmpeg, a vignette, directional blur only on whip pans.

## 3. Colour logic

- Neutral ground: grey, roughly 3–65 % in value. White means *measured*.
- One accent (warm, e.g. amber) for the single reading on screen, never decoration.
- A second hue may mark the **claim** the imagery tests (a map, a plan, a promise): flat, cartographic, never used for anything measured.
- True colour is evidence: at orbit, and again only where the story turns (the field that greened, the water that returned).
- No false-colour ramps over the imagery.

Example (our demo): ground #070B0E → #A1A7A9, marks #F2F5F6, reading #FFBE55, map blue rgb(46, 112, 206).

## 4. Type & subtitles

- **Roles**: a light condensed grotesk for the reading (96–130 px, e.g. Barlow Condensed); a monospace for instruments and dates (20–34 px, e.g. IBM Plex Mono); a sans for labels in the film's language (24–42 px); a serif only for the claim layer and the title. OFL, self-hosted, CJK subset to the characters used.
- **Labels attach to the ground** with a leader line. The reading sits in the right third beside what it measures, label above, source note below ("Landsat, measured").
- **Subtitles are a transcript strip** at the bottom left: a 2 px white rule, a dark plate fading right, left-aligned, each line on one line (measure with the real font, `nowrap`; split a long sentence into two cues). If the film is bilingual, the film's language on top.
- Nothing below 20 px at 1080p, the imagery credit included.
- Hold subtitles ≥ max(1.8 s, speech + 0.6 s); a rolling counter reports its landing value; labels stay ≥ characters ÷ 4.5 + 1.5 s (CJK).

## 6. Camera grammar

| Move | What it expresses | Can serve |
|---|---|---|
| Oblique orbit, limb in frame | scale, context, distance | an opening; a return; a title card |
| Dive (log zoom, tilt to nadir) | going to look for yourself | a reveal; checking a claim |
| Locked nadir frame, slow creep | evidence, comparison | time running in one place; a measurement |
| Push-in on a point | singling out | one town, one dam, one field |
| Track along a line | travelling a distance | measuring; a river, a road, a border |
| Whip pan with blur | a new subject at the same altitude | the counter-example; "meanwhile" |
| Climb back to orbit | consequence, perspective | an ending; a summary |

At key moments the subject fills a third of the frame height; reading right, subtitles bottom left, instruments in the corners. Transitions: scan-line swaps, a map layer switched off, zooming through plates, whip pans, the reticle opening into a title card. No crossfades between unrelated places, no hard cuts inside a zoom.

## 9. Pitfalls of the medium

- **Licences**: not usable: Google Earth/Maps, Bing, Esri World Imagery, Mapbox Satellite, Planet, Maxar, news photos, AI-generated imagery. EOX Sentinel-2 cloudless is CC BY 4.0 only for 2016 (2018 onward is NC). Raw Copernicus Sentinel data need "Contains modified Copernicus Sentinel data [year]"; check the user's rules. Public domain or free with credit: USGS Landsat (1972 on, worldwide), USGS NAIP (US, ~1 m), NASA Blue Marble, MODIS, VIIRS. Burn a readable credit into the picture and list every asset in `CREDITS`.
- **Finding imagery for a new place**: search by bounding box and date in the Planetary Computer STAC (Landsat C2, Sentinel-2 L2A; no account) or USGS EarthExplorer; MODIS/VIIRS and Blue Marble from NASA GIBS; coastlines, lakes and rivers from Natural Earth (borders and China: DIRECTOR.md §13). Log every request. OSM (ODbL), CC BY-SA and "no known restrictions" are not CC0: name the terms and ask the user first. Ask for the user's own surveys or GIS layers when the place is theirs. Never fill a gap with generated imagery presented as evidence.
- **Seams**: paths imaged on other days disagree. One date per path, each scene gain-matched on stable land, feathered overlaps, holes filled from the same year only.
- **Old sensors**: Landsat MSS (to 1992) has no blue or SWIR and drops scan lines: nearest-neighbour resampling, near-zero rows as nodata filled from same-year scenes, scan-angle streaks cleaned on land only. Inspect every year at full contrast.
- **Plumes and haze** cross water as bright diagonal bands: swap the scene for another date of the same year rather than painting it out.
- **Edges**: resampling against nodata darkens scene rims (erode the mask); drop contour pieces along a plate border. Real straight edges (dikes, polders) can read as seams: frame them out or label them.
- **Grey mush at close range**: raise local contrast for that altitude only and dim outside the measured corridor.
- **Water and cloud**: MNDWI where shortwave infrared exists, only the basin you measure; clouds read as features in grey, so use the dry season.
- **Facts**: keep a FACTS.md in the project folder (claim, source URL, quoted wording, or the measurement method with scene IDs and dates) and deliver it with the film. Measure on the date you show.

