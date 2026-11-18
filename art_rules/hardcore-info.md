# 线稿剖面图解 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/hardcore-info/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`ddcd47faa4ca8a450baa159d73767f62f66d1efe91008aa9f0e7b6c6db48f283`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

A frame reads as this style when:

- **everything is line on paper**: warm white paper with a faint grid, black ink outlines, light grey value only to give volume. No lighting drama, no shadows, no reflections, no depth of field;
- **the lines have a hierarchy**: the silhouette is thickest, edges where one part hides another are medium, creases and small parts are thinnest and greyer;
- **one accent, one meaning**: a single saturated colour marks the path the film is about, and nothing else (no accent decoration, no accent buttons, no accent backgrounds);
- **the words are attached to the object**: every label hangs from a dot on a part, dimension lines measure the model in its own perspective, numbers come with units;
- **the object is a real, sized model**: built in millimetres from published dimensions, so any view (section, top-down, close-up) is the same model cut or seen differently.

It is not an exploded teardown (dark studio, physically based light, a photographed product), not a blueprint (white on blue, flat orthographic sheets), not an isometric infographic (flat vector shapes, no 3D camera), not a whiteboard (a hand drawing in real time).

## 2. Materials & rendering

- **Live line drawing from 3D.** Each frame renders the scene twice into float targets: a grey value pass and a normal + linear depth pass. A full-screen shader traces edges, at 2× resolution, downsampled:
  1. **silhouette** (foreground against paper): the distance to the nearest pixel of the other class, a centred line about 2.7 px wide, ink #141414;
  2. **occlusion** (large relative depth jump between parts): Laplacian of 1/z, about 1.7 px;
  3. **creases and small parts** (small depth jump or normal angle): about 1 px, a lighter graphite.
  Line widths are in screen pixels and never scale with the camera, so a far object naturally reads denser.
- **Stable lines in motion.** 8 rotated-grid sub-pixel jitters per frame, accumulated, inside a very short shutter (about 0.12 frame). This removes crawling and flicker on hundreds of small parts without visible motion blur; a long shutter would draw ghost copies of each line.
- **Values**: surfaces are light greys (#FBFBF9 to #DCDCD8), dense parts (battery, chips) a dark grey, all lit by one soft directional term only to separate planes.
- **Sections**: a clipping plane cuts the model; back faces show 45° screen-space hatching. A part made of a different material (plastic between metal) carries its own lighter hatch, so a cross-section reads as "metal | plastic | metal".
- **Diagrammatic people**: a hand or tool that is not the subject is drawn one tier lighter: nearly paper-white flat fill, thinner grey outline, few inner lines, knuckles as fine segment lines, and it fades out of frame at the wrist (alpha falls off along the screen direction away from the object).
- **World-anchored 2D**: leaders, dimension lines, signal arcs and magnifier connectors are drawn in 2D but projected from 3D anchors every frame. Only subtitles and the end card sit in screen space.

## 3. Colour logic

- Ground: warm white paper with a 40 px grid at about 4 % ink and small crosses every 200 px.
- Ink: one near-black for outlines and titles, one graphite for secondary text and inner lines.
- **One accent only**, reserved for the explained path: the traces, cable and clip that carry it, the part it ends in, the leaders and badges that point at it, the waves it sends out, and one key word in a title. If the film has two paths, they are the same path at two moments (one goes dark, the other lights), never two accents.
- Never colour the background, panels or decoration. Large flat dark areas are avoided except where a real part is dark (a battery, a chip).
- Example (our demo): paper #F6F5F0, ink #141414, graphite #5A5955, part greys #FBFBF9 / #EDEDEA / #DCDCD8 / #BCBCB8 / #4A4A49, accent #FF4D1A.

## 4. Type & subtitles

- Two families, both licence-free: a technical grotesque for names and titles (IBM Plex Sans SemiBold in our demo, uppercase names with +1.4 px tracking) and its monospaced sibling for specs, units and footnotes (IBM Plex Mono). Chinese in a matching sans (Noto Sans SC), on screen at ≥ 34 px.
- Roles: titles 54–64 px with one accent word; part names 21 px; spec lines 15 px mono; footnotes 12 px mono with wide tracking; data labels on rulers 20–26 px mono.
- **Label anatomy**: anchor dot on the part → a straight leader → the name → at most one spec line in mono (drop the spec when the label cannot stay long enough to read it). A label appears only when its part is the subject and wipes out before the camera leaves it.
- **Appearance**: text only ever writes on left to right and wipes off left to right, like a plotter. No fades, no bounces, no shadows or outlines on type.
- **Subtitles**: bottom-left, one Chinese line and one English line, on a paper-coloured plate with a thin ink rule on the left; the subject is composed above the subtitle band. Hold each cue ≥ max(1.8 s, speech + 0.6 s).
- Big statements (a question, an answer, the last line) sit in one column on the left while the object stays right, so the start and the end of a film rhyme.

## 6. Camera grammar

| Move | What it expresses | Can serve |
|---|---|---|
| Section sweep reveal | the object built from a cut | an opening; introducing a new part |
| Slow push to a detail | attention, a symptom | where something goes wrong; the one part that matters |
| Orbit under or around | the hidden side | revealing what the path ends in |
| Tip-over plus crane up while layers lift | the whole, its order | explaining an inside; a structure overview |
| Tracking the accent's head | following a process | a signal, a current, a flow |
| Dive into a gap until a material fills the frame | scale change, "inside" | a slit, a vent, a seam, a channel |
| Locked top-down with a magnifier inset | measuring, comparing | dimensions, counts, a cross-section |
| Pull back with a slow orbit | the conclusion | a last statement; an end card |

- Long takes are the default: push, orbit, tip-over and tracking are one continuous move. When a cut is needed, it happens **through a shape**: push into a part until its material fills the frame, then open a circle at the same point in the next shot; the circle can shrink into a magnifier.
- At key moments the subject fills at least a third of the frame height; the subject is composed above the subtitle band (y < 900 at 1080p).
- Cuts and transitions fall between narration sentences or on a natural pause, never in the middle of a word.
- No fades, no wipes from outside the medium, no hard cuts between unrelated angles.

## 9. Pitfalls of the medium

- **Uniform line width** makes the drawing look like a mesh preview. Keep the three tiers, and the lighter fourth tier for hands and tools.
- **Crawling and flickering small parts.** Without sub-pixel accumulation, passives and holes shimmer. Use the jitter accumulation; with a long shutter it turns into ghost lines.
- **Coplanar touching parts draw no line** (a plastic insert flush with metal). Recess one by a fraction of a millimetre or give it its own hatch.
- **A 2D anchor on a hidden part.** A dot drawn on an occluded component floats on top of the part in front. Place the anchor on a visible face, or move the part.
- **Render targets cached at one size.** An inset that grows (a magnifier opening) must use targets keyed by size, or it is upscaled from its first, tiny size and comes out blurred.
- **Accent creep.** A second use of the accent (a title bar, a button) makes the path unreadable. Check every frame for accent outside the path.
- **Label pile-up.** Labels that outlive their part's moment crowd the frame. A label leaves before the camera does.
- **Hands that read as dolls.** Round capsules and a cylinder wrist look like toys. Taper the phalanges, mark the knuckles with fine lines, add nails, fade the wrist out.

