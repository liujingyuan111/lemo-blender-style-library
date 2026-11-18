# 木刻版画 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/woodcut/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`b96fda6eeac038137310cc0766d979c8d8a5f3ff6acd87bada5aa50d5136a6a0`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

Each shot is **one printed plate**: black ink on laid paper, framed by a paper margin. It follows three rules of real relief printing:

1. **Black is the wood, white is what the knife removed.** Light is *carved*: a bright area is many wide cuts, a dark area untouched wood.
2. **Pictures appear by being carved.** Nothing fades in: cuts grow stroke by stroke along the form, coarse gouges first, fine lines after.
3. **The block is a mirror.** Letters read backwards until the paper is pulled; that reversal is the style's own transition.

Not copperplate engraving (no swelling burin lines on white, no crosshatch built up from white ground), not linocut poster art (no flat colour areas), not a black-and-white photo run through a threshold filter (the cuts must follow the form).

## 2. Materials & rendering

- **Print frame**: the printed image area sits inside a paper margin; the wider bottom margin holds captions. The image edge is the block edge: ragged ink, never a clean rectangle.
- **Knife classes** (widths in 1080p pixels at 1× camera):

| Tool | Width | Use |
|---|---|---|
| Knife `k` | 1.2–2 | contours, the white outline that separates a black figure from a black ground |
| V-gouge `v` | 2–8 | hatching, hair, beard, fine light |
| U-gouge `u` | 10–22 | rays, sky sweeps, the first rough-out |
| Stab `stab` | r 3–8 | snow, sparks, flecks of loam, wood chips |

- **Hatching (Doré grammar in wood)**: line **direction follows form** (a round object is wrapped in arcs, slopes follow the fall line, fire and light radiate, cloth follows its folds). **Width follows tone**: bright = wide cuts almost merging into white, mid-tone = thin cuts, dark = no cuts. Far = dense and fine, near = sparse and coarse. Every line is a separate cut (30–160 px, blunt entry, tapered exit, chipped edge), never a continuous machine line.
- **Figures**: black silhouette + white knife halo + grazing-light hatching on the lit edge only (light z ≈ 0.2, so flat areas stay black). **Skin carved white, features left black** (the wordless-novel rule).
- **Close-ups (hands, objects)**: sculpt a small height field (capsules, blobs, planks, creases), light it and run it through `woodcutFilter` (§10), so cuts follow the isophotes like an engraver's.
- **Printing**: the mask (white = cut) goes through a WebGL2 compositor: knife burr on edges, ±6 % ink unevenness, wood-grain streaks, specks where ink didn't take, a mottled colour plate with a small fixed misregistration. Block mode: glossy inked wood with grain sheen, pale wood in the grooves.

## 3. Colour logic

- Two values carry everything: near-black ink and warm laid-paper white. The raw wood colour appears only in shots that show the block itself.
- **At most one colour plate**, printed only where white has been carved, so it glows out of the cuts and never sits on the black. A colour plate over ink is nearly invisible, so plan it on carved white.
- The colour is reserved for the one thing that matters (a flame, molten metal, a heart, a signal lamp). It can spread at a peak and shrink to a single highlight afterwards; it is never decoration.
- Examples of a plate: a burnt copper-orange for heat; a cold Prussian blue for water or night; a deep oxblood for a wound or a seal. Choose it from the topic.

## 4. Type & subtitles

- **Captions are letterpress in the paper margin**, below the plate, like a plate caption in a woodcut novel. They never cover the image. A letterpress old-style face (IM Fell English, OFL) around 40–44 px, in ink, pushed through the same print shader. The ink comes up in 0.1 s with no slide and fades over 0.15 s. Hold ≥ max(1.8 s, speech + 0.6 s).
- **Titles are carved, not typed**: cut into the block (IM Fell English SC), mirrored if the block is shown before the print is pulled.
- Any closing text is a fresh print: letterpress in the margin or carved out of a black panel.

## 6. Camera grammar

The camera moves over the paper; the margin stays fixed. The knife tip, or the brightest cut, is the focus.

| Move | What it expresses | Can serve |
|---|---|---|
| Track with the knife tip | Making; the line is the story | a first mark; a route drawn on a map; a signature |
| Continuous pull-back as cuts spread | A line becomes a world; scale | a city from one street; a family tree; a reach of sound or news |
| Locked plate | A page of a wordless novel; reading time | a decision; a portrait; the aftermath |
| Slow macro push on a sculpted close-up | Patience, touch, labour | hands at work; a tool; a letter being read |
| Snap zoom and hold | Shock; the detail that breaks | a crack; a wrong number; a face turning |
| Frame in a frame (door, window, arch) | Distance, exclusion, waiting | a crowd outside; a sickroom; a border |
| Hard cuts on the beat, each a new impression | Accumulation, a series of prints | offerings; days passing; a list of names |
| Crane up from a detail to the whole | Consequence | a flood reaching a village; a light reaching faces |
| Rack between two plates via the peel | One state printed over another | before/after; a promise kept; generations |

Opening and ending come from the topic. Framing: black masses on carved white or white on uncut black, never grey on grey; text only in the margin. Transitions: hard cut (new impression) or the peel; never a dissolve.

## 9. Pitfalls of the medium

- **White marks on white areas are invisible** → stab cuts need dark masses behind them.
- **Hatching every surface looks like fur or rain** → grazing light; 3–6 cuts on the lit edge only.
- **Black faces with white cuts don't read small** → skin white, features black, a black keep-line around white parts.
- **Hand-drawn close-up props look like mittens and blobs** → height field + `woodcutFilter`.
- **Short hatch segments with a tonal wobble turn into zig-zag chevrons** → long cuts (14–50 × spacing), one broad highlight band, a thin rim light, a stronger halo.
- **Steam or smoke on top of the subject reads as flames** → draw it behind, so only wisps escape.
- **Lazily cached strokes shared between shots** make frames depend on the render worker → every cache builds itself on first use.
- **Fine hatching + ink noise + grain inflate the file** → a higher CRF with `-tune grain`; check a 1:1 crop. `woodcutFilter` NaN in flat areas → clamp before `sqrt`.

