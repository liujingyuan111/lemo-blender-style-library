# 波普艺术 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/pop-art/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`b072389250134a9cd7968a6123c384dff5fae07f8fc30a2e4c59852afe5f1926`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

- **A printed object, not an illustration.** Four plates (red, yellow, blue, black key) on paper. Every middle tone is a dot screen; there are no gradients, no soft shadows, no transparency.
- **Dots live on the paper.** The screen is fixed in page space at 45°: the closer the camera, the bigger the dots, until one dot is the size of a coin. Distance and emphasis are told by dot size.
- **Repetition is meaning.** The same print pulled again and again, edge to edge, with small differences in register and ink: mass production, copies, sameness. Changing one tile's colourway against the wall is the strongest gesture the style has.
- **Whole-frame posters.** Each shot is a full composition (a poster, a sheet of prints, a wall), not a scene with a poster in it.
- **Telling, not a comic.** No panels or gutters as a reading order, no speech balloons, no onomatopoeia, no acting characters. Information arrives as printed labels and headlines; a voice tells the story.

Not Halftone Dossier (cream archive paper, soft colours, characters), not Risograph Print (pink/blue/yellow soy inks overprinting into new colours), not Silkscreen Travel Poster (scenic places in flat layered colour, no dot screen), not Swiss Motion Graphics (grid type with no printed image), and not a comic book.

## 2. Materials & rendering

- **Three layers, one print pass** (`demo/engine/pop.js`): a plates canvas whose R, G, B channels hold the density of the red, yellow and blue plates (1 = solid, 0.05–0.95 = dots, 0 = paper), a black key canvas (alpha), and a spot canvas for the rare unscreened colour. A WebGL2 shader turns densities into round Ben-Day dots (dots up to 50 %, round holes above), multiplies the inks over paper and lays the key on top.
- **Opaque fills knock out what is beneath** (plates, key and spot), so painter's order holds; `over` adds ink to what is already printed (red dots over yellow = orange shading, red and blue dots growing over anything = the print darkening).
- **Dot screen in page space**, converted from screen pixels by the camera's inverse. Below about 2–4 px per cell on screen the dots fade into flat tint, so a wide shot never moirés.
- **Misregistration**: each colour plate is offset from the key by a few page units (clamped to a few pixels on screen), so a white sliver shows beside the outline. Per copy, offset the fill from its key line by a different small amount: repeated prints are never identical.
- **Key lines** are variable-width ribbons, heavier on the side away from the light (upper left), tapered at open ends; the line width compensates for local scale so small prints keep their outline.
- **Paper**: warm off-white with light fibre and ink unevenness; age and roughness stay low (clean print). Raise them only to date a print (an older edition: more age, wider misregistration).
- Grain in the mux at 1; nothing blurred.

## 3. Colour logic

- Three process colours plus black and paper. Every other colour is an overprint in dots: orange = yellow + red dots, green = yellow + blue, purple = red + blue, dark = red and blue growing over everything.
- Primaries are used flat and big: one ground colour per poster, one subject colour, black for drawing, paper for breathing.
- Never put a colour on itself (red type on a red ground, a yellow subject on a yellow ground without a key line or a paper disc between).
- Darkness is never a black fill: it is dots of red and blue growing until the image drowns. Black is reserved for the key (lines, type outlines).
- Example (our demo): red #E4232B, yellow #FFD21F, blue #1E62B0, key #141414, paper #F8F2E2.

## 4. Type & subtitles

- **Headlines**: a tall condensed grotesque (e.g. Anton, OFL), 100–260 px; colour fill, black outline, an offset shadow in another plate. They are printed in: colour lands from an offset, the key snaps on.
- **Labels**: a paper slip with a black frame and a plate-coloured offset block behind it, tilted ±2°, at a fixed corner of the frame. Headline line (condensed or a heavy grotesque such as Archivo Black, 90–130 px) over one short Chinese line (a heavy CJK sans such as Noto Sans SC Black, subset to the characters used, 46–56 px). Mixed Latin and Chinese lines use a font stack (Latin face first) so Latin never falls back to a serif.
- **Subtitles** are the same paper slip at the bottom centre: Chinese 40 px over English 28 px (Archivo Black), one line each, never wrapped; hold ≥ max(1.8 s, speech + 0.6 s).
- Labels enter with a fast print (0.5 s) where paper and words appear together, and leave by sliding out; nothing fades.
- Page-space type (a word printed on the sheet beside the subject) may be covered by the next copies or carried away by the camera: that is the medium's own exit.
- One headline and one label at a time. No page headers, no centred stacks of text, no bullet lists.
- Reading time: every label line ≥ characters ÷ 15 (Latin) + characters ÷ 4.5 (CJK) + 1.5 s, checked with `readcheck.mjs`.

## 6. Camera grammar

| Move | What it expresses | Can serve |
|---|---|---|
| Pull from coin-sized dots to the whole print | "this is a print"; scale; the hook | a first image; a reveal of what a detail belongs to |
| Pull from one print to a wall of copies | sameness, quantity, mass production | copies, a product line, a crowd, a franchise |
| Push into a round shape, match-cut to another round shape | one thing is part of another | a cross-section; a planet; a coin; a pill |
| Through a hole in a printed letter or number | passing into another time or chapter | a year; a price; a percentage |
| Lateral track along a long print | sequence, growth, a line of things | generations; a production line; a journey |
| Push to fill the frame with one tile, then flip it | a substitution, a turn | replacement; before/after; a new version |
| Slow push into a wall while a front crosses it | threat, spread, inevitability | a flood; a price rise; a trend |

Framing: the subject is a whole print or a whole wall; at key moments one print fills at least a third of the frame height. Labels live in the top-left corner, subtitles at the bottom centre; keep subjects out of both. Transitions come from the print (stamp, push through a shape, flip, plate-by-plate print, sliding label); no cross-dissolves, no fades to black, no page turns.

## 9. Pitfalls of the medium

- **It turns into a comic.** Panels, balloons and sound words make it a comic strip; keep labels as printed slips and give the story to the voice.
- **Dots in screen space.** A screen-fixed dot pattern looks like a filter and swims under camera moves; always compute dots in page space.
- **Moiré in wide shots.** Fade dots to flat tint below a few pixels per cell.
- **Dirty paper.** Too much age, roughness or blotchy ink reads as a bad scan; keep it clean and use age only to date a print.
- **Same-colour collisions.** Red on red, yellow on yellow: put a key line or a paper disc between.
- **Blank print moments.** Printing plate by plate from an empty sheet leaves frames of bare paper; start with the first plate already down, and print a label's words together with its paper.
- **A key line that does not match its fill.** When an image is made of tiles, the outline must follow the tile edges; a smooth curve over square cells looks drawn wrong, not misregistered.
- **Too many words.** One label at a time, short Chinese lines, otherwise the reading-time rule cannot be met.
- **Hot transients.** Stamps and claps push the true peak over the limit; limit the mix before the master.

