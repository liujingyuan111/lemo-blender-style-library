# 浮世绘 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/ukiyoe/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`218c48a204f9034d1c2fb7f11698b4834f1faee1ca68c9e336f3d6ab992ff2e4`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

Every shot is **a complete woodblock print**: a sheet of washi, a thin double ink border, flat areas of colour printed from separate blocks, a black key-block line on top, a vertical title cartouche and a red seal. The world is flat on purpose. Depth comes from stacked horizontal layers, mist bands and bold cropping, never from perspective rendering, lighting or shading.

What makes it read as *printed* rather than *vector*:
- **Paper** is always visible: warm washi, long fibres, slight edge ageing.
- **Each colour is its own block**, slightly **out of register** (1.5–2.5 px) with the key line.
- Large colour areas show **woodgrain** and **baren rubbing** (uneven ink density, circular streaks) and fine **goma-zuri** specks.
- **Bokashi**, hand-wiped gradients, in skies and water.

Not a flat vector illustration with a paper overlay (no woodgrain, no misregistration), not Chinese ink wash (no bleeding washes, colour is printed, not painted), not anime cel shading (no light and shadow on forms).

## 2. Materials & rendering

- **The sheet is the frame**: the print fills the screen at zoom 1, inside a thick + thin ink border, with a paper margin beyond. Sheets can sit on a long mounting scroll (darker tan paper, a roller at one end), so the camera can travel from print to print.
- **Blocks**: draw each colour group into its own offscreen canvas, cached once (key lines; blues; greens / secondary; reds / figures). Composite each with a small fixed registration offset (1.5–2.5 px, a different direction per block).
- **Texture every colour block**: woodgrain (`source-atop`, strongest in sky and water) → baren streaks → goma-zuri specks (both `destination-out`); the key block gets specks only; light paper fibres over the finished sheet so paper shows through the ink. Big dynamic fills get the same textures inside their clip. Woodgrain = iso-lines of a warped noise field; baren = blurred circular arcs + zigzag streaks (recipe and alphas in [DEMO.md](DEMO.md#palette--props)).
- **Bokashi** is generated per pixel: a gradient whose top edge wanders by low-frequency noise per column (±20–30 px). Never strips of `fillRect` (vertical seams).
- **Line**: key lines 2.4–3 px; large contours are variable-width filled strokes, tapered at both ends, with ±20–35 % low-frequency width jitter. Distant things get a grey key line or none.
- **Motifs of the medium**: mist as long rounded flat bands (suyari-gasumi) fading at both ends; pines with flat-topped **needle pads**; fields as high, flat, parallel layers whose cross lines are **parallel and slanted**, never converging; rain as two sets of fine straight lines at slightly different angles under a sumi bokashi sky; water as banded blues with bokashi between bands, foam and spray left as paper.
- **Seal**: characters cut out of red, chipped edges. **Figures** are small in the landscape (roughly 80–130 px at full sheet), flat, with a clear silhouette; faces in a few strokes.

## 3. Colour logic

- **A pigment set, not a colour wheel**: 6–9 flat hues, each printed from its own block, over the paper ground. No gradients except bokashi, no shading on forms.
- **Sumi key line** over everything; **paper is the white** (no white pigment for foam, snow, mist, blank sky).
- **One dominant hue family** carries sky and water (in the 19th-century prints, Prussian blue); **red is rare**: seals, a sun, one garment or tab.
- Far layers pale and low-contrast, near layers saturated with dark key lines.
- Examples, one per film: an indigo-and-beni landscape (Prussian blue, pale blue, beni red, ochre, greens, sumi); a bijin-ga interior (pale pink, mauve, grey-green, lacquer black, a mica-grey ground); an autumn surimono (persimmon, ochre, grey-green, deep brown, one blue).

## 4. Type & subtitles

- **Subtitle = a horizontal cartouche**: a cream slip with a thick + thin ink border and a small red seal at the left; Shippori Mincho (500) in sumi, centred near the bottom. It "prints" in with the reveal mask and fades out. Hold ≥ max(1.8 s, speech + 0.6 s). It covers the bottom ~150 px: keep ground lines and figures above it.
- **View cartouche**: vertical cream slip, thick + thin border, a pale tab with the series title, the view title below in a brush font (e.g. Yuji Syuku), a seal beside: the "full stop" of each view. Titles live on the print as cartouches and seals, never as floating type.

## 6. Camera grammar

The camera moves *over* prints and between them; it never rotates in 3D space inside one. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Locked frame on one sheet | Reading a print on a wall | a place; a portrait; a still moment |
| Handscroll slide, right → left through the mounting gap (shorter slides = urgency) | Travel, the next station | a journey; a sequence of steps; a race |
| Very slow push toward a framing device (a window, a fan, a gate) | Attention narrowing | discovery; longing; a detail that matters |
| Tilt past the border into the mount | Something larger than the print | a flood; a rumour; a giant |
| Pull-back from one sheet to many | The series seen whole | a summary; a timeline; a collection |
| Crash-zoom into the texture (grain, specks, fibres) | The medium itself becomes the image | a dream; a breakdown; a memory dissolving |
| Pan across a triptych (three sheets side by side) | One scene too wide for one sheet | a procession; a battle; a festival |
| Hard cut to a blank sheet | Ma (間), a held breath | aftermath; a pause before a decision |

Framing: bold cropping and extreme foreground elements (a branch, a post, a lantern crossing the frame) are native; depth by stacking, never by perspective. Allowed transitions: scroll slides, printing reveals, a wash back to paper, a cut to blank. No cross-dissolves, no 3D flips.

## 9. Pitfalls of the medium

- Bokashi from `fillRect` strips leaves vertical seams → build it per pixel.
- Too much speckle or fibre makes dark areas look like sandpaper or scratched film → specks α ≈ 0.3, fibres α ≈ 0.09.
- A perspective grid for fields looks digital → parallel, slanted, flat layering.
- Pine clusters drawn as half-discs look like parasols → flat pads with needle fans.
- Offset curves self-intersect at tight bends → build inner lines from the gentle side of the contour; force control points x-monotonic.
- Breaking out of the print must escape **both** the sheet clip and the frame clip.
- A seal drawn with `multiply` vanishes on dark ground → `source-over` there.

