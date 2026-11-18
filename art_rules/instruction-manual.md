# 说明书插画 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/instruction-manual/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`57f9e69373bb36bafe5572bf960f9557c484210e0edaf89cfc286cc9be21282e`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

Rules (they define the style):

- **One angle: true isometric, orthographic.** Azimuth 45° (every object is seen across one vertical edge), elevation 35.264° (arctan 1/√2): the three axes meet at 120° on screen, horizontal edges run at 30°, vertical edges stay vertical, nothing gets smaller with distance. The whole film keeps this one angle.
- **The frame is the paper.** The page is seen square-on; there is no desk, no folded card in 3D, no perspective on the sheet. Every shot is a part of one printed page.
- **Line art with flat fills.** One ink line weight, flat colour, at most three values per object (top lightest), no gradients, no cast shadows.
- **Yellow means "new in this step".** The part added in a step is safety yellow and turns white once it is fitted. Nothing else is yellow (the subtitle marker excepted). The audience learns this in the first steps, so a late yellow can carry the ending.
- **The manual's signs do the explaining**: step numbers, parts boxes with counts, dotted guide lines, arrows lying in the isometric planes, rotation arrows, magnifier circles, a do/don't box, a "click" mark. On-screen words are only numbers and counts.
- **Faceless people at real proportions** whose hands always do something.

Not Isometric Infographic (no coloured diorama, no data panels), not Isometric People Scene (no painted scene, no faces), not Blueprint (dark ground, technical dimensions), not Exploded Teardown (no rendered product, no photoreal materials), not a slide deck (no header bars, centred titles or page turns).

## 2. Materials & rendering

- **Projection**: world units in centimetres, y up; `makeView({cx, cy, s, az: 45, el: 35.264})` maps world → screen. A sphere always projects to a circle, so limbs, hands and cylinders are hulls of circles and stay right at any heading.
- **Painter's order by view depth.** Long parts (rails, posts) are sorted by their nearest point; an assembly that interlocks is drawn in groups from back to front (far end and back rail → the board and what lies on it → front rail, near end, bolt heads), so large flat parts never cut through bars.
- **Fill, then outline, per part**: overlapping parts are separated by a line, a part has no lines inside itself.
- **Paper**: off-white stock with faint fibres that travel with the page on a pan and keep their size on a zoom (printed stock, not a photo of it).
- **Line weight is set in screen pixels** (2.6 px at 1080p) and follows the zoom only partly (about z^0.55, clamped), so the whole page stays crisp when pulled back and lines don't go clumsy close up.
- **Appearing** (reference): a drawing first shows its complete line art with paper-coloured fills, then its colours come in over it. A part is never drawn half-built or floating.
- **Motion blur** (reference): pans smear one frame along the camera path; fast zooms average sub-frames across half a shutter.
- **Hands in close-up** (reference): when only hands are in frame (a magnifier, a "press here" shot), draw them finer than the full-body figures: a palm, a thumb and four separate fingers at real size (≈ 18.5 cm wrist to fingertip), white like the skin elsewhere, and the line where one finger overlaps the next is all that says "fingers" (one or two lines, no nails, creases or shading). The sleeve is the wearer's shirt colour (her light grey `#CFCBC2` reads best against white hands and parts; a white sleeve keeps its cuff line) and runs on until the frame or the magnifier's rim cuts it: an arm never ends inside the frame. Bring the arm in from the nearest edge, so the forearm crosses at most about a third of the frame, and place the hand by what it touches (the fingertip on the button, the palm on the jar). `demo/hand.js` does this; its check sheet is `?f=hands`.

## 3. Colour logic

| Role | Example (our demo) | Rule |
|---|---|---|
| Paper | `#F4F1EA` | ground |
| Ink | `#1E1D1B` | every line, arrow, number |
| Fitted part (top / left / right) | `#FFFFFF` / `#ECE8DF` / `#DCD7CC` | three flat shades |
| New part (top / left / right) | `#F7D35A` / `#F2C230` / `#DEAA1F` | only the part added in this step |
| Greys | `#CFCBC2` / `#9C988F` / `#6B6862` | clothes, trousers, shoes, hair |
| Metal | `#D9D7D1` / `#BDBAB3` / `#A3A099` | bolts, tools |
| Signal red / blue | `#D23A2E` / `#2C66AC` | only the ✗ and the ✓ |

