# 流水线图解 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/assembly-line-diagram/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`179a41acc3a10bf45d7a3d91eab316077d44fdd75b0ba067d42d87e5b2e598bf`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

- **One line, one direction.** The subject is a process that turns one thing into another in steps. The film is a single continuous production line the cargo travels; every shot is a station on it, in order.
- **Metaphor per station, said straight.** Each step is one machine everyone can read (a press, a sieve, a weighing scale, a crane, a loading dock, a paint booth). The plaque gives both names: the machine's in English, the real thing's in Chinese (`SIEVE | 沉砂池`). The humour comes from the metaphor being literal, never from cartoon faces.
- **Colour is the legend.** Each kind of output gets one spot colour; its pipe, its parts and its legend tag carry that colour for the rest of the film, so the viewer follows a colour instead of reading a label twice.
- **The cut-away is the frame.** Rooms sit inside a silhouette on a dark ground; the gap of dark between the rooms and the outer wall is what makes the silhouette read (a person, a machine) at every scale.
- **Workers are scale and action.** Tiny, faceless figures, each doing one legible thing (turning a valve, holding a sign, pushing a cart, dozing). They give the factory its size and the beats their comedy.

Not Isometric Infographic (no isometric or perspective view: everything is a flat front elevation), not Whiteboard Explainer (no hand, no drawing-on), not Exploded Teardown (no 3D parts flying apart), not Blueprint (full colour on paper, not white lines on blue), not a keynote (no slides, no centred title pages, no page headers).

## 2. Materials & rendering

- **All vector, drawn in code**: SVG built per frame from shapes and paths. Clean ink outlines with round caps and joins, flat fills, no gradients.
- **Print, lightly.** Every colour plate is shifted by its own 1–1.6 px misregistration, the same direction across the frame (ink, paper and walls stay put), and a faint paper grain and fibre sit on top (multiply). Nothing more: no aging, no torn edges, no yellow stains, no mottled ink.
- **Flat shadows.** A Holmes shadow is the same shape offset down-right in one pale flat colour (plaques 5–6 px, large shapes 14–18 px). No soft shadows, no blur except motion blur on whip moves.
- **The cut-away.** The silhouette is a dark ground with a thick body wall (a band about 56 px thick with ink on both sides); where goods enter (an intake, a hatch, a door) the wall breaks and both ends get an ink cap. Rooms have a coloured frame, a pale wall and a floor strip; floors between rooms are slabs with rivets; steel trestles and gantries hold the machines.
- **Pipes**: ink edge (width + 6 px), colour, then a highlight stripe (0.2 × width, offset up-left, masked inside the pipe); rounded elbows; flanges every so often. Width encodes importance (main duct, arteries, branches).
- **One printed sheet at every distance.** Line weight follows the camera (thinner when pulling back, roughly `z^-0.6`; only slightly heavier when pushing in), and below a set scale small workers, plaques and small text are not drawn while the big machines stay. The drawing never turns into a hairline mess or a blob of text.

## 3. Colour logic

- **Paper + ink + one ground + four spot colours.** Paper outside the silhouette; one dark ground inside the cut; pale walls for rooms; a body colour for walls and slabs; then three or four spot colours that are the legend. No other hues.
- **Spot colours have one meaning each for the whole film** (in a recycling plant, say: ochre = paper, vermilion = plastic, teal = glass). Room frames may rotate through the spot colours by station; the cargo's own colours stay fixed.
- **Ground dark enough to frame, never black**: a deep indigo or wine reads as "inside" and lets the spot colours sit on it. Check that every spot colour separates from the ground (cobalt on indigo does not).
- Numbered station circles are one colour (ochre fill, ink edge); a circle is an outline until its station is reached, then fills.
- Example (our demo, palette A "Night Shift"): paper #F2ECE0, ink #1D2030, ground #24345A, wall #FBF7EE, body #EE9F87, vermilion #E04A2F, ochre #F3B23A, teal #2E8D87. Two alternatives live in `demo/lib.js` (`PALS.B`: a daylight chart with a pale body-colour ground; `PALS.C`: a wine-red ground).

