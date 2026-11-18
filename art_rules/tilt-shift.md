# 移轴微缩 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/tilt-shift/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`131ae50c6bddd30922638cbd5f2fae5c047223360a3f6924b074b0db525a5c63`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

A place seen from high up through a **tilt-shift lens**: only a thin horizontal strip of the frame is sharp, everything above and below melts into blur. The eye reads that as a macro shot of something small, so the world becomes a model. Two more things make the trick work: **saturated, sunny colour** (model-railway paint) and **time-lapse** (vehicles and people move in fast, jittery steps like wind-up toys).

Not a toy or clay render (the world is photoreal, only the lens and the clock make it small), not a game's top-down view (no UI, no clean flat shading), not drone footage (the band, the saturation and the stutter are mandatory).

## 2. Materials & rendering

- **Vantage**: always high. Oblique views at roughly 45–55° pitch from 100–200 m with a moderately long lens (~27–30° vertical FOV); straight top-down for the most "board game" look. Real tilt-shift is never shot from street level, except for a deliberate intimate moment: a true medium close-up at the actors' height, a blurred foreground object framing sharp actors who fill ~1/4–1/3 of the frame height (a long lens from high up keeps them as dots).
- **Blur band** (`demo/post.js`): physical depth of field mixed with a screen-space band. CoC in pixels = `mix(aper·(1/focus − 1/z), sign(dy)·amp·(max(0,|dy|−w)/0.5)^1.2, mix)`, clamped (~30 px). Put the band on the subject; when the subject moves, project it to screen every frame and slide the band there. Narrow the band for intimacy. Gather at output resolution after a 2× supersampled render, with many spiral taps and per-pixel rotation; far samples must not bleed onto nearer sharp ones.
- **Grade**: neutral tone mapping, strong saturation boost, soft added contrast, slightly warm highlights, a vignette. Lower saturation at night.
- **Light**: a hard sun with sharp shadows (a big shadow map fitted to each shot), a low hemisphere fill with warm ground bounce so shadows stay blue but not murky, a sky-gradient environment map for glass and paint. **Cheat the sun azimuth per shot**: each time-lapse clip is its own shot, so front-light the facades you see; one fixed sun leaves half a film backlit and grey.
- **Model-like detail** (what separates "filmed miniature" from "game CG"): facades with several window types, 1.6–3 m bays, dark reveals, world-space grime, sky-reflective glass and walls darkening toward the ground; roof clutter, awnings and signs; worn markings and stains; vehicles with dark glass, a soft contact shadow and brake lights; ambient occlusion over everything.
- **People** are small colour capsules, like model-railway figures. Actors seen up close get organic bodies with a soft sheen material and are made 20–30 % larger than real so they read.

## 3. Colour logic

- Saturated, sunny, "freshly painted model": a pale warm ground of buildings with a few candy accents, very saturated greens, dark ground surfaces so white markings and vehicles pop.
- Shadows stay blue and clean, never grey. Night and dawn are the only low-saturation states; dawn must read as early morning (a warm low fill from the sunrise side, few lit windows), not midnight.
- The subject you want found should be the one saturated thing in the sharp band, or move against the flow.
- Examples: a Mediterranean harbour (whitewash, cobalt shutters, terracotta, turquoise water); a snowy ski village (white, pine green, red gondolas, long blue shadows); a desert market (sand, saffron, indigo awnings, dusty olive).

## 4. Type & subtitles

- Subtitles belong to the world's own signage: a panel in the graphic language of the place's signs (road sign, platform board, harbour notice…), an open sign-revival font (Overpass, OFL, is a Highway-Gothic revival), sitting inside the lower blur band. Hold ≥ max(1.8 s, speech + 0.6 s).
- A **time-lapse clock** with a speed readout (e.g. `×24 TIME-LAPSE` / `×1 REAL TIME`, monospace) is the audience's speedometer for the native trick; use it whenever speed changes carry meaning.
- Titles live in the world: letters on a roof, a sign or a field, placed where nothing blocks them, lit or revealed on the beat.

## 6. Camera grammar

A vocabulary, not a route. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| High oblique wide, very slow slide | a whole system at a glance | setting a place; routine; many small actors |
| Band follows one subject across a wide | "this one" | a single commuter; a delivery; a lost child |
| Rack of the band from one subject to another | attention changing hands | cause and effect; a handover; a comparison |
| Slow push on an intersection, station or yard | a system heating up | rush hour; a festival setting up; a queue |
| Straight top-down, slowly rotating | the world as a board or machine | patterns; logistics; choreography |
| Continuous dive from high to actor height with a speed ramp | the one small thing that matters | a twist; a joke; a meeting |
| Band narrowing to a sliver | intimacy | a confession; a reunion; one decision |
| Vertical rise with logarithmic height | scale, letting go | aftermath; a summary; a system becoming a pattern |
| Lateral track along a line (rail, river, road) | a process in order | a supply chain; a parade; a race |
| Locked frame across hours | time as the actor | a construction; a market day; tide |

Framing: stay high; the sharp band carries the subject; vehicles and people stay tiny except in a close-up. Transitions: cuts on the beat, speed ramps, dives and rises; avoid dissolves that reveal the fake lens.

## 9. Pitfalls of the medium

- Tall buildings plus shallow pitch hide the ground → low to mid-rise buildings, pitch 45°+.
- The subject hides in a canyon or behind a facade → route it on the camera side and let the band follow it.
- Instance caps silently drop actors → cull by distance from the camera (≈ 4× camera height) and raise the cap.
- Simulated vehicles stop short of lines (the jam gap) → subtract it where the story needs contact.
- Focus lags a frame → update actors before the camera.
- A top-down → oblique dive twists → rotate the top-down so its screen-up matches the target shot.
- A close-up from high up is too far → go low and close, small near plane for foreground objects.
- Clouds wash out a rise → unlit white, low opacity, nothing below the camera. Light pools read as bubbles → denser, larger, fainter pools.
- Scene backlit and grey → cheat the sun per shot. Dawn reads as midnight → warm low fill, fewer lit windows.