The exact hexes are reference; the logic (paper, ink, white parts in three values, one reserved yellow, red/blue only for verdicts) is the style.

In a procedure that removes or changes things rather than adding them (opening, cleaning, a safety step), yellow marks the one thing the reader acts with or on in that step (the tool, the button, the part that comes off), and returns to white once the step is done.

## 4. Type & subtitles

- On the page only step numbers (a geometric sans, e.g. Inter 700, about 150 px at 1:1, top left of each step's area, printed on the paper and moving with it) and counts in parts boxes ("4×", Inter 600). Everything else is said by drawings and the voice.
- **Subtitles** bottom left, left-aligned: Chinese (e.g. Noto Sans SC 500, 38 px) over English (Inter 500, 32 px, ink at about 78 %), one line each, an 8 px yellow bar on the left marking the line being spoken. No box, outline or shadow; a soft paper-coloured bed (same colour as the page) keeps them readable over line art. Keep subjects out of that corner.
- A title, if any, is printed on the page like a manual's cover or footer, never a title card over the picture.

## 6. Camera grammar

The camera is a 2D camera over one long sheet: pan, whip, tilt, push, pull, and cuts. It never rotates the view.

| Move | What it expresses | Can serve |
|---|---|---|
| Push into a parts box / object | "this one" | an opening; a detail |
| Pan or whip along the page to the next step | progress | the next step; skipping dull steps |
| Tilt to the next row, the step number entering first | a new stage | a change of section |
| Locked frame on a do/don't box | judging | a rule; a common mistake |
| Push through a shape (the ✓ cell, a magnifier circle) | going into the detail | the right way, shown big; a close-up |
| Shape-matched cut (a bolt head → a round knob) | jumping to the consequence | a mistake revealed; a time jump |
| Pull back to the whole page | the full sequence, the result | an ending; a summary |

Leave a step held still long enough to read its count and its arrow; the subject is at least a third of the view when it is the point.

## 9. Pitfalls of the medium

- **The assembly must be one model with a state table.** Every picture of the object (every step, the parts list, the final page) is drawn from the same function with a state; write the table first (step → what is added → what the object has when the step ends → parts used) and add one thing per step. Counts on the parts list must add up across the steps (e.g. bolts 2 + 2 + 4 = 8). Separate drawings per step drift: parts appear early, vanish, or sit in the wrong place.
- **Footprints and guide lines come from the same geometry.** A dotted footprint must be the finished object's real corners; a guide line runs from where the part lies to where it lands. Parts in a box lie flat, stacked at real sizes, and the box is empty only after the last one leaves.
- **Knees bend with the body, not the world.** Set the knee hint from the body's heading, or a pose that is right facing one way breaks when the figure turns.
- **Kneeling hip height comes from leg length**: knee on the floor + one thigh length. A half-kneel: the kneeling knee under the hip, thigh vertical, shin and instep flat behind; the other foot flat, knee about 90°, shin vertical.
- **The far leg is one shade darker** than the near leg, so crossed or overlapping legs never merge into one shape.
- **Sitting on the floor**: cross-legged with the knees open and low and the shins crossed in front reads as sitting; a pelvis on the floor with legs straight forward reads as falling over.
- **Standing**: weight on one leg, the other relaxed and turned out, hips and shoulders tilted against each other. Feet together and arms hanging make figurines.
- **Placement**: never put a person between the viewer and what the step is about, and keep their feet outside the object's footprint. Behind slatted furniture their legs show between the bars and they read as standing inside it: put them at a front corner, or at one end with their back to the viewer.
- **A gesture that matters** (a hand on a shoulder) lands on the side nearest the viewer, with nothing in front of it.
- **Front-on (facing the viewer squarely) reads worst** at this angle; use three-quarter and profile headings.
- **Hair and buns** live in the head's own 3D frame, so they turn, tilt and hide with the head.
- **Small mistakes are hard to see at full-page scale**: a part on upside down needs the ✗ on it and a close-up, not only the voice.
- **No perspective, no turning the view**, no 3D camera orbiting the paper.
- **No brands, logos, product codes, faces or cartoon round-headed figures.**

