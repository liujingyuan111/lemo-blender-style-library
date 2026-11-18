# 孟菲斯微缩景观 · 原文美术章节

来源：Memphis Diorama by EianLu, in Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/memphis-diorama/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`7f1748f2741d069e074172800d501ec00527db8a018e1e5ab4ecfa630ed6763b`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

- **Paper and a grainy frame.** A warm white ground; the picture lives in a rounded, organic frame whose edge dissolves into grain. It grows open from the centre at the start and draws back in at the end.
- **Memphis flat colour.** Saturated primaries plus pastels, flat fills, no gradients; a deep-indigo ink outline; small patterns tiled on surfaces (dots, stripes, zigzags, terrazzo flecks, halftone).
- **The eye of a model-maker.** High three-quarter, top-down or cutaway views. The film always looks at a *place*, never at a person.
- **Small motions everywhere.** Water, wind in trees, cloud shadows, birds, boats, walkers, lights coming on one by one. The place is alive because of them, not because of a protagonist.
- **Three lines of type under the frame**: title / one sentence / small data, under three Memphis marks (a yellow dot, a pink triangle, a blue zigzag). Bilingual words take two of them, one Chinese line and one English line (§4).

Not character animation: nobody acts. Code-made faces, gestures, getting in and out of cars always look stiff, so this style never shows them. Not an isometric infographic (that one is cool and diagrammatic; this one has weather, seasons and sound). Not tilt-shift (no photograph, no depth of field: everything is flat and sharp). Not low-poly (no faceted shading or plastic highlights: flat fills, outlines and patterns do the work).

## 2. Materials & rendering

- **Three tones only**: the top face is the brightest, sun-facing sides keep the base colour, the faces turned away drop to about ×0.5–0.95. Hard edges between faces, never smooth shading.
- **Hard shadows**, never blurred, tinted cool purple (shadow ≈ base × (0.70, 0.58, 0.90)); the sun direction never changes within a film.
- **Halftone in the shade**: inside shadows, a staggered grid of lighter dots in world space, like a print. It turns dark areas into texture instead of dirt.
- **Outline as a post pass** from normals and depth: about 2 px deep indigo `#25214A` at 1080p. Light cones, decals, particles (rain, snow, petals, smoke) and thin stems carry no outline; a thin object that is all outline reads as an ink scribble.
- **Patterns belong to the world**: dots and stripes are computed from world coordinates and stay on the object as it moves. Pattern scale grows with distance so far surfaces do not buzz.
- **Detail is built, not textured**: a house is a plinth, plank-striped walls, white corner trims, two roof slabs and a ridge, a gable with a round window, framed windows with shutters and flower boxes, a door with a step, awning and lamp. A tree is a trunk with a branch and a cluster of lobes, plus lighter lobes on the sun side. Water is layered: bank, shallows, a deeper channel, white foam lines at the edges, small white squiggles drifting with the current.
- **Screen space holds only three things**: the grainy frame, the bottom type, explainer callouts.
- **Never**: depth of field, real reflections, bloom, motion blur, volumetric light. A lit lamp is a flat warm colour plus a hard-edged pool of warm light on the ground.
- **Hero objects do not receive shadows** when they pass through shade, or they turn dirty.

## 3. Colour logic

- The ground outside the frame is always warm white `#FFFCF6`; nothing else is drawn there.
- **5–7 saturated hues + 2–3 pastels** carry the picture. Ink `#25214A` is only for outlines, type, tyres and window frames.
- **Cluster colour by area**: neighbouring blocks differ in hue; one colour's share is controlled (a field type at about a third of the ground, not sprinkled at random). Leave large calm areas of one colour (water, a field, a square) so the picture can breathe.
- **Day is bright and warm.** When it gets dark, darken by the scene: a night scene may be dark, but never grey all over.
- **Night is a luminance shift toward violet**, not a general darkening, so yellows don't go olive; every light is the same warm yellow (about `#FFD36E`). **Dusk** adds an orange-pink layer (about `#FF9E7A`) on the way to night.
- **Time and season change the large areas only** (ground, crowns, roofs, water), never the whole palette. Each changing material carries one colour per state; a wave (§8) swaps them.
- **Night and day by area is also a wave.** When the dark falls or lifts street by street (dawn spreading from one landmark, a district losing power), night and day are two states like two seasons: each changing material carries its night colour (the violet shift above) and its day colour, and the ring swaps them. Lights belong to the night state: a lit window or lamp head is warm yellow on the night side and plain glass or metal on the day side; a lamp's pool is a flat disc on the ground, warm on the night side and the ground's own colour on the day side, so it goes out exactly as the ring passes. Keep the rest of the picture's light unchanged during such a wave: a global darkening on top of it turns the day side grey.
- Winter does not mean all white: crowns go to pastel lilac, ice blue and mint with white dots, paths stay swept, houses keep their colours.
- Example palette (an example only): yellow `#FFD234`, pink `#FF7EB3`, sky `#5CC8FF`, mint `#5EDFB0`, lilac `#B9A0FF`, peach `#FF9C6B`, cobalt `#2F5BFF`, coral `#FF5A5F`, green `#2FCB7A`.

