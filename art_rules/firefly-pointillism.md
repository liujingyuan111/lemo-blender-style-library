# 萤火光点 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/firefly-pointillism/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`15ab75f6b7f2eebbf24471edb9d4050c2b4db6c8699727a43a9de2dc8c2c6c59`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

- **Black is more than half the frame.** All light comes from the points themselves: no ambient light, no gradient sky, no solid surfaces.
- **Everything is the same kind of point.** Characters, grass, moon, stars, rain and titles come out of one renderer and differ only in colour, density and focus.
- **Depth is size and blur.** In-focus points are small and sharp, out-of-focus points become large, faint discs. Particles pulling from blur to sharp *is* focusing, and focusing is how a form appears.
- **Forms are outlines.** A character is a dotted silhouette (dense outline points, sparse fill), read through pose and action, never through a face.
- **Conservation.** One pool of particles for the whole film; every point is always something (a river → a road → a crowd; falling snow → a city's windows → the title). This is what lets every transition flow instead of cut.

Not a digital-rain, hologram or dark-keynote look (no cold blue, no wireframes, no tech); not a particle-logo reel (there are characters and a story); not a fluid gradient; not iron filings or hard pixels. The points are always round, soft and warm.

## 2. Materials & rendering

- **Splatting into five blur levels**: σ ≈ 1.0 / 2.1 / 4.8 / 10.5 / 23 px, rendered at 1 / 1 / ½ / ¼ / ⅛ resolution; each particle carries a fractional blur level and is split between the two neighbouring levels, so focus can be pulled continuously. Energy gain per level `[1, 1.55, 2.7, 5.2, 10] / res²`, so large bokeh is bigger and fainter at once.
- **Halo**: each point puts ~16 % of its energy two levels up, so bright points glow.
- **Exposure and tone**: linear light × exposure, `1 − exp(−x)`, gamma 2.2. Point cores burn towards white and the edges keep their hue.
- **Motion blur**: a 180° shutter; each point is drawn as samples between its positions at the two ends of the shutter, so fast flight turns into light streaks by itself. Points that wrap around the frame (rain, flows) must not draw a streak across the screen.
- **Grain**: very light, darker areas slightly more, plus 1–2 LSB dither against banding. Heavy grain multiplies the file size.
- **Characters**: a 2D bone rig (tapered capsules and polygons). Points are bound to normalised local coordinates on each part, so poses, scale and mirroring never resample. Outline points that fall inside another part on the same or a nearer layer are dimmed to a few percent (union silhouette); without this the figure reads as a wireframe.
- **Positions are functions of time**: every group has a state function per scene and transitions blend per particle with staggered delays. Any frame renders alone, in any order (parallel and reproducible). The particle count must be identical at every time.

## 3. Colour logic

Linear colours times brightness; the screen shows a mid tone and a burnt core for each.

| Role | Linear | Mid tone | Core |
|---|---|---|---|
| Ground (top → bottom) | (.00016,.00034,.00052) → (.0003,.00062,.0004) | `#050708` → `#060907` | — |
| Protagonist (exclusive) | (1.0, .74, .34) | `#B2A076` | `#F5ECC6` |
| Companion (exclusive) | (.78, 1.0, .46) | `#A3B286` | `#EEF5D6` |
| Fireflies, ambient lights | (.86, 1.0, .40) | `#A6B279` | `#F0F5C8` |
| Landscape (ground cover, hills) | (.32,.62,.20) → (.62,.88,.30) | `#73965F` → `#96AA70` | — |
| Weather (cloud, rain) | (.40,.54,.50) / (.66,.82,.74) | `#8A9893` | — |
| Stars (cold) | (.86, .90, 1.0) | `#A6AAB2` | `#F0F2F5` |
| Titles | (1.0, .90, .58) | `#B2AB92` | `#F5F2E2` |

- One warm yellow-green family. **Each character owns one colour and keeps it through every transformation**: after a scatter and re-gathering, the audience recognises who is who by colour alone. Colours are never swapped.
- Cold colour only for stars and rain, under 5 % of the frame. No pure white, no saturated red or blue.

## 4. Type & subtitles

- **Titles and credits are made of points**: the text is rendered to a mask and sampled on a jittered grid (not randomly), one particle per sample. A 140–170 px CJK title needs about 3,400 points, a 30–40 px Latin line about 800; sparser and the strokes stop reading. Once landed, the text holds absolutely still (sub-pixel shimmer only), with a short flash on landing. Place it in empty sky, left-aligned, never centred over a character, never on a plate.
- **Subtitles** are plain type burned in (legibility first), a soft brush-like CJK face such as LXGW WenKai (OFL): Chinese ≈ 40 px in warm cream, English ≈ 28 px a little dimmer, centred at the bottom, no outline, no plate, only a faint glow of the same colour. Keep every subject above the subtitle band.

## 6. Camera grammar

A 2D camera on the particle world, with parallax by depth layer (screen offset × (1 + 0.38 × depth)).

| Move | Meaning | Use for |
|---|---|---|
| Slow push | closeness, attention | an encounter, a held light |
| Lateral tracking with parallax | travelling together | a walk, a ride, time passing |
| Locked wide shot | smallness, quiet, reading time | titles, farewells, a lone figure |
| Focus pull (bokeh → sharp) | appearing, "it is real" | a character forming |
| Fast pull-back | reveal of scale | a crowd revealed across the whole horizon |
| Whole-scene re-forming | a change of place without a cut | travel, time jumps, a final tableau |

**Transitions happen only inside the medium**: a flow pours in, a swirl gathers, a gust blows the scene away and it re-forms elsewhere, lights go out, the world re-forms upward. No hard cuts, dissolves or page turns.

## 9. Pitfalls of the medium

- **Green fog**: background bokeh, out-of-focus grass and fireflies add up to a haze and the black is lost. Keep fireflies mostly dark, background bokeh at 0.1–0.38, near blurred grass around 0.2.
- **Walls of light**: distant points on one horizontal line read as a lit wall; give them height above ground and random depth, and soften ripple fronts.
- **Hard distribution edges**: a uniform random band draws a visible line; use power-law vertical distributions.
- **Unreadable characters**: fill points alone are a cloud; outlines need about 0.7 points per pixel and occlusion culling. A standing animal seen from the side hides its far legs behind the near ones: stagger the feet so all four read.
- **Shapes dissolving at the peak**: a per-particle scatter on a big character turns it into a column of dots; for a hero action, move the rig and keep the shape.
- **Unreadable text**: random sampling or moving after landing; sample on a jittered grid and freeze.
- **Low-resolution levels**: energy splatted at ⅛ resolution must be divided by res², or the frame turns white.
- **Variable counts**: optional flashes must be fixed slots with zero brightness, or the two shutter evaluations differ in length.
- **Delays from in-flight positions**: compute a transition's delays from settled positions, not from the moving ones, or the points jitter.
- **Grain = bitrate**: per-frame random grain at 1 % makes the file ten times larger.

