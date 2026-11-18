# 搞笑历史卡通 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/comic-history/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`4aec43d12d02f39438872c9825e6e0d952b2c5762643a4d0b0dffdd8adb38fac`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

- **Every change of territory is a paper action.** Land changes hands by being cut, slapped down, torn off, pressed flat, peeled at a corner, or covered with another layer. A country is never simply recoloured.
- **The map is printed matter.** An old engraved map on paper (coast ripples, graticule, ink borders, flat printed fills, small-caps names), not a map standing in a room and not a vector infographic.
- **Countries are people made of paper.** Puppets cut from card, joined with brass split pins, with oversized round heads and swapped expression heads. They personify a country or a side, never a real person.
- **A comic page holds the film.** Panels with ink frames and cream gutters on a table; one panel is one moment or one place, and narrow panels change the tone.
- **Comedy, with one serious register.** Slapstick for the squabbles; a darker panel without jokes when the history is violent.

Not Paper Pop-up Book (no folds that stand up from a spread), not Isometric Infographic or Data Storytelling (no charts, no clean vector map), not Shadow Puppetry (opaque colour, not silhouettes), not Mid-century Cartoon (cut paper with texture and pins, not cel lines).

## 2. Materials & rendering

- **Printed map** (rule): equirectangular projection with longitude compressed by cos(centre latitude); about six engraved ripple lines outside each coast; dashed graticule; thin ink borders; flat fills with a lighter rim about 20 % wide inside each shape, as if the plate inked thin at the edge; compass rose and a kilometre scale bar. A procedural paper texture (mottle, fibres, fine grain) overlays everything, about 55 % overlay.
- **Borders**: Natural Earth for modern lines, except where China is in frame (DIRECTOR.md §13); historical borders are pieced from modern ones and hand-traced where the difference shows in frame. Name the error margin in the credits.
- **Puppets** (rule): green-screen part sheets keyed and cut into parts; each part gets a cream card edge (dilated a few px) so it reads as cut paper. Parts rotate about their pins (2D forward kinematics); arms reach targets with two-bone IK. Small part-on-part shadows (about 3–4 px) and one larger cast shadow on the map (about 13–19 px).
- **Paper patches**: opaque card with a dashed line printed inside the edge and a thin cream rim; torn edges are jagged with white fibres; a peeled corner is a fold transform with the back of the paper showing.
- **Height is shadow** (rule): a patch held in the air throws a large soft shadow offset 30–45 px; once down it keeps only a 3–4 px paper-edge shadow.
- **The page**: panels drawn into their own canvases at 1:1 so a panel pushed to full screen stays sharp; ink panel frames, cream gutters, a warm grey textured table that only shows when the camera pulls back.
- Nothing is translucent: patches, bubbles, tags and caption boxes are opaque paper.

## 3. Colour logic

- Two protagonists, two colours, kept for the whole film (for example a printed blue and a printed grey). Neighbours are low-saturation print colours (sand, sage, brick, ochre) and never compete.
- **A new patch is one step away from the printed colour** of its owner (lighter or deeper), so it reads as another piece of paper laid on the print.
- Ink is one warm near-black for all type and lines; paper is a warm cream. One accent red is reserved for scissors handles and the Chinese line in speech bubbles.
- A serious panel drops saturation and value (darker, colder) instead of adding new colours.
- Example (our demo): paper #F1E8D2, ink #2B2219, side A #6E93D6, side B #5D6672, sea #A6CCD3, red #C8463A, brass #D9B158, caption card #F5E9C4, table #7B6A57.

## 4. Type & subtitles

All licence-free (OFL). Roles:

- **Place names**: an engraved small-caps serif (e.g. IM FELL English SC), tracked out, pure ink. No outline, glow or shadow.
- **Small print** (tag captions, treaty slips, title card): the same family in roman and italic.
- **Every number** (rule): a serif with lining figures (e.g. Old Standard TT). Old-style figures turn 1975 into "I975" and drop the 7 below the baseline. Year tags are bold lining figures with a thin printed rule under them; numbers inside other text switch to the lining face at the surrounding weight, on the same baseline, at about 0.9 of the surrounding size.
- **Shouts** in speech bubbles: a round heavy display face (e.g. Lilita One), one English line; the Chinese line under it in a rounded hand-drawn face (e.g. ZCOOL KuaiLe) in the accent red.
- **Where text lives** (rule): speech bubbles hold only what characters say, short, in the upper half above the speaker, tail growing from the bubble edge to the mouth. Narration goes into comic caption boxes (pale yellow card, ink border) at the bottom centre, Chinese above English, one line each, never wrapped; feet, place names and scale bars stay clear of that band. The year is a printed tag pasted at the top left of the panel; extra facts are slips pasted under it. Words on props (a passport, a pin, a title card) enter as paper: held up, stamped, dropped, slapped on.
- On-screen Chinese at least about 34 px at 1080p. Hold each caption ≥ max(1.8 s, speech + 0.6 s).

## 6. Camera grammar

| Move | What it expresses | Can serve |
|---|---|---|
| Slow push inside a panel | attention gathering on the map | a claim; a build-up before a cut |
| Shake (small / large) | weight of paper landing | a stamp; a slap; the heaviest blow of the film |
| Pull back to the whole page | "this is a comic page" | a reveal; a change of place; an ending |
| Lateral slide into the next panel | the same moment elsewhere | a parallel scene; a quiet aside |
| Whip across a gutter with speed lines | a jump in time | decades passing; a punchline |
| Diagonal drop down the page | the next row of the story | returning to the light after a dark panel |
| Tilt down and push in until the map becomes a tabletop | the thickness of the paper | layers of history; what is left underneath |

- Inside a panel the camera stays on the paper; when a panel is pushed up it fills the frame exactly (1:1). A narrow panel parks at one side of frame with the panel just played still visible beside it, never centred over bare table.
- Transitions are page moves only (slide, whip, drop, pull back); no dissolves or flips between panels.

## 9. Pitfalls of the medium

- Recolouring a country without a paper action: the style disappears.
- A new patch in exactly the printed colour of its owner: once it moves it reads as a white outline only.
- Outlines, glows or drop shadows on type; old-style figures in years; system fonts.
- Two speech bubbles on screen at once, bubbles over place names, tails pointing at hats instead of mouths.
- Characters' feet, names or the scale bar in the caption band.
- Smooth on-ones puppet motion or ease curves with no overshoot: it reads as software, not paper.
- Comic sound effects or slapstick on war deaths, massacres or persecution; those panels go darker and quieter.
- Real flags with political symbols, Nazi symbols, real people's likenesses. Uniforms personify a country; say in the narration who the actual party was when the costume simplifies it.
- Upscaling a panel past 1:1: render panels at their on-screen size.

