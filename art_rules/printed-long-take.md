# 刮版画长镜头 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/printed-long-take/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`ab296ec585615e3c0100ea22b879e88cd9790a493d0c995a24a25fe4ad25b97c`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

- **Only ink, paper and one red.** Every value is either ink or paper; grey exists only as a density of lines. One red is reserved for one small subject. A warm yellow may appear for the sun, a lamp or one material, never as a second accent.
- **Tone is cut, not shaded.** Shadow sides of hills carry knife lines that run down the fall line; skies are parallel horizontal cuts whose width makes the light; snow is paper with a few drift strokes; water is ink with cut ripples.
- **Real depth, flat marks.** The scene is built in 3D (terrain, rivers, thousands of trees, buildings), but every surface is drawn with flat marks fixed in world space, so the layers slide past each other like a printed diorama.
- **At least three layers in every held frame:** sky / a mountain or forest band / a middle ground of fields, water or snow / a foreground of branches, fences or posts. Ink and paper roughly half and half. A pass through steam or a structure is exempt for its half second; an opening inside one material (a cloud, the dark) finds its layers in that material (near wisps rushing past, the body, a gap to what lies beyond) within about a second.
- **One continuous move** carries the story; cuts are rare and designed.

Not woodcut (flat printed blocks, a mostly static camera, one block per image). Not ukiyo-e (flat colour fields, no depth travel). Not a toon-shaded 3D game (no smooth shading, no gradients, no specular). Not a pencil sketch (no hatching that follows form loosely; every line is a knife cut with a blunt entry and a tapered exit).

## 2. Materials & rendering

- **Render model:** three.js scene at 2× supersampling, box-filtered down in a final print pass. Every material is a small shader that decides "ink or paper" per pixel; there is no lighting except one direction used to choose lit and shadow faces.
- **Two kinds of field.** Every surface is either a paper field carrying ink cuts (lit faces, snow, sand, cloud, foam, steam) or an ink field carrying paper cuts (shadow faces, sky, water, forest, night). A cloud is paper with a few horizontal ink cuts on its underside, not a reversed sky as densely cut. Tone inside a field comes only from the width and density of the cuts.
- **Faceted terrain:** mountains and volcanoes are low-poly cones with flat facets. Lit facets are paper with a few fine ink cuts near the terminator; shadow facets are ink with paper cuts running down the slope. Cut spacing is fixed in world units so lines never swim when the camera moves.
- **Sky in direction space:** a sphere that travels with the camera; cuts are rows of constant elevation, so they stay horizontal and never slide with translation. Night = sparse wavy wind cuts and square stab stars; day = dense parallel cuts, thicker near the horizon. Words in the sky are plates hung in the same direction space.
- **Billboard atlases drawn on canvas:** trees (pines, frosted deciduous trees), animals, steam. Cylindrical billboards for anything standing, spherical with a screen rotation for anything flying. Sample the atlas with a negative mip bias and alpha-test so thin shapes survive at distance.
- **Water** is a ribbon cut into the snow (the ground is discarded inside a river mask), with bank walls and a paper snow lip. Ripples are short cuts across the flow, faded to solid ink where they would turn grey with distance.
- **Print pass (screen space):** paper fibre, ink mottling in the darks, soft grey blotches near the top of the sheet, a two-frame flicker, a light vignette. Nothing else lives in screen space except transitions made of paper (a whiteout, a sheet being peeled).
- **Props with words** (plates, boards, notices) are canvases on meshes: carved letters in paper on an ink ground, or ink on a pasted paper label. They sit at a 3/4 angle with thickness, a snow cap or a rim.

## 3. Colour logic

- Two values carry everything: ink (a warm black) and paper (a warm off-white). Never pure black or pure white, never a third grey fill.
- **One red, reserved for one subject**, kept small (a crown, a lamp, a flag) and never smaller than about 3 px at 1080p; enlarge it a little rather than lose it. It may carry into the subject's own trace (its ripple, its trail), never onto another object. A flat stab: no outline, highlight or gradient, a thin paper ring only where it sits on ink. When the take follows the red through steam or a whiteout, the red stays on top of the paper.
- A warm yellow is allowed for light itself (sun disc, its road on water, warm cuts in a dawn sky, a lamp) and one material at most. It never fills a large area except that one material.
- Value order by depth: far mountains paper with ink shadow facets; forest bands solid ink; the middle ground paper; foreground ink silhouettes. Keep the subject on the opposite value of what lies behind it.
- Example palette: ink `#16171b`, paper `#ede5cd`, red `#c4332b`, yellow `#dfa443`.

## 4. Type & subtitles

- One serif typeface, bold (e.g. Noto Serif SC, OFL), subset to the characters used. Chinese and English each on their own line.
- **Type lives in the world:** carved into a board, cast on a plate, printed on a pasted notice, or cut as a plate of type into the sky. Words in the world carry only keywords and numbers; no centred title cards, no headers.
- Sizes at 1080p: at most three sizes per frame; nothing smaller than 28 px for Chinese or 22 px for Latin; every word at least 5% inside the frame. Left-aligned blocks, aligned by optical edge.
- Words appear the way the medium makes them: cut left to right with chips at the knife, pressed by a seal, revealed under a peeled sheet.
- Reading time: hold every piece ≥ max(1.8 s, characters ÷ 4.5 for CJK + characters ÷ 15 for Latin + 1.5 s); judged comparisons hold still ≥ 2.5 s before the verdict lands.

