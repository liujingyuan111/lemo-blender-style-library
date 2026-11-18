# 数据叙事 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/dataviz/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`e94013d5a7c548c8844598a671ff0b49bc78770696cbca0d8d00846336f3c67f`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

**The chart is the film.** Every mark is a real number and every movement is a meaningful chart operation (a mark lands, an axis grows, the scale changes, a series morphs, a note is pinned). The data is real, openly licensed and traceable. You change the framing, never the numbers.

**Pick the chart the data asks for:**

| The data is about | Chart |
|---|---|
| comparing categories, rankings | bars, a ranked bar race |
| a relationship between two measures | scatter or bubble chart (one dot can be a character) |
| place | map, choropleth, dots on a map |
| parts of a whole, counts of people | unit / waffle chart, proportional squares |
| before → after | slope or dumbbell chart |
| a distribution | histogram, beeswarm |
| where things go | flow / Sankey |
| change over time | line or dot series, stripes, area |

Three layers make it a story, not an infographic: **a human scale** (handwritten notes pinned to marks), **a performer** (a physical pencil that draws every mark), and **sonification** (each mark is a pitch; the trend is heard before it is read).

Not a dashboard (one idea at a time), not a keynote with charts (no slides), never decoration.

## 2. Materials & rendering

- **Paper**: warm cream, fixed-seed fibre noise and a faint dot grid in world space. **Ink**: dark warm ink for axes and series, pale warm grey for grid and zero line, IBM Plex Mono ticks.
- **Marks**: data dots carry a thin ink ring so pale values stay visible on cream. A mark lands with a short pop and a thin ripple; suppress ripples when marks arrive closer than ~0.1 s.
- **Handwriting** (Caveat) in pencil, per-glyph jitter, graphite grain, written on as the tip dances over the x-height. Leaders are wobbly curves ending in an **un-closed** ring around the mark.
- **The red–blue pencil**: hex body, blue half / red half, sharpened wood cone. Only the tip end shows, from the lower right; its shadow drifts farther and softer with lift; sharp tip, soft body.
- **Layout**: a plot box fixed in world space, a **memory zone** for early notes, every note pinned in **data space** (value + pixel offset) so rescales keep the layout, a bottom band for the caption.

## 3. Colour logic

- Colour encodes **one thing: the value**. Diverging data uses a ramp (ColorBrewer RdBu family) centred on the mean of a meaningful reference period, with a symmetric span; data with no natural centre uses one sequential ramp. Everything else is ink on cream.
- **Honesty beats drama**: pale values stay pale; never stretch a ramp to make a change look bigger.
- The two pencil leads have meanings: **blue for memories and human notes, red for records and warnings**. A change of lead marks a turn.
- One `accent` colour may bypass the ramp for a mark that is not data (a logo, a highlight).

## 4. Type & subtitles

- **The subtitle is the figure caption**: a text serif (Newsreader), ink colour, left-aligned with the chart, ≤ 2 lines, with a hairline rule above it and a small mono kicker for the range drawn so far. Words appear on their whisper timestamps over a paper-colour band. Hold ≥ max(1.8 s, speech + 0.6 s).
- The title is the **chart's own headline** (Newsreader), set in world space above the plot; it fades when the camera is close and returns with the full view.
- No captions over a signature chart operation or a silence.

## 6. Camera grammar

A 2D camera `{x, y, zoom, roll}` over **one sheet of paper**. A film is one take; a hard cut is rare and meaningful. The moves below are a vocabulary, not a route. Opening and ending come from the topic.

| Move | Expresses | Can serve |
|---|---|---|
| Extreme close-up on one mark, following its leader | One fact, one life | a single case; a named person |
| Full view first, then dive to one mark | The pattern before the case | a familiar trend; a myth to correct |
| Pull back as axes grow out of the marks | The frame arrives with the unit | naming the measure; widening a claim |
| Track the pencil, newest mark at ~60 % of width | Progress: the past behind, the future ahead | a series in time; a race; a queue |
| Pedestal with rising data, a Dutch angle creeping in | Escalation, unease | runaway growth; a debt |
| Punch-in over 2 frames, decaying shake, jolt on rescale | Surprise, a broken frame | an outlier; a crash |
| Fast pull-out, roll, small constant tremor | A rush | a boom; a cascade; a panic |
| Locked-off | The transformation is the movement | a morph; a slow reading |
| Hold on one mark, then pull back | The part inside the whole | a verdict; context |
| Pull and pan to add more real data | Scale switch | a longer record; the rest of the list |
| Lateral pan across notes in the memory zone | Recollection | a biography; a timeline of events |

Framing: subjects fill ≥ 1/3 of frame height at key moments. When the real axis scrolls off-screen, pin its tick labels to a paper strip at the frame edge (frozen pane).

## 9. Pitfalls of the medium

- Select data columns by header name, never by index; print every fact the narration claims.
- Notes collide with later data → data-space pins, a memory zone.
- A frame break rescaled too fast is invisible → hold the pierced state ≥ half a beat.
- Right-aligned notes are still written left to right → the pencil hops to the first letter.
- Helpers that set `globalAlpha` must multiply the incoming alpha, or fades skip them.
- Tails leak across a hard silence → render before/after in separate buffers; verify on decoded samples.
- In dense passages the pencil body lies across fresh marks → steepen its angle.
- Synthesized human sounds (a laugh) are uncanny → use a soft non-human sound.

