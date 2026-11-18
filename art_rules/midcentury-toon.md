# 50s 扁平卡通 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/midcentury-toon/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`e73614b6f9e2f2e8ee279f4909da8429235b96f6d13a12345b6e57d5823c30b8`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

Flat, printed-looking colour with a thin, breathing ink line that never quite closes. **Every fill is a separate "cel" printed a few px off its line**, re-rolled on twos, so the picture shimmers like hand-registered paint while the camera glides. Light dry-brush tooth, paper grain, warm vignette.

People and things are geometric: egg or bean heads with the nose part of the face outline, simple garments in two or three flat colours, four-finger cartoon gloves. **A presenter's body is a held drawing: only arms, hands, eyes and mouth animate.** Rooms are not drawn: a scene is one colour plane, a floor band, a horizon line with gaps, and one or two props.

Not the 1930s rubber-hose cartoon (no black-and-white, no bouncing world, no hot jazz). Not a whiteboard explainer: it shows *how to do*, not *why*. The pictures are printed, not written on.

## 2. Materials & rendering

- **Off-register cels**: fill drawn with a small offset (a few px, down-right) from its line; the offset jitters ±1–2 px on twos. Keep it on everything, text included; switch it off only for a crisp diagram.
- **Line**: 3–5 px ink ribbons with ±40 % width breathing and 12–25 % breaks. Characters ~4 px, props 3–4.5 px, walls in plans thicker and broken. Hands: one outline around the union of palm and fingers, thin finger separations.
- **Shading**: one flat darker plane clipped inside a shape, never a gradient. Drop shadows are a copy of the shape offset down-right in a paper shade at ~50 %.
- **Ornaments**: 4-point atomic sparkles, 8–18-point starbursts, sunburst rays (~30 wedges, semi-transparent), boomerang and kidney shapes, polka dots.
- **Grain**: light; print, not film.

## 3. Colour logic

- **A warm paper ground, a warm near-black ink, soft atomic-age complements.** Nothing pure or neon.
- **One ground colour per scene**: a lighter tint for walls, a darker shade for floors. Never place the product on its own colour, never the presenter on their own accent.
- **The product keeps one colour through the whole film**; the accent (a presenter's garment, stars, bullets) is a different hue. Step grounds rotate through the rest.
- Examples: *coral / mustard / turquoise* on cream; *tomato / olive / powder blue* on oatmeal; *plum / lime / sand* on off-white.

## 4. Type & subtitles

- Roles: a 1950s script for a kicker (Oleo Script Bold); a slab serif (Alfa Slab One) for titles, numerals and headers, in ink over an offset colour plate; a geometric sans (Jost 500/600) for body, details, labels and captions.
- **Caption card**: a paper-coloured rounded slab with a thin ink border (its colour cel offset too), small turning stars at the ends, ~40 px sans, bottom-centre. Fades in quickly with a small rise. Hold ≥ max(1.8 s, speech + 0.6 s, chars/12 + 1 s).
- **Step header**: an ink disc with a paper numeral, a small letter-spaced "STEP n OF N", and the step title with a cream plate; it slides in on twos.
- **Detail tags**: a paper card with a star bullet, popping on the action beat next to the call-out. Data lands on the picture, never as a slide.

## 6. Camera grammar

The camera is "the stand": never handheld. A vocabulary, not a route. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Slow push (a few %) | Collecting the eye | a product on its stage; a result settling |
| Iris through a medallion | The number *is* the door | a change of step; a change of rule |
| Round call-out with a leader line | Context and detail at once | a hand action; a screen; a small part |
| Tilt with a pointing finger | The finger leads the frame | the one action that matters most |
| Push into a device, pan along signal rings | Person → interface → device | pairing; connecting |
| Iris from a round object into a top view | Circle to circle, function to plan | a button starting a job; a lid opening; a dial |
| Pull-back with counter-rotation from a detail to a plan | One lane becomes a pattern | a route, a schedule, a garden, a floor plan |
| Colour-block wipe (side, bottom-up) | Turning the manual's page | a tip; a summary; a new card |
| Split frame in two colour blocks | Right vs wrong, before vs after | a safety rule; an upgrade |
| Dead still ≥ 3 s | "This is the frame to screenshot" | a summary; a CTA; a QR code |
| Iris-out onto one object | The last circle | a closing on the product, the logo, the result |

Key subjects ≥ 1/3 frame height and clear of the caption band. Transitions are circles, colour-block wipes and cuts on a beat; no dissolves.

## 9. Pitfalls of the medium

- A route that ignores obstacles → follow the product's real rules; flow streamlines bend around obstacles and never cross. Lay it one region per beat, not all at once.
- A separate nose wedge looks glued on → one open spline from the bridge round the skull, closed at the nose tip.
- Thin arms read as sticks from the neck → shoulders at the torso corners, sleeves as a thick ink ribbon with a colour ribbon on top.
- Fat-blob fingers turn the hand into a cloud → stroke every part first, fill second (one union outline), slender fingers with separation lines.
- Zooming the world triples the ink → close-ups in call-out circles drawn at native scale.
- Detail text without reading time → move the data into the detail, the context into the title and the voice; chars/12 + 1 s.
- A transition drawing the next scene before its start → clamp local time to just past the start.