## 4. Type & subtitles

- **Three faces, three jobs** (all OFL): a condensed industrial display face for plaques, legend tags and the title (Big Shoulders Display 800–900, like letters painted on a factory wall); a grotesque for small labels, subtitles and credits (Archivo 600–800); a CJK sans for the one short Chinese line on each sign (Noto Sans SC 700, at least 34 px).
- **Plaques**: cream board, 2.6 px ink frame, 3 px corners, flat shadow; `[number circle] [ENGLISH METAPHOR | 中文名]`, stuck on the room's top edge or on the machine, never on a leader line.
- **Legend tags** hang above their line: a colour chip, then the English and Chinese name (`GLASS 玻璃`).
- **Leaders** (Holmes): dot → vertical → right angle → bold words, only for a moving hero, at most one per frame.
- **At most about seven pieces of text in a frame**, two to four words each.
- **The title is an object in the picture** (a gantry sign over the infeed, a machine's nameplate) hung on the thing it names, never in a page margin, never centred, never a header. The end card is the same object: a nameplate standing on the ground line.
- **Subtitles are work tickets**: a cream ticket with an ink frame, a stub on its left showing the current station number (a clock when there is none), Chinese 34 px over English 28–30 px, one line each, bottom left; move them bottom right in shots where the title or the end card holds the left. Compose every shot with that corner free.

## 6. Camera grammar

Always a flat front elevation: the camera pans, tilts, pushes and pulls in the plane of the drawing, never rotates into perspective.

| Move | What it expresses | Can serve |
|---|---|---|
| Truck with the cargo | the flow, one piece followed | an opening; moving between stations on one floor |
| Push through a door shape | entering the system | the intake; going inside a part |
| Tilt down a chute, slabs wiping past | going down a level | the next stage below |
| Pull back from a part to the whole floor | the parts working together | a sorting or splitting station; a held comparison |
| Follow one colour | one output's path | where one product goes while the others leave frame |
| Porthole POV (circular mask) | the outside world reaching in | a trigger, an alarm, a customer, an event |
| Whip down a pipe | urgency | a demand that must be met now |
| The great pull-back | the whole line at once | the ending: the full silhouette with every station lit |

Transitions happen inside the drawing: passing through a shape, floor slabs wiping the frame, a match cut on the same piece of cargo, a colour follow, a circular porthole mask, a whip along a pipe (directional motion blur from the camera's speed plus speed lines, rendered once, never stacked ghosts). No page turns, no fades to paper, no white flashes.

## 9. Pitfalls of the medium

- **Process diagram, not a story.** A station-by-station walk is a flowchart. Give it a hook (a reversal, a deadline, a question) and a payoff picture; let each station say one thing.
- **Text creep.** Plaques, tags, leaders and subtitles add up fast; keep to about seven pieces per frame and let colours carry meaning.
- **Hairlines and blobs at distance.** Without camera-dependent line weight and level of detail, the pull-back turns into a grey mesh of strokes and unreadable labels.
- **The silhouette disappears** when rooms fill the cut edge to edge: keep at least 30 px of dark ground between rooms and the outer wall.
- **Spot colours that vanish on the ground.** Test each against the dark ground and against the walls before committing.
- **Bodies that look like barrels.** When a figure has to hold a lot of rooms, its torso grows and its head shrinks; cross-fade to a schematic figure with human proportions for the full-body shot rather than inflating the cut-away.
- **Feet.** Procedural legs that swing on sine curves float, sink and slide; solve them against the ground line, and hold the final frame on a readable phase (one leg reaching, not crossed).
- **Metaphors that lie.** Every simplification the metaphor makes (one input → one output, a valve where there is really a gradient) goes into FACTS.md; the voice should not claim what the drawing only implies.
- **Leaders everywhere.** One leader per frame at most; everything else is a plaque on its object.