## 4. Type & subtitles

- **Three centred lines under the frame**: line 1, the title, Chinese and English, weight 600, about 25 px, dark; line 2, one sentence, weight 400, about 18 px, grey; line 3, small data (time, solar term, place, coordinates) in a monospace, about 15 px, light grey. Line 3 may change with the picture.
- **Line 3 is optional, and so is line 2.** An empty line leaves its place empty; the others never move up to fill it. With a voice, or when the film's words are bilingual, the type is **one Chinese line and one English line**: line 1 in Chinese (weight 600, about 25 px, dark) and line 2 in English (weight 400, about 18 px, grey), each on one line, never wrapped; line 3 stays empty unless there is small data to show. In this layout both lines change together, as one pair.
- The lines fade in and out with the frame and never move. When a line changes, the old one fades away and the new one fades in; line 1 stays (in the bilingual layout, both lines cross-fade, about 0.4 s out and 0.4 s in). The three marks stay at full strength through every change: only the words fade.
- Typefaces: Inter Tight for Latin, Noto Sans SC for Chinese, IBM Plex Mono for data (all OFL).
- Usually no voice: the type is the narration. With a voice, use plain bottom subtitles, one Chinese and one English line, no styled caption boxes.
- Hold every line ≥ max(1.8 s, reading time + 0.6 s).
- **Callouts** for explainers: a rounded pill with a leader line and a dot, Chinese main and English small, popping out of the model with a back-ease and fading when done.

## 6. Camera grammar

A vocabulary, not a route. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| High slow orbit or drift | the whole place breathing | time passing; day and night; seasons; a loop |
| Straight-down, slowly turning | a map; order | road networks; fields; coverage; data on a grid |
| Locked three-quarter frame | calm; comparable | before and after; data; several places side by side |
| Lateral move along a cutaway | above and inside at once | how a thing works; underground; under water; inside a building |
| Slow push to one detail | something is happening here | a lit window; a stall; a bird on a roof |
| Following one vehicle | flow; a route | a delivery; a commute; one line joining places |

- **Prefer one continuous take**, slow enough that the viewer can stop and look at any corner. When a long take must hold a composition, ease the camera speed down instead of letting the place drift out of frame.
- The frame is about 1520 × 744 px, a little above centre; the type sits under it and never covers the subject.
- **Transitions**: only three — the frame draws in and grows out again; a wave sweeps across (colour, light, season); the ground is cut open (the Cutaway of §8: the same move, whether the cut goes into the ground, a building or water). No white flash, spin or fast hard cut.
- The camera never passes through geometry; to get around something, move in two steps (rise, then travel).

## 9. Pitfalls of the medium

| Pitfall | Fix |
|---|---|
| Code-made people look stiff close up | keep them small and far; no acting |
| Day looks grey, not healing | raise saturation, warm it; shadows go purple, not grey |
| Yellows turn olive at night | shift by luminance toward violet; give warm objects their own night colour |
| Colours sprinkled at random look dirty | cluster by area, control each hue's share |
| Every tree looks the same | at least five crown shapes (round, cone, egg, cloud, column…), lighter lobes on the sun side |
| Thin objects turn into black scribbles | thicker stems, or no outline and a brighter colour |
| Large shadows look like dirt | halftone dots in the shade |
| Far outlines and patterns buzz | less detail far away; pattern scale grows with distance |
| A long take drifts until the subject leaves the frame | ease the camera speed down over time |
| A state change happens "by itself" and feels arbitrary | anticipate it: a squash on one landmark, then the wave from there |
| The camera passes through an object | move in two steps, or remove the blocking tree for that shot |
| The frame is crowded and has no air | keep large quiet areas of colour (water, field, square) |