### Narration & subtitles

When the film tells a story with a narrator:

- **Speech and picture move together.** Each line is spoken while the shot shows what it names; the long take keeps going under the voice, and the silent stretches (a hold to read, a pass through a structure, a flock taking off) are left without words.
- **Words in the world carry only keywords and numbers** (a count on a board, a date on a seal). The sentence is in the voice and the subtitle, not on the props.
- **One subtitle bar per spoken line**, at the bottom inside the 5% safe area: one Chinese line above one English line, never wrapped, in the film's serif, paper letters on an ink band about 80% opaque (thinner bands vanish over paper). It appears with the line and leaves with it; keep the subject of each shot above it.
- A second-language version swaps only the voice: the same picture, the same bilingual bar, each line starting at the same moment, finished before the next one starts.

## 6. Camera grammar

| Move | What it expresses | Can serve |
|---|---|---|
| High wide establishing frame, sinking and pushing | the whole place at once; the layers separate as it moves | a valley; a coastline; a city seen from its hills |
| Low glide over water or snow | speed, intimacy with the ground; foreground marks rush past | a river journey; a road; a migration |
| Hold on a prop with words, long lens | reading time inside the take | a sign; a plaque; a gauge; a date |
| Pass through a structure (bridge, gate, arch, tunnel) | a threshold, a change of time or light | night to day; outside to inside; then to now |
| Locked frame | a document, a comparison, a count | the same place in four years; before and after |
| Rise and pull back to the opening angle | the place again, changed | a return; a conclusion; an epilogue |
| Follow a flying or falling subject | the subject leads the camera to the next place | birds, a kite, a leaf, a paper plane |

Framing: the horizon sits on a third; the subject is never smaller than 1/20 of the frame height when it must be recognised; words stay inside the frame with a margin of 5% and never cross another object. Allowed transitions: through a structure, through steam or snow (under half a second of white paper), a match on a falling or rising subject, a sheet peeled from the corner, a seal. Forbidden: fades to black, cross-dissolves, slides, page flips, zoom cuts.

Fitting the high wide to the terrain (options, not a recipe). The sky is in frame only while the camera's pitch plus half its vertical field of view stays above the horizon, so a steep look down at a valley right below loses the sky. Ways round it: stand the camera farther back and higher on a longer lens, so the subject sits at a shallower angle below the horizon; take the printmaker's licence and stretch horizontal distances or compress heights, since each layer is a plane; break a far plane that fills the frame (a sea, a plain) into bands with headlands, islands, boats or tiers of cut density. When the sky is out of frame and words are needed, carve them into something in the world that faces the lens (rock, board, hull, a mark on the water), let the take tilt up into a hold where the sky returns, or keep the words for a later shot where the sky is in frame.

## 9. Pitfalls of the medium

- **Close-ups expose the flat shading.** 3D props pushed close to the lens look like toys. Keep living subjects to mid shot as flat silhouettes; give close props real materials (carved wood, concrete formwork, cast iron).
- **Empty paper.** A field of snow without layers goes blank. Keep three layers in frame; add drift strokes, reed ticks, thickets, belts.
- **Grey sludge.** Fine cuts at distance average to grey; fade them to solid ink or paper with distance and use negative mip bias for thin sprites.
- **Sliding lines.** Any cut spaced in screen space swims as the camera moves; anchor cuts to world space (or direction space for the sky).
- **The road look.** A dark river with a pale bank lip and regular dashes reads as asphalt. Break the rhythm of bank marks and keep the lip narrow.
- **Small subjects vanish.** Real-scale animals disappear in a wide frame; draw distant ones up to 3× larger (a printmaker's scale), keep the red at its minimum size.
- **Camera through solids.** Clear trees and posts from the camera path before placing scenery; check every low pass frame by frame. The same holds for every small scatter (reeds, stones, fence posts, grass): one within a metre or two of the lens fills the frame with ink. Sample the camera path and clear every instance inside a radius of it, give near sprites a dithered fade, then step stills through the low passes (`still.mjs --range a:b:0.1` and a contact sheet) and look for frames that are nearly all ink or all paper.
- **Empty paper close up.** A lit facet near the lens becomes a blank sheet. Make facets smaller near the camera path and give near lit faces their few ink cuts, grit or tufts.
- **Words on a moving take.** `readcheck` counts only the first stretch in which a piece is fully in frame, and knows nothing of occlusion or size. Report each piece in `TEXTS(t)` only inside its planned hold, when it is in frame, unobstructed and large enough to read; ease the camera into a hold or slow the clock for it.
- **Too many greys from post.** Vignette and blotches darken the paper and make the print look dirty; keep them light.

