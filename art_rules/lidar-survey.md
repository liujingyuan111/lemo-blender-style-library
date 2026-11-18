# 点云测绘 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/lidar-survey/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`fe7034a4f7a66af8712562544e8dc33d68c25ee8cfe9975fff5d0ab98b253d28`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

- **The cloud is the data**: every point is a real return at its measured position; points appear, glow, lift away or give way to a surface, but are never moved into a shape.
- **Points become a surface**: a front (scan line, cutting plane) behind which the cloud condenses into a solid model of the same place.
- **Classification is a lever**: ground, vegetation, buildings, water are layers to peel, isolate and recolour.
- **Measurement in hairlines**: one reading at a time, in the accent, attached to what it measures; numbers from the points or an official source.
- **Dark, quiet, exact**: near-black ground, restrained colour, no glow except at the front.

Not Sci-fi Hologram HUD (no invented interface: the points are real, sparse where the survey was), not Satellite Briefing (photographs from above; here a 3D cloud flown through), not Blueprint, not Low-poly Isometric, not Glass Product Render.

## 2. Materials & rendering

- **Points**: GL points sized in world units (0.12–0.3 m), floor of one output pixel, soft discs, opaque and depth-tested (additive only for a ghost layer); colour from height or class, value from intensity; distance fog.
- **Quantise for the browser**: uint16 positions (2 cm / 1 cm) plus a byte each for height above ground, class, intensity, seed.
- **Height above ground** for every return (minus a ground model triangulated from class-2 returns) drives the colour ramp, the cutting plane and the ruler.
- **The solid surface**: a 0.5–1 m mesh of the ground or surface model, smooth normals, baked short-radius AO, a low raking sun (20–35°), faint contours, crests lightened. Display exaggeration of micro relief (×2–3) only with an on-screen note; measure on undistorted data.
- **The front**: one world-space plane (one uniform) shared by the point and surface shaders; points ahead of it brighten, a thin seam glows behind it and the surface fills in over tens of metres.
- **The cutting plane** (by height above ground): returns above it lift away and fade, a ring glows where it meets the trees, a ruler on the frame edge tracks it.
- **Marks on the surface** (traced features, section lines) are a distance field in the surface shader, kept hairline with `fwidth`; readings, leaders and charts are a 2D overlay through the same world → screen function.
- **A survey window**: outside the measured area the cloud stays as dim points instead of ending in black.
- **Post**: 2× render, high-threshold bloom (only fronts and seams), vignette; no grain (points are already fine detail; encode at a higher CRF).

## 3. Colour logic

- Background near-black with a cold tint; never pure black, never a gradient sky.
- Points: one ramp by height or class, desaturated (deep green-teal → pale; or grey → white); intensity modulates value, not hue. No rainbow elevation ramps.
- The front and seams: one cool near-white; it is light, not a colour.
- The solid surface: warm neutral (stone, clay, plaster), lit; its colour never competes with the accent.
- One accent (amber) reserved for what was found and measured: traced features, the reading, the section line. A second, cooler hue only in a comparison chart.

Example (our demo): background #05080A, canopy #1F3F35 → #5C9A7A → #E2F3DC, ground returns #C8B38C, surface #BDB5A6, front #D4FFF0, accent #FFB347, chart green #83C495.

## 4. Type & subtitles

- **Roles**: light condensed numerals for readings (110–130 px, e.g. Barlow Condensed 300); a monospace for instruments, coordinates, counts and source lines (19–22 px, e.g. IBM Plex Mono); a sans for labels in the film's language (24–36 px, e.g. Noto Sans SC 500). OFL, self-hosted, CJK subset to the characters used.
- **Instruments** in one corner: place, coordinates, area, data source, point count, any exaggeration; they change only when the medium does.
- **Readings** in the right third beside what they measure: label, number, source/method line; a leader when the feature is in frame; a rolling counter reports its landing value.
- **Subtitles**: a transcript strip bottom-left (2 px rule, plate fading right), one line per language measured with the real font, split rather than wrapped; if bilingual, the film's language on top.
- Nothing below 19 px at 1080p. Hold subtitles ≥ max(1.8 s, speech + 0.6 s); labels ≥ characters ÷ 4.5 + 1.5 s (CJK), letters ÷ 15 + 1.5 s (Latin).

## 6. Camera grammar

| Move | What it expresses | Can serve |
|---|---|---|
| Locked nadir with slow push | "this is what a photo shows" | a claim to test; a before; an ending that returns to the map |
| Crane down with tilt to oblique | entering the data; the place has height | the switch from picture to cloud |
| Low oblique close to the cloud (10–20° pitch, 90–150 m) | volume; things standing up | canopy, buildings, a facade, a cliff |
| Slow orbit | studying, the plane doing the work | a peel; a scan; a held reading |
| Rising pull-back | scale reveal of what was found | a network, a site plan, a corridor |
| Lateral track | travelling a feature | a wall, a road, a pipeline, a coast |
| Push to a section | the detail that proves it | a cross-section, a clearance, a height |

Subject ≥ a third of the frame height at key moments; readings right third; instruments in a corner; nothing in the subtitle strip. Transitions are fronts and planes, never crossfades or hard cuts inside the cloud.

## 9. Pitfalls of the medium

- **Finding data for a new place**: USGS 3DEP (US) as Entwine Point Tiles per project at `https://s3-us-west-2.amazonaws.com/usgs-lidar-public/<project>/ept.json`, projects and footprints in `boundaries/resources.geojson` of github.com/hobuinc/usgs-lidar; bare-earth scouting through the 3DEP elevation ImageServer. OpenTopography (catalogue of many collections, licence per dataset). AHN (Netherlands, CC0). National portals, e.g. England's Environment Agency LiDAR (OGL), France IGN LiDAR HD (Licence Ouverte), Spain PNOA-LiDAR (CC BY 4.0), Finland NLS (CC BY 4.0), New Zealand LINZ (CC BY 4.0); read each portal's terms. Fetch a subset by box and depth, not whole tiles.
- **Licences**: public domain, CC0, CC BY and attribution-only government licences are fine, with credit in `CREDITS`. ODbL, CC BY-SA, "no known restrictions" (not CC0) or non-commercial terms: name them to the user and ask first. Never commercial scans or Google 3D tiles. Ask the user for their own scans (a site survey, a drone or terrestrial scan, their BIM) when the film is about their asset. Never stand in a generated or invented cloud for real evidence.
- **Facts**: keep a FACTS.md in the project folder (claim, source URL, quoted wording, or the measurement method) and deliver it with the film.
- **Coordinates**: EPT copies are often Web Mercator: convert to a local east/north/up frame first; check the vertical datum against known ground.
- **Leaf-off vs leaf-on**: leaf-off lidar reaches the ground but its canopy is sparse; say which season each layer is.
- **Classification is the provider's**: class 1 mixes vegetation, buildings and noise; drop 7 and 18; finish a cut below 0 m or low vegetation stays as stripes.
- **A dense cloud reads as a flat carpet** from afar: go close and low for volume; let the distance fog out.
- **Scan striping** is real texture; don't frame a reveal on it at grazing angles.
- **Traced features are interpretation**: say "traced", keep the tracing in a data file, snap it to the data, leave faint candidates out.
- **Privacy**: crop out houses and yards; keep the survey window on public or uninhabited land.

