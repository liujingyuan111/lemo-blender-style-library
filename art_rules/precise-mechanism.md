# 分色机械图解 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/precise-mechanism/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`476538b1c0d602067bbac28c822eb70f8fad19ce0d29f1dda6354c3687af237d`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

- **Colour is the structure.** Every part takes the colour of the system it belongs to (energy source, transmission, control), everything else is one light neutral. A viewer reads the machine's organisation from the colours before reading a word.
- **Soft cel, own-colour outlines.** Two-tone flat shading with no reflections; every part is ringed in a darker shade of its own colour, never in black.
- **The machine is true.** Wheels turn by their tooth ratios, the oscillator swings at its real rate, numbers on screen are computed from the model. Slow motion is stated on screen.
- **Cut, explode, follow.** The camera's job is to open the object: section cuts with hatched faces, exploded layers by system, a tracking path along the force.
- **One thing to read at a time.** A single primary label, everything already explained steps back to mid grey.

Not Exploded Teardown (no product photography, no materials, no real-brand object), not Blueprint (light ground, filled solids, not line-only), not Isometric Infographic (a perspective camera that moves through the object, not a fixed diorama), not Glass Product Render (opaque, matte, no refraction).

## 2. Materials & rendering

- **Geometry is engineered, not sculpted**: involute gears with real module and tooth counts, extruded profiles (wheels, bridges, levers), cylinders for arbors. No bevels (a bevel doubles the outline). Choose module and camera so one tooth pitch is ≥ 12 px at 1080p.
- **Soft cel shading** (`cel()` in `demo/film.js`): lit faces are the flat colour, shade faces × 0.80 and slightly cool, a third tone for faces turned away. No environment map, no cast shadows between parts.
- **Outlines** (`demo/film-outline.js`): a second pass of view normals and depth; an edge on the near side of a depth step or on a crease is drawn in the part's own colour × 0.52 mixed with 28 % ink. 2× supersampling; lines 1–1.3 px.
- **Section cuts**: clipping planes through an axis; the back faces seen through the cut are shaded as the cut face, with 45° hatching computed where the view ray meets the cut plane, in world units (it never swims when the camera moves). Cut only the housing, never the part it reveals.
- **Dye**: colour arrives as a spherical front spreading from the point where energy enters a part (a mesh point, an arbor, an impulse pin), with a thin pale wet edge. Never a global crossfade.
- **One soft contact shadow** under the base plate (a blurred silhouette, 20 % opacity), drawn in the colour pass only.
- **Text and leaders** live in an HTML/SVG layer on top, anchored to projected 3D points every frame.

## 3. Colour logic

- A warm off-white ground, flat, no gradient or vignette.
- One light neutral for the frame, plates, bridges, housings and every part not being discussed.
- Three system hues, mid-value and slightly greyed, always in the same roles: **warm yellow = energy source**, **grey-green = transmission**, **grey-violet = control or measurement**. In a different machine the roles carry over (battery / gearbox / governor; lens / shutter / meter).
- **One accent** (a saturated red-orange), only for the protagonist part at its moment, and for the control that drives it. Never two accents.
- **Focus mode**: only cause and effect keep colour, everything else falls to the neutral.
- Ink is near-black, for text, leaders, hands and markers only.

Example (our demo): ground `#F3F0EA`, neutral `#DDD8CF`, ink `#25282D`, energy `#E6B94F`, transmission `#79B09F`, control `#8A97D4`, accent `#E8472A`.

## 4. Type & subtitles

- **Roles**: a neutral grotesk for titles and labels (e.g. Inter, 600–650 weight, tight tracking); a monospace in caps with wide tracking for figure lines, readings and units (e.g. IBM Plex Mono); a CJK sans for Chinese (e.g. Noto Sans SC). All OFL, self-hosted.
- **Three levels only.** Primary: a headline (60–64 px) or the label of the part being explained (name ~30 px ink + one 18 px line). Secondary: what was already explained, name ≥ 22 px mid grey, its line greys and lingers before it goes. Tertiary: the figure line (`FIG. n · …`, 13 px mono grey) and small data tags.
- **Labels grow out of the part**: a leader draws from a dot on the part, a colour dot in the system hue pops, the text slides in. Re-project every frame; when a label would cover a part, pin it to empty space and keep the leader; when the part leaves the frame, the label goes with it.
- **Comparisons** (ratios, before/after): the number is the primary (≥ 120 px), the two ends that produce it are secondary with leaders, all held in frame ≥ 2.5 s.
- **Subtitles**: bottom left, no plate, Chinese ≥ 34 px over English ~22 px, one line each; compose the subject away from that corner. Chinese on screen only in subtitles and short ≥ 34 px lines; labels are English. Hold ≥ max(1.8 s, speech + 0.6 s).
- **The credit** belongs in the style as a drawing's title block: ink rules, mono field names, values in the grotesk.

## 6. Camera grammar

| Move | What it expresses | Can serve |
|---|---|---|
| fast pull-back from a detail to the whole object | scale, a question | an opening hook; a reveal of context |
| slow orbit around the object | volume, that it is real | a cut opening; an exploded stack |
| crane down through a cut | entering the inside | the change from outside to mechanism |
| low tracking shot skimming over the parts | following the force or signal | a power path; a data path; a sequence |
| locked overhead | reading and comparing | a ratio; a parameter; a verdict frame |
| side view of an exploded stack | the systems as layers | a breakdown; what happens without one layer |
| push-in to a contact point at slow speed | the one interaction that matters | a ratchet pawl; a latch; a valve opening |
| big pull-out to the whole object, cut still open | the answer seen in context | an ending; a summary |

Framing: the subject fills ≥ 60 % of the frame width in explanatory shots; text sits in the clear third, never on parts; nothing important in the subtitle corner. Transitions are made inside the object: a cut opening, a lid lifting, layers exploding or landing, a match cut on a mechanical event. No dissolves, page turns or slides.

## 9. Pitfalls of the medium

- **Outline flicker on fine teeth** → keep tooth pitch ≥ 12 px, render at 2×, no bevels, do not spin fine teeth fast (≤ 45° per frame for a part with 4-fold symmetry; slow the time instead).
- **Wagon-wheel aliasing** of fast oscillators → show them slowed and say so.
- **Rainbow parts** → colour by system, never by part.
- **Plastic or metal look** → no reflections, no transparency, no specular.
- **Labels everywhere at equal weight** → one primary; the rest secondary or gone.
- **Labels on parts or under subtitles** → pin to clear space with a leader; keep the subtitle corner empty.
- **A housing that moves through the parts** (a case lifting through the movement) → move each piece the way it would come apart (dial up, case down).
- **Meshing that drifts after a free run** → make the extra rotation a whole number of teeth.
- **Hatching in screen space** swims with the camera → compute it on the cut plane in world units.

